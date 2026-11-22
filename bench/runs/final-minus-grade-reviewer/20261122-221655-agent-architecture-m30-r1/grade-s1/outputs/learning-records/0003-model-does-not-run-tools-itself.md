# Riley still collapses "model requests a tool" into "model runs the tool"

On quiz 0001 (submission s1), Riley picked the option where the model itself opens the booking system and reads the calendar (q2), and counted three tool calls plus a final answer as one model call (q4) instead of four.
This answers the open question from [[0002-the-agent-loop]]: Riley has the loop's shape right but not yet the split between what the model outputs (a request) and what the program does (runs the tool, returns the result, calls the model again).
This matters for teaching context and memory next, since that topic depends on seeing each model call as a separate turn with its own input.

**Evidence:** quiz 0001, submission s1, items q2 and q4 (misconception M4 in both).
