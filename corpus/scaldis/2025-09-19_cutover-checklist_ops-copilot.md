# Cutover and Go-live Checklist

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Scaldis Ops Copilot |
| **Date** | 2025-09-19 |
| **Author** | Ruben Wouters, Junior Developer, Kestrel Consulting |
| **Document type** | Cutover checklist |
| **Go-live** | Monday 2025-09-22, 06:00 (start of early shift) |
| **Go/no-go call** | Friday 2025-09-19, 15:00 (Koen Verstraete, Nathalie Dumont, Wim Goossens, Pieter De Smet, Thomas Maes) |

## 1. Pre-conditions

| # | Item | Owner | Status |
|---|---|---|---|
| 1 | Re-test of restricted customs folders signed off | Wim Goossens | Done 2025-09-17 |
| 2 | No open high or medium security findings | Wim Goossens | Done |
| 3 | UAT signed | Nathalie Dumont | Done 2025-08-28 |
| 4 | Teams app review by Scaldis IT | Scaldis IT | Done 2025-09-03 |
| 5 | Production index complete with permissions, ~2,100 documents | Pieter De Smet | Done 2025-09-18 |
| 6 | Load test on final build | Ruben Wouters | Done 2025-09-05 |
| 7 | Champion training | Elien Jacobs | Done, week of 1 September |
| 8 | Quick reference cards printed | Nathalie Dumont | Done |
| 9 | Content owners informed of the group change procedure | Nathalie Dumont | Done 2025-09-11 |

## 2. Friday 19 September

| Time | Step | Owner |
|---|---|---|
| 12:00 | Freeze on index configuration and prompt; only content updates via normal sync | PDS |
| 13:00 | Final run of regression set (120 + D cases) and adversarial set; results to the call | PDS |
| 14:00 | Permission matrix automated test on production index | RW |
| 15:00 | Go/no-go call | TM |
| 16:00 | If go: prepare Teams app permission policy for the first wave (about 340 users) in staged mode | Scaldis IT, RW |

## 3. Weekend

- No changes to SharePoint groups on operations and restricted sites (agreed with site owners).
- Hourly permission sync and nightly reconciliation continue; Ruben checks the sync report on Saturday and Sunday at 18:00.
- On-call: Pieter (architecture), Ruben (bot), Scaldis IT on-call (Teams and identity).

## 4. Monday 22 September

| Time | Step | Owner |
|---|---|---|
| 05:00 | Assign app policy to the first wave; pin the app | Scaldis IT |
| 05:30 | Smoke test with three test accounts (gate clerk, shift leader, customs desk) in NL, FR, EN | RW |
| 05:45 | Check that a restricted customs question returns an answer only for the customs test account | RW |
| 06:00 | Go-live; champions start the 10-minute shift briefings | Champions |
| 06:00–09:00 | Kestrel team on site in the planning office for questions | EJ, RW |
| 10:00 | First check of feedback and errors | PDS |
| 14:00, 22:00 | Briefings for late and night shift | Champions |
| 17:00 | Day-1 call with Nathalie | TM |

## 5. Rollback

The copilot has no dependency for terminal operations; rollback means removing the app from the policy. Criteria for rollback, decided by Nathalie and Wim:
- any confirmed answer based on a document the user may not open;
- error rate above 10% for more than one hour.

In case of a suspected permission leak: emergency full re-sync (about 22 minutes), and the bot shows a maintenance message in the meantime.

## 6. Known open items at go-live

| Item | Owner | Plan |
|---|---|---|
| Personal sign-in on all shared PCs | Scaldis IT | Gate building done; other shared PCs in October |
| Older French SOP versions still in some libraries | Content owners | Archive during hypercare |
| L-05/L-06 (forwarding, watermark) | Accepted risk | Covered in training |

## 7. Hypercare

From 2025-09-22 to 2025-10-17. Daily feedback check (Pieter, Ruben), weekly quality report to Nathalie's team, weekly call with Wim on the sync reports.

Ruben Wouters
