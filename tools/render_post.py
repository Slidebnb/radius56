#!/usr/bin/env python3
"""Rendert ein Radius56-Instagram-Bild (Feed 1080x1350 oder Story 1080x1920).

Aufruf:
    python3 tools/render_post.py post.json

post.json:
{
  "slug": "2026-11-24-brueckensperrung",
  "ort": "Neuwied",
  "kategorie": "Verkehr",
  "titel": "Raiffeisenbrücke ab Montag nachts gesperrt",
  "kachelText": "Gesperrt",
  "kachelSub": "Raiffeisenbrücke, nachts",
  "farbe": "navy",            # navy | blau | orange (orange nur für Blaulicht)
  "footer": "Alle Infos in der Caption →",
  "format": "feed"            # feed | story
}

Ergebnis: public/social/<slug>.png bzw. public/social/<slug>-story.png
Voraussetzung: npm install (für die Schriften) und Playwright mit Chrome.
"""
import html
import json
import pathlib
import sys

from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "tools" / "post_template.html"
OUT_DIR = ROOT / "public" / "social"

FARBEN = {"navy": "#0F172A", "blau": "#1D4ED8", "orange": "#C2410C"}
TEXTFARBE = {"navy": "#F97316", "blau": "#FFFFFF", "orange": "#FFFFFF"}


def chrome_path():
    for p in ["/usr/bin/google-chrome", "/usr/bin/chromium", "/usr/bin/chromium-browser"]:
        if pathlib.Path(p).exists():
            return p
    return None


def main():
    data = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    fmt = data.get("format", "feed")
    farbe = data.get("farbe", "navy")
    width, height = (1080, 1920) if fmt == "story" else (1080, 1350)
    top_h = 1170 if fmt == "story" else 820

    werte = {
        "FONT_DIR": (ROOT / "node_modules" / "@fontsource" / "archivo" / "files").as_uri(),
        "W": str(width),
        "H": str(height),
        "TOP_H": str(top_h),
        "BG": FARBEN.get(farbe, FARBEN["navy"]),
        "KACHEL_FARBE": TEXTFARBE.get(farbe, "#FFFFFF"),
        "KACHEL_TEXT": html.escape(data["kachelText"]),
        "KACHEL_SUB": html.escape(data.get("kachelSub", "")),
        "ORT": html.escape(data["ort"]),
        "KATEGORIE": html.escape(data["kategorie"]),
        "TITEL": html.escape(data["titel"]),
        "FOOTER": html.escape(data.get("footer", "Alle Infos in der Caption →")),
    }
    seite = TEMPLATE.read_text(encoding="utf-8")
    for k, v in werte.items():
        seite = seite.replace("{{" + k + "}}", v)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    tmp = ROOT / "tools" / ".render.html"
    tmp.write_text(seite, encoding="utf-8")
    name = f"{data['slug']}-story.png" if fmt == "story" else f"{data['slug']}.png"
    ziel = OUT_DIR / name

    with sync_playwright() as p:
        kwargs = {"args": ["--no-sandbox", "--allow-file-access-from-files"]}
        if chrome_path():
            kwargs["executable_path"] = chrome_path()
        browser = p.chromium.launch(**kwargs)
        page = browser.new_page(viewport={"width": width, "height": height})
        page.goto(tmp.as_uri())
        page.wait_for_timeout(700)
        # Überschrift automatisch verkleinern, falls sie zu lang ist
        page.evaluate("""() => {
          const h = document.querySelector('h2');
          let s = parseFloat(getComputedStyle(h).fontSize);
          while (h.scrollHeight > s * 1.1 * 3 + 4 && s > 40) { s -= 2; h.style.fontSize = s + 'px'; }
          const k = document.querySelector('.ktext');
          let ks = parseFloat(getComputedStyle(k).fontSize);
          while (k.scrollWidth > k.parentElement.clientWidth - 80 && ks > 60) { ks -= 4; k.style.fontSize = ks + 'px'; }
        }""")
        page.locator("#post").screenshot(path=str(ziel))
        browser.close()
    tmp.unlink(missing_ok=True)
    print(ziel.relative_to(ROOT))


if __name__ == "__main__":
    main()
