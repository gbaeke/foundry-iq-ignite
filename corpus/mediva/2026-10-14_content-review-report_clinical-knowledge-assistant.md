# Monthly Content Review: Outdated-Source Report (October)

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Clinical Knowledge Assistant |
| **Document type** | Content review report |
| **Date** | 2026-10-14 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Meeting** | First monthly content review, 2026-10-14, 14:00 to 15:00 |
| **Participants** | Dr. Hilde Van Damme and two staff of the CMIO office; guideline coordinators of cardiology and emergency; Amira El Idrissi; Pieter De Smet |

## 1. Purpose of the monthly review

Agreed with Dr. Van Damme in September after the conflicting answers: every month the CMIO office and the guideline owners review which documents the assistant retrieved that users flagged as outdated, which documents lack a status, and which documents are due for review. Kestrel prepares this report from the usage logs and the knowledge base. Decisions on content are taken by the content owners, not by Kestrel.

## 2. Clean-up status

| Department | Documents reviewed | Current | Superseded | Archive | Status |
|---|---|---|---|---|---|
| Cardiology | 231 | 188 | 36 | 7 | Completed 2026-10-02, re-indexed 2026-10-05 |
| Emergency | 196 of about 370 | 151 | 38 | 7 | In progress since 2026-09-28 |

Emergency has more documents and more legacy copies than cardiology. The coordinator expects to finish in the first half of November.

## 3. "Outdated source" flags (2026-09-14 to 2026-10-12)

The flag was released by Ruben Wouters in September. Users can mark an answer as citing an outdated source, optionally naming the document they expected.

| | Cardiology | Emergency |
|---|---|---|
| Flags | 12 | 19 |
| Of which: confirmed outdated by coordinator | 10 | 14 |
| Of which: document was current, user expected another one | 2 | 4 |
| Of which: still being checked | 0 | 1 |
| Flags after re-index (from 2026-10-05) | 1 | n/a |

All confirmed cardiology cases date from before the re-index. In emergency, the 14 confirmed cases point to 9 distinct documents, all of which are now in the coordinator's clean-up list.

## 4. Documents without status

Since the cardiology knowledge source only indexes documents with status "current", new or changed documents without status are not visible to the assistant. This month: 6 new cardiology documents without status, all published by the same secretariat. The coordinator will set the status; Mediva IT will check whether the status field can be made mandatory on publication.

## 5. Review dates

From the metadata, 41 cardiology and 63 emergency documents marked current have a review date in the past. Being past the review date does not make a document invalid, but several are older than the accreditation rules allow. The CMIO office will send the list to the department heads.

## 6. Discussion

- **Ownership.** Hilde stressed that the clean-up would not have happened this fast without the coordinators' time. For any new department, a named content owner with time allocated is a condition, as listed in risk R2 of the September status report.
- **Flags as a signal.** The coordinators find the flags useful: they point to documents that are actually used. They asked for the flags to be sent to them weekly instead of monthly. Agreed; Amira will set up a weekly export.
- **Legacy share.** Several superseded emergency documents also exist on the legacy share. Hilde asked Jeroen's team for a plan to make the legacy share read-only for clinical content.

## 7. Decisions

- D1: Documents without status are never indexed (permanent rule).
- D2: Weekly export of "outdated source" flags to the coordinators.
- D3: Monthly content review continues, next on 2026-11-18.

## 8. Actions

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Finish emergency clean-up | Emergency coordinator | mid-November |
| 2 | Re-index emergency and rerun the evaluation set | AE | after clean-up |
| 3 | Weekly flag export | AE | 2026-10-21 |
| 4 | Status field mandatory on publication: feasibility | Mediva IT | 2026-11-04 |
| 5 | Review-date list to department heads | CMIO office | 2026-10-23 |
| 6 | Content governance summary for the Phase 1 review | PDS | 2026-10-28 |
