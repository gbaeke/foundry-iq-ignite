# Design Note: Feature Pipelines and Storage Layout

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Container Dwell-Time Forecasting |
| **Date** | 2023-10-20 |
| **Author** | Bram Visser, Databricks Specialist, DataForge (subcontractor to Kestrel Consulting) |
| **Document type** | Technical design note |
| **Reviewers** | Sofie Claes, Amira El Idrissi |

## 1. Purpose

Describe how TOS events flow from the nightly export to the feature tables used for training and scoring, so that the operations analytics team at Scaldis can maintain the pipelines after handover.

## 2. Storage layout in Azure Data Lake Storage Gen2

One storage account, hierarchical namespace enabled, three containers:

| Container | Content | Retention | Who writes |
|---|---|---|---|
| `raw` | Nightly TOS export files as delivered, partitioned by export date | 5 years | Transfer job only |
| `curated` | Cleaned events: UTC timestamps, carrier aliases mapped, visit IDs resolved | 5 years | Databricks curated jobs |
| `features` | One row per container visit per snapshot date | 2 years | Databricks feature jobs |

Raw files are never modified. Every correction lives in curated and is traceable to a rule with an ID, so planners and the TOS administrator can see why a record changed.

Access: the Databricks workspace reads and writes through a managed identity; individual users get read-only access to curated and features. Scaldis IT asked not to use account keys, which we follow.

## 3. Jobs and schedule

| Job | Start | Typical duration | Depends on |
|---|---|---|---|
| Transfer TOS export to raw | 01:00 | 10 min | TOS export server |
| Curated events | 02:00 | 25 min | raw |
| Feature snapshot | 02:45 | 35 min | curated |
| Scoring (Azure ML, later) | 05:00 | 15 min | features |

The goal is a forecast available to planners before the 06:00 shift change. Jobs run on job clusters that terminate when done; no all-purpose cluster is left running at night. Expected compute cost is modest; we will report actual cost per month to Koen as part of the status report.

## 4. Feature groups

1. **Vessel**: service/rotation, scheduled vs. actual berth time, number of moves of the call, call on a weekend.
2. **Carrier**: mapped carrier code, carrier's rolling median dwell over 8 weeks.
3. **Container**: size/type, reefer flag, empty/full, dangerous goods class present.
4. **Customs**: hold flag, hours since discharge without release, inspection zone visit.
5. **Calendar**: weekday, Belgian public holidays, school holidays, bridge days ("brugdagen"), days to the next holiday.
6. **Truck**: appointment booked, hours between discharge and first appointment slot. Paused until gate-in correction rules exist.

Commodity group is taken from the structured field only; free-text commodity descriptions are out of scope for this phase.

## 5. Point-in-time correctness

Every feature snapshot only uses events known at 02:00 on the snapshot date. This avoids leakage, for example a customs release that was recorded later than it happened. Amira will train on these snapshots exactly as they are produced in production, so training and scoring use the same code.

## 6. Testing

- Unit tests on transformation functions in the repository, run on every merge.
- Row count and null checks after each job; a failed check stops downstream jobs and sends a mail to the team.
- A reconciliation notebook compares daily visit counts with the TOS daily report that the planners already receive.

## 7. Open points

- Gate-in correction rules (Sofie): they will become the first step of the curated job. The feature snapshot design does not change.
- Rail and barge load-outs are confirmed in the export since week 41.
- Naming conventions documented in the repository README; to be reviewed by the analytics team before handover.

Bram Visser
