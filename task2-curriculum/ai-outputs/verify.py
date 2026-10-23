"""
Independent checks for the 5 AI-assisted exercises (see ../ai-exercises.md).
Each check compares the AI's answer with something I can compute or run myself.
Exercise 5 (cloud) is checked against official AWS pages, not code, so it is not here.

Run:  py verify.py      -> prints each check and exits with an error if one fails
"""
import math
import sqlite3
import sys

results = []


def check(name, condition, detail=""):
    results.append(condition)
    print(f"[{'PASS' if condition else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


# ---- Ex1 CS201 OOP: the AI's code, run as given --------------------------------
class Shape:
    def area(self):
        return 0

    def describe(self, unit=None):
        text = f"{type(self).__name__} with area {self.area():.2f}"
        return text if unit is None else f"{text} {unit}^2"


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14159 * self.r ** 2


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h


check("Ex1 overriding: Circle(2) area", Circle(2).describe() == "Circle with area 12.57")
check("Ex1 overriding: Rectangle(3,4) area", Rectangle(3, 4).describe("cm") == "Rectangle with area 12.00 cm^2")


class T:  # AI claim: Python has no Java-style overloading; the 2nd def replaces the 1st
    def f(self, a):
        return "one"

    def f(self, a, b):  # noqa: F811  (deliberate redefinition)
        return "two"


try:
    T().f(1)
    overloading_absent = False
except TypeError:
    overloading_absent = True
check("Ex1 claim 'Python has no method overloading'", overloading_absent)

# ---- Ex2 CS203 DAA ------------------------------------------------------------
merges = []


def merge_sort(a):
    if len(a) <= 1:
        return a
    m = len(a) // 2
    left, right = merge_sort(a[:m]), merge_sort(a[m:])
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out += left[i:] + right[j:]
    merges.append(out)
    return out


result = merge_sort([38, 27, 43, 3, 9, 82, 10])
ai_trace = [[27, 43], [27, 38, 43], [3, 9], [10, 82], [3, 9, 10, 82], [3, 9, 10, 27, 38, 43, 82]]
check("Ex2 merge sort trace matches the AI's 6 merge steps", merges == ai_trace)


def T_rec(n):
    return 1 if n <= 1 else 2 * T_rec(n // 2) + n


ratios = [T_rec(2 ** k) / (2 ** k * math.log2(2 ** k)) for k in (10, 14, 18)]
check("Ex2 T(n)=2T(n/2)+n grows like n log n (ratio stays near 1)",
      all(1.0 <= r <= 1.11 for r in ratios), ", ".join(f"{r:.3f}" for r in ratios))

# ---- Ex3 CS206 DBMS -----------------------------------------------------------
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE Student(sid INTEGER PRIMARY KEY, name TEXT, dept TEXT);
CREATE TABLE Enrollment(sid INTEGER, course_id TEXT, grade TEXT);
INSERT INTO Student VALUES (1,'S1','CSE'),(2,'S2','CSE'),(3,'S3','CSE'),(4,'S4','ECE'),(5,'S5','ECE'),(6,'S6','MECH');
-- CSE: 3 different students with A.  ECE: only 2 students with A, but S4 has three A grades (the trap).
INSERT INTO Enrollment VALUES (1,'C1','A'),(2,'C1','A'),(3,'C2','A'),
  (4,'C1','A'),(4,'C2','A'),(4,'C3','A'),(5,'C1','A'),(6,'C1','B');
""")
ai_query = """SELECT s.dept, COUNT(DISTINCT s.sid) FROM Student s JOIN Enrollment e ON s.sid = e.sid
WHERE e.grade = 'A' GROUP BY s.dept HAVING COUNT(DISTINCT s.sid) > 2"""
naive_query = ai_query.replace("COUNT(DISTINCT s.sid)", "COUNT(*)")
check("Ex3 AI query returns only CSE (expected by hand)", db.execute(ai_query).fetchall() == [("CSE", 3)])
check("Ex3 the COUNT(*) version is wrong on the same data (also returns ECE)",
      db.execute(naive_query).fetchall() == [("CSE", 3), ("ECE", 4)])

# ---- Ex4 DS304 ML -------------------------------------------------------------
TP, FP, FN, TN = 40, 10, 20, 130
acc, p, r = (TP + TN) / 200, TP / (TP + FP), TP / (TP + FN)
f1 = 2 * p * r / (p + r)
ai = {"accuracy": 0.85, "precision": 0.80, "recall": 0.667, "f1": 0.727}
mine = {"accuracy": acc, "precision": p, "recall": r, "f1": f1}
check("Ex4 all four metrics match the AI to 3 decimals",
      all(abs(mine[k] - ai[k]) < 0.0005 for k in ai), ", ".join(f"{k}={v:.3f}" for k, v in mine.items()))
check("Ex4 claim 'accuracy misleading': always-negative baseline already scores 0.70", (FP + TN) / 200 == 0.70)

print(f"\n{sum(results)} of {len(results)} checks passed")
sys.exit(0 if all(results) else 1)
