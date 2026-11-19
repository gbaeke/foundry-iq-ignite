# Data Profiling Note: TOS Event History

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Container Dwell-Time Forecasting |
| **Date** | 2023-09-29 |
| **Author** | Sofie Claes, Senior Data Engineer, Kestrel Consulting |
| **Document type** | Data profiling note |
| **Status** | Final for data discovery milestone |

## 1. Scope of the profile

Three years of event history from the TOS nightly export (September 2020 to August 2023), landed in the raw zone of Azure Data Lake Storage Gen2 and profiled with Databricks notebooks. Following the workshop of 21 September, history before the 2021 yard layout change is kept in raw but excluded from the training window.

| Table | Rows (millions) | Period |
|---|---|---|
| Vessel discharge and load events | 4.1 | 2020-09 to 2023-08 |
| Gate events (in and out) | 5.6 | 2020-09 to 2023-08 |
| Yard moves | 19.8 | 2020-09 to 2023-08 |
| Customs status changes | 2.3 | 2021-01 to 2023-08 |
| Truck appointments | 3.0 | 2022-03 to 2023-08 |

## 2. Completeness

- Discharge events: complete for container vessels; feeder vessels show gaps on two days in 2022 (crane system migration).
- Truck appointments only exist since March 2022, when the booking system was introduced. Features based on appointments will be limited to that period.
- Customs status: the "hold" signal is used consistently since 2022. Before that, only "released" is reliable.

## 3. Early signs of gate-in problems

First checks on gate events show what the planners described:

- Pairs of gate-in records for the same container visit, a few seconds apart, often from different source codes (camera and clerk). We have not quantified this yet across the full history; a first sample of two weeks suggests a few percent.
- Visits with yard moves but no gate-in. The share is small but not negligible.

These are noted as a **data quality risk** for the feature phase. Detailed analysis is planned for sprint 2 together with the TOS administrator. If the pattern is larger than expected, we will need rules in the curated layer before features can be trusted.

## 4. Consistency

- Timestamps are in local time with no offset. The October 2022 daylight saving change produced 1,214 gate-out events that appear before their gate-in. Conversion to UTC with explicit offset handling fixes this.
- Container numbers: 0.3% fail the ISO 6346 check digit, mostly manual entries. These are kept but flagged.
- Carrier codes: 41 active codes, of which 6 are aliases of another code. Mapping table v1 prepared with Bram.

## 5. Target variable

Median dwell time of import containers in the training window is 3.6 days; the distribution has a long tail (containers waiting for inspection or abandoned). We propose to cap the target at 30 days for training and to report MAPE on containers with a dwell time of at least 6 hours, as agreed with Amira and Nathalie. Very short stays make percentage errors meaningless.

## 6. Conclusions for the milestone

The data discovery milestone of 2023-09-29 is met:
- Data is available, extraction works nightly, the data contract v0.1 is circulated.
- The main open topic is gate-in quality. It is a risk for the feature pipeline date of 2023-11-10 if the rules turn out complex.

## 7. Recommendations

- Ask the TOS administrator whether the double registration at lanes 4 and 5 can be stopped at the source. This is unlikely before the TOS update, but worth asking.
- Keep raw data untouched and apply all corrections in the curated layer, so they stay visible and reversible.
- Re-profile monthly; the profile notebooks are parameterised for that.

Sofie Claes
