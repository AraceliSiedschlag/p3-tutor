# Lesson plan: O3 — Context and memory in an agent

Objective: "Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory."
Requested length: 30 minutes. Word budget: 150 × 30 = **4,500 visible words**.

## The win

By the end, Riley can trace one makerspace-assistant request and say, for every piece of information involved, whether it lives in the context window for that call, gets resent on the next step, survives only if saved to a file, or is pulled in on demand by retrieval — and use that to decide what the assistant must save between visits.

## Core facts

1. The context window is every token the model processes for one call — system prompt, message history, tool definitions, and tool results — and it is the model's only "working memory" for that call; nothing outside it exists to the model at that moment. — https://platform.claude.com/docs/en/build-with-claude/context-windows
2. Within one session, each new step re-sends the entire accumulated history (every prior turn and tool result) as input; the model itself does not retain anything between calls, the program just appends and resends. — https://platform.claude.com/docs/en/build-with-claude/context-windows
3. The context window has a fixed token size, and past a point, stuffing more in does not help: recall accuracy degrades as the token count grows, an effect called "context rot," so curating what's included matters as much as how much room there is. — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
4. Nothing persists automatically between sessions: when a new session starts, the context window is empty again, so anything the assistant must remember has to be written to storage outside the model and loaded back in. — https://www.helix-db.com/content/guides/llm-memory-architecture-how-agents-remember-across-sessions ; corroborated at https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
5. Retrieval is fetching a specific piece of an external source — a page of a manual, a calendar row — into context only when it's needed ("just-in-time"), instead of keeping the whole source loaded all the time. — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
6. Notes (structured note-taking / memory files) are information the agent itself writes to persistent storage — like a to-do list or a status file — specifically so a later step or a later session can read it back and continue. — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents ; mechanics at https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
7. Retrieval and notes work the same way mechanically — both pull saved text back into the context window as a tool result — but they differ in where the content came from: retrieval reads a source that already existed (the manual), notes read something the agent itself recorded earlier (a status it observed). — https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
8. Every token in the context window, whether history, a retrieved chunk, or a loaded note, counts against the same size limit and the same per-token cost, so what the assistant keeps in context at each step drives both whether it gets the right answer and what the request costs. — https://platform.claude.com/docs/en/build-with-claude/context-windows

## Misconceptions

- **The model "remembers" things it's told, the way training works.** Tempting because the chatbot visibly uses what you just said, so it feels like it learned it. In fact it only has that text because it's sitting in the current context window; the model's weights never change mid-conversation (builds on learning record 0001: training knowledge is fixed, everything else is "what's in the text it is given").
- **A new session should remember the last one, like a phone call you can pick back up.** Tempting because within a single session, history clearly carries forward turn to turn, so it feels continuous. Between sessions the context window resets to empty; continuity only happens if something explicitly saved state to a file and a later session reads that file.
- **Retrieval and notes are basically the same feature.** Tempting because both show up as a tool call that returns text into context, and the learner has not yet distinguished them. The difference is the source: retrieval reaches an existing external document (the manual), notes are the agent's own record of something it saw or decided.
- **A bigger context window means the assistant can just keep everything in it and skip memory design.** Tempting because more room sounds like fewer limits. Recall degrades as the window fills (context rot), and every extra token costs money, so even a 1M-token window still rewards deciding what belongs in context versus what should be retrieved or noted on demand.

## Section plan (4,500 words total)

| # | Section | Words |
|---|---|---|
| 1 | Opening + warm-up | 300 |
| 2 | A: The context window is working memory for one call | 500 |
| 3 | B: What's kept between steps — the history gets resent, not remembered | 450 |
| 4 | C: Why fuller isn't free — context rot and cost | 500 |
| 5 | D: What's kept between sessions — nothing, unless it's saved | 500 |
| 6 | E: Notes — the agent's own saved state | 500 |
| 7 | F: Retrieval — pulling in an external source just in time | 450 |
| 8 | G: Retrieval vs. notes, side by side | 400 |
| 9 | Worked example + faded practice | 600 |
| 10 | Summary + explain-back prompt | 200 |
| 11 | Go further + closing | 100 |
| | **Total** | **4,500** |

