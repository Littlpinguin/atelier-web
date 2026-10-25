#!/usr/bin/env python3
"""
Hook PostToolUse de l'atelier web : après l'écriture d'une page ou d'un texte du
projet, joint au contexte le résultat du linter de marque et rappelle la skill
brand-check.

Deux chemins d'écriture sont suivis :
- Write et Edit : le fichier écrit, donné par l'outil ;
- Bash : une page assemblée par script (assemble-landing.py, insertion scriptée
  d'un fragment, copie) ne passe pas par Write. Pour une commande qui mentionne
  « atelier » (un chemin atelier/, une variable ATELIER_, un script de la
  fabrique) et qui peut écrire, le hook cherche sous atelier/ les fichiers
  modifiés depuis leur dernier contrôle et les lint d'un seul passage. Une
  commande en lecture seule (ls, cat, grep, find sans -exec ni -delete, git
  status…, sans redirection vers un fichier) ne déclenche rien.

Le même script tourne aussi en PreToolUse sur Bash : avant la première commande
de la session, il note l'heure de départ du registre. Les fichiers déjà là à ce
moment (projet installé, doctrine copiée, page modifiée dans un éditeur avant la
session) ne passent donc jamais pour écrits par une commande.

Se déclenche seulement si :
- le projet a une doctrine posée (atelier/marque/tokens.json existe, ou le
  dossier de ATELIER_MARQUE) : sans elle, l'atelier n'est pas initialisé et le
  hook se tait ;
- le fichier est un .md, .mdx ou .html situé sous atelier/ (landings, pages,
  lead magnets, briefs), hors marque/, modèles et brouillons [WIP].

Registre de session : chaque fichier contrôlé y est noté avec sa date de
modification, dans le dossier temporaire du système. Un fichier inchangé depuis
son dernier contrôle ne se relint pas ; un fichier jamais vu se lint s'il a été
modifié depuis le départ du registre (premier passage en PreToolUse, ou première
écriture par Write ou Edit). Si le passage en PreToolUse manque, le départ
retombe sur les dix dernières minutes.

Le hook ne bloque jamais une écriture : linter absent, en échec, trop lent ou
avec une sortie inattendue, il retombe sur le rappel simple et sort toujours 0.
"""
from __future__ import annotations

import json
import os
import re
import shlex
import subprocess
import sys
import tempfile
import time
from pathlib import Path

PLUGIN = Path(__file__).resolve().parents[1]
LINTER = PLUGIN / "fabrique" / "scripts" / "lint-brand.py"
TIMEOUT_LINT_S = 20
MAX_LIGNES_LINT = 40
MAX_FICHIERS_BASH = 10
FENETRE_PREMIER_PASSAGE_S = 600

SOUS_CHEMINS_EXCLUS = ("/marque/", "/templates/", "/examples/", "/archives/", "/wip/")
DOSSIERS_IGNORES = {"marque", "templates", "examples", "archives", "wip", "assets", "node_modules"}
FICHIERS_META = ("CLAUDE.md", "README.md", "STATUS.md", "TODO.md")
NIVEAUX_FR = {"error": "erreur", "warning": "avertissement"}


def racine_projet(payload: dict) -> Path:
    return Path(os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd()).resolve()


def doctrine_posee(projet: Path) -> bool:
    marque = projet / os.environ.get("ATELIER_MARQUE", "atelier/marque")
    return (marque / "tokens.json").is_file()


def doit_declencher(chemin: str, projet: Path) -> bool:
    if not chemin or not re.search(r"\.(md|mdx|html)$", chemin, re.IGNORECASE):
        return False
    base = os.path.basename(chemin)
    if base in FICHIERS_META or "[WIP]" in base or "[wip]" in base:
        return False
    if not doctrine_posee(projet):
        return False
    try:
        relatif = "/" + Path(chemin).resolve().relative_to(projet).as_posix()
    except ValueError:
        return False
    if not relatif.startswith("/atelier/"):
        return False
    return not any(s in relatif for s in SOUS_CHEMINS_EXCLUS)


# --------------------------------------------------------------------------
# Registre de session
# --------------------------------------------------------------------------

def _chemin_registre(payload: dict) -> Path:
    session = re.sub(r"[^A-Za-z0-9_-]", "", str(payload.get("session_id") or ""))[:80]
    return Path(tempfile.gettempdir()) / "atelier-web-hook" / f"{session or 'sans-session'}.json"


