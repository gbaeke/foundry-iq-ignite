# Status Report #2: Container Dwell-Time Forecasting

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Container Dwell-Time Forecasting |
| **Date** | 2023-10-13 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Document type** | Status report |
| **Reporting period** | 2023-09-18 to 2023-10-13 (sprints 1 and 2) |
| **Distribution** | Koen Verstraete, Nathalie Dumont, Lotte Willems |

## 1. Overall status

| Dimension | Previous report | This report | Comment |
|---|---|---|---|
| Overall | Green | **Green** | Data discovery milestone met on 2023-09-29 |
| Scope | Green | Green | No changes |
| Schedule | Green | Green | Feature work started on time |
| Budget | Green | Green | 24% consumed |
| Data quality | Green | Amber | Gate-in anomalies larger than first sample suggested |

## 2. Progress this period

- **Data discovery closed.** Profiling of three years of TOS history is done and the data contract v0.1 was circulated on 2023-09-22. Nathalie and the TOS administrator returned comments; v0.2 is in review.
- **Nightly extraction.** The one-way file transfer from the terminal operations network to the raw zone in Azure Data Lake Storage Gen2 runs every night at 01:00. Two failed nights in week 40 were caused by a full disk on the export server; Scaldis IT added monitoring.
- **Feature pipelines.** Bram Visser has the vessel rotation and carrier features running in Databricks on the full history. The carrier alias mapping (6 aliases on 41 codes) is in place.
- **Baseline.** Amira El Idrissi reconstructed the planners' current estimate from the planning spreadsheet rules. On the last six months that baseline has a MAPE of about 31%. This is the number the model needs to beat in the planners' eyes, besides the contractual 15%.
- **First planner demo** (2023-09-29): profiling results and the dwell-time distribution per carrier. The planners recognised the long tail of containers waiting for inspection.

## 3. Data quality: gate-in events

Sofie Claes extended the first two-week sample to the full training window. Duplicate gate-in records are more frequent than the sample suggested, and visits without any gate-in are not rare either. Final figures will follow once the analysis with the TOS administrator is complete. For now, data quality moves to **amber**. Feature work that depends on gate-in timestamps (truck-related features, export containers) is paused; vessel-based features continue.

## 4. Risks and issues

| ID | Type | Description | Owner | Status |
|---|---|---|---|---|
| R-01 | Risk | Guest access for DataForge engineer delayed | TM | Closed (access granted 2023-09-11) |
| R-02 | Risk | Planner availability during peak weeks | ND | Open |
| R-03 | Risk | Gate-in event quality in the TOS | SC | Open, escalating |
| R-04 | Risk | Truck appointment data only available since March 2022 | AE | Open, accepted |

## 5. Steering committee of 2023-09-28

Short meeting. Koen confirmed that the planners' estimate is a fair internal benchmark and asked to see both figures side by side in every demo. Lotte proposed to keep the steering committee to 45 minutes unless decisions are needed.

## 6. Next steps (sprints 3 and 4)

- Detailed gate-in analysis with the TOS administrator; proposal for correction rules (SC)
- Customs status, commodity and calendar features (BV)
- First training pipeline in Azure Machine Learning on vessel-based features (AE)
- Data contract v0.2 sign-off (ND, TOS administrator)
- Autumn school holiday week (30 October to 3 November): two planners off; the next planner demo stays on 2023-11-10

## 7. Budget

| Item | Amount (EUR) |
|---|---|
| Fixed price | 185,000 |
| Invoiced to date (30% at kick-off) | 55,500 |
| Remaining | 129,500 |

*Next status report: 2023-11-10.*

Thomas Maes
