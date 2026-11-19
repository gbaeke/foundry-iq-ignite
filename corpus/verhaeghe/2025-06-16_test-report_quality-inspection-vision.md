# Model Evaluation Report: First Custom Model (v1)

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Quality Inspection Vision |
| **Date** | 2025-06-16 |
| **Author** | Amira El Idrissi, ML Engineer and project lead, Kestrel Consulting |
| **Document type** | Test and evaluation report |
| **Audience** | Dries Callens, Jonas Peeters, Ruben Wouters |

## 1. Summary

The first custom model was trained in Azure AI Vision on 2025-06-03 on images from line 3. On a held-out test set it reaches **84% defect recall** over all classes, against a project target of 90%. Foreign material is already close to target; packaging damage and clumps are not. The main limits are the number of examples and label consistency on discolouration. We propose a second model before the pilot, not changes to the setup.

## 2. Data

| Set | Images | Of which with defects |
|---|---|---|
| Training | 1,820 | 860 |
| Validation | 230 | 110 |
| Test (held out, never seen in training) | 400 | 190 |

All images come from the line 3 inspection point between 2025-04-15 and 2025-05-30, cropped to the belt as decided in ADR-02. The test set was labelled twice: by one labeller and by Dries.

## 3. How we measure

- **Recall per class:** share of real defects (in Dries' test labels) that the model flags.
- **False positive rate:** share of flags that are not real defects.
- A flag counts as correct if the model box overlaps the labelled box for at least 30%. The operator only needs to know where to look, not the exact outline.
- Threshold: confidence 0.5 for all classes. We will tune per class later.

## 4. Results

| Class | Recall | False positive rate |
|---|---|---|
| Foreign material | 91% | 6% |
| Discolouration | 83% | 14% |
| Clumps | 79% | 9% |
| Packaging damage | 70% | 11% |
| **All classes** | **84%** | **10%** |

Inference time on the industrial PC is 70 to 90 ms per image, well within the capture rate. Jonas' benchmark shows enough spare GPU capacity for a larger model.

## 5. Error analysis

We looked at all 31 missed defects and 60 false flags with Dries.

- **Discolouration:** 22 of the 60 false flags. In 14 cases Dries himself said "could be either". The training labels for this class are inconsistent: the agreement between the two labellers on discolouration is only 71%, against more than 90% on the other classes.
- **Clumps:** most misses are small clumps of three pieces, just above the size rule from the workshop.
- **Packaging damage:** only 40 training examples at the start of June. Seeded runs with film offcuts have added 70 more since, too late for v1.
- **Speed:** no difference in recall between slow and fast products. The exposure settings from the line walk work.

## 6. Actions

1. **Second opinion mode in the labelling tool.** Ruben adds a mode where every image labelled as discolouration or uncertain by one labeller is shown blind to the second labeller. Only images where both agree go into training; the others go to Dries. Ready on 2025-06-20.
2. **Re-label** the 260 discolouration training images with the second opinion mode.
3. **Per-class thresholds**: lower for foreign material (missing it is worst), higher for discolouration.
4. **More examples:** continue seeded runs; target 2,700 labelled images before v2.
5. **Model v2** for the start of the pilot on line 3, planned 2025-07-07.

## 7. Decision

Dries agreed to start the pilot with v2 in July, with flags shown to operators but no change to the reject procedure. Packaging damage stays in scope; the decision to lower its target is postponed to after the pilot.

## 8. Labelling status

2,120 images labelled by 2025-06-13. The pea campaign has started; labelling time per week is down from eight to about five hours. Dries has asked a third colleague to help on Fridays until the end of July.
