# ADR-01: Confidence threshold and the human triage queue

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Architecture decision record |
| **Date** | 2024-05-08 |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |
| **Decided with** | Laura Vermeulen (product owner), Thomas Maes, Jonas Peeters |
| **Status** | Accepted |

## Context

The triage model predicts three things for each incoming claim: claim type, complexity and urgency (U1 to U3), each with a probability. Some claims will be clear, others ambiguous. We need a rule for when the system routes a claim on its own and when a person decides. The rule must be understandable for the claims team, adjustable without retraining, and safe for urgent cases.

At the kickoff it was agreed that claims the model cannot classify with enough confidence always go to people. This ADR makes that concrete.

## Options considered

1. **One global threshold on the type prediction.** Simple, but ignores urgency: a confidently classified fire claim with an uncertain urgency could be routed as U2 while the family is sleeping at a neighbour's.
2. **Separate thresholds per output, all must pass.** Safer. Lower auto-routing rate, because three conditions must hold at the same time.
3. **Learned "route or defer" model.** Elegant, but hard to explain and to tune by the business. Rejected for the first release.

## Decision

**Option 2, separate thresholds per output, all must pass**, plus a set of hard rules that always defer.

A claim is auto-routed only if:

- the type probability is at least **0.85**, and
- the complexity probability is at least **0.80**, and
- the urgency probability is at least **0.80**, or the predicted urgency is U1 (see below), and
- none of the hard rules applies.

**Hard rules (always to the human triage queue):**

- Predicted type is "other".
- Policy number could not be extracted or does not match an active policy.
- The description mentions injury or death (keyword list in Dutch, French, English and German, maintained by Laura's team).
- The claim is flagged in the system for a special investigation.
- A possible duplicate from another channel was found within 48 hours.

**Urgency U1 is asymmetric.** If the model predicts U1 with any probability above 0.40, the claim is routed as U1, even if the type goes to the human queue. A false "urgent" costs a handler a few minutes; a missed "urgent" costs a customer a night in a hotel.

## Where the thresholds live

Thresholds and hard rules are configuration of the orchestration flow in Azure Logic Apps, not part of the model in Azure Machine Learning. Laura's team can request a change through a simple form; Jonas or the Fortalis cloud team applies it after approval. Every change is logged with date, old value, new value and approver.

## What the handler sees

Claims in the human triage queue arrive with:

- the extracted fields from Azure AI Document Intelligence, highlighted in the document;
- the top two predicted types with their probability;
- the reason for deferral (low confidence, hard rule name).

The handler confirms or changes the type, complexity and urgency. **Every change is stored as an override with the original prediction.** These overrides will be our main source of new labels later.

## Consequences

- Auto-routing rate will be lower than with a single threshold. Based on the first experiments, we expect between a third and a half of claims in scope to be auto-routed. We will measure on the hold-out set in September.
- The thresholds will need tuning during user acceptance. We agree with Laura to review them once at the end of UAT and then quarterly.
- Because of the injury rule, most complex motor claims will never be auto-routed. Laura considers this correct.

## Review

To be reviewed after the first month in production.

*Amira El Idrissi*
