# Clinical Evaluation Protocol

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Discharge Letter Summarisation |
| **Document type** | Evaluation protocol |
| **Date** | 2024-06-14 |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |
| **Approved by** | Dr. Hilde Van Damme (CMIO); privacy aspects reviewed by Sarah Mertens (DPO) |
| **Version** | 1.0 |

## 1. Objective

Measure whether a draft discharge letter generated from the patient record saves physicians time, without lowering the quality of the letter sent to the general practitioner. The evaluation also identifies the most frequent corrections so the templates and instructions can be improved before the pilot in daily practice.

## 2. Participants

- 12 physicians: six from internal medicine and six from geriatrics, assistants and staff members, nominated by the heads of department via Dr. Van Damme.
- Participation is voluntary. A physician can stop at any time without explanation.
- All participants attend a 45-minute training session (2024-06-20) on the review screen and the rating form.

## 3. Design

**Baseline period (two weeks).** Physicians write discharge letters as usual. The letter editor records the time between opening and signing the letter, and the active editing time.

**Intervention period (four weeks).** For each letter the physician first generates a draft, reviews it next to the sources, edits it and signs. The same time measures are recorded.

| Period | Planned dates |
|---|---|
| Baseline | 2024-06-24 to 2024-07-05 |
| Intervention | 2024-07-08 to 2024-08-02 |
| Analysis and report | 2024-08-05 to 2024-08-30 |

Physicians on leave simply do not contribute letters in that week; at least five letters per physician per period are needed for their data to count. If needed, the intervention period can be extended by up to two weeks, within the evaluation phase that ends 2024-08-30.

## 4. Measures

**Primary**
- Time per letter (opening to signing) in baseline versus intervention, per physician.

**Secondary**
- Active editing time
- Edit distance between draft and signed letter, per template paragraph
- Physician rating per draft: *usable with minor edits*, *usable with major edits*, *not usable*
- Number and type of corrections: factual error, missing information, too long, wording too confident, style
- Corrections or questions from GPs about the letter in the four weeks after the stay, compared with the baseline (collected by the medical secretariats)

## 5. Safety rules

1. A draft is never sent without physician review and signature. The editor does not allow signing without at least opening every paragraph.
2. Any factual error that the physician considers potentially harmful is reported the same day via the rating form, with the section reference. Amira reviews these within one working day and reports them to Dr. Van Damme.
3. If more than two potentially harmful errors are reported in one week, the evaluation is paused and discussed with Dr. Van Damme.

## 6. Data protection

- The evaluation uses the same pseudonymised flow as the prototype; no separate assessment is needed, as Sarah confirmed in the DPIA closure meeting.
- The repeat pseudonymisation test on 200 new letters (2024-06-14) showed no residual direct identifiers and 0.6% of sections with residual indirect identifiers, in line with the first test. Sarah accepted the result.
- Time measurements and ratings are linked to a physician code, not to the physician's name, in the analysis. The key is kept by Dr. Van Damme's office.
- Kestrel receives only aggregated measures and pseudonymised drafts with their edits.

## 7. Analysis

- Per physician: median time per letter in baseline and intervention; difference.
- Overall: average of the per-physician differences, with the range.
- Ratings and corrections: counts per department and per template paragraph.
- No statistical significance is claimed with 12 physicians; the goal is a reliable order of magnitude.

## 8. Reporting

An evaluation report is delivered by 2024-08-30 and discussed at the steering committee in September, together with the go/no-go for the pilot in daily practice.
