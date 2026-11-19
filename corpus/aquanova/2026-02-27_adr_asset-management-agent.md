# ADR-01: Networking and Identity for the Foundry Project

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Asset Management Agent |
| **Date** | 2026-02-27 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Document type** | Architecture decision record |
| **Status** | Accepted by Kevin Hermans, IT Architect, on 2026-02-26 |

## Context

The agent runs in a Microsoft Foundry project in AquaNova's Azure tenant, built on Foundry Agent Service, with a Foundry IQ knowledge base over AquaNova's document libraries and tools that read the asset register and maintenance history.

Kevin's requirements from the kickoff:

1. No public endpoints for the Foundry resources in the target state.
2. Planners only see documents they are allowed to see.
3. Read-only access to source systems, with minimal rights.
4. All configuration as code, so the setup can be rebuilt and reviewed.

AquaNova already runs a hub network in Azure with a connection to the office network. The asset register view is reachable only from inside AquaNova's network.

## Options considered

**A. Private networking from day one.** No public access at all. Safest, but the hub team has a two- to three-week lead time for new network integrations, which would block development in March.

**B. Public endpoints with IP restrictions permanently.** Simple, but against Kevin's requirement 1.

**C. Phased.** Development on restricted public endpoints (Kestrel and AquaNova office IP ranges only) with a limited set of documents, while private networking is built in parallel. Inspection reports and the asset register only after private networking is in place.

## Decision

Option C.

- **Phase 1 (March to May 2026):** Foundry project with restricted public access. Only a copy of maintenance procedures and technical sheets classified as internal (selection approved by Kevin) and an anonymised sample of the asset extracts. No inspection reports, no connection to the asset register.
- **Phase 2 (from June 2026):** private connectivity for the Foundry resources, the knowledge base storage and the tool backend through AquaNova's hub network. Public access switched off resource by resource, with Kevin's sign-off for each.

**Identity**

- Planners sign in with their AquaNova accounts. Access to the web chat through one group "AMA pilot".
- The knowledge base respects document-level permissions of the source libraries. A planner without access to a document does not get answers based on it.
- The tool backend reads the asset register and maintenance history with its own service identity, read-only on the views it needs, nothing else.
- Kestrel engineers get time-limited guest access, reviewed monthly by Kevin.

**Configuration as code**

All resources are described in infrastructure-as-code templates in AquaNova's repository. Changes go through a pull request reviewed by Kevin or his deputy.

## Consequences

- Development can start in March without waiting for the hub team.
- Real data arrives later than in the SOW planning; tools that need the asset register can only be tested end to end from June. This is an explicit risk for sprint block 3.
- Switching off public access later needs a small test plan per resource.
- Document-level permissions must be tested with at least two planners with different access before the pilot.

## Follow-up

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Request network integration with the hub team | KH | 2026-03-06 |
| 2 | Templates for phase 1 | JP | 2026-03-13 |
| 3 | Permission test plan | JP / PDS | 2026-05-29 |
