# Workshop Notes: Next Phase Scoping

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Customs Document Extraction |
| **Date** | 2026-09-24, 09:00 to 12:30 |
| **Location** | Customs desk meeting room, terminal building B |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Workshop notes (scoping and prioritisation) |
| **Participants** | Jan Wouters (product owner), two senior customs agents, Pieter De Smet, Amira El Idrissi. Koen Verstraete joined for the last hour. |

## 1. Purpose

The statement of work foresaw a decision on phase 2 scope at the end of phase 1; since April the project continues per quarter. After a year in operation, Jan wanted to step back and look at which next steps bring the most value.

## 2. Candidate topics

The group listed eight ideas and scored them on value for the desk, effort and dependency on other parties.

| # | Topic | Value | Effort | Dependency |
|---|---|---|---|---|
| A | Pre-fill the customs declaration from the validated export | High | High | Declaration system vendor |
| B | Risk-based validation: sample checks instead of full validation for high-scoring document types | High | Medium | Internal compliance, customs authority comfort |
| C | Priority by vessel departure and truck appointment | Medium | Medium | TOS data, new security review |
| D | More document types (credit notes, inspection reports) | Medium | Low | None |
| E | Haulier self-service upload portal | Medium | High | New intake channel, security review |
| F | Cross-document checks (invoice vs. packing list vs. weighing) | Medium | Low | None |
| G | eCMR intake from large hauliers | Medium | Medium | Hauliers' eCMR platforms |
| H | Fully automatic release without human validation | — | — | Not considered: Jan excludes it |

## 3. Discussion

**A. Pre-filling declarations.** The agents' strongest wish: today they still copy values from the export into the declaration screens. The declaration system vendor offers an import interface, but nobody at Scaldis has used it. Lesson from earlier projects with vendor-managed systems: get a direct technical contact at the vendor from the start. Jan will request one through Scaldis IT before we estimate anything.

**B. Risk-based validation.** Packing lists and certificates of origin have more than 80% of documents with zero corrections. Jan is open to sample checks for those types, but only after a pilot with double validation for a period, and after internal compliance agrees. "Customs mistakes are our licence, not just a cost."

**C. Priority feed.** Koen confirmed that any connection to the TOS needs its own architecture and security review.

**D and F.** Cheap and useful. Cross-document checks would catch most gross weight conflicts that agents now spot by eye.

**G. eCMR.** Jan reported on his talks with the five largest hauliers: two already use eCMR and could send structured data instead of a PDF. That would remove most handwriting problems for their volume. It needs a technical exchange with their platforms.

## 4. Decisions

1. **Q4 continuation** focuses on: risk-based validation pilot for packing lists (B), cross-document checks (F), and a feasibility study with the declaration system vendor (A), without building the integration yet.
2. **eCMR (G)** is explored with the two hauliers in Q4 as a study; no intake channel is built without a security review.
3. **Priority feed (C)** and **haulier portal (E)** are parked until a decision on A.
4. **More types (D)** only on request of the desk, within the quarterly capacity.
5. No change to the principle that every document is validated by a person, except for the controlled pilot under B.

## 5. Koen's remarks

Koen supports the direction and repeated that he prefers quarterly decisions. He asked for one page per quarter showing desk effort saved, accuracy and cost, "so I can defend it at the executive committee without a slide deck".

## 6. Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Request technical contact at declaration system vendor | JW via Scaldis IT | 2026-10-09 |
| 2 | Pilot design for risk-based validation of packing lists | AE, JW | 2026-10-16 |
| 3 | Consult internal compliance on sample checks | JW | 2026-10-16 |
| 4 | Q4 continuation proposal with deliverables | LW, PDS | 2026-10-02 |
| 5 | eCMR technical exchange with two hauliers | JW, AE | 2026-11-13 |

Pieter De Smet
