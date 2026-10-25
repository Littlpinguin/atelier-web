---
name: lead-magnet
description: "Crée un lead magnet aux couleurs de la marque du projet (guide PDF, calculateur, diagnostic, quiz, checklist) avec son circuit de capture complet : page, formulaire, consentement, automatisation, emailing, séquence. Pour un aimant à leads, un livre blanc, un outil ou un modèle à offrir contre un email."
---

# lead-magnet — lead magnets la marque

Vous produisez des lead magnets qui génèrent des leads qualifiés, pas des fichiers.

**Principe fondateur : un lead magnet sans capture d'email est un PDF perdu.** Aucun lead magnet n'est livré sans son circuit complet : contenu → page de capture → formulaire → automatisation → séquence de nurturing → mesure. Si l'utilisateur demande « juste le PDF », produire le PDF mais signaler explicitement que le circuit n'est pas en place et proposer de le construire.

## Étape 0 — Doctrine de marque (OBLIGATOIRE)

1. Charger `atelier/marque/checklist-pre-composition.md` — règles de voix, anti-style-IA, typographie, assets, réutilisation.
2. Charger `atelier/marque/voice.md` et `atelier/marque/personas.md` — le choix du type de lead magnet dépend du persona.
3. Charger `atelier/marque/style-guide.md` — tout livrable (PDF comme outil web) est charté.
4. Charger `atelier/marque/design-anti-generique.md` — un outil interactif visuellement générique décrédibilise la capture ; mêmes exigences qu'une landing page.
5. Lire le `CLAUDE.md` du projet (§ Atelier web) — structure du dossier, conventions, règle de réutilisation.

**Ne jamais produire sans.** Si un fichier manque ou contient des `{{...}}`, arrêter et lancer la skill `demarrer-projet-web` (atelier-web), qui pose la doctrine du projet.

## Typologie et critères de choix

| Type | Format & production | Bon pour | Effort | Qualification du lead |
|---|---|---|---|---|
| **Guide PDF / livre blanc** | Skill `pdf` ou `docx` chartée si disponible ; sinon HTML charté (tokens atelier/marque) exporté en PDF via impression navigateur | Audience haut de funnel, expertise à démontrer, sujet dense | Moyen-élevé | Faible (email seul) |
| **Outil interactif** (calculateur, simulateur, diagnostic) | HTML/JS vanilla single-file dans `outils-web/<slug>/` (méthode ci-dessous) | Audience qui veut un résultat personnalisé (ROI, score, estimation) ; forte valeur perçue, partage naturel | Élevé | Forte (les réponses qualifient) |
| **Quiz / auto-diagnostic** | Variante de l'outil interactif : questions → scoring → profil de résultat | Qualification + segmentation : chaque profil de résultat route vers une séquence de nurturing différente | Moyen | Très forte |
| **Template / checklist** | Page HTML chartée, PDF une page, ou fichier téléchargeable | Quick win immédiat, audience opérationnelle, production rapide | Faible | Faible |

**Critères de choix** (dans cet ordre) :

1. **Persona et niveau de conscience** (`atelier/marque/personas.md`) : découvre le problème → guide/checklist ; compare les solutions → calculateur/diagnostic ; prêt à agir → template + démo.
2. **Promesse en une phrase** : si la valeur ne se formule pas en une phrase (« Estimez X en 2 minutes », « Les 12 points à vérifier avant Y »), le lead magnet est mal choisi.
3. **Potentiel de qualification** : un quiz segmente, un PDF non. Si le nurturing doit être différencié, préférer l'interactif.
4. **Effort vs durée de vie** : un outil interactif coûte cher mais capte des leads pendant des années ; une checklist se produit en une session.

Présenter 2-3 options argumentées à l'utilisateur avant de produire ; le responsable de la marque tranche.

**Dès cette première réponse, le circuit de capture est sur la table**, pour l'option recommandée, en quatre points courts :

1. **Où part l'email** : l'outil d'emailing et l'automatisation déclarés dans le `CLAUDE.md` du projet ; s'il n'en déclare aucun, le demander.
2. **Ce que reçoit le visiteur** après avoir donné son email (résultat détaillé, guide, séquence) et le message de confirmation.
3. **Consentement** : mention RGPD sous le formulaire (finalité, désinscription en un clic, lien vers la politique de confidentialité), case d'opt-in marketing distincte et jamais pré-cochée si la séquence dépasse la livraison du contenu.
4. **Chiffres** : un résultat chiffré (calcul, score, économie) ne repose que sur un chiffre de `atelier/marque/messaging-framework.md` ou sur une hypothèse annoncée comme telle ; jamais de coefficient inventé.

## Workflow commun

### 1. Brief

`atelier/briefs/<slug>.md` : promesse, persona visé, type retenu, sujet ancré dans `atelier/marque/messaging-framework.md`, séquence de nurturing prévue (existante ou à créer), métrique de succès (téléchargements/mois, taux de conversion page → lead).

### 2. Production du contenu (par type)

**Guide PDF / livre blanc** — `atelier/lead-magnets/guides-pdf/<slug>/`
1. Plan validé par l'utilisateur (5-15 pages ; un guide utile et court bat un pavé).
2. Rédaction via la skill `ecriture`, mode rédiger (étape 0 doctrine incluse) ; chiffres vérifiés contre le messaging framework ou les rapports chiffrés du projet.
3. Mise en forme chartée : skill `pdf` ou `docx` si disponible dans l'environnement ; sinon document HTML aux tokens atelier/marque (custom properties, voir `${CLAUDE_PLUGIN_ROOT}/fabrique/sections-library.md`) avec CSS print, exporté en PDF via impression navigateur.
4. Couverture : assets de `atelier/marque/assets/` d'abord, sinon l'outil d'images du projet (après accord sur le coût).
5. Dernière page : CTA vers l'étape suivante (démo, contact, autre contenu) — un PDF sans CTA est une impasse.

