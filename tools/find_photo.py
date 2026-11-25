#!/usr/bin/env python3
"""Sucht lizenzfreie Fotos (Wikimedia Commons, Fallback Openverse/Flickr) und lädt eins herunter.

Schritt 1 – Kandidaten suchen (erzeugt eine Kontaktbogen-Vorschau zum Ansehen):
    python3 tools/find_photo.py search "potatoes tubers" [--limit 12]
    -> listet Kandidaten (nur erlaubte Lizenzen, nur Fotos >= 1000 px)
    -> speichert tools/.photo_candidates.json und tools/.photo_sheet.jpg
       (Vorschau mit Nummern; mit dem Read-Tool ansehen und Motiv prüfen!)

Schritt 2 – Kandidat übernehmen:
    python3 tools/find_photo.py pick 3 kartoffeln-knollen
    -> lädt Nr. 3 als public/social/fotos/kartoffeln-knollen.jpg (max. 2000 px)
    -> gibt JSON mit "bild", "bildCredit" (für post.json) und "foto" (für posted.json) aus

Erlaubt: CC0, Public Domain, CC BY, CC BY-SA. Alles mit NC/ND oder unklarer Lizenz fliegt raus.
Tipp: englische Suchbegriffe liefern auf Commons deutlich mehr Treffer.
"""
import html
import io
import json
import pathlib
import re
import sys
import time
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
CAND = ROOT / "tools" / ".photo_candidates.json"
SHEET = ROOT / "tools" / ".photo_sheet.jpg"
FOTOS = ROOT / "public" / "social" / "fotos"
API = "https://commons.wikimedia.org/w/api.php"
UA = "radius56-bot/1.0 (https://radius56.de; github.com/Slidebnb/radius56)"
ERLAUBT = re.compile(r"^(cc0|public domain|pd|cc by(-sa)? \d(\.\d)?( [a-z]+)?|cc by(-sa)?)$", re.I)


def get(url, tries=4):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read()
        except Exception as e:  # Rate-Limit (429) oder kurzer Netzfehler
            if i == tries - 1:
                raise
            wait = 5 * (i + 1)
            ra = getattr(e, "headers", None) and e.headers.get("Retry-After")
            if ra and ra.isdigit():
                wait = min(int(ra), 30)
            print(f"  ({e}) – neuer Versuch in {wait} s", file=sys.stderr)
            time.sleep(wait)


