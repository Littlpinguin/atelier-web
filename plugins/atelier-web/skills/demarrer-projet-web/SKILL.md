---
name: demarrer-projet-web
description: Point d'entrée de l'atelier web dans un nouveau projet. Pose la doctrine de marque du projet dans atelier/marque/ (jetons, charte visuelle, voix, anti-style-IA, preuves, personas, système de design du site existant) à partir du site et des contenus réels, la fait valider section par section, ajoute le bloc « Atelier web » au CLAUDE.md du projet, puis oriente vers la bonne skill. À utiliser dès qu'on ouvre l'atelier sur un projet, quand une skill de l'atelier s'arrête faute de doctrine, ou quand l'utilisateur dit « initialise l'atelier », « pose la charte », « on démarre le site ».
---

# demarrer-projet-web : poser la doctrine avant la première page

Une page belle et juste se construit sur une doctrine écrite : les valeurs exactes de la marque, sa voix, ses preuves, ce qu'elle a déjà refusé. Sans elle, chaque page se fait de mémoire et la marque se dilue. Cette skill pose cette doctrine une fois, dans le projet, puis toutes les skills de l'atelier la lisent.

## Où vit quoi

```
<projet>/
├── CLAUDE.md                    ← bloc « Atelier web » (modèle : ${CLAUDE_PLUGIN_ROOT}/modeles/CLAUDE-atelier.md)
└── atelier/
    ├── marque/                  ← doctrine, source de vérité de toutes les skills
    │   ├── CLAUDE.md            ← routeur : quoi lire pour quel livrable
    │   ├── tokens.json          ← couleurs, dégradé, polices, rayons (format DTCG)
    │   ├── tokens.css           ← généré depuis tokens.json (build-tokens.py)
    │   ├── style-guide.md       ← intention visuelle, illustration, interdits visuels
    │   ├── design.md            ← système du site existant : composants, signatures, mouvement, checklist
    │   ├── voice.md             ← position de voix, vocabulaire préféré et banni, typographie
    │   ├── anti-ai-writing-style.md, checklist-pre-composition.md, design-anti-generique.md
    │   ├── messaging-framework.md  ← chiffres et preuves réels, messages par audience
    │   ├── personas.md, exemples-rejetes.md, divulgation-ia.md, droits.md
    │   ├── lint-brand.toml, build-tokens.toml   ← réglages des scripts pour ce projet
    │   └── assets/              ← logos, polices, illustrations validés (+ index.md)
    ├── briefs/  landings/  pages/  lead-magnets/
    └── publie.md                ← registre des pages publiées
```

Le dossier se déplace si le projet l'exige : déclarer alors le chemin dans le bloc du `CLAUDE.md` et exporter `ATELIER_MARQUE` pour les scripts. Les skills lisent toujours les chemins déclarés dans ce bloc.

## Étape 0 : état des lieux

1. `atelier/marque/` existe déjà et ne contient plus de `{{…}}` (`python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/lint-placeholders.py`) : la doctrine est posée. Passer directement à l'étape 6.
2. Repérer ce que le projet possède déjà : document de design (`docs/design.md`, `DESIGN.md`, Storybook, `tokens.css`, configuration Tailwind, variables CSS de `:root`), charte PDF, guide de voix, pages de référence. **Réutiliser avant de créer** : un document de design existant reste la source ; le bloc du `CLAUDE.md` y renvoie, on ne le recopie pas.
3. Identifier la pile : HTML statique, générateur (Astro, Eleventy, Hugo), framework (Next.js, Nuxt, SvelteKit), CMS (WordPress, Webflow). La fabrique de landings produit du HTML autonome ; dans un framework, la page se porte ensuite en composants en gardant les mêmes jetons.

## Étape 1 : réunir la matière, en une salve

Demander en une fois :
- l'URL du site et deux ou trois pages soignées qui font référence ;
- au moins trois contenus récents écrits par la marque (articles, posts, newsletters) : sans eux, la voix restera générique, et il faut le dire ;
- les documents de marque disponibles (charte, plateforme, présentation commerciale) ;
- le logo en SVG, les fichiers de police et leur licence ;
- les chiffres et témoignages réels qu'on a le droit d'afficher, avec leur source.

Lire les pages publiques avec WebFetch ou le navigateur intégré, jamais une page derrière une connexion. Rien ne s'écrit sur le disque avant validation.

## Étape 2 : proposer un brouillon de doctrine

Construire en mémoire, avec la source de chaque valeur :

