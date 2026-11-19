# Lunch and Learn: Dashboards on the Wall

| | |
|---|---|
| **Organisation** | Kestrel Consulting (internal) |
| **Date** | 2023-12-08, 12:15 to 13:15 |
| **Location** | Kestrel office Ghent, big room (sandwiches provided) |
| **Author / presenter** | Elien Jacobs, UX and Frontend Developer |
| **Document type** | Internal session notes |

## Summary of the talk

This lunch session was about one lesson from the **Bed Capacity Dashboard** at Mediva Care Group, which closed on 2023-11-30: a dashboard that nobody opens is not a dashboard, it is a report nobody reads.

### The situation

The dashboard was adopted quickly by the day shifts and the bed management office. But the **night shift nurses kept using the whiteboard** at the nursing station. Their reasoning was not resistance to change. At three in the morning, with two nurses for a whole ward, nobody walks to a PC, logs in, and opens a report to see which beds are free. The whiteboard is on the wall, in the corridor, always on.

### What we did

Instead of more training, I designed a **large-screen view per ward**:
- one page, no filters, no navigation
- beds as coloured tiles (free, occupied, expected discharge, blocked), with large room numbers
- auto-refresh, no login needed on the screen itself (the device is managed by hospital IT)
- readable from about five metres, also with tired eyes

We tested it for two weeks on one internal medicine ward. After that the hospital's IT team ordered wall screens for the other wards. Some wards kept a small whiteboard for notes that do not belong in any system, and that is fine.

### Design lessons

1. **Observe the moment of use.** We interviewed head nurses during the day. We should have spent one night on a ward during discovery. Lotte has added this to the discovery checklist for operational dashboards.
2. **Distance changes everything.** On a wall screen, font size, contrast and the number of elements are the design. I use a simple rule now: if it is not readable from the door, remove it.
3. **Colour is not enough.** About one in twelve men has some form of colour blindness. Every status also has a pattern or an icon.
4. **No interaction is a feature.** The large-screen view has no clicks at all. People trust it because it always looks the same.
5. **Let the whiteboard live.** The goal was never to kill the whiteboard, only to stop people copying numbers by hand.

## Questions and discussion

- *Is this specific to hospitals?* No. Anywhere with shifts, operators and little time (factories, terminals, control rooms) the same pattern applies. The tooling does not matter much; the context does.
- *How do you handle refresh on a wall screen?* A page that refreshes every few minutes, plus a visible "last updated" time. If the time is stale, people know not to trust the screen.
- *Security of unattended screens?* The screens only show bed status and room numbers, no patient names. That was agreed with the hospital before the pilot, and it is the first thing to agree on similar projects.

## Follow-up

- Elien will add a "wall screen" page template and the readability checklist to the design library.
- Slides (anonymised) are in the internal SharePoint under "Kennisdeling 2023".

Elien
