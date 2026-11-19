# Email thread: Claims system write interface

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Email thread |
| **Date** | 2024-06-14 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Participants** | Jonas Peeters, Laura Vermeulen, Thomas Maes, claims system team lead (Fortalis) |

---

**From:** Jonas Peeters
**To:** Laura Vermeulen
**Cc:** Thomas Maes
**Date:** 2024-06-05 10:12
**Subject:** Write interface claims system - where do we stand?

Hi Laura,

Quick check on the write interface. We now have the read side working against the test environment of the claims system (claim lookup, policy lookup, document attach). For routing we need to be able to set the queue, the claim type, complexity and the urgency on a claim, and add a short note with the reason.

The proposal assumed API access by June. Without the write side we can keep testing with a stub, but we cannot start the integration tests planned from October with a stub. Could you check with the claims system team where this is?

Thanks,
Jonas

---

**From:** Laura Vermeulen
**To:** Jonas Peeters
**Cc:** Thomas Maes; claims system team lead
**Date:** 2024-06-05 15:47
**Subject:** RE: Write interface claims system - where do we stand?

Jonas,

Adding the team lead of the claims system team. As far as I know they have it on their board, but behind the regulatory reporting release at the end of June.

Laura

---

**From:** Claims system team lead
**To:** Laura Vermeulen; Jonas Peeters
**Cc:** Thomas Maes
**Date:** 2024-06-07 09:30
**Subject:** RE: Write interface claims system - where do we stand?

Hello all,

Correct, the regulatory release has priority until 2024-06-28. We can start on the write interface on 2024-07-01. Our estimate is four weeks of development plus one week of testing, so available in the test environment around 2024-08-02. Note that a large part of my team is on holiday in the second half of July, bouwverlof or not, so I'd rather say mid-August to be honest.

Some conditions from our side:
- One endpoint to update the triage fields and the queue, one to add a note. No direct database access.
- Calls authenticated with a workload identity, which we must whitelist.
- Maximum 10 calls per second in production for now. If you need more, tell us now.

Can Jonas send us the field list and the expected volumes?

Regards

---

**From:** Thomas Maes
**To:** Claims system team lead; Laura Vermeulen; Jonas Peeters
**Date:** 2024-06-07 11:05
**Subject:** RE: Write interface claims system - where do we stand?

Thank you, clear answer. Mid-August still works for our plan: integration testing starts in October, so we have about six weeks of margin. I will log it as a dependency with a target date of 2024-08-16 in our risk log.

Jonas will send the field list and volumes today.

Thomas

---

**From:** Jonas Peeters
**To:** Claims system team lead
**Cc:** Laura Vermeulen; Thomas Maes
**Date:** 2024-06-14 16:20
**Subject:** RE: Write interface claims system - where do we stand?

Hello,

As promised (sorry, a few days later than "today"), the details:

**Fields to write:** queue code, claim type code (mapped to your codes), complexity (S/ST/C), urgency (U1/U2/U3), triage source (AUTO or HUMAN), model version, confidence of the type prediction. Note text up to 500 characters.

**Volumes:** on average 5,000 to 6,000 claims per month in scope, peaks up to three times that after a storm or a hail event. The Logic Apps flow processes claims one by one, so even at peak we stay well below 10 calls per second. We will throttle on our side to 5 per second to be safe.

**Identity:** the workload identity for the orchestration flow in our spoke has been created by the Fortalis cloud team. Its ID is in the attached sheet.

**Testing:** we would like to run a load test with you in October before UAT ends. Let's plan a date in September.

Thanks for the quick reaction, and enjoy the summer.

Jonas
