# Kick-off Meeting Notes: Container Dwell-Time Forecasting

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Container Dwell-Time Forecasting |
| **Date** | 2023-09-04, 10:00 to 12:30 |
| **Location** | Scaldis HQ Antwerp, meeting room "Kaai 3" |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Document type** | Meeting notes |

## Attendees

**Scaldis Logistics:** Koen Verstraete (CIO, sponsor), Nathalie Dumont (Head of Terminal Operations, product owner), a senior yard planner, a TOS administrator from Scaldis IT.

**Kestrel Consulting:** Lotte Willems (engagement lead), Thomas Maes (project manager), Sofie Claes (data engineer), Amira El Idrissi (ML engineer).

**DataForge:** Bram Visser (Databricks engineer, subcontracted via Kestrel).

## 1. Opening

Koen recalled why the project exists: dwell-time estimates are made in the planners' heads and in a planning spreadsheet, and Monday mornings after a weekend of vessel calls are when it goes wrong. He wants a forecast the planners trust, not a model that sits in a lab. Nathalie added that the planners must be part of every evaluation; if they do not believe the numbers, they will keep stacking by gut feeling.

## 2. Scope recap

- Forecast of dwell time per import container, at discharge and at gate-in
- Acceptance target: MAPE of 15% or better on a hold-out period of at least eight weeks
- Daily batch output first; intraday refresh is an option, not a commitment
- Transhipment containers are in the data but not a priority use case for the planners

## 3. Way of working

- Sprint 0 (inception) from 2023-09-04 to 2023-09-15, then two-week sprints starting 2023-09-18.
- Demo for planners every other Friday at 14:00, short and on the terminal site, not in Ghent.
- Steering committee every four weeks on Thursday with Koen and Nathalie, Lotte attending for Kestrel. First one on 2023-09-28.
- Status report every four weeks by Thomas, used as input for the next steering committee.
- Team channel and shared project folder on the Scaldis side; Bram works with a Scaldis guest account like the Kestrel team.

## 4. Environment and data

- All resources in the Scaldis Azure tenant, West Europe: one Azure Data Lake Storage Gen2 account (raw, curated and feature zones), one Databricks workspace, one Azure Machine Learning workspace.
- The TOS administrator confirmed that a nightly batch export of gate, vessel and customs-release events is possible without involving the TOS vendor, using the existing reporting export. History available from September 2020.
- The TOS sits on the terminal operations network segment. Scaldis IT will open a one-way file transfer from that segment to the landing zone; no direct connection from the cloud into the TOS.

## 5. Discussion points

- Sofie asked who decides when TOS data is "wrong". Nathalie: the planners, with the TOS administrator as arbiter for technical questions. To be written into the data contract.
- Amira asked whether public holidays and the port's weekend patterns may be used as features. Yes; the planners also pointed to strike days, which are harder to anticipate.
- Koen asked how Scaldis will run the model after March. Answer: handover to the operations analytics team is a deliverable, with knowledge transfer planned from February.

## 6. Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Create storage, Databricks and Azure ML resources, grant team access | KV (Scaldis IT) | 2023-09-08 |
| 2 | Deliver first full TOS history export (3 years) | TOS administrator | 2023-09-13 |
| 3 | Draft data contract v0.1 for TOS events | SC | 2023-09-22 |
| 4 | Workshop on gate and yard events with planners | SC, ND | 2023-09-21 |
| 5 | Workspace conventions and repository structure for pipelines | BV | 2023-09-15 |
| 6 | Baseline definition: current planner estimate as benchmark | AE, ND | 2023-09-29 |
| 7 | Plan demo and steering committee calendar | TM | 2023-09-08 |

## 7. Next meeting

First planner demo on 2023-09-29 (data discovery results). First steering committee on 2023-09-28.

*Notes by Thomas Maes*
