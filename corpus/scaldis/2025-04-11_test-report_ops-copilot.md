# Test Report: Answer Quality Evaluation, Pilot Week 3

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Scaldis Ops Copilot |
| **Date** | 2025-04-11 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Test report |
| **Reviewed with** | Nathalie Dumont and two shift leaders, 2025-04-10 |

## 1. What we test and why

An answer that sounds right but is wrong is worse than no answer on a terminal. We therefore evaluate on three levels:

1. **Regression set:** 120 fixed questions in Dutch, French and English with an expected source and a reference answer, written by Nathalie's team. Runs automatically after every index or prompt change.
2. **Pilot sample:** 100 real questions asked by pilot users in the first three weeks, rated by two shift leaders.
3. **Adversarial set:** 30 questions meant to make the bot go wrong: out-of-scope questions, questions about restricted topics, attempts to make it ignore its instructions.

## 2. Rating scale

| Score | Meaning |
|---|---|
| A | Correct, complete, right source cited |
| B | Correct but incomplete, or right answer with a weaker source |
| C | "Not found" although the answer exists |
| D | Wrong, outdated or not supported by the cited source |

D is the score we care about most.

## 3. Results

| Set | A | B | C | D |
|---|---|---|---|---|
| Regression set (120), 14 March | 94 | 15 | 5 | 6 |
| Regression set (120), 10 April | 101 | 12 | 4 | 3 |
| Pilot sample (100) | 71 | 14 | 9 | 6 |

Improvements since March come from the content clean-up (outdated versions archived), a better section split for checklists, and a stricter instruction to quote numbers literally from the source.

**The six D answers in the pilot sample:**
- 3 × outdated document still present in a library (two French versions of the lashing checklist, one old reefer SOP)
- 1 × two SOPs contradict each other on the reporting time for a damaged seal; both are current. Sent to the content owners.
- 1 × question about an incident procedure; the bot answered from a general SOP that mentions the topic in passing. The real procedure sits in the restricted library, not available yet.
- 1 × retrieval picked a section about empty containers for a question about reefers.

## 4. Adversarial set

- 30 of 30 out-of-scope questions (weather, football, salary questions) answered with the standard "I can only help with operations procedures" message.
- Instruction override attempts: none succeeded in producing content outside the SOPs.
- 2 questions about customs inspection steps were answered from general SOPs with partial information. Correct behaviour given the current scope, but it shows that users will ask about restricted topics.

## 5. Performance and cost

| Measure | Pilot value |
|---|---|
| Median answer time | 3.1 s |
| 95th percentile | 6.8 s |
| Questions in three weeks | ~190 |
| Model cost per question (Azure OpenAI, chat plus embedding) | about two euro cents |
| Search service | fixed monthly cost, independent of usage |

Cost per question is low; the fixed Azure AI Search cost dominates at pilot volumes. At expected go-live volumes the split will be closer to half and half.

## 6. Conclusions

- Quality is acceptable for a pilot. Most wrong answers are content problems, not model problems. The monthly content clean-up needs to continue after go-live; this is a routine for Nathalie's team, not a project task.
- Users already ask about restricted topics. The access design for CR-01 must be settled before go-live.
- We keep the D score as the main quality metric in the weekly quality report.

## 7. Next steps

| Action | Owner |
|---|---|
| Archive the three outdated documents | Content owners |
| Resolve contradiction on damaged seal reporting time | ND |
| Add the six D cases to the regression set | PDS |
| Share adversarial set and results with Wim Goossens | PDS |

Pieter De Smet
