#!/usr/bin/env bash
# Installe l'atelier web et les plugins complémentaires utilisés avec lui.
#
# Usage :
#   ./outils-complementaires/installer.sh              # l'atelier + les essentiels
#   ./outils-complementaires/installer.sh --tout       # + animation avancée, 3D, SEO, marketing, Figma
#   ./outils-complementaires/installer.sh --projet     # même chose, mais pour le projet courant seulement
#   ./outils-complementaires/installer.sh --essai      # affiche les commandes sans rien installer
#
# Prérequis : Claude Code installé (commande `claude`), accès au dépôt privé
# Littlpinguin/atelier-web, et git authentifié sans invite (gh auth login puis gh auth setup-git).
# Chaque plugin s'installe depuis sa source d'origine : rien n'est recopié ici.
set -euo pipefail

TOUT=0
PORTEE="user"
ESSAI=0
for arg in "$@"; do
  case "$arg" in
    --tout) TOUT=1 ;;
    --projet) PORTEE="project" ;;
    --essai) ESSAI=1 ;;
    -h|--help) sed -n '2,12p' "$0"; exit 0 ;;
    *) echo "Option inconnue : $arg" >&2; exit 2 ;;
  esac
done

command -v claude >/dev/null 2>&1 || { echo "La commande « claude » est introuvable : installez Claude Code d'abord." >&2; exit 1; }

ECHECS=()

lancer() {
  echo "→ $*"
  if [ "$ESSAI" -eq 1 ]; then return 0; fi
  if ! "$@"; then
    ECHECS+=("$*")
    echo "  (échec, on continue)" >&2
  fi
}

marketplace() {
  # Une marketplace déjà connue renvoie une erreur sans gravité : elle est ignorée.
  echo "→ claude plugin marketplace add $1"
  [ "$ESSAI" -eq 1 ] && return 0
  claude plugin marketplace add "$1" >/dev/null 2>&1 || echo "  (déjà connue ou inaccessible : vérifiée à l'installation)"
}

plugin() {
  lancer claude plugin install "$1" --scope "$PORTEE"
}

echo "== Atelier web (portée : $PORTEE)"
marketplace Littlpinguin/atelier-web
plugin atelier-web@atelier-web

echo "== Essentiels"
marketplace anthropics/claude-plugins-official
plugin superpowers@claude-plugins-official        # cadrage, plans, débogage, revue
plugin frontend-design@claude-plugins-official    # direction esthétique, anti-gabarit
marketplace nextlevelbuilder/ui-ux-pro-max-skill
plugin ui-ux-pro-max@ui-ux-pro-max-skill           # styles, palettes, typographies, règles UX

if [ "$TOUT" -eq 1 ]; then
  echo "== Animation avancée et 3D"
  marketplace freshtechbro/claudedesignskills
  plugin gsap-scrolltrigger@claude-design-skillstack
  plugin animation-components@claude-design-skillstack
  plugin threejs-webgl@claude-design-skillstack
  plugin meta-skills@claude-design-skillstack

  echo "== SEO et marketing"
  marketplace AgriciDaniel/claude-seo
  plugin claude-seo@agricidaniel-claude-seo
  marketplace coreyhaines31/marketingskills
  plugin marketing-skills@marketingskills

  echo "== Maquettes"
  plugin figma@claude-plugins-official
fi

echo
if [ "${#ECHECS[@]}" -gt 0 ]; then
  echo "Terminé avec ${#ECHECS[@]} échec(s) :"
  printf '  - %s\n' "${ECHECS[@]}"
  echo "Vérifiez l'accès au dépôt (gh auth status) puis relancez la commande en échec."
  exit 1
fi
echo "Terminé. Redémarrez Claude Code, puis dans un projet : /atelier-web:demarrer-projet-web"
