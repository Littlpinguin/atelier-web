# Lottie : médias animés de marque en dotLottie

## Sommaire

- 1. Quoi prendre
- 2. Avant d'intégrer
- 3. Recette : HTML statique
- 4. Animation pilotée par le défilement
- 5. CSP, auto-hébergement, React
- 6. Migrer depuis lottie-web ou lottie-react
- 7. Références

Une animation Lottie est un média, comme une vidéo : elle illustre une idée, elle ne remplace ni une apparition au défilement (CSS natif, `apparitions.md`) ni une transition d'interface (CSS ou Motion). La grammaire commune du mouvement vit dans le `SKILL.md` de la skill `motion` et prime.

## 1. Quoi prendre

| Besoin | Outil |
|---|---|
| Page HTML statique, fabrique de l'atelier | Composant `<dotlottie-wc>` (`@lottiefiles/dotlottie-wc`, 0.10.0 au 25/10/2026) |
| Contrôle fin en JavaScript (canvas, segments, pilotage au défilement) | `@lottiefiles/dotlottie-web` (0.81.0), classe `DotLottie` |
| React ou Next.js | `@lottiefiles/dotlottie-react` (0.20.0), composant `DotLottieReact` |
| Animation interactive à états (survol, clic, machine à états) | dotLottie et son interactivité, ou Rive (vérifier sa licence d'export) |
| Projet existant sous lottie-web ou `lottie-react` | Les garder s'ils marchent ; migrer au prochain chantier (§ 6). Ne plus les ajouter : lottie-web n'a plus de version depuis le 21/05/2025 (5.13.0) et `lottie-react` s'appuie dessus |

Fichier : `.lottie` (archive ZIP qui regroupe une ou plusieurs animations, leurs images et leurs thèmes) plutôt que `.json`. Versions vérifiées sur npm le 25/10/2026 : toujours figer la version dans l'URL ou le `package.json`, jamais `@latest`.

## 2. Avant d'intégrer

- **Couleurs de la marque** : l'animation s'exporte avec les couleurs de `atelier/marque/tokens.json`, ou porte un thème dotLottie à ces couleurs. `lint-brand.py` ne lit pas l'intérieur d'un `.lottie` : vérifier à l'œil sur le rendu, contre les jetons.
- **Droits et divulgation** : une animation achetée ou téléchargée (LottieFiles, banque) se note dans `atelier/marque/droits.md` ; une animation générée suit `atelier/marque/divulgation-ia.md`.
- **Poids** : le moteur WASM du lecteur pèse environ 500 Ko compressés (README de dotlottie-web) et se télécharge au premier lecteur construit. Une animation n'entre donc jamais dans le premier écran d'une page qui vise un bon LCP, sauf décision de l'humain ; au-delà du premier écran, charger le composant à l'approche (§ 3).

## 3. Recette : HTML statique

```html
<figure class="illustration-animee">
  <dotlottie-wc data-lottie src="assets/anim/tournee.lottie" loop loopcount="2"
                role="img" aria-label="Le tracé de la tournée se dessine de dépôt en dépôt"
                style="width: min(100%, 420px); aspect-ratio: 1"></dotlottie-wc>
  <button type="button" class="lottie-pause" hidden>Mettre en pause</button>
</figure>
```

```js
// Lecture à l'entrée dans l'écran, jamais en mouvement réduit, chargement du lecteur à l'approche.
(function () {
  var reduit = matchMedia('(prefers-reduced-motion: reduce)').matches;
  var obs = new IntersectionObserver(function (entrees) {
    entrees.forEach(function (e) {
      if (!e.isIntersecting) return;
      obs.unobserve(e.target);
      import('https://cdn.jsdelivr.net/npm/@lottiefiles/dotlottie-wc@0.10.0/dist/dotlottie-wc.js').then(function () {
        customElements.whenDefined('dotlottie-wc').then(function () { lancer(e.target); });
      });
    });
  }, { rootMargin: '200px 0px' });
  document.querySelectorAll('dotlottie-wc[data-lottie]').forEach(function (el) { obs.observe(el); });

  function lancer(el) {
    var attendre = setInterval(function () {
      var lecteur = el.dotLottie;
      if (!lecteur || !lecteur.isLoaded) return;
      clearInterval(attendre);
      if (reduit) { lecteur.setFrame(lecteur.totalFrames - 1); return; }   // état final, immobile
      lecteur.play();
      // Plus de cinq secondes de mouvement (WCAG 2.2.2) : bouton pause visible.
      var boucle = el.hasAttribute('loop');
      var replays = boucle ? Number(el.getAttribute('loopcount') || 0) : 0;
      var bouton = el.parentElement.querySelector('.lottie-pause');
      if (bouton && ((boucle && replays === 0) || lecteur.duration * (replays + 1) > 5)) {
        bouton.hidden = false;
        bouton.addEventListener('click', function () {
          var enPause = lecteur.isPaused;
          enPause ? lecteur.play() : lecteur.pause();
          bouton.textContent = enPause ? 'Mettre en pause' : 'Reprendre';
        });
      }
    }, 100);
  }
})();
```

- `loop loopcount="2"` : trois lectures en tout (la première plus deux), puis l'animation s'arrête. C'est la règle des animations infinies du `SKILL.md`, § 1 (trois itérations au plus).
- Un mouvement automatique de plus de cinq secondes, à côté d'autre contenu, exige un moyen de le mettre en pause (WCAG 2.2.2, niveau A) : le script affiche le bouton dès que la boucle est sans fin ou que la durée totale (`duration`, en secondes, fois le nombre de lectures) dépasse cinq secondes.
- Une animation décorative prend `aria-hidden="true"` au lieu de `role="img"` et d'un `aria-label` ; une animation qui porte une information garde son équivalent en texte à côté.
- Sans JavaScript ou sans WebAssembly, rien ne s'affiche : prévoir une image fixe en repli si l'illustration porte du sens (le premier ou le dernier état exporté en SVG ou WebP).

## 4. Animation pilotée par le défilement

La progression d'une scène épinglée pilote l'image courante. Avec GSAP (`gsap.md`) :

```js
ScrollTrigger.create({
  trigger: '#methode', start: 'top top', end: '+=150%', scrub: true,
  onUpdate: function (self) {
    var l = document.querySelector('#methode dotlottie-wc').dotLottie;
    if (l && l.isLoaded) l.setFrame(Math.round(self.progress * (l.totalFrames - 1)));
  }
});
```

Sans GSAP, la même progression se calcule depuis la position de la piste collante (`SKILL.md`, § 5). En mouvement réduit : la dernière image, fixe.

## 5. CSP, auto-hébergement, React

- **WASM auto-hébergé** : par défaut, le lecteur va chercher son `.wasm` sur jsDelivr ou unpkg. Pour le servir depuis le site : copier `dist/dotlottie-player.wasm` de `@lottiefiles/dotlottie-web` (même version que le lecteur) et appeler `setWasmUrl('/js/dotlottie/dotlottie-player.wasm')` (exporté par `dotlottie-wc`) avant le premier chargement. Une adresse explicite coupe le repli vers le CDN : un mauvais chemin échoue en `loadError`.
- **CSP stricte** : autoriser la compilation WebAssembly (`script-src 'wasm-unsafe-eval'`) et l'origine du `.wasm` dans `connect-src` ; la variante worker démarre depuis une URL `blob:` (`worker-src blob:`), sinon auto-héberger `dotlottie.worker.js` et appeler `setWorkerUrl`. À vérifier sur la page assemblée avant la mise en ligne.
- **React** : `import { DotLottieReact } from '@lottiefiles/dotlottie-react'` puis `<DotLottieReact src="/anim/tournee.lottie" loop autoplay={!reduit} />`, avec `reduit` lu par `useReducedMotion()` de Motion ou un `matchMedia`.

## 6. Migrer depuis lottie-web ou lottie-react

| Avant | Après |
|---|---|
| `lottie.loadAnimation({ container, path: 'x.json', loop, autoplay })` | `<dotlottie-wc src="x.lottie" loop>` ou `new DotLottie({ canvas, src: 'x.lottie', loop, autoplay })` |
| `animation.goToAndStop(n, true)` | `lecteur.setFrame(n)` |
| `animation.play()`, `.pause()`, `.destroy()` | `lecteur.play()`, `.pause()`, `.destroy()` |
| `<Lottie animationData={json} />` (lottie-react) | `<DotLottieReact src="x.lottie" />` |
| Fichier `.json` | Le convertir en `.lottie` (Lottie Creator, outils LottieFiles) ; le `.json` reste lisible par dotLottie |

Rendu à vérifier après migration : couleurs, taille du canvas (le lecteur dessine dans un `canvas` à la taille de l'élément), mouvement réduit.

## 7. Références

- `lottie-api.md` : API de dotlottie-web et, pour la maintenance, de lottie-web et lottie-react.
- `lottie-after-effects.md` : réglages d'export Bodymovin, fonctions d'After Effects non prises en charge.
- `lottie-performance.md` : poids des fichiers, rendu, mémoire.
- `lottie-guide-origine.md` : la skill d'origine, pour un projet qui garde lottie-web.

---

*Réécrite pour l'atelier web le 25/10/2026 : dotLottie devient le lecteur par défaut et l'API enseignée a été vérifiée sur `dotlottie-wc` 0.10.0. La skill d'origine (`lottie-animations` v1.0.0 de [claudedesignskills](https://github.com/freshtechbro/claudedesignskills), freshtechbro, licence MIT, © 2025 Claude Skills Project) reste dans `lottie-guide-origine.md`. Fusionnée dans la skill `motion` le 25/10/2026 (atelier-web 1.2.0). Attribution et procédure de re-synchronisation : `${CLAUDE_PLUGIN_ROOT}/docs/sources/vendored-animation.md`.*
