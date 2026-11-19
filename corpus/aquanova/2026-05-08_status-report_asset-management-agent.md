# Status Report: Asset Management Agent

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Asset Management Agent |
| **Date** | 2026-05-08 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Monthly status report (April 2026) |
| **Distribution** | Filip Wuyts, Kevin Hermans, Lotte Willems |
| **Project status** | Ongoing |

## 1. Status overview

| Area | Status | Comment |
|---|---|---|
| Overall | Amber | Knowledge base on track, tools waiting on register access |
| Scope | Green | Phase 1 scope unchanged |
| Schedule | Amber | Tool block started, but no access to the asset register view yet |
| Budget | Green | About 26% of the first phase budget used |
| Quality | Green | Procedures and technical sheets at 89% correct in second run |

## 2. Progress in April

- **Knowledge base:** the Foundry IQ knowledge base covers maintenance procedures and technical sheets. First evaluation on 2026-04-17: 81% correct. After excluding superseded procedures, answering in Dutch and adding table context, the second run on 2026-05-06 reached **89% correct** (24 of 27), above the 85% target. All 5 permission questions correctly returned "no information".
- **Superseded documents:** the new owner of the Procedures library archived 46 old versions. Two libraries still have no owner.
- **Agent:** the agent in Foundry Agent Service now has clear instructions on sources, language and "say when you don't know". Ruben added a source panel to the web chat.
- **Tools:** Ruben started the design of four read-only tools. Development is on the anonymised sample, because the asset register view is not yet reachable from the Foundry project (I-05).
- **Networking:** the hub team scheduled the integration for the second half of May. Jonas prepared the templates for private connectivity.

## 3. Issues

### I-03: Scanned inspection reports (open, accepted)

About 1,400 older inspection reports have no text layer and are excluded in phase 1. The agent says so when the metadata shows such a report. Conversion to be considered for phase 2.

### I-04: Permissions in the Inspections libraries (open)

One of the three Inspections libraries has broken inheritance on many folders: some planners have access to subfolders they should not see, others miss access they need. Because the knowledge base respects source permissions, this would show up directly in answers. Kevin has asked the library administrator to fix it before inspection reports are added in June.

### I-05: No access to the asset register view (open)

The register view is only reachable from inside AquaNova's network, so the tools can only be tested end to end once private networking is in place (ADR-01). The read-only service identity has been created. Expected: early June.

## 4. Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-01 | Asset data quality limits answers | High | High | Source system shown in each answer; type mapping confirmed by asset data team |
| R-03 | Planners lose trust after wrong answers | Medium | High | Evaluation before pilot; sources always shown |
| R-04 | Private networking later than planned | Medium | High | Hub team date confirmed for second half of May |

## 5. Budget

About 26% of the EUR 125,000 first phase budget used. Model consumption costs in AquaNova's subscription are low during development (under EUR 150 in April).

## 6. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Tool design note | RW | 2026-05-29 |
| 2 | Private connectivity live | JP / KH | 2026-05-29 |
| 3 | Fix permissions in Inspections library | KH | 2026-05-29 |
| 4 | Pilot onboarding plan | PDS | 2026-06-12 |
| 5 | Evaluation set v2 with more asset-specific questions | PDS / pilot coordinator | 2026-06-12 |

Ascension Day (2026-05-14) and Whit Monday (2026-05-25) are holidays; expect reduced availability of the pilot coordinator and planners in those weeks.
