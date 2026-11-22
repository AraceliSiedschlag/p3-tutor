# Lesson plan: O3 - Planner/writer split in agent systems

Objective id: O3
Objective text: Understand how a planner and a writer split work inside an agent system — why an agent separates the "decide what to do and in what order" step (planning) from the "produce the actual output" step (writing), what each role is responsible for, and what goes wrong when they aren't separated.
Requested length: 5 minutes
Word budget: 750 words (150 words/minute x 5)

Note on mission fit: `MISSION.md` (cat body language) and `NOTES.md`/`learning-records/` do not cover agent architecture, so this objective sits outside the current mission's prior material. There is no earlier lesson or learning record to warm up from. Examples below are drawn from `PREFERENCES.md`'s "Examples I relate to" (IT work, cooking, data science) instead, since those are the closest fit to this objective's content.

## The win

By the end of the lesson the learner can look at any agent (including this very tutor's lesson-planner/lesson-writer setup) and say, correctly, which parts are "planning" and which are "writing," and name one concrete failure that happens when a system skips the split.

## Core facts (numbered, each with its source)

1. A plan-and-execute (planner/writer) architecture splits an agent's work into two distinct steps: a planner that decides what to do and in what order, and an executor/writer that produces the actual output for each step. — https://www.langchain.com/blog/planning-agents
2. The planner reasons about the whole task up front, breaking a big goal into an ordered sequence of sub-steps and accounting for dependencies between them, before any output is produced. — https://www.langchain.com/blog/planning-agents ; https://tianpan.co/blog/2026/04/09/agent-planning-module-hidden-architectural-seam
3. The writer/executor works at the step level: it only needs the context for its one assigned step, not the whole task, and turns that step into concrete output (text, a tool call, a file). — https://tianpan.co/blog/2026/04/09/agent-planning-module-hidden-architectural-seam
4. Because the planner is consulted once up front rather than before every single action, a split system runs faster and cheaper than one that interleaves deciding and producing on every step (a ReAct-style agent needs a model call per tool use). — https://www.langchain.com/blog/planning-agents
5. Without separation, a system that decides and produces output in the same step tends toward "greedy" choices: it picks whatever looks good for the very next action rather than the best plan for the whole task, and this derails complex tasks at a high rate. — https://tianpan.co/blog/2026/04/09/agent-planning-module-hidden-architectural-seam
6. Without separation, mistakes and irrelevant detail pile up in the single stream of context ("error self-conditioning" and "context rot"), so accuracy drops the longer an unseparated agent runs. — https://tianpan.co/blog/2026/04/09/agent-planning-module-hidden-architectural-seam
7. A plan-and-execute system can replan: after a step runs, the planner reassesses and decides whether to finish or issue a new plan, which is possible only because planning is a separate, revisitable step rather than something baked into each action. — https://www.langchain.com/blog/planning-agents
8. Splitting the roles lets each specialize: the planner can be a stronger, slower reasoning pass, while the writer/executor stays simple and focused only on producing output for its one step (and can even be a smaller, cheaper model). — https://www.langchain.com/blog/planning-agents ; https://www.comet.com/site/blog/plan-and-execute-agents-in-langchain/

## Misconceptions

- "The planner should just write the final output itself, since it already knows the whole task." Tempting because the planner does hold the big picture, so skipping the hand-off feels like saving a step; wrong because mixing the two jobs produces the myopic, error-compounding failures in facts 5-6.
- "Writer needs the whole task's history to do a good job on its step." Tempting because more context feels like it can only help; wrong because a crowded context causes "context rot" (fact 6) and the writer only needs its own step's inputs (fact 3).
- "The split is just an optimization for speed and cost, not something that changes the quality of the result." Tempting because the sources mention speed and cost gains first; wrong because an unseparated loop also produces lower-quality, more easily derailed output (fact 5), independent of cost.
- "Planning and execution have to happen in parallel, by two different systems running at once." Tempting because "split" sounds like it means simultaneous; wrong because the split is about distinct steps/calls in sequence (plan, then execute, then maybe replan), not concurrency.

## Section plan (750 words total)

| # | Section | Idea | Words | Facts | Example | Practice question + misconception targeted |
|---|---|---|---|---|---|---|
| 1 | Opening: the win | State the win and why it matters: every agent you build or use (including this tutor) makes this split somewhere | 60 | - | none yet | none |
| 2 | What the planner does | The planner's one job is deciding the ordered steps for the whole task, before any output exists | 150 | 1, 2 | IT help desk: a dispatcher who reads all open tickets and sets the order and who handles which, without touching any ticket themselves | MC: "Which of these is the planner's job?" (write the reply vs. decide the order) — targets "planner should just write the output itself" |
| 3 | What the writer does | The writer's one job is turning one step into real output, using only that step's info | 130 | 3, 8 | Cooking: the line cook who gets one ticket ("plate the salad") and only needs that order, not the whole night's menu | MC: "What does the writer need to do its job?" (whole task history vs. just its one step) — targets "writer needs the whole history" |
| 4 | Why the split pays off | Separating the two steps makes the system faster, cheaper, and able to replan, because the planner isn't re-run on every action | 140 | 4, 7 | Data science: a project lead who plans the pipeline once instead of re-approving every line of code a teammate writes | MC: "The split mainly exists to..." (save money only vs. also to keep output coherent) — targets "it's just a speed/cost trick" |
| 5 | What goes wrong without it | A system that decides-and-produces in the same step picks myopic next actions and drowns in its own accumulated mistakes | 140 | 5, 6 | IT help desk again: an engineer who grabs whatever ticket looks easiest right now instead of following the dispatcher's order, and derails the migration | T/F: "An agent with no separation just runs a little slower, but gets the same answer." (False) — targets "split is only about speed, not correctness" |
| 6 | Worked example, then faded practice | Walk through planning + writing one small job, then hand the learner a similar job with steps faded | 90 | all | Worked: planning and writing a 3-step help-desk fix (planner: order the 3 tickets; writer: resolve ticket 1). Faded: learner is given the plan for a 3-step cooking task and writes just the "writer" output for step 2, with step 1 modeled | Immediate feedback: show the modeled step 1, then check the learner's step 2 against "did it decide anything, or just produce the step's output?" |
| 7 | Summary + close | Recap in 3-4 lines: planner decides order, writer produces output per step, separation beats mixing them, replanning depends on keeping planning separate | 40 | - | none | none |

Total: 60+150+130+140+140+90+40 = 750 words.

## Worked example and faded practice

- **Worked example:** A 3-ticket help-desk job. Show the planner's output (an ordered list of 3 tickets with one dependency noted) and then the writer's output for ticket 1 (the actual reply/fix), making explicit that the writer only saw ticket 1's description, not the other two.
- **Faded practice:** Give the learner the planner's output for a 3-step cooking task (already decided: order, dependencies) and the writer's step 1 (modeled in full). The learner writes the writer's output for step 2 only, using only step 2's description. Steps left to the learner: producing the step-2 output and noticing, unprompted, that they should not need step 3's details to do it. The modeled step 1 stays visible as the pattern to follow.

## Style notes for the writer (from PREFERENCES.md)

- Short paragraphs, one idea per paragraph, no big blocks; bullets are fine where they help.
- Casual and direct, straight answers, no filler, a touch of flattery is welcome (the learner likes it).
- Big picture and the "why" first in each section, then an analogy/example, matching "How I like things explained."
- Feedback on practice questions: say plainly what is right, what is wrong with the reasoning, and how to fix it (not just right/wrong).
- Open with the win in one sentence; close with the primary source and a reminder that follow-up questions and a short quiz are available.
- Since this objective falls outside the cat mission, say so briefly in the opening (one sentence) so the learner isn't confused about why the topic shifted, then move straight into the content.

## Sources

- Primary: LangChain, "Plan-and-Execute Agents" — https://www.langchain.com/blog/planning-agents (official vendor documentation of the architecture, clearest statement of planner/executor responsibilities and the speed/cost/quality rationale).
- TianPan, "The Agent Planning Module: A Hidden Architectural Seam" — https://tianpan.co/blog/2026/04/09/agent-planning-module-hidden-architectural-seam (failure modes without separation: greedy myopia, error self-conditioning, context rot).
- Comet, "Plan-and-Execute Agents in Langchain" — https://www.comet.com/site/blog/plan-and-execute-agents-in-langchain/ (planner/executor role descriptions, specialization argument).
- LangChain blog (second result, same architecture family) — https://www.langchain.com/blog/plan-and-execute-agents (corroborates replanning step and token savings figures).
