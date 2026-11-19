# Run Book: Bed Capacity Dashboard

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Bed Capacity Dashboard |
| **Document type** | Run book (handover) |
| **Date** | 2023-11-10 |
| **Author** | Sofie Claes, Senior Data Engineer, Kestrel Consulting |
| **Audience** | Mediva IT, team of Jeroen Lambrecht |
| **Version** | 1.0 |

## 1. Components

| Component | Where | Purpose |
|---|---|---|
| ADT and bed status files | Landing folder delivered by the hospital information system every 15 minutes | Source |
| Synapse pipeline "pl_bed_state" | Production Azure Synapse Analytics workspace | Rebuilds the bed state of the last 72 hours on every new file |
| Synapse tables | bed_current, ward_aggregate, ward_outlook_24h, occupancy_daily, bed_unmapped | Model used by the reports |
| Power BI dataset "Bed Capacity" | Production workspace | Current state, outlook, 90 days of daily snapshots |
| Power BI reports | Campus overview, ward drill-down, outlook, large-screen ward view, A4 ward page | End-user reports |

## 2. Daily operation

Under normal conditions nothing needs to be done. Every new file triggers the pipeline, which triggers the dataset refresh. Expect about 96 runs per day, each 3 to 5 minutes.

**Morning check (service desk, 07:15):** open the campus overview and verify that the update time for all three campuses is less than 30 minutes old. If not, follow section 4.

## 3. Weekly and monthly tasks

| Task | Frequency | Owner |
|---|---|---|
| Compare occupied beds with the census count of the hospital information system | Weekly, Monday | Mediva IT |
| Review the bed_unmapped list and update the bed list | Monthly | Bed management office |
| Review "other" reasons for blocked beds, extend keyword list | Monthly | Bed management office |
| Check Synapse consumption and paused development resources | Monthly | Mediva IT |

## 4. Incidents

**4.1 Update time orange (no new data for 30 minutes).**
1. Check the landing folder: has a new file arrived? If not, contact the hospital information system team; the problem is upstream.
2. If files arrived, check the pipeline run history in Synapse. A failed run sends an alert to the service desk mailbox.
3. Restart the pipeline manually. Because each run rebuilds the last 72 hours, a missed run is caught up automatically; no data repair is needed.

**4.2 Dataset refresh failed but pipeline succeeded.** Start a manual refresh in the Power BI workspace. The reports keep showing the last good state in the meantime.

**4.3 Outage longer than one hour.** Inform the bed management office. As agreed at go-live, they return to the phone round until the dashboard is back.

**4.4 Large-screen view shows an old time or a sign-in page.** The device account has lost its session, usually after a password policy change or an operating system update on the ward PC. Sign in again with the ward device account; credentials are in the Mediva IT password safe.

## 5. Changes

**Adding a ward:** add the ward and its beds to the bed list table; add the ward code to the campus mapping; for the large-screen view, add the room order of the ward to the layout table. Full rebuild is not needed; the next run picks it up.

**Changing the outlook logic:** the 24-hour outlook uses the planned discharge date and, where available, the planned discharge time. The rule is in the stored procedure for ward_outlook_24h, with comments. Test changes in the development workspace with a copy of the last week of files.

**Upgrade of the hospital information system:** the upgrade of 7 October did not change the ADT format. For future upgrades, ask the vendor for a test file and run it through the development workspace before the upgrade weekend.

## 6. Large-screen ward view

After the two-week trial on an internal medicine ward on campus Centrum, Mediva IT ordered screens for the other wards; installation is planned ward by ward during November. Each screen uses a device account with read access to the page of its own ward only. The page refreshes with every dataset refresh.

## 7. Contacts

- Mediva IT: Jeroen Lambrecht and team
- Kestrel: best-effort support until the end of January 2024, via Lotte Willems
