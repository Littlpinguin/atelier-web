# Évals de l'atelier web

Suite `claude plugin eval` du plugin. Chaque cas tourne avec et sans le plugin ; l'écart `Δ` mesure ce que l'atelier apporte. Elle sert de filet avant toute refonte des skills (consolidation, descriptions raccourcies) : un changement de description peut faire tomber un déclenchement, et seule une éval le voit.

## Ce que mesurent les 26 cas

| Groupe | Cas | Ce qui est vérifié |
|---|---|---|
| `orientation` | `initialiser-atelier` | Sans doctrine, le hub demande la matière réelle (site, contenus, documents, chiffres sourcés) et n'invente aucune valeur de marque |
| | `landing-sans-doctrine` | Une demande de landing sans doctrine s'arrête et renvoie à la pose de la doctrine |
| | `orienter-page-tarifs` | Doctrine posée : la réponse s'appuie sur la doctrine du projet et n'invente ni prix ni chiffre |
| `declenchement` | `landing-cadrage` | `landing-page` lit la doctrine (Read ou commande Bash, regex sur la trace) et pose le cadrage en une salve |
| | `page-web-section` | `page-web` n'invente aucun témoignage et reprend le système du site |
| | `motion-trop-statique` | Le mouvement passe par le CSS piloté par le défilement et le mouvement réduit, sans AOS |
| | `lottie-integration` | Une animation Lottie passe par dotLottie, avec mouvement réduit et pause |
| | `brand-check-brouillon` | Vocabulaire banni, cadratin et chiffre non sourcé relevés avant publication |
| | `cro-formulaire` | Formulaire de démo ramené à ses champs essentiels |
| | `directions-hero` | Deux directions nommées par leur objet signature, aux jetons de la marque |
| | `lead-magnet-calculateur` | Circuit de capture complet, aucun résultat promis sans hypothèse |
| | `design-refonte` | `design`, route refondre : défauts « IA » de la page nommés, couleurs de la marque, correctifs ciblés par ordre de priorité, URL et champs du formulaire intacts |
| | `design-systeme` | `design`, route systématiser : bloc `:root` sur les valeurs, les polices et les rayons de la marque |
| | `motion-epinglage` | `motion` : épinglage réservé aux grands écrans et au mouvement permis, étapes toutes visibles sinon, aucun écouteur `scroll` |
| | `cro-popup-sortie` | `cro`, pop-up : une fois par visite, refus mémorisé, fermeture facile, rien en plein écran sur mobile, consentement |
| | `cro-page-diagnostic` | `cro`, page : hero, sorties concurrentes, formulaire réduit, CTA de la doctrine, aucun fait inventé |
| | `ecriture-page` | `ecriture`, rédiger : texte écrit dans `atelier/pages/comment-ca-marche.md` ; cadratin, termes bannis, vouvoiement, titres sans point et vocabulaire contrôlés par regex sur le fichier ; origine des faits jugée sur le fichier |
| | `ecriture-humaniser` | `ecriture`, relire : parallélisme négatif et formules creuses retirés, aucun fait inventé |
| | `revue-accessibilite` | `revue`, accessibilité : au moins cinq défauts WCAG relevés, chacun avec sa correction |
| | `revue-debordement` | `revue`, rendu : causes de débordement sur mobile, corrections, mesure encore à faire |
| `quasi-cas` | `script-python`, `css-sticky`, `plan-slides` | Aucune skill de l'atelier ne se déclenche |
| | `email-relance`, `post-linkedin` | Dans un projet doté d'une doctrine, aucune skill de page, de design, de mouvement, de conversion ni de revue (`brand-check` et `ecriture`, qui porte la relecture, restent permises) |
| `bout-en-bout` | `landing-matinale` | Landing assemblée par la fabrique depuis le modèle `evenement`, marqueurs branchés, CTA primaire posé, lint de marque lancé, reste à faire annoncé sans rien publier |

