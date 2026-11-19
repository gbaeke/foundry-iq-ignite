# Proposal: Container Dwell-Time Forecasting

| | |
|---|---|
| **Customer** | Scaldis Logistics, Antwerp |
| **Project** | Container Dwell-Time Forecasting |
| **Date** | 2023-07-14 |
| **Author** | Lotte Willems, Managing Partner, Kestrel Consulting |
| **Document type** | Proposal |
| **Version** | 1.0 (final, after workshop of 2023-07-04) |

## 1. Context

Scaldis Logistics operates container terminal capacity in the port of Antwerp. Today, yard planners estimate how long an import container will stay on the terminal ("dwell time") based on experience and a few rules of thumb in spreadsheets. When estimates are off, containers end up in the wrong stack, reshuffles go up and truck turnaround times suffer, especially on Mondays after a weekend of vessel calls.

During the workshop on 4 July, Koen Verstraete, CIO and sponsor of this initiative, asked whether historical terminal data could support a more reliable forecast. Nathalie Dumont, Head of Terminal Operations, will act as product owner and represents the planners who will use the forecast daily.

## 2. Objectives

- Forecast the dwell time of each import container at gate-in and at vessel discharge.
- Reach a mean absolute percentage error (MAPE) of 15% or better on a hold-out period of at least eight weeks.
- Deliver the forecast in a form that the yard planning team can consume (daily batch to begin with, intraday refresh as an option).
- Leave Scaldis with a maintainable solution that an internal analytics team can own.

## 3. Approach

We propose four phases:

1. **Data discovery (4 weeks).** Extract gate, vessel and customs-release events from the terminal operating system (TOS) and land them in Azure Data Lake Storage Gen2. Profile data quality and agree a data contract with the TOS administrators.
2. **Feature engineering (6 weeks).** Build feature pipelines in Databricks: carrier, commodity, customs status, vessel rotation, day-of-week and holiday effects.
3. **Modelling and evaluation (8 weeks).** Train and compare models in Azure Machine Learning, with experiment tracking and a registered model. Evaluate against the 15% MAPE target with the planners in the loop.
4. **Industrialisation and handover (8 weeks).** Scheduled scoring, monitoring, documentation and knowledge transfer.

## 4. Proposed team

| Role | Name |
|---|---|
| Project manager | Thomas Maes (Kestrel) |
| Data engineer | Sofie Claes (Kestrel) |
| ML engineer | Amira El Idrissi (Kestrel) |
| Databricks engineer | Bram Visser, DataForge (Utrecht), as subcontractor to Kestrel |

Bram Visser joins through our partner DataForge, a Databricks boutique we work with regularly. Kestrel remains the single contracting party and is responsible for his deliverables. I will stay involved as engagement lead for steering committees.

On the Scaldis side we expect Nathalie Dumont (product owner), one or two yard planners for roughly half a day per week, and access to a TOS administrator.

## 5. Planning

| Milestone | Date |
|---|---|
| Kick-off | 2023-09-04 |
| Data discovery complete | 2023-09-29 |
| Feature pipelines ready | 2023-11-10 |
| Model meets acceptance criteria | 2024-01-19 |
| Handover and project close | 2024-03-29 |

Steering committee every four weeks with Koen and Nathalie; fortnightly demos for the planners.

## 6. Technology

- **Azure Data Lake Storage Gen2** as the landing and curated storage layer
- **Databricks** for ingestion and feature pipelines
- **Azure Machine Learning** for training, model registry and batch scoring

All resources are deployed in the Scaldis Azure tenant (West Europe).

## 7. Commercials

- **Fixed price: EUR 185,000** excl. VAT, covering all four phases.
- Invoicing: 30% at kick-off, 30% at feature pipelines ready, 40% at handover.
- Azure consumption costs are borne directly by Scaldis.
- Changes to scope follow a lightweight change request procedure agreed in the steering committee.

## 8. Assumptions and risks

- TOS data can be exported in batch without custom development by the TOS vendor.
- Event data is reasonably complete; we reserve time in phase 1 for data quality findings.
- Planner availability for evaluation sessions is ensured.

We look forward to working with Scaldis on this.

*Lotte Willems, Kestrel Consulting, Ghent*
