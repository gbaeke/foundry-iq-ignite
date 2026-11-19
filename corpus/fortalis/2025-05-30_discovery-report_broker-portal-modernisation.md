# Discovery Report: Broker Portal Modernisation

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Broker Portal Modernisation |
| **Document type** | Discovery report |
| **Date** | 2025-05-30 |
| **Author** | Elien Jacobs, UX and Frontend Developer (UX lead), Kestrel Consulting |
| **Reviewed by** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Status** | Draft for steering committee |

## 1. Purpose

Fortalis Verzekeringen works with a network of independent insurance brokers ("makelaars" / "courtiers") who use the broker portal to request quotes, submit new policies, report claims and follow up on their portfolio. The portal is more than ten years old, and brokers increasingly complain about it.

The discovery phase, started on 2025-04-14, aimed to understand how brokers actually use the portal, where it fails them, and what a modernised portal should do first. The product owner is Laura Vermeulen, Claims Operations Manager, and the sponsor is Marc Dubois, Chief Digital Officer. I acted as UX lead; Thomas Maes was project manager. The discovery phase is contracted on time and materials, capped at EUR 30,000.

## 2. What we did

- 14 interviews with brokers (small one-person offices up to a broker with 30 staff), in Dutch and French.
- 6 contextual observations at broker offices, watching people work with the portal for half a day.
- 5 interviews with internal users: broker account managers, underwriters and claims handlers.
- Analysis of portal usage logs and of 400 helpdesk tickets from the last twelve months.
- Two co-creation workshops with brokers and Laura's team.

## 3. Key findings

1. **Claims follow-up is the biggest pain.** Brokers cannot see the status of a claim they reported; 41% of the helpdesk tickets are "where is my claim?" questions. Brokers call the claims department instead, which costs both sides time.
2. **Double entry.** Most brokers use their own office management software; they retype customer and policy data into the portal. Several told us they postpone portal work to the evening.
3. **Quote flow is too long for simple products.** A home insurance quote takes 9 screens. Brokers abandon it and send an e-mail to the account manager.
4. **Documents are scattered.** Policy documents, claim documents and correspondence sit in different sections with different search behaviour.
5. **Mobile use is real.** Brokers visit customers after a loss and want to report a claim with photos from a phone. The current portal is not usable on mobile.
6. **Trust in data is low.** Portfolio overviews are refreshed overnight; brokers do not trust figures that differ from what an account manager tells them.

## 4. Proposed roadmap

| Step | Focus | Indicative timing |
|---|---|---|
| 1 | Claim status tracking for brokers, with notifications | first 4 months |
| 2 | Mobile claim reporting with photo upload | months 3 to 6 |
| 3 | Simplified quote flow for home and motor | months 5 to 9 |
| 4 | Unified document centre | months 8 to 12 |
| 5 | Integration with broker office software (data exchange instead of retyping) | to be investigated |

We recommend starting with claim status tracking: it addresses the largest share of complaints, reuses data already available from the claims process and gives brokers a visible improvement quickly.

## 5. Technology

**No technology has been chosen yet.** The choice of front-end framework, portal platform or low-code option depends on Fortalis' integration architecture and on the decision whether to build or buy. We propose a short architecture assessment with Fortalis' enterprise architecture team (Kevin Hermans) as the first activity of the next phase.

## 6. Next steps

| Action | Owner | Due |
|---|---|---|
| Present findings and roadmap to steering committee | EJ / TM | 2025-06-06 |
| Decision on next phase and budget | MD | 2025-06-20 |
| Prioritise roadmap step 1 user stories | LV / EJ | 2025-06-13 |
| Prepare architecture assessment scope | TM | 2025-06-13 |

*Elien Jacobs, Kestrel Consulting*
