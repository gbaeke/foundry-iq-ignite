# Technical Design Note: Orchestration and deployment in the Fortalis spoke

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Technical design note |
| **Date** | 2024-06-21 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Reviewed by** | Amira El Idrissi; Fortalis cloud team |
| **Version** | 1.0 |

## 1. Scope of this note

How the triage solution is deployed in the project spoke of the Fortalis landing zone and how a claim flows through the components. The model itself is described in the model card by Amira; routing rules are in ADR-01.

## 2. Components

| Component | Service | Purpose |
|---|---|---|
| Intake flow | Azure Logic Apps | Picks up claims from the intake mailbox, the broker uploads and the portal export folder |
| Triage flow | Azure Logic Apps | Calls extraction and classification, applies thresholds and hard rules, writes to the claims system |
| Extraction | Azure AI Document Intelligence | Document type classifier plus custom extraction models (claim form, repair quote, police report) |
| Classification | Azure Machine Learning | Managed online endpoint hosting the triage model; training pipelines and model registry |
| Storage | Storage account in the spoke | Incoming documents, extraction results, audit trail |
| Secrets | Spoke secrets store | Connection secrets that cannot yet be replaced by workload identities |

All services have private endpoints in the spoke and resolve through the hub DNS zones. There are no public endpoints. The infrastructure is deployed with the landing zone's infrastructure-as-code modules and pipeline, so the Fortalis guardrails (allowed regions, mandatory tags, diagnostic settings) apply without exceptions.

## 3. Flow of one claim

1. **Pick-up.** The intake flow polls the intake mailbox every two minutes and receives broker uploads and portal exports as they arrive. Each claim gets a correlation ID.
2. **Duplicate check.** Same policy number and date of loss within 48 hours through another channel: the claim is marked as possible duplicate (hard rule, see ADR-01).
3. **Document classification.** Every attachment goes through the Document Intelligence classifier. Photos are kept but not analysed.
4. **Extraction.** Claim forms, repair quotes and police reports go to their custom model. Fields below the field-level confidence threshold are left empty, never guessed.
5. **Classification.** The triage flow sends extracted fields and the free text description to the online endpoint in Azure Machine Learning and receives type, complexity and urgency with probabilities.
6. **Decision.** Thresholds and hard rules are evaluated in the triage flow. Configuration is stored as a versioned parameter file.
7. **Write-back.** Through the claims system write interface (expected mid-August, see risk log). Until then, results go to a stub that mimics the interface.
8. **Audit.** Every step writes to the audit trail: input documents, extracted fields, model version, probabilities, decision and reason.

## 4. Environments

| Environment | Purpose | Data |
|---|---|---|
| Development | Building flows and models | Pseudonymised historical claims |
| Acceptance | Integration tests, UAT, pilot | Real claims, access restricted to the project and the claims team |
| Production | Live triage | Real claims |

Promotion between environments goes through the pipeline with approval. Model promotion is separate: a model registered in Azure Machine Learning is deployed to acceptance by the pipeline and to production only after Laura's team has signed off the evaluation report.

## 5. Error handling

- Any failure in extraction or classification sends the claim to the human triage queue with reason "technical". A claim is never lost or stuck.
- Retries with exponential back-off for the claims system calls; after three failures, an alert to the cloud team and the claim waits in a retry list.
- Throttling at 5 calls per second to the claims system.

## 6. Monitoring

Alerts on: flow failures, endpoint latency above 3 seconds, rising share of "technical" deferrals. A monitoring dashboard for the claims team is planned for the integration phase; content to be agreed with Laura.

## 7. Open points

- Retention of documents in the spoke storage: proposal 90 days after routing, as the claims system keeps the master copy. To be confirmed in the privacy review.
- Cost: the online endpoint runs permanently. We size it small and review after go-live.

*Jonas Peeters*