Les graders `tool_used: Skill` sont des indicateurs (« la skill s'est déclenchée ») : ils ne comptent pas dans le score d'un run à deux bras. Le score repose sur le résultat (regex sur la réponse ou le fichier produit, juge sur un critère PASS/FAIL) et sur le chemin suivi (lecture de la doctrine, appel du linter).

Les neuf cas du tag `fusion` ont été ajoutés avant la consolidation de la version 1.2.0 (24 skills devenues 10), pour mesurer le déclenchement des skills fusionnées. Leurs graders de déclenchement, comme ceux des cas plus anciens, acceptent l'ancien et le nouveau nom de la skill attendue : la même suite compare les deux versions. Les quasi-cas interdisent aussi les nouvelles skills.

## Doctrine de test

Les runs d'éval ne chargent ni `CLAUDE.md` ni `.claude/` ni la mémoire. La doctrine arrive donc en fichiers : `_fixtures/projet-brivalle/` est le projet d'une marque **fictive** (Brivalle, éditeur de logiciel de tournées, déjà utilisée par le modèle `evenement`), avec une doctrine complète dans `atelier/marque/` (aucun `{{…}}`), un bloc « Atelier web » (`CLAUDE-projet.md`, copié en `CLAUDE.md`) et le document d'une offre. Le `installer.sh` de chaque cas qui en a besoin la copie dans l'espace de travail vide (`context.scaffold_script`). Aucune donnée réelle de client ni de personne.

La même fixture sert aux tests de bout en bout de la fabrique : copier `projet-brivalle/` dans un dossier d'essai, renommer `CLAUDE-projet.md`, puis `build-tokens.py`, `assemble-landing.py` d'un modèle, `qa-landing.py` et `lint-brand.py` depuis sa racine.

## Lancer

Claude Code 2.1.269 ou plus, CLI connecté (`claude auth status`). Depuis la racine du dépôt, copier le plugin hors du dossier personnel puis lancer la suite sur cette copie :

```bash
rsync -a --delete --exclude evals/results --exclude __pycache__ plugins/atelier-web/ /tmp/atelier-web-eval/
```

```bash
claude plugin eval /tmp/atelier-web-eval --scaffold --trust-plugin --allow-tools Write Edit Bash --disallow-tools Agent --model claude-sonnet-5-5 --judge-model claude-sonnet-5-5 --no-publish --max-cost-usd 25 -j 4
```

- **Copie hors du dossier personnel** : le bac à sable des runs rend le dossier personnel illisible pour Bash. Depuis `~/claude-projets/…`, les scripts de la fabrique ne se lancent pas et le cas de bout en bout échoue avec le plugin (constaté le 25/10/2026). Les résultats sortent alors dans `/tmp/atelier-web-eval/evals/results/`.
- `--scaffold` installe la fixture ; `--allow-tools Write Edit Bash` n'est utile qu'au cas de bout en bout (Bash tourne dans le bac à sable du système).
- `--disallow-tools Agent` : sans lui, `landing-page` lance `inspiration-researcher` en arrière-plan, le réseau du bac à sable bloque ses galeries, et la réponse jugée de `landing-cadrage` devient le compte rendu de cette recherche.
- Juge Sonnet : Haiku a rendu un faux négatif sur `brand-check-brouillon` au passage du 25/10/2026.
- Trois runs par cas et par bras (défaut) ; modèles épinglés pour comparer les passages entre eux : un changement de modèle n'est pas une régression du plugin.
- `--case` ne garde que sa dernière occurrence : lancer un passage par cas pour en rejouer plusieurs. Les neuf cas de la consolidation, seuls : `--tag fusion`.
- `--allow-tools Bash` vaut pour tous les cas, malgré leur `allowed_tools` : Claude peut alors lire la doctrine par `cat`, ce qu'un grader `tool_used: Read` ne voit pas (`tool_used` compare un nom d'outil exact, sans alternative). Pour un chemin suivi par plusieurs outils, viser la trace : `target: trace`, où chaque appel s'écrit `"name":"Bash","input":{"command":"…"}` (voir `lit-la-doctrine` de `landing-cadrage`).
- Un contrôle d'absence sur un fichier (cadratin, termes bannis) s'écrit en motif positif, `^(?![\s\S]*<motif>)[\s\S]+$` : il échoue alors sur un fichier vide ou absent, au lieu de passer à vide.
- Garder la trace d'un run : elle vit dans `/private/tmp/e-*/out/trace.jsonl` le temps du run et disparaît ensuite ; la copier pendant le run. `--debug-file` est une option globale (`claude --debug-file <fichier> plugin eval …`) et ne journalise que le type des évènements.
- Un seul cas, un seul bras, pour itérer : `claude plugin eval /tmp/atelier-web-eval --case <cas> --runs 1 --ablation none --scaffold --trust-plugin`.
- Avec Claude Code 2.1.308, `--keep-temp` fait refuser les cas à fixture (« more than one hard link ») : le garder pour les cas sans fixture.
- Les résultats vont dans `results/`, ignoré par git.

