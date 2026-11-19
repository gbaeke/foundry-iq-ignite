# Status Report: Clinical Knowledge Assistant

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Clinical Knowledge Assistant |
| **Document type** | Status report (monthly) |
| **Date** | 2026-09-18 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Period** | 2026-08-17 to 2026-09-18 |
| **Project status** | Ongoing (pilot) |

## 1. Overall status

| Area | Status | Comment |
|---|---|---|
| Overall | Amber | Pilot running; answer consistency issue under control but not closed |
| Scope | Green | Pilot scope unchanged |
| Planning | Amber | Phase 1 review moved by about three weeks |
| Budget | Green | Within T&M cap of first phase |
| Quality | Amber | Conflicting answers traced to source content, see section 3 |

## 2. Progress this period

- The pilot is running in the **cardiology** and **emergency** departments. About 60 active users in the last four weeks, with most questions coming from the emergency department during night shifts.
- The evaluation set now contains **200 questions**, written and reviewed with clinicians from both pilot departments. Each question has a reference answer and the expected source document. We run the full set after every change to the knowledge base or prompts.
- Latest run: 81% of answers rated correct and complete, 11% partially correct, 8% incorrect or wrong source. The "incorrect" group is dominated by the issue below.
- Ruben Wouters (developer) released the new feedback form in the front end; clinicians can now flag "outdated source" directly on an answer.
- Amira El Idrissi (lead AI engineer) tuned the retrieval instructions so the assistant states the guideline version and publication date in every answer.

## 3. Main issue: outdated guideline versions

In August we saw the assistant give **conflicting answers** to essentially the same question, for example on the dosing table in a cardiology protocol. Investigation showed that the source library contains multiple versions of the same clinical guideline: the current one and one or more outdated versions that were never archived. The retrieval layer correctly found both, and depending on the wording of the question, the outdated version ranked higher.

This is a **content governance** problem rather than a model problem. Technical mitigations (prefer the most recent version, show the date) help, but cannot decide which version is valid. That decision belongs to the clinical content owners.

Actions agreed with the sponsor, Dr. Hilde Van Damme, Chief Medical Information Officer:

1. Hilde's team (the CMIO office and the department guideline coordinators) runs a clean-up of the cardiology and emergency guideline folders, marking each document as current, superseded or archive.
2. Only documents marked "current" are indexed in the knowledge base; superseded ones move to a separate, non-indexed library.
3. A monthly content review is set up between Hilde's team and the guideline owners, with a report from Kestrel listing documents that the assistant retrieved but were flagged as outdated by users.

The cardiology clean-up is about 70% done. Emergency starts next week.

## 4. Risks and issues

| # | Type | Description | Owner | Mitigation |
|---|---|---|---|---|
| R1 | Issue | Outdated guideline versions cause conflicting answers | HVD | Content clean-up and "current only" indexing |
| R2 | Risk | Clean-up does not scale to other departments without dedicated content owners | HVD | Make content ownership a condition for Phase 2 departments |
| R3 | Risk | Users trust answers without opening the source | AE | Version and date in every answer; source link mandatory |
| R4 | Risk | Night shift usage spikes on emergency department | RW | Load test before extending pilot |

## 5. Next steps

| Action | Owner | Due |
|---|---|---|
| Finish cardiology guideline clean-up | HVD | 2026-10-02 |
| Re-index cardiology with "current only" filter, rerun 200-question set | AE | 2026-10-07 |
| Start emergency department clean-up | HVD | 2026-09-28 |
| Outdated-source report for monthly content review | PDS | 2026-10-14 |
| Load test front end and retrieval | RW | 2026-10-09 |
| Prepare Phase 1 review for steering committee | PDS | 2026-11-04 |

*Pieter De Smet, Kestrel Consulting*
