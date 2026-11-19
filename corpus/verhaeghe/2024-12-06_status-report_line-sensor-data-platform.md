# Status Report: Line Sensor Data Platform

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Line Sensor Data Platform |
| **Date** | 2024-12-06 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Status report (report no. 6) |
| **Reporting period** | 2024-11-08 to 2024-12-06 |
| **Distribution** | Ann Verhaeghe, Dries Callens, Tine Desmet, Lotte Willems |

## 1. Overall status

| Area | Status | Comment |
|---|---|---|
| Overall | Green | All lines connected |
| Scope | Green | Unchanged |
| Schedule | Green | Back on track for 2025-01-31 |
| Budget | Green | About 72% used |
| Quality | Amber | Line 6 tag meanings still being confirmed |

## 2. Progress this period

- **All six production lines are connected.** Lines 3 and 5 went live on 2024-11-09, line 6 on 2024-11-30 after the extra firewall rule was implemented on 2024-11-22.
- **Tag count:** about 1,400 tags across the six lines.
- **Batch-linking v2** is live since 2024-11-15. Over the last two weeks: 87% linked via planning, 11% via packaging counters, 2% via shift fallback.
- **Batch quality report** now shows the paper log number, as asked at the steering meeting.
- **Platform phase accepted** by Dries and Ann on 2024-11-29. Invoice 2 (40%) sent.
- **Alert rules:** the eight rules are in test since 2024-12-02 and send mails to the quality team mailbox only. They will be switched to the shift leaders after two weeks of testing.

## 3. Issues

### I-05: Tag inventory line 6 (open)

Line 6 is the oldest line. The PLC programme has been changed many times and the documentation is incomplete. Of 268 tags, 31 still have an unclear meaning. The maintenance technician and Jonas go through them on the HMI screens. Until then, these tags land in bronze but are not used in silver.

### I-06: Line 4 time zone (resolved)

The planning export for line 4 used local time without daylight saving offset. After the switch on 2024-10-27 we saw a one-hour shift in batch windows. Planning fixed the export on 2024-11-12. The mapping correction in the batch-linking job was removed.

## 4. Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-03 | Incomplete PLC documentation (line 6) | Occurred | Low | Tag review with maintenance |
| R-08 | Alert fatigue for shift leaders | Medium | Medium | Two weeks test with quality team first, tune thresholds |
| R-09 | Change freeze limits fixes in late December | Medium | Low | All deployments before 2024-12-20 |
| R-10 | Handover too late in January for training | Low | Medium | Book training dates now |

## 5. Christmas planning

- Change freeze from 2024-12-20 to 2025-01-06.
- The plant runs reduced production between Christmas and New Year. The gateways and jobs keep running; Jonas is on call for urgent issues on 2024-12-23, 2024-12-27 and 2024-12-30.
- Sofie and Bram are off from 2024-12-23 to 2025-01-03.

## 6. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Acceptance test of reports and alerts with quality team | SC / DC | 2024-12-13 |
| 2 | Clear the 31 unclear tags on line 6 | JP | 2024-12-18 |
| 3 | Operations runbook draft | JP | 2025-01-10 |
| 4 | Training sessions for quality team and IT | SC | 2025-01-17 |
| 5 | Switch alerts to shift leaders | SC | 2024-12-18 |

Next status report: 2025-01-10.
