# Acceptance Criteria Note: Accuracy Thresholds per Field

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Customs Document Extraction |
| **Date** | 2025-10-30 |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |
| **Document type** | Acceptance criteria note |
| **Approved by** | Jan Wouters, product owner (sprint 2 review, 2025-10-31) |

## 1. Purpose

The statement of work says phase 1 is accepted when the agreed document types meet accuracy thresholds set with Jan Wouters in sprint 2. This note defines how accuracy is measured and which thresholds apply.

## 2. Definitions

- **Field-level accuracy:** share of fields on the test set where the extracted value equals the value confirmed by a customs agent, after normalisation (spaces, date format, decimal separator). An empty extraction where a value exists counts as an error.
- **Test set:** per document type, at least 20 labelled documents that were never used for training, drawn from different senders. Refreshed every quarter with recent documents.
- **Weighted accuracy (all types):** field-level accuracy weighted by the weekly volume of each type, so the figure reflects the actual workload at the desk.
- **Confidence:** the confidence score returned by Azure AI Document Intelligence per field. Used for routing, not for measuring accuracy.

## 3. Thresholds

| Field category | Threshold (field-level accuracy) | Below threshold |
|---|---|---|
| Critical fields (container number, HS code, gross weight, number of packages, UN number and class, seal number) | 97% | Field always highlighted for review |
| Standard fields (names, addresses, dates, references) | 92% | Field shown, review advised |
| Line items (descriptions, quantities, values) | 90% per column | Review per line |

A document type is **accepted** for phase 1 when it meets the standard and line item thresholds on its test set, and the critical fields have a confidence-based routing rule that sends uncertain values to review. We do not require 97% on critical fields for acceptance; we require that the routing catches them.

## 4. Human in the loop

In phase 1 every document is validated by a customs agent, regardless of scores. The thresholds decide how much attention the validation screen asks for, not whether a person looks at the document. Jan wants to revisit this only after several months in production.

## 5. Labelling rules (summary)

- Label what is printed, unless a handwritten correction clearly replaces it; then label the handwritten value and tick "handwritten".
- Dates labelled as written; normalisation happens afterwards.
- Stamps over a field: label the field if readable, otherwise mark "obscured".
- Two agents label 10% of documents independently. Disagreements are resolved by the senior agent and used to sharpen the guidelines.

First double-labelling round (40 commercial invoices): agreement 96% on fields. Most disagreements on whether "net weight" or "gross weight" was meant on invoices that only show one weight.

## 6. Reporting

- Field-level accuracy per type and per field category in every sprint review.
- Weighted accuracy over all accepted types in every status report.
- Share of documents validated with zero corrections, as an indicator of the effort saved at the desk.

## 7. Risks noted

- Handwriting on CMR notes is likely to keep CMR below the standard threshold for some fields. Jan accepts that CMR may need more review than other types.
- New layouts from shippers will appear continuously; test sets must be refreshed or the figures become too optimistic.

Amira El Idrissi
