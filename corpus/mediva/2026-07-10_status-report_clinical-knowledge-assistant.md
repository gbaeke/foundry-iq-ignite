# Status Report: Clinical Knowledge Assistant

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Clinical Knowledge Assistant |
| **Document type** | Status report (monthly) |
| **Date** | 2026-07-10 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Period** | 2026-06-12 to 2026-07-10 |
| **Project status** | Ongoing (pilot) |

## 1. Overall status

| Area | Status | Comment |
|---|---|---|
| Overall | Green | Pilot running in both departments |
| Scope | Green | Unchanged |
| Planning | Green | Phase 1 review still planned on 2026-10-14 |
| Budget | Green | About 61% of the EUR 140,000 cap used |
| Quality | Green | Evaluation results stable after adding user questions |

## 2. Progress

- **Pilot.** Cardiology since 2026-05-04, emergency since 2026-06-01. Around 50 active users in the last four weeks, with emergency now generating the majority of questions, many of them at night.
- **Evaluation set.** Amira El Idrissi added 50 reviewed user questions; the set now has **170 questions**. Latest run: 79% correct and complete, 13% partially correct, 8% incorrect or wrong source. The new user questions are harder than the coordinators' questions, which explains why the score did not rise despite the tuning.
- **Abbreviations.** The emergency abbreviation list (about 140 terms) is in the retrieval instructions. Questions with abbreviations now retrieve the right protocol in most cases.
- **Front end.** Ruben Wouters made the feedback buttons more visible and added a short reason list on thumbs down ("too long", "wrong document", "not understood", "slow"). Share of rated answers rose from about a quarter to 38%.
- **Privacy.** Monthly counter sent to Sarah Mertens: 2 blocked questions and 17 warnings in June.

## 3. Cost and consumption

Consumption in Mediva's subscription grew with the emergency start. Per question, cost is still a few euro cents; the monthly total is driven by the number of questions and by compound questions, which use more retrieval steps.

| Item | June |
|---|---|
| Questions | about 1,900 |
| Share of compound questions | 22% |
| Retrieval share of consumption | about 40% |
| Answer generation share | about 60% |

Measures taken: simple questions now use fewer sub-queries; answer length is limited for simple questions; the test environment is scaled down outside office hours. Jeroen has the forecast template and confirmed the figures fit the IT budget for 2026.

## 4. Summer period

- Pilot continues during July and August. Usage in cardiology is expected to drop during the holidays; emergency will not.
- Kestrel coverage: Pieter, Amira and Ruben do not overlap on leave. Ruben is away from 2026-07-20 to 2026-08-07; front end changes are frozen in that period, only fixes.
- Several guideline coordinators are on leave in late July and early August; confirmation of document versions slows down.
- Weekly sounding board demo paused from 2026-07-17 to 2026-08-14.

## 5. Risks and issues

| # | Type | Description | Owner | Mitigation |
|---|---|---|---|---|
| R1 | Risk | Older document versions cited where a newer one exists | HVD | Coordinators check flagged cases; watch "wrong document" feedback |
| R2 | Risk | Night usage growth in emergency affects answer time | RW | Load test before extending pilot |
| R3 | Risk | Users do not open sources | AE | Version and date visible; source link for every dosing statement |
| R4 | Risk | Content confirmation slows down in summer | HVD | Restart after 2026-08-15 |

## 6. Next steps

| Action | Owner | Due |
|---|---|---|
| Rerun evaluation set after abbreviation update | AE | 2026-07-17 |
| Steering committee | PDS | 2026-07-15 |
| Review of "wrong document" feedback with coordinators | AE | 2026-08-21 |
| Grow evaluation set towards 200 questions | AE | 2026-09-11 |
| Draft structure of Phase 1 review | PDS | 2026-09-30 |

*Pieter De Smet, Kestrel Consulting*
