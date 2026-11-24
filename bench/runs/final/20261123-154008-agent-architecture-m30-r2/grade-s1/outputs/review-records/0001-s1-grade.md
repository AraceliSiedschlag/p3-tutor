# Review record: grades 0001-s1

Two review passes ran.

## Pass 1

- Check 3 (q4): feedback credited nothing sound in Riley's answer before correcting it. Grader added a line crediting the correctly-tracked sequence of three tools ending in a final answer, before explaining the call-count error.
- Check 8 (q6): feedback was 178 words, over the 150-word limit (must-fix). Grader cut the chat-apps analogy sentence and trimmed the training-record analogy, bringing it to roughly 140 words.
- Check 9 (q4): same root cause as check 3 - no honest positive point in a "wrong" verdict's feedback. Same fix applied (credit line added before the correction).
- Check 10 (q6): feedback was one dense five-sentence block, against PREFERENCES.md's "short paragraphs... one idea at a time." Grader split it into two short chunks (what's right / what's wrong-and-why) separated by a blank line.

## Pass 2

- Check 2: reviewer could not open `keys/0001.json` (blocked by the keys guard) and so could not confirm the misconception ids (M4 on q2/q4, M3 on q6) against the key's actual `distractors`/rationale, though the two uses looked internally consistent. Grader (with key access) checked directly: q2's M4 matches the key's distractor map for option a, q4's M4 matches the key's rationale note on the "1" answer, and q6's M3 matches the key's q1 option-b mapping for cross-session memory, distinct from M4. No change needed; draft was already correct.
- All other checks (1, 3-12): none.

Final draft written unchanged to `grades/0001-s1.json`.
