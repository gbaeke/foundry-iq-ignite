# Meeting Notes: Privacy and security review

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Meeting notes (privacy and security review) |
| **Date** | 2024-07-04 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Participants** | Fortalis data protection officer; Fortalis information security officer; Laura Vermeulen; Amira El Idrissi; Thomas Maes; Jonas Peeters |

## 1. Purpose

Review how claim data is processed in the triage solution before real claims are used in the acceptance environment. Development so far used pseudonymised historical claims only. The DPO asked for this review at the start; it was postponed twice because of the regulatory reporting deadline at Fortalis.

## 2. What was presented

Jonas walked through the design note of 2024-06-21: components, data flow, environments, private endpoints, audit trail. Amira explained what the model uses as input and what it does not use.

Model input: extracted fields (policy number, date and place of loss, amount, document types present) and the free text description. The model does **not** use name, address, date of birth, national register number, bank account or photo content.

## 3. Points raised and outcome

| # | Point | Raised by | Outcome |
|---|---|---|---|
| 1 | Legal basis for processing claims data for automated triage | DPO | Covered by the execution of the insurance contract. Triage only decides who handles a claim, not whether it is accepted or how much is paid. No automated decision in the sense of article 22 GDPR, provided that the routing has no effect on the outcome of the claim. Laura confirmed this in writing. |
| 2 | Health data in motor claims (injury descriptions) | DPO | Special category data. The injury keyword rule sends these claims to people, but the text still passes through the model. Accepted, because processing is needed for handling the claim and stays within Fortalis. To be listed in the processing register. |
| 3 | Training data | DPO | Historical claims used for training are pseudonymised: names, addresses, plate numbers and national register numbers are replaced in the free text before training. Amira showed the replacement rules and a sample of 20 records. DPO asked for a second check on plate numbers in French texts; Amira will extend the pattern. |
| 4 | Retention | DPO | Documents in the spoke storage: 90 days after routing, then deleted automatically. Audit trail without document content: 7 years, same as claim files. Training snapshots: kept as long as the model version is in production plus one year. |
| 5 | Access by Kestrel | Security officer | Kestrel staff use Fortalis-managed accounts, just-in-time privileged access, no data on Kestrel devices. Acceptance and production data visible only to named persons. Access reviewed monthly by Laura. |
| 6 | Logging of model inputs | Security officer | The audit trail stores the full input of each prediction. Agreed, needed for explaining decisions to handlers and auditors. Access restricted to the claims operations team and the project. |
| 7 | Overrides as labels | DPO | Using handler corrections as new training labels is in line with the original purpose. Must be mentioned in the internal procedure for the claims team. |
| 8 | Transparency towards customers | DPO | Fortalis' privacy notice already mentions automated support for claims handling. Legal will check whether the wording needs an update. Not blocking. |

## 4. Decisions

- The review is **passed with conditions**. Real claims may be processed in the acceptance environment from 2024-07-15, once conditions 3 and 5 are fulfilled.
- The solution is added to the Fortalis processing register by the DPO's office.
- A short data protection section is added to the model card and to the run book.

## 5. Action items

| Action | Owner | Due |
|---|---|---|
| Extend pseudonymisation for French plate numbers, re-check sample | AE | 2024-07-11 |
| Configure 90-day retention on spoke storage | JP | 2024-07-11 |
| Named access list for acceptance environment | LV / JP | 2024-07-11 |
| Written confirmation that routing does not affect claim outcome | LV | done |
| Add data protection section to model card and run book | AE / JP | 2024-09-30 |
| Check privacy notice wording | Fortalis legal | 2024-09-30 |

## 6. Remark

The DPO appreciated that the review happened before real data was used rather than after. Worth keeping that order on every project.

*Jonas Peeters*
