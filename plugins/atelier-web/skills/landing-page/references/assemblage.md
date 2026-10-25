# Où vit quoi, socle et assemblage

Détail des phases 4 et 5 du playbook : l'arborescence d'une landing, ce que pose l'assembleur, l'insertion des fragments.

## Arborescence

```
<projet>/atelier/
├── marque/                               ← doctrine (skill demarrer-projet-web) : tokens.json, tokens.css, voice.md…
├── briefs/<slug>.md                      ← brief validé (phase 1)
├── landings/<slug>/
│   ├── index.html                        ← la page : HTML + CSS + JS inline, livrable unique
│   ├── assets/                           ← images, polices locales, données
│   └── pilotage/                         ← la fabrication, versionnée, jamais déployée
│       ├── spec.md                       ← spec validée (phase 3)
│       ├── page.json                     ← spec d'assemblage (sections et slots)
│       ├── page-charter.md               ← charte de la page (copie de references/charte.md)
│       ├── research-notes.md             ← recherche consolidée (landing-researcher)
│       ├── sections/<nn>-<id>.html       ← un fragment par section, propriété d'un seul agent
│       ├── reports/<nn>-<id>.md          ← rapports des builders
│       ├── qa.json                       ← sortie de qa-landing.py (phase 7)
│       ├── review-<grille>.md            ← rapports des revues
│       └── fix-wave-brief.md             ← arbitrage de la vague de corrections
└── publie.md                             ← registre des pages publiées

${CLAUDE_PLUGIN_ROOT}/fabrique/           ← dans le plugin, en lecture seule
├── templates/sections/<mécanique>.html   ← bibliothèque de sections (fragments à slots) + catalogue.json
├── templates/assets/                     ← tokens.css neutre, base.css, moteurs reveal / scroll / offer / forms / tracking
├── templates/landing-pages/              ← 6 modèles de landing (specs YAML + pages assemblées)
├── templates/lead-magnets/               ← 10 outils interactifs avec capture
└── scripts/
    ├── assemble-landing.py               ← spec (pilotage/page.json) → index.html autonome
    ├── qa-landing.py                     ← QA mesurable (phases 5 à 8)
    ├── controle-fonds.py                 ← continuité des fonds entre sections
    └── lint-brand.py                     ← linter de marque déterministe
```

Les scripts se lancent **depuis la racine du projet** : ils y lisent la marque (`atelier/marque/`, ou `ATELIER_MARQUE`) et y écrivent la page. Dans un projet sous framework (Next.js, Astro…), la page assemblée sert de maquette fidèle, puis se porte en composants avec les mêmes jetons.

## Catalogue des sections

Le rendu de chaque section de la bibliothèque, avec sa fiche (objection, quand l'utiliser, quand l'éviter, slots), se génère dans le projet :

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/assemble-landing.py ${CLAUDE_PLUGIN_ROOT}/fabrique/templates/sections/catalogue.json
```

La page sort dans `atelier/catalogue-sections.html`, aux couleurs de la marque du projet.

## Ce que pose l'assembleur (phase 4)

`python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/assemble-landing.py pilotage/page.json` (format, slots et garde-fous : `${CLAUDE_PLUGIN_ROOT}/fabrique/templates/sections/README.md`) écrit un `index.html` qui contient :

- le `<head>` complet : titre, description, `robots`, Open Graph, favicon, `<meta name="viewport">` ;
- les jetons (`templates/assets/tokens.css`, généré depuis `atelier/marque/tokens.json`) ;
- le CSS commun de la charte (`templates/assets/base.css` : base, en-tête de section, famille de cartes, boutons, focus, bandes sombres) ;
- **un seul moteur d'apparition** (`reveal.js` : attributs `data-reveal`, opacité et position, coupé par `prefers-reduced-motion`) ;
- le relais de mesure (`tracking.js` : `data-track` vers `dataLayer` / `gtag`, UTM) ;
- la configuration de l'offre (`offer` de la spec, lue par `offer.js`) ;
- les sections courantes, déjà remplies depuis la bibliothèque, et une paire de marqueurs par section à sa place définitive. Une section sur mesure prend d'abord le fragment `_placeholder` (id, `aria-labelledby`, titre), pour que la page s'affiche à chaque étape :

```html
<!-- section:hero -->
<section id="hero" aria-labelledby="hero-titre">…</section>
<!-- /section:hero -->
```

## Insérer un fragment (phase 5)

À réception du rapport d'un builder, le contrôleur remplace dans la spec l'entrée `_placeholder` de la section par `{"file": "sections/<nn>-<id>.html", "id": "<id>"}` et réassemble : l'assembleur insère le fragment tel quel entre ses marqueurs.

Si la page a été retouchée à la main depuis le dernier assemblage, l'assembleur refuse de l'écraser (empreinte dans `<meta name="generator">`). Le contrôleur insère alors les fragments avec un script qui vérifie que chaque marqueur existe une seule fois :

```python
import re, pathlib
page = pathlib.Path("atelier/landings/<slug>/index.html")
html = page.read_text(encoding="utf-8")
for frag in sorted(page.parent.glob("pilotage/sections/*.html")):
    sid = frag.stem.split("-", 1)[1]
    debut, fin = f"<!-- section:{sid} -->", f"<!-- /section:{sid} -->"
    assert html.count(debut) == 1 and html.count(fin) == 1, sid
    motif = re.compile(re.escape(debut) + r".*?" + re.escape(fin), re.S)
    html = motif.sub(lambda _: f"{debut}\n{frag.read_text(encoding='utf-8').strip()}\n{fin}", html)
page.write_text(html, encoding="utf-8")
```

Puis `python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/qa-landing.py <index.html>` et un commit, sur go de l'humain si la session l'exige. Le hook de l'atelier lint la page ainsi écrite : lire son constat avant la suite.

## Micro-retouches (phase 6)

Le contrôleur les fait lui-même, par un remplacement scripté qui vérifie la chaîne d'origine (`assert texte in html`), puis QA et commit.
