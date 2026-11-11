# Riley sees that the model requests a tool and the program runs it

Riley correctly picked, on quiz 0001, that at the moment the model decides to use a tool it only outputs a structured request (q2), and counted the model calls in a multi-tool run as one per request plus one for the final answer, 4 in total (q4) - both depend on knowing the model never executes a tool itself. This resolves the open question from [[0002-the-agent-loop]], whether Riley sees that the program, not the model, runs each tool.

**Evidence:** quiz 0001, submission s2, items q2 (correct) and q4 (correct count, verdict partial only for a wording slip - see [[0004-stopping-condition-misconception]] note below).

**Implications:** The underlying split is there, but the language still blurs it sometimes - q4's reasoning said the model "can only run one tool itself each time it's called," describing the model as the one running the tool even though the count built from that reasoning was right. Worth a quick check next session that this is just loose phrasing and not a residual belief.