## Δ de référence

### Version 1.2.1 (graders revus, hook corrigé)

Trois graders revus (voir le `CHANGELOG.md` à la racine), et le hook ne réagit plus aux commandes en lecture seule. Les trois cas concernés ont été rejoués à trois runs par bras, avant la refonte (24 skills) et sur la version 1.2.1. Deux cas où le hook travaille le plus l'ont été sur la version 1.2.1 : `revue-debordement`, où un `ls` déclenchait le rappel, et `landing-matinale`, où la page est assemblée par script. Mêmes réglages que le passage complet ; ≈ 11 $.

| Cas | Avec | Sans | Δ 1.2.1 | Δ avant la refonte, mêmes graders |
|---|---|---|---|---|
| `landing-cadrage` | 1,00 | 0,67 | **+0,33** | +0,50 |
| `directions-hero` | 1,00 | 0,67 | **+0,33** | +0,17 |
| `ecriture-page` | 1,00 | 1,00 | **0,00** | 0,00 |
| `revue-debordement` | 1,00 | 1,00 | **0,00** | −1,00 |
| `landing-matinale` | 1,00 | 0,05 | **+0,95** | +0,90 |

`lit-la-doctrine` passe désormais 3 fois sur 3 avec le plugin, avant comme après la refonte : la lecture par `cat` était bien là. Avec ses nouveaux contrôles, déterministes, `ecriture-page` montre que Claude seul, dans un projet doté d'une doctrine, la lit et écrit un texte conforme : Δ nul, comme `cro-formulaire`. `landing-matinale` garde tous ses contrôles avec le nouveau hook (lint lancé 3 fois sur 3).

**Δ moyen consolidé** (les cinq cas ci-dessus à leur valeur 1.2.1, les autres au passage complet 1.2.0) : **+0,32** sur 26 cas, contre +0,28 pour la même suite avant la refonte. Sur les 17 cas d'origine, +0,30 contre +0,30. Sur les neuf cas `fusion`, +0,36 contre +0,25. Score moyen avec le plugin : 0,97 sur 26 cas, 1,00 sur les 17 cas d'origine.

### Version 1.2.0 (dix skills)

Passage du 25/10/2026 sur la version consolidée, dans les mêmes conditions que celui de la version 1.1.0 (copie dans le dossier temporaire de session, trois runs par cas et par bras, Claude Code 2.1.308, Sonnet 5.5 sous test et en juge, `--disallow-tools Agent`, compte Max) : 156 runs, 1 560 s, 20,56 $ en prix catalogue. La colonne « Δ avant la refonte » reprend la référence 1.1.0 pour les 17 cas d'origine et, pour les neuf cas `fusion`, leur passage sur les 24 skills juste avant la consolidation (7,71 $). Quatre graders de ces cas ont été précisés avant comparaison, et les deux bras rejoués de part et d'autre (≈ 5 $) : ils refusaient des faits pourtant tirés du messaging framework (« six mois », « une matinée au tableur »), comptaient une couleur d'état fonctionnelle comme une teinte de marque, ou imposaient l'ordre de présentation des correctifs. La ligne `ecriture-page` vient de ce rejeu.

