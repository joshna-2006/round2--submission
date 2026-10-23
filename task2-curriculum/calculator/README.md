# Curriculum Credit Calculator

A single HTML page: no install, works offline. Its data is a copy of [../proposed-curriculum.csv](../proposed-curriculum.csv), and `check_credits.py` fails if the two ever differ.

**Open it:** after GitHub Pages is enabled, at `https://joshna-2006.github.io/round2--submission/task2-curriculum/calculator/`. Or download the repo and double-click `index.html`.

I used plain HTML/JavaScript instead of Streamlit, so a reviewer can open it in one click without installing Python.

## What it does
- Filter by **role** (Data Analyst / AI Engineer / Full Stack), **semester**, **action** and text search
- Show current vs. proposed credits, skills, the reason (R1–R11), the rationale, and how each course compares with the official IFHE page
- Live **totals, balance check, affected credits and affected %**
- Toggle the **Sem VIII internship** on or off, to show the result with and without the credits I couldn't confirm from my screenshots

## Formulas
```
affected = Σ credits of UPDATE courses + max(Σ removed by REDUCE, Σ created by ADD)
affected % = affected ÷ current total × 100
balanced   = current total == proposed total
```

## Input validation
Each row is checked for duplicate codes, credits that aren't numbers or are negative, an unknown action, KEEP/UPDATE that change credits, REDUCE that doesn't lower credits, and ADD that doesn't start at 0.

## Test results (2026-10-23, Chromium-based browser, local server)
| # | Test | Expected | Actual | Pass |
|---|---|---|---|---|
| T1 | Real data, Sem VIII included | 166 → 166, balanced, 37 affected, 22.3%, no errors | 166 → 166, Balanced ✓, 37, 22.3%, no errors | ✅ |
| T2 | Sem VIII excluded | 151 → 151, 37, 24.5% | 151 → 151, 37, 24.5% | ✅ |
| T3 | Filter Full Stack + ADD | NEW-SE1 only | NEW-SE1 | ✅ |
| T4 | Invalid synthetic rows (UPDATE changes credits, duplicate code, REDUCE that increases) | 3 errors | 3 matching errors | ✅ |
| T5 | Unbalanced synthetic data (KEEP 4 + ADD 2) | not balanced, 2 of 4 = 50% | balanced=false, 50% | ✅ |

The same totals are produced independently by `py check_credits.py`, which also runs on GitHub on every upload.

## Limitations
- The course list is from my screenshots. Only 30 of 52 courses match the official page exactly (see `../current-curriculum.csv`).
- Role tags are my judgement, from course titles and four job descriptions.
