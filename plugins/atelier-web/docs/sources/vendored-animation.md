# Registre des skills animation vendorisées

Ce template fonctionne en **standalone au fork** : les meilleures skills animation externes ont été copiées et adaptées dans `.claude/skills/` plutôt que référencées comme dépendances de plugins. Ce fichier est le registre de traçabilité : source, licence, adaptations, procédure de re-synchronisation.

Date de vendorisation : **2026-07-03**.

## Vue d'ensemble

| Skill du template | Source | Version source | Licence | Statut |
|---|---|---|---|---|
| `.claude/skills/animation-gsap/` | [claudedesignskills](https://github.com/freshtechbro/claudedesignskills) (freshtechbro), plugin `gsap-scrolltrigger`, skill `gsap-scrolltrigger` | v1.0.0 | MIT | ✅ Vendorisée |
| `.claude/skills/animation-animejs/` | idem, plugin `animation-components`, skill `animejs` | v1.0.0 | MIT | ✅ Vendorisée |
| `.claude/skills/animation-lottie/` | idem, plugin `animation-components`, skill `lottie-animations` | v1.0.0 | MIT | ✏️ Réécrite le 2026-10-25 (dotLottie par défaut) ; corps d'origine dans `references/guide-origine.md` |
| `.claude/skills/animation-scroll-reveal/` | idem, plugin `animation-components`, skill `scroll-reveal-libraries` | v1.0.0 | MIT | ✏️ Réécrite le 2026-10-25 (CSS natif par défaut) ; corps d'origine dans `references/aos-guide.md` |
| — | plugin `animation-components`, skills `react-spring-physics` et `animated-component-libraries` | v1.0.0 | MIT | ⛔ Non vendorisées (React-only, hors périmètre : les livrables web du template sont des fichiers HTML/CSS/JS autonomes) |
| — | plugins `threejs-webgl` et `meta-skills` (`web3d-integration-patterns`) | v1.0.0 | MIT | ⛔ Non vendorisées (3D/WebGL : trop lourd et rarement justifié pour une page marketing ; réévaluable au besoin) |

Licence constatée sur disque au moment de la copie : fichier `LICENSE` à la racine du dépôt claudedesignskills — MIT, © 2025 Claude Skills Project.

## Périmètre retenu

Pour chaque skill : **`SKILL.md` + `references/*.md` uniquement.**

Ce qui n'a **pas** été copié, et pourquoi :

- `scripts/*.py` (générateurs de boilerplate, timeline builders) : politique du template — aucun script externe n'est copié ni exécuté sans audit (cf. `vendored-design.md`, même règle). Les SKILL.md mentionnent encore ces scripts dans leur section « Resources » ; cette mention est inopérante et documentée ici.
- `assets/` (starters HTML, visualiseurs d'easing, exemples) : redondants avec les templates du dossier `atelier/` et le catalogue de slides ; réduisent le bruit au fork.

Adaptations effectuées :

- `name:` du frontmatter renommé (`animation-gsap`, `animation-animejs`, `animation-lottie`, `animation-scroll-reveal`) pour suivre la convention de nommage par famille du template.
- Footer d'attribution ajouté en fin de chaque `SKILL.md`.
- **2026-10-25, atelier-web 1.1.0** : `animation-scroll-reveal` et `animation-lottie` réécrites en français. AOS (sans version depuis le 03/10/2018) et lottie-web (sans version depuis le 21/05/2025) sortent de l'enseignement par défaut : la première enseigne le CSS piloté par le défilement avec un repli par `IntersectionObserver`, la seconde le lecteur dotLottie (`dotlottie-wc`, `dotlottie-web`, `dotlottie-react`). Le `SKILL.md` d'origine de chacune est conservé tel quel, sans son frontmatter, dans `references/` (`aos-guide.md`, `guide-origine.md`), avec les autres références d'origine, pour maintenir ou migrer un projet existant. `motion-defilement` (skill maison) devient la porte d'entrée de tout le mouvement.

## Cas d'usage dans le template

Ces skills servent aux livrables web (`atelier/`) : landing pages, lead magnets, pages d'offre. Retour d'expérience fondateur (jessem.fr, 2026-07-03) : reprise du système de reveal maison par GSAP + ScrollTrigger (compteurs de stats, staggers, parallaxe scrub, timeline de charnière narrative). Deux garde-fous à réutiliser systématiquement :

1. **`prefers-reduced-motion`** : désactiver toutes les animations JS et laisser un fallback CSS.
2. **Reveals bidirectionnels** : un élément masqué en `opacity: 0` doit se révéler quel que soit le sens du scroll ET si la page se charge déjà scrollée (restauration de position navigateur). Pattern : `gsap.set` initial + `ScrollTrigger.create` avec `onEnter` + `onEnterBack` + déclenchement immédiat si `st.progress > 0`. Ne jamais utiliser `gsap.from` + `once: true` seul : les éléments au-dessus du viewport restent invisibles au reload mi-page.
3. **CSP** : GSAP auto-hébergé (`assets/js/vendor/`) plutôt qu'un CDN si le site sert `script-src 'self'`.

## Procédure de re-synchronisation

1. `claude plugin marketplace add freshtechbro/claudedesignskills` puis `claude plugin install <plugin>@claude-design-skillstack`.
2. Comparer `~/.claude/plugins/cache/claude-design-skillstack/<plugin>/<version>/skills/<skill>/` avec la copie locale (`diff -ru`, en ignorant frontmatter `name:` et footer).
3. Reporter les changements utiles, conserver renommage + footer, mettre à jour la version dans ce registre. Pour `animation-scroll-reveal` et `animation-lottie`, le `SKILL.md` amont se compare à `references/aos-guide.md` et `references/guide-origine.md` ; le `SKILL.md` local, réécrit, ne se re-synchronise pas.
