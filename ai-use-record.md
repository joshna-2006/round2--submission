# AI Use Record and Personal Contribution

## How I worked
I used **Claude (Anthropic)** as an assistant for research, drafting and coding, on 22–23 October 2026. I set the direction, provided my own data, made the main decisions and checked the results. Every number in the repository can be recomputed by code instead of trusted (see "Check it yourself" in the [README](README.md)).

## My decisions and inputs
| What | Details |
|---|---|
| Target roles | I chose Data Analyst, AI Engineer and Full Stack Developer |
| Curriculum data | I provided my own Sem I–VII course list from my student portal, the Sem VIII internship information, and the DS401 course handout |
| Task 1 topic | I gathered the list of college administration areas from a faculty member. From it I chose ID card replacement, because I can verify it first-hand without private data |
| Quality standard | I rejected earlier drafts and asked for a version based only on evidence I can verify and explain |
| Repository | I created the GitHub repository and published the release |

## Where the AI assistant helped
| Area | Help given | How it was checked |
|---|---|---|
| Research | Finding the IFHE program-structure page, job postings and other universities' ID card procedures | All URLs and access dates are in the [source register](sources/source-register.md) |
| Drafting | First drafts of the reports, tables and evidence templates | Reviewed against the assignment checklist |
| Code | Prototype, tests, credit checker, calculator | 14 tests + `check_credits.py` + `verify.py`, run automatically on GitHub |
| AI exercises | Answering the 5 subject exercises (the task requires an AI model) | Each answer checked independently: code run, SQL executed, metrics calculated by hand, cloud claims compared with AWS pages |

## Problems found during checking
- An early draft said my curriculum had no statistics course. The official IFHE page shows a newer version with Probability & Statistics, so that reason was rewritten.
- My screenshot credits differ from the official page for 4 courses. The difference is now shown openly instead of hidden.
- In AI exercise 5, the AI's information on AWS free-tier limits was outdated.

## My verification checklist
- [ ] Ran the tests and checks myself (`py -m unittest -v`, `py check_credits.py`, `py verify.py`)
- [ ] Opened and screenshotted the job links
- [ ] Reviewed and confirmed the Task 1 choice in [problem-selection.md](task1-workflow/problem-selection.md)
- [ ] Asked the IFHE ID desk and students (evidence entries E5–E8)
