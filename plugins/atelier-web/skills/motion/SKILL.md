---
name: motion
description: "Mouvement d'une page web, natif d'abord : apparitions et animations pilotées par le défilement en CSS, épinglage et scrub avec GSAP, séquences anime.js, illustrations dotLottie, mouvement réduit et pause, migration depuis AOS ou lottie-web. Pour « c'est trop statique », « rends ça vivant », « anime cette section », « épingle », « parallaxe », « Lottie »."
---

# motion : du mouvement qui sert la lecture

Le mouvement rend une page vivante quand il raconte quelque chose : une section qui arrive, une méthode qui se déroule, un chiffre qui se pose. Il la rend pénible quand tout bouge tout le temps. La règle : un vocabulaire commun pour toute la page, et un seul moment orchestré par section.

Le mouvement du site existant prime : lire `atelier/marque/design.md` (§ mouvement) avant tout. Ce qui suit vaut par défaut, et c'est la porte d'entrée de tout le mouvement de l'atelier : les références par outil (§ 8) viennent après.

## 0. La pile : monter d'un niveau seulement quand le précédent ne sait pas faire

| Niveau | Usage | Outil |
|---|---|---|
| 0, sans JavaScript | apparitions, barre de progression, parallaxe légère, texte qui s'encre, entrées de modale, ressorts | CSS piloté par le défilement (`animation-timeline: view()` ou `scroll()`, § 4), `@starting-style`, `linear()`, View Transitions dans un même document |
| 0, repli | la même apparition, jouée une fois | le moteur d'apparition de la page (`reveal.js` de la fabrique, ou un `IntersectionObserver`) |
| 1 | narration épinglée avec scrub, texte cinétique, timelines longues, morphing SVG | GSAP 3.15 avec ScrollTrigger et SplitText, dans `gsap.matchMedia()` ; anime.js 4 pour une séquence sans GSAP |
| 2, en option | défilement fluide, sur les pages vitrines seulement | Lenis 1.3 (§ 3) |
| Médias | illustration ou icône animée de marque | dotLottie : composant `dotlottie-wc` (`references/lottie.md`) |
| React ou Next.js | micro-interactions, présence, mise en page animée | `motion` 14.6 (`motion/react`) ; GSAP avec `useGSAP` pour les séquences |
| Plus pour un projet neuf | | AOS (sans version depuis 2018), lottie-web (depuis mai 2025), Theatre.js et Barba (depuis 2024) : un projet qui les emploie les garde, on ne les ajoute pas |

Versions relevées sur npm le 25/10/2026 : figer la version dans l'URL ou le `package.json`, jamais `@latest`. Le CSS piloté par le défilement fonctionne dans Chrome et Edge 115, Safari 26 et Firefox 159 (sortie le 27/10/2026, données de compatibilité de MDN) ; le `@supports` et le repli couvrent les autres.

## 1. Le vocabulaire commun

- **Un seul moteur d'apparition par page** (celui du site, ou `reveal.js` de la fabrique). Les éléments portent un attribut (`data-reveal="up|left|right|scale"`), le moteur les révèle.
- **Entrées en opacité et position seulement.** Jamais `visibility: hidden` (ni `autoAlpha` de GSAP) sur un titre ou un bouton : il sort du clavier et des lecteurs d'écran tant qu'il n'est pas révélé.
- **Durées et courbe** : blocs en 0,8 à 0,9 s, montée de 30 à 44 px, décalage de 0,06 à 0,12 s entre éléments ; courbe douce qui décélère (`cubic-bezier(0.16, 1, 0.3, 1)`, `power3.out`). Un rebond seulement si la marque le revendique, et réservé à un type de bloc (par exemple les grilles en bento qui « éclosent »).
- **Un seul moment orchestré par section**, pas trois.
- **Rien ne bouge à la sortie** : un chiffre compte à l'entrée puis reste fixe, un rideau ne se referme pas en remontant.
- **Animations infinies** (pulsations, ondes) : trois itérations au plus.
- **Inclinaison 3D** : ±6° au plus, sur des objets physiques seulement (carte, billet), avec un pointeur fin (`(hover: hover) and (pointer: fine)`).
- **Survols** : 150 à 400 ms ; soulèvement de quelques pixels et bordure dans la couleur d'accent.

## 2. Déclencher les apparitions sans piège

- `IntersectionObserver` avec `rootMargin` négatif en bas (par exemple `0px 0px -15% 0px`) pour que l'entrée se voie.
- **Seuil 0 sur tout bloc plus haut que l'écran**, plus un filet au défilement qui révèle tout bloc dont le haut est entré dans la fenêtre. Un seuil de 0,08 sur une section de 9 000 px ne se déclenche jamais : le visiteur voit une colonne vide.
- Contenu révélé après un choix ou un onglet : construire ses animations après la révélation, puis recalculer les déclencheurs (`ScrollTrigger.refresh()` avec GSAP).
- Les captures sans tête ne déclenchent pas ces observateurs de façon fiable : voir `${CLAUDE_PLUGIN_ROOT}/skills/revue/references/rendu.md` avant de conclure à un bug.

## 3. Défilement fluide (Lenis)

