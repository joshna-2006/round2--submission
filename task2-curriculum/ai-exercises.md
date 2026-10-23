# AI-Assisted Exercises (5 subjects)

- **Model:** Claude Opus 5.5 (Anthropic), used through the Claude desktop app
- **Date:** 2026-10-23
- **How I checked:** I ran the code and SQL in [ai-outputs/verify.py](ai-outputs/verify.py) with Python 3 and SQLite, and compared the cloud claims with official AWS pages.

| # | Subject | Result |
|---|---|---|
| 1 | CS201 OOP | Correct (after checking a claim) |
| 2 | CS203 DAA | Correct |
| 3 | CS206 DBMS | Correct, but the test showed a common trap |
| 4 | DS304 ML | Correct |
| 5 | CS307 Cloud | **Partly correct** (outdated info) |

---

### 1. CS201 OOP Concepts
**Prompt:** `Show method overriding and method overloading in Python using a Shape class with Circle and Rectangle subclasses.`

**AI output (summary):** Circle and Rectangle override `area()`. It said Python has **no real method overloading**, and used a default argument (`describe(unit=None)`) to get the same effect.

**How I checked:** Ran the code. Output: `Circle with area 12.57`, `Rectangle with area 12.00`. I also wrote a class with two methods named `f` with different parameters. The second one replaced the first and gave `TypeError`. So the AI's claim about overloading is true.

**What I learned:** Java-style overloading doesn't carry over to Python. If OOP is taught only in Java, students may wrongly assume it does.

### 2. CS203 Design and Analysis of Algorithms
**Prompt:** `Solve T(n) = 2T(n/2) + n using the Master theorem. Then trace merge sort on [38, 27, 43, 3, 9, 82, 10].`

**AI output (summary):** a=2, b=2, f(n)=n = n^(log₂2), so case 2 gives **Θ(n log n)**. The trace ended in `[3, 9, 10, 27, 38, 43, 82]`.

**How I checked:** Worked out the Master theorem by hand and got the same answer. Ran merge sort in Python and printed every merge step; it matched the AI's trace. I also computed T(n) ÷ (n log n): it came out as 1.10, 1.07 and 1.06 as n grew, which stays steady as expected for Θ(n log n).

### 3. CS206 Database Management Systems
**Prompt:** `Tables Student(sid, name, dept) and Enrollment(sid, course_id, grade). Write SQL to find departments where more than 2 students got grade 'A'.`

**AI output:**
```sql
SELECT s.dept, COUNT(DISTINCT s.sid) AS students_with_a
FROM Student s JOIN Enrollment e ON s.sid = e.sid
WHERE e.grade = 'A'
GROUP BY s.dept HAVING COUNT(DISTINCT s.sid) > 2;
```

**How I checked:** I made a small fake database. CSE has 3 different students with A. ECE has only 2, but one ECE student has three A's. Working it out by hand, the answer should be **CSE only**.
- AI query → `[('CSE', 3)]` ✅
- The same query with `COUNT(*)` instead → `[('CSE', 3), ('ECE', 4)]` ❌. It counts grades, not students.

**What I learned:** Code can look right and still be wrong. You only catch this kind of mistake by testing with tricky data.

### 4. DS304 Machine Learning
**Prompt:** `TP=40, FP=10, FN=20, TN=130. Calculate accuracy, precision, recall and F1. Why can accuracy be misleading?`

**AI output:** accuracy 0.85, precision 0.80, recall 0.667, F1 0.727. It said accuracy is misleading because the classes are imbalanced.

**How I checked:** Hand calculation and Python gave the same numbers. I also checked the "imbalance" claim: a model that always predicts "negative" already gets **0.70 accuracy**, so 0.85 is less impressive than it looks.

### 5. CS307 Cloud Computing
**Prompt:** `What is the AWS free tier for EC2 and Lambda? Give exact limits.`

**AI output (summary):** EC2 gives 750 hours/month of t2.micro/t3.micro for 12 months. Lambda gives 1 million requests and 400,000 GB-seconds per month.

**How I checked:** Read the official pages on 2026-10-23.
- Lambda: https://aws.amazon.com/lambda/pricing/ says "one million requests and 400,000 GB-seconds per month" ✅
- EC2: https://aws.amazon.com/free/ now describes a **credit-based free plan**: $100 in credits, up to $200 total, and the account lasts 6 months. It doesn't mention "750 hours for 12 months" ❌. **The AI's EC2 answer is outdated.**

**What I learned:** AI can be confidently out of date about things that change, like prices and limits. Cloud courses should teach students to check official docs.

---

**Overall:** The AI was reliable on standard theory (exercises 2 and 4), but needed testing for code (exercise 3) and was outdated on cloud facts (exercise 5). This supports reasons R1 and R8 in the report: teach testing and AI-output checking.
