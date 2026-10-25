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
- Modèles épinglés pour comparer les runs entre eux : un changement de modèle n'est pas une régression du plugin.
- Un seul cas, un seul bras, pour itérer : `claude plugin eval . --case <cas> --runs 1 --ablation none --scaffold --trust-plugin`.
- Avec Claude Code 2.1.308, `--keep-temp` fait refuser les cas à fixture (« more than one hard link ») : le laisser de côté.
- Les résultats vont dans `results/`, ignoré par git.

## Δ de référence

Premier passage, sur la version 1.1.0 : à relever ici après le run (score avec, score sans, `Δ` par cas, coût, modèle).
