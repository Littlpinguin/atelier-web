#!/usr/bin/env python3
"""
Hook PostToolUse de l'atelier web : après un Write ou un Edit d'une page ou d'un
texte du projet, joint au contexte le résultat du linter de marque et rappelle
la skill brand-check.

Se déclenche seulement si :
- le projet a une doctrine posée (atelier/marque/tokens.json existe, ou le
  dossier de ATELIER_MARQUE) : sans elle, l'atelier n'est pas initialisé et le
  hook se tait ;
- le fichier est un .md, .mdx ou .html situé sous atelier/ (landings, pages,
  lead magnets, briefs), hors marque/, modèles et brouillons [WIP].

Le hook ne bloque jamais une écriture : linter absent, en échec, trop lent ou
avec une sortie inattendue, il retombe sur le rappel simple et sort toujours 0.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

PLUGIN = Path(__file__).resolve().parents[1]
LINTER = PLUGIN / "fabrique" / "scripts" / "lint-brand.py"
TIMEOUT_LINT_S = 20
MAX_LIGNES_LINT = 40

SOUS_CHEMINS_EXCLUS = ("/marque/", "/templates/", "/examples/", "/archives/", "/wip/")
FICHIERS_META = ("CLAUDE.md", "README.md", "STATUS.md", "TODO.md")
NIVEAUX_FR = {"error": "erreur", "warning": "avertissement"}


def racine_projet(payload: dict) -> Path:
    return Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd()).resolve()


def doit_declencher(chemin: str, projet: Path) -> bool:
    if not chemin or not re.search(r"\.(md|mdx|html)$", chemin, re.IGNORECASE):
        return False
    base = os.path.basename(chemin)
    if base in FICHIERS_META or "[WIP]" in base or "[wip]" in base:
        return False
    marque = projet / os.environ.get("ATELIER_MARQUE", "atelier/marque")
    if not (marque / "tokens.json").is_file():
        return False
    try:
        relatif = "/" + Path(chemin).resolve().relative_to(projet).as_posix()
    except ValueError:
        return False
    if not relatif.startswith("/atelier/"):
        return False
    return not any(s in relatif for s in SOUS_CHEMINS_EXCLUS)


def _formater(constat: dict) -> str:
    position = f"{constat.get('line', '?')}"
    if constat.get("column"):
        position += f":{constat['column']}"
    niveau = constat.get("level", "?")
    return f"  ligne {position} [{constat.get('rule', '?')}] {NIVEAUX_FR.get(niveau, niveau)} : {constat.get('message', '')}"


def bloc_lint(chemin: str, projet: Path) -> str | None:
    """Lance le linter sur le fichier ; None dès que le résultat n'est pas exploitable."""
    try:
        if not LINTER.exists():
            return None
        resultat = subprocess.run(
            [sys.executable, str(LINTER), chemin, "--format", "json"],
            capture_output=True, text=True, timeout=TIMEOUT_LINT_S, cwd=str(projet),
        )
        rapport = json.loads(resultat.stdout)
        resume, constats = rapport["summary"], rapport["findings"]
        erreurs, avertissements = int(resume.get("errors", 0)), int(resume.get("warnings", 0))
        if erreurs:
            titre = f"🔴 LINT DE MARQUE : {erreurs} erreur" + ("s" if erreurs > 1 else "")
            if avertissements:
                titre += f", {avertissements} avertissement" + ("s" if avertissements > 1 else "")
            consigne = "Les erreurs sont bloquantes : corrige-les avant toute autre étape du brand check."
        elif avertissements:
            titre = f"🟠 LINT DE MARQUE : {avertissements} avertissement" + ("s" if avertissements > 1 else "")
            consigne = "Aucune erreur bloquante. Lis chaque avertissement : corriger, ou justifier dans le rapport."
        else:
            return "✅ LINT DE MARQUE : aucun constat déterministe sur ce fichier.\n"
        lignes = [_formater(c) for c in constats[:MAX_LIGNES_LINT]]
        if len(constats) > len(lignes):
            lignes.append(f"  … et {len(constats) - len(lignes)} autres constats, relancer le linter pour la liste complète.")
        return f"{titre}\n" + "\n".join(lignes) + f"\n\nRelancer après correction : `python3 {LINTER} {chemin}`\n{consigne}\n"
    except Exception:
        return None


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    chemin = (payload.get("tool_input") or {}).get("file_path", "") or ""
    projet = racine_projet(payload)
    if not doit_declencher(chemin, projet):
        return 0
    rappel = (
        "BRAND CHECK À FAIRE\n\n"
        f"Tu viens d'écrire ou de modifier `{os.path.basename(chemin)}` dans l'atelier web.\n\n"
        "**Avant de rendre la main**, invoque la skill `atelier-web:brand-check` sur ce livrable "
        "(filtre 5 points : vocabulaire, ton, preuve, audience, visuel). Applique les corrections 🟠, "
        "remonte chaque 🔴, et n'annonce rien comme validé avant un ✅."
    )
    lint = bloc_lint(chemin, projet)
    if lint:
        rappel = f"{lint}\n---\n\n{rappel}"
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": rappel}}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
