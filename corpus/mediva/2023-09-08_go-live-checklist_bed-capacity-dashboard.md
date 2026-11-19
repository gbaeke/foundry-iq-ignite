# Go-Live Checklist: Campus Centrum

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Bed Capacity Dashboard |
| **Document type** | Go-live checklist |
| **Date** | 2023-09-08 |
| **Author** | Sofie Claes, Senior Data Engineer, Kestrel Consulting |
| **Go-live** | Monday 2023-09-11, 07:00, campus Centrum |
| **Go/no-go** | Friday 2023-09-08, 14:00, Jeroen Lambrecht and Lotte Willems |

## 1. Data and pipelines

| # | Check | Owner | Status |
|---|---|---|---|
| 1.1 | ADT file delivery every 15 minutes stable for 10 working days | Mediva IT | Done |
| 1.2 | Blocked bed status in 15-minute delivery | Mediva IT | Done |
| 1.3 | Event-driven Synapse pipeline in production workspace | SC | Done |
| 1.4 | Reconciliation with phone round on 3 consecutive days, campus Centrum | SC | Done, 41/41 wards matched on day 3 |
| 1.5 | Unmapped bed codes reviewed by bed management office | Bed office | Done, 7 remaining, flagged |
| 1.6 | Overflow beds flagged, shown only when occupied | SC | Done |
| 1.7 | Rebuild of last 72 hours tested after a missed file | SC | Done |

## 2. Reports

| # | Check | Owner | Status |
|---|---|---|---|
| 2.1 | Campus overview, ward drill-down and 24-hour outlook published to production workspace | EJ | Done |
| 2.2 | Changes from usability round 2 (timestamp, colours, local specialty codes, compact layout) | EJ, SC | Done |
| 2.3 | Power BI dataset refresh triggered by pipeline, failure keeps last good state | SC | Done |
| 2.4 | Report performance: ward drill-down under 3 seconds on a ward PC | EJ | Done, 1.8 s average |
| 2.5 | Printable A4 ward page | EJ | Not in this release, planned for later |

## 3. Access and security

| # | Check | Owner | Status |
|---|---|---|---|
| 3.1 | Access groups: bed managers and emergency, head nurses per campus, management | Mediva IT | Done |
| 3.2 | Test users of each group verified | EJ | Done |
| 3.3 | Development workspace not shared with end users | SC | Done |
| 3.4 | Confirmation that no patient-identifying fields are in the dataset | SC, Mediva IT | Done, checked by Jeroen's team on 2023-09-05 |

## 4. Operations

| # | Check | Owner | Status |
|---|---|---|---|
| 4.1 | Pipeline failure alert to Mediva IT service desk mailbox | SC | Done, tested 2023-09-06 |
| 4.2 | First-line support: service desk knows the escalation path to Kestrel | JL | Done |
| 4.3 | Hypercare: Sofie on site Monday and Tuesday morning | SC | Planned |
| 4.4 | Development resources paused outside office hours | SC | Done |

## 5. Users and communication

| # | Check | Owner | Status |
|---|---|---|---|
| 5.1 | 20-minute briefing for bed managers and head nurses, campus Centrum | EJ | Done, 3 sessions, 26 people |
| 5.2 | One-page quick guide on the intranet | EJ | Done |
| 5.3 | Announcement by nursing directorate: phone round stops on campus Centrum from 11 September | JL | Done |
| 5.4 | Fallback: if dashboard is unavailable for more than one hour, bed office returns to phone round | Bed office | Agreed |

## 6. Known limitations at go-live

- Events recorded late on the ward show up late; the update time per ward makes this visible.
- Seven bed codes remain unmapped and appear in a separate list for the bed office.
- The night shift has not been part of the briefing sessions. Elien plans a night visit in the second half of September.

## 7. Go/no-go decision

Decision on 2023-09-08, 14:20: **Go**, confirmed by Jeroen Lambrecht. Campus Oost follows on 2023-10-09 provided the test file of the hospital information system upgrade has been validated; campus Zuid on 2023-10-23.
