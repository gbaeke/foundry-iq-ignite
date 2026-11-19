# Go-live Checklist: Auto-routing in production

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Go-live / cutover checklist |
| **Date** | 2024-12-19 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Planned go-live** | Monday 2025-01-13, 07:00 |
| **Go/no-go** | 2025-01-09, Marc Dubois and Laura Vermeulen |

## 1. Context

The solution has been running in proposal mode on live intake since 2024-11-04. Go-live means switching on **auto-routing**: claims that pass all thresholds and hard rules of ADR-01 go directly to the queue without an intake employee confirming them. Everything else keeps going to the human triage queue as today.

Because of the Fortalis Christmas change freeze (2024-12-16 to 2025-01-06), no changes are made to production until 2025-01-07. The pilot keeps running unchanged during the holidays. This checklist was prepared now so that the first week of January is only verification and the switch itself.

## 2. Status of preconditions

| # | Precondition | Owner | Status |
|---|---|---|---|
| P1 | UAT signed off, water damage scenarios complete | LV | Done 2024-12-06; F7 accepted with workaround |
| P2 | Override rate analysis and corrective action | AE | Done, see analysis note of 2024-12-13 |
| P3 | Override rate after retraining back near acceptance level (about 9%) | AE | First week after retraining: 10%. To confirm on 2025-01-08 |
| P4 | Production quota for extraction raised | JP | Done |
| P5 | Priority lane for U1 keywords in production | JP | Done |
| P6 | Monitoring dashboard on production data, team lead access | JP | Done |
| P7 | Drift alert on weekly override rate above 12% | JP | Configured, test alert received by Laura |
| P8 | Run book v1.0 handed to Fortalis cloud team | JP | Draft; final version 2025-01-10 |
| P9 | Intake team briefed on what changes for them | LV | Planned 2025-01-08 and 2025-01-10 (two sessions for shifts) |
| P10 | Fallback procedure tested | JP | Done 2024-12-11 in acceptance |
| P11 | Claims system team on standby on go-live morning | Claims system team lead | Confirmed |

## 3. Cutover steps (2025-01-13)

| Time | Step | Who |
|---|---|---|
| 06:30 | Check overnight processing, no backlog in retry list | JP |
| 06:45 | Confirm model version in production equals the version approved on 2024-12-12 | AE |
| 07:00 | Change routing mode parameter from "proposal" to "auto" in the triage flow configuration | JP, approved by cloud team lead |
| 07:05 | Send three test claims (motor, theft, water damage) through the mailbox; check queue and audit trail | JP / AE |
| 07:30 | First real auto-routed claims checked by a senior handler | LV team |
| 09:00 | Go-live call: Laura, intake team lead, Thomas, Jonas, Amira | TM |
| 12:00 | Midday check: auto-routing rate, overrides, technical deferrals | AE |
| 16:30 | End of day review and decision to continue | LV / TM |

## 4. Fallback

If auto-routing causes wrong routing at a scale that the intake team cannot correct, the routing mode is switched back to "proposal" (one parameter change, takes effect within two minutes). Claims already auto-routed stay where they are; the intake team lead reviews them. Decision to fall back: Laura, or the intake team lead if Laura is not reachable.

## 5. First weeks after go-live

- Daily check of the dashboard by Amira in week 1 and 2, then twice a week.
- Thresholds unchanged for the first month; first review at the end of February.
- The auto-triage rate for the closing report is measured over the last six weeks before closure on 2025-02-28.
- First run of the monthly retraining procedure in the first week of February, with Fortalis IT running the pipeline and Amira watching.

## 6. Contacts during go-live week

Jonas on site 2025-01-13 and 2025-01-14. Amira and Thomas reachable by phone; Thomas on site 2025-01-13.

*Jonas Peeters*
