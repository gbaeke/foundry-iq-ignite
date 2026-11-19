# Cutover Checklist: Inspection on Lines 5 and 6

| | |
|---|---|
| **Customer** | Verhaeghe Foods |
| **Project** | Quality Inspection Vision |
| **Date** | 2025-09-08 |
| **Author** | Jonas Peeters, Cloud Platform Engineer (edge engineer), Kestrel Consulting |
| **Document type** | Cutover and go-live checklist |
| **Go-live dates** | Line 5: Monday 2025-09-15 · Line 6: Monday 2025-09-22 |

## 1. Principles

- Lines 5 and 6 get exactly the setup that works on line 3: same camera type, same enclosure, same Azure IoT Edge deployment manifest with line-specific settings only.
- The system flags, the operator decides. Nothing changes in the reject procedure.
- Go-live happens at the start of the morning shift, with Jonas or Amira on the line until the end of that shift.

## 2. Checklist per line

### A. Hardware (done during Saturday stop before go-live)

| # | Item | Line 5 | Line 6 |
|---|---|---|---|
| A1 | Gantry mounted, camera at 80 cm above belt | ☑ | ☐ |
| A2 | Enclosure mounted, LED lighting on, side panel hinges checked | ☑ (2025-09-06) | ☐ (planned 2025-09-13) |
| A3 | Industrial PC in electrical cabinet, power and cooling checked | ☑ | ☑ |
| A4 | Operator screen next to the belt, at eye height | ☑ | ☐ |
| A5 | Hygiene team sign-off on enclosure (wash-down test) | ☑ | ☐ |

### B. Network and device management

| # | Item | Line 5 | Line 6 |
|---|---|---|---|
| B1 | PC in the OT segment approved in April (request by Tine) | ☑ | ☑ |
| B2 | Device registered and visible in central device management | ☑ | ☑ |
| B3 | Deployment manifest applied: capture, inference, upload, operator display modules | ☑ | ☐ |
| B4 | Offline test: pull network cable for 10 minutes, inspection continues, uploads catch up | ☑ | ☐ |

### C. Model and configuration

| # | Item | Line 5 | Line 6 |
|---|---|---|---|
| C1 | Model v3 deployed (or v2 as fallback) | v3 ☐ | v3 ☐ |
| C2 | Crop area set to belt edges (ADR-02) | ☑ | ☐ |
| C3 | Person/large object discard rule tested on 200 images | ☐ | ☐ |
| C4 | Per-class thresholds as on line 3 | ☑ | ☐ |
| C5 | Product list for the line loaded (line 6 runs carrots and mixes; check colour range for discolouration) | ☑ | ☐ |

### D. People

| # | Item | Line 5 | Line 6 |
|---|---|---|---|
| D1 | Shift leaders of all three shifts briefed by Dries | ☐ | ☐ |
| D2 | Laminated one-page "how to read a flag" at the operator screen | ☐ | ☐ |
| D3 | Operator feedback buttons explained (confirm / not a defect) | ☐ | ☐ |

## 3. Go-live day

1. 05:45 — Jonas on site, checks device status and live images before the shift starts.
2. 06:00 — shift starts, operator screen switched on.
3. 06:00–10:00 — Amira watches flags remotely and checks the first 100 flags with the shift leader.
4. 14:00 — short handover to the afternoon shift by the shift leader, with Jonas present.
5. End of day — first numbers (flags per hour, operator "not a defect" share) mailed to Dries.

## 4. Rollback

If the false positive rate is above 15% for two consecutive hours, or the operator screen disturbs the line, the operator display module is switched off from central device management. Capture and inference keep running so we can analyse. Rollback decision: Dries, or the shift leader if Dries is not reachable.

## 5. Line 6 notes

Line 6 is the oldest line; its cabinet is full, so the industrial PC sits in an extra cabinet next to it (approved by maintenance on 2025-09-03).

## 6. Hypercare

Two weeks per line: daily flag statistics by Amira, weekly review with Dries.
