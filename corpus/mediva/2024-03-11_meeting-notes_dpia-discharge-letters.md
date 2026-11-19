# Meeting Notes: DPIA Closure, Discharge Letter Summarisation

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Discharge Letter Summarisation |
| **Document type** | Meeting notes |
| **Date** | 2024-03-11, 14:00 to 15:30 |
| **Location** | Mediva, campus admin building, meeting room "Leie" + Teams |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |

## Attendees

- Sarah Mertens, Data Protection Officer, Mediva Care Group (SM)
- Jeroen Lambrecht, IT Manager, Mediva Care Group (JL)
- Amira El Idrissi, ML Engineer, Kestrel Consulting (AE)
- Pieter De Smet, Lead AI Architect, Kestrel Consulting (PDS)

## 1. DPIA status

Sarah confirmed that the Data Protection Impact Assessment for the discharge letter project is **completed** and signed off internally. She thanked the team for the input on the data flows and the architecture diagram; the description of what goes into the prompt and what comes back was the part the hospital's privacy committee looked at most closely.

Sarah's position from the first meeting stands: no patient data was to be processed before the DPIA was finished. That is why the project did not start on the originally planned date.

## 2. Impact on planning

The DPIA took longer than expected. The project start is delayed by **6 weeks**, from 2024-02-05 to **2024-03-18**. Jeroen confirmed that the test environment and the read access to the record extracts can be ready by then.

Pieter noted that the overall phasing stays the same; all milestones shift accordingly. Thomas Maes (Kestrel project manager, not present) will update the plan and inform the sponsor, Dr. Hilde Van Damme, before the next steering committee.

## 3. Conditions from the DPIA

The DPIA comes with conditions that are now binding for the project:

1. **Pseudonymisation is mandatory.** Patient names, national register numbers, addresses, dates of birth and other direct identifiers are replaced by pseudonyms before any content is sent to the language model. Re-identification happens only inside Mediva's environment when the draft is shown to the physician.
2. **No patient data leaves the EU.** All processing, including the Azure OpenAI deployment, logging and storage, runs in EU regions. Pieter confirmed the chosen region and that abuse-monitoring data retention has been reviewed with Microsoft.
3. **Logging:** prompts and outputs are logged only in pseudonymised form, with a retention period of 90 days for quality review.
4. **Access:** only named project members get access to the pseudonymised development dataset; the list is maintained by Jeroen.

## 4. Discussion

- Amira explained the pseudonymisation approach: a rule-based pass for structured identifiers plus a named-entity model for free text. Sarah asked how residual identifiers in free text (e.g. "the patient's daughter, a nurse on ward 3B") are handled. Agreed to test on a sample and report the residual rate.
- Jeroen raised the question of who owns the pseudonymisation key. Decision: Mediva IT, stored in Mediva's key vault; Kestrel has no access.
- Pieter asked whether the evaluation with physicians requires a separate assessment. Sarah: no, as long as it uses the same pseudonymised flow.

## Decisions

- D1: Project start confirmed for 2024-03-18.
- D2: Pseudonymisation before any model call is mandatory, without exception.
- D3: All processing and storage in EU regions only.
- D4: Pseudonymisation key managed by Mediva IT.

## Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Share final DPIA conditions document with the project team | SM | 2024-03-13 |
| 2 | Provide test environment and read access to record extracts | JL | 2024-03-15 |
| 3 | Test pseudonymisation on 200 sample letters, report residual identifier rate | AE | 2024-04-05 |
| 4 | Update architecture document with DPIA conditions and EU-region confirmation | PDS | 2024-03-18 |
| 5 | Confirm access list for the development dataset | JL | 2024-03-15 |

Next check-in with Sarah: 2024-04-08.
