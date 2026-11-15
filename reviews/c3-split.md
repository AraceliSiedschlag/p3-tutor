# Reviews: c3-split

Your quick rounds while you split up the teach job, and then the major review of `c3-split`.
Add one subagent of the teach pipeline per round, so the run before it shows the lesson without it and the run after it shows the lesson with it.
The major review covers the lesson only, and its previous step is `c2-review`.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/c2-review/20261111-011240-agent-architecture-m30-r1

**My thoughts:**

The length of the lesson was short at 0.74, facts decreased, and there was nothing from my preferences.

Add a planner subagent in order to increase personlization and accuracy. The planner subagent can help meet word count requirements and use more things from the preferences.md, and shorten long paragraphs. The planner agent could make sure the needed facts were met as well.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-planner.md, tutor/.claude/skills/teach/SKILL.md
- Why: The lesson came in short at 0.74, missed a fact and used nothing from your preferences, so a lesson-planner subagent now researches the objective first and writes a plan with every core fact and its source, one-idea sections whose word budgets add up to the requested length, an example from your PREFERENCES.md and a practice question for each, and short-paragraph style notes, and the teach skill writes the draft section by section to that plan.

### Round 2

**Run:** bench/runs/_live/20261114-002653-agent-architecture-m30-r1


**My thoughts:**

The lesson score barely moved. The length ratio increased for two points, the cost was less by 10 cents but incrased to 5.92 Million tokens. The length decreased by around 5 min though which was good. It was still missing a fact the same one as c2. Personalization imporved a little but most examples are still makerspace. Next, add a writer subagent that targets length, following the plan, and short paragraphs.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-writer.md, tutor/.claude/skills/teach/SKILL.md
- Why: The lesson still came in short at 0.76 of the plan's budget and needed paragraphs split, so a lesson-writer subagent now writes the draft from the plan one section per edit, each to its word budget (writing to the top of it when unsure), with the plan's facts, examples and practice questions and no paragraph over three sentences, and reports each section's words against its budget; the teach skill no longer writes the lesson itself.


### Round 3

**Run:** bench/runs/_live/20261114-173117-agent-architecture-m30-r1



**My thoughts:**
With the planner and the writer the length ratio increased to 0.90, the heighest every, but the facts present and correctness decreated to 4/6. The time increased to 30 min and increased the token usage to 0.04M tokens and increased the cost to $6.27 with 1 shell denials. It also drew multiple examples from the preference options. Next, I want teh reviwers on topic check cut a fact the plan sadi the lesson needed but it sholdnt remove the plans core facts.

**What changed:**

- Kind: other
- Files: tutor/.claude/agents/lesson-reviewer.md, tutor/.claude/skills/teach/SKILL.md
- Why: The reviewer's on-topic check cut a core fact the plan said the lesson needed, so the lesson-reviewer now reads the plan, treats its core facts as on topic, never asks to cut one and reports any it finds missing, and the teach skill passes it the plan and never cuts a core fact to fix a finding, giving it its own paragraph or section instead.


## Major review

**Run:** bench/runs/c3-split/20261114-220703-agent-architecture-m30-r1


**Live tries:**

The lesson ran in 20 min, which might have been due to me saying make a five min lesson, and had two examples relevant to my preferences md, it had more than three questions. It was very clear to read and understand. However, this was more money and time than the others but it seems worth it for it to better meet the length requirements and personalization

### Lesson

#### Technical correctness and facts

Rating: 5

It seemed correct and like it dumbed down what was going on really well

#### Pedagogy

Rating: 5

It used prefrence.md much more than any other one I have done for my live trials with three difference examples and pullings from my analogy options. This was the first time that I have seen this during a live trial.

#### Alignment with the learning goal

Rating: 5

It created and presented a lesson that was on topic and taught about what I asked of it.

#### Overall quality

Rating: 5

I think that the teacher performed it job with the lessons presenting facts, clarity, questions while reading directly from the preferences.md.

### Compared with the previous step

Compared to the previous step this costs more but the timeing decreased from earlier steps but is still greater than c2, it cost more token, but it applies the preference.md much better than any other trial that I have done.

### What the next step should fix

I would work on making sure that facts are correct and making sure that the tutor successfully passed more probes than 2/6.
