# Handover Notes: Operations to Mediva IT

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Discharge Letter Summarisation |
| **Document type** | Handover notes |
| **Date** | 2024-10-11 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Receiving team** | Mediva IT, team of Jeroen Lambrecht |
| **Session** | 2024-10-10, 09:00 to 12:00, with two application engineers and the integration developer |

## 1. What is handed over

| Item | Location | Status |
|---|---|---|
| Mediva-side service (section selection, pseudonymisation, model calls, re-identification) | Mediva environment, source repository of Mediva IT | Handed over |
| Azure OpenAI deployment, EU region | Mediva subscription | Owned by Mediva since start |
| Templates and instructions (internal medicine v4, geriatrics v4) | Configuration folder of the service, versioned | Handed over |
| Review screen | Letter editor integration, maintained by Mediva IT | Handed over |
| Monitoring and alerts | Mediva monitoring, alerts to service desk | Handed over |
| Monthly consumption report | Report script and instructions | Handed over, first report sent by Kestrel on 2024-10-04 |
| Run book | Project documentation library | Version 1.0 |

## 2. Run book highlights

**Draft fails or times out.** The physician sees a message and writes the letter as usual. Service desk checks the alert. Most frequent cause in the pilot: the extract interface of the record was slow during the night batch, between 01:00 and 02:30. Physicians rarely write letters then; no action needed unless it shifts into the day.

**Content filter blocks a draft.** Happens rarely since the adjusted configuration. The physician writes the letter manually; no retry needed. If it happens more than a few times per week, check whether the filter configuration has been reset after a platform change.

**Changing a template or instruction.** Change in the configuration folder, run the regression set of 60 historical stays (script in the repository), compare the measures with the last run (draft length, unsupported statements, certainty underlining), and only then deploy. Template changes do not change the data flow; changes to which sections are read or what is sent to the model **do**, and must be submitted to Sarah Mertens first.

**Model version update.** Azure OpenAI model versions are retired on a published schedule. Before switching the deployment to a new version, run the same regression set and a short review with two physicians. We recommend Mediva IT checks the retirement dates every quarter.

**Pseudonymisation.** The key stays with Mediva IT. Repeat the residual identifier test on 200 letters once per year, or after any change to the pseudonymisation rules, and report the result to the DPO.

## 3. Pilot figures at handover (2024-09-09 to 2024-10-09)

| Measure | Value |
|---|---|
| Physicians using the draft at least once | 37 |
| Letters started with a draft | about 640 |
| Average draft time | 21 s |
| Regenerations per letter (after paragraph-level regeneration, 2024-10-03) | 1.2 |
| Potentially harmful errors reported | 0 |

## 4. Questions raised by Mediva IT

- *Can other departments be added?* Technically yes: a new template, a regression set and a physician review. Functionally it is a new rollout with its own training; not part of this project.
- *Who decides on template changes?* Proposal: Dr. Van Damme's office owns the content of the templates; Mediva IT owns the deployment. Agreed by Jeroen, to be confirmed by Dr. Van Damme.
- *What if a physician asks a question to the draft function, like "what is our protocol for..."?* It does not support that. The draft only uses the record of the stay. Several physicians asked this during the evaluation; Thomas will mention it in the closing report.

## 5. Open items until closing

| # | Item | Owner | Due |
|---|---|---|---|
| 1 | Switch off test deployment and test resources | JL | 2024-10-18 |
| 2 | Cost centre tags per department on resources | JL | 2024-10-18 |
| 3 | Confirm template content ownership | HVD | 2024-10-25 |
| 4 | Run book v1.0 review by Mediva IT, comments to Pieter | JL | 2024-10-17 |
| 5 | Remove Kestrel access after acceptance | JL | 2024-10-31 |

## 6. Support after closing

Kestrel provides best-effort support by mail for questions on the run book until the end of 2024. Pieter and Amira remain the contacts.
