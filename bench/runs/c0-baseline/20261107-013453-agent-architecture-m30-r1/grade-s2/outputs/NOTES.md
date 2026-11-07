# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).
- The model only requests a tool call; the program is what runs the tool and each step is a separate model call (learning record 0003, from quiz 0001 submission s2).

## What Riley does not know yet
- Has never called a language model from code or written a tool definition.
- Has heard the words "token" and "context window" but cannot say what they limit or why they affect cost.
- Has not met memory, retrieval, workflows versus agents, or multi-agent systems.
- Has no machine-learning background beyond one statistics course.
- Still holds the misconception that a stuck agent loop will fix itself if left to run longer, rather than needing a stopping condition such as a step limit (M6; quiz 0001, submission s2, q3).
- When explaining how the model picks a tool, names only the tool's name rather than its full description (name, purpose, parameters); graded partial, not a named misconception (quiz 0001, submission s2, q6).

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  `submissions/s2.json` is graded (`grades/0001-s2.json`); `submissions/s1.json` still awaits grading.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits.
  Stopping conditions (M6, above) are worth a short revisit before or alongside that, since the design review will need an answer on loop safety too.
