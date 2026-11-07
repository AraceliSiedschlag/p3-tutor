# Riley believes the model runs tools itself (M4)

On quiz 0001, Riley missed both items that distinguish the model's output from the program's action: picked "the model read the calendar by opening the booking system on its own" (q2), and answered that the model "runs the 3 tools itself" inside one call (q4). This resolves the open question from learning record 0002: the loop's shape is understood, but not yet that the model only ever emits a request, and the program is what carries it out.

**Evidence:** quiz 0001, submission s1, items q2 and q4.

**Implications:** Teach this distinction explicitly before building on tool calling further — it is likely to resurface wherever the assistant's architecture is discussed. Also note: q6 showed a second, smaller slip in the same family — stating that the model "remembers on its own" which tool it picked in past sessions, i.e. assuming automatic persistence (M3) where none exists. Worth revisiting both together, since they share the root confusion of attributing agency/memory to the model that actually belongs to the surrounding program.
