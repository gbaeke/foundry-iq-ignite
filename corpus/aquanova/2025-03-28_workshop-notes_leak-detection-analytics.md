# Workshop Notes: Field Validation Protocol with Crew Leaders

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Leak Detection Analytics |
| **Date** | 2025-03-28 |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |
| **Document type** | Workshop notes (process) |
| **Participants** | Evelien Claes, the field crew coordinator, two crew leaders from Noord-Oost, a GIS analyst, Amira El Idrissi, Sofie Claes |

## 1. Purpose

Agree how field crews will validate leak candidates during the pilot from 2025-04-07 to mid-May, and how their findings come back into the model. Action item from the steering meeting of 2025-02-07.

## 2. How crews search today

The crew leaders explained their routine. A district is flagged by a rising night flow in the weekly check. They drive the district at night or early morning with listening sticks and a ground microphone, starting with streets where they "know" the pipes are bad. On average a crew needs one to three days to find a leak in a district. Customer calls about water on the street or low pressure often come first.

They were sceptical but curious. One crew leader: "If your map sends me to the right three streets, I'll buy you coffee for a month."

## 3. Agreed protocol

1. **Morning list.** Every crew day, the candidate layer in ArcGIS is refreshed by 07:30. The coordinator picks candidates for the day.
2. **Search area.** Crews search the segments of the candidate first, then the connected segments up to the next valve.
3. **Time box.** Maximum half a day per candidate. If nothing is found, status "not found".
4. **Recording.** Crew leaders update the candidate status in ArcGIS on the tablet: *confirmed* (with location of the leak and type: main, service pipe, fitting, hydrant), or *not found*. Free text is optional.
5. **Repair.** Confirmed leaks follow the normal repair work order process. The work order number is added to the candidate.
6. **No double counting.** If a customer calls about a leak that is also a candidate, it is still counted as confirmed, and marked "also reported".

## 4. What counts as a success

Agreed with Evelien:

- A candidate is **confirmed** if a leak is found within the searched area within the time box.
- We report: number of confirmed leaks, share of candidates confirmed, distance between candidate centre and actual leak, and how many were not yet reported by customers.
- No target number of leaks is set. Filip wants to see whether the approach works, not a quota.

## 5. Concerns raised

- **Too many candidates.** Crews have two days per week. If the list is long and full of false alarms, they will stop using it. Amira: the first week will show how many candidates the current threshold produces; we will adjust quickly.
- **Night work.** Some leaks are only audible at night. The coordinator can plan one night search per week.
- **Tablets.** One crew has an older tablet where the ArcGIS app is slow. The GIS analyst will check before the pilot.

## 6. Feedback loop

- Every Friday: 30-minute call with the coordinator, a crew leader, Amira and a GIS analyst to review the week.
- Candidate status is read back by the retraining pipeline in Azure Machine Learning.

## 7. Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Add status fields to the candidate layer, editable on tablets | GIS analyst | 2025-04-02 |
| 2 | One-page guide for crews: what a candidate is, how to record | AEI / EC | 2025-04-03 |
| 3 | Check the older tablet | GIS analyst | 2025-04-04 |
| 4 | Dry run of the morning refresh on three days | SC / AEI | 2025-04-04 |
| 5 | Plan crew days and one night search per week | Crew coordinator | 2025-04-04 |
