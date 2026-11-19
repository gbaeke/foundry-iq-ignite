# Policy Note: Handling Customer Data under GDPR

| | |
|---|---|
| **Organisation** | Kestrel Consulting (internal) |
| **Date** | 2024-04-26 |
| **Author** | Lotte Willems, Managing Partner |
| **Document type** | Internal policy note, version 2.0 (replaces version 1.3 of 2022) |
| **Applies to** | All Kestrel staff and subcontractors working under Kestrel contracts |

## 1. Why an update

Our work has shifted from dashboards and pipelines towards AI on documents and text. That means we see more personal data, and sometimes special categories such as health data. This note sets out what every colleague must do. It does not replace the data processing agreement with each customer; where the agreement is stricter, the agreement wins.

## 2. Our role

In almost all engagements the customer is the **controller** and Kestrel is a **processor**. We process personal data only on documented instructions of the customer, for the purpose of the engagement, and only for as long as needed.

## 3. Before any personal data is touched

1. A signed data processing agreement is in place.
2. The customer has confirmed whether a **DPIA** (data protection impact assessment) is needed. For any processing of health data, or large-scale processing with AI models, assume it is needed until the customer's DPO says otherwise.
3. Data minimisation is agreed: which fields, which period, which population.
4. The location of processing is agreed. Default: EU regions only.

A practical example. On the **Discharge Letter Summarisation** engagement at Mediva Care Group, the DPIA had to be completed before any patient data could be processed. The start moved six weeks, from the planned 2024-02-05 to **2024-03-18**. The outcome, agreed with Mediva's DPO, was clear: pseudonymisation of the content before every call to the Azure OpenAI model, and no patient data leaving the EU. In hindsight, the DPIA should have started before the contract was signed. From now on, every proposal involving personal data in AI processing includes a line on the DPIA status and who owns it on the customer side.

## 4. During the engagement

- Work in the customer's environment wherever possible. Copies of personal data to Kestrel environments need written approval from the customer.
- Never on personal devices, personal accounts or consumer AI tools. This includes pasting "just one example" into a chatbot.
- Test data: use synthetic or pseudonymised data. Real data in development only if the customer explicitly agrees.
- Logs and prompts can contain personal data too. Agree retention for application logs and model traces with the customer.
- Access is personal and on a need-to-know basis. No shared accounts.

## 5. Incidents

A suspected data breach is reported **immediately**, by phone, to the engagement lead and to me. Do not try to fix it quietly first. The customer has 72 hours to notify the authority, and that clock starts when they could have known, not when we decide to tell them.

## 6. End of the engagement

- Delete or return all personal data, including extracts on laptops and in test environments.
- Confirm the deletion in writing to the customer.
- Keep only what the contract allows, such as anonymised metrics for the closing report.

## 7. Subcontractors

Subcontractors working through Kestrel sign the same confidentiality and data handling terms. The engagement lead makes sure they have read this note.

## 8. Questions

Ask me or the engagement lead. When in doubt, do not process, ask first.

Lotte
