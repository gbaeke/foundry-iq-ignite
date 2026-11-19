# Change Request CR-01: Restricted Operations Libraries in Scope

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Scaldis Ops Copilot |
| **Date** | 2025-03-12 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Document type** | Change request |
| **Requested by** | Nathalie Dumont, product owner |
| **Decision forum** | Steering committee of 2025-03-20 |

## 1. Request

Add three restricted SharePoint libraries of the operations department to the scope of release 1:

| Library | Approx. documents | Current access |
|---|---|---|
| Incident handling (spills, injuries, quay incidents, evacuation) | 140 | Shift leaders, HSE, management |
| Customs procedures (inspection zone, seals, holds) | 95 | Customs desk, shift leaders, planners |
| Access control (gate exceptions, visitor and contractor access) | 65 | Gate supervisors, security, shift leaders |

Together about 300 documents, on top of the roughly 1,800 documents of the general operations library.

## 2. Reason

During the user tests of the answer cards (week of 24 February), shift leaders asked for incident and gate exception procedures more often than for anything else. Without them, Nathalie expects the copilot to miss the moments where speed matters most, typically at night when no colleague is around to ask.

## 3. Impact analysis

**Functional.** Same answer cards and dialogue flow. The bot must only use restricted documents for users who are allowed to open them in SharePoint.

**Technical.** The three libraries use the same structure as the general library. Indexing is a configuration change. Restricting answers per user requires that the index knows who may read each document and that queries are filtered accordingly. In this CR we propose a first, simpler approach: restricted libraries go into a **separate index**, and the bot queries that index only for users in the SharePoint groups of the library owners. Fine-grained, document-level rules are not foreseen.

**Planning.** Indexing of the restricted libraries in sprint 7. Restricted content is **not** exposed to pilot users until the security review has assessed the approach.

**Budget.** Estimated additional effort: 6 to 8 person-days, within the existing T&M estimate of EUR 150,000. **No change to the estimate.**

**Security impact assessment.** Wim Goossens was consulted by mail on 2025-03-11. His position: acceptable to prepare, but the access approach must be part of the formal security review before any restricted content is used in production. The review is planned for June.

## 4. Risks introduced

| ID | Risk | Mitigation |
|---|---|---|
| R-12 | Group-level filtering may not match the actual document permissions inside a library | Check permissions on a sample of documents with the site owners |
| R-13 | SharePoint groups differ per site; mapping effort may be larger than estimated | Inventory of groups in sprint 7 |

## 5. Alternatives considered

1. Keep restricted content out of release 1 and plan it for a release 2. Rejected by Nathalie: the use case would lose most of its value for shift leaders.
2. Copy restricted documents to an open library in shortened form. Rejected: creates a second, unmanaged version of each procedure.

## 6. Decision

| | |
|---|---|
| Recommendation of the project team | Approve, with restricted content held back until the security review |
| Proposed classification | Scope clarification without cost impact |
| Decision of the steering committee (2025-03-20) | Pending; decision by Koen Verstraete |

Thomas Maes
