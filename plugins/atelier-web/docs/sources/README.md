# Registres de provenance

Ces registres viennent du marketing-cockpit-template (commit `eb01596`), d'où l'atelier est extrait. Ils tracent, pour chaque contenu tiers adapté, la source, la licence vérifiée, ce qui a été repris ou coupé, et la procédure de resynchronisation.

Les chemins qu'ils citent sont ceux du cockpit : `.claude/skills/<nom>/` y correspond à `skills/<nom>/` de ce plugin, `05-web-content/` à `fabrique/`, `01-brand/` à la doctrine du projet (`atelier/marque/`).

## Correspondance avec atelier-web 1.2.0

Le 25/10/2026, les 24 skills sont devenues 10 : le contenu adapté vit désormais en références d'un seul niveau sous la skill qui l'absorbe.

| Chemin cité par les registres | Fichier de la version 1.2.0 |
|---|---|
| `.claude/skills/design-direction/` | `skills/design/references/direction.md` |
| `.claude/skills/design-taste/` | `skills/design/references/execution.md` (pre-flight dans `skills/design/SKILL.md`) et `stack-et-systemes.md` ; squelettes React : `skills/motion/references/squelettes-react.md` |
| `.claude/skills/design-system/` | `skills/design/references/systeme.md`, `styles.md`, `palettes.md`, `typographie.md` |
| `.claude/skills/design-redesign/` | `skills/design/references/refonte.md` |
| `.claude/skills/design-review/` | `skills/revue/references/interface.md` |
| `.claude/skills/accessibility-web/` | `skills/revue/references/accessibilite.md` |
| `qa-rendu` (skill maison) | `skills/revue/references/rendu.md` |
| `motion-defilement` (skill maison) | `skills/motion/SKILL.md` |
| `.claude/skills/animation-gsap/` | `skills/motion/references/gsap.md`, `gsap-api.md`, `gsap-patterns.md`, `gsap-easing.md` |
| `.claude/skills/animation-animejs/` | `skills/motion/references/animejs.md`, `animejs-api.md`, `animejs-stagger.md`, `animejs-timeline.md` |
| `.claude/skills/animation-lottie/` | `skills/motion/references/lottie.md`, `lottie-api.md`, `lottie-after-effects.md`, `lottie-performance.md`, `lottie-guide-origine.md` |
| `.claude/skills/animation-scroll-reveal/` | `skills/motion/references/apparitions.md`, `aos-api.md`, `aos-catalogue.md`, `aos-guide.md` |
| `.claude/skills/cro-page/`, `cro-form/`, `cro-popup/`, `cro-pricing/` | `skills/cro/references/page.md`, `formulaire.md`, `popup.md`, `tarifs.md` |
| `.claude/skills/copywriting/`, `copy-editing/` (skills maison du cockpit) | `skills/ecriture/references/rediger.md`, `relire.md` |
| `.claude/skills/humanize-writing/` | `skills/ecriture/references/humaniser.md`, `ai-tells.md` |

Pour une re-synchronisation, le `SKILL.md` amont se compare au fichier de référence correspondant, dont le frontmatter a été retiré.
