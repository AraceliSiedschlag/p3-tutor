# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).
- On quiz 0001 (s2): correctly identifies what makes a system an agent, what the model outputs when it requests a tool, and what the program does with a tool's result and why (feeds it back as the model's next input so the model can decide what's next).
- Still believes a stuck agent loop will resolve itself given enough steps, rather than needing a built-in stopping condition (M6, learning record 0003).
- Still sometimes describes the model as "running" a tool itself, rather than only requesting it for the program to run (M4), even when the surrounding answer is otherwise correct.
- On tool selection, names only a tool's name rather than its full description (purpose and parameters); knows the model goes off the description, not the code, but not yet that a name alone can mislead.

## What Riley does not know yet
- Has never called a language model from code or written a tool definition.
- Has heard the words "token" and "context window" but cannot say what they limit or why they affect cost.
- Has not met memory, retrieval, workflows versus agents, or multi-agent systems.
- Has no machine-learning background beyond one statistics course.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  `submissions/s2.json` is graded (`grades/0001-s2.json`); `submissions/s1.json` is still ungraded.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits.
