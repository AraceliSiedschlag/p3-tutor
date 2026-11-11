# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).

## What Riley does not know yet
- Has never called a language model from code or written a tool definition.
- Has not met workflows versus agents, or multi-agent systems.
- Has no machine-learning background beyond one statistics course.
- Lesson 1 (below) just taught tokens, the context window, retrieval and notes-as-memory; not yet confirmed as learned, since quiz 0002 hasn't been taken.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  Neither attempt has been graded yet.
  Worth flagging when grading: s1's answer to q6 says the assistant "remembers on its own which tool it picked for questions like that in earlier sessions" &mdash; the same cross-session-memory misconception (M3) that lesson 1 addresses directly.
- Lesson 1, `lessons/0001-context-and-memory.html` (objective O3, 30 min), taught: the context window and statelessness, context accumulating within a run (and its cost), the non-persistence of sessions, and retrieval vs. structured note-taking as the two deliberate memory strategies. Quiz 0002 is ready on it, not yet taken.
- Two misconception ids introduced in this workspace for O3: M2 (more context in a prompt is always better / free of cost) and M5 (retrieval and saved notes are interchangeable). M3 and M4 (both from quiz 0001) were reused, not redefined.
- Next after O3 lands: workflows vs. agents (when a fixed pipeline beats a loop), per MISSION.md's "argue which parts should be a fixed workflow rather than an agent."
