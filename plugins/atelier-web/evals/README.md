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

Depuis `plugins/atelier-web/`, Claude Code 2.1.269 ou plus, CLI connecté (`claude auth status`) :

```bash
claude plugin eval . --scaffold --trust-plugin --allow-tools Write Edit Bash --model claude-sonnet-5-5 --judge-model claude-haiku-5-5 --no-publish --max-cost-usd 40 -j 4
```

- `--scaffold` installe la fixture ; `--allow-tools Write Edit Bash` n'est utile qu'au cas de bout en bout (Bash tourne dans le bac à sable du système).
- **Lancer la suite depuis une copie du plugin placée hors du dossier personnel**, par exemple `rsync -a --exclude evals/results plugins/atelier-web/ /tmp/atelier-web-eval/` puis `claude plugin eval /tmp/atelier-web-eval …`. Le bac à sable des runs rend le dossier personnel illisible pour Bash : depuis `~/claude-projets/…`, les scripts de la fabrique ne se lancent pas et le cas de bout en bout échoue avec le plugin (constaté le 25/10/2026).
- Modèles épinglés pour comparer les runs entre eux : un changement de modèle n'est pas une régression du plugin.
- Un seul cas, un seul bras, pour itérer : `claude plugin eval . --case <cas> --runs 1 --ablation none --scaffold --trust-plugin`.
- Avec Claude Code 2.1.308, `--keep-temp` fait refuser les cas à fixture (« more than one hard link ») : le laisser de côté.
- Les résultats vont dans `results/`, ignoré par git.

## Δ de référence

Passage réduit du 25/10/2026 sur la version 1.1.0 (suite au commit `78cd4c0`) : un run par cas et par bras, Claude Code 2.1.308, Sonnet 5.5 sous test, Haiku 5.5 en juge, compte Max. 34 runs, 281 s, 3,82 $ en prix catalogue. Un run par bras donne un ordre de grandeur, pas une mesure stable : à refaire à trois runs avant d'en tirer une décision.

| Cas | Avec | Sans | Δ | Coût |
|---|---|---|---|---|
| `initialiser-atelier` | 1,00 | 0,00 | +1,00 | 0,15 $ |
| `landing-sans-doctrine` | 1,00 | 0,00 | +1,00 | 0,22 $ |
| `orienter-page-tarifs` | 1,00 | 1,00 | 0,00 | 0,20 $ |
| `landing-cadrage` | 0,00 | 1,00 | −1,00 | 0,63 $ |
| `page-web-section` | 1,00 | 1,00 | 0,00 | 0,25 $ |
| `motion-trop-statique` | 1,00 | 0,67 | +0,33 | 0,21 $ |
| `lottie-integration` | 1,00 | 1,00 | 0,00 | 0,25 $ |
| `brand-check-brouillon` | 0,67 | 0,67 | 0,00 | 0,20 $ |
| `cro-formulaire` | 1,00 | 1,00 | 0,00 | 0,14 $ |
| `directions-hero` | 1,00 | 1,00 | 0,00 | 0,39 $ |
| `lead-magnet-calculateur` | 0,00 | 0,00 | 0,00 | 0,24 $ |
| `script-python` | 0,50 | 0,50 | 0,00 | 0,14 $ |
| `css-sticky` | 1,00 | 1,00 | 0,00 | 0,11 $ |
| `plan-slides` | 1,00 | 1,00 | 0,00 | 0,12 $ |
| `email-relance` | 1,00 | 1,00 | 0,00 | 0,11 $ |
| `post-linkedin` | 1,00 | 1,00 | 0,00 | 0,12 $ |
| `landing-matinale`, depuis `~/claude-projets` | 0,00 | 0,14 | −0,14 | 0,36 $ |
| `landing-matinale`, depuis une copie hors du dossier personnel | 1,00 | 0,00 | +1,00 | 0,52 $ |

Δ moyen du passage : +0,07 ; ≈ +0,14 en retenant le cas de bout en bout lancé hors du dossier personnel.

**Ce que l'atelier apporte, mesuré** : la doctrine d'abord (sans le plugin, Claude écrit toute la landing du webinar dans `index.html` avec ses propres tons verts, et, pour poser une charte, ne demande ni contenus récents de la marque ni chiffres sourcés et propose de choisir à la place de l'humain ; avec le plugin, il demande la matière réelle et ne produit rien avant), la fabrique (page assemblée, empreinte de l'assembleur, marqueurs branchés, linter lancé, rien de publié), le mouvement en CSS piloté par le défilement. Les cinq quasi-cas passent : aucune skill de l'atelier ne s'est déclenchée hors de son périmètre.

**Δ nul à 1,00** (`orienter-page-tarifs`, `page-web-section`, `lottie-integration`, `cro-formulaire`, `directions-hero`) : Claude seul fait aussi bien sur ces critères. Dans un projet doté d'une doctrine, il explore l'espace de travail et lit `atelier/marque/` de lui-même, si bien qu'un critère « s'appuie sur la doctrine » ne départage pas les bras. Deux indicateurs de déclenchement sont restés à zéro avec le plugin : aucune des skills attendues ne s'est déclenchée pour `directions-hero` (`design-direction`, `design-taste`, `landing-page`) ni pour `orienter-page-tarifs` (`cro-pricing`, `cro-page`, `demarrer-projet-web`). Ces descriptions sont à revoir lors de la consolidation.

**Δ nul ou négatif dû à la suite** :
- `landing-matinale` : depuis `~/claude-projets`, les commandes Bash qui lisent la fabrique sont refusées par le bac à sable ; Claude s'arrête et demande l'autorisation, sans contourner. Depuis une copie hors du dossier personnel, le cas passe (ligne ci-dessus).
- `landing-cadrage` : `landing-page` lance `landing-researcher` en arrière-plan (phase 0) ; le réseau du bac à sable refuse les galeries, et la réponse jugée est le message envoyé après la fin de cet agent, qui résume la recherche et rappelle cinq questions de cadrage. Le juge ne voit pas la salve de questions posée plus tôt (la réponse dit « Je n'ai toujours pas vos réponses au cadrage »), et le grader de lecture de la doctrine compte zéro lecture dans la conversation principale.
- `brand-check-brouillon` : faux négatif du juge. Avec le plugin, la réponse relève les quatre défauts attendus (« solution clé en main », « écosystème », le cadratin, « 98 % » absent des chiffres autorisés) et bloque la publication ; Haiku vote FAIL deux fois sur trois.
- `lead-magnet-calculateur` : le critère exige le circuit de capture complet dès la première réponse, alors que la skill fait d'abord choisir le type d'outil et valider la logique de calcul. Les deux bras échouent.
- `script-python` : la regex `\.lower\(\)` ne trouve rien dans aucun des deux bras ; sans trace conservée, impossible de dire si le grader est trop étroit.

**À corriger avant le prochain passage** : lancer depuis une copie hors du dossier personnel ; juge Sonnet (`--judge-model claude-sonnet-5-5`) pour les graders `llm` ; pour `landing-cadrage`, juger la trace (`focus: trace`) ou couper l'agent de recherche (`--disallow-tools Agent`) ; réécrire le critère de `lead-magnet-calculateur` pour une première réponse qui fait choisir le type ; vérifier `script-python` sur une trace ; trois runs par cas.
