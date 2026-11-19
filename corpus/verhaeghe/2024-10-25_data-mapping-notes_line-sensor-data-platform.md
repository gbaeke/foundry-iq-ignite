# Data Mapping Notes: Linking Batches to Sensor Windows (Batch-Linking v2)

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Line Sensor Data Platform |
| **Date** | 2024-10-25 |
| **Author** | Bram Visser, Databricks Specialist, DataForge (subcontracted by Kestrel Consulting) |
| **Document type** | Data mapping note |
| **Reviewed by** | Sofie Claes, Dries Callens |

## 1. Purpose

The batch quality report needs, for every batch, the sensor data of the blancher and the freezer tunnel while that batch was on the line. Version 1 of the batch-linking job, reviewed with Dries on 2024-10-08, used only the batch start and end times from the production planning export. This note describes the mapping for version 2, which adds a fallback for late or missing entries.

## 2. Sources

| Source | Content | Refresh | Owner |
|---|---|---|---|
| Production planning export (CSV, daily) | batch number, product code, line, planned and actual start/end | daily at 05:30 | Planning, via Dries |
| Silver sensor table | 10-second values per tag, per line | every 15 minutes | Platform |
| Packaging counters | box counts per interval | every 15 minutes | Platform |
| Product master (spreadsheet, maintained by quality) | product code, blancher range, freezer core target | on change | Quality team |

## 3. Field mapping

| Target field (gold `batch_window`) | Source | Rule |
|---|---|---|
| `batch_id` | planning export `BATCH_NR` | trimmed, upper case; the export sometimes contains a trailing space |
| `line_id` | planning export `LINE` | mapped `L01`–`L06` to `1`–`6` |
| `product_code` | planning export `ART_NR` | joined to product master |
| `window_start` | `ACT_START`, else fallback | see section 4 |
| `window_end` | `ACT_END`, else fallback | see section 4 |
| `link_method` | derived | `planning`, `fallback_counter`, `fallback_shift` |
| `blancher_temp_min/mean/max` | silver, blancher water temperature | aggregated over window, offset by residence time |
| `freezer_core_exit_max` | silver, core probe at tunnel exit | aggregated over window, offset by tunnel time |

The offsets matter. Product leaves the blancher several minutes before it reaches the freezer exit, so each equipment section uses its own shifted window. Residence and tunnel times per product come from the product master.

## 4. Fallback rules

About 15% of batches have no actual start or end in the export at 05:30, because operators enter them at the end of the shift or the next morning. Version 2 handles this as follows:

1. **Planning times available:** use `ACT_START`/`ACT_END`.
2. **Missing actual time, packaging counters available:** a batch change shows as a stop in the box counter followed by a new product code on the checkweigher. The window is set between those changes.
3. **Neither available:** use the planned times, clipped to the shift. Marked `fallback_shift` and shown in grey in the report.

Batches are re-linked every night for the last seven days, so a late entry replaces the fallback automatically.

## 5. Data quality findings

- 23 batch numbers in four weeks were reused for two different products. Planning confirmed this is a typing error. These batches are flagged, not linked.
- Line 4 reports times in local time without daylight saving offset; the other lines are correct. Corrected in the mapping; a fix in the export is requested.
- The product master had two codes without a freezer core target. Dries' team added them.

## 6. Results on test data

On the four-week sample: 85% linked via planning, 12% via counters, 3% via shift fallback. Dries checked 20 batches by hand against the paper logs; all 20 windows were within two minutes of the paper times.

## 7. Next steps

- Deploy v2 as a scheduled Databricks job, target 2024-11-15.
- Daylight saving switch on 2024-10-27: check line 4 data on Monday.
- Add `link_method` as a filter in the batch quality report.
