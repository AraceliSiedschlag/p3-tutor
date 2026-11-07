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
  Worth flagging for that grading pass: `submissions/s1.json` q6 shows Riley believed the model "remembers on its own" which tool it picked for similar questions across earlier sessions. That is the automatic-cross-session-memory misconception (M3), and lesson 1 (`lessons/0001-context-and-memory.html`, objective O3) now addresses it directly, so grading can reference the lesson rather than re-teach it from scratch.
- Taught objective O3 (context window, what's kept within a session vs. between sessions, retrieval, notes as memory) as a 30-minute lesson, `lessons/0001-context-and-memory.html`. Quiz 0002 and its key are ready on the same objective.
  Primary source: Anthropic's "Effective context engineering for AI agents"; also used IBM's RAG explainer for retrieval basics. See `RESOURCES.md`.
  Introduced two new misconceptions in the key: M7 (treating tokens kept in context as free, with no cost or recall downside to keeping more) and M9 (overcorrecting to "nothing from a past session can ever be retrieved," once told sessions don't share context automatically).
- Next in the mission, once O3 is checked with quiz 0002: workflows versus agents (when a fixed workflow beats a loop), and when splitting work across multiple agents pays off — both still unmet per the mission's success criteria.
