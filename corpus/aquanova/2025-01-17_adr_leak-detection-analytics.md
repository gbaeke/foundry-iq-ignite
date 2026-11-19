# ADR-03: Daily Batch Data Instead of Near Real Time

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Leak Detection Analytics |
| **Date** | 2025-01-17 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Architecture decision record |
| **Status** | Accepted by Evelien Claes (product owner) and Filip Wuyts (sponsor) on 2025-01-17 |

## Context

The proposal described "flow and pressure data from the SCADA system" without fixing the latency. During discovery we assumed near real time would be possible later, for example to detect burst mains within the hour.

OT security approved only one data path: a nightly export of the agreed tags from the historian through a data diode to a file drop in the OT DMZ, set up by Koen Martens. Since 2025-01-13 this export arrives every morning, together with 18 months of backfilled history.

A near real time flow would need a different design and a new approval round with OT security. Given the seven weeks the first approval took, that is not feasible within this project.

## Options

1. **Accept daily data for the whole project.** Design all models and the ArcGIS layer around a morning refresh.
2. **Ask for a second, near real time flow now.** New approval round, unknown duration, risk to the pilot in April.
3. **Daily data now, design so a faster feed can be plugged in later.** Same as option 1, with the ingestion and features written so that the time window is a parameter.

## Decision

Option 3.

- The lakehouse in Microsoft Fabric loads the nightly file at 06:00.
- Databricks jobs compute night-flow and pressure features for the previous day by 06:45.
- The model in Azure Machine Learning scores leak candidates by 07:15.
- The ArcGIS candidate layer is refreshed before 07:30, so crews see it at the start of their day.
- Feature jobs take the window length as a parameter, so a shorter window can be used if a faster feed is ever approved.

## Consequences

**Positive**

- Night flow, the strongest leak signal for small and medium leaks, is measured once per night anyway. Daily data loses almost nothing for this.
- Simple, robust, no dependency on a permanent connection.
- No inbound path to the OT network, in line with AquaNova's OT policy.

**Negative**

- Large bursts are not detected faster than today's SCADA alarms. That stays with the control room, as it is now. Leak detection analytics is about the leaks nobody sees.
- A failed nightly export means one day without candidates. Bram adds monitoring on the file drop.
- Pressure transients can only be analysed the next day.

## Follow-up

- Monitoring and alert on a missing or incomplete nightly file (Bram, end of January).
- Procedure for adding tags to the export without a full new approval round (Koen).
- Revisit the latency question after the pilot, as part of the rollout recommendation.

## Related

- I-02 (SCADA data only reachable through the OT DMZ), resolved.
- Data mapping note of 2024-10-18.