Il donne une impression plus soignée sur ordinateur, à condition de le borner :
- **À la molette seulement** : jamais au toucher (l'inertie native y est meilleure), jamais en `prefers-reduced-motion: reduce`.
- **Branché une seule fois** dans le script commun du site ; une page qui doit garder le défilement natif le déclare (par exemple `<html data-defilement="natif">`).
- **Toute fenêtre modale ou zone qui défile seule** porte `data-lenis-prevent` ou `aria-modal="true"`, ou verrouille la page (`body.style.overflow = 'hidden'`) : sinon la page défile derrière.
- Bibliothèque hébergée avec le site si sa CSP refuse les CDN, version dans le nom du fichier, licence MIT en tête.
- Un test qui saute par `window.scrollTo` attend que le glissé se pose (environ 1,5 s après un coup de molette), sinon Lenis termine son glissé et annule le saut.

## 4. Animations liées au défilement, en CSS natif

- `animation-timeline: view()` ou `scroll()`, toujours dans `@supports (animation-timeline: view())` **et** `@media (prefers-reduced-motion: no-preference)`, avec en repli la version déclenchée une fois par le moteur d'apparition (le script teste `CSS.supports('animation-timeline: view()')`). Recette complète, testée : `references/apparitions.md`, § 2.
- Écrire `animation-timeline` **après** le raccourci `animation`, qui le remet à zéro.
- Une animation pilotée par le défilement se rejoue à l'envers quand on remonte : borner la plage d'une apparition à `entry` (fixe dès que l'élément est entré) ; un compteur ou un rideau qui ne doit jouer qu'une fois passe par le moteur d'apparition.
- Une seule règle décide où une scène se joue (une constante du script, le même seuil dans le CSS), et un mode léger sur machine faible ou en économie de données.

## 5. Épinglages et scènes

- **Épingler en CSS** : `position: sticky` sur une piste haute (`height: calc(100vh + étapes × N vh)`). La progression vient d'une timeline de défilement nommée (`view-timeline` sur la piste, `animation-timeline` sur ce qui avance, sous `@supports`) ou de ScrollTrigger avec `scrub` ; GSAP ne fait que l'échelle, l'opacité et le scrub, sans `pin: true`. Jamais un écouteur `scroll` qui recalcule à chaque événement : la skill `design` le bannit (`${CLAUDE_PLUGIN_ROOT}/skills/design/references/execution.md`, § 6).
- Une section épinglée **se bloque pour de bon**. Une animation qui raconte une progression (tracé, allumage successif) s'épingle, sinon le visiteur voit un état intermédiaire.
- Trois épinglages au plus par page, jamais deux d'affilée sans respiration, environ sept écrans de défilement captif au total, sauf décision contraire de l'humain.
- Requête d'épinglage typique : `(min-width: 1101px) and (min-height: 720px) and (prefers-reduced-motion: no-preference)`. En dessous, la scène se déroule à plat.
- Un `overflow-x: hidden` sur `main` ou `body` casse `position: sticky` : préférer `overflow-x: clip`.
- Un titre épinglé ne passe pas sous la barre du site : retrait haut égal à la hauteur de la barre plus une marge.

## 6. Transitions entre sections

- **Fondu inversé** : la section qui part s'efface, la suivante apparaît, sans superposition. Dérive ou rideau seulement là où ils apportent, en lien avec le défilement.
- **Jamais de cartes qui s'empilent** au défilement.
- **Rien entre le hero et la section suivante** : le hero défile simplement.

## 7. Mouvement réduit

`prefers-reduced-motion: reduce` : rien ne bouge, tout est visible, les états finaux s'affichent d'emblée (compteurs à leur valeur, scènes à leur dernière étape, animation Lottie sur sa dernière image). La QA le vérifie (`qa-landing.py`, passage en mouvement réduit).

Tout mouvement automatique de plus de cinq secondes affiché à côté d'autre contenu (bandeau défilant, carrousel automatique, boucle Lottie, vidéo d'ambiance) porte un moyen visible de le mettre en pause (WCAG 2.2.2, niveau A).

## 8. Références, par outil

Chaque fichier se lit au moment où l'outil entre en jeu ; la grammaire ci-dessus prime sur eux.

| Besoin | Lire |
|---|---|
| Apparitions au défilement en CSS natif, variantes, repli, migration depuis AOS | `references/apparitions.md` |
| Timelines, ScrollTrigger, scrub, épinglage, SplitText, SVG (toujours dans `gsap.context` ou `gsap.matchMedia`, nettoyé au démontage) | `references/gsap.md`, puis `references/gsap-api.md`, `references/gsap-patterns.md`, `references/gsap-easing.md` |
| Séquences, décalages, morphing SVG sans GSAP | `references/animejs.md`, puis `references/animejs-api.md`, `references/animejs-stagger.md`, `references/animejs-timeline.md` |
| Illustrations et icônes animées en dotLottie, pilotage au défilement, CSP, migration depuis lottie-web | `references/lottie.md`, puis `references/lottie-api.md`, `references/lottie-after-effects.md`, `references/lottie-performance.md` |
| Projet React : épinglage, défilement horizontal, cascade Motion | `references/squelettes-react.md` |
| Projet existant sous AOS ou lottie-web, à maintenir | `references/aos-api.md`, `references/aos-catalogue.md`, `references/aos-guide.md` ; `references/lottie-guide-origine.md` |

Les fichiers d'origine (GSAP, anime.js, Lottie, AOS) viennent de claudedesignskills (MIT) et restent en anglais ; provenance : `${CLAUDE_PLUGIN_ROOT}/docs/sources/vendored-animation.md`. Pour la 3D, Three.js et les bibliothèques de composants animés (Magic UI, React Bits), voir les outils complémentaires du README de l'atelier.
