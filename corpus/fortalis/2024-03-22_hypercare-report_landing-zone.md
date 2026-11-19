# Hypercare Report: Fortalis Landing Zone

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Fortalis Landing Zone |
| **Document type** | Hypercare report / handover note |
| **Date** | 2024-03-22 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Distribution** | Marc Dubois, Kevin Hermans, Fortalis cloud team lead |

## 1. Summary

The four weeks of hypercare that followed acceptance on 2024-02-23 end today. The Fortalis cloud team ran the platform on its own for the whole period; Kestrel was called in for advice six times and for hands-on help twice. No production incidents were caused by the landing zone. The platform is now fully owned by the Fortalis cloud team.

## 2. Support requests during hypercare

| # | Date | Request | Outcome |
|---|---|---|---|
| H1 | 2024-02-27 | Pipeline approval stuck after the approver group was renamed | Group reference updated in the pipeline settings; naming guide amended |
| H2 | 2024-02-29 | Question on subnet sizing for a new spoke | Advised /25 default; spoke module default unchanged |
| H3 | 2024-03-04 | Tag inheritance did not apply to resources created before the policy | Remediation task run; explained in run book chapter 5 |
| H4 | 2024-03-07 | Firewall rule request with "any" destination rejected by reviewer | Correct behaviour; team helped the requester to specify destinations |
| H5 | 2024-03-12 | Just-in-time activation for a privileged role took long to approve during a holiday week | Second approver group extended with two cloud team members |
| H6 | 2024-03-14 | Monthly compliance export for the architecture board | Walked through the export together; figures presented by Kevin |
| H7 | 2024-03-19 | First request for a workload spoke for an upcoming project on claims | Reviewed parameter file with the cloud team, see section 4 |
| H8 | 2024-03-21 | Cost per cost centre view did not show the sandbox | Missing cost centre tag on the sandbox subscription; fixed |

## 3. Platform health at end of hypercare

- **Policy compliance:** 98.4% on the platform and corporate management groups. The remaining items are the legacy test resources in the decommission group; their owners have committed to deleting them by end of April.
- **Exemptions:** two active, both with an owner and expiry date. The global-location exemption for monitoring expires on 2024-07-31; the cloud team has planned the definition change in May.
- **Spokes:** two in production (shared services, data team sandbox), one in preparation.
- **Pipelines:** 37 production runs since acceptance, all with approval; one rollback (H1 related).

## 4. Preparing the next workload

Fortalis plans a first AI workload on claims in April. The cloud team has started a spoke request for it. Following the recommendation in the closing report, I discussed three points with Kevin and the cloud team before the spoke is created:

1. **Data classification.** Claim files contain personal data and sometimes medical information; the workload will be tagged "strictly confidential". Kevin wants the platform guidelines updated so that this level always requires private endpoints and customer-managed keys where available.
2. **Private endpoints.** All PaaS services in the new spoke get private endpoints registered in the hub DNS zones. The policy that registers them automatically is already in place.
3. **Identities.** Workload identities per component, no shared secrets in pipelines.

These decisions are recorded in the platform guidelines, not in the landing zone repository, so the new project can pick them up directly.

## 5. Open items handed over

| Item | Owner |
|---|---|
| Allow approved global resource types in the allowed-regions definition, then remove exemption | Cloud team lead |
| Switch naming policy from audit to deny on new spokes | Cloud team, decision by architecture board |
| Review hub firewall sizing after six months (July 2024) | Cloud team / Kevin |
| Remove legacy test resources | Resource owners |

## 6. Closing

Thanks to Kevin and the cloud team for an unusually smooth handover. Kestrel's involvement in the Fortalis Landing Zone ends with this report.

*Jonas Peeters, Kestrel Consulting*
