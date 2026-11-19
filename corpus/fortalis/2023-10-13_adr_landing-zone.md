# ADR-01: Hub-spoke network topology

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Fortalis Landing Zone |
| **Document type** | Architecture decision record |
| **Date** | 2023-10-13 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Status** | Accepted (design review of 2023-10-10, confirmed by Kevin Hermans) |

## Context

Fortalis Verzekeringen needs a network foundation for all new cloud workloads. Today a few workloads have their own isolated networks, each with its own internet exit and, in one case, its own VPN connection to the Brussels datacentre. There is no central point to inspect traffic, and the security team cannot say with confidence which workloads can reach on-premises systems.

Requirements gathered at the kickoff and in the first design review:

- All outbound internet traffic inspected centrally.
- One controlled connection to the Brussels datacentre.
- Workloads isolated from each other by default.
- New workloads must be able to get a network in days, not weeks.
- The model must be expressible in Bicep and guarded by Azure Policy.

## Options considered

1. **Flat network per workload (status quo).** Fast for each team, but no central inspection and duplicated connectivity. Rejected.
2. **Hub-spoke with a self-managed hub.** A central hub network holds the firewall, the gateway to the datacentre and the private DNS zones. Each workload gets a spoke, peered to the hub, with routes forcing traffic through the hub firewall.
3. **Managed virtual WAN style hub.** Attractive for many regions and branches, but Fortalis has one datacentre and two regions at most. More cost and less control over routing for little benefit.

## Decision

We choose **option 2, hub-spoke with a self-managed hub**.

- One hub per region; for now only the primary EU region gets a hub. The secondary region is reserved in the IP plan.
- Spokes are created from a single Bicep spoke module. A spoke always gets: peering to the hub, a route table with forced tunnelling to the hub firewall, a network security group per subnet and diagnostic settings to the central log workspace.
- Spoke-to-spoke traffic goes through the hub firewall and is denied by default.
- No public IP addresses in spokes. This is enforced by Azure Policy with a deny effect, not by convention.
- Private DNS zones live in the hub and are linked to every spoke, so PaaS services with private endpoints resolve correctly.

## Consequences

- **Positive:** one inspection point, one datacentre connection, and a repeatable spoke. Kevin noted that this also gives the security team a single place to look during audits.
- **Negative:** the hub firewall becomes a shared dependency and a cost item that runs whether or not workloads use it. We will size it small and revisit after six months.
- **Negative:** teams used to their own internet exit will need firewall rules requested through a pull request. We will document the process in the run book.
- **Dependency:** the IP plan for hub and spokes must be approved by the Fortalis network team before the hub can be deployed in production. See risk R1 in the kickoff notes.

## IP plan (draft, pending approval)

| Range | Purpose |
|---|---|
| /22 | Hub, primary region |
| /22 | Reserved, hub secondary region |
| /20 | Pool for spokes, primary region, /24 per spoke by default |
| /20 | Reserved pool, secondary region |

## Follow-up

- ADR-02 will cover the management group hierarchy.
- Spoke module interface to be reviewed in the design review of 2023-10-17.

*Jonas Peeters*
