# Email Thread: Security Review Outcome

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Scaldis Ops Copilot |
| **Date** | 2025-05-12 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting (export of thread) |
| **Document type** | Email thread (exported) |

---

**From:** Wim Goossens
**To:** Pieter De Smet; Thomas Maes
**Cc:** Koen Verstraete; Nathalie Dumont
**Date:** Friday 9 May 2025, 17:02
**Subject:** Ops Copilot: security review report v1.0

Pieter, Thomas,

Attached the report of the security review. After seeing the pilot and the plan for the restricted libraries, I preferred not to wait until June.

Summary: 11 findings. 1 high, 4 medium, 6 low.

**High (H-01).** The copilot does not apply document-level permission trimming. In the restricted libraries, about one in five documents has unique permissions that differ from the library. Example: three incident report templates are restricted to HSE only, while the library is open to all shift leaders. With the separate-index approach in CR-01, a shift leader could get an answer from a document he cannot open. That is not acceptable. The same applies to a handful of documents with unique permissions in the general library.

**Medium:**
- M-01: conversation logs contain full user names and are kept without a defined retention period
- M-02: the bot's app secret is stored in application settings instead of a secrets vault, and has no rotation
- M-03: no rate limiting per user on the bot endpoint
- M-04: the indexing identity has read access to more sites than needed

The lows are in the report. I am available next week to go through it.

Wim

---

**From:** Pieter De Smet
**To:** Wim Goossens; Thomas Maes
**Cc:** Koen Verstraete; Nathalie Dumont
**Date:** Monday 12 May 2025, 08:55
**Subject:** RE: Ops Copilot: security review report v1.0

Wim,

Thanks for the thorough review, and for doing it early. We agree with all findings, and with H-01 in particular.

What H-01 means technically: every chunk in Azure AI Search must carry the list of users and groups allowed to read the source document, kept in sync with SharePoint, and every query must be filtered on the identity of the user asking it. That replaces the separate restricted index from CR-01 and applies to the general library too. It touches the indexing pipeline, the query layer and the bot (which must pass the user's identity reliably). Estimated two sprints of redesign plus a re-test with your team.

For the mediums:
- M-01: pseudonymised user IDs in logs, 90 days retention, names only in the feedback export for Nathalie's weekly report. To check with you.
- M-02 and M-03: Ruben can fix these in sprint 10.
- M-04: we reduce the indexing identity to the in-scope sites, with written approval of each site owner.

Honestly: we cannot do this properly and still go live on 1 July. User testing of the redesign would fall in the summer holidays.

Pieter

---

**From:** Thomas Maes
**To:** Wim Goossens; Pieter De Smet
**Cc:** Koen Verstraete; Nathalie Dumont; Lotte Willems
**Date:** Monday 12 May 2025, 10:30
**Subject:** RE: Ops Copilot: security review report v1.0

All,

I have put a meeting in the agenda for Tuesday 13 May at 11:00 with Koen and Nathalie to decide on the plan. I will bring two options:

A. Go live on 2025-07-01 with the general library only and no restricted content. Still requires trimming for the documents with unique permissions in the general library, so H-01 is not avoided.
B. Re-plan go-live to mid-September with document-level trimming for all content, re-test by Wim's team in the second half of August, after "bouwverlof".

Revised budget forecast follows at the steering committee of 27 May.

Thomas

---

**From:** Koen Verstraete
**To:** Thomas Maes; Pieter De Smet; Wim Goossens
**Cc:** Nathalie Dumont; Lotte Willems
**Date:** Monday 12 May 2025, 12:14
**Subject:** RE: Ops Copilot: security review report v1.0

Thomas, I will come to the meeting tomorrow, but I can already say I see no point in option A if it does not avoid the main finding. Prepare B in detail, including a realistic date.

KV
