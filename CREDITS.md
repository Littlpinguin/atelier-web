# Provenance et licences

## Base

L'atelier est extrait du **marketing-cockpit-template** de Jessy Martin ([Littlpinguin/marketing-cockpit-template](https://github.com/Littlpinguin/marketing-cockpit-template), licence MIT), version du commit `eb01596` (release 2.3.2) : verticale web (skills de design, de conversion, d'animation et de rédaction, playbook de landing, agents, fabrique de sections, scripts de QA, de jetons et de lint de marque), découplée de l'arborescence du cockpit. S'y ajoutent les règles tirées de la production de jessem.fr (skills `page-web` et `demarrer-projet-web`, cœur de la skill `motion`, référence `rendu.md` de la skill `revue`, script `controle-fonds.py`).

## Contenus tiers adaptés

Chaque skill adaptée garde son pied d'attribution. Les registres détaillés (ce qui a été repris, coupé, et la procédure de resynchronisation) sont dans [`plugins/atelier-web/docs/sources/`](plugins/atelier-web/docs/sources/) ; ils décrivent les chemins du cockpit d'origine, et leur README donne la correspondance avec les fichiers de la version 1.2.0.

| Source | Auteur | Repris dans | Licence |
|---|---|---|---|
| [claudedesignskills](https://github.com/freshtechbro/claudedesignskills) | freshtechbro | `motion` : `apparitions.md`, `gsap*.md`, `animejs*.md`, `lottie*.md`, `aos-*.md` | MIT |
| [frontend-design](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design) | Anthropic | `design` : `direction.md` | Apache-2.0 |
| [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Next Level Builder | `design` : `systeme.md`, `styles.md`, `palettes.md`, `typographie.md` ; `revue` : `interface.md` | MIT |
| [taste-skill](https://github.com/Leonxlnx/taste-skill) | Leonxlnx | `design` : `execution.md`, `refonte.md`, `stack-et-systemes.md` ; `motion` : `squelettes-react.md` | MIT |
| [humanize-writing](https://github.com/jpeggdev/humanize-writing) | jpeggdev | `ecriture` : `humaniser.md`, `ai-tells.md` | MIT |
| [marketingskills](https://github.com/coreyhaines31/marketingskills) | Corey Haines | `cro` : `page.md`, `formulaire.md`, `popup.md`, `tarifs.md` | MIT |
| [accessibility-agents](https://github.com/Community-Access/accessibility-agents) | Community-Access, Taylor Arndt | `revue` : `accessibilite.md` ; agent `a11y-auditor` | MIT |

Les plugins installés par `outils-complementaires/installer.sh` ne sont pas copiés ici : ils viennent de leur dépôt d'origine, sous leur propre licence.

## Licence de l'atelier

MIT (voir [`LICENSE`](LICENSE)). La notice Apache-2.0 de `frontend-design` s'applique à `plugins/atelier-web/skills/design/references/direction.md`, qui en dérive.
