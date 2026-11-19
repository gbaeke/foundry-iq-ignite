# Status Report: Leak Detection Analytics

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Leak Detection Analytics |
| **Date** | 2025-04-18 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Status report (report no. 8) |
| **Reporting period** | 2025-03-21 to 2025-04-18 |
| **Distribution** | Filip Wuyts, Evelien Claes, Koen Martens, Lotte Willems |

## 1. Overall status

| Area | Status | Comment |
|---|---|---|
| Overall | Green | Pilot running, first leaks confirmed |
| Scope | Green | Unchanged |
| Schedule | Green | Field validation started on 2025-04-07 as re-planned |
| Budget | Green | About 74% used |
| Adoption | Amber | Crews' trust dipped in week one, recovering |

## 2. Progress this period

- **Field validation started** in zone Noord-Oost on Monday 2025-04-07, with two crew days per week and one night search, as agreed in the protocol of 2025-03-28.
- **Two larger leaks on cast iron mains** were found within the first three days, on 2025-04-08 and 2025-04-09. Both had been running for about two weeks according to the night-flow history. Neither had been reported by customers.
- **First two weeks in numbers:** 19 candidates sent to crews, 9 confirmed leaks, 8 not found, 2 still to be searched. Of the 9 confirmed, 7 had not been reported by customers.
- **ArcGIS layer:** refreshed every morning before 07:30 since 2025-04-01. One late refresh on 2025-04-15 (export file arrived at 06:40 instead of 06:00).
- **Retraining pipeline** in Azure Machine Learning reads crew status back from the candidate layer every night.

## 3. Issues

### I-05: Candidate list too long in week one (resolved)

In the first week the model produced 12 candidates for four crew days. Only 4 were confirmed. Crews spent half days on candidates that turned out to be night consumption of a bakery and a flushing operation that was not in the planning. At the Friday call of 2025-04-11 one crew leader said the list "feels like a lottery". Trust dropped quickly.

Action: from week two (2025-04-14) a **confidence threshold** is applied. Only candidates above 0.6 are sent to crews; lower ones stay visible on the map in grey for the GIS team. The bakery's address was added as a known night consumer. In week two, 7 candidates were sent and 5 confirmed.

### I-06: Late nightly export on 2025-04-15 (resolved)

The export arrived 40 minutes late after a restart of the historian export task. Bram's monitoring alerted Koen at 06:00. Koen restarted the task; candidates were ready at 07:50. Crews started 20 minutes later than usual.

## 4. Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-04 | Model phase compressed | Occurred | Medium | Tuning continues during validation |
| R-06 | Field crew capacity | Low | High | Crew days booked until 2025-05-16 |
| R-07 | Daily export fails unnoticed | Low | Medium | Monitoring live, worked on 2025-04-15 |
| R-08 | Crews lose trust after false alarms | Medium | High | Threshold, Friday review, known night consumers list |
| R-09 | Handover too short for the GIS team | Medium | Medium | Handover sessions planned from 2025-05-12 |

## 5. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Continue validation; Friday calls | AEI / crew coordinator | weekly |
| 2 | Review threshold after four weeks | AEI / EC | 2025-05-02 |
| 3 | Handover plan and session dates for GIS analysts | SC / EC | 2025-04-25 |
| 4 | Model card and runbook draft | AEI / BV | 2025-05-16 |
| 5 | Interim validation report | AEI | 2025-05-09 |

Easter Monday (2025-04-21) is a holiday: no crew day, no change to the morning refresh.

Next status report: 2025-05-16.
