# Outils complémentaires

L'atelier fonctionne seul : ses skills de design, de conversion et d'animation sont déjà adaptées et embarquées. Les plugins ci-dessous sont ceux que j'utilise **en plus**, chacun installé depuis sa source d'origine pour suivre ses mises à jour.

| Plugin | Marketplace | Apport | Installé par |
|---|---|---|---|
| `superpowers` | `anthropics/claude-plugins-official` | Cadrage avant de construire, plans, débogage méthodique, revue de code | défaut |
| `frontend-design` | `anthropics/claude-plugins-official` | Direction esthétique, choix qui ne ressemblent pas à un gabarit | défaut |
| `ui-ux-pro-max` | `nextlevelbuilder/ui-ux-pro-max-skill` | Base complète de styles, palettes, typographies, règles UX, et skills de marque, design system et bannières | défaut |
| `gsap-scrolltrigger`, `animation-components`, `threejs-webgl`, `meta-skills` | `freshtechbro/claudedesignskills` | GSAP complet, composants animés (Magic UI, React Bits, Lottie, Anime.js), Three.js et WebGL, design web moderne | `--tout` |
| `claude-seo` | `AgriciDaniel/claude-seo` | Audit SEO technique, contenu, données structurées, GEO | `--tout` |
| `marketing-skills` | `coreyhaines31/marketingskills` | Les skills marketing d'origine en anglais (CRO, copywriting, pricing, SEO programmatique…) | `--tout` |
| `figma` | `anthropics/claude-plugins-official` | Lire et produire des maquettes Figma | `--tout` |

## Serveur MCP facultatif

**21st.dev Magic** : composants d'interface générés et inspiration de composants (scroll, sticky, ticket, stepper…). Il demande une clé personnelle, à créer sur [21st.dev](https://21st.dev/mcp) et à ajouter soi-même dans la configuration MCP de Claude Code. Ne jamais commiter cette clé.

## Navigateur

Pour regarder une page et ses références, le navigateur intégré de l'application Claude (onglet Code) suffit. La QA mesurée, elle, passe par Playwright (`pip install playwright pillow && playwright install chromium`). Si un projet interdit de piloter un navigateur, le dire dans son `CLAUDE.md` : les skills se rabattent alors sur Playwright et Chrome sans tête.
