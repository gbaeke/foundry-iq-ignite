import '@/index.css'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { StrictMode, Suspense } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Route, Routes } from 'react-router'
import { Toaster } from 'sonner'
import { Shell } from '@/components/Shell'
import { setupApiClient } from '@/lib/api'
import { ThemeProvider } from '@/lib/theme'
import { Compare } from '@/pages/Compare'
import { Console } from '@/pages/Console'
import { Explore } from '@/pages/Explore'
import { Network } from '@/pages/NetworkLazy'
import { NotFound } from '@/pages/NotFound'

setupApiClient()
const queryClient = new QueryClient({ defaultOptions: { queries: { staleTime: 10_000 } } })

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <ThemeProvider>
      <QueryClientProvider client={queryClient}>
        <BrowserRouter>
          <Routes>
            <Route element={<Shell />}>
              <Route index element={<Compare />} />
              <Route path="gql" element={<Console />} />
              <Route
                path="graph"
                element={
                  <Suspense>
                    <Network />
                  </Suspense>
                }
              />
              <Route path="explore" element={<Explore />} />
              <Route path="*" element={<NotFound />} />
            </Route>
          </Routes>
        </BrowserRouter>
        <Toaster richColors />
      </QueryClientProvider>
    </ThemeProvider>
  </StrictMode>,
)
