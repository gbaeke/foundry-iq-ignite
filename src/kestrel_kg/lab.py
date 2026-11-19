"""What the Graph Lab API does: run strategies side by side, run GQL, and browse a graph's entities with provenance."""

from __future__ import annotations

import asyncio
import time
from collections import defaultdict
from functools import lru_cache
from typing import Any

import yaml

from .client import ROOT, SearchClient
from .graphs import GRAPHS, Graph
from .strategies import STRATEGIES, Chat, Retrieval, answer, judge

SNIPPET_CHARS = 700


@lru_cache(maxsize=1)
def questions() -> list[dict[str, Any]]:
    return yaml.safe_load((ROOT / "groundtruth" / "questions.yaml").read_text())["questions"]


def question_by_id(qid: str) -> dict[str, Any] | None:
    return next((q for q in questions() if q["id"] == qid), None)


# ---------------- strategies ----------------


def _steps(r: Retrieval) -> list[dict[str, Any]]:
    """The retrieval engine's steps in one shape: what happened, how long, how many tokens."""
    steps = []
    for a in r.debug.get("activity") or []:
        args = a.get("graphSearchArguments") or {}
        detail = args.get("naturalLanguageQuery") or a.get("knowledgeSourceName") or ""
        if a.get("count") is not None:
            detail = f"{detail} · {a['count']} result(s)".strip(" ·")
        tokens = (a.get("inputTokens") or args.get("inputTokens") or 0) + (
            a.get("outputTokens") or args.get("outputTokens") or 0
        )
        steps.append({"type": a.get("type", "?"), "detail": detail, "ms": a.get("elapsedMs"), "tokens": tokens})
    for q in r.debug.get("subQueries") or []:  # Retriever 1
        steps.append({"type": "subQuery", "detail": q.get("search", ""), "ms": None, "tokens": 0})
    if r.debug.get("steps"):  # our agent
        steps.append({"type": "agentToolCalls", "detail": f"{r.debug['steps']} tool call(s)", "ms": None, "tokens": 0})
    return steps


def _gql(r: Retrieval) -> list[str]:
    from_kb = [
        (a.get("graphSearchArguments") or {}).get("gql")
        for a in r.debug.get("activity") or []
        if a.get("type") == "graphSearch"
    ]
    return [q for q in [*from_kb, *(r.debug.get("gql") or [])] if q]


def run_strategy(c: SearchClient, chat: Chat, strategy: str, question: str, q: dict[str, Any] | None) -> dict[str, Any]:
    t = time.perf_counter()
    base: dict[str, Any] = {"strategy": strategy}
    try:
        r = STRATEGIES[strategy](c, question)
        ans, usage = answer(chat, question, r)
    except Exception as e:  # a failing preview service shows as an error card, not a failed request
        return base | {"error": str(e)[:600], "total_ms": int((time.perf_counter() - t) * 1000)}
    result = base | {
        "answer": ans,
        "retrieval_ms": r.latency_ms,
        "total_ms": int((time.perf_counter() - t) * 1000),
        "answer_input_tokens": usage.get("prompt_tokens", 0),
        "answer_output_tokens": usage.get("completion_tokens", 0),
        "retrieval_tokens": r.retrieval_tokens,
        "context": [{"source": x["source"], "text": x["text"][:SNIPPET_CHARS]} for x in r.context],
        "gql": _gql(r),
        "steps": _steps(r),
    }
    if q and q.get("required_facts"):
        g = judge(chat, q, ans)
        facts = g.get("facts", [])
        result["judge"] = {
            "correct": bool(g.get("correct")),
            "fact_recall": round(sum(f["present"] for f in facts) / max(len(facts), 1), 3),
            "facts": facts,
            "note": g.get("note", ""),
        }
    return result


async def ask(question: str, strategies: list[str], question_id: str | None) -> list[dict[str, Any]]:
    """Every strategy runs in its own thread, so the slowest one sets the wait, not the sum."""
    c, chat = SearchClient(), Chat()
    q = question_by_id(question_id) if question_id else None
    return list(await asyncio.gather(*(asyncio.to_thread(run_strategy, c, chat, s, question, q) for s in strategies)))


# ---------------- graphs ----------------


def run_gql(graph: Graph, gql: str) -> dict[str, Any]:
    t = time.perf_counter()
    r = SearchClient().post(f"/indexes('{graph.graph_index}')/docs/search.graph", {"gql": gql})
    rows = [{k: v for k, v in row.items() if not k.startswith("@")} for row in r.get("value", [])]
    columns = list(dict.fromkeys(k for row in rows for k in row))
    return {"columns": columns, "rows": rows, "row_count": len(rows), "ms": int((time.perf_counter() - t) * 1000)}


