# Handover Notes: Model and GIS Layer to the GIS Team

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Leak Detection Analytics |
| **Date** | 2025-05-27 |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |
| **Document type** | Handover notes |
| **Receiving team** | Evelien Claes (GIS Lead) and two GIS analysts |

## 1. Sessions

| Date | Topic | Trainers |
|---|---|---|
| 2025-05-12 | Data flow end to end: nightly export, lakehouse, features, scoring, layer | Sofie, Bram |
| 2025-05-19 | The model: detection, localisation, thresholds, model card | Amira |
| 2025-05-22 | Operations: daily checks, incidents, retraining pipeline | Amira, Bram |
| 2025-05-26 | **Retraining by the GIS analysts on their own**, Kestrel only observing | (observed by Amira) |

## 2. The retraining of 2025-05-26

As agreed at the steering meeting of 2025-02-07, the two GIS analysts ran a full retraining without help:

1. Checked that crew statuses of the last month were read back into the training data.
2. Started the retraining pipeline in Azure Machine Learning.
3. Compared the new expected-flow models with the current ones on the validation report: mean residual, false signals per DMA per month.
4. Decided to promote the new version for DMAs NO-1 to NO-3 and keep the current one for NO-4, where the new version gave more false signals.
5. Checked the next morning's candidate layer in ArcGIS.

It took them about two hours. They found the model registry confusing at first; Amira added a one-page "which version is live" guide to the runbook.

## 3. What the GIS team owns from now on

| Item | Owner |
|---|---|
| Model, retraining, thresholds | GIS team (Evelien) |
| Candidate layer in ArcGIS | GIS team |
| Network model corrections in Noord-Oost | GIS team |
| Nightly SCADA export through the data diode, tag list | Koen Martens (OT) |
| Lakehouse and Databricks jobs | GIS team, with AquaNova IT for access |
| Rollout decision for other zones | Filip Wuyts |

## 4. Daily routine for the GIS team

- 06:00: check the monitoring mail. No mail means the nightly file arrived complete.
- 07:30: the candidate layer is refreshed. A quick look at new candidates before the crew coordinator does.
- Fridays: 30-minute review with the crew coordinator, continued after the project.

## 5. Monthly and quarterly

- **Monthly:** run the retraining pipeline; promote only if better on the validation measures.
- **Quarterly:** performance review with Evelien: candidates sent, share confirmed, distance. Adjust threshold only after a review, not after a single bad week.

## 6. Documents handed over

- Runbook (operations, incidents, retraining) with the "which version is live" guide
- Model card: data, method, measures, known limits (coarse localisation in NO-4, small leaks below about 0.5 m³/h)
- Data mapping note and ADR-03 (daily data)
- Known night consumers list, maintained by the GIS team

## 7. Access

Kestrel and DataForge accounts stay active until the end of June for questions, then AquaNova IT removes them. The GIS analysts have owner rights on the Azure Machine Learning workspace and contributor rights on the Fabric workspace.

## 8. Open points

| # | Point | Owner |
|---|---|---|
| 1 | Add the planned pressure loggers to the export once installed | KM / EC |
| 2 | Decide on rollout to more zones | FW |
| 3 | Final validation numbers in the closing report | SC |
