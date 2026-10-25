---
name: design
description: "Design visuel des pages web sous les jetons de la marque du projet : directions nommées par leur objet signature, exécution sans tells de design IA, refonte d'un site qui fait daté, jetons CSS (palette sémantique, typographie, rayons). Pour « propose des directions », « ça fait template » ou « fait IA », « modernise ce site », « donne-moi les jetons »."
---

# design : la marque d'abord, puis une page qu'on ne confond avec aucune autre

Une page de la marque se reconnaît à ses jetons et à un objet signature tenu de bout en bout. Cette skill réunit les quatre gestes du design visuel de l'atelier : créer une direction, l'exécuter sans tells d'IA, refondre un existant, systématiser les jetons. La marque fixe les matériaux (couleurs, polices, rayons) ; le design compose l'architecture (hiérarchie, rythme, mise en page, signature, mouvement).

## Décider la route

| La demande | Route | Lire |
|---|---|---|
| Directions pour une page neuve, un hero, une campagne ; « ça fait template » sur un livrable en cours | Créer | `references/direction.md`, puis `references/execution.md` pendant le code |
| Écrire ou corriger le code d'une page pour qu'il ne ressemble pas à du design généré | Exécuter | `references/execution.md` |
| Un site ou une page existants qui font datés ou « font IA », à moderniser sans rien casser | Refondre | `references/refonte.md`, puis `references/execution.md` |
| Jetons CSS, palette sémantique, échelle typographique, espacements, rayons, style UI | Systématiser | `references/systeme.md` |

Une demande ambiguë appelle une seule question (« partir de l'existant, ou d'une direction neuve ? »), jamais une rafale. Une landing complète passe par `landing-page`, qui appelle cette skill aux phases 2 et 4 ; une page d'un site existant, par `page-web`.

## Étape 0 : la doctrine, commune aux quatre routes

1. Lire dans `atelier/marque/` : `style-guide.md` et `tokens.json` (valeurs exactes), `design.md` (système du site, signatures, mouvement), `checklist-pre-composition.md`, `design-anti-generique.md` et `voice.md`.
2. Classer chaque dimension : **verrouillée par la marque** (couleur, police, rayon, signature : aucune dérogation, même si une règle des références suggère autre chose) ou **libre** (les références s'y appliquent pleinement). Une marque violette reste violette.
3. Une signature existante (dégradé, motif, illustration, tracé) est le premier candidat de l'objet signature : l'amplifier avant d'inventer.
4. Fichier manquant ou porteur de `{{…}}` : s'arrêter et lancer `demarrer-projet-web`. Pour refondre le site d'un tiers sans doctrine, extraire d'abord ses jetons existants (`references/refonte.md`, étape 0).

Préséance : `style-guide.md` et `tokens.json`, puis `checklist-pre-composition.md`, puis `design-anti-generique.md`, puis les règles des références.

## Règles dures, toutes routes

- Jetons seuls : aucune couleur en dur hors du `:root`, aucune police hors de `tokens.json`, une échelle de rayons par page.
- Un thème et un accent par page.
- Les défauts du modèle ne passent pas par réflexe : dégradé violet, hero centré sur maillage sombre, trois cartes identiques, émoji en guise d'icônes, texte en dégradé, et les trois looks « IA » (crème, serif et terracotta ; quasi-noir et un accent acide ; broadsheet à filets). Un brief ou une marque qui en demande un l'obtient.
- Aucun chiffre, logo, témoignage ni capture d'écran inventé ; de vraies images, ou des emplacements étiquetés et signalés.
- Le mouvement passe par la skill `motion` ; `prefers-reduced-motion` respecté partout.
- Un livrable se montre rendu et capturé (skill `revue`), jamais sur la seule lecture du code.
- Rien de ce dont dépendent le SEO, le suivi ou le remplissage automatique (URL, libellés de navigation, noms des champs) ne change sans validation de l'humain.

## Pre-flight (créer, exécuter, refondre)

À dérouler case par case avant de livrer. Une case qui ne se coche pas honnêtement : le livrable n'est pas fini.

- [ ] Jetons de la marque chargés et respectés (dimensions verrouillées intactes) ; lecture design déclarée ; curseurs explicités (`references/execution.md`, § 2) ?
- [ ] Design system officiel choisi si applicable, esthétique étiquetée honnêtement sinon ?
- [ ] **Zéro cadratin `—`** visible ; règles typographiques de la checklist de marque (pas de point final sur les titres, casse de phrase) ?
- [ ] Un seul thème, un seul accent, une seule échelle de rayons ?
- [ ] Contraste AA sur chaque CTA et champ ; aucun libellé de CTA qui passe à la ligne ; une intention = un libellé ?
- [ ] Hero : titre ≤ 2 lignes, sous-texte ≤ 20 mots, ≤ 4 éléments texte, CTA visible, `pt-24` au plus ?
- [ ] Sur-titres ≤ ceil(nbSections / 3) ; pas de split-header ; ≤ 2 zigzags consécutifs ; ≥ 4 familles de mise en page ; bento sans cellule vide et avec variation visuelle ?
- [ ] Vraies images (générées, photo, ou emplacements étiquetés) ; aucune fausse capture en `div` ; logos SVG réels ; mur de logos sans étiquettes ?
- [ ] Copie relue ; aucun chiffre inventé ; citations ≤ 3 lignes, attribuées ?
- [ ] Mouvement motivé, livré s'il est annoncé, `prefers-reduced-motion` partout au-dessus de 3, squelettes conformes (`start: "top top"`, `pin: true`), aucun `addEventListener('scroll')`, nettoyages `useEffect` stricts ?
- [ ] Mode sombre testé dans les deux modes ; `min-h-[100dvh]` ; repli mobile explicite ?
- [ ] États chargement, vide et erreur fournis ; une seule famille d'icônes autorisée ; aucun tell de `references/execution.md`, § 8 ?
- [ ] Core Web Vitals plausibles ; un seul design system dans l'arbre ?

## Références

| Fichier | Contenu |
|---|---|
| `references/direction.md` | Créer : ancrer le design dans le sujet, principes, les trois looks « IA », workflow en deux passes (plan puis critique), retenue, écrire dans le design |
| `references/execution.md` | Exécuter : lecture du brief, trois curseurs (variance, mouvement, densité), règles dures de typographie, couleur, mise en page, surfaces, images et contenu, mouvement, performance, tells visuels |
| `references/refonte.md` | Refondre : modes préserver ou refondre, audit (typographie, couleur, mise en page, états, contenu, composants, icônes, code), techniques, ordre des correctifs, ce qui ne change jamais en silence |
| `references/systeme.md` | Systématiser : ordre de résolution de chaque jeton, palette sémantique en douze rôles, typographie, espacement, états, mode sombre, bloc `:root` livré avec sa provenance |
| `references/stack-et-systemes.md` | Systèmes officiels et pile React (étapes 3 et 4 de l'exécution) |
| `references/styles.md` | Une vingtaine de styles UI web : quand, jamais, effets (route systématiser) |
| `references/palettes.md` | Palettes sémantiques par type de produit, calibration ou repli (route systématiser) |
| `references/typographie.md` | Paires typographiques par tonalité, quand la marque laisse le choix |

Provenance (frontend-design, taste-skill, ui-ux-pro-max) : `${CLAUDE_PLUGIN_ROOT}/docs/sources/vendored-design.md` et `vendored-design2.md`.
