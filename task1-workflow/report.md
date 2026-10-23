# Task 1 – Department Equipment Purchase Approval

**Process studied:** how a department at IFHE buys equipment (for example, computers for a lab) from a vendor: request → vendor quotations → approvals → purchase → payment.

**Why this process:** a faculty member described it to me, so there is real evidence. It also has a clear approval hierarchy, money-based decisions and several places where it can go wrong.

**Labels:** **[F]** Fact (told to me by faculty) · **[E]** Estimate · **[A]** Assumption (not confirmed) · **[P]** Proposed design. Evidence: [evidence-log.md](evidence-log.md).

---

## 1. Current process

What the faculty member told me [F]:
- Purchases go through **budget and vendor** steps, where **price, service and configuration/quantity** are compared.
- What is bought **depends on the department's activity**.
- The approval **hierarchy** is HOD, Deans, Director, Vice Chancellor and management, with the **Governing Body at the head office (Panjagutta)** as the **financial authority**.
- **Accounts** and **admin** offices are involved.

How the steps probably fit together [A]:
```
HOD writes request (item, quantity, reason)
→ Department collects vendor quotations (price, service, configuration)
→ Dean approves → Director approves → VC approves
→ Large amounts: Governing Body, head office (financial authority)
→ Accounts raises purchase order → Vendor delivers → Accounts pays
```

| Step | Who | Hands off to | Evidence |
|---|---|---|---|
| 1. Request with item, quantity, reason | HOD / department | Dean | [A] |
| 2. Vendor quotations: price, service, configuration | Department | Approvers | [F] the comparison points; [A] who collects them |
| 3. Approvals | Dean → Director → VC | Next level | [F] the hierarchy exists; [A] the order |
| 4. Final financial approval (big amounts) | Governing Body, Panjagutta head office | Accounts | [F] it is the financial authority |
| 5. Purchase order, delivery, payment | Accounts / admin, vendor | Department | [F] accounts and admin are involved; [A] the exact steps |

**Exceptions** [A]: a missing or incomplete quotation; an approver who is away; the same item requested twice; a vendor who delivers late or delivers the wrong configuration.

## 2. The problem
A paper file moves **one office at a time**, so [A, to be confirmed]:
- nobody can see **where a request is stuck**
- a **missing quotation** found at a later level sends the file **back to the start**
- **small purchases** may go through the **same long chain** as big ones
- departments wait **weeks** for equipment they need for teaching

## 3. Scale (estimates)
| Item | Value | Label |
|---|---|---|
| Purchase requests per year (whole university) | ~200 | [E] |
| Staff effort per request (preparing, quotations, approvals, accounts) | ~8.6 hours | [E] |
| Requests sent back for missing information | ~30% | [E] |
| Time from request to delivery | ~30 days | [E] |

**Current effort ≈ 200 × 516 min ≈ 1,720 staff hours per year** (see [time-saved.md](time-saved.md)).

## 4. Proposed process [P]

**Idea:** one **tracked digital request**, checked for completeness at the start, with **approval limits based on the amount**, so small purchases don't climb the whole ladder.

```
Draft → Submitted → (complete? 3 quotations attached?) → Under-Approval
  → approvers needed depend on amount → Approved → PO-Issued → Delivered → Paid → Closed
  (incomplete → Returned-for-Info · rejected → Rejected · problem → On-Hold)
```

| Item | Design |
|---|---|
| **Inputs** | Department; item and configuration; quantity; reason (linked to department activity); budget head; 3 vendor quotations (price, service/warranty, configuration); total amount |
| **Statuses** | Draft, Submitted, Returned-for-Info, Under-Approval (shows which level), Approved, Rejected, PO-Issued, Delivered, Paid, Closed, On-Hold |
| **Accountable owner** | Purchase/Accounts officer: one named role that owns every request from Submitted to Closed |
| **Approval limits** (example values [A]) | Up to ₹50,000: HOD + Dean · ₹50,000–₹5 lakh: + Director · ₹5–25 lakh: + VC · Above ₹25 lakh: + Governing Body (financial authority) |
| **Fallback** | System down: paper file on the same form, entered later. Approver away for more than 3 days: a delegated approver at the same level. Vendor fails: the next-best quotation is used |
| **Controls** | Nobody approves above their limit; the system blocks it. Accounts audits small purchases every month |

Free tools would be enough for a first version: Google Form + Google Sheet for statuses + email notifications.

## 5. Tests
Five synthetic cases: [test-cases.md](test-cases.md).

## 6. Time saved
Net saving ≈ **510 staff hours per year**, after counting the new review, support and setup work. Small purchases should also arrive faster. See [time-saved.md](time-saved.md).

## 7. Limitations
- The faculty member gave a **summary**. The exact step order, the approval amounts and all numbers are **assumptions or estimates** and should be confirmed with the Accounts office.
- I didn't see real purchase files. That is correct, because they contain vendor prices and financial data.
- The approval limits are example values. The real limits are set by IFHE's financial rules.
- This is a design walk-through, not a working system. The tests are synthetic.
