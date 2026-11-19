# Summer Peak Review: July and August 2026

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Customs Document Extraction |
| **Date** | 2026-08-28 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Review notes (retrospective with the customs desk) |
| **Participants** | Jan Wouters, two senior customs agents, Amira El Idrissi, Pieter De Smet |

## 1. Why this review

Risk R-22 in the June report: summer peak volumes could grow the validation queue while Jan's team is at its smallest. This was the first summer with the pipeline in production. We looked back at July and August to decide what to change before the next peak around Christmas.

## 2. Figures

| Measure | June | July | August (to 27th) |
|---|---|---|---|
| Documents per week (average) | ~2,900 | ~3,400 | ~3,200 |
| Agents on duty (average per day shift) | 7 | 5 | 5 |
| Oldest item in queue at 12:00 (median) | 18 min | 41 min | 33 min |
| Days with queue older than 2 hours | 0 | 3 | 1 |
| Share of documents with zero corrections | 66% | 67% | 68% |

The three bad days in July were all Mondays after a weekend vessel peak, combined with a mailbox outage at a large forwarder that then sent 600 documents within an hour. The throttling settings from April held: no failed runs, but the queue was long.

Weighted accuracy over the 14 supported types stayed at about 94%. CMR accuracy improved after the handwriting rule went live on 2026-07-14.

## 3. What worked

- **Senior routing.** Documents with uncertain critical fields (HS code, gross weight, container number) went straight to the senior agent of the day. Juniors and temporary staff could validate the rest quickly. Jan: "without this, the summer would have been a disaster".
- **Source crop.** Temporary staff learnt the validation screen in half a day because they see the original next to each field.
- **No deployments in the quiet period.** The only deployment of the summer was on 2026-07-14. Nobody missed the others.
- **First-line monitoring by Scaldis IT.** Two mailbox permission issues were solved by first line using the runbook, without Kestrel.

## 4. What did not work

- **One senior agent per shift is a bottleneck.** On peak days the senior queue was longer than the general queue. Proposal: a second agent with the senior role during peak periods, chosen by Jan.
- **Priority is first-in, first-out.** Containers with a vessel departure or a truck appointment the same day should go first. The pipeline does not know about appointments or vessel schedules, because TOS integration is out of scope. Agents now sort manually.
- **New invoice layouts.** Two large shippers changed their invoice layout in July. Accuracy for those shippers dropped until the August retraining. The monthly cycle is a bit slow in peak months.

## 5. Agreed changes

| # | Change | Owner | Target |
|---|---|---|---|
| 1 | Second senior role during peaks | JW | Before Christmas peak |
| 2 | Agents can mark a container "urgent"; workflow moves its documents to the top of the queue | PDS | Sprint 25 |
| 3 | Fast-track retraining when a top-20 shipper's layout changes (within a week instead of monthly) | AE | From September |
| 4 | Christmas planning: deployment freeze 2026-12-21 to 2027-01-01, peak staffing plan by Jan | JW, PDS | Plan by 2026-11-13 |
| 5 | Ask for a TOS-based priority feed in a later phase, with its own security review | JW, KV | Phase 2 discussion |

## 6. Budget and continuation

The Q3 continuation was signed by Koen Verstraete at the end of June, so R-24 is closed. The Q4 proposal will build on this review and on the phase 2 workshop planned for September.

## 7. Thanks

Thanks to the summer team at the customs desk, including the temporary agents, who validated more documents in July than the full team keyed in any month of 2025.

Pieter De Smet
