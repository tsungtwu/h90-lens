# Proposal: Demo Video Links

## Problem
Users have no quick way to hear what an algorithm sounds like from H90 Lens. They must separately search YouTube for demos.

## Solution
Add YouTube demo video links to algorithms that have official Eventide demo videos. Display a YouTube icon button on both the algorithm card and detail modal that opens the demo in a new tab. Hover tooltip shows "Sound Demo".

## Scope
- Add `demoVideoId` field to `algorithms.json` for algorithms with matching playlist videos
- Add YouTube icon button to `AlgorithmCard.vue` and `DetailModal.vue`
- Source playlist: Eventide's official H90 demo playlist
