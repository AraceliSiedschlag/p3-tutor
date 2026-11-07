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
  Neither attempt has been graded yet. Worth flagging when grading: s1's answer to q6 says the model "also remembers on its own which tool it picked for questions like that in earlier sessions" — an early sign of M3 (automatic cross-session memory), the exact misconception lesson 0001-context-window-and-memory.html (objective O3) was written to address.
- Taught objective O3 (context window; what's kept between steps vs. sessions; retrieval and notes as memory) as `lessons/0001-context-window-and-memory.html`, a 30-minute lesson, with quiz `0002`/key `0002`. Primary source: Anthropic's "Effective context engineering for AI agents." Tokens and context window, previously just heard-of terms, were defined here for the first time.
- Next in the mission, once O3 is checked: workflows versus agents (when the makerspace assistant's pieces should be a fixed pipeline rather than agentic), and later, splitting work across multiple agents.
