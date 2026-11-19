import { isLiteral, typeColor } from '@/lib/entity'
import { cn } from '@/lib/utils'

export function TypeBadge({ type }: { type: string }) {
  const color = isLiteral(type)
    ? 'text-literal border-literal border-dashed'
    : (typeColor[type] ?? 'text-fg-muted border-border')
  return (
    <span className={cn('inline-block rounded border px-1.5 text-[11px] leading-5 font-medium', color)}>
      {isLiteral(type) ? 'text' : type}
    </span>
  )
}
