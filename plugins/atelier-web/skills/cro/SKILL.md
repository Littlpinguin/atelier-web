---
name: cro
description: "Conversion des pages de la marque, sur la doctrine du projet : diagnostic d'une page qui ne convertit pas, formulaire trop long, pop-up ou bannière, page tarifs et stratégie de prix. Pour « CRO », « cette page ne convertit pas », « personne ne remplit le formulaire », « pop-up de sortie », « page tarifs », « combien facturer »."
---

# cro : une page, une action, rien d'inventé

Optimiser la conversion d'une surface de la marque : une page, un formulaire, une pop-up, une page tarifs. La méthode vient de marketingskills (Corey Haines, MIT) ; la preuve, la voix et les personas viennent de la doctrine du projet, jamais de la mémoire.

## Décider la surface

| La demande | Lire |
|---|---|
| « Cette page ne convertit pas », revue CRO d'une landing, d'une page d'accueil, d'une page fonctionnalité ou d'un article | `references/page.md` |
| Formulaire trop long, abandon, champs à garder, labels et messages d'erreur | `references/formulaire.md` |
| Pop-up, modale, intention de sortie, slide-in, bannière d'annonce | `references/popup.md` |
| Prix, paliers, freemium, hausse de prix, mensuel ou annuel, page tarifs | `references/tarifs.md` |

Une demande qui touche plusieurs surfaces (une landing et son formulaire) lit chaque référence concernée. Construire la page relève de `landing-page` ou de `page-web` ; le circuit de capture d'un lead magnet, de `lead-magnet`.

## Étape 0 : la doctrine, dès le conseil

1. Lire dans `atelier/marque/` : `messaging-framework.md` (seuls chiffres, preuves et CTA utilisables), `personas.md` (langue du client, objections), `voice.md` et `checklist-pre-composition.md` (dès qu'un mot se propose), `style-guide.md` pour toute recommandation visuelle. Puis la matière de l'offre : son document (programme, proposition, fiche produit, souvent dans `docs/`) et son brief (`atelier/briefs/`), d'où viennent les faits à afficher (dates, lieu, places, prix, conditions).
2. **La première réponse dit ce qu'elle en tire**, nommément : le persona visé et son objection, les preuves et chiffres autorisés avec leur source, les CTA de la doctrine, les règles de voix qui touchent la surface (vouvoiement, termes bannis). Citer un fichier sans en rien tirer ne compte pas. Elle liste ensuite ce qui manque pour avancer : la page ou les offres actuelles, les chiffres de conversion, la source du trafic.
3. Fichier manquant ou porteur de `{{…}}` : arrêter et lancer `demarrer-projet-web`. Sans doctrine, un diagnostic général reste possible, annoncé comme tel.

## Règles dures

- **Preuve** : aucun chiffre, témoignage, logo ni compteur inventé. Une recommandation de preuve pointe un élément réel de `messaging-framework.md`, ou signale le trou.
- **Une page, un objectif** : une action primaire, visible sans défiler et répétée aux points de décision ; chaque sortie concurrente se justifie ou part.
- **Respect du visiteur** : urgence honnête (vraies places, vraie date, comptées en jours), refus poli et jamais culpabilisant, fermeture facile, consentement explicite (RGPD), aucune case pré-cochée.
- **Prix** : la décision appartient au responsable de la marque. La skill structure et argumente, elle ne tranche pas, et ne propose aucun prix avant d'avoir les offres et les chiffres.
- Tout texte proposé passe par `brand-check` avant d'entrer dans une page.

## Format de sortie commun

1. **Quick wins** : changements faciles, effet probable immédiat.
2. **Changements à fort impact** : plus d'effort, à prioriser.
3. **Hypothèses à tester** plutôt qu'à trancher d'instinct.
4. **Alternatives de texte** : deux ou trois variantes pour le titre et le CTA, dans la voix de la doctrine, avec leur raison.

Chaque point : constat, correction, priorité. Le livrable va dans `atelier/`, à côté de la page concernée, ou en réponse directe pour un diagnostic ponctuel.

## Références

| Fichier | Contenu |
|---|---|
| `references/page.md` | Sept dimensions par ordre d'impact (proposition de valeur, titre, CTA, hiérarchie, preuve, objections, friction), spécificités par type de page, questions à poser |
| `references/formulaire.md` | Coût de chaque champ, règles champ par champ, mise en page, erreurs, bouton, confiance, mesure |
| `references/popup.md` | Déclencheurs, types, design desktop et mobile, texte, fréquence et ciblage, conformité et accessibilité, repères |
| `references/tarifs.md` | Packaging, métrique de valeur, paliers Good-Better-Best, hausse de prix, page tarifs, disposition à payer, checklist |

Provenance : `${CLAUDE_PLUGIN_ROOT}/docs/sources/vendored-cro.md`.
