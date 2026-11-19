# Status Report: Claims Triage Automation

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Status report (monthly) |
| **Date** | 2024-09-20 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Period** | 2024-08-19 to 2024-09-20 |

## 1. Status overview

| Area | Previous | Current | Comment |
|---|---|---|---|
| Overall | Green | Amber | Scope extended; budget overrun forecast, covered by approved change request |
| Scope | Green | Amber | Water damage claim types added (CR-07) |
| Planning | Green | Green | Go-live window unchanged |
| Budget | Green | Amber | Forecast 15% above fixed price |
| Quality | Green | Green | Extraction and classification on target for motor, fire, theft |

## 2. Progress this period

- **Extraction:** Azure AI Document Intelligence custom models for the claim form and the repair quote are in acceptance. Field-level accuracy on the test set is above the agreed threshold for all mandatory fields.
- **Triage model:** Amira El Idrissi (ML Engineer) delivered the second version of the classification model in Azure Machine Learning. On the hold-out set for motor, fire and theft, about four in ten claims score above the auto-routing threshold.
- **Orchestration:** Jonas Peeters (Cloud Platform Engineer) finished the Logic Apps flow from the intake mailbox to the claims system test environment, including error handling and the human triage queue.
- **Labelling:** the claims handlers labelled a further 2,300 historical claims; thanks to Laura Vermeulen (Claims Operations Manager) for freeing up the extra time.

## 3. Scope change: water damage claim types

In August, Laura Vermeulen asked to include **water damage claim types** (pipe leaks, infiltration, flooding by heavy rain) in the triage. Water damage is the largest growing claim category for Fortalis and a large share of the manual intake effort, so the business case for including it now is clear. It was, however, not part of the agreed scope.

Impact analysis by the team:

- Additional extraction work for plumber invoices and leak detection reports.
- Extra labelling round and a separate sub-model for water damage severity.
- Additional test scenarios in user acceptance.

The forecast impact is an **overrun of 15%** on the fixed price of EUR 240,000. Planning can be held by running the water damage work in parallel with integration testing.

**Change request CR-07** describing the extension, cost and planning impact was submitted on 2024-09-04 and **approved by Marc Dubois**, Chief Digital Officer, on 2024-09-13. The fixed-price contract is amended accordingly.

## 4. Risks and issues

| # | Type | Description | Owner | Action |
|---|---|---|---|---|
| I1 | Issue | Scope extension with water damage types (CR-07 approved) | TM | Track additional effort separately in timesheets |
| R1 | Risk | Too few labelled water damage examples for rare sub-types | AE | Merge rare sub-types into "other water damage" for first release |
| R2 | Risk | Claims system API rate limits in production | JP | Load test with Fortalis IT in October |
| R3 | Risk | Further scope requests during UAT | TM | Freeze scope after CR-07; new requests go to backlog for after go-live |

## 5. Next steps

| Action | Owner | Due |
|---|---|---|
| Plan extra labelling round for water damage | LV | 2024-09-30 |
| Extend Document Intelligence models with plumber invoices | AE | 2024-10-18 |
| Water damage severity sub-model v1 | AE | 2024-11-08 |
| Load test claims system API | JP | 2024-10-25 |
| Update project plan and budget baseline with CR-07 | TM | 2024-09-27 |
| Next steering committee | MD / TM | 2024-10-17 |

*Thomas Maes, Kestrel Consulting*
