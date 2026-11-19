"""Our own graph agent: the model writes GQL itself, against the real schema and entity names.

It fixes three weaknesses of the managed knowledge base path:
- the model sees the ontology AND the entity names that actually exist in the graph
- it can combine graph queries with text search in one investigation
- a query that returns 0 rows is a signal to check the filters, not a final answer

The agent only gathers evidence. The shared answer step in strategies.py writes the answer,
so this strategy is compared on retrieval, like the others.
"""

from __future__ import annotations

import json
import time
from functools import lru_cache
from typing import Any

from kestrel_kg.client import ROOT, SearchClient, credential

GRAPH_INDEX = "kestrel-entities-ks-graph-index"
CHUNK_INDEX = "kestrel-entities-ks-index"
MAX_STEPS = 8
NAMED_LABELS = ("Person", "Organization", "Project", "Technology", "Place")

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "run_gql",
            "description": "Run a GQL query on the entity graph and return the rows (max 50).",
            "parameters": {
                "type": "object",
                "properties": {"gql": {"type": "string"}},
                "required": ["gql"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_text",
            "description": "Hybrid text search over the document chunks. Returns top passages with their source file.",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}, "top": {"type": "integer", "default": 5}},
                "required": ["query"],
            },
        },
    },
]


def run_gql(c: SearchClient, gql: str, graph_index: str = GRAPH_INDEX) -> list[dict[str, Any]]:
    r = c.post(f"/indexes('{graph_index}')/docs/search.graph", {"gql": gql})
    return [{k: v for k, v in row.items() if not k.startswith("@")} for row in r.get("value", [])][:50]


def search_text(c: SearchClient, query: str, top: int = 5, chunk_index: str = CHUNK_INDEX) -> list[dict[str, str]]:
    r = c.post(
        f"/indexes('{chunk_index}')/docs/search",
        {
            "search": query,
            "vectorQueries": [{"kind": "text", "text": query, "fields": "snippet_vector", "k": 50}],
            "queryType": "semantic",
            "semanticConfiguration": f"{chunk_index.removesuffix('-index')}-semantic-configuration",
            "select": "snippet,blob_url",
            "top": min(top, 10),
        },
    )
    return [{"source": d["blob_url"].split("/kestrel-corpus/")[-1], "text": d["snippet"]} for d in r["value"]]


@lru_cache(maxsize=4)
def catalog(c: SearchClient, graph_index: str = GRAPH_INDEX) -> str:
    """Entity names per label, read from the graph itself. Issues and outcomes are free text, so only counted."""
    lines = []
    for label in NAMED_LABELS:
        names = sorted(
            {r["name"] for r in run_gql(c, f"MATCH (n:{label}) RETURN DISTINCT n.name AS name LIMIT 500", graph_index)}
        )
        lines.append(f"{label} ({len(names)}): " + "; ".join(names))
    counts = run_gql(c, "MATCH (n) RETURN labels(n) AS l, count(*) AS n GROUP BY l", graph_index)
    lines.append("Node counts: " + ", ".join(f"{r['l']}={r['n']}" for r in counts))
    return "\n".join(lines)


def schema(ontology_file: str = "ontology.json") -> str:
    """Render the ontology for the prompt. Reads both the ex: prefixed form and the full-IRI plugin form."""
    o = json.loads((ROOT / "ontology" / ontology_file).read_text())["@graph"]

    def short(iri: str) -> str:
        return iri.rsplit("#", 1)[-1].split(":")[-1]

    out = []
    for x in o:
        kind = x["@type"]
        if kind == "owl:Ontology":
            continue
        name = short(x["@id"])
        if kind == "owl:Class":
            out.append(f"- node {name}: {x['rdfs:comment']}")
        else:
            d, r = short(x["rdfs:domain"]["@id"]), short(x["rdfs:range"]["@id"])
            arrow = (
                f"({d})-[{name}]->({r})"
                if kind == "owl:ObjectProperty"
                else f"({d}) property {name}: text value stored on the edge's object_string"
            )
            out.append(f"- edge {arrow}: {x['rdfs:comment']}")
    return "\n".join(out)


