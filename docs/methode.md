# La méthode : le niveau attendu et comment y arriver

Ce document dit ce qu'on vise avec l'atelier et pourquoi les skills travaillent comme elles le font. Il se lit une fois avant le premier projet, puis sert d'arbitre quand on hésite.

## 1. La barre

**On juge sur le rendu.** Une page qui respecte le plan, passe ses tests et reste plate est un échec. Du CSS juste mais sans parti pris, des cartes blanches empilées, un titre en graisse fine sur un fond uni : refusé, même si rien n'est techniquement faux.

Ce qu'on vise, à chaque page :
- **un objet fort** autour duquel le hero se construit, et qui nomme la direction (« la page du billet », « la page de la carte ») ;
- **du réel montré plutôt que décrit** : captures du vrai produit, vraies réalisations, vrais documents, vraies personnes avec leur accord ;
- **un ou deux moments de mise en scène** au défilement, un seul par section ;
- **un moment qu'on ne voit pas ailleurs** : une méthode qui se déroule sous les yeux, un personnage de la marque, un process rejoué en animation plutôt qu'un schéma ;
- **une cohérence au pixel près** avec le reste du site : mêmes sections, mêmes marges, mêmes signatures.

## 2. La doctrine d'abord, jamais de mémoire

Avant la première ligne, la doctrine de la marque est écrite dans le projet (`atelier/marque/`) : valeurs exactes, voix, preuves autorisées, système de design du site, ce que la marque a déjà refusé. Les skills la lisent et s'arrêtent si elle manque. C'est ce qui permet de transmettre l'atelier : la méthode est commune, la marque reste chez chacun.

**Réutiliser avant de créer.** Une section qui existe sur le site se reprend telle quelle. Une variante change la mise en page, jamais le style. Une section nouvelle qui servira ailleurs entre dans la bibliothèque ou dans `design.md`.

## 3. Le fond avant le dessin

- **Partir de la matière brute** : le document de l'offre, les transcriptions de rendez-vous, les avis des clients, les pages déjà en ligne (l'accueil porte souvent les douleurs validées et les preuves chiffrées).
- **Un récit qui fait décider** : chaque section répond à une objection du visiteur, dans l'ordre où il se la pose (pourquoi maintenant, quoi, pour qui, avec qui, comment ça tient dans ma vie, combien, comment réserver).
- **Rien d'inventé.** Un chiffre, un client, un logo, un témoignage ou un compteur sans source n'existe pas. Un trou reste visible (`[À FOURNIR : …]`) et se signale.
- **Des textes nets** : aucune phrase qui n'apprend rien, aucune construction « X, pas Y », aucune formule qui annonce au lieu de dire, aucun vocabulaire de communiqué. Les règles de la marque priment.

## 4. Le déroulé d'une page ambitieuse

1. **Cadrer en une seule salve** : toutes les questions bloquantes d'un coup, chacune avec l'option recommandée et ses conséquences.
2. **Chercher l'inspiration en images** pendant le cadrage : pages qui convertissent pour le même type d'offre, galeries visuelles, composants animés. Une référence se regarde, elle ne se juge pas sur son titre.
3. **Montrer deux ou trois directions** en maquettes rapides, chacune nommée par son objet signature. En recommander une. L'humain choisit.
4. **Écrire la spec** avec les textes définitifs, section par section.
5. **Poser avant de paralléliser** : textes, charte de la page, un emplacement par section.
6. **Le hero d'abord**, montré et validé : un hero raté entraîne toute la page.
7. **Construire en parallèle**, un agent par section, chacun propriétaire de ses fichiers.
8. **Montrer tôt et souvent** : après chaque étape, l'URL locale et la liste des points à regarder, puis on continue sans attendre.
9. **Mesurer, puis quatre revues** (design, marque, conversion, accessibilité), une vague de corrections arbitrée.
10. **Livrer** après QA sans erreur et brand-check positif ; publication sur go explicite, à chaque fois.

Pour une page ou une section sur un site existant, le déroulé se resserre : lire le système du site, reprendre ses sections, construire en gros blocs, rendre, montrer, itérer. Pas de cérémonie de micro-validation : l'humain juge sur le rendu.

## 5. Les goûts par défaut

Ces règles viennent de retours réels sur des pages livrées. Elles valent tant que la doctrine du projet ne dit pas autre chose.

| Domaine | Règle |
|---|---|
| Titres | Pas de pastille de sur-titre ; ni virgule ni point dans un titre (on reformule) ; aucun mot seul en fin de ligne |
| Hero | Un titre, une accroche sur deux lignes, un bouton qui mène droit à la conversion, l'objet visuel ; ni étiquette au-dessus du titre, ni rangée de visages |
| Fonds | Ils s'enchaînent : chaque section finit sur la couleur où commence la suivante, sans coupure nette |
| Largeurs | Alterner courante, élargie, pleine et resserrée ; la page se resserre vers la décision |
| Sections | Une section présente sur deux pages est la même section, au pixel près ; une page déclinée garde les animations de sa source |
| Captures | Entières dans l'écran, explication à côté et repères numérotés |
| Formulaires | En étapes qui tiennent chacune dans un écran de portable sans défiler |
| Transitions | Fondu inversé ; jamais de cartes qui s'empilent ; rien entre le hero et la section suivante |
| Épinglages | Une section épinglée se bloque pour de bon ; trois au plus, jamais deux d'affilée |
| Boutons | Un verbe court, sans prix ; un seul objectif par page |
| Logos tiers | Monochromes dans la couleur de la marque, sans tuile blanche |
| Illustrations | Sans fond ajouté derrière ; crédit IA dans le texte alternatif, jamais en clair |
| Urgence | Vraies places, vraie date, comptées en jours ; jamais de compte à rebours en secondes |

## 6. Le contrôle

- **Mesurer avant de regarder** : débordements, contrastes, planchers typographiques, CTA sous le pli, continuité des fonds, mouvement réduit.
- **Capturer aux tailles réelles** (portable 14 pouces, 1366 × 768, tablette, téléphone) et lire les images.
- **Connaître les pièges du rendu sans tête** avant de conclure à un bug (skill `qa-rendu`).
- **L'œil de l'humain reste la dernière porte.** Chaque retour s'applique, puis s'écrit : propre à la page dans sa charte, valable pour le site dans `design.md`, valable pour la marque dans `exemples-rejetes.md`.

## 7. Les garde-fous

- Aucune génération payante (images, vidéo, voix) sans accord sur l'outil et le montant.
- Aucun secret dans un fichier commité.
- Une action refusée à un agent ne se refait nulle part sans accord.
- Commit, push et publication seulement sur go explicite.
