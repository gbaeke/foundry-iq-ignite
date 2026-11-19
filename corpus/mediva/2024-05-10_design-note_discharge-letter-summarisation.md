# Design Note: Section Selection and Prompt Structure

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Discharge Letter Summarisation |
| **Document type** | Technical design note |
| **Date** | 2024-05-10 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Reviewers** | Amira El Idrissi; Jeroen Lambrecht (integration part) |

## 1. Problem

A stay in internal medicine produces on average 60 to 80 record sections; long geriatric stays easily exceed 200. Sending everything to the model in one prompt is slow, expensive, and in our first tests on 50 historical stays it produced vague course-of-stay paragraphs: the model summarised the most recent notes and forgot the first week. This note describes the two-step approach used from sprint P2 onwards.

## 2. Step 1: select and condense sections

**Selection rules (deterministic, in code):**

- Always included: admission note, discharge medication list, admission medication list, last progress note, consult reports of other specialties, the lab summary table.
- Progress notes: one per day maximum, preferring the note of the treating physician over nursing notes.
- Imaging and procedure reports: only the conclusion paragraph.
- Excluded: administrative notes, scanned documents without text (flagged), duplicated copies of the same report.

**Condensation per problem.** For stays with more than 40 selected sections, a first model call condenses the progress notes per problem, using the problem list of the stay as headings. Each condensed sentence keeps a reference to the section it came from. This intermediate result is never shown to the physician as such; it is input for step 2.

## 3. Step 2: draft the letter

The second call receives:

1. The specialty template (internal medicine or geriatrics, from the workshop of 2024-04-26)
2. Instructions on style: Dutch, one page target, no stronger wording than the source, no advice not present in the notes
3. The medication comparison computed in code (started / stopped / changed), with the request to find and phrase the reason for each change
4. The selected and condensed sections, each with its section identifier

The output is structured per template paragraph, with the section identifiers that support each sentence. The review screen uses these identifiers to show the source next to the draft.

## 4. Why not retrieval over the full record?

We considered indexing all sections of a stay and retrieving per template paragraph. For a single stay the corpus is small, and the selection rules above are easier to explain to physicians and to the DPO than a ranking. The ADR-01 data flow also stays unchanged: same sections, same pseudonymisation, same endpoint.

## 5. First measurements (50 historical stays)

| Measure | Single prompt | Two-step |
|---|---|---|
| Average draft time | 41 s | 24 s |
| Average tokens per letter (in + out) | about 38,000 | about 17,000 |
| Course of stay mentions problems from week 1 | 54% | 92% |
| Statements without a supporting section | 7.1% | 1.9% |

The remaining unsupported statements are mostly general phrases ("the patient recovered well") that physicians will judge in the evaluation.

## 6. Cost estimate

At about 17,000 tokens per letter and the current list prices for the deployed model, the consumption cost is well under one euro per letter. For the two pilot departments together (roughly 4,500 letters per year), Jeroen can budget a low four-digit amount per year for model consumption. We will refine this with real usage during the pilot.

## 7. Content filter

On the 50 stays, the default content filter blocked 3 drafts, all because of descriptions of self-harm or violence in the history. Jeroen's team has requested an adjusted filter configuration for this clinical use case. Until then, blocked drafts show a clear message and the physician writes the letter as usual.

## 8. Integration

The draft function is opened from the record with the stay key. The integration layer, maintained by Mediva IT, passes the key to the Mediva-side service, which reads the extract, pseudonymises, calls the model twice, re-identifies and returns the draft. Nothing is written back to the record automatically; the physician copies or adapts the text in the letter editor.

## 9. Next steps

- Apply to 200 historical stays for the physician review on 2024-05-24 (Amira).
- Review screen with source references (sprint P3).
- Re-measure unsupported statements after template v2.
