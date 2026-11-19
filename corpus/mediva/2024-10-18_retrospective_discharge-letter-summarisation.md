# Retrospective: Discharge Letter Summarisation

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Discharge Letter Summarisation |
| **Document type** | Retrospective (internal) |
| **Date** | 2024-10-18 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Participants** | Pieter De Smet, Amira El Idrissi, Thomas Maes |

## 1. Format

A 90-minute internal retrospective at the Kestrel office in Ghent, one week before the formal closing on 2024-10-25. We used the "keep / stop / try" format and looked at the whole project, from the proposal in January to the pilot. Lotte joined the last 15 minutes for the commercial part.

## 2. Timeline as we remembered it

- January: proposal, planned start 2024-02-05
- February to mid-March: waiting for the DPIA; team partly on other work
- 2024-03-18: start, six weeks late
- April: pseudonymisation test, residual direct identifiers to zero
- May: two-step drafting, first steering committee
- June: prototype accepted, evaluation starts
- July and August: evaluation, extended by two weeks for summer leave
- September: pilot in daily practice, consumption discussion
- October: handover

## 3. Keep

- **Source next to the draft.** The review screen with highlighted sources did more for trust than any accuracy figure. Physicians said so in the workshop, in the sprint review and in the evaluation.
- **Deterministic where possible.** Computing the medication comparison in code and letting the model only phrase reasons avoided a whole category of errors.
- **Measuring time with a baseline.** The 9 minutes per letter is credible because it compares the same physicians before and after, not a survey.
- **Close contact with the DPO.** Monthly check-ins with Sarah meant no surprise discussions late in the project. Every data flow question went to her before implementation.
- **The Thursday session with Mediva IT.** Small issues (timer, log rule, content filter) were handled in a week instead of escalating.

## 4. Stop

- **Starting the privacy assessment after signing.** We lost six weeks and had the team waiting. The DPIA should run in parallel with the proposal phase.
- **Optimistic cost estimates without user behaviour.** Our estimate per letter was based on one draft per letter; in practice physicians regenerated. Next time, include a behaviour factor.
- **Planning an evaluation in July without explicit leave data.** We recovered with the two-week extension, but we should have asked the secretariats for the leave planning at kickoff.

## 5. Try

- A **regression set** of historical cases from the first sprint, not from the evaluation. We built ours late.
- **Paragraph-level actions** in the user interface from the start (regenerate, shorten, remove).
- Ask the sponsor at kickoff who owns the **content** (templates, instructions) after handover. We only settled this in the last weeks.
- Keep a list of **out-of-scope requests** from users. The most common one, "can I ask it what our protocol says?", is a real opportunity.

## 6. Commercial (with Lotte)

- Delivered within the fixed price of EUR 120,000; no change requests. The paragraph-level regeneration was absorbed as a small change within scope.
- Third invoice (40%) after acceptance on 2024-10-25.
- The DPIA delay cost Kestrel idle time in February and March that a fixed price does not compensate. Lotte will include a clause in future healthcare proposals: start date conditional on DPIA completion, with a planning workshop in the meantime.
- Lotte will discuss the "protocol question" with Dr. Van Damme after closing, as a possible follow-up.

## 7. Actions

| # | Action | Owner |
|---|---|---|
| 1 | Recommendation for a follow-up assistant in the closing report | TM |
| 2 | Reusable pseudonymisation test procedure for the internal knowledge base | AE |
| 3 | DPIA clause in healthcare proposal template | Lotte |
| 4 | Short write-up "source next to text" pattern for other generative AI projects | PDS |
