# Task 2 – Curriculum Audit and Redesign

**Programme:** B.Tech Computer Science and Engineering (Artificial Intelligence), ICFAI Foundation for Higher Education (IFHE), Hyderabad
**Admission batch:** 2023–2027  **Curriculum version:** ⚠️ not verified
**Target roles:** Data Analyst (DA), AI Engineer (AI), Full Stack Developer (FS)

> This is a **student proposal**. It is not an official syllabus revision. Labels used throughout: **[Verified]** = confirmed from an official document; **[Screenshot]** = transcribed from my syllabus screenshots; **[Unverified]** = not confirmed; **[Recommendation]** = my proposal.

---

## A. Source verification and what is missing

| What | Status | Source |
|---|---|---|
| Programme name "B.Tech CSE (Artificial Intelligence)" | **[Verified]** It appears as a programme in the official course handout | DS401 Human Computer Interaction course handout, IFHE (S1 in [source register](../sources/source-register.md)) |
| Course list and credits, Sem I–VII | **[Screenshot]** | My syllabus screenshots (S2) |
| Semester VIII | Internship. Code and credits **[Unverified]** | Told to me by my batch; no document seen |
| Total programme credits | **[Unverified]**. Sem I–VII + Summer = 151, plus the Sem VIII internship | Calculated from S2 |
| Curriculum version / regulation code | **Missing** | – |
| Academic regulations (graduation rules, electives, prerequisites, credit-change rules) | **Missing**. Not available publicly online; I searched on 2026-10-23 | – |
| Unit-level syllabus | Only **DS401 HCI** is available | S1 |

**Documents I still need** (to make this fully verified):
1. Official programme structure / curriculum PDF for the CSE (AI) 2023 batch, including Sem VIII
2. IFHE academic regulations or student handbook
3. Course handouts for CS206, CS205, DS304, DS305, CS307 and DS408

Because these are missing, every credit figure below is based on the screenshot data and is marked as such.

---

## B. Version 1 – Current curriculum (credit map)

Full data: [current-curriculum.csv](current-curriculum.csv). All rows are **[Screenshot]**. Required/elective status and prerequisites are **[Unverified]** because the regulations were not available.

| Semester | Courses (credits) | Total |
|---|---|---:|
| I | CS101 Computer Programming (4), MT102 Engineering Graphics (3), EG101 English Language Skills (3), CH102 Environmental Sciences (2), HS101 Essence of Indian Traditional Knowledge (0), MA101 Linear Algebra & ODE (3), PHY101 Physics (5) | 20 |
| II | EC101 Basic Electronics (4), CH101 Chemistry (4), CS102 Data Structures (4), MT101 Digital Fabrication (3), MA102 Higher Calculus (3), DS101 Intro to AI & DS (3), EG102 Professional Communication (3) | 24 |
| III | DS201 Artificial Intelligence (3), CS206 DBMS (4), MA202 Discrete Mathematics (3), EC201 Intro to IoT (3), ML201 Math Essentials for ML (3), CS201 OOP Concepts (4), CR201 Power Skills-I (1), HS201 Dynamics of Social Change (3) | 24 |
| IV | CS204 Computer Organization & Architecture (3), CS203 Design & Analysis of Algorithms (3), MG201 Engineering Economics & Management (3), DS202 Industry Coding Practice (Python/R) (3), CS302 Operating Systems (4), CR202 Power Skills-II (1), DS301 Soft Computing (3), CS205 Web-Enabled Technologies (4) | 24 |
| Summer II | IP201 Internship-I (3) | 3 |
| V | DS303 Blockchain Technology (3), CS306 Computer Networks (4), HS301 Constitution of India (0), DS305 Data Wrangling & Visualization (3), CS415 Ethical Hacking (3), DS304 Machine Learning (4), CR301 Power Skills-III (1), DS310 Predictive Analytics (3) | 21 |
| VI | DS307 Big Data Systems (3), DS306 Deep Learning (3), EC308 Embedded Systems (3), CR302 Power Skills-IV (1), SP301 Special Project (3), DS311 NLP (3), DS309 Pattern Recognition (3) | 19 |
| VII | CS305 Computer Vision (3), CS307 Cloud Computing (4), CS413 Quantum Computing (3), DS408 Generative AI (3), HS206 Professional Ethics (3) | 16 |
| VIII | Internship (credits unverified) | ? |
| **Total (I–VII + Summer)** | | **151** |

