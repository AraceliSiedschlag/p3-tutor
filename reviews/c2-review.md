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

**Run:** bench/runs/c2-review/20261111-011240-agent-architecture-m30-r1

**Live tries:**

It created the lesson it felt longer than the other runs, which is was, and it said when it was being reviewed. The lesson was accurate, had facts, and interactive questions. The quiz had good questions related to the topic that were not to long nor confusing. The grading graded it accurately with feedback.

### Lesson

#### Technical correctness and facts

Rating: 5

The lesson once again had facts, questions, and interactive questions for the user. It did take longer to build though. 

#### Pedagogy

Rating: 4

The pedagogy was straight forward and taught the person what they needed to know.

#### Alignment with the learning goal

Rating: 5

It successfully taught the users about the desired topic.

#### Overall quality

Rating: 5

It was intreactive, informative, and taught the user what they wanted so I think it was a good lesson.

### Quiz

#### Difficulty

Rating: 2

The difficulty was moderate and seemed appropriate for a quiz and for the lesson taken.

#### Coverage of the lesson's core

Rating: 4

The quiz covered the lesson core and specifics to dog training which was good but some of them seemed slightly repetative just using different senarios but same concepts.

#### Wording and possible misreadings

Rating: 1

All questions were clear and easy to interpret and understand what they were asking.

#### Writing quality

Rating: 5

The writting was easy to understand and read. All mcq answers were similar lengths so it didnt give one answer away.

#### Alignment with the learning goal

Rating: 4

It allowed the user to get tested on aspects of dog trianing but some seemed like similar learning targets than hitting multiple of them.

### Feedback

#### Useful

Rating: 4

It clearly showed what I got write and what I got wrong by listing it out, but for two question I got partial credit and they did did not tell me why and only explained the completely wrong questions.

#### Explains enough

Rating: 2

It did not explain the questions I got partially correct only the ones I got fully wrong. 

#### Personalized to how I like things explained

Rating: 4

It did not give any analyogies that were connected to my personalization but it did follow the structure requested.

### Compared with the previous step

The previous step had a better tutor skill that passed more probes (2/6) where as the tutor this time passed less (1/6) dropping 0.17 points but nothing was editted so this is run to run varaiation. The others stayed where they were at perfect Teach facts also decreased compared to the last one only hitting 5/6 facts rather than 6/6. The length ration also decreased from 0.83 to 0.74 in c2-review. Quiz and grade scores stayed the same off 100% on grade verdics, 0% on false wrongs and 100% on misconceptions hit in both reviews with 100% quiz key agreement, 0 wrong key, nd 0 ambiguous items. Additionally, this run took 61.5 min, 9.45 M tokens, and $11.88, where as c1-reviewer took 21.8 min, 7.93M tokens and $6.12. 

### What the next step should fix

Work to improve the tutor skill so that it passes more than 2 probes. Expand gradings word count becasue it felt a bit lean when I got things incorrectly. Make sure the quiz cover different topics not just the same topic with different senairos or wording. Have grader explain what the user got partially correct and what was incorrect about their statement.
