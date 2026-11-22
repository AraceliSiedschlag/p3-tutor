# Still believes a stuck agent loop will fix itself given more steps

On quiz 0001 (q3), Riley picked "no change, it will eventually fix the bug" for an agent stuck repeating the same failing edit for 40 steps -- misconception M6, that more steps alone can resolve a loop with no new information coming in. This is the opposite of q1/q2/q4/q5, all answered correctly, which show a solid grip on the loop mechanics (model requests, program runs, result comes back). The gap is specifically about *when the loop should stop*, not what the loop is.

**Evidence:** quiz 0001, submission s2, item q3.

**Implications:** When agent control structures come up again (step limits, termination conditions, escalation to a human), start from this scenario rather than re-teaching the loop itself -- Riley already has that part.
