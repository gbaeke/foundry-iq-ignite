# Architecture and Security Review Notes (Sprint 1)

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Customs Document Extraction |
| **Date** | 2025-10-10 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Meeting notes (architecture review) |
| **Participants** | Jan Wouters (product owner), two members of Scaldis IT security, a Scaldis IT infrastructure engineer, Pieter De Smet, Amira El Idrissi |

## 1. Why in sprint 1

The statement of work puts the architecture and security review in sprint 1, before any document is processed. After the Ops Copilot, nobody at Scaldis or Kestrel wanted to repeat a late review.

## 2. Target architecture (as presented)

1. **Intake.** Two channels: the customs desk shared mailbox (attachments from forwarders, hauliers and shipping lines) and the scanning station at the customs desk (paper documents brought by drivers).
2. **Orchestration.** An Azure Logic Apps workflow picks up each new document, stores the original, calls classification and extraction, and puts the result in the validation queue.
3. **Classification and extraction.** Azure AI Document Intelligence: a custom classifier to recognise the document type, then a custom extraction model per type, combined in a composed model.
4. **Validation screen.** Customs agents see the document and the extracted fields side by side, confirm or correct, and release the record.
5. **Output.** Validated fields are exported as a structured file per container for the customs agents to use in the declaration system. No automatic submission in phase 1.

## 3. Security topics discussed

| Topic | Outcome |
|---|---|
| Data residency | All processing in the Scaldis tenant, West Europe. Agreed. |
| Identities | Logic Apps and Document Intelligence use managed identities; no keys in workflow definitions. Agreed. |
| Network | Document Intelligence and storage reachable only via private endpoints from the Scaldis network. Logic Apps on a plan that supports network integration. |
| Mailbox access | The workflow may only read the customs shared mailbox, not other mailboxes. Scaldis IT will scope the permission accordingly. |
| Scanning station | Sits on the office network of the customs building, not on the terminal operations network. Scans go to a network folder picked up by the workflow. |
| Access to the validation screen | Customs desk staff only, via existing Scaldis groups. Senior agents get an extra role. |
| Malicious attachments | Mail attachments pass the existing Scaldis mail filtering before reaching the shared mailbox. Only PDF, TIFF, JPEG and PNG are processed; anything else is moved to a manual folder. |

## 4. Points raised by Scaldis IT security

- **Personal data.** CMR notes contain driver names, signatures and licence plates. Security asked for a short privacy note with the data protection contact before production. Action for Pieter.
- **Retention.** How long are originals and extracted data kept? Jan: the customs desk must keep documents per legal retention requirements anyway; the question is whether our store becomes an additional copy. To be settled in the privacy note.
- **Model training data.** Labelled samples contain real documents. They must stay in the Scaldis tenant and be removed from Kestrel laptops at the end of the project. Agreed: no local copies at all; labelling happens in the tenant.

## 5. Decisions

1. Architecture accepted as baseline for phase 1, subject to the privacy note.
2. Security review is repeated at two moments: before the parallel run and before production use.
3. Any new intake channel (for example a portal for hauliers) is a change that needs a new review.

## 6. Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Privacy note with data protection contact | PDS | 2025-12-12 |
| 2 | Private endpoints and managed identities set up | Scaldis IT infrastructure | 2025-10-24 |
| 3 | Scoped permission on customs shared mailbox | Scaldis IT | 2025-10-24 |
| 4 | Network folder for scanning station | Scaldis IT infrastructure | 2025-10-17 |
| 5 | Group for validation screen users and senior agents | JW | 2025-10-17 |

Pieter De Smet
