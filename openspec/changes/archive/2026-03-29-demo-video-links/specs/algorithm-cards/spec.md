# algorithm-cards Delta Spec — Demo Video Links

## MODIFIED Requirements

### Requirement: Detail modal
A detail modal (`DetailModal.vue`) SHALL display full parameter information for an algorithm when the "Detail →" button is clicked. The modal SHALL include a "Copy Link" button for sharing and a YouTube "Sound Demo" button when a demo video is available.

#### Scenario: YouTube demo button in modal
- **WHEN** the modal is open for an algorithm with a `demoVideoId`
- **THEN** a YouTube icon button with tooltip "Sound Demo" SHALL be visible in the header
- **WHEN** the user clicks the YouTube button
- **THEN** the demo video SHALL open in a new browser tab

#### Scenario: No demo video
- **WHEN** the modal is open for an algorithm without a `demoVideoId`
- **THEN** no YouTube button SHALL be rendered

### Requirement: Algorithm card display
Each algorithm SHALL be displayed as a card showing the algorithm name, category icon, category label, overview text, parameter grid, performance parameter circles, and an info bar.

#### Scenario: YouTube demo button on card
- **WHEN** a card renders for an algorithm with a `demoVideoId`
- **THEN** a YouTube icon button with tooltip "Sound Demo" SHALL appear next to the "Detail →" button
- **WHEN** the user clicks the YouTube button
- **THEN** the demo video SHALL open in a new browser tab without triggering other card interactions

## ADDED Requirements

### Requirement: Demo video data
Algorithms MAY have an optional `demoVideoId` field containing a YouTube video ID linking to an official Eventide demo video.

#### Scenario: Video link format
- **WHEN** a `demoVideoId` is present
- **THEN** it SHALL be used to construct the URL `https://www.youtube.com/watch?v={demoVideoId}`
