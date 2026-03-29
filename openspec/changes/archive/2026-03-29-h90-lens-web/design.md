## Context

The Eventide H90 is a professional effects pedal with 76 algorithms across 12 categories. Each algorithm has 5-15 parameters (knobs) that control its behavior. The official manual at cdn.eventideaudio.com provides comprehensive documentation, but it's structured as multi-page HTML that requires multiple clicks to navigate.

## Goals / Non-Goals

**Goals:**
- Instant lookup of any H90 algorithm parameter while using the pedal
- Browse and compare algorithms by category
- Work well on both desktop and mobile (phone propped up near pedalboard)
- Zero-latency filtering and search (all data client-side)
- Agent-friendly markdown endpoints for AI tools
- Minimal maintenance burden (static site, no backend)

**Non-Goals:**
- Real-time pedal control or MIDI integration
- User accounts, saved presets, or personalization
- Audio samples or demo recordings
- PWA/offline support

## Architecture

### Tech Stack
- **Framework**: Vue 3 with Composition API (`<script setup>`)
- **Build**: Vite 8 with `@vitejs/plugin-vue`
- **Styling**: Tailwind CSS v4 via `@tailwindcss/vite` (build-time, not CDN)
- **Fonts**: Google Fonts — Righteous (headings) + Poppins (body)
- **Data**: Static JSON loaded via `fetch()` at runtime

### Component Architecture

```
App.vue
├── SearchBar.vue          — Debounced search input (150ms)
├── CategoryFilters.vue    — Category pill buttons with count badges
├── AlgorithmCard.vue      — Main card (flex-col for bottom-aligned InfoBar)
│   ├── CategoryIcon.vue   — SVG icon renderer (useAttrs for class passthrough)
│   ├── ParamCard.vue      — Individual parameter tile (hover/click)
│   ├── PerfCircle.vue     — Performance parameter circle
│   └── InfoBar.vue        — Structured param info display (no v-html)
└── DetailModal.vue        — Full parameter detail (Teleport, ARIA, focus trap)
```

### Shared State
- `composables/useAlgorithms.js` — Module-level singleton state (not Pinia)
  - `allAlgorithms`, `filteredAlgorithms`, `categories`, `categoryCounts`
  - `loadAlgorithms()` with double-call guard
  - `setSearch()`, `toggleCategory()`, `getAlgorithmByName()`
- `composables/useCategoryIcons.js` — SVG icon map for 12 categories

### Data Flow

```
algorithms.json → fetch() → allAlgorithms (ref)
                                ↓
searchQuery + activeCategories → filteredAlgorithms (computed)
                                ↓
AlgorithmCard → ParamCard hover/click → activeParam → InfoBar (structured props)
                                                    → DetailModal (full descriptions)
```

## Decisions

### 1. Vue 3 + Vite (not vanilla JS)
**Decision**: Vue 3 Composition API with Vite build.
**Rationale**: Production-ready SPA with proper component architecture, reactive state, and optimized build output (82KB JS + 24KB CSS gzipped ~36KB).
**Alternative**: Vanilla JS prototype worked but wasn't maintainable.

### 2. Tailwind CSS v4 via build plugin (not CDN)
**Decision**: `@tailwindcss/vite` plugin with `@theme` directive.
**Rationale**: Proper build-time processing, tree-shaking, no CDN dependency. Tailwind v4 uses `@theme` instead of `tailwind.config`.
**Alternative**: CDN was used in prototype but not suitable for production.

### 3. Separate JSON file loaded via fetch
**Decision**: `public/data/algorithms.json` loaded at runtime.
**Rationale**: Keeps data maintainable, versionable, and cacheable. Uses `import.meta.env.BASE_URL` for correct GitHub Pages path.

### 4. Structured InfoBar props (not v-html)
**Decision**: InfoBar accepts `paramName`, `paramDescription`, `paramRange`, `isPerformance` props.
**Rationale**: Eliminates XSS risk from v-html. Text interpolation via `{{ }}` is auto-escaped.

### 5. Module-level singleton composable (not Pinia)
**Decision**: `useAlgorithms.js` stores state at module level outside the function.
**Rationale**: Simple shared state without Pinia overhead. All components share the same reactive refs.

### 6. Agent-friendly markdown (llms.md)
**Decision**: Pre-generated `llms.md` and `llms-full.md` as static assets.
**Rationale**: GitHub Pages can't do content negotiation. Static `.md` files follow llmstxt.org convention. Generated from JSON by Python script during build.

### 7. CSP meta tag
**Decision**: Content-Security-Policy meta tag in index.html.
**Rationale**: Static site can't set HTTP headers. Meta tag restricts scripts to 'self', allows Google Fonts for styles/fonts.

### Design System
- **Colors** (`@theme`): bg `#0F0F23`, bg-card `#161637`, primary `#1E1B4B`, accent `#E97C2E`, text `#F8FAFC`, muted `#94A3B8`
- **Typography**: Righteous (headings, italic uppercase) + Poppins (body)
- **Cards**: `rounded-2xl`, `border-white/10`, `hover:border-white/20`
- **Param grid**: 2-col mobile, 3-col sm, 5-col md+
- **Card grid**: 1-col default, 2-col xl

## Security Considerations

- No v-html in InfoBar — all user-facing text uses `{{ }}` interpolation
- CategoryIcon uses v-html for trusted SVG only (from internal composable, not user data)
- CSP meta tag restricts script sources to 'self'
- Python script validates URL domain against allowlist (SSRF prevention)
- No cookies, localStorage, or tracking
- All CDN resources loaded over HTTPS

## Risks / Trade-offs

- **Data accuracy** → Python script re-extracts from manual. Background agent verified verbatim descriptions.
- **GitHub Pages base path** → `base: '/h90-lens/'` in vite.config, `import.meta.env.BASE_URL` for data fetch.
- **Manual data updates** → Python script + `--sync-public` flag. Document extraction process.
