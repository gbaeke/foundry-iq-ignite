# Handover Notes: Operations Analytics Team

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Container Dwell-Time Forecasting |
| **Date** | 2024-03-15 |
| **Author** | Sofie Claes, Senior Data Engineer, Kestrel Consulting |
| **Document type** | Handover notes |
| **Audience** | Operations analytics team (Nathalie Dumont's department) |

## 1. Purpose

This note is the working checklist for the handover of the dwell-time forecast to the operations analytics team. It complements the runbook and the retraining guide in the project folder. It will be updated after the last knowledge transfer session and attached to the closing report.

## 2. Where things stand

- Formal hold-out finished on 2024-03-03 (eight weeks from 2024-01-08). Final MAPE on the hold-out: **11.8%**, against the 15% target. Nathalie confirmed final acceptance on 2024-03-07.
- The TOS update went live over the weekend of 24–25 February. Extraction had been adapted to the two renamed gate columns and the new OCR source code beforehand. No nightly run was lost. Double registrations on lanes 4 and 5 dropped after the update, but rule GI-01 stays in place: it costs nothing when there are no duplicates.
- Data contract v1.0 is final and includes rules GI-01 and GI-02.

## 3. Knowledge transfer sessions

| # | Date | Topic | Presenter | Status |
|---|---|---|---|---|
| 1 | 2024-03-05 | Data flow: TOS export, storage zones in Azure Data Lake Storage Gen2, curated rules | Sofie, Bram | Done |
| 2 | 2024-03-12 | Databricks jobs, monitoring, rerun procedures | Bram, Sofie | Done |
| 3 | 2024-03-21 | Azure Machine Learning: training pipeline, model registry, scoring, retraining | Amira | Planned |

Recordings are stored in the project folder; slides in Dutch, code comments in English as agreed.

## 4. Ownership after handover

| Component | Owner after 2024-03-29 | Backup |
|---|---|---|
| Nightly TOS export and file transfer | Scaldis IT (TOS administrator) | Scaldis IT on-call |
| Databricks curated and feature jobs | Operations analytics team | — |
| Carrier alias mapping table | Yard planners (business), analytics team (technical) | — |
| Scoring and output table | Operations analytics team | — |
| Retraining (quarterly) | Operations analytics team | Kestrel best effort until end of April 2024 |
| Azure cost follow-up | Scaldis IT finance contact | — |

## 5. Retraining under supervision

The analytics team ran its first retraining cycle on 2024-03-07 with Amira watching, on data up to the end of February. The candidate model was compared with the production model on the last four weeks, as described in the retraining guide; it was registered but not promoted because the gain was below the threshold of 0.5 percentage point. That is the expected outcome and a good test of the procedure. A second supervised cycle is planned on 2024-03-26.

## 6. Access and security

- Kestrel and DataForge guest accounts are removed on 2024-04-30, after the best-effort support period. Until then they are read-only from 2024-03-29.
- The managed identity used by the Databricks jobs stays; its permissions are documented in the runbook.
- No personal data is processed. Truck appointment data contains haulier company codes only; driver data is not in the export.

## 7. Open items before closing

| Item | Owner | Due |
|---|---|---|
| Third KT session | AE | 2024-03-21 |
| Second supervised retraining cycle | Analytics team, AE | 2024-03-26 |
| Runbook review by the analytics team, comments processed | SC | 2024-03-27 |
| Known limitations section (transhipment, customs release delay) | AE | 2024-03-27 |
| Switch Kestrel and DataForge accounts to read-only | Scaldis IT | 2024-03-29 |

## 8. Tips from the team

- When the forecast looks odd for one carrier, check the alias mapping first. Mergers happen.
- If the TOS export is missing, do not rerun the downstream jobs on yesterday's file; the stale marker will do its job.
- Keep the planners' Friday demo habit going once a month. It is the cheapest monitoring there is.

Sofie Claes
