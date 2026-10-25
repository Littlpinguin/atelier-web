---
name: revue
description: "Revue d'une page web avant de la montrer ou de la livrer : rendu mesuré (débordements, contrastes, fonds, captures, mouvement réduit), interface (jetons de la marque, états, responsive) et accessibilité WCAG 2.2 AA. Pour « vérifie le rendu », « ça déborde ? », « fais une capture », « revue de la page », « vérifie l'accessibilité »."
---

# revue : juger la page rendue avant de la montrer

Trois angles, une règle : mesurer d'abord avec des scripts, regarder ensuite les captures, puis laisser l'humain regarder la page lui-même. Un code qui a l'air juste peut donner une page cassée, et une capture qui a l'air cassée peut tromper.

## Décider l'angle

| La demande | Angle | Lire | Qui relit |
|---|---|---|---|
| « Vérifie le rendu », « ça déborde ? », « fais une capture », QA après construction ou retouche | Rendu | `references/rendu.md` | le contrôleur, avec `qa-landing.py` et `controle-fonds.py` |
| « Revue de la page », « le design ne fait pas pro », conformité aux jetons, états, responsive | Interface | `references/interface.md` | agent `landing-reviewer-design` pour une landing (phase 7) |
| Accessibilité, WCAG, clavier, focus, contrastes, lecteur d'écran | Accessibilité | `references/accessibilite.md` | agents `landing-reviewer-a11y` (code et mesures) et `a11y-auditor` (rendu réel, avant livraison) |

Une revue avant livraison couvre les trois angles ; une question ciblée, le sien. Le fond éditorial relève de `brand-check`.

## Avant de commencer

1. Lire le bloc « Atelier web » du `CLAUDE.md` du projet : commande d'aperçu, outils autorisés pour voir un rendu (certains projets interdisent de piloter un navigateur).
2. Lire `atelier/marque/style-guide.md`, `tokens.json` et `design.md` : la conformité à la marque est la priorité 0 de toute revue. Doctrine absente : le dire et limiter la revue aux règles génériques.
3. Prévisualiser la sortie du build, jamais des sources qui portent encore des marqueurs d'inclusion.

## Règles

- **Mesurer avant de conclure** : `python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/qa-landing.py <page.html> --format json` (trois tailles d'écran puis mouvement réduit), `controle-fonds.py` pour la continuité des fonds. Sans Playwright, le dire : la revue reste statique et son verdict partiel.
- **Revue d'abord, correction sur validation** : le rapport liste les constats sans toucher au code. Les agents relecteurs ne modifient rien ; le contrôleur applique.
- **Chaque constat est actionnable** : où (fichier et ligne, ou sélecteur), taille d'écran, critère (WCAG cité pour l'accessibilité), gravité (bloquant, majeur, mineur), correction sous contrainte de marque (un jeton de `tokens.json`, jamais une couleur inventée).
- Bloquants et majeurs se corrigent avant livraison ; les mineurs se consignent.
- Captures et rapports vont dans le scratchpad, jamais dans le dépôt.
- L'œil de l'humain reste la dernière porte : lui donner l'URL locale et la liste des points à regarder (hero, jonctions de fonds, moments animés, formulaire, mobile).

## Références

| Fichier | Contenu |
|---|---|
| `references/rendu.md` | Mesures (`qa-landing.py`, `controle-fonds.py`), tailles de capture, Playwright et Chrome sans tête, pièges du rendu sans tête qui font conclure à tort, format du rapport |
| `references/interface.md` | Grille par priorité : P0 marque, puis accessibilité, interaction, performance perçue, style, mise en page, typographie, animation, formulaires ; checklist express |
| `references/accessibilite.md` | Référentiel WCAG 2.2 AA : structure, clavier et focus, ARIA, modales, formulaires, contrastes, contenus dynamiques, tableaux, liens, sévérités |

Provenance : `${CLAUDE_PLUGIN_ROOT}/docs/sources/vendored-design.md` (interface) et `vendored-content.md` (accessibilité).
