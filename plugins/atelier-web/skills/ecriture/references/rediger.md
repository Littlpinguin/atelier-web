# Rédiger : les textes web de la marque

## Sommaire

- Étape 0 — Doctrine de marque (OBLIGATOIRE)
- Préflight obligatoire
- Référence rapide du design system
- Catalogue des templates de sections
- Principes d'écriture
- Bilinguisme (le cas échéant)
- Personnalisations spécifiques à la marque
- Règles état de l'art (2026)
- Checklist avant livraison
- Skills associées

Tu rédiges les landing pages, pages produit et contenus web longs en t'appuyant sur le design system et la voix de marque.

## Étape 0 — Doctrine de marque (OBLIGATOIRE)

Avant d'écrire la moindre ligne de copy :

1. Charger `atelier/marque/checklist-pre-composition.md` — règles de voix, anti-style-IA, typographie, assets, réutilisation.
2. Charger `atelier/marque/voice.md` — position de voix, vocabulaire, interdits.

**Ne jamais produire sans.** Si l'un des deux fichiers manque ou contient encore des `{{...}}`, arrêter et lancer la skill `demarrer-projet-web` (atelier-web), qui pose la doctrine du projet. Les interdits anti-style-IA (parallélismes négatifs, vocabulaire IA mort, tiret cadratin) s'appliquent à chaque headline, sous-titre et CTA.

## Préflight obligatoire

1. Lire `atelier/marque/voice.md` — ton, vocabulaire, interdits.
2. Lire `atelier/marque/style-guide.md` — système visuel, tokens.
3. Lire le `CLAUDE.md` du projet (§ Atelier web) — structure et conventions techniques.
4. Parcourir les pages existantes dans `atelier/` pour calibrer le ton.
5. **Récupérer la matière source :**
   - Lire `atelier/marque/messaging-framework.md` — positionnement, formulations canoniques, chiffres clés.
   - Scanner `atelier/` et les pages du site pour les pages similaires : structures qui ont fonctionné, sections réutilisables.
   - Piocher dans les contenus déjà publiés par la marque (site, newsletters, posts) les formulations validées et les accroches qui résonnent.
   - Chaque chiffre utilisé doit venir de `atelier/marque/messaging-framework.md`, des rapports chiffrés du projet ou d'une référence externe citée.

## Référence rapide du design system

Les valeurs ne se recopient jamais ici : elles se lisent dans la doctrine du projet.

| Élément | Où le lire |
|---|---|
| Police principale, couleurs, dégradé, rayons | `atelier/marque/tokens.json` |
| Style d'illustration, interdits visuels | `atelier/marque/style-guide.md` |
| Composants et sections du site existant | `atelier/marque/design.md`, s'il existe |

## Catalogue des templates de sections

Chaque landing page s'assemble à partir de sections modulaires :

| Section | Usage |
|---|---|
| Hero | Headline principale + sous-titre + CTA principal |
| Énoncé du problème | Points de douleur du persona |
| Solutions / Fonctionnalités | Proposition de valeur en 3-4 blocs |
| Preuve sociale | Logos clients, chiffres, témoignages |
| Timeline / Processus | Étapes du processus |
| Tableau comparatif | vs alternatives |
| Vitrine de chiffres | Gros chiffres |
| Témoignages | Citations avec portrait |
| FAQ accordéon | Questions fréquentes |
| Étude de cas | Résultats concrets |
| Pour qui | Blocs par persona |
| CTA final | Bloc de conversion avec dégradé |

**Séquence par défaut** : Hero → Problème → Solutions → Preuve sociale → Chiffres → Témoignages → FAQ → CTA final.

## Principes d'écriture

### La clarté avant la créativité

S'il faut choisir entre clair et malin, choisir clair. Chaque page répond à UNE question.

### La donnée en héros

Les chiffres sont l'élément visuel principal. Un gros chiffre vaut mieux qu'un paragraphe.

### Le bénéfice avant la fonctionnalité

« Trouvez le bon expert en 48 heures » > « Accès à notre réseau de 100+ experts »

### La précision avant le vague

« 8,8/10 de satisfaction (n=136) » > « Grande satisfaction »

### Scannable

- Un H2 par section
- 2-3 phrases max par paragraphe
- Blancs généreux
- Un CTA max par section
- Mobile-first (tester à 375px de large)

## Bilinguisme (le cas échéant)

Règles propres à la marque : `atelier/marque/voice.md`, § règles spécifiques, s'il existe.

## Personnalisations spécifiques à la marque

Règles propres à la marque : `atelier/marque/voice.md`, § règles spécifiques, s'il existe.

## Règles état de l'art (2026)

Synthèse actionnable :

1. **Structure descendante** : l'information la plus importante en premier, toujours. Aucun préambule institutionnel en ouverture (« Chez X, nous sommes fiers de… ») — la première phrase porte la promesse, la donnée ou la tension, le contexte vient après. Le contenu « entonne » vers le CTA : accroche → idée principale → preuve → CTA → secondaire.

## Checklist avant livraison

- [ ] Pages existantes relues pour calibrer le ton
- [ ] Une proposition de valeur claire par page
- [ ] La donnée en héros (chiffres visibles, pas enterrés)
- [ ] Chaque chiffre vérifié contre la doctrine de marque (`atelier/marque/messaging-framework.md`, les rapports chiffrés du projet) ou source externe citée
- [ ] Scannable (titres, paragraphes courts, blancs)
- [ ] Un CTA clair et unique par section
- [ ] Design system respecté (couleurs, polices, border-radius)
- [ ] Pas de photos stock (interdits visuels du style-guide)
- [ ] Vocabulaire de marque respecté
- [ ] Versions bilingues si applicable
- [ ] Rendu mobile testé

## Skills associées

- `relire.md` : relecture en 7 passes
- génération d'images : l'outil du projet s'il en a un, après accord sur le coût
- `seo` — optimisation on-page
- `brand-check` — validation finale obligatoire
