"""Independent checks for the 5 AI-assisted exercises. Run: py verify.py"""
import sqlite3

print("=== Ex1 CS201 OOP: run the AI's code ===")
# AI output (exactly as given in ex1.txt)
class Shape:
    def area(self):
        return 0
    def describe(self, unit=None):          # AI's "overloading" via default argument
        if unit is None:
            return f"{type(self).__name__} with area {self.area():.2f}"
        return f"{type(self).__name__} with area {self.area():.2f} {unit}^2"

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r ** 2   # overriding

class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h            # overriding

for s in [Circle(2), Rectangle(3, 4)]:
    print(s.describe()); print(s.describe("cm"))
# Check: does Python really support Java-style overloading?
class T:
    def f(self, a): return "one"
    def f(self, a, b): return "two"   # replaces the first f
try:
    T().f(1); print("overloading works")
except TypeError as e:
    print("Second def replaced the first -> TypeError:", e)

print("\n=== Ex2 CS203 DAA: merge sort trace ===")
steps = []
def merge_sort(a):
    if len(a) <= 1: return a
    m = len(a) // 2
    l, r = merge_sort(a[:m]), merge_sort(a[m:])
    out, i, j = [], 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]: out.append(l[i]); i += 1
        else: out.append(r[j]); j += 1
    out += l[i:] + r[j:]
    steps.append(f"merge {l} + {r} -> {out}")
    return out
res = merge_sort([38, 27, 43, 3, 9, 82, 10])
print("\n".join(steps)); print("result", res)
# Master theorem check by counting work: T(n)=2T(n/2)+n  -> compare with n log2 n
import math
def T(n): return 1 if n <= 1 else 2 * T(n // 2) + n
for n in [2**10, 2**14, 2**18]:
    print(n, "T(n)/(n log2 n) =", round(T(n) / (n * math.log2(n)), 3))

print("\n=== Ex3 CS206 DBMS: run the AI's SQL on synthetic data ===")
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE Student(sid INTEGER PRIMARY KEY, name TEXT, dept TEXT);
CREATE TABLE Enrollment(sid INTEGER, course_id TEXT, grade TEXT);
INSERT INTO Student VALUES (1,'S1','CSE'),(2,'S2','CSE'),(3,'S3','CSE'),(4,'S4','ECE'),(5,'S5','ECE'),(6,'S6','MECH');
-- CSE: 3 distinct students with A.  ECE: only 2 students with A but S4 has three A's.
INSERT INTO Enrollment VALUES (1,'C1','A'),(2,'C1','A'),(3,'C2','A'),
  (4,'C1','A'),(4,'C2','A'),(4,'C3','A'),(5,'C1','A'),(6,'C1','B');
""")
ai_query = """SELECT s.dept, COUNT(DISTINCT s.sid) AS students_with_a FROM Student s
JOIN Enrollment e ON s.sid = e.sid WHERE e.grade = 'A'
GROUP BY s.dept HAVING COUNT(DISTINCT s.sid) > 2;"""
naive_query = ai_query.replace("COUNT(DISTINCT s.sid)", "COUNT(*)")
print("AI query            :", db.execute(ai_query).fetchall())
print("Naive COUNT(*) query:", db.execute(naive_query).fetchall())
print("Expected by hand: only CSE (3 distinct students); ECE has 2 students")

print("\n=== Ex4 DS304 ML: metrics ===")
TP, FP, FN, TN = 40, 10, 20, 130
acc = (TP + TN) / (TP + FP + FN + TN); p = TP / (TP + FP); r = TP / (TP + FN); f1 = 2 * p * r / (p + r)
print(f"accuracy={acc:.3f} precision={p:.3f} recall={r:.3f} f1={f1:.3f}")
# baseline that always predicts negative
print(f"always-negative baseline accuracy = {(FP + TN) / 200:.3f}")
