# ADR-02: Resample Sensor Signals to 10-Second Intervals in the Silver Layer

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Line Sensor Data Platform |
| **Date** | 2024-08-02 |
| **Author** | Bram Visser, Databricks Specialist, DataForge (subcontracted by Kestrel Consulting) |
| **Document type** | Architecture decision record |
| **Status** | Accepted (reviewed by Sofie Claes and Dries Callens on 2024-08-01) |

## Context

The line PLCs produce signals at very different rates. Blancher temperatures and belt speeds arrive every second, freezer zone temperatures every one to five seconds, energy meters every 15 seconds, and packaging counters only when something happens. Line 1 alone gives about 235 tags. At source frequency, six lines produce several hundred million rows per month.

The quality team does not need one-second detail for its main questions (batch traceability, range checks, shift comparison). It does need to see short excursions, for example a blancher that drops two degrees for half a minute after a restart.

ADR-01 already fixed the layering: raw telemetry lands unchanged in the bronze layer of the Microsoft Fabric lakehouse, and transformations run in Databricks notebooks on the same storage.

## Options considered

1. **Keep source frequency in silver.** Simple, no information lost. Large tables, slow queries for every report, and every consumer must handle irregular timestamps.
2. **Resample to 1 minute.** Small and fast, but a 30-second excursion disappears into an average.
3. **Resample to 10 seconds, with min, max and mean per interval.** About ten times fewer rows than source, keeps short excursions visible through min and max.
4. **Different interval per signal type.** Most precise, but harder to explain and to join.

## Decision

Option 3. The silver layer holds one row per tag per 10-second interval, with:

- `value_mean`, `value_min`, `value_max`, `sample_count`
- `quality_flag`: `ok`, `gap` (no samples), `frozen` (identical value for more than 10 minutes on a signal that normally moves)
- line, equipment and tag metadata from the tag inventory

Counters (packaging, rejects) are not averaged but summed per interval. Gaps are flagged, not filled. Bronze keeps the full source data for at least two seasons, so we can always resample again if a new use case needs it.

## Consequences

- Reports and alert rules work on a regular time grid, which makes joins with batch windows straightforward.
- A drift or dip shorter than 10 seconds shows only in `value_min`/`value_max`, not in the mean. Dries accepted this.
- Storage for silver is estimated at roughly 12% of bronze.
- The frozen-value rule needs a per-tag exception list (some setpoints never move). Maintenance owns that list; Sofie will add it to the tag inventory sheet.
- Late-arriving data (gateway buffering after a network outage) must be handled. The resampling job reprocesses the last 48 hours on every run.

## Validation

Tested on two weeks of manual HMI exports from line 1. A restart on 2024-07-09 shows a blancher dip of 2.4 °C for about 40 seconds: clearly visible in `value_min` at 10 seconds, invisible at 1 minute.

## Follow-up

- Implement as a scheduled Databricks job once live telemetry from Azure IoT Hub arrives.
- Revisit after three lines are live to check job runtime and cost.
