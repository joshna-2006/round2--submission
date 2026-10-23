# Benchmarks: how other universities handle ID card replacement

These are **public documents from other institutions, not IFHE**. They show what a real replacement process usually involves, and I used them to shape the design. They **do not prove anything about IFHE's process**. That still has to be checked (V1–V9). Fee amounts and bank details are deliberately not copied.

| | NIT Calicut (E3) | Thapar Institute, Patiala (E4) |
|---|---|---|
| Document | "Application for Duplicate Identity Card" form | "Procedure for Issue of duplicate ID Card in case of Lost/Damage/Updation" + form |
| Student provides | Form; where it was lost; **previous losses and number of duplicates issued**; fee receipt; declaration | Form; **FIR copy if lost**, or old card if damaged/updating; finance receipt; declaration |
| Offices involved | Faculty Advisor → Head of Department → Library → Main Computer Centre → Academic Section | Finance (payment) → Dean of Student Affairs (approval) → Library (ID-card room: old card suspended, new card issued) |
| Number of separate sign-offs | **5** | **3** (+ bank payment) |
| While waiting | A **duplicate paper card** is issued first, and the smart card is prepared later | Not stated |
| Old card | Must be surrendered if found | Must be returned if found; **old card suspended** |

URLs (accessed 2026-10-23):
- NIT Calicut: https://nitc.ac.in/imgserver/uploads/attachments/form-for-issue-of-duplicate-identity-cards-to-the-students_340_0.pdf
- Thapar: https://thapar.edu/upload/files/Lost_Damage_Updation.pdf

## What I took from them
| Observation | How it changed my design |
|---|---|
| Both need **several offices** to sign | Supports hypothesis H1 (several visits) as **plausible**. Not proof for IFHE |
| NIT Calicut asks how many times a duplicate was issued before | My **approval boundary**: a 3rd+ replacement goes to the admin head |
| NIT Calicut issues a **temporary paper card** | My **temporary pass** fallback |
| Thapar needs an **FIR for lost cards** and the **old card for damaged** | Proof now depends on the reason. FIR is a setting (`REQUIRE_FIR_FOR_LOST`) because IFHE's rule is unknown (V9) |
| Thapar **suspends the old card** | COLLECTED deactivates the old card |
