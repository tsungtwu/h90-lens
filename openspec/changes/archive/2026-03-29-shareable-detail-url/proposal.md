# Proposal: Shareable Detail URL

## Problem
Users cannot share a direct link to a specific algorithm's detail view. When sharing the site URL, recipients always land on the homepage and must manually search for the algorithm.

## Solution
Add URL hash-based deep linking (`#algo=AlgorithmName`) so that:
1. The detail modal has a "Copy Link" button that copies a shareable URL to the clipboard
2. Opening a URL with `#algo=AlgorithmName` automatically opens the detail modal for that algorithm

## Scope
- Modify `App.vue` to read/write URL hash on modal open/close
- Modify `DetailModal.vue` to add a copy-link button
- No new dependencies required
