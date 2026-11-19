# Experiment Report: Handwriting-Aware Extraction for CMR Notes

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Customs Document Extraction |
| **Date** | 2026-07-10 |
| **Author** | Amira El Idrissi, Lead AI Engineer, Kestrel Consulting |
| **Document type** | Experiment report |
| **Period** | Sprints 19 and 20 (2026-06-15 to 2026-07-10) |
| **Reviewed with** | Jan Wouters, Pieter De Smet (2026-07-09) |

## 1. Background

Handwritten annotations on CMR consignment notes are the main accuracy issue of the project. At the June status report, field-level accuracy on CMR was 86%, against more than 95% for most printed types. On 2026-06-04 Jan Wouters agreed to two measures:

- **Option 2, immediately:** CMR notes with detected handwriting in an extracted field are marked "always review" for that field. Implemented on 2026-06-18.
- **Option 1, as an experiment:** a separate handwriting-aware model for the three most affected fields: seal number, remarks and date of delivery.

This report covers the experiment.

## 2. Set-up

- 620 CMR notes with handwriting, labelled with the "handwritten" flag since January, of which 470 for training and 150 for testing. The test set includes documents from 40 different hauliers.
- A second custom extraction model in Azure AI Document Intelligence, trained only on CMR notes with handwriting and only on the three target fields, using the service's handwriting recognition.
- In the Azure Logic Apps workflow, CMR notes flagged with handwriting are sent to both the standard CMR model and the handwriting model. For the three fields, the value with the higher confidence wins; all other fields come from the standard model.

## 3. Results on the test set (150 CMR notes with handwriting)

| Field | Standard model | Handwriting model | Combined rule |
|---|---|---|---|
| Seal number | 71% | 87% | 89% |
| Date of delivery | 78% | 90% | 91% |
| Remarks (free text, character level ≥ 90% similar) | 52% | 57% | 58% |

On all CMR notes (with and without handwriting), CMR field-level accuracy over all extracted fields goes from 86% to 89% with the combined rule.

Cost: the second model call only happens for CMR notes with handwriting, about 40% of CMR volume. Expected additional Document Intelligence cost is a few percent of the monthly total.

## 4. What does not work

- **Remarks.** Free-text remarks are handwritten in four languages, often abbreviated ("ok zonder schade", "pal. cassée", "Fahrer wartet"). Recognition improves slightly, but the content is too varied to be useful as structured data. The remarks field is not exported anyway (see the privacy note).
- **Overwritten printed values.** When a driver writes a seal number straight over the printed one, both models often read a mix of the two. The confidence is usually low, so routing catches it, but the value is wrong.
- **Stamps.** Company stamps across box 18 remain a problem for any model.

## 5. Decision (Jan Wouters, 2026-07-09)

1. Deploy the combined rule for **seal number** and **date of delivery** from sprint 21, after the monthly retraining cycle.
2. Seal number stays a critical field and is still always highlighted on CMR notes with handwriting. The gain is that the proposed value is now right more often, which saves the agent typing.
3. Remarks: no further work. Field remains "always review", not exported.
4. No deployment during the last two weeks of July, in line with the summer planning; deployment on 2026-07-14, before the quiet period.

## 6. Effect on overall figures

The weighted field-level accuracy over the 14 supported document types stays at about 94%: the CMR gain is roughly offset by new invoice layouts from shippers seen in June, which the July retraining addresses. The real benefit is at the desk: fewer keystrokes on the highest-volume paper document.

## 7. Recommendations

- Keep collecting handwriting samples; retrain the handwriting model every quarter rather than monthly.
- Support Jan's conversation with the large hauliers about eCMR. Every digital CMR removes the problem at the source.
- Re-measure CMR accuracy at the end of September, after the summer peak.

Amira El Idrissi
