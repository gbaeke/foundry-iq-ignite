# Sprint Review Notes: Sprints 7 and 8

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Container Dwell-Time Forecasting |
| **Date** | 2024-01-05, 14:00 to 15:00 |
| **Location** | Scaldis terminal, planning office |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Document type** | Sprint review notes |

## Present

Nathalie Dumont, three yard planners (day and late shift), Amira El Idrissi, Sofie Claes, Bram Visser (online), Thomas Maes.

Sprint 7 ran from 2023-12-11 to 2023-12-22; sprint 8 was shortened by the Christmas freeze (no deployments from 2023-12-22 to 2024-01-02) and ends today. The planner demo of 22 December was skipped.

## 1. What was shown

**Tuned model (Amira).** Two model families were compared in Azure Machine Learning on the same feature snapshots: a gradient boosting model and a quantile regression variant. After tuning, the gradient boosting model reaches a MAPE of 13.6% on the validation window (September to November 2023), down from 17.4% in early December. The quantile variant is slightly worse on the point forecast but gives better ranges. Decision in the team: gradient boosting for the point forecast, separate quantile models for the bounds.

**Forecast range.** As agreed in the steering committee of 23 November, the output table now has a P10 and P90 column next to the point forecast. Amira explained it in planner terms: "in eight out of ten cases the box leaves between these two moments". The planners liked that a wide range is a signal in itself: those are the containers to keep accessible.

**Output table (Sofie).** One row per container on the yard at 05:00, with forecast gate-out, P10, P90, a reconstructed gate-in flag and a customs hold flag. The planning spreadsheet reads the table through the existing reporting connection.

**Operations over the holidays (Bram).** Nightly jobs ran every night through the freeze. One failure on 26 December: the TOS export server did not produce a file after a reboot. Rerun manually on the 27th. The reconciliation check caught it before anyone saw stale numbers.

## 2. Planner feedback

- Reefers: forecasts are too optimistic for reefers waiting for a customs inspection. Amira will check whether the inspection zone flag is used correctly for reefer rows.
- Monday effect: visible and correct according to the planners, who recognise "the Monday wave" of trucks.
- Transhipment containers: forecasts are often wrong. Expected: customs-release events for transhipment arrive late (R-07). Planners agree this is less critical for them.
- Request: sort the list by "risk of reshuffle" instead of container number. Small change in the spreadsheet view, done by the planners themselves.

## 3. Formal hold-out

The eight-week hold-out period starts Monday 2024-01-08 and runs to the beginning of March. The model version is frozen for that period; only bug fixes are allowed, documented in the change log. The planners will compare the forecast with reality on a sample each week.

## 4. Risks

| ID | Status | Comment |
|---|---|---|
| R-05 TOS schema change | Open | Koen's written request sent; vendor promises release notes mid-January |
| R-06 Planner availability over holidays | Closed | Freeze period passed |
| R-07 Late customs release for transhipment | Open | Accepted as known limitation for now |

## 5. Next steps

- Planner evaluation session on 2024-01-19 (Nathalie organises, Amira prepares)
- Fix reefer inspection flag if confirmed (AE)
- Draft runbook for nightly jobs and scoring (BV, SC)
- Steering committee 2024-01-25

Thomas Maes
