# algorithm-cards Delta Spec — Shareable Detail URL

## MODIFIED Requirements

### Requirement: Detail modal
A detail modal (`DetailModal.vue`) SHALL display full parameter information for an algorithm when the "Detail →" button is clicked. The modal SHALL include a "Copy Link" button for sharing.

#### Scenario: Modal content
- **WHEN** the modal opens
- **THEN** it SHALL display the algorithm name, category, overview, all parameters with fullDescription, and performance parameters

#### Scenario: ARIA compliance
- **WHEN** the modal is open
- **THEN** it SHALL have `role="dialog"`, `aria-modal="true"`, `aria-label`, and a focus trap

#### Scenario: Close modal
- **WHEN** the user clicks the overlay, the close button, or presses Escape
- **THEN** the modal SHALL close and focus SHALL return to the previously focused element

#### Scenario: Copy link button
- **WHEN** the modal is open
- **THEN** a "Copy Link" button SHALL be visible in the modal header
- **WHEN** the user clicks the "Copy Link" button
- **THEN** the current page URL (including `#algo=<slug>`) SHALL be copied to the clipboard
- **AND** the button SHALL show "Copied!" feedback for 2 seconds

## ADDED Requirements

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
