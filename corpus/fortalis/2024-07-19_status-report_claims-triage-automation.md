# Status Report: Claims Triage Automation

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Status report (monthly) |
| **Date** | 2024-07-19 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Period** | 2024-06-17 to 2024-07-19 (sprints 6 to 8) |
| **Distribution** | Marc Dubois, Laura Vermeulen |

## 1. Status overview

| Area | Previous | Current | Comment |
|---|---|---|---|
| Overall | Green | Green | Build phase on plan |
| Scope | Green | Green | Two scope clarifications logged (CR-02, CR-03), no cost impact |
| Planning | Green | Green | Dependency on claims system write interface, target mid-August |
| Budget | Green | Green | Effort in line; milestone "discovery and labelling" invoiced |
| Quality | Green | Green | Claim form extraction above threshold |

## 2. Progress this period

- **Privacy and security review** held on 2024-07-04 and passed with conditions. Pseudonymisation for French plate numbers extended, 90-day retention configured and named access list agreed. Real claims are processed in the acceptance environment since 2024-07-15.
- **Extraction.** Amira El Idrissi delivered the custom Azure AI Document Intelligence model for the Fortalis claim form (Dutch and French version). Mandatory fields (policy number, date of loss, place of loss, claimed amount) are above the agreed field-level accuracy on the test set. The repair quote model covers the 20 most frequent garage layouts; a generic model for the long tail is in progress.
- **Triage model v1.** First version of the classification model trained in Azure Machine Learning on 3,400 labelled claims. Type prediction is good for motor and theft; fire is weaker because fire files often combine smoke, water from firefighting and contents damage. Complexity and urgency are still noisy, as expected with this number of labels.
- **Orchestration.** Jonas Peeters completed the intake flow in Azure Logic Apps for all three channels and the duplicate check across channels. The triage flow runs end-to-end against the stub of the claims system.
- **Labelling.** 3,850 claims labelled for complexity and urgency, close to the 4,000 target for end of July. Agreement between labellers on urgency improved from about two thirds to 84% after the guidelines of 2024-05-29.

## 3. Scope clarifications

| CR | Subject | Cost impact |
|---|---|---|
| CR-02 | Claims flagged for special investigation are never auto-routed (hard rule) | None |
| CR-03 | Broker uploads count as an intake channel from the first release, with the same rules as the intake mailbox | None |

## 4. Risks and issues

| # | Type | Description | Owner | Action |
|---|---|---|---|---|
| R2 | Risk | Claims system write interface expected around 2024-08-16; holiday period in the claims system team | LV | Weekly check-in; integration tests not before October, margin of about six weeks |
| R3 | Risk | Long tail of repair quote layouts | AE | Generic model plus field-level confidence; low confidence leaves the field empty |
| R5 | Risk | Fire claims harder to classify than expected | AE | More fire examples in next labelling batch; consider splitting "fire" into sub-types later |
| R6 | Risk | Summer holidays: Laura absent 2024-07-29 to 2024-08-16, labellers on reduced capacity | TM | Backup decision maker for scope questions: intake team lead; sprint review of 2024-08-09 held with the senior handlers, Laura joins remotely |

## 5. Next steps

| Action | Owner | Due |
|---|---|---|
| Generic repair quote model | AE | 2024-08-09 |
| Triage model v2 with full labelled set | AE | 2024-09-13 |
| Connect triage flow to the real write interface in test | JP | 2024-08-30 |
| Load test date with claims system team | JP | 2024-09-13 |
| Next labelling batch (fire focus) | LV | 2024-09-20 |

## 6. Remark

Kestrel is open during the summer; the team takes holidays in turns so that two of the three are always available. The Belgian national holiday on 21 July falls on a Sunday this year, so no impact.

*Thomas Maes, Kestrel Consulting*
