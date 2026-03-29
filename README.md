# H90 Lens

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Vue](https://img.shields.io/badge/vue-3.5-42b883.svg)
![Vite](https://img.shields.io/badge/vite-8-646CFF.svg)
![Tailwind](https://img.shields.io/badge/tailwind-4-38BDF8.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**A fast, searchable reference for all Eventide H90 harmonizer pedal algorithms**

Browse 76 algorithms across 12 categories with instant search, parameter details, and full manual descriptions — all in a lightweight static site.

[Live Site](https://tsungtwu.github.io/h90-lens/) | [H90 Manual](https://cdn.eventideaudio.com/manuals/h90/latest/content/algorithms/index.html)

</div>

---

## Features

- **76 Algorithms** — All algorithms across 12 categories (Delay, Reverb, Modulation, Distortion, etc.)
- **Instant Search** — Filter by algorithm name, parameter name, or overview text with 150ms debounce
- **Category Filters** — Multi-select pill buttons with count badges
- **Parameter Info Bar** — Hover or click any parameter tile to see its description and range; click to lock
- **Detail Modal** — Full verbatim parameter descriptions from the official H90 manual
- **Performance Parameters** — Circular badges showing performance knobs (Repeat, Self Osc, etc.)
- **Pagination** — Algorithms with 10+ parameters paginate automatically
- **Agent-Friendly** — `llms.md` and `llms-full.md` endpoints for AI agent consumption
- **Keyboard Navigation** — `/` to focus search, `Escape` to close modal, `Tab` through elements
- **Responsive** — Works at 375px, 768px, 1024px, 1440px

---

## Quick Start

```bash
git clone https://github.com/tsungtwu/h90-lens.git
cd h90-lens
npm install
npm run dev
```

Open http://localhost:5173/h90-lens/

---

## Build & Deploy

```bash
npm run build     # production build → dist/
npm run preview   # preview production build locally
```

Deployment is automated via GitHub Actions — push to `main` triggers build and deploy to GitHub Pages.

---

## Data Update

Re-extract algorithm data from the latest official H90 manual:

```bash
pip install beautifulsoup4 requests

# Extract and sync to public/
python scripts/update_algorithms.py --sync-public

# Regenerate agent-friendly markdown
python scripts/generate_llms_txt.py
```

Options:
- `--fresh` — Ignore existing data and extract from scratch
- `--dry-run` — Print JSON to stdout without writing
- `--base-url` — Override manual URL (restricted to Eventide domains)

---

## Architecture

```
h90-lens/
├── src/
│   ├── App.vue                      # Root component, keyboard shortcuts
│   ├── main.js                      # Vue app entry
│   ├── assets/main.css              # Tailwind v4 @theme config
│   ├── components/
│   │   ├── AlgorithmCard.vue        # Card with param grid, perf circles, info bar
│   │   ├── CategoryFilters.vue      # Category pill buttons with counts
│   │   ├── CategoryIcon.vue         # SVG icon renderer per category
│   │   ├── DetailModal.vue          # Full parameter detail (ARIA, focus trap)
│   │   ├── InfoBar.vue              # Structured param info display
│   │   ├── ParamCard.vue            # Individual parameter tile
│   │   ├── PerfCircle.vue           # Performance parameter circle
│   │   └── SearchBar.vue            # Debounced search input
│   └── composables/
│       ├── useAlgorithms.js         # Shared state (algorithms, search, filters)
│       └── useCategoryIcons.js      # SVG icon map for 12 categories
├── public/
│   ├── data/algorithms.json         # 76 algorithms (static asset)
│   ├── llms.md                      # Agent-friendly overview
│   └── llms-full.md                 # Agent-friendly full reference
├── scripts/
│   ├── update_algorithms.py         # Extract data from H90 manual
│   └── generate_llms_txt.py         # Generate markdown from JSON
├── data/algorithms.json             # Source data (edit here)
├── vite.config.js                   # Vite + Vue + Tailwind, base: '/h90-lens/'
└── index.html                       # Entry point with CSP meta tag
```

### Tech Stack
- **Framework:** Vue 3 (Composition API, `<script setup>`)
- **Build:** Vite 8
- **Styling:** Tailwind CSS v4 via `@tailwindcss/vite`
- **Fonts:** Google Fonts — Righteous (headings) + Poppins (body)
- **Data Extraction:** Python + BeautifulSoup
- **Deploy:** GitHub Pages via GitHub Actions

---

## Agent-Friendly Endpoints

| URL | Format | Description |
|-----|--------|-------------|
| `/h90-lens/llms.md` | Markdown | Site overview + links |
| `/h90-lens/llms-full.md` | Markdown | All 76 algorithms with full parameter details |
| `/h90-lens/data/algorithms.json` | JSON | Structured algorithm data |

---

## Data Source

Algorithm data sourced from the [Eventide H90 Manual](https://cdn.eventideaudio.com/manuals/h90/latest/content/algorithms/index.html). Not affiliated with Eventide Audio.

---

## License

MIT

---

## Author

**tsungtwu** - [@tsungtwu](https://github.com/tsungtwu)

---

<div align="center">

Built with [Claude Code](https://claude.ai/code)

</div>
