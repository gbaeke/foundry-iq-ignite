# Handover Notes: Edge Operations Session with IT

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Quality Inspection Vision |
| **Date** | 2025-11-06 |
| **Author** | Jonas Peeters, Cloud Platform Engineer (edge engineer), Kestrel Consulting |
| **Document type** | Handover notes |
| **Participants** | Tine Desmet and her deputy, a maintenance technician, Jonas Peeters, Amira El Idrissi (first hour) |

## 1. What is handed over

| Item | Quantity | Location |
|---|---|---|
| Industrial cameras in enclosures | 3 | lines 3, 5, 6 |
| Industrial PCs running Azure IoT Edge | 3 | electrical cabinets (line 6 in extra cabinet) |
| Operator screens | 3 | next to the transfer belts |
| Spare camera | 1 | IT store room, labelled |
| Deployment manifests per line | 3 | repository in Verhaeghe's subscription |
| Image store and labelling tool | 1 | Verhaeghe Azure subscription |

## 2. Daily and weekly checks

- **Daily (Tine's deputy, 5 minutes):** all three devices "connected" in central device management, flag counts per line for yesterday not zero.
- **Weekly:** disk usage on the PCs (the 7-day ring buffer from ADR-02 should keep it below 60%), upload queue empty.
- **Monthly:** compare the three deployment manifests with the automatic check Jonas added after the September incident.

## 3. Updating a model

The quality team decides when a new model is ready (see the training on 2025-11-12). IT deploys it:

1. Update the model version in the deployment manifest of line 3 only.
2. Watch flags for one full day, compare with the day before.
3. If fine, update lines 5 and 6.
4. Keep the previous model version in the manifest history for rollback.

Tine asked for a rule that no model is deployed on Friday afternoon or before a holiday. Added to the runbook.

## 4. Security and access

- The devices only make outbound connections from the OT segment. No inbound access, no remote desktop. Changes go through central device management only.
- Device credentials are rotated yearly; first rotation planned for November 2026. Procedure in runbook annex A.
- Kestrel guest accounts are removed at the end of the warranty period, on 2025-12-14.
- Four access groups: device admins (Tine and deputy), labellers, reviewers (Dries), model trainers (quality team).

## 5. Physical maintenance (with the maintenance technician)

- **Enclosure:** the hinged side panel is opened for nightly cleaning. Check that the LED bars are dry before closing. Do not use the high-pressure lance directly on the LED strip.
- **Camera lens:** wiped weekly with the cloth in the cabinet. A dirty lens shows as a rise in discolouration flags.
- **Replacing a camera:** spare in the IT store. After replacement, run the crop and discard rule test on 200 images (runbook chapter 3).

## 6. Questions from Tine

- *What happens if a PC dies?* Inspection on that line stops; production continues with manual spot checks as before the project. A spare PC is advised; Tine will order one.
- *Costs?* Azure consumption for image storage, training and device management is about EUR 240 per month. Tine has set a budget alert.
- *Who to call?* During the warranty period, Amira for model questions and Jonas for devices.

## 7. Open points

| # | Point | Owner | Due |
|---|---|---|---|
| 1 | Order a spare industrial PC | TD | 2025-11-28 |
| 2 | Final runbook version | JP | 2025-11-12 |
| 3 | Retraining and labelling session with Dries' team | AEI / RW | 2025-11-12 |