| Cas | Avec | Sans | Δ | Δ avant la refonte | Déclenchement | Coût |
|---|---|---|---|---|---|---|
| `initialiser-atelier` | 1,00 | 0,00 | **+1,00** | +1,00 | 3/3 | 0,50 $ |
| `landing-sans-doctrine` | 1,00 | 0,00 | **+1,00** | +1,00 | 3/3 | 0,75 $ |
| `orienter-page-tarifs` | 1,00 | 1,00 | **0,00** | 0,00 | 3/3 | 0,91 $ |
| `landing-cadrage` | 0,50 | 0,50 | **0,00** | +0,17 | 3/3 | 1,17 $ |
| `page-web-section` | 1,00 | 1,00 | **0,00** | 0,00 | 3/3 | 0,80 $ |
| `motion-trop-statique` | 1,00 | 0,78 | **+0,22** | +0,22 | 3/3 | 0,72 $ |
| `lottie-integration` | 1,00 | 0,89 | **+0,11** | +0,33 | 3/3 | 0,88 $ |
| `brand-check-brouillon` | 1,00 | 0,78 | **+0,22** | +0,33 | 3/3 | 0,75 $ |
| `cro-formulaire` | 1,00 | 1,00 | **0,00** | 0,00 | 3/3 | 0,63 $ |
| `directions-hero` | 0,83 | 0,67 | **+0,17** | +0,33 | 3/3 | 1,68 $ |
| `lead-magnet-calculateur` | 1,00 | 0,00 | **+1,00** | +0,67 | 3/3 | 0,80 $ |
| `design-refonte` (fusion) | 0,83 | 0,67 | **+0,17** | +0,33 | 3/3 | 1,21 $ |
| `design-systeme` (fusion) | 1,00 | 0,33 | **+0,67** | +0,67 | 3/3 | 1,02 $ |
| `motion-epinglage` (fusion) | 1,00 | 0,44 | **+0,56** | +0,44 | 3/3 | 1,30 $ |
| `cro-popup-sortie` (fusion) | 0,67 | 0,00 | **+0,67** | +1,00 | 3/3 | 0,98 $ |
| `cro-page-diagnostic` (fusion) | 1,00 | 0,50 | **+0,50** | −0,17 | 3/3 | 1,02 $ |
| `ecriture-page` (fusion) | 0,33 | 0,00 | **+0,33** | 0,00 | 3/3 | 1,37 $ |
| `ecriture-humaniser` (fusion) | 0,67 | 0,00 | **+0,67** | +1,00 | 3/3 | 0,92 $ |
| `revue-accessibilite` (fusion) | 1,00 | 1,00 | **0,00** | 0,00 | 3/3 | 0,76 $ |
| `revue-debordement` (fusion) | 1,00 | 0,67 | **+0,33** | −1,00 | 3/3 | 0,80 $ |
| `script-python` | 1,00 | 1,00 | **0,00** | 0,00 | 3/3 | 0,36 $ |
| `css-sticky` | 1,00 | 1,00 | **0,00** | 0,00 | 3/3 | 0,37 $ |
| `plan-slides` | 1,00 | 1,00 | **0,00** | 0,00 | 3/3 | 0,44 $ |
| `email-relance` | 1,00 | 1,00 | **0,00** | 0,00 | 3/3 | 0,38 $ |
| `post-linkedin` | 1,00 | 1,00 | **0,00** | 0,00 | 3/3 | 0,38 $ |
| `landing-matinale` | 1,00 | 0,05 | **+0,95** | +0,90 | 3/3 | 1,99 $ |

Pour un quasi-cas, « 3/3 » dans la colonne Déclenchement signifie qu'aucune skill de l'atelier ne s'est déclenchée dans les trois runs.

**Δ moyen** : **+0,33** sur les 26 cas, contre +0,28 pour la même suite avant la refonte. Sur les 17 cas d'origine, +0,275 contre +0,29 ; sur les neuf cas `fusion`, +0,43 contre +0,25. Score moyen avec le plugin : 0,92 sur 26 cas, 0,96 sur les 17 cas d'origine (0,98 en 1.1.0).

**Déclenchement** : avec le plugin, chacun des 21 cas qui attend une skill la déclenche 3 fois sur 3, et les 5 quasi-cas n'en déclenchent aucune, 3 fois sur 3. `design-systeme` passe de 1 sur 3 (ancienne `design-system`) à 3 sur 3 (`design`).

