# Status Report #4: Container Dwell-Time Forecasting

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Container Dwell-Time Forecasting |
| **Date** | 2023-12-08 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Document type** | Status report |
| **Reporting period** | 2023-11-13 to 2023-12-08 (sprints 5 and 6) |
| **Distribution** | Koen Verstraete, Nathalie Dumont, Lotte Willems |

## 1. Overall status

| Dimension | Previous report | This report | Comment |
|---|---|---|---|
| Overall | Amber | **Green** | Data quality issue resolved, back on plan |
| Scope | Green | Green | No changes |
| Schedule | Amber | Green | Feature pipeline milestone reached with a 2-week delay, absorbed in modelling phase |
| Budget | Green | Green | 52% consumed, in line with fixed price plan |
| Data quality | Red | Green | Deduplication rules in production |

Status moves from **amber to green**.

## 2. Progress this period

- **Gate-in data quality.** In the previous report we flagged duplicate and missing gate-in events coming from the terminal operating system (TOS). Roughly 6% of gate-in events were duplicated (same container, same gate, timestamps a few seconds apart), and for about 2% of containers there was no gate-in event at all, only a later yard move. Sofie Claes analysed the patterns with a TOS administrator and wrote a set of deduplication rules, plus an inference rule that reconstructs a missing gate-in from the first yard position and the truck appointment. The rules run as the first step of the curated layer and are documented in the data contract (v0.3).
- **Feature pipelines.** Bram Visser (DataForge) completed the Databricks feature pipelines: vessel rotation, carrier, commodity group, customs status, weekday and Belgian public holiday features. The pipelines run nightly and write to the curated zone in ADLS Gen2.
- **Modelling.** Amira El Idrissi started baseline experiments in Azure Machine Learning. A first gradient boosting model gives a MAPE of 17.4% on the validation window, before tuning. Target remains 15%.
- **Planner sessions.** Two feedback sessions with yard planners, organised by Nathalie Dumont. Planners asked for a confidence band next to the point forecast, which we will add without scope impact.

## 3. Risks and issues

| ID | Type | Description | Owner | Status |
|---|---|---|---|---|
| I-03 | Issue | Duplicate and missing gate-in events from the TOS | SC | Closed |
| R-05 | Risk | TOS schema change announced for Q1 2024 could break extraction | TM | Open, monitoring |
| R-06 | Risk | Planner availability over the holiday period | ND | Open |
| R-07 | Risk | Customs-release events arrive late for transhipment containers | AE | Open, under analysis |

R-05 remains the main concern: we have no direct contact with the TOS vendor and depend on the Scaldis administrator for information about the upcoming change.

## 4. Next steps (sprints 7 and 8)

- Hyperparameter tuning and comparison of two model families (AE)
- Add confidence band to output table (AE, SC)
- Request schema change details for the TOS update via Scaldis IT (TM, by 2023-12-20)
- Plan evaluation session with planners for week 3 of January (ND)
- Holiday freeze from 2023-12-22 to 2024-01-02; no deployments in that window

## 5. Budget

| Item | Amount (EUR) |
|---|---|
| Fixed price | 185,000 |
| Invoiced to date | 111,000 |
| Remaining | 74,000 |

*Next status report: 2024-01-12.*

Thomas Maes
