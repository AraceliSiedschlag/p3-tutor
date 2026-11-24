# Lesson plan — O3: Context and memory in an agent

Objective: Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.
Requested length: 30 minutes.
Learner: Riley (data science major, works in IT, likes cooking, comfortable with Python, has met the agent loop and "a model predicts text from training + input" but not tokens, memory, retrieval, or context limits).

## Core facts

1. The context window is all the text (tokens) a model can reference when generating a response — the system prompt, the conversation so far, tool definitions and tool results, and the output itself — and it is a "working memory" distinct from what the model learned in training.
   Source: https://platform.claude.com/docs/en/build-with-claude/context-windows
2. The context window has a fixed size measured in tokens; it is shared between input and output, and if the input alone is already too big the request fails, while hitting the limit mid-generation stops the output early.
   Source: https://platform.claude.com/docs/en/build-with-claude/context-windows
3. Within one running agent session, previous turns are preserved completely by default: each new step's input is everything that came before plus the newest message, so earlier tool results stay visible unless something explicitly removes them.
   Source: https://platform.claude.com/docs/en/build-with-claude/context-windows
4. More context is not automatically better: as token count grows, accuracy and recall degrade ("context rot"), so what is kept in context matters as much as how much room there is.
   Source: https://platform.claude.com/docs/en/build-with-claude/context-windows
5. Nothing survives automatically between separate sessions: when a session ends, its context window is gone, so an agent only "remembers" something from a prior session if it was written to storage outside the context window and read back in.
   Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
6. Notes-as-memory means the agent itself writes what it learns (facts, decisions, progress) to files or a database outside the context window and reads them back in a later session, building knowledge over time without keeping everything loaded at once.
   Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
7. Retrieval (as in retrieval-augmented generation) is a technique that searches a large external source — such as a long manual — for the part relevant to the current request and adds only that part to the prompt, instead of loading the whole source.
   Source: https://www.ibm.com/think/topics/retrieval-augmented-generation
8. Retrieval exists because it lets a model answer accurately from material much larger than its context window and keep answers current, without retraining the model; the knowledge stays external and is pulled in only when needed.
   Source: https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/what-is-rag.html

## Misconceptions

- **"A bigger context window always gives a better answer."** Tempting because capacity sounds like it can only help, but context rot means stuffing in more, including irrelevant history, can make the model less accurate, not more (fact 4).
- **"The model remembers earlier conversations on its own, like a person would."** Tempting because talking to it across visits feels continuous, but each session's context window starts empty; anything that feels like memory was actually written to storage and read back in, or it is not there at all (fact 5).
- **"Context window and memory are the same thing."** Tempting because both answer "what does the model know right now," but the context window is temporary and per-session while notes/retrieval are durable storage the agent chooses to write to and search, outside the window (facts 1, 5, 6).
- **"Retrieval means handing the model the whole document."** Tempting because "giving the model access" sounds like giving it everything, but retrieval's point is to pull in only the relevant slice so the context window never has to hold the whole source (facts 7, 8).
- **"Mid-session, only the most recent tool result matters."** Tempting because the agent seems to move on after each step, but by default every earlier turn in the same session stays in context unless something is explicitly dropped (fact 3).

## The win

By the end, Riley can take a request the makerspace assistant handles (such as "can I book the laser cutter Friday, and do I still need safety training?") and correctly sort each piece of information it needs into "lives in context for this turn," "saved as a note for next session," or "retrieved from the manual on demand," with a reason for each.

## Word budget

30 minutes x 150 words/minute = **4,500 words**.

| Part | Words |
|---|---|
| Opening | 300 |
| Warm-up recall | 200 |
| A. What's in the context window right now | 500 |
| B. What carries forward step to step, same session | 450 |
| C. Limits and context rot | 500 |
| D. Between sessions: nothing survives unless saved | 500 |
| E. Notes as memory | 500 |
| F. Retrieval: finding the right page on demand | 550 |
| Worked example + faded practice | 650 |
| Summary | 250 |
| Go further / closing | 100 |
| **Total** | **4,500** |

## Sections

