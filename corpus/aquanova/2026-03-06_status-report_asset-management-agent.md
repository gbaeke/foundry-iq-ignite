# Status Report: Asset Management Agent

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Asset Management Agent |
| **Date** | 2026-03-06 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Monthly status report (February 2026) |
| **Distribution** | Filip Wuyts, Kevin Hermans, Lotte Willems |
| **Project status** | Ongoing |

## 1. Status overview

| Area | Status | Comment |
|---|---|---|
| Overall | Green | Foundation block completed with a small delay on access |
| Scope | Green | Phase 1 scope unchanged |
| Schedule | Green | Knowledge block starts as planned |
| Budget | Green | About 8% of the first phase budget used |
| Quality | Amber | Profiling shows asset data issues, as expected |

## 2. Progress in February

- **Kickoff** in Leuven on 2026-02-02. Pilot coordinator named among the asset planners.
- **Access:** guest accounts for Kestrel, the resource group and the pilot group were ready on 2026-02-19, a week after the SOW date of 2026-02-13 (see I-01).
- **Data profiling:** Ruben profiled extracts of both legacy systems. Main findings: different asset type codes per system, missing coordinates for 8% of valves and hydrants in System B, unreliable status values in System A, and an unchecked risk of overlapping IDs between the two systems. Note shared on 2026-02-20.
- **ADR-01 (networking and identity)** accepted by Kevin on 2026-02-26: phased approach, restricted public access for development with a limited set of documents, private networking through AquaNova's hub network from June.
- **Microsoft Foundry project** created from templates in AquaNova's repository. The language model deployment and the Foundry Agent Service setup are in place in the development environment.
- **Document library inventory:** about 380 maintenance procedures, 9,200 inspection reports and 2,700 technical sheets across five libraries.

## 3. Issues

### I-01: Tenant and group access later than planned (resolved)

The access request needed approval from AquaNova's security team, which meets weekly. Access came on 2026-02-19 instead of 2026-02-13. Impact: the team used the week for the profiling and the library inventory. No schedule impact.

### I-02: No owner for two document libraries (open)

Two of the five libraries have no clear owner. Nobody can confirm which documents in them are current. Kevin will ask Filip to assign owners.

## 4. Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-01 | Asset data quality limits answers about specific assets | High | High | Profiling findings to asset data team; caveats in tool answers |
| R-02 | Low adoption by planners | Medium | Medium | Real questions in the evaluation set; pilot coordinator involved in every review |
| R-03 | Planners lose trust after wrong answers | Medium | High | Evaluation before pilot, sources shown with every answer |
| R-04 | Private networking takes longer than planned | Medium | Medium | Request hub integration early (done 2026-03-04) |

## 5. Budget

About EUR 10,000 of the EUR 125,000 first phase budget used (about 8%). Invoiced monthly on approved timesheets.

## 6. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | First knowledge base on procedures and technical sheets | PDS | 2026-03-27 |
| 2 | Evaluation workshop with planners | PDS / pilot coordinator | 2026-03-25 |
| 3 | Owners for the two libraries without owner | KH / FW | 2026-03-20 |
| 4 | Asset type mapping to the asset data team | RW | 2026-03-13 |
| 5 | Hub network integration, design session | JP / KH | 2026-03-18 |

Next steering meeting: 2026-04-02.
