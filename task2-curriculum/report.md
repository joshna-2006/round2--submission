# Task 2 – Curriculum Audit and Redesign

**Programme:** B.Tech Computer Science & Engineering (Artificial Intelligence), IFHE Hyderabad · **Batch:** 2023–2027 · **Target roles:** Data Analyst (DA), AI Engineer (AI), Full Stack Developer (FS)

> Student proposal, not an official syllabus revision. Labels: **[Official]** = IFHE program-structure page · **[Screenshot]** = my own semester screenshots · **[Unverified]** · **[Proposal]**.

---

## A. Sources and what they verify

| Source | What it verifies | Limits |
|---|---|---|
| **S1 IFHE program-structure page** (ifheindia.org, accessed 2026-10-23) [Official] | The CSE (AI) programme exists; course titles and L-T-P-C credits for Sem I–VI; summer internship 5 credits; **Sem VIII Internship IP401 = 15 credits**; AI elective list | **No batch, year or version stated.** No total credits. Elective credit values not stated for some slots |
| **S2 My screenshots** [Screenshot] | The courses and credits of **my** Sem I–VII | Not an official document |
| **S3 DS401 handout** [Official] | Units of one course | One course only |

### The two sources disagree
I compared them course by course in [current-curriculum.csv](current-curriculum.csv):

| Result | Courses |
|---|---|
| Same course, same credits | **30 of 52** |
| Same course, different semester | 6 (e.g. Chemistry Sem II vs I, Computer Vision Sem VII vs VI) |
| **Different credits** | Physics **5 vs 4**, Industry Coding Practice **3 vs 4**, Summer internship **3 vs 5**, Deep Learning **3 vs 4** |
| Not on the official page | ML201 (the page has **BS105 Probability & Statistics** instead), Pattern Recognition, and my 5 Sem VII courses (the page lists "Electives PE/OE (5)", so these are probably my electives) |
| Course codes | All different (my CS101 = their ES105, etc.) |

**My interpretation [Unverified]:** the web page is probably a **newer curriculum version** than the one my 2023 batch follows. So I use **my screenshots as the baseline**, because they are my actual courses, and take **only Sem VIII (IP401, 15 credits)** from the official page, since my screenshots don't include it. Where the newer official version already changed something, I use that as **evidence of the college's own direction**.

**Still missing:** the regulations/handbook (graduation and credit-change rules) and the curriculum version code for my batch.

---

## B. Version 1 – Current curriculum

| Sem | Credits | Source |
|---|---:|---|
| I | 20 | Screenshot |
| II | 24 | Screenshot |
| III | 24 | Screenshot |
| IV | 24 | Screenshot |
| Summer II | 3 | Screenshot (official page says 5) |
| V | 21 | Screenshot |
| VI | 19 | Screenshot |
| VII | 16 | Screenshot (5 electives) |
| VIII | 15 | Official page (IP401 Internship) |
| **Total** | **166** | 151 from screenshots + 15 |

The full course list is in [current-curriculum.csv](current-curriculum.csv). Required vs. elective status is **[Unverified]**, apart from what the official page shows.

---

## C. Job-role alignment

The job descriptions are in [job-description-analysis.md](job-description-analysis.md): JD-1 Portcast Data Analyst Intern (2026-08-07), JD-2 Keywords Studios AI Engineer Fresher (2026-06-15, partly verified), JD-3 Kulfi Software Engineer I Full-Stack (~2026-10-19), JD-4 recruiter's ML Engineer (CV) JD (undated). **Four postings are a sample, not the job market.**

**How to read the ratings:** without unit-level handouts I can't tell whether a skill is only *introduced*, *practised* in a lab, or *assessed*. The one handout I have (DS401) showed that a modern-sounding title can be theory-only ([units-analysis.md](units-analysis.md)). So every rating below is **title-based** unless marked otherwise. L-T-P from the official page is used as a hint: P > 0 means there is lab time.

