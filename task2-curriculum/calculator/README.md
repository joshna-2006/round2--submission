# Curriculum Credit Calculator

A single HTML page with no installation and no internet needed. Data is built in from [../proposed-curriculum.csv](../proposed-curriculum.csv).

## How to run
- **Easiest:** double-click `index.html` and it opens in any browser.
- **Or** run a local server: `py -m http.server 8765` in this folder, then open http://localhost:8765
- **Online:** enable GitHub Pages on the repository and open `/task2-curriculum/calculator/`

I chose plain HTML/JavaScript instead of Streamlit, so reviewers can open it with one click without installing Python.

## Features
- Filter by **role** (Data Analyst / AI Engineer / Full Stack), **semester**, **action** (KEEP/UPDATE/REDUCE/ADD), and text search
- Compare **current vs. proposed credits** for every course
- See the skills, reason number (R1–R10) and rationale for each course
- Live totals: current and proposed totals, a balance check, affected credits, affected %, and credits supporting the selected role
- Load a different CSV (same columns) or download the current data as CSV

## Data schema
| Column | Meaning |
|---|---|
| semester | 1–7 or `Summer-II` |
| code | Course code; proposed courses start with `NEW-` |
| course | Course name |
| current_credits | Credits now (0 for proposed new courses) |
| proposed_credits | Credits in the proposal |
| action | KEEP / UPDATE / REDUCE / ADD |
| roles | `DA`, `AI`, `FS`, separated by `;` |
| skills | Skills taught, separated by `;` |
| reason_id | Links to reasons R1–R10 in the report |
| rationale | Short justification |

## Formulas
```
current total     = Σ current_credits
proposed total    = Σ proposed_credits
balanced          = (current total == proposed total)
updated credits   = Σ current_credits of UPDATE rows
reduced credits   = Σ (current − proposed) of REDUCE rows
added credits     = Σ proposed_credits of ADD rows
affected credits  = updated credits + max(reduced, added)   ← reallocated credits counted once
affected %        = affected credits ÷ current total × 100
role credits      = Σ proposed_credits of rows tagged with the role
```

## Input validation
Each row is checked for:
- a missing or duplicate course code
- credits that aren't a number, or are negative
- an action other than KEEP/UPDATE/REDUCE/ADD
- KEEP or UPDATE rows whose credits change
- REDUCE rows where proposed credits aren't lower than current
- ADD rows where current credits aren't 0

Problems are shown in red above the table.

## Test results (run 2026-10-23 in the browser on a local server, by calling the page's `calc()` / `validate()` functions)

| # | Test | Input | Expected | Actual | Pass |
|---|---|---|---|---|---|
| T1 | Real proposal data | proposed-curriculum.csv (54 rows) | 151 → 151, balanced, affected 32, 21.2%, no validation errors | 151 → 151, balanced, 32, 21.19%, 0 errors | ✅ |
| T2 | Unbalanced proposal | KEEP 4→4 plus ADD 0→3 | Not balanced (+3); affected 3 of 4 = 75% | balanced=false, affected 3, 75% | ✅ |
| T3 | Invalid rows (synthetic) | negative credit, duplicate code, REDUCE that increases credits, action "DELETE" | 5 error messages | 5 matching error messages | ✅ |
| T4 | Filters | Role = Full Stack, Action = UPDATE | CS206, DS202, CS205, CS307 | CS206, DS202, CS205, CS307 | ✅ |

## Limitations
- Course list and credits come from my syllabus screenshots and are **not yet verified** against the official IFHE curriculum.
- Semester VIII (internship) is **not included** because its credits are unverified. Adding it would increase the total and lower the affected %.
- Role tags are my own judgement, based on course titles and four job descriptions.
