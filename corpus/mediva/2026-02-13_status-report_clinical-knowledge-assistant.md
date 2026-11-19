# Status Report: Clinical Knowledge Assistant

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Clinical Knowledge Assistant |
| **Document type** | Status report |
| **Date** | 2026-02-13 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Period** | 2026-01-12 to 2026-02-13 |
| **Project status** | Ongoing (build) |

## 1. Overall status

| Area | Status | Comment |
|---|---|---|
| Overall | Green | Foundation in place, first knowledge source indexed |
| Scope | Green | Pilot departments confirmed |
| Planning | Green | Knowledge base on first sources in February as planned |
| Budget | Green | About 17% of the EUR 140,000 cap used |
| Quality | Green | No evaluation yet; question collection started |

## 2. Progress

- **Pilot departments.** The steering committee of 2026-01-28 confirmed **cardiology** and **emergency**, as proposed after the source inventory workshop.
- **Architecture.** ADR-01 accepted: Foundry IQ knowledge base with agentic retrieval, assistant in Microsoft Foundry, Azure OpenAI model in the EU region.
- **Ingestion.** Mediva IT delivered the export of 550 cardiology and emergency documents. Amira El Idrissi indexed the cardiology documents as the first knowledge source on 2026-02-11. Emergency follows next week, together with the nursing procedures.
- **Metadata.** Version and date derived automatically where missing (about 18% of documents). Coordinators received the list of documents with derived values.
- **Front end.** Ruben Wouters delivered the front end skeleton in the intranet test environment: sign-in with the hospital account, a department selector, the answer view with citations and a thumbs up/down feedback button.
- **Sounding board.** Five clinicians (two cardiologists, an emergency physician, two nurses) attended the first two Friday demos.

## 3. First observations

The first internal tests on cardiology look promising. Compound questions are split as intended. Two points:

- Some answers cite a training slide deck that slipped into the export despite the decision to exclude them. Fixed with a document type filter.
- Dosing tables in spreadsheets are indexed as text and lose their structure. Amira is testing a conversion to a simple table format before ingestion.

## 4. Risks and issues

| # | Type | Description | Owner | Mitigation |
|---|---|---|---|---|
| R1 | Risk | Version metadata missing or ambiguous; wrong version may be cited | HVD | Coordinators confirm current versions; derived values marked |
| R2 | Risk | Users type patient details into questions | AE, SM | Front end safeguards; DPO review in March |
| R3 | Risk | Coordinators have limited time for content work | HVD | Agree time allocation at next steering committee |
| R4 | Risk | Latency of agentic retrieval at night when users are in a hurry | PDS | Measure against 6 s / 15 s target |
| R5 | Risk | Consumption cost unclear for Mediva's budget | PDS | Report cost per question from first demos |

## 5. Next steps

| Action | Owner | Due |
|---|---|---|
| Index emergency documents and nursing procedures | AE | 2026-02-20 |
| Sprint review with sounding board on both departments | RW | 2026-02-27 |
| First 60 example questions from the coordinators | Coordinators | 2026-02-20 |
| Design review with Sarah Mertens on front end safeguards | AE | 2026-03-06 |
| Steering committee | PDS | 2026-02-25 |

*Pieter De Smet, Kestrel Consulting*