| Need (from JDs) | DA | AI | FS | My courses | Lab time? (official L-T-P) | Rating |
|---|---|---|---|---|---|---|
| Python programming | R | R | P | CS101, DS202 | Yes (2-0-4, 2-1-2) | Strong |
| SQL | R | – | P | CS206 DBMS | Yes (2-1-2) | Partial: analytical SQL unknown |
| Data structures & algorithms | – | R | – | CS102, CS203 | CS102 yes | Strong |
| Statistics for evaluation | detail | – | – | ML201 (maths for ML) | No (not on page) | **Weak**: no course titled statistics in my batch |
| ML fundamentals | – | R | R | DS304, DS309 | Yes (3-0-2) | Strong |
| NLP / LLM / RAG | – | R | – | DS311, DS408 | DS311 no (3-0-0) | Partial: RAG unknown |
| REST APIs / backend | – | R | P | CS205 | Yes (2-1-2) | **Unverified**: official title says "WEB 3.0" |
| Dashboards / reports | R | – | – | DS305 | Yes (2-0-2) | Partial: tool unknown |
| Testing own code, code review | – | – | R | – | – | **Gap** |
| Git / CI/CD / DevOps | – | – | P | maybe DS202 | – | **Gap** |
| Cloud deployment | – | – | P | CS307 (elective) | Unknown | Partial |
| Shipped multi-layer project | – | – | R | SP301, IP201 | Project | Partial: not required to be shipped or tested |
| Validating AI output | R | – | P | – | – | **Gap** |
| Communication | R | – | R | EG101, EG102, CR201–302 | – | Strong |
| Computer vision | – | – | – | CS305 (JD-4 required) | No (3-0-0) | Partial |

**Main finding:** the AI theory is well covered. The weakest area is **engineering practice** (testing, Git/CI, deployment, checking AI output), which appears in 3 of the 4 JDs.

---

## D. Five-unit analysis
See [units-analysis.md](units-analysis.md). It contains a full five-unit analysis of DS401 (the only handout I have), the five priority courses whose handouts I still need, and a template for each. **Not complete for the priority courses.**

---

## E. Version 2 – Proposed curriculum

Full data: [proposed-curriculum.csv](proposed-curriculum.csv) · Interactive: [calculator/](calculator/)

| Action | Course | Credits | Reason |
|---|---|---|---|
| UPDATE | ML201 → add probability & statistics units | 3 → 3 | R4 |
| UPDATE | CS206 DBMS: assessed analytical SQL lab | 4 → 4 | R2 |
| UPDATE | DS202 Industry Coding Practice: Git, code review, unit tests | 3 → 3 | R1 |
| UPDATE | CS205 Web-Enabled Tech: REST API + deployed two-layer project | 4 → 4 | R3 |
| UPDATE | DS305 Data Wrangling & Viz: assessed dashboard | 3 → 3 | R5 |
| UPDATE | DS310 Predictive Analytics: business cases + written recommendation | 3 → 3 | R6 |
| UPDATE | DS304 Machine Learning: one end-to-end evaluated project | 4 → 4 | R9 |
| UPDATE | SP301 Special Project: Task 1 workflow as a project option | 3 → 3 | R11 |
| UPDATE | CS307 Cloud Computing: deployment lab | 4 → 4 | R7 |
| UPDATE | DS408 Generative AI: RAG + AI-output verification | 3 → 3 | R8 |
| REDUCE | PHY101 Physics | 5 → **4** | R10 (same as the official BS102) |
| REDUCE | MT102 Engineering Graphics | 3 → 2 | R10 |
| REDUCE | EC101 Basic Electronics | 4 → 3 | R10 |
| ADD | **NEW-SE1 Software Testing & DevOps Lab** (Sem V) | 0 → 3 | R1 |
| KEEP | all other 39 courses, including Sem VIII internship | unchanged | – |

**What I chose not to do:** I don't remove Chemistry, Blockchain, Quantum Computing, Embedded Systems or the humanities courses just because the four JDs don't mention them. Four job ads aren't enough reason to remove foundations or breadth.

### NEW-SE1 Software Testing & DevOps Lab [Proposal]
- **Semester:** V · **Credits:** 3 (L1-T0-P4) · **Prerequisites:** CS201 OOP, DS202 Industry Coding Practice
- **Objectives:** use Git branches and pull requests; write unit and integration tests; set up a CI pipeline that runs tests on every push; review a classmate's code; check AI-generated code with tests
- **Why:** neither my curriculum nor the newer official one has a testing or DevOps course, yet JD-3 requires "tests their work" and JD-3/JD-4 mention CI/CD and DevOps. This repository's own GitHub Actions check is a small example of what students would build.

### Three pathways (flexible, nothing extra is mandatory)
Everyone takes the common core, i.e. every KEEP/UPDATE course plus NEW-SE1. The pathway is chosen through **choices that already exist**: Sem V–VII electives, the SP301 project topic, and the internship.

