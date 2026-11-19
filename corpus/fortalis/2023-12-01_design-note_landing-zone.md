# Design Note: Policy-as-code with Azure Policy

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Fortalis Landing Zone |
| **Document type** | Technical design note |
| **Date** | 2023-12-01 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Reviewers** | Kevin Hermans, Enterprise Architect; Fortalis security team |
| **Version** | 0.9 (for design review of 2023-12-05) |

## 1. Goal

Guardrails on the Fortalis platform must be enforced automatically, versioned and reviewable. No portal clicks, no "we agreed in a meeting". This note describes how policies are written, tested, assigned and changed.

## 2. Principles

1. **Every policy is code.** Definitions, initiatives, assignments and exemptions are Bicep files in the platform repository.
2. **Assign at the highest sensible level.** Most assignments sit on the Fortalis root or on the platform, corporate and sandbox management groups. Assignments at subscription level are exceptions and need a reason in the pull request.
3. **Audit first, then deny.** A new policy starts in audit mode for at least two weeks. We look at the compliance results with the owners of non-compliant resources before switching to deny.
4. **Exemptions expire.** Every exemption has an expiry date, an owner and a link to the reason. No permanent exemptions.
5. **Four eyes.** Changes need approval from one person of Kevin's architecture team and, for security-related policies, one person of the security team.

## 3. Policy set

The target set at handover is about 45 assignments, grouped in four initiatives.

| Initiative | Examples | Effect |
|---|---|---|
| Location and residency | allowed regions (two EU regions only), allowed regions for resource groups | deny |
| Tagging | mandatory tags cost centre, owner, data classification, business line; inherit tags from resource group | deny on new spokes, audit elsewhere |
| Network | deny public IP on spokes, deny peering outside the hub, private DNS zone registration for private endpoints | deny / deploy if not exists |
| Monitoring and security | diagnostic settings to the central log workspace, secure transfer on storage, minimum TLS version | deploy if not exists / deny |

The data classification tag uses the four levels from the Fortalis information classification policy, as confirmed by security on 2023-11-03: public, internal, confidential, strictly confidential. The policy only checks that a valid value is present. What each level implies for a workload (for example, private endpoints mandatory from "confidential") is described in the platform guidelines, and could become a policy later.

## 4. Repository and pipeline

```
/policy
  /definitions      custom definitions, one file each
  /initiatives      grouping of definitions
  /assignments      per management group
  /exemptions       one file per exemption, with expiry
```

The pipeline runs on every pull request:

- Bicep build and lint.
- What-if against the target management group, shown as a comment on the pull request.
- A small test step that deploys a deliberately non-compliant resource into the sandbox and checks that the deny policies actually block it.

Merging to the main branch deploys to development automatically. Production needs a manual approval from the cloud team lead.

## 5. Identity for the pipeline

Following issue I1 from the status report of 2023-11-17, two separate workload identities in Microsoft Entra ID are used: one with rights to deploy platform resources, one with rights to manage policy at management group level only. Neither identity can assign Owner roles.

## 6. Reporting

The built-in Azure Policy compliance view per management group is the reference. Kevin wants a monthly compliance review in the architecture board after handover; the cloud team will export the figures for that meeting. Target at handover: at least 95% compliant resources, excluding resources in the decommission group.

## 7. Open points for the design review

- Do we deny or audit the allowed-SKU policy on the sandbox? Proposal: audit, because sandboxes are for trying things.
- Exemption approval for urgent production fixes outside office hours: who can approve? Proposal: on-call cloud engineer plus security on-call, by phone, regularised next working day.

*Jonas Peeters*
