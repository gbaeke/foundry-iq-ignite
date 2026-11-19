# Runbook: Customs Document Extraction Pipeline (First Line)

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Customs Document Extraction |
| **Date** | 2026-05-08 |
| **Author** | Pieter De Smet, Lead AI Architect, Kestrel Consulting |
| **Document type** | Runbook |
| **Audience** | Scaldis IT operations (first line), customs desk coordinator |
| **Version** | 1.0, handed over in session of 2026-05-07 |

## 1. What the pipeline does

Documents arrive in the customs shared mailbox or the scanning station folder. An Azure Logic Apps workflow stores the original, calls the classifier and the composed extraction model in Azure AI Document Intelligence, checks values against reference lists and places the result in the validation queue. Customs agents validate every document. Nothing is sent to the declaration system automatically.

## 2. Daily checks (first line, 07:30)

| Check | Where | Normal | Action if not normal |
|---|---|---|---|
| Failed workflow runs overnight | Logic Apps run history, filter "Failed" | 0–3 | See 3.1 |
| Validation queue age | Queue dashboard on the validation screen | Oldest item < 30 min in office hours | Inform desk coordinator |
| Manual folder | Scanning share, folder "manual" | < 20 new items | Inform desk coordinator |
| Retention job | Last run status | Succeeded, ran at 02:00 | See 3.5 |

Alerts already mail the desk coordinator and Kestrel for failures longer than 30 minutes and for queue age above 30 minutes.

## 3. Procedures

### 3.1 Failed workflow run
1. Open the failed run and read the failing action.
2. **Extraction call returned "too many requests"**: the workflow retries four times with increasing delay. If it still fails, resubmit the run. If many runs fail, check whether a large batch arrived (for example 300 scans at once) and resubmit in groups of 50.
3. **Mailbox connection failed**: usually an expired or changed permission on the shared mailbox. Contact the Scaldis messaging team; do not grant broader permissions.
4. **Document unreadable or unsupported format**: the run moves the file to "manual" by design. No action.
5. Anything else: create a ticket for Kestrel with the run ID.

### 3.2 Queue growing during office hours
Usually a staffing issue, not technical. Check that the workflow is running (new items arriving). If yes, inform the desk coordinator. If no new items for 15 minutes during office hours, check the mailbox trigger and the scan folder connection.

### 3.3 Scanning station problems
Skewed or dark scans: the station must use the profile "Customs-CMR-single". Paper jams and hardware: scanner supplier, contract number on the station.

### 3.4 New model version
Model versions are deployed only by Kestrel (Amira El Idrissi) after Jan Wouters approves the test set results. First line does not change model IDs in the workflow. Rollback to the previous version: change the model ID parameter in the workflow to the previous tag listed in the model register. Takes five minutes.

### 3.5 Retention job failed
The job deletes images and extracted data 90 days after container release. One failed night is not urgent; three in a row is. Ticket for Kestrel.

## 4. Throughput tuning applied in April

During a peak on 20 April (about 900 documents in one morning after a mailbox outage at a forwarder), extraction calls were throttled. Changes since:
- concurrency of the extraction step limited to 8 parallel runs;
- retry policy with exponential back-off;
- classifier call and extraction call separated, so a throttled extraction does not repeat classification and cost.

Result: the backlog of 900 documents clears in about 40 minutes without failed runs.

## 5. Monthly retraining (for information)

First week of each month: Amira collects corrected documents from the previous month, adds new layouts to the training set after labelling checks, retrains, compares with the production version on the test sets and asks Jan for approval. First line only sees a model ID change in the workflow parameters.

## 6. Contacts

| Topic | Contact |
|---|---|
| Business priorities, approval of model versions | Jan Wouters, Customs Coordinator |
| Architecture, workflow changes | Pieter De Smet, Kestrel |
| Models, retraining, accuracy | Amira El Idrissi, Kestrel |
| Shared mailbox permissions | Scaldis messaging team |
| Scanner hardware | Scanner supplier (contract on station) |

Pieter De Smet
