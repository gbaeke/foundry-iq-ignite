"""Run the eval question set against every strategy and store the results.

Usage:
    uv run python -m kestrel_kg.evaluate                       # all strategies, all questions
    uv run python -m kestrel_kg.evaluate --strategies rag entity --ids C1 M1
    uv run python -m kestrel_kg.evaluate --ask "Who worked with Kevin Hermans?"   # one-off, no scoring
"""

from __future__ import annotations

import argparse
import json
import time
from datetime import UTC, datetime

import yaml

from kestrel_kg.client import ROOT, SearchClient
from kestrel_kg.strategies import STRATEGIES, Chat, answer, judge

RESULTS = ROOT / "results"


def run_one(c: SearchClient, chat: Chat, strategy: str, q: dict, score: bool = True) -> dict:
    t = time.perf_counter()
    try:
        r = STRATEGIES[strategy](c, q["question"])
    except Exception as e:  # keep going; a failing preview strategy shouldn't stop the run
        return {"id": q.get("id"), "strategy": strategy, "error": str(e)[:500]}
    ans, usage = answer(chat, q["question"], r)
    row = {
        "id": q.get("id"),
        "category": q.get("category"),
        "strategy": strategy,
        "question": q["question"],
        "answer": ans,
        "retrieval_ms": r.latency_ms,
        "total_ms": int((time.perf_counter() - t) * 1000),
        "answer_input_tokens": usage.get("prompt_tokens", 0),
        "answer_output_tokens": usage.get("completion_tokens", 0),
        "retrieval_tokens": r.retrieval_tokens,
        "context_sources": sorted({x["source"] for x in r.context}),
        "debug": r.debug,
    }
    if score and q.get("required_facts"):
        g = judge(chat, q, ans)
        facts = g.get("facts", [])
        row |= {
            "correct": bool(g.get("correct")),
            "fact_recall": round(sum(f["present"] for f in facts) / max(len(facts), 1), 3),
            "judge": g,
        }
    return row


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--strategies", nargs="+", default=list(STRATEGIES))
    p.add_argument("--ids", nargs="*")
    p.add_argument("--ask")
    a = p.parse_args()

    c, chat = SearchClient(), Chat()
    if a.ask:
        for s in a.strategies:
            row = run_one(c, chat, s, {"question": a.ask}, score=False)
            print(f"\n=== {s} ({row.get('retrieval_ms')} ms) ===\n{row.get('answer') or row.get('error')}")
        return

    qs = yaml.safe_load((ROOT / "groundtruth" / "questions.yaml").read_text())["questions"]
    if a.ids:
        qs = [q for q in qs if q["id"] in a.ids]
    rows = []
    for q in qs:
        for s in a.strategies:
            row = run_one(c, chat, s, q)
            rows.append(row)
            status = row.get("error", "")[:80] or f"correct={row.get('correct')} recall={row.get('fact_recall')}"
            print(f"{q['id']:<3} {s:<8} {row.get('retrieval_ms', '-'):>6} ms  {status}")

    RESULTS.mkdir(exist_ok=True)
    out = RESULTS / f"run-{datetime.now(UTC):%Y%m%dT%H%M%SZ}.json"
    out.write_text(json.dumps(rows, indent=2, ensure_ascii=False))
    print(f"\nwrote {out.relative_to(ROOT)}")
    summarize(rows)


def summarize(rows: list[dict]) -> None:
    by: dict[str, list[dict]] = {}
    for r in rows:
        by.setdefault(r["strategy"], []).append(r)
    print(f"\n{'strategy':<9}{'correct':>9}{'recall':>8}{'in tok':>9}{'retr ms':>9}{'errors':>8}")
    for s, rs in by.items():
        ok = [r for r in rs if "error" not in r]
        n = max(len(ok), 1)
        print(
            f"{s:<9}{sum(r.get('correct', False) for r in ok) / n:>9.0%}"
            f"{sum(r.get('fact_recall', 0) for r in ok) / n:>8.0%}"
            f"{sum(r['answer_input_tokens'] + r['retrieval_tokens'] for r in ok) / n:>9.0f}"
            f"{sum(r['retrieval_ms'] for r in ok) / n:>9.0f}"
            f"{len(rs) - len(ok):>8}"
        )


if __name__ == "__main__":
    main()