def plain(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def search(query, limit=12):
    try:
        out = search_commons(query, limit)
    except Exception as e:
        print(f"Commons nicht erreichbar ({e}) – nehme Openverse.", file=sys.stderr)
        out = []
    if len(out) < 4:
        try:
            out += search_openverse(query, limit - len(out), start=len(out))
        except Exception as e:
            print(f"Openverse nicht erreichbar ({e}).", file=sys.stderr)
    CAND.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    for c in out:
        print(f'{c["nr"]:>2}. [{c["quelle"]}] {c["titel"]} | {c["lizenz"]} | {c["urheber"]} | {c["groesse"]}')
    if not out:
        print("Keine passenden Treffer – anderen (englischen) Suchbegriff probieren oder Higgsfield-Symbolbild.")
        return
    contact_sheet(out)
    print(f"\nVorschau: {SHEET.relative_to(ROOT)} – ansehen und Motiv prüfen, dann: find_photo.py pick <nr> <name>")


OV_LIZ = {"cc0": "CC0", "pdm": "Public Domain", "by": "CC BY", "by-sa": "CC BY-SA"}


def search_openverse(query, limit, start=0):
    """Fallback: Openverse (Flickr, Commons u. a.), nur CC0/PD/BY/BY-SA."""
    params = {"q": query, "license": ",".join(OV_LIZ), "page_size": 30, "mature": "false",
              "extension": "jpg"}
    data = json.loads(get("https://api.openverse.org/v1/images/?" + urllib.parse.urlencode(params)))
    out = []
    for r in data.get("results", []):
        if min(r.get("width") or 0, r.get("height") or 0) < 1000 or r.get("license") not in OV_LIZ:
            continue
        lic = OV_LIZ[r["license"]] + (f' {r["license_version"]}' if r["license"] in ("by", "by-sa") else "")
        out.append({
            "nr": start + len(out) + 1, "quelle": r.get("source", "openverse"),
            "titel": (r.get("title") or "ohne Titel")[:60], "lizenz": lic,
            "urheber": (r.get("creator") or "unbekannt")[:80], "seite": r["foreign_landing_url"],
            "thumb": r["thumbnail"], "download": r["url"], "groesse": f'{r["width"]}x{r["height"]}',
        })
        if len(out) >= limit:
            break
    return out


def search_commons(query, limit=12):
    params = {
        "action": "query", "format": "json", "generator": "search", "gsrnamespace": 6,
        "gsrsearch": f"{query} filetype:bitmap", "gsrlimit": 40, "prop": "imageinfo",
        "iiprop": "url|extmetadata|size|mime", "iiurlwidth": 330,  # Wikimedia-Standardgröße (w.wiki/GHai)
    }
    data = json.loads(get(API + "?" + urllib.parse.urlencode(params)))
    pages = sorted(data.get("query", {}).get("pages", {}).values(), key=lambda p: p.get("index", 0))
    out = []
    for p in pages:
        ii = p["imageinfo"][0]
        m = ii.get("extmetadata", {})
        lic = plain(m.get("LicenseShortName", {}).get("value"))
        if ii.get("mime") != "image/jpeg" or not ERLAUBT.match(lic):
            continue
        if min(ii["width"], ii["height"]) < 1000:
            continue
        titel = p["title"].removeprefix("File:")
        out.append({
            "nr": len(out) + 1, "quelle": "commons",
            "titel": titel,
            # Standard-Thumbnail 1920 px statt Originaldatei (vermeidet 429-Sperren)
            "download": ii["thumburl"].replace("/330px-", "/1920px-") if ii["width"] > 1920
            else ii["url"],
            "lizenz": lic,
            "urheber": plain(m.get("Artist", {}).get("value"))[:80] or "unbekannt",
            "seite": ii["descriptionurl"],
            "thumb": ii["thumburl"],
            "groesse": f'{ii["width"]}x{ii["height"]}',
        })
        if len(out) >= limit:
            break
    return out


def contact_sheet(cands):
    from PIL import Image, ImageDraw, ImageFont
    tw, th, cols = 300, 225, 4
    rows = (len(cands) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tw, rows * th), "white")
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    except OSError:
        font = ImageFont.load_default()
    for i, c in enumerate(cands):
        try:
            im = Image.open(io.BytesIO(get(c["thumb"]))).convert("RGB")
        except Exception:
            continue
        im.thumbnail((tw, th))
        x, y = (i % cols) * tw, (i // cols) * th
        sheet.paste(im, (x + (tw - im.width) // 2, y + (th - im.height) // 2))
        d = ImageDraw.Draw(sheet)
        d.rectangle([x, y, x + 56, y + 46], fill="black")
        d.text((x + 8, y + 2), str(c["nr"]), fill="white", font=font)
    sheet.save(SHEET, quality=80)


QNAME = {"commons": "Wikimedia Commons", "wikimedia": "Wikimedia Commons", "flickr": "Flickr"}


def pick(nr, name):
    from PIL import Image
    cands = json.loads(CAND.read_text(encoding="utf-8"))
    c = next(x for x in cands if x["nr"] == int(nr))
    im = Image.open(io.BytesIO(get(c["download"]))).convert("RGB")
    im.thumbnail((2000, 2000))
    FOTOS.mkdir(parents=True, exist_ok=True)
    ziel = FOTOS / f"{name}.jpg"
    im.save(ziel, quality=85)
    rel = str(ziel.relative_to(ROOT))
    print(json.dumps({
        "bild": rel,
        "bildCredit": f'Foto: {c["urheber"]}, {c["lizenz"]}, {QNAME.get(c["quelle"], c["quelle"])}',
        "foto": {"datei": rel, "urheber": c["urheber"], "lizenz": c["lizenz"], "url": c["seite"]},
        "captionHinweis": None if c["lizenz"].lower().startswith(("cc0", "public", "pd"))
        else f'Foto: {c["urheber"]} / {c["lizenz"]} via {QNAME.get(c["quelle"], c["quelle"])}',
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "search":
        lim = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else 12
        search(sys.argv[2], lim)
    elif len(sys.argv) == 4 and sys.argv[1] == "pick":
        pick(sys.argv[2], sys.argv[3])
    else:
        sys.exit(__doc__)
