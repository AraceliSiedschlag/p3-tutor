# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).
- Knows a step limit, not a bigger model or a sterner prompt, is the right safeguard against a looping agent (quiz 0001 s1, q3).
- Knows the model picks a tool from the name-and-description list it is given (quiz 0001 s1, q6, partial).

## What Riley does not know yet
- Has never called a language model from code or written a tool definition.
- Has heard the words "token" and "context window" but cannot say what they limit or why they affect cost.
- Has not met memory, retrieval, workflows versus agents, or multi-agent systems.
- Has no machine-learning background beyond one statistics course.
- Still believes the model runs a tool itself rather than just requesting it and getting the result handed back by the program - misconception M4, confirmed in quiz 0001 s1 (q2 and q4; see learning record 0003).
- Also showed the model remembers, on its own, which tool it used in earlier sessions - misconception M3, shown in quiz 0001 s1 (q6).
- Can say a tool result goes back to the model (q5) but not yet why, i.e. so the model can decide its next step or final answer.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  `s1` is graded (`grades/0001-s1.json`); `s2` is not graded yet.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits.
  Before that, the model/program split (M4) should be revisited directly, since it is still open.
