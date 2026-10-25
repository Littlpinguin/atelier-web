#!/usr/bin/env bash
# Installe la doctrine de test Brivalle (marque fictive) dans l'espace de travail du cas.
set -euo pipefail
ICI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$ICI/../../_fixtures/installer-projet.sh"
mkdir -p "$(dirname 'atelier/pages/a-propos.md')"
cat > 'atelier/pages/a-propos.md' <<'TEXTE'
# À propos de Brivalle

Dans un monde où la logistique évolue à toute vitesse, Brivalle s'impose comme un acteur incontournable de la planification de tournées.

Il est important de noter que notre outil ne se contente pas de planifier : il transforme en profondeur la manière dont vos équipes travaillent. Ce n'est pas un simple logiciel, c'est un véritable partenaire au quotidien.

De plus, Brivalle permet de plonger au cœur de vos données afin de prendre des décisions éclairées, rapides et pertinentes. En outre, notre équipe passionnée vous accompagne à chaque étape de votre parcours.

En conclusion, l'avenir de vos tournées s'annonce prometteur avec Brivalle.
TEXTE
