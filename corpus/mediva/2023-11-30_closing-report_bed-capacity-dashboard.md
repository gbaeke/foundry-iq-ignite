# Closing Report: Bed Capacity Dashboard

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Bed Capacity Dashboard |
| **Document type** | Closing report |
| **Date** | 2023-11-30 |
| **Author** | Lotte Willems, Managing Partner, Kestrel Consulting |
| **Version** | 1.0 (final) |

## 1. Summary

The Bed Capacity Dashboard project ran from 2023-05-08 to 2023-11-30 and closes today as planned. Mediva Care Group now has a single, near real-time view of bed occupancy, expected discharges and admissions in the pipeline, and the dashboard is in daily use on all three campuses. The project was delivered within the fixed price of EUR 60,000.

The sponsor on the Mediva side was Jeroen Lambrecht, IT Manager. I acted as engagement lead and project manager for Kestrel myself, which suited a small, tightly scoped engagement like this one.

## 2. Scope and solution

The goal was to replace the morning phone round, in which bed managers called every ward to collect occupancy figures, with a shared dashboard.

- **Data layer:** Azure Synapse Analytics pulls admission, transfer and discharge events from the hospital information system every 15 minutes and consolidates them into a bed-level model per campus, ward and room. Sofie Claes, Senior Data Engineer, built the pipelines and the occupancy model, including the logic for "blocked" beds (isolation, maintenance) that the source system records inconsistently.
- **Reporting layer:** Power BI reports on top of Synapse, with a campus overview, a ward drill-down and a short-term outlook for the next 24 hours. Elien Jacobs, UX and Frontend Developer, designed the dashboards and ran two rounds of usability sessions with bed managers and head nurses.

## 3. Delivery against plan

| Item | Plan | Actual |
|---|---|---|
| Start | 2023-05-08 | 2023-05-08 |
| End | 2023-11-30 | 2023-11-30 |
| Budget | EUR 60,000 fixed price | EUR 60,000, no change requests |
| Campuses live | 3 | 3 |

The rollout was staged: the first campus went live in September, the remaining two in October after the ward mapping was validated with the bed management office.

## 4. Adoption: the whiteboard problem

The main issue was not technical. Day shifts adopted the dashboard quickly, but the night shift nurses kept using the whiteboard at the nursing station. Their feedback was simple: at 3 a.m. nobody logs in to a laptop to check a report, while the whiteboard is just there on the wall.

Rather than pushing training, Elien designed a large-screen view per ward: a simplified, auto-refreshing page showing beds as coloured tiles, readable from across the corridor, running on a wall-mounted screen. After a two-week trial on one internal medicine ward, Jeroen's team ordered screens for the other wards. Whiteboard usage has largely stopped, although a few wards keep one for notes that do not belong in any system, and that is fine.

## 5. Handover

- Power BI workspace and Synapse pipelines transferred to Mediva IT; documentation and run book stored in the project document library.
- Two knowledge transfer sessions held with Jeroen's team (refresh monitoring, adding a ward, changing the outlook logic).
- Kestrel provides best-effort support until the end of January 2024.

## 6. Lessons learned

1. **Design for the actual moment of use.** The large-screen ward view should have been in the original scope; observing a night shift during discovery would have revealed it.
2. **Bed master data is political.** Agreeing which beds "exist" took longer than building the pipelines. Start that conversation in week one.
3. **Small fixed-price projects work well with one accountable lead** combining engagement and project management.

## 7. Sign-off

Accepted on behalf of Mediva Care Group by Jeroen Lambrecht, IT Manager, on 2023-11-30.

*Lotte Willems, Kestrel Consulting, Ghent*
