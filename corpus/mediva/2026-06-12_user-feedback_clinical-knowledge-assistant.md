# User Feedback Summary: First Pilot Weeks

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Clinical Knowledge Assistant |
| **Document type** | User feedback summary |
| **Date** | 2026-06-12 |
| **Author** | Amira El Idrissi, Lead AI Engineer, Kestrel Consulting |
| **Period** | Cardiology 2026-05-04 to 2026-06-11; emergency 2026-06-01 to 2026-06-11 |

## 1. Sources

- Usage logs (questions, answer time, feedback buttons, comments)
- Six short interviews with cardiology physicians and nurses, three with emergency staff
- Two visits to the emergency department during the night of 2026-06-04 and 2026-06-09, together with Ruben Wouters
- Monthly counter of blocked questions and warnings (also sent to Sarah Mertens)

## 2. Usage

| | Cardiology | Emergency |
|---|---|---|
| Pilot users with access | 74 | 118 |
| Users who asked at least one question | 29 | 21 |
| Questions | 412 | 236 |
| Share of questions between 20:00 and 08:00 | 18% | 47% |
| Thumbs up | 61% of rated answers | 58% |
| Thumbs down | 14% of rated answers | 17% |
| Answers rated at all | 31% | 22% |

Emergency has been live for less than two weeks but already generates more night questions than cardiology does in total. Nurses ask about a third of all emergency questions.

## 3. What users say

**Positive**
- "Faster than the intranet search, and it shows me the right protocol instead of five." (cardiology nurse)
- Physicians like the action-list-first answers and the version and date on each citation.
- The "not found in Mediva sources" answer is appreciated: "at least it doesn't make things up".

**Negative or mixed**
- Compound questions still feel slow at night (15 seconds or more).
- Some answers cite a document with the label "version derived"; two cardiologists said this makes them unsure whether the document is still valid.
- Emergency nurses use abbreviations the assistant does not always understand.
- Several users did not know the feedback buttons existed or did not see the point.

## 4. Night visits in emergency

During both nights the assistant was used on the shared PC at the nurses' desk, mostly for medication preparation and for procedures that are rare at night. Observations:

- Users read the action list and rarely open the source. For dosing questions they did open it in four of six cases we saw.
- The 30-minute session timeout on shared PCs, introduced after the security review, works but annoys users when they come back after 35 minutes. We keep it.
- One nurse typed a question with a bed number and age. No identifier was blocked, but the warning appeared; she rephrased. Good sign that the notice is understood.

## 5. Thumbs-down analysis (cardiology, 58 cases with comment)

| Cause | Cases |
|---|---|
| Answer too long or too general | 19 |
| Expected a different document | 14 |
| Abbreviation or local term not understood | 9 |
| Question outside the sources (correctly refused, user unhappy) | 8 |
| Answer slow | 5 |
| Other | 3 |

The 14 "expected a different document" cases were reviewed with the cardiology coordinator. Nine were acceptable (another current document with the same content). Five cited an older document where a newer one exists; the coordinator is checking these. We will watch this category closely.

## 6. Privacy counters (2026-05-04 to 2026-06-11)

- Questions blocked by the national register number or patient number check: 3
- Warnings shown for name patterns: 21
- Reported to Sarah Mertens on 2026-06-11.

## 7. Actions

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Abbreviation list for emergency, from the coordinator, added to the retrieval instructions | AE | 2026-06-26 |
| 2 | Make feedback more visible; short reason list on thumbs down | RW | 2026-06-26 |
| 3 | Shorter answers for simple questions | AE | 2026-06-19 |
| 4 | Add 50 real user questions to the evaluation set after review | AE | 2026-07-03 |
| 5 | Coordinator checks the five cardiology cases citing an older document | Cardiology coordinator | 2026-06-26 |
