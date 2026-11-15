# Review record: lessons/0001-context-and-memory.html (O3)

Two review passes ran.

## Pass 1 (5 findings, 0 must-fix)

- **D13** (length trending ~11-20% over budget): trimmed redundant "Section N showed..." transition sentences in Sections 3 and 4.
- **D14** (dense 45-word, triple-em-dash sentence in Section 1's opening): split into two sentences.
- **D15** (two justifications crammed into one sentence in Section 4 after "Second:"): split "accuracy" into its own sentence.
- **A2** (the "context windows have grown enormous" aside in Section 1 had no citation, unlike every other main claim): added a link to the Redis source.
- Check 1, 3, 4-12, 16: no findings, no change.

## Pass 2 (6 findings, 0 must-fix)

- **A2 (recurrence)**: Section 5's compaction/context-editing claim cited "(same source)" as plain text instead of a link; replaced with an explicit `<a href>` to the Anthropic source.
- **B6 / C10** (compaction and context editing, core fact 7, were explained but never checked, and were crowded into the same section as the unrelated notes idea): added a dedicated check-yourself question distinguishing compaction (within-session) from notes (cross-session), between the explanation and the lab-notebook example.
- **B7** (the term "tokens" was used in Section 1's first paragraph before its own `<dfn>` definition appeared in the next paragraph; "system prompt" and "tool definitions" were used throughout but never defined in plain words, even though NOTES.md says Riley has never written a tool definition): reordered Section 1 so tokens are defined first, then folded short plain-word definitions of "system prompt" and "tool definitions" into the context-window sentence.
- Check 1, 3, 4, 5, 8, 9, 11, 12, 14 (beyond the Section 5 crowding), 15, 16: no findings, no change.

Also fixed before either review pass, on my own read of the writer's draft: the warm-up's first recall question originally asked Riley to recall what a token is and why it matters for cost, framed as review of learning record 0001. But record 0001 explicitly states tokens "came up only in passing... has not been taught yet," and NOTES.md confirms Riley cannot yet say what a token limits or why it affects cost. Replaced it with a genuine recall question from record 0001 (why a chatbot can state an outdated fact confidently), so the warm-up is true spaced retrieval rather than new content mislabeled as review, and so Section 1 remains the single place "token" is first taught.

Stopped after two passes per the skill's rule (never a third).