- **Jetons** : couleur d'action (boutons, liens), accent, sombre, clair, blanc ; dégradé signature s'il existe ; polices (titre, texte, éventuelle police d'accent) ; rayons (cartes, boutons, badges, champs). Lire les valeurs dans le CSS calculé, pas à l'œil.
- **Signatures visuelles** : ce qui rend le site reconnaissable (une ornementation, un motif de fond, un traitement des titres, une illustration, un personnage). Elles vont dans `design.md` et ne se perdent jamais d'une page à l'autre.
- **Composants** : les sections et blocs qui existent déjà (hero, preuves, FAQ, appel final, boutons, cartes), avec le fichier qui les porte. Modèle : `${CLAUDE_PLUGIN_ROOT}/modeles/design.md`.
- **Voix** : position, tutoiement ou vouvoiement, vocabulaire préféré, termes bannis, règles typographiques (tirets, emoji, espaces insécables).
- **Preuves** : les seuls chiffres, clients et témoignages qu'on peut afficher, avec leur source. Rien d'inventé : un trou reste un trou, signalé.
- **Personas** : deux à quatre, avec leurs objections réelles.
- **Interdits** : visuels (photos de banque d'images, styles écartés) et éditoriaux.

## Étape 3 : valider section par section

Présenter le brouillon par blocs (jetons, signatures et composants, voix, preuves, personas, interdits), avec une recommandation pour chaque choix ouvert. L'humain valide, corrige ou complète chaque bloc. Une valeur non validée ne s'écrit pas.

## Étape 4 : écrire la doctrine

1. Copier les modèles : `${CLAUDE_PLUGIN_ROOT}/modeles/marque/` vers `atelier/marque/`, `${CLAUDE_PLUGIN_ROOT}/modeles/design.md` vers `atelier/marque/design.md` (sauf si le projet a déjà son document de design).
2. Remplir chaque `{{…}}` avec les valeurs validées. Un champ sans valeur se supprime ou reçoit `[À FOURNIR : …]`, jamais une valeur plausible.
3. Copier `${CLAUDE_PLUGIN_ROOT}/fabrique/templates/assets/tokens.css` vers `atelier/marque/tokens.css`, `${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/lint-brand.toml` et `build-tokens.toml` vers `atelier/marque/`. Reporter les termes bannis de `voice.md` dans `[forbidden-words.charter]` de `lint-brand.toml`.
4. Générer les jetons CSS, depuis la racine du projet :
   ```bash
   python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/build-tokens.py
   python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/build-tokens.py --check
   ```
5. Contrôler : `python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/lint-placeholders.py` (zéro placeholder) puis `python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/lint-brand.py atelier/marque` (lire les avertissements).
6. Poser les assets validés dans `atelier/marque/assets/` avec leur fiche dans `index.md` (source, droits, auteur). Les fichiers lourds restent hors du dépôt si le projet a cette règle.

## Étape 5 : le bloc du CLAUDE.md

Ajouter au `CLAUDE.md` du projet le bloc de `${CLAUDE_PLUGIN_ROOT}/modeles/CLAUDE-atelier.md`, rempli : chemins de la doctrine et des livrables, document de design de référence, pages modèles du site, commande d'aperçu local, outils autorisés pour voir un rendu (navigateur intégré, Chrome sans tête), mesure d'audience, règles de publication. Lire le `CLAUDE.md` avant de l'éditer, et ne rien y retirer.

## Étape 6 : orienter

| Demande | Skill ou agent |
|---|---|
| Landing, page de vente, page d'inscription, page de campagne | `landing-page` |
| Page ou section sur un site qui existe déjà | `page-web` |
| Direction artistique d'une page nouvelle | `design-direction`, puis `design-taste` |
| Jetons, palette sémantique, échelle typographique | `design-system` |
| Refonte d'un site qui fait daté ou « fait IA » | `design-redesign` |
| Mouvement, défilement, apparitions, épinglages | `motion-defilement` d'abord (pile et grammaire), puis `animation-scroll-reveal` (apparitions en CSS natif), `animation-gsap` (épinglage, scrub), `animation-animejs`, `animation-lottie` (illustrations en dotLottie) |
| Revue de l'interface avant livraison | `design-review`, `qa-rendu` |
| Accessibilité | `accessibility-web`, agent `a11y-auditor` |
| Conversion d'une page, d'un formulaire, d'une pop-up, d'une page tarifs | `cro-page`, `cro-form`, `cro-popup`, `cro-pricing` |
| Outil interactif ou guide contre un email | `lead-magnet` |
| Textes | `copywriting`, `copy-editing`, `humanize-writing` |
| Validation finale de tout livrable | `brand-check` |

## Règles

- **Doctrine d'abord** : aucune skill de l'atelier ne produit sans `atelier/marque/` rempli. Elle s'arrête et renvoie ici.
- **Rien d'inventé** : chiffres, clients, logos, témoignages, faits sur une personne viennent d'une source validée.
- **Secrets** : aucune clé ni mot de passe dans la doctrine ni dans le `CLAUDE.md` ; `.env` local, jamais commité.
- **Droits** : une police, une photo de personne ou un logo tiers n'entre dans `assets/` qu'avec sa licence ou son accord noté dans `droits.md`.
