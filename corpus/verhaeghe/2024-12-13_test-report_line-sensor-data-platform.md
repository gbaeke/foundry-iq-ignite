# Acceptance Test Report: Batch Quality Report, Shift Report and Alert Rules

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Line Sensor Data Platform |
| **Date** | 2024-12-13 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | User acceptance test report |
| **Test period** | 2024-12-02 to 2024-12-12 |
| **Testers** | Dries Callens, two quality technicians, one shift leader per shift |

## 1. Scope

This test covers the insight phase deliverables:

- Batch quality report (all six lines)
- Shift report (energy per tonne, reject rate, stops)
- Eight alert rules on blancher and freezer tunnel ranges, frozen sensors and gateway status

The underlying platform (Azure IoT Hub ingestion, Microsoft Fabric lakehouse, Databricks jobs) was accepted with the platform phase on 2024-11-29 and is not retested here.

## 2. Test approach

The quality team used a list of 34 test cases, written together with Dries in November. Each case is a real question from daily work, with the expected answer taken from paper logs or HMI screens. For alerts, we compared every alert sent during the test period with the HMI alarm history and the shift log.

## 3. Results

| Area | Cases | Passed | Passed after fix | Open |
|---|---|---|---|---|
| Batch quality report | 16 | 13 | 3 | 0 |
| Shift report | 10 | 8 | 1 | 1 |
| Alert rules | 8 | 6 | 2 | 0 |
| **Total** | **34** | **27** | **6** | **1** |

### Findings fixed during the test

- **B-04:** batches that ran over a shift change appeared twice in the shift report. Fixed: a batch is assigned to the shift in which it started, with a split view on request.
- **B-09:** freezer core temperature showed the wrong product target for two new product codes. The product master was updated by the quality team.
- **B-11:** the paper log number was empty for line 6 batches. The column name differs in the line 6 planning export; mapping corrected by Bram.
- **A-03 and A-06:** the "gateway offline" rule fired during planned weekend stops. A maintenance calendar is now checked before the alert is sent.
- **S-07:** reject rate for line 2 counted test packs from the checkweigher calibration. Excluded via the reject reason code.

### Open finding

- **S-10:** energy per tonne on line 5 is about 8% higher than the plant energy report. Probably one sub-meter is counted twice. To be checked with maintenance in January. Not blocking.

## 4. Alert rule results

During the test period the eight rules produced 41 alerts. 36 were confirmed as real deviations by the shift leaders, 5 were caused by planned stops (fixed under A-03/A-06).

One alert stood out. On 2024-12-10 at 03:40, the blancher water temperature on line 2 slowly drifted below its range after a steam valve problem. The alert reached the quality mailbox 12 minutes before the HMI alarm limit was reached. The night shift leader corrected the valve and no product had to be held. Dries called this "the first time the platform paid for itself".

## 5. Performance

- Batch quality report opens in about 4 seconds for a single batch and 9 seconds for a full week of one line.
- Alert latency from sensor value to e-mail is between 2 and 6 minutes. This is only possible because the alert tables run on a 5-minute cycle instead of the 15-minute resampling cycle.

## 6. Decision

Dries accepts the insight deliverables with one open, non-blocking finding (S-10). Alerts will be switched to the shift leaders on 2024-12-18, before the change freeze starting on 2024-12-20.

## 7. Next steps

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Switch alert recipients to shift leaders | SC | 2024-12-18 |
| 2 | Investigate S-10 with maintenance | JP | 2025-01-15 |
| 3 | Training sessions in January | SC | 2025-01-17 |
