#!/usr/bin/env python3
"""Reconstruit les démos publiées dans docs/ : trois landings de marques fictives et le catalogue.

Usage : python3 demos/construire.py [--travail DOSSIER]

Chaque marque est montée dans un projet d'essai (dossier de travail, temporaire par défaut) :
jetons tirés du modèle de doctrine, spec du modèle de landing, photos posées dans les emplacements
d'image, puis assemble-landing.py. Écrit docs/demo/<marque>/index.html, docs/catalogue/index.html
et docs/credits-photos/index.html, rien d'autre dans le dépôt.

Les photos viennent de Pexels (licence Pexels). Elles ne sont pas copiées dans le dépôt : chaque page
appelle le CDN de Pexels, recadré au format de l'emplacement et servi en WebP. Elles tiennent la place
des vraies photos qu'une marque fournirait ; la page de crédits nomme chaque photographe.
"""
import argparse
import copy
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parents[1]
P = RACINE / "plugins" / "atelier-web"
F = P / "fabrique"
DOCS = RACINE / "docs"
CREDITS = "credits-photos"

# Photo Pexels : photographe, profil, page de la photo.
PHOTOS = {
    7821731: ("RDNE Stock project", "https://www.pexels.com/@rdne", "https://www.pexels.com/photo/people-holding-a-document-on-a-table-7821731/"),
    8871851: ("Mikhail Nilov", "https://www.pexels.com/@mikhail-nilov", "https://www.pexels.com/photo/an-elderly-woman-in-black-button-down-shirt-seriously-looking-at-the-camera-8871851/"),
    7565176: ("cottonbro studio", "https://www.pexels.com/@cottonbro", "https://www.pexels.com/photo/close-up-shot-a-man-wearing-a-gray-vest-7565176/"),
    33623771: ("abdo alshreef", "https://www.pexels.com/@alshreef", "https://www.pexels.com/photo/aerial-view-of-white-vans-in-rows-in-parking-lot-33623771/"),
    40184469: ("Davide Comunian", "https://www.pexels.com/@tuttosfocato", "https://www.pexels.com/photo/professional-female-portrait-in-gray-suit-40184469/"),
    12191498: ("Daniel Friday Danzor", "https://www.pexels.com/@iamdanzor", "https://www.pexels.com/photo/portrait-of-man-12191498/"),
    30479371: ("Augusto Carneiro Junior", "https://www.pexels.com/@augustocarneirojr", "https://www.pexels.com/photo/professional-woman-in-black-blazer-portrait-30479371/"),
    13375591: ("Sandro Tavares", "https://www.pexels.com/@sandro-tavares-260503371", "https://www.pexels.com/photo/portrait-of-a-young-man-13375591/"),
    5899282: ("Karolina Grabowska", "https://www.pexels.com/@karola-g", "https://www.pexels.com/photo/selective-focus-photo-of-a-person-s-hand-with-a-ring-near-a-touchpad-of-a-laptop-5899282/"),
    14839073: ("Nina zeynep güler", "https://www.pexels.com/@ninazey", "https://www.pexels.com/photo/woman-in-plaid-blazer-wearing-eyeglasses-while-holding-books-14839073/"),
    6981103: ("Mikhail Nilov", "https://www.pexels.com/@mikhail-nilov", "https://www.pexels.com/photo/a-blind-man-wearing-headset-while-using-braille-6981103/"),
    29462835: ("Owen.outdoors", "https://www.pexels.com/@owen-outdoors-409204690", "https://www.pexels.com/photo/hanging-frying-pans-in-kitchen-store-display-29462835/"),
    3042436: ("Caleb Oquendo", "https://www.pexels.com/@caleboquendo", "https://www.pexels.com/photo/a-family-walking-in-the-park-3042436/"),
    39192334: ("Vitaly Gariev", "https://www.pexels.com/@silverkblack", "https://www.pexels.com/photo/doctor-discussing-medical-report-with-patient-39192334/"),
    19961417: ("Th2city Santana", "https://www.pexels.com/@th2city", "https://www.pexels.com/photo/view-of-a-bus-on-a-street-in-city-19961417/"),
    2810140: ("Pragyan Bezbaruah", "https://www.pexels.com/@pragyanbezbo", "https://www.pexels.com/photo/interior-of-a-classic-aerican-muscle-car-2810140/"),
    38256977: ("Antoine Pittet", "https://www.pexels.com/@antoine-pittet-1518705150", "https://www.pexels.com/photo/charming-french-town-hall-facade-in-summer-38256977/"),
    32558348: ("Daria K", "https://www.pexels.com/@daria-k-192438477", "https://www.pexels.com/photo/historic-train-station-in-bornel-france-32558348/"),
    32517434: ("Serra Nur Çevikdal", "https://www.pexels.com/@serra-nur-cevikdal-2147703100", "https://www.pexels.com/photo/cozy-bookstore-interior-with-diverse-shelves-32517434/"),
    963631: ("Brett Sayles", "https://www.pexels.com/@brett-sayles", "https://www.pexels.com/photo/white-and-gray-manual-gauge-963631/"),
    20819288: ("Emiliano Vittoriosi", "https://www.pexels.com/@emilianovittoriosi", "https://www.pexels.com/photo/portrait-of-woman-with-hand-under-chin-20819288/"),
    30976000: ("Hao Peng", "https://www.pexels.com/@hao-peng-2148478861", "https://www.pexels.com/photo/portrait-of-a-man-wearing-glasses-in-studio-30976000/"),
    37363857: ("Mehmet Turgut Kirkgoz", "https://www.pexels.com/@tkirkgoz", "https://www.pexels.com/photo/industrial-worker-pouring-molten-metal-in-factory-37363857/"),
    29948395: ("Burçak Çubukçu", "https://www.pexels.com/@burcak-cubukcu-1107169385", "https://www.pexels.com/photo/modern-hospital-corridor-in-ankara-turkiye-29948395/"),
    37399388: ("Bingqian Li", "https://www.pexels.com/@bingqian-li-230971044", "https://www.pexels.com/photo/scenic-view-of-escalles-village-in-hauts-de-france-37399388/"),
    13005858: ("Brian Magill", "https://www.pexels.com/@brian-magill-157994702", "https://www.pexels.com/photo/a-person-in-white-long-sleeve-shirt-scraping-wood-plank-13005858/"),
    6627667: ("Karolina Grabowska", "https://www.pexels.com/@karola-g", "https://www.pexels.com/photo/doctor-using-a-centrifuge-machine-6627667/"),
    4483610: ("Tiger Lily", "https://www.pexels.com/@tiger-lily", "https://www.pexels.com/photo/warehouse-with-concrete-floors-4483610/"),
    35758714: ("Caleb Oquendo", "https://www.pexels.com/@caleboquendo", "https://www.pexels.com/photo/bright-empty-school-hallway-with-bulletin-boards-35758714/"),
    36706459: ("Zayed Hossain", "https://www.pexels.com/@zayedhossain120", "https://www.pexels.com/photo/focused-developer-at-dual-monitor-setup-36706459/"),
    36423789: ("Keegan Checks", "https://www.pexels.com/@keeganjchecks", "https://www.pexels.com/photo/industrial-glass-furnace-in-operation-36423789/"),
}

