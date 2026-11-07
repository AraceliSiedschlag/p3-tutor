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
  `s1` is graded (`grades/0001-s1.json`): correct on the loop itself and on stopping conditions (q1, q3); partial on stating the result-goes-back step without its purpose (q5); still holds the misconception that the model runs tools itself rather than just requesting them, on both q2 and q4, and let it leak into q6 as a claim that the model remembers its own past tool choices across sessions (see learning record 0003).
  `s2` is not graded yet.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits.
  Hold off until the model/program boundary from learning record 0003 is solid, since memory is the program choosing what to carry into the model's input, and that will be confusing while Riley still pictures the model acting or remembering on its own.
