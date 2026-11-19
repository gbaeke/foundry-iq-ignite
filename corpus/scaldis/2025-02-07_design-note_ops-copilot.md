# Conversation Design Note: Answer Cards and Dialogue Flow

| | |
|---|---|
| **Customer** | Scaldis Logistics |
| **Project** | Scaldis Ops Copilot |
| **Date** | 2025-02-07 |
| **Author** | Elien Jacobs, UX and Frontend Developer, Kestrel Consulting |
| **Document type** | Design note |
| **Reviewers** | Nathalie Dumont, Pieter De Smet, Ruben Wouters |

## 1. Who we design for

Based on two mornings of shadowing on the terminal (28 and 30 January), three user groups:

| Group | Context | What they need |
|---|---|---|
| Shift leaders | Office and on the quay, phone in hand, interrupted every few minutes | Short, certain answers; who to call |
| Planners | Desktop, several screens, Teams always open | Exact steps, links to the full SOP |
| New operators and clerks | First months on the job, often on a shared PC in the gate building | Plain explanations, no jargon, reassurance |

Most questions observed were procedural ("what do I do when a reefer alarm goes off during a vessel operation?") and lookup ("which form for a damaged seal?"). Almost nobody asked open questions.

## 2. Principles

1. **Answer first, source always.** The first two lines answer the question. The source link is never optional.
2. **Same language as the question.** Dutch, French or English, detected per message. The source may be in another language; the card then says so.
3. **Short on mobile.** Maximum about 80 words in the card body; "show steps" expands the full procedure.
4. **Never pretend.** If the retrieved passages do not answer the question, the bot says it did not find it and offers the shift leader fallback. No general knowledge answers about terminal operations.
5. **Feedback in one tap.** Thumbs up/down, with an optional reason list on thumbs down.

## 3. Answer card layout (Microsoft Teams)

```
[Title of the SOP section]                       [language tag]
Answer in 1–3 sentences.

Steps (collapsed by default)
  1. ...
  2. ...

Sources: SOP-OPS-112 "Reefer alarms" §3.2  (opens in SharePoint)
         WI-GATE-031 "Damaged seals" §1

[Helpful]  [Not helpful]  [Ask the shift leader]
```

Mock-ups for desktop and phone are in the design folder. On phone, the steps open as a separate card to keep the first view readable.

## 4. Dialogue flow

1. User asks a question in a one-to-one chat with the bot (no group chats in release 1).
2. Bot shows a short "searching the procedures…" indicator if the answer takes more than 2 seconds.
3. Bot posts the answer card.
4. Follow-up questions keep the context of the last answer for 10 minutes.
5. "Ask the shift leader" opens a pre-filled message to the shift leader on duty, with the original question. The roster lookup is a simple list maintained by Nathalie's team; no integration with the planning system.

## 5. Tone of voice

- Use "you", short sentences, imperative for steps.
- Use the terminal's own words: "kade", "stack", "reefer plug", "lashing", even in English answers when that is what people say.
- No emojis, no "Great question!".

## 6. Accessibility and shared devices

Some gate building PCs are shared by several clerks. We assume a personal Teams login on those PCs; to be confirmed by Scaldis IT. Cards use the Teams theme colours so they stay readable in dark mode and high contrast.

## 7. Open questions

- Does Nathalie want a welcome message with example questions? (Proposal: yes, three examples per language.)
- Should answers mention the SOP version date? Pieter prefers yes, to make outdated documents visible.
- Do we show the source passage text, or only the link? To be tested with pilot users.

## 8. Next steps

| Action | Owner | Due |
|---|---|---|
| Clickable prototype of cards in the dev tenant | RW, EJ | 2025-02-21 |
| Test three card variants with four shift leaders | EJ | 2025-02-28 |
| Confirm login situation on shared gate PCs | Scaldis IT via ND | 2025-02-21 |

Elien Jacobs
