# Status Report: Quality Inspection Vision

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Quality Inspection Vision |
| **Date** | 2025-04-07 |
| **Author** | Amira El Idrissi, ML Engineer and project lead, Kestrel Consulting |
| **Document type** | Biweekly status report (no. 2) |
| **Distribution** | Ann Verhaeghe, Dries Callens, Tine Desmet, Lotte Willems |

## 1. Status

| Area | Status | Comment |
|---|---|---|
| Overall | Green | On plan |
| Scope | Green | Defect classes agreed |
| Schedule | Green | Hardware delivery expected this week |
| Budget | Green | About 11% of the fixed price used |
| Risks | Amber | Steam and frost, camera position solves most of it |

## 2. Done in the last two weeks

- **Line walk** on line 3 (2025-03-18). Inspection point chosen on the vibrating transfer belt, six metres after the freezer exit, away from the fog.
- **Hardware ordered** on 2025-03-20: three industrial cameras, three industrial PCs, one spare camera.
- **Defect class workshop** (2025-03-28): definitions for foreign material, discolouration, clumps and packaging damage, with example photos. An "uncertain" label is allowed.
- **Network:** Tine's request for the edge devices was approved by the change board on 2025-04-01. The firewall partner implemented it on 2025-04-03. Thank you Tine. Jonas remembers this taking much longer during the sensor platform project.
- **Labelling tool:** Ruben has a first working version on a test environment. Demo planned for the quality team on 2025-04-11.

## 3. Planned for the next two weeks

- Hardware delivery and installation of camera and PC on line 3 (gantry ready on 2025-04-04).
- Azure IoT Edge runtime on the line 3 PC, first capture module deployed.
- Test captures at three belt speeds.
- Labelling tool demo and first labelling session.
- Easter Monday (2025-04-21) is a holiday; the next status meeting moves to Tuesday 2025-04-22.

## 4. Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-01 | Steam and frost affect images | Low (after position choice) | High | Position six metres after freezer exit |
| R-02 | Not enough real defects for labelling | High | High | Weekly seeded runs with rejected product |
| R-03 | Labellers disagree on discolouration | Medium | Medium | "Uncertain" label, weekly review by Dries |
| R-04 | Hardware delivery delayed | Low | Medium | Supplier confirmed week 15 |
| R-05 | Labelling time not available in harvest season | Medium | Medium | Front-load labelling in April to June |

## 5. Decisions needed

None this period.

## 6. Budget

About 11% of the fixed price of EUR 110,000 used. First invoice (kickoff) paid. Hardware is bought by Verhaeghe directly and is not part of the fixed price.
