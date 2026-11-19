import { lazy } from 'react'

/** Cytoscape is most of the bundle, so the Graph page loads it only when opened. */
export const Network = lazy(() => import('@/pages/Network').then((m) => ({ default: m.Network })))
