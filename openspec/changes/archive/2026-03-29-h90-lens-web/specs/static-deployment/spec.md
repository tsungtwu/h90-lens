## ADDED Requirements

### Requirement: Vite build for GitHub Pages
The project SHALL use Vite 8 with `base: '/h90-lens/'` for GitHub Pages deployment. The build SHALL output to `dist/` with optimized JS and CSS bundles.

#### Scenario: Production build
- **WHEN** `npm run build` is executed
- **THEN** Vite SHALL produce `dist/` with index.html, JS bundle, CSS bundle, and static assets (data/algorithms.json, llms.md, llms-full.md)

#### Scenario: Prebuild step
- **WHEN** `npm run build` is executed
- **THEN** the `prebuild` script SHALL generate `llms.md` and `llms-full.md` from algorithms.json before Vite builds

#### Scenario: Base path
- **WHEN** the site is served from GitHub Pages at `/h90-lens/`
- **THEN** all asset references and data fetches SHALL use the correct base path via `import.meta.env.BASE_URL`

### Requirement: Vue 3 + Tailwind CSS v4
The site SHALL use Vue 3 (Composition API with `<script setup>`) and Tailwind CSS v4 via `@tailwindcss/vite` plugin (build-time processing, not CDN).

#### Scenario: Tailwind theme
- **WHEN** the CSS is processed
- **THEN** custom theme colors (bg, bg-card, primary, accent, muted) SHALL be defined via `@theme` directive in `src/assets/main.css`

### Requirement: Content Security Policy
The site SHALL include a CSP meta tag in `index.html` restricting: `default-src 'self'`, `script-src 'self'`, `style-src 'self' 'unsafe-inline' https://fonts.googleapis.com`, `font-src https://fonts.gstatic.com`, `img-src 'self' data:`.

#### Scenario: CSP enforcement
- **WHEN** the page loads
- **THEN** only scripts from the same origin SHALL be allowed to execute
- **AND** styles from self, inline, and Google Fonts SHALL be allowed
- **AND** fonts from Google Fonts CDN SHALL be allowed

### Requirement: Accessibility
The site SHALL meet basic accessibility requirements.

#### Scenario: Keyboard navigation
- **WHEN** the user navigates via keyboard
- **THEN** all interactive elements SHALL be reachable via Tab, activatable via Enter/Space, and have visible focus indicators

#### Scenario: Reduced motion
- **WHEN** the user has `prefers-reduced-motion` enabled
- **THEN** animations SHALL be disabled or reduced

#### Scenario: Modal accessibility
- **WHEN** the detail modal is open
- **THEN** it SHALL have proper ARIA attributes (`role="dialog"`, `aria-modal="true"`) and trap focus within the modal
