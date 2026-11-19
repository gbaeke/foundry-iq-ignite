# Policy Note: Identity, Access and Secrets on Customer Work

| | |
|---|---|
| **Organisation** | Kestrel Consulting (internal) |
| **Date** | 2026-04-17 |
| **Author** | Jonas Peeters, Cloud Platform Engineer |
| **Document type** | Internal security policy note, version 1.0 |
| **Approved by** | Lotte Willems |

## Purpose

More of our work now involves AI agents that read documents and call tools on customer systems. That raises the stakes on identity and access: an agent with too many rights is an attacker's dream. This note sets the minimum rules for how Kestrel colleagues handle identities, access and secrets in customer and internal environments. Customer policies that are stricter always take precedence.

## 1. Our own accounts

- MFA on every account, phishing-resistant methods where the customer supports them.
- Use the guest or member account the customer gives you, never a shared account. If a customer proposes a shared "kestrel" account, politely refuse and explain why.
- Privileged roles only through just-in-time activation, time-limited, with a reason. No standing owner rights on production subscriptions, also not "just for the duration of the project".
- When you leave an engagement, ask the customer to remove your access, and confirm it in writing. Put it in the handover checklist.

## 2. Workload identities

- Services authenticate with **managed identities** wherever the platform supports it. Keys and connection strings are the exception and need a written reason in the design document.
- One identity per workload and per environment. Never reuse the production identity in test.
- Role assignments in code (Bicep), with Microsoft Entra ID groups or workload identities as principals. The smallest built-in role that works; custom roles only when no built-in role fits.
- Review role assignments at every release: anything that was added "temporarily" is removed or justified.

## 3. Agents and tools

- A tool that acts on behalf of a user should use the **user's identity and rights** where possible, so the agent can never see or do more than the person asking.
- Where a technical identity is unavoidable, it gets read-only access by default, scoped to the data the tool needs. Write actions require explicit design approval from the customer's security officer.
- Log every tool call with the calling user, the tool, the parameters and the result status. Content in logs follows the data processing agreement.
- Agent permissions are part of the security review in sprint 1, together with the permission model of the source documents.

## 4. Secrets

- Secrets live in the customer's secrets vault, referenced at deployment or run time. Never in code, parameter files, notebooks, pipeline variables in plain text, or chat messages.
- Rotate on a schedule agreed with the customer, and immediately when someone with access leaves the team.
- If a secret is exposed, even in a private repository: report it to the engagement lead and the customer the same day, rotate it, and check the logs for use. Do not just delete the commit.

## 5. Guardrails with Azure Policy

On environments we build, the default policy set includes:
- deny public network access on data services where private access is available
- require diagnostic settings to the central log workspace
- audit resources using key-based authentication where identity-based access is supported
- allowed regions limited to the EU, unless agreed otherwise

Exemptions are in code, with an owner and an expiry date.

## 6. Personal devices and tools

- Customer code and data only on Kestrel-managed laptops.
- No customer content in consumer AI tools. Use the environments agreed with the customer.
- Browser password managers are not a secrets store for customer credentials.

## 7. Checklist for sprint 1

- [ ] Access for each team member requested with named accounts and least privilege
- [ ] Managed identities and role assignments defined in Bicep
- [ ] Agent and tool permissions reviewed with the customer's security officer
- [ ] Secrets in the customer's vault, rotation agreed
- [ ] Access removal included in the handover checklist

Questions: ask me in the "platform" channel, or directly.

Jonas