**Note:** the DS401 HCI handout lists CSE (AI) in its CO-PO mapping, but DS401 is not in my Sem I–VII screenshots. It may be an elective or from another semester. **[Unverified]**

---

## C. Job-role alignment

Job descriptions: see [job-description-analysis.md](job-description-analysis.md) (JD-1 Portcast Data Analyst Intern, 2026-08-07; JD-2 Keywords Studios AI Engineer Fresher, 2026-06-15; JD-3 Kulfi Software Engineer I Full-Stack, ~2026-10-19; JD-4 recruiter ML Engineer CV JD, undated). **Four postings are a sample, not the whole job market.**

**Important honesty note:** apart from DS401, I could not see syllabus units. So the ratings below are based on course **titles**, and I mark them as **Partial (title-only)** or **Unverified** unless the title is unambiguous. I can't yet tell whether a skill is only *introduced*, *practised* in labs, or *assessed* in practical work. That needs the course handouts.

### C1. Data Analyst
| Course | Sem / Cr | JD need supported | Rating | Reason | Gap |
|---|---|---|---|---|---|
| CS101, DS202 | I/4, IV/3 | Python (JD-1 R) | Partial (title-only) | DS202 explicitly says Python/R | Unknown whether scripting for data is practised |
| CS206 DBMS | III/4 | SQL (JD-1 R) | Partial (title-only) | DBMS normally includes SQL | Analytical SQL (aggregations, window functions) not confirmed |
| DS305 Data Wrangling & Viz | V/3 | Dashboards, reports (JD-1) | Partial (title-only) | Title matches directly | BI tool (Power BI/Tableau) not confirmed |
| DS310 Predictive Analytics | V/3 | Data-driven decisions | Unverified | – | Business context and communication of results |
| ML201, MA101 | III/3, I/3 | Statistics, attention to numbers | Weak | Maths for ML, not applied statistics | **No dedicated statistics course** |
| DS307 Big Data | VI/3 | Not in JD-1 | Unverified | – | – |
| EG101, EG102, MG201 | I, II, IV | Communication, business understanding (JD-1 R) | Partial | Communication courses exist | Data-storytelling not confirmed |
| – | – | Validating AI output (JD-1 R) | **Weak** | No course found | **Gap** |

### C2. AI Engineer
| Course | Sem / Cr | JD need supported | Rating | Reason | Gap |
|---|---|---|---|---|---|
| CS101, CS201 | I/4, III/4 | Python, OOP (JD-2 R) | Partial (title-only) | – | – |
| CS102, CS203 | II/4, IV/3 | DSA (JD-2 R) | Strong (title-only) | Titles match exactly | – |
| ML201, MA101, MA102 | I–III | ML maths | Partial | – | – |
| DS201, DS304, DS309 | III, V, VI | ML fundamentals (JD-2 R) | Strong (title-only) | Dedicated ML course with 4 credits | – |
| DS306, CS305 | VI, VII | Deep learning, CV (JD-4) | Partial (title-only) | – | PyTorch/OpenCV use not confirmed |
| DS311 NLP | VI/3 | NLP pipelines (JD-2) | Partial (title-only) | – | – |
| DS408 Generative AI | VII/3 | LLM features, RAG (JD-2) | Partial (title-only) | – | **RAG, LLM APIs and evaluation not confirmed** |
| CS205 | IV/4 | APIs with FastAPI (JD-2) | Unverified | – | API development not confirmed |
| CS307 Cloud | VII/4 | Deployment, DevOps (JD-4) | Partial (title-only) | – | Hands-on deployment not confirmed |
| – | – | Git, testing, MLflow (JD-4) | **Weak** | No course found | **Gap** |