UTILISEES = {}  # page -> [(emplacement, id)], pour la page de crédits


def photo(page, emplacement, pid, w, h, recadrage=None):
    """URL du CDN de Pexels, recadrée à w × h et servie en WebP ; note la photo pour les crédits."""
    UTILISEES.setdefault(page, []).append((emplacement, pid))
    url = (f"https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg"
           f"?auto=compress&cs=tinysrgb&fit=crop&w={w}&h={h}&fm=webp")
    return url + (f"&crop={recadrage}" if recadrage else "")


def image(page, emplacement, pid, w, h, alt="", recadrage=None):
    return {"src": photo(page, emplacement, pid, w, h, recadrage), "alt": alt, "width": w, "height": h}


def section(spec, ident):
    return next(s for s in spec["sections"] if (s.get("id") or s["use"]) == ident)


def exemple(fragment, slot):
    """Valeur d'exemple d'un slot, lue dans la fiche du fragment."""
    t = (F / "templates" / "sections" / f"{fragment}.html").read_text(encoding="utf-8")
    meta = json.loads(re.search(r'<script type="application/json" data-section-meta>(.*?)</script>', t, re.S).group(1))
    return copy.deepcopy(meta["slots"][slot]["example"])


def lien_credits(spec, chemin):
    pied = section(spec, "pied").setdefault("slots", {})
    pied["links"] = pied.get("links") or exemple("footer", "links")
    pied["links"].append({"label": "Crédits photos", "href": chemin})


