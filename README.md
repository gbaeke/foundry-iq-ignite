# Kestrel Graph Lab

A local lab for learning how Foundry IQ (Azure AI Search) knowledge graphs compare with passage search. It runs one
question through up to ten retrieval strategies side by side (RAG, Microsoft Retriever 1, the managed knowledge base
and our own GQL agent, on an ungrounded and two grounded graphs), lets you run GQL directly, and browse every entity
with the passages it was extracted from. It runs on your machine against the search service and models in Azure.

Background: the session notes in `docs/BRK297-session.md`, the portal walkthrough in `docs/foundry-iq-walkthrough.md`,
and the explainer page `viz/explainer.html`.

## Prerequisites in Azure

`infra/deploy.sh` creates the resources and writes `.env`; `python -m kestrel_kg.setup create` builds the ungrounded
graph. The grounded graphs were built with the Foundry IQ skills plugin (see the build log). Sign in with `az login`:
the app uses your Azure CLI identity (DefaultAzureCredential) for Search and the models.

## Run it

Needs [uv](https://docs.astral.sh/uv/), Node.js 24+.

```bash
scripts/run-local.sh        # http://localhost:8318
```

Settings live in `.env` (created from `.env.example` on the first run).

## Pages

- **Compare**: pick an eval question (scored against `groundtruth/questions.yaml`) or type your own, choose strategies,
  and see each answer with time, tokens, the generated GQL, the engine's steps and the retrieved passages.
- **GQL console**: GQL against any of the three graph indexes, with examples.
- **Graph**: the whole entity graph as a network (Cytoscape), filtered by type and relationship; click a node for its
  neighbours and provenance. Lists likely duplicates, so ungrounded vs grounded shows what grounding merges.
- **Explore**: every entity per graph, its name variants and relationships, and the source passage of each.

## Command-line tools

```bash
uv run python -m kestrel_kg.evaluate --strategies rag10 gql_agent_g3   # the eval set, results in results/
uv run python -m kestrel_kg.check_corpus                               # corpus against the ground truth rules
uv run python -m kestrel_kg.setup status                               # the ungrounded knowledge source
```

## Develop

```bash
scripts/run-local.sh --dev  # hot reload on http://localhost:5173
scripts/check.sh            # lint, types, tests: what CI runs
```

API docs: http://localhost:8318/api/docs
