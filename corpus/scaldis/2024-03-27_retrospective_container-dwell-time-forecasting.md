# Project Retrospective: Container Dwell-Time Forecasting

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Container Dwell-Time Forecasting |
| **Date** | 2024-03-27 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Document type** | Retrospective (internal team) |
| **Participants** | Thomas Maes, Sofie Claes, Amira El Idrissi, Bram Visser (DataForge, online) |

## Format

One hour, online, the classic three columns plus a short "what would we tell the next team" round. Input for the closing report of 2024-03-29. Everyone added notes beforehand; the session was used to group and discuss them.

## 1. What went well

- **Planners in the loop.** The Friday demos at the terminal and the case review on 19 January were mentioned by everyone. The forecast range came straight from those sessions and is now the column planners use most.
- **Point-in-time feature snapshots.** Training and scoring use exactly the same snapshot code. No surprises when we moved to production. Bram: "the boring design was the right one".
- **Raw stays raw.** Keeping all corrections in the curated layer with rule IDs made the gate-in discussion factual. Nathalie and the TOS administrator could see what each rule did.
- **Subcontracting.** Bram's work through DataForge was smooth: one contract on Kestrel's side, clear deliverables, same working rhythm as the rest of the team.
- **Result.** MAPE 11.8% on the hold-out against a 15% target, and planners who trust the list.

## 2. What could be better

- **TOS vendor contact.** We never had a direct technical contact at the TOS vendor. Both the gate-in issue and the schema change came to us second hand. It cost about two weeks in Q4 and a lot of mail. Sofie: "we spent more time asking who knows than fixing".
- **Data quality buffer.** The proposal reserved time for data quality findings, but not enough. The gate-in rules pushed the feature pipeline milestone by two weeks.
- **Transhipment.** Never really scoped. We discovered late that customs-release events for transhipment arrive too late to be useful. It is now a known limitation (MAPE around 16% on that segment).
- **Holidays.** Autumn holiday, Christmas freeze and the planners' leave were each handled when they came up. They should have been in the plan from day one.
- **Effort.** Internal effort ended about 4% above plan, mostly data quality work. Absorbed by Kestrel under the fixed price.

## 3. Puzzles

- Was reconstructing missing gate-ins worth it, given they are only about 2% of visits? Consensus: yes, because those visits are mostly gate outages on busy days, which are exactly the days planners care about.
- Should we have pushed for an intraday refresh? Amira's ADR-03 argument still holds: without an event feed from the TOS it would have been fragile.

## 4. What we would tell the next team

1. Ask for a direct technical contact at the vendor of any operational system we depend on, during discovery, and write it into the assumptions.
2. Plan holiday freezes and leave periods in the first planning, with the customer's calendar in hand.
3. Scope edge segments (here: transhipment) explicitly, even if only to exclude them.
4. Bring a reconciliation check against a report the business already trusts. It caught the missing export on 26 December before anyone noticed.
5. Write the data contract early and keep it alive; it was the backbone of the handover.

## 5. Actions

| Action | Owner |
|---|---|
| Put lessons 1 to 3 in the closing report | TM |
| Share the data contract template on the Kestrel intranet | SC |
| Share the retraining guide structure as a template | AE |
| Feedback to DataForge on the collaboration | TM |

Thanks all. Good project, good team.

Thomas
