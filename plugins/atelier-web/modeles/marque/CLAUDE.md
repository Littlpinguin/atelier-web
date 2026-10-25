# atelier/marque — doctrine de {{COMPANY_NAME}}

Ce dossier est la **source de vérité** de l'identité, de la voix, des preuves et du système visuel. Il ne produit rien : toutes les skills de l'atelier web le lisent avant de produire.

**Règle absolue.** Quand ce dossier et une autre source se contredisent, ce dossier l'emporte ; signaler le conflit à l'humain avant d'agir.

## Quoi lire, pour quel livrable

Lire ce que la ligne indique, dans cet ordre, et rien de plus. Un fichier déjà lu dans la session ne se relit pas.

| Livrable | Fichiers, dans l'ordre |
|---|---|
| Page, section ou landing | `design.md` → `voice.md` → `messaging-framework.md` → `style-guide.md` → `tokens.json` → `design-anti-generique.md` |
| Texte de page | `voice.md` → `checklist-pre-composition.md` → `anti-ai-writing-style.md` → `exemples-rejetes.md` → `messaging-framework.md` |
| Visuel ou illustration | `tokens.json` → `style-guide.md` → `assets/index.md` → `divulgation-ia.md` → `droits.md` si un logo tiers ou une personne apparaît |
| Cibler une audience | `personas.md` |
| Un chiffre, une preuve | `messaging-framework.md` (chiffres clés et leur source) |

## Inventaire

| Fichier | Rôle |
|---|---|
| `tokens.json` | Valeurs exactes : couleurs, dégradé, polices, rayons (DTCG). Seule source des valeurs |
| `tokens.css` | Généré depuis `tokens.json` par `build-tokens.py`. Ne jamais l'éditer à la main entre ses marqueurs |
| `style-guide.md` | Intention visuelle, illustration, interdits visuels |
| `design.md` | Système du site : fondations, signatures, composants, mouvement, règles, checklist, décisions de la marque |
| `voice.md` | Position de voix, vocabulaire préféré et banni, typographie |
| `anti-ai-writing-style.md`, `checklist-pre-composition.md`, `design-anti-generique.md` | Garde-fous contre l'écriture et le design « générés » |
| `messaging-framework.md` | Positionnement, messages par audience, chiffres réels et leurs sources |
| `personas.md` | Deux à quatre audiences, leurs objections |
| `exemples-rejetes.md` | Ce que la marque a déjà refusé, avec la règle |
| `divulgation-ia.md`, `droits.md` | Mention des contenus générés ; registre des droits (polices, logos, personnes) |
| `lint-brand.toml`, `build-tokens.toml` | Réglages des scripts de la fabrique pour ce projet |
| `assets/` | Logos, polices, illustrations validés, avec leur fiche dans `assets/index.md` |
