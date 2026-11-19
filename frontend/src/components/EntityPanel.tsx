import { useQuery } from '@tanstack/react-query'
import { ArrowLeft, ArrowRight } from 'lucide-react'
import { useMemo } from 'react'
import type { Edge } from '@/client'
import { getEntityOptions } from '@/client/@tanstack/react-query.gen'
import { TypeBadge } from '@/components/TypeBadge'
import { errorMessage } from '@/lib/api'
import { isLiteral } from '@/lib/entity'

/** One row per related entity (or text value): every triple that says the same thing becomes one of its sources. */
type Relation = { edge: Edge; sources: { file: string; snippet: string }[] }

export function EntityPanel({ graph, id, open }: { graph: string; id: string; open: (id: string) => void }) {
  const detail = useQuery(getEntityOptions({ path: { graph_id: graph }, query: { id } }))
  const groups = useMemo(() => {
    const byPredicate = new Map<string, Map<string, Relation>>()
    for (const e of detail.data?.edges ?? []) {
      const key = `${e.direction === 'out' ? '→' : '←'} ${e.predicate}`
      const rels = byPredicate.get(key) ?? new Map<string, Relation>()
      const target = e.other_id && !isLiteral(e.other_type) ? e.other_id : e.other_name
      const rel = rels.get(target) ?? { edge: e, sources: [] }
      if (e.source_file && !rel.sources.some((x) => x.file === e.source_file))
        rel.sources.push({ file: e.source_file, snippet: e.snippet })
      rels.set(target, rel)
      byPredicate.set(key, rels)
    }
    return [...byPredicate.entries()]
      .map(([key, rels]) => [key, [...rels.values()].sort((a, b) => b.sources.length - a.sources.length)] as const)
      .sort((a, b) => b[1].length - a[1].length)
  }, [detail.data])

  if (detail.isPending) return <div className="card text-fg-muted">Loading…</div>
  if (detail.isError) return <div className="card text-danger">{errorMessage(detail.error)}</div>
  const d = detail.data
  return (
    <div className="card max-h-[70vh] space-y-4 overflow-auto">
      <header className="space-y-1">
        <div className="flex flex-wrap items-center gap-2">
          <h2 className="text-lg font-semibold">{d.name}</h2>
          <TypeBadge type={d.type} />
        </div>
        <p className="font-mono text-xs text-fg-muted">{d.id}</p>
        {d.names.length > 1 && <p className="text-xs text-fg-muted">Also written as: {d.names.slice(1).join(' · ')}</p>}
        <p className="text-xs text-fg-muted">
          {d.edges.length} triple(s) · {groups.reduce((n, [, rels]) => n + rels.length, 0)} distinct relationship(s)
        </p>
      </header>
      {groups.map(([key, rels]) => (
        <section key={key} className="space-y-1.5">
          <h3 className="font-mono text-xs text-accent">
            {key} <span className="text-fg-muted">({rels.length})</span>
          </h3>
          <ul className="space-y-1">
            {rels.map(({ edge: e, sources }, i) => (
              <li key={i} className="rounded-md border border-border p-2 text-xs">
                <div className="flex flex-wrap items-center gap-2">
                  {e.direction === 'out' ? (
                    <ArrowRight className="size-3.5 text-fg-muted" />
                  ) : (
                    <ArrowLeft className="size-3.5 text-fg-muted" />
                  )}
                  {isLiteral(e.other_type) || !e.other_id ? (
                    <span>{e.other_name}</span>
                  ) : (
                    <button
                      className="text-left underline decoration-border underline-offset-2 hover:decoration-accent"
                      onClick={() => open(e.other_id)}
                    >
                      {e.other_name}
                    </button>
                  )}
                  <TypeBadge type={e.other_type} />
                  {e.other_id && !isLiteral(e.other_type) && (
                    <span className="font-mono text-[10.5px] text-fg-muted">{e.other_id}</span>
                  )}
                </div>
                {sources.length > 0 && (
                  <details className="mt-1">
                    <summary className="cursor-pointer text-[11px] text-fg-muted">
                      {sources.length} source document{sources.length === 1 ? '' : 's'}
                    </summary>
                    <ul className="mt-1 space-y-1.5">
                      {sources.map((src) => (
                        <li key={src.file}>
                          <span className="font-mono text-[11px] text-fg-muted">{src.file}</span>
                          <p className="whitespace-pre-wrap text-fg-muted">{src.snippet}</p>
                        </li>
                      ))}
                    </ul>
                  </details>
                )}
              </li>
            ))}
          </ul>
        </section>
      ))}
    </div>
  )
}
