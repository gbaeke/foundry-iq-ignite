# Status Report: Bed Capacity Dashboard

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Bed Capacity Dashboard |
| **Document type** | Status report (biweekly) |
| **Date** | 2023-06-23 |
| **Author** | Lotte Willems, engagement lead and project manager, Kestrel Consulting |
| **Period** | 2023-06-12 to 2023-06-23 |
| **Distribution** | Jeroen Lambrecht; Kestrel project team |

## 1. Overall status

| Area | Status | Comment |
|---|---|---|
| Overall | Amber | Technical work on track; bed list decision overdue |
| Scope | Green | No changes |
| Planning | Amber | First go-live in September still feasible, but depends on bed list |
| Budget | Green | 31% of fixed price consumed, in line with plan |
| Quality | Green | First pipeline runs reconcile with ward counts |

## 2. Progress this period

- Sofie Claes finished the first version of the Synapse pipelines: the ADT files are loaded every 15 minutes and the bed state of the last 72 hours is rebuilt on each run. A full run takes about four minutes.
- Reconciliation test on campus Centrum: on 2023-06-20 the model was compared with the phone round. 37 of 41 wards matched exactly; the four differences were all explained by events recorded late on the ward.
- Mediva IT confirmed that the bed status table (blocked beds) can be delivered every 15 minutes from July onwards. Until then we use the daily file.
- Elien Jacobs prepared paper prototypes for the campus overview and the ward page. First usability round planned for 2023-07-04 to 2023-07-07 with bed managers and head nurses.
- The data mapping note was reviewed by Jeroen's team; comments processed in version 1.0.

## 3. Main issue: who owns the bed list

The official bed list (1,118 beds) and the bed codes used in practice (1,163) differ, as described in the data mapping note. Technically we can handle it with an "unmapped" table, but someone has to decide which beds count. The question went to the nursing directorate on 2023-05-31 and has not been answered.

This matters for go-live: if the overview shows beds that wards consider non-existent, the first reaction of users will be "the dashboard is wrong", and we lose trust before we start. Jeroen agreed to escalate and to propose that the bed management office owns the list, with a monthly review.

## 4. Risks and issues

| # | Type | Description | Owner | Mitigation |
|---|---|---|---|---|
| R1 | Issue | Bed list ownership not decided | JL | Escalation to nursing directorate, decision needed by 2023-07-07 |
| R2 | Risk | Head nurses unavailable for usability round in summer | EJ | Round 1 early July, round 2 end of August |
| R3 | Risk | Free-text reasons for blocked beds stay unreliable | SC | Keyword list owned by bed management office, "other" reviewed monthly |
| R4 | Risk | ADT extract format changes during a planned upgrade of the hospital information system in autumn | JL | Ask the vendor for the upgrade date and a test file |

## 5. Next steps

| Action | Owner | Due |
|---|---|---|
| Decision on bed list ownership | JL | 2023-07-07 |
| First Power BI report on the Synapse model (campus overview) | SC, EJ | 2023-07-07 |
| Usability round 1 | EJ | 2023-07-07 |
| Switch blocked beds to 15-minute delivery | SC | 2023-07-14 |
| Confirm date of the hospital information system upgrade | JL | 2023-07-14 |

## 6. Remarks

Next status meeting on Friday 2023-07-07. Note that from 2023-07-21 to 2023-08-15 several participants are on leave; Sofie and I keep the project going with a reduced rhythm, and the status meeting of 2023-08-04 is cancelled.

*Lotte Willems, Kestrel Consulting*
