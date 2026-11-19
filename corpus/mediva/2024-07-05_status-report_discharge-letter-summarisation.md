# Status Report: Discharge Letter Summarisation

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Discharge Letter Summarisation |
| **Document type** | Status report (biweekly) |
| **Date** | 2024-07-05 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Period** | 2024-06-24 to 2024-07-05 |
| **Distribution** | Dr. Hilde Van Damme, Jeroen Lambrecht, Sarah Mertens |

## 1. Overall status

| Area | Status | Comment |
|---|---|---|
| Overall | Amber | Evaluation running; holiday availability lower than planned |
| Scope | Green | No change |
| Planning | Amber | Intervention period likely to need the two-week extension |
| Budget | Green | Second invoice (30%) sent after prototype acceptance on 2024-06-12 |
| Privacy | Green | Repeat pseudonymisation test accepted by DPO |

## 2. Progress

- **Prototype accepted** by Dr. Van Damme at the steering committee of 2024-06-12.
- **Training** of the 12 evaluation physicians held on 2024-06-20; two physicians who could not attend received a short individual session.
- **Baseline period** (2024-06-24 to 2024-07-05) completed. 11 of 12 physicians reached the minimum of five letters; the twelfth will add baseline letters in the first week back from leave.
- **Tooling.** The edit-time timer and the rating form work. Amira found and fixed one issue: the timer kept running when the physician switched to another patient file. Affected measurements (14 letters) are excluded.
- **Production environment.** Jeroen's team started preparing the production subscription for the pilot in September, including the 90-day log deletion rule.

## 3. Holiday impact

The intervention period runs from 2024-07-08. Based on the leave planning shared by the medical secretariats:

| Week | Physicians available |
|---|---|
| 8 to 12 July | 11 |
| 15 to 19 July | 9 |
| 22 to 26 July | 6 |
| 29 July to 2 August | 7 |
| 5 to 9 August | 8 |
| 12 to 16 August | 10 |

With six or seven physicians in the second half of July, several will not reach five letters in the planned four weeks. The protocol allows an extension of up to two weeks within the evaluation phase. **I propose to decide now to run the intervention period until 2024-08-16.** Analysis then has two weeks instead of four, which Amira considers sufficient. The evaluation phase still ends on 2024-08-30 and the overall end date of 2024-10-25 is not affected.

## 4. First observations (informal)

It is too early for numbers. From the rating forms of the first week:

- Physicians mostly rate drafts as usable with minor edits.
- The most frequent corrections so far: course of stay too long for internal medicine, and wording that is more certain than the notes.
- No potentially harmful errors reported.

## 5. Risks and issues

| # | Type | Description | Owner | Mitigation |
|---|---|---|---|---|
| R1 | Issue | Fewer physicians available in July | TM | Extend intervention period to 2024-08-16 (decision requested) |
| R2 | Risk | Short analysis window | AE | Analysis scripts prepared during the evaluation |
| R3 | Risk | Over-confident wording in drafts | AE, PDS | Count in corrections; prompt change after evaluation |
| R4 | Risk | Kestrel holiday coverage | TM | Pieter and Amira do not overlap on leave; Amira reachable for safety reports |
| R5 | Risk | Production environment not ready in time for the September pilot | JL | Weekly check in the Thursday session |

## 6. Decision requested

Dr. Van Damme: approve the extension of the intervention period to 2024-08-16. A reply by mail is sufficient.

## 7. Next steps

| Action | Owner | Due |
|---|---|---|
| Intervention period | Evaluation physicians | until 2024-08-16 |
| Weekly safety review of reported errors | AE | weekly |
| Production environment ready | JL | 2024-08-23 |
| Evaluation report | AE | 2024-08-30 |
| Steering committee: evaluation results and pilot go/no-go | TM | 2024-09-04 |

The status report of 2024-07-19 will be short; the next full report is planned for 2024-08-02.

*Thomas Maes, Kestrel Consulting*
