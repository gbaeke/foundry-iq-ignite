# Performance Test Report: Query Latency with Security Filters

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Scaldis Ops Copilot |
| **Date** | 2025-07-04 |
| **Author** | Ruben Wouters, Junior Developer, Kestrel Consulting |
| **Document type** | Test report (performance) |
| **Reviewed by** | Pieter De Smet |

## 1. Why this test

Risk R-14: document-level permission trimming (ADR-03) adds a group lookup and a security filter to every query. Pilot users are used to a median answer time of about 3 seconds. Nathalie Dumont set the acceptable limit for go-live at a median below 5 seconds and a 95th percentile below 10 seconds, measured from the moment the user sends the question in Microsoft Teams until the answer card appears.

## 2. Set-up

- Test environment with a full copy of the production index: about 2,100 documents (general and restricted libraries), with permissions synced from SharePoint.
- 12 test accounts with different roles, from a gate clerk (few groups) to an operations manager (64 group memberships).
- Load script replaying 500 questions from the pilot logs (pseudonymised), at 1, 5 and 15 questions per second. 15 per second is about five times the expected peak at shift change.
- Timings logged per step: bot receive, group lookup, search, model call, card rendering.

## 3. First run (2 July)

| Load | Median | P95 | Errors |
|---|---|---|---|
| 1 q/s | 5.6 s | 10.9 s | 0 |
| 5 q/s | 5.9 s | 11.8 s | 0 |
| 15 q/s | 7.4 s | 16.2 s | 2.1% (rate limit on model calls) |

Breakdown at 5 q/s (median): group lookup 1.4 s, search 0.6 s, model call 3.3 s, rest 0.6 s. The group lookup was the new cost: for every question we resolved the user's groups from scratch, because the 15-minute cache from ADR-03 was not yet active in the test build.

## 4. Changes

1. **Group cache switched on** (15 minutes, as designed). Lookup drops to near zero for repeated questions; the first question of a session still pays the cost.
2. **Pre-warm at sign-in.** When a user opens the bot chat, the bot resolves groups in the background before the first question.
3. **Filter size.** For users with many groups, only groups that actually appear in the index are included in the filter. For the operations manager this goes from 64 to 11 groups.
4. **Shorter prompt.** Top 5 chunks trimmed to the relevant section only; average prompt size down by about 30%, which also lowers model cost.
5. **Typing indicator** shown immediately rather than after 2 seconds, as Elien Jacobs suggested. Does not change the numbers, but users perceive it as faster.

## 5. Second run (3 July)

| Load | Median | P95 | Errors |
|---|---|---|---|
| 1 q/s | 4.0 s | 7.6 s | 0 |
| 5 q/s | 4.1 s | 7.9 s | 0 |
| 15 q/s | 4.9 s | 9.8 s | 0.3% |

Within Nathalie's limits at all loads. The remaining errors at 15 q/s are model rate limits; the bot retries once and then shows a friendly "please ask again" message. We will ask Scaldis IT to raise the model quota before go-live as a precaution.

## 6. Correctness check

The security test over the 40 × 12 matrix was rerun on the tuned build: no chunk returned from a document the test user cannot open. Filter optimisation (change 3) did not change any result.

## 7. Conclusions

- R-14 can be lowered from open to monitored.
- Expect a median of roughly 4 seconds in production, about 1 second slower than in the pilot. Pilot users will notice; we will tell them why.
- Repeat the test after the security re-test if the index or filter logic changes.

## 8. Follow-up

| Action | Owner | Due |
|---|---|---|
| Request higher model quota | Scaldis IT via TM | 2025-07-18 |
| Add latency per step to the weekly quality report | RW | 2025-07-11 |
| Re-run load test after re-test fixes | RW | 2025-09-05 |

Ruben Wouters
