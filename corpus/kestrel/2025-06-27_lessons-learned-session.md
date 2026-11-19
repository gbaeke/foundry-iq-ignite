# Knowledge Sharing Session: Lessons Learned

| | |
|---|---|
| **Organisation** | Kestrel Consulting (internal) |
| **Date** | 2025-06-27, 15:00 to 17:00, followed by drinks |
| **Location** | Kestrel office Ghent, big room, plus Teams for remote colleagues |
| **Author / facilitator** | Elien Jacobs, UX and Frontend Developer |
| **Document type** | Internal meeting notes |

## Purpose

Second "kennisdeling" session of 2025. This time we chose three projects where something went sideways, to see what we can change in the way we start and run projects. About 18 colleagues attended, 4 remotely. The rule was the usual one: no blame, focus on what we would do differently.

## 1. Scaldis Ops Copilot: the late security review

*Presented by Pieter De Smet*

- The copilot answers questions on SOPs in SharePoint through a Teams bot. The customer's IT Security Officer, Wim Goossens, did his formal review only after the pilot was running.
- His main finding: answers must respect document-level permissions in SharePoint. Restricted procedures had come into scope halfway, and our index did not trim on permissions.
- Result: rework of the index and query layer, and the go-live moved from 1 July to 15 September.
- Discussion: several people said that on RAG projects "security review before go-live" is too late by definition, because permissions shape the architecture. Wim was right; we just involved him too late.

**Takeaways**
- Put the security officer's architecture review in sprint 1 of every project that indexes company documents.
- Ask early which content is restricted, even if it is "not in scope yet".

## 2. Fortalis Claims Triage: scope creep on a fixed price

*Presented by Thomas Maes*

- Fixed price project for automated triage of incoming claims. Midway, the customer asked to add water damage claim types. It was handled with change request CR-07, approved by their sponsor, but only after a lot of work had already started informally.
- Thomas was candid: the team said yes in sprint reviews before the change was costed. By the time CR-07 was drafted, part of the effort was already spent.
- Discussion on whether fixed price is a good fit for ML projects where the data decides the effort. No consensus, but agreement that new categories or document types are always a change request.

**Takeaways**
- Keep a visible "parking lot" for new requests in each sprint review; nothing moves into the sprint without a cost estimate.
- Draft the change request the same week the request comes in, not when the budget runs out.

## 3. Verhaeghe Line Sensor Data Platform: OT access

*Presented by Sofie Claes*

- Connecting line sensors to the cloud platform was blocked by the firewall between the OT and IT network. It took 5 weeks before the customer's IT coordinator could arrange the firewall change.
- In the meantime the team built pipelines on sample files, which helped, but integration testing was squeezed at the end.
- Sofie's main point: in manufacturing, OT access is a project in itself, with its own owners, change windows and approvals.

**Takeaways**
- Arrange OT network access before kickoff and make it an explicit precondition in proposals.
- Identify the OT owner on the customer side during presales, not after kickoff.

## Common thread

Elien summarised it on the whiteboard: all three issues were **known unknowns at the start**. Security, scope and network access each have an owner on the customer side who was involved too late. Proposal: a short "day zero checklist" in our project template.

## Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Draft "day zero checklist" (security review, OT access, change procedure) | EJ | 2025-07-18 |
| 2 | Add security review in sprint 1 to the RAG project template | PDS | 2025-07-18 |
| 3 | Add OT access precondition to proposal template | SC | 2025-07-25 |
| 4 | Update change request template with a "date requested" field | TM | 2025-07-11 |
| 5 | Review checklist at the partner meeting | LW | 2025-09-04 |

Next session: December 2025, topic to be decided.

Elien
