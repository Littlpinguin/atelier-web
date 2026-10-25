# Système de design — {{NOM_DU_SITE}}

> Source de vérité visuelle du site. À **lire et appliquer avant toute page ou section**. Le principe absolu : **on réutilise le système existant, on ne recrée jamais un style « maison » à côté.** En cas de doute, ouvrir une page de référence et copier le composant.
>
> Pages de référence : `{{PAGE_REFERENCE_1}}`, `{{PAGE_REFERENCE_2}}`. Valeurs exactes : `atelier/marque/tokens.json` (ce fichier explique l'usage, `tokens.json` fait foi sur les valeurs).

---

## 1. Fondations

**Couleurs** (variables de `{{FEUILLE_PRINCIPALE}}`, `:root`)

| Variable | Usage |
|---|---|
| `{{VAR_FOND}}` | Fond principal |
| `{{VAR_FOND_ALTERNE}}` | Fond alterné, bas des dégradés entre sections |
| `{{VAR_ACCENT}}` | Accent : CTA, chiffres, mot mis en avant dans un titre. Avec parcimonie, un accent par écran |
| `{{VAR_TITRE}}` | Titres, texte fort |
| `{{VAR_TEXTE}}` | Corps |
| `{{VAR_SECONDAIRE}}` | Métadonnées, labels, texte secondaire |

**Typographie** : `{{POLICE_TEXTE}}` pour le corps et les titres ; `{{POLICE_ACCENT}}` réservée à {{USAGE_POLICE_ACCENT}}, jamais en corps de texte. Titre de section : graisse {{GRAISSE_TITRE}}, `{{TAILLE_TITRE}}`.

**Espacements** : `{{ECHELLE_ESPACEMENTS}}`. Souffle vertical d'une section par défaut : `{{PADDING_SECTION}}`.

**Rayons** : {{REGLE_RAYONS}} (exemple : 0 sur les blocs de contenu, 12 px sur les boutons, 100 px sur les pilules). Rayons concentriques : le contenant vaut le rayon du contenu plus l'écart qui les sépare.

**Curseur, défilement, particularités globales** : {{PARTICULARITES_GLOBALES}} (exemple : curseur personnalisé, ne jamais réintroduire `cursor: pointer` ; défilement fluide branché dans le script commun).

---

## 2. Éléments signature

Ce qui rend le site reconnaissable. Une page neuve les porte tous ; les oublier est l'erreur la plus visible.

- **{{SIGNATURE_1}}** : {{DESCRIPTION_ET_CODE_1}}
- **{{SIGNATURE_2}}** : {{DESCRIPTION_ET_CODE_2}}

---

## 3. Composants (réutiliser, ne pas recréer)

| Composant | Classe(s) | Feuille | Notes |
|---|---|---|---|
| Bouton principal | `{{CLASSE}}` | `{{FICHIER}}` | Tous les CTA finaux |
| Bouton secondaire | | | |
| Titre de section | | | Règles des titres (§ 5) |
| Hero | | | |
| Bloc de preuves / chiffres | | | |
| FAQ | | | Accordéon ; FAQ doublée en JSON-LD ? |
| Appel final | | | Modèle de tout bloc de conversion final |
| Navigation / pied de page | | | Partagés (partials, composants) |
| Barre du haut des pages sans menu | | | Une seule, partagée |
| Pop-up ou formulaire en étapes | | | Chaque étape tient en 1366 × 768 |

Pour réutiliser un composant hors de sa page d'origine : **charger sa feuille source** plutôt que redéfinir ses règles.

---

## 4. Mouvement

- Apparitions : `{{CLASSE_REVEAL}}` ({{DUREE_ET_COURBE}}), déclenchées par `{{SCRIPT_COMMUN}}`.
- Variante pour {{TYPE_DE_BLOC}} : `{{CLASSE_VARIANTE}}`.
- Survols : {{REGLE_SURVOL}}.
- Défilement fluide : {{REGLE_DEFILEMENT}} (fenêtres modales en `data-lenis-prevent` ou `aria-modal`).
- `prefers-reduced-motion` respecté partout : tout visible, rien ne bouge.

---

## 5. Règles dures

- {{REGLE_1}} (exemple : pas de pastille de sur-titre au-dessus des titres)
- {{REGLE_2}} (exemple : ni virgule ni point dans un titre)
- Fonds continus : une section finit sur la couleur où commence la suivante.
- Pas de données inventées : chiffres fournis ou déjà publiés.
- Images : WebP, `width` / `height`, `alt`, `loading="lazy"` hors premier écran.
- CSS et JS modifiés : lien versionné (`?v=AAAAMMJJ`) sur chaque page qui les charge.

---

## 6. Checklist avant de livrer une page

- [ ] Chaque section reprend un composant existant (§ 3) ?
- [ ] Éléments signature présents (§ 2) ?
- [ ] Règles des titres respectées ?
- [ ] Apparitions et mouvement conformes (§ 4) ?
- [ ] Fonds continus : `controle-fonds.py <url> 1440` et `390` sans coupure ?
- [ ] Responsive vérifié ({{POINTS_DE_RUPTURE}}) ?
- [ ] Textes conformes à `voice.md`, aucun chiffre inventé ?
- [ ] Images optimisées ?
- [ ] Publication selon les règles du projet ?

---

## 7. Décisions de la marque

Les retours de l'humain qui valent pour tout le site s'ajoutent ici, datés, avec la règle qu'on en tire. Ils priment sur les règles générales de l'atelier.

| Date | Retour | Règle |
|---|---|---|
| | | |
