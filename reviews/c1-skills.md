# Reviews: c1-skills

Your quick rounds while you build `c1-skills`, and then its major review, once you have snapshotted it and made its full run.
In this step no round adds a subagent, because subagents arrive in `c2-review` and `c3-split`: a round changes or adds a skill, or makes another change the skills need, such as an allow rule (Kind `other`).
Your first round can start from the tutor as it ships, so the baseline is the output without your first change.
The major review covers all four jobs, and its previous step is `c0-baseline`, so compare with your baseline runs.
What it finds becomes the checklists of your reviewer subagents in `c2-review`, so be specific.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/c0-baseline/20261107-163908-agent-architecture-m30-r2, the baseline


**My thoughts:**

Going through the lesson I think it does simplify and teach context and memory well to a beginner with interactive texts and quizzes in the lesson. The quiz has questions that are distinguishably answered between a workflow and agent that someone with knowledge of a workflow and an agent would reasonably be able to answer.

I think the quiz questions could be shorter and slightly simplifed.  Additionally, the tutor replies should do better on meeting the expected behavior.

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/tutor/SKILL.md
- Why: You wanted the tutor replies to meet the expected behavior better, and the judge's notes on the baseline show three repeated misses (hints that sort or contrast quiz options and so settle the item, too-advanced questions answered in jargon with no plain explanation or next step, and replies over the length limit), so a tutor skill now handles chat replies with stricter rules for each.

### Round 2

**Run:** bench/runs/_live/20261107-183624-agent-architecture-m30-r1

**My thoughts:**

The new skill did not help the tutor, the replies got worse especialy when explaining things. In round 1 it explained to much and gave the asnwer away but in round 2 it didnt explain enough to be able to answer or help at all. Also, 2/6 were met and the other 4 were not met. I would like to expand the words, 200 at times seemed to short and really focus on the explination and make the explination more of a plane explination.

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/tutor/SKILL.md
- Why: You found the replies now explained too little and wanted more words and plainer explanations, so the limit goes from 200 to about 250 words, the plain explanation becomes the first and main part of every reply, and a request for a quiz answer now gets a concrete way to think through every option instead of a bare refusal.

### Round 3

**Run:** bench/runs/_live/20261107-185249-agent-architecture-m30-r1

**My thoughts:**

Round 2's helped in some ways and hurt in others. It allowed p04 to be met but p06 failed this time and the replies are about 300 words. I want a quiz skill. 

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/quiz/SKILL.md
- Why: You asked for a quiz skill, and in Round 1 for shorter, simpler quiz questions, so the new quiz skill caps stems at about 30 words and options at about 12, asks for plain words at the learner's level and one idea per item, and checks the length and the spread of answer letters before it finishes.

### Round 4

**Run:** bench/runs/_live/20261108-215423-agent-architecture-m30-r1


**My thoughts:**

The question lengths have decreased which is good. One thing I would like to change is reduce the amount of misconseptions the person has so make sure to explain very clearly what their misconseption is and why it is wrong 

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/grade/SKILL.md
- Why: You wanted fewer misconceptions to stick, with each one explained very clearly, what it is and why it is wrong, so the new grade skill's feedback on every answer that shows a misconception states the wrong idea plainly from the learner's own answer, explains why it is wrong and what is true instead, and says how to avoid it next time.

## Major review

**Run:** bench/runs/c1-skills/20261109-003401-agent-architecture-m30-r1

**Live tries:**

The lesson was completed quickly, it has sources and images, it gave me the information that it needed and taught me abouty cats body languages. The tutor corrected my misconseption and told me it was a misconception using information from the lesson. The quiz was clean and told me very clearly what I got right and what I got wrong and where/why.I was wrong. The whole process taught, quizzed, and graded me on things.

### Lesson

#### Technical correctness and facts

Rating: 4

The lesson was all very technically correct and it had sources. I gave it a very broad topic and it narrowed it down fro me then taught me multiple different aspects about the topic.

#### Pedagogy

Rating: 3

The method to teach was very straight forward, it gave the facts and information without a lot of fluf.

#### Alignment with the learning goal

Rating: 5

It did not go over random things and stuck to the topics with both questions, images, paragaphs, and information. It taught me what I needed to know.

#### Overall quality

Rating: 4

The lesson did what it was intended to do and taught me about cats in a very simple way. It has had multiple different interactive things with questions on teh topics so it not only taught you but allowed you to try to test your knowledge as well.

### Quiz

#### Difficulty

Rating: 4

The quiz had questions that were directly asked in the lesson but it wasnt to difficult and if I completed the lesson it was 100% doable.

#### Coverage of the lesson's core

Rating: 4

I think the quiz did really well at covering what the lesson taught, if I completed the lesson the quiz was 100% doable.

#### Wording and possible misreadings

Rating: 1

I think the possible misreading was low it was very easy to read and understand, plus it matched really well with the lesson so if you did the lesson it was harder to misread the questions.

#### Writing quality

Rating: 4

The quiz was straight forward and easy to understand without misspellings or incorrect information so I think teh writing quality was good.

#### Alignment with the learning goal

Rating: 5

It quizzed you just on stuff about the lesson which is what it was supposed to do and stayed on topic.

### Feedback

#### Useful

Rating: 4

It told me when I was incorrect, told me why, and correct my misconseption

#### Explains enough

Rating: 4

It had a good paragrpah telling me why I was incorrect without making it to long.

#### Personalized to how I like things explained

Rating: 3

It was straight forward and told me why I was incorrect with some "you were close" so it wasn't completely just like you were wrong

### Tutor

#### Guardrails

Rating: 4

When asking it a misconception it corrected me and explained why I was incorrect. Additionally when asking it to tell me the answer on a quiz it said it could not then explained it to me.

#### Personalization

Rating: 3

I am not sure it was necessarly personalized, it was striaght forward and told me what I needed to know and not know which was good.

### Compared with the previous step

The previous step was the baseline so I am not sure how much that has changed but this one was far more interactive than the baseline with more personalization and stricker word counts and ways to answer question

### What the next step should fix

I want to change the quiz so that it makes sure that no quiz questions directly from the lesson word for works.
