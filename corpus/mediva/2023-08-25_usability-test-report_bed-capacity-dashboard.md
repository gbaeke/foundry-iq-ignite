# Usability Test Report: Round 2

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Bed Capacity Dashboard |
| **Document type** | Usability test report |
| **Date** | 2023-08-25 |
| **Author** | Elien Jacobs, UX and Frontend Developer, Kestrel Consulting |
| **Sessions** | 2023-08-22 to 2023-08-24, campuses Centrum, Oost and Zuid |

## 1. Set-up

The second usability round tested the Power BI reports on real (current-day) data from the Synapse model, instead of the paper prototypes of round 1. Each participant received three to five tasks and was asked to think aloud. Sessions lasted 30 to 45 minutes. No patient data is visible in the reports; participants worked on bed status only.

| Group | Planned | Held |
|---|---|---|
| Bed managers | 2 | 2 |
| Head nurses | 4 | 5 |
| Emergency coordinator | 1 | 1 |
| Night nurse | 1 | 0 |
| **Total** | **8** | **8** |

The night session on campus Centrum (23 August, 21:00) did not take place: the ward had two emergency admissions at shift change and the night nurse could not leave the floor. We did not manage to reschedule before the end of the round. I note it as an open point below.

## 2. Tasks and results

| # | Task | Success | Avg. time |
|---|---|---|---|
| T1 | Find the number of free beds in cardiology on campus Oost | 8/8 | 14 s |
| T2 | Find out why bed 2 in a given room is blocked | 7/8 | 21 s |
| T3 | Tell how many discharges your ward expects in the next 24 hours | 8/8 | 18 s |
| T4 | Find the campus with the lowest free capacity in surgery | 6/8 | 35 s |
| T5 | See when the data was last updated | 5/8 | 26 s |

Compared with round 1, the ward page is clearly easier: T2 went from 4/11 to 7/8, mainly because the blocked reason is now shown on the tile itself.

## 3. Findings

**F1: Last update time is overlooked (high).** Three participants did not find the update timestamp in the header. Since late data is the main risk for trust, the timestamp moves next to the ward name and turns orange after 30 minutes without new data, as described in Sofie's design note.

**F2: Specialty filter confusing for emergency (medium).** The emergency coordinator expected "internal medicine" to include geriatrics on campus Zuid, which uses local specialty codes. Sofie will map the two local codes to the common specialty list; the local name stays visible on the ward page.

**F3: Colours (medium).** Red for "occupied" was read as "problem". New palette: occupied in dark grey, free in green, blocked in amber, expected discharge as an outline. Checked for colour-blind readability.

**F4: Printing (low).** Two head nurses asked for a printable version for the evening handover. A simple A4 page per ward is in the "could" list; we will add it if time allows after the first go-live.

**F5: Too many clicks on a small screen (low).** On the small ward PC monitors the ward page needs a compact layout.

## 4. Quotes

- "If this is right, I don't need to call anyone at half past seven." (bed manager, campus Oost)
- "I want to see my ward at a glance, not a report." (head nurse, campus Zuid)

## 5. Open point: night shift

We have not seen the night shift use or react to the dashboard. Night teams work with fewer people, rarely sit at a PC and today use the whiteboard at the nursing station for the bed situation. I recommend that after the go-live of campus Centrum someone from Kestrel visits a ward during a night shift to observe how the bed status is actually used.

## 6. Changes before go-live (11 September)

1. Update timestamp next to ward name, orange after 30 minutes (F1).
2. Local specialty codes on campus Zuid mapped (F2).
3. New colour palette (F3).
4. Compact ward page for small monitors (F5).

All four are planned in the last two weeks before go-live and fit within the fixed price.
