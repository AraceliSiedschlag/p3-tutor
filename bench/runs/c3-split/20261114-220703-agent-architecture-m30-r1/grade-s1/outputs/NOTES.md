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
- Believes the model can run a tool or act on the world itself, rather than only emit a request the program carries out (M4): missed quiz 0001 q2 and q4 on this.
- Believes the model automatically remembers things across sessions (M3): added this, unprompted, to an otherwise-correct answer on quiz 0001 q6.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  `s1` is now graded (`grades/0001-s1.json`): correct on q1 and q3 (the loop, stopping conditions), wrong on q2 and q4 (M4), partial on q5 (right idea, missing the why) and q6 (right on tool descriptions, but M3 crept into the answer).
  `s2` is still ungraded.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits.
  M4 and M3 should be named directly at the start of that session before new material is introduced.
