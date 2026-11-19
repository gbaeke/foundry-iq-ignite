# Email thread: Water damage claims - scope and change request

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Email thread |
| **Date** | 2024-08-28 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Participants** | Thomas Maes, Laura Vermeulen, Marc Dubois, Amira El Idrissi |

---

**From:** Thomas Maes
**To:** Laura Vermeulen
**Cc:** Amira El Idrissi
**Date:** 2024-08-26 08:47
**Subject:** Water damage in the triage - before we go further

Hi Laura,

Welcome back. Following your question in the sprint 9 review and the demo on Friday, I want to be straightforward about where we are.

Amira looked at 50 plumber invoices and a handful of leak detection reports in sprint 10. The good news: the claim form extraction works for water damage claims as it is. The less good news: plumber invoices and leak detection reports need their own extraction models, and you asked on Friday for a severity level for water damage (is the damage spreading, is there mould, is the building still dry) that does not fit our current complexity scale. That means an extra labelling round and a separate sub-model, plus extra UAT scenarios.

This is a new claim type. Our agreement covers motor, fire and theft, and the contract says changes to the agreed claim types go through a formal change request approved by Marc. I should have said this already in the sprint 9 review instead of agreeing to "have a look". My apologies for that.

My proposal: we stop the water damage work now, I write an impact analysis this week with Amira and Jonas, and we submit a change request to Marc early next week. If he approves, we can run the water damage work in parallel with integration testing and probably keep the go-live window.

Thomas

---

**From:** Laura Vermeulen
**To:** Thomas Maes
**Cc:** Amira El Idrissi; Marc Dubois
**Date:** 2024-08-26 13:20
**Subject:** RE: Water damage in the triage - before we go further

Thomas,

Fair point, and I'd rather have this clear now than at the end. Adding Marc.

Marc, some context: water damage is now our largest growing claim category and the biggest share of what intake still sorts manually. Including it in the triage now instead of in a phase 2 would make a real difference for my team this winter. I support a change request.

Laura

---

**From:** Marc Dubois
**To:** Laura Vermeulen; Thomas Maes
**Cc:** Amira El Idrissi
**Date:** 2024-08-27 18:02
**Subject:** RE: Water damage in the triage - before we go further

Thomas, Laura,

Understood. Send me the change request with the cost and the planning impact. I want to see three things: what exactly is added, what it costs on top of the EUR 240,000, and whether January still holds. I'll decide within two weeks of receiving it.

Thomas, no need to apologise, but let's agree that from now on nothing new starts before it's on paper.

Marc

---

**From:** Thomas Maes
**To:** Marc Dubois; Laura Vermeulen
**Cc:** Amira El Idrissi; Jonas Peeters
**Date:** 2024-08-28 10:35
**Subject:** RE: Water damage in the triage - before we go further

Marc, Laura,

Agreed on all points. Planning:

- Impact analysis with Amira and Jonas: this week.
- Change request CR-07 submitted to Marc: Wednesday 2024-09-04.
- The water damage exploration is paused until a decision. The effort already spent in sprint 10 will be shown in the change request, so it is transparent.

First rough indication, to be confirmed in the CR: the extra effort is in the order of 15% of the fixed price, mostly ML and extraction work. Go-live in January looks feasible if the work runs in parallel with integration testing.

Thomas
