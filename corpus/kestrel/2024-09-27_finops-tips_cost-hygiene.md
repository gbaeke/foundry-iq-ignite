# FinOps Tips: Cost Hygiene on Customer and Internal Subscriptions

| | |
|---|---|
| **Organisation** | Kestrel Consulting (internal) |
| **Date** | 2024-09-27 |
| **Author** | Jonas Peeters, Cloud Platform Engineer |
| **Document type** | Internal guideline (FinOps tips, part 1) |

## Why this note

Twice this year a customer asked us, a bit pointedly, why their development environment cost more than production. Both times the answer was idle compute left running by the project team. Nobody was careless on purpose; it is just easy to forget. Below are the habits I want every project to follow. None of them take more than a few minutes.

## 1. Tag everything from day one

Every resource carries at least `owner`, `costCenter`, `environment` and `workload`. Our Bicep templates set these by default and the policy set denies untagged resources in new environments. Tags are what make a cost report readable for the customer's finance team. Without them, every cost review starts with "what is this?".

## 2. Budgets and alerts per environment

- Create a budget per resource group or subscription for each environment, at the start of the project.
- Alerts at 50%, 80% and 100% of the monthly budget, sent to the engagement lead and to a customer contact.
- The first alert is not a crisis. It is a reason to look.

## 3. Switch it off

The biggest savings are always the same:
- **Compute instances and notebooks**: configure idle shutdown (30 to 60 minutes) on every personal compute instance.
- **Spark clusters**: auto-termination after 20 to 30 minutes of inactivity, and a cluster policy that limits node types and the maximum number of workers in development. Nobody needs a 16-node cluster to test a notebook.
- **Capacity-based services**: if the service can be paused, schedule a pause outside working hours and at weekends in development and test.
- **Virtual machines** for jump hosts or tooling: auto-shutdown at 19:00.

On one platform this summer, auto-termination plus a smaller default node type cut the development compute bill by more than half, without anyone noticing a difference in their work.

## 4. Right-size after the first month

Start small, measure, then scale. After the first month of real use, review SKUs, tiers and reserved capacity with the customer. Production sizing based on a guess in the proposal is almost always too big or too small.

## 5. Storage is cheap until it is not

- Set lifecycle rules on raw landing storage: move to cool tier after 30 days, archive or delete according to the agreed retention.
- Delete test extracts and temporary tables at the end of each sprint.
- Watch log retention. Diagnostics to a central workspace are good; keeping verbose logs for two years by default is not.

## 6. Make cost visible in the status report

Add one line to the biweekly status report: cloud cost this period versus budget, per environment. Customers appreciate it, and it stops surprises at the end of the quarter.

## 7. Internal subscriptions

Our own sandbox subscriptions follow the same rules. I run a cost check every month and send a list of the top ten resources. If your name is on it, either explain why or switch it off.

## Checklist for the first sprint

- [ ] Tags in place, policy assigned
- [ ] Budgets and alerts configured
- [ ] Idle shutdown on personal compute
- [ ] Auto-termination and cluster policy in development
- [ ] Cost line in the status report template

Part 2, on cost of AI workloads, follows later.

Jonas
