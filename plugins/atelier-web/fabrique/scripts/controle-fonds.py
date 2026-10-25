#!/usr/bin/env python3
"""
Contrôle de la continuité des fonds d'une page : aucune coupure de couleur entre deux sections.

Une page soignée enchaîne ses fonds : chaque section finit sur la couleur où commence la
suivante, souvent par un dégradé. Ce script charge la page dans Chromium, liste les sections
avec leur fond calculé, puis cherche dans les deux marges latérales les changements de couleur
nets ET durables : la moyenne des 10 lignes au-dessus comparée aux 10 lignes au-dessous, chaque
fenêtre restant homogène, en hauteur comme en largeur. Un dégradé ne déclenche rien ; une coupure
entre deux sections, si. Une photo ou une carte qui touche le bord de l'écran n'est pas homogène
en largeur : elle est ignorée. Seuls les sauts situés à moins de 40 px d'une limite de section
sont retenus (--tout : tous les sauts).

Les éléments en position fixed ou sticky (barre de navigation, bandeau cookies, bouton flottant)
faussent les marges : ils sont masqués le temps de la mesure. --masquer en ajoute d'autres.

Usage (la page servie en local, par exemple python3 -m http.server --directory dist 8093) :
    python3 controle-fonds.py http://localhost:8093/ma-page/
    python3 controle-fonds.py <url> 390                      (largeur de fenêtre, 1440 par défaut)
    python3 controle-fonds.py <url> 1440 --tout              (aussi les sauts dans les sections)
    python3 controle-fonds.py <url> --sections "main > section, footer"
    python3 controle-fonds.py <url> --masquer ".promo-bar,#chat"

Sortie : la liste des sections, puis les coupures trouvées (0 attendu). Code de retour 1 s'il y en a,
2 si l'appel est fautif. Le script ne fait que lire la page : il n'écrit aucun fichier.
Dépendances : playwright (pip install playwright && playwright install chromium) et Pillow.
"""

import argparse
import asyncio
import io
import sys

SEUIL, HOMOGENE, FENETRE = 2.5, 1.6, 10


def lire_arguments():
    p = argparse.ArgumentParser(description="Contrôle de la continuité des fonds d'une page.")
    p.add_argument("url")
    p.add_argument("largeur", nargs="?", type=int, default=1440)
    p.add_argument("--tout", action="store_true", help="signaler aussi les sauts à l'intérieur des sections")
    p.add_argument("--sections", default="main > *, body > footer",
                   help="sélecteur des sections (défaut : « main > *, body > footer »)")
    p.add_argument("--masquer", default="", help="sélecteurs supplémentaires à masquer, séparés par des virgules")
    return p.parse_args()


async def mesurer(args):
    from PIL import Image
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        nav = await p.chromium.launch()
        page = await (await nav.new_context(viewport={"width": args.largeur, "height": 900})).new_page()
        await page.goto(args.url, wait_until="networkidle")
        # défilement natif et instantané : un défilement fluide rend scrollTo asynchrone
        await page.add_style_tag(content="html{scroll-behavior:auto!important}")
        hauteur, y = await page.evaluate("document.documentElement.scrollHeight"), 0
        while y < hauteur:  # descente lente : les apparitions au défilement se déclenchent
            await page.evaluate(f"window.scrollTo({{top:{y},behavior:'instant'}})")
            await page.wait_for_timeout(100)
            y += 700
            hauteur = await page.evaluate("document.documentElement.scrollHeight")
        await page.wait_for_timeout(1500)
        # les éléments fixes ou collants faussent les marges : masqués le temps de la mesure
        await page.evaluate("""(extra) => {
            for (const e of document.querySelectorAll('body *')) {
                const pos = getComputedStyle(e).position;
                if (pos === 'fixed' || pos === 'sticky') e.style.setProperty('visibility', 'hidden', 'important');
            }
            if (extra) for (const e of document.querySelectorAll(extra)) e.style.setProperty('visibility', 'hidden', 'important');
        }""", args.masquer)
        sections = await page.evaluate("""(sel) => [...document.querySelectorAll(sel)].map(e => {
            const r = e.getBoundingClientRect(), cs = getComputedStyle(e);
            return {nom: e.tagName.toLowerCase() + '.' + (e.className || '').toString().split(' ').slice(0, 2).join('.') + (e.id ? '#' + e.id : ''),
                    haut: Math.round(r.top + scrollY), bas: Math.round(r.bottom + scrollY),
                    fond: (cs.backgroundImage !== 'none' ? cs.backgroundImage : cs.backgroundColor).slice(0, 100)}; })
            .filter(s => s.bas - s.haut > 4)""", args.sections)
        hauteur = await page.evaluate("document.documentElement.scrollHeight")
        await page.evaluate("window.scrollTo({top:0,behavior:'instant'})")
        await page.wait_for_timeout(300)
        gauche, droite = [], []
        L = args.largeur
        # par tranches de 4 000 px : Chromium plafonne une capture pleine page à 16 384 px
        for y0 in range(0, hauteur, 4000):
            png = await page.screenshot(full_page=True, clip={"x": 0, "y": y0, "width": L, "height": min(4000, hauteur - y0)})
            im = Image.open(io.BytesIO(png)).convert("RGB")
            for ligne in range(im.size[1]):
                for x0, x1, acc in ((2, 10, gauche), (L - 10, L - 2, droite)):
                    px = [im.getpixel((x, ligne)) for x in range(x0, x1, 2)]
                    m = tuple(sum(c[i] for c in px) / len(px) for i in range(3))
                    acc.append(m + (max(max(abs(c[i] - m[i]) for i in range(3)) for c in px),))
        await nav.close()
    return sections, gauche, droite


def coupures(colonne):
    def fenetre(a, b):
        lignes = colonne[a:b]
        m = tuple(sum(r[i] for r in lignes) / len(lignes) for i in range(3))
        en_largeur = max(r[3] for r in lignes)
        return m, max(en_largeur, max(max(abs(r[i] - m[i]) for i in range(3)) for r in lignes))
    trouvees, y = [], FENETRE + 2
    while y < len(colonne) - FENETRE - 2:
        (m1, d1), (m2, d2) = fenetre(y - FENETRE - 1, y - 1), fenetre(y + 1, y + FENETRE + 1)
        ecart = max(abs(m1[i] - m2[i]) for i in range(3))
        if ecart >= SEUIL and d1 < HOMOGENE and d2 < HOMOGENE:
            trouvees.append((y, round(ecart, 1), tuple(round(v) for v in m1), tuple(round(v) for v in m2)))
            y += FENETRE + 2
        else:
            y += 1
    return trouvees


def main():
    args = lire_arguments()
    try:
        sections, gauche, droite = asyncio.run(mesurer(args))
    except ImportError as err:
        print(f"ERREUR : dépendance absente ({err}). pip install playwright pillow && playwright install chromium", file=sys.stderr)
        sys.exit(2)
    print(f"{args.url} en {args.largeur} px\n\nSections :")
    for s in sections:
        print(f"  {s['haut']:>6} à {s['bas']:<6} {s['nom']:<48} {s['fond']}")
    limites = [s["haut"] for s in sections] or [0]
    total = 0
    for cote, colonne in (("gauche", gauche), ("droite", droite)):
        for y, ecart, avant, apres in coupures(colonne):
            if not args.tout and min(abs(y - l) for l in limites) > 40:
                continue
            total += 1
            print(f"  coupure marge {cote} à y = {y} : écart {ecart}, {avant} puis {apres}")
    print(f"\n{total} coupure(s) de fond." if total else "\nAucune coupure : les fonds s'enchaînent.")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