def habiller_ferlane(spec):
    page = "Ferlane · formation"
    section(spec, "hero")["slots"]["image"] = image(
        page, "Hero", 7821731, 1000, 1250, alt="Deux personnes relisent un dossier et l’annotent au stylo rouge")
    section(spec, "lettre")["slots"]["portrait"] = image(page, "Lettre : Hélène Marchetti", 8871851, 480, 480)
    gens = section(spec, "formateurs")["slots"]["people"]
    for personne, pid in zip(gens, (8871851, 7565176)):
        personne["photo"] = photo(page, f"Formateurs : {personne['name']}", pid, 600, 750)
        personne["photo_alt"] = ""


def habiller_brivalle(spec):
    page = "Brivalle · événement"
    i = next(n for n, s in enumerate(spec["sections"]) if s["use"] == "hero-editorial")
    edito = spec["sections"][i]["slots"]
    hero = {"use": "hero", "slots": {
        # dans la colonne du hero à image, « Passer vos tournées » laisserait « tournées » seul sur sa ligne
        "title": "Électrifier<br><span class=\"hl\">vos tournées</span>",
        "lede": edito["lede"], "cta_label": edito["cta_label"], "cta_href": edito["cta_href"], "primary": True,
        "deadline": edito["deadline"], "countdown": edito["countdown"], "detail": edito["detail"],
        "image": image(page, "Hero", 33623771, 1000, 1000,
                       alt="Des dizaines d’utilitaires blancs garés en rangs serrés, vus d’en haut"),
        "object": ""}}
    pratique = {"use": "facts-grid", "id": "essentiel", "slots": {
        "title": "La matinale<br><span class=\"hl\">en pratique</span>", "title_hidden": True, "intro": "",
        "items": [
            {"icon": "calendar", "label": "Quand", "value": "Jeudi 3 juin 2027", "note": "De 8 h 30 à 13 h"},
            {"icon": "pin", "label": "Où", "value": "Halle Lucine à Bordeaux", "note": "Et en direct"},
            {"icon": "list", "label": "Programme", "value": "Trois retours d’expérience", "note": "Puis une table ronde"},
            {"icon": "price", "label": "Prix", "value": "Gratuit", "note": "Replay sous 48 heures"},
        ],
        "cta_label": "", "cta_href": "#inscription", "primary": False}}
    spec["sections"][i:i + 1] = [hero, pratique]
    gens = section(spec, "intervenants")["slots"]["people"]
    for personne, pid in zip(gens, (40184469, 12191498, 30479371, 13375591)):
        personne["photo"] = photo(page, f"Intervenants : {personne['name']}", pid, 600, 750)
        personne["photo_alt"] = ""


def habiller_ouvrance(spec):
    page = "Ouvrance · prestation"
    section(spec, "hero-image-title")["slots"]["image"] = image(page, "Hero, dans le titre", 5899282, 440, 200)
    couvertures = {"cuisine": 29462835, "portail-famille": 3042436, "mutuelle": 39192334, "billetterie": 19961417,
                   "assurance-auto": 2810140, "mairie": 38256977, "train": 32558348, "librairie": 32517434}
    for item in section(spec, "realisations")["slots"]["items"]:
        item["image"] = photo(page, f"Réalisations : {item['title']}", couvertures[item["key"]], 960, 720)
    gens = section(spec, "equipe")["slots"]["people"]
    for personne, (pid, recadrage) in zip(gens, ((14839073, None), (6981103, "right"))):
        personne["photo"] = photo(page, f"Équipe : {personne['name']}", pid, 600, 750, recadrage)
        personne["photo_alt"] = ""


def habiller_catalogue(spec):
    page = "Catalogue des sections"
    spec["intro"]["text"] += (" Dans cette copie en ligne, les emplacements d’image portent des photos Pexels,"
                              " à la place des vraies photos d’une marque.")
    for s in spec["sections"]:
        if s["use"] == "hero-image-title":
            s.setdefault("slots", {})["image"] = image(page, "Hero à image dans le titre", 963631, 440, 200)
    gens = exemple("people", "people")
    for personne, pid in zip(gens, (20819288, 30976000)):
        personne["photo"] = photo(page, f"Personnes : {personne['name']}", pid, 600, 750)
        personne["photo_alt"] = ""
    section(spec, "animateurs").setdefault("slots", {})["people"] = gens
    section(spec, "lettre")["slots"]["portrait"] = image(page, "Lettre signée : Nadia Ferrand", 20819288, 480, 480)
    couvertures = {"fonderie": 37363857, "cliniques": 29948395, "plan-climat": 37399388, "menuiserie": 13005858,
                   "laboratoires": 6627667, "bricolage": 4483610, "lycees": 35758714, "editeur": 36706459,
                   "verrerie": 36423789}
    items = exemple("work-wall", "items")
    for item in items:
        item["image"] = photo(page, f"Mur de réalisations : {item['title']}", couvertures[item["key"]], 960, 720)
    section(spec, "realisations").setdefault("slots", {})["items"] = items


