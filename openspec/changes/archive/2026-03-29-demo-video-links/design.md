# Design: Demo Video Links

## Data Model
Add optional `demoVideoId` (string) field to each algorithm object in `algorithms.json`. Only present for algorithms with a matching demo video.

## Video Matching
Videos from Eventide's official playlist matched by title pattern:
- `H90 Harmonizer® Pedal Demo: {Algorithm} Algorithm` → exact match
- Granular walkthrough → Cosmic Web, Glitch, GrainMod, Stutter
- Harmonizer+ vocal → VocalShift, VocalShiftMIDI, VocalTune, Quadravox+

## UI
- **AlgorithmCard.vue**: YouTube icon button next to "Detail →", with `@click.stop` to prevent card interaction
- **DetailModal.vue**: YouTube icon button in header next to copy-link and close buttons
- Both use `target="_blank" rel="noopener"`, `title="Sound Demo"` for hover tooltip
- Icon: YouTube logo SVG, hover color red-500
- Only rendered when `algo.demoVideoId` exists
