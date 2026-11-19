# Engineering Guideline: Coding Standards

| | |
|---|---|
| **Organisation** | Kestrel Consulting (internal) |
| **Date** | 2025-02-14 |
| **Author** | Pieter De Smet, Lead AI Architect |
| **Document type** | Engineering guideline, version 2.0 |
| **Applies to** | Application, data and ML code written by Kestrel |

## Why

We hand over almost everything we build. The customer's team will read our code long after we have left, often without us in the room. Code that is consistent, tested and boring to read is a feature. This guideline replaces the 2023 version, mainly to add rules for code that calls language models.

## 1. Languages and project setup

- **Python** for data, ML and back-end services. **TypeScript** for front ends, Teams apps and lightweight APIs where the team prefers it.
- Every repository starts from the internal template: folder layout, formatter, linter, type checking, test setup and pipeline definition included. Do not start from an empty folder.
- Dependencies are pinned with a lock file. Upgrades are a deliberate pull request, not a side effect.

## 2. Style

- Formatting is automatic. Nobody discusses whitespace in a review.
- Linter warnings fail the pipeline. If a rule really does not fit, disable it in the configuration with a comment, not inline all over the code.
- Type hints in Python on every public function. Strict mode in TypeScript.
- Names in English, also for customers with Dutch or French domain terms. Keep a glossary in the README for domain words that have no good translation.

## 3. Structure

- Small modules with one responsibility. A file longer than about 400 lines is a signal, not a crime.
- Configuration through environment variables and a typed settings object. No hard-coded endpoints, no keys in code.
- Business rules (deduplication rules, routing thresholds, class definitions) live in one place and are readable by a non-developer. Customers will ask to change them.

## 4. Tests

- Unit tests for business logic. Aim for meaningful coverage of rules and edge cases, not a percentage.
- Integration tests for every external dependency, runnable against a test environment.
- Data pipelines get tests on sample files that include the known bad cases: duplicates, missing values, late corrections.
- For AI components: an evaluation set run in the pipeline (see the AI evaluation guideline). A prompt change without an evaluation run is not merged.

## 5. Code that calls language models

- Prompts live in versioned files, not inline strings scattered through the code.
- Every call logs model name, version, token usage and latency. Content is logged only where the data processing agreement allows it.
- Set timeouts and retries with backoff. Handle throttling as a normal situation, not an exception.
- Never trust model output as code or as a query. Validate structured output against a schema before using it.
- Respect source permissions. If a user may not open a document, the system may not use it to answer that user.

## 6. Reviews

- Every change goes through a pull request with at least one reviewer. On customer production code, the reviewer is not the author's pair of the day.
- Small pull requests. If a review takes more than 30 minutes, the pull request is too big.
- Review checklist: correctness, tests, naming, security (secrets, permissions, input validation), logging, cost.
- Be kind and specific. "This breaks when the list is empty" beats "this is wrong".

## 7. Documentation

- README with purpose, how to run locally, how to deploy, and who owns what.
- Decisions that are hard to reverse get a short architecture decision record in the `docs/adr` folder.
- Runbooks are written for the person on duty at the customer, not for us.

## 8. Juniors and pairing

New colleagues pair with a senior on their first pull requests. Reviewing is also learning: juniors review seniors' code too, and ask questions.

Pieter
