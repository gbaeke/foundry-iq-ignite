# Data Mapping Notes: SCADA Signals for the Noord-Oost Pilot Zone

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Leak Detection Analytics |
| **Date** | 2024-10-18 |
| **Author** | Bram Visser, Databricks Specialist, DataForge (subcontracted by Kestrel Consulting) |
| **Document type** | Data mapping note |
| **Reviewed by** | Koen Martens (OT), Sofie Claes |

## 1. Purpose

Describe which SCADA signals of zone Noord-Oost we need, how they map onto the network model, and how they will be stored in the Microsoft Fabric lakehouse. This note is also input for the data access request that Koen and Sofie will submit to OT security.

## 2. Source: Koen's tag list

Koen delivered the tag list for Noord-Oost on 2024-10-10: **243 tags** with name, description, unit, resolution and the station they belong to. Not all of them are useful or still in use.

| Tag group | Tags in list | Needed for the model | Remarks |
|---|---|---|---|
| DMA inlet flow | 6 | 4 | two are old meters replaced in 2023, kept for history |
| Pressure points | 14 | 11 | three test points from a past campaign |
| Reservoir level and outflow | 18 | 8 | |
| Pump station (pressure, flow, pump status) | 71 | 30 | many alarm and status bits |
| Valve positions | 29 | 25 | |
| Other (alarms, setpoints, internal counters) | 105 | 0 | not needed |

We need about 78 tags. For the access request, we keep the full list of 243 for now, because the description is not always enough to be sure. Koen will review the doubtful ones.

## 3. Mapping onto the network model

Every needed tag is linked to an object in the ArcGIS network model:

| Tag group | ArcGIS object | Link key |
|---|---|---|
| DMA inlet flow | DMA boundary meter | meter asset ID |
| Pressure points | pressure logger point | logger asset ID |
| Pump station signals | pump station | station code |
| Valve positions | valve | valve asset ID |

For 9 tags the asset ID in the tag description does not exist in the network model. Evelien's GIS analyst checks whether these are renamed assets or errors.

## 4. Lakehouse layout

| Layer | Content | Granularity |
|---|---|---|
| Bronze | raw historian export, one file per day, as delivered | 1 minute or on change |
| Silver | cleaned time series per tag: UTC timestamps, unit conversion, `quality_flag` (`ok`, `gap`, `frozen`, `out_of_range`) | 1 minute |
| Gold | per DMA: inflow, minimum night flow (02:00–04:00), pressure statistics, flow balance | 15 minutes and daily |

Rules for cleaning (Databricks jobs):

- Timestamps in the historian are local time. Converted to UTC; the daylight saving switch on 2024-10-27 is a good first test.
- Gaps are flagged, **not filled**. A filled gap can look like a leak or hide one.
- A value that does not change for more than 6 hours on a signal that normally varies is flagged `frozen`.
- Negative flow on inlet meters is flagged `out_of_range`, except on the one bidirectional meter between two DMAs.

## 5. Open questions for Koen

1. Are the 1-minute values averages or snapshots? (Affects pressure transients.)
2. How far back does the historian keep 1-minute data before it is compressed?
3. Which of the three test pressure points are still physically installed?
4. Is there a list of planned works and flushing in Noord-Oost? These cause night-flow peaks that are not leaks.

## 6. Interim working data

Until the data flow is approved, Koen has provided a one-off manual export of one DMA for two weeks of September (CSV). We use it to build and test the silver layer. Real history is needed before model work can start.

## 7. Next steps

- Koen and Sofie submit the data access request to OT security, based on this note.
- Bram builds the silver jobs on the sample export.
- Amira starts a baseline night-flow analysis on the sample.
