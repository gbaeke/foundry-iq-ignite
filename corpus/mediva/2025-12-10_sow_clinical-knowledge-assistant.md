# Statement of Work: Clinical Knowledge Assistant (Phase 1)

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Clinical Knowledge Assistant |
| **Document type** | Statement of work |
| **Date** | 2025-12-10 |
| **Author** | Lotte Willems, Managing Partner, Kestrel Consulting |
| **Reference** | KC-SOW-2025-017 |

## 1. Background

This Statement of Work is a follow-up of the **Discharge Letter Summarisation** project, which Kestrel Consulting delivered for Mediva Care Group in 2024. In the evaluation of that project, physicians repeatedly asked for a way to query Mediva's own clinical guidelines, protocols and procedures. The closing report recommended a clinical knowledge assistant; after two scoping workshops in autumn 2025, Dr. Hilde Van Damme, Chief Medical Information Officer, asked us to formalise a first phase.

The assistant answers clinical staff questions ("What is our protocol for anticoagulation bridging before surgery?") using only Mediva-approved sources, and always cites the document and version it used.

## 2. Scope of Phase 1

In scope:

- Ingestion of the clinical guideline and protocol library (currently on the intranet document library and a legacy document management share) for an initial set of departments to be chosen with the sponsor.
- A **Foundry IQ knowledge base with agentic retrieval** over these sources, so that complex questions are broken down into sub-queries and answered with citations.
- An assistant built in **Microsoft Foundry**, using **Azure OpenAI** models deployed in an EU region.
- A web front end integrated in the intranet, with feedback buttons per answer.
- An evaluation set of representative clinical questions, built with clinicians, and a repeatable evaluation run.
- Pilot in a limited number of departments.

Out of scope for Phase 1: integration with the patient record, patient-specific advice, mobile apps, and any use by patients.

## 3. Data protection

The privacy approach and EU-only processing agreed with Sarah Mertens, Data Protection Officer, in the previous project remain the baseline. Phase 1 processes guideline documents, not patient data. Sarah will review the design before the pilot starts and confirm whether an update of the existing assessment is required.

## 4. Team and governance

| Role | Name |
|---|---|
| Sponsor | Dr. Hilde Van Damme, CMIO, Mediva |
| IT counterpart | Jeroen Lambrecht, IT Manager, Mediva |
| DPO | Sarah Mertens, Mediva |
| Lead architect | Pieter De Smet, Kestrel |
| Lead AI engineer | Amira El Idrissi, Kestrel |
| Developer | Ruben Wouters, Kestrel |
| Engagement lead | Lotte Willems, Kestrel |

Steering committee every four weeks; weekly demo to a clinical sounding board nominated by Dr. Van Damme.

## 5. Planning

| Milestone | Target |
|---|---|
| Start | 2026-01-12 |
| Knowledge base on first sources | February 2026 |
| Evaluation set v1 agreed | March 2026 |
| Pilot start | Q2 2026 |
| Phase 1 review | end of Phase 1 budget, decision on Phase 2 |

## 6. Commercials

- **Time and materials**, first phase capped at **EUR 140,000** excl. VAT.
- Monthly invoicing based on timesheets; burn-down reported in every steering committee.
- Azure and Foundry consumption billed directly to Mediva's subscription.
- Work beyond the cap requires written approval from the sponsor.

## 7. Assumptions

- Mediva nominates content owners who can confirm which guideline version is current.
- Mediva IT provides access to the source libraries and an Azure subscription in an EU region by the start date.
- Clinicians are available for evaluation sessions (about one hour per week per department).

## 8. Acceptance

Signed for Mediva Care Group: Dr. Hilde Van Damme
Signed for Kestrel Consulting: Lotte Willems
