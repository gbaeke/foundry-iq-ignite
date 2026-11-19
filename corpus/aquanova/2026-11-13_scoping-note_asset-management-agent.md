# Phase 2 Scoping Note: Asset Management Agent

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Asset Management Agent |
| **Date** | 2026-11-13 |
| **Author** | Lotte Willems, Managing Partner, Kestrel Consulting (with Pieter De Smet) |
| **Document type** | Scoping note (input for the phase 2 proposal) |
| **For** | Filip Wuyts, Kevin Hermans |

## 1. Purpose

At the steering meeting of 2026-10-23, Filip asked for a phase 2 proposal before the end of the year. This note lists the options we see, what each needs, and our recommendation, so that Filip and Kevin can choose the scope. Effort and budget follow in the formal proposal, once the scope is agreed. Phase 1 is not finished yet: the evaluation report and the acceptance session are planned for December.

## 2. Where phase 1 stands

- Agent on Foundry Agent Service in AquaNova's Microsoft Foundry project, private networking only.
- Foundry IQ knowledge base over maintenance procedures, technical sheets and inspection reports (scanned reports excluded).
- Four read-only tools: asset details, maintenance history, assets near a location, open inspection findings.
- Pilot with 12 active planners, around 400 to 450 conversations per month.
- Main limit: asset data quality, in particular duplicate IDs between the two legacy systems. Composite key in place; clean-up by the asset data team in Q1 2027.

## 3. Options

### A. Wider rollout to all asset planners

From about 15 to about 40 planners. Needs onboarding, a support model at AquaNova, monitoring of quality and cost per month, and a lighter evaluation routine that the pilot coordinator can run.

*Dependencies:* none blocking. Best after the register clean-up has started.

### B. Field crew access on tablets

Crews ask about assets on site. Needs a mobile-friendly front end, shorter answers, and a security review by Kevin for access from the field devices. Out of scope in phase 1 by design.

*Dependencies:* Kevin's mobile device policy.

### C. Scanned inspection reports

About 1,400 older reports are excluded because they have no text layer. Converting them makes the history of older assets complete. Needs a one-off conversion and a quality check by planners on a sample.

*Dependencies:* decision on which conversion approach fits AquaNova's platform choices; Kevin to advise.

### D. Support for the register clean-up

The asset data team cleans up duplicate IDs in Q1 2027. Kestrel could help with matching rules and an overlap report per zone, and update the tools once new IDs are assigned.

*Dependencies:* Kevin's clean-up plan, due 2026-11-27.

### E. Write-back: draft work orders

Planners asked whether the agent could prepare a work order. This is a step from reading to writing in source systems, with approval flows and audit trail. We recommend not starting this before A and D are done.

## 4. Recommendation

| Priority | Option | Why |
|---|---|---|
| 1 | D. Register clean-up support | Fixes the root cause of the main quality issue |
| 2 | A. Wider rollout | Most value, once data is cleaner |
| 3 | C. Scanned reports | Completes history, limited effort |
| 4 | B. Field crew access | Valuable, but needs policy work first |
| Later | E. Write-back | Only after the agent is trusted on reading |

We suggest a phase 2 of about six months starting in February 2027, with D and C in the first months and A from spring 2027.

## 5. Team

Same core team as phase 1, so knowledge of the setup and the data issues is kept: Pieter De Smet as lead architect, Jonas Peeters for platform, Ruben Wouters for tools and front end.

## 6. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Scope choice by Filip and Kevin | FW / KH | 2026-11-27 |
| 2 | Formal phase 2 proposal with effort and budget | LW | two weeks after scope choice |
| 3 | Phase 1 acceptance session | LW | December 2026 |

*Lotte Willems, Kestrel Consulting, Ghent*
