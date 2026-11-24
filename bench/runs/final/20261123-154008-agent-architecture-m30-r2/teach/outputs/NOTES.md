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
- Taught in lesson 0001 (below) but not yet evidenced by a quiz or in conversation: token, context window, context rot, cross-session memory, notes as memory, retrieval. Treat as covered, not yet confirmed.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  Neither attempt has been graded yet.
- Lesson `lessons/0001-context-and-memory.html` (objective O3, 30 min) taught: the context window's contents and fixed size, context rot, within-session persistence by default, cross-session loss unless saved, notes as memory, and retrieval. Quiz `0002.json` / key `0002.json` check it; not yet taken.
- Next in the mission after O3 is confirmed: workflows versus agents, and when splitting work across multiple agents pays off.

## Misconception ids (O3, introduced in quiz 0002's key)
- **M1** — conflating the context window's hard token limit (an over-budget request fails outright) with context rot (accuracy degrading gradually, before the window is even full).
- **M2** — believing a bigger or more-loaded context window always gives a better answer; ignores context rot.
- **M3** — believing something is already in context because it could be relevant (e.g. assuming the whole manual or a tool's full history is already loaded), rather than only what was actually sent this turn.
- **M4** — believing only the most recent tool result matters mid-session, i.e. that earlier tool results expire or need to be re-fetched.
- Also seen in the lesson's practice (not yet given an id, since not tested in quiz 0002): "the assistant remembers across sessions like a person would" and "retrieval means handing over the whole document."
