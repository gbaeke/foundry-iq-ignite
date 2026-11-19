# Technical Design Note: Indexing Pipeline Proof of Concept

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Scaldis Ops Copilot |
| **Date** | 2025-02-14 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Technical design note |
| **Related** | ADR-01 chunking strategy, ADR-02 answer language and citations |

## 1. Scope of the proof of concept

Action 7 of the kick-off: index one SharePoint site end to end and answer questions over it. We used the "Operations – Quay" site: 214 documents (SOPs, work instructions, checklists), mostly text documents and PDFs, 61% Dutch, 27% French, 12% English.

## 2. Pipeline

1. **Crawl.** An indexing job lists documents in the in-scope libraries through the SharePoint API, using an app identity with read access granted by the site owner. Only published major versions are taken; drafts are skipped.
2. **Extract.** Text and headings are extracted per document. Scanned PDFs without a text layer (9 of 214) are reported to the site owner instead of being processed.
3. **Chunk.** One chunk per section, split on headings; sections longer than about 600 tokens are split on paragraph boundaries with a small overlap. Each chunk keeps the document title, section path, SOP number, language and version date (ADR-01).
4. **Embed and index.** Chunks are embedded with an Azure OpenAI embedding model and written to an Azure AI Search index with both a text field and a vector field.
5. **Refresh.** Nightly incremental run based on the document modified date; deletions detected by comparing the document list.

## 3. Query flow

1. The question from the Teams bot is sent with its detected language.
2. Hybrid query on Azure AI Search: keyword and vector, merged and re-ranked by the semantic ranker; top 5 chunks.
3. Prompt to the Azure OpenAI chat model with the chunks, the instruction to answer only from the chunks and to cite SOP number and section.
4. Answer is returned in the question's language with citation links (ADR-02).

## 4. First results

We ran 40 questions written by two shift leaders against the PoC.

| Measure | Result |
|---|---|
| Correct source in top 5 | 35 / 40 |
| Answer judged correct and complete | 29 / 40 |
| Answer judged correct but incomplete | 6 / 40 |
| Wrong or invented answer | 2 / 40 |
| "Not found" when the answer did exist | 3 / 40 |

The two wrong answers came from an outdated checklist that still sits next to its replacement in the same library. This will come back: version hygiene in the SOP libraries is a content issue, not something the pipeline can solve. We will report duplicates and old versions to Nathalie's team.

French questions over Dutch-only SOPs work well; the answer is in French with a note that the source is in Dutch.

## 5. Not yet addressed

- **Permissions.** The PoC site is readable by all operations staff, so every user may see every chunk. Restricted sites will need a decision before they enter scope. Flagged for Wim Goossens' security review; we propose to discuss it at the steering committee.
- **Images and tables.** Several SOPs are mostly diagrams. Only the captions are indexed today.
- **Cost.** Embedding all 1,800 documents is a one-off cost of a few euros; query cost depends on usage. Consumption alerts set up by Thomas cover the resource group.

## 6. Proposed next steps

- Extend to all operations sites in sprint 3 and 4.
- Add a "version date" field to the answer card, as Elien proposed.
- Build a test set of 120 questions with Nathalie's team for regression testing.
- Prepare the permissions question for the steering committee of 2025-02-20.

Pieter De Smet
