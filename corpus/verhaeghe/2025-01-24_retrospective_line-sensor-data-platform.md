# Project Retrospective: Line Sensor Data Platform

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Line Sensor Data Platform |
| **Date** | 2025-01-24 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Retrospective (internal, Kestrel and DataForge) |
| **Participants** | Sofie Claes, Jonas Peeters, Bram Visser (remote), Lotte Willems |

## 1. Format

One hour, "start, stop, continue", followed by a short timeline of the project. This is input for the closing report; final lessons learned will be written there.

## 2. Timeline as the team remembers it

- **June:** kickoff, workshop with quality, tag inventory of lines 1 and 2. Good energy.
- **July:** gateway ready, firewall request stuck in the change board and then the bouwverlof of the firewall partner.
- **August:** no live data. Platform built on HMI exports. "The longest month," according to Jonas.
- **September:** line 1 live on a temporary rule, subnet rule on 2024-09-20, lines 2 and 4 right after.
- **October:** batch-linking v1, data mapping for v2.
- **November:** lines 3, 5 and 6, platform phase accepted.
- **December:** acceptance test, first real drift caught on line 2.
- **January:** training and handover.

## 3. Continue

- Building the lakehouse on manual exports while waiting for live data. It saved the schedule.
- The gateway template. Lines 3, 5 and 6 took one weekend each, including testing.
- Weekly demos on site. Dries' team saw progress every Thursday and gave feedback on real batches.
- Bram working through Sofie as single point of contact. Clear for Verhaeghe, no confusion about who decides.
- Letting the quality team write the acceptance test cases from real questions.

## 4. Stop

- Treating network access as an assumption in the proposal. It was on the list, but nobody owned it with a date.
- Discovering tag meanings on the line during the inventory. Old PLC programmes need much more time.
- Sending alerts directly to shift leaders before testing. We did not do it here, but it was proposed in November and would have caused alert fatigue.

## 5. Start

- Ask for the OT-to-cloud network path, change procedure and responsible people in the pre-sales phase, and make it a precondition for the kickoff date.
- Check holiday periods of external partners (firewall maintainer, integrators) when planning the first two months.
- A data quality section in every status report, not only when something goes wrong.
- A one-page "how to add a line" guide from the start, not at the end.

## 6. Numbers

- Fixed price EUR 130,000; effort used at closing about 96%.
- Six production lines, about 1,400 tags.
- Pilot line live about five weeks later than planned; final handover on the planned date.
- 34 acceptance test cases, one open finding at the end, fixed in January.
- Monthly Azure and Fabric consumption at handover about EUR 1,150, paid by Verhaeghe.

## 7. Follow-up

Dries has mentioned image-based inspection on the packaging lines several times. Lotte will ask Ann whether she wants a separate proposal. If so, the network path for any new devices on the lines must be requested before the kickoff, using the procedure Tine wrote down in December.

## 8. Thanks

To Tine for pushing the firewall changes through, and to the maintenance technicians of lines 1 and 6, who spent more hours on the tag lists than anyone planned.
