# Übergabeprompt an Claude Opus 4.8 — letzte Verfeinerung

Du arbeitest im Repository `Klotzkette/claude-fuer-deutsches-recht` auf Branch `main`.

## Auftrag

Führe eine letzte fachliche Verfeinerung des Repos durch. Schwerpunkt ist juristische Tiefe, Eleganz, Konsistenz und direkte Nutzbarkeit. Prüfe alle drei Ebenen:

1. Skills: vorhandene Skills präzisieren, Wiederholungen entfernen, Pflichtnormen, Prüfraster, Risiken und Anti-Muster schärfen. Keine neuen Skills anlegen und keine Slugs umbenennen.
2. Werkstatt-Prompts: `{slug}-werkstatt.md` je Plugin autark halten, 10 bis 30 Druckseiten, keine Cross-Verweise, keine Floskeln, keine Audit-Sprache.
3. Schnellstart-Prompts: `{slug}-schnellstart.md` je Plugin autark halten, maximal 7500 Zeichen inklusive Leerzeichen, mit Rolle, Pflichtnormen, zwei bis drei Leitentscheidungen, Kurzprüfraster und Hinweis auf den Werkstatt-Prompt.

## Klotzkette-Regeln

- Skill-`description` im Frontmatter maximal 1024 Zeichen.
- `plugin.json`- und `marketplace.json`-`description` maximal 300 Zeichen.
- Keine Komma-Ziffer-Paare der Form `\d,\d`; Punkt verwenden.
- Keine XML-artigen Klammern in Plugin-, Werkstatt-, Schnellstart- oder Skill-Dateien.
- Keine Emojis.
- Statt Paragrafensymbol immer `Paragraf` oder `Paragrafen` ausschreiben. README-Dateien dürfen das Symbol enthalten.
- Slugs nur `[a-z0-9-]`, maximal 64 Zeichen.
- In Slugs, `name` und validatorrelevanten JSON-Feldern keine Umlaute oder Eszett, sondern `ae`, `oe`, `ue`, `ss`.
- In Markdown-Prosa echte Umlaute und Eszett verwenden.
- Generisches Maskulinum repo-weit, aber nicht in `CLAUDE.md` ausstellen.
- KI-VO, DSGVO und Aktengeheimnis nur in der Repo-`README.md` thematisieren, nicht in Plugin-Dateien, Werkstatt-Prompts, Schnellstart-Prompts oder Skills.
- Niemals die Begriffe `scrape`, `scraping`, `crawl`, `crawling` verwenden. Nutze `abrufen`, `lesen`, `auslesen`, `einsammeln`, `konsultieren`.
- Keine Floskeln wie `live verifizieren`, `AUDIT`, `NOT_FOUND`, `TBD`, `siehe Skill X`.
- Autor in jedem Commit: `Klotzkette <39582916+Klotzkette@users.noreply.github.com>`.
- Keine Erwähnung von Claude, AI, Codex oder Assistant in Commit-Messages.
- Vor jedem Push: `git fetch origin`.
- Push mit `api_credentials=["github"]`.

## Distribution

Werkstatt- und Schnellstart-Prompts werden nur als Markdown ausgeliefert, nicht als ZIP. README-Links sollen auf Raw-Dateien zeigen:

- `https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/{plugin-dir}/{slug}-werkstatt.md`
- `https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/{plugin-dir}/{slug}-schnellstart.md`

## Prüfprogramm

1. Stichprobe aus großen Kerngebieten lesen: Arbeitsrecht, Mietrecht, Familienrecht, Strafrecht, Datenschutzrecht, Gesellschaftsrecht, Insolvenzrecht, Steuerrecht, Sozialrecht, Verwaltungsrecht, Verfassungsrecht, Vergaberecht, Urheberrecht, Versicherungsrecht, IT-Recht und Liquiditätsplanung.
2. Prüfen, ob Werkstatt-Prompts tatsächlich autark sind und ohne Skill-Verweise arbeiten.
3. Prüfen, ob Schnellstart-Prompts unter 7500 Zeichen bleiben.
4. Prüfen, ob Leitentscheidungen realistisch, korrekt und thematisch passend sind. Keine Fundstelle erfinden.
5. Validatoren laufen lassen:
   - `node scripts/validate-plugin-structure.mjs`
   - `python3 scripts/validate-yaml-frontmatter.py`
6. Vor Push `git fetch origin`.

## Abschluss

Melde im Chat knapp:

- welche Bereiche geändert wurden,
- ob Validatoren grün sind,
- ob Schnellstarts unter 7500 Zeichen bleiben,
- welche offenen Risiken oder Lücken du nicht ohne neue Skills lösen konntest,
- und einen kurzen Diff-Statusbericht.

