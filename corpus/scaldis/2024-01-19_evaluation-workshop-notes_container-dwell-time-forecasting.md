# Evaluation Workshop Notes: Planner Acceptance

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Container Dwell-Time Forecasting |
| **Date** | 2024-01-19, 09:00 to 11:30 |
| **Location** | Scaldis terminal, planning office |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |
| **Document type** | Workshop notes (evaluation) |

## Participants

Nathalie Dumont (product owner), four yard planners, one member of the operations analytics team, Amira El Idrissi, Sofie Claes, Thomas Maes.

## 1. Goal

Check with the people who use the forecast whether the model meets the acceptance criteria, before the formal hold-out result is known. This is the milestone "model meets acceptance criteria" of 2024-01-19 in the proposal.

## 2. Quantitative results

| Evaluation | Window | MAPE | Planner baseline |
|---|---|---|---|
| Rolling backtest | 2023-09 to 2023-12 | 12.6% | ~31% |
| First two weeks of hold-out | 2024-01-08 to 2024-01-19 | 12.9% | ~30% |
| Transhipment only (backtest) | 2023-09 to 2023-12 | ~16% | n/a |

MAPE is computed on containers with a dwell time of at least 6 hours, as agreed during data discovery. The P10–P90 range contains the actual gate-out in 79% of cases, close to the intended 80%.

The reefer issue from the last sprint review was real: reefer containers in the inspection zone were not getting the inspection flag because their yard moves use a different block prefix. Fixed on 2024-01-10 as a documented bug fix; the hold-out continues with that fix.

## 3. Case review

Each planner brought five containers where they thought the forecast was "wrong". We reviewed 20 cases together:

- 9 cases: forecast was right, the planner's expectation was wrong (often a carrier that changed its free-time policy).
- 6 cases: customs hold released unexpectedly fast or slow. The model cannot know this in advance.
- 3 cases: transhipment.
- 2 cases: data issue, a gate-out registered on the wrong visit. Sent to the TOS administrator.

This exercise did more for trust than the MAPE table. One planner: "So it knows the carriers better than me now. Fine, but it does not know the customs officer."

## 4. Usability

- The range columns are used; planners already put wide-range containers on the accessible rows.
- Requested: show the forecast in days and hours instead of decimal hours. Done in the spreadsheet view.
- Requested: keep the 05:30 availability. The morning shift plans between 05:45 and 06:30.

## 5. Acceptance decision

Nathalie accepted the milestone on the condition that the full eight-week hold-out confirms a MAPE of 15% or better. If the hold-out ends above 15%, Kestrel will propose corrective work within the fixed price. Thomas will note the conditional acceptance in the next status report and the steering committee of 25 January.

## 6. Data quality observations

- The share of reconstructed gate-ins stays around 2% of visits, as expected.
- After the TOS vendor's release notes arrived this week, Sofie confirmed the gate module will rename two export columns and add a new source code for the OCR portal. Extraction will be adapted before the update.

## 7. Next steps

| Action | Owner | Due |
|---|---|---|
| Weekly hold-out tracking report to Nathalie | AE | Every Monday |
| Adapt extraction to TOS release notes | SC | 2024-02-09 |
| Start knowledge transfer plan with the analytics team | SC, AE | 2024-02-16 |
| Send two wrong-visit cases to TOS administrator | ND | 2024-01-24 |

Amira El Idrissi
