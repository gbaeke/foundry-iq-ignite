# Training Outline: Retraining and Labelling for the Quality Team

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Quality Inspection Vision |
| **Date** | 2025-10-27 |
| **Author** | Amira El Idrissi, ML Engineer and project lead, Kestrel Consulting (with Ruben Wouters) |
| **Document type** | Training material outline |
| **Session** | 2025-11-12, 09:00 to 15:00, quality office Roeselare |
| **Participants** | Dries Callens and three members of the quality team |

## 1. Learning goals

After the session, Dries' team can on their own:

1. Keep the labelled set up to date with the labelling tool, including review of operator feedback.
2. Start a retraining of the custom model in Azure AI Vision with a new labelled set.
3. Judge whether a new model is better than the current one, using the fixed test set.
4. Ask Tine to deploy a new model to one line, check it, then roll out to the other lines.

The team does not need to understand the internals of the model. They need to know what good data looks like and how to read the evaluation.

## 2. Programme

| Time | Block | Trainer |
|---|---|---|
| 09:00 | Why the model makes mistakes: examples from line 3 in July, small clumps | Amira |
| 09:45 | Labelling tool refresher: queue, second opinion mode, review, statistics | Ruben |
| 10:30 | Break | |
| 10:45 | From operator feedback to label: the "not a defect" queue | Ruben |
| 11:30 | Hands-on: each participant labels and reviews 40 images | Ruben |
| 12:15 | Lunch | |
| 13:00 | Retraining step by step (export, training run, evaluation) | Amira |
| 14:00 | Reading the evaluation: recall, false positive rate, per class | Amira |
| 14:30 | When to retrain, and when not to | Amira |
| 15:00 | Close | |

## 3. Key content per block

**Why the model makes mistakes.** Light, product variation, rare defects, inconsistent labels. The July lighting episode on line 3 is the main example: the fix was physical (the enclosure), not a new model.

**Second opinion mode.** Every discolouration or uncertain label is shown blind to a second labeller. Only agreement goes into training. This is the main reason discolouration recall went up.

**Fixed test set.** 600 images, labelled by Dries and one labeller, never used in training. Every new model is compared with the current one on this set. On this set the current model (v4) reaches 96% recall over all classes. If a new model scores lower on any class, it is not deployed.

**When to retrain.**
- Every quarter, as a routine.
- After a new product or packaging type is introduced.
- After changes to the camera, enclosure or lighting.
- Not after one bad shift. Look at the data first.

## 4. Materials

- Runbook chapter 5 (retraining) and chapter 6 (labelling and review), updated by Ruben.
- One-page checklist "before you deploy a new model", laminated for the quality office.
- Labelling tool access for the fourth team member, requested from Tine.

## 5. Exercise for the session

Ruben prepares a small set of 300 newly labelled images, including 80 clumps from the October production. The team runs a retraining on the training environment, compares it with v4 on the fixed test set, and decides whether they would deploy it. Expected outcome: slightly better on clumps, equal elsewhere. That is a realistic "yes, deploy to line 3 first" decision.

## 6. Follow-up

- Recommendation for the coming season: label about 500 extra images for the clumps class.
- First retraining by the team on its own: planned for early December 2025, before the end of the warranty period on 2025-12-14, with Amira available by mail.
