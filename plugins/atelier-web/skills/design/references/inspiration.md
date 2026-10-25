# Recherche d’inspiration

Avant de dessiner, regarder ce que font les meilleures pages du même genre. La recherche part en arrière-plan (agent `inspiration-researcher`) dès que le sujet est clair, et le travail continue sans l’attendre jusqu’au moment où les références servent : directions, hero, section nouvelle. Une référence se regarde en images : elle ne se juge jamais sur son titre ni sur sa description.

## Sommaire

1. Qui cherche quoi, selon la skill
2. Benchmark
3. Inspiration visuelle
4. Filtre de marque
5. Consolidation
6. Motifs et licences (recherche du 5 octobre 2026)

## 1. Qui cherche quoi, selon la skill

| Skill et moment | Volets | Ce que les références peuvent changer | Notes |
|---|---|---|---|
| `landing-page`, phase 0 | Benchmark (§ 2) et visuel par besoin de section (§ 3) | Composition, objet signature, mouvement, sous les jetons de la marque | `atelier/landings/<slug>/pilotage/research-notes.md` |
| `page-web`, étape 0 | Visuel seulement : les sections que le site n’a pas encore, et le moment qui marque | La composition et le comportement d’une section nouvelle ; jamais une carte, une marge ni un style que le site a déjà | `atelier/pages/<slug>/research-notes.md` |
| `design`, route créer | Visuel par direction pressentie : objets signatures, compositions de hero, traitements typographiques | La direction entière, sauf les dimensions verrouillées par la marque | celles de la page ou de la landing visée |
| `design`, route refondre, mode refondre seulement, après le diagnostic | Benchmark de 4 à 6 sites du même secteur refaits récemment, puis visuel sur les sections que le diagnostic désigne | Ces sections seulement ; jamais l’ordre des correctifs ni ce qui ne change jamais en silence | `atelier/pages/<slug>/research-notes.md` |

- **Notes déjà là** (landing en cours, refonte commencée) : les lire avant toute recherche, et ne relancer que pour un besoin qu’elles ne couvrent pas.
- **Sans agent** (outil indisponible, sous-agents refusés) : la skill fait elle-même une recherche courte, 4 à 6 références, si elle a la recherche web ; sinon elle le dit en une ligne et poursuit sur la doctrine et le site. La recherche nourrit le dessin, elle ne le bloque jamais.
- **Déclinaison stricte** (`page-web` : une page existante recopiée, seuls les textes et les visuels changent) : pas de recherche.

## 2. Benchmark

- **Sources** : recherche web et lecture de pages publiques.
- **Volume** : 8 à 12 pages du même type d’offre pour une landing (formation, atelier, logiciel en essai, prestation, événement, liste d’attente…), 4 à 6 sites du même secteur pour une refonte ; de préférence chez des acteurs reconnus et chez des concurrents directs (`02-strategy/veille/` s’il existe).
- **Pour chaque page** : ordre des sections, nature de la preuve, rendu du programme ou de l’offre, rareté, choix de formule, CTA (libellé, nombre, destination), traitement mobile.
- **Synthèse** : 10 motifs récurrents, 5 idées distinctives, erreurs à éviter, bonnes pratiques UX. Sources citées, aucun chiffre fabriqué, 1 200 mots au plus.

## 3. Inspiration visuelle

### Galeries publiques

| Source | Ce qu’on y cherche |
|---|---|
| Dribbble | Compositions de section, objets signatures, traitements de cartes et de billets |
| Awwwards, Godly, One Page Love, Siteinspire | Pages complètes de haut niveau : rythme, mise en scène au défilement, typographie |
| Land-book, Lapa Ninja, Landingfolio, SaaS Landing Page | Landings et pages de site par type : ordre des sections, blocs de prix, pages « à propos », études de cas, formulaires |
| Codrops | Techniques d’animation et de défilement expliquées pas à pas |
| 21st.dev, Aceternity UI, Magic UI, Animata, React Bits, Free Frontend | Composants : défilement collant, révélation, billet, arborescence, frise, FAQ (licences très différentes : § 6) |
| Vitrine GSAP et démos CodePen de l’éditeur | Épinglage, scrub, tracés SVG, textes découpés |

**Méthode qui marche** :

1. Certaines galeries répondent vide ou refusent un accès automatisé (réponse 202 sans contenu, ou 403). Utiliser alors le navigateur intégré, **uniquement sur des sites tiers publics**, jamais sur un environnement local, de préproduction ou un compte connecté.
2. Sur une galerie à recherche (Dribbble, par exemple) : ouvrir la page de recherche, relever les vignettes (lien, titre, image), composer une planche-contact en grille et la capturer, puis ouvrir en grand les maquettes retenues.
3. Si une navigation est refusée, ne pas la contourner : le dire et passer à la source suivante.
4. Aucune donnée personnelle collectée.

**Requêtes qui donnent de bons résultats** :
- landings : `course landing page`, `workshop landing page`, `bootcamp landing page`, `saas pricing section`, `pain points section`, `choose your path`, `learning path`, `course curriculum`, `ticket design`, `boarding pass`, `testimonial wall`, `two column faq` ;
- pages d’un site : `about page`, `team page`, `case study page`, `services page`, `pricing page`, `contact page`, `blog article layout`, `portfolio grid` ;
- directions et refontes : `hero section`, `editorial website`, `brand redesign`, `website redesign before after`, `kinetic typography`, `line art landing page`, `scrollytelling`, `sticky scroll`.

### Points de départ par besoin

