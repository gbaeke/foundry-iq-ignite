# Hypercare Closure and Handover Note

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Scaldis Ops Copilot |
| **Date** | 2025-10-17 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Handover note |
| **Distribution** | Koen Verstraete, Nathalie Dumont, Wim Goossens, Thomas Maes, Elien Jacobs, Ruben Wouters |

## 1. Summary

Hypercare ends today, four weeks after the go-live of 2025-09-22. The copilot runs stable, the first rollout wave of **340 users** is active, and the routines needed to keep answer quality up are now owned by Nathalie Dumont's team. Thomas Maes will send the final project report and budget reconciliation by the end of October.

## 2. Hypercare in numbers

| Measure | Week 1 | Week 4 |
|---|---|---|
| Questions per week | ~2,000 | ~1,600 |
| Rated helpful | 79% | 82% |
| D-score answers in weekly sample of 50 | 3 | 1 |
| Median answer time | 4.2 s | 4.0 s |
| Permission sync errors (daily report) | 6 | 0 |
| Incidents with user impact | 1 | 0 |

The drop in questions after week 1 is expected: the first days had many curiosity questions. Usage is now concentrated at shift changes and at night.

## 3. Issues handled during hypercare

1. **Old French SOP versions.** Nathalie's content owners archived 48 outdated French documents. These were the most frequent cause of wrong answers in week 1.
2. **Bot not visible on a shared terminal PC.** The PC in the reefer workshop was still signed in with a generic account that is not in the app policy. Ruben Wouters and Scaldis IT moved it to personal sign-in, like the gate building PCs. The other shared PCs follow the same procedure.
3. **Incident on 2025-09-30.** The hourly permission sync stopped for three hours after a certificate on the indexing job expired. Fail-closed behaviour meant no exposure; recently changed documents were simply not updated. Renewed, and the expiry date is now in Scaldis IT's monitoring.
4. **Contradicting SOPs.** Two pairs of SOPs gave different instructions on lashing inspection intervals. Resolved by the content owners.

## 4. Handover: who does what from now on

| Routine | Frequency | Owner |
|---|---|---|
| Review weekly quality report (feedback, D-score sample, top questions) | Weekly | Nathalie's operations team |
| Archive outdated or duplicate documents flagged by the index report | Monthly | Content owners per site |
| Announce SharePoint group changes on operations and restricted sites | Before each change | Site owners to Scaldis IT |
| Review permission sync report | Daily, automated alert on errors | Scaldis IT |
| Security review of changes to scope or architecture | Per change | Wim Goossens |
| Regression and adversarial test after prompt or index changes | Per change | Scaldis IT, with the runbook |
| Onboarding of new staff | Ongoing | HR onboarding day, module from Elien Jacobs |

The runbook (operations, sync, emergency re-sync, rollback), the architecture documentation including ADR-01 to ADR-03, and the test sets are in the project SharePoint site, handed over to Scaldis IT on 2025-10-15.

## 5. Recommendations

- **Second rollout wave.** Other departments (technical services, HSE) asked for access. Each new library goes through the same steps: content owner, permission check, regression questions, and Wim's review before indexing, not after.
- **Content governance.** The copilot makes outdated documents visible. Keep the monthly clean-up, otherwise quality will drift back within months.
- **Cost.** Running cost is now mostly the search service plus model usage at about two euro cents per question. Consumption alerts stay in place on the resource group.
- **Lesson for the next project.** Plan the security review in the first sprint. On this project the architecture would have been designed for permission trimming from day one.

## 6. Thanks

Thanks to the champions on every shift, who did more for adoption than any training slide, and to Wim's team for the thorough re-tests.

Pieter De Smet
