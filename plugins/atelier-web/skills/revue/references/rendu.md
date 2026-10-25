# Rendu : juger sur le rendu, pas sur le code

Un code qui a l'air juste peut donner une page cassée, et une page qui a l'air cassée en capture peut être juste. On mesure d'abord avec des scripts, on regarde ensuite les captures, puis l'humain regarde la page lui-même : son œil reste la dernière porte.

## Avant de commencer

- Lire le bloc « Atelier web » du `CLAUDE.md` du projet : commande d'aperçu local, et **outils autorisés pour voir un rendu**. Certains projets interdisent de piloter un navigateur : dans ce cas, Chrome sans tête en ligne de commande et Playwright seulement, et l'humain ouvre la page lui-même.
- Prévisualiser la **sortie du build** (dossier `dist/`, serveur du framework), jamais des sources qui contiennent encore des marqueurs d'inclusion.
- Dépendances : `pip install playwright pillow && playwright install chromium`. Absentes : le dire, puis faire la revue statique du code (causes probables, sélecteur, correction) et donner la commande qui mesurera ; le verdict reste partiel, jamais « propre » sans mesure.

## 1. Mesurer

**Landing ou page autonome** (fichier HTML) :
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/qa-landing.py <page.html> --format json
python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/qa-landing.py <page.html> --captures <dossier du scratchpad>
```
Trois tailles d'écran (375 × 812, 768 × 1024, 1440 × 900) puis un passage en mouvement réduit : débordements, contrastes calculés, planchers typographiques, police hors marque, cibles tactiles, CTA primaire sous le pli en mobile, mots orphelins, ponctuation des titres, pastilles de sur-titre, suivi des CTA, textes masqués en mouvement réduit. Lire le JSON (`summary`, puis chaque constat) et corriger jusqu'à zéro erreur ; chaque avertissement restant se justifie.

**Continuité des fonds** (toute page, servie en local) :
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/controle-fonds.py http://localhost:<port>/<page>/ 1440
python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/controle-fonds.py http://localhost:<port>/<page>/ 390
```
« Aucune coupure » attendu. Si les sections ne sont pas des enfants directs de `main`, passer `--sections`. Le script signale tout changement net de couleur à une limite de section : une bande sombre voulue par la charte, à bord franc, sort aussi. Trancher selon `design.md` : une doctrine à fonds continus la corrige (dégradé, vague), une doctrine à bandes sombres l'assume et le rapport le dit.

**Accessibilité en rendu réel** : agent `a11y-auditor` (axe-core et parcours clavier), en complément.

## 2. Capturer et regarder

Tailles de référence : **1512 × 842** (portable 14 pouces), 1440 × 900, 1280 × 800, **1366 × 768** (portable courant, pour les pop-ups et formulaires), 768 × 1024, **390 × 844** et 375 × 812, puis 2 560 px de large pour les débordements de largeur.

Avec Playwright (fiable, toutes largeurs) : rendre la page, laisser jouer les apparitions, capturer en pleine page, puis **lire l'image** et la découper avec PIL pour juger chaque section.

Avec Chrome sans tête en ligne de commande :
```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
  --hide-scrollbars --force-device-scale-factor=2 --window-size=1440,4200 \
  --virtual-time-budget=7000 --screenshot=<scratchpad>/capture.png "http://127.0.0.1:<port>/<page>/"
```
Captures et rapports vont dans le scratchpad, jamais dans le dépôt.

## 3. Les pièges qui font conclure à tort

| Ce qu'on voit | Ce qui se passe vraiment | Parade |
|---|---|---|
| Tout est vide sous le hero | La capture part avant que le JS ait révélé les sections (blocs à `opacity: 0`) | `--virtual-time-budget=5000` au moins ; vérifier la hauteur réelle du contenu avant de diagnostiquer |
| Le contenu est coupé en « mobile » à 390 px | Chrome sans tête impose une fenêtre d'au moins 500 px : la page se met en page à 500 et la capture coupe | Capturer le mobile à 500 px avec Chrome, ou utiliser Playwright pour 390 ; ne jamais conclure à un débordement sur la seule image |
| Le bas de l'image manque | Chrome sans tête rogne environ 95 px en bas avec `--window-size=L,H` | Rendre à H + 180 px, puis recadrer avec PIL |
| Un état piloté au défilement ne bouge pas | `scroll-behavior: smooth` rend `scrollTo` asynchrone ; `requestAnimationFrame` ne tourne pas en rendu sans tête | Injecter `html{scroll-behavior:auto!important}` et `scrollTo({top, behavior: 'instant'})` ; vérifier le calcul à la main plutôt que le résultat |
| La section basse n'apparaît pas sur la capture | Le défilement programmatique ne se voit pas dans `--screenshot` | Masquer les sections précédentes (`previousElementSibling.style.display = 'none'`) plutôt que défiler |
| Une très haute section reste vide chez le client | `IntersectionObserver` avec un seuil de 0,08 ne se déclenche jamais sur un bloc de 9 000 px ; forcer l'opacité en QA masque le bug | Seuil 0 sur les blocs plus hauts que l'écran, et un filet au défilement qui révèle tout bloc entré dans la fenêtre. Test qui tranche : sections précédentes masquées, fenêtre de 600 px, capture, compter les pixels du contenu |
| Une page vue sur un téléphone est « cassée » alors qu'elle est juste ailleurs | Feuille CSS ou JS périmée dans le cache du visiteur | Reproduire avec le HTML neuf et l'ancienne feuille ; corriger par la version dans le lien (`?v=AAAAMMJJ`) |
| Un sommaire ou un en-tête est invisible | Un `<nav>` ou un `<header>` hérite du style global de la barre du site et part se coller en haut | Voir la skill `page-web`, pièges techniques |
| Un titre « trop long » | Les entités (`&nbsp;`) comptent plusieurs caractères dans le source | Mesurer après résolution des entités |
| Une bande sombre ressemble à une coupure | Ombre portée noire sous un bouton, ou zone morte d'un `align-items: center` | Garder des ombres teintées de la marque ; ancrer le bas du bloc |

**Mesurer un débordement** : comparer `document.documentElement.scrollWidth` et `clientWidth` dans la page (Playwright `evaluate`, ou script injecté qui écrit le verdict dans le `<title>` puis `--dump-dom`).

## 4. Montrer à l'humain

Donner l'URL locale de l'aperçu (ou la commande pour le lancer) et la liste précise des points à regarder : le hero, les jonctions de fonds, les moments animés, le formulaire, le mobile. Les défauts de rendu que les scripts ne voient pas (un en-tête collé, une matière masquée, un épinglage absent, une page qui « fait gabarit ») restent à son œil.

## Format du rapport

```
## QA rendu · <page> · <ce qui a été contrôlé>

Verdict : ✅ propre | 🔴 N défauts (M bloquants)

| # | Où | Taille d'écran | Contrôle | Gravité | Constat | Correction |
|---|---|---|---|---|---|---|

Écartés (faux positifs assumés) : <liste courte, avec la raison>
Captures : <chemins dans le scratchpad>
À regarder à l'œil : <liste>
```

Chaque défaut est actionnable : où, quel sélecteur, valeur constatée, valeur attendue, correction. Zéro défaut se dit simplement, avec ce qui a été contrôlé. À la troisième passe, signaler les défauts qui reviennent : ils trahissent un problème de gabarit, pas de contenu.
