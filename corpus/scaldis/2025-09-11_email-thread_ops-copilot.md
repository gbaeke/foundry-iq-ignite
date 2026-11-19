# Email Thread: Renamed Customs Group and Go-live Date

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Scaldis Ops Copilot |
| **Date** | 2025-09-11 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting (export of thread) |
| **Document type** | Email thread (exported) |

---

**From:** Pieter De Smet
**To:** Wim Goossens
**Cc:** Thomas Maes; Nathalie Dumont; Ruben Wouters
**Date:** Tuesday 9 September 2025, 16:20
**Subject:** Permission sync errors on the customs procedures library

Wim,

Since this morning the daily sync report shows 41 documents in the customs procedures library that are no longer returned for anyone in the customs desk and shift leader roles. The sync logs show that the SharePoint group used on those documents was replaced last night by a group with a new name. Our job could not resolve the old group anymore and, as designed, failed closed: the documents are hidden for everyone except the site owners.

Nothing is exposed; the opposite. But it means the restricted customs content is currently not usable, six days before go-live. Do you know who made the change? The nightly reconciliation will pick up the new group tonight.

Pieter

---

**From:** Wim Goossens
**To:** Pieter De Smet
**Cc:** Thomas Maes; Nathalie Dumont; Ruben Wouters; Koen Verstraete
**Date:** Wednesday 10 September 2025, 08:45
**Subject:** RE: Permission sync errors on the customs procedures library

Pieter,

The site owner of the customs procedures library renamed the group as part of an internal reorganisation of the customs desk. It was not announced to us either. Good that the sync failed closed.

My concern: the renamed group was not a pure rename. Members were moved and a few documents got their permissions re-applied by hand. My team tested this library in August in a different state. I want one more round on the restricted customs folders, using the permission matrix, before I sign off for production. We can do it Monday 15 and Tuesday 16 September. That means no go-live on the 15th for my part.

Wim

---

**From:** Thomas Maes
**To:** Wim Goossens; Pieter De Smet
**Cc:** Koen Verstraete; Nathalie Dumont; Ruben Wouters; Elien Jacobs; Lotte Willems
**Date:** Wednesday 10 September 2025, 11:30
**Subject:** RE: Permission sync errors on the customs procedures library

All,

Proposal after a call with Pieter and Nathalie:

- Re-test of the customs folders by Wim's team on 15–16 September, results by 17 September.
- Fixes, if any, on 17–18 September.
- **Go-live on Monday 2025-09-22**, one week after the re-planned date.
- Champion training (done last week) stays valid; the shift briefings simply move one week.
- Pilot users keep access in the meantime, without the customs folders.

Effort for the extra week is limited: the team is mostly in standby, and the re-test itself is on the Scaldis side.

Koen, can you confirm?

Thomas

---

**From:** Koen Verstraete
**To:** Thomas Maes
**Cc:** Wim Goossens; Pieter De Smet; Nathalie Dumont; Ruben Wouters; Elien Jacobs; Lotte Willems
**Date:** Wednesday 10 September 2025, 17:05
**Subject:** RE: Permission sync errors on the customs procedures library

Confirmed: go-live 22 September. I prefer one week later with Wim's signature than a discussion afterwards.

Nathalie, please make sure group changes on the operations sites are announced to Pieter's team until hypercare is over. And the site owner of customs should hear this from you, not from me.

KV

---

**From:** Nathalie Dumont
**To:** Koen Verstraete; Thomas Maes
**Cc:** Wim Goossens; Pieter De Smet; Ruben Wouters; Elien Jacobs; Lotte Willems
**Date:** Thursday 11 September 2025, 07:55
**Subject:** RE: Permission sync errors on the customs procedures library

Done. I spoke with the site owner yesterday evening. From now on, any group change on the operations and restricted sites goes through a short mail to the copilot team and Wim, until the end of October at least.

Champions have been told the new date; briefings move to the week of 22 September.

Nathalie
