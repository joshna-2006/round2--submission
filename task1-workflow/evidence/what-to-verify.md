# Evidence Collection Plan

Goal: replace the hypothesis in [../current-process.md](../current-process.md) and the illustrative numbers in [../prototype/params.json](../prototype/params.json) with real, permitted evidence.

**Rules I follow:** ask permission first; record **roles, not names**; no student IDs, card numbers, photos, fee amounts or private messages; anyone can decline, and I record only "declined".

## A. ID desk / admin office (5 minutes)
**Opening:** "I'm a B.Tech student doing a college assignment on improving a student process. Could I ask 6 quick questions about how ID card replacement works? I won't record any names or personal data."

| # | Question | Fills |
|---|---|---|
| 1 | Where does a student apply, and is there a form (paper or online)? | V1, V2 |
| 2 | What must the student bring (photo, letter, declaration)? | V2 |
| 3 | Is there a replacement charge, yes or no? Where is it paid? (amount not recorded) | V3, V4 |
| 4 | Who approves the request? | V5 |
| 5 | Is the card printed here or outside? How many working days, usually? | V6 |
| 6 | Roughly how many replacement requests come in per month? How long does one take you? | `requests_per_month`, `old_staff_minutes` |
| 7 | What goes wrong most often? | exceptions |
| 8 | For a lost card, is a police report (FIR) needed? For a damaged card, must the old card be returned? | V9, `REQUIRE_FIR_FOR_LOST` |

## B. Students who have replaced a card (aim for 3–5)
Ask on class groups: "Has anyone replaced their ID card? 1 minute of questions, anonymous." Record each answer as one row in [student-check-sheet.csv](student-check-sheet.csv).

| # | Question |
|---|---|
| 1 | Lost or damaged? |
| 2 | Roughly when (month/year)? |
| 3 | How many working days until you got the new card? |
| 4 | How many separate visits to offices did it take? |
| 5 | About how long was each visit (minutes)? |
| 6 | What did you use as ID meanwhile? |
| 7 | Anything that went wrong? |

## C. After collecting
1. Add each conversation to [evidence-log.md](evidence-log.md) with the date and a label: F (fact told to me), E (estimate), A (assumption).
2. Mark V1–V8 in the evidence log as ✅ / ✏️ / ❌.
3. Put the medians into `../prototype/params.json`, set `"label": "observed"`, and set `"source"` to the log entry.
4. Run `py savings.py` again and copy the new result into [../time-saving.md](../time-saving.md).
5. If H1 is not supported, say so in the report.
