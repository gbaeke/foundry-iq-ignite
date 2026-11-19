# Closing Report: Line Sensor Data Platform

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Line Sensor Data Platform |
| **Date** | 2025-01-31 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Closing report |
| **Status** | Completed |

## 1. Summary

The Line Sensor Data Platform has been delivered and handed over to Verhaeghe Foods. **6 production lines** are now connected and stream sensor data to a central platform. Dries Callens' quality team uses the batch quality reports daily, and the platform is in production under Verhaeghe's own operations.

The project was delivered within the fixed price. The schedule ended on the planned date of 2025-01-31, although the connectivity work in the autumn was behind plan for several weeks.

## 2. Delivered scope

| Deliverable | Status |
|---|---|
| Edge gateways and telemetry for 6 production lines | Delivered |
| Ingestion via Azure IoT Hub | Delivered |
| Fabric lakehouse (bronze, silver, gold) | Delivered |
| Databricks jobs for resampling and batch linking | Delivered |
| Batch quality report and shift report | Delivered |
| Alert rules for blancher and freezer tunnel ranges | Delivered (8 rules) |
| Operations runbook and handover sessions | Delivered |

## 3. Results

- 6 production lines connected, about 1,400 sensor tags in total.
- Freezing temperature per batch can now be traced in minutes instead of half a day of searching through paper logs.
- Two blancher drift events were caught by the alert rules in December, before they affected product.
- History of all connected lines is kept in the lakehouse and can be used for the coming seasons.

## 4. What went well

- Close cooperation with Dries and the quality team. Weekly demo sessions on site kept the reports close to how the team actually works.
- Jonas' standard gateway setup made the rollout to lines 3, 5 and 6 a repeat exercise.
- Bram's batch-linking job with fallback on time window solved the problem of late batch entries in the planning export.

## 5. What could have gone better

- Network access from the OT side to Azure was not arranged before the project started. The firewall change, eventually arranged by Tine Desmet, cost us several weeks in the first months.
- The tag inventory took longer than planned on the oldest line, because documentation of the PLC programmes was incomplete.

## 6. Lessons learned

1. **Arrange OT access before kickoff.** For any project that needs data from the plant floor, the network path from OT to cloud (firewall rules, change procedure, responsible people) must be agreed and ideally in place before the kickoff date. We will add this as an explicit precondition in future proposals.
2. Plan on-site work around the harvest season, not during it.
3. Ask for PLC tag lists early, and budget extra time for older lines.

## 7. Handover and ownership

| Item | Owner at Verhaeghe |
|---|---|
| Platform operations and access management | Tine Desmet, IT Coordinator |
| Reports and alert thresholds | Dries Callens, Quality Manager |
| Sponsor sign-off | Ann Verhaeghe, CEO |

Final acceptance was signed by Ann on 2025-01-29. Warranty period of one month: issues can be reported to Sofie until 2025-02-28.

## 8. Follow-up

Dries has asked about image-based quality inspection on the packaging lines, using the platform as a foundation. A separate proposal will follow.

*Sofie Claes, on behalf of the Kestrel project team (Sofie, Jonas, Bram)*
