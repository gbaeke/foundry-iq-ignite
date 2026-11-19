# Test Report: Latency of Combined Questions and Parallel Tool Calls

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Asset Management Agent |
| **Date** | 2026-10-21 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Document type** | Performance test report |
| **Related issue** | I-08: Slow responses on combined questions |

## 1. Summary

Combined questions, which need both the Foundry IQ knowledge base and two tools, took up to 25 seconds in the September pilot. With parallel tool calls and two smaller changes, the median response time for these questions drops from 19 to **11 seconds**, and the slowest 10% from 25 to **16 seconds**. Single-source questions are not affected. We recommend releasing the changes to the pilot on 2026-10-26.

## 2. Test set

- 40 combined questions from the evaluation set and the September pilot logs, for example "Is hydrant X due for inspection according to the procedure, and what did the last inspection find?"
- 40 single-source questions as a control group (knowledge base only, or one tool only).
- Each question run 5 times, at different times of day, in the test environment of the Microsoft Foundry project, with the same private networking as production.

## 3. Where the time went (baseline)

Breakdown of a typical combined question of 19 seconds:

| Step | Time |
|---|---|
| Agent plans the answer | 2.1 s |
| Knowledge base retrieval | 4.0 s |
| Tool call 1 (`get_asset_details`) | 1.2 s |
| Agent decides on next call | 1.8 s |
| Tool call 2 (`get_maintenance_history`) | 2.6 s |
| Agent decides on next call | 1.5 s |
| Agent writes the answer | 5.8 s |

The tools themselves are fast. Most of the time is spent in sequential rounds: the agent calls one source, reads the result, then decides to call the next.

## 4. Changes tested

1. **Parallel tool calls.** The agent instructions in Foundry Agent Service now encourage calling independent sources at the same time. For most combined questions the knowledge base and both tools can be called in one round, because the asset ID is already in the question.
2. **History tool returns fewer items by default.** `max_items` lowered from 10 to 5, with the total count. Less text to read for the agent.
3. **Shorter answer format.** One paragraph plus sources, details on request, as the planners asked in March.

## 5. Results

| Question type | Baseline median | New median | Baseline p90 | New p90 |
|---|---|---|---|---|
| Combined (40) | 19.2 s | 11.4 s | 25.1 s | 16.3 s |
| Knowledge base only (20) | 8.4 s | 7.9 s | 11.2 s | 10.6 s |
| One tool only (20) | 6.1 s | 5.8 s | 8.0 s | 7.7 s |

Answer quality on the combined questions, scored by two planners: 31 of 40 correct before, 32 of 40 after. No question got worse.

Case where parallel calls do not help: when the planner gives an address instead of an asset ID, the agent first needs `find_assets_near_location`, then the other tools. These stay at around 18 seconds.

## 6. Cost

Fewer sequential rounds also mean fewer model calls. Estimated model consumption per combined question drops by about 20%. For the pilot volume this is a small amount, but it matters for any wider rollout.

## 7. Recommendation

| # | Action | Owner | Date |
|---|---|---|---|
| 1 | Release changes 1 to 3 to the pilot | RW / JP | 2026-10-26 |
| 2 | Show a short "looking up asset records…" message after 5 seconds | RW | 2026-10-30 |
| 3 | Monitor p90 of combined questions weekly | JP | from 2026-10-26 |
| 4 | Close I-08 if p90 stays below 18 s for two weeks | PDS | 2026-11-09 |

Results to be presented at the steering meeting of 2026-10-23.
