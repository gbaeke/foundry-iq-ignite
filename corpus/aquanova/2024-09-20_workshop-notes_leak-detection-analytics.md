# Workshop Notes: Pilot Zone Selection

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Leak Detection Analytics |
| **Date** | 2024-09-20 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Workshop notes (prioritisation) |
| **Participants** | Evelien Claes, Koen Martens, a GIS analyst, a field crew coordinator, Sofie Claes, Amira El Idrissi, Bram Visser |

## 1. Purpose

Choose one pilot zone for model development and field validation. Filip Wuyts asked for a zone that is "representative, not the easiest".

## 2. Candidate zones

Koen's list (action 1 of the kickoff) showed five zones where every DMA has an inlet flow meter and at least two pressure points. We scored them on five criteria, 1 (poor) to 5 (good).

| Criterion | Weight | Noord-Oost | Centrum | West | Zuid | Heuvel |
|---|---|---|---|---|---|---|
| SCADA coverage (flow and pressure per DMA) | 3 | 5 | 4 | 4 | 3 | 4 |
| Network model quality in ArcGIS | 2 | 3 | 5 | 4 | 3 | 2 |
| Leak history (enough repairs as labels) | 3 | 4 | 3 | 2 | 4 | 3 |
| Mix of pipe materials and ages | 2 | 5 | 2 | 3 | 4 | 3 |
| Crew availability for validation | 1 | 4 | 3 | 4 | 2 | 4 |
| **Weighted score** | | **46** | 39 | 36 | 37 | 35 |

## 3. Discussion

- **Centrum** has the best network model but is mostly recent PE pipes with few leaks. Too easy, and too few labels.
- **Noord-Oost** has four DMAs, a mix of cast iron mains, older PVC and recent PE, and 212 repaired leaks in three years. The network model has known gaps on older segments.
- Evelien's GIS team is willing to correct the gaps in Noord-Oost before the model phase. Her analyst estimates about 30 to 40 segments with missing material or diameter.
- Koen noted that two pressure points in Noord-Oost were replaced in 2023, so their history before that may not be comparable.
- The field crew coordinator confirmed that Noord-Oost crews know the zone well and can validate quickly.

## 4. Decision

**Pilot zone: Noord-Oost, 4 district metered areas.** Confirmed by Filip by mail on 2024-09-23.

## 5. Data needs for Noord-Oost

| Signal | Count (Koen's first estimate) | Resolution in historian |
|---|---|---|
| DMA inlet flow | 4 | 1 minute |
| Pressure points | 11 | 1 minute |
| Reservoir and pump station signals feeding the zone | about 40 | 1 minute |
| Valve positions (where telemetered) | about 25 | on change |

History wanted: at least 18 months, to cover two summers and a winter.

## 6. Labels

Filip's repair work orders contain an address and a date, not always a pipe segment. Evelien's analyst will geocode them onto the network model. Amira warned that the date in a work order is the repair date; the leak itself usually started earlier. We will estimate leak start from the night-flow history.

## 7. Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Tag list for Noord-Oost, with tag descriptions | KM | 2024-10-11 |
| 2 | Geocode repair work orders of Noord-Oost | EC (GIS analyst) | 2024-10-18 |
| 3 | List of network model gaps in Noord-Oost | EC | 2024-10-11 |
| 4 | Data mapping note for SCADA signals | BV | 2024-10-18 |
| 5 | Propose the data access path to OT security | KM / SC | after the tag list |
