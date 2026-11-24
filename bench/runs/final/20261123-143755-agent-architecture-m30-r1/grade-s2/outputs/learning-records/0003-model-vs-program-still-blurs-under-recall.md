---
status: active
---

# The model/program split blurs for Riley once answers come from memory, not a lookup

On quiz 0001's second attempt (s2, four days later, from memory), Riley still got the right tool-call count in q4 but explained it by picturing the model itself running `check_calendar`, `search_manuals`, and `check_training_record` - the M4 misconception that the model executes tools rather than just requesting them. This is despite correctly describing, in q1, q2 and q5, that the model only ever outputs a request and that the program runs it and feeds the result back. So the mechanics are understood when asked directly, but the model/program boundary isn't yet solid enough to survive being restated from memory under a different framing.

Riley also picked the "just let it run longer, it'll eventually fix the bug" distractor in q3 (M6: more iterations imply more insight), a new misconception not seen on the first attempt.

**Evidence:** quiz 0001, submission s2, items q3 and q4.

**Implications:** Before moving on to context and memory, a quick exercise that has Riley label each step of a worked example as "model output" vs. "program action" (as suggested in the q4 feedback) would target the still-soft M4 boundary directly. M6 (iteration without a stopping condition fixes bugs) is new and worth a short follow-up check next session.
