# Workshop Notes: Claims intake and triage process mapping

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | Workshop notes |
| **Date** | 2024-04-19 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Participants** | Laura Vermeulen; two senior claims handlers; one intake team lead; Amira El Idrissi; Thomas Maes |

## 1. Goal

Map how a claim moves from arrival to the first handler today, agree the definitions the model will learn (type, complexity, urgency) and identify where automation adds most value. Full day at the Fortalis office, with a long sheet of brown paper and too many sticky notes.

## 2. Current process (as-is)

1. **Arrival.** Claims arrive through three channels: the central intake mailbox (about half), the broker upload function (about a third), and the customer portal (the rest). Brokers often send the same claim by mail and upload, which creates duplicates.
2. **Registration.** An intake employee creates or finds the claim in the claims management system, links the policy and attaches the documents. Average 6 to 8 minutes per claim, much longer when the policy number is missing.
3. **Sorting.** The same employee opens the documents, decides the claim type and assigns a queue. For doubtful cases they ask a senior handler.
4. **Urgency.** Set by gut feeling. There is a flag "urgent" in the system, but each team uses it differently.
5. **First handler.** Picks the claim from the queue, often re-reads everything, and in about one in eight cases sends it back because it is in the wrong queue.

Observations from the handlers: the sorting step itself is quick for an experienced person; what costs time is opening and reading poorly scanned documents, and chasing missing policy numbers.

## 3. Definitions agreed

**Claim type (first release):** motor (own damage), motor (third party), fire, theft from home, theft of vehicle, other. "Other" is a legitimate answer and goes to the human triage queue.

**Complexity:** simple, standard, complex. Complex means: injury mentioned, more than one party, estimated amount above the threshold Laura's team uses today for expert involvement, or signs of litigation.

**Urgency:** three levels.
- **U1** - the customer cannot use their home or vehicle, or there is a risk of further damage (open roof, broken door lock).
- **U2** - normal handling within the service level.
- **U3** - no time pressure (for example, a minor scratch reported for information).

This replaces the "every fire claim is urgent" rule. Laura will confirm the definitions in writing; they will be captured as a scope clarification in the change log, without cost impact.

## 4. Where automation helps most

| Step | Automation potential | Comment |
|---|---|---|
| Duplicate detection across channels | High | Same policy, same date of loss, within 48 hours |
| Field extraction (policy number, date and place of loss, amount) | High | Biggest time saver for intake |
| Claim type | High for motor and theft, medium for fire | Fire claims often mix several damage types |
| Complexity | Medium | Injury mentions are hard to catch in free text |
| Urgency | Medium | Depends on details in the customer's description |

## 5. Pain points not in scope

- Poor scan quality from some brokers. Not solvable by the project; Laura will raise it with the broker account managers.
- Claims reported by phone and typed in by the call centre. These arrive in the system without documents and are excluded from the first release.

## 6. Action items

| Action | Owner | Due |
|---|---|---|
| Confirm type, complexity and urgency definitions in writing | LV | 2024-04-26 |
| Log definitions as scope clarification | TM | 2024-04-26 |
| Add duplicate detection rule to backlog | TM | 2024-04-22 |
| Use definitions in labelling guidelines | AE | 2024-05-24 |

*Thomas Maes*
