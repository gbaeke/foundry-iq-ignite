# Email Thread: Gate-in Correction Rules

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Container Dwell-Time Forecasting |
| **Date** | 2023-11-17 |
| **Author** | Sofie Claes, Senior Data Engineer, Kestrel Consulting |
| **Document type** | Email thread (exported) |

---

**From:** Sofie Claes
**To:** TOS administration (Scaldis IT shared mailbox)
**Cc:** Nathalie Dumont; Thomas Maes
**Date:** Tuesday 14 November 2023, 16:42
**Subject:** Gate-in correction rules: proposal for review

Hello,

Thanks again for the session on Monday. As discussed, here is the proposal for the gate-in corrections in the curated layer. Figures are over the full training window (2021-06 to 2023-08).

1. **Duplicates.** About 6% of gate-in events are duplicates: same container number, same visit, same gate, timestamps within 120 seconds. Almost all come from lanes 4 and 5, where the camera and the clerk both register. Rule GI-01: keep the earliest record, prefer source code CAM over CLK when timestamps are equal, mark the other as duplicate.
2. **Missing gate-in.** For about 2% of visits there is no gate-in at all, only a first yard move. Rule GI-02: reconstruct the gate-in from the truck appointment slot start if the first yard move falls within 90 minutes after it; otherwise use the first yard move minus the median gate-to-stack time for that block (currently 14 minutes).
3. Reconstructed records get a flag, so the model and the planners can see them.

Could you confirm whether lanes 4 and 5 are the only lanes with double registration, and whether gate outages are logged somewhere? That would let us explain most of the missing cases.

Kind regards,
Sofie

---

**From:** TOS administration (Scaldis IT)
**To:** Sofie Claes
**Cc:** Nathalie Dumont; Thomas Maes
**Date:** Wednesday 15 November 2023, 11:05
**Subject:** RE: Gate-in correction rules: proposal for review

Hi Sofie,

Lanes 4 and 5 are the two lanes where the OCR portal was installed last year while the clerk workflow was not changed. Lane 2 had the same set-up for a few weeks in spring 2022, so you may find some duplicates there too.

Gate outages: there is no formal log, but the gate supervisor keeps an outage list in the shift report. I can send you the 2023 lists; older ones are on paper.

We cannot switch off clerk registration on lanes 4 and 5 before the TOS update next year. The vendor's change process takes too long for that and the update itself will change the gate module anyway.

Regards,
TOS administration, Scaldis IT

---

**From:** Nathalie Dumont
**To:** Sofie Claes; TOS administration (Scaldis IT)
**Cc:** Thomas Maes
**Date:** Thursday 16 November 2023, 08:17
**Subject:** RE: Gate-in correction rules: proposal for review

Sofie,

Business view: GI-01 is fine. For GI-02 the planners agree with the appointment rule. The 14 minutes gate-to-stack is realistic for the import blocks, but for the reefer rows it is closer to 25 minutes because of plug-in. Can the median be per block type rather than one number?

Also please keep the flagged records visible in the output. If the planners see a forecast based on a reconstructed gate-in, they want to know.

Nathalie

---

**From:** Sofie Claes
**To:** Nathalie Dumont; TOS administration (Scaldis IT)
**Cc:** Thomas Maes; Bram Visser
**Date:** Friday 17 November 2023, 10:30
**Subject:** RE: Gate-in correction rules: proposal for review

Thanks both.

- GI-02 will use the median gate-to-stack time per block type (import, reefer, empty, dangerous goods), recalculated monthly.
- Lane 2 spring 2022 is included in the duplicate check.
- The flag `gate_in_reconstructed` is passed through to the output table.
- I will add the 2023 outage lists as a validation set to check how many missing gate-ins they explain.

Both rules go into data contract v0.3 and into the curated job next week. Bram can then switch on the truck features. If all goes well we reach the feature pipeline milestone on the 24th.

Have a good weekend,
Sofie
