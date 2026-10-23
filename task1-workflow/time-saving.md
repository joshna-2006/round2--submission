# 5. Net Time Saved

> ⚠️ **ILLUSTRATIVE.** All 14 inputs are still illustrative (see [prototype/params.json](prototype/params.json)). This page shows **the method and a worked example**. It is not a finding. It becomes one once the values are replaced with evidence (see [evidence/what-to-verify.md](evidence/what-to-verify.md)).

## Formula
```
N           = requests per month × months
old/request = old visits × minutes per visit + old staff minutes
new/request = online form minutes + new visits × minutes per visit + new staff minutes
gross       = N × (old − new)
review      = N × escalation rate × review minutes        (admin head)
support     = N × support rate × support minutes          (helping with the form)
setup       = one-time setup minutes                      (form, sheet, training)
NET         = gross − review − support − setup
```

## Worked example (illustrative values, output of `py savings.py`)
| Input | Value |
|---|---|
| Requests | 30 per month × 12 = 360 |
| Old: 3 visits × 30 min + 20 min staff | 110 min per request |
| New: 10 min online + 1 visit × 15 min + 12 min staff | 37 min per request |

```
Gross saved     : 26,280 min
- review        :    360 min
- support       :    720 min
- setup         :    600 min
= NET saved     : 24,600 min (410 hours per year)
  students      : 390 hours
  staff (net)   :  20 hours
```

## What the example already tells me
- **Almost all of the benefit goes to students** (fewer visits). Staff save only about 20 hours, because they take on the review, support and setup work.
- **The result depends mostly on the number of old visits.** If students actually need only 1 visit today, the gross saving falls a lot. That's why visits are the first thing I need to measure.

`test_savings.py` checks this example against the hand calculation above.
