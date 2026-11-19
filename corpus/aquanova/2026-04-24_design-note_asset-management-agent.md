# Design Note: Foundry IQ Knowledge Base for Asset Documents

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Asset Management Agent |
| **Date** | 2026-04-24 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Technical design note |
| **Reviewed by** | Kevin Hermans, Jonas Peeters |

## 1. Purpose

Describe how the knowledge base in Foundry IQ is set up for the agent, what it contains, and what we learned from the first evaluation run on 2026-04-17.

## 2. Sources

| Knowledge source | Library | Documents | In phase 1 dev | Notes |
|---|---|---|---|---|
| Maintenance procedures | Procedures | about 380 | yes | owner: asset management |
| Technical sheets | Technical documentation | about 2,700 | yes | many supplier PDFs, several languages |
| Inspection reports | Inspections (3 libraries) | about 9,200 | from June | needs private networking (ADR-01) |

Each library becomes a separate knowledge source in the knowledge base, so we can tune and refresh them separately and show the planner where an answer came from.

## 3. How the agent uses it

- The agent in Foundry Agent Service calls the knowledge base for any question about procedures, specifications or inspection findings.
- Foundry IQ plans the retrieval: it can split a question into sub-queries ("inspection interval" and "hydrant type in residential street") and combine the results.
- The agent answers only from retrieved content and always lists the sources with a link.
- If nothing relevant is found, the agent says so. The instructions are explicit: no general knowledge about water networks in place of AquaNova's own procedures.

## 4. Metadata

For every document we keep: library, title, document date, asset type (when it can be derived from the folder or file name), and version status. Asset type filtering matters: "inspection interval" has a different answer for hydrants, valves and reservoirs.

## 5. First evaluation (2026-04-17)

Run on the 27 knowledge base questions of evaluation set v1 plus the 5 permission questions, scored by two planners.

| Category | Questions | Correct | Partly | Wrong |
|---|---|---|---|---|
| Procedure | 18 | 15 | 2 | 1 |
| Technical sheet | 9 | 7 | 1 | 1 |
| Permission ("no information") | 5 | 5 | – | – |

Procedures and technical sheets: 22 of 27 correct (81%), below the 85% target.

## 6. What went wrong

- **Two versions of the same procedure.** The Procedures library has old versions next to new ones, sometimes with the same title. In two cases the agent answered from the old one. The planners recognised it immediately.
- **Supplier sheets in German and French.** Retrieval works across languages, but the agent sometimes quoted the German text untranslated. Instructions updated.
- **Tables in PDFs.** One pressure rating came from the wrong row of a table. We now return the surrounding table rows with the answer, so the planner can check.

## 7. Changes

| # | Change | Status |
|---|---|---|
| 1 | Exclude documents marked as superseded; ask the library owner to archive old versions | asked, owner assigned for Procedures (I-02 partly resolved) |
| 2 | Answer in Dutch, quote source language only between quotes | done |
| 3 | Show table context for numeric answers | done |
| 4 | Add document date to every source link | done |

## 8. Scanned inspection reports

About 1,400 older inspection reports are scans without a text layer. In phase 1 they are excluded from the knowledge base (I-03). The agent says "an older inspection report exists but cannot be read" when the metadata shows one for the asset. Whether to convert them is a phase 2 question.

## 9. Next steps

- Second evaluation run after the changes, target 2026-05-08.
- Inspection reports from June, once private networking is ready.
