# Test Report: Pseudonymisation Residual Identifier Rate

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Discharge Letter Summarisation |
| **Document type** | Test report |
| **Date** | 2024-04-05 |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |
| **Distribution** | Sarah Mertens, Jeroen Lambrecht, Pieter De Smet, Thomas Maes |

## 1. Purpose

Action item 3 of the DPIA closure meeting (2024-03-11): test the pseudonymisation on 200 sample letters and report the residual identifier rate. The test was run inside Mediva's environment. The review of residual identifiers was done by a Mediva IT staff member with access to the identifiable source, together with me looking only at the pseudonymised output and the position markers. No identifiable content left Mediva's environment or appears in this report.

## 2. Method

**Sample.** 200 discharge letters from 2023, 100 from internal medicine and 100 from geriatrics, randomly selected by Mediva IT, together with the record sections the letters were based on (about 1,900 text sections in total).

**Pseudonymisation pipeline (version 0.3).**
1. Rule-based pass for structured identifiers: national register number, patient number, dates of birth, phone numbers, postal addresses, email addresses.
2. Named-entity model for free text: person names, places, institutions.
3. Dictionary pass with the names of Mediva staff, which are kept as role labels ("treating physician") rather than names.
4. Dates are shifted by a per-stay offset, so intervals stay correct ("day 3 of admission") but the real dates do not reach the model.

**Review.** Every remaining token that could identify a patient was marked by the reviewer and categorised as *direct* (name, number, exact address) or *indirect* (a combination that could point to a person: a rare occupation, a family relation with a role, a small village).

## 3. Results

| Measure | Result |
|---|---|
| Text sections processed | 1,912 |
| Sections with at least one residual **direct** identifier | 9 (0.47%) |
| Sections with at least one residual **indirect** identifier | 41 (2.1%) |
| Letters with any residual direct identifier | 6 of 200 |

**Residual direct identifiers, by cause:**

- 4 cases: patient names written in lower case or with a typo in free text, missed by the entity model
- 3 cases: national register number written with spaces in an unusual pattern
- 2 cases: name of a family member written inside quotes

**Residual indirect identifiers:** mostly family relations combined with an occupation or a workplace, as Sarah anticipated in the DPIA meeting, and village names in the social history.

## 4. Fixes in version 0.4

1. Rule pass extended with alternative spacing and separators for national register numbers.
2. Patient and relative names from the structured record are now also matched fuzzily (edit distance 1) in free text.
3. Social history: occupations and workplaces of relatives are replaced by a generic label ("relative, occupation removed").
4. Village and street names replaced by "[place]" in the social history section; campus names are kept.

Re-run on the same 200 letters with version 0.4: **0 sections with residual direct identifiers**, 11 sections (0.58%) with residual indirect identifiers, mostly rare medical histories that we cannot remove without destroying the clinical content.

## 5. Effect on draft quality

Removing occupations and places from the social history slightly reduces the quality of that paragraph in the draft. Physicians will have to complete it themselves. We consider this acceptable; the social history is short in most letters.

## 6. Proposal for Sarah

- Accept version 0.4 for the prototype phase.
- Repeat the test on a new sample of 200 letters before the clinical evaluation starts in June.
- Report the residual rate in every monthly privacy check-in.

To be discussed at the check-in of 2024-04-08.
