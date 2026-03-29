# Proposal: SEO Optimization

## Problem
The site had no meta tags, favicon, OG/Twitter cards, or structured data — resulting in poor search engine visibility and blank social media previews.

## Solution
Add comprehensive SEO meta tags, favicon (waveform SVG), OG image, JSON-LD structured data, and optimize Google Fonts loading for better FCP/LCP performance.

## Scope
- `index.html`: meta description, canonical, OG, Twitter Card, JSON-LD, favicon links, non-blocking font loading
- `main.css`: system font fallback stack
- `public/`: favicon.svg, og-image.png, apple-touch-icon.png
- `scripts/generate-og-image.mjs`: reproducible image generation
- `package.json`: add description
