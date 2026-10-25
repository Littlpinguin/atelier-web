# Évals de l'atelier web

Suite `claude plugin eval` du plugin. Chaque cas tourne avec et sans le plugin ; l'écart `Δ` mesure ce que l'atelier apporte. Elle sert de filet avant toute refonte des skills (consolidation, descriptions raccourcies) : un changement de description peut faire tomber un déclenchement, et seule une éval le voit.

## Ce que mesurent les 17 cas

| Groupe | Cas | Ce qui est vérifié |
|---|---|---|
| `orientation` | `initialiser-atelier` | Sans doctrine, le hub demande la matière réelle (site, contenus, documents, chiffres sourcés) et n'invente aucune valeur de marque |
| | `landing-sans-doctrine` | Une demande de landing sans doctrine s'arrête et renvoie à la pose de la doctrine |
| | `orienter-page-tarifs` | Doctrine posée : la réponse s'appuie sur la doctrine du projet et n'invente ni prix ni chiffre |
| `declenchement` | `landing-cadrage` | `landing-page` lit la doctrine et pose le cadrage en une salve |
| | `page-web-section` | `page-web` n'invente aucun témoignage et reprend le système du site |
| | `motion-trop-statique` | Le mouvement passe par le CSS piloté par le défilement et le mouvement réduit, sans AOS |
| | `lottie-integration` | Une animation Lottie passe par dotLottie, avec mouvement réduit et pause |
| | `brand-check-brouillon` | Vocabulaire banni, cadratin et chiffre non sourcé relevés avant publication |
| | `cro-formulaire` | Formulaire de démo ramené à ses champs essentiels |
| | `directions-hero` | Deux directions nommées par leur objet signature, aux jetons de la marque |
| | `lead-magnet-calculateur` | Circuit de capture complet, aucun résultat promis sans hypothèse |
| `quasi-cas` | `script-python`, `css-sticky`, `plan-slides` | Aucune skill de l'atelier ne se déclenche |
| | `email-relance`, `post-linkedin` | Dans un projet doté d'une doctrine, aucune skill de page, de design ou de conversion (les skills de relecture restent permises) |
| `bout-en-bout` | `landing-matinale` | Landing assemblée par la fabrique depuis le modèle `evenement`, marqueurs branchés, CTA primaire posé, lint de marque lancé, reste à faire annoncé sans rien publier |

Les graders `tool_used: Skill` sont des indicateurs (« la skill s'est déclenchée ») : ils ne comptent pas dans le score d'un run à deux bras. Le score repose sur le résultat (regex sur la réponse ou le fichier produit, juge sur un critère PASS/FAIL) et sur le chemin suivi (lecture de la doctrine, appel du linter).

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
- `--disallow-tools Agent` : sans lui, `landing-page` lance `landing-researcher` en arrière-plan, le réseau du bac à sable bloque ses galeries, et la réponse jugée de `landing-cadrage` devient le compte rendu de cette recherche.
- Juge Sonnet : Haiku a rendu un faux négatif sur `brand-check-brouillon` au passage du 25/10/2026.
- Trois runs par cas et par bras (défaut) ; modèles épinglés pour comparer les passages entre eux : un changement de modèle n'est pas une régression du plugin.
- Un seul cas, un seul bras, pour itérer : `claude plugin eval /tmp/atelier-web-eval --case <cas> --runs 1 --ablation none --scaffold --trust-plugin`.
- Avec Claude Code 2.1.308, `--keep-temp` fait refuser les cas à fixture (« more than one hard link ») : le garder pour les cas sans fixture.
- Les résultats vont dans `results/`, ignoré par git.

## Δ de référence

Passage du 25/10/2026 sur la version 1.1.0 (suite au commit `0278591`), lancé depuis une copie hors du dossier personnel : trois runs par cas et par bras, Claude Code 2.1.308, Sonnet 5.5 sous test et en juge, `--disallow-tools Agent`, compte Max. 102 runs, 829 s, 12,15 $ en prix catalogue. Δ moyen **+0,21** ; score moyen avec le plugin 0,92.

| Cas | Avec | Sans | Δ | Coût |
|---|---|---|---|---|
| `initialiser-atelier` | 1,00 | 0,00 | +1,00 | 0,52 $ |
| `landing-sans-doctrine` | 1,00 | 0,00 | +1,00 | 0,70 $ |
| `orienter-page-tarifs` | 0,67 | 1,00 | −0,33 | 0,65 $ |
| `landing-cadrage` | 0,67 | 0,50 | +0,17 | 1,11 $ |
| `page-web-section` | 1,00 | 1,00 | 0,00 | 0,79 $ |
| `motion-trop-statique` | 1,00 | 0,78 | +0,22 | 0,69 $ |
| `lottie-integration` | 1,00 | 0,67 | +0,33 | 0,71 $ |
| `brand-check-brouillon` | 1,00 | 0,67 | +0,33 | 0,78 $ |
| `cro-formulaire` | 1,00 | 1,00 | 0,00 | 0,46 $ |
| `directions-hero` | 1,00 | 0,67 | +0,33 | 1,17 $ |
| `lead-magnet-calculateur` | 0,33 | 0,67 | −0,33 | 0,78 $ |
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

**Δ négatifs, à lire comme des constats sur les skills** :
- `lead-magnet-calculateur` : avec le plugin, la première réponse présente des formats à choisir et oublie le consentement deux fois sur trois ; sans le plugin, Claude y pense trois fois sur trois. Le circuit de capture « obligatoire » de la skill ne remonte pas jusqu'à sa première réponse.
- `orienter-page-tarifs` : un run sur trois avec le plugin déroule une méthode (diagnostic, packaging, copy, conversion) en citant `personas.md` et `messaging-framework.md` sans rien en tirer de concret ; sans le plugin, Claude cite Nadia, Marc ou les chiffres de la marque à chaque run.

**Artefacts de la suite encore visibles** :
- `landing-cadrage` : le grader `lit-la-doctrine` compte zéro lecture de `voice.md`, `messaging-framework.md` ou `checklist-pre-composition.md` dans deux runs avec le plugin, alors que la réponse dit avoir lu « la voix, les chiffres, les personas » : lecture probablement passée par un autre outil (Grep, par exemple), à vérifier sur une trace avant d'élargir le grader.
- `landing-matinale`, run 1 avec le plugin : la page passe tous les contrôles de fichier, mais la réponse jugée est le message envoyé après la fin d'une commande lancée en arrière-plan, pas le compte rendu.

Passage précédent, réduit (un run par bras, juge Haiku, depuis `~/claude-projets`) : Δ moyen +0,07, 3,82 $. Il a servi à trouver les corrections appliquées depuis (copie hors du dossier personnel, juge Sonnet, agent de recherche coupé, critères de `lead-magnet-calculateur` et `script-python`).