### C3. Full Stack Developer
| Course | Sem / Cr | JD need supported | Rating | Reason | Gap |
|---|---|---|---|---|---|
| CS101, CS201 | I, III | Backend language: Python/Java (JD-3 P) | Partial (title-only) | – | – |
| CS102, CS203 | II, IV | Problem solving, debugging (JD-3 R) | Partial | – | – |
| CS206 DBMS | III/4 | SQL (JD-3 P) | Partial (title-only) | – | – |
| CS205 Web-Enabled Tech | IV/4 | Two layers: web + backend (JD-3 R), REST APIs (P) | Unverified | Only one web course in the programme | Modern framework and API work not confirmed |
| CS306, CS302 | V, IV | Networking, OS | Partial | Foundations | – |
| CS415 Ethical Hacking | V/3 | App security | Partial | – | – |
| CS307 Cloud | VII/4 | Cloud deployment, CI/CD (JD-3 P) | Partial (title-only) | – | CI/CD not confirmed |
| SP301, IP201 | VI, Summer | Shipped a real project (JD-3 R) | Partial | Project slots exist | Not required to be multi-layer or deployed |
| – | – | Testing own work, code review (JD-3 R) | **Weak** | No course found | **Gap** |

---

## D. Five-unit analysis

**Courses chosen:** I could only do a five-unit analysis for **DS401 Human Computer Interaction**, because it is the only course whose official unit structure I have. I chose not to invent units for other courses. The courses I would analyse next are CS205, CS206, DS305, DS408 and CS307, because they carry the most job-relevant skills (see section C). Their handouts are listed as missing in section A.

**DS401 Human Computer Interaction – 3 credits (L3 T0 P0)** [Verified, S1]

| Unit | Official topics (summary) | Roles | JD skill | Coverage | Evidence | Recommendation |
|---|---|---|---|---|---|---|
| I | HCI fundamentals; human cognition; input/output devices; VR/3D devices | FS | UX care (JD-3) | Strong for theory; outdated in places | Textbook T1 is Dix et al., 2004; covers "Paper: printing and scanning" | **UPDATE:** reduce older device content |
| II | Models of interaction; ergonomics; interaction styles; WIMP | FS | UX (JD-3) | Strong for theory | Sessions 9–16 | **KEEP** |
| III | Design process; scenarios; navigation and screen design; prototyping; usability heuristics | FS, DA (dashboard design) | Loading/empty/error states (JD-3) | Partial: no lab (P = 0) | L-T-P is 3-0-0, so no practical credits | **UPDATE:** add an assessed prototyping exercise (Figma or HTML) |
| IV | Windowing systems; UI toolkits (Tkinter, JavaFX); evaluation techniques; cognitive models | FS | Testing own work (JD-3) | Partial; tools outdated | R1 lists Tkinter and JavaFX, not modern web frameworks | **UPDATE:** use web UI tooling and run a usability test |
| V | Groupware; dialog design; AR/VR/mixed reality | AI (conversational) | Conversational AI (JD-2) | Partial | Dialog design is covered, but chatbots are not | **UPDATE:** add chatbot / AI-driven UX |

**The college agrees:** the handout's own "Gaps in the syllabus" section lists "Add topics on Chatbots, Emotion-aware UI, AI-driven UX design" and "Add dedicated lectures on ethical design and accessibility laws (e.g., WCAG)". This supports reason R11.

**Assessment:** 100% of DS401 marks come from assignments, a mid-term and an end-term exam [S1]. There is no project or lab component, so it doesn't test whether students can build and evaluate a real interface.

---

## E. Version 2 – Proposed curriculum

Full data: [proposed-curriculum.csv](proposed-curriculum.csv). Interactive view: [calculator/index.html](calculator/index.html).

### Summary of changes
| Action | Course | Current → Proposed credits | Reason |
|---|---|---|---|
| UPDATE | DS202 Industry Coding Practice | 3 → 3 | R1 |
| UPDATE | CS206 DBMS | 4 → 4 | R2 |
| UPDATE | CS205 Web-Enabled Technologies | 4 → 4 | R3 |
| UPDATE | DS305 Data Wrangling & Visualization | 3 → 3 | R5 |
| UPDATE | DS310 Predictive Analytics | 3 → 3 | R6 |
| UPDATE | CS307 Cloud Computing | 4 → 4 | R7 |
| UPDATE | DS408 Generative AI | 3 → 3 | R8 |
| REDUCE | PHY101 Physics | 5 → 3 | R9 |
| REDUCE | CH101 Chemistry | 4 → 2 | R9 |
| REDUCE | MT102 Engineering Graphics | 3 → 1 | R9 |
| REDUCE | EC101 Basic Electronics | 4 → 3 | R9 |
| REDUCE | MT101 Digital Fabrication | 3 → 2 | R9 |
| ADD | NEW-ST1 Applied Statistics & Probability for Data Analysis (Sem II) | 0 → 3 | R4 |
| ADD | NEW-SE1 Software Engineering & Testing Lab (Sem V) | 0 → 2 | R1 |
| ADD | NEW-CP1 Capstone: Admission Document Workflow (Sem VII) | 0 → 3 | R10 |
| KEEP | All other 39 courses | unchanged | – |

