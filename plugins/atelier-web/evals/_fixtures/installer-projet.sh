#!/usr/bin/env bash
# Installe le projet d'essai Brivalle (marque fictive) dans le dossier courant,
# l'espace de travail vide d'un cas d'éval. Appelé par le scaffold_script de
# chaque cas : bash "$ICI/../../_fixtures/installer-projet.sh".
#
# Les runs d'éval ne chargent ni CLAUDE.md ni .claude/ : la doctrine arrive ici
# comme de simples fichiers, que les skills de l'atelier lisent comme dans un
# vrai projet.
set -euo pipefail
FIXTURES="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE="$FIXTURES/projet-brivalle"
[ -d "$SOURCE/atelier/marque" ] || { echo "fixture introuvable : $SOURCE" >&2; exit 1; }
cp -R "$SOURCE/." .
mv CLAUDE-projet.md CLAUDE.md
