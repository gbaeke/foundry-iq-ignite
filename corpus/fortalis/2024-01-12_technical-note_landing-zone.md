# Technical Note: Allowed-regions policy and the global-location exemption

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Fortalis Landing Zone |
| **Document type** | Technical note / issue analysis |
| **Date** | 2024-01-12 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **For** | Kevin Hermans, Enterprise Architect; Fortalis security team |

## 1. What happened

On 2024-01-10, the day after the hub was connected to the Brussels datacentre, the deployment of the monitoring components for the shared services spoke failed in the acceptance environment. The pipeline log showed a deny from the **allowed regions** assignment in Azure Policy.

The cause: one of the monitoring services we deploy does not live in a region. It can only be created with the location "global". Our allowed-regions definition lists the two EU regions only, so "global" is denied. In development this went unnoticed, because the allowed-regions policy was still in audit mode there when the monitoring module was first deployed.

## 2. Options

| Option | Pro | Con |
|---|---|---|
| A. Add "global" to the allowed list | Simple | Opens the door for every global resource type, including ones that could process data outside the EU. Security rejected this immediately. |
| B. Exclude the monitoring resource group from the assignment | Simple | Excludes everything in that group, also regional resources. Too broad. |
| C. Scoped exemption for the specific resource type in the monitoring resource group | Narrow, visible, expires | One more file to maintain |
| D. Rewrite the definition to allow "global" only for a list of approved resource types | Precise and reusable | More complex definition, needs testing and review time |

## 3. Decision

Agreed with Kevin and security on 2024-01-11:

- **Short term: option C.** An exemption on the allowed-regions assignment, scoped to the monitoring resource group in each environment, with category "mitigated". Expiry date 2024-07-31, owner the Fortalis cloud team lead. The exemption file in the repository explains why and links to this note.
- **Medium term: option D.** The cloud team adds a parameter with approved global resource types to the definition after handover. When that is done, the exemption is removed. This is listed in the run book as a follow-up item.

The security team confirmed that the monitoring service in question stores its data in the regional log workspace, so the data residency principle is not affected. That confirmation is attached to the exemption pull request.

## 4. Why this did not show up earlier

Our rule is "audit first, then deny". That rule is right, but we only looked at the compliance results of existing resources during the audit period, not at the deployment history of our own modules. A new module deployed during the audit period will pass and only fail later.

Lesson for the remaining work and for anyone building new spokes: **after switching a policy to deny, redeploy every module once in a test environment.** I have added a pipeline job that does exactly that on the sandbox every night, so a deny on one of our own modules is caught before a project hits it.

## 5. Impact on planning

None on the critical path. The acceptance deployment of the shared services spoke was repeated on 2024-01-11 with the exemption in place and succeeded. Production deployment of the shared services spoke stays planned for 2024-01-23, the sandbox spoke for the data team for 2024-01-30.

## 6. Other observations this week

- The datacentre connection on 2024-01-09 went smoothly. Two firewall rules were missing for the internal DNS forwarders; added the same morning through a pull request.
- Compliance on the corporate management group rose from 81% to 89% since the cloud team started cleaning tags on older resources after the holidays.
- The two old test subscriptions in the decommission group still contain resources. The owners have been asked to delete them before the end of February.

*Jonas Peeters*
