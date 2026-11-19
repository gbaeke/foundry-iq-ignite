# Workshop Notes: Requirements and Process Mapping

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Bed Capacity Dashboard |
| **Document type** | Workshop notes |
| **Date** | 2023-05-24, 13:30 to 16:30 |
| **Location** | Mediva, campus Centrum |
| **Author** | Elien Jacobs, UX and Frontend Developer, Kestrel Consulting |

## Participants

Three bed managers (one per campus), the bed management office coordinator, the emergency department coordinator, two head nurses, Jeroen Lambrecht (IT Manager, part of the session), Sofie Claes and Elien Jacobs (Kestrel). Lotte Willems joined for the prioritisation at the end.

## 1. Current process, as mapped on the wall

We mapped the morning bed round step by step with sticky notes. The current flow:

1. 7:30: bed manager calls each ward, writes free / occupied / blocked / expected discharges on a printed list.
2. 8:30: lists from the three campuses are typed into one spreadsheet.
3. 9:00: spreadsheet is mailed to management on call, emergency and the ward heads.
4. During the day: emergency calls the bed manager directly; the bed manager calls wards again.
5. Evening: the late-shift bed manager hands over by phone to the night nurse coordinator.

Observations from my visit on 2023-05-16 confirmed this. One round on campus Centrum took 52 minutes, of which a large part was waiting for someone to pick up the phone on the ward.

Pain points named by participants:

- Figures are outdated within an hour.
- "Expected discharge" means different things: some wards report discharges planned for today, others for today and tomorrow.
- Blocked beds are reported inconsistently: isolation, maintenance, a broken bed, a room kept free for a planned admission.
- Nobody trusts the official bed list.

## 2. What users need to see

| User | Main question | Frequency |
|---|---|---|
| Bed manager | Where can I place the next admission? | Continuously |
| Emergency coordinator | How many beds per specialty are free right now? | Several times per hour at peak |
| Head nurse | What does my ward look like for the next 24 hours? | Start of shift |
| Management on call | Are we heading for a capacity problem today? | Twice a day |

## 3. Definitions agreed

- **Occupied:** a patient is admitted to the bed according to the hospital information system.
- **Free:** the bed exists in the agreed bed list, is not occupied and not blocked.
- **Blocked:** the bed cannot be used, with one of four reasons: isolation, maintenance, reserved, other. Sofie will check how these are recorded in the source.
- **Expected discharge:** a discharge date of today or tomorrow is recorded. The outlook shows "today" and "next 24 hours" separately to avoid the current confusion.

The bed coordinator will bring the definitions to the nursing directorate for confirmation.

## 4. Prioritisation (MoSCoW)

**Must:** campus overview, ward drill-down, blocked beds with reason, 15-minute refresh, outlook next 24 hours.
**Should:** specialty filter for emergency, history of occupancy per day.
**Could:** printed A4 version for the evening handover, simple occupancy trend for management.
**Won't (this project):** patient names, nurse staffing, automatic bed assignment.

## 5. Open points

- Who owns the bed list? Jeroen proposed that the bed management office becomes the owner, with facility management providing changes. Needs a decision from the nursing directorate.
- Several wards have "extra" beds placed in corridors during winter peaks. Should they exist in the model? Parked until the data model is drafted.

## Next steps

- Sofie drafts the bed model and the mapping of ADT events (target 2023-06-09).
- Elien prepares paper prototypes of the overview and the ward page for the first usability round in early July.
- Lotte raises the bed list ownership question with Jeroen for the nursing directorate.
