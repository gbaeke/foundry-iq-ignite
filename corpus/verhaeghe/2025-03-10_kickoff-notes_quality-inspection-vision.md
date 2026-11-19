# Kickoff Meeting Notes: Quality Inspection Vision

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Quality Inspection Vision |
| **Date** | 2025-03-10, 09:30 to 12:00 |
| **Location** | Verhaeghe Foods, Roeselare (meeting room above the packaging hall) |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |
| **Document type** | Meeting notes |

## Attendees

- Dries Callens, Quality Manager, Verhaeghe Foods (product owner)
- Tine Desmet, IT Coordinator, Verhaeghe Foods
- Amira El Idrissi, ML Engineer, Kestrel Consulting (project lead)
- Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting (edge engineer)

Excused: Ann Verhaeghe (sponsor), who confirmed the signed order by mail on Friday.

## 1. Goal and scope

Dries explained the problem. Quality checks on the frozen vegetable lines are visual and done by operators on spot samples: foreign material, discoloured pieces, clumps and damaged packaging. Defects found at the customer cost much more than defects found on the line. The goal is automatic visual inspection with a camera above the belt, flagging suspect product for the operator in real time.

Scope for this project: three lines, starting with line 3 as pilot because it has the most quality complaints. Rejection stays manual. The system flags, the operator decides.

## 2. Technical approach

Amira presented the approach:

- A **custom model in Azure AI Vision**, trained on images from Verhaeghe's own lines.
- The model runs locally on an industrial PC next to each line, deployed with **Azure IoT Edge**. Inference happens on the edge, so a network outage does not stop the inspection.
- Only flagged images and counts are sent to the cloud, for retraining and reporting.
- **Labelling:** the plan is to label **4,000 images** over the first months, covering the main defect classes. Kestrel will provide a simple labelling tool so that Dries' quality team can label images themselves.

Jonas explained the edge setup: one camera and one industrial PC per line, managed centrally through IoT Edge, with updates rolled out line by line.

## 3. Network and access

Tine confirmed that the network path for the edge devices will be requested this week, before any hardware goes on the line, given the experience during the sensor platform project. The edge devices will sit in the same OT segment as the existing line gateways.

## 4. Commercials and planning

- Contract: **fixed price, EUR 110,000** excl. VAT, as in the signed proposal.
- Start: today, 2025-03-10. Target handover mid-November 2025.
- Rough phases: camera installation and image capture (March to May), labelling and first model (May to July), pilot on line 3 (summer), rollout to the other two lines and handover (autumn).

## 5. Discussion points

- Dries is worried about steam and frost near the freezer exit affecting image quality. Jonas will look at camera positions on the day of the line walk.
- Belt speed varies per product. Amira will capture images at different speeds from the start.
- Who labels? Dries will assign two people from the quality team, about four hours per week each.

## 6. Decisions

1. Line 3 is the pilot line.
2. Inference runs on the edge, not in the cloud.
3. Defect classes for version 1: foreign material, discolouration, clumps, packaging damage.
4. The system only flags; operators keep the reject decision.

## Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Submit firewall and network request for edge devices on lines 3, 5 and 6 | TD | 2025-03-14 |
| 2 | Line walk on line 3, decide camera position | JP / DC | 2025-03-18 |
| 3 | Order cameras and industrial PCs | JP | 2025-03-21 |
| 4 | Draft defect class definitions with example photos | DC | 2025-03-28 |
| 5 | Set up labelling tool and image storage | AEI | 2025-04-11 |
| 6 | Assign two quality team members for labelling | DC | 2025-03-21 |

Next meeting: 2025-03-24, bi-weekly on Monday mornings.
