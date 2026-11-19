# Incident Note: Two Network Outages in September

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Quality Inspection Vision |
| **Date** | 2025-09-29 |
| **Author** | Jonas Peeters, Cloud Platform Engineer (edge engineer), Kestrel Consulting |
| **Document type** | Incident note |
| **Distribution** | Tine Desmet, Dries Callens, Amira El Idrissi |

## 1. Summary

In September the inspection devices lost their connection to Azure twice. Both times inspection on the lines kept working, because the model runs locally on the industrial PCs with Azure IoT Edge. Operators kept seeing flags. Only uploads of flagged images and counts were delayed, and they caught up automatically after the connection came back. No data was lost.

## 2. Incident 1: 2025-09-11, 10:12 to 10:53

- **What happened:** a switch in the OT network serving lines 3 and 5 was replaced by the network partner. The change was announced to Tine, but the expected interruption of "a few minutes" took 41 minutes because the new switch needed a configuration fix.
- **Impact on inspection:** none for operators. Only line 3 was in production use at the time; line 5 had its hardware installed but was not live yet.
- **Impact on data:** 41 minutes of uploads queued on the line 3 PC, sent within 6 minutes after reconnecting.

## 3. Incident 2: 2025-09-24, 14:30 to 14:55

- **What happened:** the internet connection of the Roeselare site went down for 25 minutes after a fault at the provider.
- **Impact on inspection:** none for operators on lines 3, 5 and 6.
- **Impact on data:** uploads from all three PCs queued and sent within 10 minutes. Device management showed the devices as "disconnected" during the outage, as expected.
- **Side effect:** the modules on line 6 restarted once at 14:56 when the connection returned. Inspection was interrupted for about 40 seconds. Cause: a setting in the line 6 deployment manifest that differed from lines 3 and 5. Fixed the same day.

## 4. What worked

- Local inference: the design choice from the kickoff (inference on the edge, not in the cloud) did exactly what it was meant to do.
- Local queue on the PCs: sized for 72 hours of uploads. We used less than 1%.
- The offline test on the cutover checklist (pull the network cable for 10 minutes) had already shown the behaviour, so nobody on the line was surprised.

## 5. What we change

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Compare deployment manifests of all three lines automatically on every deployment | JP | 2025-10-03 |
| 2 | Ask the network partner to include the inspection PCs in the impact list of planned OT network changes | TD | 2025-10-10 |
| 3 | Add "what to do if the screen says offline" to the operator one-pager (answer: nothing, keep working) | DC | 2025-10-06 |
| 4 | Alert to Tine if a device is disconnected for more than 2 hours | JP | 2025-10-10 |

## 6. Timeline of go-lives, for reference

- Line 3: pilot from 2025-07-07, enclosure from 2025-08-18
- Line 5: live 2025-09-15
- Line 6: live 2025-09-22
