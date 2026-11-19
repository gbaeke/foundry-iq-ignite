# Kickoff Notes: Discharge Letter Summarisation

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Discharge Letter Summarisation |
| **Document type** | Meeting notes (kickoff) |
| **Date** | 2024-03-18, 09:30 to 11:30 |
| **Location** | Mediva, campus admin building, meeting room "Leie" |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |

## Attendees

- Dr. Hilde Van Damme, Chief Medical Information Officer, Mediva (HVD), sponsor
- Jeroen Lambrecht, IT Manager, Mediva (JL)
- Sarah Mertens, Data Protection Officer, Mediva (SM), first hour
- Pieter De Smet, Lead AI Architect, Kestrel (PDS)
- Amira El Idrissi, ML Engineer, Kestrel (AE)
- Thomas Maes, Project Manager, Kestrel (TM)

## 1. Opening

Hilde opened by thanking Sarah and the privacy committee for closing the DPIA. The start moved six weeks, from 2024-02-05 to today, and she prefers that to starting without a clear framework. She repeated the principle that the physician always reviews and signs: the system writes a draft, never the letter.

## 2. Re-planned milestones

All phases shift by six weeks. The fixed price of EUR 120,000 is unchanged.

| Phase | Period |
|---|---|
| Foundation | 2024-03-18 to 2024-04-12 |
| Prototype | 2024-04-15 to 2024-06-07 |
| Clinical evaluation | 2024-06-10 to 2024-08-30 |
| Pilot in daily practice and handover | 2024-09-02 to 2024-10-25 |

Thomas pointed out that the evaluation now falls in the summer holidays. Hilde accepted the risk but asked to recruit physicians early and to plan the baseline period before the main holiday weeks.

## 3. Pilot departments

Two departments were proposed and agreed: **internal medicine** and **geriatrics**. Both write many letters with long stays and many medication changes, which is where most time is lost. Hilde will ask the heads of department to nominate physicians for the evaluation group, mixing assistants and staff members.

## 4. DPIA conditions

Sarah walked through the binding conditions: pseudonymisation before any model call, EU-only processing and storage, pseudonymised logging with 90 days retention, and named access to the development dataset. Pieter confirmed that the architecture document has been updated with these conditions today. Sarah asked to be informed of any change to the data flow before it is implemented, not after.

## 5. Technical approach

Pieter presented the target architecture: record sections are read from a read-only extract provided by Mediva IT, pseudonymised inside Mediva's environment, sent to an Azure OpenAI deployment in an EU region, and the draft is re-identified inside Mediva's environment before it is shown to the physician. Amira explained the pseudonymisation test she is running on 200 sample letters.

Jeroen confirmed the test environment and the read access are ready. The weekly working session with his team is set on Thursday mornings.

## 6. Governance

- Steering committee: monthly, chaired by Hilde. First meeting in mid-May at the end of the first prototype sprints.
- Status report: biweekly, by Thomas, to Hilde, Jeroen and Sarah.
- Working session with Mediva IT: weekly, Thursday 9:00.
- Privacy check-ins with Sarah: monthly, first on 2024-04-08.

## 7. Invoicing

As in the proposal: 30% at start, 30% after prototype acceptance, 40% at handover. The first invoice (30%) will be sent this week.

## Decisions

- D1: Re-planned end date 2024-10-25.
- D2: Pilot departments internal medicine and geriatrics.
- D3: Any change to the data flow is submitted to Sarah before implementation.

## Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Nominate physicians for the evaluation group | HVD | 2024-04-19 |
| 2 | Provide 20 recent example letters per department, through the pseudonymised flow, for template work | HVD | 2024-04-05 |
| 3 | Pseudonymisation residual rate report | AE | 2024-04-05 |
| 4 | Detailed plan and RAID log | TM | 2024-03-22 |
| 5 | ADR on model deployment and region | PDS | 2024-03-22 |
