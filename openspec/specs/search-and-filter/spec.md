# search-and-filter Specification

## Purpose
TBD - created by archiving change h90-lens-web. Update Purpose after archive.
## Requirements
### Requirement: Real-time search filtering
The system SHALL provide a search input (`SearchBar.vue`) that filters algorithms in real-time with 150ms debounce. Filtering MUST match against algorithm names, parameter names, and overview text (case-insensitive). The debounce timeout SHALL be cleared on component unmount.

#### Scenario: Search by algorithm name
- **WHEN** the user types "black" in the search box
- **THEN** the Blackhole algorithm card SHALL be visible and non-matching algorithms SHALL be hidden

#### Scenario: Search by parameter name
- **WHEN** the user types "feedback" in the search box
- **THEN** all algorithms that have a parameter containing "feedback" SHALL be visible

#### Scenario: Search by overview text
- **WHEN** the user types "analog" in the search box
- **THEN** all algorithms whose overview contains "analog" SHALL be visible

#### Scenario: Null safety for overview
- **WHEN** an algorithm has a null or undefined overview field
- **THEN** the search SHALL not crash and SHALL treat it as an empty string

#### Scenario: Empty search shows all
- **WHEN** the search box is empty
- **THEN** all algorithms (subject to active category filters) SHALL be visible

#### Scenario: No results
- **WHEN** the search query matches no algorithms
- **THEN** the page SHALL display a "No matching algorithms found" message

#### Scenario: Keyboard shortcut
- **WHEN** the user presses "/" (and focus is not in an input)
- **THEN** the search input SHALL receive focus

### Requirement: Category filter buttons
The system SHALL display filter buttons (`CategoryFilters.vue`) for each algorithm category with count badges. Users MUST be able to click buttons to toggle category visibility. Multiple categories MAY be active simultaneously. Category counts SHALL be provided as a computed data prop (`categoryCounts` object), not a function prop.

#### Scenario: Single category filter
- **WHEN** the user clicks the "Reverb" filter button
- **THEN** only Reverb algorithms SHALL be displayed and the "Reverb" button SHALL appear in active state

#### Scenario: Multiple category filters
- **WHEN** the user clicks "Delay" and then "Reverb" filter buttons
- **THEN** both Delay and Reverb algorithms SHALL be displayed

#### Scenario: Deselect category filter
- **WHEN** the user clicks an already-active category button
- **THEN** that category SHALL be deselected

#### Scenario: No filters active shows all
- **WHEN** no category filter buttons are active
- **THEN** all algorithms SHALL be visible (subject to search query)

#### Scenario: Count badges
- **WHEN** category buttons render
- **THEN** each button SHALL display the category icon and the total number of algorithms in that category

### Requirement: Combined search and filter
Search and category filters SHALL work together. An algorithm is visible only if it matches BOTH the active search query AND at least one active category filter (or no category filter is active).

#### Scenario: Search within filtered category
- **WHEN** the user has "Delay" category active and types "mod" in search
- **THEN** only matching Delay algorithms SHALL be visible

