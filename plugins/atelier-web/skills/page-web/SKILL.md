---
name: page-web
description: "Construit ou retouche une page ou une section d'un site existant au niveau de ses meilleures pages, en reprenant son système de design au pixel près, puis vérifie le rendu. Pour une page de plus, une section ajoutée, une déclinaison, « fais la page X comme la page Y », « reprends le style du site ». Une landing de conversion complète relève de landing-page."
---

# page-web : une page de plus, au niveau des meilleures

Sur un site qui existe, la qualité vient de la cohérence : une page neuve qui ressemble à ses voisines, au pixel près, paraît professionnelle ; une page qui invente ses propres cartes, ses propres marges et ses propres effets se voit tout de suite, même si elle est jolie seule. Cette skill sert à ajouter sans diluer.

**La barre.** Du CSS juste mais plat est un échec. Une page se montre seulement après un vrai passage de design, rendue et capturée, au moins au niveau des pages de référence du site.

## Étape 0 : doctrine et système du site

1. Lire le bloc « Atelier web » du `CLAUDE.md` du projet, puis `atelier/marque/design.md` (ou le document de design que ce bloc désigne). Absent : lancer `demarrer-projet-web`.
2. Lire `atelier/marque/voice.md`, `checklist-pre-composition.md`, `design-anti-generique.md` et `exemples-rejetes.md`.
3. **Ouvrir une page de référence** (celle que le `CLAUDE.md` désigne, sinon l'accueil et la page la plus soignée) et relever ce qu'on va reprendre : sections, classes, feuilles de style, comportements JS.
4. **Ancrer le texte dans le site en ligne** : les douleurs, preuves chiffrées et témoignages déjà publiés (l'accueil en porte souvent le plus) priment sur une spec plus ancienne.

## Étape 1 : choisir chaque section, dans cet ordre

1. **Réutiliser** une section du site telle quelle, en chargeant sa feuille d'origine plutôt qu'en redéfinissant ses règles.
2. Sinon lui ajouter une **variante de mise en page** (une classe ou un attribut), jamais une variante de style.
3. Sinon créer une **section partagée** nouvelle, inscrite dans `design.md`, validée par l'humain avant d'être posée ailleurs.
4. Seulement s'il n'existe aucun équivalent : une section propre à la page, qui respecte les jetons, les signatures et le mouvement du site.

**Une section reprise est identique.** Recopier son balisage section par section depuis la page source, avec ses comportements JS (filtres, sommaire, accordéon), sans surcharger son CSS. Avant de livrer, comparer le squelette (balises et classes) des sections reprises avec la source : zéro écart attendu, hors contenu. Un détail retiré ou ajouté sur une section « reprise » se voit.

**Une page déclinée garde les comportements de sa source.** Seuls les textes, les visuels et le contenu changent. Toute amélioration de comportement faite sur la source se reporte le jour même sur ses déclinaisons, puis se vérifie sur chacune ; tant que les moteurs sont des copies, comparer avec `diff` avant chaque report.

## Étape 2 : composer la page

### Fonds qui s'enchaînent
Chaque section finit sur la couleur où commence la suivante, souvent par un dégradé : aucune coupure nette entre deux sections. Une section posée hors de son ordre d'origine casse la chaîne, et une ombre longue rognée en bas de section crée aussi une coupure. Contrôle mesuré : `controle-fonds.py` (`${CLAUDE_PLUGIN_ROOT}/skills/revue/references/rendu.md`), à 1440 puis 390 px, « Aucune coupure » attendu.

### Rythme des largeurs
Sur une page longue, treize sections à la même largeur donnent un rythme monotone. Alterner quatre largeurs, sans en mettre deux identiques d'affilée quand c'est possible :
- **courante** : le conteneur du site ;
- **élargie** : à mi-chemin du bord de l'écran, 1 560 px au plus ;
- **pleine** : bord à bord, gouttière `clamp(1rem, 2.5vw, 2.5rem)` ;
- **resserrée** : environ 1 120 px, puis plus étroite encore pour l'offre et l'appel final, la page se resserre vers la décision.

Pleine ou élargie pour ce qui se regarde (réalisations, comparateur, schéma, captures), resserrée pour ce qui se lit (compétences, pour qui, FAQ). Dans une section élargie ou pleine, le titre part du bord gauche du bloc qui déborde ; il se centre dans les sections resserrées ; sous 900 px, tous les titres reviennent au bord de la grille. Souffles verticaux variés en `clamp()` : amples autour des grands visuels, serrés autour de ce qui se lit.

Aucune largeur fixe : `min()`, `calc()`, `margin-inline: calc(50% - var(--l) / 2)`. Jamais `100vw` sans gouttière (la barre de défilement de Windows crée un débordement) ; `html { overflow-x: clip }`. Vérifier de 390 à 2 560 px qu'aucune largeur ne déborde.

### Captures de produit
Une capture d'interface se montre entière dans la fenêtre, avec son explication à côté, jamais dessous : à gauche les vues (une dépliée à la fois, légende numérotée), à droite la capture, réglée sur la hauteur de l'écran (par exemple `max-width: calc((100svh - 15rem) * 1.6)`), avec des repères numérotés posés en pourcentage aux mêmes numéros que la légende ; le survol d'une ligne allume son repère. Vérifier que titre, sélecteur, capture et légende tiennent ensemble à 1512 × 842, 1440 × 900, 1280 × 800 et 390 × 844.

### Formulaires et pop-ups en étapes
Un formulaire d'inscription ou de réservation se découpe en étapes courtes qui tiennent chacune dans l'écran d'un portable (1366 × 768) sans défilement : barre d'étapes en haut, cases de choix en grille 2 × 2 de même hauteur (une colonne sous 340 px), bouton Retour à partir de l'étape 2 ; en mobile, la colonne d'accompagnement ne garde que son titre. Mesurer chaque étape (`scrollHeight` du panneau, bas du bouton) en 1366 × 768 et en 375 px avant de livrer. Le même modèle sert à toutes les pop-ups du site.

### Barre du haut d'une page sans menu
Une landing sans navigation reprend la barre partagée du site, jamais une barre recréée : logo fixe ; au défilement, fond flouté, nom de la page à gauche, bouton à droite dès que celui du hero sort de l'écran ; bouton et pastille mobile qui se retirent devant l'offre ou le formulaire final. Si le site n'en a pas encore, la créer une fois comme composant partagé.

### Matières et détails
- **Rayons concentriques** : à valeur égale, deux formes emboîtées ne paraissent pas égales. Le rayon du contenant vaut celui du contenu plus l'écart qui les sépare.
- **Logos d'outils tiers** : dans la couleur de la marque, en glyphe monochrome (Simple Icons en masque CSS), sans tuile blanche ni couleurs d'origine, sauf décision contraire de la marque. Un logo absent ne se dessine pas : le fichier officiel de la marque, avec l'accord de l'humain.
- **Images** : renommées en kebab-case, converties en WebP (qualité 80 environ), dimensionnées à l'usage, `width`, `height` et `alt` posés, `loading="lazy"` hors premier écran.
- **Titres** : règles de la doctrine du projet. Par défaut dans l'atelier : pas de pastille de sur-titre (eyebrow), ni virgule ni point dans un titre (reformuler plutôt que supprimer), aucun mot seul en fin de ligne.
- **Textes** : aucune phrase qui n'apprend rien au visiteur, aucune construction « X, pas Y », aucune formule qui annonce au lieu de dire, aucun chiffre inventé.

### Le moment qui marque
Une page conforme peut rester banale. Chercher au moins un moment qu'on ne voit pas ailleurs : une scène qui montre la méthode en mouvement, du vrai produit, un personnage ou un objet de la marque, une visualisation animée d'un process plutôt qu'un schéma. Le proposer en deux concepts si le sujet s'y prête, avec le coût de toute génération payante, validé avant dépense.

## Étape 3 : pièges techniques qui reviennent

| Piège | Parade |
|---|---|
| La feuille globale style `nav`, `header` ou `footer` comme la barre du site : un sommaire ou un en-tête de section en `<nav>` ou `<header>` part se coller en haut de page | En-tête de section en `<div>` ; un vrai `<nav>` garde la balise et neutralise `position: static; z-index: auto; padding: 0` dans sa propre règle, avec un `aria-label` |
| CSS et JS en cache long sans empreinte : la page neuve arrive, l'ancienne feuille reste, la page casse chez les visiteurs revenus | Versionner le lien (`?v=AAAAMMJJ`, une lettre en plus si plusieurs le même jour) sur **chaque** page qui charge le fichier modifié |
| Contenu en double, HTML visible et JSON-LD dans le `<head>` (FAQ, prix, offres) : un remplacement non ciblé trouve d'abord l'occurrence du `<head>` | Remplacer dans le bloc visible seulement, puis régénérer ou retoucher le JSON-LD, et recompter `<div>`, `<section>` et feuilles chargées |
| Un enfant de conteneur qui redéfinit `padding: X 0 Y` écrase la gouttière horizontale : le texte colle au bord en mobile | `padding-top` et `padding-bottom` sur les enfants d'un conteneur |
| Curseur personnalisé du site : un `cursor: pointer` le casse | Lire `design.md` ; ne jamais réintroduire un curseur que le site a remplacé |
| Une bibliothèque tierce chargée depuis un CDN que la CSP du site refuse | L'héberger dans les assets du site, version dans le nom du fichier, licence en tête |
| Une page qui dépend d'une partie générée (partials, build) servie sans build | Toujours prévisualiser la sortie du build, jamais les sources brutes |

## Étape 4 : rendre, montrer, itérer

1. Construire en gros blocs, sans cérémonie de micro-validation : l'humain juge sur le rendu.
2. Passer la revue de rendu de la skill `revue` (captures aux tailles d'écran, fonds, débordements, mouvement réduit).
3. Montrer : l'URL locale de l'aperçu, avec la liste des points à regarder. L'œil de l'humain reste la dernière porte.
4. Appliquer chaque retour, puis l'écrire : propre à la page dans la conversation, valable pour tout le site dans `design.md` ou `exemples-rejetes.md`.
5. `brand-check` avant toute livraison ; commit et publication selon les règles du projet, sur go explicite.

## Checklist avant de livrer

- [ ] Chaque section vient d'un composant du site (ou d'une section nouvelle validée et inscrite dans `design.md`)
- [ ] Sections reprises identiques à leur source (squelette comparé, comportements JS compris)
- [ ] Signatures visuelles du site présentes ; jetons seuls, aucune couleur en dur
- [ ] Fonds continus : `controle-fonds.py` à 1440 et 390 px sans coupure
- [ ] Largeurs alternées, aucune largeur fixe, aucun débordement de 390 à 2 560 px
- [ ] Captures et formulaires tiennent dans l'écran aux tailles de référence
- [ ] Liens CSS et JS versionnés sur toutes les pages concernées
- [ ] Images WebP dimensionnées, `alt`, `lazy` hors premier écran
- [ ] Titres et textes conformes à la doctrine, aucun chiffre inventé
- [ ] Revue de rendu passée (skill `revue`), page montrée, `brand-check` ✅
