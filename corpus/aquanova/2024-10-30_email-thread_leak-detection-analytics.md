# Email Thread: Access Request for SCADA History

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Leak Detection Analytics |
| **Date** | 2024-10-30 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Email thread (exported) |

---

**From:** Koen Martens
**To:** Sofie Claes
**Cc:** Evelien Claes, Bram Visser
**Date:** 2024-10-28 09:14
**Subject:** Access request submitted to OT security

Hi Sofie,

I submitted the request to OT security this morning, with Bram's mapping note and the full tag list attached.

As expected, the idea of a direct connection from Azure to the historian is off the table. OT security does not allow any connection from outside into the OT network, read-only or not. The only possible path is through the OT DMZ, and every new data flow out of the DMZ needs approval from the OT security process. They meet every two weeks and usually ask questions in the first round.

I asked for a nightly export of the tags in the list to a server in the DMZ, from where your side can pick it up. Realistically, count on several weeks.

Koen

---

**From:** Sofie Claes
**To:** Koen Martens
**Cc:** Evelien Claes, Bram Visser, Amira El Idrissi
**Date:** 2024-10-28 13:40
**Subject:** RE: Access request submitted to OT security

Thanks Koen, that's clear.

A nightly export is fine for us in principle; night flow is the main signal and it is a once-a-day thing anyway. We would lose near real time, which was a nice-to-have.

Two questions you may get from OT security, so we can prepare:

1. *What exactly leaves the OT network?* Only the values of the agreed tags, as files. No commands, no credentials.
2. *Who picks it up on the other side?* A scheduled pipeline in AquaNova's own Microsoft Fabric workspace, with a service account managed by AquaNova IT. No Kestrel or DataForge account touches the DMZ.

Meanwhile we keep working on your sample export. Could you check whether a second manual export with three months of one DMA is possible? That would let Amira test the night-flow features on more than two weeks.

Sofie

---

**From:** Koen Martens
**To:** Sofie Claes
**Cc:** Evelien Claes, Bram Visser, Amira El Idrissi
**Date:** 2024-10-29 17:05
**Subject:** RE: Access request submitted to OT security

Good answers, I added them to the request.

Manual export of three months for one DMA: yes, but I have to do it by hand from the historian client, and every manual export also needs to be logged. I'll do one for DMA NO-2 this week. After that I'd rather wait for the approved flow than keep doing this.

Also, I'll use the waiting time to clean up the tag list. There are tags in there for equipment that no longer exists. Less to approve, less to export.

Koen

---

**From:** Evelien Claes
**To:** Koen Martens, Sofie Claes
**Cc:** Bram Visser, Amira El Idrissi, Filip Wuyts
**Date:** 2024-10-30 08:30
**Subject:** RE: Access request submitted to OT security

Thanks both. I'm copying Filip, because if this takes "several weeks" it touches the model phase in January.

On my side the GIS team keeps correcting the network model in Noord-Oost in the meantime, so that part will be ready when the data arrives.

Evelien
