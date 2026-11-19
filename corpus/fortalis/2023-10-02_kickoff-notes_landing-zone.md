# Kickoff Notes: Fortalis Landing Zone

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Fortalis Landing Zone |
| **Document type** | Meeting notes (kickoff) |
| **Date** | 2023-10-02 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Location** | Fortalis head office, Brussels, meeting room 4.12 |

## Attendees

- Marc Dubois, Chief Digital Officer, Fortalis Verzekeringen (sponsor, first 30 minutes)
- Kevin Hermans, Enterprise Architect, Fortalis Verzekeringen
- A representative of the Fortalis network team and one of the security team
- Jonas Peeters, Kestrel Consulting (lead engineer)

## 1. Why this project

Marc opened by explaining the context. Fortalis has a handful of workloads in the cloud today, created over the years by different teams, without a common network, naming or access model. Several new initiatives (data, analytics, and possibly AI on claims) are on the roadmap for 2024, and Marc does not want each of them to reinvent the basics. "I want one foundation, built once, that the next projects can just plug into."

The project is a fixed price engagement of EUR 75,000, running from today until 2024-02-23.

## 2. Scope as agreed

- Hub-spoke network topology with central egress through a hub firewall and connectivity to the Brussels datacentre.
- Management group and subscription structure.
- Identity and access model on Microsoft Entra ID: groups, role assignments, privileged access.
- Governance guardrails as policy-as-code with Azure Policy.
- Everything defined as code in Bicep and deployed through pipelines with approval.
- Handover and training for the Fortalis cloud team.

Out of scope: migration of existing workloads, application landing (the first workload spokes are owned by the projects that need them), and the on-premises network changes themselves.

## 3. Ways of working

- **Weekly design review** on Tuesday morning, chaired by Kevin. Decisions are recorded as short architecture decision records (ADR-xx) in the platform repository.
- Jonas works on site at Fortalis on Tuesdays and Thursdays, remote from Ghent the other days.
- Changes to anything that touches the on-premises network go through the Fortalis network team's change board, which meets every second Wednesday. Kevin warned that this board is "thorough, not fast".
- Kevin's architecture team reviews every pull request on the policy definitions.

## 4. First discussions

- **Regions:** Kevin confirmed the board position: data stays in the EU. Allowed regions will be limited to two EU regions, primary and secondary.
- **Naming:** Kevin wants the naming convention settled before any resource is deployed. Jonas proposed a first draft based on the usual pattern (resource type, workload, environment, region, instance). To be discussed at the first design review.
- **Business lines:** the management group structure should reflect how Fortalis is organised, but without creating a group per department. Kevin will bring the current org chart next week.
- **Security:** the security team asked for break-glass accounts to follow their existing vault procedure, and for privileged roles to require approval. Agreed in principle.

## 5. Risks raised

| # | Risk | Owner |
|---|---|---|
| R1 | IP address plan for the hub needs network team approval; lead time unknown | Kevin |
| R2 | Existing workloads may not fit new policies; risk of noise in the compliance view | Jonas |
| R3 | Christmas change freeze at Fortalis from mid-December limits production deployments | Kevin |

## 6. Action items

| Action | Owner | Due |
|---|---|---|
| Share org chart and list of existing subscriptions | KH | 2023-10-06 |
| Draft naming convention and ADR-01 (topology) | JP | 2023-10-10 |
| Request IP ranges from the network team | KH | 2023-10-11 |
| Set up platform repository and first pipeline skeleton | JP | 2023-10-13 |
| Confirm Christmas freeze dates | KH | 2023-10-17 |

Next design review: Tuesday 2023-10-10.

*Jonas Peeters, Kestrel Consulting*
