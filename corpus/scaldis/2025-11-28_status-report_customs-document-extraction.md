# Status Report: Customs Document Extraction

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Customs Document Extraction |
| **Date** | 2025-11-28 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Status report |
| **Reporting period** | Sprints 3 and 4 (2025-11-03 to 2025-11-28) |
| **Distribution** | Koen Verstraete, Jan Wouters, Lotte Willems, Amira El Idrissi |

## 1. Overall status

| Dimension | Status | Comment |
|---|---|---|
| Overall | **Green** | Parallel run started on plan |
| Scope | Green | Eight priority types agreed |
| Schedule | Green | Parallel run from sprint 4, as planned |
| Budget (T&M) | Green | 24% of EUR 95,000 consumed |
| Quality | Amber | CMR samples harder than expected |

## 2. Progress this period

- **Models.** Amira El Idrissi trained custom extraction models in Azure AI Document Intelligence for commercial invoices and packing lists, and a first classifier for six document types. Both models are composed into one model behind the classifier.
- **Workflow.** The Azure Logic Apps workflow handles both intake channels: the customs shared mailbox and the scanning station folder. Average time from arrival to validation queue: 48 seconds.
- **Validation screen.** First version in use by three customs agents. Fields are grouped as on the declaration; critical fields on top.
- **Parallel run.** Since 17 November, every commercial invoice and packing list is processed by the pipeline in parallel with manual keying. Agents compare and log differences.
- **Mapping.** Data mapping note and export layout v1 reviewed with Jan Wouters.

## 3. Key figures (test sets)

| Type | Standard fields | Line items | Critical fields routed correctly | Status |
|---|---|---|---|---|
| Commercial invoice | 91.4% | 88.7% | 100% | Below threshold on line items |
| Packing list | 95.2% | 93.1% | 100% | Meets threshold |
| CMR consignment note | 81% (first model) | — | n/a | In progress |

"Critical fields routed correctly" means every critical field that was wrong had a confidence low enough to be highlighted for review.

## 4. Observations from the parallel run

- On packing lists, agents found three keying errors of their own that the pipeline had right. Jan mentioned this at the desk meeting, which helped acceptance.
- Commercial invoices from two Asian shippers use a layout not in the training set; accuracy on those is poor. 60 extra samples requested.
- The scanning station produces skewed scans when documents are fed in a stack. Agents now feed CMR notes one by one; a better scanner profile is being tested with the scanner supplier.

## 5. Risks and issues

| ID | Type | Description | Owner | Status |
|---|---|---|---|---|
| R-03 | Risk | Handwriting on CMR notes limits extraction quality | AE | Open |
| R-04 | Risk | Shipper layouts change without notice | AE | Open, retraining process to be defined |
| R-05 | Risk | Labelling time at the desk competes with year-end peak | JW | Open |
| R-06 | Risk | Privacy note not yet approved; needed before production | PDS | Open, due 2025-12-12 |
| I-01 | Issue | Skewed scans from the scanning station | JW | Open, with scanner supplier |

## 6. Next steps (sprints 5 and 6)

- CMR model v2 with more samples and handwriting flag in the labelling (AE)
- Certificate of origin and T1 models (AE)
- Privacy note with the data protection contact (PDS)
- Second security check before production use (PDS with Scaldis IT security)
- Christmas planning: freeze from 2025-12-22 to 2026-01-02, parallel run continues for invoices and packing lists, no deployments

## 7. Budget

| Item | Value |
|---|---|
| Phase 1 budget (T&M) | EUR 95,000 |
| Consumed | 24% |
| 75% signal expected | March 2026 |

Pieter De Smet