**Ce que la consolidation a corrigé, mesuré** : réunir les skills a fait apparaître trois contradictions, levées dans la version 1.2.0.
- `revue-debordement` (−1,00 → +0,33) : l'ancienne `qa-rendu` demandait de s'arrêter sans Playwright ; Claude refusait alors tout diagnostic. La revue de rendu fait désormais une revue statique au verdict partiel, comme `a11y-auditor`.
- `cro-page-diagnostic` (−0,17 → +0,50) : sans le plugin, Claude allait lire le document de l'offre (date, lieu, 120 places) ; l'ancienne `cro-page` ne lisait que la doctrine. La skill `cro` lit aussi la matière de l'offre.
- `motion-epinglage` (+0,44 → +0,56) : l'ancienne `motion-defilement` faisait « calculer la progression au défilement », d'où un écouteur `scroll` que `design-taste` bannissait (2 runs sur 3). L'épinglage passe par une timeline de défilement CSS ou par ScrollTrigger : 0 écouteur sur 3 runs.

**Baisses sur les 17 cas d'origine, lues sur les réponses** :
- `landing-cadrage` (+0,17 → 0,00) : artefact du grader `lit-la-doctrine`, confirmé par une trace et corrigé en 1.2.1. Avec le plugin, Claude lit `voice.md`, `messaging-framework.md` et `checklist-pre-composition.md` par `cat` dans Bash, que le grader ne compte pas (voir § Lancer). Le cadrage en une salve passe 3 fois sur 3 avec le plugin, 0 fois sans.
- `lottie-integration` et `brand-check-brouillon` : le bras avec le plugin reste à 1,00 ; c'est le bras sans qui monte (0,67 → 0,89 et 0,67 → 0,78), du bruit de base à trois runs.
- `directions-hero` : un run sur trois nomme les couleurs par leurs variables (`--color-primary`, `--color-light`) ; le regex `jetons-de-la-marque` ne cherche que les valeurs hexadécimales. Grader élargi en 1.2.1 aux variables `--brand-*` et à JetBrains Mono.
- `ecriture-page` reste bas avec le plugin (0,33) alors que les textes relus tiennent le critère à la lecture : le juge est plus sévère que la consigne. Remplacé en 1.2.1 par des contrôles déterministes sur le fichier écrit.

La copie évaluée diffère du commit par la seule écriture de six renvois croisés en chemin complet (`${CLAUDE_PLUGIN_ROOT}/skills/…`), faite après le passage.

### Version 1.1.0 (24 skills)

Passage du 25/10/2026 sur la version 1.1.0 (suite au commit `0278591`), lancé depuis une copie hors du dossier personnel : trois runs par cas et par bras, Claude Code 2.1.308, Sonnet 5.5 sous test et en juge, `--disallow-tools Agent`, compte Max. 102 runs, 829 s, 12,15 $ en prix catalogue. Δ moyen **+0,21** ; score moyen avec le plugin 0,92. Après correction de `lead-magnet` et de `cro-pricing`, les deux cas en Δ négatif ont été rejoués à trois runs avec les mêmes réglages (valeurs après la flèche, 1,54 $) : en les reportant, le Δ moyen passe à ≈ +0,29.

| Cas | Avec | Sans | Δ | Coût |
|---|---|---|---|---|
| `initialiser-atelier` | 1,00 | 0,00 | +1,00 | 0,52 $ |
| `landing-sans-doctrine` | 1,00 | 0,00 | +1,00 | 0,70 $ |
| `orienter-page-tarifs` | 0,67 → **1,00** | 1,00 | −0,33 → **0,00** | 0,65 $ + 0,78 $ |
| `landing-cadrage` | 0,67 | 0,50 | +0,17 | 1,11 $ |
| `page-web-section` | 1,00 | 1,00 | 0,00 | 0,79 $ |
| `motion-trop-statique` | 1,00 | 0,78 | +0,22 | 0,69 $ |
| `lottie-integration` | 1,00 | 0,67 | +0,33 | 0,71 $ |
| `brand-check-brouillon` | 1,00 | 0,67 | +0,33 | 0,78 $ |
| `cro-formulaire` | 1,00 | 1,00 | 0,00 | 0,46 $ |
| `directions-hero` | 1,00 | 0,67 | +0,33 | 1,17 $ |
| `lead-magnet-calculateur` | 0,33 → **1,00** | 0,67 → 0,33 | −0,33 → **+0,67** | 0,78 $ + 0,76 $ |
| `script-python` | 1,00 | 1,00 | 0,00 | 0,41 $ |
| `css-sticky` | 1,00 | 1,00 | 0,00 | 0,36 $ |
| `plan-slides` | 1,00 | 1,00 | 0,00 | 0,41 $ |
| `email-relance` | 1,00 | 1,00 | 0,00 | 0,37 $ |
| `post-linkedin` | 1,00 | 1,00 | 0,00 | 0,35 $ |
| `landing-matinale` | 0,95 | 0,05 | +0,90 | 1,91 $ |

