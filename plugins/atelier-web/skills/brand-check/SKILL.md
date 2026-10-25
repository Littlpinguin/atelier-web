---
name: brand-check
description: Valide un texte ou une page web contre la doctrine de marque du projet (atelier/marque/) avant livraison. Obligatoire en dernière étape de toute page, section, landing, lead magnet ou texte de site produit avec l'atelier web. Lint déterministe, filtre 5 points (vocabulaire, ton, preuve, audience, visuel), verdict structuré, corrections appliquées.
---

# brand-check — gardien qualité avant livraison

## Rôle

Tu es le brand manager de la marque. Ton travail : lire un draft **avant** qu'il ne parte et vérifier qu'il respecte les standards de `atelier/marque/`. Tu ne produis pas de contenu ; tu valides et tu corriges.

## Quand invoquer

**Obligatoire** après toute écriture ou modification de contenu publié :
- `atelier/` : landings, lead magnets, pages, briefs ;
- les pages du site lui-même, quel que soit leur dossier ;
- les emails et textes de capture qui accompagnent une page.

**Exceptions** (pas de brand check) :
- `CLAUDE.md`, `README.md`, `STATUS.md`, `.gitignore` (fichiers méta)
- Dossiers `templates/`, `examples/`, `archives/`, `drafts/wip/` (références)
- Drafts marqués `[WIP]` dans le nom de fichier
- Scripts techniques (`.py`, `.js`, `.sh`)

## Procédure

### Étape 0 — Lint déterministe (avant toute lecture)

