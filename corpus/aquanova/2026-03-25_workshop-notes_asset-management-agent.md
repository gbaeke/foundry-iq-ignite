# Workshop Notes: Evaluation Questions with Asset Planners

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Asset Management Agent |
| **Date** | 2026-03-25 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Workshop notes (requirements and evaluation) |
| **Participants** | The pilot coordinator, five asset planners, Pieter De Smet, Ruben Wouters; Kevin Hermans for the last hour |

## 1. Purpose

Build the first version of the evaluation set from real questions, and agree with the planners what a "good answer" means. The SOW makes the evaluation report part of phase 1 acceptance.

## 2. Input

The pilot coordinator collected 74 questions from planners over three weeks, written as they were asked on the phone or in mails. We removed duplicates and questions that are clearly out of scope (creating work orders, questions about personnel planning). 60 remained.

## 3. Question categories

| Category | Example | Count | Needs |
|---|---|---|---|
| Procedure | "What is the inspection interval for fire hydrants in residential streets?" | 18 | knowledge base |
| Technical sheet | "What is the maximum operating pressure of valve type X?" | 9 | knowledge base |
| Inspection result | "What did the last inspection of reservoir Y find?" | 11 | knowledge base (inspection reports) |
| Maintenance history | "When was pump P-xx last overhauled, and why?" | 12 | tool |
| Asset lookup | "Which valves are within 200 m of this address?" | 6 | tool |
| Combined | "Is this hydrant due for inspection, and what did the last one find?" | 4 | knowledge base and tool |

Only 27 of the 60 can be answered with the knowledge base alone. The rest need the tools on the asset register and maintenance history.

## 4. What is a good answer

The planners agreed on these criteria, in their own words:

1. **Correct.** "If it's wrong once, I'll check everything afterwards, and then it saves me nothing."
2. **Shows the source.** A link to the document or the record. Planners want to click and check.
3. **Says when it doesn't know.** Better "I found no inspection report for this asset" than a guess.
4. **Specific to the asset.** Not a general procedure when the question is about one valve.
5. Short. One paragraph, then details if asked.

## 5. How we will score

- Every answer is scored by two planners: correct / partly correct / wrong, and "source shown: yes/no".
- An answer is counted as correct only if both planners say correct.
- Pieter and Ruben do not score.
- The set is versioned. New questions are added during the pilot; old ones are not changed.

Kevin asked to add a few questions about documents that pilot planners are *not* allowed to see, to test that permissions are respected. Five such questions were added, with the expected answer "no information".

## 6. Targets

No hard target in the SOW. Proposal, accepted by the pilot coordinator:

- Procedures and technical sheets: at least 85% correct before the pilot.
- Asset-specific categories: reported separately, no target until the tools exist.
- Permission questions: 100% "no information".

## 7. Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Evaluation set v1 (60 + 5 questions) in the repository | RW | 2026-03-27 |
| 2 | Expected answers and sources for each question | Pilot coordinator with two planners | 2026-04-10 |
| 3 | First evaluation run on the knowledge base | PDS | 2026-04-17 |
| 4 | Scoring sheet and instructions | PDS | 2026-04-10 |
