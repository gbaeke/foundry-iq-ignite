# Steering Committee Minutes: Phase 1 Review

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Clinical Knowledge Assistant |
| **Document type** | Steering committee minutes |
| **Date** | 2026-11-04, 15:30 to 17:00 |
| **Location** | Mediva, campus admin building, meeting room "Leie" |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |

## Present

Dr. Hilde Van Damme (chair, CMIO), Jeroen Lambrecht (IT Manager), Sarah Mertens (DPO, item 4), the guideline coordinator of emergency (item 3), Pieter De Smet, Amira El Idrissi, Ruben Wouters. Lotte Willems excused; commercial follow-up through Pieter.

## 1. Purpose

The Phase 1 review was originally planned for 2026-10-14 and moved by about three weeks, so that the cardiology clean-up and re-index could be included. The project status remains **ongoing (pilot)**. This meeting reviews Phase 1 against the SOW and discusses the conditions for a possible Phase 2. No Phase 2 decision is taken today.

## 2. Phase 1 against the SOW

| SOW item | Result |
|---|---|
| Knowledge base on first sources | Foundry IQ knowledge base with agentic retrieval, live since February |
| Assistant | Built in Microsoft Foundry, Azure OpenAI models in the EU region |
| Front end in intranet with feedback | Live; thumbs up/down, reason list, "outdated source" flag |
| Evaluation set and repeatable run | 200 questions plus 40 paraphrase pairs; run after every change |
| Pilot in a limited number of departments | Cardiology since 2026-05-04, emergency since 2026-06-01 |
| Budget | Within the EUR 140,000 time-and-materials cap; about 88% used |

## 3. Quality and content

Amira presented the evaluation trend: from 72% correct and complete in the March baseline (120 questions) to 85% on the full 200-question set after the cardiology re-index, with the cardiology subset at 91%. Emergency is still at 82% and is expected to improve after its clean-up. The paraphrase test shows no more version conflicts in cardiology.

The emergency coordinator reported the clean-up at about 80%. Completion is expected around 2026-11-13, followed by a re-index and a full evaluation run.

Hilde summarised the main lesson of Phase 1: the quality of the answers depends more on the state of the guideline library than on the model. The monthly content review stays, with weekly flag exports to the coordinators.

## 4. Privacy and security

Sarah confirmed that the monthly counters of blocked questions and warnings are stable and low (October: 1 blocked, 12 warnings). She sees no need to revise the addendum for the current scope. For any extension to the patient record she would require a new assessment; that is not proposed.

Ruben summarised the load test of October: the current set-up handles about five times the observed night peak without noticeable degradation. A hospital-wide rollout would need more model capacity.

## 5. Usage and cost

- About 60 active users per four weeks, majority from emergency, many questions at night.
- Consumption cost per question remains a few euro cents; Jeroen confirmed the yearly forecast fits the IT budget for the current pilot scope.

## 6. Discussion: conditions for Phase 2

Hilde and Jeroen listed what a Phase 2 would need before any department is added:

1. A named content owner per department with time allocated, and the current/superseded/archive status set **before** indexing.
2. The status field mandatory on publication in the library (Mediva IT feasibility answer: possible, planned for January).
3. A capacity and cost estimate per added department, based on the load test.
4. A plan for the legacy share to become read-only for clinical content.

Intensive care was mentioned again as a candidate, as in the January inventory. No department choice was made.

## 7. Decisions

- D1: Phase 1 review accepted by the sponsor as a basis for discussion.
- D2: The pilot continues in cardiology and emergency within the remaining Phase 1 budget.
- D3: Kestrel prepares a Phase 2 proposal including the four conditions above, for discussion at the steering committee of 2026-12-02.

## 8. Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Finish emergency clean-up | Emergency coordinator | 2026-11-13 |
| 2 | Re-index emergency, rerun full evaluation set | AE | 2026-11-20 |
| 3 | Phase 2 proposal draft | PDS, with Lotte Willems | 2026-11-25 |
| 4 | Burn-down forecast to end of Phase 1 budget | PDS | 2026-11-11 |
| 5 | Answer streaming improvement released after review | RW, AE | 2026-11-13 |
| 6 | Legacy share plan | JL | 2026-12-02 |

Next steering committee: 2026-12-02.
