# Riley believes the model can run tools or act on the world itself (M4)

On quiz 0001 (submission s1), Riley missed both items that hinge on this: choosing "the model read the calendar by opening the booking system on its own" for q2, and answering "1 model call" for q4 because "it runs the 3 tools itself and answers." The model only ever emits a structured request naming a tool and its arguments; the program is what runs the tool and feeds the result back as a separate call. This needs to be corrected explicitly before context and memory, since every claim about what the model "sees" or "remembers" depends on first accepting that the model cannot act or fetch anything on its own.

**Evidence:** quiz 0001, submission s1, items q2 and q4.

**Implications:** Revisit this directly at the start of the context-and-memory session; it is load-bearing for understanding why context has to be explicitly assembled by the program.
