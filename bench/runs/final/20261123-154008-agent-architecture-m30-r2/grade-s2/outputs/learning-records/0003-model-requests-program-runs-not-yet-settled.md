# The model-requests, program-runs split is not yet settled

Riley can count model calls correctly (quiz 0001 q4: answered 4, right) but still describes the mechanism as the model "running" each tool itself, and separately gave a stuck coding agent the benefit of the doubt rather than naming a step limit as the safeguard (q3). Both point at the same seam: who acts, versus who decides. This was the open question flagged in [[0002-the-agent-loop]], and the quiz shows it only half-closed - the loop's shape is solid, but the division of labor inside each step, and why an agent needs a forced stop, are not yet firm.

**Evidence:** quiz 0001, submission s2, items q3 (wrong, M6: trusted a stuck loop to self-correct instead of needing a stopping condition) and q4 (partial, M4: right answer, reasoning said the model runs the tool rather than requests it).

**Implications:** Next lesson on this objective should make the model-requests/program-runs split and the need for a step limit concrete with a worked trace, before moving on to context and memory. Also worth a light touch: q6 showed Riley thinks tool selection is by name alone; the model actually matches on the full tool description (name, purpose, parameters), so that's a small gap to fold into the same lesson.
