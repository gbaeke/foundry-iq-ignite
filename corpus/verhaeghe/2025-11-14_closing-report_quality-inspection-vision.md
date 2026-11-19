# Closing Report: Quality Inspection Vision

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Quality Inspection Vision |
| **Date** | 2025-11-14 |
| **Author** | Amira El Idrissi, ML Engineer and project lead, Kestrel Consulting |
| **Document type** | Closing report |
| **Status** | Completed |

## 1. Summary

The Quality Inspection Vision project is completed and handed over to Verhaeghe Foods today. Camera-based inspection runs on lines 3, 5 and 6. A custom Azure AI Vision model on Azure IoT Edge flags suspect product for the operator in real time. On the final test set the model reaches **96% defect recall**, above the 90% target agreed with Dries Callens.

The project was delivered within the fixed price and on the planned end date.

## 2. Results

| Metric | Target | Result |
|---|---|---|
| Defect recall (all classes) | 90% | **96%** |
| False positive rate (line 3, after fix) | below 5% | 3.1% |
| Labelled images | 4,000 | **4,000** |
| Lines live | 3 | 3 |

Recall per class: foreign material 98%, packaging damage 97%, discolouration 95%, clumps 93%. Clumps remain the hardest class, mostly with small pieces.

## 3. Main issue: lighting on line 3

During the pilot on line 3 in the summer, the model produced many false positives. Analysis showed the cause was **inconsistent lighting**: daylight from the skylights above the line changed during the day, and reflections from the stainless steel frame made healthy product look discoloured. In some hours more than 20% of flags were false.

Solution: Jonas designed a **camera enclosure** for the inspection point, a closed hood with its own LED lighting and a matte inner finish. After the enclosure was installed on line 3, the false positive rate fell to 3.1%. The same enclosure was used on lines 5 and 6 from day one.

## 4. Labelling tool

**Ruben Wouters**, Junior Developer at Kestrel, built the labelling tool. It is a simple web app where the quality team sees images flagged on the line, draws boxes and picks a defect class. Ruben added a "second opinion" mode after the quality team disagreed about discolouration cases, so two labellers review the uncertain images. Dries' team labelled most of the 4,000 images themselves with this tool, about 8 hours per week in total.

## 5. What went well

- The network for the edge devices was requested in the first week, before the hardware arrived, so installation started without waiting.
- Running inference on the edge meant inspection kept working during two short network outages in September.
- The quality team owned the labels. That made the defect definitions much sharper than in our first draft.

## 6. What could have gone better

- We should have checked lighting conditions during the line walk at different hours of the day. A standard enclosure is now part of our edge vision setup.
- Clump detection needs more examples. We advise labelling another 500 images over the coming season.

## 7. Handover

| Item | Owner at Verhaeghe |
|---|---|
| Edge devices and network | Tine Desmet, IT Coordinator |
| Defect classes, thresholds and labelling | Dries Callens, Quality Manager |
| Sponsor acceptance | Ann Verhaeghe, CEO |

Handover sessions were held on 2025-11-06 (operations, with Tine) and 2025-11-12 (model retraining and labelling, with Dries' team). Retraining instructions are in the runbook.

## 8. Recommendations

1. Label about 500 extra images for the clumps class before the next harvest season.
2. Retrain the model every quarter, or after changing products or packaging.
3. Consider linking flags to the batch data on the sensor platform, so quality can see defect rates per batch.

*Amira El Idrissi, on behalf of the project team (Amira, Jonas, Ruben)*