### 1. Opening + warm-up — 300 words
State the win above and tie it to the mission: the makerspace assistant has to answer from long manuals it can't hold in full, and remember each student's training status across visits, days apart.
Warm-up (answers revealed on demand): recall from learning record 0001 ("what does the model know, besides what training gave it?") and learning record 0002 ("what repeats in the agent loop until it stops?").
No new core fact; sets up why context and memory matter.

### 2. Section A — the context window is working memory for one call — 500 words
**Idea:** everything the model sees for one call — system prompt, messages so far, tool results, tool definitions — is the context window, and nothing else exists to the model at that moment.
**Facts taught:** 1.
**Example:** IT support ticket — a technician can only act on what's pasted into the current ticket thread, not the whole company wiki, unless someone pastes a snippet in; the makerspace assistant can only act on what's in its current call, not the whole manual library, unless a chunk of it is placed there.
**Practice:** a short scenario ("the assistant is mid-call; which of these is in its context window right now: the system prompt, yesterday's conversation, next week's maintenance schedule?") with immediate feedback distinguishing "in context now" from "exists somewhere but not loaded."

### 3. Section B — what's kept between steps: resent, not remembered — 450 words
**Idea:** within one session, each new step's input is the full history so far, appended and resent by the program; the model has no memory of its own between calls.
**Facts taught:** 2.
**Example:** IT support — a reply-all email thread where every new message carries the full quoted history below it; nothing is "remembered," it's just quoted in again. The makerspace assistant resends the student's question, the tool call it made, and the result, every single step.
**Practice:** scenario — the assistant looks up the laser cutter's free slot, then answers a follow-up about the same slot. Question: does it answer correctly because it remembers the lookup, or because the lookup's result was resent as text? Targets the "model remembers" misconception; feedback explains the resend.

### 4. Section C — why fuller isn't free: context rot and cost — 500 words
**Idea:** the context window has a fixed size, and recall gets worse, not better, as it fills — plus every token costs money — so what goes in matters more as the budget shrinks.
**Facts taught:** 3, 8.
**Example:** cooking — a countertop crowded with every spice jar in the house makes it harder to find the salt than a counter with just today's ingredients out; a cluttered context window makes it harder for the model to find the one fact it needs.
**Practice:** "the assistant's context has grown to include six past students' entire conversations. Will adding more of today's manual pages on top make today's answer more reliable, less reliable, or no different?" Targets the "bigger/fuller is better" misconception; feedback ties to context rot and token cost.

### 5. Section D — what's kept between sessions: nothing, unless saved — 500 words
**Idea:** a new session starts with an empty context window; anything from an earlier session only comes back if it was written to storage and that storage is read back in.
**Facts taught:** 4.
**Example:** IT — rebooting a computer clears what was in RAM; only what was saved to disk survives the restart. A new chat session is a reboot of the model's working memory; only what the assistant wrote to a file survives.
**Practice:** "A student asks about the drill press on Monday, in one session. On Wednesday they open a new session and ask a follow-up. Does the assistant still have Monday's conversation unless something was done to save it?" Targets the "sessions carry over automatically" misconception; feedback states the reset plainly.

### 6. Section E — notes: the agent's own saved state — 500 words
**Idea:** notes are text the agent itself writes to a file (or similar storage) outside the context window, specifically so a later step or session can read it back and pick up where it left off.
**Facts taught:** 6, 7 (the "comes from the agent itself" half).
**Example:** cooking — a kitchen journal entry after a bake ("ran out of flour, substituted X, came out dense") that you reread before the next bake; the makerspace assistant writes "Priya passed laser training on Nov 10" to a student-status file and rereads it the next time Priya asks to book the laser cutter.
**Practice:** "After the assistant writes that note and the session ends, is the fact now part of the model's trained knowledge, usable for any future question without opening the file?" Targets the "model remembers/learns" misconception directly; feedback: no, it is only a file, and must be read back in to matter again.

### 7. Section F — retrieval: pulling in an external source just in time — 450 words
**Idea:** retrieval fetches one specific piece of a large existing source into context only when it's needed, instead of keeping the whole source loaded all the time.
**Facts taught:** 5.
**Example:** data science — querying a database for one row instead of loading the whole table into memory; the makerspace assistant fetches page 42 of the drill press manual for the torque spec, not the entire manual.
**Practice:** "Should the assistant keep the full 80-page manual in context on every call, or fetch just the relevant page when a question needs it?" Targets the "more loaded context is more thorough/accurate" instinct; feedback ties back to context rot and cost from section C.

