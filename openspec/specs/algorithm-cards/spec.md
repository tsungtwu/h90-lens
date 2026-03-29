# algorithm-cards Specification

## Purpose
TBD - created by archiving change h90-lens-web. Update Purpose after archive.
## Requirements
### Requirement: Algorithm card display
Each algorithm SHALL be displayed as a card (`AlgorithmCard.vue`) showing the algorithm name, category icon, category label, overview text, parameter grid, performance parameter circles, and an info bar. Cards SHALL use `flex-col` layout to bottom-align the info bar across cards of different heights.

#### Scenario: Card header
- **WHEN** a card renders
- **THEN** it SHALL display a category SVG icon, the algorithm name (Righteous font, italic uppercase), category label, and a "Detail →" button

#### Scenario: YouTube demo button on card
- **WHEN** a card renders for an algorithm with a `demoVideoId`
- **THEN** a YouTube icon button with tooltip "Sound Demo" SHALL appear next to the "Detail →" button
- **WHEN** the user clicks the YouTube button
- **THEN** the demo video SHALL open in a new browser tab without triggering other card interactions

#### Scenario: Overview display
- **WHEN** an algorithm has a non-empty `overview` field
- **THEN** the card SHALL display the overview text below the header

### Requirement: Parameter grid with hover/click info
Parameters SHALL be displayed as a grid of clickable tiles. Hovering a tile shows its info in the InfoBar. Clicking a tile locks the info display until clicked again or another tile is clicked.

#### Scenario: Parameter grid layout
- **WHEN** the card renders parameters
- **THEN** they SHALL display in a grid: 2 columns (mobile), 3 columns (sm), 5 columns (md+)

#### Scenario: Hover info
- **WHEN** the user hovers a parameter tile (and no parameter is locked)
- **THEN** the InfoBar SHALL display the parameter name, description, and range (if available)

#### Scenario: Click to lock
- **WHEN** the user clicks a parameter tile
- **THEN** its info SHALL be locked in the InfoBar until the same tile is clicked again

#### Scenario: Page change resets lock
- **WHEN** the user navigates to a different parameter page
- **THEN** the locked parameter SHALL be cleared

### Requirement: InfoBar without XSS risk
The InfoBar (`InfoBar.vue`) SHALL display parameter information using structured Vue props (`paramName`, `paramDescription`, `paramRange`, `isPerformance`), NOT v-html. All text SHALL be rendered via `{{ }}` interpolation.

#### Scenario: Performance parameter info
- **WHEN** a performance parameter is active
- **THEN** the InfoBar SHALL display the name, description, and a "[Performance]" tag

#### Scenario: Regular parameter info
- **WHEN** a regular parameter is active
- **THEN** the InfoBar SHALL display the name, description, and range tag (if available)

#### Scenario: No active parameter
- **WHEN** no parameter is hovered or locked
- **THEN** the InfoBar SHALL display "Hover or click a parameter to see details..."

### Requirement: Performance parameter circles
Performance parameters SHALL be displayed as circular badges alongside the parameter grid. They support the same hover/click/lock behavior as regular parameter tiles.

#### Scenario: Performance circles layout
- **WHEN** an algorithm has performance parameters
- **THEN** they SHALL display as circles in a row (mobile) or column (sm+) next to the parameter grid

#### Scenario: No performance parameters
- **WHEN** an algorithm has no performance parameters (or `performanceParams` is null/empty)
- **THEN** the performance parameter section SHALL not render

### Requirement: Parameter pagination
When an algorithm has more than 10 parameters, the parameter grid SHALL paginate.

#### Scenario: Pagination buttons
- **WHEN** an algorithm has more than 10 parameters
- **THEN** "PAGE 1", "PAGE 2", etc. buttons SHALL appear below the grid

### Requirement: Detail modal
A detail modal (`DetailModal.vue`) SHALL display full parameter information for an algorithm when the "Detail →" button is clicked. The modal SHALL include a "Copy Link" button for sharing and a YouTube "Sound Demo" button when a demo video is available.

#### Scenario: Modal content
- **WHEN** the modal opens
- **THEN** it SHALL display the algorithm name, category, overview, all parameters with fullDescription, and performance parameters

