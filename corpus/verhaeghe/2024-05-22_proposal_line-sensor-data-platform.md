# Proposal: Line Sensor Data Platform

| | |
|---|---|
| **Customer** | Verhaeghe Foods, Roeselare |
| **Project** | Line Sensor Data Platform |
| **Date** | 2024-05-22 |
| **Author** | Lotte Willems, Managing Partner, Kestrel Consulting |
| **Document type** | Proposal |
| **Version** | 1.1 (after review call of 2024-05-17) |

## 1. Context

Verhaeghe Foods processes and freezes vegetables on several production lines in Roeselare. Each line already carries sensors on blanchers, tunnel freezers and packaging equipment: temperatures, belt speeds, energy use and moisture. Today the readings stay in the line PLCs and local HMIs. Quality reports are put together by hand from exports and paper logs, and nobody can look at trends across lines or across seasons.

Ann Verhaeghe, CEO, wants one central data platform so that quality and production decisions are based on the same numbers. Dries Callens, Quality Manager, will be product owner and has asked first for traceability of freezing temperatures per batch, and for early warnings when a blancher drifts outside its range.

## 2. Objectives

1. Collect sensor data from the production lines in near real time in a central, governed platform.
2. Keep a history of at least two seasons for trend analysis and audits.
3. Give Dries' quality team reports per batch, per line and per shift.
4. Lay a foundation for later use cases (predictive maintenance, image-based inspection).

## 3. Proposed approach

We propose a phased delivery over roughly eight months.

- **Phase 1, Connect (June to August 2024).** Inventory of sensors and PLC tags per line, an edge gateway per line, and telemetry ingestion into **Azure IoT Hub**. We start with one line as pilot and roll out line by line.
- **Phase 2, Platform (August to November 2024).** A lakehouse in **Microsoft Fabric** with bronze, silver and gold layers. Heavier transformations, such as resampling high-frequency signals and linking batches to sensor windows, run in **Databricks** notebooks on the same storage.
- **Phase 3, Insight (November 2024 to January 2025).** Quality dashboards for Dries' team, alert rules for blancher and freezer ranges, documentation and handover.

### Architecture at a glance

Line sensors and PLCs feed an edge gateway, which feeds Azure IoT Hub. From there the data lands in the Fabric lakehouse, Databricks handles the transformations, and the gold layer serves the operational reports.

## 4. Team

| Role | Name |
|---|---|
| Engagement lead | Lotte Willems |
| Project lead and data engineer | Sofie Claes, Senior Data Engineer |
| IoT and platform engineer | Jonas Peeters, Cloud Platform Engineer |
| Databricks engineer | Bram Visser, Databricks Specialist, subcontracted via our partner DataForge (Utrecht) |

On the Verhaeghe side:

- **Sponsor:** Ann Verhaeghe, CEO
- **Product owner:** Dries Callens, Quality Manager
- **IT contact:** Tine Desmet, IT Coordinator, for network, accounts and the Azure tenant

## 5. Planning

| Milestone | Target date |
|---|---|
| Kickoff on site in Roeselare | 2024-06-03 |
| Pilot line streaming to IoT Hub | end of July 2024 |
| Lakehouse and batch linking in place | November 2024 |
| All lines in scope connected, handover | 2025-01-31 |

## 6. Assumptions

- Verhaeghe gives us network access from the line gateways to Azure, coordinated by Tine Desmet.
- Line operators and maintenance are available for the tag inventory, about half a day per line.
- The Azure subscription and Fabric capacity are paid for by Verhaeghe directly.
- Work on the lines is done outside the peak harvest weeks where possible.

## 7. Commercials

- **Contract type:** fixed price
- **Price:** EUR 130,000 excl. VAT, covering the three phases above, including DataForge's subcontracted work
- **Invoicing:** 30% at kickoff, 40% when the platform phase is accepted, 30% at final handover
- **Change requests:** extra lines or use cases are quoted separately

## 8. Next steps

We propose a short call with Dries and Tine before the end of May to confirm the list of lines and gateways. Once Ann signs, we can start on 2024-06-03 as planned.

*Lotte Willems, Kestrel Consulting, Ghent*