def lire_registre(payload: dict) -> dict:
    try:
        registre = json.loads(_chemin_registre(payload).read_text(encoding="utf-8"))
        if isinstance(registre, dict) and isinstance(registre.get("fichiers"), dict):
            return registre
    except Exception:
        pass
    return {"debut": None, "fichiers": {}}


def noter_controles(payload: dict, registre: dict, chemins: list[Path]) -> None:
    """Note la date de modification de chaque fichier contrôlé ; ne lève jamais."""
    try:
        for chemin in chemins:
            try:
                registre["fichiers"][str(chemin)] = chemin.stat().st_mtime
            except OSError:
                continue
        if registre.get("debut") is None:
            registre["debut"] = time.time()
        cible = _chemin_registre(payload)
        cible.parent.mkdir(parents=True, exist_ok=True)
        cible.write_text(json.dumps(registre), encoding="utf-8")
    except Exception:
        pass


# --------------------------------------------------------------------------
# Fichiers écrits par une commande Bash
# --------------------------------------------------------------------------

def commande_vise_atelier(payload: dict) -> bool:
    commande = (payload.get("tool_input") or {}).get("command", "") or ""
    return bool(re.search(r"atelier", commande, re.IGNORECASE))


COMMANDES_LECTURE = {
    "ls", "cat", "head", "tail", "less", "more", "grep", "egrep", "fgrep", "rg", "find", "wc", "stat",
    "file", "du", "tree", "pwd", "cd", "echo", "printf", "sort", "uniq", "cut", "tr", "diff", "cmp",
    "jq", "which", "test", "[", "true", "basename", "dirname", "realpath", "readlink", "sed", "awk",
    "column", "nl", "od", "xxd", "shasum", "md5", "git",
}
GIT_LECTURE = {"status", "log", "diff", "show", "ls-files", "grep", "blame", "rev-parse"}
FIND_ECRITURE = {"-exec", "-execdir", "-ok", "-okdir", "-delete", "-fprint", "-fprint0", "-fprintf", "-fls"}
REDIRECTIONS_SANS_FICHIER = re.compile(r"\d?>&\d|&?\d?>\s*/dev/null")


def lecture_seule(commande: str) -> bool:
    """Vrai si chaque segment de la commande ne fait que lire. Au moindre doute, faux."""
    if not commande.strip() or "$(" in commande or "`" in commande:
        return False
    nettoyee = REDIRECTIONS_SANS_FICHIER.sub(" ", commande)
    if ">" in nettoyee:
        return False
    for segment in re.split(r"\|\||&&|[;|&\n]", nettoyee):
        segment = segment.strip().strip("(){} ")
        if not segment:
            continue
        try:
            mots = shlex.split(segment)
        except ValueError:
            return False
        while mots and re.match(r"^[A-Za-z_][A-Za-z0-9_]*=", mots[0]):
            mots = mots[1:]
        if mots and mots[0] in ("for", "done", "fi"):
            continue
        while mots and mots[0] in ("do", "then", "else", "if", "!"):
            mots = mots[1:]
        if mots and mots[0] == "rtk":
            mots = mots[2:] if len(mots) > 1 and mots[1] == "proxy" else mots[1:]
        if not mots:
            continue
        nom = os.path.basename(mots[0])
        if nom not in COMMANDES_LECTURE:
            return False
        if nom == "find" and FIND_ECRITURE.intersection(mots):
            return False
        if nom == "sed" and any(m.startswith("-i") or m.startswith("--in-place") for m in mots[1:]):
            return False
        if nom == "git":
            reste, i = mots[1:], 0
            while i < len(reste) and reste[i].startswith("-"):
                i += 2 if reste[i] in ("-C", "-c") else 1
            if i >= len(reste) or reste[i] not in GIT_LECTURE:
                return False
    return True


def noter_depart(payload: dict, projet: Path) -> None:
    """PreToolUse : note le départ du registre avant la première commande ; ne lève jamais."""
    try:
        if not doctrine_posee(projet):
            return
        registre = lire_registre(payload)
        if registre.get("debut") is None:
            noter_controles(payload, registre, [])
    except Exception:
        pass


