# Operations Runbook: Line Sensor Data Platform

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Line Sensor Data Platform |
| **Date** | 2025-01-10 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Document type** | Runbook (version 0.9, draft for handover) |
| **Intended owner** | Tine Desmet, IT Coordinator, Verhaeghe Foods |

## 1. Components

| Component | Where | Purpose |
|---|---|---|
| Edge gateways (6) | electrical cabinet of each line, OT network | read PLC tags, buffer up to seven days, send telemetry |
| Azure IoT Hub | Verhaeghe Azure subscription | receive telemetry, one device identity per gateway |
| Microsoft Fabric lakehouse | Verhaeghe Fabric workspace | bronze, silver and gold tables |
| Databricks jobs | Verhaeghe Databricks workspace | resampling (every 15 min), batch linking (nightly), alert tables (every 5 min) |
| Reports and alerts | Fabric workspace | batch quality report, shift report, eight alert rules |

## 2. Daily checks (5 minutes)

1. Open the "platform health" page in the Fabric workspace. All six lines should show data from the last 15 minutes.
2. Check the Databricks job history: resampling and alert jobs green, nightly batch linking green.
3. Check the share of batches linked by shift fallback for yesterday. Above 5% usually means the planning export was late.

## 3. Common incidents

### Gateway offline

Symptom: "gateway offline" alert, or a line missing on the health page.

1. Check the maintenance calendar. Planned stops suppress the alert, but a stop added late may not be in the calendar.
2. Check the gateway in IoT Hub: last activity time.
3. Ask maintenance to check power and network cable in the cabinet. The status LED should be green.
4. If the gateway is up but cannot connect, check the firewall log for denied traffic from the gateway subnet. Contact the firewall partner through the standard change channel if a rule was changed.
5. The gateway buffers up to seven days. Once it reconnects, the resampling job picks up late data automatically for the last 48 hours. For outages longer than 48 hours, run the resampling job manually with the `reprocess_from` parameter.

### Planning export missing

Symptom: no new batches in the batch quality report in the morning.

1. Check the file drop for the daily export (05:30).
2. If missing, contact planning. Once the file arrives, start the batch-linking job manually.

### Alert floods

If a rule sends more than 10 alerts per hour, the shift leaders will stop reading them. Pause the rule in the alert configuration table and inform Dries. Do not change thresholds without the quality team.

## 4. Access management

- Access is granted through four groups: platform admins (Tine and one deputy), data engineers, report readers (quality and production), alert recipients.
- Kestrel and DataForge accounts are guest accounts and will be removed on 2025-02-28, at the end of the warranty period.
- Device keys of the gateways are rotated once a year. Next rotation: November 2025. Procedure in annex B.

## 5. Changes and freezes

- Changes to firewall rules follow Verhaeghe's wijzigingsaanvraag process. The procedure written by Tine in December is in annex C.
- Respect the IT change freeze around Christmas and avoid changes on the lines during the main harvest weeks.

## 6. Adding a new line or tag

1. Tag inventory with maintenance, update the tag inventory sheet.
2. Copy the gateway template, adjust the tag mapping file.
3. Register a new device identity in IoT Hub.
4. Check that the gateway sits in the covered subnet. If not, request a firewall change first.
5. Add the tags to the silver configuration; the resampling job picks them up on the next run.

## 7. Contacts during warranty (until 2025-02-28)

Sofie Claes for data and reports, Jonas Peeters for gateways and platform.
