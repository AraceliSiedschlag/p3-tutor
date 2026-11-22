"""The keys guard: a PreToolUse hook that keeps keys/ away from the main conversation.

Claude Code runs this script before every Read, Grep, Glob, Bash and PowerShell call,
with the call as JSON on stdin. Inside a subagent the input carries `agent_type`, the
subagent's name; in the main conversation it does not. A call that would read, search
or list keys/ is blocked (exit 2, with a message on stderr the model sees) unless it
comes from a subagent named in ALLOWED_AGENTS. Everything else goes ahead (exit 0).
The script decides on purpose in every case: input it cannot read is blocked too.
"""

import json
import os
import re
import sys

ALLOWED_AGENTS = {"grader"}

KEYS_DIR = "keys"

BLOCK_MESSAGE = (
    "keys guard: the answer keys in keys/ are for the grader subagent only, "
    "so this conversation may not read, search or list them. "
    "To grade a submission, start the grader subagent and use its report; "
    "to work on a quiz, use quizzes/ and drafts/. "
    "A search over the whole workspace also reaches keys/: name the folder to search instead, such as lessons/."
)

# "keys" as a whole path component: not part of a longer name such as "monkeys" or "keys.md".
_KEYS_COMPONENT = re.compile(r"(?i)(?:^|[\s\"'`=(:;|&<>/*{,])keys(?:$|[\s\"'`/*;|&)<>},])")


def block(reason=BLOCK_MESSAGE):
    sys.stderr.write(reason + "\n")
    sys.exit(2)


def allow():
    sys.exit(0)


def _norm(text):
    """Forward slashes, so keys\\0001.json and keys/0001.json read the same."""
    return str(text).replace("\\", "/")


def names_keys(text):
    """True when the text names keys/ as a path component anywhere in it."""
    return bool(text) and bool(_KEYS_COMPONENT.search(_norm(text)))


def _resolve(path, cwd):
    path = os.path.expanduser(_norm(path))
    if not os.path.isabs(path):
        path = os.path.join(cwd, path)
    return os.path.normcase(os.path.realpath(os.path.normpath(path)))


def covers_keys(path, cwd, root):
    """True when a search rooted at `path` would reach root/keys (it is keys/ or a folder above it)."""
    keys_dir = _resolve(os.path.join(root, KEYS_DIR), cwd)
    target = _resolve(path if path else cwd, cwd)
    return keys_dir == target or keys_dir.startswith(target.rstrip(os.sep) + os.sep)


def decide(data):
    if not isinstance(data, dict):
        block("keys guard: the hook input was not a JSON object, so the call is blocked.")

    if data.get("agent_type") in ALLOWED_AGENTS:
        allow()

    tool = data.get("tool_name") or ""
    args = data.get("tool_input") or {}
    if not isinstance(args, dict):
        args = {}
    cwd = data.get("cwd") or os.getcwd()
    root = os.environ.get("CLAUDE_PROJECT_DIR") or cwd

    if tool == "Read":
        if names_keys(args.get("file_path")):
            block()
    elif tool == "Glob":
        if names_keys(args.get("pattern")) or names_keys(args.get("path")):
            block()
    elif tool == "Grep":
        if names_keys(args.get("path")) or names_keys(args.get("glob")):
            block()
        if covers_keys(args.get("path"), cwd, root):
            block()
    elif tool in ("Bash", "PowerShell"):
        if names_keys(args.get("command")):
            block()
    allow()


def main():
    try:
        data = json.loads(sys.stdin.read())
    except Exception:
        block("keys guard: the hook input could not be read as JSON, so the call is blocked.")
    try:
        decide(data)
    except SystemExit:
        raise
    except Exception as exc:
        block("keys guard: the guard could not check this call ({}), so it is blocked.".format(exc))


if __name__ == "__main__":
    main()
