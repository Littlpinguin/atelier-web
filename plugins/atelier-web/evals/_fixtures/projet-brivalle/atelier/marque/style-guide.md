# Visual identity — Brivalle

Source of truth for colors, typography, illustration style, and visual constraints. Read by every atelier-web skill before any page, section or visual.

**Machine-readable values live in `atelier/marque/tokens.json`** (DTCG format: palette, gradient, fonts, type scale, radii, logo clear space). It is the single source for every hex code and font stack: CSS consumers are generated from it by `python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/build-tokens.py`, and `${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/lint-brand.py` checks deliverables against it. This page explains the intent; when a value here and `tokens.json` disagree, `tokens.json` wins.

## Colors

| Role | Hex | Notes |
|---|---|---|
| Primary | `#0B5D66` | Buttons, links, highlights, key accents |
| Accent | `#F2A541` | Secondary emphasis, hover states, badges |
| Dark | `#102A30` | Body text, dark backgrounds |
| Light | `#F5F3EE` | Page backgrounds, card fills |

### Signature gradient

```
linear-gradient(90deg, #0B5D66 0%, #F2A541 100%)
```

Use for conversion blocks (final CTA sections, pricing callouts). Do not overuse — one per page max.

### Contrast constraints

- Body text on light background: AA minimum, AAA preferred
- Interactive elements: 3:1 minimum against adjacent colors
- Verify with a contrast checker before ship — the `brand-check` skill flags obvious violations but doesn't replace a real check

## Typography

| Usage | Family | Fallback stack |
|---|---|---|
| Primary display | Inter | `Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif` |
| Secondary / mono | JetBrains Mono | `JetBrains Mono, ui-monospace, "SF Mono", Menlo, monospace` |

### Weights used

- Regular (400): body copy
- Medium (500): emphasis
- Semi-bold (600): H3
- Bold (700): H1, H2
- (Add or remove per actual brand usage)

## Spacing and radius

- **Border-radius**: cartes 16 px, boutons et badges en pilule, champs 8 px
- **Base spacing unit**: 8px (multiples: 8, 16, 24, 32, 48, 64)
- **Card padding**: 24px default, 32px for hero cards
- **Section vertical rhythm**: 80-120px between major sections on desktop, 48-72px on mobile

## Illustration style

Plans de tournée stylisés : tracés fins sur fond papier, une seule couleur d'accent, aucun personnage.

Examples worth encoding:
- "Minimalist line art, single color + accent, no solid fills"
- "Isometric 3D, pastel palette, no photo-realistic elements"
- "Geometric flat, 2-3 colors per illustration, bold outlines"

## Banned visual tropes

Never produce or commission visuals featuring:

- Photos de banque d'images (poignées de main, open spaces souriants)
- Camions en 3D brillants
- Cartes du monde parcourues d'arcs lumineux

Typical items encoded here:
- Stock office photos with diverse smiling teams
- Generic handshakes
- Post-it walls
- Light-bulb-on-head "ideation" clichés
- Generic laptops on desks
- Puzzle-piece metaphors

## Logo

- Safe zone: (equal to the height of the lowercase 'x' in the wordmark)
- Minimum size: (e.g. 24px wide on screen, 15mm in print)
- Do not: recolor, rotate, distort, add effects, embed in a paragraph

Logo assets live in `atelier/marque/assets/`.

## Components (reusable patterns)

Common UI patterns used on landing pages and decks. Each should exist once, as a section of the plugin library (`fabrique/templates/sections/`) or as a component of the site, listed in `design.md`.

- Hero block (headline + sub + CTA)
- Stats showcase (3-4 big numbers in a row)
- Testimonial card
- Pricing table
- FAQ accordion
- Final CTA with gradient background

## AI image generation specifics

Any image generation tool of the project reads this file and injects the palette, typography, illustration style, and banned tropes into every prompt. No need to repeat them in individual briefs — just describe the subject.

Aucune personne générée, aucun logo tiers.

## Appendix: CSS variables (generated)

Generated from `atelier/marque/tokens.json` by `python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/build-tokens.py`. Do not edit the block below: change `tokens.json` and re-run the script (`--check` reports any drift).

```css
/* brand-tokens:start */
/* Généré depuis atelier/marque/tokens.json (python3 scripts/build-tokens.py). Ne pas éditer. */
:root {
  --color-primary: #0B5D66;
  --color-accent: #F2A541;
  --color-dark: #102A30;
  --color-light: #F5F3EE;
  --color-white: #FFFFFF;
  --color-positive: #2E9E6A;
  --color-negative: #D64545;
  --gradient-signature: linear-gradient(90deg, #0B5D66 0%, #F2A541 100%);
  --font-display: 'Inter', system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', ui-monospace, 'Menlo', monospace;
  --radius-card: 16px;
  --radius-cta: 999px;
  --radius-badge: 999px;
  --radius-input: 8px;
}
/* brand-tokens:end */
```
