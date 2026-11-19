# Sprint Review Notes: Sprint 16

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Sprint review notes |
| **Date** | 2024-11-15 |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting (notes taken for Thomas Maes) |
| **Sprint** | 16 (2024-11-04 to 2024-11-15) |
| **Attendees** | Laura Vermeulen, two senior claims handlers, intake team lead, Thomas Maes, Jonas Peeters, Amira El Idrissi |

## 1. Demo: water damage severity sub-model v1

Delivered on 2024-11-08, on the CR-07 milestone date. Shown on 200 water damage claims from the second labelling round that the model had not seen.

- Sub-type (pipe leak, infiltration, flooding by heavy rain, other water damage) is correct for most claims. Infiltration and flooding are confused when the customer writes "water came in" without saying from where.
- Severity (contained, spreading, structural or health risk): "structural or health risk" is recognised in most cases. Mentions of mould and of electricity near water are the strongest signals. As agreed in CR-07, that level always goes to human triage.
- The plumber invoice and leak detection report models extract amount, date of intervention and the cause line ("cause / oorzaak / origine") reliably on typed documents. Handwritten invoices from one-person plumbing companies remain hard; fields are left empty when confidence is low.

Laura's reaction: good enough to include water damage in the pilot from Monday 2024-11-18. The handlers want the cause line shown at the top of the claim.

## 2. Pilot in proposal mode: first two weeks

The pilot started on 2024-11-04 as decided by the steering committee. Every incoming motor, fire and theft claim gets a proposal in the claims system; intake staff confirm or change it.

| Measure | Week 1 | Week 2 |
|---|---|---|
| Claims in scope processed | 1,420 | 1,690 |
| Share that would have been auto-routed | 39% | 35% |
| Override rate on reviewed proposals | 10% | 13% |
| Technical deferrals | 1.8% | 0.9% |

Week 2 volumes were higher after the storm of the previous weekend. The rise in overrides is concentrated in claims with storm-related damage: roof damage, fallen trees on cars, water coming in through a damaged roof. These claims are often classified as "other" or as fire (because of words like "damage to the roof structure"), and some urgent cases got U2.

Discussion:

- The senior handlers said storm claims "read differently": short texts typed on a phone, many photos and few documents, often a roofer's quote instead of a garage or plumber document.
- Amira pointed out that the historical extract contains storm claims, but most are coded under storm codes that we mapped to "other" in April, and the period had relatively mild autumns. The model has seen little of what is arriving now.
- Laura asked whether this is a bug. Amira: not a bug, but the model is meeting data that differs from its training data. We need to watch whether it continues after the storm weeks.

**Agreed:** Amira tracks the override rate daily and labels a sample of storm-period overrides with the senior handlers. If the override rate stays above 12% for two more weeks, she proposes a retraining in sprint 18.

## 3. Other items

- Jonas showed the priority lane for U1 keywords (load test action A3) and the parallel batches for the intake mailbox (A2). The repeated burst test on 2024-11-14 processed 3,000 claims with a 95th percentile of 6 minutes instead of 17.
- The monitoring dashboard now shows the override rate per type and per week. Team leads use it in their Monday meeting.
- The intake team lead reported that new colleagues trust the proposals too quickly. Laura will remind the team that confirming a proposal is a decision, not a click.

## 4. Sprint 17 plan

| Item | Owner |
|---|---|
| Water damage routing in the pilot from 2024-11-18 | JP |
| Cause line at the top of water damage claims | JP |
| Daily override tracking, labelling of storm overrides | AE with senior handlers |
| UAT interim report | TM |

*Amira El Idrissi*
