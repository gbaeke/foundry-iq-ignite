# Status Report: Leak Detection Analytics

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Leak Detection Analytics |
| **Date** | 2024-09-27 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Status report (report no. 1) |
| **Reporting period** | 2024-09-02 to 2024-09-27 |
| **Distribution** | Filip Wuyts, Evelien Claes, Koen Martens, Lotte Willems |

## 1. Overall status

| Area | Status | Comment |
|---|---|---|
| Overall | Green | Discovery on plan |
| Scope | Green | Pilot zone chosen |
| Schedule | Green | |
| Budget | Green | About 9% of the fixed price used |
| Data access | Amber | Path to SCADA data not yet defined |

## 2. Progress this period

- **Kickoff** held in Leuven on 2024-09-02.
- **Pilot zone chosen:** Noord-Oost, 4 district metered areas, after a scoring workshop on 2024-09-20. Filip confirmed on 2024-09-23.
- **Labels:** Filip delivered three years of leak repair work orders. 212 repairs in Noord-Oost. The GIS team started geocoding them onto the network model.
- **Platform:** the Microsoft Fabric workspace is set up in AquaNova's tenant, with separate access groups for Kestrel, DataForge and the GIS team. Bram has a Databricks workspace connected to the same lakehouse storage.
- **Consumption data:** the billing team can deliver meter readings per address. Most readings are yearly, which limits their use for leak detection. We will use them for the yearly water balance only.

## 3. Issues

None open.

## 4. Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-01 | Access to SCADA history takes longer than planned | Medium | High | Define the data flow early with Koen; work on exports in the meantime |
| R-02 | Network model gaps in Noord-Oost hurt localisation | Medium | Medium | GIS team corrects gaps before the model phase |
| R-03 | Repair dates are not leak start dates | High | Medium | Estimate start from night-flow history |

## 5. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Tag list Noord-Oost | KM | 2024-10-11 |
| 2 | SCADA data mapping note | BV | 2024-10-18 |
| 3 | Data access proposal to OT security | KM / SC | end of October |
| 4 | Network model gap list | EC | 2024-10-11 |
| 5 | Baseline night-flow analysis on a manual export of one DMA | AEI | 2024-10-25 |

Next status report: 2024-10-25. Next steering meeting: 2024-11-08 (to be confirmed by Filip).
