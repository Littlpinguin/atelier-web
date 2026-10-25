# Atelier web

La méthode et les outils que j'utilise avec Claude Code pour créer des pages web belles, cohérentes et qui convertissent, réunis dans un plugin à installer sur n'importe quel projet.

Le plugin ne contient aucune marque : chaque projet pose sa propre doctrine (couleurs, polices, voix, preuves, système de design du site), et toutes les skills la lisent avant de produire. Résultat : des pages qui ressemblent au site qu'elles rejoignent, au pixel près, plutôt qu'à un gabarit généré.

Jessy Martin · [jessem.fr](https://jessem.fr) · dépôt privé, partagé sur invitation.

---

## Ce que contient le dépôt

| Élément | Contenu |
|---|---|
| **Plugin `atelier-web`** | 24 skills, 7 agents, un hook de contrôle de marque, la fabrique de pages et les modèles de doctrine |
| **Fabrique** | 44 sections éprouvées (hero, preuves, programme, offre, FAQ, porte de choix…), 6 modèles de landing, 10 outils interactifs avec capture, et les scripts d'assemblage, de QA mesurée, de génération des jetons et de lint de marque |
| **Outils complémentaires** | Le script qui installe les plugins tiers que j'utilise avec l'atelier, depuis leur source d'origine |
| **Méthode** | [`docs/methode.md`](docs/methode.md) : le niveau attendu et la manière d'y arriver |

## Installer

**Prérequis**
- [Claude Code](https://claude.com/claude-code) (application de bureau, onglet Code, ou terminal).
- Un accès à ce dépôt privé (invitation GitHub), et git authentifié sans invite : `gh auth login` puis `gh auth setup-git`.
- Python 3.11 ou plus récent, et pour la QA du rendu : `pip install playwright pillow pyyaml && playwright install chromium`.

**L'atelier seul**

```bash
claude plugin marketplace add Littlpinguin/atelier-web
```

```bash
claude plugin install atelier-web@atelier-web
```

**L'atelier et les outils complémentaires** (depuis une copie du dépôt)

```bash
./outils-complementaires/installer.sh
```

`--tout` ajoute l'animation avancée et la 3D, le SEO, les marketing skills d'origine et Figma ; `--projet` installe pour le projet courant seulement ; `--essai` affiche les commandes sans rien installer. Détail : [`outils-complementaires/README.md`](outils-complementaires/README.md).

**Pour une équipe sur un même projet** : ajouter le contenu de [`outils-complementaires/settings-projet.json`](outils-complementaires/settings-projet.json) au `.claude/settings.json` du projet et le commiter. Chaque membre accepte la confiance du dossier à l'ouverture ; si `/plugin` signale le plugin comme « activé mais non installé », une seule commande suffit : `claude plugin install atelier-web@atelier-web --scope project`.

Redémarrer Claude Code après l'installation.

## Démarrer dans un projet

Ouvrir la session dans le dossier du projet, puis :

1. **`/atelier-web:demarrer-projet-web`** : lit le site et vos contenus, propose la doctrine de marque (jetons, signatures visuelles, composants, voix, preuves, personas), la fait valider bloc par bloc, l'écrit dans `atelier/marque/` et ajoute un bloc « Atelier web » au `CLAUDE.md` du projet. Une fois par projet.
2. Ensuite, selon le besoin :
   - **`/atelier-web:landing-page`** pour une landing, une page de vente, d'inscription ou de campagne ;
   - **`/atelier-web:page-web`** pour une page ou une section sur un site qui existe ;
   - **`/atelier-web:design-redesign`** pour moderniser un site qui fait daté.

Chaque livrable passe par **`qa-rendu`** (rendu mesuré et capturé) puis **`brand-check`** (validation finale) avant de vous être montré.

## Les skills

| Famille | Skills | À quoi elles servent |
|---|---|---|
| Démarrer | `demarrer-projet-web` | Poser la doctrine du projet, orienter vers la bonne skill |
| Produire une page | `landing-page`, `page-web`, `lead-magnet` | Playbook de landing en huit phases ; page ou section sur un site existant ; outil ou guide contre un email |
| Direction et système | `design-direction`, `design-taste`, `design-system`, `design-redesign` | Direction artistique distinctive, protocole anti-gabarit, jetons et échelles, refonte |
| Mouvement | `motion-defilement`, `animation-gsap`, `animation-scroll-reveal`, `animation-animejs`, `animation-lottie` | Grammaire du mouvement, défilement fluide, épinglages, puis la technique de chaque bibliothèque |
| Conversion | `cro-page`, `cro-form`, `cro-popup`, `cro-pricing` | Proposition de valeur, objections, formulaires, pop-ups, pages tarifs |
| Textes | `copywriting`, `copy-editing`, `humanize-writing` | Rédaction, relecture en passes, chasse aux tournures « générées » |
| Contrôle | `qa-rendu`, `design-review`, `accessibility-web`, `brand-check` | Rendu mesuré, revue d'interface, WCAG 2.2 AA, conformité à la marque |

## Les agents

| Agent | Rôle |
|---|---|
| `landing-researcher` | Benchmark de pages qui convertissent et recherche visuelle regardée en images, en arrière-plan |
| `landing-section-builder` | Construit une section dans les seuls fichiers qu'on lui confie, en parallèle des autres |
| `landing-reviewer-design` | Revue de cohérence webdesign : en-têtes, rythme, matières, typographie, mouvement, responsive |
| `landing-reviewer-brand` | Revue de marque : voix, ton, visuel, preuves, droits |
| `landing-reviewer-cro` | Revue de conversion : récit, objections, CTA, bloc de conversion, mesure |
| `landing-reviewer-a11y` | Revue d'accessibilité statique en 14 points, contrastes calculés |
| `a11y-auditor` | Audit d'accessibilité en rendu réel (axe-core, parcours clavier) |

## La fabrique

Les scripts se lancent depuis la racine du projet ; ils lisent la marque dans `atelier/marque/` (ou le dossier de `ATELIER_MARQUE`).

| Script | Rôle |
|---|---|
| `assemble-landing.py` | Spec (sections et textes) → page HTML autonome, aux couleurs du projet |
| `qa-landing.py` | QA mesurée à trois tailles d'écran et en mouvement réduit : débordements, contrastes, planchers typographiques, CTA sous le pli, suivi |
| `controle-fonds.py` | Continuité des fonds entre sections, mesurée dans les marges |
| `build-tokens.py` | `tokens.json` → variables CSS du projet, contrastes WCAG garantis sur les dérivées |
| `lint-brand.py` | Linter de marque déterministe : vocabulaire banni, tirets, ponctuation des titres, couleurs et polices hors marque |
| `lint-placeholders.py` | Vérifie qu'aucun `{{…}}` ne reste dans la doctrine |

Le catalogue des sections s'ouvre dans un navigateur : `plugins/atelier-web/fabrique/templates/sections/catalogue.html`.

## Mettre à jour

```bash
claude plugin marketplace update atelier-web
```

```bash
claude plugin update atelier-web@atelier-web
```

La doctrine de chaque projet n'est jamais touchée par une mise à jour : elle vit dans le projet.

## Règles de ce dépôt

- **Aucune donnée de marque ni de client ici.** Les valeurs, textes et assets d'une marque vivent dans son projet (`atelier/marque/`). Les exemples de la fabrique utilisent des marques fictives.
- **Aucun secret.** Clés et identifiants restent dans le `.env` local de chaque projet.
- Les contenus repris de projets tiers gardent leur licence et leur attribution : voir [`CREDITS.md`](CREDITS.md).