**Outil interactif / quiz** — `atelier/lead-magnets/outils-web/<slug>/`
1. Spécifier la logique (entrées, calcul ou scoring, restitution) et la faire valider AVANT de coder.
2. Build : `index.html` autonome, HTML/JS vanilla, tokens atelier/marque, mobile-first, conventions techniques de le `CLAUDE.md` du projet (§ Atelier web). Design via la skill `design` (routes créer et systématiser) avec les tokens injectés (la marque prime) ; fallback : sections-library + style-guide seuls.
3. **Capture intégrée à l'outil** : le résultat détaillé (score complet, rapport, recommandations) est délivré contre l'email — l'utilisateur voit un aperçu du résultat, l'email débloque le reste. Jamais de formulaire avant toute valeur : donner d'abord, capturer ensuite.
4. Pour un quiz : chaque profil de résultat porte un identifiant transmis à l'automatisation (segmentation du nurturing).

**Template / checklist**
1. Contenu via la skill `ecriture`, format le plus actionnable (checklist cochable, tableau à remplir).
2. Livrable charté : page HTML dans `outils-web/` ou PDF une page dans `guides-pdf/`.

### 3. Page de capture

Invoquer la skill **`landing-page`** (brief allégé : hero avec promesse du lead magnet, aperçu/mockup, 3 bénéfices, preuve, formulaire). La page vit dans `atelier/landings/<slug>/`.

### 4. Formulaire

Chemin nominal : skill interne **`cro`** (`formulaire.md`). Fallback inline :

- Le minimum de champs : **email seul** par défaut ; prénom uniquement si le nurturing le personnalise ; toute question de qualification doit payer son coût en friction.
- Label explicite, bouton formulé en bénéfice (« Recevoir le guide », jamais « Envoyer »).
- Mention RGPD sous le formulaire : finalité, désinscription en un clic, lien politique de confidentialité. Case d'opt-in marketing distincte si la séquence dépasse la livraison du contenu (politique d'opt-in du projet).
- Message de confirmation qui annonce la suite (« Le guide arrive par email dans 2 minutes »).

### 5. Automatisation — circuit de capture

**Le circuit complet, sans exception :**

```
Lead magnet → formulaire → automatisation (n8n, Make…) → outil emailing → séquence de nurturing
```

- **Si le projet a un outil d'automatisation** (déclaré dans le `CLAUDE.md` du projet) : concevoir le workflow (méthode conseil → plan → validation → exécution → retour d'expérience). Pattern : webhook du formulaire → validation/normalisation de l'email → ajout au groupe/segment dans **l'outil d'emailing du projet** (tag = slug du lead magnet, + profil de résultat pour un quiz) → déclenchement de la séquence → envoi du livrable. Export du workflow sans identifiants.
- **Sinon** : brancher le formulaire directement sur le formulaire natif ou l'API de l'outil d'emailing du projet (tag identique), et signaler qu'une automatisation apporterait la validation, la segmentation fine et le suivi d'erreurs.
- Jamais de credentials dans le HTML ni dans les exports : `.env` ou coffre de l'outil d'automatisation uniquement.

### 6. Séquence de nurturing

Écrire la séquence avec la skill d'emailing installée (par exemple `email-sequence`), sinon directement avec la skill `ecriture`. Minimum vital :

1. **Email 0 (immédiat)** : livraison du lead magnet + rappel de la promesse.
2. **Emails 1-3 (J+2 à J+14)** : approfondissement du sujet, preuve, puis passage vers l'offre.

Pour un quiz : une branche par profil de résultat. La séquence est validée par brand-check comme tout contenu publié.

### 7. Brand-check (obligatoire)

`brand-check` sur chaque livrable : le lead magnet lui-même, la page de capture, les emails de la séquence.

### 8. Mesure — versée dans le reporting

Suivre, et noter dans `atelier/publie.md` :

- **Téléchargements / complétions** (événement GA4 `generate_lead` de la page de capture — conventions de la skill `landing-page`)
- **Taux de conversion** visiteur → lead de la page de capture (cible indicative : 20-40 % sur trafic qualifié)
- **Qualité** : taux d'ouverture de la séquence, leads devenus opportunités (le CRM du projet si configuré)

Mettre à jour `atelier/publie.md` (et le calendrier éditorial du projet s'il existe).

## Checklist pré-livraison

- [ ] Type choisi et argumenté selon persona + niveau de conscience, validé par le responsable de la marque
- [ ] Contenu produit via `ecriture`, chiffres vérifiés, livrable charté (tokens atelier/marque)
- [ ] CTA de sortie présent dans le lead magnet lui-même
- [ ] Page de capture livrée via la skill `landing-page` (UTM + événement de conversion inclus)
- [ ] Formulaire minimal (`cro`, `formulaire.md`, ou règles inline), mention RGPD + opt-in
- [ ] Circuit complet branché : formulaire → n8n (ou direct) → l'outil d'emailing du projet → séquence
- [ ] Séquence de nurturing en place (skill d'emailing installée, ou `ecriture`), email 0 livre le contenu
- [ ] `brand-check` passé sur les trois livrables (contenu, page, emails)
- [ ] Mesure configurée et `atelier/publie.md` + calendrier à jour

## Skills associées

- `landing-page` — page de capture (structure CRO, design, tracking)
- `ecriture` : contenu (rédiger, relire)
- `cro` : capture (`formulaire.md`, `popup.md`)
- `design` et `revue` : design sous tokens atelier/marque, puis revue
- skill d'emailing installée (par exemple `email-sequence`) : séquence de nurturing
- `brand-check` — validation obligatoire
