---
description: 'Landing assemblée par la fabrique depuis le modèle evenement, marqueurs branchés, lint de marque passé.'
tags: [bout-en-bout]
max_turns: 45
timeout_seconds: 1500
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash, TodoWrite]
runs: 2
---

Le cadrage de la page d'inscription de la matinale Brivalle 2027 est fait et validé : brief, direction et textes sont ceux du modèle « evenement » de l'atelier, que j'ai relus et que je garde tels quels. Produis la page dans atelier/landings/matinale-2027/index.html à partir de ce modèle, en branchant les adresses de test : formulaire https://brivalle.example/api/inscription, itinéraire https://brivalle.example/itineraire, confidentialité https://brivalle.example/confidentialite, mentions légales https://brivalle.example/mentions-legales. Passe ensuite le linter de marque sur la page et dis-moi ce qui reste à faire avant publication. Ne publie rien.
