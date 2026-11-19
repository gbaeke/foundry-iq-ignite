# Status Report: Line Sensor Data Platform

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Line Sensor Data Platform |
| **Date** | 2024-10-11 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Status report (report no. 4) |
| **Reporting period** | 2024-09-13 to 2024-10-11 |
| **Distribution** | Ann Verhaeghe, Dries Callens, Tine Desmet, Lotte Willems |

## 1. Overall status

| Area | Status | Comment |
|---|---|---|
| Overall | Amber | Connectivity work behind plan, recovery under way |
| Scope | Green | No changes to scope |
| Schedule | Amber | Sensor connectivity delayed by 5 weeks |
| Budget | Green | Within fixed price, delay absorbed so far |
| Quality | Green | Data from connected lines is complete and consistent |

## 2. Progress this period

- **Lines connected:** 3 production lines are now streaming to Azure IoT Hub (lines 1, 2 and 4). Line 1 has been live since the start of September, lines 2 and 4 went live in the past two weeks.
- **Fabric lakehouse:** bronze and silver layers are running for the connected lines. Sensor data is resampled to 10-second intervals.
- **Databricks:** Bram has built the first version of the batch-linking job, which matches freezer tunnel readings to batch numbers from the production planning export. First results reviewed with Dries on 2024-10-08.
- **Edge gateways:** Jonas has standardised the gateway configuration, so connecting the remaining lines should mainly be repeat work.

## 3. Issues

### I-03: OT/IT firewall blocked sensor connectivity (resolved)

The line gateways sit on the OT network of the plant. The firewall between the OT and IT networks did not allow outbound traffic from the gateways to Azure IoT Hub, and the change had to go through Verhaeghe's internal change procedure and the external firewall maintainer. This delayed sensor connectivity by **5 weeks** compared to plan.

Tine Desmet arranged the firewall change: a dedicated rule for the gateway subnet, outbound only over the IoT Hub endpoints, with logging enabled. The rule has been active since 2024-09-20. Thanks to Tine for pushing this through the "wijzigingsaanvraag" process faster than usual.

Impact: the pilot line started streaming about five weeks late. Lines 2 and 4 followed quickly once the rule was in place.

## 4. Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-05 | Remaining lines need further firewall changes (other VLANs) | Medium | High | Tine to check VLAN layout for lines 3, 5 and 6 this month |
| R-06 | Harvest season limits access to lines for gateway installation | High | Medium | Schedule installs in weekend maintenance windows |
| R-07 | Batch numbers in the planning export are sometimes entered late | Medium | Medium | Dries to check with planning; fallback matching on time window |

## 5. Budget

Effort used is about 48% of the fixed price, against 50% of the planned elapsed time. The delay has not led to extra cost so far, because the team worked on the lakehouse in parallel.

## 6. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Confirm VLAN and firewall layout for lines 3, 5 and 6 | TD | 2024-10-25 |
| 2 | Install gateways on lines 3 and 5 during weekend window | JP | 2024-11-09 |
| 3 | Gold layer design for batch quality report, review with quality team | SC / DC | 2024-11-08 |
| 4 | Batch-linking job v2 with fallback on time window | BV | 2024-11-15 |
| 5 | Update planning baseline and share with Ann | SC | 2024-10-18 |

Next steering meeting: 2024-11-08 in Roeselare.