SYSTEM = """You investigate questions about Kestrel Consulting's customer projects (2023-2026) by querying
an entity graph extracted from project documents, plus text search over the same documents.

Graph schema (ontology):
{schema}

Entity names that exist in the graph (extraction is imperfect: the same entity can appear under
several names, e.g. a first name only or a short customer name; treat these as the same entity):
{catalog}

GQL dialect that works on this graph:
- MATCH (p:Person)-[e]->(j:Project) WHERE e.predicate = 'workedOn' AND p.name CONTAINS 'Idrissi'
  RETURN DISTINCT j.name AS project
- MATCH (j:Project)-[e]->(t:Technology) WHERE e.predicate = 'usesTechnology' AND t.name CONTAINS 'Databricks'
  RETURN DISTINCT j.name
- Use DISTINCT, count(DISTINCT x), CONTAINS on the most distinctive part of a name,
  and e.predicate IN [...] for several relationships.

Method:
1. Look up the exact entity names in the catalog above and cover every name variant of the same entity.
2. Use run_gql for relationships, counting, lists and "who/which" questions.
3. Use search_text for numbers, dates, amounts, reasons, narrative and anything the graph doesn't model.
4. If a query returns 0 rows, check whether that really means "no" (the right relationship and every
   name variant were queried) or whether a filter was too strict; then retry. For a negative question,
   confirm with one query that lists what DOES exist (e.g. all customers someone worked for).
5. Stop when you have enough evidence, at most {max_steps} tool calls. Then reply with a short evidence
   summary listing the facts you found and which query or passage supports each. Don't write the final answer prose.
"""


def investigate(
    c: SearchClient,
    chat: Any,
    question: str,
    graph_index: str = GRAPH_INDEX,
    chunk_index: str = CHUNK_INDEX,
    ontology_file: str = "ontology.json",
) -> tuple[list[dict], dict]:
    from kestrel_kg.strategies import OPENAI_SCOPE

    messages: list[dict[str, Any]] = [
        {
            "role": "system",
            "content": SYSTEM.format(
                schema=schema(ontology_file), catalog=catalog(c, graph_index), max_steps=MAX_STEPS
            ),
        },
        {"role": "user", "content": question},
    ]
    evidence: list[dict] = []
    usage = {"input": 0, "output": 0, "steps": 0, "queries": []}
    for _ in range(MAX_STEPS + 1):
        token = credential().get_token(OPENAI_SCOPE).token
        r = chat._http.post(
            f"{chat.s.model_endpoint}/openai/v1/chat/completions",
            headers={"Authorization": f"Bearer {token}"},
            json={"model": chat.s.chat_deployment, "messages": messages, "tools": TOOLS},
        )
        r.raise_for_status()
        d = r.json()
        u = d.get("usage", {})
        usage["input"] += u.get("prompt_tokens", 0)
        usage["output"] += u.get("completion_tokens", 0)
        msg = d["choices"][0]["message"]
        messages.append(msg)
        calls = msg.get("tool_calls") or []
        if not calls:
            evidence.insert(0, {"source": "agent-evidence-summary", "text": msg.get("content") or ""})
            break
        for call in calls:
            usage["steps"] += 1
            args = json.loads(call["function"]["arguments"] or "{}")
            try:
                if call["function"]["name"] == "run_gql":
                    usage["queries"].append(args["gql"])
                    rows = run_gql(c, args["gql"], graph_index)
                    result = {"rows": rows, "row_count": len(rows)}
                    evidence.append(
                        {"source": "graph", "text": f"GQL: {args['gql']}\nRows: {json.dumps(rows, ensure_ascii=False)}"}
                    )
                else:
                    hits = search_text(c, args["query"], args.get("top", 5), chunk_index)
                    result = {"passages": hits}
                    evidence += hits
            except Exception as e:  # return errors to the model so it can fix its query
                result = {"error": str(e)[:600]}
            messages.append(
                {"role": "tool", "tool_call_id": call["id"], "content": json.dumps(result, ensure_ascii=False)[:12000]}
            )
    return evidence, usage


def gql_agent(
    c: SearchClient,
    question: str,
    graph_index: str = GRAPH_INDEX,
    chunk_index: str = CHUNK_INDEX,
    name: str = "gql_agent",
    ontology_file: str = "ontology.json",
):
    from kestrel_kg.strategies import Chat, Retrieval

    t = time.perf_counter()
    evidence, usage = investigate(c, Chat(), question, graph_index, chunk_index, ontology_file)
    return Retrieval(
        name,
        evidence,
        int((time.perf_counter() - t) * 1000),
        retrieval_tokens=usage["input"] + usage["output"],
        debug={"steps": usage["steps"], "gql": usage["queries"]},
    )
