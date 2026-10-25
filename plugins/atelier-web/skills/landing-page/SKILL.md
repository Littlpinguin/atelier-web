---
name: landing-page
description: "Playbook de production d'une landing page de conversion pour la marque du projet, du cadrage à la livraison d'un HTML statique dans atelier/landings/. Méthode en huit phases (doctrine et matière réelle, cadrage en une salve, directions, spec, charte commune posée avant le travail parallèle, construction en parallèle par fichiers disjoints, montrer et appliquer les retours, quatre revues parallèles puis une vague de corrections arbitrée, livraison), six agents dédiés (landing-researcher, landing-section-builder, landing-reviewer-design / -brand / -cro / -a11y) et une QA mesurable (${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/qa-landing.py). Orchestre cro-page, copywriting, design-direction, design-system, design-review, accessibility-web et brand-check. Utiliser dès que l'utilisateur demande une landing page, une page de vente, une page de capture, une page d'inscription à un événement, une page d'offre ou de campagne, ou la refonte d'une page de conversion. Entrée : /atelier-web:landing-page."
---

# landing-page : produire une landing page de haut niveau pour la marque du projet

Une landing réussie se lit comme un seul récit, section par section, et amène son visiteur à une seule action. Ce playbook donne la méthode et le système qui y mènent, ni un ordre de sections à recopier ni une apparence : chaque landing a sa propre direction, sinon toutes les pages finissent pareilles.

**La barre.** Une page faite de cartes blanches empilées qui respecte le plan et passe ses tests reste refusée. Ce qu'on vise : des visuels de marque, un hero construit autour d'un objet fort, un ou deux moments de mise en scène au défilement, une alternance de sections claires et de bandes sombres, et partout de la preuve concrète.

## Invariants (à relire en reprenant une session)

**Ordre des phases.** Aucune ne se saute ; un modèle de la fabrique raccourcit les phases 2, 4 et 5, il n'en supprime aucune.

| Phase | Produit | Validation avant la suite |
|---|---|---|
| 0. Doctrine et matière réelle | lecture de `atelier/marque/` ; `landing-researcher` lancé en arrière-plan | doctrine complète, sinon arrêt et skill `demarrer-projet-web` |
| 1. Cadrage en une salve | `atelier/briefs/<slug>.md` | le responsable de la marque valide le brief |
| 2. Directions | 2 ou 3 maquettes nommées par leur objet signature | l'humain choisit |
| 3. Spec | `pilotage/spec.md`, textes définitifs clé par clé | l'humain valide ; la spec est figée pendant la construction |
| 4. Socle et charte | `index.html` assemblé, `pilotage/page-charter.md` | le hero est montré et validé avant le reste |
| 5. Construction parallèle | un fragment par builder, le contrôleur seul assemble | QA après chaque assemblage |
| 6. Montrer, appliquer | chemin de la page et points à regarder, après chaque étape | chaque retour écrit au § 9 de la charte |
| 7. Mesure, revues, corrections | `pilotage/qa.json`, quatre `review-*.md`, `fix-wave-brief.md` | QA à zéro erreur après la vague |
| 8. Livraison | contrôles bloquants, enregistrement, publication | go explicite de l'humain pour chaque commit, push et publication |

