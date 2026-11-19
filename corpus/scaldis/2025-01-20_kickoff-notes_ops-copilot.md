# Kick-off Meeting Notes: Scaldis Ops Copilot

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Scaldis Ops Copilot |
| **Date** | 2025-01-20, 09:30 to 12:00 |
| **Location** | Scaldis HQ Antwerp, meeting room "Kaai 3" |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Meeting notes |

## Attendees

**Scaldis Logistics**
- Koen Verstraete, CIO (sponsor)
- Nathalie Dumont, Head of Terminal Operations (product owner)
- Wim Goossens, IT Security Officer

**Kestrel Consulting**
- Pieter De Smet, Lead AI Architect
- Thomas Maes, Project Manager
- Elien Jacobs, UX and Frontend Developer
- Ruben Wouters, Junior Developer

## 1. Context and goals

Koen opened by referring to the earlier dwell-time forecasting work as a good basis of trust between both teams. The new problem is different: shift leaders and planners lose a lot of time searching standard operating procedures (SOPs), work instructions and incident checklists spread over several SharePoint sites. New staff in particular call the shift leader for things that are documented somewhere.

Nathalie described the goal as "one place to ask how we do things on the terminal", in Microsoft Teams, because that is where shift teams already communicate.

## 2. Proposed solution

Pieter presented the target architecture:
- SOPs and work instructions stay in **SharePoint**; no content migration.
- Content is indexed into **Azure AI Search** (hybrid keyword and vector search, chunked per section).
- **Azure OpenAI** generates answers grounded on retrieved passages, always with links to the source document.
- A **Microsoft Teams** bot is the user interface. Elien will design the conversation flow and answer cards; Ruben will develop the bot.
- Scope of the first release: SOPs of the operations department, about 1,800 documents in Dutch, French and English.

## 3. Discussion

- Nathalie asked for answers in the language of the question. Agreed as a requirement.
- Wim asked how access rights in SharePoint would be handled, since some procedures (security incidents, customs) are restricted. Pieter explained that the first sprints will work on the general operations library. Wim will do a formal security review before go-live and will share the Scaldis security checklist for AI applications.
- Koen asked about cost control. Thomas proposed a monthly burn report and Azure consumption alerts.
- Ruben joined Kestrel two weeks ago; Elien will pair with him during the first sprints.

## 4. Decisions

1. Target go-live: **2025-07-01**, for terminal operations staff on all shifts.
2. Contract basis: **time and materials, estimate EUR 150,000**, reported monthly against the estimate.
3. Two-week sprints, starting today. Sprint review every other Thursday with Nathalie and two shift leaders.
4. Pilot group of 25 users from sprint 6 onwards.

## 5. Planning (high level)

| Phase | Period |
|---|---|
| Sprints 1 to 3: indexing pipeline, first prototype | Jan to Mar 2025 |
| Sprints 4 to 7: Teams bot, pilot group | Mar to May 2025 |
| Security review and hardening | June 2025 |
| Go-live | 2025-07-01 |

## 6. Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Provide list of SharePoint sites in scope and site owners | ND | 2025-01-27 |
| 2 | Share security checklist for AI applications | WG | 2025-01-31 |
| 3 | Arrange Azure subscription and resource group for the project | KV | 2025-01-31 |
| 4 | Draft conversation design and answer card mock-ups | EJ | 2025-02-07 |
| 5 | Set up Teams bot skeleton and dev tenant app registration | RW | 2025-02-07 |
| 6 | Set up monthly burn report and consumption alerts | TM | 2025-02-14 |
| 7 | Indexing pipeline proof of concept on one SharePoint site | PDS | 2025-02-14 |
| 8 | Nominate 25 pilot users across shifts | ND | 2025-03-14 |

Next steering committee: 2025-02-20.

*Notes by Pieter De Smet*
