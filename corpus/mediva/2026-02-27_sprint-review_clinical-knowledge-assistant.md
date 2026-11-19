# Sprint Review Notes: Sprint 3

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Clinical Knowledge Assistant |
| **Document type** | Sprint review notes |
| **Date** | 2026-02-27, 12:30 to 13:30 (Friday sounding board demo) |
| **Location** | Mediva, campus Centrum, and online |
| **Author** | Ruben Wouters, Developer, Kestrel Consulting |

## Attendees

Clinical sounding board (two cardiologists, one emergency physician, two emergency nurses), the guideline coordinator of emergency, Dr. Hilde Van Damme (first 20 minutes), Jeroen Lambrecht, Pieter De Smet, Amira El Idrissi, Ruben Wouters.

## 1. Sprint goal

Both pilot departments in the knowledge base; answer view with version and date; first measurements of answer time and cost per question.

## 2. Demonstrated

**2.1 Emergency sources live.** Amira indexed the emergency protocols and the emergency nursing procedures on 2026-02-19. The department selector now offers cardiology, emergency and "both".

**2.2 Answer view.** Each answer shows:
- the answer text, with numbered citations
- per citation: document title, version, publication date and a link to the document in the library
- a grey label "version derived" when the version was not in the metadata
- thumbs up / thumbs down, with an optional comment

**2.3 Compound questions.** The emergency physician asked: "Chest pain, suspected aortic dissection, patient on a DOAC: what do we do first and when do we call the cardiologist on call?" The answer combined the emergency chest pain protocol, the cardiology protocol for aortic syndromes and the anticoagulation reversal procedure, with three citations. The physician checked the sources and agreed with the answer, but noted it was too long to read at 3 a.m.

**2.4 Not found.** Asked about a procedure that only exists in intensive care, the assistant answered that no Mediva source in the selected departments covers it, and suggested selecting "all departments" (not yet available in the pilot).

## 3. Measurements (internal test set, 45 questions)

| Measure | Result | Target |
|---|---|---|
| Time to first words | 4.1 s median | 6 s |
| Complete answer | 11.8 s median, 17.5 s at the 90th percentile | 15 s for 90% |
| Consumption cost per question | a few euro cents | to be agreed |

The 90th percentile is above target, mainly on compound questions with three or more sub-queries. Amira will tune the retrieval instructions to limit the number of sub-queries for simple questions.

## 4. Feedback from the sounding board

1. **Shorter answers.** "Give me the steps first, explanation after." Agreed: answers start with a short action list, followed by details and citations.
2. **Dosing tables.** A cardiologist asked a dosing question; the answer quoted the table correctly but the layout was hard to read. Ruben will render tables as tables in the answer view.
3. **Nurses' language.** The nurses phrase questions differently ("what do I prepare for..."). They want their own example questions in the evaluation set. Amira agreed.
4. **Trust.** Both cardiologists said they will always open the source for dosing questions. The emergency nurse said she probably will not at night. Pieter noted this as a design point: the most critical facts must be visibly linked to their source.

## 5. Technical notes

- Front end hosted in the intranet test environment, sign-in with hospital accounts, access limited to the sounding board group for now.
- Answers and feedback are logged with the question text. Retention and the handling of patient details in questions are on the agenda with Sarah Mertens next week.
- Knowledge sources refresh daily at 05:00.

## 6. Next sprint (sprint 4, 2 to 13 March)

| Item | Owner |
|---|---|
| Action-list-first answer format | AE |
| Tables rendered in answer view | RW |
| Patient detail warning and blocking in the question box (for DPO review) | RW |
| Limit sub-queries for simple questions | AE |
| Evaluation set v1 draft | AE |
