# Review record: lesson 0001, "Context and memory"

Two review passes ran, as the teach skill allows at most two.

## Pass 1 (5 findings, 0 must-fix)

- Check 6 (pedagogy): "Retrieval and notes as memory" piled two ideas under one check. **Fixed:** split into two sections (retrieval, notes), each with its own check-yourself.
- Check 13 (length): ~2,900 visible words (~19 min) against a 30-minute, 4,500-word budget &mdash; close to the 0.6x floor. **Fixed:** added a cost-arithmetic worked passage, a new section and check, and expanded worked-example reasoning.
- Check 14 (style): PREFERENCES.md asks for short paragraphs, not big blocks; two misconception boxes and one explanatory paragraph ran long. **Fixed:** split each into two shorter paragraphs.
- Check 14 (style): PREFERENCES.md asks for "some flattery"; the draft had none. **Fixed:** added warmth in the warm-up reveal and the summary.
- Check 15 (style): the "Problem two" paragraph chained too many clauses. **Fixed:** split into three sentences across two shorter paragraphs (now in the new "Notes" section).

## Pass 2 (7 findings, 1 must-fix)

- Check 3 (correctness, **must-fix**): the token-cost worked example and its check-yourself both said "call 4" for a run with only two tool calls, which should be call 3 under the N tool calls &rarr; N+1 model calls rule the learner already knows from quiz 0001 q4. Figure 1 also drew four bars for a two-tool-call scenario. **Fixed:** corrected the math to three calls (600 &rarr; 750 &rarr; 1,150 tokens), redrew Figure 1 with three bars, and changed the check-yourself to "third model call."
- Check 2 (correctness): the claim that nothing persists between sessions was cited to the Anthropic context-engineering article, which doesn't state that directly. **Fixed:** replaced with a direct quote from the memory-tool docs ("memory lives entirely in your application") and framed the claim as a consequence of the statelessness already established in section 1.
- Check 6 (pedagogy): the new, larger "The context window" section (after pass 1's fix) itself piled up the window definition, accumulation, cost math, and the context-rot misconception under one check. **Fixed:** split again into "The context window" (definition, statelessness, a new check on the single-chat-window illusion) and "Context grows every step" (accumulation, cost, context rot, the original check).
- Check 13 (length): still ~20% under budget after pass 1's additions. **Fixed:** the second section split (previous bullet) added a full new section with its own explanation, figure-adjacent reasoning, and check, bringing the lesson closer to budget without padding.
- Check 14 (style): the token-math paragraph was still one dense block. **Fixed:** converted the three running totals into a short bulleted list.
- Check 15 (style): the step-limit aside had an awkward dangling clause. **Fixed:** reworded it to a clean em-dash construction.

No findings remained unaddressed. Final lesson written to `lessons/0001-context-and-memory.html`.
