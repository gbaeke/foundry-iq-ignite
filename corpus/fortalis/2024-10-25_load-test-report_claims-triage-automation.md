# Load Test Report: Claims system integration

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Test report (load and performance) |
| **Date** | 2024-10-25 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Test date** | 2024-10-23, 18:00-21:30 |
| **Participants** | Jonas Peeters; claims system team (two developers, one operator); Fortalis cloud team on call |

## 1. Purpose

Check that the triage solution and the claims system write interface cope with peak volumes after a storm, and that throttling and retries behave as designed. This closes risk R2 from the status report of 2024-09-20 ("claims system API rate limits in production"), if the results are good.

## 2. Set-up

- Acceptance environment of the triage solution, connected to the performance test environment of the claims system (same sizing as production).
- 18,000 test claims generated from pseudonymised historical claims, with their documents, injected into a test intake mailbox and the broker upload folder.
- Three scenarios, each 45 minutes.

| Scenario | Rate | Represents |
|---|---|---|
| S1 Normal day | 300 claims/hour | Average weekday |
| S2 Storm peak | 1,000 claims/hour | Monday after a storm, three times a normal peak |
| S3 Burst | 3,000 claims in 10 minutes, then normal | Broker bulk upload after a weekend |

The orchestration flow in Azure Logic Apps throttles calls to the claims system at 5 per second, as agreed in June. The claims system team set their interface limit at 10 per second.

## 3. Results

| Measure | S1 | S2 | S3 |
|---|---|---|---|
| Claims processed | 225 | 750 | 3,000 + 120 |
| End-to-end time per claim, median | 41 s | 58 s | 6 min 40 s |
| End-to-end time per claim, 95th percentile | 1 min 10 s | 2 min 05 s | 17 min |
| Document Intelligence extraction, median per document | 4.1 s | 4.6 s | 5.2 s |
| Classification endpoint latency, median | 0.3 s | 0.4 s | 0.9 s |
| Claims system calls rejected (rate limit) | 0 | 0 | 0 |
| Claims system calls failed and retried | 0 | 3 | 21 |
| Claims lost or stuck | 0 | 0 | 0 |

## 4. Observations

1. **Extraction is the bottleneck, not the claims system.** In S3 the queue built up in front of the extraction step. The extraction service throttled our requests at the configured rate. The claims system was never close to its limit.
2. **Retries worked.** The 21 failed calls in S3 were timeouts while the claims system test environment ran a scheduled batch job at 20:00. All succeeded on the second or third attempt.
3. **The classification endpoint stayed fast.** One small instance was enough, with CPU at 60% at the peak of S3. No need to scale up for production.
4. **Order of processing.** In S3, claims were processed roughly in arrival order. Urgent claims (U1) from the burst waited as long as the others. For a real storm Monday, that is not ideal.

## 5. Actions

| # | Action | Owner | Due |
|---|---|---|---|
| A1 | Increase the extraction request limit for production; request quota increase through the cloud team | JP | 2024-11-08 |
| A2 | Process claims from the intake mailbox in parallel batches of 10 instead of one by one | JP | 2024-11-08 |
| A3 | Priority lane: claims with U1 keywords in the e-mail subject or first lines skip ahead in the queue | JP | 2024-11-22 |
| A4 | Ask claims system team to move the 20:00 batch out of the production peak window, or accept retries | Claims system team | 2024-11-15 |
| A5 | Repeat S3 after A1 and A2 | JP | 2024-11-22 |

## 6. Conclusion

The solution handles a storm-day peak of 1,000 claims per hour with all claims processed within about two minutes at the 95th percentile. A broker burst is processed without loss, but too slowly for urgent claims. Risk R2 is closed: the claims system interface limits are not a problem. A new, smaller item is opened for the burst behaviour (A1 to A3).

Cost note: the test cost about EUR 140 in extraction calls in the acceptance subscription, charged to Fortalis' Azure consumption as agreed.

*Jonas Peeters*
