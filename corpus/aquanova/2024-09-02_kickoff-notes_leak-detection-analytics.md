# Kickoff Meeting Notes: Leak Detection Analytics

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Leak Detection Analytics |
| **Date** | 2024-09-02, 10:00 to 13:00 |
| **Location** | AquaNova offices, Leuven |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Meeting notes |

## Attendees

- Filip Wuyts, Director Asset Management, AquaNova (sponsor)
- Evelien Claes, GIS Lead, AquaNova (product owner)
- Koen Martens, OT Engineer, AquaNova
- Sofie Claes, Kestrel Consulting (project lead and data engineer)
- Amira El Idrissi, Kestrel Consulting (ML engineer)
- Bram Visser, DataForge (Databricks engineer, subcontracted)
- Lotte Willems, Kestrel Consulting (engagement lead), first hour

A note on names, since it came up immediately: Evelien Claes (AquaNova) and Sofie Claes (Kestrel) are not related. In action items we use the initials EC and SC.

## 1. Context from Filip

Filip described the non-revenue water problem. Leak search today starts from night-flow checks per district metered area (DMA) and acoustic searches by field crews, usually after a customer calls. A leak on a service pipe can run for weeks before anyone notices. The board has set a target to reduce non-revenue water, and Filip wants to send crews "to a street, not to a district".

## 2. Scope recap

Sofie walked through the proposal:

- Discovery and data access in September and October, including the choice of a pilot zone.
- A Microsoft Fabric lakehouse for history, with time series preparation in Databricks (Bram).
- Anomaly detection and localisation models in Azure Machine Learning (Amira).
- Leak candidates as a layer in ArcGIS, so crews see them on the map they already use.
- Field validation in April and May 2025, handover to Evelien's GIS team on 2025-05-30.
- Fixed price, EUR 160,000 excl. VAT.

The solution only reads data. No control actions on the SCADA system.

## 3. Data sources discussed

| Source | Owner | First remarks |
|---|---|---|
| SCADA historian (flow, pressure, reservoir levels) | Koen | sits in the OT network, see section 4 |
| ArcGIS network model | Evelien | good for mains, gaps in material and diameter for older segments |
| Customer consumption (meter readings) | billing team, via Filip | quarterly or yearly readings for most customers, smart meters for a minority |
| Work orders of past leak repairs | asset management | needed as labels for the model |

## 4. Access to operational data

Koen explained that the historian is in the OT network and that AquaNova applies strict separation between OT and the office network. He will first check which tags exist for the candidate pilot zones, and then look into how the data can be made available. "Read only" is a necessary condition, but it is not sufficient on its own; OT security will want to see the exact data flow.

Sofie asked whether the approach could already be discussed with OT security in September. Koen prefers to come with a concrete tag list first.

## 5. Ways of working

- Kestrel on site in Leuven every Tuesday.
- Status report every four weeks to Filip, Evelien, Koen and Lotte.
- Steering meeting every two months, chaired by Filip.

## Decisions

1. The pilot zone is chosen in a workshop on 2024-09-20, based on data availability and leak history.
2. Past repair work orders are used as training labels.
3. Results are shown in ArcGIS, not in a separate application.

## Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | List of DMAs with flow and pressure measurement | KM | 2024-09-17 |
| 2 | Leak repair work orders of the last three years, export | FW | 2024-09-17 |
| 3 | Known gaps in the network model per DMA | EC | 2024-09-17 |
| 4 | Workshop pilot zone selection | SC | 2024-09-20 |
| 5 | Fabric workspace and access groups in AquaNova's tenant | SC / AquaNova IT | 2024-09-27 |
