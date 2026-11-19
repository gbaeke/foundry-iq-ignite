# Data Mapping Note: Historical claims extract

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Data mapping note |
| **Date** | 2024-04-26 |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |
| **Reviewed by** | Laura Vermeulen, Claims Operations Manager |

## 1. The extract

The claims system team delivered the historical extract on 2024-04-24 into the project storage in the Fortalis spoke. It covers claims registered between October 2022 and March 2024 (18 months) for private customers.

| Item | Count |
|---|---|
| Claims (all types) | 54,812 |
| Of which motor, fire, theft | 38,960 |
| Attached documents | 171,400 (PDF, JPEG, a few TIFF and word-processor files) |
| Claims without any document | 6,140 (mostly phone reports, excluded) |

## 2. Field mapping

| Target field | Source | Quality notes |
|---|---|---|
| Claim ID | `CLM_NR` | Unique, reliable |
| Policy number | `POL_NR` | Empty in 7% of claims at registration; filled in later. We use the value at registration for training, otherwise the model learns from information it will not have at intake. |
| Date of loss | `DT_SINISTRE` | Sometimes equals the registration date as a default; 4% suspect |
| Channel | `CANAL` | Values MAIL, MAKELAAR, PORTAAL plus legacy code "X" (meaning unknown) |
| Claim type (final) | `TYPE_FINAL` | 41 codes; mapped to the 6 types agreed in the workshop of 2024-04-19 |
| Claim type (at intake) | `TYPE_INIT` | Differs from final type in 11% of claims |
| Queue history | separate table | Allows us to see re-routing |
| Urgency flag | `URG` | Y/N only, used inconsistently, not usable as a label |
| Complexity | not available | Must be labelled |
| Free text description | `OMSCHR` / `DESCR` | Two columns depending on language of the form; to be merged |

## 3. Code mapping for claim type

The 41 final type codes were mapped with Laura and one senior handler. Examples:

| Source codes | Target type |
|---|---|
| AUTO-EIG, AUTO-OMNIUM, AUTO-GLAS | Motor (own damage) |
| AUTO-BA, AUTO-RC | Motor (third party) |
| BRAND, BRAND-ROOK, BLIKSEM | Fire |
| DIEF-WON, VOL-HAB | Theft from home |
| DIEF-VTG, VOL-VEH | Theft of vehicle |
| WATER-*, STORM-*, GLAS-WON, others | Other |

Note: the water codes and storm codes fall under "other" because they are not in scope for this phase. They represent a large share of the "other" group, about 9,000 claims in the extract.

## 4. Data quality findings

- **Duplicates.** 3.2% of claims have a near-identical twin (same policy, same date of loss, registered through a different channel within two days). Most were merged later in the system, but the documents stayed attached to both. We drop the twin with fewer documents.
- **Language columns.** Dutch and French descriptions are stored in different columns; about 600 claims have text in both. Merged with a language tag.
- **Default dates.** Where the date of loss equals the registration date and the description mentions another date, we keep the record but flag it. Not a blocker for classification.
- **Document types.** Documents have no reliable type label. Filenames are anything from "scan0001.pdf" to the full claim description. We will classify document types as a first step in Document Intelligence.

## 5. Implications for labelling

- Claim type can be derived from `TYPE_FINAL` after mapping. No manual labelling needed, only a check on a sample of 300.
- Complexity and urgency must be labelled manually. Target: 4,000 claims by end of July, stratified per type and channel.
- Labelling is done in a simple labelling screen inside the spoke. Claim data does not leave the Fortalis environment.

## 6. Open questions

1. Can the claims system team add the queue history for the last two months, so we can test on recent data? (Laura)
2. Do we keep the legacy channel code "X" or drop those 1,100 claims? Proposal: keep, mark as unknown. (Amira)

*Amira El Idrissi*
