# Voice doctrine: Brivalle

Source of truth for tone, vocabulary, and style rules. Every producing role (03 through 09) reads this before drafting. The `brand-check` skill uses it as the filter.

## Voice position

Brivalle parle comme une cheffe d'exploitation qui a fait des tournées : concrète, chiffrée, sans jargon logiciel. Sûre de son outil, elle dit aussi ce qu'il ne fait pas. Vouvoiement partout.

(Two sentences describing where this brand sits on the axes formal/casual, technical/accessible, confident/humble, playful/serious. Avoid single-label summaries like "professional yet approachable": they don't encode anything the cockpit can use.)

## Preferred vocabulary

Use these words intentionally and often:

- tournée, dépôt, créneau, chauffeur, kilomètre évité
- planifier, livrer, prévoir, recaler
- « vos chauffeurs », « votre dépôt », « la tournée du lendemain »

## Banned vocabulary

Never use these. Claimed terms, clichés, and words the brand has actively rejected:

- écosystème
- révolution, révolutionnaire
- « optimisation intelligente »
- « leader du marché »
- « solution clé en main »

This list is mirrored in `${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/lint-brand.toml` (`[forbidden-words.charter]`), so the deterministic linter blocks it in every draft. Change it here first, then there. The generic dead AI vocabulary lives in `anti-ai-writing-style.md`, not here.

## Typography rules

- Vouvoiement partout.
- Espace insécable avant ; : ! ? et à l'intérieur des guillemets « ».
- Demi-cadratin toléré dans les plages (9 h – 12 h) ; jamais de cadratin.
- Titres en casse de phrase, sans point final.
- Aucun emoji sur les pages.

Default construction rules, kept unless the brand explicitly overrides them:
- **No final period on a title.** Headlines, hooks, slide titles, text on visuals and email subject lines end without a period; body copy and captions keep normal punctuation. *Why*: a period closes the reading exactly where a title should open it. Checked by `${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/lint-brand.py` (rule `title-period`).
- **No orphan word at the end of a short block.** In a title, lede, tag or call to action, no word sits alone on the last line; check the line breaks and force the break at the right place. *Why*: an isolated word draws the eye to the empty space and gives away an unreviewed layout. No linter can see a rendered line break: check it on the rendered visual or page.
- **No em dash (U+2014, the long dash) in published copy** (see `anti-ai-writing-style.md`, section 2). Checked by `${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/lint-brand.py` (rule `dashes`).

Examples of rules worth encoding:
- Em dashes vs en dashes vs hyphens (a ban on en dashes too goes in `[dashes]` of `${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/lint-brand.toml`)
- Serial comma / Oxford comma
- Capitalization in headings (sentence case vs title case)
- Single vs double space after period
- Quotes: curly vs straight, single vs double
- Hashtag policy on social channels (a total ban turns on `[hashtags]` in `${CLAUDE_PLUGIN_ROOT}/fabrique/scripts/lint-brand.toml`)

## Signature phrases and taglines

Recurring phrasings that feel like house style. Reusable in copy where appropriate:

- « La tournée prête avant le café »

## Key numbers (canonical)

Every number cited in published content comes from this list (or `messaging-framework.md`). Numbers outside these lists require explicit external citation.

- 1 200 dépôts équipés (chiffre fictif de la fixture de test)
- 20 minutes pour planifier la tournée du lendemain, contre une matinée au tableur (chiffre fictif de la fixture de test)

## Language rules

- **Primary language**: français
- **Bilingual**: non, français seulement
- **Bilingual production rules**: sans objet

## AI disclosure policy

Lives in `divulgation-ia.md` (single reference: what gets disclosed, the wording per channel, edge cases). Not repeated here.

## What counts as "off-voice"

Examples of phrasings that would fail a brand-check on tone grounds, even if they use allowed vocabulary:

- (3-5 real-world examples collected during la skill `demarrer-projet-web` from rejected drafts or explicit user feedback)

Every later rejection is logged in `exemples-rejetes.md` (written by step 5 of the `brand-check` skill), and the generic AI tells live in `anti-ai-writing-style.md`. Read both alongside the published examples before drafting.
