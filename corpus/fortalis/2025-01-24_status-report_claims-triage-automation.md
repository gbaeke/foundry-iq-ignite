# Status Report: Claims Triage Automation

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Status report (monthly) |
| **Date** | 2025-01-24 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Period** | 2024-12-16 to 2025-01-24 |
| **Distribution** | Marc Dubois, Laura Vermeulen |

## 1. Status overview

| Area | Previous | Current | Comment |
|---|---|---|---|
| Overall | Amber | Green | Live since 2025-01-13; budget on the CR-07 baseline |
| Scope | Green | Green | Delivered including CR-07; scope frozen |
| Planning | Green | Green | Go-live on the planned date; closure 2025-02-28 |
| Budget | Amber | Amber | EUR 276,000 baseline (EUR 240,000 + CR-07); forecast on baseline |
| Quality | Amber | Green | Override rate back near acceptance level after retraining |

Budget stays amber in the report, as it has since September, because the final cost is above the original fixed price. There is no further deviation.

## 2. Progress this period

- **Christmas freeze.** No production changes between 2024-12-16 and 2025-01-06. The pilot ran in proposal mode during the holidays without incidents. Volumes in the week between Christmas and New Year were low, as usual.
- **Override rate after retraining.** Since the retrained model was deployed on 2024-12-12, the weekly override rate was 10%, 9%, 9% and 8% (the last over a short holiday week). This meets precondition P3 of the go-live checklist.
- **Go/no-go on 2025-01-09.** Marc Dubois and Laura Vermeulen decided "go".
- **Go-live on 2025-01-13.** Auto-routing switched on at 07:00 as planned. The three test claims were routed correctly; the first real auto-routed claims were checked by a senior handler. No fallback was needed. In the first ten working days, a little over a third of incoming claims was auto-routed; the definitive figure will be measured over the last six weeks up to closure.
- **Intake team.** Two briefing sessions held on 2025-01-08 and 2025-01-10. The intake team lead reports that the team now spends most of its time on the human triage queue, where claims arrive with fields already filled in.
- **Run book.** Version 1.0 delivered to the Fortalis cloud team on 2025-01-10. Jonas Peeters gave two handover sessions on 2025-01-16 and 2025-01-21.

## 3. Monthly retraining

Following the analysis of December, monthly retraining becomes the standard procedure. Jonas is automating the retraining pipeline in Azure Machine Learning in the Fortalis spoke: data collection from the overrides of the past month, training, evaluation against the fixed reference set and a report for Laura's approval. The first run is planned for the week of 2025-02-03, executed by Fortalis IT with Amira El Idrissi watching.

## 4. Risks and issues

| # | Type | Description | Owner | Action |
|---|---|---|---|---|
| R7 | Risk | New colleagues in intake confirm human-triage proposals too quickly, which pollutes the override labels | LV | Reminder in team meeting; spot checks by senior handlers |
| R8 | Risk | Retraining depends on Fortalis IT availability each month | LV / Fortalis IT | Fixed slot in the first week of each month; documented in run book |
| R9 | Risk | Handwritten plumber invoices still often unreadable | AE | Accepted limitation; handlers read the document |
| I2 | Issue | Two claims auto-routed to the wrong team on 2025-01-15 because a broker used an outdated claim form | AE | Old form version added to the extraction training set |

## 5. Support after closure

Agreed with Marc and Laura: after closure, a support arrangement for three months, best effort, two days per month, covering advice on retraining results and threshold reviews. To be included in the closing report.

## 6. Next steps

| Action | Owner | Due |
|---|---|---|
| Automated retraining pipeline | JP | 2025-01-31 |
| First monthly retraining run | Fortalis IT / AE | 2025-02-07 |
| Retraining procedure and model card final | AE | 2025-02-14 |
| Project retrospective | TM | 2025-02-21 |
| Closing report and acceptance | TM / MD / LV | 2025-02-28 |

*Thomas Maes, Kestrel Consulting*
