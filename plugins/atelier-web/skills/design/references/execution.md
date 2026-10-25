# Exécuter : protocole anti-slop

## Sommaire

- Invariants (à relire en reprenant une session)
- Place parmi les skills design
- Étape 0 — Charger la marque (OBLIGATOIRE)
- 1. Lecture du brief (avant tout code)
- 2. Les trois curseurs
- 5. Directives d'exécution (correction de biais)
- 6. Mouvement
- 7. Performance et accessibilité
- 8. Tells d'IA (motifs interdits)
- 9. Pre-flight check

Ce protocole ne choisit pas un style : il empêche l'exécution de ressembler à du design généré. Il s'applique aux landing pages, pages marketing, portfolios et refontes ; pas aux dashboards denses, tables de données ou interfaces produit à étapes (y prendre un design system officiel).

## Invariants (à relire en reprenant une session)

**Ordre, sans sauter d'étape** : 0. charger la marque → 1. lire le brief et **déclarer la lecture design en une ligne** → 2. fixer les trois curseurs → 3-4. système officiel et pile si le projet en a un (`stack-et-systemes.md`) → 5. exécuter sous les règles dures → 6. mouvement motivé → 7. performance et accessibilité → 8. chasse aux tells → 9. **pre-flight check**, case par case, avant de livrer.

**Préséance** : `atelier/marque/style-guide.md` et `tokens.json` > `atelier/marque/checklist-pre-composition.md` > `atelier/marque/design-anti-generique.md` > les règles de ce protocole. Une dimension fixée par la marque (couleur, police, rayon) ne se discute pas ; les règles ci-dessous ne s'appliquent pleinement que là où la marque est muette.

**Validations** : une seule question de clarification si le brief est ambigu, jamais une rafale ; curseurs annoncés et motivés, modifiés seulement à voix haute ; une case du pre-flight qui ne se coche pas honnêtement = le livrable n'est pas fini.

**Pre-flight check (étape 9)** : dans le `SKILL.md` de la skill `design` (§ Pre-flight), commun aux routes créer et refondre.

