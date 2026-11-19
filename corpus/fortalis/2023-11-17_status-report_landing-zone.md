# Status Report: Fortalis Landing Zone

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Fortalis Landing Zone |
| **Document type** | Status report (biweekly) |
| **Date** | 2023-11-17 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Period** | 2023-11-06 to 2023-11-17 |
| **Distribution** | Marc Dubois, Kevin Hermans |

## 1. Status overview

| Area | Status | Comment |
|---|---|---|
| Overall | Green | On track for 2024-02-23 |
| Scope | Green | No changes |
| Planning | Amber | Hub IP plan still waiting for network team approval |
| Budget | Green | Fixed price, effort in line with plan |
| Quality | Green | All modules pass what-if and linting in the pipeline |

## 2. Progress this period

- **Management groups (ADR-02).** Accepted in the design review of 2023-11-07. Three groups below the Fortalis root: platform, corporate and sandbox. Existing subscriptions were mapped; two old test subscriptions go to a temporary "decommission" group so they no longer pollute the compliance view.
- **Bicep module library.** Hub, spoke and monitoring modules are complete in the development environment. The naming function from the third naming review is used everywhere. Kevin reviewed the spoke module interface and asked for one change: the subnet layout should be a parameter with a sensible default instead of fixed.
- **Identity.** Entra ID groups created for platform owners, network operators, policy contributors and readers, following the agreed `grp-az-<scope>-<role>` pattern. Role assignments are now in Bicep. Privileged roles are only available through just-in-time activation with approval by a second person from the cloud team.
- **Policy-as-code.** First 20 Azure Policy assignments deployed in audit mode on the development management group: allowed regions, mandatory tags, diagnostic settings. Results are as expected: the older workloads are mostly non-compliant on tags.

## 3. Issues and risks

| # | Type | Description | Owner | Action |
|---|---|---|---|---|
| R1 | Risk | Hub IP plan not yet approved; the network team's change board postponed the item on 2023-11-08 for more information on the reserved ranges | KH | Kevin presents again on 2023-11-22 with an annotated plan |
| R2 | Risk | Older workloads fail the tag policies; switching to deny could break their deployments | JP | Keep audit on existing subscriptions; deny only on new spokes; cloud team cleans tags by end January |
| R3 | Risk | Christmas change freeze from 2023-12-18 to 2024-01-05 confirmed by Kevin | JP | Production hub deployment must happen before 2023-12-15 or after 2024-01-08 |
| I1 | Issue | Pipeline service connection needed more rights than the cloud team expected to grant | JP | Split into two identities: one for platform resources, one for policy; approved by security |

If the IP plan is approved on 2023-11-22, the production hub can be deployed in the first week of December, before the freeze. If not, the hub goes to production in the week of 2024-01-08. In the meantime the policy work continues, as it does not depend on the network.

## 4. Next steps

| Action | Owner | Due |
|---|---|---|
| Present annotated IP plan to network change board | KH | 2023-11-22 |
| Remaining policy assignments (public IP deny, private DNS, allowed SKUs) | JP | 2023-12-01 |
| Draft policy-as-code design note for review | JP | 2023-12-01 |
| Break-glass procedure walkthrough with security | JP / KH | 2023-11-24 |
| Decide on production deployment window | KH / JP | 2023-11-24 |

## 5. Note for the sponsor

Marc, nothing needs your attention right now. The one thing to watch is the network approval: if it slips past the freeze, the planning stays green overall but there will be less buffer in January.

*Jonas Peeters, Kestrel Consulting*
