# Steering Committee Minutes #3: Container Dwell-Time Forecasting

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Container Dwell-Time Forecasting |
| **Date** | 2023-11-23, 15:00 to 15:50 |
| **Location** | Scaldis HQ Antwerp and online |
| **Author** | Lotte Willems, Managing Partner, Kestrel Consulting |
| **Document type** | Steering committee minutes |

## Attendees

Koen Verstraete (CIO, sponsor), Nathalie Dumont (Head of Terminal Operations, product owner), Lotte Willems (engagement lead), Thomas Maes (project manager). Sofie Claes joined for item 2.

## 1. Status

Thomas summarised status report #3: overall amber, data quality red, schedule amber because of the gate-in issue. Budget green at 38% consumed on 10 November. Feature groups other than truck features are complete.

## 2. Gate-in data quality (I-03)

Sofie presented the correction rules agreed by mail with Nathalie and the TOS administrator:
- GI-01 removes duplicate gate-in records (about 6% of gate-in events, mainly lanes 4 and 5);
- GI-02 reconstructs a missing gate-in (about 2% of visits) from the truck appointment or the first yard position, with a per-block-type gate-to-stack time;
- reconstructed records stay flagged up to the planners' output.

The rules were deployed to the curated job on 21 November. First checks against the gate supervisor's 2023 outage lists explain most of the missing gate-ins. Koen asked whether this is a permanent fix. Sofie: it is a correction downstream; the root cause sits in the gate workflow and the TOS. The TOS update next year may remove the double registration, but it may also change the data.

**Decision:** I-03 can be closed once the rules have run one full week without incidents. Thomas to confirm in the next status report.

## 3. Milestone and invoicing

**Decision:** the steering committee accepts that the "feature pipelines ready" milestone moves from 2023-11-10 to 2023-11-24. The second invoice (30%) follows the milestone. The final date of 2024-03-29 stays.

## 4. TOS schema change (R-05)

Koen contacted the TOS vendor's account manager. The vendor confirms an update in Q1 2024 but did not yet share technical release notes. A direct technical contact for Kestrel was not granted; communication goes through the Scaldis TOS administrator. Lotte stressed that this is the biggest external dependency of the project and asked for the release notes as soon as they exist.

**Action:** KV to ask again in writing for the gate module and export changes, with a copy to Thomas.

## 5. Holiday period

Nathalie reminded everyone that the terminal has a change freeze around Christmas and New Year. Agreed:
- no deployments from 2023-12-22 to 2024-01-02;
- planner evaluation session planned in week 3 of January, when the planning team is back at full strength;
- R-06 (planner availability over the holidays) to be added to the risk log.

## 6. Planners' requests

Planners would like a range next to the forecast. Amira's view, relayed by Thomas: a lower and upper bound can come from the same model family at limited extra effort. **Decision:** included without scope change, as long as it remains a column in the output table and not a new user interface.

## 7. Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Written request to TOS vendor for Q1 release notes | KV | 2023-11-30 |
| 2 | Confirm closure of I-03 in status report #4 | TM | 2023-12-08 |
| 3 | Add R-06 to the risk log | TM | 2023-11-24 |
| 4 | Plan planner evaluation session, week 3 of January | ND | 2023-12-15 |
| 5 | Prototype forecast range column | AE | 2024-01-05 |

Next steering committee: 2023-12-21 (short, online, if needed) and otherwise 2024-01-25.

*Minutes by Lotte Willems*
