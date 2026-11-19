# Closing Report: Claims Triage Automation

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Closing report |
| **Date** | 2025-02-28 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Distribution** | Marc Dubois, Laura Vermeulen; Kestrel project team |

## 1. Summary

Claims Triage Automation is in production at Fortalis Verzekeringen and the project closes today, 2025-02-28. Incoming claims for motor, fire, theft and water damage are read, classified and routed automatically, and handlers receive only the cases that need a human decision.

The key result: **38% of incoming claims are auto-triaged** without manual intervention, measured over the last six weeks of production. The remaining claims arrive in the human triage queue with the extracted fields and a proposed classification, which still saves intake time.

The **final cost is EUR 276,000**, against the original fixed price of EUR 240,000. The difference is fully explained by change request CR-07 (adding water damage claim types), approved by the sponsor, Marc Dubois, Chief Digital Officer, in September 2024.

| Area | Result |
|---|---|
| Scope | Delivered, including CR-07 |
| Planning | Go-live in January 2025 as planned |
| Budget | EUR 276,000 (EUR 240,000 + CR-07) |
| Auto-triage rate | 38% of incoming claims |

## 2. Delivered solution

- Extraction of claim forms, repair quotes, plumber invoices and police reports with Azure AI Document Intelligence.
- Classification of claim type, complexity and urgency with models in Azure Machine Learning.
- End-to-end orchestration with Azure Logic Apps, from intake mailbox and broker uploads to the claims management system.
- Monitoring dashboard for Laura Vermeulen (Claims Operations Manager) and her team leads: volumes, auto-triage rate, queue times and override rate.

## 3. Model drift after the storm season

In November and December 2024, after the autumn storm season, the classification quality dropped noticeably. Handlers overrode the proposed classification about twice as often as in the acceptance period. Analysis by Amira El Idrissi (ML Engineer) showed clear **model drift**: storm-related claims (roof damage, fallen trees, water infiltration) came in with different wording, different document mixes and much higher volumes than in the historical training data, and several were classified as the wrong type or with too low urgency.

Measures taken:

- Retrained the model on a dataset including the storm-season claims, which restored the override rate to the acceptance level.
- Introduced **monthly retraining** as a standard procedure: each month the model is retrained on the latest labelled claims (handler overrides serve as labels), evaluated against a fixed reference set and promoted only after approval by Laura's team.
- Added a drift alert on the override rate, so the claims team is warned before quality drops visibly.

Jonas Peeters (Cloud Platform Engineer) automated the retraining pipeline in the Fortalis spoke so it runs without Kestrel involvement.

## 4. Lessons learned

1. **Freeze scope early, or price change properly.** CR-07 was the right business decision, but it should have been anticipated in the original scope discussion; water damage was always going to be asked for.
2. **Seasonality is a requirement, not an exception.** Insurance volumes and wording change with the weather; plan retraining from the start.
3. **Overrides are free labels.** Designing the handler interface to capture overrides made monthly retraining cheap.

## 5. Handover and support

- Run book, retraining procedure and model cards delivered to Fortalis IT and the claims operations team.
- Support contract for the first three months: best effort, two days per month.

## 6. Acceptance

Accepted by Marc Dubois, Chief Digital Officer, and Laura Vermeulen, Claims Operations Manager, on 2025-02-28.

*Thomas Maes, Kestrel Consulting*