def fichiers_modifies(projet: Path, registre: dict) -> list[Path]:
    """Pages et textes sous atelier/ modifiés depuis leur dernier contrôle, les plus récents d'abord."""
    racine = projet / "atelier"
    if not racine.is_dir():
        return []
    depuis = registre.get("debut") or (time.time() - FENETRE_PREMIER_PASSAGE_S)
    deja = registre.get("fichiers", {})
    trouves: list[tuple[float, Path]] = []
    for dossier, sous_dossiers, fichiers in os.walk(racine):
        sous_dossiers[:] = [d for d in sous_dossiers if d not in DOSSIERS_IGNORES and not d.startswith(".")]
        for nom in fichiers:
            chemin = Path(dossier) / nom
            if not doit_declencher(str(chemin), projet):
                continue
            try:
                mtime = chemin.stat().st_mtime
            except OSError:
                continue
            vu = deja.get(str(chemin))
            if (vu is not None and mtime <= vu) or (vu is None and mtime < depuis):
                continue
            trouves.append((mtime, chemin))
    trouves.sort(reverse=True)
    return [chemin for _, chemin in trouves]


# --------------------------------------------------------------------------
# Lint et message
# --------------------------------------------------------------------------

def _formater(constat: dict, avec_fichier: bool) -> str:
    position = f"{constat.get('line', '?')}"
    if constat.get("column"):
        position += f":{constat['column']}"
    niveau = constat.get("level", "?")
    fichier = f"{constat.get('file', '?')} " if avec_fichier else ""
    return f"  {fichier}ligne {position} [{constat.get('rule', '?')}] {NIVEAUX_FR.get(niveau, niveau)} : {constat.get('message', '')}"


def bloc_lint(chemins: list[str], projet: Path) -> str | None:
    """Lance le linter sur les fichiers ; None dès que le résultat n'est pas exploitable."""
    try:
        if not LINTER.exists() or not chemins:
            return None
        resultat = subprocess.run(
            [sys.executable, str(LINTER), *chemins, "--format", "json"],
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
            sujet = "ce fichier" if len(chemins) == 1 else "ces fichiers"
            return f"✅ LINT DE MARQUE : aucun constat déterministe sur {sujet}.\n"
        lignes = [_formater(c, len(chemins) > 1) for c in constats[:MAX_LIGNES_LINT]]
        if len(constats) > len(lignes):
            lignes.append(f"  … et {len(constats) - len(lignes)} autres constats, relancer le linter pour la liste complète.")
        return (f"{titre}\n" + "\n".join(lignes)
                + f"\n\nRelancer après correction : `python3 {LINTER} {' '.join(chemins)}`\n{consigne}\n")
    except Exception:
        return None


def rappel_brand_check(livrable: str) -> str:
    return (
        "BRAND CHECK À FAIRE\n\n"
        f"{livrable}\n\n"
        "**Avant de rendre la main**, invoque la skill `atelier-web:brand-check` sur ce livrable "
        "(filtre 5 points : vocabulaire, ton, preuve, audience, visuel). Applique les corrections 🟠, "
        "remonte chaque 🔴, et n'annonce rien comme validé avant un ✅."
    )


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    if not isinstance(payload, dict):
        return 0
    projet = racine_projet(payload)
    if payload.get("hook_event_name") == "PreToolUse":
        if payload.get("tool_name") == "Bash":
            noter_depart(payload, projet)
        return 0
    if payload.get("tool_name") == "Bash":
        commande = (payload.get("tool_input") or {}).get("command", "") or ""
        if not commande_vise_atelier(payload) or lecture_seule(commande) or not doctrine_posee(projet):
            return 0
        registre = lire_registre(payload)
        modifies = fichiers_modifies(projet, registre)
        if not modifies:
            return 0
        retenus = modifies[:MAX_FICHIERS_BASH]
        relatifs = [p.relative_to(projet).as_posix() for p in retenus]
        liste = ", ".join(f"`{r}`" for r in relatifs)
        if len(modifies) > len(retenus):
            liste += f" (et {len(modifies) - len(retenus)} autres)"
        livrable = f"Une commande vient d'écrire ou de modifier dans l'atelier web : {liste}."
        lint = bloc_lint(relatifs, projet)
        noter_controles(payload, registre, retenus)
    else:
        chemin = (payload.get("tool_input") or {}).get("file_path", "") or ""
        if not doit_declencher(chemin, projet):
            return 0
        livrable = f"Tu viens d'écrire ou de modifier `{os.path.basename(chemin)}` dans l'atelier web."
        lint = bloc_lint([chemin], projet)
        noter_controles(payload, lire_registre(payload), [Path(chemin).resolve()])
    rappel = rappel_brand_check(livrable)
    if lint:
        rappel = f"{lint}\n---\n\n{rappel}"
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": rappel}}))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)
