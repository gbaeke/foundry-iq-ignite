# Tech Talk: Trusting Operational Event Data

| | |
|---|---|
| **Organisation** | Kestrel Consulting (internal) |
| **Date** | 2024-04-12, 15:00 to 16:00 (kennisdeling session, moved from March) |
| **Location** | Kestrel office Ghent and Teams |
| **Author / presenter** | Sofie Claes, Senior Data Engineer |
| **Document type** | Internal tech talk notes |

## Context

This talk used the **Container Dwell-Time Forecasting** project at Scaldis Logistics, which closed on 2024-03-29, as a case. The project forecasts how long import containers stay on the terminal yard. The forecast is only as good as the event history behind it, and the event history came from the terminal operating system (TOS).

## The problem: events that lie

The model needs, for every container, a clean sequence of gate-in, yard moves and gate-out. In the raw data we found:

- **Duplicate gate-in events**: the same container registered twice within minutes, sometimes with a slightly different timestamp, sometimes on a different lane.
- **Missing gate-in events**: containers that appear in yard moves without ever having entered the terminal.
- Late corrections: an event corrected days later by a clerk, overwriting the original.

A dwell time computed on such data is simply wrong, and a model trained on it learns the wrong lesson.

## What we did

1. **Deduplication rules.** Two gate-in events for the same container within a configurable time window are one event; the first one counts, unless the second is a correction. The rules are written down in plain language with the operations team, then implemented in the pipeline.
2. **Inferred events.** For a missing gate-in, we infer the time from the first yard move and flag the record. The model sees the flag as a feature, and the monitoring counts them.
3. **A data contract (v1.0)** for TOS events: field definitions, allowed values, the deduplication rules and what happens when the schema changes. This document made the handover much easier than any notebook.
4. **Quality checks per daily load**: number of duplicates, number of inferred events, and an alert when either jumps.

Result: the model ended at a **MAPE of 11.8%** against a target of 15%, and the solution is now owned by Nathalie Dumont's operations analytics team.

## What I would do differently

- **Talk to the TOS vendor early.** Most of the problems came from how the vendor's system records events. We only had indirect contact through an administrator at the customer, which cost us around two weeks. Next time, a direct technical contact at the vendor goes into the project assumptions.
- **Measure data quality before estimating.** A one-day profiling exercise before the proposal would have told us how much cleaning work there was.
- **Name a data owner for each event type.** Somebody at the customer must be able to say "this is the correct definition".

## Generic takeaways

- Treat operational event data as hostile until proven otherwise: count duplicates, gaps and corrections on day one.
- Write cleaning rules in business language first. If the operations team cannot read them, they cannot own them.
- Flag, do not hide. Inferred or corrected values should stay visible downstream.
- A data contract is a deliverable, not documentation overhead.

## Questions

- *Did the customer accept inferred events?* Yes, once they saw the flags in the output. Planners prefer an honest estimate to a missing one.
- *How often did the rules change?* Three times during the project, each time after a review with the planners.

Slides (anonymised) are on the internal SharePoint.

Sofie
