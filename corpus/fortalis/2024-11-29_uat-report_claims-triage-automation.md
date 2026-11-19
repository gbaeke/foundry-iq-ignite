# UAT Interim Report: Claims Triage Automation

| | |
|---|---|
| **Customer** | Fortalis Verzekeringen |
| **Project** | Claims Triage Automation |
| **Document type** | User acceptance test report (interim) |
| **Date** | 2024-11-29 |
| **Author** | Thomas Maes, Project Manager, Kestrel Consulting |
| **Test lead (Fortalis)** | Laura Vermeulen, Claims Operations Manager |
| **Period** | 2024-10-07 to 2024-11-29 |

## 1. Summary

User acceptance testing is in its last week but one. Functional scenarios for motor, fire and theft are complete with no blocking findings. Water damage scenarios (CR-07) are 60% executed and on track for the closure date of 2024-12-06. One quality topic needs attention before go-live: the rising override rate in the live pilot since mid-November.

| Area | Status |
|---|---|
| Functional scenarios motor, fire, theft | Complete, accepted |
| Water damage scenarios | In progress |
| Integration with claims system | Accepted |
| Performance | Accepted after load test actions |
| Model quality in live pilot | Under analysis |

## 2. Test scenarios

| Group | Scenarios | Passed | Failed, minor | Failed, major | Not yet run |
|---|---|---|---|---|---|
| Intake channels (mailbox, broker upload, portal) | 18 | 18 | 0 | 0 | 0 |
| Duplicate detection | 9 | 8 | 1 | 0 | 0 |
| Extraction (claim form, repair quote, police report) | 26 | 24 | 2 | 0 | 0 |
| Classification and thresholds | 31 | 30 | 1 | 0 | 0 |
| Hard rules (injury, investigation, duplicates, "other") | 14 | 14 | 0 | 0 | 0 |
| Handler screen and overrides | 16 | 14 | 2 | 0 | 0 |
| Error handling and technical deferrals | 11 | 11 | 0 | 0 | 0 |
| Water damage (CR-07) | 22 | 12 | 1 | 0 | 9 |
| **Total** | **147** | **131** | **7** | **0** | **9** |

## 3. Minor findings

| # | Finding | Status |
|---|---|---|
| F1 | Duplicate not detected when the broker uses a different date of loss than the customer | Accepted as known limitation; documented |
| F2 | Repair quotes with two VAT rates: total amount extracted, VAT left empty | Accepted |
| F3 | Police report number misread when stamped over the text | Accepted; handlers check |
| F4 | Threshold change log did not show the approver name | Fixed 2024-11-21 |
| F5 | Override screen: urgency drop-down resets when type is changed | Fixed 2024-11-26 |
| F6 | Override comment limited to 200 characters | Raised to 500, fixed 2024-11-26 |
| F7 | Water damage: cause line missing when the plumber invoice is a photo | Open, workaround: handler reads the photo |

## 4. Model quality

**Acceptance sessions (October).** On claims reviewed by the senior handlers in the UAT sessions, the override rate was about 9%. This was the reference figure presented to the steering committee on 2024-10-17.

**Live pilot (from 2024-11-04).** The override rate on reviewed proposals:

| Week | Override rate |
|---|---|
| 1 (from 2024-11-04) | 10% |
| 2 (from 2024-11-11) | 13% |
| 3 (from 2024-11-18) | 16% |
| 4 (from 2024-11-25, partial) | 18% |

The increase is driven by claims related to the autumn storms: roof damage, fallen trees, water infiltration through storm damage. Volumes of these claims are much higher than in the historical data and their wording and document mix differ. Amira El Idrissi has started a structured analysis of the overrides; first results are expected in the week of 2024-12-09.

The figure is not a reason to stop the pilot: every proposal is still checked by a person. It is a reason not to switch on auto-routing until the override rate is back near the acceptance level.

## 5. Proposed conditions for UAT sign-off

1. All water damage scenarios executed with no major findings.
2. F7 either fixed or accepted with workaround by Laura.
3. Analysis of the pilot override rate presented, with a corrective action and a measured effect, before the go/no-go for auto-routing.

## 6. Next steps

| Action | Owner | Due |
|---|---|---|
| Complete water damage scenarios | Laura's team / TM | 2024-12-06 |
| Override analysis and corrective proposal | AE | 2024-12-13 |
| UAT sign-off (conditions 1 and 2) | LV | 2024-12-06 |
| Go/no-go for auto-routing | MD / LV | 2025-01-09 |

*Thomas Maes*
