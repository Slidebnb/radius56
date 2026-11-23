# Radius56 – Website

Lokale News für Neuwied, Koblenz & 30 km drumherum. Gebaut mit [Astro](https://astro.build), komplett statisch.

## Neuen Beitrag anlegen

Eine neue Datei in `src/content/posts/` anlegen, z. B. `2026-11-24-titel.md`:

```md
---
title: "Überschrift"
date: "2026-11-24T07:00:00+01:00"
ort: "Neuwied"
kategorie: "news"        # news | events | blaulicht | geld-alltag | mitmachen | immo
teaser: "Ein Satz, der neugierig macht."
quelle: "Polizeipräsidium Koblenz"
quelleUrl: "https://www.presseportal.de/..."
kachelText: "Großes Wort"
kachelSub: "Kleine Zeile darunter"
kachelFarbe: "navy"      # navy | blau
---

Text des Beitrags.
```

## Lokal starten

```bash
npm install
npm run dev
```

## Veröffentlichen

Jeder Push auf `main` baut die Seite und veröffentlicht sie über GitHub Pages
(Einstellungen › Pages › Source: „GitHub Actions“). Die Domain steht in `public/CNAME`.

## Vor dem Livegang

- Impressum (`src/pages/impressum.astro`) und Datenschutz ausfüllen
- E-Mail-Adressen redaktion@ und werbung@radius56.de einrichten
- Preise und Reichweite auf `src/pages/werben.astro` eintragen
