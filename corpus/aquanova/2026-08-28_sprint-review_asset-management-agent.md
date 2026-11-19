# Sprint Review Notes: Sprint 15

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Asset Management Agent |
| **Date** | 2026-08-28 (review held on Thursday 2026-08-27) |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Sprint review / demo notes |
| **Participants** | Kevin Hermans, the pilot coordinator, two asset planners, Pieter De Smet, Jonas Peeters, Ruben Wouters |

## 1. Sprint goal

Three tools working end to end on the full asset register, in the test environment, ready for testing with planners in September.

Result: **reached**, with one open point on response time.

## 2. Demo

Ruben showed the agent in the test environment, built on Foundry Agent Service, with the three tools connected.

**Demo 1: "When was the last intervention on valve 2208114, and what was done?"**
The agent called `get_asset_details` and `get_maintenance_history` and answered in four lines, with the source system (B), the date of the last work order and the free text. The planners checked it in the maintenance system: correct.

**Demo 2: "Which hydrants are within 300 m of Tiensestraat 120?"**
`find_assets_near_location` returned 11 hydrants with distances, and the note "6 hydrants in this zone have no coordinates and may be missing from this list". The pilot coordinator liked that warning: "That's exactly what I'd tell a new colleague."

**Demo 3: "Is pump P-0412 due for an overhaul according to the procedure, and when was it last done?"**
A combined question. The agent used the knowledge base for the overhaul interval and the history tool for the last overhaul. Correct, but the answer took **23 seconds**.

## 3. Data

- The asset data team added **System A records** to the register view on 2026-08-24. The tools now see both systems.
- Asset type mapping (31 rows, from the February profiling) is applied in `get_asset_details`.
- Ruben has not yet run the planned ID overlap check across both systems (profiling finding F-5), because System A records only arrived this week. It is the first task of next sprint.

## 4. Feedback from the planners

- Show the work order number as a clickable reference, not only as text.
- When an asset has more than ten interventions, say how many there are in total.
- The answer to the combined question was good, but "I'd have opened the systems myself by then".

## 5. Platform

Jonas reported that four of five Microsoft Foundry resources now run without public access. The last one follows after a test with Kevin in September.

Kevin raised logging: tool call logs contain the planner's ID. That is agreed for 90 days. He asked that the logs are not exported outside AquaNova's tenant for analysis. Confirmed; analysis is done inside the tenant.

## 6. Sprint 16 plan (2026-08-31 to 2026-09-11)

| # | Item | Owner |
|---|---|---|
| 1 | ID overlap check across systems A and B | RW |
| 2 | Tool testing with three planners on real questions | RW / pilot coordinator |
| 3 | Clickable work order references, total count of interventions | RW |
| 4 | Investigate latency of combined questions | JP |
| 5 | Evaluation set v2 with asset-specific questions | PDS |
| 6 | Last resource to private access | JP / KH |

## 7. Budget note

About 60% of the first phase budget used. Lotte will share a forecast for the remaining tool work in the September status report.
