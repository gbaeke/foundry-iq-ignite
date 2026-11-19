# Status Report: Discharge Letter Summarisation

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Discharge Letter Summarisation |
| **Document type** | Status report (biweekly) |
| **Date** | 2024-04-12 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Period** | 2024-03-18 to 2024-04-12 (foundation phase) |
| **Distribution** | Dr. Hilde Van Damme, Jeroen Lambrecht, Sarah Mertens |

## 1. Overall status

| Area | Status | Comment |
|---|---|---|
| Overall | Green | Foundation phase closed on the re-planned date |
| Scope | Green | Scanned documents excluded and flagged, agreed with DPO |
| Planning | Green | Prototype phase starts Monday 2024-04-15 |
| Budget | Green | Fixed price; first invoice (30%) sent |
| Privacy | Green | Pseudonymisation v0.4 accepted by DPO |

## 2. Progress

- **Environment.** Jeroen's team delivered the test environment, the read-only extract of the record and the named access for Amira and Pieter. The Azure OpenAI resource runs in an EU region in Mediva's subscription, as recorded in ADR-01.
- **Pseudonymisation.** Amira's test on 200 sample letters found residual direct identifiers in 0.47% of sections with version 0.3. Version 0.4 brought this to zero on the same sample. Sarah accepted version 0.4 for the prototype phase on 2024-04-08 and asked for a repeat test before the evaluation.
- **Architecture.** ADR-01 accepted: pseudonymisation and re-identification inside Mediva's environment, pseudonymised logs with 90 days retention, no data used for training.
- **Pilot departments.** Internal medicine and geriatrics confirmed. Dr. Van Damme has asked both heads of department for evaluation physicians.
- **Scanned documents.** Older scanned notes without text are skipped and flagged in the draft. No change to the data flow.

## 3. Plan for the prototype phase (2024-04-15 to 2024-06-07)

| Sprint | Dates | Goal |
|---|---|---|
| P1 | 15 to 26 April | Letter structure per specialty; template workshop with physicians |
| P2 | 29 April to 17 May | Section selection from the record; first drafts on historical stays |
| P3 | 20 May to 7 June | Review screen with sources next to draft; prototype acceptance |

Note that 1 May, Ascension (9 May) and Whit Monday (20 May) fall in this phase. Sprint P2 is three weeks long for that reason.

## 4. Risks and issues

| # | Type | Description | Owner | Mitigation |
|---|---|---|---|---|
| R1 | Risk | Evaluation falls in the summer holidays; physicians unavailable | HVD, TM | Recruit by 19 April; baseline period before mid-July |
| R2 | Risk | Draft quality for long stays (more than 20 days) too low because of input size | PDS | Section selection and summarisation per section in sprint P2 |
| R3 | Risk | Content filter flags clinical vocabulary and blocks drafts | AE | Measure on historical stays; discuss settings with Mediva IT |
| R4 | Risk | Residual indirect identifiers in free text | AE, SM | Repeat test before evaluation; report monthly |
| R5 | Issue | Scanned documents without text layer cannot be used | PDS | Skip and flag; revisit only on physician request |

## 5. Decisions needed

None this period.

## 6. Next steps

| Action | Owner | Due |
|---|---|---|
| Template workshop with physicians of both departments | AE | 2024-04-26 |
| Names of evaluation physicians | HVD | 2024-04-19 |
| First drafts on 50 historical stays | AE, PDS | 2024-05-10 |
| Token usage per draft, first cost estimate for Mediva | PDS | 2024-05-15 |
| Steering committee 1 | TM | 2024-05-15 |

*Thomas Maes, Kestrel Consulting*
