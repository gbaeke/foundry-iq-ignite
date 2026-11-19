# Closing Report: Container Dwell-Time Forecasting

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Container Dwell-Time Forecasting |
| **Date** | 2024-03-29 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Document type** | Closing report |
| **Approved by** | Koen Verstraete (CIO, Scaldis), Lotte Willems (Kestrel) |

## 1. Summary

The project delivered a dwell-time forecast for import containers that runs daily and is used by the yard planning team. The final model reaches a **MAPE of 11.8%** on the eight-week hold-out period (January to February 2024), well below the target of 15%. The solution has been **handed over to Nathalie Dumont's operations analytics team**, which now owns scoring, monitoring and retraining.

The project closes on the planned date, within the fixed price.

## 2. Results against objectives

| Objective | Target | Result |
|---|---|---|
| Forecast accuracy (MAPE, hold-out) | 15% or better | 11.8% |
| Daily batch forecast available to planners | Yes | Yes, at 05:30 each morning |
| Confidence band on forecast | Added during project | Delivered (P10 / P90) |
| Internal ownership at Scaldis | Handover completed | Completed, 3 knowledge transfer sessions |

Accuracy is somewhat lower for transhipment containers (MAPE around 16%), mainly because customs-release information arrives late. This is documented as a known limitation.

## 3. Delivered artefacts

- Ingestion and feature pipelines, scheduled nightly
- Registered model, scoring pipeline and monitoring notebook
- Output table consumed by the yard planning spreadsheet and a simple report
- Data contract for TOS events (v1.0), including the deduplication rules
- Runbook and retraining guide (quarterly retraining recommended)

## 4. Handover

Three knowledge transfer sessions took place in March with the operations analytics team ("de analisten", as the planners call them). The team has run two retraining cycles on its own under supervision. Kestrel provides best-effort support for questions until the end of April 2024, outside the fixed price.

## 5. Budget

| Item | Amount (EUR) |
|---|---|
| Fixed price | 185,000 |
| Invoiced | 185,000 |
| Change requests | none |

Internal effort was about 4% above plan, absorbed by Kestrel, mostly due to the data quality work in Q4 2023.

## 6. Lessons learned

**What went well**
- Fortnightly demos with planners kept the model grounded in operational reality; the confidence band request came straight from those sessions.
- The subcontracting setup with DataForge for Databricks work was smooth.
- A written data contract made the handover much easier.

**What could be better**
- **Involve the TOS vendor early.** The duplicate and missing gate-in events and the announced schema change both originated in the terminal operating system. We only had indirect contact through a Scaldis administrator, which cost us around two weeks in Q4. On future projects that depend on a vendor-managed operational system, we will ask for a direct technical contact at the vendor during discovery and put it in the project assumptions.
- Customs data for transhipment should have been scoped explicitly.
- Holiday freeze periods at the terminal need to be in the plan from the start.

## 7. Recommendations

- Retrain quarterly, or sooner after major changes in carrier mix.
- Consider an intraday refresh once the TOS event feed is available in near real time.
- Revisit transhipment accuracy when better customs-release data becomes available.

Thank you to Koen, Nathalie and the planning team for a constructive collaboration.

Thomas Maes
