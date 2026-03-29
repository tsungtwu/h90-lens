## Why

The Eventide H90 effects pedal has 76 algorithms across 12 categories, each with multiple knobs and parameters. The official manual is comprehensive but slow to navigate when you need a quick answer during a live session or practice. A lightweight, searchable static website would let users instantly find what any knob does on any algorithm — both for real-time reference while tweaking the pedal and for pre-session research.

## What Changes

- Create a single-page Vue 3 + Vite static website ("H90 Lens") that displays all H90 algorithms and their parameters
- Implement instant search filtering by algorithm name, parameter name, and algorithm overview
- Add category filter buttons (Delay, Reverb, Modulation, etc.) for quick browsing
- Display each algorithm as a card showing: overview, parameter grid with hover/click info bar, performance parameter circles, pagination, and detail modal for full descriptions
- Use Tailwind CSS v4 (build-time via `@tailwindcss/vite`) with a dark theme suited for musicians
- Structure algorithm data as a separate JSON dataset loaded at runtime
- Provide agent-friendly markdown endpoints (`llms.md`, `llms-full.md`)
- Python script for re-extracting data from the official H90 manual on demand
- Deploy on GitHub Pages as a static site with Vite build

## Capabilities

### New Capabilities
- `algorithm-data`: Structured JSON dataset of all 76 H90 algorithms with categories, parameters (name, description, range, fullDescription), and performance parameters (name, description). Python extraction script with SSRF protection and `--sync-public` support. Agent-friendly markdown output via `llms.md` / `llms-full.md`.
- `search-and-filter`: Real-time debounced search by algorithm name, parameter name, and overview text, plus category filter buttons with multi-select and count badges. Instant filtering with no page reload.
- `algorithm-cards`: Card UI for each algorithm showing overview, parameter grid (hover/click info bar, pagination), performance parameter circles, and detail modal with full parameter descriptions. ARIA-compliant modal with focus trap.
- `static-deployment`: GitHub Pages deployment with Vite build. Vue 3 + Tailwind CSS v4 + CSP meta tag. Base path `/h90-lens/`.

### Modified Capabilities
<!-- None - this is a greenfield project -->

## Impact

- **Tech stack**: Vue 3 (Composition API) + Vite 8 + Tailwind CSS v4
- **New files**: Vue SFC components, composables, Vite config, Python scripts, llms.md files
- **Dependencies**: vue, @vitejs/plugin-vue, @tailwindcss/vite, tailwindcss, vite
- **External data source**: Content extracted from https://cdn.eventideaudio.com/manuals/h90/latest/content/algorithms/
- **Deployment**: GitHub Pages via Vite build (`dist/` output)
- **No backend**: Entirely client-side, no API calls at runtime
- **Agent-friendly**: `llms.md` and `llms-full.md` for AI agent consumption
