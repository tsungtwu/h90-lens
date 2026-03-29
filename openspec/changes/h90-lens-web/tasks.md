## 1. Data Extraction & Processing

- [x] 1.1 Fetch all H90 category pages and extract algorithm data using BeautifulSoup
- [x] 1.2 Structure data as `data/algorithms.json` with schema: `{name, category, overview, parameters: [{name, description, range?, fullDescription}], performanceParams: [{name, description}]}`
- [x] 1.3 Verify dataset covers all 12 categories and 76 algorithms
- [x] 1.4 Re-extract verbatim fullDescription from manual HTML (replacing AI summaries)
- [x] 1.5 Create Python script (`scripts/update_algorithms.py`) with BeautifulSoup parsing, SSRF domain whitelist, `--sync-public` flag, and `--base-url` defaulting to `latest`
- [x] 1.6 Handle extraction edge cases: inner option lists in `<dd>`, section header contamination, footer artifacts

## 2. Project Setup

- [x] 2.1 Initialize Vue 3 + Vite 8 project with `@vitejs/plugin-vue`
- [x] 2.2 Configure Tailwind CSS v4 via `@tailwindcss/vite` with `@theme` directive for custom colors
- [x] 2.3 Set up Google Fonts: Righteous (headings) + Poppins (body)
- [x] 2.4 Configure `vite.config.js` with `base: '/h90-lens/'`
- [x] 2.5 Add CSP meta tag in `index.html`

## 3. Core Components

- [x] 3.1 `useAlgorithms.js` composable — shared state with double-call guard, null-safe overview filtering, categoryCounts computed, user-friendly error messages
- [x] 3.2 `useCategoryIcons.js` composable — SVG icon map for 12 categories
- [x] 3.3 `SearchBar.vue` — debounced input (150ms), timeout cleanup on unmount, `/` keyboard shortcut, expose focus()
- [x] 3.4 `CategoryFilters.vue` — pill buttons with category icons and count badges (data prop, not function prop)
- [x] 3.5 `CategoryIcon.vue` — SVG renderer using `useAttrs()` + `inheritAttrs: false` (not props.class)
- [x] 3.6 `ParamCard.vue` — parameter tile with hover/click/lock behavior
- [x] 3.7 `PerfCircle.vue` — performance parameter circle with hover/click/lock
- [x] 3.8 `InfoBar.vue` — structured props (paramName, paramDescription, paramRange, isPerformance), no v-html XSS
- [x] 3.9 `AlgorithmCard.vue` — card with overview, param grid (pagination), perf circles, info bar (flex-col + mt-auto for bottom alignment), lockedParam reset on page change, null-safe performanceParams
- [x] 3.10 `DetailModal.vue` — Teleport to body, ARIA dialog with focus trap, focus restore on close, null-safe performanceParams
- [x] 3.11 `App.vue` — root orchestrator with keyboard shortcuts (/, Escape)

## 4. Agent-Friendly Output

- [x] 4.1 Create `scripts/generate_llms_txt.py` to generate `llms.md` and `llms-full.md` from algorithms.json
- [x] 4.2 Add `prebuild` npm script to auto-generate markdown before Vite build
- [x] 4.3 Verify `llms.md` and `llms-full.md` included in `dist/` output

## 5. Code Quality & Security

- [x] 5.1 Eliminate all v-html XSS risks (InfoBar refactored to structured props)
- [x] 5.2 Add null/undefined safety across all components (performanceParams, overview, description)
- [x] 5.3 Add ARIA attributes and focus trap to DetailModal
- [x] 5.4 Add CSP meta tag to index.html
- [x] 5.5 Add SSRF domain whitelist to Python script
- [x] 5.6 Fix CategoryIcon useAttrs for proper class passthrough
- [x] 5.7 Add double-call guard and loadError reset to loadAlgorithms()
- [x] 5.8 Fix SearchBar timeout cleanup on unmount
- [x] 5.9 Replace getCategoryCount function prop with categoryCounts data prop

## 6. Responsive Design & Accessibility

- [x] 6.1 Param grid: 2-col mobile, 3-col sm, 5-col md+
- [x] 6.2 Card grid: 1-col default, 2-col xl
- [x] 6.3 Keyboard navigation: tabindex, Enter/Space, focus-visible, `/` to search, Escape
- [x] 6.4 `prefers-reduced-motion` support
- [x] 6.5 Bottom-aligned InfoBar across cards of different heights (flex-col + mt-auto)
- [x] 6.6 Test at 375px, 768px, 1024px, 1440px

## 7. Deployment

- [x] 7.1 Verify `npm run build` produces correct `dist/` output
- [ ] 7.2 Configure GitHub Pages deployment (GitHub Actions or gh-pages branch)
- [x] 7.3 Verify base path `/h90-lens/` works correctly for all assets and data fetch
