# Sprint Review Notes: Sprint 9

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Sprint review notes |
| **Date** | 2024-08-09 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Sprint** | 9 (2024-07-29 to 2024-08-09) |
| **Attendees** | Laura Vermeulen (remote, during her leave), two senior claims handlers, intake team lead, Amira El Idrissi, Jonas Peeters, Thomas Maes |

## 1. Demo

**Generic repair quote model (Amira).** Shown on 30 quotes from garages that were not in the top 20 layouts. Amount and garage name are found in most cases; VAT and labour hours less reliably. Because fields below the confidence threshold are left empty, the handlers see a blank rather than a wrong figure. The senior handlers prefer that.

**Triage flow with highlighted fields (Jonas).** A claim in the human triage queue now opens with the extracted fields highlighted in the original document. One of the handlers: "That alone saves me the zoom-in on bad scans." Overrides are stored with the original prediction, as designed in ADR-01.

**Triage model v1 on recent claims (Amira).** Run on 500 claims from June and July in the acceptance environment. Type is correct for most motor and theft claims; fire remains the weakest type. Urgency U1 is caught in most cases thanks to the asymmetric rule, at the cost of some false U1 flags.

## 2. Feedback from the claims team

- The reason for deferral ("low confidence on complexity") is useful but should be in plain language. Jonas will change the wording.
- The handlers want to see the second-best type only if it is close to the first. Agreed.
- The intake team lead asked whether duplicates could be merged automatically instead of flagged. Not now: merging touches the claims system data model. Added to the backlog for after go-live.

## 3. Question from Laura on water damage

Laura asked how hard it would be to include water damage claims. Context: water damage (leaking pipes, infiltration, flooding after heavy rain) is the fastest growing category at Fortalis and in the extract it represents most of the "other" group, which today always goes to people. She would like the triage to handle it "if it isn't much work".

Discussion in the room:

- Amira said the claim form is the same, so extraction largely works already. Plumber invoices and leak detection reports are new document types and would need their own extraction. Severity of water damage is a different question from the current complexity scale.
- Jonas said the routing and queues are configuration, so adding a water damage queue is easy on the orchestration side.
- The team agreed to "have a look" in sprint 10: collect a sample of plumber invoices and check how far the existing models get.

*Note added by Thomas after the review:* water damage is a new claim type and therefore outside the agreed scope (motor, fire and theft). Before the team spends real effort, this needs an impact analysis and, if Fortalis wants it, a change request approved by Marc. I will raise it with Laura when she is back on 2024-08-19.

## 4. Sprint 10 plan

| Item | Owner |
|---|---|
| Plain-language deferral reasons | JP |
| Show second-best type only when close | JP |
| Fire sub-type analysis | AE |
| Water damage sample: 50 plumber invoices, first extraction check | AE |
| Prepare connection to the write interface (expected in test week of 2024-08-19) | JP |

## 5. Next review

Friday 2024-08-23, 14:00, Fortalis office. Laura back in person.

*Thomas Maes*
