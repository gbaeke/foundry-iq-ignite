# Steering Committee Minutes: Meeting 3

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Clinical Knowledge Assistant |
| **Document type** | Steering committee minutes |
| **Date** | 2026-03-25, 16:00 to 17:00 |
| **Location** | Mediva, campus admin building, meeting room "Leie" |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |

## Present

Dr. Hilde Van Damme (chair), Jeroen Lambrecht, Sarah Mertens (item 3), Pieter De Smet, Amira El Idrissi. Ruben Wouters joined for the demo. Lotte Willems excused.

## 1. Status and budget

Pieter: overall green. Both pilot departments are in the knowledge base, the front end runs in the intranet test environment, and the evaluation set v1 is ready. Burn-down: about 34% of the EUR 140,000 first-phase cap used after ten weeks, slightly below plan because the source export took less effort than expected.

Azure consumption in Mediva's subscription so far is modest. Retrieval and answer generation together cost a few euro cents per question. Jeroen asked for a monthly forecast once real users start.

## 2. Evaluation set v1

Amira presented the 120-question set and the baseline run: 72% correct and complete, 17% partially correct, 11% incorrect or wrong source. After this week's tuning (fewer sub-queries for simple questions, action-list-first answers, tables fixed) the rerun of 2026-03-23 gave 77% correct and complete.

Hilde asked what is "good enough" for the pilot. Agreed: no fixed threshold for starting the pilot, as clinicians always see the source; but **no incorrect answers on single-fact dosing questions** in the set, and every incorrect answer is analysed and reported.

**Decision: evaluation set v1 agreed.**

## 3. Data protection

Sarah confirmed that the addendum to the existing assessment is finished. Conditions: monthly report of blocked questions and warnings, 90-day retention, and the notice in the question box, which now also states that the assistant gives no patient-specific advice (wording confirmed by Hilde).

## 4. Pilot planning

| Step | Date |
|---|---|
| Security review and test by Mediva IT | April |
| Pilot start cardiology | Monday 2026-05-04 |
| Pilot start emergency | Monday 2026-06-01 |
| Phase 1 review | 2026-10-14 |

Emergency starts four weeks later so that the night teams can be briefed after the cardiology start and so that the emergency coordinator can finish confirming the legacy documents. Pilot users: physicians and nurses of both departments, through a dedicated access group. Hilde asked to include the emergency night coordinators explicitly.

## 5. Content ownership

The coordinators have confirmed current versions for roughly half of the documents with derived metadata. Hilde will ask the heads of department to free up a few hours per week for the coordinators until the pilot start. Pieter repeated that the assistant cannot decide which version is valid; that stays with the content owners.

## 6. Demo

Ruben showed the question box safeguards (blocked national register number, warning on name patterns) and the table rendering of a cardiology dosing table. Jeroen asked for the front end to show a clear maintenance message when the knowledge base refresh is running. Ruben will add it.

## Decisions

- D1: Evaluation set v1 (120 questions) agreed.
- D2: Pilot cardiology from 2026-05-04, emergency from 2026-06-01.
- D3: Phase 1 review planned on 2026-10-14.

## Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Security review and test plan with Mediva IT | RW, JL | 2026-04-17 |
| 2 | Free time for coordinators to confirm versions | HVD | 2026-04-22 |
| 3 | Access group for pilot users | JL | 2026-04-24 |
| 4 | Consumption forecast template | PDS | 2026-04-22 |
| 5 | Maintenance message during refresh | RW | 2026-04-10 |

Next steering committee: 2026-04-22.
