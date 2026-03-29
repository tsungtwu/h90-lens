# algorithm-cards Delta Spec — Factory Presets & Preset Search

## ADDED Requirements

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
