# User Feedback Summary: Operators and Shift Leaders

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Quality Inspection Vision |
| **Date** | 2025-10-13 |
| **Author** | Amira El Idrissi, ML Engineer and project lead, Kestrel Consulting |
| **Document type** | User feedback summary |
| **Period** | 2025-09-22 to 2025-10-10 |

## 1. How we collected feedback

- Short interviews at the line with 14 operators and 5 shift leaders across lines 3, 5 and 6, all three shifts. Dries Callens or a quality technician joined each round, because operators talk more easily with someone they know.
- The "confirm / not a defect" buttons on the operator screen: 6,850 flags with a response in the period.
- Two conversations with the quality team about labelling and reviewing.

Questions asked: Do you look at the screen? When do you ignore it? What would you change?

## 2. What we heard

### It is used, mostly for foreign material

Almost every operator looks at the screen when it beeps for foreign material. "That one I trust. Last week it found a piece of glove before I did." Discolouration flags are looked at, but often accepted without action when the shift is busy.

### Trust took a hit in July, and came back

On line 3, several operators of the afternoon shift remembered the summer, when the screen "flagged everything". Since the enclosure, most say it is "calm" and "mostly right". On lines 5 and 6, which had the enclosure from day one, nobody mentioned false alarms as a problem.

### Small clumps slip through

Shift leaders of lines 5 and 6 mentioned clumps that the screen did not flag, usually small ones of three or four pieces. The operator feedback confirms this: clumps have the lowest confirmation rate of missed-defect reports.

### The screen is in the wrong place on line 6

The operator on line 6 stands on the other side of the belt during most of the shift. The screen is behind him. Maintenance will move it.

### Night shift wants less sound

The night shift asked to switch the beep off for discolouration and clumps, and keep it for foreign material.

## 3. Numbers from the feedback buttons

| Class | Flags with response | Confirmed by operator |
|---|---|---|
| Foreign material | 920 | 95% |
| Discolouration | 3,310 | 89% |
| Clumps | 1,780 | 92% |
| Packaging damage | 840 | 94% |

These are operator judgements under time pressure, not the official evaluation. The evaluation on the final test set is done separately by Dries' team.

## 4. Labelling status

The 4,000 labelled images were reached on 2025-10-10. The quality team now spends about two hours per week reviewing operator "not a defect" responses, which go back into the labelling tool as candidates for the next retraining.

## 5. Actions

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Move the operator screen on line 6 | Maintenance via DC | 2025-10-17 |
| 2 | Sound only for foreign material, all shifts (agreed by Dries for all lines) | JP | 2025-10-15 |
| 3 | Extra clump examples: advise about 500 more images next season | AEI | closing report |
| 4 | Feedback-to-labelling flow documented in the runbook | RW | 2025-10-31 |
| 5 | Short refresher for the afternoon shift of line 3 | DC | 2025-10-24 |

## 6. Our reading

Adoption is good where the system is quiet and right. The July episode shows how fast trust drops after a period of false alarms, and that it takes weeks to recover. For the handover we will stress to Dries' team that thresholds should only be lowered after a trial, never on a single complaint.
