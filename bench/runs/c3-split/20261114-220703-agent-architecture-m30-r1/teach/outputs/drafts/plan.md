# Lesson plan — O3: Context and memory in an agent

Objective: Explain context and memory in an agent: the context window, what is kept between steps and between
sessions, and retrieval and notes as memory.
Requested length: 30 minutes.

## The win

By the end, Riley can take any moment in the makerspace assistant's agent loop and say correctly what is
currently in the context window, what will and will not still be there next session, and whether retrieval or
notes is the right fix for getting old information back.

## Word budget

30 minutes x 150 words/minute = **4,500 words**, all visible text (explanations, examples, practice, captions).

| Section | Words |
|---|---|
| Opening | 200 |
| Warm-up (recall) | 150 |
| 1. The context window: finite, token-counted working memory | 600 |
| 2. Within one session: the loop keeps feeding the growing context back in | 550 |
| 3. Between sessions: by default, nothing survives | 500 |
| 4. Retrieval: pulling in just the relevant piece on demand | 600 |
| 5. Notes: the agent's own summaries as memory it writes and rereads | 600 |
| Common mix-ups (quick-fire) | 300 |
| Worked example + faded practice (two-session trace) | 700 |
| Summary, explain-back prompt, go further, closing | 300 |
| **Total** | **4,500** |

## Core facts

1. The context window is the full set of tokens (system prompt, tool definitions, message history, tool
   results, and the output) an LLM can attend to in one call; it is finite, and the whole thing is sometimes
   called the model's "attention budget."
   — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
2. A token is a chunk of text, roughly three-quarters of a word; everything sent to or returned from the model —
   prompt, retrieved manual pages, conversation history — is counted in tokens against the context-window limit
   and against cost.
   — https://redis.io/blog/llm-context-windows/
3. Within one agent session, each loop step's tool calls and results are appended to the context and carried
   forward into the next model call, which is why the context keeps growing turn by turn until something trims
   it.
   — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
4. By default, nothing in the context window survives once a session ends — a new session starts with an empty
   window, so without deliberate saving, the agent has no memory of a past conversation.
   — https://github.com/addyosmani/agent-engineer/blob/main/05-memory-and-context/README.md
5. To remember things across sessions, an agent (really, the surrounding program) saves selected information to
   external, durable storage, then retrieves only the relevant part and inserts it back into the next session's
   context window.
   — https://github.com/addyosmani/agent-engineer/blob/main/05-memory-and-context/README.md
6. Structured note-taking — the agent writing its own short summaries or logs to a file outside the context
   window, which are read back in later — is a lightweight memory technique that does not require a database.
   — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
7. When a single session's context window is filling up, agents use compaction (summarizing older turns) or
   context editing (clearing stale tool results) to keep going without losing the critical facts.
   — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
8. Dumping an entire manual or history into a huge context window costs more per call and can still lose
   accuracy as unrelated text piles up (the "lost-in-the-middle" effect), so retrieving just the relevant piece
   is usually cheaper and more reliable than stuffing everything in.
   — https://redis.io/blog/llm-context-windows/

## Common misconceptions

- **"A bigger context window means I don't need memory or retrieval."** Tempting because today's windows are
  huge (hundreds of thousands to millions of tokens), so it feels like everything could just fit. Wrong because
  cost scales with tokens sent and accuracy can still drop as irrelevant text piles up — fact 8.
- **"The model remembers me from last time we talked."** Tempting because chat apps feel continuous across
  visits. Wrong because the model itself holds nothing between calls; any apparent memory is the surrounding
  program re-inserting saved text into a fresh context window — facts 1, 4, 5.
- **"Context window and memory are the same thing."** Tempting because both answer "what does the model know
  right now." Wrong because the context window is the per-call budget, while memory is the external storage and
  retrieval system that decides what gets put into that budget — facts 1, 4, 5.
- **"Writing a note is enough; the agent will just know it later."** Tempting because saving feels like the
  whole job. Wrong because something must still explicitly retrieve that note and insert its text back into a
  later context window, or it is never seen again — facts 5, 6.
