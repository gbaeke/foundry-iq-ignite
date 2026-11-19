# Workshop Notes: Letter Templates per Specialty

| | |
|---|---|
| **Customer** | Mediva Care Group |
| **Project** | Discharge Letter Summarisation |
| **Document type** | Workshop notes |
| **Date** | 2024-04-26, 12:30 to 14:00 (lunch session) |
| **Location** | Mediva, campus Centrum, seminar room internal medicine |
| **Author** | Amira El Idrissi, ML Engineer, Kestrel Consulting |

## Participants

Four physicians from internal medicine (two staff members, two assistants), three from geriatrics (two staff, one assistant), a medical secretary from geriatrics, Dr. Hilde Van Damme (first half hour), Pieter De Smet and Amira El Idrissi (Kestrel).

## 1. Goal

Agree on the structure of the draft letter per specialty, and on what the draft should and should not contain. We used 20 historical letters per department, viewed through the pseudonymised flow, as examples.

## 2. What a good letter looks like

The group agreed that the general practitioner reads the letter in under two minutes and is looking for four things: why the patient was admitted, what was done, what changed in the medication, and what the GP needs to do next. Everything else is secondary.

Common structure, both departments:

1. Reason for admission (two or three sentences)
2. Relevant history (short, only what matters for this stay)
3. Course of stay (per problem, not per day)
4. Key results (lab, imaging, only abnormal or decisive results)
5. Medication at discharge, with changes marked: started, stopped, dose changed, with reason
6. Follow-up: appointments, instructions for the GP, pending results

## 3. Differences per specialty

**Internal medicine**
- Course of stay per problem is essential; multi-problem stays are common.
- Pending results must be explicit ("culture result pending, will be communicated").

**Geriatrics**
- Functional status at admission and discharge (mobility, cognition, falls) is a mandatory paragraph.
- Discharge destination (home, home with care, rehabilitation, residential care) and the care arrangements.
- Social context matters more. We explained that relatives' occupations and place names are removed by pseudonymisation; the physicians accepted completing that part themselves.
- The medical secretary pointed out that geriatric letters often include a list of involved disciplines (physiotherapy, occupational therapy, dietitian, social worker). Added as an optional section.

## 4. What the draft must not do

- Invent findings or results that are not in the source. Every statement should be traceable to a section.
- Write the diagnosis more firmly than the notes do. "Suspected" must stay "suspected".
- Give advice to the GP that the treating physician has not written somewhere.
- Use English terms where Dutch is usual. Letters are in Dutch; drug names follow the Belgian product names as recorded.

## 5. Medication changes

Both departments rated the medication section as the most time-consuming part to write today: comparing the medication at admission with the discharge list and finding the reason for each change in the notes. This is where the draft can save the most time. Pieter explained that the comparison of the two lists is done in code before the model is called, so the model only has to find and phrase the reason. Physicians liked that the list itself is not "generated".

## 6. Length

Current letters range from half a page to four pages. The group asked for a target of one page, with the course of stay as the paragraph that may grow for long stays. One staff member warned that a draft which is too long will just be deleted.

## 7. Agreements

- Template v1 per specialty based on the structure above, by 2024-05-03.
- Every draft paragraph shows which source sections it is based on in the review screen.
- Medication comparison deterministic in code; model writes the reasons only.
- Target length one page.

## 8. Next session

Review of the first drafts on historical stays, 2024-05-24, same group.
