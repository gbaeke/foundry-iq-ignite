# Email thread: Hub IP plan approval and production window

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Fortalis Landing Zone |
| **Document type** | Email thread |
| **Date** | 2023-12-12 |
| **Author** | Jonas Peeters, Cloud Platform Engineer, Kestrel Consulting |
| **Participants** | Jonas Peeters, Kevin Hermans, Marc Dubois |

---

**From:** Kevin Hermans
**To:** Jonas Peeters
**Cc:** Marc Dubois
**Date:** 2023-12-06 17:42
**Subject:** Hub IP plan - change board outcome

Hi Jonas,

Good news and less good news. The network change board approved the IP plan this afternoon, including the reserved ranges for the second region. The annotated version did the trick; they mainly wanted to see that nothing overlaps with the ranges of the branch offices in Liège and Antwerp.

The less good news: the board wants the firewall rule base reviewed by their own team before the hub is connected to the datacentre. They can only do that review on 2023-12-14. That leaves one working day before the freeze starts on the 18th, which I don't like.

Can you give me your view on whether we push it in before the freeze or wait until January?

Kevin

---

**From:** Jonas Peeters
**To:** Kevin Hermans
**Cc:** Marc Dubois
**Date:** 2023-12-07 09:15
**Subject:** RE: Hub IP plan - change board outcome

Hi Kevin,

Thanks, that's a relief. My recommendation is to wait.

- Deploying the hub itself is low risk, but connecting it to the datacentre the day before a freeze is not. If something goes wrong with routing, nobody wants to debug that during the Christmas weeks.
- We can deploy the hub in production on 2023-12-14 or 15 without the datacentre connection. That part is fully inside Azure and doesn't touch on-premises routing.
- The connection to the datacentre, with the reviewed rule base, then goes live in the week of 2024-01-08.

The planning impact is small: the shared services spoke and the sandbox spoke can be built on the hub in January. I have enough buffer until the end of February.

Jonas

---

**From:** Marc Dubois
**To:** Kevin Hermans, Jonas Peeters
**Date:** 2023-12-07 11:03
**Subject:** RE: Hub IP plan - change board outcome

Fine for me. I prefer a quiet Christmas over a heroic one. Go with Jonas' proposal and keep me posted only if the January date moves.

Marc

---

**From:** Kevin Hermans
**To:** Jonas Peeters
**Date:** 2023-12-12 16:20
**Subject:** RE: Hub IP plan - change board outcome

Jonas,

Confirmed with the network team: rule base review on the 14th as planned, datacentre connection booked as a standard change for Tuesday 2024-01-09, 07:00. They want someone from Kestrel available that morning, so please be on site.

For the hub deployment on the 14th: the cloud team lead will approve the production pipeline run. Please share the what-if output beforehand so the network team sees exactly what gets created.

Kevin

---

**From:** Jonas Peeters
**To:** Kevin Hermans
**Date:** 2023-12-12 17:05
**Subject:** RE: Hub IP plan - change board outcome

Noted. What-if output will be in the pull request tomorrow morning, I'll send you the link. I'll be in Brussels on the 9th from 06:30.

Jonas
