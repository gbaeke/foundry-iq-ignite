# User Feedback Summary: First Four Weeks on Campus Centrum

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Bed Capacity Dashboard |
| **Document type** | User feedback summary |
| **Date** | 2023-10-06 |
| **Author** | Elien Jacobs, UX and Frontend Developer, Kestrel Consulting |
| **Period** | 2023-09-11 to 2023-10-05 |

## 1. Sources

- Usage figures from the Power BI workspace (views per report page and per user group)
- 14 short interviews with bed managers, head nurses and the emergency coordinator
- Two night visits on campus Centrum (2023-09-20 and 2023-09-27, 22:00 to 01:00), one on an internal medicine ward and one on surgery
- Tickets and mails received by the Mediva IT service desk

## 2. Day shifts: adopted

The phone round on campus Centrum has stopped. The bed management office now opens the campus overview at the start of the day and keeps it open on a second screen. The emergency coordinator uses the specialty filter several times per hour at peak.

| User group | Active users (of total) | Typical use |
|---|---|---|
| Bed managers | 4 of 4 | Continuously during the day |
| Head nurses, day | 17 of 19 | Start of shift, before the bed meeting |
| Emergency coordinator | 3 of 3 | At peak, several times per hour |
| Management on call | 5 of 6 | Twice a day |

Service desk received six tickets, of which four were access requests for staff not yet in the right group and two were questions about "unknown" beds. No outages.

## 3. Night shift: still on the whiteboard

On both night visits the dashboard was not opened once. The night teams keep using the whiteboard at the nursing station: bed numbers in marker, with magnets for blocked beds and a cross for expected discharges. When the emergency department called for a bed, the nurse walked to the whiteboard, not to the PC.

What the night nurses told us:

- "At 3 a.m. I'm not going to log in to a laptop to look at a report."
- The ward PC is usually locked or in use for medication registration.
- The whiteboard is visible from the corridor and from the medication room; everybody on the floor sees it without doing anything.
- They trust the figures when shown to them. The problem is the moment and place of use, not the data.

So training will not solve this. The night shift needs something that is just there, like the whiteboard.

## 4. Proposal: large-screen ward view

A simplified, auto-refreshing page per ward, designed to be read from a distance on a wall-mounted screen near the nursing station:

- Beds as large coloured tiles in the physical layout of the ward (rooms in corridor order)
- Only four states: free, occupied, blocked, expected discharge today
- Large font, high contrast, readable from about five metres
- No login on the screen itself; the screen runs under a ward device account with read access to that ward's page only
- Refresh with every dataset refresh, with the update time in the corner

Sofie checked the data side: no model change is needed, the page uses the existing current-state table. I estimate the design and build at four to five days, which Lotte confirmed fits in the remaining fixed-price budget without a change request.

## 5. Trial

- Ward: one internal medicine ward on campus Centrum (the head nurse volunteered)
- Period: two weeks, 2023-10-16 to 2023-10-27
- Hardware: Mediva IT provides one wall-mounted screen and a small PC from stock
- Evaluation: night visit in the second week, short questionnaire for day and night teams, whiteboard photo at start and end of the trial

If the trial works, the decision to order screens for the other wards lies with Jeroen.

## 6. Other improvements requested

1. Printable A4 ward page for evening handover (moved up, combined with the large-screen layout).
2. A "beds freeing up before noon" indicator for the bed meeting. To be discussed; data depends on wards recording planned discharge times.

## 7. Next steps

| Action | Owner | Due |
|---|---|---|
| Build large-screen ward view | EJ | 2023-10-13 |
| Screen and device account for trial ward | Mediva IT | 2023-10-13 |
| Start trial | EJ, head nurse | 2023-10-16 |
| Same briefing format for campus Oost (go-live 2023-10-09) | EJ | 2023-10-06 |
