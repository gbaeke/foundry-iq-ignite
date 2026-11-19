# Workshop Notes: Defect Class Definitions

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Quality Inspection Vision |
| **Date** | 2025-03-28 |
| **Author** | Amira El Idrissi, ML Engineer and project lead, Kestrel Consulting |
| **Document type** | Workshop notes |
| **Participants** | Dries Callens, the two quality team members assigned to labelling, Amira El Idrissi, Ruben Wouters |

## 1. Purpose

Agree on clear definitions for the four defect classes of version 1, with example photos, so that labels are consistent. Kickoff action item 4.

Dries brought 60 photos from complaint files and spot checks. Ruben joined to understand how the labelling tool must present classes.

## 2. Definitions agreed

### Foreign material (FM)

Anything that is not the product: stones, wood, plastic, metal, insects, leaves of another crop. Also stems longer than 2 cm for peas and beans.

- Label even when very small, as long as it is visible.
- Pieces of product's own leaf (for spinach) are *not* FM.

### Discolouration (DC)

A piece whose colour is clearly outside normal for the product: brown or black spots larger than about 3 mm, yellowing on green products, grey surfaces from freezer burn.

- Natural colour variation between pieces is *not* a defect.
- This was the hardest class to agree on. The two labellers disagreed on 9 out of 20 example photos. We agreed to mark doubtful cases as "uncertain" rather than force a choice.

### Clumps (CL)

Two or more pieces frozen together into a lump larger than about three times a normal piece. Clumps lead to wrong pack weights and customer complaints.

- Small clumps of two pieces are not labelled in version 1.

### Packaging damage (PD)

Torn or open film, bags with a bad seal visible at the packaging machine infeed side. Version 1 will only see what is visible from the camera position chosen on the line walk.

## 3. Labelling rules

1. Draw a box around each defect. One box per object.
2. An image without defects is labelled "OK". OK images are needed too, in large numbers.
3. "Uncertain" is allowed and preferred over guessing.
4. Do not label partial objects at the image edge unless more than half is visible.
5. Labellers work on images in random order, not in sequence, to avoid labelling "by habit".

## 4. Target numbers

The plan from the kickoff is 4,000 labelled images over the first months. Proposed split:

| Class | Target images containing at least one example |
|---|---|
| Foreign material | 600 |
| Discolouration | 800 |
| Clumps | 700 |
| Packaging damage | 400 |
| OK images | 1,500 |

Real defects are rare on a good day. Dries will ask the line to keep rejected product from the spot checks so we can run it through the inspection point on purpose ("seeded runs").

## 5. Labelling tool requirements (for Ruben)

- Works in a browser on the quality office PCs, no installation.
- Shows the four classes with the agreed example photo next to each button.
- Keyboard shortcuts for speed.
- Shows who labelled what, for later review.
- A filter for "uncertain" images, so Dries can review them weekly.

## 6. Decisions

1. Definitions above are version 1. Changes only via Dries.
2. "Uncertain" is a valid label.
3. Seeded runs once per week, on Wednesday afternoon.

## 7. Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | One-page definition sheet with photos, laminated, in the quality office | DC | 2025-04-04 |
| 2 | Labelling tool first version | RW | 2025-04-11 |
| 3 | Plan seeded runs with line 3 shift leader | DC | 2025-04-09 |
