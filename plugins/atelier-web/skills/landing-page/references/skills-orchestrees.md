# Skills orchestrées par le playbook

Ce que chaque skill apporte au playbook `landing-page`, à quelle phase, et ce qui la remplace si elle manque dans la session.

| Skill | Rôle dans le playbook | Repli si absente |
|---|---|---|
| `cro` | Structure CRO (phase 3, `page.md`), formulaire de capture (`formulaire.md`) et regard CRO en revue | Ordre des objections de `references/charte.md` § 7 ; règles formulaire de `references/sections.md` |
| `ecriture` | Textes définitifs de la spec (rédiger), relecture (relire) | Aucun : obligatoire |
| `design` | Directions (phase 2), système visuel et protocole d'exécution, sous les jetons de `atelier/marque/tokens.json` | Bibliothèque `${CLAUDE_PLUGIN_ROOT}/fabrique/templates/sections/` + `style-guide.md` |
| `motion` | Pile et grammaire du mouvement, épinglages, défilement fluide, mouvement réduit | Charte § 5 |
| `page-web` | Sections reprises du site, fonds continus, rythme des largeurs, pièges techniques du site | `atelier/marque/design.md` |
| `revue` | Rendu (captures aux tailles de référence, fonds, pièges du rendu sans tête), interface (grille lue par `landing-reviewer-design`), accessibilité (référentiel WCAG 2.2 AA chargé avant de construire, lu par `a11y-auditor`) | `qa-landing.py` seul ; grilles des agents |
| `lead-magnet` | Circuit complet si la page capture un email contre un contenu | Règles formulaire de `references/sections.md` |
| Outil d'images du projet | Visuels manquants, après la bibliothèque et accord sur le coût | Assets de `atelier/marque/assets/` |
| `brand-check` | Validation finale obligatoire | Aucun : obligatoire |
