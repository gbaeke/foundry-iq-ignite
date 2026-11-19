import { useMutation, useQuery } from '@tanstack/react-query'
import { Play } from 'lucide-react'
import { useState } from 'react'
import { useLocation } from 'react-router'
import { listGraphsOptions, runGqlMutation } from '@/client/@tanstack/react-query.gen'
import { errorMessage } from '@/lib/api'

const EXAMPLES: { label: string; gql: string }[] = [
  {
    label: "Amira's projects, by id (grounded graphs)",
    gql: "MATCH (p:Person)-[e]->(j:Project)\nWHERE e.predicate = 'workedOn' AND p.id = 'person:amira'\nRETURN count(DISTINCT j) AS n, COLLECT_LIST(DISTINCT j.name) AS projects",
  },
  {
    label: "Amira's projects, by name",
    gql: "MATCH (p:Person)-[e]->(j:Project)\nWHERE e.predicate = 'workedOn' AND p.name CONTAINS 'Idrissi'\nRETURN count(DISTINCT j) AS n, COLLECT_LIST(DISTINCT j.name) AS projects",
  },
  {
    label: 'Projects Thomas managed',
    gql: "MATCH (p:Person)-[e]->(j:Project)\nWHERE e.predicate = 'managedProject' AND p.name CONTAINS 'Maes'\nRETURN DISTINCT j.name AS project",
  },
  {
    label: 'Who worked with Kevin (multi-hop)',
    gql: "MATCH (k:Person)-[e1]->(j:Project)<-[e2]-(c:Person)\nWHERE k.name CONTAINS 'Kevin' AND e2.predicate = 'workedOn'\nRETURN c.name AS consultant, COLLECT_LIST(DISTINCT j.name) AS projects",
  },
  {
    label: 'Databricks projects',
    gql: "MATCH (j:Project)-[e]->(t:Technology)\nWHERE e.predicate = 'usesTechnology' AND t.name CONTAINS 'Databricks'\nRETURN DISTINCT j.name AS project",
  },
  { label: 'Nodes per type', gql: 'MATCH (n) RETURN labels(n) AS type, count(*) AS n GROUP BY type' },
  {
    label: 'Relationships by count',
    gql: 'MATCH (a)-[e]->(b) RETURN e.predicate AS predicate, count(*) AS n GROUP BY e.predicate ORDER BY n DESC',
  },
]

const DEFAULT_GQL = EXAMPLES[0]?.gql ?? ''

const show = (v: unknown) => (typeof v === 'string' ? v : JSON.stringify(v))

export function Console() {
  const state = (useLocation().state ?? {}) as { gql?: string; graph?: string }
  const graphs = useQuery(listGraphsOptions())
  const [graph, setGraph] = useState(state.graph ?? 'grounded-v3')
  const [gql, setGql] = useState(state.gql ?? DEFAULT_GQL)
  const run = useMutation(runGqlMutation())
  const go = () => run.mutate({ body: { graph, gql } })
  const info = graphs.data?.find((g) => g.id === graph)

  return (
    <div className="mx-auto max-w-6xl space-y-5">
      <div>
        <h1 className="text-xl font-semibold">GQL console</h1>
        <p className="text-fg-muted">
          Run GQL straight against a graph index (<span className="font-mono text-xs">search.graph</span>), with no
          model in between.
        </p>
      </div>

      <div className="card space-y-3">
        <div className="flex flex-wrap items-end gap-3">
          <label className="space-y-1">
            <span className="label">Graph</span>
            <select id="console-graph" className="input w-56" value={graph} onChange={(e) => setGraph(e.target.value)}>
              {graphs.data?.map((g) => (
                <option key={g.id} value={g.id}>
                  {g.label}
                </option>
              ))}
            </select>
          </label>
          <label className="space-y-1">
            <span className="label">Example</span>
            <select
              id="console-example"
              className="input w-64"
              value=""
              onChange={(e) => setGql(EXAMPLES[Number(e.target.value)]?.gql ?? gql)}
            >
              <option value="">Load an example…</option>
              {EXAMPLES.map((x, i) => (
                <option key={x.label} value={i}>
                  {x.label}
                </option>
              ))}
            </select>
          </label>
        </div>
        {info && (
          <p className="text-xs text-fg-muted">
            {info.description} Index <span className="font-mono">{info.graph_index}</span>.
          </p>
        )}
        <textarea
          id="console-gql"
          className="input min-h-[140px] font-mono text-[12.5px]"
          spellCheck={false}
          value={gql}
          onChange={(e) => setGql(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === 'Enter' && (e.metaKey || e.ctrlKey)) go()
          }}
        />
        <div className="flex items-center gap-3">
          <button className="btn-primary" onClick={go} disabled={run.isPending || gql.trim().length < 6}>
            <Play className="size-4" /> {run.isPending ? 'Running…' : 'Run'}
          </button>
          <span className="text-xs text-fg-muted">Ctrl+Enter runs · max 2,048 characters, 1,000 rows</span>
          {run.data && (
            <span className="ml-auto font-mono text-xs text-fg-muted tabular-nums">
              {run.data.row_count} row(s) · {run.data.ms} ms
            </span>
          )}
        </div>
        {run.isError && (
          <pre className="rounded-md bg-danger/10 p-3 text-xs whitespace-pre-wrap text-danger">
            {errorMessage(run.error)}
          </pre>
        )}
      </div>

      {run.data && (
        <div className="card overflow-x-auto p-0">
          {run.data.rows.length === 0 ? (
            <p className="p-4 text-fg-muted">
              0 rows. That can mean "no such relationship", or a filter that doesn't match how names are stored.
            </p>
          ) : (
            <table className="w-full text-left text-xs">
              <thead className="bg-muted">
                <tr>
                  {run.data.columns.map((c) => (
                    <th key={c} className="px-3 py-2 font-medium">
                      {c}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {run.data.rows.map((row, i) => (
                  <tr key={i} className="border-t border-border align-top">
                    {run.data.columns.map((c) => (
                      <td key={c} className="px-3 py-1.5 font-mono break-words">
                        {show(row[c])}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      )}
    </div>
  )
}
