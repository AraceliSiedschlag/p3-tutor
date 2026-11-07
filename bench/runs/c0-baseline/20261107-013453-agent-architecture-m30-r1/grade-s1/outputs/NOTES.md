# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).

## What Riley does not know yet
- Has never called a language model from code or written a tool definition.
- Has heard the words "token" and "context window" but cannot say what they limit or why they affect cost.
- Has not met memory, retrieval, workflows versus agents, or multi-agent systems.
- Has no machine-learning background beyond one statistics course.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  `s1` is graded (`grades/0001-s1.json`): 2 correct (q1, q3), 2 partial (q5 missing the "why", q6 missing the memory half), 2 wrong (q2, q4), both wrong answers showing M4 (learning record 0003). `s2` is not graded yet.
- Open misconceptions to watch for: M4, that the model runs tools itself rather than the program (learning record 0003); M3, that the model remembers things across sessions on its own (learning record 0004) — Riley is inconsistent on M3, ruling it out in q1 but stating it unprompted in q6.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits. Start that lesson by ruling out M3 explicitly (see learning record 0004).
