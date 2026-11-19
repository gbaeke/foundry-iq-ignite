# Status Report: Leak Detection Analytics

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Leak Detection Analytics |
| **Date** | 2024-11-22 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Status report (report no. 3) |
| **Reporting period** | 2024-10-25 to 2024-11-22 |
| **Distribution** | Filip Wuyts, Evelien Claes, Koen Martens, Lotte Willems |

## 1. Overall status

| Area | Status | Comment |
|---|---|---|
| Overall | Amber | Platform progressing, no SCADA history yet |
| Scope | Green | Unchanged |
| Schedule | Amber | First SCADA history in the lakehouse (November milestone) will be missed |
| Budget | Green | About 34% used |
| Data quality | Amber | Work orders and network model being corrected |

## 2. Progress this period

- **Data access request** submitted to OT security by Koen on 2024-10-28. The first round on 2024-11-06 asked for a description of the server in the DMZ and of the pickup. Koen answered on 2024-11-12. Next round: 2024-11-20, outcome not yet known at the time of writing.
- **Working data:** Koen made a manual export of three months for DMA NO-2. Bram's silver jobs run on it: time zone conversion, unit checks, gap and frozen value flags. 4.1% of the values were flagged as gaps, mostly one night in October. For the other three DMAs, Bram generated synthetic series with the same profile, so the pipelines can be tested on the full zone.
- **Night-flow features:** Amira built minimum night flow and night-to-day ratio per day for NO-2. Two known repairs in the export period show clearly as a step up in night flow, a few days to two weeks before the repair date.
- **Network model:** Evelien's team has corrected 21 pipe segments in Noord-Oost with missing material or diameter so far.
- **Work orders:** 196 of 212 repair work orders geocoded onto a pipe segment. The rest have incomplete addresses.

## 3. Issues

### I-02: SCADA history only reachable through the OT DMZ (open)

A direct connection from Azure to the historian is not allowed. The only path is through the OT DMZ, with approval from OT security for any new data flow. The request is in its second review round. We do not know yet when it will be approved.

Impact so far: model work can only use the manual export of one DMA. The milestone "first SCADA history in the lakehouse" in November will not be met. If approval comes in December, model work starts in January, about a month later than planned.

## 4. Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-01 | SCADA access takes longer than planned | Occurred | High | Work on manual exports; escalation by Filip if no approval in December |
| R-02 | Network model gaps hurt localisation | Medium | Medium | Correction ongoing, target before January |
| R-03 | Repair dates are not leak start dates | Confirmed | Medium | Leak start from night-flow steps |
| R-04 | Model phase compressed by the access delay | Medium | Medium | Prepare features and pipelines now, on NO-2 data |

## 5. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Follow up OT security decision | KM | 2024-11-29 |
| 2 | If no decision by mid-December, raise with the OT manager | FW | 2024-12-13 |
| 3 | Finish network model corrections in Noord-Oost | EC | 2024-12-20 |
| 4 | Daily load pipeline in Fabric ready to pick up files once approved | SC | 2024-12-06 |
| 5 | Feature pipeline in Databricks for all four DMAs (tested on NO-2) | BV | 2024-12-13 |

Next status report: 2024-12-13.
