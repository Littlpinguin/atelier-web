# Tarifs : stratégie de prix et page tarifs

Adapté du plugin marketingskills (Corey Haines / fork Littlpinguin, MIT) — voir `${CLAUDE_PLUGIN_ROOT}/docs/sources/vendored-cro.md`. Deux registres : **conseil stratégique** (packaging, prix) et **production** (copy de la page tarifs). La décision de prix appartient toujours à le responsable de la marque — cette skill structure et argumente, elle ne tranche pas.

## Étape 0 — Doctrine de marque (OBLIGATOIRE dès qu'elle existe, conseil compris)

Avant le premier conseil comme avant toute copy :

1. `atelier/marque/messaging-framework.md` — les preuves de valeur qui justifient le prix (chiffres sourcés uniquement).
2. `atelier/marque/personas.md` — chaque palier doit correspondre à un persona identifiable.
3. `atelier/marque/checklist-pre-composition.md` et `atelier/marque/voice.md` — voix, vocabulaire, interdits (obligatoires dès qu'un texte se rédige).

**La première réponse dit ce qu'elle tire de la doctrine**, nommément : le ou les personas visés et leur objection sur le prix, les preuves de valeur et chiffres autorisés (avec leur source), les règles de voix qui touchent la page (vouvoiement, termes bannis). Citer un fichier sans en rien tirer ne compte pas. Puis elle liste ce qui manque pour avancer : la page tarifs actuelle, les offres et leurs prix, les chiffres de performance. Aucun prix n'est proposé avant.

Si un fichier manque ou contient des `{{...}}` : arrêter et lancer la skill `demarrer-projet-web` (atelier-web), qui pose la doctrine du projet. Sans doctrine, seul un conseil stratégique général reste possible, annoncé comme tel ; toute sortie rédigée passe par l'étape 0 puis `brand-check`.

## Cadrage initial

1. **Business** : type de produit/service, pricing actuel, marché cible (TPE/PME, mid-market, enterprise), motion (self-serve, sales-led, hybride)
2. **Valeur et concurrence** : valeur principale délivrée, alternatives considérées par les clients, prix concurrents
3. **Performance** : conversion actuelle, panier moyen/ARPU, churn, retours clients sur le prix
4. **Objectif** : croissance, revenu ou marge ? montée ou descente en gamme ?

## Les trois axes du pricing

1. **Packaging** — ce que contient chaque palier (fonctionnalités, limites, niveau de support)
2. **Métrique de valeur** — ce qu'on facture (par utilisateur, à l'usage, forfait…) : « quand le client consomme plus de [métrique], reçoit-il plus de valeur ? » Si oui, bonne métrique. Elle doit être compréhensible, croître avec le client, difficile à contourner
3. **Niveau de prix** — le montant : **fondé sur la valeur perçue, pas sur le coût**. Plancher = meilleure alternative du client ; plafond = valeur perçue ; se placer entre les deux

## Structure de paliers — Good-Better-Best

| Palier | Rôle | Repères |
|---|---|---|
| Entrée | acquisition, réassurance | cœur fonctionnel, limites basses |
| **Recommandé** | ancre — là où on veut la majorité | complet, limites raisonnables |
| Premium | capture de valeur haute | tout + avancé, 2-3x le prix du recommandé |

Différencier par : fonctionnalités (basique vs avancé), limites d'usage, niveau de support, accès (API, SSO, marque blanche). Chaque palier doit se décrire en une phrase « Pour [persona] qui [besoin] ».

## Quand augmenter les prix

Signaux : concurrents plus chers, prospects qui ne tiquent pas, « c'est donné ! », conversion très élevée (> 40%), churn très bas, valeur produit nettement accrue depuis le dernier pricing.

Stratégies : grandfathering (nouveau prix pour les nouveaux seulement) ; annonce 3-6 mois à l'avance ; hausse liée à de la valeur ajoutée ; restructuration des plans.

## Page tarifs — bonnes pratiques

- Au-dessus de la ligne de flottaison : comparaison claire des paliers, palier recommandé signalé, toggle mensuel/annuel, un CTA par palier
- Éléments : tableau comparatif des fonctionnalités, « pour qui » par palier, FAQ (objections prix), remise annuelle explicite (17-20% typique), garantie, preuves (logos, témoignages — sourcés doctrine)
- **Psychologie** (à utiliser honnêtement, jamais contre l'utilisateur) : ancrage (option chère visible d'abord), effet de compromis (palier du milieu = meilleure valeur), prix charme 49 € (positionnement valeur) vs prix rond 50 € (positionnement premium)
- La revue de conversion de la page elle-même : `page.md`

## Recherche de disposition à payer

- **Van Westendorp** (4 questions : trop cher / trop bon marché pour être fiable / cher mais envisageable / bonne affaire) → zone de prix acceptable
- **MaxDiff** (arbitrages entre fonctionnalités) → informe le packaging des paliers
- À défaut d'étude : entretiens clients (skill `customer-research` du plugin source, non vendorée — ou entretiens directs) + grille concurrentielle

## Format de sortie

- **Conseil** : note structurée dans `atelier/strategie/` — diagnostic, options de packaging/métrique/prix argumentées, risques, plan de migration si hausse
- **Production** : copy de la page tarifs dans `atelier/` (structure, descriptions de paliers, FAQ, CTA), conforme doctrine, validée par `brand-check`

## Checklist avant de figer un pricing

- [ ] Personas cibles définis (`atelier/marque/personas.md`) et un palier par persona
- [ ] Prix concurrents documentés (notes de veille du projet, sources citées)
- [ ] Métrique de valeur identifiée et testée à la phrase « plus de X = plus de valeur »
- [ ] Recherche de disposition à payer menée (même minimale)
- [ ] Stratégie de remise annuelle et palier enterprise/custom prévus

## Skills associées

- `page.md` : conversion de la page tarifs
- skill `ecriture` : rédaction de la page
- `landing-page` — production HTML
- `brand-check` — validation obligatoire
