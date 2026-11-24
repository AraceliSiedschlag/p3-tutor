# Review record — lessons/0001-context-and-memory.html (O3)

Two review passes ran, as the first pass had findings.

## Pass 1 — 7 findings, 1 must-fix

- **Check 2 (must-fix):** Section F's "scale and freshness" claim cited the AWS Prescriptive Guidance RAG page, which doesn't state that retrieval lets a model exceed its context window or skip retraining. Fixed: swapped the citation to https://aws.amazon.com/what-is/retrieval-augmented-generation/ (verified via a fetch agent to state the no-retraining claim directly) and reworded the sentence.
- **Check 6:** Section C held two ideas (fixed-size overflow, context rot) with only one practice check. Fixed: added a dedicated check on overflow behavior.
- **Check 8:** Only 2 of 5 planned misconceptions had a dedicated callout. Fixed: added a callout for "context window and memory are the same thing" in Section E.
- **Check 14:** No flattery in correct-answer feedback, against PREFERENCES.md. Fixed: added genuine flattery to three correct-answer `data-why` strings.
- **Check 14 (writing):** One paragraph in Section A bundled three sub-analogies. Fixed: split into two shorter paragraphs.

## Pass 2 — 8 findings, 0 must-fix

- **Check 1/2:** Section F's reworded sentence still paired one citation with two claims (context-window scale + no-retraining), and only the second is on the cited page. Fixed: split the scale claim out as the lesson's own inference (pointing back to Section C) and kept the citation only on the no-retraining claim.
- **Check 2:** Section D's "no background copy kept anywhere" overstated what the memory-tool page says. Fixed: softened to "that progress is simply lost."
- **Check 6:** Repeated suggestion to split Section C into two headed sections. **Not applied** — both sub-ideas already have their own paragraph and check; splitting would require renumbering anchors, the TOC, and time budgets for a stylistic preference with no must-fix behind it. Noted here instead.
- **Check 8:** 2 of 5 planned misconceptions ("only the latest tool result matters," "retrieval means the whole document") still lacked a dedicated callout. Fixed: added both, in Sections B and F.
- **Check 15:** The opening lead sentence ran ~75 words in one breath. Fixed: split into two sentences.

Final file written to `lessons/0001-context-and-memory.html` after both rounds of fixes.
