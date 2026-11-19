# Design Note: Read-Only Agent Tools on Asset Register and Maintenance History

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Asset Management Agent |
| **Date** | 2026-05-29 |
| **Author** | Ruben Wouters, Developer, Kestrel Consulting |
| **Document type** | Technical design note |
| **Reviewed by** | Pieter De Smet, Kevin Hermans |

## 1. Purpose

Define the tools that the agent in Foundry Agent Service can call to answer asset-specific questions. In the evaluation set, 22 of 60 questions need these tools (maintenance history, asset lookup, combined questions).

All tools are **read only**. They never write to the asset register or the maintenance history.

## 2. Tool list

| Tool | Question it answers | Priority |
|---|---|---|
| `get_asset_details` | "What is asset X, where is it, what type, what status?" | 1 |
| `get_maintenance_history` | "What was done on asset X, when and why?" | 1 |
| `find_assets_near_location` | "Which valves are within 200 m of this address?" | 2 |
| `get_open_inspection_findings` | "Which open findings exist for asset X or in zone Y?" | 3 |

Priorities agreed with the pilot coordinator on 2026-05-21.

## 3. Contracts

### get_asset_details

- **Input:** `asset_id` (string), optional `asset_type`.
- **Output:** ID, source system (A or B), type (mapped to the common type list), status, installation year, material and diameter (for network assets), coordinates, zone.
- **Behaviour:** if the ID is not found, return "not found" with the input echoed. Never guess a similar ID.

### get_maintenance_history

- **Input:** `asset_id`, optional `from_date`, `to_date`, `max_items` (default 10).
- **Output:** list of interventions: date, type, cause (if structured), free text (shortened to 300 characters), work order number.
- **Behaviour:** newest first. Free text is passed as is; the agent is instructed not to infer causes that are not written.

### find_assets_near_location

- **Input:** address or coordinates, `radius_m` (max 1,000), optional `asset_type`.
- **Output:** up to 25 assets with distance.
- **Behaviour:** assets without coordinates are not returned. The tool says how many assets of that type in the zone have no coordinates, so the planner knows the list may be incomplete (profiling finding F-2).

### get_open_inspection_findings

- **Input:** `asset_id` or `zone`.
- **Output:** open findings with severity and date.
- Design to be detailed once the inspection data view is available.

## 4. Implementation

- The tools are a small web service in AquaNova's subscription, reachable only over private connectivity, registered as tools of the agent in Foundry Agent Service with an API description.
- The service uses its own read-only service identity on the register and history views.
- Each call is logged with the planner's ID, the tool, the input and the response time. Logs are kept for 90 days, agreed with Kevin.
- Response time target: under 2 seconds per call.

## 5. Agent instructions for tools

- Use a tool when the question names an asset ID, address or zone.
- Always show the source system and the record date in the answer.
- Combine tool results with the knowledge base only when the question asks for it ("and what does the procedure say?").
- When a tool returns nothing, say so; do not fill in from documents about similar assets.

## 6. Test approach

- Unit tests per tool on the anonymised sample.
- End-to-end tests on the real register view once private connectivity is live.
- The asset-specific questions of the evaluation set, scored by two planners like the knowledge base questions.
- A check of ID overlap between systems A and B as soon as the combined register view is reachable (profiling finding F-5).

## 7. Open points

| # | Point | Owner |
|---|---|---|
| 1 | Geocoding of addresses: which AquaNova service to use | KH |
| 2 | Read access to the inspection findings view | KH |
| 3 | Confirm 90-day log retention with AquaNova's privacy officer | KH |
