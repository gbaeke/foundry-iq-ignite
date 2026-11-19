# Design Note: Refresh Architecture and Performance

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Bed Capacity Dashboard |
| **Document type** | Technical design note |
| **Date** | 2023-07-14 |
| **Author** | Sofie Claes, Senior Data Engineer, Kestrel Consulting |
| **Reviewers** | Jeroen Lambrecht (Mediva IT), Elien Jacobs |

## 1. Context

The first Power BI report on the Synapse model was shown to bed managers on 2023-07-07. The content was well received, but two technical concerns came up: the report sometimes showed figures that were 30 minutes old instead of 15, and the ward drill-down took up to 12 seconds to open. This note describes the changes to the refresh chain and the model to fix both.

## 2. Refresh chain before the change

1. ADT file lands every 15 minutes.
2. Synapse pipeline is triggered on a fixed schedule (:00, :15, :30, :45) and rebuilds the bed state for the last 72 hours.
3. Power BI dataset refresh scheduled on its own fixed schedule.

Because the file delivery, the pipeline and the dataset refresh each ran on independent schedules, a file arriving at :16 was only processed at :30 and visible after the dataset refresh at :45 or later.

## 3. Changes

**3.1 Event-driven pipeline.** The Synapse pipeline now starts when a new ADT file arrives, instead of on a fixed schedule. A guard prevents two runs in parallel; if a file arrives during a run, the next run picks it up.

**3.2 Dataset refresh triggered by the pipeline.** At the end of a successful run, the pipeline triggers the Power BI dataset refresh. If the pipeline fails, the dataset keeps the last good state and the report shows the "last update" time in orange after 30 minutes.

**3.3 Smaller dataset.** The report does not need the full event history. The Power BI dataset now contains only:

- the current state per bed (about 1,160 rows)
- the 24-hour outlook per ward
- daily occupancy snapshots for the last 90 days

The full history stays in Synapse for analysis. The dataset went from 1.4 GB to under 40 MB and refreshes in less than a minute.

**3.4 Pre-aggregated ward table.** The drill-down used to compute counts per ward over all beds on the fly. A small aggregated table per ward and status, built in Synapse, brought the drill-down below two seconds in our tests.

## 4. Expected end-to-end latency

| Step | Typical duration |
|---|---|
| File delivery after event recorded | 0 to 15 min |
| Synapse pipeline run | 3 to 5 min |
| Power BI dataset refresh | under 1 min |
| **Worst case visible delay** | **about 21 min** |

Bed managers accepted this; the phone round it replaces was several hours behind by noon.

## 5. Monitoring

- Pipeline failures send a mail to the Mediva IT service desk mailbox (to be confirmed by Jeroen).
- The report header shows the timestamp of the last ADT file processed, per campus.
- A weekly check compares the number of occupied beds with the census count from the hospital information system.

## 6. Cost

The event-driven pipeline runs about 96 times per day. Synapse consumption for the pipelines is estimated at a low two-digit amount per day, which Jeroen considers acceptable. We will review actual consumption after the first month in production and switch off development resources outside office hours.

## 7. Access

Access to the Power BI workspace follows the existing hospital user groups, as decided at kickoff: one group for bed managers and emergency (all campuses), one per campus for head nurses, one for management. No row-level restrictions are needed because the reports contain no patient data.

## 8. Decision requested

Jeroen to approve the event-driven setup and the monitoring mailbox before 2023-07-21, so the change is live before the summer break.
