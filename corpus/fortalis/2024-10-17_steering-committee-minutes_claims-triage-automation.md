# Steering Committee Minutes: Claims Triage Automation

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Steering committee minutes |
| **Date** | 2024-10-17 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Attendees** | Marc Dubois (chair), Laura Vermeulen, Thomas Maes, Amira El Idrissi (item 3), Jonas Peeters (items 4 and 5) |

## 1. Status and budget

Thomas presented the status. Overall amber, as in the September report, only because of the budget: the baseline is now **EUR 276,000** after CR-07, and the forecast is on that baseline. The CR-07 effort is tracked separately in the timesheets as Marc requested; spent so far on CR-07: about 40% of the EUR 36,000, in line with plan. No other change requests with cost impact. The scope freeze after CR-07 holds: three new requests from the claims team since September went to the post-go-live backlog (automatic merging of duplicates, triage of phone reports, a weekly e-mail summary for team leads).

Marc asked whether the original EUR 240,000 part is still on budget on its own. Thomas: yes, with a small buffer left for UAT.

## 2. Planning

| Item | Date |
|---|---|
| Integration tests with the claims system | started 2024-10-07, end 2024-11-01 |
| Load test with claims system team | 2024-10-23 |
| Pilot on live intake (proposal mode) | from 2024-11-04 |
| UAT closure | 2024-12-06 |
| Christmas change freeze at Fortalis | 2024-12-16 to 2025-01-06 |
| Go-live (auto-routing on) | proposed 2025-01-13 |
| Project closure | 2025-02-28 |

**Decision:** the committee approves the pilot in proposal mode from 2024-11-04. During the pilot, the solution processes every incoming claim and writes its proposal (type, complexity, urgency, queue) to the claims system; intake staff confirm or change it before routing. This gives real override figures before auto-routing is switched on.

**Decision:** go-live date 2025-01-13, subject to UAT sign-off by Laura.

## 3. Model quality (Amira)

- Triage model v2 on the hold-out set for motor, fire and theft: about four in ten claims pass all thresholds of ADR-01 and would be auto-routed; on those, the type is correct in nearly all cases.
- In the October UAT sessions with the senior handlers, the handlers overrode the proposed classification in about 9% of the claims they reviewed. Laura considers this acceptable for go-live.
- Water damage: plumber invoice extraction model delivered on 2024-10-15, ahead of the 2024-10-18 milestone. The second labelling round for water damage is at 1,100 claims; the severity sub-model v1 is planned for 2024-11-08.

Marc asked what happens when claim patterns change, for example after a storm. Amira explained that the override rate is the best early signal and will be visible on the monitoring dashboard. A retraining procedure is foreseen in the run book; how often to retrain will be decided based on the pilot.

## 4. Monitoring dashboard (Jonas)

Content agreed with Laura: daily volumes per channel, share auto-routed vs human triage, deferral reasons, override rate per type, queue waiting times. Team leads get read access. First version available at the start of the pilot.

## 5. Operations after go-live

- The Fortalis cloud team takes over platform operations; Jonas prepares the run book and two handover sessions in January.
- Model ownership after closure: Laura's team decides on promotions, Fortalis IT runs the pipelines. To be detailed in the run book.
- Marc wants a short support arrangement after closure. Thomas will propose one with Lotte Willems before the next committee.

## 6. Action items

| Action | Owner | Due |
|---|---|---|
| Start pilot in proposal mode | JP / LV | 2024-11-04 |
| Dashboard v1 live | JP | 2024-11-04 |
| Severity sub-model v1 | AE | 2024-11-08 |
| Support proposal after closure | TM | 2024-12-13 |
| Next steering committee | MD / TM | 2024-12-12 |

*Thomas Maes*
