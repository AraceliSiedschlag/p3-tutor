---
name: grade
description: Grade the learner's answers to a quiz in this workspace - a verdict and the misconception for every item, and feedback that explains each misconception very clearly, what the wrong idea is and why it is wrong, written the way PREFERENCES.md asks; use it whenever a submission needs grading.
argument-hint: "Which quiz and submission should I grade?"
---

# Grade

You run the grading of the learner's answers to a quiz in this workspace.
The `grader` subagent does the grading itself, because it is the only agent here that may read the answer keys in `keys/`; you never read, search or list `keys/`, and a guard blocks you if you try.
A grade is two things: a verdict the bench and the learner can trust, and feedback that helps the learner stop holding a wrong idea.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
Do what it asks now, without stopping to ask first; put any question for the learner at the end of your final message.

## Read first

1. `FORMATS.md`, the exact shape of the grades file.
2. The quiz in `quizzes/` and the submission in `submissions/`, to know which quiz and submission to grade; never `keys/`.
3. `PREFERENCES.md`, `MISSION.md` and `NOTES.md`, for the summary you give the learner at the end.

Use Read, Glob and Grep on named folders such as `quizzes/` and `submissions/`, never on the whole workspace, because a search over everything reaches `keys/`.
You need no shell.
Never write anything under `.claude/` or `keys/`.

## Start the grader

1. Take the grades file name `NNNN-sN.json`, after the quiz and the submission; the draft path is `drafts/grades-NNNN-sN.json`.
2. Start the `grader` subagent with a task message that gives only the quiz path, the submission path and the draft path.
3. **Wait for its report before you do anything else**; do not write a grades file of your own while it is running.
   If it reports that it could not write the draft, say so in the chat and stop; never grade without it.

## Review loop

A reviewer with a fresh context reads the feedback the way the learner will, which neither you nor the grader can do with your own reasoning in view.

1. Start the `grade-reviewer` subagent with a task message that gives only the paths of the draft, the quiz, its key (`keys/NNNN.json`) and the submission.
   Do not pass the grader's report or a summary of the grades.
2. **Wait for its report before you do anything else.**
3. If the report has any finding, start the `grader` again with the same three paths and the reviewer's findings, word for word, and wait for its report; it revises the draft, because only it can check a verdict against the key.
4. If the first report had any finding, start the reviewer again on the revised draft, the same way, and wait for it: this is the second pass.
   Send its findings to the `grader` once more and wait.
5. **Stop after two passes**, or earlier when a report has no findings. Never start a third.
6. Read the final draft and write it, unchanged, to `grades/NNNN-sN.json`, exactly as `FORMATS.md` shows.
7. Write a short record to `review-records/NNNN-sN-grade.md`: how many passes ran, each finding by check number and item, and what the grader changed for it or why it left it, from its reports.

## After grading

1. Write a learning record for what the grades show, an understanding or a misconception to work on, in the format in `.claude/skills/teach/references/LEARNING-RECORD-FORMAT.md`, and update `NOTES.md`.
2. Finish in the chat with the summary from the grades file and the next step.
