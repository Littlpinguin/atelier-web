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
<style>
  .conteneur { width: 1200px; margin: 0 auto; }
  .bandeau { width: 100vw; padding: 0 48px; background: var(--brand-dark); color: var(--brand-white); }
  .programme { display: grid; grid-template-columns: 300px 300px 300px; gap: 40px; }
  .visuel img { width: 1400px; }
  table { width: 900px; }
</style>
</head>
<body>
  <main>
    <section class="conteneur">
      <h1>La tournée du lendemain prête en vingt minutes</h1>
      <a href="#inscription" data-cta="primaire">Réserver ma place</a>
    </section>
    <section class="bandeau"><p>Jeudi 3 juin 2027, Halle Lucine, Bordeaux, et en direct</p></section>
    <section class="conteneur programme">
      <div>8 h 30 Accueil</div><div>9 h Planifier en vingt minutes</div><div>11 h Atelier créneaux</div>
    </section>
    <section class="visuel"><img src="plan-tournee.webp" alt="Plan d'une tournée de livraison" width="1400" height="700"></section>
    <section class="conteneur">
      <table><tr><th>Heure</th><th>Séquence</th><th>Intervenant</th><th>Format</th></tr></table>
    </section>
  </main>
</body>
</html>
TEXTE
