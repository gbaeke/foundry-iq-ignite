# Engineering Guideline: Bicep Conventions

| | |
|---|---|
| **Organisation** | Kestrel Consulting (internal) |
| **Date** | 2023-11-10 |
| **Author** | Jonas Peeters, Cloud Platform Engineer |
| **Document type** | Engineering guideline, version 1.0 |
| **Applies to** | All infrastructure-as-code written by Kestrel |

## Why this guideline

Bicep is our standard for infrastructure as code on Azure. Until now every project had its own style, which makes handover to customer IT teams harder and makes it difficult to reuse modules. This guideline sets the minimum conventions. It is short on purpose; where it is silent, use common sense and the existing modules in the internal template repository.

## 1. Repository layout

```
infra/
  main.bicep            # entry point per environment scope
  main.<env>.bicepparam # one parameter file per environment
  modules/              # project-specific modules
  shared/               # copied from the internal template, do not edit in place
```

- One `main.bicep` per deployment scope (subscription or resource group). Do not mix scopes in one file.
- Shared modules are copied with a version tag in the header comment. If you improve one, contribute it back to the template repository.

## 2. Naming

- Resource names follow `<type>-<workload>-<env>-<region>-<nn>`, for example `vnet-hub-prd-weu-01`. Type abbreviations follow the list in the template repository.
- Customers often have their own naming standard. **Theirs wins.** Put the naming logic in one module (`naming.bicep`) so it can be swapped.
- Parameters and variables in camelCase, no abbreviations except the usual ones (`env`, `rg`, `vnet`).

## 3. Parameters

- Every parameter gets a `@description`. Use `@allowed` for environment and SKU parameters.
- No secrets in parameter files, ever. Reference them at deployment time from the customer's secret store.
- Defaults only for values that are truly the same in every environment.

## 4. Identity and access

- Role assignments are part of the code, not clicked in the portal afterwards. Use Microsoft Entra ID groups as principals, not individual users.
- Prefer managed identities for service-to-service access. A connection string with a key is an exception that needs a comment explaining why.
- Use `guid()` with stable inputs for role assignment names so redeployments are idempotent.

## 5. Policy as code

Governance rules belong in Azure Policy definitions and assignments, deployed from the same repository as the infrastructure. On the **Fortalis Landing Zone** engagement, which is running now, the hub-spoke landing zone is set up exactly this way: policy definitions, initiatives and assignments are all in Bicep, versioned and reviewed like any other code. Exemptions are also in code, with an expiry date and a reason. That makes the yearly governance review a matter of reading a pull request history instead of a portal hunt.

Default policy set for new environments (adapt per customer):
- allowed regions (EU only, unless agreed otherwise)
- mandatory tags: `owner`, `costCenter`, `environment`, `workload`
- deny public IP addresses on network interfaces in spokes
- diagnostic settings to the central log workspace

## 6. Deployment

- Deploy through a pipeline with a what-if step before every apply. The what-if output is attached to the pull request.
- Production deployments require a second reviewer and are never done from a laptop.
- Use named, tagged deployments so it is clear which deployment created which resource.

## 7. Linting and review

- The Bicep linter runs with our shared configuration; warnings are treated as errors in the pipeline.
- Every module has a short README with inputs, outputs and an example.
- Review checklist: naming, tags, identity, network exposure, diagnostics, cost.

## Questions

Ask in the "platform" channel in Teams. Proposals to change this guideline are welcome via a pull request on the template repository.

Jonas
