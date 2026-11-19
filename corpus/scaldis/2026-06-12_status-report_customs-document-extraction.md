# Status Report: Customs Document Extraction

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Customs Document Extraction |
| **Date** | 2026-06-12 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Status report |
| **Reporting period** | Sprints 17 and 18 (2026-05-18 to 2026-06-12) |
| **Distribution** | Koen Verstraete, Jan Wouters, Lotte Willems, Amira El Idrissi |

## 1. Overall status

| Dimension | Status | Comment |
|---|---|---|
| Overall | **Green** | Project ongoing, steady progress |
| Scope | Green | Two additional document types added on request of Jan |
| Schedule | Green | On plan for the summer peak |
| Budget (T&M) | Amber | Phase 1 budget used; continuation agreed per quarter |
| Quality | Amber | Accuracy on CMR notes below threshold |

The project is **ongoing**. The extraction pipeline runs in production at the customs desk with human validation on every document.

## 2. Key figures

| Metric | Previous report | Now |
|---|---|---|
| Document types supported | 12 | **14** |
| Field-level accuracy (all types, weighted) | 92.6% | **94%** |
| Documents processed per week | ~2,300 | ~2,900 |
| Share of documents with zero corrections | 61% | 66% |

The two new types this period are phytosanitary certificates and a carrier-specific delivery order format, both prioritised by Jan Wouters' team.

## 3. Progress

- Amira retrained the composed Document Intelligence model with 340 extra labelled samples, mainly commercial invoices from Asian shippers.
- The Logic Apps workflow now routes documents with low confidence on critical fields (HS code, gross weight, container number) to a senior customs agent instead of the general queue.
- The validation screen shows the source crop next to each field, which customs agents say saves them several clicks per document.

## 4. Main issue: handwritten annotations on CMR notes

**Handwritten annotations on CMR consignment notes are the main accuracy issue.** Truck drivers and warehouse staff often write corrections, seal numbers or remarks on the CMR by hand, sometimes over the printed fields. Field-level accuracy on CMR notes is 86%, against more than 95% on most printed documents. CMR is also one of the highest-volume types, so it pulls down the overall figure.

Options discussed with Jan on 2026-06-04:
1. Train a separate handwriting-aware model for the most affected fields (seal number, remarks, delivery date)
2. Flag CMR notes with detected handwriting as "always review" and stop trying to extract those fields
3. Ask the main hauliers to use a digital eCMR where possible (longer term, outside our scope)

Proposal: do option 2 immediately and run a two-sprint experiment on option 1.

## 5. Risks and issues

| ID | Type | Description | Owner | Status |
|---|---|---|---|---|
| I-21 | Issue | Handwritten annotations on CMR notes lower extraction accuracy | AE | Open |
| R-22 | Risk | Summer peak volumes may grow the validation queue | JW | Open |
| R-23 | Risk | New invoice layouts from shippers not seen in training | AE | Open, monthly retraining |
| R-24 | Risk | Budget continuation for Q3 not yet signed | LW | Open |

## 6. Next steps

| Action | Owner | Due |
|---|---|---|
| Implement "always review" rule for CMR notes with handwriting | AE | 2026-06-19 |
| Experiment with handwriting-aware model for 3 CMR fields | AE, PDS | 2026-07-10 |
| Q3 budget continuation to Koen for approval | LW | 2026-06-26 |
| Staffing plan for summer peak at the customs desk | JW | 2026-06-26 |

Pieter De Smet
