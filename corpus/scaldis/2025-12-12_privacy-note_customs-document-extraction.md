# Privacy Note: Personal Data in Customs Documents

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Customs Document Extraction |
| **Date** | 2025-12-12 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Privacy note |
| **Reviewed with** | Scaldis data protection contact (2025-12-09), Jan Wouters |
| **Status** | Approved for production use |

## 1. Why this note

The architecture review of 10 October asked for a short assessment of personal data before production. Most customs documents describe goods and companies, but several types contain data about natural persons. This note describes what is processed, why, and which measures apply. It was discussed with the Scaldis data protection contact, who concluded that a full impact assessment is not required for phase 1, given the measures below and the fact that the processing replaces manual keying of the same data.

## 2. Personal data found in the samples

| Document type | Personal data | Needed for customs? |
|---|---|---|
| CMR consignment note | Driver name, signature, truck and trailer licence plates, sometimes phone number | Licence plates yes; driver name sometimes; signature no |
| Commercial invoice | Contact person name, e-mail and phone of seller or buyer | No |
| Packing list | Contact person name | No |
| T1 transit document | Name of the person lodging the document | Yes |
| Bill of lading | Rarely: notify party being a private person | Sometimes |

No special categories of personal data were found. Private individuals as consignee are rare (removals, personal effects) and handled manually.

## 3. Principles applied

1. **Purpose.** Data is processed only to prepare customs declarations, the same purpose as today's manual keying.
2. **Minimisation.** Extraction models do **not** extract fields that are not needed: signatures, contact persons on invoices and packing lists, phone numbers and e-mail addresses are left on the image and not stored as data.
3. **Location.** All processing in the Scaldis tenant, West Europe: Azure AI Document Intelligence, Azure Logic Apps and storage. No data leaves the tenant; Kestrel staff work on it only through Scaldis accounts.
4. **Access.** Validation screen limited to customs desk staff. Kestrel's access is limited to the labelling and test sets and is removed at the end of the engagement.
5. **Retention.** The original document is already archived by the customs desk under the legal retention rules. The project store keeps its own copy of the image and the extracted data for **90 days** after the container is released, for corrections and accuracy measurement, then deletes it. Labelled training samples are kept for the duration of the project and reviewed every quarter.
6. **Logs.** Workflow run history contains document IDs, types and timings, never field values.

## 4. Training data

Labelled samples contain real documents with personal data. Measures:
- labelling in the tenant only, no exports to laptops;
- driver names and signatures are not labelled, so the models never learn to extract them;
- when a sample is no longer used for training or testing, it is deleted;
- the sample register lists for each sample its source and deletion date.

## 5. Rights of data subjects

Requests from drivers or contact persons are handled through the existing Scaldis procedure. The project store can be searched by container number and date, which is enough to locate a document within the 90-day window.

## 6. Residual risks

| Risk | Measure |
|---|---|
| Free-text remarks on CMR notes can contain personal data (for example "driver called M. at depot") | Remarks field is extracted for review but excluded from the export, until Jan decides it is needed |
| Agents may export more than needed | Export layout fixed; no free columns |
| Samples kept longer than needed | Quarterly review of the sample register by Amira and Jan |

## 7. Actions before production

| Action | Owner | Due |
|---|---|---|
| Remove signature and contact fields from labelling schema | AE | 2025-12-19 |
| Retention job (90 days) in place and tested | PDS | 2026-01-23 |
| Sample register set up | AE | 2026-01-09 |
| Add processing to the Scaldis record of processing activities | Scaldis data protection contact | 2026-01-31 |

Pieter De Smet
