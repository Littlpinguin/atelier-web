#!/usr/bin/env bash
# Installe la doctrine de test Brivalle (marque fictive) dans l'espace de travail du cas.
set -euo pipefail
ICI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$ICI/../../_fixtures/installer-projet.sh"
mkdir -p "$(dirname 'atelier/pages/brouillon-accueil.md')"
cat > 'atelier/pages/brouillon-accueil.md' <<'TEXTE'
# Brivalle, la solution clé en main de vos tournées.

Brivalle révolutionne la planification — un véritable écosystème pour vos chauffeurs.

98 % de nos clients gagnent une heure par jour.
TEXTE
