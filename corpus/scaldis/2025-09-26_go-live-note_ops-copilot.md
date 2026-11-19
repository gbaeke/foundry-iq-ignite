# Go-live Note: Scaldis Ops Copilot

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Scaldis Ops Copilot |
| **Date** | 2025-09-26 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Go-live note |

Hi all,

Short note to confirm that the Ops Copilot is **live since Monday 2025-09-22**. That is one week after the re-planned date of 2025-09-15. The extra week went to the final security re-test: Wim Goossens wanted one more round on the restricted customs folders after a SharePoint group was renamed on the Scaldis side. Fair call, and the result is a clean sign-off with no open high or medium findings.

## What went live

- Teams bot available to all terminal operations staff across shifts, in Dutch, French and English
- About 2,100 SOPs and work instructions indexed, with document-level permission trimming: you only get answers from documents you can open in SharePoint
- Feedback buttons and a weekly quality report for Nathalie Dumont's team

## First days

The rollout wave for the first month covers **340 users**, all of whom have access since Monday. In the first four days about 1,150 questions were asked. Most popular topics: reefer plug-in procedures, gate exception handling and the new checklist for lashing inspections. Median answer time is 4.2 seconds, a bit slower than in the pilot because of the security filters but within what Nathalie considers acceptable.

Two small issues:
- Some old French SOP versions still appear in answers; Nathalie's team is archiving them.
- One shift leader reported that the bot does not show up in Teams on a shared terminal PC. Ruben is looking into the app policy.

## Lessons learned

The main one, and I will bring this to the next internal session as well: **plan the security review in the first sprint**. On this project the review was scheduled just before go-live, while restricted content entered scope midway. Had Wim reviewed the architecture in sprint 1, we would have designed for permission trimming from day one and avoided most of the slip. For every project that puts an LLM on top of company documents, the security officer should see the design before we index anything.

Other points:
- Pairing Ruben with Elien on the Teams front end worked well.
- Keeping the pilot group running through the summer kept the momentum while we reworked the index.

## Next steps

- Hypercare until 2025-10-17, daily check of feedback (PDS, RW)
- Handover of the content-governance routine to Nathalie's team
- Final project report and budget reconciliation by Thomas in October

Thanks to Koen, Nathalie, Wim and the whole team for getting this over the line.

Pieter
