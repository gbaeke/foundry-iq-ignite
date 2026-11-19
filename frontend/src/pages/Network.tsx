import { useQuery } from '@tanstack/react-query'
import cytoscape, { type Core, type ElementDefinition } from 'cytoscape'
import { Maximize2, RefreshCw } from 'lucide-react'
import { useEffect, useMemo, useRef, useState } from 'react'
import { useSearchParams } from 'react-router'
import type { NetworkNode } from '@/client'
import { getNetworkOptions, listGraphsOptions } from '@/client/@tanstack/react-query.gen'
import { EntityPanel } from '@/components/EntityPanel'
import { errorMessage } from '@/lib/api'
import { cn } from '@/lib/utils'

const TYPES = ['Person', 'Project', 'Organization', 'Technology', 'Place', 'Issue', 'Outcome']
const DEFAULT_ON = ['Person', 'Project', 'Organization', 'Technology', 'Place']
const TYPE_TOKEN: Record<string, string> = {
  Person: '--person',
  Project: '--project',
  Organization: '--org',
  Technology: '--tech',
  Place: '--place',
  Issue: '--danger',
  Outcome: '--warn',
}

const css = (name: string) => getComputedStyle(document.documentElement).getPropertyValue(name).trim()
const nodeColor = (type: string) => css(TYPE_TOKEN[type] ?? '--fg-muted')

/** Same-type entities whose name contains another one's ("Amira" in "Amira El Idrissi"): likely one real entity. */
function likelyDuplicates(nodes: NetworkNode[]) {
  const norm = (s: string) =>
    ` ${s
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, ' ')
      .trim()} `
  const groups: NetworkNode[][] = []
  for (const type of DEFAULT_ON) {
    const used = new Set<string>()
    const ofType = nodes.filter((n) => n.type === type).sort((a, b) => b.name.length - a.name.length)
    for (const a of ofType) {
      if (used.has(a.id)) continue
      const same = ofType.filter(
        (b) => b !== a && !used.has(b.id) && norm(b.name).trim().length >= 3 && norm(a.name).includes(norm(b.name)),
      )
      if (same.length) {
        groups.push([a, ...same])
        for (const x of [a, ...same]) used.add(x.id)
      }
    }
  }
  return groups
}

function graphStyle(): cytoscape.StylesheetJson {
  return [
    {
      selector: 'node',
      style: {
        'background-color': 'data(color)',
        width: 'data(size)',
        height: 'data(size)',
        label: 'data(label)',
        'font-size': 10,
        color: css('--fg'),
        'text-valign': 'bottom',
        'text-margin-y': 3,
        'text-max-width': '110px',
        'text-wrap': 'ellipsis',
        'min-zoomed-font-size': 7,
      },
    },
    {
      selector: 'edge',
      style: {
        width: 'mapData(count, 1, 15, 0.8, 4)',
        'line-color': css('--border'),
        'curve-style': 'haystack',
        opacity: 0.7,
      },
    },
    { selector: '.faded', style: { opacity: 0.1 } },
    {
      selector: 'edge.hi',
      style: {
        'line-color': css('--fg-muted'),
        opacity: 1,
        'curve-style': 'bezier',
        'target-arrow-shape': 'triangle',
        'target-arrow-color': css('--fg-muted'),
        'arrow-scale': 0.7,
        label: 'data(predicate)',
        'font-size': 8,
        color: css('--fg-muted'),
        'text-rotation': 'autorotate',
        'text-background-color': css('--surface'),
        'text-background-opacity': 0.85,
        'text-background-padding': '1px',
      },
    },
    { selector: 'node.sel', style: { 'border-width': 3, 'border-color': css('--fg') } },
    { selector: 'node.match', style: { 'border-width': 3, 'border-color': css('--accent') } },
  ]
}

