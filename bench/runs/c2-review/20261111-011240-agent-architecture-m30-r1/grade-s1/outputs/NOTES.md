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
- Believes the model runs tools itself inside one call, rather than only emitting a request that the program executes (M4; learning record 0003). Shown twice on quiz 0001 (q2, q4), not yet corrected.
- Can correctly explain that the model picks a tool from the descriptions it's given (quiz 0001 q6), but still assumes the assistant automatically remembers things like which tool it picked in past sessions (M3), without that being fed back explicitly.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  `submissions/s1.json` has been graded (`grades/0001-s1.json`): correct on q1 (agent loop), q3 (stopping condition); wrong on q2, q4 (both M4); partial on q5 (missing the "why" of returning a tool result) and q6 (right mechanism, plus a false claim about cross-session memory, M3).
  `submissions/s2.json` has not been graded yet.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits. The upcoming lesson should lead with the model/program split (M4) before introducing memory, since real memory being something the program builds will otherwise reinforce the same "model does it automatically" instinct (M3).