### Opening — 300 words
One idea: name the win and tie it to the mission (the makerspace assistant must answer from long manuals and remember each student's training status between visits — this lesson is exactly how).
No new fact taught yet; sets up why this matters for the design review.

### Warm-up recall — 200 words
One idea: spaced recall of two earlier ideas the new material depends on: (1) from learning record 0001, that the model's input is everything it has to work with beyond training; (2) from learning record 0002, the agent loop (model asks for an action, result comes back, repeats).
Answers revealed on demand. No practice-with-feedback question here (this is recall, not new-skill practice).

### Section A — What's in the context window right now — 500 words
One idea: the context window is everything sent to the model for one turn — system prompt, conversation, tool definitions and results, output — not the model's training.
Teaches fact 1.
Example: the IT "RAM vs. installed software vs. disk" analogy — RAM (context window) is what the program is actively working with right now, separate from the software already compiled into it (training) and from files sitting unread on disk (name only; do not write out).
Practice: given the laser-cutter booking request, ask which items count toward the context window for that turn (e.g., the tool definitions and the calendar result) versus which do not (e.g., pages of the manual nobody has pulled in yet). Wrong answer targets the misconception that context window = memory = everything relevant, not just what was actually sent.

### Section B — What carries forward step to step, same session — 450 words
One idea: by default, every earlier turn in a session stays in the context window for later turns — nothing mid-session is quietly dropped.
Teaches fact 3.
Example: re-trace the laser-cutter request from learning record 0002 across three steps and point out step 1's tool result is still sitting in context at step 3 (name the example: the Friday-booking trace; do not write it out in full here).
Practice: ask whether a step-1 tool result is visible to the model at step 3 of the same run. Wrong answer targets "only the latest tool result matters mid-session."

### Section C — Limits and context rot — 500 words
One idea: the context window has a fixed token size shared by input and output, and filling it with more (even if it fits) can make answers worse, not better.
Teaches fact 2 and fact 4.
Example: the IT analogy again — a machine that is slow and makes mistakes once RAM is crammed with old, irrelevant data, versus one kept tidy (name only).
Practice: "the assistant's context is almost full of old, unrelated chat turns — does adding more history make the next answer more reliable?" Wrong answer targets "bigger/more context is always better."

### Section D — Between sessions: nothing survives unless saved — 500 words
One idea: when a session ends its context window disappears completely; across a new session, nothing is remembered unless something wrote it to storage outside the window first.
Teaches fact 5.
Example: cooking — a recipe you worked out in your head while cooking is gone once you leave the kitchen unless you wrote it on an index card first (name the example: the recipe index card; do not write it out).
Practice: "a student who finished safety training yesterday returns today in a new session — does the assistant know, if nothing was saved?" Wrong answer targets "the model remembers like a person because we already talked."

### Section E — Notes as memory — 500 words
One idea: an agent gets session-to-session memory by writing what it learns to files or a database outside the context window, then reading them back in later.
Teaches fact 6.
Example: the recipe index-card box, now applied directly to the mission — the assistant writing "student X passed laser safety training on [date]" to a saved record so next visit's session can read it back.
Practice: given a short scenario, choose what belongs in a saved note (the training date) versus what does not (this morning's exact wording of the question). Wrong answer targets "memory and context window are the same thing."

### Section F — Retrieval: finding the right page on demand — 550 words
One idea: retrieval searches a large external source and pulls in only the relevant part for the current request, instead of loading all of it into context.
Teaches facts 7 and 8.
Example: data-science-flavored search-index analogy — like searching a textbook's index for "laser cutter maintenance" instead of reading the whole 300-page manual before answering (name the example: the manual search; do not write it out).
Practice: "to let the assistant answer from a 300-page manual, should you paste the whole manual into every prompt, or retrieve just the relevant page?" Wrong answer targets "retrieval means handing the model the whole document."

## Worked example and faded practice

**Task:** For the request "Can I book the laser cutter Friday afternoon, and do I still need to retake safety training?", the assistant has four pieces of information available: (1) the student's current question, (2) the booking calendar's result for Friday, (3) the laser cutter manual's safety-retraining-interval section, (4) the student's safety-training completion date from their last visit.

**Worked steps (shown in full):** Classify item (1) and (2) as "context window for this turn" — they arrive as the user message and the tool result for this specific request, with the reasoning spelled out (fact 1, fact 3).

**Faded for the learner:** Classify item (3) — reasoning left to the learner, pointing back to Section F (retrieval: a section of a long manual, pulled in on demand). Classify item (4) — reasoning left to the learner, pointing back to Section E (notes as memory: a fact saved from a past session). Solution revealed on demand, explaining why each is retrieval vs. notes rather than context.

## Style notes for the writer

- Open with the big picture and the why (tie to the makerspace assistant) before any analogy, per PREFERENCES.md; then give the analogy, then the mechanism.
- Short paragraphs, one idea each; bullets are fine, no big blocks of text.
- Use the IT (RAM/disk), cooking (recipe index cards), and data-science (search index) analogies named in PREFERENCES.md's "examples I relate to," each tied back to the makerspace assistant, not left generic.
- Define each new term (token, context window, context rot, retrieval, memory) once, in plain words, the first time it appears.
- Every practice question gives feedback immediately: state plainly what is right, what was wrong with the reasoning behind each tempting wrong answer, and how to fix that reasoning — per PREFERENCES.md's "how I like feedback."
- Tone: casual and direct, no filler, a little genuine flattery when Riley gets something right (per PREFERENCES.md).
- Close by naming the primary source to read next, reminding Riley they can ask follow-up questions in chat, and that a quiz on this lesson is ready when they want it.
- Link back to learning records 0001 and 0002's ideas in the warm-up, and leave a clear pointer that workflows-vs-agents and multi-agent systems (next in NOTES.md's "does not know yet") come after this.

## Sources

**Primary source:** Context windows — Claude Platform Docs. https://platform.claude.com/docs/en/build-with-claude/context-windows
Chosen because it is the official, precise definition of the context window and of what carries forward turn to turn within a session, which anchors two of the three parts of this objective.

**Other sources:**
- Memory tool — Claude Platform Docs. https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool (notes-as-memory and persistence between sessions, facts 5 and 6)
- What is Retrieval Augmented Generation (RAG)? — IBM. https://www.ibm.com/think/topics/retrieval-augmented-generation (retrieval as a technique, fact 7)
- Understanding Retrieval Augmented Generation — AWS Prescriptive Guidance. https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/what-is-rag.html (why retrieval is used instead of retraining, fact 8)
