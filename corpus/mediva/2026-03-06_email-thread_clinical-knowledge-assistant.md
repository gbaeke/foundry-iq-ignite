# Email Thread: DPO Review of Front End Safeguards

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Clinical Knowledge Assistant |
| **Document type** | Email thread |
| **Date** | 2026-03-06 |
| **Author** | Amira El Idrissi, Lead AI Engineer, Kestrel Consulting (thread export) |

---

**From:** Amira El Idrissi
**To:** Sarah Mertens
**Cc:** Pieter De Smet, Ruben Wouters, Jeroen Lambrecht
**Date:** 2026-03-03 16:20
**Subject:** Clinical Knowledge Assistant: design for your review

Dear Sarah,

As announced at kickoff, here is the design for your review before the pilot. In short:

1. The knowledge base contains only guideline and protocol documents of cardiology and emergency. No patient data is indexed.
2. All processing runs in Mediva's subscription in an EU region: Microsoft Foundry project, Foundry IQ knowledge base and Azure OpenAI deployment. No data is used for model training.
3. Users may still type patient details in a question. Ruben built three safeguards in the question box:
   - a permanent notice: "Do not enter patient names or identifiers"
   - detection of national register numbers, patient numbers and dates of birth before the question is sent; if found, the question is blocked with an explanation
   - detection of capitalised name patterns next to words like "patient" or "mevrouw/meneer", which shows a warning but does not block
4. Questions, answers, citations and feedback are logged for quality review, with automatic deletion after 90 days, as in the discharge letter project.

Could we go through it on Thursday or Friday?

Kind regards,
Amira

---

**From:** Sarah Mertens
**To:** Amira El Idrissi
**Cc:** Pieter De Smet, Ruben Wouters, Jeroen Lambrecht
**Date:** 2026-03-04 09:47
**Subject:** RE: Clinical Knowledge Assistant: design for your review

Dear Amira,

Thank you, this is clear. Friday 10:00 works. A few questions so I can prepare:

- Who can read the logs? Same rule as before (named persons only)?
- Is the warning in point 3 logged? I would like to know how often people try.
- Is a blocked question stored anywhere?

Sarah

---

**From:** Amira El Idrissi
**To:** Sarah Mertens
**Cc:** Pieter De Smet, Ruben Wouters, Jeroen Lambrecht
**Date:** 2026-03-04 11:02
**Subject:** RE: Clinical Knowledge Assistant: design for your review

- Logs: Pieter and I at Kestrel, plus two named people in Mediva IT. Ruben works on the front end with synthetic test questions only and has no access to production logs.
- Warnings: we log that a warning was shown, not the text that triggered it.
- Blocked questions: not sent and not stored. Only a counter is kept.

Amira

---

**From:** Sarah Mertens
**To:** Amira El Idrissi, Pieter De Smet
**Cc:** Ruben Wouters, Jeroen Lambrecht, Dr. Hilde Van Damme
**Date:** 2026-03-06 14:15
**Subject:** RE: Clinical Knowledge Assistant: design for your review

Dear all,

Following our meeting this morning, my conclusions:

1. The assistant does not process patient data by design. A full new DPIA is not required.
2. Because users could still enter patient details, I will write a short **addendum** to the existing assessment covering the question box safeguards and the logging. I expect to finish it by 20 March.
3. Condition for the pilot: the counter of blocked questions and warnings is reported to me monthly. If warnings stay frequent, we review the safeguards.
4. The 90-day retention is confirmed.
5. The notice in the question box should also say that the assistant does not give patient-specific advice. Hilde, please confirm the wording.

Kind regards,
Sarah Mertens
Data Protection Officer
