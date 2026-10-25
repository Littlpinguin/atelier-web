#!/usr/bin/env bash
# Installe la doctrine de test Brivalle (marque fictive) dans l'espace de travail du cas.
set -euo pipefail
ICI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$ICI/../../_fixtures/installer-projet.sh"
mkdir -p "$(dirname 'atelier/landings/matinale/index.html')"
cat > 'atelier/landings/matinale/index.html' <<'TEXTE'
<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Matinale Brivalle</title>
<link rel="stylesheet" href="../../marque/tokens.css">
</head>
<body>
  <nav><a href="/">Accueil</a> <a href="/produit/">Produit</a> <a href="/tarifs/">Tarifs</a> <a href="/blog/">Blog</a> <a href="/contact/">Contact</a></nav>
  <section class="hero">
    <h1>Bienvenue chez Brivalle</h1>
    <p>Nous organisons un événement pour parler de logistique et d'innovation.</p>
    <a href="/produit/">En savoir plus</a>
    <a href="/contact/">Nous contacter</a>
  </section>
  <section>
    <h2>Notre entreprise</h2>
    <p>Fondée par des passionnés, Brivalle accompagne les entreprises dans leur transformation.</p>
  </section>
  <section>
    <h2>Le programme</h2>
    <p>Accueil, conférences, atelier et questions.</p>
  </section>
  <section>
    <h2>Inscription</h2>
    <form action="/api/inscription" method="post">
      <input name="prenom" placeholder="Prénom"><input name="nom" placeholder="Nom">
      <input name="email" placeholder="Email"><input name="telephone" placeholder="Téléphone">
      <input name="entreprise" placeholder="Entreprise"><input name="poste" placeholder="Poste">
      <input name="taille" placeholder="Taille de la flotte"><input name="logiciel" placeholder="Logiciel actuel">
      <button>Envoyer</button>
    </form>
  </section>
</body>
</html>
TEXTE
