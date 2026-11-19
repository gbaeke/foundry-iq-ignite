# Kickoff Notes: Clinical Knowledge Assistant

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Clinical Knowledge Assistant |
| **Document type** | Meeting notes (kickoff) |
| **Date** | 2026-01-12, 13:30 to 15:30 |
| **Location** | Mediva, campus admin building, meeting room "Leie" |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |

## Attendees

- Dr. Hilde Van Damme, Chief Medical Information Officer, Mediva (HVD), sponsor
- Jeroen Lambrecht, IT Manager, Mediva (JL)
- Sarah Mertens, Data Protection Officer, Mediva (SM)
- Pieter De Smet, Lead AI Architect, Kestrel (PDS)
- Amira El Idrissi, Lead AI Engineer, Kestrel (AE)
- Ruben Wouters, Developer, Kestrel (RW)

## 1. Purpose and principles

Hilde recalled where the project comes from: during the discharge letter evaluation in 2024 physicians kept asking "can I also ask it what our protocol says?". Today clinical staff search the intranet and old shared drives for guidelines and often find several versions. The assistant must answer only from Mediva-approved sources and always show which document and which version it used.

Principles agreed:

1. Answers only from Mediva's own guideline and protocol library; no general medical knowledge without a source.
2. Every answer cites document, version and publication date, with a link.
3. If the sources do not answer the question, the assistant says so.
4. No patient-specific advice; no integration with the patient record in Phase 1.

## 2. Scope and budget

As in the SOW of 2025-12-10: time and materials, first phase capped at EUR 140,000 excl. VAT, Azure and Foundry consumption billed to Mediva's subscription. Pieter will report burn-down at every steering committee.

## 3. Environment

Jeroen's team delivered the Azure subscription in an EU region on Friday 9 January, the first working day after the Christmas change freeze. The Microsoft Foundry project is created; Azure OpenAI model deployments follow this week. Access for the three Kestrel team members is granted through named accounts, as in the previous project.

## 4. Technical approach

Pieter presented the target picture:

- A **Foundry IQ knowledge base** with agentic retrieval over the guideline sources: complex questions are split into sub-queries, results are merged and answered with citations.
- The assistant built in **Microsoft Foundry**, with **Azure OpenAI** models in the EU region.
- A web front end in the intranet, built by Ruben, with a feedback button per answer.
- A repeatable evaluation run on a question set built with clinicians, owned by Amira.

## 5. Privacy

Sarah confirmed that the EU-only processing and governance of the discharge letter project remain the baseline. Phase 1 indexes guidelines, not patient data. Her concern is what users type: a physician may paste patient details into a question. She will review the design before the pilot and decide whether the existing assessment needs an update. Amira proposed to show her the front end safeguards in March.

## 6. Departments

Hilde wants to start with two departments that have many protocols and many questions outside office hours. Candidates: cardiology, emergency, intensive care, oncology. Decision after the source inventory workshop.

## 7. Governance

- Steering committee every four weeks on Wednesday, first on 2026-01-28.
- Weekly demo to a clinical sounding board nominated by Hilde, Friday at 12:30.
- Status reports by Pieter, monthly, plus short notes after each steering committee.

## Decisions

- D1: Answers only from approved sources, with version and date.
- D2: No patient record integration in Phase 1.
- D3: Pilot departments chosen after the source inventory.

## Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Source inventory workshop with guideline coordinators | AE | 2026-01-23 |
| 2 | Access to the intranet library and the legacy document share | JL | 2026-01-16 |
| 3 | Nominate the clinical sounding board | HVD | 2026-01-21 |
| 4 | ADR on knowledge base design | PDS | 2026-02-06 |
| 5 | Front end skeleton with sign-in and feedback button | RW | 2026-02-13 |
