# Kickoff Meeting Notes: Line Sensor Data Platform

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Line Sensor Data Platform |
| **Date** | 2024-06-03, 09:00 to 12:30 |
| **Location** | Verhaeghe Foods, Roeselare (canteen meeting room) |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Meeting notes |

## Attendees

- Ann Verhaeghe, CEO, Verhaeghe Foods (sponsor), first hour
- Dries Callens, Quality Manager, Verhaeghe Foods (product owner)
- Tine Desmet, IT Coordinator, Verhaeghe Foods
- Sofie Claes, Kestrel Consulting (project lead and data engineer)
- Jonas Peeters, Kestrel Consulting (IoT and platform engineer)
- Bram Visser, DataForge (Databricks engineer, subcontracted)
- Lotte Willems, Kestrel Consulting (engagement lead), first hour

## 1. Why this project

Ann opened by saying that she wants "one version of the numbers" for quality and production. Today every line has its own HMI and its own paper log, and the monthly quality meeting starts with a discussion about whose export is right. Dries added that customer audits ask for freezing temperatures per batch, and that it takes his team half a day to find them.

## 2. Scope recap

Sofie walked through the signed proposal:

- Six production lines in scope, connected one by one, with line 1 as pilot.
- Telemetry from an edge gateway per line into Azure IoT Hub.
- A Microsoft Fabric lakehouse with bronze, silver and gold layers. Resampling and batch linking in Databricks notebooks, owned by Bram.
- Batch quality report, shift report and alert rules for blanchers and freezer tunnels.
- Fixed price, EUR 130,000 excl. VAT. Handover on 2025-01-31.

Out of scope: control actions on the lines, changes to PLC programmes, predictive maintenance.

## 3. Network and access

Tine explained the plant network. The PLCs and HMIs sit on the OT network; offices and servers sit on the IT network. A firewall separates the two and is maintained by an external partner. Tine will submit the request for outbound traffic from the line 1 gateway this month. Nobody at the table expected this to take long, since only outbound traffic is needed.

Jonas will send Tine the exact endpoints and ports by Friday.

## 4. Planning and harvest season

Dries warned that the pea campaign starts in the second half of June and the line teams will be very busy until the end of the bean season. On-site work on the lines must be agreed with the shift leaders at least a week ahead, and preferably done in weekend maintenance windows.

Sofie proposed to do the tag inventory for line 1 and line 2 in June, before the peak, and the other lines later.

## 5. Ways of working

- Weekly demo on site in Roeselare, Thursday afternoon, starting once data flows.
- Status report every four weeks to Ann, Dries, Tine and Lotte.
- Steering meeting roughly every two months, with Ann.
- Sofie is the single point of contact for Verhaeghe; Bram works through Sofie.

## Decisions

1. Line 1 is the pilot line.
2. The platform only reads data. No writes back to the PLCs.
3. Reports are shift-based, not per operator (see action 6).

## Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Send endpoint and port list for the gateway to Tine | JP | 2024-06-07 |
| 2 | Submit firewall request for line 1 gateway | TD | 2024-06-21 |
| 3 | Tag inventory line 1 with maintenance | SC / JP | 2024-06-14 |
| 4 | Share production planning export (sample) | DC | 2024-06-12 |
| 5 | Create Azure resource groups and Fabric workspace | TD / JP | 2024-06-21 |
| 6 | Check with HR whether operator names may appear in reports | DC | 2024-06-28 |

Next meeting: requirements workshop with the quality team, 2024-06-14.