- **"Once the window fills, everything so far is safely remembered somewhere automatically."** Tempting because
  it is counterintuitive for a computer to "forget." Wrong because, without compaction or notes, trimmed or
  dropped content is simply gone — facts 3, 7.

## Sections

### Opening (200 words)
One idea: name the win and tie it to the mission — the makerspace assistant must answer from long manuals and
remember each student's training status between visits, and both of those are context-and-memory problems.
No new facts yet; sets up why this lesson matters for the design review.

### Warm-up (150 words)
Recall check on learning records 0001–0002: ask Riley to name, in one line, what a token is used for and to
retrace the agent loop for "book the laser cutter Friday." Reveals answers on demand; spacing practice, not new
content.

### Section 1 — The context window is finite, token-counted working memory (600 words)
- **Idea:** everything the model currently sees — system prompt, tool defs, history, tool results — shares one
  limited, token-measured space.
- **Facts taught:** 1, 2.
- **Example:** cooking — prepping a big meal on one counter/cutting board; only so much fits in front of you at
  once, so you cannot lay the whole cookbook open while you work (name it; do not write it out). Tie back to the
  makerspace manual being too long to fit whole.
- **Practice:** a short scenario gives a tool result and a question; ask "is this still inside the context
  window right now, yes or no, and why." Wrong answer targets the "bigger window = no limit" misconception by
  having a case where the window is large but the question is really about cost/relevance, not about whether it
  technically fits.

### Section 2 — Within one session, the loop keeps feeding the growing context back in (550 words)
- **Idea:** each step of the agent loop appends its tool call and result to the context, and that whole, growing
  thing is sent back in on the next call — this is what "kept between steps" means.
- **Facts taught:** 3.
- **Example:** reuse and extend the already-taught agent-loop trace ("is the laser cutter free Friday?" from
  learning record 0002) — name it, show one more step (the booking confirmation) being appended.
- **Practice:** given a 3-step loop trace, ask which step's result is still visible to the model at step 4.
  Wrong answer targets the misconception that only the very last tool result is kept, versus the whole growing
  history.

### Section 3 — Between sessions, by default nothing survives (500 words)
- **Idea:** a new session starts with an empty context window; last session's loop history is gone unless it
  was deliberately saved outside the window.
- **Facts taught:** 4.
- **Example:** IT work — a server process restarting wipes anything only held in RAM; whatever was not written
  to disk is gone (name it, tie to the assistant restarting between student visits).
- **Practice:** "Riley booked the laser cutter Monday. Wednesday a new session starts. Does the assistant know
  about Monday's booking?" Correct answer is "only if it was saved somewhere outside the window and is
  retrieved now." Wrong answer targets "the model remembers me from last time."

### Section 4 — Retrieval: pulling in just the relevant piece on demand (600 words)
- **Idea:** memory across sessions mostly works by retrieval — saving things in durable storage, then fetching
  only the relevant piece back into context when it is needed, instead of loading everything.
- **Facts taught:** 5, 8.
- **Example:** cooking again — flipping straight to the one page a cookbook's index points to, instead of
  reading the whole book before you cook (name it, tie to looking up one page of a machine manual instead of
  loading the whole manual every time).
- **Practice:** "the manual is 300 pages. Should the assistant put the whole manual in context every request,
  or retrieve the one relevant page?" Correct answer: retrieve the page. Wrong answer targets "bigger context
  window means I don't need retrieval."

### Section 5 — Notes: the agent's own summaries as memory it writes and rereads (600 words)
- **Idea:** an agent can keep its own memory by writing short notes or summaries to a file outside the context
  window, which get read back in later; this is also how a long session stays usable (compaction/context
  editing) without losing the key facts.
