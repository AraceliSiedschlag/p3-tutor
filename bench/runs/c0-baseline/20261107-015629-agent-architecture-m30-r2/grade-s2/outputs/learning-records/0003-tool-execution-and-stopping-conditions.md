---
status: active
---

# Two misconceptions still open after spaced practice

On quiz 0001, submission s2 (four days after the agent-loop lesson, from memory), Riley got the tool-calling and feedback-loop items right (q1, q2, q5) but showed two specific gaps. On q4, the count of model calls was correct (4), but the stated reasoning still described the model as running the tool itself rather than the program running it (M4) — a softer version of the same mistake made outright on s1's q4. On q3, Riley chose "no change, it will eventually fix the bug" for a stuck 40-step loop, showing M6: the belief that an agent needs no stopping condition.

**Evidence:** quiz 0001, submission s2, items q3 and q4.

**Implications:** M4 is fading (the number came out right this time) but the wording habit hasn't caught up yet — worth a quick retrieval prompt next session ("who actually runs the tool?") rather than a full re-teach. M6 is newer evidence and worth a short, separate check: ask Riley to name a stopping condition other than a step limit before moving on to context and memory.
