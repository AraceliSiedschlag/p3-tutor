# Decision log

The decisions you made on the ladder, in your own words.
About one to two pages in total: each answer is two to four sentences with one number or one quote in it.

This file is the write-up of the project since version 0.2.
It replaces `EVAL.md`, which you no longer need to write.
If you already wrote a section of `EVAL.md` that answers a prompt here, keep it and point to it, such as "See EVAL.md, section 3", with one sentence that gives the answer.

The numbers come from `REPORT.md`, which `uv run p3 report --write` writes from your scored runs, so you never copy a table by hand.
Your ratings come from your major reviews in `reviews/`.
Specifics beat polish: a short, honest answer with a number in it is worth more than a long vague one, and "it did not pay off" is a full answer when you measured it.

Answer prompts 1 to 3 as you finish each step, while the decision is still fresh, and the rest once `final` has its runs.
Each prompt ends with a marker line.
Replace that line with your answer.
`uv run p3 check` reports a marker as work still to do, and `uv run p3 check --final` fails while any marker is left.

Please do not let an agent write these for you.
They are about what you chose and what you saw, and the Builder and the Guide never write them.

---

## 1. Step 1: the skill change that mattered most

Of everything you changed while building `c1-skills`, which one change to a skill made the biggest difference, and how do you know?
Name the round, and give the evidence: a rating that moved, a check in `REPORT.md` that moved, or a quote from an output before and after.

One change that made the biggest difference in the skill is a change to the quiz skill in Round 3. Starting out the quiz skills were very long and complicated unnecessarly so that was changed to make them shorter and simplier. This change was seen to be signinficant becasue in round 1 is when it was found out that the questions were very long and tedious howver after round 3 (the change) they were noticably shorter and the lengths had decreased. So, the biggest change was at round 3 where the quiz skill was adjusted to be shorter and more consise.

---

## 2. Step 2: which review loop earned its cost

In `c2-review` you put reviewers on teach, quiz and grade.
Which loop earned its cost and which did not?
For each of the two, give what it cost in tokens against `c1-skills` and one thing its reviewer caught, or say that it caught nothing.

The loops that earned its cost were the grade-reviewer which had tokens increase from 690.6K to 2.29M and while that is a lot the personalized feedback increased as well.
The ones that did not were the teach (lesson reviewer) which went from 58.8K to 161.7K outpput tokens and 11 min to 26, the quiz reviewer in the direct test did well but in the full run the quiz skill came out rated low and increased the tokens by 0.93M but did catch an ambiquety in the questions. So, the one that earned it was the grade reviewer the ones that did not were the lesson and quiz reviewer.


---

## 3. Step 3: whether splitting the teach job paid

`c3-split` splits the teach job across subagents.
Did the lesson get better by your own ratings, and what did the split cost against `c2-review`?
Say in one sentence whether you would pay that price again.

Yes, I would pay the price again because the personlization, facts, and length all increased in ratings and scores.

---

## 4. `final`: what you kept, what you dropped, and a change that did not pay

Which components did `final` keep and which did it drop, and what rule did you use to decide?
Then name one change anywhere on the ladder that did not pay off: what you expected, what you measured, and what you did about it.

The final kept all components and nothing was dropped. I kept lesson reviewer which I said was unhelpful to see if it was significant and helpful in the final run, making it as different from the baseline as possible. One change that did not pay off was the lesson-reviewer which was not worth it seeing as it measured a small change for an extra 15 min and 3 dollars.

---

## 5. The ablation

Which component did you remove, and what did you predict would happen to quality and to cost before you ran it?
Then the result, with the numbers of the ablation's run beside `final`'s, and what one run lets you claim and what it does not.

I am removing the grade-reviewer. I predict that it 
will barely change the numbers(quality stays similar) and reduce the cost of the runs. However, in reality the verdict agreement dropped from 1 to 0.92, false wrong rate stayed the dame the misconception hit went from 1 to 0.8 and the tokens decreaked from 3.38 to 1.16M and went from $3.45 to $1.39 with 7 agents vs 2 subagents. And while these numbers seem very different in reality you cannot fully rely on them because it is a single run so they could be chance but should not been taken as 100% the truth or very moving evidence. 

---

## 6. Your blind picks against your open reviews

You reviewed `final` openly, knowing you built it, and then compared it with `c0-baseline` blind.
Give the blind tally for each job, and say where it agreed with your open reviews and where it did not.
Where they disagreed, say what you think happened.

- teach: final 2, baseline 0, tie 0
- quiz: final 1, baseline 0, tie 1
- grade: final 18, baseline 5, tie 1
- tutor: final 8, baseline 4, tie 0

The most mixed or closest in score was the tutor with 8 for the final and 4 for the baseline. Grade, had significantly more chosen for it but it still had 5 for the baseline, I think when they were shorter answers and I didnt need as much explinations which slightly agrees with my explains enough but sometimes it was to much. You could tell more which was which purely using feebdack with it being nicer and more explanitory than the baseline, this agrees with my rating which rated the final as five for explains enough and personalization. Moreover, the tutor and lesson choice of the final agrees with my ratings which set personalization to 5 and the chosen one had far more related examples compared to the baseline. 
---

## 7. The test topic

You tuned the tutor on the shared topic only.
On your test topic, did `final` still beat `c0-baseline`, and was the gain smaller, the same, or larger than on the shared topic?
Give one number or one quote from each config's output on it.

On the shared topic the facts correctness stayed flat for the new topic but grew for the shared (0.04+ v 0). The quiz stayed the same for shared topic and the new topic didnt finsih. The grade verdic grew (0.98 v 1.00) for the shared topic but got worse from the new topic (1.00 v 0.83) yet the biggest growth was for the tutor behavior met that for the shared one went 0.37 v 0.42 to 0.20 v 0.60 in the new topic. Overall, the numbers are faily mixed for this in some senarious it increased some it decreased and some it stayed the same.

---

## 8. The judge check

The bench's judge scored your lessons' facts and your tutor's replies.
Label ten of the items it judged yourself, before you look at its verdicts.
On how many of the ten did you agree with it, and what was one disagreement about?

1 Met N
2 Met M
3 Met M
4 Not met (Included distinguishing numbers) N
5 Not met (didnt say it was out of scope) N
6 Met N
7 Met N
8 Not Met N
9 Met M
10 Met M

When comparing them the judge and I had rulled the same on 7/10 questions, however, we disagreed on three. For example, one we disagreed on was probe 01 in the final run (bench/runs/final/20261123-143755-agent-architecture-m30-r1)> The prompt that is asking for an answer during the retake was classified as not met by the judge and met for me. I said it was met becasue it did not give the answers and was polite but from the judges perspective they said that they are singling out a specific answer by including (maybe a nicer sounding prompt) and I agree with it. I think I was being to lenate when saying that its fine becasue it didnt state the asnwer directly but in realiy it defintely singled out the correct answer.

---

## 9. The stretch

What you tried, what it showed, and the one number that says so.
For the length study, give the outcome your `PREREG.md` rule points to.
If you did not take a stretch, write "No stretch."

No stretch.
