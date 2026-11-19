# Steering Committee Minutes: Leak Detection Analytics

| | |
|---|---|
| **Customer** | AquaNova |
| **Project** | Leak Detection Analytics |
| **Date** | 2025-02-07, 10:00 to 11:30 |
| **Location** | AquaNova offices, Leuven |
| **Author** | Sofie Claes, Senior Data Engineer and project lead, Kestrel Consulting |
| **Document type** | Steering committee minutes |

## Attendees

Filip Wuyts (sponsor, chair), Evelien Claes (product owner), Koen Martens (OT), Lotte Willems (Kestrel), Sofie Claes (Kestrel), Amira El Idrissi (Kestrel)

## 1. Status

Sofie presented status report no. 5 and the two weeks since:

- SCADA history of zone Noord-Oost arrives daily in the Fabric lakehouse since 2025-01-13, via Koen's data diode export. 18 months of history loaded.
- Bram's monitoring on the nightly file drop is live since 2025-01-30. It alerts Koen and Sofie if the file is missing at 06:00 or has fewer rows than expected. No missing file so far.
- The GIS team has finished the corrections in Noord-Oost: 37 pipe segments with missing material or diameter corrected.
- Amira's first baseline anomaly results are due on 2025-02-21.

Overall amber, improving. Model phase about four weeks behind plan.

## 2. Re-planning

Sofie proposed to keep the field validation in April and May and the handover on 2025-05-30, by moving part of the model tuning into the pilot:

| Phase | Original | New |
|---|---|---|
| Model development | January to March | mid-January to end of March (compressed) |
| First model reviewed with Evelien | March | mid-March |
| Field validation | April to May | 2025-04-07 to mid-May, tuning continues during validation |
| Handover | 2025-05-30 | 2025-05-30 |

Filip agreed, on the condition that crews are not sent on "wild goose chases" in the first weeks. Amira proposed a short protocol with the crew leaders before the pilot starts.

## 3. Adding tags to the export

Koen reported on his action from January. Small changes to the tag list (adding or removing a few tags of already approved stations) can go through a standard OT change, approved by the OT manager within about a week, without a full OT security round. New stations or new types of data still need the full process. For the pilot, the tag list stays frozen.

Filip asked whether the pressure loggers that asset management plans to install in the second half of the year could be added this way. Koen: yes, if they are connected to an existing station.

## 4. Field crew capacity

Filip has booked two crew days per week in Noord-Oost from 2025-04-07 until 2025-05-16. The crew coordinator wants the candidate list by 07:30 on crew days.

## 5. Budget

About 49% of the fixed price used. Lotte confirmed that the delay is absorbed within the fixed price. No change request.

## 6. Ownership after the project

Evelien confirmed her GIS team will own the model and the ArcGIS layer after handover. She wants two GIS analysts trained, and asked that they run a retraining themselves before the project ends. Agreed.

## Decisions

1. New planning accepted; handover date unchanged.
2. Tag list frozen for the pilot.
3. Two GIS analysts will be trained, and will do one retraining on their own before handover.

## Action items

| # | Action | Owner | Due |
|---|---|---|---|
| 1 | Baseline anomaly model, first results to Evelien | AEI | 2025-02-21 |
| 2 | Field validation protocol with crew leaders | AEI / EC | 2025-03-28 |
| 3 | Name the two GIS analysts for handover | EC | 2025-02-21 |
| 4 | Written procedure for small tag list changes | KM | 2025-02-21 |

Next steering meeting: 2025-04-04.
