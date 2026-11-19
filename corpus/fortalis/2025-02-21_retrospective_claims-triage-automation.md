# Retrospective: Claims Triage Automation

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Retrospective notes |
| **Date** | 2025-02-21 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Participants** | Thomas Maes, Jonas Peeters, Amira El Idrissi; Laura Vermeulen joined for the second hour |

## Format

Two hours at the Fortalis office, one week before closure. First hour Kestrel team only, second hour with Laura. Classic format: what went well, what did not, what we do differently next time. Every point needed a concrete example.

## What went well

- **Building on the landing zone.** The spoke was ready in the first week. No discussion about networks, regions or tags. Jonas: "The guardrails meant we never had to argue about security from scratch."
- **Privacy review before real data.** Holding the DPO review before real claims entered acceptance meant no rework. The pseudonymisation rules written then were reused for the monthly retraining.
- **Labelling guidelines and calibration.** Agreement between labellers on urgency went from about two thirds to 84% after one calibration session and a two-page guideline.
- **Proposal mode pilot.** Running on live intake for two months before auto-routing gave us real override figures and showed the storm drift before it could do harm.
- **Overrides as labels.** Designing the handler screen to store every correction with the original prediction made the December retraining possible in days instead of weeks.
- **Load test.** Found the real bottleneck (extraction, not the claims system) and the urgent-claims-in-a-burst problem early.

## What did not go well

- **Water damage started before it was costed.** We said "we'll have a look" in the sprint 9 review and spent about four days before CR-07 was written. Marc was fair about it, but it put the project in amber for the rest of its life. (Thomas)
- **We under-estimated seasonality.** The historical extract contained one mild autumn. Nobody asked "what does a storm Monday look like?" during discovery. (Amira)
- **Dependency on the claims system team.** The write interface came in August instead of June. We had the margin, but only by luck of the plan.
- **Fire as one class.** Fire claims mix smoke, firefighting water and contents. We spent effort trying to improve "fire" as one class when splitting it would have been simpler.
- **Too little time for documentation at the end.** The run book chapters were written in the last three weeks, partly in evenings.

## Laura's view

Laura joined for the second hour. Her points:

- The biggest visible change for her team is not the auto-routed share, but that claims in the human triage queue arrive with fields filled in and highlighted. "Nobody zooms into bad scans anymore."
- The monitoring dashboard is now part of the Monday team lead meeting.
- She would have liked water damage in the original scope, and agreed that Fortalis should have raised it during the proposal.
- New colleagues need training on what an override means. She will include it in the intake onboarding.

## Actions for next projects (Kestrel)

| # | Action | Owner |
|---|---|---|
| 1 | New categories or document types are always a change request, also when asked in a sprint review. Say so in the review itself. | Thomas |
| 2 | Discovery checklist for ML projects: ask explicitly about seasonal peaks and events, and check whether the historical data contains them | Amira |
| 3 | Plan retraining and drift monitoring from the start, not after the first drop | Amira |
| 4 | Book the privacy review in the first month | Jonas |
| 5 | Start run book chapters per component during the build, not at the end | Jonas |
| 6 | Track external interface dependencies in the plan with a named owner on the customer side | Thomas |

## Closing

Thanks to Laura and her team, and in particular to the senior claims handlers who labelled thousands of claims on top of their normal work. Closing report and acceptance planned for 2025-02-28.

*Thomas Maes*
