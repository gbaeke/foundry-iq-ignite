# ADR-03: Daily Batch Scoring, Intraday Refresh Deferred

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Container Dwell-Time Forecasting |
| **Date** | 2024-02-09 |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |
| **Document type** | Architecture decision record |
| **Status** | Accepted (Nathalie Dumont, product owner, 2024-02-09) |
| **Related** | ADR-01 storage zones, ADR-02 point-in-time feature snapshots |

## Context

The proposal describes a daily batch forecast to begin with and an intraday refresh as an option. Planners now use the 05:30 forecast for the morning plan. During the evaluation workshop on 2024-01-19, two planners asked whether the forecast could refresh at noon, when many customs releases come in.

Current pipeline:
- TOS export lands in Azure Data Lake Storage Gen2 at 01:00;
- curated and feature jobs in Databricks finish around 03:20;
- batch scoring in Azure Machine Learning starts at 05:00 and writes the output table by 05:30.

The TOS export is a nightly file. There is no near-real-time event feed today. The TOS update announced by the vendor does not add one.

## Options considered

1. **Keep daily batch only.** Simple, already in production, fully covered by the runbook.
2. **Second batch at noon from a partial export.** Requires a second export from the TOS reporting module at 11:30. The TOS administrator says this export puts load on the TOS database during the busiest hours, and the vendor advises against it.
3. **Intraday scoring from an event stream.** Requires an event feed from the TOS, which does not exist. Would mean a different ingestion design and new integration work with the TOS vendor.

## Decision

Option 1. The forecast is scored once a day, available at 05:30. Intraday refresh is deferred until the TOS can provide events in near real time. Recorded as a recommendation in the closing report.

To reduce the pain at noon, the output table already carries the customs hold flag and the P10–P90 range. Planners agreed to treat "customs hold + wide range" containers as the ones to re-check manually after the noon releases.

## Consequences

- No extra load on the TOS during operations.
- One scoring run per day keeps compute cost low and predictable. January cost for Databricks job clusters, Azure ML compute and storage combined stayed well under the monthly envelope agreed with Koen Verstraete.
- The model's information about customs releases is up to 12 hours old by early afternoon. Containers released in the morning will look "too long" in the forecast until the next morning. Planners know this and accept it for now.
- The operations analytics team runs only one schedule, which suits a small team.

## Operational details fixed by this ADR

| Item | Value |
|---|---|
| Scoring schedule | Daily 05:00, Europe/Brussels time |
| Output deadline | 05:30; if late, an alert mail goes to the analytics team and the shift supervisor |
| Fallback | If scoring fails, the previous day's forecast stays visible with a "stale" marker |
| Model version | Fixed during the hold-out until early March 2024; afterwards per retraining cycle |
| Retraining | Quarterly, or sooner after major changes in carrier mix |

## Review

To be revisited when Scaldis gets near-real-time TOS events or when the planners' noon re-check takes more than 30 minutes a day on average.

Amira El Idrissi
