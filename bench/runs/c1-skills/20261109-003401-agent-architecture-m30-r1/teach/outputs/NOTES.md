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

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  Neither attempt has been graded yet.
- Taught objective O3 (context and memory) as a 30-minute lesson, `lessons/0001-context-and-memory.html`: the context window as a shared, finite token budget; context rot when it fills up within a session; sessions starting empty by default; notes and retrieval as the two patterns that bridge both gaps. Tied throughout to the makerspace assistant's manual search and per-student training records.
  New misconceptions introduced: **M7** (bigger context window is automatically more reliable), **M8** (being able to search a source means having effectively read all of it), **M9** (standing or input tokens — instructions, tool descriptions, already-known context — don't really count toward cost). Quiz 0002 / key 0002 test O3 and these three misconceptions, plus a callback to **M3**.
  Cheat sheet written at `cheatsheets/context-and-memory.html`.
- Still pending: grading quiz 0001 (s1 and s2) and quiz 0002, once Riley takes it.
