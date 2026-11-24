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
- Open misconception (M4): believes the model itself executes tool calls, rather than the program running each tool while the model only ever outputs one request or final answer per call (quiz 0001 s1, q2 and q4; see learning record 0003).
- Open misconception (M3): believes the model remembers things across sessions by itself, rather than the program saving and re-feeding state (quiz 0001 s1, q6; see learning record 0003).

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  `s1` is graded (`grades/0001-s1.json`): correct on q1, q3; wrong on q2, q4 (both M4); partial on q5, q6 (q6 also M3).
  `s2` is not yet graded.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits.
  The M4/M3 misconceptions above should be addressed at the start of that lesson, before introducing what the program chooses to carry forward between calls.
