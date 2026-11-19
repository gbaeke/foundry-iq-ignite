# Security Re-test and UAT Report

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Scaldis Ops Copilot |
| **Date** | 2025-08-29 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Test report (security re-test and UAT) |
| **Test period** | 2025-08-18 to 2025-08-28 |

## 1. Summary

The security re-test by Wim Goossens' team and the user acceptance test by shift leaders ran in parallel over the last two weeks of August. **All findings from the review of 9 May are closed or formally accepted.** UAT passed with minor remarks. The team recommends go-live on 2025-09-15, as re-planned.

## 2. Security re-test

### 2.1 Status of findings

| ID | Severity | Topic | Status |
|---|---|---|---|
| H-01 | High | Document-level permission trimming | **Closed** |
| M-01 | Medium | User names and retention in conversation logs | Closed |
| M-02 | Medium | App secret storage and rotation | Closed |
| M-03 | Medium | Rate limiting per user | Closed |
| M-04 | Medium | Indexing identity scope too broad | Closed |
| L-01 to L-04 | Low | Headers, error messages, dependency versions, admin documentation | Closed |
| L-05, L-06 | Low | Answer cards can be forwarded in Teams; no watermark on restricted answers | Accepted by Wim, to be addressed in user training |

### 2.2 Tests performed by Wim's team

- **Permission matrix.** 40 documents with unique permissions × 12 test accounts, including documents in the incident handling, customs procedures and access control libraries. No leakage.
- **Change scenarios.** User removed from a group, document permission tightened, document moved to a restricted folder. All took effect within the hourly sync; the manual emergency re-sync was tested once (took 22 minutes for the full index).
- **Prompt injection.** Wim's team placed a test document with hidden instructions in a test library. The bot quoted it as content and did not follow the instructions.
- **Log review.** Only pseudonymised IDs, retention job deletes entries older than 90 days.

Wim remarked that the group structure on the restricted sites is "the cleanest it has been in years", partly thanks to the June clean-up.

## 3. User acceptance test

- 12 shift leaders and planners, including 5 who were in the pilot, tested with their own accounts.
- 86 scripted scenarios, of which 81 passed and 5 passed with remarks.
- Remarks: two answers cite the right SOP but an older section number; one French translation of a button label; two cases where users expected an answer they could not get because of their permissions. That is correct behaviour; the training explains it.

Nathalie Dumont signed the UAT on 2025-08-28.

## 4. Performance

Load test re-run on the final build (Ruben Wouters): median 4.1 seconds, 95th percentile 8.0 seconds at five questions per second. Within limits.

## 5. Go-live conditions

| Condition | Status |
|---|---|
| No open high or medium security findings | Met |
| UAT signed by product owner | Met |
| Training for champions planned | Met (week of 1 September) |
| Teams app review by Scaldis IT | Planned 2025-09-03 |
| Higher model quota in production | Met |
| Personal sign-in on gate building PCs | In progress, not blocking |

## 6. Recommendation

Go-live on **2025-09-15**. Any change to SharePoint groups on the restricted sites between now and go-live should be announced to the project team, so the permission sync can be checked before the rollout.

Pieter De Smet
