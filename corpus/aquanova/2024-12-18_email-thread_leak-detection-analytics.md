# Email Thread: Approval and Data Diode Export Over the Holidays

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Leak Detection Analytics |
| **Date** | 2024-12-18 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Email thread (exported) |

---

**From:** Koen Martens
**To:** Sofie Claes, Evelien Claes
**Cc:** Filip Wuyts, Bram Visser
**Date:** 2024-12-16 15:22
**Subject:** OT security: approved

Hi all,

OT security signed off on the data flow today. Seven weeks after I submitted it, but it's there.

The condition is that the export goes through a **data diode**: a one-way link from the historian side to a file drop in the DMZ. Data can only flow out of the OT network, never back in. There is no network path from the DMZ to the historian at all. We already have a diode for another reporting flow, so I can reuse that hardware with a new channel.

How it will work:

1. Every night at 01:30 the historian exports the agreed tags for the previous day to a file.
2. The file goes through the diode to the file drop in the DMZ.
3. From there your pickup in Fabric collects it, as described in the request.

I also want to clean up the tag list before I configure the export. About 60 of the 243 tags are for equipment that no longer exists or was never used. Any objection?

Koen

---

**From:** Sofie Claes
**To:** Koen Martens, Evelien Claes
**Cc:** Filip Wuyts, Bram Visser, Amira El Idrissi
**Date:** 2024-12-16 17:05
**Subject:** RE: OT security: approved

Koen, great news, thank you for pushing this through.

No objection to the clean-up. Bram's mapping only needs 78 tags; please check that those all remain. Bram will send you the list tomorrow.

One more question: can the first export include history? We need at least 18 months for the model.

Sofie

---

**From:** Koen Martens
**To:** Sofie Claes
**Cc:** Evelien Claes, Filip Wuyts, Bram Visser, Amira El Idrissi
**Date:** 2024-12-17 08:50
**Subject:** RE: OT security: approved

History: yes, I can push a one-time backfill of 18 months through the same channel, in monthly files, before the nightly export starts.

Timing is the problem. The OT change window closes for the Christmas period from 2024-12-20 until 2025-01-06. I can do the configuration on the diode channel before the 20th. The backfill and the first nightly run I will do in the first week of January; I'm on standby duty between Christmas and New Year anyway and can test quietly in between. Count on data in your lakehouse around **2025-01-13**.

Koen

---

**From:** Bram Visser
**To:** Koen Martens, Sofie Claes
**Cc:** Amira El Idrissi
**Date:** 2024-12-18 10:15
**Subject:** RE: OT security: approved

Koen, list of the 78 tags attached, all are in your cleaned-up list. Thanks.

On our side:

- The pickup pipeline in Fabric is ready and tested with dummy files in the agreed format.
- I will add a check for a missing or incomplete nightly file, so nobody has to find out from a gap in the report. Target end of January.
- The Databricks feature jobs run on the backfill as soon as it lands.

Sofie, I'm off from 2024-12-23 to 2025-01-03, like you. Back for the first files.

Bram

---

**From:** Sofie Claes
**To:** Koen Martens, Bram Visser
**Cc:** Evelien Claes, Filip Wuyts, Amira El Idrissi
**Date:** 2024-12-18 11:00
**Subject:** RE: OT security: approved

Thanks all. Summary for Filip:

- Approved 2024-12-16, via a data diode export to the DMZ. Daily data, not near real time.
- Backfill of 18 months and first nightly export in the first week of January; data in the lakehouse around 2025-01-13.
- Model phase starts about four weeks later than planned. I'll bring an updated planning to the steering meeting.

Merry Christmas, and thank you Koen for doing this over the holidays.

Sofie
