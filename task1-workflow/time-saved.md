# Net Time Saved

All values are **estimates [E]**: staff effort per year, for the whole university.

## Inputs
| Variable | Old | New |
|---|---|---|
| Requests per year (N) | 200 | 200 |
| Preparing the request | 120 min | 90 min (one standard form) |
| Collecting 3 quotations | 180 min | 180 min (vendors still have to be contacted) |
| Approvals (incl. moving the file) | 4 levels × 30 min = 120 min | Small (60% of requests): 2 levels × 10 min · Large (40%): 4 × 10 min → average 28 min |
| Accounts processing | 60 min | 45 min |
| Sent back for missing info | 30% × 120 min | 10% × 60 min (checked at submission) |

## Per request
```
Old = 120 + 180 + 120 + 60 + 0.30×120 = 516 min
New =  90 + 180 +  28 + 45 + 0.10×60  = 349 min
Saved per request = 167 min
```

## Per year, including review and support effort
```
Gross saved     = 200 × 167                    = 33,400 min
Review effort   = monthly audit, 12 × 120 min  = −1,440 min  (Accounts checks small purchases)
Support effort  = 10% need help × 200 × 20 min =   −400 min
Setup effort    = form + sheet + training      =   −960 min  (16 hours, one time)
Net saved                                      = 30,600 min ≈ 510 staff hours per year
```

**Also faster:** small purchases skip 2 approval levels, so the time from request to delivery should drop for about 60% of requests. I haven't put a number on this because I have no data.

## Low scenario
100 requests, 15% sent back now, 5% after:
```
Old = 480 + 0.15×120 = 498 min,  New = 343 + 0.05×60 = 346 min,  Saved = 152 min
100 × 152 − (1,440 + 200 + 960) = 12,600 min ≈ 210 hours per year
```
Even the low case saves time, mainly because the review and setup effort is fixed.
