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

## Wachstum (Follower gewinnen) – gilt für jeden Lauf

Ziel in der Startphase: Community aufbauen, nicht Geld verdienen. Deshalb:

1. **Interaktion vor Menge:** Jede Feed-Caption endet mit einer konkreten Frage an die Leser
   („Wart ihr schon da?“, „Was meint ihr?“) oder einer Bitte zum Teilen/Markieren
   („Markiere jemanden aus Neuwied, der das wissen muss“).
2. **Feste Formate (zusätzlich zu den News, zählen zum Feed-Limit von 4):**
   - **Montag, ca. 18 Uhr – Frage der Woche:** eine lokale Frage, bei der jeder mitreden kann
     (z. B. „Bester Döner in Neuwied?“, „Schönster Weihnachtsmarkt im Umkreis?“).
     Kachel: farbe "blau", Kachel-Text „Frage der Woche“. Antworten werden im Rückblick aufgegriffen.
   - **Freitag, ca. 7 Uhr – Dein Wochenende:** 4–6 Termine fürs Wochenende im Umkreis.
   - **Sonntag, ca. 19 Uhr – Wochenrückblick:** die 3–5 wichtigsten Meldungen der Woche,
     dazu die beliebteste Antwort auf die Frage der Woche (ohne Nachnamen).
   Vor dem Anlegen eines festen Formats in data/posted.json prüfen, ob es diese Woche schon lief
   (id z. B. `frage-der-woche-2026-w48`).
3. **Story-Hinweis auf neue Feed-Posts:** Nach jedem Feed-Post zusätzlich eine Story mit derselben
   Grafik im Story-Format (format "story"), damit auch Story-Gucker den Post finden.
4. **Lokale Hashtags:** immer 1–2 Ortshashtags (#neuwied, #koblenz, #andernach, #bendorf …)
   plus #radius56; keine generischen Massen-Hashtags.
5. **Folgen-Aufforderung sparsam:** höchstens einmal pro Tag „Folg @radius56.de für alles aus
   deinem Umkreis“ am Ende einer Caption.
6. **Nachtruhe:** zwischen 22 und 6 Uhr nichts veröffentlichen.
