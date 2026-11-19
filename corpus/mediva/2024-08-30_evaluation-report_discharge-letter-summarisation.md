# Evaluation Report: Draft Discharge Letters

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Discharge Letter Summarisation |
| **Document type** | Evaluation report |
| **Date** | 2024-08-30 |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |
| **Distribution** | Dr. Hilde Van Damme, Jeroen Lambrecht, Sarah Mertens; Pieter De Smet, Thomas Maes |

## 1. Summary

The clinical evaluation ran over **eight weeks**, from 2024-06-24 to 2024-08-16: a two-week baseline and a six-week intervention period. The intervention period was extended by two weeks because of summer leave, as approved by Dr. Van Damme in July. **12 physicians** of internal medicine and geriatrics took part and **410 letters** were written with a draft.

Main result: physicians saved **about 9 minutes per discharge letter** on average. We saw no increase in corrections or questions from general practitioners compared with the baseline.

## 2. Participation

| | Internal medicine | Geriatrics | Total |
|---|---|---|---|
| Physicians | 6 | 6 | 12 |
| Letters in evaluation (with draft) | 231 | 179 | 410 |

All 12 physicians met the minimum of five letters in each period. Baseline letters are used only as the reference for time and GP questions and are not counted in the 410. 14 letters were excluded earlier because of the timer issue in the first week.

## 3. Time

Time is measured from opening to signing the letter, per physician, as the median of their letters in each period. The difference is then averaged over the 12 physicians.

| Measure | Result |
|---|---|
| Average time saved per letter | about 9 minutes |
| Range over physicians | 4 to 15 minutes |
| Largest savings | long geriatric stays with many medication changes |
| Smallest savings | short internal medicine stays |

Two physicians who already wrote very short letters saved the least. Two assistants saved the most, mainly on the medication section.

## 4. Ratings

| Rating | Share of drafts |
|---|---|
| Usable with minor edits | 78% |
| Usable with major edits | 16% |
| Not usable | 6% |

"Not usable" drafts were concentrated in stays with many scanned external documents (flagged, not used) and in a few very short stays where the physician found writing from scratch quicker.

## 5. Corrections

| Correction type | Share of corrected paragraphs |
|---|---|
| Too long (mostly course of stay) | 38% |
| Wording too confident | 21% |
| Missing information | 19% |
| Style or local phrasing | 15% |
| Factual error | 7% |

**Course of stay too long** remains the main complaint, especially in internal medicine. **Over-confident wording**: the draft turned "probably" or "suspected" into a firm statement in a minority of letters. Both are addressed with prompt and template changes before the pilot (section 7).

**Factual errors** were mostly wrong dates of a procedure caused by the date shift in pseudonymisation being applied twice in one specific section type. Fixed on 2024-07-22. Two errors were reported as potentially harmful (a dose stated with the wrong unit, a stopped drug listed as continued); both were caught by the physician during review. The pause threshold of the protocol was never reached.

## 6. General practitioners

The medical secretariats recorded GP questions or correction requests in the four weeks after each stay. Baseline and intervention rates were comparable; we see no sign that draft-based letters are less clear for GPs.

## 7. Changes before the pilot

1. Course of stay: maximum three sentences per problem, with an explicit instruction to leave out normal daily observations.
2. Wording: the instruction to keep the certainty level of the source is strengthened, and the review screen underlines words like "caused by" or "confirmed" when the source uses a hedge.
3. Unit check for doses in the medication section, done in code.
4. Date shift fix verified on all section types.

## 8. Recommendation

Proceed with the pilot in daily practice in internal medicine and geriatrics from September, with the changes above. To be decided at the steering committee of 2024-09-04.
