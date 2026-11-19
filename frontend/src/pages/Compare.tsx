import { useMutation, useQuery } from '@tanstack/react-query'
import { CircleCheck, CircleX, Play, TerminalSquare } from 'lucide-react'
import { useMemo, useState } from 'react'
import { useNavigate } from 'react-router'
import type { Question, Strategy, StrategyResult } from '@/client'
import { askMutation, listQuestionsOptions, listStrategiesOptions } from '@/client/@tanstack/react-query.gen'
import { errorMessage } from '@/lib/api'
import { cn } from '@/lib/utils'

/** Answers use **bold** for the key facts; render just that, everything else stays plain text. */
function Answer({ text }: { text: string }) {
  return (
    <p className="whitespace-pre-wrap leading-relaxed">
      {text.split(/\*\*(.+?)\*\*/g).map((part, i) => (i % 2 ? <strong key={i}>{part}</strong> : part))}
    </p>
  )
}

const DEFAULT_STRATEGIES = ['rag10', 'agentic', 'entity_g3', 'gql_agent_g3']
const CATEGORY_ORDER = ['lookup', 'counting', 'negative', 'multi_hop', 'entity_resolution', 'temporal', 'synthesis']

/** Which graph a graph strategy reads, so its GQL opens in the console on the right graph. */
const graphOf = (strategy: string) =>
  strategy.endsWith('_g3') ? 'grounded-v3' : strategy.endsWith('_g') ? 'grounded-v2' : 'ungrounded'

export function Compare() {
  const questions = useQuery(listQuestionsOptions())
  const strategies = useQuery(listStrategiesOptions())
  const [text, setText] = useState('How many projects has Amira El Idrissi worked on, and which ones?')
  const [questionId, setQuestionId] = useState<string | null>('C1')
  const [picked, setPicked] = useState<string[]>(DEFAULT_STRATEGIES)
  const ask = useMutation(askMutation())

  const byCategory = useMemo(() => {
    const groups = new Map<string, Question[]>()
    for (const q of questions.data ?? []) groups.set(q.category, [...(groups.get(q.category) ?? []), q])
    return CATEGORY_ORDER.filter((c) => groups.has(c)).map((c) => [c, groups.get(c)!] as const)
  }, [questions.data])
  const selected = questions.data?.find((q) => q.id === questionId) ?? null
  const labels = new Map((strategies.data ?? []).map((s) => [s.id, s.label]))

  const choose = (id: string) => {
    const q = questions.data?.find((x) => x.id === id)
    setQuestionId(q?.id ?? null)
    if (q) setText(q.question)
  }
  const toggle = (id: string) => setPicked((p) => (p.includes(id) ? p.filter((x) => x !== id) : [...p, id]))
  const run = () => ask.mutate({ body: { question: text, strategies: picked, question_id: questionId } })

  return (
    <div className="mx-auto max-w-[1400px] space-y-5">
      <div>
        <h1 className="text-xl font-semibold">Compare strategies</h1>
        <p className="text-fg-muted">
          One question, several retrieval strategies, the same answer model. Eval questions are scored against the
          ground truth.
        </p>
      </div>

      <div className="card space-y-4">
        <div className="grid gap-3 md:grid-cols-[260px_minmax(0,1fr)]">
          <label className="space-y-1">
            <span className="label">Eval question</span>
            <select
              id="question-pick"
              className="input"
              value={questionId ?? ''}
              onChange={(e) => choose(e.target.value)}
            >
              <option value="">Your own question</option>
              {byCategory.map(([cat, qs]) => (
                <optgroup key={cat} label={cat.replace('_', ' ')}>
                  {qs.map((q) => (
                    <option key={q.id} value={q.id}>
                      {q.id} · {q.question.slice(0, 60)}
                    </option>
                  ))}
                </optgroup>
              ))}
            </select>
          </label>
          <label className="space-y-1">
            <span className="label">Question</span>
            <textarea
              id="question-text"
              className="input min-h-[64px] resize-y"
              value={text}
              onChange={(e) => {
                setText(e.target.value)
                if (selected && e.target.value !== selected.question) setQuestionId(null)
              }}
              onKeyDown={(e) => {
                if (e.key === 'Enter' && (e.metaKey || e.ctrlKey) && picked.length) run()
              }}
            />
          </label>
        </div>

        <StrategyPicker strategies={strategies.data ?? []} picked={picked} toggle={toggle} />

        <div className="flex flex-wrap items-center gap-3">
          <button
            className="btn-primary"
            onClick={run}
            disabled={ask.isPending || !picked.length || text.trim().length < 3}
          >
            <Play className="size-4" />
            {ask.isPending ? `Running ${picked.length} strategies…` : `Run ${picked.length} strategies`}
          </button>
          <span className="text-xs text-fg-muted">Ctrl+Enter runs · graph strategies take 10–20 s</span>
        </div>
        {ask.isError && <p className="text-danger">{errorMessage(ask.error)}</p>}
      </div>

      {selected && <Expected q={selected} />}

      {ask.data && (
        <div className="grid items-start gap-4 lg:grid-cols-2 2xl:grid-cols-3">
          {ask.data.map((r) => (
            <ResultCard key={r.strategy} r={r} label={labels.get(r.strategy) ?? r.strategy} />
          ))}
        </div>
      )}
    </div>
  )
}

