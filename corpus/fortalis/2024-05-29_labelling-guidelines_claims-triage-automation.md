# Labelling Guidelines v1.0: Complexity and urgency

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Guideline / working instruction |
| **Date** | 2024-05-29 |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |
| **Approved by** | Laura Vermeulen, Claims Operations Manager |
| **For** | Claims handlers labelling historical claims |

## 1. Why this document

After the first three weeks of labelling, the two labellers agreed on urgency in only about two thirds of the 50 claims they both labelled. Most disagreements were not about the facts but about the rule being applied. In the calibration session of 2024-05-23 we went through every disagreement together. This document captures the outcome so that every labeller, including the colleague joining on Wednesdays, applies the same rules.

## 2. General rules

1. **Label what was known at intake.** Look only at the documents and text available when the claim arrived. Do not use information from later correspondence or the final settlement, even if you remember the case.
2. **When in doubt, choose "unsure".** An "unsure" label is useful. A guessed label harms the model.
3. **One claim, one label set.** If a file contains two claims (for example a car theft with damage to the garage), label the main claim and add a note.
4. **Do not correct the claim type here.** Claim type comes from the system. If you think it is wrong, tick "type doubtful".

## 3. Complexity

| Label | Use when | Examples |
|---|---|---|
| Simple | One party, clear cause, no injury, estimated amount below the expert threshold | Broken car window, stolen bicycle from a shed |
| Standard | Normal investigation needed, possibly a second party, amount below the expert threshold | Parking damage with a known third party |
| Complex | Any of: injury mentioned, more than two parties, amount above the expert threshold, signs of litigation, a lawyer in copy | Kitchen fire with smoke damage to the whole house |

If the amount is unknown, judge on the description. A fire with "smoke everywhere" is complex even without an amount.

## 4. Urgency

| Label | Rule | Typical signals |
|---|---|---|
| U1 | The customer cannot use their home or the vehicle they need, or damage will get worse without action | "We sleep at my parents'", "the door can't be locked", "roof partly open", "car needed for work tomorrow" |
| U2 | Normal handling | Most claims |
| U3 | Nothing to do soon | Claim reported "for information", minor damage, customer explicitly says no rush |

Important clarifications from the calibration session:

- **Fire is not automatically U1.** A small fire in a barbecue that scorched a terrace is U2 or U3.
- **Theft of a car is U1 only if** the description mentions the customer needs the car, or a replacement vehicle is requested.
- **A broken lock after a burglary is always U1.**
- **Weather words alone are not a signal.** "There was a storm" says nothing about urgency; look at the consequence.

## 5. Language

Labellers work in their own language. Claims in a language you do not read well: skip with "language" as reason. About 3% of claims are in English or German; these are labelled by the colleague who handles international claims.

## 6. Practical

- The labelling screen runs inside the Fortalis environment. Do not copy text or screenshots to e-mail or chat.
- Target pace: 25 to 30 claims per hour once you are used to it. Quality comes first.
- Every Friday, Amira samples 20 labels per labeller and shares the agreement score. This is not an evaluation of you; it is how we see whether the rules are clear.
- Questions: post them in the labelling question list. Laura decides on business rules, Amira on the use of labels.

## 7. Changes in this version

- Added the "type doubtful" checkbox.
- Merged the old "urgent" and "very urgent" into U1.
- Added rule on burglary locks and on weather words.

*Amira El Idrissi*
