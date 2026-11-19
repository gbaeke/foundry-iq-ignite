# Steering Committee Minutes #1: Scaldis Ops Copilot

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Scaldis Ops Copilot |
| **Date** | 2025-02-20, 14:00 to 15:00 |
| **Location** | Scaldis HQ Antwerp, meeting room "Kaai 3" |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Document type** | Steering committee minutes |

## Attendees

Koen Verstraete (CIO, sponsor), Nathalie Dumont (Head of Terminal Operations, product owner), Wim Goossens (IT Security Officer, for item 3), Pieter De Smet, Thomas Maes. Lotte Willems excused.

## 1. Progress

Thomas reported on the first month:
- Indexing proof of concept done on the Quay site (214 documents), with 29 of 40 test questions answered correctly and completely.
- Teams bot skeleton running in the dev tenant; Ruben Wouters and Elien Jacobs have a clickable prototype of the answer cards ready for user tests next week.
- Burn: about 14% of the EUR 150,000 estimate, in line with plan. Monthly burn report and Azure consumption alerts are in place.

## 2. Content quality

Pieter showed the two wrong answers from the proof of concept; both came from an outdated checklist next to its replacement. Nathalie was surprised by how many old versions are still in the libraries. Koen: "The copilot is a mirror, it shows us what we never cleaned."

**Decision:** Nathalie appoints one content owner per SharePoint site. Kestrel delivers a monthly list of suspected duplicates and outdated versions from the index.

## 3. Security and permissions

Wim shared the Scaldis security checklist for AI applications on 31 January. He wants a formal review before go-live. Pieter asked whether restricted procedures will enter scope. Nathalie confirmed there is demand: shift leaders want incident handling procedures in the bot as well. Koen prefers to finish the general library first.

Wim indicated that if restricted content comes in, the bot must not show anything a user cannot open in SharePoint. Pieter explained that this needs permission information in the index and a filter at query time, and that it is significantly more work than the current design.

**Decision:** release 1 remains the general operations library. Any extension to restricted content goes through a change request with a security impact assessment. The formal security review stays planned for June, before go-live.

## 4. Planning

No change: pilot group of 25 users from sprint 6, target go-live 2025-07-01. Nathalie will nominate pilot users across all shifts by 14 March, including two users who only work on shared gate PCs.

## 5. Cost control

Koen asked what drives the running cost after go-live. Pieter: mainly the number of questions and the size of the retrieved context, plus a fixed cost for the search service. A cost per question will be reported from the pilot onwards.

## 6. Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Appoint content owners per SharePoint site | ND | 2025-03-07 |
| 2 | First list of suspected outdated documents | PDS | 2025-03-07 |
| 3 | Nominate 25 pilot users | ND | 2025-03-14 |
| 4 | Cost per question estimate | PDS | 2025-04-17 |
| 5 | Plan formal security review slot | WG, TM | 2025-03-31 |

Next steering committee: 2025-03-20.

*Minutes by Thomas Maes*
