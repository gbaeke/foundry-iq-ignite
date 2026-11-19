# Steering Committee Minutes: Phase 1 Review

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Customs Document Extraction |
| **Date** | 2026-04-16, 14:00 to 15:15 |
| **Location** | Scaldis HQ Antwerp, meeting room "Kaai 3" |
| **Author** | Lotte Willems, Managing Partner, Kestrel Consulting |
| **Document type** | Steering committee minutes |

## Attendees

Koen Verstraete (CIO, sponsor), Jan Wouters (Customs Coordinator, product owner), Lotte Willems (engagement lead), Pieter De Smet (architect), Amira El Idrissi (Lead AI Engineer).

## 1. Phase 1 review against the statement of work

Pieter presented the review. Summary:

| SOW item | Target | Result |
|---|---|---|
| Document types with custom models | At least 8 | **8** accepted: commercial invoice, packing list, CMR, certificate of origin, T1, bill of lading, dangerous goods declaration, EUR.1 |
| Intake workflow in Azure Logic Apps (mailbox and scanning station) | Yes | In production since 2026-02-02 |
| Validation screen | Yes | In use by all customs desk staff |
| Field-level accuracy measured per type on labelled test sets | Yes | Weighted accuracy 91.9% over eight types |
| Architecture and security review in sprint 1 | Yes | Done 2025-10-10, repeated before parallel run and production |

Jan added the desk's view: average handling time per supported document went from about 4.5 minutes of keying to about 1.8 minutes of validation. The Monday morning backlog has disappeared since February. One agent who was sceptical in October now trains new colleagues on the validation screen.

**Decision:** Koen and Jan accept phase 1 as delivered.

## 2. Open quality topic: CMR handwriting

Amira explained why CMR stays below the standard threshold: about four in ten CMR notes carry handwritten annotations in fields we extract, often on top of printed values. Field-level accuracy on CMR is around 85%. Critical fields are caught by routing, but agents spend more time on CMR than on any other type.

Koen asked whether hauliers could simply send digital CMRs. Jan: a few large hauliers already use eCMR, most do not, and Scaldis cannot impose it. He will start a conversation with the five largest hauliers anyway, outside the project.

## 3. Continuation

As agreed by mail in March, continuation is per quarter on the same time and materials basis. Q2 deliverables, as prioritised by Jan:

1. New types: delivery orders (generic) and weighing certificates, then the customs warehouse release note and arrival notice if time allows
2. Routing of uncertain critical fields (HS code, gross weight, container number) to a senior agent instead of the general queue
3. Source crop next to each field in the validation screen, requested by the agents
4. Analysis of CMR handwriting options, to be presented in June

Capacity: Amira about four days per week, Pieter about one and a half days per week.

**Decision:** Q2 continuation approved by Koen. Q3 to be decided in June, with the summer peak in mind.

## 4. Cost and operations

- Azure consumption for Document Intelligence and Logic Apps stays within the monthly envelope. Dropping "terms and conditions" pages before extraction reduced the page count by about 18%.
- Koen asked who runs the pipeline when Kestrel is not around. Pieter proposed a runbook and a short handover to Scaldis IT operations in May, so that first-line monitoring sits with Scaldis.

## 5. Planning and holidays

- Easter holidays: reduced desk staffing, no impact on the sprint plan.
- Summer: Jan's team is smallest from mid-July to mid-August, while volumes peak. Planning for Q3 must keep deployments away from the last two weeks of July.

## 6. Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Q2 deliverables and capacity in writing | LW | 2026-04-21 |
| 2 | Runbook and first-line handover to Scaldis IT operations | PDS | 2026-05-08 |
| 3 | Contact five largest hauliers about eCMR | JW | 2026-05-29 |
| 4 | CMR handwriting options for June steering committee | AE | 2026-06-04 |
| 5 | Q3 continuation proposal | LW | 2026-06-26 |

*Minutes by Lotte Willems*
