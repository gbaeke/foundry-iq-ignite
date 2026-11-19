# Design Note: Leak Detection and Localisation Model, Version 1

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Leak Detection Analytics |
| **Date** | 2025-03-14 |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |
| **Document type** | Technical design note |
| **Reviewed with** | Evelien Claes and a GIS analyst, 2025-03-12 |

## 1. Problem

Two questions per morning, for each of the four district metered areas (DMAs) of Noord-Oost:

1. **Detection:** is there a new leak in this DMA?
2. **Localisation:** if so, on which pipe segments is it most likely?

The output is a short list of candidates on the ArcGIS map, each with a confidence score.

## 2. Data

- Daily SCADA export since 2025-01-13, plus 18 months of backfill: inlet flow per DMA, 11 pressure points, pump and reservoir signals.
- Silver and gold features from Bram's Databricks jobs: minimum night flow (02:00–04:00), night-to-day ratio, pressure statistics per point, flow balance per DMA.
- ArcGIS network model of Noord-Oost, after the 37 segment corrections by the GIS team.
- 196 geocoded repair work orders from the last three years, used as labels.

## 3. Detection

Approach: compare each night's minimum night flow with what is expected for that DMA, given season, day of week and temperature.

- An expected-flow model per DMA is trained on nights without known leaks.
- The residual (observed minus expected) is tracked over time. A **sustained step up** over at least three nights is a leak signal. A single high night (flushing, a large consumer, a fire hydrant used) is not.
- Planned works and flushing from asset management's planning are used to mask nights.

On historical data, this flags 71% of repaired leaks at least three days before the repair date, with about one false signal per DMA per month.

## 4. Localisation

When a DMA shows a leak signal, the location is estimated from pressure.

- A leak lowers pressure most at the points closest to it. For each pressure point, the change in night pressure is compared with the change expected from the extra flow.
- The network model gives, for each pipe segment, how strongly each pressure point "sees" a leak there (a sensitivity table, computed once from the network model in a Python notebook).
- Segments are ranked by how well their sensitivity pattern matches the observed pressure changes.
- Prior per segment from material, age and repair history: cast iron and old PVC get a higher prior.

The top candidate segments that together explain most of the signal form one candidate, shown as a group of segments on the map.

## 5. Training and tracking

- All experiments, models and metrics are tracked in Azure Machine Learning.
- A scheduled pipeline in Azure Machine Learning scores the previous day every morning at 07:00, after the features are ready.
- A retraining pipeline refits the expected-flow models monthly. The GIS team will run this after handover.

## 6. Output to ArcGIS

| Field | Meaning |
|---|---|
| candidate_id | unique per candidate |
| dma | DMA code |
| segments | pipe segments in the candidate area |
| estimated_flow | extra night flow in m³/h |
| confidence | 0 to 1 |
| first_seen | first night of the signal |
| status | new / sent to crew / confirmed / not found |

Crews update the status after validation; the model reads it back for retraining.

## 7. Known limits

- With only 11 pressure points in four DMAs, localisation is coarse in the outer streets. Expect hundreds of metres, not tens.
- Small leaks below about 0.5 m³/h are hard to separate from consumption noise.
- Customer consumption is yearly for most addresses and is not used in the daily model.

## 8. Review with Evelien (2025-03-12)

Evelien and the GIS analyst agreed with the approach. They asked to show the candidate area as segments, not as a point, so that crews do not search one exact spot. Agreed and reflected above.
