# Email Thread: Conflicting Answers on a Cardiology Dosing Question

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Clinical Knowledge Assistant |
| **Document type** | Email thread |
| **Date** | 2026-08-21 |
| **Author** | Amira El Idrissi, Lead AI Engineer, Kestrel Consulting (thread export) |

---

**From:** Amira El Idrissi
**To:** Dr. Hilde Van Damme
**Cc:** Pieter De Smet, Ruben Wouters, Jeroen Lambrecht
**Date:** 2026-08-18 17:45
**Subject:** Conflicting answers: cardiology dosing table

Dear Hilde,

I want to flag an issue before the review with the coordinators on Friday.

Two cardiologists sent thumbs-down feedback last week on what is essentially the same question about the dosing table in one of the cardiology protocols. The assistant gave **two different answers** depending on how the question was phrased. Both answers cited a document called by the same title, with a different version and date.

What I found:

- The intranet library contains the current version of the protocol and an older version that was never archived. A third copy sits in the legacy share.
- The knowledge base indexes both intranet versions, as both are marked as published.
- Retrieval finds both. Depending on the wording, the older version ranks higher, because its wording matches the way some colleagues still phrase the question.
- The dosing table differs between the versions.

The assistant is not "wrong" with respect to its sources; it is faithful to a document that should not be there. But the effect for the user is the same: a conflicting answer on a dosing question. Nobody reported acting on the older table, and the answer always showed the version and date.

I checked further: in cardiology alone I find at least 23 titles with more than one version marked as published. Emergency has not been checked yet.

Kind regards,
Amira

---

**From:** Dr. Hilde Van Damme
**To:** Amira El Idrissi
**Cc:** Pieter De Smet, Ruben Wouters, Jeroen Lambrecht
**Date:** 2026-08-19 08:10
**Subject:** RE: Conflicting answers: cardiology dosing table

Amira,

Thank you for the quick analysis. This is serious enough that I want to act before the steering committee.

Can you immediately remove the older version of this specific protocol from the index? I will ask the cardiology coordinator to confirm today which version is valid.

On the broader point: I am not surprised. We have been saying for years that the library needs cleaning. But I need to understand what you can do technically and what has to come from us.

Hilde

---

**From:** Pieter De Smet
**To:** Dr. Hilde Van Damme, Amira El Idrissi
**Cc:** Ruben Wouters, Jeroen Lambrecht
**Date:** 2026-08-19 11:32
**Subject:** RE: Conflicting answers: cardiology dosing table

Hilde,

The older version of the protocol was removed from the index this morning after the coordinator's confirmation. Amira reran the dosing questions in the evaluation set: consistent answers now.

What we can do technically:
- Prefer the most recent version when several documents share a title.
- Always show version and date in the answer (already done) and warn when two versions of the same document were found.
- Report every answer where users flagged an outdated source.

What we cannot do: decide which version is valid. A newer date does not always mean the valid one; we have seen drafts published by mistake with a later date. That decision must come from the content owners.

Our proposal: your team and the guideline coordinators mark every cardiology and emergency document as current, superseded or archive; we index only "current". We would like to discuss it at the steering committee of 9 September.

Pieter

---

**From:** Dr. Hilde Van Damme
**To:** Pieter De Smet, Amira El Idrissi
**Cc:** Ruben Wouters, Jeroen Lambrecht
**Date:** 2026-08-21 09:20
**Subject:** RE: Conflicting answers: cardiology dosing table

Agreed in principle. Please put the proposal on the agenda for 9 September, with an estimate of the coordinators' effort. In the meantime:

- Ruben, can users flag "outdated source" directly on an answer? I want the clinicians to help us find these.
- Amira, please prepare the list of the 23 cardiology titles for the coordinator.

Hilde
