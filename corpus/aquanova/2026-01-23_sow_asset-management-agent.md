# Statement of Work: Asset Management Agent

| | |
|---|---|
| **Customer** | AquaNova, Leuven |
| **Project** | Asset Management Agent |
| **Date** | 2026-01-23 |
| **Author** | Lotte Willems, Managing Partner, Kestrel Consulting |
| **Document type** | Statement of work (SOW-AQN-02) |
| **Version** | 1.0, for signature |

## 1. Background

AquaNova manages thousands of assets: mains, valves, hydrants, pumps and reservoirs. Information about these assets is spread over the asset register, maintenance history, inspection reports and technical documents. Asset planners lose a lot of time looking up the status, history and documents of a single asset before they can plan work or answer a question from the field.

Filip Wuyts, Director Asset Management, wants an AI agent that asset planners can ask questions in plain language, and that can look up and combine information from these sources. This SOW covers the first phase. It follows the earlier cooperation between AquaNova and Kestrel on leak detection.

## 2. Stakeholders

| Role | Name |
|---|---|
| Sponsor | Filip Wuyts, Director Asset Management |
| IT architect and technical counterpart | Kevin Hermans, IT Architect |
| Engagement lead (Kestrel) | Lotte Willems |

Kevin Hermans joined AquaNova as IT Architect on 2025-09-01. He was previously at Fortalis Verzekeringen and knows Kestrel's way of working from there. Kevin will approve the architecture, the security design and the integration with AquaNova's systems.

## 3. Scope of phase 1

In scope:

1. An agent built on **Foundry Agent Service** in **Microsoft Foundry**, deployed in AquaNova's Azure tenant.
2. A knowledge base in **Foundry IQ** over maintenance procedures, inspection reports and technical asset documents.
3. Agent tools to query the asset register and the maintenance history (read only).
4. A web chat for a pilot group of about 15 asset planners.
5. An evaluation set of questions agreed with the planners, and a report on answer quality.

Out of scope for phase 1: writing back to source systems, creating work orders, field crew access on mobile devices.

## 4. Approach

| Sprint block | Period | Content |
|---|---|---|
| 1. Foundation | February 2026 | Foundry project, networking and identity with Kevin, source inventory |
| 2. Knowledge | March to April 2026 | Foundry IQ knowledge base, document ingestion, first evaluation |
| 3. Tools | April to June 2026 | Agent tools on asset register and maintenance history |
| 4. Pilot | from June 2026 | Pilot with planners, feedback rounds, evaluation report |

The asset register is fed from two legacy systems. Data quality of the asset data is a known risk. A short data profiling exercise is part of sprint block 1.

## 5. Team

| Role | Name |
|---|---|
| Lead architect | Pieter De Smet, Lead AI Architect |
| Platform engineer | Jonas Peeters, Cloud Platform Engineer |
| Developer | Ruben Wouters, Developer |

Pieter is the day-to-day contact for Kevin and the pilot group. Lotte follows up on planning and commercials.

## 6. Commercials

- **Contract type:** time and materials
- **Budget first phase:** EUR 125,000 excl. VAT, based on the effort estimate in annex A
- **Start date:** 2026-02-02
- **Invoicing:** monthly, based on approved timesheets
- **Reporting:** monthly status report; Kestrel warns AquaNova as soon as 80% of the budget is used
- Azure consumption is billed to AquaNova directly.

## 7. Assumptions and dependencies

- Kevin arranges access to the Azure tenant, Entra ID groups and read access to the asset register before 2026-02-13.
- AquaNova names a pilot coordinator among the asset planners.
- Documents for the knowledge base are delivered from the existing document libraries.

## 8. Acceptance

Phase 1 is accepted when the agent is available to the pilot group and the evaluation report has been discussed with Filip and Kevin.

| For AquaNova | For Kestrel Consulting |
|---|---|
| Filip Wuyts | Lotte Willems |
| Date: | Date: |
