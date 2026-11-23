# Radius56 – Ablauf der stündlichen News-Prüfung

Gebiet: rund 30 km um Neuwied (Neuwied, Koblenz, Andernach, Bendorf, Vallendar, Lahnstein,
Linz, Bad Hönningen, Dierdorf, Montabaur, Mayen-Koblenz). Instagram: @radius56.de über Buffer.

## Quellen

**Frei verwendbar (mit Quellenangabe):**
- Polizeipräsidium Koblenz auf presseportal.de (PI Neuwied, Koblenz, Andernach, Mayen, Montabaur, Linz)
- Feuerwehren der Region auf presseportal.de
- Pressemitteilungen: Stadt Neuwied, Stadt Koblenz, Andernach, Bendorf, Kreis Neuwied,
  Kreis Mayen-Koblenz, Westerwaldkreis, Verbandsgemeinden
- Stadtwerke Neuwied, Koblenzer Verkehrsbetriebe (koveb)
- Landesbetrieb Mobilität (Sperrungen, Baustellen), Deutscher Wetterdienst (Unwetterwarnungen)
- Veranstaltungskalender der Städte, Koblenz-Touristik, Rhein-Mosel-Halle

**Nur Fakten, immer komplett neu formuliert, nie Text oder Fotos übernehmen:**
- NR-Kurier, WW-Kurier, News-Koblenz, Lebendiges Neuwied, Blick aktuell
- Rhein-Zeitung und Merkurist: höchstens zur Bestätigung von Fakten

## Regeln

1. Nur Meldungen aus dem Gebiet, nicht älter als 24 Stunden (Termine: kommende 7 Tage).
2. Keine Doppelten: jede Meldung bekommt eine `id`, abgleichen mit `data/posted.json`.
3. **Feed:** maximal 4 Posts pro Kalendertag (Zähler `feedCount`), mindestens 2 Stunden Abstand.
   Wichtigste Meldungen in den Feed (Sperrungen, große Einsätze, Service-Infos, Events).
4. **Story:** alles Weitere, das relevant ist (kleinere Polizeimeldungen, Termine, Hinweise).
5. Keine Namen, Kennzeichen, Hausnummern oder Fotos von Betroffenen. Bei Unfällen keine
   Spekulation über Schuld. Bei Vermisstenfahndungen nur aktive Fahndungen der Polizei, mit Link.
6. Kein Material von Bildagenturen oder fremden Instagram-Accounts. Grafiken nur über
   `tools/render_post.py` erzeugen.
7. Caption: kurze Meldung in eigenen Worten, Quelle nennen („Quelle: Polizeipräsidium Koblenz“),
   3–5 Hashtags, immer `#radius56`. Ohne Gewähr bei Terminen.
8. Im Zweifel nicht posten.

## Technik

```bash
npm ci                                   # Schriften für die Grafik
python3 tools/render_post.py post.json   # erzeugt public/social/<slug>.png (feed) oder <slug>-story.png
git add public/social data/posted.json && git commit && git push   # Bild wird öffentlich
```

Bild-URL für Buffer: `https://raw.githubusercontent.com/Slidebnb/radius56/main/public/social/<datei>.png`

Buffer: Organisation „My organization“, Kanal „radius56.de“ (Instagram, Business).
Feed: `metadata.instagram.type = "post"`, Story: `type = "story"`, `shouldShareToFeed: true`,
`schedulingType: "automatic"`, `mode: "shareNow"` (Feed nur, wenn kein anderer Feed-Post in den
letzten 2 Stunden; sonst `customScheduled` auf die nächste freie Lücke).
