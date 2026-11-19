# Sprint Review Notes: Sprint P3 and Prototype Demo

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Discharge Letter Summarisation |
| **Document type** | Sprint review notes |
| **Date** | 2024-06-07, 14:00 to 15:15 |
| **Location** | Online |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |

## Attendees

Dr. Hilde Van Damme (CMIO), Jeroen Lambrecht and one integration developer of Mediva IT, two physicians of the evaluation group (internal medicine and geriatrics), Pieter De Smet, Thomas Maes, Amira El Idrissi.

## 1. Sprint goal

Review screen with source references next to the draft; template v2 for both departments; prototype ready for acceptance at the steering committee of 2024-06-12.

## 2. Demonstrated

**2.1 Review screen.** The physician sees the draft on the left and, per paragraph, the source sections on the right. Clicking a sentence highlights the section it came from. Sentences without a supporting section are underlined in orange. The geriatrics physician tried it on a long stay and found the highlighting "the reason I would trust this".

**2.2 Template v2.**
- Geriatrics: course of stay limited to a short paragraph per problem; functional status at admission and discharge as a fixed table; involved disciplines as an optional list.
- Internal medicine: pending results moved to a separate paragraph at the end, as requested in the workshop.

**2.3 Medication changes.** The comparison of admission and discharge medication is computed in code. In the test set of 200 historical stays the model found a documented reason for 84% of changes; for the others the draft says "reason not found in record" instead of guessing. Both physicians preferred this honest gap to a plausible invented reason.

**2.4 Scanned documents flag.** Stays with scanned documents without text show a line at the top of the draft listing how many were not used.

## 3. Measurements on 200 historical stays

| Measure | Sprint P2 | Sprint P3 |
|---|---|---|
| Average draft time | 24 s | 22 s |
| Statements without supporting section | 1.9% | 1.2% |
| Average draft length (internal medicine) | 1.4 pages | 1.0 pages |
| Average draft length (geriatrics) | 1.9 pages | 1.2 pages |
| Drafts blocked by content filter | 3 of 50 | 0 of 200 (adjusted configuration) |

## 4. Feedback

- The internal medicine physician noted that the draft sometimes uses wording that is more confident than the notes ("the infection was caused by" where the note says "probably"). Logged as a quality item for the evaluation; we will count these cases in the edit analysis.
- The geriatrics physician asked whether the draft can start automatically when the discharge is planned, so it is ready when she opens the letter. Pieter: technically possible, but it means generating drafts that may never be used and processing data before a physician asks for it. That is a data flow change and needs Sarah. Parked; not for this project.
- Jeroen asked for a short technical walkthrough for his integration developer before the evaluation. Planned for 2024-06-13.

## 5. Readiness for the evaluation

| Item | Status |
|---|---|
| Prototype functionally complete | Yes |
| Repeat pseudonymisation test | Running, results 2024-06-14 |
| Evaluation protocol | Draft, final 2024-06-14 |
| Training session for 12 physicians | Planned 2024-06-20 |
| Timer in review screen for edit time | Built, to be tested |

## 6. Decision

The attendees agreed to propose the prototype for acceptance at the steering committee of 2024-06-12. Thomas will prepare the acceptance note; on acceptance the second invoice (30%) can be sent.

## 7. Next sprint (E0, 10 to 21 June)

Finalise evaluation tooling: edit-time timer, edit distance between draft and signed letter, rating form for physicians. Run the repeat pseudonymisation test. Train the evaluation group.
