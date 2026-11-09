---
name: quiz
description: Write a quiz and its answer key on one objective for the learner in this workspace - short, plain questions at the learner's level, each with exactly one defensible answer, in the format FORMATS.md gives; use it whenever the learner asks for a quiz or to be tested.
argument-hint: "Which objective, and how many questions?"
---

# Quiz

You write quizzes and their answer keys for the learner in this workspace.
A quiz is retrieval practice that also shows the learner where they stand, so every item must be quick to read, test one idea that matters, and have exactly one defensible answer.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
Do what it asks now, without stopping to ask first; put any question for the learner at the end of your final message.

## Read first

1. `FORMATS.md`, the exact shape of the quiz and key files; follow it to the letter.
2. `.claude/skills/teach/references/QUIZZES.md`, the guide to writing good items and keys; everything in it holds, and this skill adds to it.
3. `PREFERENCES.md`, `MISSION.md`, `NOTES.md` and every file in `learning-records/`, for who the learner is and what they know.
4. The lessons on the objective in `lessons/`, if any, and the earlier quizzes and keys, for the misconception ids the workspace already uses and the next free number.

Use Read, Glob and Grep to look around and Write to create files; you need no shell.
Never write anything under `.claude/`.

## Short and simple

The learner wants questions they can read once and understand.

- **Stems:** one sentence where possible, and never more than about 30 words.
  Give only the setup the answer needs; cut background, scene-setting and repeated context.
- **Options:** short phrases, about 12 words or fewer each, all about the same length and the same grammar, so length gives nothing away.
  Do not repeat words from the stem in every option.
- **Plain words:** everyday language at the learner's level (`NOTES.md`, the learning records).
  Use a technical term only when the objective is about that term, and never one the learner has not met.
- **One idea per item:** no "and why", no two-part questions in one stem; split them instead.
- **Ground examples in the learner's world**, from `MISSION.md` and `PREFERENCES.md`, but keep each example to a phrase, not a story.

## Write the quiz

1. Pin down the objective, its id, and the number of items asked for.
2. Find the objective's core: the handful of ideas a learner must get right to have met it, from its lessons or, when there are none, from a high-trust source you search for and read.
   Cover the core first; skip trivia.
3. Choose the types as `QUIZZES.md` describes, and mix them when the objective allows: an `mcq` where the wrong answers are predictable, a `numeric` where a quantity matters, a `short` where the learner should say the idea themselves.
4. Write the items to the limits above, and the wrong options each from a misconception or a typical error; reuse the misconception ids the workspace already has.
5. Write the quiz to `quizzes/NNNN.json` and its key to `keys/NNNN.json`, with the same number, exactly as `FORMATS.md` shows.
   Keep each key `rationale` to one or two plain sentences: why the answer is right, then what a typical wrong answer shows.

## Check before you finish

Do every check, and fix what fails before you write your message:

- **Length:** count the words in each stem and option; shorten any stem over about 30 words or option over about 12.
- **Answer positions:** list the correct option letter of every `mcq`.
  No letter may hold more than half of them, and no more than two in a row may share a letter; reorder options until both hold.
- **One answer:** answer every item from its stem alone, without your key, and compare.
  Rewrite any item where you hesitate or where a careful expert could argue for a second option.
- **Independence:** no item gives away another item's answer.
- **Format:** every item carries the objective's id, the quiz file holds no answers, and the key has one entry per item with the same ids in the same order.

## Finish

End with a short message that the quiz is ready, its path and how many items it has, without any answers.
When the quiz runs ahead of the lessons, say so.
