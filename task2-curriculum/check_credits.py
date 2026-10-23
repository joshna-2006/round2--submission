"""
Recomputes every credit figure in the Task 2 report from the CSV files, so the
numbers can be checked instead of trusted.

Run:  py check_credits.py
It exits with an error if the data is invalid, the total is not balanced, the
affected share is outside 20-25%, or the calculator's embedded copy of the data
differs from proposed-curriculum.csv.
"""
import csv
import sys
from collections import OrderedDict
from pathlib import Path

HERE = Path(__file__).parent
ACTIONS = {"KEEP", "UPDATE", "REDUCE", "ADD"}


def read(name):
    with open(HERE / name, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def validate(rows):
    errors, seen = [], set()
    for i, r in enumerate(rows, start=2):
        cur, new, act = int(r["current_credits"]), int(r["proposed_credits"]), r["action"]
        if r["code"] in seen:
            errors.append(f"row {i}: duplicate code {r['code']}")
        seen.add(r["code"])
        if act not in ACTIONS:
            errors.append(f"row {i}: bad action {act}")
        if act in ("KEEP", "UPDATE") and cur != new:
            errors.append(f"row {i}: {act} must not change credits")
        if act == "REDUCE" and not new < cur:
            errors.append(f"row {i}: REDUCE must lower credits")
        if act == "ADD" and cur != 0:
            errors.append(f"row {i}: ADD must start from 0")
        if act != "KEEP" and not r["reason_id"]:
            errors.append(f"row {i}: {act} needs a reason_id")
    return errors


def summarise(rows, include_sem8=True):
    rows = [r for r in rows if include_sem8 or r["semester"] != "8"]
    cur = sum(int(r["current_credits"]) for r in rows)
    new = sum(int(r["proposed_credits"]) for r in rows)
    updated = sum(int(r["current_credits"]) for r in rows if r["action"] == "UPDATE")
    reduced = sum(int(r["current_credits"]) - int(r["proposed_credits"]) for r in rows if r["action"] == "REDUCE")
    added = sum(int(r["proposed_credits"]) for r in rows if r["action"] == "ADD")
    affected = updated + max(reduced, added)   # reallocated credits counted once
    return dict(current=cur, proposed=new, updated=updated, reduced=reduced, added=added,
                affected=affected, pct=100 * affected / cur)


def main():
    baseline = read("current-curriculum.csv")
    rows = read("proposed-curriculum.csv")
    problems = validate(rows)

    if [r["code"] for r in baseline] != [r["code"] for r in rows if r["action"] != "ADD"]:
        problems.append("proposed-curriculum.csv does not contain exactly the baseline courses in order")
    for b, p in zip(baseline, [r for r in rows if r["action"] != "ADD"]):
        if b["credits"] != p["current_credits"]:
            problems.append(f"{b['code']}: current credits differ between the two CSV files")

    embedded = (HERE / "calculator" / "index.html").read_text(encoding="utf-8")
    start = embedded.index('<script id="data" type="text/csv">') + len('<script id="data" type="text/csv">')
    block = embedded[start:embedded.index("</script>", start)].strip()
    if block.replace("\r", "") != (HERE / "proposed-curriculum.csv").read_text(encoding="utf-8").strip().replace("\r", ""):
        problems.append("calculator/index.html embedded data differs from proposed-curriculum.csv")

    print("Semester totals (current -> proposed):")
    sems = OrderedDict()
    for r in rows:
        c, n = sems.get(r["semester"], (0, 0))
        sems[r["semester"]] = (c + int(r["current_credits"]), n + int(r["proposed_credits"]))
    for s, (c, n) in sems.items():
        print(f"  {s:<10} {c:>3} -> {n:>3}")

    official_match = sum(1 for b in baseline if b["comparison"] == "match")
    print(f"\nBaseline courses matching the official page exactly: {official_match} of {len(baseline)}")

    for label, inc in (("Whole programme (incl. Sem VIII internship, 15)", True),
                       ("Sem I-VII + summer only (screenshot data)", False)):
        s = summarise(rows, inc)
        print(f"\n{label}")
        print(f"  current {s['current']} -> proposed {s['proposed']}  balanced={s['current'] == s['proposed']}")
        print(f"  updated {s['updated']} + reallocated max({s['reduced']}, {s['added']}) = affected {s['affected']}")
        print(f"  affected share = {s['pct']:.1f}%")
        if s["current"] != s["proposed"]:
            problems.append(f"{label}: not balanced")
        if not 20 <= s["pct"] <= 25:
            problems.append(f"{label}: affected share {s['pct']:.1f}% is outside 20-25%")

    if problems:
        print("\nPROBLEMS:\n  " + "\n  ".join(problems))
        sys.exit(1)
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
