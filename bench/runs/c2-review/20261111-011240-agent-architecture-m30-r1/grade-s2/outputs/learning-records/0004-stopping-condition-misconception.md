---
status: active
---

# Misconception: an unsupervised loop will eventually fix itself

On quiz 0001 q3 (a coding agent stuck repeating the same failing edit for 40 steps), Riley picked "no change; left to run longer, it will eventually fix the bug" over the step-limit answer. This shows the belief that more iterations alone improve an agent's output, rather than seeing that identical steps with no new information just repeat; the actual safeguard is an explicit stopping condition.

**Evidence:** quiz 0001, submission s2, item q3 (wrong, misconception M6).

**Implications:** This is a fresh gap, not touched by [[0001-what-a-language-model-does]] or [[0002-the-agent-loop]]. Worth revisiting directly next session, ideally with a concrete trace of a stuck loop so Riley can see that nothing changes between identical steps.
