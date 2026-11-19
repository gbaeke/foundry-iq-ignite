# Interim Validation Report: Field Results After Five Weeks

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Leak Detection Analytics |
| **Date** | 2025-05-09 |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |
| **Document type** | Test and evaluation report (interim) |
| **Period** | 2025-04-07 to 2025-05-08 |
| **Audience** | Evelien Claes, Filip Wuyts, Sofie Claes, Bram Visser |

## 1. Summary

After five weeks of field validation in zone Noord-Oost, the crews have confirmed **19 leaks** out of 33 candidates sent to them. Since the confidence threshold was introduced in week two, the share of confirmed candidates has gone up from one in three to about two in three. Localisation is useful for crews but coarse in the outer streets. The validation continues until 2025-05-16; the final numbers will be in the closing report.

## 2. Method

Crews follow the protocol agreed on 2025-03-28: search the candidate segments and connected segments up to the next valve, maximum half a day per candidate, record the result in ArcGIS on the tablet. A candidate is confirmed if a leak is found within the searched area.

Distance is measured between the centre of the candidate area and the actual leak location recorded by the crew.

## 3. Results

| Measure | Week 1 (no threshold) | Weeks 2–5 (threshold 0.6) | Total |
|---|---|---|---|
| Candidates sent | 12 | 21 | 33 |
| Confirmed | 4 | 15 | 19 |
| Not found | 8 | 4 | 12 |
| Still to search | 0 | 2 | 2 |
| Share confirmed (of searched) | 33% | 79% | 61% |

Of the 19 confirmed leaks:

| Type | Number |
|---|---|
| Service pipe | 12 |
| Fitting or joint | 3 |
| Cast iron main | 2 |
| Hydrant | 2 |

14 of the 19 had not been reported by customers. The other 5 were reported while the candidate was already on the map, mostly within one or two days.

**Localisation:** median distance between candidate centre and leak about 160 m. In the two inner DMAs, with more pressure points, the median is about 90 m. In the outer DMA NO-4, with only two pressure points, several leaks were found more than 300 m from the centre, at the edge of the search area.

## 4. What the "not found" cases tell us

We reviewed all 12 not-found candidates with the crew leaders:

- 5 were unusual night consumption (a bakery, a greenhouse, a sports club filling a pool). Now in the known night consumers list.
- 3 were flushing or works not in the planning.
- 2 were likely real leaks that crews could not hear in the time box; one was found by acoustic loggers a week later on the same street.
- 2 have no explanation.

## 5. Crew feedback

From the Friday calls:

- "The grey candidates are useful when we are in the area anyway."
- Crews prefer a list sorted by confidence and estimated flow, not by DMA.
- They would like to see how long a leak has probably been running. Added to the layer as "first seen".

## 6. Model changes during validation

- Week 2: confidence threshold 0.6 for sending candidates to crews.
- Week 3: known night consumers masked in the expected-flow model.
- Week 4: prior for hydrant segments lowered; two hydrant candidates turned out to be legitimate use.

All changes were tracked as new model versions in Azure Machine Learning.

## 7. Next steps

- Continue validation until 2025-05-16.
- Final numbers and night-flow reduction estimate in the closing report.
- Recommendation for more pressure loggers in NO-4.
- Handover sessions with the two GIS analysts from 2025-05-12.
