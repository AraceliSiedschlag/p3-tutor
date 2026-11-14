# Components

One entry for every skill and every subagent you built, from `c1-skills` to `final`, including the ones you dropped, even one you took out again before any snapshot.
The heading is the skill's folder name or the subagent's `name` from its frontmatter, and `reviews/README.md` says what each field holds.
Replace the empty entry at the bottom with your first component, and copy it for each one after that.
Claude Code may fill in Kind, Step added, and With and without; Purpose, Review and Kept in final are yours.

<!--
An example of a finished entry:

### quiz-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: My c1 review found two quiz items that could be read two ways (q2 and q4) and one whose correct option repeated the stem; a reviewer with a fresh context reads the draft the way a learner will, which the quiz skill writing its own items cannot do, so it is a subagent and not a step in the skill.
- With and without: reviews/c2-review.md, Round 1 (without) and Round 2 (with)
- Review: Without it, q2 asked which design "is better" with no criterion; with it, every stem names its criterion and the reviewer's record shows two items flagged and fixed in one pass, for about 0.6M more tokens per quiz, which I think a quiz is worth, because a misread item teaches the wrong thing.
- Kept in final: yes
-->

### tutor

- Kind: skill
- Step added: c1-skills
- Purpose: Added to reduce giving out quiz answers and running longer. Answer students questions about the chosen topic.I
- With and without: reviews/c1-skills.md, Round 1 (without) and Round 2 (with)
- Review: When using tutor it created answeres and corrected misconceptions which was helpful. Otherwise, you can miss or continue believing what you are doing. Tutors price decreased with the skill but probes 2/6 passing stayed the same with and without.
- Kept in final: TODO

### quiz

- Kind: skill
- Step added: c1-skills
- Purpose: Added to quiz students on a topic they learned to show if they did learn. Creates a short mcq and short response quiz on the given topic.
- With and without: reviews/c1-skills.md, Round 3 (without) and Round 4 (with)
- Review: It helped to make sure you understood the lesson and pair with grader if you missed something. With this skill it helped to lower the word count compare to with and without.
- Kept in final: TODO

### grade

- Kind: skill
- Step added: c1-skills
- Purpose: Added to give users feedback on their quiz, grade quiz, and correct misconceptions or other incorrect thinkings/answers.
- With and without: reviews/c1-skills.md, Round 4 (without) and Round 5 (with)
- Review: It helps to give feedback and correct misconseption while grading a users quiz. With this skill the misconseption feedback grew in word count.
- Kept in final: TODO

### teach

- Kind: skill
- Step added: c1-skills
- Purpose: Added to create a lesson for a specific topic. This includes interactive sections, pictures, and sources.
- With and without: not changed in a round; it is the shipped skill, the same in c0-baseline and c1-skills
- Review: It worked well to create a ten min interactive lesson that stayed on topic and taught the user.
- Kept in final: TODO

### quiz-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: The quiz reviewer was added to because in c1 it was found that it copied questions directly from the lesson. It reads each quiz draft and its key with fresh context before it is final and checks it against 10 things.
- With and without: reviews/c2-review.md, Round 1 (without) and Round 2 (with)
- Review: This did not seem worth it, it moves one of all of the scores and otherwise they stayed the same.
- Kept in final: TODO

### grade-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: grade-reviewer was added to provide additional feedback to the user while staying under a certain length. It reads each draft of teh grades with the quix, key, submission and preferences.md checks it against a list then fixes it or lets it pass.
- With and without: reviews/c2-review.md, Round 2 (without) and Round 3 (with)
- Review: This seemed worth it becuase it raised scores and made substantial differences for the feedback.
- Kept in final: TODO

### lesson-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: This reviewer was added to make sure at least three interactive questions were added in every lesson, with the lesson staying on topic. It reads each lesson draft in four sepreate reviews, checks against a list and reports it so that the teach skill can make the fixes.
- With and without: reviews/c2-review.md, Round 3 (without) and the c2-review full run (with)
- Review: This was not worth it for a smaller change in the lessons for an additional 15 min and 3 dollars. So it did not seem worth it.
- Kept in final: TODO
