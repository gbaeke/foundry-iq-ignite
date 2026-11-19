# Line Walk Notes: Line 3 Inspection Point

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Quality Inspection Vision |
| **Date** | 2025-03-18 |
| **Author** | Jonas Peeters, Cloud Platform Engineer (edge engineer), Kestrel Consulting |
| **Document type** | Site visit notes |
| **Present** | Dries Callens, the line 3 shift leader (morning shift), a maintenance technician, Jonas Peeters |

## 1. Purpose

Choose the camera position on line 3, the pilot line, and check power, network and mounting options for the industrial PC. Action item 2 from the kickoff of 2025-03-10.

## 2. Walk

We walked line 3 from the freezer exit to packaging between 07:45 and 09:30.

**Freezer exit.** Product leaves the tunnel freezer at around −18 °C. There is visible fog for about two metres after the exit, and frost forms on every cold surface. Dries' concern from the kickoff is justified: a camera here would see fog for most of the shift. Rejected.

**Vibrating transfer belt, about six metres after the exit.** The fog is gone, product is spread in a thin layer, belt speed is constant per product. This is also the last point before product goes into the packaging hoppers, so foreign material found here can still be removed. **Chosen as inspection point.**

**Packaging outfeed.** Closed packs pass on the outfeed conveyor. Packaging damage is easier to see here, but adding a second camera is outside the budget. Dries agreed that packaging damage in version 1 will be detected from the open bag mouths and torn film visible on the transfer belt side of the packaging machine, and we will check results during the pilot.

## 3. Chosen position: technical notes

- Camera on a stainless gantry above the transfer belt, about 80 cm above the product, looking straight down.
- Field of view: full belt width (60 cm).
- Belt speed varies by product between 0.3 and 0.6 m/s. With the planned camera and exposure time this gives sharp images at all speeds. Amira will confirm with test captures.
- Industrial PC in the existing electrical cabinet of line 3, about 12 metres away. Power available. The cabinet already holds the sensor gateway of line 3, so the network port sits in the same OT segment.
- Cleaning: the area is washed down every night. The camera housing and PC cabinet need at least IP65, preferably IP69K for the camera.

## 4. Lighting

The hall has skylights above line 3 and LED strip lighting along the frame. During our visit (morning, overcast) the light on the belt looked even. We used the line's own lighting for the first test pictures. *Note: we have not checked the light at other times of the day.*

## 5. Network

Tine Desmet confirmed by mail on 2025-03-14 that the network request for the edge devices on lines 3, 5 and 6 has been submitted. The devices will use the same outbound-only pattern as the sensor gateways. We do not expect a delay here.

## 6. Hardware to order

| Item | Quantity | Note |
|---|---|---|
| Industrial camera, IP69K housing | 3 | one per line |
| Industrial PC with GPU, fanless | 3 | runs Azure IoT Edge and the model |
| Stainless gantry | 3 | made by Verhaeghe's maintenance workshop |
| Spare camera | 1 | |

Order placed by Jonas on 2025-03-20. Delivery expected in week 15.

## 7. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Gantry for line 3 | Maintenance workshop | 2025-04-04 |
| 2 | Test captures at three belt speeds | AEI | after camera delivery |
| 3 | Line walk on lines 5 and 6 | JP / DC | May 2025 |
| 4 | Edge device setup and first module deployment | JP | 2025-04-18 |
