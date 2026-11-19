# Status Report: Asset Management Agent

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Asset Management Agent |
| **Date** | 2026-10-09 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Monthly status report (September 2026) |
| **Distribution** | Filip Wuyts, Kevin Hermans, Lotte Willems |
| **Project status** | Ongoing |

## 1. Status overview

| Area | Status | Comment |
|---|---|---|
| Overall | Amber | Pilot running, asset data quality limits answers |
| Scope | Green | Phase 1 scope unchanged |
| Schedule | Amber | Asset tools later than planned |
| Budget | Green | About 71% of the first phase budget used |
| Quality | Amber | Good on documents, weaker on asset-specific questions |

## 2. Progress in September

- **Pilot.** 12 asset planners use the agent, with 410 conversations in September. Most questions are about maintenance history and inspection results of a single asset.
- **Knowledge base.** The Foundry IQ knowledge base now covers maintenance procedures, inspection reports and technical sheets. Answers on procedures score well in the evaluation (about 88% judged correct by the planners).
- **Agent tools.** Ruben is building the agent tools in Foundry Agent Service: "get asset details", "get maintenance history" and "find assets near location" are in test. A tool for open inspection findings is next.
- **Platform.** Jonas finished the private networking setup with Kevin. All Microsoft Foundry resources now run without public endpoints.

## 3. Issues

### I-07: Duplicate asset IDs between two legacy systems (open)

The asset register combines data from two legacy systems. During testing we found that a number of asset IDs exist in both systems but refer to different assets, mostly valves and hydrants added in the years when both systems were in use. In a sample of 5,000 assets, 312 IDs were duplicated.

Impact: when a planner asks about an asset by ID, the agent can return the history of the wrong asset. Ruben has added a check to the tool: if an ID matches more than one record, the agent asks the planner to confirm the location or asset type before answering. This prevents wrong answers but adds a step.

Structural fix: AquaNova needs to clean up the register. Kevin proposes a composite key (source system plus ID) as a short-term measure and a clean-up by the asset data team in Q1 2027. Decision expected at the next steering meeting.

### I-08: Slow responses on combined questions (open)

Questions that need both the knowledge base and two tools take up to 25 seconds. We are testing parallel tool calls.

## 4. Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-03 | Planners lose trust after wrong asset answers | Medium | High | ID check in tools, communication to pilot group |
| R-05 | Register clean-up not staffed in time | Medium | Medium | Filip to confirm capacity |
| R-06 | Budget insufficient to finish all tools in phase 1 | Medium | Medium | Prioritise tools with the pilot coordinator |

## 5. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Decide on composite key for asset IDs | KH / FW | 2026-10-23 |
| 2 | Finish "open inspection findings" tool | RW | 2026-10-30 |
| 3 | Test parallel tool calls, report on latency | JP | 2026-10-23 |
| 4 | Extend evaluation set with asset-specific questions | PDS | 2026-10-30 |
| 5 | Proposal for phase 2 scope and budget | PDS / LW | 2026-11-13 |

Next steering meeting: 2026-10-23, AquaNova offices in Leuven.