export function Network() {
  const [params, setParams] = useSearchParams()
  const graph = params.get('graph') ?? 'grounded-v3'
  const selected = params.get('id')
  const [types, setTypes] = useState<string[]>(DEFAULT_ON)
  const [predicate, setPredicate] = useState('')
  const [find, setFind] = useState('')
  const [tab, setTab] = useState<'entity' | 'duplicates'>('entity')
  const graphs = useQuery(listGraphsOptions())
  const net = useQuery(getNetworkOptions({ path: { graph_id: graph } }))
  const box = useRef<HTMLDivElement>(null)
  const cy = useRef<Core | null>(null)

  const select = (id: string | null) => {
    const p = new URLSearchParams(params)
    if (id) p.set('id', id)
    else p.delete('id')
    setParams(p)
    if (id) setTab('entity')
  }
  const setGraph = (g: string) => setParams(new URLSearchParams({ graph: g }))

  const predicates = useMemo(() => [...new Set(net.data?.edges.map((e) => e.predicate))].sort(), [net.data])
  const duplicates = useMemo(() => likelyDuplicates(net.data?.nodes ?? []), [net.data])
  const triples = net.data?.edges.reduce((n, e) => n + e.count, 0) ?? 0

  const runLayout = () => {
    const c = cy.current
    if (!c) return
    const big = c.nodes().length > 400
    c.layout({
      name: 'cose',
      animate: false,
      randomize: true,
      nodeRepulsion: () => (big ? 9000 : 14000),
      idealEdgeLength: () => (big ? 45 : 70),
      gravity: big ? 0.6 : 0.35,
      numIter: big ? 600 : 1500,
      padding: 30,
    }).run()
  }

  // rebuild the drawing when the data or the filters change
  useEffect(() => {
    if (!net.data || !box.current) return
    const shown = new Set(types)
    const byId = new Map(net.data.nodes.map((n) => [n.id, n]))
    const edges = net.data.edges.filter(
      (e) =>
        (!predicate || e.predicate === predicate) &&
        shown.has(byId.get(e.source)?.type ?? '') &&
        shown.has(byId.get(e.target)?.type ?? ''),
    )
    const used = new Set(edges.flatMap((e) => [e.source, e.target]))
    const elements: ElementDefinition[] = [
      ...net.data.nodes
        .filter((n) => used.has(n.id))
        .map((n) => ({
          data: { id: n.id, label: n.name, color: nodeColor(n.type), size: Math.min(14 + Math.sqrt(n.degree) * 4, 60) },
        })),
      ...edges.map((e, i) => ({
        data: { id: `e${i}`, source: e.source, target: e.target, predicate: e.predicate, count: e.count },
      })),
    ]
    const c = cytoscape({ container: box.current, elements, style: graphStyle(), minZoom: 0.05, maxZoom: 3 })
    cy.current = c
    c.on('tap', 'node', (ev) => select(ev.target.id()))
    runLayout()
    return () => c.destroy()
    // select/runLayout only read refs and params; rebuilding on them would redraw on every click
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [net.data, types, predicate])

  // highlight the selected entity and its neighbours
  useEffect(() => {
    const c = cy.current
    if (!c) return
    c.elements().removeClass('faded hi sel')
    const n = selected ? c.getElementById(selected) : null
    if (!n || n.empty()) return
    c.elements().addClass('faded')
    n.closedNeighborhood().removeClass('faded')
    n.connectedEdges().addClass('hi')
    n.addClass('sel')
    c.animate({ fit: { eles: n.closedNeighborhood(), padding: 60 } }, { duration: 300 })
  }, [selected, net.data, types, predicate])

  // search: ring the matching nodes and zoom to them
  useEffect(() => {
    const c = cy.current
    if (!c) return
    c.nodes().removeClass('match')
    const q = find.trim().toLowerCase()
    if (q.length < 2) return
    const names = new Map((net.data?.nodes ?? []).map((n) => [n.id, n.names]))
    const hits = c.nodes().filter((n) => (names.get(n.id()) ?? []).some((x) => x.toLowerCase().includes(q)))
    hits.addClass('match')
    if (hits.nonempty()) c.animate({ fit: { eles: hits.closedNeighborhood(), padding: 60 } }, { duration: 300 })
  }, [find, net.data])

  // graph colours follow the theme toggle
  useEffect(() => {
    const restyle = () => {
      const c = cy.current
      if (!c || !net.data) return
      const typeOf = new Map(net.data.nodes.map((n) => [n.id, n.type]))
      c.nodes().forEach((n) => {
        n.data('color', nodeColor(typeOf.get(n.id()) ?? ''))
      })
      c.style(graphStyle())
    }
    const obs = new MutationObserver(restyle)
    obs.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] })
    return () => obs.disconnect()
  }, [net.data])

  return (
    <div className="mx-auto flex h-full max-w-[1600px] flex-col gap-3">
      <div>
        <h1 className="text-xl font-semibold">Graph</h1>
        <p className="text-fg-muted">
          The whole entity graph. Switch between the ungrounded and grounded graphs to see name variants collapse into
          one node.
        </p>
      </div>

      <div className="flex flex-wrap items-end gap-3">
        <label className="space-y-1">
          <span className="label">Graph</span>
          <select id="network-graph" className="input w-52" value={graph} onChange={(e) => setGraph(e.target.value)}>
            {graphs.data?.map((g) => (
              <option key={g.id} value={g.id}>
                {g.label}
              </option>
            ))}
          </select>
        </label>
        <label className="space-y-1">
          <span className="label">Relationship</span>
          <select
            id="network-predicate"
            className="input w-48"
            value={predicate}
            onChange={(e) => setPredicate(e.target.value)}
          >
            <option value="">All relationships</option>
            {predicates.map((p) => (
              <option key={p} value={p}>
                {p}
              </option>
            ))}
          </select>
        </label>
        <label className="space-y-1">
          <span className="label">Find</span>
          <input
            id="network-find"
            className="input w-48"
            placeholder="Name…"
            value={find}
            onChange={(e) => setFind(e.target.value)}
          />
        </label>
        <div className="flex flex-wrap gap-1.5">
          {TYPES.map((t) => (
            <button
              key={t}
              type="button"
              aria-pressed={types.includes(t)}
              onClick={() => setTypes((ts) => (ts.includes(t) ? ts.filter((x) => x !== t) : [...ts, t]))}
              className={cn(
                'flex items-center gap-1.5 rounded-full border border-border px-2.5 py-1 text-xs',
                types.includes(t) ? 'text-fg' : 'text-fg-muted opacity-50',
              )}
            >
              <span className="size-2.5 rounded-full" style={{ background: `var(${TYPE_TOKEN[t]})` }} />
              {t}
            </button>
          ))}
        </div>
        <div className="ml-auto flex gap-1">
          <button
            className="btn-ghost"
            onClick={() => cy.current?.fit(undefined, 30)}
            title="Fit the graph to the view"
          >
            <Maximize2 className="size-4" /> Fit
          </button>
          <button className="btn-ghost" onClick={runLayout} title="Run the layout again">
            <RefreshCw className="size-4" /> Layout
          </button>
        </div>
      </div>

      {net.data && (
        <p className="font-mono text-xs text-fg-muted tabular-nums">
          {net.data.nodes.length.toLocaleString()} entities · {triples.toLocaleString()} entity triples ·{' '}
          {net.data.edges.length.toLocaleString()} distinct relationships · {duplicates.length} likely duplicate groups
        </p>
      )}

      <div className="grid min-h-[560px] flex-1 gap-3 lg:grid-cols-[minmax(0,1fr)_380px]">
        <div className="card relative min-h-[480px] p-0">
          {net.isPending && (
            <p className="absolute inset-0 grid place-items-center text-fg-muted">Reading every triple of the graph…</p>
          )}
          {net.isError && (
            <p className="absolute inset-0 grid place-items-center text-danger">{errorMessage(net.error)}</p>
          )}
          <div className="absolute inset-0">
            {/* cytoscape makes its container position: relative, so it needs a sized parent */}
            <div ref={box} className="size-full" />
          </div>
          <span className="pointer-events-none absolute bottom-2 left-3 text-xs text-fg-muted">
            Scroll to zoom · drag to pan · click a node
          </span>
        </div>
        <div className="flex min-w-0 flex-col gap-2">
          <div className="flex gap-1">
            {(['entity', 'duplicates'] as const).map((t) => (
              <button
                key={t}
                onClick={() => setTab(t)}
                aria-pressed={tab === t}
                className={cn(
                  'rounded-md px-3 py-1 text-xs',
                  tab === t ? 'bg-accent-soft text-accent' : 'text-fg-muted hover:bg-muted',
                )}
              >
                {t === 'entity' ? 'Entity' : `Likely duplicates (${duplicates.length})`}
              </button>
            ))}
          </div>
          {tab === 'entity' &&
            (selected ? (
              <EntityPanel graph={graph} id={selected} open={select} />
            ) : (
              <div className="card text-fg-muted">
                Click a node to see its name variants, relationships and the passages they were extracted from.
              </div>
            ))}
          {tab === 'duplicates' && (
            <div className="card max-h-[70vh] space-y-2 overflow-auto text-xs">
              <p className="text-fg-muted">
                Same-type entities whose name contains another one's. They are separate nodes, so a query on one name
                misses the others. Grounding is meant to merge them.
              </p>
              {duplicates.length === 0 && <p>None found.</p>}
              {duplicates.map((g) => (
                <div
                  key={g[0]!.id}
                  className="flex flex-wrap items-baseline gap-x-2 gap-y-1 border-t border-border pt-2"
                >
                  <span className="text-fg-muted">{g[0]!.type}</span>
                  {g.map((n) => (
                    <button
                      key={n.id}
                      className="underline decoration-border underline-offset-2 hover:decoration-accent"
                      onClick={() => select(n.id)}
                    >
                      {n.name} <span className="text-fg-muted">({n.degree})</span>
                    </button>
                  ))}
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
