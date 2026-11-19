# Statement of Work: Customs Document Extraction (Phase 1)

| | |
|---|---|
| **Customer** | Scaldis Logistics, Antwerp |
| **Project** | Customs Document Extraction |
| **Date** | 2025-09-30 |
| **Author** | Lotte Willems, Managing Partner, Kestrel Consulting |
| **Document type** | Statement of work |
| **Reference** | KC-SOW-2025-031 |

## 1. Background

The customs desk of Scaldis Logistics processes a high volume of paper and scanned documents for import and export containers: CMR consignment notes, commercial invoices, packing lists, certificates of origin, T1 transit documents and others. Today the customs team keys the relevant fields into the customs declaration system manually. At peak moments this creates a backlog that delays container release.

Following the go-live of the Ops Copilot last week, Koen Verstraete, CIO, asked Kestrel to start a first phase that automates the extraction of key fields from these documents.

## 2. Roles

| Role | Name | Organisation |
|---|---|---|
| Sponsor | Koen Verstraete, CIO | Scaldis Logistics |
| Product owner | Jan Wouters, Customs Coordinator | Scaldis Logistics |
| Architect | Pieter De Smet, Lead AI Architect | Kestrel Consulting |
| ML engineer | Amira El Idrissi | Kestrel Consulting |
| Engagement lead | Lotte Willems | Kestrel Consulting |

Jan Wouters decides on priorities among document types, validates extraction results with his team and accepts deliverables. Scaldis IT security will be involved in the architecture review in sprint 1.

## 3. Scope of phase 1

**In scope**
- Analysis of the document landscape at the customs desk and prioritisation of document types with Jan
- Custom extraction models in **Azure AI Document Intelligence** for the priority document types (target: at least 8 types in phase 1)
- An intake workflow in **Azure Logic Apps**: documents arrive via a shared mailbox and a scanning station, are classified, extracted and placed in a validation queue
- A simple validation screen where customs staff confirm or correct extracted fields
- Field-level accuracy measurement per document type on a labelled test set
- Architecture and security review in sprint 1 with Scaldis IT security

**Out of scope for phase 1**
- Automatic submission to the customs declaration system
- Integration with the terminal operating system
- Documents in languages other than Dutch, French, English and German

## 4. Approach and planning

- **Start: 2025-10-06**
- Two-week sprints; sprint review with Jan and two customs agents
- Sprint 1: architecture and security review, document inventory, labelling guidelines
- Sprints 2 to 6: model training per document type, Logic Apps workflow, validation screen
- From sprint 4: parallel run on live documents at the customs desk
- Phase 1 review and decision on phase 2 scope at the end of the budget

## 5. Commercials

- **Time and materials, first phase budget EUR 95,000** excl. VAT
- Monthly invoicing based on timesheets, with a burn report against budget
- Kestrel signals at 75% consumption with a forecast to complete
- Azure consumption is billed directly to Scaldis

## 6. Assumptions

- Scaldis provides at least 50 historical samples per document type, anonymised where needed
- Customs staff are available for labelling support (about 4 hours per week)
- Documents can be processed in the Scaldis Azure tenant in West Europe

## 7. Acceptance

Each sprint deliverable is accepted by the product owner at the sprint review. Phase 1 is accepted when the agreed document types meet the accuracy thresholds set together with Jan Wouters in sprint 2.

---

For Kestrel Consulting: Lotte Willems
For Scaldis Logistics: Koen Verstraete
