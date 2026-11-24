# Riley believes the model runs tools and remembers across sessions by itself

Quiz 0001 (submission s1) shows two related misconceptions, open rather than corrected: on q2 and q4, Riley picked answers where the model itself executes tool calls (reading the calendar, running three tools in one turn) instead of the program running each tool and calling the model again; on q6, Riley added, unprompted, that the model "remembers on its own" which tool it picked in earlier sessions.
This confirms what learning record [[0002-the-agent-loop]] flagged as not yet checked: Riley has the loop's shape right (q1, q3 correct) but not yet that each step is a separate model call with the program doing the execution and all memory, and that the model carries nothing between calls by itself.

**Evidence:** quiz 0001, submission s1, items q2, q4 (both M4) and q6 (M3).

**Implications:** This lands right before the next mission topic, context and memory - the lesson should open by drawing the model/program line explicitly (the model only ever outputs one request or a final answer per call) before introducing what the program chooses to carry forward between calls.
