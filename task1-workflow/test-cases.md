# 4. Five Synthetic Test Cases

These are **synthetic** cases (STU-A etc. are made up), run against the prototype as **automated tests**. They test the **design**, not the real college process.

| # | Case | Input | Expected result | Recovery | Automated test |
|---|---|---|---|---|---|
| 1 | Normal | STU-A, lost card, all fields complete | SUBMITTED → VERIFIED → APPROVED → READY → COLLECTED | – | `test_1_normal` ✅ |
| 2 | Missing information | STU-B, no photo, no declaration | NEEDS_INFO listing both fields; the desk **cannot** verify it | Student adds both → back to SUBMITTED | `test_2_missing_information` ✅ |
| 3 | Duplicate | STU-C submits again while the first request is open | Second request REJECTED and linked to the first; the first is untouched | Student follows the first request | `test_3_duplicate` ✅ |
| 4 | Unauthorized request | STU-X requests STU-D's card; a student tries to approve; STU-X tries to collect STU-D's card | All three blocked and written to the security log; the card stays at the desk | Real owner collects with their own login | `test_4_unauthorized_request` ✅ |
| 5 | Failed step | Printer fails twice | 1st failure: PRINT_FAILED + temporary pass. 2nd failure: manual card, READY | Student collects normally | `test_5_failed_step` ✅ |

Extra tests (9): officer approval within the boundary, escalation of a 3rd replacement to the admin head, invalid or changed reason, no skipped steps, old card required for damaged cards, FIR only when the setting is on, the student reference cannot be changed, and two checks of the time-saving formula.

## Actual test run
Run on 2026-10-23 with Python 3 on this laptop (`py -m unittest -v` in `prototype/`). The output is saved in [prototype/test-output.txt](prototype/test-output.txt):
```
Ran 14 tests ... OK
```
The tests also run automatically on GitHub on every upload (see the badge in the main README).
