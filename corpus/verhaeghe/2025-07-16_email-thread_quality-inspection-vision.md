# Email Thread: False Flags on Line 3 in the Afternoon

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Quality Inspection Vision |
| **Date** | 2025-07-16 |
| **Author** | Amira El Idrissi, ML Engineer and project lead, Kestrel Consulting |
| **Document type** | Email thread (exported) |

---

**From:** Dries Callens
**To:** Amira El Idrissi
**Cc:** Jonas Peeters
**Date:** 2025-07-14 17:52
**Subject:** Line 3 – too many flags after lunch

Hi Amira,

The pilot started well last Monday, but the afternoon shift complains. Between about 13:00 and 17:00 the screen flags discolouration all the time, on product that looks perfectly fine. Today the shift leader stopped looking at the screen after 15:00. In the morning and at night it is much better.

Can you have a look before the operators lose faith in it?

Dries

---

**From:** Amira El Idrissi
**To:** Dries Callens
**Cc:** Jonas Peeters, Ruben Wouters
**Date:** 2025-07-15 16:20
**Subject:** RE: Line 3 – too many flags after lunch

Hi Dries,

Thanks, this is very useful. I went through all flags of the first week per hour:

- 06:00 to 12:00: about 6% false flags
- 13:00 to 17:00: between 15% and **more than 20%** false flags, on sunny days the worst
- night: about 4%

Almost all afternoon false flags are discolouration. Ruben pulled the flagged images: in the afternoon there is direct sunlight from the skylights on part of the belt, and bright reflections from the stainless frame next to the belt. Healthy green beans in the bright patches look pale and the edges of the reflections look like grey spots. The model has hardly seen such light, because most training images were taken in spring.

So it is not the model getting worse, it is the light changing during the day. We did our line walk on an overcast morning and missed this.

Amira

---

**From:** Jonas Peeters
**To:** Amira El Idrissi, Dries Callens
**Cc:** Ruben Wouters
**Date:** 2025-07-16 08:45
**Subject:** RE: Line 3 – too many flags after lunch

Morning both,

I would not try to solve this in the model. Retraining on more sunny images helps a bit, but the light will change with every season. Proposal:

- A **camera enclosure** over the inspection point: a closed hood over the belt section, with its own LED lighting and a matte inner finish, so neither skylights nor the frame can reflect into the image.
- Openings at both ends just high enough for the product layer, a hinged side panel for cleaning.
- The same design for lines 5 and 6, built in before they go live.

Dries, your maintenance workshop could build it from my drawing, but the supplier of the stainless sheet and the LED bars closes for the bouwverlof from next Monday, 21 July, for three weeks. If we order this week, we get the material in the week of 11 August and can install on line 3 around 18 August.

Jonas

---

**From:** Dries Callens
**To:** Jonas Peeters, Amira El Idrissi
**Cc:** Ruben Wouters, Tine Desmet
**Date:** 2025-07-16 11:02
**Subject:** RE: Line 3 – too many flags after lunch

Agreed, go ahead with the enclosure. I'll sign the order for the material today.

Until then, let's show only foreign material flags on the screen between 12:00 and 18:00, so the afternoon shift keeps using it. Discolouration flags are still logged for you, Amira, but not shown.

I'll explain it to the shift leaders at Thursday's meeting.

Dries
