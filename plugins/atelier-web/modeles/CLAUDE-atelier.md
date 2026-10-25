## Atelier web

Ce projet utilise le plugin `atelier-web` (skills, agents et fabrique de pages). Point d'entrée : skill `atelier-web:demarrer-projet-web`.

- **Doctrine de marque** : `atelier/marque/` (lire `atelier/marque/CLAUDE.md` d'abord). Une skill de l'atelier ne produit rien sans elle.
- **Système de design du site** : `{{CHEMIN_DESIGN_MD}}` (par défaut `atelier/marque/design.md`). Pages de référence : `{{PAGES_REFERENCE}}`.
- **Livrables** : landings dans `{{DOSSIER_LANDINGS}}` (par défaut `atelier/landings/<slug>/`), pages dans `{{DOSSIER_PAGES}}`, registre `atelier/publie.md`.
- **Pile** : {{PILE}} (exemple : HTML statique et build Python ; Next.js ; WordPress).
- **Aperçu local** : `{{COMMANDE_APERCU}}` (exemple : `python3 -m http.server --directory dist 8093`). Toujours prévisualiser la sortie du build.
- **Voir un rendu** : {{OUTILS_RENDU}} (exemple : navigateur intégré autorisé ; ou « aucun navigateur piloté : Playwright et Chrome sans tête seulement, l'humain ouvre la page »).
- **Mesure d'audience** : {{MESURE}} (exemple : GA4 `G-XXXX` dans la configuration, ou aucune).
- **Publication** : {{REGLES_PUBLICATION}} (exemple : chaque modification part sur `staging` ; la production seulement après validation explicite).
- **Variables des scripts** : si la doctrine ne vit pas dans `atelier/marque/`, exporter `ATELIER_MARQUE=<chemin>` avant de lancer les scripts de la fabrique.

Règles qui priment, dans ce projet : {{REGLES_PROJET}}
