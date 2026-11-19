# ADR-03: Document-Level Permission Trimming at Query Time

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Scaldis Ops Copilot |
| **Date** | 2025-06-06 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Architecture decision record |
| **Status** | Accepted (reviewed by Wim Goossens, 2025-06-05) |
| **Supersedes** | Restricted-index approach described in CR-01 |
| **Related** | ADR-01 chunking strategy, ADR-02 answer language and citations, security finding H-01 |

## Context

Security finding H-01 requires that a user only receives answers based on documents they are allowed to open in SharePoint. About one in five documents in the restricted libraries, and a small number in the general library, have unique permissions. The separate restricted index proposed in CR-01 filters per library and is therefore insufficient.

## Options

1. **Query-time check per result.** Retrieve as today, then check for every candidate document whether the user can open it, by calling SharePoint at query time. Accurate, but adds several calls per question and makes latency depend on SharePoint response times.
2. **Security filter in the index.** Store the allowed principals (users and groups) per document on every chunk in Azure AI Search, and filter every query on the user's identity and group memberships. Requires a sync of permissions.
3. **One index per permission set.** Not realistic with hundreds of distinct permission sets.

## Decision

Option 2, with a fail-closed rule.

- **Indexing.** For each document the indexing job reads the effective read permissions from SharePoint and resolves SharePoint groups to the directory groups and users they contain. The list of allowed principal IDs is written to a filterable field on every chunk of that document.
- **Sync.** An hourly job processes permission changes since the last run; a nightly reconciliation compares the full permission set for all documents. A changed document is re-indexed with its new permissions within the hour.
- **Query.** The Teams bot passes the authenticated user's ID. The query layer resolves the user's group memberships (cached for 15 minutes) and adds a filter: allowed principals must contain the user or one of their groups. The filter applies before ranking, so nothing outside the user's permissions reaches the model prompt.
- **Fail closed.** If permissions for a document cannot be read, or a group cannot be resolved, the document is not indexed or not returned. Errors are logged and reported daily.
- **Answer cards.** No change for the user. If a question cannot be answered from permitted documents, the bot says it did not find an answer. It never says that a restricted document exists.

## Consequences

- Correctness depends on the sync: a permission removed in SharePoint stays effective in the index for at most about an hour. Wim accepted this delay for the operations content, with the condition that an emergency full re-sync can be started manually.
- Users with very many group memberships produce long filters. We will measure the latency impact (R-14) in the performance test planned for early July.
- Messy permissions become visible. Clean-up of the group structure on the restricted sites (led by Wim) reduces support questions after go-live.
- Group caching means a user added to a group may wait up to 15 minutes before seeing new answers. Acceptable.
- The pilot group gets restricted content only after the re-index with trimming is complete and spot-checked.

## Verification

- Test matrix of 40 documents with unique permissions × 12 test users with different roles, prepared with Wim's team.
- Automated test: for every test user, no returned chunk may come from a document that user cannot open via SharePoint.
- Re-test by Wim's team in the second half of August.

Pieter De Smet
