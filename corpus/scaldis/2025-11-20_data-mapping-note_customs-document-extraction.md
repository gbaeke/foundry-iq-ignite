# Data Mapping Note: Extracted Fields to Declaration Data

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Customs Document Extraction |
| **Date** | 2025-11-20 |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |
| **Document type** | Data mapping note |
| **Reviewed by** | Jan Wouters, Pieter De Smet |

## 1. Purpose

Phase 1 does not submit anything to the customs declaration system. Agents still create the declaration themselves, from a validated export instead of from paper. This note maps every extracted field to the data element the agent needs and defines the export layout.

## 2. Principles

- One export record per container, combining all validated documents for that container.
- Field names in the export follow the names the customs agents use in the declaration screens, not the names on the source documents.
- Values are normalised (dates ISO, weights in kg with a dot as decimal separator, country codes ISO 3166 alpha-2).
- Each exported value keeps a reference to its source document and page, so an agent can always go back to the original.
- When two documents disagree (for example gross weight on the invoice and on the packing list), both values are exported and the conflict is flagged. The agent decides.

## 3. Mapping for the first three document types

| Export field | Commercial invoice | Packing list | CMR | Notes |
|---|---|---|---|---|
| container_number | if present | if present | box 18 / remarks | Validated with ISO 6346 check digit |
| consignor_name, consignor_country | seller | shipper | box 1 | Country normalised |
| consignee_name, consignee_country | buyer | consignee | box 2 | |
| invoice_number, invoice_date | header | reference | — | |
| incoterm | header | — | — | Code + place |
| currency, invoice_total | totals | — | — | |
| line[n].description | line items | line items | box 9 | |
| line[n].hs_code | line items | — | — | Critical field; 6 to 10 digits kept as text |
| line[n].quantity, unit | line items | line items | box 7 | |
| line[n].net_weight_kg | line items (if present) | line items | — | |
| gross_weight_kg | totals (if present) | totals | box 11 | Critical field; conflicts flagged |
| packages_count | — | totals | box 7 | Critical field |
| seal_number | — | — | box 18 / handwritten | Critical field |
| place_and_date_of_taking_over | — | — | box 4 | Often handwritten |

The mapping for certificate of origin, T1, bill of lading, dangerous goods declaration and EUR.1 follows in sprint 6 and later, as each model is trained.

## 4. Master data and reference checks

The workflow checks extracted values against reference data before they reach the validation screen:
- **HS codes** against a reference list maintained by the customs desk (updated yearly in January). An unknown code is not corrected, only flagged.
- **Country names** against a mapping table that includes Dutch, French and German spellings ("Duitsland", "Allemagne", "Deutschland").
- **Shipper names** against a list of the top 200 shippers kept by Jan's team. Matching uses the VAT or EORI number when present; otherwise a normalised name. About 6% of invoices in the samples use a trading name that differs from the registered name.

The shipper list turned out to contain duplicates: several shippers appear twice after mergers or with and without the legal form. Jan's team will clean it up; until then we match on identifiers first.

## 5. Open questions

- Should net weight be summed from line items when the invoice has no total? Jan: no, export only what is on the document.
- How to handle invoices covering several containers? Proposal: split lines by container if marked, otherwise attach the full invoice to each container and flag it.

## 6. Next steps

| Action | Owner | Due |
|---|---|---|
| Export file layout v1 for the parallel run | AE | 2025-11-26 |
| Clean-up of the shipper reference list | JW's team | 2026-01-16 |
| HS code reference list 2026 version | JW | 2026-01-09 |

Amira El Idrissi