**Not removed on purpose:** Blockchain, Quantum Computing, Embedded Systems, IoT and the general-education courses are kept. They don't appear in my four JDs, but four JDs aren't enough reason to remove foundational or breadth courses.

### New courses [Recommendation – not official courses]

**NEW-ST1 Applied Statistics & Probability for Data Analysis**: Sem II, 3 credits (2 lecture + 1 lab). Prerequisite: MA101.
- Objectives: descriptive statistics; probability distributions; sampling; confidence intervals; hypothesis tests; correlation vs. causation; classification metrics (precision, recall, F1); doing all of this in Python.
- Why: no statistics course exists, yet JD-4 requires "statistics relevant to deep learning … to assess model's performance", and analysts must spot wrong numbers (JD-1).

**NEW-SE1 Software Engineering & Testing Lab**: Sem V, 2 credits (lab). Prerequisites: CS201, DS202.
- Objectives: Git branching and pull requests; code review; unit and integration tests (pytest/JUnit); a simple CI pipeline (GitHub Actions); debugging; checking AI-generated code.
- Why: JD-3 requires testing your own work, JD-3 and JD-4 mention CI/CD or DevOps, and no course title covers this.

**NEW-CP1 Capstone: Admission Document Workflow**: Sem VII, 3 credits. See section I.

### Three pathways (flexible, not all mandatory)

All students take the **common CSE (AI) core**: all KEEP and UPDATE courses plus NEW-ST1 and NEW-SE1. The pathway is chosen through the **existing project slots** (SP301 Special Project, IP201 Internship, NEW-CP1 Capstone), so no extra credits are needed.

| | Data Analyst | AI Engineer | Full Stack Developer |
|---|---|---|---|
| Key existing courses | CS206, DS305, DS310, DS307, MG201 | DS304, DS306, DS311, CS305, DS408 | CS205, CS206, CS306, CS415, CS307 |
| Updated courses that matter most | CS206 (SQL lab), DS305 (dashboards), DS310 (business cases) | DS408 (RAG), CS307 (deployment), DS202 (testing) | CS205 (APIs and deployment), DS202, CS307 |
| New content | NEW-ST1 Statistics | NEW-SE1 Testing Lab | NEW-SE1 Testing Lab |
| SP301 project focus | Dashboard plus analysis report on a public dataset | Train and serve a model behind an API | Multi-layer web app with tests |
| Capstone (NEW-CP1) role | Workflow metrics and time-saved dashboard | AI step, e.g. auto-checking requests for missing fields | Build the request portal and status tracking |

---

## F. Reasons for change (11)

