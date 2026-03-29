#!/usr/bin/env node
/**
 * Generate OG image (1200x630) and Apple touch icon (180x180) from SVG templates.
 * Usage: node scripts/generate-og-image.mjs
 * Requires: npx sharp-cli
 */
import { execSync } from 'child_process'
import { writeFileSync } from 'fs'
import { resolve, dirname } from 'path'
import { fileURLToPath } from 'url'

const __dirname = dirname(fileURLToPath(import.meta.url))
const publicDir = resolve(__dirname, '..', 'public')

// Waveform path reused across assets
const waveform = 'M0.05 0.5 L0.15 0.5 L0.22 0.15 L0.32 0.85 L0.42 0.1 L0.52 0.9 L0.62 0.2 L0.72 0.8 L0.82 0.5 L0.95 0.5'

// OG Image SVG (1200x630)
const ogSvg = `<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e293b"/>
    </linearGradient>
    <linearGradient id="accent" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#60a5fa"/>
      <stop offset="100%" stop-color="#a78bfa"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="630" fill="url(#bg)"/>
  <rect x="0" y="0" width="1200" height="4" fill="url(#accent)"/>
  <!-- Waveform icon -->
  <path d="M80 315 L130 315 L160 200 L200 430 L240 180 L280 450 L320 210 L360 420 L400 315 L450 315"
        fill="none" stroke="url(#accent)" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
  <!-- Title -->
  <text x="520" y="260" font-family="sans-serif" font-weight="bold" font-size="72" fill="white">H90 Lens</text>
  <text x="520" y="340" font-family="sans-serif" font-weight="400" font-size="36" fill="#94a3b8">Eventide H90 Algorithm Reference</text>
  <text x="520" y="410" font-family="sans-serif" font-weight="300" font-size="28" fill="#64748b">76 algorithms · 12 categories · Search &amp; filter</text>
  <!-- Bottom bar -->
  <rect x="0" y="600" width="1200" height="30" fill="url(#accent)" opacity="0.3"/>
</svg>`

// Apple touch icon SVG (180x180)
const appleSvg = `<svg xmlns="http://www.w3.org/2000/svg" width="180" height="180" viewBox="0 0 180 180">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#60a5fa"/>
      <stop offset="100%" stop-color="#a78bfa"/>
    </linearGradient>
  </defs>
  <rect width="180" height="180" rx="36" fill="url(#bg)"/>
  <path d="M20 90 L38 90 L50 40 L68 140 L86 30 L104 150 L122 45 L140 135 L152 90 L165 90"
        fill="none" stroke="url(#g)" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
</svg>`

// Write SVGs then convert to PNG
const ogSvgPath = resolve(publicDir, 'og-image.svg')
const appleSvgPath = resolve(publicDir, 'apple-touch-icon.svg')

writeFileSync(ogSvgPath, ogSvg)
writeFileSync(appleSvgPath, appleSvg)

// Convert using sharp-cli
execSync(`npx sharp-cli -i "${ogSvgPath}" -o "${resolve(publicDir, 'og-image.png')}"`, { stdio: 'inherit' })
execSync(`npx sharp-cli -i "${appleSvgPath}" -o "${resolve(publicDir, 'apple-touch-icon.png')}"`, { stdio: 'inherit' })

// Clean up temp SVGs
execSync(`rm "${ogSvgPath}" "${appleSvgPath}"`)

console.log('Generated: public/og-image.png (1200x630), public/apple-touch-icon.png (180x180)')
