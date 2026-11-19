# Data Mapping Note: ADT Events to Bed Model

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Bed Capacity Dashboard |
| **Document type** | Data mapping note |
| **Date** | 2023-06-09 |
| **Author** | Sofie Claes, Senior Data Engineer, Kestrel Consulting |
| **Version** | 0.9 (for review by Mediva IT) |

## 1. Purpose

This note describes how admission, discharge and transfer (ADT) events from the hospital information system are mapped to the bed-level model in Azure Synapse Analytics. It is the basis for the Power BI reports and for the definitions agreed in the workshop of 2023-05-24. No patient-identifying attributes are loaded; the patient is represented only by a stay key generated in the extract.

## 2. Source

The ADT extract is delivered by Mediva IT as files every 15 minutes, containing all events since the previous file. Each event has: event type, event timestamp, recorded timestamp, stay key, campus code, ward code, room code, bed code, specialty code and, for discharges, the planned discharge date.

Observed volume in the test month: about 9,000 events per day across the three campuses.

## 3. Event mapping

| Source event | Meaning | Effect on bed model |
|---|---|---|
| A01 admit | Patient admitted to a bed | Bed becomes occupied |
| A02 transfer | Patient moves to another bed | Old bed free, new bed occupied |
| A03 discharge | Patient discharged | Bed becomes free |
| A08 update | Data update, often planned discharge date | Update outlook only |
| A11 cancel admit | Admission cancelled | Revert to previous state |
| A12 cancel transfer | Transfer cancelled | Revert both beds |
| A13 cancel discharge | Discharge cancelled | Bed occupied again |

The cancel events are the tricky part: about 2% of events are cancellations, sometimes arriving hours later. The model therefore rebuilds the state of the last 72 hours on every run instead of applying events one by one.

## 4. Blocked beds

Blocked beds are not ADT events. They are recorded in a separate bed status table in the hospital information system, with a free-text reason field. In the sample of 1,400 blocks:

- 61% had a recognisable reason ("isolatie", "onderhoud", "defect", "gereserveerd")
- 27% had an empty reason
- 12% had something else ("zie dokter", "familie", initials of a nurse)

Mapping to the four agreed reasons is done with a keyword list maintained by the bed management office. Empty and unrecognised reasons map to "other". I propose that the bed management office reviews the "other" list monthly; without that, the category will grow.

## 5. Master data: the bed list

The official bed list from facility management contains 1,118 beds. In the ADT events of the test month we saw 1,163 distinct bed codes. The difference:

- 29 bed codes that are corridor or overflow beds used during peaks
- 11 codes for beds that were removed during a renovation but are still used in the system
- 5 codes that look like typing errors

Proposal: the model uses the official list as reference and shows unknown bed codes in a separate "unmapped" table that the bed management office reviews. Overflow beds get a flag and appear in the overview only when occupied. This needs confirmation from the bed management office before the first go-live.

## 6. Timing and late events

Event timestamp and recorded timestamp can differ by several hours, especially for night-time discharges entered the next morning. The dashboard uses the recorded timestamp for the current state (what the system knows now) and shows a "last update" time per ward, so users understand why a ward lags behind.

## 7. Open questions for Mediva IT

1. Can the extract include the bed status table changes in the same 15-minute delivery? (Today it is delivered daily.)
2. Are the specialty codes stable across campuses? Campus Zuid uses two local codes for geriatrics.
3. Who is the contact for changes to the ADT extract format?

Please send comments to Sofie by 2023-06-16.
