# Reviews: c2-review

Your quick rounds while you build the review loops on teach, quiz and grade, and then the major review of `c2-review`.
Add one reviewer subagent per round, so the run before it shows the output without it and the run after it shows the output with it.
The major review covers the lesson, the quiz and the feedback, and its previous step is `c1-skills`.
Say in it whether the problems your `c1-skills` review found are gone.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/c1-skills/20261109-003401-agent-architecture-m30-r1, the c1-skills full run

**My thoughts:**

The quiz should not copy the quiz word for word from the lesson. The quiz answers should not be reviewed, the grader should explain what they did wrong, where it was, and how to correct it. The word count for thr quiz should not go over 50 words per questions. The teach should have at least 3 interactive questions baised on the lesson.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/quiz-reviewer.md, tutor/.claude/skills/quiz/SKILL.md
- Why: You want quiz questions that never copy the lesson word for word and never run over 50 words, so a quiz-reviewer subagent now reads each draft with a fresh context against a checklist led by those two checks, and the quiz skill revises from its findings for at most two passes before writing the final quiz.

### Round 2

**Run:** bench/runs/_live/20261110-214959-agent-architecture-m30-r1

**My thoughts:**

The cost was significantly more growing from $0.67 to $1.62 and went from 3.5 min to 10.5 min. It does help to hide the answer by not making it the longest one so it is not obvious. The grade reviewer is next and should make sure to note what they got correct, what they got wrong and what their miconseption is if they got something incorrect. They should never go over 150 words, or give out the answers it should check if the feedback is helpful for the question or if it explains the root issue. It should also give positive feedback in incorrect written responses. 

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/grade-reviewer.md, tutor/.claude/skills/grade/SKILL.md
- Why: You want feedback that says what was right and wrong, names the misconception and its root issue, stays under 150 words, does not just hand over the answer, and finds something positive in wrong written answers, so a grade-reviewer subagent now checks each draft of the grades for exactly those, and the grade skill revises from its findings for at most two passes before writing the final grades.


### Round 3

**Run:** bench/runs/_live/20261110-223454-agent-architecture-m30-r1

**My thoughts:**
Accuracy held at 1.00, no right answers were marked wrong and the misconception was named every time. It took 16.8 min vs 3.4 min 1.98 M tokens and $2.89 vs $0.87 dollars with 4 subagents. It also took 8 min against its 15 min limit. The grade reviwer doesnt seem worth the substantially larger price. For the teach reviewer I would like three interactive questions at least and verifying it is on topic.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-reviewer.md, tutor/.claude/skills/teach/SKILL.md
- Why: You want every lesson to have at least three interactive questions and to stay on topic, so a lesson-reviewer subagent now reads each lesson draft in four separate reviews (correctness and facts, pedagogy, alignment, overall quality), with those two as must-fix and on-topic checks, and the teach skill revises from its findings for at most two passes before writing the final lesson.

## Major review

**Run:** bench/runs/c2-review/TODO

**Live tries:**

TODO

### Lesson

#### Technical correctness and facts

Rating: TODO

TODO

#### Pedagogy

Rating: TODO

TODO

#### Alignment with the learning goal

Rating: TODO

TODO

#### Overall quality

Rating: TODO

TODO

### Quiz

#### Difficulty

Rating: TODO

TODO

#### Coverage of the lesson's core

Rating: TODO

TODO

#### Wording and possible misreadings

Rating: TODO

TODO

#### Writing quality

Rating: TODO

TODO

#### Alignment with the learning goal

Rating: TODO

TODO

### Feedback

#### Useful

Rating: TODO

TODO

#### Explains enough

Rating: TODO

TODO

#### Personalized to how I like things explained

Rating: TODO

TODO

### Compared with the previous step

TODO

### What the next step should fix

TODO
