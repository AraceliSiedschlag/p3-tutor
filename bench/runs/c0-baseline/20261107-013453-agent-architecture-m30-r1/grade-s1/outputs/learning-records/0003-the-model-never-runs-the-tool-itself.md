---
status: active
---

# Riley still thinks the model runs the tool itself

On quiz 0001, Riley picked up this misconception (M4) twice: on q2, choosing "the calendar entries, which it read by opening the booking system on its own" instead of the structured request the model actually outputs; and on q4, answering that the model was called once and ran all three tools inside that call, rather than 4 (one call per tool request, plus one for the final answer).
The model never touches a real system; it only ever outputs text or a structured request, and the program is what runs the tool and feeds the result back as a fresh call. This is foundational for the makerspace assistant's architecture, since every tool call Riley designs depends on this split between what the model decides and what the program does.

**Evidence:** quiz 0001, submission s1, items q2 and q4 (grades/0001-s1.json).

**Implications:** Worth a concrete worked trace (as in learning record 0002, but stepping through the model-call count explicitly) before the context-and-memory lesson, since that lesson's tool-use examples will keep assuming this split.
