# Design Note: Labelling Tool, Version 1

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Quality Inspection Vision |
| **Date** | 2025-04-11 |
| **Author** | Ruben Wouters, Junior Developer, Kestrel Consulting |
| **Document type** | Technical design note |
| **Reviewed by** | Amira El Idrissi |

## 1. Goal

Let Dries Callens' quality team label images from the inspection points themselves, quickly and consistently, without installing software. The plan is 4,000 labelled images. With two labellers at about four hours per week each, the tool must make one image take well under a minute on average.

## 2. Users

| Role | What they do |
|---|---|
| Labeller (two people from the quality team) | draw boxes, pick a class, mark OK or uncertain |
| Reviewer (Dries) | review uncertain images, correct labels, see statistics |
| ML engineer (Amira) | export labelled sets for training in Azure AI Vision |

## 3. Main screens

**Queue.** Shows the next image from a randomised queue. Images come from three sources: random captures, images flagged by the model (later, once a model runs), and seeded runs.

**Label view.** The image at full size, the four class buttons with the example photo from the definition sheet, and three actions: *Save*, *OK (no defect)*, *Uncertain*. Keyboard shortcuts: 1 to 4 for classes, O for OK, U for uncertain, Enter to save.

**Review.** For Dries: all uncertain images, with filter per labeller and per class. Dries can accept, change or delete labels.

**Statistics.** Number of labelled images per class against the targets from the workshop of 2025-03-28.

## 4. Data flow

1. The capture module on the edge device saves images on the industrial PC.
2. A selection of images is uploaded to the image store in Verhaeghe's Azure subscription: all flagged images, all seeded runs, and a random sample of 1 in 200 normal images.
3. The labelling tool reads from the image store and writes labels to a small database next to it. Each label records image, box, class, labeller, time.
4. Amira exports a labelled set in the format expected by the custom model training in Azure AI Vision.

Images never leave Verhaeghe's tenant. Labels contain the labeller's initials, not full names.

## 5. Technical choices

- A small web app with a server part and a browser front end. The front end is plain and responsive enough for a 24-inch screen; we do not support phones.
- Sign-in with the existing Verhaeghe accounts of the quality team. Tine Desmet creates one access group for labellers and one for reviewers.
- Hosted in Verhaeghe's subscription, reachable only from the office network.

## 6. What is not in version 1

- Polygon or pixel masks. Boxes are enough for the defect classes we have.
- Model-assisted labelling (pre-drawing boxes from the model). Possible later.
- Labelling on the line itself.

## 7. First feedback (demo of 2025-04-11)

The quality team tried 50 test images in the demo:

- Average 22 seconds per image for OK images, 48 seconds for images with defects.
- They asked for a zoom on mouse wheel; small foreign material is hard to box at normal size.
- They asked for an "undo last save" button.
- Dries asked to see, per labeller, how often their label differs from his review. Ruben will add this to statistics.

## 8. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Zoom and undo | RW | 2025-04-18 |
| 2 | Per-labeller agreement statistic | RW | 2025-05-02 |
| 3 | Access groups for labellers and reviewers | TD | 2025-04-16 |
| 4 | First real labelling session after camera installation | DC | week of 2025-04-22 |
