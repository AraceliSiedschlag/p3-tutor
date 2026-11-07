# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).

## What Riley does not know yet
- Has never called a language model from code or written a tool definition.
- Taught, not yet evidenced: tokens, the context window and why it limits cost and accuracy (context rot), memory (saving state outside the model between sessions), and retrieval (searching a large store instead of pasting it all into context) &mdash; covered in lesson `0001-context-and-memory.html` on 2026-11-07. Quiz 0002 checks these; nothing above moves to "knows" until it's graded.
- Has not met workflows versus agents, or multi-agent systems.
- Has no machine-learning background beyond one statistics course.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  Neither attempt has been graded yet.
- Lesson `0001-context-and-memory.html` (objective O3, 30 minutes) taught on 2026-11-07, with quiz 0002 ready and not yet taken. It reused misconception M3 (automatic memory across sessions) from quiz 0001's key, and introduced M2 (bigger/fuller context window is always fine) as a new id.
- Next in the mission, once O3 is evidenced: workflows versus agents, and when splitting work across multiple agents pays off.
