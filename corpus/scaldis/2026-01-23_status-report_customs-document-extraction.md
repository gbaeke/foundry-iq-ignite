# Status Report: Customs Document Extraction

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Customs Document Extraction |
| **Date** | 2026-01-23 |
| **Author** | Amira El Idrissi, Lead AI Engineer, Kestrel Consulting |
| **Document type** | Status report |
| **Reporting period** | Sprints 7 and 8 (2026-01-05 to 2026-01-23) |
| **Distribution** | Koen Verstraete, Jan Wouters, Lotte Willems, Pieter De Smet |

Sprint 7 was a short restart week after the Christmas freeze (2025-12-22 to 2026-01-02), during which the parallel run continued without any deployment.

## 1. Overall status

| Dimension | Status | Comment |
|---|---|---|
| Overall | **Green** | Ready for production use on 2026-02-02 |
| Scope | Green | Six types in the pipeline, two to go for the phase 1 target |
| Schedule | Green | Production start confirmed by Jan Wouters |
| Budget (T&M) | Green | 47% of EUR 95,000 consumed |
| Quality | Amber | CMR below threshold on standard fields |

## 2. Progress

- **Document types.** Six types now in the composed model: commercial invoice, packing list, CMR consignment note, certificate of origin, T1 transit document and bill of lading. Dangerous goods declaration and EUR.1 are in labelling.
- **Accuracy.** Weighted field-level accuracy over the six types on the test sets: 90.8%. Without CMR: 93.5%.
- **Parallel run.** Over eight weeks, agents compared pipeline results with manual keying on about 9,000 documents. Pipeline errors were caught in validation in every logged case; the agents logged 41 cases where their own keying was wrong and the pipeline was right.
- **Privacy.** Privacy note approved on 2025-12-12. Retention job (90 days after release) tested this week. Signatures and contact persons removed from the labelling schema.
- **Security check before production.** Done with Scaldis IT security on 2026-01-20. One remark: the scanning station network folder allowed write access to all customs building users. Restricted to the scanning account.

## 3. CMR consignment notes

CMR remains the hardest type. Standard fields on the CMR test set: 84%, critical fields routed correctly in 98% of cases. The main reason is handwriting: corrections and remarks written over printed boxes, seal numbers added by hand, dates in many styles. Labelling now marks every handwritten value, so we can measure the effect separately. First count: 38% of CMR notes in the samples carry at least one handwritten annotation in a field we extract.

The two missed critical fields were both seal numbers written by hand next to a printed seal number. Until we have a better solution, seal number on CMR is always highlighted for review.

## 4. Performance and cost

- Average time from arrival to validation queue: 41 seconds. The mailbox trigger was changed from polling every 5 minutes to every minute during office hours.
- Document Intelligence cost is driven by pages processed. Multi-page invoices with terms and conditions on every page doubled the page count; the workflow now drops pages that the classifier marks as "terms" before extraction.

## 5. Risks and issues

| ID | Type | Description | Owner | Status |
|---|---|---|---|---|
| R-03 | Risk | Handwriting on CMR limits extraction quality | AE | Open, measured separately |
| R-04 | Risk | Shipper layouts change without notice | AE | Open, monthly retraining from February |
| R-06 | Risk | Privacy note approval | PDS | Closed |
| I-01 | Issue | Skewed scans from the scanning station | JW | Closed, new scanner profile since 2025-12-15 |
| R-07 | Risk | Agents rely on the pipeline and validate less carefully | JW | New |

R-07 came from Jan himself: in the second half of the parallel run, validation got faster, which is the goal, but also less attentive. Jan will do weekly spot checks.

## 6. Next steps

- Production use from 2026-02-02 for the six types, validation on every document (PDS, JW)
- Dangerous goods declaration and EUR.1 models (AE)
- Monthly retraining routine from February (AE)
- Weekly spot checks of validated records (JW)

Amira El Idrissi
