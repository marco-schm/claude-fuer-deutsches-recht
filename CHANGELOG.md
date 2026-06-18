# v335.0.0 — Scheidungs-Testakte umbenannt und entpeinlicht

## Testakte scheidungsdrama

Die Testakte `scheidung-trennungsdrama-wagenknecht-luetzelberg` wurde inhaltlich und namentlich überarbeitet:

- **Order-Slug**: `scheidung-trennungsdrama-wagenknecht-luetzelberg` → `scheidungsdrama`
- **Eheleute**: Vera Wagenknecht → **Hanna Trüffelberch**; Theo Lützelberg → **Franz Ürgelheim**
- **Entpeinlicht**: Die Erstgesprächsnotiz beschrieb die Mandantin als "pünktlich, gut gekleidet, merklich erschöpft" mit "laminiertem Deckblatt" — diese auf das Äußere zielenden Beschreibungen sind entfernt. Sachstand (pünktlich, erschöpft, strukturiert vorbereitet) bleibt erhalten.
- **Datei-Umbenennungen** im Akten-Ordner:
  - `15_trennungsunterhalt_theo_gegen_vera.md` → `15_trennungsunterhalt_franz_gegen_hanna.md`
  - `05_kommunikation_theo_und_studentin.md` → `05_kommunikation_franz_und_studentin.md`
  - `docx/scheidungsantrag_entwurf_vera_wagenknecht.docx` → `docx/scheidungsantrag_entwurf_hanna_trueffelberch.docx`
  - `emails/2024-11-19_vera_an_kanzlei_erstanfrage.eml` → `emails/2024-11-19_hanna_an_kanzlei_erstanfrage.eml`
  - `emails/2025-04-30_theo_anwalt_an_kanzlei_wechselmodell.eml` → `emails/2025-04-30_franz_anwalt_an_kanzlei_wechselmodell.eml`
  - `jpg/holzwerkstatt_theo_bothfeld.jpg` → `jpg/holzwerkstatt_franz_bothfeld.jpg`
  - `gesamt-pdf/scheidung-trennungsdrama-wagenknecht-luetzelberg_gesamt.pdf` → `gesamt-pdf/scheidungsdrama_gesamt.pdf`
- **Inhalt**: Alle Markdown-, eml-, yaml-Stellen sowie die docx-XML wurden vollständig auf die neuen Namen umgeschrieben (inkl. Genitive). Gesamt-PDF wurde neu gebaut.
- **Querverweise aktualisiert**: `testakten/README.md`, `fachanwalt-familienrecht/README.md`, `ASSET_INDEX.md`, `EVAL_RESULTS.md`.

Kinder (Mara, Jonas, Lina), Stadt (Hannover), Adresse (Lindener Hofstraße 47) und übrige Eigennamen bleiben — laut Nutzerwunsch.

## Validatoren

- `validate-plugin-structure.mjs`: OK
- `validate-yaml-frontmatter.py`: 0 Fehler, 0 Warnungen
- `validate-testakten-gesamt-pdf.py`: OK (205 Testakten)

## Versions-Bump

- v334.0.0 → v335.0.0 (marketplace.json: 215 Einträge, 214 plugin.json, 3 READMEs).

---