| | Data Analyst | AI Engineer | Full Stack Developer |
|---|---|---|---|
| Core courses that matter most | CS206, DS305, DS310, DS307, ML201 | DS304, DS306, DS311, CS305, DS408 | CS205, CS206, CS306, CS415, NEW-SE1 |
| Electives (from the official AI elective list) | Data Science specialization (AI421–425), e.g. AI425 Analytics Tools | AI Specialization (AI401–405), e.g. AI403 Responsible AI | Cloud Computing (CS307), plus NoSQL (AI406) |
| SP301 project | Dashboard + analysis on a public dataset | Trained model served behind an API | Task 1 ID card workflow as a web app |
| Missing content still needed | – | RAG (in DS408 update) | REST APIs (in CS205 update) |

---

## F. Reasons for the redesign (11)

| # | Issue | Course evidence | Job evidence | Change | Roles | Outcome | Trade-off |
|---|---|---|---|---|---|---|---|
| R1 | No testing or CI | No such course in my screenshots **or** on the official page | JD-3: "tests their work" (required), CI/CD (preferred); JD-4: DevOps | UPDATE DS202 + ADD NEW-SE1 | FS, AI, DA | Ships tested code under version control | Needs lab time and staff who know CI |
| R2 | SQL depth unknown | CS206, 4 cr, lab 2-1-2 [Official] | JD-1: "Python and SQL … write a query" | Assessed analytical SQL lab | DA, FS | Writes join/aggregate/window queries | Less time for DB theory |
| R3 | Only one web course; title says "WEB 3.0" | AI208 title [Official] | JD-3: two layers (required), REST APIs (preferred); JD-2: FastAPI | REST API + deployed two-layer project | FS, AI | Builds frontend + API + DB | May reduce Web3 content |
| R4 | No statistics course in my batch | ML201 in my Sem III; the newer official structure has **BS105 Probability & Statistics** in its place | JD-4: "statistics … to assess model's performance" | Add statistics units to ML201 | DA, AI | Chooses and interprets the right metric | ML201's maths content gets squeezed |
| R5 | Dashboard tool not confirmed | DS305, lab 2-0-2 | JD-1: dashboards and reports | Assessed dashboard with a free BI tool | DA | Publishes a dashboard with an insight | Tool licences, so use free tools |
| R6 | Analytics without business context | DS310, 3-0-0 (no lab) | JD-1: understand domain, product, customers | Case studies + written recommendation | DA | Turns analysis into a decision | Finding shareable data |
| R7 | Deployment may be theory-only | CS307 (my elective) | JD-3: cloud deployment; JD-4: deployment, DevOps | Docker + free-tier deployment lab | AI, FS | Deploys and monitors an app | Free tiers change (see AI exercise 5) |
| R8 | RAG unknown; no AI-output checking | DS408 (my elective) | JD-2: RAG, LLM features; JD-1: validate AI output | RAG lab + verification exercise | AI, DA | Builds and evaluates a RAG app | API costs, so use open models |
| R9 | ML may stop at training | DS304, 3-0-2 | JD-4: end-to-end pipeline, statistics, MLflow | One end-to-end evaluated project | AI | Reports results with uncertainty | Bigger project load |
| R10 | Small reallocation from basic science/engineering | Physics is 5 cr in my batch but **4 in the official newer version**; Graphics 3, Electronics 4 | Not in JDs (not a reason by itself) | Physics 5→4, Graphics 3→2, Electronics 4→3 | All | Frees 3 credits for R1 | **Must meet basic-science credit rules (unverified)**; Graphics and Electronics cuts are my judgement only |
| R11 | Projects not required to be shipped and tested | SP301 0-0-6, 3 cr | JD-3: "shipped at least one real project" (required) | Task 1 workflow offered as an SP301 project | All | A tested, demoable project | Supervision load |

---

## G. Credit calculation, sequencing and approvals

**Affected credit** = every credit of an UPDATE course, plus every credit moved from REDUCE to ADD, **counted once**. No course is counted twice. All numbers below are produced by [check_credits.py](check_credits.py).

