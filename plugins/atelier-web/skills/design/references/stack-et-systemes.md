# Systèmes de design officiels et pile par défaut

Détail des étapes 3 et 4 de `execution.md`. Dans l'atelier, la fabrique produit du HTML statique avec les jetons de la marque (`atelier/marque/tokens.json`) : ces conventions valent pour un projet sous framework, ou quand le brief demande un système officiel.

## Brief → design system

Si le brief correspond à un système officiel, installer le **paquet officiel**, ne pas recréer son CSS : Material (`@material/web`), Fluent (`@fluentui/react-components`), Carbon (`@carbon/react`), Polaris (Shopify), Atlaskit, Primer (GitHub), `govuk-frontend` ou `uswds` (secteur public), Bootstrap 5.3 (MVP rapide), Radix Themes, shadcn/ui (jamais en état par défaut), Tailwind v4 (défaut indé et SaaS moderne). **Un seul système par projet.**

Si le brief est une **esthétique** sans paquet officiel (glassmorphism, bento, brutalisme, éditorial, dark tech, aurora, typographie cinétique) : CSS natif + Tailwind, en disant en commentaire ce qui est une approximation (le « Liquid Glass » web est une approximation du glassmorphism : il n'existe pas de `liquid-glass.css` officiel d'Apple).

## Pile et conventions par défaut (projet sous framework)

- **Framework** : React ou Next.js, Server Components par défaut. Tout composant avec mouvement, défilement ou pointeur = feuille isolée `'use client'`.
- **Styles** : Tailwind v4 (plugin `@tailwindcss/postcss`, pas `tailwindcss` dans `postcss.config`).
- **Animation** : Motion (`import { motion } from "motion/react"`, version figée). Jamais `useState` pour des valeurs continues (souris, défilement) → `useMotionValue`, `useTransform`, `useScroll`. Pile complète et niveau natif : skill `motion`.
- **Polices** : `next/font` ou `@font-face` auto-hébergé + `font-display: swap`. Jamais de `<link>` Google Fonts en production.
- **Icônes** : Phosphor > HugeIcons > Radix > Tabler. Lucide sur demande explicite seulement. **Jamais de SVG d'icône dessiné à la main.** Une famille par projet, `strokeWidth` global.
- **Emoji** : découragés dans le code et le texte visible (cohérent avec la checklist de marque § 3).
- **Mise en page** : conteneur `max-w-[1400px] mx-auto` ; `min-h-[100dvh]`, jamais `h-screen` ; CSS Grid plutôt que des calculs flexbox en pourcentages.
- **Dépendances** : vérifier `package.json` avant tout import ; donner la commande d'installation d'abord.
