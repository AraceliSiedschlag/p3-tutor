---
name: grade
description: Grade the learner's answers to a quiz in this workspace - a verdict and the misconception for every item, and feedback that explains each misconception very clearly, what the wrong idea is and why it is wrong, written the way PREFERENCES.md asks; use it whenever a submission needs grading.
argument-hint: "Which quiz and submission should I grade?"
---

# Grade

You grade the learner's answers to a quiz in this workspace.
A grade is two things: a verdict the bench and the learner can trust, and feedback that helps the learner stop holding a wrong idea.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
Do what it asks now, without stopping to ask first; put any question for the learner at the end of your final message.

## Read first

1. `FORMATS.md`, the exact shape of the grades file; follow it to the letter.
2. `.claude/skills/teach/references/GRADING.md`, the guide to verdicts, misconception ids and feedback; everything in it holds, and this skill adds to it.
3. The quiz in `quizzes/`, its key in `keys/`, and the submission in `submissions/`.
4. `PREFERENCES.md`, `MISSION.md`, `NOTES.md`, every file in `learning-records/`, and the lesson on the quiz's objective if there is one.

Use Read, Glob and Grep to look around and Write to create files; you need no shell.
Never write anything under `.claude/`.

## Verdicts and misconceptions

Grade every item exactly as `GRADING.md` says:

- Judge what the answer means, not its wording: an oddly worded or unusual answer that means what the key means is `correct`.
- `partial` when part is right, including the right answer with a wrong reason or an added false claim; `wrong` when it misses or contradicts the idea, or is blank.
- Name a misconception id only when the answer or its reasoning shows it, from the ids the workspace already uses; otherwise `null`, and never invent an id.

## Feedback that clears up a misconception

The learner wants each misconception explained very clearly, what it is and why it is wrong, so it does not stick.
For every item whose answer shows a misconception, wrong or partial, the feedback does these four things, in this order:

1. **Say exactly what the wrong idea is**, in one plain sentence, in terms of the learner's own answer: "Your answer assumes that ...".
   Do not hint at it or leave the learner to work it out.
2. **Say clearly why it is wrong**: what actually happens instead and the reason it happens, in plain words, in one or two sentences, the big picture and the why, the way `PREFERENCES.md` asks.
   Where a short concrete case from the learner's world (`MISSION.md`, `PREFERENCES.md`) makes the difference obvious, add it in a phrase.
3. **Say why the wrong idea is tempting**, in a clause, without blame, so the learner sees where it came from.
4. **Say how to avoid it next time**, in a few words.

Keep it to about five sentences: clear beats long.

For the other items:

- **Correct:** say so, and add the one insight that makes it stick.
- **Partial with no misconception:** say what was right, exactly what was missing, and how to complete it.
- **Wrong with no misconception** (a slip, a mix-up, a blank): give the right idea and why it holds, in two or three sentences.

In every item, follow `PREFERENCES.md` for tone: plain about what is right and wrong, casual and direct, with a little encouragement where it is earned, and no filler.

## The summary

The `summary` says, in a few sentences: what the learner has down, the misconception that matters most to clear up next, and one concrete next step, such as a short practice to try.
Mention only things the learner can see; never refer to `NOTES.md`, learning records or keys by name.

## Write and finish

1. Take the grades file name `NNNN-sN.json`, after the quiz and the submission, and write the draft, exactly as `FORMATS.md` shows, with one entry per quiz item in the quiz's order, unanswered items included, to `drafts/grades-NNNN-sN.json`; not yet to `grades/`.
2. Check the draft yourself first: every verdict against the key and `GRADING.md`; every misconception id exists in the workspace; every item with a misconception says plainly what the wrong idea is and why it is wrong.

## Review loop

A reviewer with a fresh context reads the feedback the way the learner will, which you cannot do with your own reasoning in view.

1. Start the `grade-reviewer` subagent with a task message that gives only the paths of the draft, the quiz, its key and the submission.
   Do not pass your reasoning or a summary of the grades.
2. **Wait for its report before you do anything else**; do not revise or finish while it is running.
3. Fix every finding marked must-fix, and every other finding unless you have a clear reason not to, in the draft.
   Change a verdict only when the reviewer's reason holds against the key and `GRADING.md`.
4. If the report had any finding, start the reviewer again on the revised draft, the same way, and wait for it: this is the second pass.
   Fix what it finds once more.
5. **Stop after two passes**, or earlier when a report has no findings. Never start a third.
6. Write the final grades to `grades/NNNN-sN.json`, exactly as `FORMATS.md` shows.
7. Write a short record to `review-records/NNNN-sN-grade.md`: how many passes ran, each finding by check number and item, and what you changed for it or why you left it.

## After grading

1. Write a learning record for what the grades show, an understanding or a misconception to work on, in the format in `.claude/skills/teach/references/LEARNING-RECORD-FORMAT.md`, and update `NOTES.md`.
2. Finish in the chat with the summary and the next step.
