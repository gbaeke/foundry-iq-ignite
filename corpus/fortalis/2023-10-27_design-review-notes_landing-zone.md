# Design Review Notes: Naming conventions (third round)

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Fortalis Landing Zone |
| **Document type** | Design review notes |
| **Date** | 2023-10-27 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Chair** | Kevin Hermans, Enterprise Architect, Fortalis Verzekeringen |

## Attendees

Kevin Hermans (chair), Jonas Peeters, a delegate of the Fortalis cloud team and a delegate of the security team. This review was moved from Tuesday to Friday because of the autumn school holiday week coming up.

## 1. Background

This was the third review on naming. The first two rounds (2023-10-10 and 2023-10-17) agreed on the general pattern but stalled on three points: how to encode the business line, whether to include the region for global resources, and how to name things that have strict length limits. Kevin's position from the start: "We rename nothing after go-live. So we argue now." In hindsight a reasonable position.

## 2. Decisions

**Pattern.** `<type>-<workload>-<env>-<region>-<nn>`, lowercase, hyphen separated. Example: a spoke network for the shared services workload in production in the primary region becomes `vnet-shared-prd-we-01`.

**Business line.** Not part of the name. It goes into a mandatory tag instead, together with cost centre, owner and data classification. Reason: business lines get reorganised, names should not.

**Environments.** Four codes only: `dev`, `tst`, `acc`, `prd`. The cloud team asked for `sbx` for sandboxes; accepted, since sandboxes live in their own management group and are treated differently anyway.

**Region codes.** Two-letter codes for the two allowed EU regions. Global resources use `gl`.

**Short names.** For resources with tight length limits and no hyphens allowed (storage accounts, for example), the pattern is compressed: type abbreviation, workload, environment, two random characters. A lookup table in the repository documents every exception.

**Management groups and subscriptions.** Names follow the hierarchy proposed in ADR-02 (draft): platform, corporate, sandbox at the first level.

## 3. Enforcement

- The Bicep modules compute names from parameters; nobody types a full name by hand.
- An Azure Policy definition in audit mode checks the pattern on resource groups. We decided against deny for now: a deny on names tends to block emergency fixes. To be revisited after go-live.
- The naming guide becomes part of the run book handed over at the end of the project.

## 4. Other points

- **Tags.** Security asked that the data classification tag uses the same four levels as their information classification policy (public, internal, confidential, strictly confidential). Agreed.
- **Identity.** First discussion on Entra ID group naming. Kevin wants groups named after the role and scope (`grp-az-<scope>-<role>`), not after people or teams. Jonas to include this in the identity design.
- **Cost reporting.** The finance controller would like a monthly cost view per cost centre. This depends entirely on tags being applied, which is one more reason to enforce them from day one.

## 5. Action items

| Action | Owner | Due |
|---|---|---|
| Update naming guide v0.3 with today's decisions | JP | 2023-10-31 |
| Implement naming function in the Bicep module library | JP | 2023-11-07 |
| Audit policy for resource group names | JP | 2023-11-07 |
| Confirm classification levels in writing with security | KH | 2023-11-03 |
| Draft ADR-02 management group hierarchy for review | JP | 2023-11-07 |

Naming is now closed unless someone finds a real blocker. Next design review: 2023-11-07.

*Jonas Peeters*
