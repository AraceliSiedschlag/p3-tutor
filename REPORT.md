# Report

This file is written by `p3 report --write` (p3 0.2.0, 2026-11-25 01:04 UTC). Do not edit it by hand: it is written again whenever new runs are scored.

## Results on agent-architecture

Scored full runs (quick runs and --only runs left out); each cell is the mean over the runs, with the range in brackets.

### Quality

| config | runs | teach facts | teach misconc. | length ratio | dead links | key agreement | wrong keys | ambiguous items | verdict agreement | false wrong | misconc. hit | leaks | behavior met |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 4 | 0.71 (0.00-1.00) | 0 (n=3) | 0.68 (0.66-0.71, n=3) | 0 (n=3) | 1.00 | 0 | 0 | 0.98 (0.92-1.00) | 0.00 | 0.95 (0.80-1.00) | 0 | 0.37 (0.33-0.50) |
| `c1-skills` | 1 | 1.00 | 0 | 0.83 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.33 |
| `c2-review` | 1 | 0.83 | 0 | 0.74 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.17 |
| `c3-split` | 1 | 1.00 | 0 | 0.88 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.17 |
| `final` | 2 | 0.75 (0.67-0.83) | 0 | 0.83 (0.82-0.84) | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.42 (0.33-0.50) |

Teach facts, key agreement, verdict agreement, false wrong, misconception hit and behavior met are shares (0 to 1); misconceptions, dead links, wrong keys, ambiguous items and leaks are counts per run.
A dash means no run could be scored on that check, and n= says how many of the runs could.
A job that failed counts against the config: no lesson scores 0 teach facts, no quiz and key 0 key agreement, a missing grades file disagrees on every item, and a tutor scenario with no reply is not met; leaks need a reply to check, so such a scenario is left out of them.
The length ratio is a rough reading-time estimate (visible words / 150) over the minutes requested; 0.6 to 1.5 counts as on length.

### Cost: teach

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 4 | 2.95M (133.0k-5.96M) | 41.4k (1.7k-60.3k) | 8.1 (0.4-12.7) | 0 | 2.12 (0.36-3.60) |
| `c1-skills` | 1 | 6.07M | 58.8k | 11.0 | 0 | 3.41 |
| `c2-review` | 1 | 4.93M | 161.7k | 26.0 | 2 | 5.52 |
| `c3-split` | 1 | 6.69M | 164.9k | 29.0 | 4 | 6.48 |
| `final` | 2 | 4.89M (4.28M-5.49M) | 138.0k (136.3k-139.6k) | 26.3 (25.7-26.8) | 5 | 5.34 (5.02-5.66) |

### Cost: quiz

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 4 | 805.1k (678.6k-944.4k) | 19.4k (15.3k-21.8k) | 3.8 (3.0-4.3) | 0 | 0.83 (0.71-0.92) |
| `c1-skills` | 1 | 410.5k | 19.2k | 3.5 | 0 | 0.67 |
| `c2-review` | 1 | 1.34M | 69.9k | 12.5 | 2 | 2.01 |
| `c3-split` | 1 | 1.67M | 64.8k | 12.1 | 2 | 2.06 |
| `final` | 2 | 1.05M | 57.4k (56.9k-58.0k) | 11.1 (11.0-11.2) | 2 | 1.72 (1.66-1.78) |

### Cost: grade

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 4 | 646.4k (546.3k-716.4k) | 16.9k (15.1k-19.1k) | 3.1 (2.9-3.4) | 0 | 0.92 (0.87-1.04) |
| `c1-skills` | 1 | 690.6k | 18.3k | 3.4 | 0 | 0.87 |
| `c2-review` | 1 | 2.29M | 107.1k | 18.9 | 4 | 3.13 |
| `c3-split` | 1 | 2.41M | 109.6k | 18.8 | 4 | 3.19 |
| `final` | 2 | 2.38M (2.35M-2.40M) | 108.7k (107.1k-110.3k) | 22.2 (21.2-23.2) | 7 | 3.45 (3.36-3.53) |

### Cost: tutor

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 4 | 941.9k (837.7k-1.10M) | 20.1k (18.2k-21.9k) | 4.5 (4.1-5.0) | 0 | 1.50 (1.43-1.66) |
| `c1-skills` | 1 | 761.6k | 15.2k | 3.8 | 0 | 1.17 |
| `c2-review` | 1 | 890.0k | 16.6k | 4.1 | 0 | 1.22 |
| `c3-split` | 1 | 669.4k | 14.0k | 3.4 | 0 | 1.06 |
| `final` | 2 | 771.2k (735.0k-807.3k) | 14.5k (13.7k-15.3k) | 4.1 (3.8-4.4) | 0 | 1.48 (1.45-1.51) |

### Cost: all jobs

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 4 | 5.34M (2.59M-8.72M) | 97.7k (58.3k-118.3k) | 19.6 (12.2-24.6) | 0 | 5.38 (3.60-7.22) |
| `c1-skills` | 1 | 7.93M | 111.5k | 21.8 | 0 | 6.12 |
| `c2-review` | 1 | 9.45M | 355.3k | 61.5 | 8 | 11.88 |
| `c3-split` | 1 | 11.44M | 353.3k | 63.3 | 10 | 12.79 |
| `final` | 2 | 9.08M (8.42M-9.74M) | 318.6k (315.1k-322.1k) | 63.7 (61.9-65.5) | 14 | 11.98 (11.61-12.36) |

