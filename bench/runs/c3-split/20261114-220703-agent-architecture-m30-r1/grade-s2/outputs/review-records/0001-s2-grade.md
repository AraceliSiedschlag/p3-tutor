# Review record: grades/0001-s2.json

Two review passes ran.

## Pass 1 (7 findings, 2 must-fix)
- Check 1 (must-fix): q4 verdict was `correct`, but the response's stated reasoning ("the model can only run one tool itself") asserts the model executes tools, matching M4. Changed verdict to `partial`.
- Check 2 (must-fix): q4 `misconception` was `null`; set to `"M4"`.
- Check 4/5/6: q4 feedback called the error "a nit on the wording" without quoting the flawed phrase, naming the wrong idea plainly, or explaining the underlying reason. Rewrote the feedback to quote the learner's line, state the wrong idea directly, and explain that the model can only produce text/requests, never execute code.
- Check 10: q3 feedback was one dense run-on paragraph. Split into shorter sentences per PREFERENCES.md.
- Check 11: summary cited q4 as evidence the model-vs-program split was "down cold," which contradicted q4's own reasoning problem, and didn't mention q6's related partial. Rewrote summary to drop q4 as supporting evidence and tie q4 and q6 together as the same family of confusion.
- Checks 3, 7, 8, 9, 12: none.

## Pass 2 (1 finding)
- Check 11: summary's next step told the learner to "check it against q2's key," naming an internal file (`key`) the learner has no access to. Replaced with "compare it with how you reasoned through q2."
- All other checks: none.

Stopped after pass 2, which had only the one finding, now fixed.
