# Systématiser : un système de design web sous contrainte de marque

Vous produisez des systèmes de design complets : tokens sémantiques, style UI, palette, typographie, échelles. Les données de référence (styles, palettes, pairings) sont condensées dans `styles.md`, `palettes.md` et `typographie.md` : elles servent de bibliothèque de fallback, jamais de source prioritaire.

## Étape 0 — Charger les design tokens de la marque (OBLIGATOIRE)

**Charger `atelier/marque/style-guide.md` — la marque PRIME sur tout style générique de cette skill.**

1. Lire `atelier/marque/style-guide.md` : couleurs, police, radius, gradient, style d'illustration, interdits visuels.
2. Lire `atelier/marque/checklist-pre-composition.md` si présent (règles anti-style-IA) et `atelier/marque/design-anti-generique.md` (doctrine design anti-générique — elle gouverne les dimensions libres, jamais celles verrouillées par la marque : celles-là viennent de `atelier/marque/style-guide.md` et, pour les valeurs exactes, de `atelier/marque/tokens.json`).
3. Classer chaque dimension du système en deux catégories :
   - **Verrouillée par la marque** — le style-guide fournit une valeur (ex. couleur primaire, police). On l'utilise telle quelle. Interdiction de la remplacer par une valeur des références de cette skill.
   - **Libre** — le style-guide est muet (ex. couleur `muted`, échelle d'espacement, style des états d'interaction). C'est le seul espace où les références de cette skill s'appliquent.

Si `atelier/marque/style-guide.md` est manquant ou contient des `{{...}}` : s'arrêter et proposer la skill `demarrer-projet-web`. Ne jamais générer un système 100 % générique pour un projet configuré.

## Étape 1 — Qualifier le besoin

Extraire du brief :
- **Type de livrable** : landing page, page produit, dashboard de reporting, page événement, espace client…
- **Type de produit / secteur** : SaaS, service B2B, agence, e-commerce, formation, communauté… (sert à choisir palette et style de fallback dans `palettes.md` et `styles.md`)
- **Tonalité** : sobre, premium, énergique, éditorial, technique…
- **Contraintes** : dark mode requis, contrainte de performance, audience accessibilité renforcée.

## Étape 2 — Composer le système

Ordre de résolution pour **chaque token** : `atelier/marque/style-guide.md` → dérivation depuis la marque (teintes, opacités) → `styles.md`, `palettes.md`, `typographie.md` → défaut neutre. Documenter la provenance de chaque valeur dans le livrable.

1. **Style UI** — choisir dans `styles.md` le style compatible avec la marque ET le type de produit. Vérifier la colonne « Ne pas utiliser pour ». Un seul style par site ; pas de mélange flat/glassmorphism aléatoire.
2. **Palette sémantique** — construire les 12 rôles à partir de la marque :

   | Rôle | Source |
   |---|---|
   | `--primary` / `--on-primary` | `color.primary` de `tokens.json` + contraste calculé |
   | `--accent` / `--on-accent` | `color.accent` (CTA) |
   | `--background` / `--foreground` | `color.light` / `color.dark` |
   | `--card` / `--card-foreground` | dérivés du background (élévation) |
   | `--muted` / `--muted-foreground` | dérivés neutres (texte secondaire ≥ 4.5:1) |
   | `--border`, `--ring`, `--destructive` | dérivés ou `palettes.md` |

   Si la marque ne fournit que 2-3 couleurs, compléter les rôles manquants par dérivation (jamais en remplaçant les couleurs fournies). `palettes.md` sert uniquement de calibration (quel niveau de saturation pour tel secteur) ou de fallback si la marque n'a pas de couleurs du tout.
3. **Typographie** — la police principale de `tokens.json` est la police de référence. Décider de son rôle (display, body ou les deux) et compléter si besoin avec un pairing de `typographie.md` compatible. Échelle type : 12 / 14 / 16 / 18 / 24 / 32 / 48 px, body ≥ 16 px, line-height 1.5–1.75.
4. **Espacement et rythme** — échelle 4/8 px (4, 8, 12, 16, 24, 32, 48, 64). Radius : celui de `tokens.json` partout, décliné en échelle (sm/md/lg) cohérente, rayons concentriques (le contenant vaut le rayon du contenu plus l'écart qui les sépare).
5. **Effets et états** — ombres/blur/gradients alignés sur le style choisi (étape 2.1) et le dégradé de marque éventuel. Chaque interactif a 4 états : default, hover, active/pressed, disabled. Transitions 150–300 ms, `transform`/`opacity` uniquement.
6. **Dark mode** (si demandé) — variantes désaturées/éclaircies, jamais une simple inversion. Re-vérifier les contrastes séparément.

## Étape 3 — Livrer les tokens

Livrer un bloc `:root` CSS prêt à coller, précédé d'un tableau récapitulatif (token, valeur, provenance : marque / dérivé / référence). Exemple de squelette :

```css
:root {
  /* Marque — atelier/marque/style-guide.md (ne pas modifier) */
  --primary: <color.primary>;
  --accent: <color.accent>;
  --background: <color.light>;
  --foreground: <color.dark>;
  --radius: <radius de tokens.json>;
  --font-sans: '<police principale>', system-ui, sans-serif;
  /* Dérivés + fallbacks références (documenter chaque choix) */
  --muted: …; --muted-foreground: …; --border: …; --ring: …;
  --space-1: 4px; --space-2: 8px; --space-3: 16px; --space-4: 24px; --space-5: 48px;
}
```

Si le livrable appartient à un dossier de production (`atelier/`), enregistrer le système à côté du livrable (ex. `atelier/landings/<slug>/design-tokens.md`) pour réutilisation.

## Garde-fous (non négociables)

- **Contraste** : texte normal ≥ 4.5:1, texte large et composants UI ≥ 3:1 (WCAG AA). Vérifier chaque paire fond/texte du système.
- **Pas d'emoji comme icônes structurelles** : SVG uniquement (Lucide, Heroicons, Phosphor), un seul set par projet, stroke cohérent.
- **Tokens sémantiques, pas de hex brut** dans les composants.
- **Un seul CTA primaire par écran** ; les actions secondaires sont visuellement subordonnées.
- **Interdits visuels de la marque** : ils l'emportent sur toute recommandation des références. Si un style de `styles.md` entre en conflit avec un interdit, écarter le style.
- Passer le résultat par la skill `revue` (angle interface) avant toute livraison de code UI.

## Références embarquées

| Fichier | Contenu | Usage |
|---|---|---|
| `styles.md` | ~20 styles UI web (quand, jamais, effets, mots-clés CSS) | Choix du style — étape 2.1 |
| `palettes.md` | ~28 palettes sémantiques par type de produit (WCAG-ajustées) | Calibration / fallback couleur — étape 2.2 |
| `typographie.md` | ~24 pairings Google Fonts par tonalité | Complément typo — étape 2.3 |

---

*Source : données condensées et adaptées de [ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) v2.5.0, © 2024 Next Level Builder, licence MIT. Adaptations : recentrage web marketing (mobile natif, Flutter, SwiftUI, BI exclus), priorité absolue aux tokens atelier/marque, suppression de la dépendance aux scripts Python. Registre : `${CLAUDE_PLUGIN_ROOT}/docs/sources/vendored-design.md`. Fusionnée dans la skill `design` le 25/10/2026 (atelier-web 1.2.0).*
