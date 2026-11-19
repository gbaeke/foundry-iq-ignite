# Analysis Note: Override rate in the pilot and model drift

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Technical analysis note |
| **Date** | 2024-12-13 |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |
| **For** | Laura Vermeulen, Thomas Maes, Jonas Peeters; for information Marc Dubois |

## 1. Question

Why did the override rate in the live pilot rise from about 9% (acceptance sessions in October) to about 18% at the end of November and in the first week of December, and what do we do about it before auto-routing goes live?

## 2. What we looked at

- All 2,960 overrides from 2024-11-04 to 2024-12-08, with the original prediction and the handler's correction.
- A sample of 400 overridden claims, re-read with the two senior claims handlers in three sessions.
- Comparison of the input data in the pilot with the training data: text length, language, vocabulary, document types per claim, claim volumes per week.

## 3. Findings

**3.1 It is the data, not the software.** Extraction quality on claim forms and repair quotes is unchanged. Technical deferrals are below 1%. The classification endpoint returns the same results for the same input. The problem is the input itself.

**3.2 Storm-related claims dominate the overrides.** About 70% of the overridden claims relate to storm damage after the autumn storms: roof damage, fallen trees on houses and cars, water infiltration through a damaged roof. These claims:

- were three to four times more frequent per week than in the same weeks of the historical extract;
- have shorter descriptions (median 19 words against 46), often typed on a phone;
- carry more photos and fewer documents, and a new document type: the roofer's or contractor's quote;
- use vocabulary the model rarely saw ("dakpannen", "tuiles", "boom omgewaaid", "chute d'arbre").

**3.3 Typical wrong predictions.**

| Pattern | Effect |
|---|---|
| Roof damage with interior water described as "water damage" only | Routed to water damage instead of the storm handling team in the "other" queue |
| "Damage to the roof structure" | Predicted as fire in some cases |
| Fallen tree on a car | Predicted motor (own damage) correctly, but complexity too low when the tree also hit the house |
| "Roof open, rain coming in" in a short text | Urgency U2 instead of U1 |

The last pattern matters most: a missed U1 means a family with an open roof waits in a normal queue.

**3.4 This is drift, and it will come back.** The model was trained on 18 months up to March 2024, including only one autumn, which was mild. The relation between text and correct class has not changed for the old claim types; what changed is the mix and the wording of what comes in. Every storm season, and likely every hail or flooding event, will do this again.

## 4. Corrective actions

**Done this week:**

1. Labelled 1,850 pilot claims from November and December, using the handler overrides as labels after a quick check by the senior handlers.
2. Retrained the triage model in Azure Machine Learning on the original training set plus these claims. Added the roofer's quote as a document type in the Document Intelligence classifier.
3. Evaluated on two sets: the original hold-out set (to check nothing got worse) and a new storm reference set of 300 claims. Result: unchanged on the original set; on the storm set, wrong type halved and missed U1 reduced from 14% to 4%.
4. Laura approved the promotion on 2024-12-12. The retrained model was deployed to the pilot the same day, before the Christmas change freeze starts on 2024-12-16.

**Proposed for operations:**

- **Monthly retraining.** Each month, retrain on the latest labelled claims with the overrides as labels, evaluate on a fixed reference set (original hold-out plus storm set), and promote only after approval by Laura's team. Jonas will automate the pipeline so it runs without Kestrel.
- **Drift alert.** An alert when the weekly override rate exceeds 12%, sent to Laura and the team leads, so the team knows before quality visibly drops.
- **Seasonal awareness.** The reference set gets a "seasonal" part that is refreshed after each storm or hail period.

## 5. What to watch next

The effect of the retrained model on the override rate will only be clear after one or two weeks. I will report the figures in the go-live checklist and before the go/no-go of 2025-01-09.

*Amira El Idrissi*