MARQUES = [
    # nom, modèle, couleurs, police, famille Google, rayon des cartes, habillage
    ("ferlane", "formation", dict(primary="#2F6F5E", accent="#C8A24B", dark="#14231F", light="#F6F3EC"),
     "Fraunces", "Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700", "6px", habiller_ferlane),
    ("brivalle", "evenement", dict(primary="#0F4C81", accent="#F2A541", dark="#0B1B2B", light="#F3F6FA"),
     "Space Grotesk", "Space Grotesk:wght@400;500;600;700", "20px", habiller_brivalle),
    ("ouvrance", "prestation", dict(primary="#8C3B2E", accent="#E0A43A", dark="#2A1A14", light="#FBF6F0"),
     "DM Sans", "DM Sans:opsz,wght@9..40,400;9..40,500;9..40,700", "2px", habiller_ouvrance),
]


def assembler(projet, spec, sortie):
    (projet / "page.json").write_text(json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")
    r = subprocess.run([sys.executable, str(F / "scripts" / "assemble-landing.py"), "page.json", "-o", str(sortie),
                        "--force"], cwd=projet, capture_output=True, text=True)
    sys.stdout.write(r.stdout)
    sys.stderr.write(r.stderr)
    if r.returncode:
        sys.exit(f"échec de l'assemblage : {sortie}")
    t = sortie.read_text(encoding="utf-8")
    # liens du dépôt à brancher (mentions, confidentialité, itinéraire) : inertes sur une démo
    sortie.write_text(re.sub(r'href="\{\{URL_[A-Z_]+\}\}"', 'href="#"', t), encoding="utf-8")


def construire_marque(travail, nom, modele, couleurs, police, google, rayon, habiller):
    projet = travail / nom
    marque = projet / "atelier" / "marque"
    if projet.exists():
        shutil.rmtree(projet)
    marque.mkdir(parents=True)
    t = (P / "modeles" / "marque" / "tokens.json").read_text(encoding="utf-8")
    for cle, val in {"{{BRAND_COLOR_PRIMARY}}": couleurs["primary"], "{{BRAND_COLOR_ACCENT}}": couleurs["accent"],
                     "{{BRAND_COLOR_DARK}}": couleurs["dark"], "{{BRAND_COLOR_LIGHT}}": couleurs["light"],
                     "{{BRAND_FONT_PRIMARY}}": police, "{{BRAND_FONT_SECONDARY}}": "JetBrains Mono",
                     "{{COMPANY_NAME}}": nom.capitalize()}.items():
        t = t.replace(cle, val)
    d = json.loads(t)
    d["radius"]["card"]["$value"] = rayon
    (marque / "tokens.json").write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    shutil.copy(F / "templates" / "assets" / "tokens.css", marque / "tokens.css")
    shutil.copy(F / "scripts" / "build-tokens.toml", marque / "build-tokens.toml")
    shutil.copy(P / "modeles" / "marque" / "style-guide.md", marque / "style-guide.md")
    subprocess.run([sys.executable, str(F / "scripts" / "build-tokens.py")], cwd=projet, check=True,
                   stdout=subprocess.DEVNULL)
    spec = yaml.safe_load((F / "templates" / "landing-pages" / "specs" / f"{modele}.yaml").read_text(encoding="utf-8"))
    spec["fonts"] = [google, "JetBrains Mono:wght@500;600"]
    habiller(spec)
    lien_credits(spec, f"../../{CREDITS}/")
    sortie = DOCS / "demo" / nom / "index.html"
    sortie.parent.mkdir(parents=True, exist_ok=True)
    assembler(projet, spec, sortie)


def construire_catalogue(travail):
    projet = travail / "catalogue"
    if projet.exists():
        shutil.rmtree(projet)
    projet.mkdir(parents=True)
    spec = json.loads((F / "templates" / "sections" / "catalogue.json").read_text(encoding="utf-8"))
    habiller_catalogue(spec)
    lien_credits(spec, f"../{CREDITS}/")
    sortie = DOCS / "catalogue" / "index.html"
    assembler(projet, spec, sortie)


def page_credits():
    blocs = []
    for page, emplois in UTILISEES.items():
        lignes = []
        for emplacement, pid in emplois:
            auteur, profil, lien = PHOTOS[pid]
            vignette = (f"https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg"
                        f"?auto=compress&cs=tinysrgb&fit=crop&w=160&h=120&fm=webp")
            lignes.append(
                f'      <li><img src="{html.escape(vignette)}" width="80" height="60" alt="" loading="lazy">'
                f'<span><strong>{html.escape(emplacement)}</strong>'
                f'<a href="{lien}">Photo</a> de <a href="{profil}">{html.escape(auteur)}</a> sur Pexels</span></li>')
        blocs.append(f'    <h2>{html.escape(page)}</h2>\n    <ul role="list">\n' + "\n".join(lignes) + "\n    </ul>")
    gabarit = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Crédits photos des démos de l’atelier web</title>
<meta name="description" content="Les photos Pexels des démos de l’atelier web, emplacement par emplacement, avec leur photographe.">
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap">
<style>
  :root { --midnight: #0D1B2A; --midnight-light: #112240; --golden: #F9DC5C; --off-white: #FAFAFA; --light-blue: #ACCBE1; --soft-blue: #7C98B3; --line: rgba(124, 152, 179, 0.16); }
  * { box-sizing: border-box; }
  body { margin: 0; font-family: "Plus Jakarta Sans", system-ui, sans-serif; color: var(--light-blue); background: linear-gradient(180deg, var(--midnight), var(--midnight-light)); min-height: 100vh; }
  main { max-width: 860px; margin: 0 auto; padding: clamp(2rem, 6vw, 4.5rem) 16px; }
  h1 { color: var(--off-white); font-weight: 800; font-size: clamp(2rem, 4.5vw, 3rem); line-height: 1.08; letter-spacing: -0.02em; margin: 0 0 1rem; }
  h2 { color: var(--off-white); font-size: 1.15rem; margin: 2.5rem 0 0.8rem; }
  p { font-size: 1.05rem; line-height: 1.6; max-width: 44rem; }
  ul { list-style: none; margin: 0; padding: 0; border-top: 1px solid var(--line); }
  li { display: flex; gap: 1rem; align-items: center; padding: 0.7rem 0; border-bottom: 1px solid var(--line); }
  li img { flex: none; border-radius: 6px; object-fit: cover; background: var(--midnight-light); }
  li strong { display: block; color: var(--off-white); font-weight: 600; }
  a { color: var(--golden); }
  .retour { display: inline-block; margin-bottom: 2rem; color: var(--off-white); }
</style>
</head>
<body>
<main>
  <a class="retour" href="../">Retour aux démos</a>
  <h1>Crédits photos</h1>
  <p>Les marques des démos sont fictives. Leurs photos viennent de <a href="https://www.pexels.com">Pexels</a>, sous la <a href="https://www.pexels.com/license/">licence Pexels</a>, et tiennent la place des vraies photos qu’une marque fournirait : son équipe, ses clients, ses réalisations. Les personnes photographiées n’ont aucun lien avec les personnages ni avec les marques des démos.</p>
__BLOCS__
</main>
</body>
</html>
"""
    sortie = DOCS / CREDITS / "index.html"
    sortie.parent.mkdir(parents=True, exist_ok=True)
    sortie.write_text(gabarit.replace("__BLOCS__", "\n".join(blocs)), encoding="utf-8")
    print("écrit :", sortie.relative_to(RACINE))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--travail", help="dossier des projets d'essai (défaut : dossier temporaire supprimé à la fin)")
    args = ap.parse_args()
    if args.travail:
        travail = Path(args.travail).resolve()
        travail.mkdir(parents=True, exist_ok=True)
        tmp = None
    else:
        tmp = tempfile.TemporaryDirectory(prefix="atelier-demos-")
        travail = Path(tmp.name)
    try:
        for m in MARQUES:
            construire_marque(travail, *m)
        construire_catalogue(travail)
        page_credits()
    finally:
        if tmp:
            tmp.cleanup()


if __name__ == "__main__":
    main()
