# Lunch and Learn: Evaluating a Knowledge Assistant with Clinicians

| | |
|---|---|
| **Organisation** | Kestrel Consulting (internal) |
| **Date** | 2026-10-23, 12:15 to 13:30 (kennisdeling session) |
| **Location** | Kestrel office Ghent, big room, and Teams |
| **Author / presenter** | Amira El Idrissi, Lead AI Engineer |
| **Document type** | Internal session notes |

## Context

This session used the **Clinical Knowledge Assistant** at Mediva Care Group as a case. The assistant, built on Microsoft Foundry with a Foundry IQ knowledge base and Azure OpenAI, answers questions from physicians and nurses based on Mediva's own clinical guidelines and protocols, always with a reference to the source. It is in pilot in the **cardiology** and **emergency** departments.

The talk was not about the architecture. It was about one question: how do you know whether a clinical assistant is good enough?

## 1. Build the evaluation set with the people who will use it

The evaluation set now contains **200 questions**, written and reviewed with clinicians from both pilot departments. Every question has:
- a reference answer, written by a clinician
- the expected source document and section
- a tag for the department and the type of question (dosing, procedure, contraindication, organisation)

Practical tips that worked:
- Sessions of 45 minutes at most, with coffee, in the department rather than in a meeting room.
- Ask clinicians for the questions they actually asked a colleague last week, not for "test questions". The second kind is always too easy.
- Let a second clinician review every reference answer. Disagreements between clinicians are information, not noise.

## 2. Score what matters

We rate every answer on three things: correct and complete, partially correct, or incorrect / wrong source. A correct answer from the wrong source counts as wrong. In a clinical setting, the source is part of the answer, because the clinician must be able to check it.

The full set runs after every change to prompts, retrieval settings or the content of the knowledge base, so we can tell which change helped and which did harm.

## 3. The surprise: conflicting answers

In the summer we saw the assistant give **conflicting answers** to essentially the same question. Our first suspicion was the model. It was not. The guideline library contained several **versions of the same guideline**: the current one and outdated ones that were never archived. Retrieval found both, and depending on the wording, the outdated version ranked higher.

What we learned:
- Technical mitigations help: prefer the most recent version, and show the guideline version and publication date in every answer. But they cannot decide which version is valid.
- That decision belongs to the content owners. The team of Dr. Hilde Van Damme, the sponsor, now runs a clean-up per department, marking each document as current, superseded or archive, and only current documents are indexed.
- The evaluation set made the problem visible. Without the expected source per question, we would have seen "sometimes wrong" without knowing why.

This is a **content governance** problem, and it will come back on every knowledge assistant over a document library that grew over years. Ask in the first workshop who owns each folder and how old versions are archived.

## 4. Feedback from users is evaluation too

Clinicians can flag an answer as "outdated source" directly in the front end. These flags feed a monthly review with the content owners. In practice, user flags find problems the fixed evaluation set does not cover, so the two complement each other.

## 5. Generic advice for knowledge assistants

1. Evaluation set before the first demo, built with real users.
2. Expected source per question, not only expected answer.
3. Rerun the full set after every content change, not only after code changes.
4. Make content ownership a condition before adding a new department or library.
5. Report errors by category: content, retrieval, generation, unclear reference.

## Questions

- *Can an LLM judge replace the clinicians?* For regression runs, as a pre-filter, calibrated on a sample of human ratings. Not for the sign-off.

Slides on the internal SharePoint.

Amira
