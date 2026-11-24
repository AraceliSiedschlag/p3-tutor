# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).

## What Riley does not know yet
- Has never called a language model from code or written a tool definition.
- Has not met workflows versus agents, or multi-agent systems.
- Has no machine-learning background beyond one statistics course.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  Neither attempt has been graded yet.
- Taught O3 (context, memory, retrieval and notes) as `lessons/0001-context-and-memory.html`, a 30-minute lesson. Quiz `quizzes/0002.json` and key `keys/0002.json` are ready but not yet taken.
  A cheat sheet, `cheatsheets/context-and-memory.html`, covers the terms, the retrieval-vs-notes table, and the four misconceptions for later lookup.
- The lesson introduces four misconceptions (model "remembers" mid-conversation; a new session continues automatically; retrieval and notes are the same feature; a bigger context window means memory design can be skipped). None has a workspace-wide `Mn` id yet: the grading subagent correctly refused to expose `keys/0001.json`'s ids when asked outside a real grading task, so quiz 0002's key states each wrong idea in its rationale text instead of a `distractors` mapping. Assign formal ids next time both quizzes' misconceptions need cross-referencing.
- Next candidate in the mission, per `MISSION.md`'s success list: tool descriptions and how the model uses them (not yet taught), or the workflow-versus-agent judgment call.
