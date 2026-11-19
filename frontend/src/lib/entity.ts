/** Text colour per entity type, the same palette as the explainer. Unknown types (and xsd literals) stay muted. */
export const typeColor: Record<string, string> = {
  Person: 'text-person border-person',
  Project: 'text-project border-project',
  Organization: 'text-org border-org',
  Technology: 'text-tech border-tech',
  Place: 'text-place border-place',
}

/** Datatype properties (ontology v3) have an xsd: range: a text value, not an entity you can open. */
export const isLiteral = (type: string) => type.startsWith('xsd:')
