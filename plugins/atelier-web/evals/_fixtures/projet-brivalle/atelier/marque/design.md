# Système de design : brivalle.example

> Fixture de test du plugin atelier-web : site **fictif**. Le site n'a pas encore de feuille de style propre : ses pages de conversion s'assemblent depuis la fabrique de l'atelier (`fabrique/templates/assets/base.css`, `tokens.css` généré depuis `atelier/marque/tokens.json`). Valeurs exactes : `tokens.json`, qui fait foi.

## 1. Fondations

| Variable | Usage |
|---|---|
| `--brand-light` | Fond de page, papier légèrement chaud |
| `--brand-surface-2` | Cartes teintées |
| `--brand-accent` | Bouton de conversion, un seul accent par écran |
| `--brand-dark` | Titres, bandes sombres |
| `--brand-muted` | Métadonnées, légendes |

**Typographie** : Inter pour les titres et le corps ; JetBrains Mono réservée aux horaires, chiffres de tableau et étiquettes, jamais en corps de texte. Titres de section en graisse 800.

**Rayons** : cartes 16 px, boutons et badges en pilule, champs 8 px.

## 2. Éléments signature

- **Le tracé de tournée** : une ligne fine qui relie les étapes d'un programme ou d'un parcours, comme un itinéraire sur un plan.
- **Les horaires en mono** : toute heure ou durée s'écrit en JetBrains Mono.

## 3. Composants

Les sections de la bibliothèque de la fabrique (`fabrique/templates/sections/`) servent de composants. Aucune feuille maison à côté.

## 4. Mouvement

- Apparitions : moteur `reveal.js` de la fabrique (`data-reveal`), entrées en opacité et position.
- Pas de défilement fluide.
- `prefers-reduced-motion` respecté partout : tout visible, rien ne bouge.

## 5. Règles dures

- Pas de pastille de sur-titre au-dessus des titres.
- Fonds continus : une section finit sur la couleur où commence la suivante.
- Aucun chiffre inventé : seuls ceux de `messaging-framework.md`, avec la mention « chiffre d'exemple ».

## 6. Décisions de la marque

| Date | Retour | Règle |
|---|---|---|
| 2026-10-25 | Fixture créée pour les évals | Aucune |
