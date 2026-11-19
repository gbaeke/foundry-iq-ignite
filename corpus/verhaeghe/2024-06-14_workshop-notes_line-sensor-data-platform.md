# Workshop Notes: Quality Requirements and Tag Inventory

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Line Sensor Data Platform |
| **Date** | 2024-06-14 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Workshop notes (requirements) |
| **Participants** | Dries Callens, two quality technicians, the line 1 maintenance technician, Sofie Claes, Jonas Peeters, Bram Visser |

## 1. Purpose

Agree what the quality team needs from the platform first, and finish the tag inventory of line 1.

## 2. Quality questions, in order of priority

The team put sticky notes on the wall and voted. The top five:

1. "What was the core temperature at the freezer tunnel exit for batch X?" (audit question, asked weekly)
2. "Was the blancher within range for the whole batch?"
3. "Which batches ran during a stop or restart?" (restarts often give quality deviations)
4. "How do shifts compare on reject rate and energy per tonne?"
5. "Warn us when a blancher drifts, before product is affected."

Questions 1 to 3 need the link between sensor data and batch numbers. Bram noted that this link does not exist in any system today: the batch number lives in the production planning export, the temperatures live in the PLC.

## 3. Tag inventory line 1

With the maintenance technician we went through the PLC tag list and the HMI screens.

| Equipment | Tags kept | Typical frequency |
|---|---|---|
| Blancher (water temperature, residence time, belt speed) | 46 | 1 s |
| Cooling section | 22 | 1 s |
| Tunnel freezer (air temperature per zone, product core probe, fan speed) | 88 | 1 to 5 s |
| Packaging (counts, rejects, checkweigher) | 61 | per event |
| Energy meters | 18 | 15 s |

That gives 235 tags for line 1. About 40 tags in the PLC were not used any more or duplicated, and were left out. The PLC documentation was incomplete in places; the technician confirmed tag meanings from memory.

## 4. Data needs

- History of at least two seasons, as in the proposal.
- Raw data at source frequency in bronze; 10-second resampled data in silver (to be confirmed in an ADR by Bram).
- Batch-level aggregates in gold.
- Shift calendar: three shifts, 06:00, 14:00, 22:00. Weekend shifts differ in the campaign.

## 5. Privacy and works council

Dries checked with HR after the kickoff. Reports may show shift and team, not individual operators. The works council was informed that the platform does not monitor individual performance. We will not load the operator login field from the HMI.

## 6. Agreements

- First report: batch traceability for line 1 (questions 1 to 3).
- Alert rules come after the batch link works, in the insight phase.
- The quality team reviews every gold table definition before it goes live.

## 7. Open points

| # | Point | Owner |
|---|---|---|
| 1 | Sample of the production planning export for four weeks | DC |
| 2 | Confirm meaning of 12 unclear freezer tags | Maintenance technician |
| 3 | ADR on resampling frequency | BV |
| 4 | Tag inventory line 2 planned for 2024-06-27 | SC / JP |
