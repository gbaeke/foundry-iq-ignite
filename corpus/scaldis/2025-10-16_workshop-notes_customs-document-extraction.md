# Workshop Notes: Document Inventory and Prioritisation

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Customs Document Extraction |
| **Date** | 2025-10-16 |
| **Location** | Customs desk, Scaldis terminal building B |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |
| **Document type** | Workshop notes |
| **Participants** | Jan Wouters (Customs Coordinator, product owner), three customs agents (one senior), Pieter De Smet, Amira El Idrissi |

## 1. Goal

Make an inventory of the documents that reach the customs desk, estimate volumes and keying effort per type, and agree on the order in which we build extraction models.

## 2. Inventory

Jan's team counted documents over the two weeks before the workshop. Volumes are per week, rounded.

| Document type | Volume / week | Channel | Main language(s) | Keying effort |
|---|---|---|---|---|
| Commercial invoice | 820 | Mail | EN, DE, NL | High, many fields |
| Packing list | 640 | Mail | EN | Medium |
| CMR consignment note | 590 | Paper (scanning station), some mail | NL, FR, DE | Medium, often hard to read |
| Certificate of origin | 210 | Mail | EN, FR | Low |
| T1 transit document | 180 | Mail, paper | NL, FR | Medium |
| Bill of lading | 170 | Mail | EN | Medium |
| EUR.1 movement certificate | 95 | Paper, mail | EN, FR, DE | Low |
| Dangerous goods declaration | 80 | Mail | EN | High, critical fields |
| Delivery orders (various formats) | 150 | Mail | EN, NL | Low |
| Other (phytosanitary, weighing, warehouse notes…) | ~200 | Mixed | Mixed | Varies |

About 3,100 documents per week in total, of which roughly a quarter on paper.

## 3. Pain points mentioned by the customs agents

- Commercial invoices from the same shipper change layout without warning.
- CMR notes arrive crumpled, stamped over and with handwriting. "Sometimes the driver writes the seal number on top of the printed one."
- HS codes and gross weight are the fields where a typo hurts most: wrong duty or a mismatch with the weighing data at the gate.
- Peaks on Monday mornings and before holidays; in summer the backlog grows when colleagues are on leave.

## 4. Prioritisation

We scored each type on volume × keying effort × feasibility. Jan decided the order:

1. Commercial invoice
2. Packing list
3. CMR consignment note
4. Certificate of origin
5. T1 transit document
6. Bill of lading
7. Dangerous goods declaration
8. EUR.1 movement certificate

These eight are the phase 1 target ("at least 8 types" in the statement of work). Delivery orders and the "other" group follow if time and budget allow.

Jan was clear that CMR stays high on the list despite the expected difficulty: "if we skip CMR, the paper pile stays and nothing changes for my team".

## 5. Critical fields

Agreed list of fields that are critical across types, because an error has direct customs or safety consequences:
- container number
- HS code (per line)
- gross weight
- number of packages
- UN number and class (dangerous goods)
- seal number (CMR, bill of lading)

These will get stricter thresholds and always be visible first in the validation screen.

## 6. Samples

Jan's team will collect at least 50 historical samples per priority type, with personal data left in (processing stays in the Scaldis tenant) and labelling done in the tenant. For commercial invoices we ask for at least 150, spread over the top 30 shippers.

## 7. Next steps

| Action | Owner | Due |
|---|---|---|
| Labelling guidelines draft | AE | 2025-10-24 |
| Collect samples, first four types | JW | 2025-10-29 |
| Proposal for accuracy thresholds per field | AE, PDS | 2025-10-30 |
| Book four hours per week of agent time for labelling | JW | 2025-10-20 |

Amira El Idrissi
