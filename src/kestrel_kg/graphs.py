"""The three entity graphs on the search service, and which indexes, knowledge base and ontology belong to each."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Graph:
    id: str
    label: str
    description: str
    knowledge_source: str
    knowledge_base: str
    ontology_file: str  # in ontology/

    @property
    def graph_index(self) -> str:
        return f"{self.knowledge_source}-graph-index"

    @property
    def chunk_index(self) -> str:
        return f"{self.knowledge_source}-index"


GRAPHS: dict[str, Graph] = {
    g.id: g
    for g in (
        Graph(
            "ungrounded",
            "Ungrounded (v2)",
            "Built with REST. Entity ids come from the extracted names, so name variants are separate nodes.",
            "kestrel-entities-ks",
            "kestrel-entities-kb",
            "ontology.json",
        ),
        Graph(
            "grounded-v2",
            "Grounded (v2)",
            "Built with the skills plugin and a grounding index. Issues and outcomes are entities.",
            "entity-managed-584653aa7c8656e0",
            "entity-kb-584653aa7c8656e0",
            "ontology.json",
        ),
        Graph(
            "grounded-v3",
            "Grounded (v3)",
            "Grounded, with issues and outcomes stored as text values instead of entities.",
            "entity-managed-03116d12fb395249",
            "entity-kb-03116d12fb395249",
            "ontology-v3.jsonld",
        ),
    )
}
