# Go-live Checklist: Production Use from 2026-02-02

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Customs Document Extraction |
| **Date** | 2026-01-30 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Go-live checklist |
| **Go decision** | Jan Wouters, product owner, 2026-01-30 14:00 |

## 1. What changes on Monday 2 February

From the start of the early shift at the customs desk, agents no longer key the six supported document types from scratch. Every document of those types goes through the pipeline and lands in the validation queue; the agent confirms or corrects every field and releases the export record. Manual keying remains the fallback for any document the pipeline cannot process.

Supported types at go-live: commercial invoice, packing list, CMR consignment note, certificate of origin, T1 transit document, bill of lading.

## 2. Readiness checklist

| # | Item | Owner | Status |
|---|---|---|---|
| 1 | Accuracy on test sets reviewed and accepted per type (CMR accepted with extra review rules) | JW | Done 2026-01-23 |
| 2 | Security check before production with Scaldis IT security | PDS | Done 2026-01-20 |
| 3 | Privacy note approved; retention job active | PDS | Done |
| 4 | Composed model version frozen and tagged in Azure AI Document Intelligence | AE | Done 2026-01-28 |
| 5 | Azure Logic Apps workflow promoted from test to production, connections re-pointed to production mailbox and scan folder | PDS | Done 2026-01-29 |
| 6 | Validation screen access group with all customs desk staff; senior agent role assigned | JW | Done |
| 7 | Export layout v1 confirmed by the agents who create declarations | JW | Done |
| 8 | Fallback procedure for manual keying printed at each desk | JW | Done |
| 9 | Alerting: workflow failures and queue age above 30 minutes, mail to the desk coordinator and Kestrel | PDS | Done |
| 10 | Short briefing for all agents, including night and weekend team | JW, AE | Planned 2026-01-30 and 2026-01-31 |

## 3. Briefing points for agents

- Validate every field. The pipeline is a first draft, not a decision.
- Critical fields are on top and highlighted when uncertain. Never release a record with a highlighted critical field you did not check.
- Seal numbers on CMR notes are always highlighted, regardless of confidence. This is deliberate.
- If a document lands in the "manual" folder (unsupported format, unreadable, wrong type), key it as before and press "report" so we can learn from it.
- Use the comment box for anything odd; Amira reads them daily during the first two weeks.

## 4. Monday schedule

| Time | Step | Owner |
|---|---|---|
| 05:45 | Check workflow run history of the night: no failed runs, queue empty or normal | AE |
| 06:00 | Production use starts | Customs desk |
| 06:00–10:00 | Amira on site at the customs desk | AE |
| 10:30 | First check of corrections and queue age with Jan | AE, JW |
| 16:00 | Day-1 review: volumes, corrections per type, issues | PDS, JW |

## 5. Rollback criteria

Rollback means switching the intake trigger off and returning to manual keying, which takes about five minutes. Jan decides. Criteria:
- workflow failures for more than 30 minutes during office hours;
- validation queue older than two hours while agents are available;
- a systematic error on a critical field across several documents.

## 6. Known limitations at go-live

| Limitation | Handling |
|---|---|
| CMR standard field accuracy below threshold | Extra review; handwriting measured separately |
| New shipper layouts | Monthly retraining from February |
| Dangerous goods declaration and EUR.1 not yet supported | Manual keying until their models are accepted |
| Credit notes and other documents classified as "other" | Manual |

## 7. Hypercare

Two weeks, until 2026-02-13. Daily check of corrections per type and queue age; issues logged in the project log with the label "hypercare".

Pieter De Smet