**Chemins** : `stack-et-systemes.md` (étapes 3-4 : systèmes officiels, pile React, polices, icônes) ; skill `motion` (mouvement en HTML statique, et ses squelettes React `${CLAUDE_PLUGIN_ROOT}/skills/motion/references/squelettes-react.md` pour l'étape 6) ; provenance : `${CLAUDE_PLUGIN_ROOT}/docs/sources/vendored-design2.md`.

## Place parmi les skills design

Dans la skill `design`, `direction.md` choisit la direction visuelle au cadrage, `systeme.md` pose les jetons sémantiques sous contrainte de marque, `refonte.md` audite et modernise un existant ; `ui-ux-pro-max` (plugin tiers, s'il est installé) sert de base de choix (palettes, paires de polices, styles). **Ce protocole** est l'exécution, pendant et après l'écriture du code. Ordre type : direction → système → production (`landing-page`, `page-web`) avec ce protocole en garde-fou → pre-flight.

## Étape 0 — Charger la marque (OBLIGATOIRE)

1. Lire `atelier/marque/style-guide.md` (couleurs, police, rayon, dégradé, illustration, interdits visuels), `checklist-pre-composition.md` (anti-style-IA et typographie ; elle fait foi contre les bans de cette skill : si elle autorise le demi-cadratin `–`, le ban ne porte que sur le cadratin `—`) et `design-anti-generique.md`.
2. Classer chaque dimension : **verrouillée par la marque** (aucune dérogation, même si un ban ci-dessous suggère autre chose) ou **libre** (le protocole s'applique pleinement). Une marque violette reste violette malgré la règle « LILA ».
3. Si `style-guide.md` manque ou contient des `{{...}}` : s'arrêter et proposer la skill `demarrer-projet-web`.

## 1. Lecture du brief (avant tout code)

Lire le **type de page** (landing SaaS, grand public, agence, événement ; portfolio ; refonte à préserver ou à refondre ; éditorial), les **mots d'ambiance** (« minimaliste », « premium », « brutaliste »…), les **références** (URL, captures, concurrents), l'**audience** (c'est elle qui choisit l'esthétique) et les **contraintes silencieuses** (accessibilité renforcée, secteur régulé, confiance d'abord), qui priment sur le goût.

Déclarer en une ligne : *« Je lis ceci comme : \<type de page> pour \<audience>, langage \<ambiance>, penchant vers \<famille esthétique ou design system>. »* Inférence confiante : déclarer et avancer.

**Discipline anti-défaut** : jamais de dégradé violet d'IA, de hero centré sur mesh sombre, de trois cartes identiques, de glassmorphism partout, de micro-animations en boucle sur tout, d'Inter + slate-900 par réflexe. Ce sont les défauts du modèle : s'en écarter délibérément selon la lecture.

## 2. Les trois curseurs

- **`DESIGN_VARIANCE`** : 1 = symétrie parfaite, 10 = chaos artistique
- **`MOTION_INTENSITY`** : 1 = statique, 10 = cinématique et physique
- **`VISUAL_DENSITY`** : 1 = galerie d'art, 10 = cockpit de données

Base : `8 / 6 / 4`.

| Signal du brief | VARIANCE | MOTION | DENSITY |
|---|---|---|---|
| minimaliste / calme / éditorial / Linear-style | 5-6 | 3-4 | 2-3 |
| premium grand public / luxe | 7-8 | 5-7 | 3-4 |
| joueur / expérimental / agence | 9-10 | 8-10 | 3-4 |
| landing / portfolio / site marketing (défaut) | 7-9 | 6-8 | 3-5 |
| confiance d'abord / public / régulé / a11y critique | 3-4 | 2-3 | 4-5 |
| refonte, préserver | = existant | +1 | = existant |
| refonte, refondre | +2 | +2 | = existant |

- **VARIANCE 1-3** : grille symétrique, marges égales, centré. **4-7** : chevauchements, ratios d'image variés, titres à gauche. **8-10** : masonry, colonnes fractionnaires (`2fr 1fr 1fr`), grands vides. **Sous 768 px, les niveaux 4 à 10 passent en une colonne stricte.**
- **MOTION 1-3** : `:hover` et `:active` seulement. **4-7** : transitions fluides (`cubic-bezier(0.16,1,0.3,1)`), cascades d'entrée, `transform` et `opacity` seulement. **8-10** : chorégraphie au défilement (CSS `animation-timeline` d'abord, GSAP ScrollTrigger pour l'épinglage). `window.addEventListener('scroll')` est un ban dur.
- **DENSITY 1-3** : `py-32` à `py-48`. **4-7** : `py-16` à `py-24`. **8-10** : marges serrées, filets de 1 px au lieu de cartes, chiffres en `font-mono`.

## 5. Directives d'exécution (correction de biais)

### 5.1 Typographie
- Display : `text-4xl md:text-6xl tracking-tighter leading-none`. Corps : `text-base leading-relaxed max-w-[65ch]`.
- Sans par défaut : Geist, Outfit, Cabinet Grotesk, Satoshi (Inter si demandé, ou brief neutre ou a11y). **Une police imposée par la marque s'impose.**
- **Discipline serif** : « brief créatif = serif » est le tell le plus testé. Serif seulement si la marque la nomme, ou si l'univers est vraiment éditorial, luxe ou patrimoine, et justifiable. `Fraunces` et `Instrument Serif` bannis comme défauts. Emphase d'un titre = italique ou gras de la MÊME police, jamais un mot serif dans un titre sans-serif.
- Mot italique avec `y g j p q` en display : `leading-[1.1]` au moins et réserve `pb-1`.

### 5.2 Couleur
- Un accent au plus, saturation < 80 % par défaut. **Règle LILA** : pas de violet d'IA ni de néon par défaut, sauf marque violette.
- **Verrou de cohérence** : un accent choisi vaut pour TOUTE la page.
- **Ban de la palette premium** : beige ou crème + laiton, terre cuite ou ocre + espresso pour tout brief artisan, bien-être ou luxe est banni comme défaut. Alternatives : luxe froid (argent, chrome), forêt (vert profond, os, ambre), noir + tan, cobalt + crème, terracotta + ardoise, monochrome + un seul accent saturé. Sauf si la marque nomme ces couleurs.
- Une seule famille de gris (chaude OU froide).

### 5.3 Mise en page — règles dures (en manquer une = livrable cassé)
- **Le hero tient dans la fenêtre initiale** : titre ≤ 2 lignes sur ordinateur, sous-texte ≤ 20 mots et ≤ 4 lignes, CTA visible sans défiler. Un titre de hero sur 4 lignes est une erreur de taille de police.
- **Pile du hero, 4 éléments texte au plus** : un sur-titre OU un bandeau de marque (zéro ou un), titre, sous-texte, CTA (1 primaire + 1 secondaire au plus). Bannis dans le hero : mini-slogan sous les CTA, micro-bandeau de confiance, prix, liste de fonctions, rangée d'avatars. Marge haute `pt-24` au plus.
- Le mur de logos vit SOUS le hero, jamais dedans.
- **Anti-centrage** : hero centré évité si `DESIGN_VARIANCE > 4` (sauf manifeste ou éditorial).
- **Navigation** : une ligne sur ordinateur, 80 px de haut au plus.
- **Sur-titres** (règle la plus violée) : au plus 1 sur-titre en capitales espacées pour 3 sections, hero compris ; contrôle mécanique : compte > ceil(nbSections / 3) = échec. À la place : rien, le titre suffit.
- **Ban du split-header** : gros titre à gauche + petit paragraphe flottant à droite, banni par défaut. Empiler (titre, puis corps en 65ch).
- **Zigzag** : 2 sections consécutives en alternance image et texte au plus ; la troisième échoue au pre-flight. Casser avec une pleine largeur, un bento ou un bandeau.
- **Familles de mise en page** : une famille (3 cartes, citation pleine largeur, texte et image côte à côte…) apparaît au plus UNE fois par page ; ≥ 4 familles pour 8 sections.
- **Bento** : exactement autant de cellules que de contenus (jamais de tuile vide) ; 2 ou 3 cellules au moins avec une vraie variation visuelle (image, dégradé de marque, motif), pas six cartes blanches sur fond blanc.
- Repli mobile explicite par section pour tout multi-colonnes.

### 5.4 Surfaces, états, formulaires
- Des cartes seulement quand l'élévation exprime une hiérarchie ; sinon filets, `divide-y`, espace. Ombres teintées du fond, jamais noir pur.
- **Verrou de forme** : UNE échelle de rayons par page, ou une règle documentée appliquée partout.
- États complets : chargement (squelettes qui épousent la mise en page finale, pas de spinner), vide (composé, dit comment remplir), erreur (en ligne pour un formulaire), retour tactile (`:active` → `scale-[0.98]`).
- **Contraste des CTA** : WCAG AA 4,5:1 (3:1 au-delà de 18 px) ; bouton fantôme sur photo → voile ou bordure. **Un libellé de CTA tient sur une ligne** (3 mots au plus) ; **un seul libellé par intention**.
- Formulaires : label AU-DESSUS du champ, erreur dessous, jamais de placeholder en guise de label ; contraste AA sur placeholders, focus et aides.

### 5.5 Images et assets
Priorité : **1)** l'outil d'images du projet, après `atelier/marque/assets/index.md` (un asset existant se réutilise) ; **2)** de vraies photos (`https://picsum.photos/seed/{seed-descriptif}/{w}/{h}`, sources de la marque) ; **3)** en dernier recours, des emplacements étiquetés (`<!-- TODO: photo hero produit, 1600x1200 -->`), à signaler.
- Même un site minimaliste a besoin de 2 ou 3 vraies images : une page 100 % texte est un travail incomplet.
- **Fausses captures en `<div>` bannies** (faux dashboard, fausse liste, faux terminal).
- Mur de logos : vrais SVG (Simple Icons : `https://cdn.simpleicons.org/{slug}`) ou monogramme SVG pour une marque inventée, jamais des noms en texte brut ; des logos et rien d'autre (pas d'étiquette de catégorie sous chaque logo).
- SVG décoratifs dessinés à la main : fortement découragés.