#### Scenario: ARIA compliance
- **WHEN** the modal is open
- **THEN** it SHALL have `role="dialog"`, `aria-modal="true"`, `aria-label`, and a focus trap

#### Scenario: Close modal
- **WHEN** the user clicks the overlay, the close button, or presses Escape
- **THEN** the modal SHALL close and focus SHALL return to the previously focused element

#### Scenario: YouTube demo button in modal
- **WHEN** the modal is open for an algorithm with a `demoVideoId`
- **THEN** a YouTube icon button with tooltip "Sound Demo" SHALL be visible in the header
- **WHEN** the user clicks the YouTube button
- **THEN** the demo video SHALL open in a new browser tab

#### Scenario: No demo video in modal
- **WHEN** the modal is open for an algorithm without a `demoVideoId`
- **THEN** no YouTube button SHALL be rendered

#### Scenario: Copy link button
- **WHEN** the modal is open
- **THEN** a "Copy Link" icon button SHALL be visible in the modal header
- **WHEN** the user clicks the "Copy Link" button
- **THEN** the current page URL (including `#algo=<slug>`) SHALL be copied to the clipboard
- **AND** the button SHALL show a green checkmark for 2 seconds

### Requirement: URL hash deep linking
The app SHALL support hash-based deep linking to algorithm detail views using the format `#algo=<slug>`.

#### Scenario: Open detail from URL hash
- **WHEN** the page loads with a URL hash matching `#algo=<slug>`
- **THEN** the detail modal for the matching algorithm SHALL open automatically

#### Scenario: Hash updates on modal open
- **WHEN** the user opens a detail modal
- **THEN** the URL hash SHALL update to `#algo=<slug>` for the displayed algorithm

#### Scenario: Hash clears on modal close
- **WHEN** the user closes the detail modal
- **THEN** the URL hash SHALL be cleared using `history.replaceState` (no browser history entry)

#### Scenario: Invalid hash slug
- **WHEN** the page loads with a hash slug that does not match any algorithm
- **THEN** no modal SHALL open and the hash SHALL be cleared

### Requirement: Category icon with class passthrough
`CategoryIcon.vue` SHALL render SVG icons for each category and accept class attributes via `useAttrs()` (not `props.class`) with `inheritAttrs: false`.

#### Scenario: Class applied to SVG
- **WHEN** `<CategoryIcon category="Delay" class="w-6 h-6 text-accent" />` is used
- **THEN** the class SHALL be applied to the inner `<svg>` element

### Requirement: Responsive card grid
Algorithm cards SHALL display in a responsive grid in the main layout.

#### Scenario: Desktop layout
- **WHEN** the viewport is xl (1280px+)
- **THEN** cards SHALL display in a 2-column grid

#### Scenario: Mobile layout
- **WHEN** the viewport is narrower than xl
- **THEN** cards SHALL stack in a single column

### Requirement: Demo video data
Algorithms MAY have an optional `demoVideoId` field containing a YouTube video ID linking to an official Eventide demo video.

#### Scenario: Video link format
- **WHEN** a `demoVideoId` is present
- **THEN** it SHALL be used to construct the URL `https://www.youtube.com/watch?v={demoVideoId}`

### Requirement: Demo filter
The app SHALL provide a toggle filter to show only algorithms with demo videos.

#### Scenario: Demo filter active
- **WHEN** the user clicks the "Demo" filter button
- **THEN** only algorithms with a `demoVideoId` SHALL be displayed

#### Scenario: Demo filter inactive
- **WHEN** the user clicks the "Demo" filter button again
- **THEN** the filter SHALL be removed and all algorithms SHALL be displayed

### Requirement: Factory presets display
The detail modal SHALL display factory preset names when available.

#### Scenario: Presets section in modal
- **WHEN** the modal is open for an algorithm with a non-empty `presets` array
- **THEN** a "Factory Presets" section SHALL display all preset names as pill-style tags

#### Scenario: No presets
- **WHEN** the algorithm has no `presets` field or an empty array
- **THEN** no presets section SHALL be rendered

### Requirement: Preset search
The search filter SHALL match against factory preset names.

#### Scenario: Search by preset name
- **WHEN** the user types a preset name in the search bar
- **THEN** algorithms containing a matching preset SHALL appear in results

