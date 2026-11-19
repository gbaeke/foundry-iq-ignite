# Proposal: Claims Triage Automation

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Proposal |
| **Date** | 2024-03-18 |
| **Author** | Lotte Willems, Managing Partner, Kestrel Consulting |
| **Reference** | KC-PROP-2024-009 |

## 1. Context

Fortalis Verzekeringen receives several thousand property and casualty claims ("schadeaangiftes" / "déclarations de sinistre") every month, by e-mail, through brokers and via the customer portal. Each claim arrives with a mix of documents: claim forms, photos, repair quotes, police reports. Today the claims handlers open every file manually to decide the claim type, urgency and which team should handle it. During peak periods, the backlog in the intake team grows to several days.

Marc Dubois, Chief Digital Officer, asked Kestrel Consulting to propose a solution that triages incoming claims automatically, so that handlers can focus on assessment rather than sorting. Laura Vermeulen, Claims Operations Manager, will act as product owner.

## 2. Proposed approach

The solution reads the incoming documents, extracts key fields, classifies the claim and routes it to the right queue in the claims management system, with a confidence score. Claims below the confidence threshold go to a human triage queue.

**Components**

- **Azure AI Document Intelligence** to extract fields from claim forms, quotes and reports (policy number, date and place of loss, claimed amount, damage description).
- **Azure Machine Learning** for the triage model: claim type, complexity and urgency classification, trained on historical claims labelled by Laura's team.
- **Azure Logic Apps** to orchestrate the flow: pick up incoming claims, call extraction and classification, write the result to the claims system and notify handlers.

**Platform**

The solution **builds on the Fortalis Landing Zone** that Kestrel delivered in February 2024. It will be deployed in a dedicated spoke, using the existing infrastructure modules, identity roles and policy guardrails. This saves set-up time and means the security and network design is already approved.

## 3. Scope

Phase scope covers the claim types motor, fire and theft for private customers. Commercial lines and liability claims are out of scope for this proposal.

## 4. Team

| Role | Name |
|---|---|
| Project manager | Thomas Maes, Project Manager |
| Platform engineer | Jonas Peeters, Cloud Platform Engineer |
| ML engineer | Amira El Idrissi, ML Engineer |
| Engagement lead | Lotte Willems, Managing Partner |

Fortalis side: Marc Dubois (sponsor), Laura Vermeulen (product owner), two senior claims handlers for labelling and acceptance testing (about one day per week each).

## 5. Planning

| Phase | Period |
|---|---|
| Start | 2024-04-08 |
| Discovery and data labelling | April to May 2024 |
| Extraction and model build | June to September 2024 |
| Integration and user acceptance | October to December 2024 |
| Production and hypercare | January to February 2025 |

## 6. Commercials

| Item | Amount |
|---|---|
| Fixed price | EUR 240,000 excl. VAT |
| Invoicing | 20% at start, then per accepted milestone |
| Azure consumption | billed directly to Fortalis |

Changes to the agreed claim types or volumes are handled through a formal change request approved by the sponsor.

## 7. Assumptions

- Fortalis provides at least 18 months of historical claims with their final classification.
- API access to the claims management system is available by June 2024.
- Labelling support from the claims team is available as planned.

## 8. Next steps

Confirmation by Marc Dubois by 2024-03-29 keeps the start date of 2024-04-08.

*Lotte Willems, Kestrel Consulting, Ghent*
