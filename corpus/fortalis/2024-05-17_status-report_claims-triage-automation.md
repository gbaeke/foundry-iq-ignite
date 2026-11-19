# Status Report: Claims Triage Automation

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Status report (monthly) |
| **Date** | 2024-05-17 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Period** | 2024-04-08 to 2024-05-17 (sprints 1 to 3) |
| **Distribution** | Marc Dubois, Laura Vermeulen |

## 1. Status overview

| Area | Status | Comment |
|---|---|---|
| Overall | Green | Discovery on track |
| Scope | Green | Definitions agreed, logged as scope clarification CR-01 (no cost impact) |
| Planning | Green | Labelling slightly behind, recoverable |
| Budget | Green | Effort in line with plan; first invoice (20% at start) sent |
| Quality | Green | Data profiling complete |

## 2. Progress this period

- **Spoke and access.** Jonas Peeters set up the project spoke in the Fortalis landing zone with the cloud team in the first week. All services use private endpoints, tagging is "strictly confidential" as agreed with the Fortalis architecture team in March. Kestrel staff work through Fortalis-managed accounts only.
- **Process mapping.** The workshop of 2024-04-19 produced agreed definitions for claim type, complexity and urgency (U1 to U3). Laura Vermeulen confirmed them in writing on 2024-04-25; recorded as CR-01, a scope clarification without cost impact.
- **Historical data.** The 18-month extract arrived on 2024-04-24 with 54,812 claims, of which 38,960 in scope. Amira El Idrissi completed the data mapping and profiling. Main data quality findings: 3.2% cross-channel duplicates, a missing policy number at registration in 7% of claims, and inconsistent urgency flags that cannot be used as labels.
- **Decision on routing.** ADR-01 (confidence thresholds and human triage queue) accepted on 2024-05-08.
- **Document types.** A first Azure AI Document Intelligence classifier separates claim forms, repair quotes, police reports, photos and "other". Early results are promising on the claim forms; repair quotes vary a lot between garages.

## 3. Labelling

The two senior claims handlers started labelling complexity and urgency on 2024-05-06. Progress: 640 claims of the 4,000 targeted by end of July. One handler lost a week to the intake peak after the hailstorm at the start of May. Laura has asked a third handler to help on Wednesday afternoons in June.

## 4. Risks and issues

| # | Type | Description | Owner | Action |
|---|---|---|---|---|
| R1 | Risk | Labelling capacity competes with intake peaks | LV | Third handler on Wednesdays; review end of June |
| R2 | Risk | Write interface to the claims system to set the queue does not exist yet; claims system team estimates 4 to 6 weeks | LV | Escalate priority with claims system team lead; we start with a test stub |
| R3 | Risk | Repair quotes from smaller garages vary strongly in layout | AE | Train on top 20 garage layouts first, generic model for the rest |
| R4 | Risk | Agreement between the two labellers on urgency is only moderate | AE | Calibration session on 2024-05-23 with 50 shared claims |

## 5. Next steps

| Action | Owner | Due |
|---|---|---|
| Labelling calibration session | AE / LV | 2024-05-23 |
| Labelling guidelines v1.0 | AE | 2024-05-29 |
| Claims system API: agree interface specification | JP / LV | 2024-06-14 |
| Privacy and security review with the Fortalis DPO (first available date) | JP | 2024-07-04 |
| First extraction model for claim forms | AE | 2024-06-28 |

## 6. Remarks

Ascension (9 May) and Whit Monday (20 May) cost us two sprint days, foreseen in the plan. Nothing requires a decision from the sponsor this month.

*Thomas Maes, Kestrel Consulting*
