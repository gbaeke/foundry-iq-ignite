# Status Report: Quality Inspection Vision

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Quality Inspection Vision |
| **Date** | 2025-08-25 |
| **Author** | Amira El Idrissi, ML Engineer and project lead, Kestrel Consulting |
| **Document type** | Biweekly status report (no. 12) |
| **Distribution** | Ann Verhaeghe, Dries Callens, Tine Desmet, Lotte Willems |

## 1. Status

| Area | Status | Comment |
|---|---|---|
| Overall | Green | Lighting issue on line 3 solved |
| Scope | Green | Unchanged |
| Schedule | Amber | Rollout to lines 5 and 6 about two weeks later than first planned |
| Budget | Green | About 66% used |
| Quality | Green | False positive rate on line 3 below target |

## 2. Done in the last two weeks

- **Camera enclosure installed on line 3** on 2025-08-18, built by Verhaeghe's maintenance workshop from Jonas' drawing. Closed hood with own LED lighting and a matte inner finish.
- **Effect:** in the first week after installation the false positive rate on line 3 dropped from between 15% and more than 20% in afternoon hours to **3.4%** over the whole day, below the 5% target. There is no longer a difference between morning, afternoon and night.
- **All flags shown again.** The temporary rule from July (only foreign material flags shown in the afternoon) was removed on 2025-08-20.
- **Labelling:** 3,350 images labelled. The second opinion mode raised labeller agreement on discolouration from 71% to 89%.
- **Enclosures for lines 5 and 6** are being built and will be installed before go-live.

## 3. Issue closed

### I-04: Inconsistent lighting on line 3 caused false positives (closed)

Daylight from the skylights and reflections from the stainless frame changed the image during the day, mainly in the afternoon. The pilot on line 3 showed more than 20% false flags in some hours. Solved with the camera enclosure. Lesson for us: check lighting at several times of day during the line walk.

## 4. Model

- The light inside the enclosure is different from the old images. Model v2 works under the new light, but recall on discolouration dropped slightly in the first days because product now looks darker and more even.
- Amira is training **model v3** on a mix of old images and 600 new images taken under enclosure light. Target: 2025-09-08, before line 5 goes live.

## 5. Planning lines 5 and 6

| Line | Enclosure | Edge device and camera | Go-live |
|---|---|---|---|
| 5 | 2025-09-06 (Saturday stop) | installed, tested | 2025-09-15 |
| 6 | 2025-09-13 (Saturday stop) | installed, tested | 2025-09-22 |

The two-week shift compared to the original planning comes from the enclosure, which had to wait for the bouwverlof of the material supplier.

## 6. Risks

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-03 | Discolouration labels inconsistent | Low | Medium | Second opinion mode in place |
| R-05 | Labelling time in harvest season | High | Medium | Third labeller on Fridays until end of September |
| R-07 | Enclosure hinders cleaning | Medium | Medium | Hinged side panel; check with hygiene team after two weeks |
| R-08 | Model v3 not ready before line 5 | Low | Medium | Line 5 can start on v2 |

## 7. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Model v3 trained and evaluated | AEI | 2025-09-08 |
| 2 | Cutover checklist lines 5 and 6 | JP | 2025-09-08 |
| 3 | Hygiene check of the enclosure with the cleaning team | DC | 2025-09-01 |
| 4 | Labelling tool: export of operator feedback on flags | RW | 2025-09-12 |
