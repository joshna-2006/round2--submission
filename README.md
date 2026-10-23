# HKAIVERSE Round 2 – Joshna

[![checks](https://github.com/joshna-2006/round2--submission/actions/workflows/checks.yml/badge.svg)](https://github.com/joshna-2006/round2--submission/actions/workflows/checks.yml)

B.Tech CSE (Artificial Intelligence), IFHE Hyderabad, batch 2023–2027.

> Student work. Not an official syllabus revision. All test data is synthetic. No student names, IDs, marks, fee amounts, credentials or private messages are included.

## Release
- Release: **[to be added after the release is published]**
- Full commit URL of the reviewed revision: **[to be added]**

## The two tasks at a glance
| | Task 1 – College workflow | Task 2 – Curriculum audit |
|---|---|---|
| **Topic** | Replacing a lost or damaged **student ID card** | CSE (AI) curriculum vs. **Data Analyst, AI Engineer, Full Stack** roles |
| **Main idea** | One tracked request with proof checked online, a clear owner, an approval boundary for repeat replacements, and a temporary pass when printing fails | Engineering practice (testing, Git/CI, deployment, checking AI output) is the main gap. 10 updates, 3 small reductions, 1 new lab |
| **Built** | Working Python prototype: **14 automated tests** incl. the 5 required cases; time-saving calculator | Credit checker, interactive calculator, AI-exercise checks (**9 of 9**) |
| **Key number** | Net time saved: *method done; numbers illustrative until measured* | **37 of 166 credits affected (22.3%)**, balanced. 24.5% if Sem VIII is excluded |
| **Strongest evidence** | Two other universities' published procedures (3 and 5 office sign-offs) | **IFHE's official program-structure page**, compared course by course with my own course list |
| **Start here** | [task1-workflow/README.md](task1-workflow/README.md) | [task2-curriculum/report.md](task2-curriculum/report.md) |

## What is finished and what is not
| Item | Status |
|---|---|
| Task 1 design, prototype, 5 tests, time-saving method | Done and tested |
| Task 1 **evidence from IFHE** (ID desk + students) | **Not collected yet.** The current process is a labelled hypothesis. Questions and sheets are ready in [task1-workflow/evidence/](task1-workflow/evidence/) |
| Task 1 real time-saving figure | Pending: needs the measured values above |
| Task 2 credit map, comparison with the official page, proposal, 11 reasons, credit calculation, pathways, capstone | Done |
| Task 2 five-unit analysis | Partly done: complete for the one handout I have (DS401); priority courses need handouts |
| Task 2 job descriptions | Done: 3 dated + 1 undated; JD-2 only partly verified |
| Task 2 five AI exercises | Done and automatically re-checked |
| Faculty feedback on the redesign | Pending: message ready; none received |
| AI-use record, sources, limitations | Pass |

## Check it yourself
Python 3 only, nothing to install. The same commands run on GitHub on every upload (badge above).
```bash
cd task1-workflow/prototype && py -m unittest -v && py savings.py && cd ../..
cd task2-curriculum && py check_credits.py && cd ai-outputs && py verify.py
```
Interactive calculator: `task2-curriculum/calculator/index.html` (double-click), or online once GitHub Pages is on: https://joshna-2006.github.io/round2--submission/task2-curriculum/calculator/

## Repository map
```
task1-workflow/        README · problem-selection · current-process (hypothesis) · proposed-process
                       test-cases · time-saving · evidence/ (log, questions, sheet, benchmarks) · prototype/ (code + tests)
task2-curriculum/      report · current-curriculum.csv (with official comparison) · proposed-curriculum.csv
                       job-description-analysis · units-analysis · ai-exercises · feedback-request
                       check_credits.py · calculator/ · ai-outputs/verify.py
sources/               source-register (every URL with access date)
ai-use-record.md       where AI was used, and what I did myself
.github/workflows/     automatic checks
```

## Personal contribution
See [ai-use-record.md](ai-use-record.md): my decisions and inputs, where an AI assistant helped, and how each part was checked.

## Limitations (summary)
- **Task 1:** IFHE's actual process hasn't been observed yet. Benchmarks are from other universities. All time figures are illustrative.
- **Task 2:** IFHE's official structure states no batch or version, and 22 of my 52 courses differ from it. Regulations weren't available. Unit-level evidence covers one course only.
