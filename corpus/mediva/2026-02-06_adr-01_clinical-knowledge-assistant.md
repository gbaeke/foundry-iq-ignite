# ADR-01: Knowledge Base Design with Foundry IQ

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Clinical Knowledge Assistant |
| **Document type** | Architecture decision record |
| **Date** | 2026-02-06 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Status** | Accepted |
| **Reviewed by** | Amira El Idrissi; Jeroen Lambrecht (Mediva IT) |

## Context

The assistant must answer clinical staff questions only from Mediva-approved guidelines and protocols, cite document, version and date, and say so when the sources do not answer the question. Questions are often compound: "What is the protocol for chest pain with suspected dissection in a patient on anticoagulants, and when do we call cardiology?" touches two departments and three documents. The SOW names a Foundry IQ knowledge base with agentic retrieval; this ADR records how we set it up and why.

## Options considered

**Option A: Hand-built retrieval pipeline.** Our own chunking, embedding, ranking and a single retrieval call per question, orchestrated in code. Full control, but we would rebuild query planning and multi-source merging ourselves, and own all of it after handover.

**Option B: Foundry IQ knowledge base with agentic retrieval.** Knowledge sources per source library, a knowledge base on top, and agentic retrieval that plans sub-queries, runs them over the sources and returns grounded results with references. The assistant in Microsoft Foundry uses the knowledge base as its retrieval layer and an Azure OpenAI model to write the answer.

**Option C: Long-context prompting.** Put the relevant department's guidelines in the prompt. Rejected: emergency alone has about 340 documents, cost per question would be high, and citations would be unreliable.

## Decision

**Option B.**

- One knowledge base for the pilot, with separate knowledge sources for the intranet library export, the confirmed legacy documents and the emergency nursing procedures.
- Agentic retrieval enabled; the retrieval instructions tell the planner to prefer documents of the department the user selects in the front end, without excluding others.
- Answer generation with an Azure OpenAI chat model deployed in the EU region, from the Microsoft Foundry project.
- Every result carries document title, version, publication date and link; the answer instructions require at least one citation per statement and an explicit "not found in Mediva sources" when retrieval returns nothing relevant.
- All resources in Mediva's subscription in an EU region.

## Metadata as filters

The knowledge sources carry department, document type, version and review date as filterable fields. Where the metadata is missing, Amira's ingestion step derives version and date from the cover page or file name and marks the field as "derived". Of the 550 cardiology and emergency documents analysed, version information was missing or ambiguous for about 18%.

This matters because the assistant can only show the right version if the index knows it. Derived values are a stopgap, not a substitute for owners confirming the current version.

## Consequences

- Less custom code to hand over; query planning behaviour depends on the platform and must be covered by the evaluation set.
- Retrieval behaviour can change with platform updates. We pin settings where possible and rerun the full evaluation set after every change to sources, instructions or model deployment.
- Consumption has two parts: retrieval (query planning plus searches) and answer generation. We will report both per question from the first demo, so Jeroen can forecast.
- Agentic retrieval adds latency compared with a single search. Target: answer start within 6 seconds, complete within 15 seconds for 90% of questions.

## Out of scope

- Patient record content of any kind.
- Writing back to the guideline library. The assistant never modifies sources.
- Mobile apps.

## Open points

- Refresh frequency of the knowledge sources: daily is the starting assumption; to be aligned with the coordinators' publication rhythm.
- How superseded documents are recognised when owners do not archive them. Raised in the source inventory workshop; tracked as a risk.
