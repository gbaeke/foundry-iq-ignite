# Go-Live Checklist: Pilot Start Cardiology

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Clinical Knowledge Assistant |
| **Document type** | Go-live checklist |
| **Date** | 2026-05-04 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Pilot start** | Monday 2026-05-04, 08:00, cardiology |
| **Go/no-go** | Thursday 2026-04-30, Dr. Hilde Van Damme and Jeroen Lambrecht |

## 1. Content

| # | Check | Owner | Status |
|---|---|---|---|
| 1.1 | Cardiology documents in the knowledge base, daily refresh at 05:00 | AE | Done |
| 1.2 | Versions confirmed by coordinator for documents with derived metadata | Cardiology coordinator | 84% confirmed, rest labelled "version derived" |
| 1.3 | Training slide decks excluded | AE | Done |
| 1.4 | Dosing tables rendered as tables | RW, AE | Done |
| 1.5 | Emergency sources indexed but hidden for cardiology users until 2026-06-01, except cross-department questions | AE | Done |

## 2. Quality

| # | Check | Owner | Status |
|---|---|---|---|
| 2.1 | Evaluation set run on production configuration | AE | Done, 2026-04-29 |
| 2.2 | Result: correct and complete | AE | 80% (cardiology subset 83%) |
| 2.3 | No incorrect answers on single-fact dosing questions | AE | Done, 0 of 22 |
| 2.4 | Unanswerable questions handled correctly | AE | 11 of 12 |
| 2.5 | Every incorrect answer analysed and reported to the coordinator | AE | Done |

## 3. Security and privacy

| # | Check | Owner | Status |
|---|---|---|---|
| 3.1 | All findings of the security review fixed and retested | RW | Done |
| 3.2 | Public access disabled, EU region confirmed | PDS | Done |
| 3.3 | Question box safeguards and notice active | RW | Done |
| 3.4 | 90-day log deletion in production | JL | Done |
| 3.5 | Addendum to the assessment signed by the DPO | SM | Done |
| 3.6 | Monthly counter report of blocked questions and warnings to the DPO | AE | Template ready |

## 4. Operations

| # | Check | Owner | Status |
|---|---|---|---|
| 4.1 | Monitoring: questions per hour, answer time, errors, feedback | PDS | Done |
| 4.2 | Alert when the knowledge base refresh fails | PDS | Done, to Mediva IT service desk |
| 4.3 | Maintenance message during refresh | RW | Done |
| 4.4 | Consumption forecast template for Jeroen | PDS | Done |
| 4.5 | Service desk knows the escalation path to Kestrel | JL | Done |
| 4.6 | Fallback: intranet search as today; nothing depends on the assistant | All | By design |

## 5. Users

| # | Check | Owner | Status |
|---|---|---|---|
| 5.1 | Pilot access group: cardiology physicians and nurses | JL | Done |
| 5.2 | 15-minute briefing at the cardiology staff meeting | AE | Done, 2026-04-28 |
| 5.3 | One-page guide on the intranet: what it does, what it does not, how to give feedback | RW | Done |
| 5.4 | Message from Dr. Van Damme: always check the source for dosing and critical decisions | HVD | Sent 2026-04-30 |
| 5.5 | Sounding board members act as local champions | HVD | Confirmed, 3 in cardiology |

## 6. Known limitations

- Only cardiology and emergency sources; other departments not covered.
- Some documents carry a derived version; the answer shows the label.
- Answers can take up to 15 to 20 seconds for compound questions.
- No patient record integration and no patient-specific advice.

## 7. Hypercare

- Ruben on site on campus Centrum on 4 and 5 May, visiting the cardiology wards and the outpatient clinic.
- Daily review of thumbs-down feedback by Amira during the first two weeks.
- Weekly sounding board demo continues.

## 8. Decision

Go/no-go of 2026-04-30: **Go** for cardiology on 2026-05-04. Emergency follows on 2026-06-01, after a separate check of the emergency content and briefings for the night teams.
