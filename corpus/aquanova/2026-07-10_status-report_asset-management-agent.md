# Status Report: Asset Management Agent

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Asset Management Agent |
| **Date** | 2026-07-10 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Monthly status report (June 2026) |
| **Distribution** | Filip Wuyts, Kevin Hermans, Lotte Willems |
| **Project status** | Ongoing |

## 1. Status overview

| Area | Status | Comment |
|---|---|---|
| Overall | Amber | Pilot started on documents; tools behind plan |
| Scope | Green | Phase 1 scope unchanged |
| Schedule | Amber | Tool block planned to end in June, now expected in September |
| Budget | Green | About 46% of the first phase budget used |
| Quality | Green | Document answers stable in the pilot |

## 2. Progress in June

- **Private connectivity** live since 2026-06-03 for the knowledge base storage and the tool backend, through AquaNova's hub network. Public access switched off for two of five Microsoft Foundry resources; the others follow after testing, resource by resource with Kevin's sign-off.
- **Inspection reports** added to the Foundry IQ knowledge base on 2026-06-10, after the permission fix in the Inspections library (I-04 resolved). About 7,800 reports are searchable; the scanned ones remain excluded.
- **Pilot started** on 2026-06-15 with two onboarding sessions. 14 planners invited, 9 active in the first two weeks, 162 conversations in June.
- **Register access:** the asset register view became reachable from the tool backend on 2026-06-22 (I-05 resolved). For now the view contains only System B records (network assets). The asset data team will add System A records in August.
- **Tools:** Ruben has `get_asset_details` working end to end on System B records. `get_maintenance_history` is in development. Tools are not yet available to pilot users.

## 3. Pilot feedback (first two weeks)

- 78% thumbs up on rated answers. Most thumbs down are questions about a specific asset, which the agent cannot answer yet.
- Planners like the source links and document dates.

## 4. Issues

### I-06: Summer availability of the pilot group (open)

Most planners take leave in July or August, and so does the pilot coordinator in the second half of July. Feedback and evaluation scoring will slow down. We will use July and August for tool development and plan the next evaluation round in September.

## 5. Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-01 | Asset data quality limits answers | High | High | Source system in each answer; type mapping in tools |
| R-03 | Planners lose trust after wrong answers | Medium | High | Tools only released to the pilot after testing on the full register |
| R-04 | Remaining resources not moved to private access in time | Low | Medium | Jonas and Kevin plan the remaining switches for August and September |

## 6. Schedule

The tool block was planned for April to June in the SOW. Because the asset register was only reachable from late June, and System A records only come in August, tools for the pilot are now expected in September. Lotte discussed this with Filip on 2026-07-07; Filip prefers a later release over tools that work on half the register.

## 7. Budget

About 46% of the EUR 125,000 first phase budget used, against roughly 55% of the planned time. Lower spend during the summer is expected.

## 8. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | `get_maintenance_history` end to end | RW | 2026-07-24 |
| 2 | `find_assets_near_location` with geocoding service | RW | 2026-08-21 |
| 3 | System A records in the register view | Asset data team via KH | 2026-08-21 |
| 4 | Remaining resources to private access | JP / KH | 2026-09-18 |
| 5 | Evaluation set v2 (asset-specific questions) | PDS / pilot coordinator | 2026-09-11 |

Kestrel holidays: Pieter from 2026-07-20 to 2026-08-07, Ruben from 2026-08-03 to 2026-08-14. Jonas covers questions in that period.
