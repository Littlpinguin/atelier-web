# Mesure : UTM et événements

Lu en phase 3 (comportements de la spec) et en phase 8 (enregistrement).

## UTM

Toute URL diffusée vers la page, en kebab-case et minuscules :

| Paramètre | Contenu | Exemples |
|---|---|---|
| `utm_source` | Plateforme d'origine | `linkedin`, `newsletter`, `google`, `partenaire-x` |
| `utm_medium` | Type de canal | `social`, `email`, `cpc`, `qr`, `referral` |
| `utm_campaign` | Slug de campagne + année | `{{CAMPAIGN_SLUG}}-2026` |
| `utm_content` | Variante ou emplacement | `post-1`, `cta-hero`, `cta-final` |

Le tableau des URL suivies va dans le brief et dans `atelier/publie.md`.

## Événements

- Chaque CTA porte `data-track` (`cta_click` au clic, avec `data-cta-position` : `hero`, `offre`, `final`…), le formulaire `data-track="generate_lead"`. Le CTA primaire porte en plus `data-cta="primaire"`, que la QA lit pour savoir quelle conversion protéger.
- Si le projet déclare un suivi GA4 (`CLAUDE.md` du projet, § Atelier web) : snippet gtag avec `{{GA4_MEASUREMENT_ID}}`, et un relais qui transforme ces attributs en événements `gtag('event', …)` ou `dataLayer.push(…)`, avec la formule et la langue en paramètres. `generate_lead` se marque comme conversion clé côté GA4 (action manuelle, à signaler à l'humain).
- Sinon : les attributs restent posés, pour brancher la mesure plus tard sans retoucher le HTML.

La QA vérifie les deux cas : suivi déclaré, un événement doit partir au clic de chaque CTA primaire ; suivi absent, le crochet `data-track` doit être là.
