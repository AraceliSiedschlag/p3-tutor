# An agent needs a stopping condition, not more steps

On quiz 0001 (submission s2), Riley picked "no change, it'll eventually fix the bug" for a coding agent stuck repeating the same failing edit, showing the belief that a stuck loop resolves itself if it runs long enough rather than needing a built-in limit that halts it and reports back.
This is the misconception to clear before the design review, since the makerspace assistant will need the same safeguard anywhere it loops on a booking or manual lookup that could stall.

**Evidence:** quiz 0001, submission s2, item q3.

**Implications:** The same submission's q4 shows a smaller, related residue: Riley's correct answer (4 model calls) was reasoned through language suggesting the model itself "runs" the tool, rather than only requesting it for the program to run. Worth a quick check once Riley writes a real tool definition, to see if that distinction has firmed up.