**Contrôles bloquants de la phase 8**, tous :
- `python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/qa-landing.py atelier/landings/<slug>/index.html` sans erreur aux trois tailles d'écran et en mouvement réduit ; les avertissements restants sont listés et assumés dans le rapport de livraison ;
- agent `a11y-auditor` (rendu réel, axe-core, parcours clavier complet) : aucun constat bloquant ni majeur ;
- `python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/lint-brand.py atelier/landings/<slug>/index.html` sans erreur ;
- skill `brand-check` (texte et visuel) : verdict positif ;
- aucun secret ni identifiant en dur dans le diff (l'ID de mesure vit dans la configuration).

**Règles dures.**
- **Contenu** : aucun chiffre, client, logo, témoignage, compteur ni fait sur une personne inventé. Un compteur sans vrai chiffre reste vide.
- **Une page, un objectif** : tous les boutons mènent à la conversion ou à l'étape de choix qui y conduit. Pas de navigation complète : logo et CTA suffisent. Le CTA primaire porte `data-cta="primaire"`.
- **Urgence honnête** : vraies places, vraie date de clôture, comptées en jours. Jamais de compte à rebours en secondes.
- **Fichiers** : un fichier, un propriétaire. Aucun agent n'écrit dans un fichier qu'on ne lui a pas confié ; le contrôleur seul assemble et commite.
- **Actions refusées** : une action refusée à un agent (suppression, navigation, écriture) n'est refaite par personne sans l'accord de l'humain.
- **Outils tiers** : toute écriture dans un outil de vente, d'emailing ou de calendrier passe par un dry-run montré, puis un go.
- **Mouvement** : `prefers-reduced-motion: reduce` affiche tout, d'emblée, et rien ne bouge.

**Reprendre** après une compaction ou une limite d'usage : relire `pilotage/` (spec, charte et son § 9, rapports, revues, `fix-wave-brief.md`) et `git log` pour situer la phase ; reprendre un agent coupé par `SendMessage`, jamais par un agent neuf.

**Chemins.** Scripts dans `${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/` (`assemble-landing.py`, `qa-landing.py`, `controle-fonds.py`, `lint-brand.py`), lancés depuis la racine du projet. Références du skill, à lire au moment indiqué :

| Fichier | Quand |
|---|---|
| `references/charte.md` | phase 4 : copiée dans `pilotage/page-charter.md` et donnée à **chaque** agent ; son § 9 (décisions de l'humain) prime sur tout |
| `references/sections.md` | phases 3 à 5 : mécaniques de section, objection servie, anti-modèles, mouvement réduit |
| `references/assemblage.md` | phases 4 à 6 : arborescence, ce que pose l'assembleur, insertion scriptée des fragments, micro-retouches |
| `references/inspiration.md` | phase 0 : méthode de recherche, galeries, filtre de marque |
| `references/pieges.md` | toutes phases : pièges techniques, de session et de marque, avec leur parade |
| `references/revues.md` | phase 7 : lancer les quatre revues, arbitrer |
| `references/mesure.md` | phases 3 et 8 : UTM et événements |
| `references/livraison.md` | phase 8 : budget, publication, checklist de livraison |
| `references/skills-orchestrees.md` | phases 2 à 8 : rôle de chaque skill appelée et repli si elle manque |
| `templates/spec.md`, `templates/brief-section.md`, `templates/brief-corrections.md` | phases 3, 5 et 7 |

## Agents (`${CLAUDE_PLUGIN_ROOT}/agents/`)

| Agent | Phase | Rôle |
|---|---|---|
| `landing-researcher` | 0, en arrière-plan | Benchmark de pages qui convertissent et recherche visuelle, consolidés dans `pilotage/research-notes.md`. Ne code rien |
| `landing-section-builder` | 4 à 7 | Construit ou corrige une section (ou un lot) dans les seuls fichiers qu'on lui confie. Ne commite jamais |
| `landing-reviewer-design` / `-brand` / `-cro` / `-a11y` | 7 | Webdesign ; marque ; conversion ; WCAG 2.2 AA en 14 points. En lecture seule : ils n'écrivent que leur rapport |
| `a11y-auditor` | 8 | Rendu réel, axe-core, parcours clavier |

Avec le plugin actif, les agents s'appellent `atelier-web:<nom>` ; si un type n'est pas reconnu (registre chargé au démarrage), dispatcher un agent généraliste dont le prompt commence par « Lis et applique `${CLAUDE_PLUGIN_ROOT}/agents/<nom>.md` ».

## Gabarit de données ou page sur mesure

- **Gabarit** : une spec qui assemble des sections de la bibliothèque (compositions de départ dans `${CLAUDE_PLUGIN_ROOT}/fabrique/templates/sections/README.md`, catalogue visuel généré depuis `catalogue.json`) ou un des six modèles de `${CLAUDE_PLUGIN_ROOT}/fabrique/templates/landing-pages/`, slots remplis puis assemblés. Pour une offre courante, un délai court, une série de pages de même forme. Le modèle ne dispense ni du brief, ni de la charte, ni de la QA, ni des revues de marque et de conversion, ni du brand-check.
- **Sur mesure** : tout le playbook, pour une offre phare, un lancement, un ticket élevé, une signature visuelle propre. Les sections courantes viennent quand même de la bibliothèque ; une section créée ici qui servira ailleurs y entre comme fragment (« réutiliser avant de créer »).

Une section qui figure sur deux pages est **la même section** : même fragment, mêmes jetons, au pixel près.

## Phase 0 : doctrine et matière réelle

1. **Doctrine**, jamais de mémoire : dans `atelier/marque/`, `checklist-pre-composition.md`, `voice.md`, `anti-ai-writing-style.md`, `messaging-framework.md` (chiffres et hiérarchie de preuves), `personas.md`, `style-guide.md` et `tokens.json` (valeurs exactes), `design-anti-generique.md`, `divulgation-ia.md`, `droits.md`, `exemples-rejetes.md` ; puis le `CLAUDE.md` du projet (§ Atelier web : conventions, publication). Un fichier manquant ou qui porte encore des `{{...}}` : arrêter et lancer `demarrer-projet-web`.
2. **Matière réelle** : document de l'offre (programme, proposition, fiche produit), chiffres des rapports du projet, calendrier éditorial s'il existe, assets de `atelier/marque/assets/` et leur catalogue, pages déjà produites dans `atelier/landings/`. Une intel confidentielle se reformule, et aucun fait sur une personne n'en vient.
3. **Nom de l'offre** : vérifier que le nom ou la marque affichés ont le droit de porter un prix et des dates (marque tierce, partenaire, programme officiel).
4. **Recherche** : lancer tout de suite `landing-researcher` en arrière-plan, avec l'offre, l'audience et les besoins de section pressentis.

## Phase 1 : cadrage, en une seule salve

Toutes les questions bloquantes en une fois (outil de question à choix s'il existe), chacune avec l'option recommandée en premier et la conséquence de chaque option :

1. **Audience et accès** : page publique indexée (`robots`, JSON-LD, liens depuis le site) ou lien direct en `noindex`.
2. **Objectif unique et action de conversion** : réservation, rendez-vous, formulaire, achat, téléchargement, appel.
3. **Circuit de vente** : qui inscrit, facture, encaisse, confirme. Il réécrit le bloc de conversion, les étapes et la FAQ : il se tranche avant ces textes.
4. **Chiffres affichés** : places, prix (HT ou TTC), dates, remises, échéance. Signaler chaque écart entre la demande et le document source : le document fait foi.
5. **Preuves disponibles** : vraies personnes (avec leur accord pour le portrait), vrais documents, chiffres, témoignages. Ce qui manque ne s'invente pas.
6. **Visuels** : réutiliser la bibliothèque, ou générer (outil d'images du projet), avec le coût de chaque option.
7. **Source de trafic et mesure** : d'où viennent les visiteurs (message match), suivi d'audience actif ou non.

Un point ouvert se formule dans les mots de l'humain : ce que voit le visiteur, et pourquoi ça compte. Les réponses vont dans `atelier/briefs/<slug>.md` (objectif, cible et niveau de conscience, offre, trafic, preuves, métrique de succès).

## Phase 2 : directions

Montrer 2 ou 3 directions en maquettes rapides (widget, capture ou page jetable dans le scratchpad), chacune nommée par son **objet signature**, l'élément dont on se souviendra ; en recommander une ; écarter toute direction qui reprend la signature d'une autre page de la marque. Appliquer le workflow en deux passes de `atelier/marque/design-anti-generique.md` § 3 (plan de jetons, puis auto-critique contre le brief) et la skill `design-direction`, sous les jetons de `tokens.json` : la marque prime, la skill décide des compositions, jamais des couleurs ni des polices. Une fois la direction choisie, détailler la conception dans la conversation et la faire valider.

## Phase 3 : spec

`pilotage/spec.md` depuis `templates/spec.md` : le cadre (réponses de la phase 1 et leur source) ; la direction et son objet signature ; le récit, une ligne par section (objection traitée, mécanique de `references/sections.md`, moment orchestré, fond) ; les comportements (état de l'offre, ouverte, liste d'attente ou close, piloté par **une seule configuration** en tête du script ; porte de choix ; liens profonds ; échéance ; événements de `references/mesure.md`) ; **les textes définitifs, clé par clé**, dans chaque langue de la marque. Structure CRO par `cro-page`, texte par `copywriting` (puis `copy-editing` si l'enjeu le justifie), chaque chiffre de `messaging-framework.md` ou d'une source citée. Si la spec doit changer en cours de construction, prévenir les agents en cours.

## Phase 4 : poser avant de paralléliser

Le contrôleur (l'agent principal), seul, prépare puis montre :

1. **`index.html` socle**, assemblé depuis `pilotage/page.json` par `python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/assemble-landing.py pilotage/page.json` : `<head>`, jetons, CSS de la charte, un seul moteur d'apparition, relais de mesure, configuration de l'offre, sections courantes remplies (`references/assemblage.md`) ;
2. **une paire de marqueurs par section** à sa place définitive (`<!-- section:<id> -->` … `<!-- /section:<id> -->`), le fragment `_placeholder` pour une section sur mesure à venir ;
3. `pilotage/page-charter.md`, copié de `references/charte.md` et complété (§ 9 : décisions déjà prises), et `pilotage/research-notes.md` à côté.

**Le hero d'abord** : le construire, le montrer et le faire valider avant le reste. Un hero raté entraîne toute la page.

## Phase 5 : construction en parallèle

- **Un agent par section** : un `landing-section-builder` propriétaire d'un seul fragment, `pilotage/sections/<nn>-<id>.html` (la `<section>`, son `<style>` préfixé par `#<id>`, son `<script>` éventuel enfermé dans une fonction). Aucun builder n'écrit dans `index.html`. Les lancer tous dans un seul message, chacun avec un brief tiré de `templates/brief-section.md`.
- **Assemblage** : à chaque rapport, le contrôleur branche le fragment dans la spec et réassemble ; si la page a été retouchée à la main, insertion scriptée avec contrôle des marqueurs (`references/assemblage.md`). Puis `qa-landing.py` et un commit, sur go de l'humain si la session l'exige.
- **Recherche visuelle** : faite en amont par `landing-researcher` (la navigation peut être refusée aux agents de section) ; les builders lisent `research-notes.md`.
- **Limite d'usage** : si des agents sont coupés, assembler et commiter ce qui est fini, puis reprendre chacun par `SendMessage` avec l'endroit où il s'est arrêté et la consigne « relis d'abord l'état actuel de ton fichier ».

## Phase 6 : montrer, écouter, appliquer

- **Montrer** après chaque étape : le chemin ou l'URL locale de la page (serveur statique depuis la racine du dépôt si la page lit `atelier/marque/assets/`), avec la liste des points à regarder, puis enchaîner sans attendre.
- **Appliquer un retour**, puis l'écrire au § 9 de `pilotage/page-charter.md`. S'il vaut pour toutes les landings, proposer de le reporter dans la doctrine (`style-guide.md`, `exemples-rejetes.md`) ou dans ce skill.
- **Micro-retouches** : par le contrôleur, en remplacement scripté qui vérifie la chaîne d'origine, puis QA et commit.
- **Ce que les revues ne voient pas** : un en-tête collé, un fond qui masque la matière, un épinglage absent, une page qui « fait template ». L'œil de l'humain reste la dernière porte.

## Phase 7 : mesure, quatre revues, une vague de corrections

1. **Mesure** : `python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/qa-landing.py <index.html> --format json > pilotage/qa.json`. Les relecteurs partent de ces constats au lieu de les recalculer.
2. **Revues** : les quatre relecteurs en parallèle, dans un seul message, en lecture seule ; chacun écrit `pilotage/review-<grille>.md` (`references/revues.md`).
3. **Arbitrage** : `pilotage/fix-wave-brief.md` depuis `templates/brief-corrections.md`. Les décisions de l'humain priment, aucun chiffre n'est inventé, une structure reçoit une seule valeur, les décisions business ou légales sont posées à l'humain en une fois.
4. **Corrections** : deux `landing-section-builder` en parallèle sur des fragments disjoints (sections 1 à 4, 5 à 8). Le socle (`index.html` hors marqueurs) et toute section partagée avec d'autres pages se corrigent par le contrôleur, à l'identique partout. Constats tardifs et retours de l'humain partent aux deux agents par `SendMessage`, avec la mention « ils priment sur le brief ».
5. **Clôture** : assembler, relancer la QA jusqu'à zéro erreur, montrer la page.

## Phase 8 : livraison

Les contrôles bloquants des invariants, tous au vert ; puis budget, enregistrement dans `atelier/publie.md`, publication par dry-run sans `pilotage/` et contrôle en ligne (`references/livraison.md`, avec la checklist). Commit, push et publication seulement sur go explicite de l'humain, à chaque fois.

## Skills orchestrées

`cro-page` (structure CRO), `copywriting` et `copy-editing` (textes, obligatoires), `design-direction`, `design-system` et `design-taste` (directions et système visuel, sous les jetons de la marque), `design-review`, `motion-defilement` (pile et grammaire du mouvement), `page-web`, `qa-rendu`, `accessibility-web`, `cro-form` et `lead-magnet` (capture), l'outil d'images du projet, et `brand-check` (validation finale, obligatoire). Rôle de chacune et repli si elle manque : `references/skills-orchestrees.md`.
