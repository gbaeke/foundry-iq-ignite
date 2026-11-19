# Engineering Guideline: Evaluating AI Output

| | |
|---|---|
| **Organisation** | Kestrel Consulting (internal) |
| **Date** | 2024-11-15 |
| **Author** | Amira El Idrissi, ML Engineer |
| **Document type** | Engineering guideline, version 1.0 |
| **Reviewed by** | Pieter De Smet |

## Purpose

Customers rarely ask "how accurate is it?" in the first meeting. They always ask it in the steering committee before go-live. This guideline describes how we evaluate the output of models, both classic ML and generative AI, so that we can answer that question with numbers instead of impressions. It applies to every project that puts a model in front of users.

## 1. Agree what "good" means, with the customer, in sprint 1

- Write down the **decision the output supports** (draft a letter, route a document, raise an alert).
- Agree **one primary metric** and at most three secondary ones. For extraction: field-level accuracy. For classification: precision and recall per class. For forecasts: MAPE or MAE on a hold-out period. For generated text: a rubric scored by domain experts, plus a business metric.
- Agree the **target** and what happens below it (human review, fall-back, no go-live).

## 2. Build the evaluation set before the first demo

- Use real cases, selected with the customer, not by us. Cover the common cases and the known hard ones.
- Every item has a **reference answer** or label and, where relevant, the **source** it should be based on.
- Keep it **frozen** per version. When you add items, create a new version and report on both.
- Size: start with 50 to 100 items. It is better to have 80 good items early than 500 in the last sprint.

## 3. Human evaluation for generated text

Automated metrics are useful for regression testing, but for text that people sign or act on, domain experts must judge it. The **Discharge Letter Summarisation** project at Mediva, which closed in October, is our reference:

- The evaluation ran over eight weeks with **12 physicians** from two departments.
- Each physician first wrote letters as usual during a **baseline period**, then with the generated draft.
- Drafts were rated on a simple scale ("usable with minor edits", "usable with major edits", "not usable") and the time per letter was measured, not asked.
- Headline result: about **9 minutes saved per discharge letter**.

What made it convincing for the sponsor was the baseline. Surveys asking "how much time does this save you?" give optimistic and inconsistent answers. Measure before and after.

## 4. Automate the regression run

- Every change to prompts, retrieval, model version or training data triggers a run of the full evaluation set.
- Results are stored per run with the configuration that produced them, so we can say which change made it better or worse.
- Use an LLM-as-judge only as a pre-filter, calibrated against human ratings on a sample. Report the agreement rate.

## 5. Look at the errors, not only the score

- Read at least 20 failed items after every significant run. Classify them: data problem, retrieval problem, model problem, unclear reference.
- Unclear references are common. Fix the evaluation set, and note it in the version log.
- Report errors by segment (document type, department, class). An average hides the segment that matters.

## 6. Keep evaluating after go-live

- Monitor input drift: new document layouts, new claim types, seasonal effects. Data changes; models do not adapt by themselves.
- Collect user feedback with a single click on each answer or prediction, and review it on a fixed rhythm.
- Agree a retraining or review cadence with the customer as part of the handover.

## 7. Reporting template

Every status report for an AI project includes: evaluation set version, primary metric versus target, change since last run, top three error categories. The template is in the project SharePoint.

## Questions

Ask me directly or in the "ai-engineering" Teams channel.

Amira
