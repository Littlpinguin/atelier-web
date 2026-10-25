# Brivalle — site et pages de conversion

Projet **fictif** : fixture de test des évals du plugin atelier-web. Le script d'installation des cas le copie en `CLAUDE.md` à la racine de l'espace de travail.

## Atelier web

Ce projet utilise le plugin `atelier-web` (skills, agents et fabrique de pages). Point d'entrée : skill `atelier-web:demarrer-projet-web`.

- **Doctrine de marque** : `atelier/marque/` (lire `atelier/marque/CLAUDE.md` d'abord). Une skill de l'atelier ne produit rien sans elle.
- **Système de design du site** : `atelier/marque/design.md`. Pages de référence : aucune, le site n'a pas encore de page publiée.
- **Livrables** : landings dans `atelier/landings/<slug>/`, pages dans `atelier/pages/`, registre `atelier/publie.md`.
- **Pile** : HTML statique assemblé par la fabrique de l'atelier.
- **Aperçu local** : `python3 -m http.server 8093` depuis la racine du projet.
- **Voir un rendu** : Playwright et Chrome sans tête seulement ; l'humain ouvre la page.
- **Mesure d'audience** : aucune (attributs `data-track` posés, sans suivi branché).
- **Publication** : aucune depuis cet espace de travail.
- **Variables des scripts** : la doctrine vit dans `atelier/marque/`, rien à exporter.

Règles qui priment, dans ce projet : vouvoiement ; aucun chiffre hors de `atelier/marque/messaging-framework.md`.
