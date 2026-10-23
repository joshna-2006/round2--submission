# Synthetic Test Cases

All data is fake (REQ-01 etc.). These are walk-throughs of the proposed design, **not real observations**. Approval limits are the example values from the report.

| # | Case | Input | Expected result | Final status | Recovery |
|---|---|---|---|---|---|
| 1 | **Normal** | REQ-01: CSE dept, 5 monitors, ₹40,000, 3 quotations attached | Needs only HOD + Dean (under ₹50,000). Both approve; Accounts issues the PO | Approved → PO-Issued → Delivered → Paid → Closed | – |
| 2 | **Missing information** | REQ-02: lab PCs, ₹4 lakh, only **2 quotations** | The system won't move it to approval | Returned-for-Info | Department adds the 3rd quotation and resubmits; it continues from where it was |
| 3 | **Duplicate** | REQ-03: CSE requests the same 5 monitors again within 30 days | Flagged as a possible duplicate of REQ-01 and linked to it | On-Hold | HOD confirms whether it's a genuine second need; if not, it is Rejected |
| 4 | **Unauthorized request** | REQ-04: ₹8 lakh, and the HOD tries to give final approval | Blocked: above the HOD's limit. Routed to Dean → Director → VC | Under-Approval (VC level) | Logged for the Accounts audit; no PO can be raised without the right approvals |
| 5 | **Failed step** | REQ-05: approved, but the vendor misses the delivery date by 2 weeks | Owner is alerted | On-Hold | Next-best quotation vendor is contacted; the PO is re-issued after approver sign-off |

## Results (design walk-through, 2026-10-23)
| # | Handled? | Note |
|---|---|---|
| 1 | Yes | Small purchases skip Director/VC, which is the main time saving |
| 2 | Yes | Simple "3 files required" rule |
| 3 | Yes | Needs a rule: same department + same item within 30 days |
| 4 | Yes | Needs each user's approval limit stored |
| 5 | Yes | Depends on keeping the other quotations on file |