function StrategyPicker({
  strategies,
  picked,
  toggle,
}: {
  strategies: Strategy[]
  picked: string[]
  toggle: (id: string) => void
}) {
  return (
    <div className="grid gap-3 md:grid-cols-2">
      {(['search', 'graph'] as const).map((family) => (
        <fieldset key={family} className="space-y-1.5">
          <legend className="label mb-1">{family === 'search' ? 'Passage search' : 'Knowledge graph'}</legend>
          <div className="flex flex-wrap gap-1.5">
            {strategies
              .filter((s) => s.family === family)
              .map((s) => (
                <button
                  key={s.id}
                  type="button"
                  title={s.description}
                  onClick={() => toggle(s.id)}
                  aria-pressed={picked.includes(s.id)}
                  className={cn(
                    'rounded-full border px-3 py-1 text-xs transition-colors',
                    picked.includes(s.id)
                      ? 'border-accent bg-accent-soft text-accent'
                      : 'border-border text-fg-muted hover:text-fg',
                  )}
                >
                  {s.label}
                </button>
              ))}
          </div>
        </fieldset>
      ))}
    </div>
  )
}

function Expected({ q }: { q: Question }) {
  return (
    <div className="card border-dashed">
      <p className="label mb-1">Expected answer · {q.category.replace('_', ' ')}</p>
      <p>{q.answer}</p>
      {q.required_facts.length > 0 && (
        <p className="mt-2 text-xs text-fg-muted">Required facts: {q.required_facts.join(' · ')}</p>
      )}
    </div>
  )
}

function Metric({ label, value }: { label: string; value: string }) {
  return (
    <span className="flex flex-col">
      <span className="text-[11px] text-fg-muted">{label}</span>
      <span className="font-mono text-xs tabular-nums">{value}</span>
    </span>
  )
}

function ResultCard({ r, label }: { r: StrategyResult; label: string }) {
  const navigate = useNavigate()
  const tokens = r.answer_input_tokens + r.retrieval_tokens
  return (
    <article className="card space-y-3">
      <header className="flex items-start justify-between gap-2">
        <h2 className="font-semibold">{label}</h2>
        {r.judge && (
          <span
            className={cn(
              'inline-flex items-center gap-1 rounded-full px-2 py-0.5 text-xs font-medium',
              r.judge.correct ? 'bg-ok/10 text-ok' : 'bg-danger/10 text-danger',
            )}
          >
            {r.judge.correct ? <CircleCheck className="size-3.5" /> : <CircleX className="size-3.5" />}
            {r.judge.correct ? 'correct' : 'incorrect'} · {Math.round(r.judge.fact_recall * 100)}% facts
          </span>
        )}
      </header>

      {r.error ? (
        <p className="rounded-md bg-danger/10 p-3 text-xs text-danger">{r.error}</p>
      ) : (
        <>
          <div className="flex flex-wrap gap-5">
            <Metric label="retrieval" value={`${((r.retrieval_ms ?? 0) / 1000).toFixed(1)} s`} />
            <Metric label="total" value={`${(r.total_ms / 1000).toFixed(1)} s`} />
            <Metric label="tokens" value={tokens.toLocaleString()} />
            <Metric label="passages" value={String(r.context.length)} />
          </div>
          <Answer text={r.answer ?? ''} />

          {r.judge && r.judge.facts.length > 0 && (
            <ul className="space-y-0.5 text-xs">
              {r.judge.facts.map((f) => (
                <li key={f.fact} className={cn('flex gap-1.5', f.present ? 'text-ok' : 'text-danger')}>
                  {f.present ? '✓' : '✗'} <span className="text-fg-muted">{f.fact}</span>
                </li>
              ))}
            </ul>
          )}

          {r.gql.length > 0 && (
            <details open>
              <summary className="label cursor-pointer">Generated GQL ({r.gql.length})</summary>
              {r.gql.map((q, i) => (
                <div key={i} className="mt-2 space-y-1">
                  <pre className="overflow-x-auto rounded-md bg-muted p-2 font-mono text-[11.5px] whitespace-pre-wrap">
                    {q}
                  </pre>
                  <button
                    className="btn-ghost px-2 py-0.5 text-xs"
                    onClick={() => navigate('/gql', { state: { gql: q, graph: graphOf(r.strategy) } })}
                  >
                    <TerminalSquare className="size-3.5" /> Open in GQL console
                  </button>
                </div>
              ))}
            </details>
          )}

          {r.steps.length > 0 && (
            <details>
              <summary className="label cursor-pointer">Engine steps ({r.steps.length})</summary>
              <ol className="mt-2 space-y-1 text-xs">
                {r.steps.map((s, i) => (
                  <li key={i} className="grid grid-cols-[130px_minmax(0,1fr)_auto] gap-2">
                    <span className="font-mono text-fg-muted">{s.type}</span>
                    <span className="break-words">{s.detail}</span>
                    <span className="font-mono text-fg-muted tabular-nums">
                      {s.ms != null ? `${s.ms} ms` : ''} {s.tokens ? `· ${s.tokens.toLocaleString()} tok` : ''}
                    </span>
                  </li>
                ))}
              </ol>
            </details>
          )}

          <details>
            <summary className="label cursor-pointer">Retrieved context ({r.context.length})</summary>
            <ul className="mt-2 space-y-2">
              {r.context.map((p, i) => (
                <li key={i} className="rounded-md border border-border p-2 text-xs">
                  <span className="font-mono text-[11px] text-fg-muted">{p.source}</span>
                  <p className="mt-1 whitespace-pre-wrap">{p.text}</p>
                </li>
              ))}
            </ul>
          </details>
        </>
      )}
    </article>
  )
}
