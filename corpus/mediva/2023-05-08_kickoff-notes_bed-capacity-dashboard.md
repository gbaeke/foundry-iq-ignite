# Kickoff Notes: Bed Capacity Dashboard

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Bed Capacity Dashboard |
| **Document type** | Meeting notes (kickoff) |
| **Date** | 2023-05-08, 10:00 to 12:00 |
| **Location** | Mediva, campus Centrum, meeting room "Schelde" |
| **Author** | Lotte Willems, Managing Partner, Kestrel Consulting |

## Attendees

- Jeroen Lambrecht, IT Manager, Mediva Care Group (JL), sponsor
- The coordinator of the central bed management office, Mediva
- Two head nurses (internal medicine, surgery), campus Centrum
- Lotte Willems, engagement lead and project manager, Kestrel (LW)
- Sofie Claes, Senior Data Engineer, Kestrel (SC)
- Elien Jacobs, UX and Frontend Developer, Kestrel (EJ)

## 1. Why this project

Jeroen opened by describing the current morning routine. Every day around 7:30 the bed management office phones each ward on the three campuses (Centrum, Oost and Zuid) to ask how many beds are free, how many discharges are expected and which beds are blocked. The figures go into a spreadsheet that is outdated by the time it is mailed around at 9:00. On busy days the emergency department calls the bed managers directly and the round starts again.

The goal of the project is one shared, near real-time view of bed occupancy that replaces the phone round, not another report next to it.

## 2. Scope as agreed in the offer

- Data layer in Azure Synapse Analytics, fed by the admission, discharge and transfer (ADT) events from the hospital information system.
- A bed-level model per campus, ward and room.
- Power BI reports: campus overview, ward drill-down and a short-term outlook.
- Rollout on all three campuses before the end of November.
- Fixed price EUR 60,000, period 2023-05-08 to 2023-11-30.

Explicitly out of scope: integration back into the hospital information system, staffing and nurse planning, and anything that shows patient names. The bed coordinator confirmed that bed managers do not need names on the overview; a bed status and an expected discharge date are enough.

## 3. Discussion

- **Definition of a bed.** The head nurse of surgery pointed out that the official bed list and the beds actually in use differ, especially where rooms are converted for isolation. Sofie asked for the official bed list per ward as a starting point. Jeroen warned that the list is maintained by facility management and "not everybody agrees with it". To be discussed in the requirements workshop.
- **Refresh frequency.** Bed managers would like "live". Sofie explained that the ADT feed lands in batches; a 15-minute refresh is realistic and was accepted as sufficient.
- **Users.** Bed managers, head nurses, the emergency department coordinator and the hospital management on call. Elien will run usability sessions with each group.
- **Access.** Jeroen asked that access follows the existing hospital user groups; no separate accounts.

## 4. Planning

| Phase | Period |
|---|---|
| Discovery and requirements | May |
| Data model and pipelines | June to July |
| Dashboard design and usability rounds | July to August |
| Go-live first campus | September |
| Go-live remaining campuses, handover | October to November |

The summer holidays are a known constraint: many head nurses are away in the second half of July and early August. Usability sessions will be planned around that.

## Decisions

- D1: Refresh every 15 minutes is the target.
- D2: No patient-identifying fields in the data model or the reports.
- D3: Campus Centrum goes first.

## Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Provide official bed list per ward for all campuses | JL | 2023-05-17 |
| 2 | Arrange read access to the ADT event extract | JL | 2023-05-19 |
| 3 | Plan requirements workshop with bed management office | LW | 2023-05-12 |
| 4 | Observe a morning phone round on campus Centrum | EJ | 2023-05-16 |
| 5 | Set up the Synapse workspace in Mediva's subscription | SC | 2023-05-26 |

Next status meeting: biweekly on Friday, starting 2023-05-26.