| | With Sem VIII (main figure) | Sem I–VII only |
|---|---:|---:|
| Current total | 166 | 151 |
| Updated (3+4+3+4+3+3+4+3+4+3) | 34 | 34 |
| Reallocated: reduced 3, added 3 → counted once | 3 | 3 |
| **Affected** | **37** | **37** |
| **Affected %** | **22.3%** (in range) | **24.5%** (in range) |
| Proposed total | 166, balanced | 151, balanced |
| Retained unchanged | 129 | 114 |

The figure stays within 20–25% **whether or not** the Sem VIII credits are counted, so the uncertainty about Sem VIII doesn't change the conclusion.

**Semester loads (current → proposed):** I 20→18, II 24→23, III–IV unchanged, V 21→24, VI–VIII unchanged. No semester goes above 24, the current maximum.

**Prerequisites:**
- NEW-SE1 (Sem V) comes after CS201 (III) and DS202 (IV), and before SP301 (VI), so Special Projects can require tests.
- Statistics units in ML201 (III) come before DS304 ML (V).
- The CS205 API work (IV) comes before CS307 deployment (VII).

**Approvals [Unverified]:** curriculum changes would normally go through the department Board of Studies and then the Academic Council. They would apply to a future batch, not mine. Reducing Physics must respect any minimum basic-science credits. The newer official structure already has Physics at 4, which suggests 4 is acceptable.

**If credit changes aren't allowed:** apply only the 10 UPDATEs (34 credits = 20.5% of 166) and run NEW-SE1 as a non-credit workshop.

---

## H. AI-assisted exercises
[ai-exercises.md](ai-exercises.md): five subjects (CS201, CS203, CS206, DS304, CS307). Exercises 1–4 are checked automatically by [ai-outputs/verify.py](ai-outputs/verify.py) (9 of 9 checks pass). Exercise 5 was checked against official AWS pages, and the AI's answer was **partly outdated**.

---

## I. Capstone / lab from Task 1: ID Card Replacement System (SP301 option)

| Item | Proposal |
|---|---|
| Problem | Replacing a lost/damaged ID card may need several visits with no status visibility. This is hypothesis H1 from [Task 1](../task1-workflow/README.md), not yet confirmed |
| Learning objectives | 1) Model a process as states and transitions. 2) Build a validated multi-layer app. 3) Enforce role-based permissions and an approval boundary. 4) Write automated tests for normal and failure cases. 5) Measure time saved with real data |
| Prerequisites | CS205, CS206, NEW-SE1 |
| Inputs / scope | Synthetic students only: reason, photo attached, declaration, charge cleared. No real student data |
| Workflow | SUBMITTED → NEEDS_INFO → VERIFIED → (ESCALATED) → APPROVED → PRINT_FAILED/READY → COLLECTED; REJECTED |
| Owner / approvals | Admin officer owns the process; admin head approves 3rd+ replacements (illustrative boundary) |
| Fallback | Temporary pass on printer failure; manual card after a 2nd failure; paper form if the system is down |
| Test cases | The 5 required cases, already automated in [task1-workflow/prototype/](../task1-workflow/prototype/). Students extend them |
| Measurements | Visits per request, days to card, % needing info, tests passing, net time saved via `savings.py` |
| Rubric | Process model 20% · working app 25% · tests and failure handling 25% · measured evaluation 20% · demo 10% |
| Pathways | FS: web app + API · AI: auto-check the uploaded photo for quality · DA: dashboard of request times |
| Credits | Uses SP301's existing 3 credits (0-0-6), so no new credits are needed |

---

## J. Feedback and limitations

**Feedback:** a request message is ready in [feedback-request.md](feedback-request.md). **No curriculum feedback had been received when this was written.** A faculty member did share information about college administration, which I used for Task 1, but that isn't feedback on this redesign.

**Limitations:**
1. My course list comes from screenshots. The only official structure I found states no batch or version, and 22 of 52 courses differ from it.
2. Regulations (graduation rules, credit-change rules) were not available.
3. Only one handout (DS401) gives units. The priority courses are rated from titles and L-T-P only.
4. JD-2 is only partly verified, and JD-4 is undated. Four JDs are a sample.
5. The R10 reductions for Graphics and Electronics are my judgement, without official support.
6. This is a student proposal. IFHE has not reviewed or approved it.

---

## K. Interactive tool
[calculator/](calculator/): filters, current vs. proposed comparison, rationale, comparison with the official page, a Sem VIII toggle and live checks. 5 browser tests passed; the same totals come from `check_credits.py`.

## L. Sources
[../sources/source-register.md](../sources/source-register.md)
