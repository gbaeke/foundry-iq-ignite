# Status Report: Line Sensor Data Platform

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Line Sensor Data Platform |
| **Date** | 2024-07-19 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Status report (report no. 1) |
| **Reporting period** | 2024-06-03 to 2024-07-19 |
| **Distribution** | Ann Verhaeghe, Dries Callens, Tine Desmet, Lotte Willems |

## 1. Overall status

| Area | Status | Comment |
|---|---|---|
| Overall | Amber | Good progress on platform, connectivity waiting on firewall |
| Scope | Green | Unchanged |
| Schedule | Amber | Pilot line streaming by end of July is at risk |
| Budget | Green | About 14% of the fixed price used |
| Quality | Green | Tag inventory of lines 1 and 2 complete |

## 2. Progress this period

- **Kickoff** held on site on 2024-06-03.
- **Requirements workshop** with the quality team on 2024-06-14. Priorities: batch traceability first, then shift comparison, then drift alerts.
- **Tag inventory** done for line 1 (235 tags) and line 2 (212 tags).
- **Edge gateway line 1** installed and reading from the PLC. Data is buffered on the gateway.
- **Azure IoT Hub** and the **Microsoft Fabric** workspace are set up in Verhaeghe's tenant, with access groups agreed with Tine.
- **Lakehouse:** bronze tables are being built on manual HMI exports from line 1, so the design can be tested before live data arrives.
- **Databricks:** Bram set up the workspace and a first resampling notebook on the exported data.

## 3. Issues

I-01 (Fabric capacity not yet assigned to the workspace) and I-02 (guest account for Bram in Verhaeghe's tenant) were both resolved by Tine in June.

### I-03: Outbound traffic from OT network to Azure not yet allowed (open)

The line 1 gateway sits on the OT network. The firewall between OT and IT does not allow its outbound traffic yet. The change request was submitted by Tine on 2024-06-20 and discussed by Verhaeghe's change board on 2024-07-01, which asked for more detail on destinations. Jonas provided the details on 2024-07-03.

The external firewall partner is closed for the bouwverlof from 2024-07-15. As of today the change has not been implemented. Realistically, the pilot line will start streaming in the second half of August at the earliest.

## 4. Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-01 | Firewall change delays pilot line | High | High | Escalate via Tine; build lakehouse on exports in parallel |
| R-02 | Line teams unavailable during campaign | High | Medium | Book weekend windows two weeks ahead |
| R-03 | PLC documentation incomplete on older lines | Medium | Medium | Extra time in tag inventory for lines 5 and 6 |
| R-04 | Batch number link to sensor data harder than expected | Medium | High | Early sample of planning export, Bram to prototype |

## 5. Budget

About 14% of the fixed price used. Invoice 1 (30% at kickoff) sent on 2024-06-05 and paid.

## 6. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Get emergency slot or first date after the bouwverlof from firewall partner | TD | 2024-07-26 |
| 2 | ADR on resampling frequency | BV | 2024-08-02 |
| 3 | Silver layer design on exported data | SC | 2024-08-09 |
| 4 | Gateway configuration template for the other lines | JP | 2024-08-16 |
| 5 | Planning export sample, four weeks | DC | 2024-07-26 |

Next status report: 2024-08-16.
