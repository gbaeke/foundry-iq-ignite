# Change Request CR-07: Water damage claim types

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Change request |
| **Date** | 2024-09-13 (version 1.1, approved) |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Submitted** | 2024-09-04 (version 1.0) |
| **Requested by** | Laura Vermeulen, Claims Operations Manager |
| **Approver** | Marc Dubois, Chief Digital Officer |

## 1. Description of the change

Extend the automated triage with **water damage claim types** for private customers. Today these claims fall under "other" and always go to the human triage queue. Water damage is the largest growing claim category at Fortalis.

Sub-types in the first release:

- Pipe leaks (burst or leaking pipes, appliances)
- Infiltration (roof, walls, windows)
- Flooding by heavy rain
- Other water damage (rare sub-types merged, such as sewer backflow and aquarium or waterbed leaks)

## 2. Work included

| # | Work | Owner |
|---|---|---|
| 1 | Document Intelligence extraction models for plumber invoices and leak detection reports | Amira El Idrissi |
| 2 | Extra labelling round for water damage: type, sub-type and severity; labelling guideline addendum | Amira, with Laura's team |
| 3 | Separate severity sub-model for water damage in Azure Machine Learning (levels: contained, spreading, structural or health risk) | Amira |
| 4 | Water damage queue and routing rules in the Logic Apps triage flow; hard rule for "structural or health risk" to human triage | Jonas Peeters |
| 5 | Additional UAT scenarios and test data for water damage | Thomas Maes, Laura's team |
| 6 | Updates to model card, run book and monitoring dashboard | Amira, Jonas |

## 3. Out of scope of this change

- Storm and hail claims (roof damage by wind, hail on vehicles), unless the main damage is water infiltration.
- Commercial lines water damage.
- Photo analysis of water damage.

## 4. Impact

**Cost.** EUR 36,000 excl. VAT, which is **15% of the fixed price** of EUR 240,000. The new contract value is **EUR 276,000** excl. VAT.

| Item | Amount (EUR) |
|---|---|
| Extraction and labelling support | 14,500 |
| Severity sub-model | 8,000 |
| Orchestration and routing | 6,000 |
| Additional UAT and test data | 3,000 |
| Project management | 4,500 |
| **Total** | **36,000** |

This amount includes the exploratory work already done in sprint 10 (about four days, before this change request was written).

**Planning.** The water damage work runs in parallel with integration testing. Milestones:

| Milestone | Date |
|---|---|
| Extraction models for plumber invoices | 2024-10-18 |
| Water damage severity sub-model v1 | 2024-11-08 |
| Water damage UAT scenarios complete | 2024-12-06 |
| Go-live window | January 2025, unchanged |

**Risks.**
- Few labelled examples for rare sub-types; mitigated by merging them into "other water damage".
- Labelling capacity in the claims team in September and October.
- Further scope requests. Proposal: **scope is frozen after CR-07**; new requests go to a backlog for after go-live.

**Invoicing.** The amount is added to the milestone "integration and user acceptance" (50%) and to final acceptance (50%).

## 5. Alternatives considered

- **Phase 2 after go-live.** Lower risk for the planning, but water damage would stay fully manual during the coming winter, the period with most water damage claims.
- **Extraction only, no severity sub-model.** Cheaper, but Laura's team indicated that severity is what drives the routing for water damage.

## 6. Approval

| Role | Name | Decision | Date |
|---|---|---|---|
| Product owner | Laura Vermeulen | Recommended | 2024-09-05 |
| Sponsor | Marc Dubois | **Approved** | 2024-09-13 |
| Kestrel | Thomas Maes | Accepted | 2024-09-13 |

Marc added one condition on approval: the additional effort is tracked separately in the timesheets and reported in each status report until go-live.

*Thomas Maes, Kestrel Consulting*
