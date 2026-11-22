"""The keys guard (tutor/.claude/hooks/keys_guard.py).

Each test runs the guard the way Claude Code does: as a subprocess with the PreToolUse
hook input as JSON on stdin, inside a temporary workspace that has a keys/ folder.
Exit 2 blocks the call and exit 0 allows it.
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

GUARD = Path(__file__).resolve().parent.parent / "tutor" / ".claude" / "hooks" / "keys_guard.py"

BLOCKED = 2
ALLOWED = 0


class KeysGuardTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = self._tmp.name
        for folder in ("keys", "quizzes", "lessons"):
            os.makedirs(os.path.join(self.root, folder))
        self.addCleanup(self._tmp.cleanup)

    def run_guard(self, tool, tool_input, agent_type=None):
        """Run the guard on one tool call and return (exit code, stderr)."""
        payload = {
            "hook_event_name": "PreToolUse",
            "cwd": self.root,
            "tool_name": tool,
            "tool_input": tool_input,
        }
        if agent_type is not None:
            payload["agent_type"] = agent_type
            payload["agent_id"] = "test-agent"
        env = dict(os.environ, CLAUDE_PROJECT_DIR=self.root)
        proc = subprocess.run(
            [sys.executable, str(GUARD)],
            input=json.dumps(payload), capture_output=True, text=True,
            env=env, cwd=self.root,
        )
        return proc.returncode, proc.stderr

    def assertBlocked(self, tool, tool_input, agent_type=None):
        code, err = self.run_guard(tool, tool_input, agent_type)
        self.assertEqual(code, BLOCKED, f"{tool} {tool_input} should be blocked")
        self.assertIn("keys guard", err)

    def assertAllowed(self, tool, tool_input, agent_type=None):
        code, err = self.run_guard(tool, tool_input, agent_type)
        self.assertEqual(code, ALLOWED, f"{tool} {tool_input} should be allowed, stderr: {err}")

    # The main conversation's reads of keys/ are blocked, with every tool.

    def test_main_read_of_a_key_is_blocked(self):
        self.assertBlocked("Read", {"file_path": "keys/0001.json"})

    def test_main_read_of_a_key_by_absolute_path_is_blocked(self):
        self.assertBlocked("Read", {"file_path": os.path.join(self.root, "keys", "0001.json")})

    def test_main_grep_in_keys_is_blocked(self):
        self.assertBlocked("Grep", {"pattern": "answer", "path": "keys"})

    def test_main_grep_over_the_whole_workspace_is_blocked(self):
        self.assertBlocked("Grep", {"pattern": "answer"})

    def test_main_glob_in_keys_is_blocked(self):
        self.assertBlocked("Glob", {"pattern": "keys/*.json"})

    def test_main_bash_cat_of_a_key_is_blocked(self):
        self.assertBlocked("Bash", {"command": "cat keys/0001.json"})

    def test_main_powershell_get_content_of_a_key_is_blocked(self):
        self.assertBlocked("PowerShell", {"command": "Get-Content keys/0001.json"})

    # The grader may read keys/.

    def test_grader_read_of_a_key_is_allowed(self):
        self.assertAllowed("Read", {"file_path": "keys/0001.json"}, agent_type="grader")

    def test_grader_grep_in_keys_is_allowed(self):
        self.assertAllowed("Grep", {"pattern": "answer", "path": "keys"}, agent_type="grader")

    def test_another_subagent_read_of_a_key_is_blocked(self):
        self.assertBlocked("Read", {"file_path": "keys/0001.json"}, agent_type="quiz-reviewer")

    # The main conversation's other reads still work.

    def test_main_read_of_a_quiz_is_allowed(self):
        self.assertAllowed("Read", {"file_path": "quizzes/0001.json"})

    def test_main_read_of_mission_is_allowed(self):
        self.assertAllowed("Read", {"file_path": "MISSION.md"})

    def test_main_bash_ls_lessons_is_allowed(self):
        self.assertAllowed("Bash", {"command": "ls lessons"})

    def test_main_grep_in_lessons_is_allowed(self):
        self.assertAllowed("Grep", {"pattern": "planner", "path": "lessons"})

    def test_main_glob_of_quizzes_is_allowed(self):
        self.assertAllowed("Glob", {"pattern": "quizzes/*.json"})

    def test_a_name_that_only_contains_keys_is_allowed(self):
        self.assertAllowed("Read", {"file_path": "lessons/monkeys.md"})

    # Input the guard cannot read is blocked.

    def test_unreadable_input_is_blocked(self):
        proc = subprocess.run(
            [sys.executable, str(GUARD)], input="not json", capture_output=True, text=True,
        )
        self.assertEqual(proc.returncode, BLOCKED)


if __name__ == "__main__":
    unittest.main()
