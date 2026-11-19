# Run Book Chapter 6: Monthly retraining of the triage model

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Run book / procedure |
| **Date** | 2025-02-14 |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |
| **Pipeline automation** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Owner after handover** | Claims operations (Laura Vermeulen) for model decisions; Fortalis IT for execution |
| **Version** | 1.0 |

## 1. Why monthly retraining

Claims change with the seasons. After the autumn storms of 2024, claims arrived with different wording, documents and volumes, and the override rate doubled in a few weeks. A retraining on recent claims restored quality. To avoid waiting for the next drop, the triage model is retrained every month on the latest labelled claims.

## 2. Roles

| Role | Who | Responsibility |
|---|---|---|
| Model owner | Claims Operations Manager | Approves or rejects promotion |
| Reviewers | Two senior claims handlers | Check the evaluation report and a sample of changed predictions |
| Operator | Fortalis IT, data platform team | Starts the pipeline, follows up failures, deploys after approval |
| Platform | Fortalis cloud team | Spoke, identities, quota |

## 3. Schedule

- **First Tuesday of the month:** the operator starts the retraining pipeline in Azure Machine Learning.
- **By Thursday:** evaluation report available to the model owner.
- **By the following Tuesday:** decision. Promotion happens in a normal change window. During the Fortalis Christmas change freeze, no promotion takes place; the December run is evaluated but promoted in January, unless the drift alert has fired.

## 4. Pipeline steps

1. **Collect labels.** All claims of the previous month that went through the human triage queue, with the final type, complexity, urgency and water damage severity after any override. Auto-routed claims that were later re-routed by a handler are included with the corrected values.
2. **Quality filter.** Overrides where the handler spent less than five seconds on the claim are excluded (see risk R7, January status report). Claims with "type doubtful" or "unsure" labels are excluded.
3. **Pseudonymise.** The same replacement rules as for the original training data (names, addresses, plate numbers, national register numbers).
4. **Train.** Training set = previous training set + new month, with the most recent 12 months weighted higher. Same features and settings unless a change has been approved separately.
5. **Evaluate** against the **fixed reference set**: the original hold-out set, the storm reference set of December 2024, and a water damage set. The reference set is never used for training.
6. **Report.** Per type: accuracy, share above thresholds, missed U1 rate, and a comparison with the model in production. Plus 50 claims where the new model would decide differently, for the reviewers.

## 5. Promotion criteria

The new model is promoted only if **all** of these hold on the reference set:

- Missed U1 rate not higher than the production model.
- Type accuracy not lower than the production model by more than 0.5 percentage point on any type.
- Share above thresholds not lower by more than 2 points overall.
- The reviewers found no systematic problem in the 50 sample claims.

If the criteria are not met, the production model stays. The operator logs the result and the model owner decides whether to ask for an analysis.

## 6. Drift alert

Independently of the monthly cycle, an alert is sent to the model owner and the team leads when the weekly override rate exceeds 12%. In that case an extra retraining can be started outside the schedule. Expect this after storms, hail and periods of heavy rain.

## 7. Rollback

Every promoted model stays in the model registry. Rolling back means deploying the previous version to the online endpoint; this takes about ten minutes and is described in chapter 4 (deployments).

## 8. First run (February 2025)

Executed by Fortalis IT on 2025-02-04 with Amira watching. 4,920 new labelled claims; all promotion criteria met; approved on 2025-02-11 and promoted on 2025-02-12. Duration of the pipeline: 2 hours 40 minutes. Two small fixes made to the report layout afterwards.

## 9. Cost

One training run costs a small amount of compute in the Fortalis subscription. The online endpoint cost is not affected.

*Amira El Idrissi*
