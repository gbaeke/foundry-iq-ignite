# ADR-02: Image Retention and Personal Data on the Inspection Images

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Quality Inspection Vision |
| **Date** | 2025-05-05 |
| **Author** | Amira El Idrissi, ML Engineer and project lead, Kestrel Consulting |
| **Document type** | Architecture decision record |
| **Status** | Accepted (Dries Callens and Tine Desmet, 2025-05-05) |

## Context

The camera on line 3 has been capturing images since 2025-04-15. While reviewing the first captures, the quality team noticed that some images show operators' hands and sleeves, and in a few cases a face, when someone leans over the transfer belt to take a sample or clear a blockage.

The images are needed for labelling and retraining. At the same time, images that show identifiable people are personal data, and Verhaeghe's works council was told during the sensor platform project that the plant floor systems do not monitor individual workers. Dries asked for a clear rule before more images are stored.

ADR-01 (inference on the edge with Azure IoT Edge, only flagged images and counts to the cloud) remains valid. This ADR adds retention and privacy rules.

## Options

1. **Store everything, restrict access.** Simple, but keeps images of people for as long as the training set exists.
2. **Blur people automatically before upload.** Requires a second detection step on the edge and still keeps the original on the device.
3. **Crop to the belt area and drop images with a person in view.** The model only needs the belt. Images where something other than product covers part of the belt are not useful for training anyway.

## Decision

Option 3, combined with short retention on the edge.

- The capture module crops every image to the belt area. The belt edges and the gantry frame are outside the crop.
- Images where more than 10% of the belt area is covered by a large non-product object (a hand, an arm, a tool) are discarded on the edge and never uploaded. A simple rule on the capture module detects this; it does not need to recognise people, only large objects.
- Images on the industrial PC are kept for **7 days** in a ring buffer, for troubleshooting, then deleted.
- Uploaded images (flagged, seeded runs, 1-in-200 random sample) are kept as long as they are part of a training set. Unused uploaded images are deleted after **12 months**.
- The labelling tool shows labeller initials only.

## Consequences

- About 1.5% of captured images are discarded by the rule, mostly during sampling moments. This is acceptable.
- Foreign material that sits on a glove (for example a piece of plastic in an operator's hand) is not captured. Not relevant for inspection.
- Dries will inform the works council of the rule via HR. Tine adds the retention periods to Verhaeghe's processing register.
- The rule must be tested again after every change to the camera position or crop.

## Validation

On 2,300 captured images from 2025-04-15 to 2025-04-30, the rule removed 34 images. Ruben and Dries checked all 34: every one showed a hand or arm. In a random check of 200 kept images, none showed a person.

## Related

- Kickoff decision 2: inference runs on the edge, not in the cloud.
- Labelling tool design note of 2025-04-11.
