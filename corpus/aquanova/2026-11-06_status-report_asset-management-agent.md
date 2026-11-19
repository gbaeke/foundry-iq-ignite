# Status Report: Asset Management Agent

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Asset Management Agent |
| **Date** | 2026-11-06 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Monthly status report (October 2026) |
| **Distribution** | Filip Wuyts, Kevin Hermans, Lotte Willems |
| **Project status** | Ongoing |

## 1. Status overview

| Area | Status | Comment |
|---|---|---|
| Overall | Amber | All four tools done; budget at 80% |
| Scope | Green | Phase 1 scope unchanged, no new tools (steering decision) |
| Schedule | Amber | Evaluation report and acceptance in December |
| Budget | Amber | 80% threshold reached, formal notice sent |
| Quality | Green | Asset answers improving with composite key |

## 2. Progress in October

- **Steering meeting** on 2026-10-23: composite key adopted for duplicate asset IDs, register clean-up by the asset data team in Q1 2027 with two people from January, latency changes approved.
- **Fourth tool done.** Ruben finished `get_open_inspection_findings` on 2026-10-29. It returns open findings per asset or per zone, with severity and date. In test with three planners since 2026-10-30.
- **Composite key.** Kevin's team added source system plus ID to the register view on 2026-11-04. Ruben's tool update went live in test on 2026-11-05. The agent now only asks for confirmation when a bare ID matches records in both systems and the question gives no hint of the asset type. In the first two days this happened in 3 of 41 asset questions, against 14 of 52 the week before.
- **Latency.** Parallel tool calls released on 2026-10-26. Over the first ten days, p90 for combined questions is 16.8 seconds. I-08 can be closed if this holds until 2026-11-09.
- **Pilot use.** 12 active planners, 437 conversations in October.
- **Evaluation set** extended with 40 asset-specific questions written by planners, now 180 questions in total.

## 3. Issues

### I-07: Duplicate asset IDs between two legacy systems (open, mitigated)

The short-term measure is in place. The structural clean-up is planned for Q1 2027 by the asset data team. Kevin is writing the plan (due 2026-11-27). It no longer blocks the pilot.

### I-08: Slow responses on combined questions (open, closing)

See above.

### I-09: Inspection findings without asset reference (new)

About 6% of open inspection findings have a zone but no asset ID. The new tool returns them only for zone questions. Reported to the asset data team as part of the clean-up scope.

## 4. Budget

On 2026-11-02 Lotte sent the formal notice foreseen in the SOW: 80% of the EUR 125,000 first phase budget has been used. The remaining work agreed at the steering meeting (composite key in tools, evaluation report, acceptance session) is estimated to fit within the remaining 20%. No new work will be started in phase 1 without a written decision by Filip.

## 5. Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-03 | Planners lose trust after wrong asset answers | Low | High | ID check and composite key in place |
| R-05 | Register clean-up not staffed in time | Low | Medium | Two people committed by Filip from January 2027 |
| R-06 | Budget insufficient to finish phase 1 | Medium | Medium | Scope frozen; weekly burn check by Lotte |

## 6. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Phase 2 scoping note | LW / PDS | 2026-11-13 |
| 2 | Full evaluation run on the 180-question set | PDS / two planners | 2026-11-20 |
| 3 | Evaluation report draft | PDS | 2026-11-27 |
| 4 | Register clean-up plan | KH | 2026-11-27 |
| 5 | Release fourth tool to the whole pilot group | RW | 2026-11-13 |
| 6 | Acceptance session with Filip and Kevin | LW | December, date to be set |
