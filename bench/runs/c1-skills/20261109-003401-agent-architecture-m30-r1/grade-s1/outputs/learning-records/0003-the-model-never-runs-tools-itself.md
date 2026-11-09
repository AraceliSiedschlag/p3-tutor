# The model never runs tools itself - M4 is still open

Quiz 0001 showed, in two separate items, that Riley believes the model that requests a tool also executes it: picking "it read the calendar by opening the booking system on its own" for q2, and reasoning for q4 that the model "runs the 3 tools itself" inside one call before answering. This is misconception M4, flagged as untested in learning record 0002 and now confirmed rather than corrected. The next lesson on tool calling should separate, explicitly and repeatedly, what the model outputs (a structured request) from what the program does (runs the tool, gets the real result, feeds it back) - this split is the floor for context, memory and multi-step plans later in the mission.

**Evidence:** quiz 0001, submission s1, items q2 and q4.

**Implications:** Before moving to context and memory, revisit the model/program split directly. Also worth checking whether Riley's q6 answer ("it remembers which tool it picked in earlier sessions") - which shows M3, automatic memory of past conversations - is the same instinct in a new spot: nothing persists unless the program explicitly stores and resends it.
