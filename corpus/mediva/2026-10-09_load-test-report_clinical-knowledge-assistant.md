# Load Test Report: Front End and Retrieval

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Clinical Knowledge Assistant |
| **Document type** | Test report (performance) |
| **Date** | 2026-10-09 |
| **Author** | Ruben Wouters, Developer, Kestrel Consulting |
| **Reviewed by** | Pieter De Smet; Jeroen Lambrecht (Mediva IT) |
| **Test window** | 2026-10-06 and 2026-10-07, 21:00 to 23:30, test environment |

## 1. Why

Risk R4 in the status report of September: usage spikes at night in the emergency department. Before the pilot is extended to more users or departments, we need to know how the front end and the retrieval behave under a multiple of today's load, and where the first bottleneck is.

## 2. Current load (production, September)

| Measure | Value |
|---|---|
| Active users (last four weeks) | about 60 |
| Questions per day | 70 to 110 |
| Peak observed | 19 questions in one hour, emergency, Saturday night |
| Answer time, median / 90th percentile | 9.6 s / 16.2 s |

## 3. Test set-up

- Test environment with the same configuration as production: front end, Microsoft Foundry assistant, Foundry IQ knowledge base on a copy of the cardiology and emergency content, Azure OpenAI deployment with the same model and capacity as production.
- Scripted virtual users sending questions taken from the evaluation set, mixed as in production: 78% simple, 22% compound.
- No real users and no production data involved; questions are from the evaluation set, which contains no patient data.
- Three steps of 30 minutes: 2x, 5x and 10x the observed peak hour.

## 4. Results

| Step | Questions per hour | Median answer time | 90th percentile | Errors |
|---|---|---|---|---|
| Baseline (1x) | 19 | 9.4 s | 15.8 s | 0 |
| 2x | 38 | 9.7 s | 16.4 s | 0 |
| 5x | 95 | 11.2 s | 21.0 s | 0.5% |
| 10x | 190 | 18.9 s | 41.3 s | 6.8% |

**Errors** at 5x and 10x were all rate-limit responses from the model deployment, retried by the assistant. Where retries ran out, the user saw "please try again".

## 5. Bottlenecks

1. **Model deployment capacity.** The first limit is the token capacity of the Azure OpenAI deployment. Compound questions use several model calls for query planning and one for the answer, so they hit the limit first.
2. **Retrieval.** Query planning and searches in the knowledge base stayed stable up to 5x; at 10x retrieval time rose by about 30%, much less than the model calls.
3. **Front end.** No issue. CPU and memory stayed low; the front end only waits for the assistant.

## 6. What this means

- Today's pilot load, including the night peaks, has a comfortable margin: up to about 5x the current peak hour without noticeable degradation.
- Extending the pilot to two or three more departments of similar size is feasible with the current capacity, if usage per user stays similar.
- A hospital-wide rollout would require more model capacity and a review of the retry behaviour.

## 7. Changes made after the test

| # | Change | Status |
|---|---|---|
| 1 | Retry with backoff tuned; user sees "busy, retrying" instead of a silent wait | Done, 2026-10-08 |
| 2 | Simple questions use one sub-query instead of up to three | Was already in place; verified |
| 3 | Alert to Mediva IT when the share of rate-limited calls exceeds 1% over 15 minutes | Done |
| 4 | Answer streaming starts after the first retrieval result instead of after all sub-queries | Tested, gives about 1.5 s faster first words; to be released after review by Amira |

## 8. Cost note

The test consumed model and retrieval capacity in Mediva's subscription for about five hours. Jeroen was informed beforehand; the consumption is a small fraction of a month of production use. Test resources were scaled down again on 2026-10-08.

## 9. Recommendations

1. Repeat the load test before any extension beyond the current pilot departments.
2. Include the capacity figures in the Phase 1 review so that the Phase 2 scope comes with a capacity and cost estimate.
3. Keep monitoring answer time per hour of the day; night peaks in emergency remain the reference.