| # | Issue observed | Course evidence | JD evidence | Change | Roles | Expected outcome | Trade-off |
|---|---|---|---|---|---|---|---|
| R1 | No course teaches testing, Git or CI | No such title in Sem I–VII [Screenshot] | JD-3: "tests their work" (required); CI/CD (preferred). JD-4: DevOps practices | UPDATE DS202 + ADD NEW-SE1 | FS, AI, DA | Students ship tested code under version control | Needs lab time and staff trained in CI tools |
| R2 | SQL practice level unknown | CS206 DBMS, 4 credits [Screenshot] | JD-1: Python and SQL required; JD-3: SQL preferred | UPDATE CS206: assessed analytical SQL lab | DA, FS | Can write join, aggregate and window queries | Less time for DB theory such as normal-form proofs |
| R3 | Only one web course; API work unconfirmed | CS205, 4 credits [Screenshot] | JD-3: work across two layers (required), REST APIs (preferred); JD-2: FastAPI services | UPDATE CS205: REST API plus deployed mini-project | FS, AI | Builds a working frontend + API + DB | Framework choice will date; teach concepts first |
| R4 | No statistics course | Only ML201/MA101 maths [Screenshot] | JD-4: statistics to assess model performance; JD-1: spot wrong numbers | ADD NEW-ST1 (3 cr) | DA, AI | Chooses and interprets the right metric | Uses credits taken from basic science (R9) |
| R5 | BI tool not confirmed | DS305 [Screenshot] | JD-1: dashboards, reports | UPDATE DS305: dashboard project with free Power BI / Looker Studio | DA | Publishes a dashboard with a written insight | Licensing; use free tools |
| R6 | Analytics without business context | DS310 [Screenshot] | JD-1: understand domain, product and customers | UPDATE DS310: case studies plus a stakeholder report | DA | Turns analysis into a recommendation | Finding real but shareable datasets |
| R7 | Cloud may be theory-only | CS307, 4 credits [Screenshot] | JD-3: cloud deployment; JD-4: deployment and DevOps | UPDATE CS307: Docker plus free-tier deployment lab | AI, FS | Deploys and monitors an app | Free-tier limits; need a no-card alternative |
| R8 | GenAI content unknown; no AI-output checking | DS408 [Screenshot] | JD-2: RAG, LLM features; JD-1: validate AI-generated output | UPDATE DS408: RAG lab plus output-validation exercise | AI, DA | Builds and evaluates a RAG app | API costs; use open models |
| R9 | Basic science/engineering credits are high for an AI branch | PHY101 = 5 credits, the largest Sem I course; CH101 4; MT102 3 [Screenshot] | None of the 4 JDs mention them (this alone isn't a reason to remove them) | REDUCE 5 courses by 8 credits total; **none removed** | All (frees credits) | Core science kept; credits move to R1, R4, R10 | **Must satisfy basic-science credit rules (AICTE / IFHE)**, which are not verified |
| R10 | Projects not required to be shipped or tested | SP301 3 cr, IP201 3 cr [Screenshot] | JD-3: "shipped at least one real project" (required); JD-4: end-to-end pipeline | ADD NEW-CP1 capstone + use SP301 for pathways | All | A tested, documented, demonstrable project | Supervision load on faculty |
| R11 | HCI has no practical component and dated tools | DS401: L-T-P 3-0-0; Tkinter/JavaFX; the handout's own gap list [Verified, S1] | JD-3: UX, loading/error states | UPDATE DS401 content (no credit change, not counted) | FS | Prototypes and usability-tests a real UI | DS401 status in my programme is unverified |

---

## G. Credit calculation, sequencing and regulations

**Definition of an affected credit:**
- every credit of an UPDATE course (its content changes), **plus**
- every credit moved from REDUCE courses into ADD courses, counted **once** (not once when removed and again when added).

A course is never counted twice. R11 (DS401) is excluded because its programme status is unverified.

| Item | Credits |
|---|---:|
| Current total (Sem I–VII + Summer) [Screenshot] | 151 |
| Credits updated (DS202 3 + CS206 4 + CS205 4 + DS305 3 + DS310 3 + CS307 4 + DS408 3) | 24 |
| Credits reduced (2 + 2 + 2 + 1 + 1) | 8 |
| Credits added (3 + 2 + 3) | 8 |
| Reallocated (counted once) = max(8, 8) | 8 |
| **Affected = 24 + 8** | **32** |
| **Affected % = 32 ÷ 151** | **21.2%** ✅ (target 20–25%) |
| Retained unchanged = 151 − 24 − 8 | 119 |
| Proposed total | 151 ✅ balanced |

**Effect of Semester VIII:** if the internship carries *X* credits, affected % = 32 ÷ (151 + X). The proposal stays within 20–25% only if X ≤ 9; beyond that it falls below 20%. Once X is known, the fix is to update 1–2 more courses (e.g., DS304 or CS305).

**Semester loads (current → proposed):** I 20→16, II 24→23, III 24→24, IV 24→24, Summer 3→3, V 21→23, VI 19→19, VII 16→19. No semester goes above the current maximum of 24.

**Prerequisites and sequencing:**
- NEW-ST1 (Sem II) needs MA101 (Sem I). It comes before DS304 ML (Sem V), so ML can rely on it.
- NEW-SE1 (Sem V) needs CS201 (III) and DS202 (IV). It comes before SP301 (VI), so the Special Project can require tests.
- NEW-CP1 (Sem VII) needs CS205, CS206 and NEW-SE1.
- Reducing EC101 still leaves the base for EC201 IoT and EC308 Embedded Systems.

**Approvals and regulatory conditions:**
- Changes would need the department **Board of Studies** and then the **Academic Council** of IFHE. The exact process is [Unverified] because the regulations aren't available.
- They could apply only to a **future batch**, not to the 2023 batch mid-programme.
- Reducing Physics, Chemistry and Graphics must respect any **minimum basic-science / engineering-science credits** in IFHE's regulations or AICTE model curriculum guidance. This is [Unverified] and is the biggest risk in the proposal.
- **If the credit changes aren't allowed:** apply R1–R8 as content and assessment updates within existing credits only (24 affected credits = 15.9%), and run NEW-SE1 as a non-credit workshop.

---

## H. AI-assisted exercises
See [ai-exercises.md](ai-exercises.md): five subjects (CS201, CS203, CS206, DS304, CS307), each with prompt, model, date, output, independent verification and result.

---

## I. Capstone: Admission Document Pre-Verification System (from Task 1)

Based on [Task 1](../task1-workflow/report.md). The Task 1 figures are estimates, so the capstone's first job is to measure them properly.

| Item | Proposal |
|---|---|
| Problem | New students' documents are checked only on reporting day, causing queues, repeat visits and manual follow-up of pending documents (Task 1, mostly assumptions and estimates) |
| Learning objectives | 1) Model a real process as states and transitions. 2) Build a validated multi-layer app (upload form → API → DB). 3) Enforce role-based access and approval limits. 4) Write tests for normal and failure cases. 5) Measure time saved and reliability |
| Prerequisites | CS205, CS206, NEW-SE1 (CS201 recommended) |
| Scope / inputs | Synthetic applicants only: application number, document type, scanned file, original available (yes/no), expected date. **No real student data** |
| Workflow | Not-Started → Uploaded → Pre-Verified / Needs-Correction → Original-Verified → Complete; also Pending-Document, Escalated |
| Owner / approval limits | Admissions office in-charge owns the process; desk staff verify standard documents; the admissions head approves undertakings, extensions and mismatches |
| Fallback | Paper checklist if the system is down (scans uploaded later); deputy approver if the head is absent |
| Test cases | The same 5 as Task 1 [test-cases.md](../task1-workflow/test-cases.md): normal, missing TC, duplicate upload, unauthorized access, portal down |
| Measurements | Median reporting-day time per student; % of students needing an extra visit; % of tests passing; net time saved = gross − review − support − setup effort |
| Rubric | Process model 20%, working app 25%, tests and failure handling 25%, metrics and report 20%, demo 10% |
| Pathways | FS: portal and API. AI: auto-check for missing or invalid fields. DA: metrics dashboard |
| Credits | 3. Comparable to SP301 Special Project (3 credits) for one semester of team project work |

---

## J. Faculty / graduate feedback and limitations

Feedback request message and record: [feedback-request.md](feedback-request.md). [TO FILL: who was contacted (role only), when, and the responses, or the "no response" statement.]

**Limitations:**
1. Course list and credits come from screenshots, not the official curriculum PDF. The curriculum version and regulations were not available.
2. Semester VIII credits are unknown, so the programme total and the affected % may change.
3. Only one course (DS401) has official unit-level evidence. All other alignment ratings are based on course titles.
4. Four job descriptions are a small sample. JD-1 is an internship, JD-2's details came from a listing copy I couldn't open directly, and JD-4 is undated.
5. The regulatory limits on reducing basic-science credits are unverified.
6. This is a student proposal. It has not been reviewed or approved by IFHE.

---

## K. Interactive tool
[calculator/index.html](calculator/index.html): role, semester and action filters; current vs. proposed comparison; rationale per course; affected-credit and balance calculation; input validation. Tests T1–T4 pass. See [calculator/README.md](calculator/README.md).

## L. Sources
[../sources/source-register.md](../sources/source-register.md)
