---
name: motion-defilement
description: Grammaire du mouvement d'une page web soignée - apparitions au défilement, défilement fluide (Lenis), animations liées au défilement en CSS natif, épinglages, transitions entre sections, mouvement réduit - avec les pièges qui cassent une page en production. À charger avant d'animer une page ou une section, de poser un défilement fluide, une scène épinglée ou une animation pilotée par le défilement, et quand l'utilisateur dit « c'est trop statique », « il faut que ce soit vivant », « anime cette section ». Les skills animation-gsap, animation-scroll-reveal, animation-animejs et animation-lottie donnent ensuite la technique de chaque bibliothèque.
---

# motion-defilement : du mouvement qui sert la lecture

Le mouvement rend une page vivante quand il raconte quelque chose : une section qui arrive, une méthode qui se déroule, un chiffre qui se pose. Il la rend pénible quand tout bouge tout le temps. La règle : un vocabulaire commun pour toute la page, et un seul moment orchestré par section.

Le mouvement du site existant prime : lire `atelier/marque/design.md` (§ mouvement) avant tout. Ce qui suit vaut par défaut.

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
- Les captures sans tête ne déclenchent pas ces observateurs de façon fiable : voir la skill `qa-rendu` avant de conclure à un bug.

## 3. Défilement fluide (Lenis)

Il donne une impression plus soignée sur ordinateur, à condition de le borner :
- **À la molette seulement** : jamais au toucher (l'inertie native y est meilleure), jamais en `prefers-reduced-motion: reduce`.
- **Branché une seule fois** dans le script commun du site ; une page qui doit garder le défilement natif le déclare (par exemple `<html data-defilement="natif">`).
- **Toute fenêtre modale ou zone qui défile seule** porte `data-lenis-prevent` ou `aria-modal="true"`, ou verrouille la page (`body.style.overflow = 'hidden'`) : sinon la page défile derrière.
- Bibliothèque hébergée avec le site si sa CSP refuse les CDN, version dans le nom du fichier, licence MIT en tête.
- Un test qui saute par `window.scrollTo` attend que le glissé se pose (environ 1,5 s après un coup de molette), sinon Lenis termine son glissé et annule le saut.

## 4. Animations liées au défilement, en CSS natif

- `animation-timeline: view()` ou `scroll()`, toujours dans `@supports (animation-timeline: view())` **et** `@media (prefers-reduced-motion: no-preference)`, avec en repli la version déclenchée une fois par le moteur d'apparition (le script teste `CSS.supports('animation-timeline', 'view()')`).
- Écrire `animation-timeline` **après** le raccourci `animation`, qui le remet à zéro.
- Une seule règle décide où une scène se joue (une constante du script, le même seuil dans le CSS), et un mode léger sur machine faible ou en économie de données.

## 5. Épinglages et scènes

- **Épingler en CSS** : `position: sticky` sur une piste haute (`height: calc(100vh + étapes × N vh)`), progression calculée au défilement ; GSAP ne fait que l'échelle, l'opacité et le scrub, sans `pin: true`.
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

`prefers-reduced-motion: reduce` : rien ne bouge, tout est visible, les états finaux s'affichent d'emblée (compteurs à leur valeur, scènes à leur dernière étape). La QA le vérifie (`qa-landing.py`, passage en mouvement réduit).

## 8. Technique, par bibliothèque

| Besoin | Skill |
|---|---|
| Timelines, ScrollTrigger, scrub, SVG | `animation-gsap` (toujours dans `gsap.context` ou `gsap.matchMedia`, nettoyé au démontage) |
| Apparitions simples sur une page de contenu | `animation-scroll-reveal` |
| Séquences, décalages, morphing SVG sans GSAP | `animation-animejs` |
| Animations After Effects exportées | `animation-lottie` |

Pour la 3D, Three.js et les bibliothèques de composants animés (Magic UI, React Bits), voir les outils complémentaires du README de l'atelier.
