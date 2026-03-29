# algorithm-data Specification

## Purpose
TBD - created by archiving change h90-lens-web. Update Purpose after archive.
## Requirements
### Requirement: Structured algorithm dataset
The system SHALL provide a JSON dataset (`public/data/algorithms.json`) containing all 76 H90 algorithms organized by category. Each algorithm entry MUST include: `name` (string), `category` (string), `overview` (string), `parameters` (array of objects), and `performanceParams` (array of objects).

#### Scenario: Complete category coverage
- **WHEN** the dataset is loaded
- **THEN** it SHALL contain entries for all 12 H90 categories: Delay, Distortion, EQ, Granular, Harmonizer, Harmonizer+, Looper, Modulation, Multi, Reverb, Synth, Utility

#### Scenario: Algorithm parameter structure
- **WHEN** an algorithm entry is accessed
- **THEN** each parameter SHALL contain `name` (string), `description` (string, short), `fullDescription` (string, verbatim from manual), and optional `range` (string)
- **AND** each performance parameter SHALL contain `name` (string) and `description` (string)

#### Scenario: Data sourced from official manual
- **WHEN** the dataset is compared against the H90 manual
- **THEN** all algorithm names, parameter names, and fullDescription fields SHALL match the official documentation verbatim

### Requirement: JSON file served statically
The algorithm dataset SHALL be stored as `public/data/algorithms.json` and loaded at page initialization via `fetch()` using `import.meta.env.BASE_URL` for correct path resolution on GitHub Pages.

#### Scenario: Data file loads successfully
- **WHEN** the page loads
- **THEN** the application SHALL fetch the JSON file, parse it, and populate the reactive state
- **AND** the loading guard SHALL prevent duplicate fetch calls

#### Scenario: Data load failure
- **WHEN** the JSON file fails to load
- **THEN** the page SHALL display a user-friendly error message: "Unable to load algorithm data. Please refresh the page and try again."

### Requirement: Python extraction script
The system SHALL include a Python script (`scripts/update_algorithms.py`) that extracts algorithm data from the official H90 manual HTML pages using BeautifulSoup.

#### Scenario: Extract from latest manual
- **WHEN** the script runs with default settings
- **THEN** it SHALL fetch from `https://cdn.eventideaudio.com/manuals/h90/latest/content/algorithms/`

#### Scenario: SSRF prevention
- **WHEN** the `--base-url` argument specifies a non-Eventide domain
- **THEN** the script SHALL reject the URL with a validation error

#### Scenario: Sync to public directory
- **WHEN** the script runs with `--sync-public` flag
- **THEN** it SHALL copy the output to `public/data/algorithms.json`

#### Scenario: Merge with existing data
- **WHEN** the script runs without `--fresh` flag and existing data exists
- **THEN** it SHALL merge new extractions with existing data, preserving manual edits to short descriptions and ranges

### Requirement: Agent-friendly markdown output
The system SHALL provide algorithm data in markdown format for AI agent consumption, following the llms.txt convention.

#### Scenario: Markdown files generated at build time
- **WHEN** `npm run build` is executed
- **THEN** `public/llms.md` (overview + links) and `public/llms-full.md` (all 76 algorithms with full details) SHALL be generated from `data/algorithms.json`

#### Scenario: llms.md content
- **WHEN** an agent fetches `/h90-lens/llms.md`
- **THEN** it SHALL receive a markdown file with site overview, category listing, and links to full data (markdown and JSON)

