const categoryIcons = {
  Delay: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 12h3l2-3 2 6 2-6 2 3h3"/><path d="M18 8l3 4-3 4" opacity="0.5"/></svg>`,
  Distortion: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h2l2-7 3 14 3-14 3 14 2-7h2"/></svg>`,
  EQ: `<svg viewBox="0 0 24 24" fill="currentColor"><rect x="3" y="10" width="2.5" height="8" rx="0.5"/><rect x="7.5" y="6" width="2.5" height="12" rx="0.5"/><rect x="12" y="3" width="2.5" height="15" rx="0.5"/><rect x="16.5" y="8" width="2.5" height="10" rx="0.5"/></svg>`,
  Granular: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 17l5-10 5 10 5-10 5 10"/><circle cx="7" cy="12" r="1" fill="currentColor" stroke="none"/><circle cx="17" cy="12" r="1" fill="currentColor" stroke="none"/></svg>`,
  Harmonizer: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 6l10 12L22 6"/><path d="M2 18L12 6l10 12"/></svg>`,
  'Harmonizer+': `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 6l8 12L18 6"/><path d="M2 18L10 6l8 12"/><line x1="20" y1="9" x2="20" y2="15"/><line x1="17" y1="12" x2="23" y2="12"/></svg>`,
  Looper: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="7" cy="12" r="4"/><circle cx="17" cy="12" r="4"/><circle cx="12" cy="5" r="3" opacity="0.6"/></svg>`,
  Modulation: `<svg viewBox="0 0 24 24" fill="currentColor"><rect x="2" y="4" width="4" height="16" rx="1"/><rect x="10" y="4" width="4" height="16" rx="1"/><rect x="18" y="4" width="4" height="16" rx="1"/></svg>`,
  Multi: `<svg viewBox="0 0 24 24" fill="currentColor"><path d="M2 20V16h4v4H2zm5-4V12h4v8H7zm5-8V4h4v16h-4zm5 0V8h5v12h-5z" opacity="0.9"/></svg>`,
  Reverb: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 18V6h4v12"/><path d="M10 18V9h4v9" opacity="0.7"/><path d="M17 18v-5h4v5" opacity="0.4"/></svg>`,
  Synth: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="4"/><line x1="12" y1="2" x2="12" y2="6"/><line x1="12" y1="18" x2="12" y2="22"/><line x1="2" y1="12" x2="6" y2="12"/><line x1="18" y1="12" x2="22" y2="12"/><line x1="4.9" y1="4.9" x2="7.8" y2="7.8"/><line x1="16.2" y1="16.2" x2="19.1" y2="19.1"/><line x1="4.9" y1="19.1" x2="7.8" y2="16.2"/><line x1="16.2" y1="7.8" x2="19.1" y2="4.9"/></svg>`,
  Utility: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94L6.73 20.15a2.1 2.1 0 01-3-3l6.72-6.72a6 6 0 017.94-7.94l-3.76 3.77z"/></svg>`,
}

export function useCategoryIcons() {
  function getIconSvg(category) {
    return categoryIcons[category] || ''
  }

  return { getIconSvg }
}
