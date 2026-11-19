# FinOps Tips, Part 2: The Cost of AI Workloads

| | |
|---|---|
| **Organisation** | Kestrel Consulting (internal) |
| **Date** | 2026-11-13 |
| **Author** | Jonas Peeters, Cloud Platform Engineer |
| **Document type** | Internal guideline (FinOps tips, part 2), presented at the November kennisdeling |

## Why part 2

Part 1 (September 2024) was about idle compute, tags and budgets. Those rules still apply. But our cost profile has changed: on generative AI and agent work, the bill is driven less by virtual machines and clusters and more by model tokens, search capacity and evaluation runs. These are harder to predict and easier to waste. Below is what we have learned.

## 1. Make token cost visible from sprint 1

- Every model call logs input tokens, output tokens, model name and the feature that made the call (chat answer, query planning, summarisation, evaluation).
- Build a simple cost dashboard per environment in the first sprint: cost per day, per feature and per 100 user questions. The tech radar already says this; this is how.
- Report "cost per answered question" in the status report. Customers understand that number much better than a monthly total.

## 2. Pick the smallest model that passes the evaluation

- Start with a smaller, cheaper model for each step and move up only if the evaluation set shows it is needed.
- Query rewriting, classification and routing rarely need the largest model. The final answer sometimes does.
- Re-check the choice when new model versions come out. A newer small model often beats the older large one.

## 3. Control the context

- Retrieval returns too much by default. Fewer, better passages lower cost and usually improve answers.
- Trim conversation history: keep a summary of earlier turns instead of the full transcript.
- System prompts grow over a project like ivy on a wall. Review them every few sprints; remove instructions that no longer change the evaluation results.

## 4. Agents: watch the loops

- Agents that plan and call tools can make many model calls for one user question. Set a maximum number of steps and tool calls per request.
- Log the number of steps per request. A rising average is an early warning for both cost and latency.
- Run independent tool calls in parallel: it does not lower the token cost, but it cuts waiting time, which users notice more.

## 5. Evaluation runs are not free

- A full evaluation run with an LLM judge on a few hundred questions costs real money when it runs on every commit. Run a small smoke set on every pull request and the full set nightly or before a release.
- Cache answers for unchanged questions and configurations where the evaluation design allows it.

## 6. Search and retrieval capacity

- Size search capacity on the measured index size and query volume after the pilot, not on the proposal estimate.
- Development and test environments rarely need the same tier as production. Agree with the customer which environments can run on a lower tier.
- Re-indexing everything after each small content change is expensive. Prefer incremental updates.

## 7. Provisioned capacity versus pay-per-use

Provisioned capacity makes sense only when usage is high and steady. For pilots and most internal tools, pay-per-use is cheaper and more flexible. Revisit after three months of production data, with the customer's finance team in the room.

## 8. Internal subscriptions

Our own AI sandbox and the internal knowledge graph experiment follow the same rules. The October cost list showed one forgotten evaluation job that ran nightly on a large model for three weeks. It has been fixed; the owner bought cake.

## Checklist for AI engagements

- [ ] Token logging per feature and a cost dashboard in sprint 1
- [ ] Cost per answered question in the status report
- [ ] Model choice per step justified by the evaluation set
- [ ] Step and tool-call limits for agents
- [ ] Smoke set on pull requests, full evaluation nightly
- [ ] Search tier reviewed after the pilot

Jonas
