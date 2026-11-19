# Workshop Notes: Gate and Yard Events

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Container Dwell-Time Forecasting |
| **Date** | 2023-09-21 |
| **Location** | Scaldis terminal, planning office, first floor |
| **Author** | Sofie Claes, Senior Data Engineer, Kestrel Consulting |
| **Document type** | Workshop notes |

## Participants

Nathalie Dumont (product owner), two yard planners from the day shift, the Scaldis TOS administrator, Sofie Claes, Bram Visser (DataForge), Amira El Idrissi.

## Purpose

Understand which events in the terminal operating system (TOS) mark the start and the end of a container's stay, and how reliable each event is in practice. The result feeds data contract v0.1.

## 1. Lifecycle of an import container

The planners walked us through a typical import box, on a whiteboard:

1. **Vessel discharge**: quay crane moves the container to the yard. Event recorded automatically by the crane system and pushed to the TOS.
2. **Yard moves**: zero or more reshuffles. Recorded by straddle carrier drivers on their terminals.
3. **Customs release**: status update from the customs channel. Arrival time varies a lot.
4. **Truck appointment**: the haulier books a slot. Not always used.
5. **Gate-out**: the truck leaves with the box. This ends the dwell period.

For export and empty containers the sequence starts with a **gate-in** at the truck gate. Gate-in also matters for imports that go back in after inspection. The planners agreed that dwell time is measured from discharge (or gate-in) to gate-out, in hours.

## 2. Known quirks (planner view)

- "At the truck gate, sometimes the OCR camera and the clerk both register the box." The planners believe this causes double gate-in records, mostly at lanes 4 and 5.
- During gate outages, clerks register containers afterwards in a batch, or not at all, and the first trace is a yard move.
- Containers moved to the inspection zone for customs scanning get a separate set of yard moves that can look like a second stay.
- Daylight saving changes (last Sunday of October) have caused odd timestamps before.

## 3. Decisions for the data contract

| Topic | Decision |
|---|---|
| Unit of analysis | One stay per container visit, identified by container number + visit ID from the TOS |
| Start event | Discharge for imports; first gate-in otherwise |
| End event | Gate-out, or rail/barge load-out |
| Timestamps | Stored in UTC in the curated zone; local time only in outputs for planners |
| Arbiter | Planners for business meaning, TOS administrator for technical questions |
| Inspection zone moves | Kept, flagged, not treated as a new visit |

## 4. Master data

- Carrier codes are maintained by hand in the TOS. The administrator knows of at least three carriers with two codes after a merger. Bram will build a small mapping table, owned by the planners after handover.
- Commodity groups are free text for about a third of containers. Amira will start with the structured part only.

## 5. Open questions

- Is there a reliable signal for "customs hold"? The administrator will check which status codes are used today.
- Rail and barge departures come from a different module; confirm they are in the nightly export.
- How many years of history are representative? The planners suggest not using anything before the 2021 yard layout change.

## 6. Next steps

| Action | Owner | Due |
|---|---|---|
| Data contract v0.1 to Nathalie and the TOS administrator | SC | 2023-09-22 |
| Profiling of three years of gate and yard events | SC, BV | 2023-09-28 |
| Carrier code mapping table, first version | BV | 2023-10-06 |
| Check customs hold status codes | TOS administrator | 2023-09-27 |

Thanks to the planners for their time during a busy week on the terminal.

Sofie
