# Status Report: Line Sensor Data Platform

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Line Sensor Data Platform |
| **Date** | 2024-08-16 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Status report (report no. 2) |
| **Reporting period** | 2024-07-19 to 2024-08-16 |
| **Distribution** | Ann Verhaeghe, Dries Callens, Tine Desmet, Lotte Willems |

## 1. Overall status

| Area | Status | Comment |
|---|---|---|
| Overall | Amber | Platform on track, no live data yet |
| Scope | Green | Unchanged |
| Schedule | Red | Pilot line not streaming; end-of-July milestone missed |
| Budget | Green | About 26% used |
| Quality | Green | Silver layer design validated on exports |

## 2. Progress this period

- **ADR-02** accepted: resampling to 10-second intervals with min, max and mean in the silver layer.
- **Silver layer** built and tested on two weeks of HMI exports from line 1.
- **Gateway template:** Jonas finished a standard gateway configuration (tag mapping file, buffering, device identity per gateway). The same template will be used on all lines.
- **Tag inventory line 4** completed with maintenance (204 tags) during a weekend stop on 2024-08-10.
- **Planning export:** Dries delivered four weeks of the production planning export. Bram started analysing how batch start and end times relate to the freezer data.

## 3. Issues

### I-03: Outbound traffic from OT network to Azure not yet allowed (open, escalated)

The firewall change for the line 1 gateway was not implemented before the bouwverlof of the external firewall partner. After their return on 2024-08-05, the partner asked for a broader design: instead of one host rule per gateway, a dedicated rule for a gateway subnet, with logging, so the other lines do not need separate changes later. Tine agrees this is better, but it needs a new pass through the change board.

Tine has asked the partner for a temporary rule for the line 1 gateway only, so the pilot can start while the subnet rule is prepared. Expected in the first week of September.

Impact: the pilot line is now about four weeks behind the end-of-July target. Sofie discussed this with Ann on 2024-08-12. Ann asked to keep the final date of 2025-01-31 and accepted that the rollout of the remaining lines will be compressed.

## 4. Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-01 | Firewall change delays pilot line | Occurred | High | Temporary rule for line 1; subnet rule in parallel |
| R-02 | Line teams unavailable during campaign | High | Medium | Weekend windows, booked with shift leaders |
| R-03 | PLC documentation incomplete on older lines | Medium | Medium | Extra time for lines 5 and 6 |
| R-04 | Batch link harder than expected | Medium | High | Bram prototyping on export sample |

## 5. Budget

About 26% of the fixed price used. The team kept working on the platform with exported data, so the delay has not cost extra effort so far. If live data comes later than mid-September, we will need to re-plan the rollout.

## 6. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Temporary firewall rule for line 1 gateway | TD | 2024-09-06 |
| 2 | Subnet rule to change board | TD | 2024-09-09 |
| 3 | Batch-linking prototype on export sample | BV | 2024-09-13 |
| 4 | Install gateways for lines 2 and 4 (ready to go live when the rule is in place) | JP | 2024-09-13 |
| 5 | Re-planned rollout schedule | SC | 2024-09-13 |

Next status report: 2024-09-13.