def _all_edges(c: SearchClient, graph: Graph, flt: str | None = None) -> list[dict[str, Any]]:
    fields = "subject,subject_id,subject_type,predicate,object,object_id,object_type,object_string,chunk_id"
    out, skip = [], 0
    while True:
        body: dict[str, Any] = {"search": "*", "select": fields, "top": 1000, "skip": skip}
        if flt:
            body["filter"] = flt
        batch = c.post(f"/indexes('{graph.graph_index}')/docs/search", body)["value"]
        out += batch
        if len(batch) < 1000:
            return out
        skip += 1000


@lru_cache(maxsize=8)
def _graph_edges(graph_id: str) -> list[dict[str, Any]]:
    """Every triple of one graph, read once per process (a few thousand rows, a few seconds)."""
    return _all_edges(SearchClient(), GRAPHS[graph_id])


@lru_cache(maxsize=8)
def _entity_table(graph_id: str) -> dict[str, dict[str, Any]]:
    """Every entity in one graph, built once from its triples: id → name variants, type and degree."""
    table: dict[str, dict[str, Any]] = {}
    names: dict[str, defaultdict[str, int]] = defaultdict(lambda: defaultdict(int))
    for e in _graph_edges(graph_id):
        for side in ("subject", "object"):
            i, kind = e.get(f"{side}_id"), e.get(f"{side}_type")
            if not i or not kind or kind.startswith("xsd:"):
                continue
            row = table.setdefault(i, {"id": i, "type": kind, "degree": 0})
            row["degree"] += 1
            names[i][e.get(side) or i] += 1
    for i, row in table.items():
        ranked = sorted(names[i].items(), key=lambda kv: -kv[1])
        row["name"], row["names"] = ranked[0][0], [n for n, _ in ranked]
    return table


def entities(graph: Graph, kind: str | None, text: str | None, limit: int) -> list[dict[str, Any]]:
    rows = list(_entity_table(graph.id).values())
    if kind:
        rows = [r for r in rows if r["type"] == kind]
    if text:
        t = text.casefold()
        rows = [r for r in rows if any(t in n.casefold() for n in r["names"]) or t in r["id"].casefold()]
    rows.sort(key=lambda r: -r["degree"])
    return [{k: r[k] for k in ("id", "name", "type", "degree")} for r in rows[:limit]]


def entity(graph: Graph, entity_id: str) -> dict[str, Any] | None:
    table = _entity_table(graph.id)
    if entity_id not in table:
        return None
    c = SearchClient()
    quoted = entity_id.replace("'", "''")
    edges = _all_edges(c, graph, f"subject_id eq '{quoted}' or object_id eq '{quoted}'")
    chunk_ids = sorted({e["chunk_id"] for e in edges if e.get("chunk_id")})
    chunks: dict[str, dict[str, str]] = {}
    for i in range(0, len(chunk_ids), 50):  # search.in keeps the filter short
        ids = ",".join(chunk_ids[i : i + 50])
        hits = c.post(
            f"/indexes('{graph.chunk_index}')/docs/search",
            {"search": "*", "filter": f"search.in(uid, '{ids}', ',')", "select": "uid,snippet,blob_url", "top": 50},
        )["value"]
        for h in hits:
            chunks[h["uid"]] = {"file": h["blob_url"].split("/kestrel-corpus/")[-1], "text": h["snippet"]}
    out = []
    for e in edges:
        outgoing = e.get("subject_id") == entity_id
        other_side = "object" if outgoing else "subject"
        src = chunks.get(e.get("chunk_id") or "", {})
        out.append(
            {
                "predicate": e["predicate"].removeprefix("prop:"),
                "direction": "out" if outgoing else "in",
                "other_id": e.get(f"{other_side}_id") or "",
                "other_name": e.get(f"{other_side}_string") or e.get(other_side) or "",
                "other_type": e.get(f"{other_side}_type") or "",
                "source_file": src.get("file", ""),
                "snippet": src.get("text", "")[:SNIPPET_CHARS],
            }
        )
    row = table[entity_id]
    return {"id": entity_id, "name": row["name"], "type": row["type"], "names": row["names"], "edges": out}


@lru_cache(maxsize=8)
def network(graph_id: str) -> dict[str, Any]:
    """The whole graph for drawing: entities as nodes, and one edge per (subject, predicate, object) with how many
    triples say it. Text values (ontology v3 datatype properties) aren't nodes, so they're left out."""
    table = _entity_table(graph_id)
    counts: defaultdict[tuple[str, str, str], int] = defaultdict(int)
    for e in _graph_edges(graph_id):
        s, o = e.get("subject_id"), e.get("object_id")
        if s in table and o in table and not (e.get("object_type") or "").startswith("xsd:"):
            counts[(s, e["predicate"].removeprefix("prop:"), o)] += 1
    nodes = [{k: r[k] for k in ("id", "name", "type", "degree", "names")} for r in table.values()]
    edges = [{"source": s, "predicate": p, "target": o, "count": n} for (s, p, o), n in counts.items()]
    return {"nodes": nodes, "edges": edges}
