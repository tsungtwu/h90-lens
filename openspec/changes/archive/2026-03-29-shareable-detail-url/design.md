# Design: Shareable Detail URL

## Architecture

### URL Scheme
Use URL hash fragment: `#algo={slug}` where slug is the algorithm name with spaces replaced by hyphens, lowercased.

Examples:
- `https://h90-lens.tsungtwu.dev/#algo=blackhole`
- `https://h90-lens.tsungtwu.dev/#algo=digital-delay`

### Component Changes

**App.vue**
- On `loadAlgorithms` completion, check `window.location.hash` for `#algo=<slug>`
- If found, look up algorithm by slug and open detail modal
- On modal open: set `window.location.hash` to `#algo=<slug>`
- On modal close: clear hash via `history.replaceState` (no back-button pollution)

**DetailModal.vue**
- Add "Copy Link" button in the header area
- Use `navigator.clipboard.writeText()` to copy the URL
- Show brief "Copied!" feedback via a reactive ref with timeout

**useAlgorithms.js**
- Add `getAlgorithmBySlug(slug)` helper — converts slug back to name and looks up
- Add `toSlug(name)` utility

### Data Flow
```
Page Load → check hash → getAlgorithmBySlug → openDetail
User clicks "Detail →" → openDetail → set hash
User clicks "Copy Link" → copy current URL to clipboard
User closes modal → clear hash (replaceState)
```
