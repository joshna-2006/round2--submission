# Task 1 – Student ID Card Replacement

**Process:** what an IFHE student does to get a new ID card after losing or damaging one.
**Status:** design and prototype done. Desk research done. **Evidence from IFHE not yet collected** (see the table below).

## Read in this order
| # | File | What it contains | Evidence level |
|---|---|---|---|
| 1 | [problem-selection.md](problem-selection.md) | Why this process: 5 candidates compared | Candidates from a faculty member (fact); scores are my judgement |
| 2 | [current-process.md](current-process.md) | Expected current steps (V1–V9) and the problem hypothesis H1 | **Hypothesis**, to be checked |
| 3 | [evidence/](evidence/) | Evidence log, questions to ask, student check sheet | 4 real entries (faculty list, web search, 2 other-university benchmarks); IFHE desk and students still to ask |
| 4 | [proposed-process.md](proposed-process.md) | New process: inputs, statuses, owner, approval boundary, fallback | Design |
| 5 | [test-cases.md](test-cases.md) | 5 required synthetic cases with expected results and recovery | Tested: 14 automated tests pass |
| 6 | [time-saving.md](time-saving.md) | Net time saved after review, support and setup effort | Method done; numbers **illustrative** |
| – | [prototype/](prototype/) | Working Python code for the workflow and the calculation | Runs; see below |

## Requirement checklist
| Requirement | Where | Status |
|---|---|---|
| Choose a small process studied with permission | problem-selection.md, evidence-log permission table | Chosen; ID desk and students not yet asked |
| Map steps, handoffs, approvals, exceptions | current-process.md | Done as a hypothesis; to be verified |
| Dated evidence log with F/E/A labels | evidence/evidence-log.md | E1–E4 filled (desk research); IFHE desk and student entries still empty |
| Problem and its scale | current-process.md (H1), time-saving.md | Pending: scale needs measurement |
| Improved process: inputs, statuses, owner, approval boundaries, fallback | proposed-process.md | Pass |
| 5 synthetic tests with expected results and recovery | test-cases.md + automated tests | Pass |
| Net time saved after review and support effort | time-saving.md, `savings.py` | Method done; numbers illustrative |
| Mockup (optional) | prototype/ (working code instead of a mockup) | Pass |

## Run it yourself (Python 3, nothing to install)
```bash
cd task1-workflow/prototype
py idcard_workflow.py          # walks one request through every step
py -m unittest -v              # runs all 14 tests
py savings.py                  # prints the time-saving calculation
```
On Mac/Linux use `python3` instead of `py`.

## Limitations
- The current process is a **hypothesis**. I haven't yet spoken to the ID desk or students, so the problem (H1) isn't confirmed.
- All time and volume numbers are **illustrative**. The calculation shows the method only.
- The approval boundary (3rd replacement → admin head) is my design choice, not a known IFHE rule.
- The prototype runs in memory with synthetic data. It has no login system, database or real printer.
