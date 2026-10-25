# Journal des versions

## 1.0.0 · 2026-10-25

Première version.

- Plugin `atelier-web` : 24 skills, 7 agents, hook de lint de marque, fabrique (44 sections, 6 modèles de landing, 10 outils interactifs), modèles de doctrine.
- Extrait de la verticale web du marketing-cockpit-template (commit `eb01596`), découplé de l'arborescence du cockpit : la doctrine vit dans `atelier/marque/` du projet, les scripts lisent le projet courant (`ATELIER_PROJET`, `ATELIER_MARQUE`).
- Ajouts tirés de jessem.fr : `demarrer-projet-web`, `page-web`, `qa-rendu`, `motion-defilement`, `controle-fonds.py`, modèle `design.md`.
- Corrections au passage : conflit de nom dans `qa-landing.py`, marqueurs `{{MARKER}}` en commentaire qui faisaient échouer le lint des pages assemblées, en-têtes YAML de cinq skills et agents.
- `outils-complementaires/installer.sh` : installation de l'atelier et des plugins tiers depuis leur source.
- Référencement : README anglais et français, aperçu de partage, démos en ligne (`docs/`, GitHub Pages), README et licence dans le dossier du plugin avec la description de ce qu'il exécute et va chercher, métadonnées en anglais. Le catalogue des sections se génère dans le projet (`catalogue.json`) et n'est plus livré dans le plugin (limite de 256 Ko de l'annuaire officiel).
