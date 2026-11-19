# Handover and Training Notes: Line Sensor Data Platform

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Line Sensor Data Platform |
| **Date** | 2025-01-17 |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Handover notes |

## 1. Sessions held

| Date | Session | Audience | Trainer |
|---|---|---|---|
| 2025-01-14 | Platform operations and runbook | Tine Desmet and her deputy | Jonas |
| 2025-01-15 | Databricks jobs: how they run, how to rerun | Tine's deputy, one analyst from planning | Bram (remote from Utrecht) |
| 2025-01-16 | Batch quality report and shift report | Dries Callens, quality technicians, shift leaders | Sofie |
| 2025-01-17 | Alert rules and thresholds | Dries Callens, two quality technicians | Sofie |

## 2. Operations session (Tine)

Jonas walked through the runbook draft. Tine and her deputy simulated two incidents: a gateway on line 5 disconnected by pulling the network cable, and a missing planning export. Both were solved without help in under 20 minutes.

Questions raised:

- *Who renews the gateway device keys?* Tine, yearly, procedure in annex B.
- *What if the firewall partner changes something?* The firewall log is the first place to look. Tine asked the partner to notify her before any change to the gateway subnet rules.
- *Who pays for Azure and Fabric?* Verhaeghe, directly. Tine will set a monthly budget alert in the subscription. Current consumption is about EUR 1,150 per month, mostly Fabric capacity.

## 3. Report sessions (quality team)

The shift leaders already used the reports during the December test. The session focused on:

- Reading the `link_method` marking: grey batches are linked by shift fallback and must be checked by hand before they are used in a customer audit.
- Comparing shifts fairly: always filter on product code, because energy per tonne depends heavily on the product.
- Finding a batch from a customer complaint: batch number, or product code plus production date.

Feedback: the shift leaders asked for a printable one-page view per batch for the audit file. Sofie added it the same afternoon.

## 4. Alert rules (Dries)

Dries is the owner of the thresholds. Agreed rules for changes:

1. A threshold changes only after a two-week trial in the quality mailbox.
2. Every change is written in the "alert changes" log in the workspace.
3. New rules are a change request after handover.

## 5. Open items at handover

| # | Item | Owner | Status |
|---|---|---|---|
| 1 | S-10: line 5 energy sub-meter counted twice | Jonas with maintenance | fixed 2025-01-13 |
| 2 | Runbook version 1.0 with Tine's comments | Jonas | due 2025-01-24 |
| 3 | Remove the last unused tags of line 6 from silver | Sofie | due 2025-01-24 |
| 4 | Guest accounts of Kestrel and DataForge removed | Tine | 2025-02-28 |

## 6. Ownership after handover

- Platform and access: Tine Desmet
- Reports and thresholds: Dries Callens
- Final acceptance: Ann Verhaeghe, planned at the steering meeting of 2025-01-29