- **Facts taught:** 6, 7.
- **Example:** data science — keeping a lab notebook entry after each experiment instead of rerunning it from
  scratch (name it, tie directly to the mission's own example: a one-line note like "Riley completed laser
  safety training on Nov 2," written once and reread at the next visit).
- **Practice:** "the assistant wrote a note about Riley's training status last week. This week, a student asks
  about booking. Is the note automatically in context, or does something have to fetch it?" Correct answer:
  something must fetch and insert it. Wrong answer targets "writing a note is enough."

### Common mix-ups (quick-fire, 300 words)
One idea: fire through the five misconceptions above as quick true/false or one-line prompts, each with the
one-line fix, reinforcing facts 1, 3, 4, 5, 6, 7, 8 already taught — no new facts.

### Worked example, then faded practice (700 words)
**Worked example:** trace the makerspace assistant end to end across two sessions.
- Session 1 (Monday): student asks "is the laser cutter free Friday?" — show what enters context (system
  prompt, tool defs), the tool call and result for the calendar check, the retrieval of one manual page for a
  safety rule, the booking, and the note the assistant writes afterward ("Riley: laser training incomplete").
- Session 2 (the next visit): show the fresh, empty context window at session start, and the note being
  retrieved back in because the student mentions the laser cutter again.

**Faded practice:** give the learner session 1 fully worked (as above) and the start of session 2. They fill in,
unaided: (a) what is in context at the very start of session 2, (b) what must be retrieved for the student's new
question, and (c) whether the booking made in session 1 is remembered and how. Solution revealed on demand.

### Summary, explain-back, go further, closing (300 words)
Three to five lines: context window = finite, shared, token-counted, per-call; within a session the loop keeps
appending; across sessions nothing survives unless saved; retrieval fetches the relevant saved piece on demand;
notes are memory the agent writes and someone must reread. Prompt: "explain to your teammate, in your own words,
why the makerspace assistant needs notes about training status even though its context window is huge." Point to
the primary source to read next, the other sources cited, and remind Riley they can ask follow-up questions in
chat and that a short quiz on this lesson is ready.

## Worked example and faded practice (summary for writer)

- **Task:** trace what is in context, what is retrieved, and what is noted, across two sessions of the
  makerspace assistant handling a laser-cutter booking and a later training-status check.
- **Fully worked:** session 1, start to finish (context contents, tool call/result, one retrieval, the note
  written at the end).
- **Faded for the learner:** session 2's starting context contents, what needs to be retrieved, and whether/how
  the earlier booking is remembered — the learner supplies all three with no steps given.

## Style notes for the writer (from PREFERENCES.md)

- Short paragraphs, one idea each; bullets are fine, no big blocks of text.
- Big picture and the "why" first in each section, then the analogy/example, then the check.
- Tone: casual and direct, no filler, a little genuine flattery (Riley just nailed the agent loop — say so).
- Every new term defined the first time it appears (context window, token, retrieval, compaction, note-taking).
- Feedback on every practice question: say plainly what is right, what is wrong with the reasoning, and how to
  fix it — not just right/wrong.
- Open with the win stated plainly and the mission tie-in; close with the primary source and the reminder that
  follow-up questions and a quiz are available.
- Link back to `learning-records/0001-what-a-language-model-does.md` and
  `learning-records/0002-the-agent-loop.md` material in the warm-up and in Section 2, since this lesson builds
  directly on both.

## Sources

**Primary source:** Anthropic, "Effective context engineering for AI agents" —
https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
(official vendor engineering guidance, directly on the context window, the agent loop, compaction, and
structured note-taking as memory).

**Other sources:**
- Redis, "LLM context windows: what they are & how they work" — https://redis.io/blog/llm-context-windows/
  (tokens, context-window sizing, cost, and the "lost-in-the-middle" accuracy effect).
- addyosmani/agent-engineer, "05-memory-and-context" README (GitHub) —
  https://github.com/addyosmani/agent-engineer/blob/main/05-memory-and-context/README.md
  (context window vs. memory distinction; within-session vs. cross-session storage; retrieval and
  summarization as memory strategies).
- Anthropic, "The components of agent memory" —
  https://www.anthropic.com/research/components-of-agent-memory
  (background on how agent memory is structured, for the writer's own reading before drafting).
- Claude Platform Docs, "Memory tool" —
  https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
  (a concrete, shipped example of notes-as-memory and just-in-time retrieval, for the writer's own reading).
