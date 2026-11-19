# Kickoff Meeting Notes: Asset Management Agent

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Asset Management Agent |
| **Date** | 2026-02-02, 09:30 to 12:30 |
| **Location** | AquaNova offices, Leuven |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Meeting notes |

## Attendees

- Filip Wuyts, Director Asset Management, AquaNova (sponsor)
- Kevin Hermans, IT Architect, AquaNova
- An asset planner, proposed as pilot coordinator
- Pieter De Smet, Kestrel Consulting (lead architect)
- Jonas Peeters, Kestrel Consulting (platform engineer)
- Ruben Wouters, Kestrel Consulting (developer)
- Lotte Willems, Kestrel Consulting (engagement lead, planning and commercials)

## 1. Why this project

Filip opened with an example from last week. A planner needed to prepare the replacement of a pressure-reducing valve. She looked in the asset register for the valve, in the maintenance history for past interventions, in a document library for the last inspection report, and in another library for the technical sheet of the valve type. It took her most of a morning. "Multiply that by forty planners," Filip said.

The pilot coordinator confirmed: most of a planner's questions are about one asset, its history and its documents.

## 2. Scope recap (SOW-AQN-02)

Pieter presented the phase 1 scope:

- An agent on **Foundry Agent Service** in a **Microsoft Foundry** project in AquaNova's Azure tenant.
- A **Foundry IQ** knowledge base over maintenance procedures, inspection reports and technical asset documents.
- Read-only agent tools on the asset register and the maintenance history.
- A web chat for a pilot group of about 15 asset planners.
- An evaluation set agreed with the planners and a report on answer quality.

Out of scope: writing back to source systems, creating work orders, mobile access for field crews.

Time and materials, first phase EUR 125,000. Kestrel warns when 80% of the budget is used.

## 3. Architecture and security

Kevin will approve the architecture and the security design. His starting points:

- Everything runs inside AquaNova's tenant. No AquaNova data in Kestrel systems.
- Target: no public endpoints for the Foundry resources. Jonas and Kevin will work out the networking in February.
- Access for planners through existing AquaNova groups. The agent sees only what the asking planner is allowed to see in the document libraries.
- Read only towards the asset register and maintenance history, through a service account with minimal rights.

Jonas asked whether a temporary setup with restricted public access is acceptable for the build phase. Kevin: yes, for development data only, until private networking is ready.

## 4. Data

The asset register is fed from two legacy systems. Kevin warned that the data is "not as clean as the dashboards suggest". Ruben will do a short data profiling exercise in February on extracts of both systems.

Documents: Kevin estimates several thousand inspection reports, a few hundred procedures and a few thousand technical sheets. Some older inspection reports are scans.

## 5. Ways of working

- Two-week sprints, review every second Thursday with the pilot coordinator and Kevin.
- Monthly status report to Filip, Kevin and Lotte.
- Steering meeting every two months, chaired by Filip.
- Kestrel on site in Leuven on Wednesdays.

## Decisions

1. Pilot coordinator: the asset planner attending today, confirmed by Filip.
2. Development starts with the knowledge base; tools follow once read access to the asset register is in place.
3. Evaluation questions come from real planner questions, not from the project team.

## Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Access to the Azure tenant, groups and asset register read access | KH | 2026-02-13 |
| 2 | Extracts of both legacy systems for profiling | KH | 2026-02-11 |
| 3 | Networking and identity proposal (ADR-01) | JP | 2026-02-27 |
| 4 | Data profiling note | RW | 2026-02-20 |
| 5 | Collect 50 real questions from planners | Pilot coordinator | 2026-03-20 |
| 6 | Inventory of document libraries | PDS / KH | 2026-02-20 |