**Déclenchement** : avec le plugin, chacun des 12 cas qui attend une skill la déclenche 3 fois sur 3, et les 5 quasi-cas n'en déclenchent aucune, 3 fois sur 3. Les deux indicateurs restés à zéro au passage réduit étaient du bruit d'un run unique.

**Ce que l'atelier apporte, mesuré** :
- La doctrine d'abord : sans le plugin, Claude écrit toute la landing du webinar dans `index.html` avec ses propres couleurs et, pour poser une charte, ne demande ni contenus récents de la marque ni chiffres sourcés ; avec le plugin, il demande la matière réelle et ne produit rien avant (Δ +1,00 deux fois).
- La fabrique : page assemblée (empreinte de l'assembleur), marqueurs branchés, CTA primaire posé, linter lancé, rien de publié (Δ +0,90). Sans le plugin, aucun run ne produit la page attendue.
- Le cadrage en une salve : le juge le reconnaît 3 fois sur 3 avec le plugin, 0 fois sans.
- La relecture de marque (les quatre défauts relevés à chaque run), dotLottie à la place de lottie-web, le CSS piloté par le défilement, deux directions aux jetons de la marque : Δ +0,22 à +0,33.

**Δ nul à 1,00** (`cro-formulaire`, `page-web-section`, et les cinq quasi-cas par construction) : Claude seul fait aussi bien sur ces critères. Pour `cro-formulaire`, c'est un signe que la skill ajoute peu de capacité ; à considérer lors de la consolidation.

**Δ négatifs du passage, corrigés dans les skills** :
- `lead-magnet-calculateur` : avec le plugin, la première réponse présentait des formats à choisir et oubliait le consentement deux fois sur trois ; le circuit de capture « obligatoire » de la skill n'arrivait qu'à son étape 4. La skill pose désormais, dès la première réponse, la destination de l'email, la contrepartie, le consentement et l'origine des chiffres. Rejeu : 3 runs sur 3 au vert avec le plugin, consentement compris.
- `orienter-page-tarifs` : un run sur trois avec `cro-pricing` déroulait une méthode en citant `personas.md` et `messaging-framework.md` sans rien en tirer ; l'étape 0 réservait la doctrine à la rédaction. Elle vaut maintenant pour le conseil, et la première réponse nomme personas, preuves, chiffres et règles de voix qu'elle en tire. Rejeu : 3 runs sur 3 au vert avec le plugin ; la skill s'est déclenchée 2 fois sur 3, le run sans skill passant aussi.

**Artefacts de la suite encore visibles** :
- `landing-cadrage` : le grader `lit-la-doctrine` compte zéro lecture de `voice.md`, `messaging-framework.md` ou `checklist-pre-composition.md` dans deux runs avec le plugin, alors que la réponse dit avoir lu « la voix, les chiffres, les personas » : lecture probablement passée par un autre outil (Grep, par exemple), à vérifier sur une trace avant d'élargir le grader.
- `landing-matinale`, run 1 avec le plugin : la page passe tous les contrôles de fichier, mais la réponse jugée est le message envoyé après la fin d'une commande lancée en arrière-plan, pas le compte rendu.

Passage précédent, réduit (un run par bras, juge Haiku, depuis `~/claude-projets`) : Δ moyen +0,07, 3,82 $. Il a servi à trouver les corrections appliquées depuis (copie hors du dossier personnel, juge Sonnet, agent de recherche coupé, critères de `lead-magnet-calculateur` et `script-python`).
