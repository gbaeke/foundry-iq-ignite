import { useQuery } from '@tanstack/react-query'
import { useState } from 'react'
import { useSearchParams } from 'react-router'
import { listEntitiesOptions, listGraphsOptions } from '@/client/@tanstack/react-query.gen'
import { EntityPanel } from '@/components/EntityPanel'
import { TypeBadge } from '@/components/TypeBadge'
import { errorMessage } from '@/lib/api'
import { cn } from '@/lib/utils'

const TYPES = ['Person', 'Project', 'Organization', 'Technology', 'Place', 'Issue', 'Outcome']

export function Explore() {
  const [params, setParams] = useSearchParams()
  const graph = params.get('graph') ?? 'grounded-v3'
  const selected = params.get('id')
  const [type, setType] = useState<string | null>(null)
  const [text, setText] = useState('')
  const graphs = useQuery(listGraphsOptions())
  const list = useQuery(
    listEntitiesOptions({
      path: { graph_id: graph },
      query: { type: type ?? undefined, q: text || undefined, limit: 300 },
    }),
  )
  const set = (next: Record<string, string | null>) => {
    const p = new URLSearchParams(params)
    for (const [k, v] of Object.entries(next)) {
      if (v) p.set(k, v)
      else p.delete(k)
    }
    setParams(p)
  }

  return (
    <div className="mx-auto max-w-[1400px] space-y-5">
      <div>
        <h1 className="text-xl font-semibold">Explore a graph</h1>
        <p className="text-fg-muted">
          Every entity, its name variants and relationships, and the passage each relationship came from.
        </p>
      </div>

      <div className="flex flex-wrap items-end gap-3">
        <label className="space-y-1">
          <span className="label">Graph</span>
          <select
            id="explore-graph"
            className="input w-56"
            value={graph}
            onChange={(e) => set({ graph: e.target.value, id: null })}
          >
            {graphs.data?.map((g) => (
              <option key={g.id} value={g.id}>
                {g.label}
              </option>
            ))}
          </select>
        </label>
        <label className="space-y-1">
          <span className="label">Find</span>
          <input
            id="explore-find"
            className="input w-56"
            placeholder="Name or id…"
            value={text}
            onChange={(e) => setText(e.target.value)}
          />
        </label>
        <div className="flex flex-wrap gap-1.5">
          {TYPES.map((t) => (
            <button
              key={t}
              type="button"
              aria-pressed={type === t}
              onClick={() => setType(type === t ? null : t)}
              className={cn(
                'rounded-full border px-2.5 py-1 text-xs',
                type === t ? 'border-accent bg-accent-soft text-accent' : 'border-border text-fg-muted hover:text-fg',
              )}
            >
              {t}
            </button>
          ))}
        </div>
      </div>

      <div className="grid gap-4 md:grid-cols-[320px_minmax(0,1fr)]">
        <div className="card max-h-[70vh] overflow-auto p-1">
          {list.isPending && <p className="p-3 text-fg-muted">Loading entities… the first load reads every triple.</p>}
          {list.isError && <p className="p-3 text-danger">{errorMessage(list.error)}</p>}
          {list.data?.length === 0 && <p className="p-3 text-fg-muted">No entities match.</p>}
          <ul>
            {list.data?.map((e) => (
              <li key={e.id}>
                <button
                  className={cn(
                    'flex w-full items-center justify-between gap-2 rounded-md px-2.5 py-1.5 text-left hover:bg-muted',
                    selected === e.id && 'bg-accent-soft',
                  )}
                  onClick={() => set({ id: e.id })}
                >
                  <span className="min-w-0 truncate">{e.name}</span>
                  <span className="flex shrink-0 items-center gap-2">
                    <TypeBadge type={e.type} />
                    <span className="w-7 text-right font-mono text-[11px] text-fg-muted tabular-nums">{e.degree}</span>
                  </span>
                </button>
              </li>
            ))}
          </ul>
        </div>
        {selected ? (
          <EntityPanel graph={graph} id={selected} open={(id) => set({ id })} />
        ) : (
          <div className="card text-fg-muted">
            Pick an entity on the left. On the ungrounded graph, search for "Amira" to see her name variants as separate
            entities; on a grounded graph they are one.
          </div>
        )}
      </div>
    </div>
  )
}
