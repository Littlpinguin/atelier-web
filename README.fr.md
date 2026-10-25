# Atelier web pour Claude Code

[English](README.md) · **Français**

[![Licence MIT](https://img.shields.io/badge/licence-MIT-0D1B2A.svg)](LICENSE) ![Version 1.3.0](https://img.shields.io/badge/version-1.3.0-0D1B2A.svg) ![Plugin Claude Code](https://img.shields.io/badge/Claude%20Code-plugin-F9DC5C.svg) ![10 skills](https://img.shields.io/badge/skills-10-1B4965.svg) ![6 agents](https://img.shields.io/badge/agents-6-1B4965.svg)

![Atelier web : trois landings de trois marques fictives, produites par la même fabrique](docs/assets/apercu-fr.webp)

**Atelier web est un plugin Claude Code pour concevoir et construire des landing pages et des pages web belles, qui convertissent et qui ressemblent exactement à la marque qu'elles servent.** Il réunit 10 skills, 6 agents (recherche d'inspiration, construction en parallèle, revues design, marque, conversion et accessibilité), une bibliothèque de 44 sections de landing éprouvées et une QA qui mesure le rendu réel avant de vous montrer quoi que ce soit.

Il reprend la méthode avec laquelle je construis les sites et les landings de mes clients. Je suis [Jessy Martin](https://jessem.fr), consultant et formateur sur Claude Code et les agents IA pour les équipes marketing.

## Le problème qu'il règle

Claude Code construit une page en quelques minutes. Laissé seul, il produit souvent la même page : un dégradé violet, des cartes blanches empilées, une police générique, des chiffres inventés, et un rendu jamais vérifié sur un téléphone avant la mise en ligne.

L'atelier change trois choses :

1. **La marque d'abord.** Chaque projet écrit sa doctrine une fois (couleurs, polices, voix, preuves autorisées, composants du site), et toutes les skills la lisent avant de produire. Les pages ressemblent au site qu'elles rejoignent.
2. **Une méthode éprouvée sur de vraies pages.** Cadrage en une salve, directions nommées par leur objet signature, hero validé d'abord, sections construites en parallèle, quatre revues spécialisées, puis une vague de corrections arbitrée.
3. **Un contrôle mesuré.** Débordements, contrastes, tailles de texte, bouton visible sans défiler sur mobile, continuité des fonds entre sections, mouvement réduit : tout se mesure à trois tailles d'écran avant que la page vous soit montrée.

## Une fabrique pour toutes les marques

Les trois pages ci-dessous sortent des mêmes commandes, avec trois doctrines différentes. Les marques sont fictives ; des photos Pexels tiennent la place de celles qu'une vraie marque fournirait ([crédits](https://littlpinguin.github.io/atelier-web/credits-photos/)).

| Formation | Événement | Prestation |
|---|---|---|
| ![Landing de formation, marque fictive Ferlane](docs/assets/landing-ferlane.webp) | ![Landing d'événement, marque fictive Brivalle](docs/assets/landing-brivalle.webp) | ![Landing de prestation, marque fictive Ouvrance](docs/assets/landing-ouvrance.webp) |
| [Démo en ligne](https://littlpinguin.github.io/atelier-web/demo/ferlane/) | [Démo en ligne](https://littlpinguin.github.io/atelier-web/demo/brivalle/) | [Démo en ligne](https://littlpinguin.github.io/atelier-web/demo/ouvrance/) |

Les 44 sections se parcourent dans le [catalogue en ligne](https://littlpinguin.github.io/atelier-web/catalogue/).

## Installer

Prérequis : [Claude Code](https://claude.com/claude-code) (application de bureau ou terminal), Python 3.11 ou plus récent, et pour la QA du rendu `pip install playwright pillow pyyaml && playwright install chromium`.

```bash
claude plugin marketplace add Littlpinguin/atelier-web
```

```bash
claude plugin install atelier-web@atelier-web
```

Redémarrez Claude Code. Pour ajouter les plugins que j'utilise avec l'atelier (UI/UX Pro Max, frontend-design, superpowers, et en option GSAP, Three.js, SEO, Figma), lancez depuis une copie du dépôt `./outils-complementaires/installer.sh` (détail dans [`outils-complementaires/README.md`](outils-complementaires/README.md)).

**Pour une équipe** : ajoutez [`outils-complementaires/settings-projet.json`](outils-complementaires/settings-projet.json) au `.claude/settings.json` du projet et commitez-le. Chaque membre retrouve l'atelier en ouvrant le dossier.

## Démarrer en trois étapes

1. Ouvrez Claude Code dans le dossier de votre site.
2. Lancez `/atelier-web:demarrer-projet-web` : Claude lit votre site et vos contenus, propose la doctrine de marque, la fait valider bloc par bloc et l'écrit dans `atelier/marque/`.
3. Lancez `/atelier-web:landing-page` pour une landing, `/atelier-web:page-web` pour une page ou une section sur un site existant, `/atelier-web:design` pour moderniser un site qui fait daté.

Chaque livrable passe par `revue` puis `brand-check` avant de vous être montré.

## Ce que contient le plugin

| Famille | Skills |
|---|---|
| Démarrer | `demarrer-projet-web` : doctrine du projet et orientation |
| Produire une page | `landing-page` (playbook en huit phases), `page-web` (site existant), `lead-magnet` (outil ou guide contre un email) |
| Design | `design` : recherche visuelle avant de dessiner, directions nommées par leur objet signature, protocole contre le « design IA », refonte d'un existant, jetons |
| Mouvement | `motion` : CSS natif piloté par le défilement d'abord, GSAP pour l'épinglage, anime.js, dotLottie pour les médias animés |
| Conversion | `cro` : page, formulaire, pop-up, tarifs |
| Textes | `ecriture` : rédiger, relire en sept passes, humaniser un texte qui sonne généré |
| Contrôle | `revue` (rendu mesuré, interface, accessibilité WCAG 2.2 AA), `brand-check` |

Chaque skill garde son détail dans des fichiers de référence, à un niveau sous son `SKILL.md`, lus seulement quand la tâche en a besoin.

**Agents** : `inspiration-researcher` (benchmark et recherche visuelle en arrière-plan, avant une landing, une page d'un site existant, des directions ou une refonte), `landing-section-builder` (une section par agent, en parallèle), `landing-reviewer-design`, `landing-reviewer-brand`, `landing-reviewer-cro`, et `a11y-auditor` (accessibilité : mesures, code et rendu réel).

**Fabrique** : 44 sections (hero, preuves, programme, offre, FAQ, porte de choix, comparateur…), 6 modèles de landing (formation, événement, prestation, démo B2B, vente longue, capture), 10 outils interactifs avec capture (calculateur de ROI, diagnostic, quiz…), et les scripts `assemble-landing.py`, `qa-landing.py`, `controle-fonds.py`, `build-tokens.py`, `lint-brand.py`. Un hook lance le contrôle de marque après chaque page écrite, y compris celles qu'assemble un script.

**Évals** : `plugins/atelier-web/evals/` contient une suite `claude plugin eval` (orientation, déclenchement des skills, demandes qui ne doivent pas les déclencher, une landing de bout en bout), jouée sur la doctrine d'une marque fictive fournie en fixture.

La méthode complète est dans [`docs/methode.md`](docs/methode.md).

## Questions fréquentes

**Faut-il savoir coder ?**
Pour l'usage courant, vous pouvez vous en passer : vous décrivez la page, validez la direction et relisez le rendu. Savoir lire du HTML aide à aller plus loin.

**Ça marche avec Next.js, Astro ou WordPress ?**
La fabrique produit des pages HTML autonomes, prêtes pour un site statique. Dans un framework, la page assemblée sert de maquette fidèle, puis se porte en composants avec les mêmes jetons. Les skills de design, de conversion et de revue s'appliquent à toutes les piles.

**Les pages sont-elles en français ?**
Les skills sont écrites en français. Claude produit les pages dans la langue que vous voulez.

**Quelle différence avec frontend-design ou UI/UX Pro Max ?**
Ce sont d'excellentes sources, et l'atelier en intègre des parties adaptées (voir [`CREDITS.md`](CREDITS.md)). frontend-design donne une direction esthétique, UI/UX Pro Max une base de styles, de palettes et de règles. L'atelier ajoute la doctrine de marque par projet, une méthode de bout en bout avec des agents spécialisés, une bibliothèque de sections et une QA mesurée. Les trois se complètent : le script d'installation les pose ensemble.

**Est-ce gratuit ?**
Oui, sous licence MIT. Si vous voulez que votre équipe sache s'en servir, je donne une [formation sur la création de pages web avec Claude](https://jessem.fr/formations/creer-pages-web-claude/).

**Mes données partent-elles quelque part ?**
Le plugin ne contient aucun service distant : les scripts tournent sur votre machine. La doctrine de votre marque reste dans votre projet.

## À propos

Je m'appelle Jessy Martin. J'accompagne les équipes marketing sur Claude Code et les agents IA, en conseil et en formation, et j'enseigne à la Clermont School of Business. L'atelier vient des pages que je construis pour mes clients et de mon propre site, [jessem.fr](https://jessem.fr).

- Formation : [créer des pages web avec Claude, du brief à la publication](https://jessem.fr/formations/creer-pages-web-claude/)
- Méthode détaillée : [créer un site web avec Claude Code](https://jessem.fr/blog/creer-site-web-claude-code)
- Autres projets ouverts : [marketing-cockpit-template](https://github.com/Littlpinguin/marketing-cockpit-template) (le département marketing dans Claude Code, dont l'atelier est extrait), [claude-site-starter](https://github.com/Littlpinguin/claude-site-starter) (le socle d'un site statique)
- [LinkedIn](https://www.linkedin.com/in/jessy-martin/)

## Mettre à jour

```bash
claude plugin marketplace update atelier-web
```

```bash
claude plugin update atelier-web@atelier-web
```

Une mise à jour ne touche jamais la doctrine de vos projets.

## Licence

MIT. Les contenus repris de projets tiers gardent leur licence et leur attribution : voir [`CREDITS.md`](CREDITS.md).
