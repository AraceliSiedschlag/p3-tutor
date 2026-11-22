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
- Still collapses "the model requests a tool" into "the model runs the tool," and miscounts separate model calls as one (learning record 0003).
- Believes the model remembers past sessions on its own, rather than that memory has to be stored and fed back in by the surrounding program (learning record 0004) - directly relevant to the next topic.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  `submissions/s1.json` is now graded (`grades/0001-s1.json`): correct on the loop itself (q1) and the step-limit safeguard (q3), partial on how a tool result flows back to the model (q5) and on tool selection (q6, with M3), wrong on the model-vs-program split (q2, q4, both M4).
  `submissions/s2.json` is still ungraded.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits.
