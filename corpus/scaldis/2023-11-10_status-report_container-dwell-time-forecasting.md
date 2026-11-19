# Status Report #3: Container Dwell-Time Forecasting

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Container Dwell-Time Forecasting |
| **Date** | 2023-11-10 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Document type** | Status report |
| **Reporting period** | 2023-10-16 to 2023-11-10 (sprints 3 and 4) |
| **Distribution** | Koen Verstraete, Nathalie Dumont, Lotte Willems |

## 1. Overall status

| Dimension | Previous report | This report | Comment |
|---|---|---|---|
| Overall | Green | **Amber** | Feature pipeline milestone slips two weeks |
| Scope | Green | Green | No changes |
| Schedule | Green | Amber | Feature pipelines ready expected 2023-11-24 instead of 2023-11-10 |
| Budget | Green | Green | 38% consumed |
| Data quality | Amber | **Red** | Gate-in events not reliable enough for features |

## 2. Summary

The gate-in problem flagged in the previous report is now an issue (I-03). The TOS produces duplicate gate-in records and, for part of the visits, no gate-in at all. Without correction, truck-related features and every export or re-entry visit are wrong. Sofie Claes is working through the patterns with the TOS administrator and expects to have correction rules ready in sprint 5. The feature pipeline milestone moves from 2023-11-10 to **2023-11-24**. We expect to absorb the two weeks in the modelling phase; the final date of 2024-03-29 is not at risk today.

## 3. Progress this period

- **Feature pipelines.** Bram Visser finished the vessel, carrier, container, customs and calendar feature groups in Databricks. Only the truck group waits for corrected gate-in data.
- **Modelling.** Amira El Idrissi set up the training pipeline in Azure Machine Learning with experiment tracking. First runs on vessel-based features only are promising but not yet comparable with the target.
- **Data contract.** v0.2 signed off by Nathalie and the TOS administrator on 2023-10-27.
- **Planner demo** of 2023-11-10: dwell-time per carrier and the effect of weekend calls. Planners asked whether the forecast could show a range instead of a single number. Noted for the next sprints.

## 4. Risks and issues

| ID | Type | Description | Owner | Status |
|---|---|---|---|---|
| I-03 | Issue | Duplicate and missing gate-in events from the TOS (was R-03) | SC | Open, rules in progress |
| R-02 | Risk | Planner availability during peak weeks | ND | Open |
| R-04 | Risk | Truck appointment data only available since March 2022 | AE | Open, accepted |
| R-05 | Risk | TOS schema change announced for Q1 2024 could break extraction | TM | **New** |

R-05 came to us via the TOS administrator, who heard it from the TOS vendor's account manager. We have no direct technical contact at the vendor. We asked Koen whether Scaldis can arrange one.

## 5. Decisions needed at the steering committee of 2023-11-23

1. Accept the two-week shift of the feature pipeline milestone (and therefore of the second invoice).
2. Ask the TOS vendor, through Scaldis, for the technical details of the Q1 schema change.

## 6. Next steps (sprints 5 and 6)

- Deduplication and missing gate-in rules in the curated layer (SC)
- Truck feature group once rules are live (BV)
- Model comparison on all feature groups (AE)
- Planner feedback session on a first forecast list (ND, AE)

## 7. Budget

| Item | Amount (EUR) |
|---|---|
| Fixed price | 185,000 |
| Invoiced to date | 55,500 |
| Next invoice (30%) | at feature pipelines ready, now expected end of November |

*Next status report: 2023-12-08.*

Thomas Maes
