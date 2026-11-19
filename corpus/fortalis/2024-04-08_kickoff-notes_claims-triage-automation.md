# Kickoff Notes: Claims Triage Automation

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Meeting notes (kickoff) |
| **Date** | 2024-04-08 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Location** | Fortalis head office, Brussels |

## Attendees

- Marc Dubois, Chief Digital Officer, Fortalis Verzekeringen (sponsor)
- Laura Vermeulen, Claims Operations Manager, Fortalis Verzekeringen (product owner)
- Two senior claims handlers from the intake team (labelling and acceptance testing)
- A delegate of the Fortalis cloud team
- Thomas Maes (project manager), Jonas Peeters (platform engineer), Amira El Idrissi (ML engineer), Kestrel Consulting

## 1. Opening by the sponsor

Marc recalled why Fortalis started this: the intake team spends most of its time opening files to decide what they are, not deciding what to do with them. In the peak weeks of last winter the intake backlog reached four working days. His goal for the project: "handlers should handle, not sort". He also made clear that the fixed price of EUR 240,000 is the budget, and that any change in claim types or volumes goes through a formal change request that he signs himself.

## 2. Scope recap

- Claim types in scope: **motor, fire and theft** for private customers.
- Out of scope: commercial lines, liability claims.
- The solution reads incoming documents with Azure AI Document Intelligence, classifies type, complexity and urgency with a model in Azure Machine Learning, and routes the claim with Azure Logic Apps to the right queue in the claims management system. Below a confidence threshold, claims go to a human triage queue.
- The platform is the Fortalis landing zone: a dedicated spoke, using the existing guardrails. The cloud team delegate confirmed that a spoke request was prepared in March and can be created this week.

## 3. Planning

| Phase | Period |
|---|---|
| Discovery and data labelling | April to May 2024 |
| Extraction and model build | June to September 2024 |
| Integration and user acceptance | October to December 2024 |
| Production and hypercare | January to February 2025 |

Two-week sprints, starting today. Sprint reviews on Friday afternoon every second week, with Laura and the senior handlers. A monthly status report to Marc, and a steering committee every two to three months.

## 4. Discussion points

- **Historical data.** Laura confirmed that 18 months of closed claims with their final classification can be extracted. The claims system team needs about two weeks. Amira asked for the documents as well as the structured fields, otherwise extraction cannot be trained.
- **What "urgent" means.** Laura and the handlers did not fully agree. One handler considers every fire claim urgent; Laura wants urgency based on the situation of the customer (home uninhabitable, vehicle needed for work, risk of further damage). To be settled in the process mapping workshop.
- **Languages.** About 60% of claims arrive in Dutch, 35% in French, the rest in English or German. The model must handle at least Dutch and French from the first release.
- **API to the claims system.** The proposal assumes API access by June. Laura will check with the claims system team whether the write interface for setting the queue already exists or has to be built.
- **Privacy.** Claim files contain personal data and in motor claims sometimes injury information. Jonas proposed a short privacy and security review with the Fortalis data protection officer before any real data lands in the spoke.

## 5. Decisions

- Laura is the single point of contact for scope and priorities.
- Claims that the model cannot classify with enough confidence always go to people. No silent defaults.
- Kestrel works only inside the Fortalis spoke; no claim data on Kestrel laptops or systems.

## 6. Action items

| Action | Owner | Due |
|---|---|---|
| Request 18-month historical extract with documents | LV | 2024-04-12 |
| Create project spoke and access groups | JP with cloud team | 2024-04-12 |
| Process mapping workshop, intake and triage | TM / LV | 2024-04-19 |
| Privacy and security review with DPO, plan date | JP | 2024-04-19 |
| Check status of claims system write interface | LV | 2024-04-26 |
| First data profiling of the extract | AE | 2024-05-03 |

*Thomas Maes, Kestrel Consulting*
