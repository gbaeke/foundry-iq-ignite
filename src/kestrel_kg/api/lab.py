from typing import Annotated, Any

from fastapi import APIRouter, Query
from pydantic import BaseModel, ConfigDict, Field

from .. import lab
from ..graphs import GRAPHS
from ..strategies import STRATEGIES, STRATEGY_INFO
from .errors import ApiError

router = APIRouter(tags=["lab"])


class Strategy(BaseModel):
    id: str
    label: str
    family: str
    description: str


class GraphInfo(BaseModel):
    id: str
    label: str
    description: str
    graph_index: str
    chunk_index: str
    knowledge_base: str


class Question(BaseModel):
    id: str
    category: str
    question: str
    answer: str
    required_facts: list[str]


class AskRequest(BaseModel):
    question: str = Field(min_length=3, max_length=500)
    strategies: list[str] = Field(min_length=1)
    question_id: str | None = None


class Passage(BaseModel):
    source: str
    text: str


class Step(BaseModel):
    model_config = ConfigDict(json_schema_serialization_defaults_required=True)

    type: str
    detail: str
    ms: int | None = None
    tokens: int = 0


class Fact(BaseModel):
    fact: str
    present: bool


class Judgement(BaseModel):
    correct: bool
    fact_recall: float
    facts: list[Fact]
    note: str


class StrategyResult(BaseModel):
    # fields with a default are still always present in the response, so the client types them as required
    model_config = ConfigDict(json_schema_serialization_defaults_required=True)

    strategy: str
    answer: str | None = None
    error: str | None = None
    retrieval_ms: int | None = None
    total_ms: int
    answer_input_tokens: int = 0
    answer_output_tokens: int = 0
    retrieval_tokens: int = 0
    context: list[Passage] = []
    gql: list[str] = []
    steps: list[Step] = []
    judge: Judgement | None = None


class GqlRequest(BaseModel):
    graph: str
    gql: str = Field(min_length=6, max_length=2048)  # the service limit


class GqlResult(BaseModel):
    columns: list[str]
    rows: list[dict[str, Any]]
    row_count: int
    ms: int


class NetworkNode(BaseModel):
    id: str
    name: str
    type: str
    degree: int
    names: list[str]


class NetworkEdge(BaseModel):
    source: str
    predicate: str
    target: str
    count: int


class Network(BaseModel):
    nodes: list[NetworkNode]
    edges: list[NetworkEdge]


class EntitySummary(BaseModel):
    id: str
    name: str
    type: str
    degree: int


class Edge(BaseModel):
    predicate: str
    direction: str
    other_id: str
    other_name: str
    other_type: str
    source_file: str
    snippet: str


class EntityDetail(BaseModel):
    id: str
    name: str
    type: str
    names: list[str]
    edges: list[Edge]


def _graph(graph_id: str):
    if graph_id not in GRAPHS:
        raise ApiError("unknown_graph", f"Unknown graph '{graph_id}'. Use one of: {', '.join(GRAPHS)}.", 404)
    return GRAPHS[graph_id]


@router.get("/strategies")
def list_strategies() -> list[Strategy]:
    return [Strategy(**s.__dict__) for s in STRATEGY_INFO]


@router.get("/graphs")
def list_graphs() -> list[GraphInfo]:
    return [
        GraphInfo(
            id=g.id,
            label=g.label,
            description=g.description,
            graph_index=g.graph_index,
            chunk_index=g.chunk_index,
            knowledge_base=g.knowledge_base,
        )
        for g in GRAPHS.values()
    ]


@router.get("/questions")
def list_questions() -> list[Question]:
    return [Question(**{k: q[k] for k in Question.model_fields}) for q in lab.questions()]


@router.post("/ask")
async def ask(req: AskRequest) -> list[StrategyResult]:
    unknown = [s for s in req.strategies if s not in STRATEGIES]
    if unknown:
        raise ApiError("unknown_strategy", f"Unknown strategies: {', '.join(unknown)}.", 422)
    results = await lab.ask(req.question, req.strategies, req.question_id)
    return [StrategyResult(**r) for r in results]


@router.post("/gql")
def run_gql(req: GqlRequest) -> GqlResult:
    try:
        return GqlResult(**lab.run_gql(_graph(req.graph), req.gql))
    except RuntimeError as e:  # the service rejected the query: show its message
        raise ApiError("gql_failed", str(e)[:800], 400) from e


@router.get("/graphs/{graph_id}/entities")
def list_entities(
    graph_id: str,
    type: Annotated[str | None, Query()] = None,
    q: Annotated[str | None, Query(max_length=100)] = None,
    limit: Annotated[int, Query(ge=1, le=500)] = 200,
) -> list[EntitySummary]:
    return [EntitySummary(**e) for e in lab.entities(_graph(graph_id), type, q, limit)]


@router.get("/graphs/{graph_id}/entity")
def get_entity(graph_id: str, id: Annotated[str, Query(min_length=1)]) -> EntityDetail:
    detail = lab.entity(_graph(graph_id), id)
    if detail is None:
        raise ApiError("not_found", f"No entity '{id}' in graph {graph_id}.", 404)
    return EntityDetail(**detail)


@router.get("/graphs/{graph_id}/network")
def get_network(graph_id: str) -> Network:
    return Network(**lab.network(_graph(graph_id).id))
