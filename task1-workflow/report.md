# Task 1 – Admission Document Submission and Verification

**Process studied:** how new B.Tech students submit and get their certificates verified when joining IFHE (when I joined: 10th memo, Inter memo, Transfer Certificate, Aadhaar, photos).

**Why this process:** every new student goes through it, it has clear handoffs and exceptions (missing TC, name mismatch), and I went through it myself when I joined in 2023.

**Labels used:** **[F]** Fact (I experienced or saw it) · **[E]** Estimate · **[A]** Assumption (not confirmed) · **[P]** Proposed design. Evidence is in [evidence-log.md](evidence-log.md).

---

## 1. Current process (as I understand it)

```
Admission confirmed → Student gets list of documents → Reporting day: queue at verification desk
→ Staff check each original against photocopies → (missing doc? → sign undertaking, submit later)
→ College keeps some originals (TC, etc.), returns others → Receipt given → Data entered in system
→ Pending documents followed up manually
```

| Step | Who | Hands off to | Evidence |
|---|---|---|---|
| 1. Send document checklist | Admissions office | Student | [A] |
| 2. Bring originals + copies on reporting day | Student | Verification desk | [F] my own joining, 2023 |
| 3. Wait in queue | Student | – | [F] / [E] waiting time |
| 4. Check originals vs. copies | Desk staff | Admissions office | [A] |
| 5. Missing document → undertaking with due date | Staff + student | Admissions head (approves) | [A] |
| 6. Keep TC/originals, give receipt | Desk staff | Student | [A] |
| 7. Enter data, follow up pending documents | Admissions office | Student | [A] |

**Exceptions:** a document is missing (often the TC, because the old college hasn't issued it yet), the name or date of birth doesn't match across documents, a parent comes instead of the student, or a student later needs an original back. [A]

## 2. The problem
On reporting day, hundreds of students arrive with their documents at the same time. Problems are found **only at the desk**: a missing TC, a wrong copy, a name mismatch. That means long queues, repeat visits, and pending documents that are tracked by hand with no status the student can see. [A, to be confirmed with the admissions office]

## 3. Scale (estimates)
| Item | Value | Label |
|---|---|---|
| New students per intake (B.Tech) | ~600 | [E] |
| Student time on verification day (queue + check) | ~180 min | [F] mine was about 3 hours; used as the typical value [E] |
| Students with at least one pending or wrong document | ~30% | [E] |
| Extra visit for a pending document | ~60 min | [E] |
| Staff time per student | ~10 min (+10 min per follow-up) | [E] |

**Current total ≈ 600 × 211 min ≈ 2,110 hours per intake** (student time plus staff time; see [time-saved.md](time-saved.md)).

## 4. Proposed process [P]

**Idea:** check documents **before** reporting day, so the desk only matches originals.

```
Admission confirmed → Student uploads scans on a form (before joining)
→ Staff pre-check → Needs-Correction (student fixes from home) or Pre-Verified
→ Reporting day: quick original match only → Complete
   (missing original → Pending-Document with due date + automatic reminder)
```

| Item | Design |
|---|---|
| **Inputs** | Application number; document type; scanned file (PDF/JPG); "original available?" yes/no; expected date if not |
| **Statuses** | Not-Started → Uploaded → Pre-Verified / Needs-Correction → Original-Verified → Complete; plus Pending-Document, Escalated |
| **Owner** | Admissions office in-charge (one named role) |
| **Approval boundaries** | Desk staff can verify standard documents. **Admissions head** approves undertakings, due-date extensions and name/DOB mismatches |
| **Fallback** | If the form or portal is down, use the paper checklist at the desk and upload the scans later. If the admissions head is absent, a deputy approves |
| **Privacy** | Scans are visible only to the student and admissions staff, and deleted after verification (except what the rules require keeping) |

Free tools would be enough for a first version: Google Form + Google Sheet for statuses + an email reminder add-on.

## 5. Tests
Five synthetic cases: [test-cases.md](test-cases.md). All five are handled by the design.

## 6. Time saved
Net time saved ≈ **1,487 hours per intake**, but **most of it is student time**. Staff save only about **17 hours**, because they take on new review and support work. See [time-saved.md](time-saved.md).

## 7. Limitations
- I couldn't interview admissions staff before the deadline, so most of the current process and all the numbers are **assumptions or estimates**. Only my own joining experience is a fact.
- Intake size and percentages are guesses and should be checked against office records (counts only, no personal data).
- Uploading scans adds a privacy risk, which needs proper access control.
- This is a design. It hasn't been built or tested with real users; the tests are synthetic.
