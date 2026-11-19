"""The Graph Lab API without Azure: the lists it serves and how it refuses bad input."""

from kestrel_kg.graphs import GRAPHS
from kestrel_kg.strategies import STRATEGIES


def test_strategies_match_the_registry(client):
    ids = [s["id"] for s in client.get("/api/strategies").json()]
    assert ids == list(STRATEGIES)


def test_graphs_list_their_indexes(client):
    graphs = {g["id"]: g for g in client.get("/api/graphs").json()}
    assert set(graphs) == set(GRAPHS)
    assert graphs["ungrounded"]["graph_index"] == "kestrel-entities-ks-graph-index"


def test_questions_come_from_the_eval_set(client):
    qs = client.get("/api/questions").json()
    assert len(qs) == 24
    assert {q["category"] for q in qs} >= {"counting", "multi_hop", "synthesis"}


def test_unknown_strategy_is_refused_before_any_call(client):
    res = client.post("/api/ask", json={"question": "Who is Jan Wouters?", "strategies": ["nope"]})
    assert res.status_code == 422
    assert res.json()["error"]["code"] == "unknown_strategy"


def test_unknown_graph_is_a_404(client):
    res = client.post("/api/gql", json={"graph": "nope", "gql": "MATCH (n) RETURN n LIMIT 1"})
    assert res.status_code == 404
    assert res.json()["error"]["code"] == "unknown_graph"


def test_network_of_an_unknown_graph_is_a_404(client):
    res = client.get("/api/graphs/nope/network")
    assert res.status_code == 404
    assert res.json()["error"]["code"] == "unknown_graph"


def test_too_short_question_is_invalid(client):
    res = client.post("/api/ask", json={"question": "x", "strategies": ["rag"]})
    assert res.status_code == 422
    assert res.json()["error"]["code"] == "invalid"
