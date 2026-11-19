# Data Profiling Note: Asset Register Extracts

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Asset Management Agent |
| **Date** | 2026-02-20 |
| **Author** | Ruben Wouters, Developer, Kestrel Consulting |
| **Document type** | Data quality note |
| **Reviewed by** | Pieter De Smet, Kevin Hermans |

## 1. Purpose

Sprint block 1 includes a short profiling of the asset data, because data quality was flagged as a known risk in the SOW. Kevin Hermans provided two extracts on 2026-02-12, one from each legacy system that feeds the asset register:

- **System A**, the older maintenance management system, used for pumps, reservoirs and stations, and historically also for network assets.
- **System B**, the network asset inventory, introduced later for mains, valves and hydrants.

The combined asset register is a view on top of both. Read access to that view was not yet available at the time of profiling, so each extract was profiled separately in a Python notebook.

## 2. Volumes

| | System A | System B |
|---|---|---|
| Asset records | 38,400 | 61,900 |
| Of which status "in service" | 29,100 | 57,300 |
| Asset types used | 14 codes | 9 codes |
| Records with maintenance history | 22,600 | 18,200 |
| Oldest record | 1994 | 2009 |

## 3. Findings

### F-1: Asset type codes differ between systems

System A uses codes like `VAL-PRV`, System B uses `PRV` and `VALVE-RED` for what seem to be the same thing. A mapping table is needed before the agent can answer "show all pressure-reducing valves in zone X". Draft mapping with 31 rows in annex 1, to be confirmed by the asset data team.

### F-2: Missing or rough coordinates

- System B: 8% of valves and hydrants have no coordinates, 3% have coordinates outside AquaNova's service area (probably swapped X and Y).
- System A: coordinates only on station level, not on individual assets.

This matters for a "find assets near location" tool.

### F-3: Status values are not reliable

In System A, 2,100 assets marked "in service" have no maintenance or inspection record in the last ten years. Some may have been removed without updating the status. Planners know this and "ignore the old ones".

### F-4: Free text in maintenance history

About 40% of System A maintenance entries have only free text, without structured cause or action. The agent can still show them, but cannot reliably count "how many repairs of type X".

### F-5: Asset IDs

Both systems use numeric IDs of similar length. Within each system, IDs are unique. **Overlap between the two systems has not been checked**, because the combined register view was not available. Kevin indicated that assets were migrated from System A to System B over several years and that both systems were in use during that time.

## 4. What this means for the agent

- Tools must tell the planner which system a record comes from.
- Answers about counts and lists of assets need caveats until F-1 and F-3 are addressed.
- F-5 must be checked as soon as the combined register view is accessible.

## 5. Recommendations

| # | Recommendation | Owner |
|---|---|---|
| 1 | Confirm asset type mapping (F-1) | Asset data team via KH |
| 2 | Report on coordinate outliers to the asset data team (F-2) | RW |
| 3 | Check ID overlap between systems once the register view is available (F-5) | RW |
| 4 | Show source system in every tool answer | RW |

## 6. Time spent

About four days, within the profiling estimate of sprint block 1.
