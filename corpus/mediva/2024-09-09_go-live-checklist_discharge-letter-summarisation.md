# Go-Live Checklist: Pilot in Daily Practice

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Discharge Letter Summarisation |
| **Document type** | Go-live checklist |
| **Date** | 2024-09-09 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Pilot start** | Monday 2024-09-09, internal medicine and geriatrics |
| **Go/no-go** | Steering committee 2024-09-04 (go, conditional on items marked *) and final check 2024-09-06 |

## 1. Functional readiness

| # | Check | Owner | Status |
|---|---|---|---|
| 1.1 | Course-of-stay instruction: max three sentences per problem | AE | Done |
| 1.2 | Certainty wording: stronger instruction plus underlining in review screen* | AE | Done, tested on 60 stays |
| 1.3 | Dose unit check in code for medication section* | PDS | Done |
| 1.4 | Date shift fix verified on all section types* | AE | Done |
| 1.5 | Scanned documents flagged at top of draft | AE | Done |
| 1.6 | Signing only possible after opening every paragraph | Mediva IT | Done |

## 2. Privacy and security

| # | Check | Owner | Status |
|---|---|---|---|
| 2.1 | Production Azure OpenAI deployment in EU region, Mediva subscription | JL, PDS | Done |
| 2.2 | No data retained for training or abuse review, confirmation on file | PDS | Done |
| 2.3 | Pseudonymisation service v0.6 in production, inside Mediva's environment | JL | Done |
| 2.4 | Pseudonymisation key managed by Mediva IT; Kestrel no access | JL | Done |
| 2.5 | Logs pseudonymised only, automatic deletion after 90 days in production | JL | Done, confirmation sent to Sarah Mertens on 2024-08-28 |
| 2.6 | Kestrel production access limited to Pieter and Amira, read-only on logs | JL | Done |
| 2.7 | DPO sign-off on production data flow (unchanged from evaluation) | SM | Done, 2024-09-03 |

## 3. Operations

| # | Check | Owner | Status |
|---|---|---|---|
| 3.1 | Monitoring: number of drafts, draft time, errors, edit distance | PDS | Done |
| 3.2 | Alert if draft time exceeds 60 seconds for 10 minutes | PDS | Done |
| 3.3 | Monthly consumption report for Jeroen | PDS | Template ready, first report early October |
| 3.4 | Service desk instructions: what to do if drafts fail | JL | Done |
| 3.5 | Fallback: physician writes the letter as usual; nothing depends on the draft | All | By design |
| 3.6 | Run book draft | PDS | Draft v0.8, final at handover |

## 4. Users

| # | Check | Owner | Status |
|---|---|---|---|
| 4.1 | The 12 evaluation physicians continue in the pilot | HVD | Confirmed |
| 4.2 | Other physicians of both departments trained (30 minutes, four sessions) | AE | Done, 29 physicians |
| 4.3 | Quick reference card at the physicians' desks | AE | Done |
| 4.4 | Message from Dr. Van Damme: draft is a draft; review and signature remain the physician's responsibility | HVD | Sent 2024-09-05 |
| 4.5 | Feedback channel: rating form stays available, optional | AE | Done |

## 5. Known limitations

- Scanned documents without text layer are not used.
- Social history: relatives' occupations and place names are removed by pseudonymisation and must be completed by the physician.
- The function is available only in internal medicine and geriatrics; other departments are out of scope of this project.
- Drafts are not generated in advance; the physician starts the draft when writing the letter.

## 6. Hypercare

- Amira on site on Monday 9 and Tuesday 10 September, morning and afternoon visit per department.
- Daily check of monitoring and safety reports in the first two weeks.
- Weekly Thursday session with Mediva IT continues until handover.

## 7. Planning to closure

| Milestone | Date |
|---|---|
| Pilot start | 2024-09-09 |
| Pilot review in steering committee | 2024-10-02 |
| Handover to Mediva IT | 2024-10-11 |
| Closing and acceptance | 2024-10-25 |

## 8. Final check

Final check on 2024-09-06 by Pieter De Smet and Jeroen Lambrecht: all items marked * done. **Go.**