Des composants publics qui ont déjà servi de base. Une nouvelle page cherche les siens.

| Besoin | Points de départ |
|---|---|
| Parcours en défilement collant | Aceternity UI « Sticky Scroll Reveal » (à regarder seulement, § 6) |
| Billet ou carte d’offre | 21st.dev (composants « ticket »), Free Frontend « CSS Tickets » |
| Révélation au défilement | Codrops, articles sur les effets de révélation |
| Choix entre deux formules | Animata « Tilted Card » |
| Carte ou schéma tracé au défilement | Codrops, animations de cartes SVG pilotées par le défilement ; Aceternity UI « World Map » (à regarder seulement, § 6) |
| Arborescence de fichiers | 21st.dev et Magic UI, composants « File Tree » |
| FAQ avec carte collante | 21st.dev, FAQ en deux colonnes |
| Scènes épinglées | Démos GSAP de panneaux épinglés ; reproduction en `position: sticky` plutôt qu’en épinglage par script |

Pour chaque besoin retenu : 2 ou 3 références vérifiées, la technique CSS et JS pour la reproduire dans un HTML statique (vanilla sur les moteurs de la bibliothèque ou du site ; GSAP seulement sur une section sur mesure qui le justifie, § 6), et le comportement en mouvement réduit.

## 4. Filtre de marque, à mettre dans chaque prompt de recherche

- **À garder** : ce que dit `atelier/marque/style-guide.md` (palette de `atelier/marque/tokens.json`, polices de la marque, rayons, style d’illustration).
- **À écarter, en disant pourquoi** : les tropes bannis de `atelier/marque/style-guide.md`, les marqueurs du look IA de `atelier/marque/design-anti-generique.md` § 1 (dégradé violet par défaut, emojis en icônes, héros centré par réflexe, excès d’animation, cartes de faible densité, les trois clusters récents), les ressorts et rebonds, la photo de banque d’images générique, et toute signature déjà portée par une autre page de la marque.
- **Sur un site existant** : `atelier/marque/design.md` prime sur toute référence. Une référence apporte la composition ou le comportement d’une section que le site n’a pas ; ses cartes, ses marges et ses effets restent ceux du site.

## 5. Consolidation

Tout atterrit au chemin des notes (§ 1) :
- la synthèse du benchmark, s’il y en a un ;
- les références retenues, rangées par besoin (section, direction, moment qui marque) ;
- pour chacune, ce qu’on en prend ;
- une liste « Écartés », motivée.

Ce qui en sort cite ses références : le rapport d’un agent de section, les 3 qui lui ont le plus servi ; une direction montrée à l’humain, les 2 ou 3 qui l’ont nourrie, avec le lien et ce qu’on en prend.

## 6. Motifs et licences (recherche du 5 octobre 2026)

L’atelier est sous licence MIT : ce qu’une recherche verse dans la bibliothèque doit pouvoir y être redistribué. Une référence vue dans une galerie donne une idée ; son code n’entre que si sa licence le permet.

**Adaptables, avec mention de l’auteur** (licence MIT, vérifiée le 5 octobre 2026) : Magic UI, Motion Primitives, Animata, Rough Notation, Tufte CSS, Scrollama. Ce sont surtout des composants React et Tailwind : on en reprend le principe et on le réécrit en vanilla sur les moteurs de la bibliothèque, avec une ligne « principe : <projet> (<auteur>), MIT » en tête du code, comme `annotate.js` pour Rough Notation ou les notes en marge de `base.css` pour Tufte CSS.

**Idée seulement, aucun code porté** :

- **React Bits** : licence MIT assortie de la Commons Clause, qui interdit de redistribuer les composants, y compris dans une version portée.
- **Aceternity UI** : licence propriétaire, la source ne se redistribue pas. 21st.dev en recopie beaucoup de composants : idée seulement, sauf licence MIT explicite sur le composant.
- **Codrops** : à vérifier dépôt par dépôt. Les dépôts récents sont en majorité sous MIT, les plus anciens portent une licence maison qui interdit de republier la ressource telle quelle. Par défaut, réimplémenter.

**Poids.** GSAP avec ScrollTrigger pèse environ 116 Ko minifiés, plus de la moitié du budget d’une page livrée en un seul fichier, sous une licence gratuite qui n’est pas une licence open source. La bibliothèque garde ses moteurs maison (`reveal.js` et `scroll.js` font ensemble 13 Ko, non minifiés) : chaque motif retenu tient en CSS natif et quelques lignes branchées sur eux.

**Clichés refusés**, à écarter de toute planche d’inspiration en disant pourquoi :

| Motif | Pourquoi on l’écarte | À la place |
|---|---|---|
| Bandeau défilant infini (logos, avis) | Boucle sans pause, illisible | Mur d’avis (`wall`) |
| Grille bento | Cartes de faible densité, signature du look IA | Index de `work-wall`, `evidence-chart` |
| Bordures lumineuses, faisceaux, boutons brillants | Un seul accent fort par page : le bouton de conversion | Rien |
| Projecteur qui suit le curseur | Aucun équivalent au clavier ni au doigt | Rien |
| Texte brouillé, machine à écrire, mots qui basculent | Retarde la lecture et pollue les annonces des lecteurs d’écran | Titre fixe |
| Cartes qui s’empilent au défilement | Interdit par la charte | Fondu inversé de `scroll.js` |
| Défilement lissé qui remplace le natif | Casse les sauts d’ancre et la recherche dans la page | Défilement natif, `position: sticky` |
| Écran de préchargement | Retarde le contenu et le LCP | Rien |