### 8. Section G — retrieval vs. notes, side by side — 400 words
**Idea:** retrieval and notes both return text into the context window through a tool call, but they differ in where that text came from: retrieval reads something that already existed, notes read something the agent itself recorded.
**Facts taught:** 5, 6, 7 (stated together as the contrast).
**Example:** IT — looking up the company's existing password-reset policy page (retrieval) versus writing a note in a ticket for the next technician ("customer prefers callbacks after 5pm") (notes); both get read back later, but one already existed and one didn't until the agent wrote it.
**Practice:** multiple-choice — "the assistant needs the drill press's torque spec. Should it (a) keep the whole manual in context every turn, (b) retrieve just that page when asked, (c) write a note guessing the number from memory?" Targets both the "load everything" misconception (a) and the "notes replace retrieval" confusion (c); feedback explains why (b) is the only one that's both accurate and cheap.

### 9. Worked example, then faded practice — 600 words
**Worked example:** trace one full request end to end — a student asks, in one session, "is the laser cutter free Friday, and am I trained on it?" Step by step, label each piece: the question (context), the tool call to the booking calendar (retrieval), the result (now in context, resent on the next step), the tool call to the student's training-status file (retrieval of a note written earlier), the final answer. Then show session two, days later: the context window opens empty; the assistant must read the training-status file again before it can answer "can I still book Friday?" — nothing from session one is there unless it was saved.
**Faded practice:** a parallel scenario — a student asks to book the 3D printer and also asks whether they finished their printer-safety module. Steps 1 and 2 are given (the question arrives; the assistant checks context for anything already known). The learner fills in the rest: which step is a retrieval call, which step is a note being read, what happens if this becomes a new session the next day. Solution revealed on demand.

### 10. Summary + explain-back prompt — 200 words
Three to five lines: the context window is the model's working memory for one call; within a session the whole history gets resent each step; across sessions nothing survives unless it was saved; retrieval pulls in an existing source on demand, notes are what the agent saved itself, and both cost the same tokens as everything else in context.
Prompt: "In your own words, tell me what the makerspace assistant needs to save to a file so it still knows a student's training status next week."

### 11. Go further + closing — 100 words
Primary source link (Anthropic's context engineering article) to read next, the two or three other sources cited, and a one-line pointer to a community (skip if NOTES.md ever says otherwise — it currently says nothing against one; a brief note that r/LocalLLaMA or an agent-framework's Discord is a place to see these patterns discussed, kept optional).
Closing: a reminder Riley can ask follow-up questions in chat, and that a short quiz on this lesson is ready when they are.

## Style notes for the writer (from PREFERENCES.md)

- Open with the big picture and the why, then analogies and concrete examples — in that order, every section: idea first, then the example, not the reverse.
- Short paragraphs, one idea each; bullets over big blocks wherever a list is natural (e.g., the context-window contents, the retrieval-vs-notes contrast).
- Every new term (context window, token, context rot, retrieval, notes) defined in plain words right where it first appears.
- A worked example for anything new, as required by preferences, which is why section 9 carries one before the faded practice.
- Tone: casual and direct, no filler, a little flattery is welcome ("you've already got the agent loop down, this builds right on it").
- Draw on cooking, IT support, and data-science/database analogies for examples, since those are what Riley relates to; keep every example tied back to the makerspace assistant from MISSION.md.
- Close each section's practice with feedback that says plainly what's right, what's wrong in the reasoning, and how to fix it, per PREFERENCES.md's feedback style.
- Open the lesson with the win; close it with the primary source and the reminder that Riley can ask questions and a quiz is ready.

## Sources

**Primary:** Anthropic, "Effective context engineering for AI agents" — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

**Others:**
- Anthropic, "Context windows" (Claude Platform Docs) — https://platform.claude.com/docs/en/build-with-claude/context-windows
- Anthropic, "Memory tool" (Claude Platform Docs) — https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
- LangChain, "Context Engineering for Agents" — https://www.langchain.com/blog/context-engineering-for-agents
- Helix DB, "LLM Memory Architecture: How Agents Remember Across Sessions" — https://www.helix-db.com/content/guides/llm-memory-architecture-how-agents-remember-across-sessions
