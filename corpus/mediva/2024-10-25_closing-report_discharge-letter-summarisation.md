# Closing Report: Discharge Letter Summarisation

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Discharge Letter Summarisation |
| **Document type** | Closing report |
| **Date** | 2024-10-25 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Distribution** | Dr. Hilde Van Damme, Jeroen Lambrecht, Sarah Mertens; Kestrel project team |

## 1. Summary

The Discharge Letter Summarisation project closes today. Physicians at Mediva Care Group can now generate a draft discharge letter from the patient record, review it and sign it. The draft is built with Azure OpenAI on pseudonymised content, in line with the conditions agreed with the DPO.

The headline result of the clinical evaluation: **physicians save about 9 minutes per discharge letter**, with no increase in the number of corrections requested by general practitioners during the evaluation period.

| Area | Status |
|---|---|
| Scope | Delivered |
| Budget | Within fixed price |
| Planning | Closed on the re-planned date |
| Quality | Accepted by sponsor |

## 2. What was delivered

- Draft generation for discharge letters in internal medicine and geriatrics, with specialty-specific templates.
- Pseudonymisation pipeline before every model call; re-identification only inside Mediva's environment.
- A review screen where the physician sees the draft next to the source sections it was based on.
- Monitoring of usage, generation time and edit distance between draft and signed letter.
- Run book and operational handover to Jeroen Lambrecht's IT team.

## 3. Clinical evaluation

The evaluation ran over eight weeks with **12 physicians** (assistants and staff members, two departments). Each physician wrote letters as usual for a baseline period and then with the draft for the remainder.

| Measure | Result |
|---|---|
| Physicians in evaluation | 12 |
| Letters in evaluation | 410 |
| Average time saved per letter | about 9 minutes |
| Drafts rated "usable with minor edits" | 78% |
| Drafts rated "not usable" | 6% |

Physicians appreciated the structure and the medication-change section most. The main complaints were the length of the course-of-stay paragraph and occasional over-confident wording, which we addressed with prompt changes in the final sprint.

## 4. Issues during the project

- **Late start:** the project started six weeks later than originally planned because the DPIA had to be completed first. The rest of the plan shifted accordingly; no scope was cut.
- **Source data quality:** some older notes were scanned PDFs without text; these are skipped and flagged in the draft.
- **Physician availability** during the summer holidays slowed down the evaluation by about two weeks; we absorbed this in the planning buffer.

## 5. Lessons learned

1. Start the privacy assessment before signing the contract, not after.
2. Show the source next to the generated text; it builds trust faster than any accuracy metric.
3. Measure time saved with a baseline period, not with a survey.

## 6. Recommendation: follow-up

During the evaluation, several physicians asked the same question in different forms: "Can I also ask it what our protocol says?" Today they search the intranet and shared drives for clinical guidelines, protocols and procedures, often finding several versions.

We recommend a follow-up project: a **clinical knowledge assistant** that answers questions from physicians and nurses on the basis of Mediva's own clinical guidelines and protocols, with references to the source documents. It can reuse the secure EU environment, the governance set up with Sarah Mertens and the evaluation approach of this project. We suggest Dr. Van Damme and Kestrel explore the scope in a short workshop in the coming months.

## 7. Acceptance

Accepted by Dr. Hilde Van Damme, Chief Medical Information Officer, on 2024-10-25.

*Thomas Maes, Kestrel Consulting*
