# Review record: grades/0001-s1.json

Two review passes ran.

## Pass 1
- Check 3 (q4): feedback never credited the part Riley got right - that the three tools fire in the correct order before the final answer.
  Grader fix: added an opening line crediting the correct sequencing before explaining why the count is still 4, not 1.
- Check 9 (q4): same root cause - no honest positive point before pivoting to the fix.
  Grader fix: same addition also folded into the summary, which now notes the correct sequencing before naming the undercounting misconception.
- All other checks (1, 2, 4-8, 10-12): none.

## Pass 2
- Check 6 (q4): the revised feedback explained the call count by restating the stem's bookkeeping rule ("one tool request or final answer per call") rather than the deeper reason - that a model call is a single text output with no built-in way to execute anything, so one turn can only ever carry one instruction.
  Grader fix: added a line tying the count back to that root fact, ahead of the "3 + 1 = 4" bookkeeping.
- All other checks (1-5, 7-12): none.

No third pass was run, per the two-pass limit.
