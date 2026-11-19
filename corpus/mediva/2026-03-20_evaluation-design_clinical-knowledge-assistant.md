# Evaluation Design: Question Set v1

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Clinical Knowledge Assistant |
| **Document type** | Evaluation design note |
| **Date** | 2026-03-20 |
| **Author** | Amira El Idrissi, Lead AI Engineer, Kestrel Consulting |
| **Agreed with** | Guideline coordinators of cardiology and emergency; clinical sounding board |

## 1. Purpose

A fixed, versioned set of questions that we run after every change to the knowledge base, the retrieval instructions, the answer instructions or the model deployment. The set tells us whether a change makes the assistant better or worse before clinicians notice. It replaces "it looked fine in the demo" with a number we can track.

## 2. Version 1 at a glance

| | Cardiology | Emergency | Cross-department | Total |
|---|---|---|---|---|
| Questions | 48 | 52 | 20 | **120** |
| Written by physicians | 30 | 28 | 12 | 70 |
| Written by nurses | 10 | 20 | 6 | 36 |
| Written by coordinators | 8 | 4 | 2 | 14 |

The plan is to grow the set to about 200 questions during the pilot, adding real questions from users (after review and removal of anything patient-related).

## 3. What a question looks like

Each item contains:

- the question, in the words of the person who wrote it, Dutch or English as they asked it
- a reference answer written by the coordinator, short, in action-list form
- the expected source document(s) and the section
- the category (see below)
- critical elements: facts that must be in the answer (for example a dose, a threshold, a time limit)

Example (emergency): "What do I prepare for a patient with suspected sepsis in the waiting room?" Reference: the steps of the emergency sepsis protocol, expected source: the current sepsis protocol, critical elements: the time target for antibiotics and the lactate measurement.

## 4. Categories

| Category | Share | Example |
|---|---|---|
| Single fact (dose, threshold, timing) | 30% | Maximum dose in a cardiology protocol |
| Procedure steps | 30% | Preparation for cardioversion |
| Compound / cross-department | 17% | Chest pain on anticoagulants, when to call cardiology |
| Not answerable from Mediva sources | 10% | A procedure that exists only in intensive care |
| Ambiguous wording | 13% | Abbreviations, local jargon, nurses' phrasing |

The "not answerable" questions test that the assistant says so instead of improvising.

## 5. Scoring

Each answer is scored on three criteria:

1. **Correct and complete:** all critical elements present and correct.
2. **Right source:** the expected document is cited (another current document with the same content is accepted).
3. **Safe refusal:** for unanswerable questions, the assistant states that Mediva sources do not cover it.

Final label per question: *correct and complete*, *partially correct* (some critical elements missing, nothing wrong), or *incorrect or wrong source*.

**Who scores.** A first pass is done automatically: a model-based grader compares the answer with the reference and the critical elements. Every answer labelled other than "correct and complete", plus a random 20% of the rest, is reviewed by a clinician of the sounding board. In the dry run, the grader and the clinicians agreed on 91% of labels; disagreements were mostly on partially correct answers, where the clinician label wins.

## 6. Baseline run (2026-03-18)

| Label | Share |
|---|---|
| Correct and complete | 72% |
| Partially correct | 17% |
| Incorrect or wrong source | 11% |

Main causes of "incorrect": dosing tables read wrongly from spreadsheets (fixed in the meantime for cardiology), and two answers that cited a local working instruction from the legacy share instead of the current protocol. Unanswerable questions: 10 of 12 handled correctly.

## 7. Rules

- The set is versioned; changes to reference answers require the coordinator's approval.
- Reference answers are checked against the current source when a guideline is updated.
- Results are reported per category and per department at every steering committee.
- The set contains no patient data. User questions are added only after review by Amira and the coordinator.

## 8. Next steps

Agree v1 at the steering committee of 2026-03-25; rerun after the next retrieval tuning; start collecting pilot questions from the first pilot week.
