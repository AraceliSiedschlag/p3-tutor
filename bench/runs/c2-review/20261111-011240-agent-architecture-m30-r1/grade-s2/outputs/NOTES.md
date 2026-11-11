# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).
- The model only ever outputs a request for a tool; the program is what actually runs the tool and feeds the result back in, so each tool call is a separate model call (learning record 0003). The idea is solid, but the wording still sometimes describes the model as "running" the tool - worth a quick check that this is just loose phrasing.

## What Riley does not know yet
- Has never called a language model from code or written a tool definition.
- Has heard the words "token" and "context window" but cannot say what they limit or why they affect cost.
- Has not met memory, retrieval, workflows versus agents, or multi-agent systems.
- Has no machine-learning background beyond one statistics course.
- Misconception to clear up: believes an agent loop stuck repeating the same failing step will eventually fix itself given enough iterations, rather than needing an explicit stopping condition (learning record 0004, M6).
- Only partial on how a model picks which tool to call: leans on the tool's name alone rather than its full description (quiz 0001, submission s2, q6) - not yet a named misconception, just incomplete.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  `submissions/s2.json` is graded (`grades/0001-s2.json`); `submissions/s1.json` is still ungraded.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits.
