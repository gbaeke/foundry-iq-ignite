# Closing Report: Leak Detection Analytics

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Leak Detection Analytics |
| **Date** | 2025-05-30 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Closing report |
| **Status** | Completed |

## 1. Summary

Leak Detection Analytics is completed. In the pilot zone the solution detected **23 leaks** during the validation period, each confirmed by an AquaNova field crew. The model and the GIS layer have been **handed over to Evelien Claes' GIS team**, which now owns, runs and retrains the model.

The project stayed within the fixed price and finished on the planned date, despite a delay in the data access phase over the winter.

## 2. Results in the pilot zone

| Metric | Result |
|---|---|
| Leaks detected and confirmed in the field | **23** |
| Of which not yet reported by customers | 17 |
| Median localisation accuracy | within about 150 m of the actual leak |
| Candidates sent to crews | 41 (56% confirmed) |
| Estimated reduction of night flow in the pilot zone | about 9% |

Most leaks were small service pipe leaks that would have run for weeks. Two were larger leaks on cast iron mains, found within three days of starting.

## 3. Delivered scope

- Daily SCADA export of the pilot zone into the Microsoft Fabric lakehouse
- Databricks pipelines for time series cleaning and night-flow features
- Anomaly detection and localisation models in Azure Machine Learning, with a retraining pipeline
- Leak candidate layer in ArcGIS, refreshed each morning, with a confidence score
- Runbook, model card and three handover sessions with the GIS team

## 4. Handover

| Item | Owner at AquaNova |
|---|---|
| Model, retraining and GIS layer | Evelien Claes, GIS Lead, and her team |
| SCADA export and tag list | Koen Martens, OT Engineer |
| Sponsor acceptance and rollout decision | Filip Wuyts, Director Asset Management |

Two GIS analysts in Evelien's team followed the handover sessions and ran a retraining on their own on 2025-05-26. Koen keeps ownership of the export from the OT side.

## 5. What went well

- Showing candidates in ArcGIS, the tool crews already use, made adoption easy. Crews started asking for the morning layer by themselves after two weeks.
- The GIS team corrected the network model of the pilot zone, which improved localisation.
- Bram's pipelines dealt with frozen and missing sensor values without manual work.

## 6. What could have gone better

- Getting access to operational data took much longer than the proposal assumed. The model phase had to be compressed and part of the tuning moved into the field validation.
- The first candidate lists were too long. Crews lost trust after a few false alarms, so we added a confidence threshold in week two of the pilot.

## 7. Lessons learned

1. Treat access to operational data as a project deliverable in its own right, with an owner and a date, not as an assumption.
2. Involve field crews from the first model version.
3. Let the future owner run a retraining before handover.

## 8. Recommendations

- Roll out to two more zones in the second half of 2025, using the same setup.
- Add the pressure loggers planned by asset management to the export.
- Review model performance every quarter with Evelien's team.

*Sofie Claes, on behalf of the project team (Sofie, Amira, Bram)*
