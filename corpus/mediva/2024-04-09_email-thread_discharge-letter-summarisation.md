# Email Thread: Follow-up Privacy Check-in, Logging and Scanned Notes

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Discharge Letter Summarisation |
| **Document type** | Email thread |
| **Date** | 2024-04-09 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting (thread export) |

---

**From:** Sarah Mertens
**To:** Amira El Idrissi
**Cc:** Thomas Maes, Pieter De Smet, Jeroen Lambrecht
**Date:** 2024-04-08 17:02
**Subject:** Check-in 8 April: pseudonymisation v0.4

Dear Amira,

Thank you for the clear report. As discussed this afternoon:

1. Version 0.4 is accepted for the prototype phase.
2. I agree with a repeat test on a fresh sample of 200 letters before the evaluation in June.
3. The remaining indirect identifiers are acceptable given the purpose, as long as the logs stay pseudonymised and are deleted after 90 days.

One additional question I did not raise in the meeting: who at Kestrel can read the pseudonymised logs? I would like that list in writing.

Kind regards,
Sarah

---

**From:** Thomas Maes
**To:** Sarah Mertens
**Cc:** Amira El Idrissi, Pieter De Smet, Jeroen Lambrecht
**Date:** 2024-04-09 08:35
**Subject:** RE: Check-in 8 April: pseudonymisation v0.4

Dear Sarah,

Thank you. On the log access: within Kestrel, only Amira and Pieter have read access to the pseudonymised prompt and output logs. I do not, and Lotte Willems as engagement lead does not either. The accounts are granted by Jeroen's team and listed on the access list he maintains for the development dataset.

Retention of 90 days is configured as an automatic deletion rule. Jeroen, can you confirm the rule is active in the production subscription as well as in test?

Best regards,
Thomas

---

**From:** Jeroen Lambrecht
**To:** Thomas Maes, Sarah Mertens
**Cc:** Amira El Idrissi, Pieter De Smet
**Date:** 2024-04-09 10:14
**Subject:** RE: Check-in 8 April: pseudonymisation v0.4

Confirmed for test. Production does not exist yet; I will set the rule there when we build it in August and send a screenshot to Sarah.

Something else that came up in our Thursday session: a part of the older notes in the record are scanned PDFs, mostly reports from external hospitals before 2019. They contain no text layer. What do we do with them?

Jeroen

---

**From:** Pieter De Smet
**To:** Jeroen Lambrecht, Thomas Maes, Sarah Mertens
**Cc:** Amira El Idrissi
**Date:** 2024-04-09 11:48
**Subject:** RE: Check-in 8 April: pseudonymisation v0.4

Jeroen,

Our proposal: skip them for now and flag them in the draft ("This stay contains 2 scanned documents that were not used"). Adding text recognition would be a new processing step on identifiable images, which means a change to the data flow and a discussion with Sarah, and it is not in the fixed scope.

If physicians tell us during the evaluation that the scanned documents matter, we can look at it as a separate request.

Pieter

---

**From:** Sarah Mertens
**To:** Pieter De Smet
**Cc:** Jeroen Lambrecht, Thomas Maes, Amira El Idrissi
**Date:** 2024-04-09 13:20
**Subject:** RE: Check-in 8 April: pseudonymisation v0.4

Agreed, skipping and flagging is fine from my side. Thanks for the list, Thomas.

Sarah
