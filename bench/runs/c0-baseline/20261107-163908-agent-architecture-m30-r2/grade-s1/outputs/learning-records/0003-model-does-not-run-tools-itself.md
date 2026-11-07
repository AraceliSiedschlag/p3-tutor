---
status: active
---

# Riley believes the model can act directly, not just request actions (M4)

Quiz 0001, submission s1, showed the same misconception twice: on q2, Riley chose the option where the model "reads calendar entries by opening the booking system on its own," and on q4, Riley counted 1 model call because "it runs the 3 tools itself and answers." Both treat the model as something that executes tools, when it only ever outputs a structured request naming a tool and its arguments; the program runs the tool and feeds the result back as a separate call.

**Evidence:** quiz 0001, submission s1, items q2 and q4.

**Implications:** This is the open item flagged in learning record 0002 ("whether Riley sees that the program, not the model, runs each tool") — not yet resolved. The same quiz also surfaced a related slip in q6, treating the model as if it remembers its own past tool choices across sessions. Before moving on to context and memory, redraw the agent loop from 0002 with each arrow labeled "model" or "program" to make this boundary explicit; memory lessons will be confusing until this is solid, since memory is precisely a case of the program choosing what to carry forward.
