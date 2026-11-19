# Closing Report: Fortalis Landing Zone

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Fortalis Landing Zone |
| **Document type** | Closing report |
| **Date** | 2024-02-23 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Version** | 1.0 |

## 1. Summary

The Fortalis Landing Zone project ran from 2023-10-02 to 2024-02-23 and was delivered **on time** and within the **fixed price of EUR 75,000**. Fortalis Verzekeringen now has a production-ready Azure foundation: a hub-spoke network topology, identity and access built on Microsoft Entra ID, and guardrails enforced as policy-as-code with Azure Policy. All infrastructure is defined in Bicep and deployed through pipelines.

The sponsor was Marc Dubois, Chief Digital Officer. My day-to-day counterpart at Fortalis was Kevin Hermans, Enterprise Architect, who owned the architecture decisions on the customer side and chaired the weekly design review.

| Area | Status |
|---|---|
| Scope | Delivered in full |
| Planning | On time |
| Budget | Within fixed price, no change requests |
| Acceptance | Signed off by sponsor |

## 2. What was delivered

**Network: hub-spoke**
- Hub virtual network with Azure Firewall, VPN gateway to the Brussels datacentre and private DNS zones.
- Spoke template for new workloads, peered to the hub, with forced tunnelling to the firewall.
- Two spokes created during the project: a shared services spoke and a sandbox spoke for the data team.

**Identity: Microsoft Entra ID**
- Management group hierarchy aligned with Fortalis' business lines (platform, corporate, sandbox).
- Role-based access with Entra ID groups; privileged roles only through Privileged Identity Management with approval.
- Break-glass accounts documented and stored according to the security team's procedure.

**Governance: Azure Policy as code**
- 46 policy assignments, among them allowed regions (EU only), mandatory tags (cost centre, owner, data classification), deny public IPs on spokes, diagnostic settings to the central Log Analytics workspace.
- Policies stored as Bicep in the platform repository; changes go through pull requests reviewed by Kevin's architecture team.
- Compliance dashboard in Azure Policy; at handover, 98% of resources compliant, remaining items are legacy test resources scheduled for removal.

**Infrastructure as code: Bicep**
- Modular Bicep library (hub, spoke, policy, identity, monitoring).
- Deployment pipelines with what-if previews and manual approval for production.

## 3. How it went

The project ran smoothly. A few points worth recording:

- The allowed-regions policy initially blocked a monitoring service that only deploys to a global location. Resolved with a scoped exemption, documented in the policy repository.
- Naming conventions took three design reviews to agree on. Kevin's insistence on settling them early paid off: no renaming was needed later.
- The Fortalis network team needed time to approve the IP plan for the hub; we used that window to finish the policy work, so the critical path was not affected.

## 4. Handover

- Platform repository, pipelines and run book handed over to the Fortalis cloud team.
- Two training sessions: "Deploying a new spoke" and "Changing a policy safely".
- Kestrel provides four weeks of hypercare until 2024-03-22.

## 5. Recommendations

1. Use the spoke template for every new workload; do not create networks outside it.
2. Review policy compliance monthly in the architecture board.
3. Before onboarding the first AI or data workload, define the data classification tags and the private endpoint approach for PaaS services, so new projects can build on the landing zone without exceptions.

## 6. Acceptance

Accepted by Marc Dubois, Chief Digital Officer, Fortalis Verzekeringen, on 2024-02-23.

*Jonas Peeters, Kestrel Consulting*