Costs are per run, summed over the job's scenarios; list-price $ is the list-price equivalent, not what you pay on a subscription.

## Your ratings

Your ratings from 1 to 5 in the major reviews (reviews/<step>.md), which review full runs on the shared topic; a dash means no rating there yet, one that p3 check does not accept, or a job that step does not review (Tutor in c2-review; Quiz, Feedback and Tutor in c3-split).

| job | criterion | c1-skills | c2-review | c3-split | final |
|---|---|---:|---:|---:|---:|
| Lesson | Technical correctness and facts | 4 | 5 | 5 | 5 |
| Lesson | Pedagogy | 3 | 4 | 5 | 5 |
| Lesson | Alignment with the learning goal | 5 | 5 | 5 | 5 |
| Lesson | Overall quality | 4 | 5 | 5 | 5 |
| Quiz | Difficulty | 4 | 2 | - | 3 |
| Quiz | Coverage of the lesson's core | 4 | 4 | - | 5 |
| Quiz | Wording and possible misreadings | 4 | 1 | - | 5 |
| Quiz | Writing quality | 4 | 5 | - | 4 |
| Quiz | Alignment with the learning goal | 5 | 4 | - | 5 |
| Feedback | Useful | 4 | 4 | - | 5 |
| Feedback | Explains enough | 4 | 2 | - | 5 |
| Feedback | Personalized to how I like things explained | 3 | 4 | - | 5 |
| Tutor | Guardrails | 4 | - | - | 5 |
| Tutor | Personalization | 3 | - | - | 5 |

## The ablation

Each `final-minus-*` config's latest scored run on agent-architecture at 30 minutes (not a quick run) beside `final`'s scored full runs, for the jobs that run covered; each cell is the mean over the runs, with the range in brackets.

### `final-minus-grade-reviewer`

#### Quality

| config | runs | verdict agreement | false wrong | misconc. hit |
|---|---:|---:|---:|---:|
| `final` | 2 | 1.00 | 0.00 | 1.00 |
| `final-minus-grade-reviewer` | 1 | 0.92 | 0.00 | 0.80 |

`final-minus-grade-reviewer` was run with --only and covers only these scenarios: grade-s1, grade-s2; its costs add up only those, while the costs of `final` add up every scenario of each job.

#### Cost: grade

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `final` | 2 | 2.38M (2.35M-2.40M) | 108.7k (107.1k-110.3k) | 22.2 (21.2-23.2) | 7 | 3.45 (3.36-3.53) |
| `final-minus-grade-reviewer` | 1 | 1.16M | 26.0k | 5.3 | 2 | 1.39 |

Costs are per run, summed over the job's scenarios; list-price $ is the list-price equivalent, not what you pay on a subscription.

## Results on cake-baking

Scored full runs (quick runs and --only runs left out); each cell is the mean over the runs, with the range in brackets.

### Quality

| config | runs | teach facts | teach misconc. | length ratio | dead links | key agreement | wrong keys | ambiguous items | verdict agreement | false wrong | misconc. hit | leaks | behavior met |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 1 | 0.75 | 0 | 0.78 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.20 |
| `final` | 1 | 0.75 | 0 | 0.81 | 0 | 1.00 | 0 | 1 | 0.83 | 0.00 | 1.00 | 0 | 0.60 |

Teach facts, key agreement, verdict agreement, false wrong, misconception hit and behavior met are shares (0 to 1); misconceptions, dead links, wrong keys, ambiguous items and leaks are counts per run.
A dash means no run could be scored on that check, and n= says how many of the runs could.
A job that failed counts against the config: no lesson scores 0 teach facts, no quiz and key 0 key agreement, a missing grades file disagrees on every item, and a tutor scenario with no reply is not met; leaks need a reply to check, so such a scenario is left out of them.
The length ratio is a rough reading-time estimate (visible words / 150) over the minutes requested; 0.6 to 1.5 counts as on length.

### Cost: teach

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 1 | 6.42M | 78.8k | 16.5 | 0 | 4.06 |
| `final` | 1 | 14.08M | 217.3k | 40.4 | 8 | 10.88 |

### Cost: quiz

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 1 | 894.5k | 24.4k | 4.7 | 1 | 1.23 |
| `final` | 1 | 1.67M | 132 | 15.0 | 2 | - |

### Cost: grade

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 1 | 282.8k | 6.6k | 1.3 | 0 | 0.45 |
| `final` | 1 | 1.29M | 59.9k | 12.7 | 5 | 2.01 |

### Cost: tutor

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 1 | 1.28M | 21.7k | 5.4 | 0 | 1.78 |
| `final` | 1 | 553.6k | 10.5k | 3.1 | 0 | 1.07 |

### Cost: all jobs

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 1 | 8.87M | 131.6k | 27.8 | 1 | 7.51 |
| `final` | 1 | 17.59M | 287.9k | 71.1 | 15 | 13.97 |

Costs are per run, summed over the job's scenarios; list-price $ is the list-price equivalent, not what you pay on a subscription.
