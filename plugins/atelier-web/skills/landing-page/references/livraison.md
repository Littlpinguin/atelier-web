# Livraison : budget, publication, checklist

Détail de la phase 8. Les contrôles bloquants sont en tête du `SKILL.md` ; ce fichier donne le reste.

## Budget de la page

- HTML, CSS et JS en ligne sous 200 Ko.
- Images en WebP dimensionnées à l'usage, `loading="lazy"` hors hero.
- Polices en `font-display: swap`.
- Aucun script bloquant ; cible LCP < 2,5 s.

## Enregistrement et publication

1. **Enregistrement** : UTM et métrique de succès dans `atelier/publie.md` (`references/mesure.md`), calendrier éditorial à jour s'il existe.
2. **Publication** : suivre le `CLAUDE.md` du projet (§ Atelier web, publication ; dry-run obligatoire), sans le dossier `pilotage/`.
3. **Contrôle en ligne** : HTTP 200, balise `robots` conforme au brief, rendu identique à la version validée.
4. **Commit, push, publication** : seulement sur go explicite de l'humain, à chaque fois.

## Checklist de livraison

- [ ] Brief validé par le responsable de la marque ; spec validée, textes définitifs clé par clé
- [ ] Direction choisie par l'humain, objet signature nommé, aucune signature reprise d'une autre page
- [ ] Charte de page à jour (§ 9 : toutes les décisions de l'humain)
- [ ] Un seul objectif, `data-cta="primaire"` posé, CTA primaire visible sans défiler sur mobile
- [ ] `qa-landing.py` : zéro erreur ; avertissements restants listés et assumés
- [ ] Quatre revues rendues, vague de corrections arbitrée et appliquée
- [ ] `a11y-auditor` sans bloquant ni majeur ; `lint-brand.py` et `brand-check` au vert
- [ ] UTM et événements en place ; `atelier/publie.md`, calendrier et inventaire à jour
- [ ] Publication par dry-run, sans `pilotage/` ; contrôle en ligne fait
