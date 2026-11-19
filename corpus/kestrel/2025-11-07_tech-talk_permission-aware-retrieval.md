# Tech Talk: Permission-Aware Retrieval

| | |
|---|---|
| **Organisation** | Kestrel Consulting (internal) |
| **Date** | 2025-11-07, 16:00 to 17:00 |
| **Location** | Kestrel office Ghent and Teams |
| **Author / presenter** | Pieter De Smet, Lead AI Architect |
| **Document type** | Internal tech talk notes |

## Why this talk

A retrieval system that ignores permissions is a data leak with a nice chat interface. I learned that the expensive way on the **Scaldis Ops Copilot**, which went live on **2025-09-22**. This talk explains what went wrong, how we fixed it, and how we design for it from now on. It complements the June lessons-learned session, which covered the project management side.

## The case in short

- The copilot answers questions from terminal staff in Microsoft Teams, based on SOPs and work instructions stored in SharePoint. Retrieval runs on Azure AI Search; answers are generated with Azure OpenAI.
- Halfway through the project, restricted procedures (customs, security, some incident procedures) came into scope.
- The customer's IT Security Officer, Wim Goossens, did his formal review in spring, when the pilot was already running. His finding: the index did not respect **document-level permissions**. A user could get an answer based on a procedure they were not allowed to open in SharePoint.
- Go-live was re-planned to 2025-09-15. After a final re-test following a renamed SharePoint group, we went live a week later, on 2025-09-22, with a clean sign-off.
- In the first month **340 users** used the copilot.

Wim was right. The lesson is not "security reviews slow you down" but "security shapes the architecture, so it belongs in sprint 1".

## How permission trimming works

1. **Index the permissions with the content.** For every document chunk, store the identifiers of the groups and users allowed to read the source document.
2. **Resolve the user at query time.** The bot knows who is asking. We resolve that user's group memberships and pass them as a filter on the search query.
3. **Filter before ranking.** The search only considers chunks the user can read. Never retrieve everything and filter afterwards in application code; ranking, snippets and logs would already have seen restricted content.
4. **Keep permissions fresh.** Permissions change more often than content. We sync access lists on a schedule separate from content updates, and we re-test after every change in the customer's group structure.
5. **Fail closed.** If the permission lookup fails, the user gets no answer, not an unfiltered one.

## Costs of doing it late

- Re-indexing the full SOP library with permission metadata.
- Rewriting the query layer and the logging, because logs had to stop containing restricted snippets.
- A slightly slower median response, because of the extra filter and group resolution. Still acceptable for the users.
- Most of all, about two and a half months of calendar time.

## The checklist we now use

For every project that indexes company documents:
- [ ] Security officer reviews the architecture in sprint 1
- [ ] Inventory of restricted content, including content "not in scope yet"
- [ ] Permission model of the source system documented (groups, inheritance, exceptions)
- [ ] Permission filter tested with at least three test users with different rights
- [ ] Re-test procedure when the customer changes groups
- [ ] Logs and traces checked for leakage of restricted content

## Discussion

- *Does this also apply to agents that call tools?* Yes, even more. A tool should act with the user's rights, not with a technical account that sees everything.
- *What if the customer's permissions are a mess?* They usually are. That is a finding to raise early, not a reason to skip trimming.
- *Content governance?* Separate problem, same lesson: old document versions in the library also produced odd answers in the first days after go-live. Nathalie's team is archiving them.

Slides on the internal SharePoint. The checklist goes into the project template next week.

Pieter
