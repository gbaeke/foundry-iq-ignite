# Lunch and Learn: Building a Teams Bot That People Actually Use

| | |
|---|---|
| **Organisation** | Kestrel Consulting (internal) |
| **Date** | 2025-04-25, 12:15 to 13:15 |
| **Location** | Kestrel office Ghent, big room, and Teams |
| **Author / presenter** | Ruben Wouters, Junior Developer |
| **Document type** | Internal session notes |

## Introduction

First kennisdeling session of 2025, and my first talk at Kestrel. Elien convinced me that a junior perspective is useful, so here it is: what I learned in three months of building the Teams bot front end for the **Scaldis Ops Copilot**. The copilot answers questions from terminal staff about SOPs and work instructions stored in SharePoint, using Azure AI Search for retrieval and Azure OpenAI to write the answer. My part is the bot in Microsoft Teams, the piece that users actually see.

## 1. Teams is the user interface, so respect Teams

Shift leaders at a terminal do not want a new app. They already live in Teams on a laptop in the office or on their phone on the quay. That is the whole reason for choosing a bot. But it also means users expect the bot to behave like a colleague in a chat:
- answer in the language of the question (Dutch, French or English at Scaldis)
- short first answer, details on request
- no walls of text on a phone screen

Elien and I paired on the answer layout. We ended up with a three-part card: the answer in at most five sentences, the source procedure with a link, and two buttons ("helpful" and "not helpful").

## 2. Always show the source

The single most appreciated feature in the pilot is the link to the SOP. Planners told us they do not mind if the bot is sometimes vague, as long as they can click through to the procedure and check. A bot without sources would not be trusted in an environment where a wrong procedure can mean a safety incident.

## 3. Things that cost me time

- **App policies.** The bot did not show up for some users because of the customer's Teams app setup policies. That is not a code problem; it needs the customer's Teams administrator. Ask for the app policy rules on day one.
- **Authentication.** Single sign-on in a Teams bot has more moving parts than I expected. Write down the consent and redirect settings per environment; you will forget them.
- **Timeouts.** Retrieval plus generation sometimes takes several seconds. Teams expects a fast response, so the bot first sends a typing indicator and then updates the message. Without it, users ask the same question twice.
- **Card features on mobile.** The mobile Teams client supports a slightly different set of features than desktop. Test on a phone early.

## 4. Logging and feedback

Every question and the feedback button click are logged, without the user's name, with the sources used and the response time. Pieter reviews the "not helpful" answers with Nathalie Dumont's team every two weeks. Most of the bad answers so far trace back to outdated or duplicate SOP versions, not to the model. It turns out that content quality is half of the job.

## 5. What I would tell another junior

1. Ask the customer's Teams administrator for a test tenant or a test policy in week one.
2. Build the feedback buttons in the first sprint, not the last.
3. Pair with UX. My first card design was technically correct and nobody liked it.
4. Read the existing documents. Half the questions users ask are already answered in an SOP; the other half show which SOPs are missing.

## Questions from the room

- *Can the bot be reused for other customers?* The front-end part, largely yes. We are keeping the card templates and the logging generic.
- *What about restricted procedures?* Pieter answered that one: content and access rules are being reviewed with the customer.

Thanks to Elien for the coaching and to everyone for the questions.

Ruben
