# Proposal: Discharge Letter Summarisation

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Discharge Letter Summarisation |
| **Document type** | Proposal |
| **Date** | 2024-01-15 |
| **Author** | Lotte Willems, Managing Partner, Kestrel Consulting |
| **Reference** | KC-PROP-2024-003 |

## 1. Context

Physicians at Mediva Care Group spend a significant part of their last hours with a patient writing the discharge letter ("ontslagbrief") for the general practitioner. The letter pulls together the admission reason, the course of the stay, lab results, medication changes and follow-up instructions, information that already exists in the electronic patient record but is spread over notes, reports and orders.

Dr. Hilde Van Damme, Chief Medical Information Officer, asked Kestrel Consulting to propose a solution that drafts a first version of the discharge letter, which the physician then reviews, edits and signs. The physician always stays in control; the system produces a draft, never a final letter.

This proposal follows two workshops in December 2023 with Dr. Van Damme, Jeroen Lambrecht (IT Manager) and Sarah Mertens (Data Protection Officer).

## 2. Proposed approach

We propose a generative AI solution based on **Azure OpenAI**, deployed in an Azure region inside the European Union. EU data residency is a firm requirement: prompts, patient content and generated drafts are processed and stored only in EU datacentres, and the Azure OpenAI deployment is configured so that no data is retained for model training.

The work is organised in four phases:

1. **Foundation (weeks 1 to 4):** secure Azure environment, integration pattern with the patient record, data protection review with Sarah Mertens, selection of two pilot departments.
2. **Prototype (weeks 5 to 12):** prompt design and retrieval of relevant record sections, letter templates per specialty, first drafts on historical letters.
3. **Clinical evaluation (weeks 13 to 24):** structured evaluation with a group of physicians who compare drafts against their own letters and record editing time and corrections.
4. **Pilot and handover (weeks 25 to 34):** use in daily practice on the pilot departments, monitoring, documentation and handover to Mediva IT.

## 3. Team

| Role | Name |
|---|---|
| Architect | Pieter De Smet, Lead AI Architect |
| ML engineer | Amira El Idrissi, ML Engineer |
| Project manager | Thomas Maes, Project Manager |
| Engagement lead | Lotte Willems, Managing Partner |

On the Mediva side we propose Dr. Hilde Van Damme as sponsor, Jeroen Lambrecht as IT contact for integration and infrastructure, and Sarah Mertens as DPO for all privacy questions.

## 4. Planning

- Planned start: **2024-02-05**
- Planned duration: about 34 weeks
- Steering committee: monthly, chaired by Dr. Van Damme
- Weekly working session with Jeroen's team during the foundation and prototype phases

## 5. Commercials

| Item | Amount |
|---|---|
| Fixed price, all phases | EUR 120,000 excl. VAT |
| Invoicing | 30% at start, 30% after prototype acceptance, 40% at handover |
| Azure consumption | billed directly to Mediva, estimated separately |

## 6. Assumptions and risks

- Mediva provides access to a representative set of historical letters and record extracts in time for the prototype phase.
- Physicians are available for the evaluation phase (roughly two hours per physician per week).
- The data protection review may lead to additional technical measures. We will assess their impact with Sarah Mertens as soon as possible and agree on any change to planning or price through the steering committee.
- Generated drafts may contain errors; the design assumes mandatory physician review before signing.

## 7. Next steps

We kindly ask Dr. Van Damme to confirm this proposal by 2024-01-26 so we can hold the start date of 2024-02-05.

*Lotte Willems, Kestrel Consulting, Ghent*
