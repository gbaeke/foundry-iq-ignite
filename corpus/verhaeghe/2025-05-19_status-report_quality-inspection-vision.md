# Status Report: Quality Inspection Vision

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Quality Inspection Vision |
| **Date** | 2025-05-19 |
| **Author** | Amira El Idrissi, ML Engineer and project lead, Kestrel Consulting |
| **Document type** | Biweekly status report (no. 5) |
| **Distribution** | Ann Verhaeghe, Dries Callens, Tine Desmet, Lotte Willems |

## 1. Status

| Area | Status | Comment |
|---|---|---|
| Overall | Green | Capture running, labelling on track |
| Scope | Green | Unchanged |
| Schedule | Green | First model training planned in June |
| Budget | Green | About 29% used |
| Data | Amber | Too few packaging damage examples |

## 2. Done in the last two weeks

- **ADR-02 accepted** on 2025-05-05: images cropped to the belt, images with hands or arms discarded on the edge, 7-day retention on the industrial PC, 12 months for unused uploaded images. Dries informed the works council through HR.
- **Labelling:** 1,240 images labelled so far, of which 610 OK images. Labellers now average 18 seconds per OK image, thanks to the zoom and undo added by Ruben.
- **Seeded runs:** three Wednesday sessions held. Each run passes about 15 kg of rejected product through the inspection point.
- **Edge:** the Azure IoT Edge deployment on line 3 now runs two modules, capture and upload. Jonas set up a deployment manifest per line so lines 5 and 6 can reuse it.
- **Line walk lines 5 and 6** done on 2025-05-14. Same position type as line 3: transfer belt after the freezer exit. Gantries ordered from the maintenance workshop.

## 3. Labelling progress per class

| Class | Target | Labelled | Comment |
|---|---|---|---|
| Foreign material | 600 | 180 | mostly from seeded runs |
| Discolouration | 800 | 260 | 41 marked uncertain |
| Clumps | 700 | 150 | |
| Packaging damage | 400 | 40 | camera position sees little of it |
| OK | 1,500 | 610 | |

## 4. Issues

### I-02: Packaging damage hardly visible (open)

As expected at the line walk, the inspection point sees only a small part of the packaging process. Only 40 examples so far. Options discussed with Dries:

1. Seeded runs with damaged film offcuts passing on the belt.
2. Accept lower recall for packaging damage in version 1.

Dries chose option 1 for now. Decision on option 2 at the end of June if numbers stay low.

## 5. Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-02 | Not enough real defects | Medium | High | Seeded runs weekly |
| R-03 | Labellers disagree on discolouration | Medium | Medium | Review by Dries every Friday |
| R-05 | Labelling time in harvest season | High | Medium | Pea campaign starts mid-June; aim for 2,500 labels by then |
| R-06 | GPU capacity on edge PC with more classes | Low | Medium | Benchmark after first model |

## 6. Next two weeks

- First training run in Azure AI Vision on the labelled set (target 2025-06-02).
- Ruben: per-labeller agreement statistic, and an export check that flags images without any label.
- Jonas: inference module skeleton on the edge, ready for the first model.
