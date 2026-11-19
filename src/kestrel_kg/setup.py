"""Create, inspect and delete the Foundry IQ objects for the demo.

Usage:
    uv run python -m kestrel_kg.setup create   # entity graph knowledge source + knowledge base
    uv run python -m kestrel_kg.setup status   # sync state and generated resource names
    uv run python -m kestrel_kg.setup delete   # knowledge base, then knowledge source

The ontology can't change after the source exists (no ingestion cache configured), so an
ontology change means delete + create. With 34 small documents that's cheap.
"""

from __future__ import annotations

import json
import sys

from kestrel_kg.client import ROOT, SearchClient

ENTITY_KS = "kestrel-entities-ks"
ENTITY_KB = "kestrel-entities-kb"
GRAPH_NAME = "kestrel"


def _model(c: SearchClient, deployment: str, model_name: str) -> dict:
    return {
        "kind": "azureOpenAI",
        "azureOpenAIParameters": {
            "resourceUri": c.settings.model_endpoint,
            "deploymentId": deployment,
            "modelName": model_name,
        },
    }


def entity_source_body(c: SearchClient) -> dict:
    ontology = json.loads((ROOT / "ontology" / "ontology.json").read_text())
    return {
        "name": ENTITY_KS,
        "kind": "azureBlob",
        "description": (
            "Kestrel Consulting project documents: proposals, SOWs, status reports, meeting notes, "
            "closing reports and internal memos for customer projects 2023-2026."
        ),
        "resultsProcessing": "none",
        "azureBlobParameters": {
            "connectionString": f"ResourceId={c.settings.storage_resource_id}",
            "containerName": c.settings.container_name,
            "ingestionParameters": {
                "contentExtractionMode": "minimal",
                "disableImageVerbalization": True,
                "chatCompletionModel": _model(c, c.settings.chat_deployment, "gpt-5.6-luna"),
                "embeddingModel": _model(c, c.settings.embedding_deployment, "text-embedding-3-small"),
            },
            "graphExtraction": {
                "graphName": GRAPH_NAME,
                "pageDegreeOfParallelism": 2,
                "ontology": {
                    "kind": "inline",
                    "name": "kestrel-v2",
                    "value": json.dumps(ontology, separators=(",", ":")),
                },
            },
        },
    }


def entity_base_body(c: SearchClient) -> dict:
    return {
        "name": ENTITY_KB,
        "description": "Kestrel project knowledge: an entity graph of people, projects, customers and technologies.",
        "knowledgeSources": [{"name": ENTITY_KS}],
        "models": [_model(c, c.settings.chat_deployment, "gpt-5.6-luna")],
        "retrievalReasoningEffort": {"kind": "low"},
        "outputMode": "extractiveData",
        "retrievalInstructions": (
            "Use graph_search for questions about who worked on what, which projects used a technology, "
            "counting, comparisons across customers and relationships between people, projects and organizations. "
            "Use text search for specific numbers, dates, amounts and narrative detail, and also run text search "
            "whenever a graph query returns no rows. "
            "Graph schema facts: every Project in this graph is a Kestrel Consulting project, so never filter on "
            "'Kestrel Consulting'. deliveredFor always points to the CUSTOMER organization (Scaldis Logistics, "
            "Mediva Care Group, Fortalis Verzekeringen, Verhaeghe Foods, AquaNova). "
            "Entity names can be partial or vary (first name only, short customer names such as 'Fortalis', "
            "project names without the customer prefix), so match names with CONTAINS on the most distinctive "
            "part (surname, or the core project words) instead of exact equality, and count DISTINCT entities. "
            "Customer contacts link to projects with sponsors, productOwnerOf or contactFor; consultants with "
            "workedOn or managedProject."
        ),
    }


def create() -> None:
    c = SearchClient()
    c.put(f"/knowledgesources('{ENTITY_KS}')", entity_source_body(c))
    print(f"created knowledge source {ENTITY_KS}")
    c.put(f"/knowledgebases('{ENTITY_KB}')", entity_base_body(c))
    print(f"created knowledge base {ENTITY_KB}")


def status() -> None:
    c = SearchClient()
    ks = c.get(f"/knowledgesources('{ENTITY_KS}')")
    st = c.get(f"/knowledgesources('{ENTITY_KS}')/status")
    print(json.dumps({"createdResources": ks["azureBlobParameters"].get("createdResources"), "status": st}, indent=2))


def delete() -> None:
    c = SearchClient()
    for path in (f"/knowledgebases('{ENTITY_KB}')", f"/knowledgesources('{ENTITY_KS}')"):
        try:
            c.delete(path)
            print(f"deleted {path}")
        except RuntimeError as e:
            print(f"skip {path}: {e}")


def main() -> None:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    {"create": create, "status": status, "delete": delete}[cmd]()
