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
   **Themen sind bewusst breit (Entscheidung Wladi, 24.11.2026):** neben Blaulicht alles, was
   für Leute im Umkreis nützlich oder interessant ist und bald ansteht: Weihnachtsmärkte, Feste,
   Märkte, Konzerte, Eröffnungen/Schließungen, Baustellen, Fahrplan- und Müllabfuhr-Änderungen,
   Öffnungszeiten an Feiertagen, Stadtrat-Beschlüsse, Fristen (Anträge, Anmeldungen), Vereine,
   Sport, Wetter, Service-Tipps. Wenn es keine frische Eilmeldung gibt, aktiv nach solchen
   allgemeinen Themen der kommenden Tage suchen und daraus posten.
2. Keine Doppelten: jede Meldung bekommt eine `id`, abgleichen mit `data/posted.json`.
3. **Feed UND Story, kein Limit (Entscheidung Wladi, 24.11.2026, ersetzt das frühere 4er-Limit):**
   Jede geeignete Meldung wird IMMER zweimal veröffentlicht – als Feed-Beitrag (format "feed")
   und als Story (format "story"). Keine Obergrenze pro Tag; `feedCount` wird nur noch gezählt,
   nicht begrenzt. **Sofort veröffentlichen, nichts einplanen:** alles direkt mit `shareNow`.
4. In `data/posted.json` pro Meldung ein Eintrag mit `"format": "feed+story"`.
5. Keine Namen, Kennzeichen, Hausnummern oder Fotos von Betroffenen. Bei Unfällen keine
   Spekulation über Schuld. Bei Vermisstenfahndungen nur aktive Fahndungen der Polizei, mit Link.
6. Kein Material von Bildagenturen, Zeitungen, Polizei-/Feuerwehr-/Pressefotos oder fremden
   Instagram-Accounts. Grafiken immer über `tools/render_post.py` erzeugen – optional mit einem
   lizenzfreien Hintergrundfoto (siehe „Lizenzfreie Fotos“).
7. Caption: kurze Meldung in eigenen Worten, Quelle nennen („Quelle: Polizeipräsidium Koblenz“),
   3–5 Hashtags, immer `#radius56`. Ohne Gewähr bei Terminen.
8. Im Zweifel nicht posten.

## Lizenzfreie Fotos (Entscheidung Wladi, 24.11.2026)

Bei jedem Post kurz recherchieren, ob es ein passendes, sauber lizenziertes Foto gibt. Wenn ja,
als Hintergrund der Kachel nutzen; wenn nein, normale Kachel ohne Foto (kein Zwang).

- **Quellen:** zuerst Wikimedia Commons (commons.wikimedia.org), dann Unsplash oder Pexels.
- **Erlaubte Lizenzen:** CC0 / Public Domain, CC BY, CC BY-SA (Commons), Unsplash-/Pexels-Lizenz.
  Nicht erlaubt: CC …-NC, CC …-ND, „alle Rechte vorbehalten“, unklare Lizenz.
  Die Lizenz auf der Dateiseite selbst prüfen (bei Commons: Abschnitt „Lizenz“), nicht raten.
- **Motive:** Orte, Gebäude, Brücken, Straßen, Landschaft, Symbolbilder (z. B. Weihnachtsmarkt,
  Baustellenschild). Niemals: Unfälle, Brände, Einsätze, erkennbare Personen, Kennzeichen,
  Wohnhäuser von Betroffenen. Bei Blaulicht-Meldungen höchstens ein neutrales Ortsbild – im
  Zweifel ohne Foto.
- **Ablage:** Datei nach `public/social/fotos/<sprechender-name>.jpg` (max. ~2000 px Breite,
  ggf. verkleinern), damit Herkunft nachvollziehbar bleibt. Bereits abgelegte Fotos wiederverwenden.
- **post.json:** `"bild": "public/social/fotos/<datei>.jpg"`, `"bildCredit": "Foto: <Urheber>,
  <Lizenz>, <Quelle>"` (Pflicht – der Renderer bricht ohne ab), optional
  `"bildPosition": "center top"`. Der Credit steht klein unten links im Bild.
- **Caption:** bei CC BY / CC BY-SA zusätzlich „Foto: <Urheber> / <Lizenz> via Wikimedia Commons“.
- **posted.json:** beim Eintrag `"foto": {"datei", "urheber", "lizenz", "url"}` ergänzen.
- Bild nach dem Rendern ansehen: Text muss gut lesbar sein, Foto darf nichts Sensibles zeigen.

## Technik

```bash
npm ci                                   # Schriften für die Grafik
python3 tools/render_post.py post.json   # erzeugt public/social/<slug>.png (feed) oder <slug>-story.png
git add public/social data/posted.json && git commit && git push   # Bild wird öffentlich
```

Bild-URL für Buffer: `https://raw.githubusercontent.com/Slidebnb/radius56/main/public/social/<datei>.png`

Buffer: Organisation „My organization“, Kanal „radius56.de“ (Instagram, Business).
Feed: `metadata.instagram.type = "post"`, Story: `type = "story"`, `shouldShareToFeed: true`,
`schedulingType: "automatic"`, `mode: "shareNow"` für Feed und Story – kein `customScheduled`.

## Wachstum (Follower gewinnen) – gilt für jeden Lauf

Ziel in der Startphase: Community aufbauen, nicht Geld verdienen. Deshalb:

1. **Interaktion vor Menge:** Jede Feed-Caption endet mit einer konkreten Frage an die Leser
   („Wart ihr schon da?“, „Was meint ihr?“) oder einer Bitte zum Teilen/Markieren
   („Markiere jemanden aus Neuwied, der das wissen muss“).
2. **Feste Formate (zusätzlich zu den News):**
   - **Montag, ca. 18 Uhr – Frage der Woche:** eine lokale Frage, bei der jeder mitreden kann
     (z. B. „Bester Döner in Neuwied?“, „Schönster Weihnachtsmarkt im Umkreis?“).
     Kachel: farbe "blau", Kachel-Text „Frage der Woche“. Antworten werden im Rückblick aufgegriffen.
   - **Freitag, ca. 7 Uhr – Dein Wochenende:** 4–6 Termine fürs Wochenende im Umkreis.
   - **Sonntag, ca. 19 Uhr – Wochenrückblick:** die 3–5 wichtigsten Meldungen der Woche,
     dazu die beliebteste Antwort auf die Frage der Woche (ohne Nachnamen).
   Vor dem Anlegen eines festen Formats in data/posted.json prüfen, ob es diese Woche schon lief
   (id z. B. `frage-der-woche-2026-w48`).
3. **Feed + Story immer zusammen:** Zu jedem Feed-Post dieselbe Meldung als Story (format "story")
   und umgekehrt – siehe Regel 3 oben.
4. **Lokale Hashtags:** immer 1–2 Ortshashtags (#neuwied, #koblenz, #andernach, #bendorf …)
   plus #radius56; keine generischen Massen-Hashtags.
5. **Folgen-Aufforderung sparsam:** höchstens einmal pro Tag „Folg @radius56.de für alles aus
   deinem Umkreis“ am Ende einer Caption.
6. **Nachtruhe:** zwischen 22 und 6 Uhr nichts veröffentlichen.
