"""
Net time saved by the proposed ID card process, after review, support and setup effort.

Reads params.json. If ANY value is still 'illustrative', the result is printed as
ILLUSTRATIVE, not as a finding.

Run:  py savings.py            (uses params.json)
      py savings.py other.json (uses another parameter file)
"""
import json
import sys
from pathlib import Path


def load(path):
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    params = {k: v for k, v in raw.items() if not k.startswith("_")}
    for name, p in params.items():
        if p["label"] not in ("illustrative", "observed"):
            raise ValueError(f"{name}: label must be 'illustrative' or 'observed'")
        if p["value"] < 0:
            raise ValueError(f"{name}: value cannot be negative")
    return params


def calculate(params):
    v = {k: p["value"] for k, p in params.items()}
    n = v["requests_per_month"] * v["months"]

    old_student = v["old_student_visits"] * v["old_minutes_per_visit"]
    new_student = v["new_student_online_minutes"] + v["new_student_visits"] * v["new_minutes_per_visit"]
    old_per_request = old_student + v["old_staff_minutes"]
    new_per_request = new_student + v["new_staff_minutes"]

    gross = n * (old_per_request - new_per_request)
    review = n * v["escalation_rate"] * v["review_minutes_per_escalation"]
    support = n * v["support_rate"] * v["support_minutes"]
    setup = v["setup_minutes_one_time"]
    net = gross - review - support - setup

    staff_net = n * (v["old_staff_minutes"] - v["new_staff_minutes"]) - review - support - setup
    return {
        "requests": n,
        "old_per_request": old_per_request,
        "new_per_request": new_per_request,
        "gross": gross, "review": review, "support": support, "setup": setup,
        "net": net, "student_net": n * (old_student - new_student), "staff_net": staff_net,
    }


def main(path="params.json"):
    params = load(path)
    r = calculate(params)
    illustrative = [k for k, p in params.items() if p["label"] == "illustrative"]
    print(f"Requests in period          : {r['requests']:.0f}")
    print(f"Minutes per request old/new : {r['old_per_request']:.0f} / {r['new_per_request']:.0f}")
    print(f"Gross saved                 : {r['gross']:>8.0f} min")
    print(f"- review effort             : {r['review']:>8.0f} min")
    print(f"- support effort            : {r['support']:>8.0f} min")
    print(f"- setup effort              : {r['setup']:>8.0f} min")
    print(f"= NET saved                 : {r['net']:>8.0f} min  ({r['net'] / 60:.1f} hours)")
    print(f"  of which students         : {r['student_net'] / 60:.1f} hours")
    print(f"  of which staff (net)      : {r['staff_net'] / 60:.1f} hours")
    if illustrative:
        print(f"\nILLUSTRATIVE RESULT: {len(illustrative)} of {len(params)} values are not measured yet.")
    else:
        print("\nAll values are observed.")
    return r


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "params.json")
