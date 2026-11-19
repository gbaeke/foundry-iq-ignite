# Status Report: Scaldis Ops Copilot

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Scaldis Ops Copilot |
| **Date** | 2025-06-20 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Document type** | Status report |
| **Reporting period** | Sprints 10 and 11 (2025-05-19 to 2025-06-13), plus week 25 |
| **Distribution** | Koen Verstraete, Nathalie Dumont, Wim Goossens, Lotte Willems |

## 1. Overall status

| Dimension | Previous report | This report | Comment |
|---|---|---|---|
| Overall | Red | **Amber** | Redesign on track for the re-planned date |
| Scope | Amber | Green | Permission trimming now part of baseline scope |
| Schedule | Red | Amber | Go-live 2025-09-15 holds; little slack |
| Budget (T&M) | Amber | Amber | Tracking the revised forecast approved on 27 May |
| Quality | Green | Green | Regression and adversarial sets stable |

## 2. Progress

- **Permission trimming (I-11).** ADR-03 accepted by Wim Goossens on 5 June. Permission sync and query filter implemented by Pieter De Smet in sprints 10 and 11. The automated test over the 40 × 12 test matrix passes on the general library.
- **Medium findings.** M-02 (app secret moved to a secrets vault, rotation every 90 days) and M-03 (rate limit of 30 questions per user per 10 minutes) fixed by Ruben Wouters. M-01 implemented: pseudonymised IDs, 90-day retention. M-04: approvals received from all site owners, indexing scope reduced.
- **Group clean-up.** Wim and the site owners finished the restricted sites today. 17 individual permissions replaced by groups; two obsolete groups removed.
- **Pilot.** Still running with 25 users. About 620 questions since 24 March.

## 3. Risks and issues

| ID | Type | Description | Owner | Status |
|---|---|---|---|---|
| I-11 | Issue | No document-level permission trimming (H-01) | PDS | In progress, general library done |
| R-14 | Risk | Security trimming increases query latency | PDS | Open, performance test 2025-07-02 |
| R-15 | Risk | Holiday period limits availability for UAT | ND | Open, UAT moved to end of August |
| R-16 | Risk | T&M forecast exceeds EUR 150,000 estimate | TM | Accepted by steering committee, monitored |
| R-17 | Risk | SharePoint group structure inconsistent across sites | WG | Closed today |
| R-09 | Risk | Generic account on shared gate PCs | RW | Open; Scaldis IT investigating personal sign-in |

## 4. Team

From 1 July I work 60% on Kestrel projects. Status reports and steering committees continue as planned; Pieter covers day-to-day questions on Thursdays and Fridays.

## 5. Next steps

| Action | Owner | Due |
|---|---|---|
| Index restricted libraries with trimming, spot-check with site owners | PDS | 2025-06-27 |
| Extend pilot to restricted content for pilot shift leaders | ND, RW | 2025-07-01 |
| Performance test with security filters | PDS, RW | 2025-07-02 |
| Training outline and champion programme | EJ | 2025-07-11 |
| UAT plan for 18–29 August | TM, ND | 2025-06-27 |
| Security re-test slot confirmed | WG | 2025-07-04 |

## 6. Milestones

| Milestone | Re-planned | Status |
|---|---|---|
| Redesign implemented | 2025-06-13 | Done |
| Restricted libraries indexed | 2025-06-27 | On track |
| Security re-test | second half of August | Planned |
| Go-live | 2025-09-15 | On track, amber |

Thomas Maes
