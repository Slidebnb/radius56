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

**Geprüfte, lesbare Direkt-URLs (Stand 25.11.2026) – bei jedem Lauf abklappern:**
- Polizei: presseportal.de/blaulicht/nr/117712 (PD Koblenz), /nr/117715 (PP Koblenz),
  /nr/117709 (PD Neuwied), presseportal.de/regional/Neuwied, /blaulicht/r/Montabaur
- Städte/Kreise: neuwied.de/aktuelles, koblenz.de (Startseite „Aktuelles“), andernach.de,
  bendorf.de, kreis-neuwied.de, westerwaldkreis.de
- Verkehr: lbm.rlp.de (Presse/Aktuelles), koveb.de (Verkehrs-Infos)
- Nur Fakten (neu formulieren): news-koblenz.de, nr-kurier.de, ww-kurier.de, ak-kurier.de,
  lebendiges-neuwied.de, blick-aktuell.de, antenne-koblenz.de
- Nicht direkt lesbar: kreis-myk.de, stadtwerke-neuwied.de, dwd.de (dann per Websuche bzw.
  über Berichte prüfen)

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
- **Pflicht, nicht optional:** Die Fotosuche wird bei JEDEM Post wirklich durchgeführt.
  Motiv muss zur Meldung passen (z. B. bei Kartoffel-Rückruf Knollen, nicht Blüten oder Acker).

## Bilder mit Higgsfield (Entscheidung Wladi, 25.11.2026)

Ziel: möglichst jeder Post mit Bild. Reihenfolge:

1. Passendes lizenzfreies Foto suchen (siehe oben). Das Foto darf mit Higgsfield bearbeitet
   werden (z. B. Zuschnitt, Look, Hintergrund erweitern), Credit bleibt Pflicht
   („Foto: <Urheber>, <Lizenz>, bearbeitet“). Bei CC BY-SA Bearbeitung in der Caption nennen.
2. Gibt es kein passendes freies Foto: mit Higgsfield (`generate_image`) ein **neutrales
   Symbolbild** erzeugen, z. B. Kartoffeln, Glühweintasse, Baustellenschild, Rheinufer
   allgemein. Nach `public/social/fotos/ki-<name>.jpg` speichern, `bildCredit`:
   „Symbolbild (KI)“.
3. Niemals: Fotos oder Bilder ohne freie Lizenz als Vorlage (auch nicht „verändert“ –
   eine Bearbeitung macht ein geschütztes Bild nicht frei), KI-Bilder von echten Personen,
   Unfällen, Bränden, Einsätzen, Tatorten oder erkennbaren echten Gebäuden/Orten, die
   eine echte Situation vortäuschen.
4. KI-Bilder: in Buffer `metadata.instagram.isAiGenerated: true` setzen und Credit
   „Symbolbild (KI)“ im Bild – Meta verlangt die Kennzeichnung fotorealistischer KI-Bilder,
   und ein Nachrichtenkanal darf keine KI-Bilder als echte Fotos ausgeben.
5. Higgsfield-Credits sparsam: pro Meldung ein Bild, für Feed und Story wiederverwenden.

### Bild-Ablauf Schritt für Schritt (gilt für jeden Post)

1. **Erst schauen, ob es schon passt:** `ls public/social/fotos/` – vorhandene Fotos wiederverwenden.
2. **Foto suchen** (englische Begriffe, konkret: „red potatoes“, „christmas market night“,
   „road closed sign“, „Koblenz Deutsches Eck“):
   ```bash
   python3 tools/find_photo.py search "red potatoes"
   ```
   Durchsucht Commons (Fallback Openverse/Flickr), filtert NC/ND/unklare Lizenzen und Bilder
   unter 1000 px raus und erzeugt `tools/.photo_sheet.jpg` mit nummerierten Vorschaubildern.
   **Den Kontaktbogen mit dem Read-Tool ansehen** und nur ein Motiv nehmen, das wirklich zur
   Meldung passt (keine Personen, Kennzeichen, Unfälle). Ggf. 1–2 andere Suchbegriffe probieren.
3. **Übernehmen:** `python3 tools/find_photo.py pick <nr> <sprechender-name>` – lädt das Bild
   (1920-px-Standardgröße, vermeidet Wikimedia-Sperren) und gibt `bild`, `bildCredit`,
   `foto` (für posted.json) und ggf. den Caption-Hinweis aus. Bei HTTP 429 kurz warten,
   das Skript versucht es selbst erneut.
4. **Kein passendes Foto → Higgsfield:** `generate_image` mit `model: "gpt_image_2_6"`,
   `aspect_ratio: "4:5"`, `use_unlim: false` (ca. 0,75 Credits). Prompt-Vorlage:
   „Neutral editorial stock photo: <Motiv>, soft natural light, subject in the lower/right
   part of the frame, calm dark negative space in the upper center for text overlay.
   No people, no hands, no text, no logos, no brand packaging, no license plates.“
   Dann `jobs_wait` bis `completed`, `result_url` per curl laden, mit PIL als
   `public/social/fotos/ki-<name>.jpg` speichern (JPEG, Qualität 85) und in post.json
   `"bild": "...", "ki": true` setzen (Credit „Symbolbild (KI)“ setzt der Renderer selbst).
   In Buffer `metadata.instagram.isAiGenerated: true`. Ergebnis ansehen – sieht es aus wie ein
   echter Ort oder ein echtes Ereignis, verwerfen und neutraler generieren.
5. **Rendern und ansehen** (Feed + Story). Der Renderer legt einen Verlauf übers Foto
   (oben heller, unten dunkler); bei sehr hellen Fotos `"farbe": "navy"` lassen und prüfen,
   ob die Kachel-Schrift klar lesbar ist. Mit `"bildPosition": "center 30%"` o. ä. den
   Ausschnitt verschieben.

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
