---
status: active
---

# Riley still conflates the model with the program around it

Quiz 0001 (submission s1) confirms the gap record 0002 flagged as unchecked: Riley does not yet see that the model only ever requests a tool and the program is what executes it, nor that each tool use costs a separate model call (M4, missed on q2 and q4).
A related, previously unflagged idea also showed up: Riley believes the model has automatic memory across sessions, rather than that being something the program would have to store and feed back in (M3, added on q6).
Riley does firmly have the loop itself (q1, q3) and that a tool's result goes back to the model (q5, partial - has the "what," not yet the "why").

**Evidence:** quiz 0001, submission s1, items q2, q4 (both M4) and q6 (M3); grades in `grades/0001-s1.json`.

**Implications:** Before moving on to context and memory (next in the mission), Riley needs the model/program boundary made explicit - what the model outputs (a request) versus what runs it and carries state (the program) - since M3 is exactly the belief that would make "memory" seem like something the model does for free rather than something the assistant has to build. Re-test both M4 and M3 after that lesson, not just once passed over.
