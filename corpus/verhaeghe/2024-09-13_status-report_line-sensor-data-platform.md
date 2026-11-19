# Status Report: Line Sensor Data Platform

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Line Sensor Data Platform |
| **Date** | 2024-09-13 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Status report (report no. 3) |
| **Reporting period** | 2024-08-16 to 2024-09-13 |
| **Distribution** | Ann Verhaeghe, Dries Callens, Tine Desmet, Lotte Willems |

## 1. Overall status

| Area | Status | Comment |
|---|---|---|
| Overall | Amber | First live data, rollout re-planned |
| Scope | Green | Unchanged |
| Schedule | Amber | Pilot line live about five weeks late |
| Budget | Green | About 37% used |
| Quality | Green | Live data matches HMI values |

## 2. Progress this period

- **Line 1 is streaming.** The temporary firewall rule for the line 1 gateway was implemented on 2024-09-03 and the gateway connected to Azure IoT Hub the same afternoon. The buffered data from the last weeks was not kept: the gateway buffer covers seven days only.
- **Validation:** Jonas and the line 1 maintenance technician compared 30 tags between the HMI and the lakehouse over two shifts. All values matched; two tags had a wrong unit in the tag inventory (°F label on a °C value) and were corrected.
- **Resampling job** now runs every 15 minutes in Databricks on live data and reprocesses the last 48 hours, as agreed in ADR-02.
- **Gateways for lines 2 and 4** are installed and tested on site. They are waiting for the definitive subnet rule.
- **Batch link:** Bram's prototype matches about 85% of batches in the export sample to a freezer window. The rest have batch numbers entered after the batch has finished.

## 3. Issues

### I-03: Outbound traffic from OT network to Azure (partly resolved)

The temporary rule covers the line 1 gateway only. The definitive change, a dedicated rule for the gateway subnet, outbound only to the IoT Hub endpoints and with logging, was approved by the change board on 2024-09-10. Tine has booked the firewall partner to implement it on 2024-09-20. The temporary rule will be removed at the same time.

Compared to the plan (pilot line streaming at the end of July), line 1 went live about five weeks late.

## 4. Re-planned rollout

| Line | Gateway installed | Expected live |
|---|---|---|
| 1 | July | live since 2024-09-03 |
| 2 | September | week after 2024-09-20 |
| 4 | September | week after 2024-09-20 |
| 3 | November (weekend window) | depends on VLAN check |
| 5 | November (weekend window) | depends on VLAN check |
| 6 | late November | depends on VLAN check |

Lines 3, 5 and 6 sit in other parts of the OT network. Tine will check whether the subnet rule covers them or whether more changes are needed.

## 5. Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-03 | PLC documentation incomplete on older lines | Medium | Medium | Extra time for lines 5 and 6 |
| R-05 | Lines 3, 5 and 6 need more firewall changes | Medium | High | VLAN check by Tine |
| R-06 | Harvest season limits access to lines for gateway installation | High | Medium | Weekend maintenance windows |
| R-07 | Batch numbers in the planning export are sometimes entered late | Medium | Medium | Fallback matching on time window |

## 6. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Subnet rule implemented, temporary rule removed | TD | 2024-09-20 |
| 2 | Lines 2 and 4 live | JP | 2024-09-27 |
| 3 | First batch-linking job on live line 1 data | BV | 2024-10-04 |
| 4 | Weekly demo on site, from 2024-09-19 | SC | ongoing |

Next status report: 2024-10-11.
