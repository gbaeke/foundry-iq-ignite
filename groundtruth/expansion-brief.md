# Corpus expansion brief

Goal: grow the Kestrel corpus from 34 to about 230 documents so that topic graphs have real themes to
separate (target several hundred passages), while every fact in `groundtruth/world.yaml` and every
answer in `groundtruth/questions.yaml` stays true. Never upload this file or world.yaml.

## Hard rules (the eval depends on them)

1. **No new ground-truth facts.** Do not add projects, people, customers, partners or technologies.
   - Team membership per project is exactly the `team` in world.yaml. Nobody else from Kestrel or
     DataForge works on a project; customer contacts stay as listed. Unnamed roles ("a planner",
     "two claims handlers", "the TOS vendor") are fine.
   - Technologies: a project document may only name products from that project's `technologies`
     list. Use generic words otherwise ("the pipeline", "a Python notebook", "the dashboard").
     Do not name Databricks, Azure OpenAI, Microsoft Fabric etc. in a project that doesn't list them.
   - Dates, amounts, go-live dates, outcomes and issue facts must match world.yaml exactly when
     mentioned. Respect each document's own date: it can't know later events (Thomas leaves on
     2025-12-31, Kevin moves to AquaNova on 2025-09-01, Ruben joins on 2025-01-06, Amira's title
     changes on 2025-12-01, the Ops Copilot slips, Claims Triage overruns, Broker Portal is cancelled).
   - Don't contradict the existing documents in `corpus/`. Read the existing documents of your
     projects first and stay consistent with their invented details (sprint names, CR numbers, lines,
     zones, ward names).
2. **Keep facts scattered.** No document lists a full team roster across projects, all projects of a
   person, or all projects per technology.
3. **Look-alike names** (Tine Desmet vs Pieter De Smet, Evelien Claes vs Sofie Claes, Jan Wouters vs
   Ruben Wouters, Koen Verstraete vs Koen Martens) must never be confused. Use first names and
   initials naturally after the first mention.

## What to add

Realistic, varied day-to-day project documents, spread over each project's period (ongoing projects
up to 2026-11-15). Mix of:

- biweekly status reports (RAG table, progress, risks, next steps)
- sprint review or demo notes, steering committee minutes
- technical design notes, architecture decision records (ADR-xx), data mapping notes
- workshop notes (requirements, process mapping, prioritisation)
- email threads (2–5 messages, quoted headers)
- UAT or test reports, cutover and go-live checklists, runbooks, handover notes
- risk and issue logs, change requests (only CR-07 changes budget for Claims Triage; other CRs are
  scope clarifications without cost impact)
- retrospectives, user feedback summaries, training material outlines

Give the corpus **themes beyond the issues in world.yaml**, recurring across customers but never
cross-referenced by name: data quality and master data, security reviews and identity, privacy and
GDPR, OT/IT networking, change management and user adoption, testing and evaluation of AI output,
cost and FinOps, vendor coordination, documentation and handover, performance tuning, scheduling and
holidays ("bouwverlof", Christmas freeze), stakeholder communication.

## Format

- Markdown, 300–700 words, with a header block: title, customer, project, date, author, document type.
  The author must be someone on that project (or Lotte Willems for commercial or management documents).
- File name: `corpus/<customer-folder>/<YYYY-MM-DD>_<doc-type>_<project-slug>.md`, lowercase,
  hyphens. Use the existing project slugs. Never overwrite an existing file.
- English, professional, concrete, occasional Belgian touch. No marketing tone.
