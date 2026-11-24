# Review record: lessons/0001-context-and-memory.html

Objective O3, 30 minutes. Two reviewer passes ran; fixes applied after each.

## Pass 1 — 4 findings, 0 must-fix

- **A, check 2** (s-retrieval): cost comparison ("a few hundred tokens" vs. "tens of thousands") had no citation of its own.
  Fixed: replaced with an uncited-safe relative comparison ("roughly as many tokens as that page/the manual has words").
- **D, check 15** (worked example, step 3): one sentence packed two distinct ideas (mechanical retrieval vs. the note's content) into one dense clause.
  Fixed: split into two short sentences.
- **D, check 16**: the section-time labels summed to 36 minutes against a declared 30-minute lesson.
  Fixed: reduced five section-time labels (s-steps, s-sessions, s-retrieval: 4→3 min; worked example+practice: 6→4 min; summary: 2→1 min) so they sum to 30.
- Also fixed proactively, before the first reviewer pass, while checking the draft myself: every multiple-choice practice check had its correct answer in the middle position (position 2) with no variation across all 7 checks, violating `LESSONS.md`'s "vary which position holds the right one." Reordered options so correct answers now fall at positions 1, 3, 2, 1, 3, 2, 1 across the seven checks.

## Pass 2 — 3 findings, 0 must-fix

- **B, check 6** (s-rot): the section's single practice check didn't clearly separate which wrong option targeted the context-rot/accuracy idea versus the token-cost idea.
  Fixed: rewrote the two wrong options' feedback to each name the one idea they target (accuracy vs. cost) explicitly.
- **B, check 7**: "session" was used as a load-bearing technical term throughout (s-steps, s-rot, s-sessions, s-notes) but never defined with `<dfn>`, unlike the lesson's other new terms.
  Fixed: added a one-sentence `<dfn>` definition of "session" in section s-context, before its first heavy technical use.
- **D, check 14**: `PREFERENCES.md` and the plan's style notes called for a little flattery, but no section carried any encouraging line.
  Fixed: added one line at the start of the warm-up ("You've already got the model basics and the agent loop down — this builds right on top of them.").

No core fact from the plan was cut to resolve any finding. Stopped after two passes, per the skill's cap.
