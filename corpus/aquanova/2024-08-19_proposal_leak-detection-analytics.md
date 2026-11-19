# Proposal: Leak Detection Analytics

| | |
|---|---|
| **Customer** | AquaNova, Leuven |
| **Project** | Leak Detection Analytics |
| **Date** | 2024-08-19 |
| **Author** | Lotte Willems, Managing Partner, Kestrel Consulting |
| **Document type** | Proposal |
| **Version** | 1.0 |

## 1. Context

AquaNova distributes drinking water through a large network of mains, valves and pumping stations. A significant share of the water that enters the network is never billed: non-revenue water, mostly caused by leaks that go unnoticed for weeks. Leak search today relies on night-flow checks per district and on field crews with acoustic equipment, often after a customer reports a problem.

Filip Wuyts, Director Asset Management, wants to find leaks earlier and send crews to the right street instead of the right district. Evelien Claes, GIS Lead, will be product owner. Her team maintains the network model in ArcGIS and will own the result after the project.

## 2. Objectives

1. Combine flow and pressure data from the SCADA system with the network model, asset data and customer consumption.
2. Build a model that detects likely leaks and ranks them by location and size.
3. Show results on the GIS map that the field crews already use.
4. Validate the approach in a pilot zone before any wider rollout.

## 3. Proposed approach

- **Discovery and data access (September to October 2024).** Inventory of SCADA tags in the pilot zone, the ArcGIS network model and consumption data. Choice of the pilot zone together with Evelien.
- **Data platform (October to December 2024).** A lakehouse in **Microsoft Fabric** for history and integration. Time series preparation (cleaning, alignment of pressure and flow signals, night-flow features) in **Databricks**.
- **Model (January to March 2025).** Anomaly detection and leak localisation models trained and tracked in **Azure Machine Learning**, using pressure transients and flow balance per district metered area.
- **Integration and pilot (March to May 2025).** Leak candidates published as a layer in **ArcGIS**, so crews see them next to the network. Field validation with AquaNova crews, model tuning and handover to Evelien's team.

## 4. Team

| Role | Name |
|---|---|
| Engagement lead | Lotte Willems |
| Project lead and data engineer | Sofie Claes, Senior Data Engineer |
| ML engineer | Amira El Idrissi, ML Engineer |
| Databricks engineer | Bram Visser, Databricks Specialist, subcontracted via our partner DataForge (Utrecht) |

On the AquaNova side:

- **Sponsor:** Filip Wuyts, Director Asset Management
- **Product owner:** Evelien Claes, GIS Lead
- **OT contact:** Koen Martens, OT Engineer, for SCADA tags, historian and access to operational data

## 5. Planning

| Milestone | Target date |
|---|---|
| Kickoff in Leuven | 2024-09-02 |
| Pilot zone chosen, data inventory complete | October 2024 |
| First SCADA history in the lakehouse | November 2024 |
| First model version reviewed with Evelien | March 2025 |
| Field validation in pilot zone | April to May 2025 |
| Handover to GIS team | 2025-05-30 |

## 6. Assumptions

- AquaNova provides read access to historical and recent SCADA data for the pilot zone, through Koen Martens.
- The ArcGIS network model of the pilot zone is up to date. Evelien's team corrects known gaps.
- Field crews are available for leak validation in April and May 2025, about two crew days per week.
- No control actions are taken on the SCADA system. The solution only reads data.
- AquaNova pays for Azure consumption and Fabric capacity directly.

## 7. Commercials

- **Contract type:** fixed price
- **Price:** EUR 160,000 excl. VAT, including the subcontracted Databricks work by DataForge
- **Invoicing:** 25% at kickoff, 25% after the data platform phase, 25% after model acceptance, 25% at handover
- **Out of scope:** rollout beyond the pilot zone, hardware (extra pressure loggers), changes to SCADA configuration

## 8. Why Kestrel

We bring together data engineering, machine learning and a pragmatic way of working with operational teams. Bram Visser of DataForge adds deep Databricks experience for the time series work. The team works on site in Leuven at least one day per week.

We look forward to discussing this with Filip and Evelien and can start on 2024-09-02.

*Lotte Willems, Kestrel Consulting, Ghent*
