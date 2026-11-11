# Riley believes the model executes tools itself

On quiz 0001 (submission s1), Riley twice described the model as running tools directly inside one call, rather than the model only emitting a structured request that the program then executes: picking "opened the booking system on its own" for what the model outputs when calling check_calendar (q2), and counting a 3-tool, 1-answer run as a single model call because "it runs the 3 tools itself" (q4). Riley did correctly describe tool selection from tool descriptions (q6), so the gap is specifically about who carries out the call, not how the tool is chosen.

**Evidence:** quiz 0001, submission s1, items q2 and q4 (graded wrong, misconception M4 both times).

**Implications:** Not yet corrected. The next lesson on tools should make the model/program split explicit and concrete, e.g. walk through one request call by call, labeling each step as "model outputs a request" vs. "program runs the tool," before moving on to context and memory.
