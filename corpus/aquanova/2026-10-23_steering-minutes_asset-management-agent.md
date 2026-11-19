# Steering Committee Minutes: Asset Management Agent

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Asset Management Agent |
| **Date** | 2026-10-23, 14:00 to 15:30 |
| **Location** | AquaNova offices, Leuven |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Steering committee minutes |

## Attendees

Filip Wuyts (sponsor, chair), Kevin Hermans (IT Architect), the pilot coordinator, Lotte Willems (Kestrel), Pieter De Smet (Kestrel), Jonas Peeters (Kestrel)

## 1. Status

Pieter summarised the September status report and the weeks since:

- 12 active planners in the pilot, 410 conversations in September and a similar pace in October.
- Document answers stable: about 88% correct on procedures.
- Three tools in test with planners. The fourth, open inspection findings, is due on 2026-10-30.
- All Microsoft Foundry resources run without public endpoints since September.

Overall amber, because of asset data quality.

## 2. I-07: Duplicate asset IDs

Pieter recapped: in a sample of 5,000 assets, 312 IDs exist in both legacy systems for different assets. The agent now asks the planner to confirm location or asset type when an ID is ambiguous. Kevin presented two options, as proposed in September.

**Decision 1:** the composite key (source system plus ID) is adopted as the short-term measure. Kevin's team adds it to the register view; Ruben adapts the tools. Target: 2026-11-06. With the composite key, the agent only needs to ask when the planner gives a bare ID without any hint of the asset type.

**Decision 2:** Filip commits two people from the asset data team for the register clean-up from January 2027, in Q1 2027, as Kevin proposed. Kevin will write a short plan. This mitigates R-05.

The pilot coordinator added that planners accepted the extra question well: "They'd rather confirm than be wrong."

## 3. I-08: Response time

Jonas presented the test report of 2026-10-21. With parallel tool calls the median for combined questions drops from 19 to 11 seconds, p90 from 25 to 16 seconds. Release to the pilot on 2026-10-26 approved.

## 4. Budget

Lotte reported about 77% of the EUR 125,000 first phase budget used by mid-October. Kestrel will send the formal 80% notice as foreseen in the SOW, expected in early November.

Remaining phase 1 work:

1. Open inspection findings tool.
2. Composite key in the tools.
3. Evaluation report on the extended evaluation set.
4. Acceptance session with Filip and Kevin.

Lotte confirmed this fits in the remaining budget if no new tools are added. Filip agreed: no new tools in phase 1 (R-06).

## 5. Phase 2

Filip wants a phase 2 proposal before the end of the year. Topics he mentioned: more planners, field crew access on tablets, converting scanned inspection reports, and support for the register clean-up. Kevin added: monitoring and cost reporting for a wider rollout. Lotte and Pieter will send a scoping note by 2026-11-13.

## Decisions

1. Composite key adopted as short-term measure for duplicate IDs.
2. Register clean-up by the asset data team in Q1 2027, two people from January.
3. Latency changes released on 2026-10-26.
4. No new tools in phase 1.

## Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Composite key in register view | KH | 2026-11-04 |
| 2 | Tools adapted to composite key | RW | 2026-11-06 |
| 3 | Clean-up plan for the register | KH | 2026-11-27 |
| 4 | Phase 2 scoping note | LW / PDS | 2026-11-13 |
| 5 | Evaluation report draft | PDS | 2026-11-27 |
| 6 | Formal 80% budget notice | LW | when reached |

Next steering meeting: phase 1 acceptance, date to be set in December.