### 5.6 Densité de contenu et copie
- Section par défaut : titre ≤ 8 mots + paragraphe ≤ 25 mots + un visuel OU un CTA.
- Pas de section fourre-tout (table de 20 lignes sur une page marketing) : 3 à 5 éléments puis « tout voir », un carrousel ou une autre page. Une liste de plus de 5 éléments devient un autre composant (grille de cartes, onglets, pastilles en défilement, groupes), pas un `<ul>` plus long avec un filet sous chaque ligne.
- **Relecture obligatoire** de chaque chaîne visible : réécrire ce qui est cassé, flou ou « sonne LLM » (checklist de marque § 2 et skill `ecriture`, mode relire).
- **Chiffres faussement précis bannis** : une donnée sourcée (`messaging-framework.md`) ou un exemple étiqueté.
- Citations : ≤ 3 lignes, nom + rôle (+ entreprise), guillemets typographiques.
- **Verrou de thème** : un thème par page ; aucune section n'inverse le mode en plein défilement (sauf un bloc de couleur délibéré, une fois). Les bandes sombres prévues par la charte d'une landing de la fabrique échappent à ce verrou.

## 6. Mouvement

**Mouvement motivé** : chaque animation se justifie en une phrase (hiérarchie, narration, retour, transition d'état) ; « ça faisait joli » = suppression. **Un bandeau défilant par page au plus.** « Mouvement annoncé = mouvement livré » : si `MOTION_INTENSITY > 4`, la page bouge vraiment ; sinon baisser le curseur à 3 et livrer un statique propre.

Pile et grammaire : skill `motion` (CSS natif d'abord, GSAP pour l'épinglage avec scrub, dotLottie pour les médias). Squelettes React corrigés (épinglage `start: "top top"`, défilement horizontal, cascade Motion) : `${CLAUDE_PLUGIN_ROOT}/skills/motion/references/squelettes-react.md`.

Interdits : `window.addEventListener("scroll", …)` (utiliser le CSS piloté par le défilement, ScrollTrigger, `IntersectionObserver` ou `useScroll()`) ; progression calculée avec `window.scrollY` dans un état React ; boucles `requestAnimationFrame` qui touchent l'état React ; GSAP ou Three.js mélangés à Motion dans le même arbre de composants.

## 7. Performance et accessibilité

- Animer UNIQUEMENT `transform` et `opacity` ; `will-change` avec parcimonie.
- **`prefers-reduced-motion` obligatoire** au-dessus de `MOTION_INTENSITY` 3 : boucles, parallaxe, épinglages et physique deviennent statiques.
- **Mode sombre** : concevoir les deux modes dès le départ (sauf éditorial qui imite l'imprimé, ou décision de la marque) ; une stratégie de jetons par projet (`dark:` OU variables CSS) ; jamais `#000000` ni `#ffffff` purs ; hiérarchie et fidélité à la marque équivalentes dans les deux modes ; tester les deux avant de livrer.
- Core Web Vitals : LCP < 2,5 s (hero préchargé), INP < 200 ms, CLS < 0,1.
- Grain ou bruit sur pseudo-élément `fixed inset-0 pointer-events-none` seulement, jamais sur un conteneur qui défile.
- Échelle de `z-index` documentée, pas de `z-[9999]`.

## 8. Tells d'IA (motifs interdits)

Complète la § 2 de `atelier/marque/checklist-pre-composition.md` (le texte) par les tells **visuels** :

- **Visuel et CSS** : halos néon, noir pur, accents sursaturés, texte en dégradé sur les grands titres, curseurs personnalisés.
- **Mise en page** : trois cartes identiques ; marges mathématiquement parfaites sans intention.
- **Contenu** : « John Doe » et avatars génériques ; chiffres trop ronds (`99.99%`) ; noms de marque creux (« Acme », « Nexus », « SmartFlow ») ; verbes creux (« Elevate », « Seamless », « Unleash »).
- **Micro-étiquettes** : sur-titres numérotés (`001 · Capabilities`) ; étiquettes de version dans le hero (`V0.6`, `BETA`) hors lancement ; pagination `01 / 4` sur les images ; point médian `·` rationné (un par ligne de métadonnées au plus) ; pastilles de statut décoratives.
- **Copie marketing** : « Quietly trusted by », étiquettes poétiques, bandeaux météo ou heure locale, micro-phrases sous les sur-titres, « Step 1 / Step 2 » (le verbe d'action EST l'étiquette).
- **Décoration** : pastilles posées sur les photos ; faux crédits photo ; numéro de version en pied de page marketing ; bandeau en capitales mono en bas du hero ; texte vertical pivoté ; **indices de défilement bannis** (« ↓ scroll ») ; filet haut et bas sur chaque ligne d'une longue liste ; barres de progression avec piste de fond comme visuel comparatif.
- **Tiret cadratin (`—`)** : banni partout dans le rendu (titres, corps, citations, boutons, alt), conformément à la checklist de marque § 2b : demi-cadratin `–`, virgule, deux-points, parenthèses ou reformulation.

## 9. Pre-flight check

La liste est dans le `SKILL.md` de la skill `design` (§ Pre-flight), commune aux routes créer et refondre. La dérouler avant de livrer le code.

---

*Vendorisée et condensée depuis [taste-skill](https://github.com/Leonxlnx/taste-skill) de Leonxlnx (skill `design-taste-frontend` v2, licence MIT). Le 25/10/2026 (atelier-web 1.1.0), invariants et pre-flight remontés en tête, pile React et squelettes de mouvement déplacés dans `references/`. Fusionnée dans la skill `design` le 25/10/2026 (atelier-web 1.2.0). Pre-flight remonté dans son `SKILL.md`, squelettes React passés dans la skill `motion`. Attribution, périmètre retenu et procédure de re-synchronisation : `${CLAUDE_PLUGIN_ROOT}/docs/sources/vendored-design2.md`.*
