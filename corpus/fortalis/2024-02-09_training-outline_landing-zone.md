# Training Outline: Deploying a new spoke / Changing a policy safely

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Fortalis Landing Zone |
| **Document type** | Training material outline |
| **Date** | 2024-02-09 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Audience** | Fortalis cloud team (5 people), two delegates of the architecture team |

## Purpose

Two hands-on sessions to make the Fortalis cloud team self-sufficient before the project closes on 2024-02-23. Both sessions are given on site in Brussels, half a day each, with everyone on their own laptop and access to the sandbox management group. Kevin Hermans asked that the sessions be recorded for colleagues who join the team later.

## Session 1: Deploying a new spoke (2024-02-13, 09:00-12:30)

**Learning goals.** After the session, participants can request, review and deploy a new workload spoke without help from Kestrel, and explain what the spoke gets by default.

| Block | Content | Time |
|---|---|---|
| 1 | Recap of the topology: hub, spokes, forced tunnelling, why no public IPs (ADR-01) | 20 min |
| 2 | Walkthrough of the spoke module in Bicep: parameters, defaults, naming function, subnet layout | 40 min |
| 3 | Exercise: create a spoke parameter file for a fictitious workload "training-tst" in the sandbox | 40 min |
| 4 | Pull request flow: what-if output, reviewers, approval for production | 20 min |
| 5 | Exercise: request a firewall rule for the new spoke and get it reviewed | 30 min |
| 6 | Identity: which Entra ID groups and role assignments a spoke gets, how to add a workload team | 30 min |
| 7 | Questions, checklist handout | 20 min |

**Handout: new spoke checklist**
- IP range reserved in the spoke pool register.
- Tags filled in: cost centre, owner, business line, data classification.
- Workload owner group and reader group requested.
- Firewall rules described per destination, no "any".
- Private endpoints for any PaaS service classified confidential or higher.

## Session 2: Changing a policy safely (2024-02-15, 09:00-12:30)

**Learning goals.** Participants can add or change a policy assignment, run it in audit mode, interpret the compliance results and switch to deny without breaking deployments. They know how to create a time-limited exemption.

| Block | Content | Time |
|---|---|---|
| 1 | Principles from the policy design note: everything as code, audit first, exemptions expire, four eyes | 20 min |
| 2 | Repository structure and pipeline: lint, what-if, the deny test in the sandbox | 30 min |
| 3 | Exercise: add a new tag requirement in audit mode on the sandbox management group | 45 min |
| 4 | Reading the compliance view in Azure Policy; exporting figures for the monthly architecture board | 25 min |
| 5 | Case study: the allowed-regions deny on the monitoring module in January and the scoped exemption | 25 min |
| 6 | Exercise: write an exemption with expiry and owner, get it reviewed | 30 min |
| 7 | Nightly redeploy job: what it does and how to read a failure | 15 min |
| 8 | Questions | 20 min |

## Materials

- Slide deck (Dutch, technical terms in English), maximum 25 slides per session.
- Exercise repository forked from the platform repository, with a dedicated sandbox subscription that is wiped after the training.
- Run book chapters 3 (spokes) and 5 (policy) printed as reference.

## Practical

- Participants need their just-in-time access to the sandbox contributor role activated before the session starts. Activation needs a second approver, so please do it the day before.
- Coffee and broodjes arranged by the Fortalis team assistant.
- Feedback form at the end of each session; results go into the handover file.

*Jonas Peeters*
