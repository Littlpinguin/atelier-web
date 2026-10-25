# Skills orchestrées par le playbook

Ce que chaque skill apporte au playbook `landing-page`, à quelle phase, et ce qui la remplace si elle manque dans la session.

| Skill | Rôle dans le playbook | Repli si absente |
|---|---|---|
| `cro-page` | Structure CRO (phase 3) et regard CRO en revue | Ordre des objections de `references/charte.md` § 7 |
| `copywriting` / `copy-editing` | Textes définitifs de la spec | Aucun : obligatoires |
| `design-direction` / `design-system` / `design-taste` | Directions et système visuel, sous les jetons de `atelier/marque/tokens.json` | Bibliothèque `${CLAUDE_PLUGIN_ROOT}/fabrique/templates/sections/` + `style-guide.md` |
| `design-review` | Regard UI en complément de `landing-reviewer-design` | La grille de l'agent |
| `motion-defilement` | Pile et grammaire du mouvement, épinglages, défilement fluide, mouvement réduit | Charte § 5 |
| `page-web` | Sections reprises du site, fonds continus, rythme des largeurs, pièges techniques du site | `atelier/marque/design.md` |
| `qa-rendu` | Captures aux tailles de référence, continuité des fonds, pièges du rendu sans tête | `qa-landing.py` seul |
| `accessibility-web` | Référentiel WCAG 2.2 AA chargé avant de construire | Grille de `landing-reviewer-a11y` |
| `cro-form` / `lead-magnet` | Formulaire de capture ; circuit complet si la page capture un email contre un contenu | Règles formulaire de `references/sections.md` |
| Outil d'images du projet | Visuels manquants, après la bibliothèque et accord sur le coût | Assets de `atelier/marque/assets/` |
| `brand-check` | Validation finale obligatoire | Aucun : obligatoire |
