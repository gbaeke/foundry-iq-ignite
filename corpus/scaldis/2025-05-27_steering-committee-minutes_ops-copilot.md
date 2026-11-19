# Steering Committee Minutes #4: Scaldis Ops Copilot

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Scaldis Ops Copilot |
| **Date** | 2025-05-27, 10:00 to 11:15 |
| **Location** | Scaldis HQ Antwerp, meeting room "Kaai 3" |
| **Author** | Lotte Willems, Managing Partner, Kestrel Consulting |
| **Document type** | Steering committee minutes |

## Attendees

Koen Verstraete (CIO, sponsor), Nathalie Dumont (product owner), Wim Goossens (IT Security Officer), Lotte Willems, Pieter De Smet, Thomas Maes.

## 1. Context

Following the security review report of 9 May and the meeting of 13 May, go-live was re-planned from 2025-07-01 to **2025-09-15**. This steering committee confirms the plan, the revised forecast and the conditions for go-live.

## 2. Security findings and redesign

Pieter presented the redesign for H-01 (document-level permission trimming):
- each indexed chunk carries the identifiers of the users and groups allowed to read the source document in SharePoint;
- a permission sync job runs every hour, and a full reconciliation every night;
- every query from the Teams bot is filtered on the asking user's identity and group memberships;
- if permissions cannot be determined for a document, the document is not indexed ("fail closed").

Wim agreed with the direction and asked for an architecture decision record he can review before implementation starts. He also asked that the re-test includes the restricted customs procedures, where several documents have unique permissions.

Status of the mediums: M-02 and M-03 are fixed in sprint 10 (Ruben Wouters). M-01 retention agreed at 90 days with pseudonymised user IDs. M-04 waiting for approvals from two site owners.

## 3. SharePoint group structure

Wim and Pieter both raised that groups on the restricted sites are inconsistent: some sites use SharePoint groups, others individual permissions added over the years. Trimming will be correct either way, but messy permissions make it hard to explain why someone does or does not get an answer.

**Decision:** Wim leads a clean-up of the group structure on the restricted sites with the site owners, to be finished by 2025-06-20.

## 4. Revised plan

| Milestone | Date |
|---|---|
| ADR for permission trimming reviewed by Wim | 2025-06-06 |
| Redesign implemented (sprints 10 and 11) | 2025-06-13 |
| Restricted libraries indexed with trimming | 2025-06-27 |
| Pilot continues over the summer, extended to restricted content for pilot shift leaders | July–August |
| Security re-test by Wim's team | second half of August |
| Go-live | 2025-09-15 |

Nathalie confirmed that most shift leaders are on "bouwverlof" from 21 July to 8 August; user acceptance testing is planned in the last two weeks of August, overlapping with the re-test.

## 5. Budget

Thomas presented the revised forecast to complete. With the redesign, the re-test and the longer pilot, the forecast is above the EUR 150,000 estimate. Lotte confirmed that Kestrel will not charge the extra effort spent on the CR-01 separate index, which is now replaced. Koen asked for a clear cost line per month until go-live and a stop-and-discuss point if the forecast moves again.

**Decision:** Koen approves continuation on a time and materials basis according to the revised forecast. Monthly reporting against it.

## 6. Lessons recorded today

Koen asked that one point is written down explicitly: the security review was planned at the end, while restricted content entered scope in March. "Next time Wim sees the design before anything is indexed." All agreed.

## 7. Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | ADR permission trimming to Wim | PDS | 2025-06-06 |
| 2 | Group structure clean-up on restricted sites | WG with site owners | 2025-06-20 |
| 3 | Approvals for reduced indexing scope (M-04) | ND | 2025-06-06 |
| 4 | Monthly cost line until go-live | TM | monthly |
| 5 | UAT plan for end of August | TM, ND | 2025-06-27 |

Next steering committee: 2025-06-24.

*Minutes by Lotte Willems*
