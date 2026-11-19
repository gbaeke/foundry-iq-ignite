# Status Report: Scaldis Ops Copilot

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Scaldis Ops Copilot |
| **Date** | 2025-03-14 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Document type** | Status report |
| **Reporting period** | 2025-02-17 to 2025-03-14 |
| **Distribution** | Koen Verstraete, Nathalie Dumont, Wim Goossens, Lotte Willems |

## 1. Overall status

| Dimension | Status | Comment |
|---|---|---|
| Overall | **Green** | Pilot start on plan |
| Scope | Amber | CR-01 (restricted libraries) submitted for the steering committee |
| Schedule | Green | Go-live 2025-07-01 confirmed |
| Budget (T&M) | Green | 27% of EUR 150,000 estimate consumed |
| Quality | Green | Regression set in place |

## 2. Progress this period

- **Indexing.** All general operations libraries are indexed: about 1,800 documents in Azure AI Search, refreshed nightly. 37 scanned PDFs without text layer reported to the content owners.
- **Answer quality.** A regression set of 120 questions, written by Nathalie's team in three languages, runs after every change to the index or the prompt. Current score: 94 of 120 correct and complete, 15 correct but incomplete, 5 "not found" while the answer exists, 6 wrong.
- **Teams bot.** Ruben Wouters delivered the answer cards from Elien Jacobs' design, including the collapsed steps and the "Ask the shift leader" button. Language detection works on short questions from four words on; shorter ones default to the user's Teams language.
- **User tests.** Elien tested three card variants with four shift leaders. Winner: answer plus version date plus source link, passage text hidden behind "show source".
- **Content clean-up.** Content owners have been appointed for all sites. The first list of 64 suspected duplicates and outdated versions went to them on 2025-03-07; 22 already archived.

## 3. Pilot preparation

- Nathalie nominated 25 pilot users across the four shifts: shift leaders, planners, gate clerks and two operators who only use shared gate PCs.
- Pilot starts on 2025-03-24 for four weeks minimum, then continues until go-live.
- The bot is published for the pilot group only, through a Teams app permission policy prepared with Scaldis IT.

## 4. Risks and issues

| ID | Type | Description | Owner | Status |
|---|---|---|---|---|
| R-08 | Risk | Outdated SOP versions produce wrong answers | ND | Open, monthly clean-up |
| R-09 | Risk | Shared gate PCs: users not logged in personally in Teams | ND | Open, check during pilot |
| R-10 | Risk | Cost per question unknown until pilot usage | PDS | Open |
| R-11 | Risk | Low engagement of night shift in pilot | EJ | Open |

## 5. Change request

CR-01 adds three restricted libraries (incident handling, customs procedures, access control; about 300 documents). The proposal is a separate index filtered by group membership, with no restricted content in production before the security review. No change to the estimate. Decision at the steering committee of 2025-03-20.

## 6. Next steps

- Pilot kick-off session with the 25 users on 2025-03-24 (EJ, RW)
- Weekly feedback review with Nathalie during the pilot (EJ)
- Indexing of restricted libraries into a separate index, after CR-01 approval (PDS)
- Inventory of SharePoint groups on the restricted sites (PDS, with site owners)
- First cost per question figure after two weeks of pilot (PDS)

## 7. Milestones

| Milestone | Date | Status |
|---|---|---|
| Indexing pipeline on all general libraries | 2025-03-14 | Done |
| Pilot start | 2025-03-24 | On track |
| Security review | June 2025 | Planned |
| Go-live | 2025-07-01 | On track |

Thomas Maes
