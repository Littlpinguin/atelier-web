---
name: animation-scroll-reveal
description: "Apparitions au défilement en CSS natif (animation-timeline view(), scroll()) avec repli IntersectionObserver ou reveal.js : fondu, montée, cascade, image qui se découvre, barre de lecture, parallaxe légère. À charger après motion-defilement pour faire apparaître des blocs au scroll, ou pour maintenir ou migrer un projet sous AOS (data-aos), qu'on n'ajoute plus à un projet neuf."
---

# animation-scroll-reveal : apparitions au défilement, natif d'abord

La grammaire du mouvement (durées, courbe, un seul moment orchestré par section, rien ne bouge à la sortie, mouvement réduit) vit dans la skill `motion-defilement` et prime sur ce qui suit. Cette skill donne les recettes d'apparition, écrites pour les trois moteurs de navigateur : `animation-timeline` existe dans Chrome et Edge depuis la 115, Safari depuis la 26 et Firefox depuis la 159 (sortie le 27/10/2026, données de compatibilité de MDN). Un navigateur plus ancien reçoit le repli, et un visiteur en mouvement réduit voit tout, tout de suite.

## 1. Décider

| Situation | Faire |
|---|---|
| Page assemblée par la fabrique | Rien à ajouter : poser `data-reveal` (`up`, `left`, `right`, `scale`, `fade`) ou `data-reveal-group` sur les blocs, le moteur `reveal.js` du socle les révèle une fois. Ne jamais ajouter un second moteur |
| Effet lié à la progression du défilement (barre de lecture, paragraphe qui s'encre, parallaxe) | CSS natif seul (§ 3), sans JavaScript |
| Page hors fabrique, apparition simple | Recette du § 2 |
| Apparition jouée une seule fois et qui ne doit jamais se rejouer (compteur, rideau) | Le moteur d'apparition (`IntersectionObserver`), pas le CSS piloté par le défilement, qui se rejoue à l'envers quand on remonte |
| Épinglage avec scrub, texte cinétique, timeline longue | Skill `animation-gsap` |
| Projet qui emploie déjà AOS | § 5 |

## 2. Recette de base : CSS natif, repli par observateur

Le contenu reste visible sans JavaScript et en mouvement réduit : l'état masqué ne s'applique que sous `@supports` ou une fois le repli démarré.

```html
<div class="bloc" data-reveal>…</div>
```

```css
@keyframes apparition {
  from { opacity: 0; translate: 0 36px; }
}

@media (prefers-reduced-motion: no-preference) {
  /* Natif : l'apparition suit l'entrée de l'élément dans la fenêtre. */
  @supports (animation-timeline: view()) {
    [data-reveal] {
      animation: apparition linear both;
      animation-timeline: view();            /* après le raccourci animation, qui le remet à zéro */
      animation-range: entry 0% entry 90%;   /* fixe dès qu'il est entré */
    }
  }
  /* Repli : déclenché une fois par le script. */
  .rv-repli [data-reveal] {
    opacity: 0;
    translate: 0 36px;
    transition: opacity 0.85s cubic-bezier(0.16, 1, 0.3, 1), translate 0.85s cubic-bezier(0.16, 1, 0.3, 1);
  }
  .rv-repli [data-reveal].est-entre { opacity: 1; translate: none; }
}
```

```js
// Repli seulement si le natif manque et que le mouvement est permis.
(function () {
  var reduit = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var natif = window.CSS && CSS.supports && CSS.supports('animation-timeline: view()');
  if (reduit || natif || !('IntersectionObserver' in window)) return;
  document.documentElement.classList.add('rv-repli');
  var obs = new IntersectionObserver(function (entrees) {
    entrees.forEach(function (e) {
      if (!e.isIntersecting) return;
      obs.unobserve(e.target);
      e.target.classList.add('est-entre');
    });
  }, { rootMargin: '0px 0px -15% 0px', threshold: 0 });   // seuil 0 : un bloc plus haut que l'écran entre aussi
  document.querySelectorAll('[data-reveal]').forEach(function (el) { obs.observe(el); });
})();
```

## 3. Variantes

- **Gauche, droite, échelle** : changer le `from` (`translate: -40px 0`, `translate: 40px 0`, `scale: 0.96`) dans une `@keyframes` par variante, sélectionnée par la valeur de `data-reveal`.
- **Cascade dans une grille** : en natif, les enfants d'une même rangée entrent ensemble ; décaler leur plage d'entrée avec un rang posé en ligne (`style="--i: 2"`) : `animation-range: entry calc(var(--i) * 5%) entry calc(60% + var(--i) * 5%)`. En repli, `transition-delay: calc(var(--i) * 0.08s)`. Huit rangs au plus.
- **Image qui se découvre** : `from { clip-path: inset(0 0 100% 0); }` sur le conteneur de l'image, jamais sur l'image LCP du hero.
- **Barre de progression de lecture** : une barre fixe en `transform-origin: left`, `animation: progression linear both; animation-timeline: scroll(root);` avec `@keyframes progression { from { transform: scaleX(0); } }`. Décorative : `aria-hidden="true"`.
- **Parallaxe légère** : `animation-timeline: view(); animation-range: cover;` et un déplacement de 40 px au plus, sur un élément décoratif seulement, jamais sur du texte.
- **Paragraphe qui s'encre au défilement** : modèle dans le fragment `letter` de la fabrique (`${CLAUDE_PLUGIN_ROOT}/fabrique/templates/sections/letter.html`).

## 4. Pièges

- **Ordre des propriétés** : `animation-timeline` écrit avant le raccourci `animation` est remis à `auto`, et l'animation se joue au chargement.
- **Rejeu à l'envers** : une apparition pilotée par le défilement se rejoue quand l'élément ressort par le bas. Borner la plage à `entry` (§ 2) ; pour un effet unique, passer par le repli.
- **`visibility: hidden`** interdit sur un titre ou un bouton en attente : il sort du clavier et des lecteurs d'écran. Opacité et position seulement.
- **Élément LCP** : le titre et l'image du hero ne partent jamais d'une opacité nulle, ni en natif ni en repli.
- **Deux moteurs** : `data-aos`, `data-reveal` du socle et une recette maison sur la même page donnent des doubles apparitions. Un seul moteur par page.
- **Captures sans tête** : elles ne déclenchent pas toujours les observateurs ; voir la skill `qa-rendu` avant de conclure à un bug.
- **`will-change`** : seulement sur un problème constaté, puis retiré.

## 5. Projets qui emploient déjà AOS

AOS (dernière version 2.3.4 du 03/10/2018, la 3.0.0-beta.6 n'a jamais été stabilisée) se maintient tel quel s'il fonctionne ; on ne l'ajoute plus. Pour migrer une page :

| AOS | Équivalent |
|---|---|
| `data-aos="fade-up"` | `data-reveal` (ou `data-reveal="up"`) |
| `data-aos="fade-right"` (entre par la gauche) | `data-reveal="left"` |
| `data-aos="fade-left"` (entre par la droite) | `data-reveal="right"` |
| `data-aos="zoom-in"` | `data-reveal="scale"` |
| `data-aos="fade"` | `data-reveal="fade"` |
| `data-aos-delay` | rang `--i` (cascade, § 3) |
| `data-aos-once="true"` | comportement par défaut du repli ; en natif, plage bornée à `entry` |
| `AOS.refresh()` après un changement du DOM | observer les nouveaux éléments ; avec GSAP, `ScrollTrigger.refresh()` |

Retirer ensuite `aos.css`, `aos.js` et l'appel `AOS.init()`, puis vérifier en mouvement réduit que tout s'affiche (`qa-landing.py`, passage en mouvement réduit). L'API complète d'AOS, pour un projet qu'on maintient : `references/aos_api.md`, `references/animation_catalog.md` et le guide d'origine `references/aos-guide.md`.

---

*Réécrite pour l'atelier web le 25/10/2026 : l'enseignement par défaut passe au CSS natif. La skill d'origine (`scroll-reveal-libraries` v1.0.0 de [claudedesignskills](https://github.com/freshtechbro/claudedesignskills), freshtechbro, licence MIT, © 2025 Claude Skills Project) reste dans `references/` pour les projets AOS existants. Attribution et procédure de re-synchronisation : `${CLAUDE_PLUGIN_ROOT}/docs/sources/vendored-animation.md`.*
