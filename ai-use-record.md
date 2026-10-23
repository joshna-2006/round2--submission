# AI Use Record and Personal Contribution

Tool used throughout: **Claude Opus 5.5 (Anthropic)**, in the Claude desktop app, 22–23 October 2026. Commits written by the assistant carry a `Co-Authored-By: Claude` line in the Git history.

## What I did
| Contribution | Evidence |
|---|---|
| Chose the three target roles (Data Analyst, AI Engineer, Full Stack) | Task 2 report |
| Supplied my own semester course list (Sem I–VII screenshots from my portal) and told the assistant that Sem VIII is the internship | current-curriculum.csv, columns 1–4 |
| Supplied the DS401 course handout from my LMS | units-analysis.md, Part A |
| Got the list of college administration areas from a faculty member, which is where the Task 1 candidates came from | Task 1 evidence E1 |
| Rejected earlier Task 1 versions (bonafide → admission documents → equipment purchase) and asked for a rebuild that I can personally verify and explain | Git history |
| Created the GitHub repository, approved the upload and published the release | GitHub |
| ☐ Confirmed the Task 1 choice after reviewing the scoring (problem-selection.md) | *tick when done* |
| ☐ Re-ran the tests and checks myself (`py -m unittest`, `check_credits.py`, `verify.py`) | *tick when done* |
| ☐ Asked the ID desk and students (evidence E5–E8) | *fill evidence-log.md* |
| ☐ Opened and screenshotted the job links | *tick when done* |

## What the AI assistant did
| Work | How it can be checked |
|---|---|
| Found and read the IFHE program-structure page and compared it with my course list | current-curriculum.csv; the URL is in the source register |
| Found the job postings and the two benchmark ID card procedures | URLs in the source register |
| Drafted the problem-selection scoring, current-process hypothesis, proposed process and evidence templates | Marked as drafted with AI help in problem-selection.md |
| Wrote the prototype, the 14 tests and the time-saving calculator | Run them: `py -m unittest -v` |
| Drafted the Task 2 proposal, the 11 reasons and the pathways | Numbers recomputed by `check_credits.py` |
| Answered the 5 AI exercises, then wrote independent checks for them | `py verify.py` (9 of 9) and the AWS pages |
| Built the interactive calculator and the GitHub checks | Calculator README test table; GitHub Actions |
| Installed Git and uploaded files on my machine | Git history |

## Errors the AI made that were caught and fixed
- An earlier version claimed my curriculum had "no statistics course". The official page shows a newer version has BS105 Probability & Statistics, so reason R4 was rewritten.
- An earlier version used Physics = 5 credits as the only source. The official page says 4, and this is now shown as a conflict.
- An evidence entry described a web search before that search had been done. The search was then run and the entry corrected.
- AI exercise 5: the AI's answer about AWS EC2 free-tier limits was outdated.
