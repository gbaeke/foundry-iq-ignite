# Status Report: Leak Detection Analytics

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Leak Detection Analytics |
| **Date** | 2025-01-24 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Status report (report no. 5) |
| **Reporting period** | 2024-12-13 to 2025-01-24 (including holiday period) |
| **Distribution** | Filip Wuyts, Evelien Claes, Koen Martens, Lotte Willems |

## 1. Overall status

| Area | Status | Comment |
|---|---|---|
| Overall | Amber, improving | SCADA data now flowing, model work started late |
| Scope | Green | Unchanged |
| Schedule | Amber | About 4 weeks behind on model phase |
| Budget | Green | Within fixed price |
| Data quality | Green | SCADA history complete for pilot zone |

## 2. Progress this period

- **SCADA data available.** Since 2025-01-13 the pressure and flow history of the pilot zone ("zone Noord-Oost", 4 district metered areas) arrives daily in the Fabric lakehouse. Eighteen months of history have been loaded.
- **Databricks pipelines.** Bram has finished the time series cleaning and the night-flow feature jobs. Gaps and frozen sensor values are flagged, not filled.
- **First model experiments.** Amira started baseline anomaly models in Azure Machine Learning on the first three weeks of complete data. Too early for results.
- **GIS.** Evelien's team corrected 37 pipe segments with missing material or diameter in the ArcGIS model of the pilot zone.

## 3. Issues

### I-02: SCADA data only reachable through the OT DMZ (resolved)

The SCADA historian sits in AquaNova's OT network. The only allowed path to it is through the OT DMZ, and any new data flow out of the DMZ needs approval from the OT security process. A direct connection from Azure to the historian was not acceptable.

The approval took **7 weeks**, from the first request at the end of October to sign-off in mid-December. During that time we worked on synthetic and exported sample data, which kept the pipelines moving but delayed model work.

The solution was designed and set up by Koen Martens, OT Engineer: a **data diode export** from the historian to a file drop in the DMZ. Data can only flow out of the OT network, never back in. Every night an export of the agreed tags lands in the DMZ, from where it is picked up and loaded into the lakehouse. Koen also cleaned up the tag list, which removed about 60 tags that were no longer in use. Many thanks to Koen for taking this on over the holidays.

Consequence: data is daily, not near real time. For leak detection based on night flow this is acceptable. Evelien and Filip agreed on 2025-01-17.

## 4. Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-04 | Model phase compressed by the access delay | High | Medium | Shift part of the tuning into the pilot phase, field validation stays in April |
| R-05 | Changes to the tag list need a new approval round | Medium | Medium | Freeze tag list for the pilot; KM to confirm process for small changes |
| R-06 | Field crew capacity in spring | Medium | High | Book crew days with Filip's planning now |
| R-07 | Daily export fails without anyone noticing | Low | Medium | Monitoring and alert on missing file drop |

## 5. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Alert when the nightly export is missing or incomplete | BV | 2025-01-31 |
| 2 | Confirm procedure for adding tags to the export | KM | 2025-02-07 |
| 3 | Baseline anomaly model, first results to Evelien | AEI | 2025-02-21 |
| 4 | Reserve field crew days for April and May | FW | 2025-02-14 |
| 5 | Updated planning to steering committee | SC | 2025-01-31 |

Next steering meeting: 2025-02-07 in Leuven.
