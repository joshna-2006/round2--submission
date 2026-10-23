# Synthetic Test Cases

All data is fake. "APP-101" etc. are made-up application numbers. These are design walk-throughs of the proposed process, **not real-world observations**.

| # | Case | Input | Expected result | Status after | Recovery |
|---|---|---|---|---|---|
| 1 | **Normal** | APP-101 uploads all 6 documents; names match | Staff pre-check, then the original is matched on reporting day | Pre-Verified → Original-Verified → Complete | – |
| 2 | **Missing information** | APP-102 has no TC (old college hasn't issued it); marks "original available: no, expected 15 Aug" | Can't be completed. An undertaking goes to the admissions head, and a due date is set | Pending-Document | Reminder 3 days before the due date. If it's missed, Escalated to the admissions head |
| 3 | **Duplicate** | APP-103 uploads the Inter memo twice (or two records exist for the same application number) | The system flags the duplicate; staff keep the latest and discard the other | Uploaded (one copy kept) | Student is told which copy was kept; nothing is lost |
| 4 | **Unauthorized request** | Someone without the student's login tries to view APP-104's documents, or a person who isn't the student or a listed parent asks to collect originals | Denied; the attempt is logged | No change | The student and admissions office are informed. Originals are released only with ID and written consent |
| 5 | **Failed step** | The form/portal is down on reporting day | The desk switches to the paper checklist | Original-Verified (on paper) | Staff upload the scans within 2 days; the status is updated in the sheet |

## Results (design walk-through, done 2026-10-23)
| # | Handled by the design? | Note |
|---|---|---|
| 1 | Yes | – |
| 2 | Yes | Depends on the admissions head being available. The deputy rule covers this |
| 3 | Yes | Needs a simple "one file per document type" rule in the sheet |
| 4 | Yes | Needs logins. A plain Google Form can't do this alone, which is a limitation |
| 5 | Yes | Paper fallback means double entry later (counted as support effort) |
