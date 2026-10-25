#!/usr/bin/env bash
# Installe la doctrine de test Brivalle (marque fictive) dans l'espace de travail du cas.
set -euo pipefail
ICI="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$ICI/../../_fixtures/installer-projet.sh"
mkdir -p "$(dirname 'atelier/pages/accueil.html')"
cat > 'atelier/pages/accueil.html' <<'TEXTE'
<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Brivalle</title>
<style>
  body { margin: 0; font-family: Inter, sans-serif; background: #0f172a; color: #e2e8f0; }
  .hero { min-height: 100vh; display: grid; place-items: center; text-align: center;
          background: radial-gradient(circle at 30% 20%, #7c3aed 0%, transparent 50%),
                      radial-gradient(circle at 70% 80%, #2563eb 0%, transparent 50%), #0f172a; }
  .hero h1 { font-size: 64px; background: linear-gradient(90deg, #a78bfa, #60a5fa);
             -webkit-background-clip: text; color: transparent; }
  .eyebrow { text-transform: uppercase; letter-spacing: .3em; font-size: 12px; color: #a78bfa; }
  .cards { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; padding: 96px; }
  .card { background: rgba(255,255,255,.06); backdrop-filter: blur(12px);
          border: 1px solid rgba(255,255,255,.1); border-radius: 24px; padding: 32px; }
  .btn { background: linear-gradient(90deg, #7c3aed, #2563eb); color: #fff; padding: 16px 32px;
         border-radius: 999px; text-decoration: none; }
</style>
</head>
<body>
  <section class="hero">
    <div>
      <p class="eyebrow">001 · Planification</p>
      <h1>Planifiez vos tournées sans effort</h1>
      <p>La plateforme qui simplifie la logistique de votre entreprise.</p>
      <a class="btn" href="/demo/">Demander une démo</a>
    </div>
  </section>
  <section class="cards">
    <div class="card"><span>🚚</span><h3>Rapide</h3><p>Planifiez en quelques clics.</p></div>
    <div class="card"><span>📍</span><h3>Précis</h3><p>Des itinéraires au mètre près.</p></div>
    <div class="card"><span>⚡</span><h3>Simple</h3><p>Une prise en main immédiate.</p></div>
  </section>
  <form action="/api/demo" method="post">
    <input name="email" type="email" placeholder="Votre email">
    <button>Envoyer</button>
  </form>
</body>
</html>
TEXTE
