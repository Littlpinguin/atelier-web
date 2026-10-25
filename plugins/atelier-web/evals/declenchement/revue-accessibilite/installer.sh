#!/usr/bin/env bash
# Installe la doctrine de test Brivalle (marque fictive) dans l'espace de travail du cas.
set -euo pipefail
ICI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$ICI/../../_fixtures/installer-projet.sh"
mkdir -p "$(dirname 'atelier/pages/contact.html')"
cat > 'atelier/pages/contact.html' <<'TEXTE'
<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<title>Contact</title>
<style>
  :focus { outline: none; }
  .note { color: #9a9a9a; background: #ffffff; }
  .bouton { background: #0B5D66; color: #fff; padding: 12px 24px; cursor: pointer; display: inline-block; }
</style>
</head>
<body>
  <img src="equipe.jpg">
  <h3>Contactez-nous</h3>
  <p class="note">Réponse sous 24 h ouvrées.</p>
  <form>
    <input type="text" placeholder="Votre nom">
    <input type="email" placeholder="Votre email" tabindex="3">
    <textarea placeholder="Votre message"></textarea>
    <div class="bouton" onclick="envoyer()">Envoyer</div>
  </form>
  <a href="#">Cliquez ici</a> pour lire notre politique de confidentialité.
</body>
</html>
TEXTE
