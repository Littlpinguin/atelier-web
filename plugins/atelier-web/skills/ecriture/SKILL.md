---
name: ecriture
description: "Textes des pages web dans la voix de la marque du projet, en deux modes : rédiger (titres, accroches, sections, boutons) et relire (sept passes, puis passe curative quand un texte sonne IA). Pour « écris le texte de », « réécris », « relis ce texte », « ça sonne ChatGPT », « humanise »."
---

# ecriture : les mots de la marque, sans tics d'IA

Deux modes, une seule doctrine. **Rédiger** produit les textes d'une page : titres, accroches, sections, boutons, microcopie. **Relire** corrige un texte existant en sept passes, puis l'humanise s'il sonne encore généré.

## Décider le mode

| La demande | Mode | Lire |
|---|---|---|
| « Écris le texte de », « rédige le hero », « propose des titres », textes définitifs d'une spec de landing, contenu d'un lead magnet | Rédiger | `references/rediger.md` |
| « Relis », « corrige », « valide ce texte avant publication » | Relire | `references/relire.md` |
| « Ça sonne ChatGPT », « trop robotique », « humanise », texte hérité ou écrit par un tiers | Relire, passe curative | `references/humaniser.md` ; pour un texte en anglais, aussi `references/ai-tells.md` |

Un texte rédigé passe par une relecture avant livraison, puis par `brand-check`.

## Étape 0 : la doctrine, avant la première ligne

1. Lire dans `atelier/marque/` : `voice.md` (position, vocabulaire préféré et banni, typographie), `checklist-pre-composition.md`, `anti-ai-writing-style.md`, `exemples-rejetes.md`, `messaging-framework.md` (formulations canoniques, seuls chiffres publiables), et `personas.md` si le texte vise une audience.
2. Lire les textes déjà publiés qui s'en approchent (pages du site, `atelier/publie.md`) pour calibrer le ton et ne pas se répéter.
3. Fichier manquant ou porteur de `{{…}}` : arrêter et lancer `demarrer-projet-web`.

## Règles dures, les deux modes

- Les termes bannis de `voice.md` et la liste noire de `anti-ai-writing-style.md` ne passent jamais. `python3 ${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/lint-brand.py <fichier>` les contrôle, avant et après une relecture.
- Aucun tiret cadratin (`—`), aucun parallélisme négatif (« ce n'est pas X, c'est Y »), aucune formule qui annonce au lieu de dire, aucune phrase qui n'apprend rien au lecteur.
- Chaque chiffre vient de `messaging-framework.md` ou d'une source citée ; un chiffre absent reste un trou, signalé.
- Le registre de la doctrine partout (vouvoiement ou tutoiement) ; titres sans point final ; règles typographiques de `voice.md`.
- L'information la plus importante d'abord : aucun préambule institutionnel (« Chez X, nous… »).
- Relire, c'est corriger : une violation trouvée se corrige, elle ne se signale pas seulement ; la voix de l'auteur reste, sauf demande de réécriture.

## Références

| Fichier | Contenu |
|---|---|
| `references/rediger.md` | Préflight, design system à lire, catalogue des sections, principes (clarté, donnée en héros, bénéfice, précision, lecture en diagonale), checklist avant livraison |
| `references/relire.md` | Les sept passes (données, vocabulaire, ton, clarté, structure, brand-check, format), rapport de relecture, passe curative |
| `references/humaniser.md` | Passe curative en huit passes (structure, inflation, vocabulaire, grammaire, rythme, précautions, transitions, voix), test à voix haute, format des changements |
| `references/ai-tells.md` | Liste anglaise des mots, phrases et structures qui signent un texte généré, avec heuristique de détection |

Provenance (humanize-writing) : `${CLAUDE_PLUGIN_ROOT}/docs/sources/vendored-design2.md`.
