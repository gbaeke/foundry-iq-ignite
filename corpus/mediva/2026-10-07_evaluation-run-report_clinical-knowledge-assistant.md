# Evaluation Run Report: Cardiology Re-index with "Current Only" Filter

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Clinical Knowledge Assistant |
| **Document type** | Evaluation run report |
| **Date** | 2026-10-07 |
| **Author** | Amira El Idrissi, Lead AI Engineer, Kestrel Consulting |
| **Distribution** | Dr. Hilde Van Damme, Jeroen Lambrecht; Pieter De Smet, Ruben Wouters |

## 1. Context

In August the assistant gave conflicting answers on cardiology questions because several versions of the same guideline were published in the source library. As agreed with Dr. Hilde Van Damme, the CMIO office and the department guideline coordinators marked each cardiology and emergency document as *current*, *superseded* or *archive*, and only *current* documents are indexed. The cardiology clean-up was completed on 2026-10-02. This report covers the re-index of cardiology and the rerun of the full 200-question evaluation set.

## 2. What changed in the knowledge base

| | Before | After |
|---|---|---|
| Cardiology documents indexed | 231 | 188 |
| Of which superseded (moved to non-indexed library) | n/a | 36 |
| Of which archived | n/a | 7 |
| Titles with more than one indexed version | 23 | 0 |
| Documents with "version derived" label | 29 | 4 |

The superseded documents moved to a separate library that is not indexed. They remain available for the coordinators and for accreditation.

Technically, the knowledge source for cardiology now filters on the new status field. Documents without a status are not indexed; the coordinator receives a weekly list of new documents without status.

Emergency is still being cleaned up (started 2026-09-28) and was not re-indexed. Emergency questions in the set therefore still run against the old content.

## 3. Results, full set (200 questions)

| Label | 2026-09-14 run | 2026-10-06 run |
|---|---|---|
| Correct and complete | 81% | 85% |
| Partially correct | 11% | 10% |
| Incorrect or wrong source | 8% | 5% |

**By department**

| Subset | Questions | Correct and complete (before → after) | Incorrect or wrong source (before → after) |
|---|---|---|---|
| Cardiology | 76 | 80% → 91% | 9% → 1% |
| Emergency | 84 | 82% → 82% | 7% → 7% |
| Cross-department | 40 | 80% → 80% | 8% → 8% |

The improvement is entirely in cardiology, as expected. The single remaining incorrect cardiology answer is a question where the reference answer was written against the superseded version; the coordinator corrected the reference answer, so it will count as correct in the next run.

## 4. Consistency test

In addition to the set, I ran 40 paraphrase pairs: the same cardiology question in two different wordings, including the dosing question from August. Before the re-index, 9 of 40 pairs got answers citing different versions. After the re-index: 0 of 40.

## 5. Observations

- With fewer near-duplicate documents, answers are also slightly shorter and cite fewer documents per answer (1.8 on average, was 2.4).
- Answer time did not change measurably.
- "Outdated source" flags from users in cardiology dropped from 11 in September to 1 since the re-index on 2026-10-05; that one concerned a document that had been marked current by mistake and was corrected the same day.

## 6. Recommendations

1. Re-index emergency as soon as its clean-up is done, and rerun the full set.
2. Keep "documents without status are not indexed" as a permanent rule.
3. Add the 40 paraphrase pairs to the evaluation set as a separate consistency check, run after every change.
4. For any future department, make the clean-up and the status field a precondition before indexing, not a repair afterwards.

## 7. Next steps

| Action | Owner | Due |
|---|---|---|
| Emergency clean-up | HVD (coordinators) | ongoing |
| Re-index emergency, rerun set | AE | after clean-up |
| Paraphrase pairs added to set | AE | 2026-10-14 |
| Input for the outdated-source report of the monthly content review | AE | 2026-10-12 |
