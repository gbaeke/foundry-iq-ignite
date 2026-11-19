# Status Report: Scaldis Ops Copilot

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Scaldis Ops Copilot |
| **Date** | 2025-05-16 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Document type** | Status report |
| **Reporting period** | Sprints 8 and 9 (2025-04-14 to 2025-05-16) |
| **Distribution** | Koen Verstraete, Nathalie Dumont, Wim Goossens, Lotte Willems |

## 1. Overall status

| Dimension | Status | Comment |
|---|---|---|
| Overall | **Red** | Go-live of 2025-07-01 no longer achievable |
| Scope | Amber | Permission trimming added as mandatory requirement |
| Schedule | Red | Go-live re-planned to 2025-09-15 |
| Budget (T&M) | Amber | 61% of EUR 150,000 estimate consumed; forecast above estimate |
| Quality | Green | Pilot feedback positive |

## 2. Summary

Wim Goossens brought the security review forward after the pilot started, and the outcome is clear: the copilot must apply **document-level permission trimming** on SharePoint content. A user may only receive answers based on documents they are allowed to open in SharePoint. The current index treats the operations library as one shared corpus, which is acceptable for most SOPs but not for the restricted folders that were added to the scope in March (incident handling, customs procedures, access control).

We agree with the finding. It does mean rework of the indexing pipeline and the query layer, and a new round of testing with Wim's team. After discussion with Koen and Nathalie on 2025-05-13, **go-live is re-planned to 2025-09-15**. The July and August holiday period ("bouwverlof" for several shift leaders) makes an earlier date unrealistic for user testing.

## 3. Progress this period

- **Teams bot front end.** Ruben Wouters built the Teams bot front end: adaptive answer cards with source links, feedback buttons, language detection and a "contact the shift leader" fallback. Elien Jacobs reviewed it with the pilot users; the design is stable.
- **Pilot.** 25 pilot users active since sprint 6. About 410 questions asked; 78% rated helpful.
- **Indexing.** All 1,800 operations documents indexed, including French and English versions.
- **Security review.** Review report received from Wim on 2025-05-09 with 11 findings: 1 high (permission trimming), 4 medium, 6 low.

## 4. Risks and issues

| ID | Type | Description | Owner | Status |
|---|---|---|---|---|
| I-11 | Issue | No document-level permission trimming in search results (high finding) | PDS | Open, redesign in progress |
| R-14 | Risk | Security trimming increases query latency | PDS | Open |
| R-15 | Risk | Holiday period limits availability for UAT | ND | Open |
| R-16 | Risk | T&M forecast exceeds EUR 150,000 estimate | TM | Open, revised forecast at next steerco |
| R-17 | Risk | SharePoint group structure is inconsistent across sites | WG | Open |

The root cause of the delay is that the security review was planned only at the end, right before go-live, while the restricted content was added to scope midway.

## 5. Next steps

- Redesign of index with security filters based on SharePoint permissions and group membership (PDS, sprint 10 and 11)
- Clean-up of SharePoint group structure on restricted sites (WG with site owners, by 2025-06-20)
- Fix medium findings (RW, PDS, by 2025-06-13)
- Revised budget forecast and plan to steering committee (TM, 2025-05-27)
- Re-test with Wim's team planned for the second half of August

## 6. Updated milestones

| Milestone | Original | Re-planned |
|---|---|---|
| Security re-test | June 2025 | August 2025 |
| Go-live | 2025-07-01 | 2025-09-15 |

Thomas Maes