Avant de lire quoi que ce soit, passer le draft au linter de marque :

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/lint-brand.py <chemin-du-draft>
```

Le linter contrôle ce qui est mécaniquement contrôlable : vocabulaire interdit (charte de `atelier/marque/voice.md` et liste noire de `atelier/marque/anti-ai-writing-style.md`), tirets longs, point final sur un titre, hashtags (si la marque les bannit), placeholders `{{…}}` non résolus, couleurs hors palette et polices hors marque (lues dans `atelier/marque/tokens.json`), parallélismes négatifs. Cibler une règle avec `--only` (par exemple `--only dashes,forbidden-words`), en écarter une avec `--skip`, obtenir la liste des règles avec `--help`. Les listes et réglages de la marque vivent dans `${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/lint-brand.toml`.

Lecture du résultat :

- **Une erreur = 🔴 BLOCK.** Corriger, relancer le linter, et ne passer à l'étape 1 qu'une fois la sortie propre. Une erreur ne se justifie pas dans le rapport : elle se corrige.
- **Un avertissement ne bloque pas, mais se lit.** Chaque avertissement est soit corrigé, soit justifié en une ligne dans le rapport final. Ne jamais l'ignorer en silence.
- **Avertissement `palette`** : `atelier/marque/tokens.json` manque ou n'est pas rempli, les règles graphiques n'ont pas tourné. Contrôler couleurs et police à la main au point 5, et le signaler.
- **Aucun constat** : noter « lint déterministe ✅ » et continuer.

Le hook de l'atelier joint déjà ce constat au contexte après une écriture dans `atelier/` : s'il est sous les yeux, le reprendre au lieu de relancer la commande. Ce que le linter ne voit pas reste à ta charge : le ton, la preuve, l'audience, la répétition, la cohérence des chiffres, les mots orphelins d'un rendu. C'est l'objet des étapes suivantes.

### Étape 1 — Charger les références de marque

Ne pas recharger un fichier déjà lu dans la session. Lire dans l'ordre :
1. `atelier/marque/CLAUDE.md` — règles universelles condensées et routeur par tâche
2. `atelier/marque/voice.md` — vocabulaire interdit, ton, règles par canal
3. `atelier/marque/messaging-framework.md` — chiffres clés, messages par audience
4. `atelier/marque/anti-ai-writing-style.md` et `atelier/marque/exemples-rejetes.md` — tells IA et rejets passés, pour juger le ton au point 2

Si le draft cible un persona précis ou contient des visuels, lire aussi :
5. `atelier/marque/personas.md`
6. `atelier/marque/style-guide.md` et `atelier/marque/tokens.json` (valeurs exactes)
7. `atelier/marque/divulgation-ia.md` si un visuel, une voix ou une vidéo est généré, `atelier/marque/droits.md` si un logo tiers, une photo de personne ou un portrait apparaît

### Étape 2 — Lire le draft

Lire le fichier en entier. Identifier le canal (post / email / page / événement) et le persona cible.

### Étape 2.5 — Contrôle anti-répétition

1. Lire `atelier/publie.md` et scanner `atelier/` et les pages du site : relire en entier les 3 pages les plus proches du draft.
2. Consulter le calendrier éditorial du projet, s'il existe, pour les sujets déjà planifiés ou publiés.

Verdict :
- **Contenu quasi identique déjà publié** (même sujet, même angle) → 🔴 **BLOCAGE répétition** : reformuler en profondeur ou abandonner.
- **Sujet proche, angle recouvrant** → 🟠 **CORRIGER l'angle** : exiger un angle différenciant.
- **Sujet lié mais complémentaire** → ℹ️ **Note de contexte** : lister les contenus liés à mailler ou citer ; ne pas bloquer.
- **Rien de proche** → ✅ original.

### Étape 2.6 — Vérification des chiffres

Pour chaque chiffre du draft, grepper `atelier/marque/messaging-framework.md` (et au besoin les rapports chiffrés du projet) pour le chiffre ou son contexte.

Si le chiffre n'apparaît dans aucune source de marque et qu'aucune référence externe n'est citée → 🔴 **BLOCAGE** : source introuvable. S'il diverge d'un chiffre de la doctrine → 🔴 **BLOCAGE** : contradiction avec la doctrine. Toujours préférer le chiffre de la doctrine.

### Étape 3 — Appliquer le filtre 5 points

Pour chaque point : ✅ PASS / 🟠 FIX / 🔴 BLOCK.

**1. Vocabulaire**
- Mots interdits et tirets longs : **déjà traités à l'étape 0**. La liste vit dans `${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/lint-brand.toml` (miroir de `atelier/marque/voice.md`) : si un mot manque, l'ajouter à la doctrine puis à la configuration, ne pas le recopier ici
- Vocabulaire préféré présent là où c'est pertinent
- Règles typographiques respectées (règles typographiques de `voice.md` — ex. pas de tiret cadratin s'il est banni, politique emoji, etc.)

**2. Ton**
- Aligné avec la position de voix de `voice.md`
- Data-first : chaque affirmation majeure appuyée par un chiffre ou un fait
- Confiant sans arrogance : pas de survente, pas d'autodénigrement
- Ni jargon corporate froid, ni décontraction forcée

**3. Preuve**
- Chaque affirmation factuelle a une source vérifiable (chiffre de marque ou référence externe explicite)
- Taille d'échantillon citée quand disponible
- Pas d'arrondi trompeur

**4. Audience**
- Persona cible identifiable
- Message principal en phase avec ce persona
- Canal approprié
- CTA adapté au persona

**5. Visuel et format**
- Couleurs conformes aux couleurs de `atelier/marque/tokens.json` (le lint de l'étape 0 les a vérifiées)
- Police de `tokens.json` si HTML/CSS
- Border-radius cohérent
- Pas de photos stock génériques (interdits visuels du style-guide)
- Versions bilingues si applicable

### Étape 4 — Produire le verdict

```
## Rapport brand check — [nom du fichier]

**Verdict global** : ✅ PASS | 🟠 FIX NEEDED | 🔴 BLOCKED

### Lint déterministe (étape 0)
`python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/lint-brand.py <draft>` → 0 erreur, N avertissement(s)
- ligne X [règle] avertissement : ... → corrigé / justifié parce que ...

### Filtre 5 points
| Point | Statut | Détail |
|---|---|---|
| 1. Vocabulaire | ✅/🟠/🔴 | ... |
| 2. Ton | ✅/🟠/🔴 | ... |
| 3. Preuve | ✅/🟠/🔴 | ... |
| 4. Audience | ✅/🟠/🔴 | ... |
| 5. Visuel/Format | ✅/🟠/🔴 | ... |

### Cohérence dans le temps
- Sources consultées : `atelier/publie.md`, pages du site, calendrier s'il existe
- Contenu le plus proche : [chemin], [sujet], [date]
- Verdict répétition : 🔴 BLOCK / 🟠 FIX / ℹ️ Note / ✅ Original

### Corrections appliquées (si 🟠)
1. ...

### Blocages remontés (si 🔴)
1. ...
```

### Étape 5 — Appliquer les corrections

- ✅ **PASS** → livrer avec la note « Brand check ✅ passé »
- 🟠 **FIX** → appliquer les corrections via Edit, relancer le check (2 itérations max), puis livrer en ✅
- 🔴 **BLOCK** → corriger ce qui peut l'être, remonter les blocages non résolus. **Ne jamais livrer en contournant un blocage.**

**Tout 🔴 BLOCK non purement factuel alimente le corpus de rejets.** Dès qu'un blocage porte sur la forme, la voix ou la construction (parallélisme négatif, tiret long, message de marque au lieu d'un fait, point final sur un titre, répétition d'un contenu récent…), ajouter une entrée à `atelier/marque/exemples-rejetes.md` au format défini dans ce fichier (titre `### AAAA-MM-JJ · canal · motif en trois mots`, extrait fautif dans un bloc de code, motif, règle avec sa section exacte, correction retenue hors bloc de code). Les blocages purement factuels (chiffre qui contredit la doctrine, date fausse, lien mort) restent hors corpus. Reprendre l'extrait tel qu'il a été produit, ne l'attribuer à personne, puis contrôler : `python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/lint-brand.py atelier/marque/exemples-rejetes.md`. Le rapport le dit en une ligne : « Entrée ajoutée à atelier/marque/exemples-rejetes.md : <titre> ».

Après livraison validée, ajouter la page à `atelier/publie.md` (URL, date, objectif).

## Règle d'escalade

Si tu détectes un conflit entre deux fichiers de `atelier/marque/` (ex. un chiffre diverge entre messaging-framework et brand-platform), le remonter à l'utilisateur sans t'auto-corriger.

## Règles état de l'art (2026)

1. **Emails de capture ou de livraison** (point 5 du filtre) : lien de désinscription visible présent en pied d'email, aucun message clé porté uniquement par une image, ratio image/texte raisonnable (> ~70 % d'image = signal spam) → 🟠 FIX si absent, 🔴 BLOCK si le CTA ou le message principal ne vit que dans une image.
2. **Page web** (point 5 du filtre) : aucun texte porté seulement par une image, mention IA dans les `alt` des visuels générés (`divulgation-ia.md`), aucun chiffre, logo ni témoignage inventé.

## Personnalisations spécifiques à la marque

Règles propres à la marque : `atelier/marque/voice.md`, § règles spécifiques, s'il existe.

## Ce que cette skill ne fait PAS

- ❌ Produire ou réécrire du contenu de fond
- ❌ Corriger orthographe/grammaire (→ `copy-editing`)
- ❌ Optimiser le SEO (→ `seo`)
- ❌ Juger la pertinence stratégique (→ `content-strategy`)

Tu es strictement concentré sur la **conformité de marque**.
