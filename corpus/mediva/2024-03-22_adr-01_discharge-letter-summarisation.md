# ADR-01: Model Deployment, Region and Pseudonymisation Boundary

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Discharge Letter Summarisation |
| **Document type** | Architecture decision record |
| **Date** | 2024-03-22 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Status** | Accepted |
| **Reviewed by** | Jeroen Lambrecht (Mediva IT), Sarah Mertens (DPO) |

## Context

The project generates draft discharge letters from sections of the patient record. The DPIA, closed on 2024-03-11, sets binding conditions: no patient data leaves the EU, pseudonymisation before any model call, pseudonymised logging only, and the pseudonymisation key managed by Mediva IT. We need to fix where the model runs, where the pseudonymisation boundary sits and what is logged, before the prototype phase starts on 2024-04-15.

## Options considered

**Option A: Azure OpenAI deployment in an EU region, pseudonymisation inside Mediva's network.**
Record extracts are pseudonymised by a service running in Mediva's environment. Only pseudonymised text crosses to the Azure OpenAI endpoint. Re-identification happens in the same Mediva-side service before the draft is shown.

**Option B: Azure OpenAI deployment in an EU region, pseudonymisation in the cloud application layer.**
Simpler to operate, but identifiable data would sit in an additional cloud component, and the key would need to be reachable from there. Sarah indicated this would require an update of the DPIA.

**Option C: A locally hosted open-weight model on Mediva hardware.**
No data leaves the hospital. Rejected: Mediva has no GPU capacity, the quality of available models for Dutch clinical text was clearly lower in our first tests, and procurement would not fit the project timeline.

## Decision

**Option A.**

- One Azure OpenAI resource in an EU region, in a subscription owned by Mediva. Kestrel works through named accounts that Jeroen's team grants and revokes.
- The modified abuse-monitoring arrangement requested with Microsoft so that prompts and completions are not retained for human review; confirmation filed with the DPIA.
- No data is used for model training.
- The pseudonymisation and re-identification service runs inside Mediva's environment. The key is managed by Mediva IT; Kestrel has no access.
- Prompts and outputs are logged only after pseudonymisation, with 90 days retention, for quality review.

## Data flow

1. The physician opens the draft function for a stay in the record.
2. The integration reads the relevant sections (admission note, progress notes, lab summary, medication list, specialist reports) from the read-only extract.
3. The pseudonymisation service replaces direct identifiers with pseudonyms and removes free-text identifiers it recognises.
4. The pseudonymised sections and the specialty template go to Azure OpenAI.
5. The draft comes back, is re-identified inside Mediva's environment and shown next to its source sections.
6. The physician edits and signs in the record. The signed letter is never sent back to the model.

## Consequences

- All prompt engineering and evaluation work is done on pseudonymised data. Kestrel engineers never see identifiable content.
- Latency increases by the pseudonymisation step; target is a draft within 30 seconds.
- Any change to steps 2 to 5 is a change to the data flow and goes to Sarah before implementation (kickoff decision D3).
- Costs: model consumption is billed directly to Mediva. We will report token usage per letter from the prototype phase onwards so Jeroen can estimate yearly cost.

## Open points

- Residual identifier rate after pseudonymisation: Amira reports on 2024-04-05.
- Content filtering: the default filters occasionally flag clinical vocabulary. To be measured in the prototype phase.
