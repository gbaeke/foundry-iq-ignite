# Status Report: Customs Document Extraction

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Customs Document Extraction |
| **Date** | 2026-10-30 |
| **Author** | Amira El Idrissi, Lead AI Engineer, Kestrel Consulting |
| **Document type** | Status report |
| **Reporting period** | Sprints 27 and 28 (2026-10-05 to 2026-10-30) |
| **Distribution** | Koen Verstraete, Jan Wouters, Lotte Willems, Pieter De Smet |

## 1. Overall status

| Dimension | Status | Comment |
|---|---|---|
| Overall | **Green** | Project ongoing; Q4 continuation signed |
| Scope | Green | Q4 deliverables from the September workshop |
| Schedule | Green | Pilot for risk-based validation started |
| Budget (T&M) | Green | Q4 continuation on plan |
| Quality | Amber | CMR still below threshold on standard fields |

The project is **ongoing**. The pipeline runs in production at the customs desk for the 14 supported document types, with human validation on every document except within the controlled pilot below.

## 2. Key figures

| Metric | End of September | Now |
|---|---|---|
| Document types supported | 14 | 14 |
| Field-level accuracy (all types, weighted) | ~94% | ~94% |
| CMR field-level accuracy | 89% | 89% |
| Documents processed per week | ~3,000 | ~3,050 |
| Share of documents with zero corrections | 68% | 69% |

## 3. Progress

- **Risk-based validation pilot (packing lists).** Internal compliance agreed on 2026-10-14 to a pilot with double validation: for eight weeks, packing lists that score above the agreed confidence on all fields are validated as usual, and in parallel a sample of 20% is checked again by a senior agent. Only if the second check finds no material errors will sample checks replace full validation for that type. Started 2026-10-19.
- **Cross-document checks.** Gross weight and number of packages are now compared between invoice, packing list and CMR for the same container. Conflicts above 2% are highlighted. In the first week, 37 conflicts were flagged; agents confirmed 29 as real document discrepancies.
- **Declaration system vendor.** Scaldis IT obtained a technical contact at the vendor. A first call on the import interface is planned for 2026-11-10. No integration work before the feasibility study is done.
- **Retraining.** Monthly retraining continues; fast-track retraining was used twice since September for top-20 shipper layout changes. Test sets refreshed in October with recent documents, as every quarter.
- **Retention audit.** Scaldis' data protection contact checked the 90-day retention job on a sample of 50 containers. All images and data deleted on time.

## 4. Risks and issues

| ID | Type | Description | Owner | Status |
|---|---|---|---|---|
| I-21 | Issue | Handwritten annotations on CMR notes lower extraction accuracy | AE | Open, mitigated for seal number and delivery date |
| R-23 | Risk | New invoice layouts from shippers not seen in training | AE | Open, fast-track retraining |
| R-31 | Risk | Pilot sample checks find errors and delay the decision | JW | Open |
| R-32 | Risk | Christmas peak with reduced staffing | JW | Open, staffing plan in progress |
| R-33 | Risk | Vendor import interface proves unsuitable for pre-filling | PDS | Open, feasibility study |

## 5. Christmas planning

- Deployment freeze from 2026-12-21 to 2027-01-01. The last model version of the year goes live after the December retraining, at the latest on 2026-12-15.
- Second senior role active from 2026-12-14 to 2027-01-08, as agreed in the summer review.
- New HS code reference list for 2027 to be loaded in the first week of January; Jan's team prepares it in December.

## 6. Next steps

| Action | Owner | Due |
|---|---|---|
| First call with declaration system vendor | PDS, JW | 2026-11-10 |
| eCMR technical exchange with two hauliers | JW, AE | 2026-11-13 |
| Peak staffing plan for Christmas | JW | 2026-11-13 |
| One-page quarterly summary for Koen | PDS | 2026-11-20 |
| Interim results of the validation pilot | AE | 2026-11-27 |

Amira El Idrissi
