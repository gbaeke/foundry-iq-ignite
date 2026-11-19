# Email Thread: Duplicate Asset IDs Found in Tool Testing

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Asset Management Agent |
| **Date** | 2026-09-17 |
| **Author** | Ruben Wouters, Developer, Kestrel Consulting |
| **Document type** | Email thread (exported) |

---

**From:** Ruben Wouters
**To:** Pieter De Smet
**Cc:** Jonas Peeters
**Date:** 2026-09-15 16:40
**Subject:** Wrong history returned for a valve – IDs exist in both systems

Hi Pieter,

During testing with the planners today, one of them asked for the history of a valve by its ID. The agent returned a clean answer, with a hydrant inspection from 2019 in it. She spotted it immediately.

Cause: the same asset ID exists in System A and System B, for two different assets. The register view returns both rows; my tool took the first one.

I ran the overlap check from the profiling note (F-5) on a sample of 5,000 assets from the register view: **312 IDs** appear in both systems and refer to different assets. Mostly valves and hydrants, created in the years when both systems were in use.

For now I have changed the tools: if an ID matches more than one record, the agent does not answer but asks the planner to confirm the location or the asset type. That prevents wrong answers, but adds a step for the planner.

Ruben

---

**From:** Pieter De Smet
**To:** Kevin Hermans
**Cc:** Ruben Wouters, Jonas Peeters, Filip Wuyts
**Date:** 2026-09-16 08:55
**Subject:** FW: Wrong history returned for a valve – IDs exist in both systems

Kevin,

See Ruben's mail below. This is the risk we noted in February, now confirmed: 312 duplicated IDs in a sample of 5,000. Extrapolated to the full register it could be several thousand.

Ruben's check stops wrong answers, which is what matters most for the planners' trust. But the structural fix is in the register, not in the agent. Can we discuss options this week? I'll log it as I-07 in the September report.

Pieter

---

**From:** Kevin Hermans
**To:** Pieter De Smet
**Cc:** Ruben Wouters, Jonas Peeters, Filip Wuyts
**Date:** 2026-09-16 14:20
**Subject:** RE: Wrong history returned for a valve – IDs exist in both systems

Pieter, Ruben,

Thanks for catching this before the tools went to the whole pilot group. I'm not surprised; the migration between the two systems ran for years without a clear cut-off.

My proposal:

1. **Short term:** a composite key, source system plus ID, in the register view and in the tools. Planners usually know whether they are asking about a station asset or a network asset, and the agent can ask if not.
2. **Structural:** a clean-up by the asset data team, assigning new unique IDs where needed and updating references in the maintenance history. That's a real project; Q1 2027 at the earliest.

Filip, I'd like a decision on both at the steering meeting in October. The clean-up needs people from your asset data team.

Kevin

---

**From:** Filip Wuyts
**To:** Kevin Hermans, Pieter De Smet
**Cc:** Ruben Wouters, Jonas Peeters
**Date:** 2026-09-17 09:10
**Subject:** RE: Wrong history returned for a valve – IDs exist in both systems

Agreed to put both on the agenda for 23 October. I need to check capacity in the asset data team before I can commit to the clean-up.

Ruben, please keep the confirmation step until then. A planner answering one extra question is better than a crew sent to the wrong valve.

Filip
