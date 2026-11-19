# Steering Committee Minutes: Line Sensor Data Platform

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Line Sensor Data Platform |
| **Date** | 2024-11-08, 14:00 to 15:30 |
| **Location** | Verhaeghe Foods, Roeselare |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Steering committee minutes |

## Attendees

Ann Verhaeghe (sponsor), Dries Callens (product owner), Tine Desmet (IT), Lotte Willems (Kestrel), Sofie Claes (Kestrel), Jonas Peeters (Kestrel)

## 1. Status

Sofie summarised status report no. 4 and the weeks since:

- Lines 1, 2 and 4 stream to Azure IoT Hub. Data has been complete since the subnet rule went live on 2024-09-20.
- Gateways for lines 3 and 5 will be installed tomorrow, Saturday 2024-11-09, during the weekend stop.
- The lakehouse in Microsoft Fabric has bronze, silver and a first gold table for batch windows.
- Batch-linking v2 with fallback on packaging counters and shift is in test, go-live planned 2024-11-15.

Overall status amber, improving. The five-week connectivity delay of the summer has been mostly recovered by working on the platform in parallel and by Jonas' standard gateway template.

## 2. Network for lines 3, 5 and 6

Tine reported on the VLAN check. Lines 3 and 5 sit in a segment already covered by the subnet rule. Line 6 is on an older, separate VLAN and needs one additional rule. Tine filed it in October and the change board approved it on 2024-11-05; the firewall partner will implement it on 2024-11-22. Line 6 installation is planned for Saturday 2024-11-30.

Ann asked why this was so much faster than in the summer. Tine: the board now knows the pattern, and the partner is not on holiday. Ann asked Tine to write down the procedure so that future projects can start with it.

## 3. Gold layer and reports

Dries presented the draft batch quality report with his team's feedback:

- They want the paper log number next to the batch number for the first season, to build trust.
- Shift comparison should show energy per tonne and reject rate side by side.
- Grey marking for batches linked by shift fallback is fine, as long as there are few.

Decision: the gold layer design is accepted. The platform phase milestone (40% invoice) will be signed once lines 3 and 5 are live and the v2 job runs, expected end of November.

## 4. Budget

About 58% of the fixed price used, against about 63% of elapsed time. Lotte confirmed no change request is needed. The extra rule for line 6 has no cost impact for Kestrel.

## 5. Alerts

Dries wants the first alert rules before Christmas, as the leek and sprout season brings more restarts. Agreed scope: eight rules (blancher water temperature low/high per line type, freezer tunnel exit temperature high, frozen core probe, gateway offline). Sofie warned that rules must be tested on live data for at least two weeks before the quality team relies on them.

## 6. Christmas period

Tine reminded everyone of the IT change freeze from 2024-12-20 to 2025-01-06. No deployments to the platform in that period except urgent fixes, approved by Tine.

## Decisions

1. Gold layer design accepted.
2. Eight alert rules in scope, live before the change freeze.
3. Line 6 installation on 2024-11-30.

## Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Install gateways lines 3 and 5 | JP | 2024-11-09 |
| 2 | Line 6 rule implemented | TD | 2024-11-22 |
| 3 | Write down OT-to-cloud network procedure | TD | 2024-12-13 |
| 4 | Alert rules in test | SC | 2024-12-02 |
| 5 | Add paper log number to batch report | SC / BV | 2024-11-22 |

Next steering meeting: 2025-01-29 (acceptance).
