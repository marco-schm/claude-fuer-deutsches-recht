# Megaprompt: fachanwalt-verwaltungsrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 80 Skills des Plugins `fachanwalt-verwaltungsrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Fachanwalt Verwaltungsrecht: ordnet Rolle (Bürger/Antragsteller, Behörde, Verwaltungsge…
2. **mandat-triage-verwaltungsrecht** — Eingangs-Triage für verwaltungsrechtliche Mandate: Erst-Qualifizierung des Sachgebiets, Verfahrensstands und Frist-Sofor…
3. **fachanwalt-verwaltungsrecht-orientierung** — Orientierung im Fachanwaltsrecht Verwaltungsrecht: FAO-Voraussetzungen, Kerngebiete, typische Mandate und Fristen ueberb…
4. **orientierung-mandat-fachanwaltschaft** — Orientierung im Fachanwaltsrecht Verwaltungsrecht: FAO-Voraussetzungen, Kerngebiete, typische Mandate und Fristen überbl…
5. **orientierung-sonderfall-edge-case** — Orientierung: Sonderfall und Edge-Case-Prüfung: Orientierung: Sonderfall und Edge-Case-Prüfung.
6. **erstgespraech-mandatsannahme** — Strukturierter Erstgespraechsleitfaden für Allgemeines Verwaltungs- und Bauplanungsrecht: Erfassung der Konstellation, K…
7. **erstpruefung-und-mandatsziel** — Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.
8. **fachanwalt-verwaltungsrecht-widerspruchsschrift** — Widerspruchsschrift nach §§ 68 ff. VwGO gegen belastenden Verwaltungsakt formulieren: Mandant hat Bescheid erhalten und …
9. **fachanwalt-verwaltungsrecht-beamten-disziplinarverfahren** — Beamten-Disziplinarverfahren führen oder verteidigen: Beamter hat Dienstvergehen begangen oder ist Dienstherr bei Einlei…
10. **fachanwalt-verwaltungsrecht-drittanfechtung-umwelt** — Drittanfechtung umweltrechtlicher Genehmigungen (BImSchG, BauGB) durch Nachbarn oder Umweltverband: Klagebefugnis und ma…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Fachanwalt Verwaltungsrecht: ordnet Rolle (Bürger/Antragsteller, Behörde, Verwaltungsgericht), markiert Frist (§ 74 VwGO Klagefrist 1 Mon.), wählt Norm (VwGO, VwVfG, AO (steuerlich)) und Zuständigkeit (VG, OVG/VGH, BVerwG), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Fachanwalt Verwaltungsrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `amtshaftung-paragraf-839-bgb-art-34-gg` — Amtshaftung Paragraf 839 BGB ART 34 GG
- `anfechtungs-risikoampel-und-gegenargumente` — Anfechtungs Eilrechtsschutz ABS
- `anhoerung-paragraf-28-vwvfg` — Anhoerung Paragraf 28 Vwvfg
- `anordnung-quellenkarte` — Anordnung Quellenkarte
- `drittanfechtung-umwelt` — Drittanfechtung
- `eilrechtsschutz-paragraf-80-vwgo` — Eilrechtsschutz Paragraf 80 Vwgo
- `einstweilige-verhandlung-vergleich-und-eskalation` — Einstweilige Fachanwalt Kanzlei
- `ermessen-paragraf-40-vwvfg` — Ermessen Paragraf 40 Vwvfg
- `erstgespraech-mandatsannahme` — Erstgespraech Mandatsannahme FA Vwgo
- `workflow-mandantenkommunikation` — FA Verwaltungsrecht Mandant Redteam Gate
- `einstieg-schnelltriage-fallrouting` — FA Verwaltungsrecht Start Chronologie Fristen
- `klagefrist-paragraf-58-vwgo-bverwg-4-c-1-19` — Klagefrist Paragraf 58 Vwgo Bverwg 4 C 1 19
- `kommunalrecht-paragraf-2-go` — Kommunalrecht Paragraf 2 GO
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Fachanwalt Verwaltungsrecht sind VwGO, VwVfG, § 80 Abs 5 VwGO einstweilige Anordnung Normenkontrolle Polizei. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `mandat-triage-verwaltungsrecht`

_Eingangs-Triage für verwaltungsrechtliche Mandate: Erst-Qualifizierung des Sachgebiets, Verfahrensstands und Frist-Sofort-Checks: Eingangs-Triage für verwaltungsrechtliche Mandate: Erst-Qualifizierung des Sachgebiets, Verfahrensstands und Frist-Sofort-Check..._

# Eingangs-Triage für verwaltungsrechtliche Mandate: Erst-Qualifizierung des Sachgebiets, Verfahrensstands und Frist-Sofort-Checks


## Aktenstart statt Formularstart

Wenn zu **Widerspruchsschrift Mandat Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Fachanwalt Verwaltungsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Eingangs-Triage für verwaltungsrechtliche Mandate: Erst-Qualifizierung des Sachgebiets, Verfahrensstands und Frist-Sofort-Checks. Normen: § 70 VwGO (Widerspruch 1 Monat), § 74 VwGO (Klage 1 Monat), § 75 VwGO (Untätigkeitsklage 3 Monate). Prüfraster: Sachgebiet (Bau, Gewerbe, Polizei, Beamtenrecht, Schule, Subventionen, Ausländer), Behördenebene, Verfahrensstand, Frist-Sofort-Check, Eskalation bei drohendem Vollzug. Output Triage-Protokoll mit Fristen-Ampel, Routing-Empfehlung. Abgrenzung: Detailprüfung siehe widerspruch-oder-klage-erstprüfung; Schriftsatz siehe schriftsatzkern-substantiierung.

### Mandat-Triage Verwaltungsrecht

## Ablauf — sieben Fragen

### Frage 1 — Wer und für wen?

- Bürger gegen Behörde
- Unternehmen gegen Behörde
- Behörde (selten — vertretbar nur unter strikter Trennung)
- Verband-Klagebefugnis

### Frage 2 — Sachgebiet?

- **Bau- und Planungsrecht** Baugenehmigung Nachbarklage Bebauungsplan
- **Gewerberecht** Gewerbeerlaubnis Untersagung Gaststätte Spielhalle
- **Polizei- und Ordnungsrecht** polizeiliche Maßnahme Versammlungsrecht
- **Beamten- und Soldatenrecht** Disziplinar Beurteilung Konkurrentenklage
- **Schule und Hochschule** Versetzung Abitur Zulassung
- **Subventionsrecht** Förderbescheid Rückforderung
- **Asyl- und Ausländerrecht** (an `fachanwalt-migrationsrecht` weiter)
- **Sozialrecht** (an `fachanwalt-sozialrecht` weiter)
- **Steuerrecht** (an `steuerrecht-anwalt-und-berater` weiter)
- **Vergaberecht** (an `fachanwalt-vergaberecht` weiter)
- **Umweltrecht**
- **Versammlungsrecht**
- **Kommunalrecht**

### Frage 3 — Akute Eilbedürftigkeit?

- Sofortige Vollziehung angeordnet
- Vollzug innerhalb Tage angekündigt
- Demonstrationsverbot ein-Tages-Vorlauf
- Räumung droht
- Untersagung erteilt — Geschäftsstillstand
- Bauleitplan-Aufstellung in der Beschlussphase

### Frage 4 — Stand?

- Vor Antragstellung (Beratung)
- Antrag eingereicht — wartet auf Bescheid
- Anhörung läuft § 28 VwVfG
- Bescheid liegt vor (Datum)
- Widerspruchsverfahren läuft
- Klage erhoben (Az VG)
- Berufung / Revision (OVG BVerwG)
- Verfassungsbeschwerde

### Frage 5 — Behörde?

- Bundesbehörde (z.B. BAMF Bundespolizei BfArM)
- Landesbehörde (z.B. Bezirksregierung Landratsamt)
- Kommunalbehörde
- Sondereinrichtung Anstalt öffentlichen Rechts

### Frage 6 — Frist?

- **Widerspruch** ein Monat § 70 VwGO; Bekanntgabe-Fiktion § 41 Abs. 2 VwVfG vier Tage seit 01.01.2025 (PostModG)
- **Klage** ein Monat § 74 VwGO ab Bekanntgabe Widerspruchsbescheid
- **Untätigkeitsklage** § 75 VwGO nach drei Monaten ohne Bescheid
- **Verfassungsbeschwerde** ein Monat § 93 BVerfGG
- **Bei fehlender Rechtsbehelfsbelehrung** ein Jahr § 58 Abs. 2 VwGO

### Frage 7 — Wirtschaftliche Verhältnisse PKH?

- Prozesskostenhilfe § 166 VwGO iVm §§ 114 ff. ZPO
- Beratungshilfe für außergerichtlich

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Baugenehmigung Nachbarklage | (Skill bau-nachbarklage — perspektivisch) |
| Bauliche Untersagung | `widerspruch-oder-klage-erstpruefung` |
| Gewerbe-Erlaubnis-Streit | `widerspruch-oder-klage-erstpruefung` |
| Beamten-Konkurrentenklage | (Skill konkurrentenklage — perspektivisch) |
| Beurteilung Beamter | (Skill beurteilungsanfechtung — perspektivisch) |
| Schule Versetzung Zulassung | `widerspruch-oder-klage-erstpruefung` |
| Asyl Ausländerrecht | weiter an `mandat-triage-migrationsrecht` |
| Sozialleistung | weiter an `mandat-triage-sozialrecht` |
| Steuerrecht | weiter an `anw-mandat-triage-steuerrecht` |
| Polizei-Maßnahme | (Skill polizei-feststellungs-klage — perspektivisch) |
| Versammlungs-Verbot | `widerspruch-oder-klage-erstpruefung` plus § 80 Abs. 5 VwGO |

## Eilmodus

Bei sofortiger Vollziehung oder akutem Vollzug:

1. Mandantengespräch — Sachverhalt zwanzig Minuten
2. Bescheid einlesen — fünfzehn Minuten
3. Widerspruch einlegen (formloser Schriftsatz) — gleichzeitig
4. Eilantrag § 80 Abs. 5 VwGO oder § 123 VwGO formulieren
5. Bei VG einreichen — Eingang sicherstellen Empfangsbestätigung

## Eskalation

- **Telefon-Sofort** drohender Vollzug binnen Stunden
- **Binnen einer Stunde** Bescheid mit sofortiger Vollziehung
- **Heute** Widerspruchsschrift Eilantrag-Erstentwurf
- **Diese Woche** Klage-Erstentwurf Begründung

## Ausgabe

- `triage-protokoll-verwaltungsrecht.md`
- Frist im Fristenbuch
- Bei Eilmodus: Eilantrag-Entwurf im Anhang
- Mandatsvereinbarung mit Streitwertabschätzung § 52 GKG
- Empfehlung Folge-Skill

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Leitentscheidungen Mandat-Triage

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen

- VwGO §§ 42 58 68 70 74 75 80 80a 123
- VwVfG §§ 28 35 41
- GKG § 52
- BVerwGE Std.Spruch
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

---

## Skill: `fachanwalt-verwaltungsrecht-orientierung`

_Orientierung im Fachanwaltsrecht Verwaltungsrecht: FAO-Voraussetzungen, Kerngebiete, typische Mandate und Fristen ueberblicken. Normen: VwGO (Anfechtungs-, Verpflichtungs-, Leistungs-, Feststellungsklage, Eilrechtsschutz §§ 80 und 123 VwGO), VwVfG, Polizei- und Ordnungsrecht, Baurecht. Prüfraster: Sachgebiet (Bau, Gewerbe, Polizei, Beamtenrecht), Verfahrensarten, Fristen-Überblick. Output Orientierungs-Memo, Routing zu Spezialskills. Abgrenzung: Detailarbeit in Spezialskills; Mandats-Triage siehe mandat-triage-verwaltungsrecht._

# Fachanwalt für Verwaltungsrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 80 Fälle in den letzten drei Jahren, davon mindestens 30 gerichtliche Verfahren.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Verwaltungsverfahren | VwVfG (Bund) Landes-VwVfG |
| Verwaltungsprozess | VwGO §§ 40 ff. 80 86b 123 |
| Allgemeines Verwaltungsrecht | Quellenprüfung Hartmann Grundbegriffe |
| Polizei- und Ordnungsrecht | Polizei- und Ordnungsgesetze der Länder (PolG NRW BayPAG) |
| Baurecht | BauGB BauNVO Landesbauordnungen |
| Beamtenrecht | BeamtStG BBG Landesbeamtengesetze |
| Versammlungsrecht | VersG / Landesversammlungsgesetze |
| Datenschutz öffentlich | BDSG Landesdatenschutzgesetze |

## Typische Mandate

- Bauantrag Widerspruch und Klage
- Polizei- und Ordnungsverfügung
- Beamtenrechtliche Streitigkeiten (Beurteilung Versetzung Disziplinarverfahren)
- Sozialhilfe vs Eingliederung (Abgrenzung zu Sozialrecht)
- Versammlungsverbot
- Ausländer- und Asylrechtsstreit (siehe fachanwalt-migrationsrecht)
- Verwaltungsvollstreckung

## Fristen

- **Widerspruchsfrist** § 70 VwGO — ein Monat.
- **Klagefrist** § 74 VwGO — ein Monat ab Bekanntgabe.
- **Berufungsantrag (Zulassung)** § 124a VwGO — ein Monat.
- **Eilrechtsschutz** § 80 Abs. 5 VwGO und § 123 VwGO — keine Frist; aber Eilbedürfnis erforderlich.
- **Normenkontrolle** § 47 VwGO — ein Jahr ab Bekanntmachung der Norm.

## Hauptgerichte

- Verwaltungsgericht erste Instanz (§ 45 VwGO).
- OVG / VGH Berufung und Normenkontrolle.
- BVerwG Leipzig Revision.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- ARGE Verwaltungsrecht DAV.

## Aktuelle Rechtsprechung (Leitsaetze)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Fristen im Ueberblick

| Verfahrensschritt | Frist | Grundlage |
|---|---|---|
| Widerspruch | 1 Monat | § 70 VwGO |
| Klage | 1 Monat | § 74 VwGO |
| Normenkontrolle | 1 Jahr | § 47 Abs. 2 VwGO |
| Untaetigkeitsklage | 3 Monate | § 75 VwGO |
| Berufungsantrag | 1 Monat | § 124a VwGO |
| Verfassungsbeschwerde | 1 Monat | § 93 BVerfGG |
| Revisionsantrag | 1 Monat | § 139 VwGO |

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Schnittstellen

- **kanzlei-allgemein** fuer Fristen Versand.
- **fachanwalt-migrationsrecht** bei Auslaenderrecht.
- **fachanwalt-sozialrecht** bei Abgrenzung Sozialgericht vs. Verwaltungsgericht.

---

## Skill: `orientierung-mandat-fachanwaltschaft`

_Orientierung im Fachanwaltsrecht Verwaltungsrecht: FAO-Voraussetzungen, Kerngebiete, typische Mandate und Fristen überblicken: N..._

# Orientierung im Fachanwaltsrecht Verwaltungsrecht: FAO-Voraussetzungen, Kerngebiete, typische Mandate und Fristen überblicken


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung im Fachanwaltsrecht Verwaltungsrecht: FAO-Voraussetzungen, Kerngebiete, typische Mandate und Fristen überblicken. Normen: VwGO (Anfechtungs-, Verpflichtungs-, Leistungs-, Feststellungsklage, Eilrechtsschutz §§ 80 und 123 VwGO), VwVfG, Polizei- und Ordnungsrecht, Baurecht. Prüfraster: Sachgebiet (Bau, Gewerbe, Polizei, Beamtenrecht), Verfahrensarten, Fristen-Überblick. Output Orientierungs-Memo, Routing zu Fachmodule. Abgrenzung: Detailarbeit in Fachmodule; Mandats-Triage siehe mandat-triage-verwaltungsrecht.

### Fachanwalt für Verwaltungsrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 80 Fälle in den letzten drei Jahren, davon mindestens 30 gerichtliche Verfahren.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Verwaltungsverfahren | VwVfG (Bund) Landes-VwVfG |
| Verwaltungsprozess | VwGO §§ 40 ff. 80 86b 123 |
| Allgemeines Verwaltungsrecht | Quellenprüfung Hartmann Grundbegriffe |
| Polizei- und Ordnungsrecht | Polizei- und Ordnungsgesetze der Länder (PolG NRW BayPAG) |
| Baurecht | BauGB BauNVO Landesbauordnungen |
| Beamtenrecht | BeamtStG BBG Landesbeamtengesetze |
| Versammlungsrecht | VersG / Landesversammlungsgesetze |
| Datenschutz öffentlich | BDSG Landesdatenschutzgesetze |

## Typische Mandate

- Bauantrag Widerspruch und Klage
- Polizei- und Ordnungsverfügung
- Beamtenrechtliche Streitigkeiten (Beurteilung Versetzung Disziplinarverfahren)
- Sozialhilfe vs Eingliederung (Abgrenzung zu Sozialrecht)
- Versammlungsverbot
- Ausländer- und Asylrechtsstreit (siehe fachanwalt-migrationsrecht)
- Verwaltungsvollstreckung

## Fristen

- **Widerspruchsfrist** § 70 VwGO — ein Monat.
- **Klagefrist** § 74 VwGO — ein Monat ab Bekanntgabe.
- **Berufungsantrag (Zulassung)** § 124a VwGO — ein Monat.
- **Eilrechtsschutz** § 80 Abs. 5 VwGO und § 123 VwGO — keine Frist; aber Eilbedürfnis erforderlich.
- **Normenkontrolle** § 47 VwGO — ein Jahr ab Bekanntmachung der Norm.

## Hauptgerichte

- Verwaltungsgericht erste Instanz (§ 45 VwGO).
- OVG / VGH Berufung und Normenkontrolle.
- BVerwG Leipzig Revision.

## Berufsverband

- ARGE Verwaltungsrecht DAV.

## Aktuelle Rechtsprechung (Leitsaetze)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Fristen im Überblick

| Verfahrensschritt | Frist | Grundlage |
|---|---|---|
| Widerspruch | 1 Monat | § 70 VwGO |
| Klage | 1 Monat | § 74 VwGO |
| Normenkontrolle | 1 Jahr | § 47 Abs. 2 VwGO |
| Untaetigkeitsklage | 3 Monate | § 75 VwGO |
| Berufungsantrag | 1 Monat | § 124a VwGO |
| Verfassungsbeschwerde | 1 Monat | § 93 BVerfGG |
| Revisionsantrag | 1 Monat | § 139 VwGO |

## Schnittstellen

- **kanzlei-allgemein** für Fristen Versand.
- **fachanwalt-migrationsrecht** bei Ausländerrecht.
- **fachanwalt-sozialrecht** bei Abgrenzung Sozialgericht vs. Verwaltungsgericht.

---

## Skill: `orientierung-sonderfall-edge-case`

_Orientierung: Sonderfall und Edge-Case-Prüfung: Orientierung: Sonderfall und Edge-Case-Prüfung._

# Orientierung: Sonderfall und Edge-Case-Prüfung


## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 28 Abs. 1 VwVfG` — Anhörung vor belastender Verwaltungsentscheidung.
- `§ 37 Abs. 1 VwVfG` — Bestimmtheit des Verwaltungsakts.
- `§ 39 Abs. 1 VwVfG` — Begruendungspflicht.
- `§ 40 VwVfG` — Ermessensausübung und Ermessensfehler.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist, soweit Widerspruchsverfahren vorgesehen.
- `§ 74 Abs. 1 VwGO` — Klagefrist.
- `§ 80 Abs. 5 VwGO` — Eilrechtsschutz gegen Vollziehung.
- `§ 123 Abs. 1 VwGO` — einstweilige Anordnung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung: Sonderfall und Edge-Case-Prüfung.

## Spezialwissen: Orientierung: Sonderfall und Edge-Case-Prüfung
- **Normen-/Quellenanker:** VwGO, VwVfG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Orientierung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `erstgespraech-mandatsannahme`

_Strukturierter Erstgespraechsleitfaden für Allgemeines Verwaltungs- und Bauplanungsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen: Strukturierter Erstgespra..._

# Strukturierter Erstgespraechsleitfaden für Allgemeines Verwaltungs- und Bauplanungsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierter Erstgespraechsleitfaden für Allgemeines Verwaltungs- und Bauplanungsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.

### Erstgespraech und Mandatsannahme im Allgemeines Verwaltungs- und Bauplanungsrecht

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Allgemeines Verwaltungs- und Bauplanungsrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klären, Konflikt- und GwG-Prüfung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Allgemeines Verwaltungs- und Bauplanungsrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klägerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: VA, Widerspruch, Klage VG, Bauplanung, Gewerberecht, Beamtenrecht
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Widerspruch, Anfechtungsklage VG, Verpflichtungsklage, Eilantrag § 80 Abs. 5 VwGO). Frist-Alarm an die Vorbereitung weitergeben.

### 2. Konflikt-Prüfung und GwG-Check (5 Min.)

- Konflikt-Check über Mandantsystem: Gegnerin, Streitgegenstand, frueherer Mandant?
- GwG-Identifizierung: amtlicher Lichtbildausweis (Ausweisscan), bei juristischer Person Handelsregister-/Transparenzregister-Auszug, ggf. wirtschaftlich Berechtigte/n.
- Risikobewertung (niedrig/mittel/hoch) abhaengig von Mandatscharakter, Bargeld, Auslandsbezug.
- Doku im Mandatsbogen (Pflicht nach §§ 10 ff. GwG i.V.m. § 2 Abs. 1 Nr. 10 GwG für RA-Mandate).

### 3. Vollmacht und Schweigepflichtentbindung

- Allgemeine Prozess-/Aussenvollmacht (BORA, ZPO, FamFG, je nach Fachgebiet).
- Spezielle Vollmachten: ggf. Akteneinsicht Strafakte, KV-Abrechnungsdaten, Sozialdaten (Schweigepflichtentbindung gegenueber Krankenkasse, Arzt, Behörde).
- Bei Eheleuten/GbR/GmbH: einzelvollmachtgebende Person und Vertretungsmacht klären.

### 4. Streitwert und Gebührenvereinbarung

Standard-Streitwerte im Bereich Allgemeines Verwaltungs- und Bauplanungsrecht:

- Skizze: Streitwert grob abschaetzen (z.B. Hauptforderung, ggf. + Zinsen, Nebenforderungen).
- RVG-Pauschalrechnung (Berechnungstool im Plugin) oder Stundenhonorarvereinbarung.
- Beratungshilfe-/Prozesskostenhilfe-Antrag prüfen, wenn wirtschaftlich angezeigt.
- Vorschussanforderung nach § 9 RVG.

### 5. Strategie-Erstskizze

Drei Weichen am Ende des Erstgespraechs:

- **Mandat annehmen:** vollstaendig (Prüfung + Schriftsatz) oder begrenzt (nur Prüfung/Gutachten).
- **Verweisen:** wenn Spezialgebiet ausserhalb der Fachanwaltschaft, oertlich unzuständig oder Konflikt.
- **Ablehnen:** offensichtlich aussichtslos, GwG-Hit, Bauchgefuehl-Vorsicht.

## Pflicht-Output am Ende

1. **Mandatsbogen** mit Beteiligten, Konflikt-Check, GwG-Status, Streitwert.
2. **Frist-Liste** (Sofortfristen, Verjährung, Ausschlussfristen, Beweisanforderungs-Fristen).
3. **Anlagenverzeichnis** des uebergebenen Datenraums (Stand erstes Sortieren).
4. **Naechster-Schritt-Plan:** binnen 24/48/72 h, Owner, Output.
5. **Honorarvereinbarung** unterschrieben oder Vorbehalt notiert.

## Relevante Rechtsgrundlagen und Standards

- BORA, BRAO, FAO für Fachanwaltschaft Allgemeines Verwaltungs- und Bauplanungsrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- VwVfG, VwGO, BauGB, BauNVO, GewO, BBG/BeamtStG (für fachliche Erstpruefung).
- DSGVO und BDSG für den Umgang mit Mandantendaten (Art. 6 DSGVO als Rechtsgrundlage, Art. 9 ggf. Gesundheitsdaten).

## Typische Fehler im Erstgespraech

- Frist uebersehen, weil Mandantin sie nicht selber genannt hat (immer aus jedem Schreiben Frist herausziehen).
- Konflikt-Check nur nach Personennamen, nicht nach Sachzusammenhang (gleiche Liegenschaft, gleicher Sachverhalt).
- Vollmachtsumfang unklar -> später Streit mit Mandantin über Befugnisse.
- Honorarvereinbarung muendlich -> Beweisnot bei Streitwert-/Honorar-Streit.
- GwG: kein Lichtbildausweis erfasst, kein Aktenvermerk über Risikobewertung.

## Praxis-Checkliste

- [ ] Personalien und Rolle aller Beteiligten erfasst
- [ ] Konflikt-Check durchgefuehrt
- [ ] GwG: Identifizierung + Risikobewertung notiert
- [ ] Allgemeine Vollmacht unterschrieben
- [ ] Speziale Vollmacht / Entbindungserklaerung (wo noetig) unterschrieben
- [ ] Streitwert geschaetzt
- [ ] Honorarvereinbarung unterschrieben oder ausdruecklich auf RVG verwiesen
- [ ] Fristenliste angelegt und in Kalender eingetragen
- [ ] Mandatsbogen vollstaendig
- [ ] Naechster-Schritt-Plan dem Mandanten kommuniziert (E-Mail-Zusammenfassung)

## Konkrete Praxis-Konstellationen

### Konstellation A: Eilbeduerftigkeit

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Allgemeines Verwaltungs- und Bauplanungsrecht). Handlungs-Sequenz:

1. Sofort-Vollmacht und Sofort-Akteneinsicht (per beA, ELSTER, Behördenportal).
2. Antrag auf Wiedereinsetzung (§ 233 ZPO, § 60 VwGO, § 110 AO) als Reserve dokumentieren.
3. Spaeteste-Stunde-Versand-Plan: beA bevorzugt, mit qualifizierter Signatur und Empfangsbekenntnis.
4. Honorarvereinbarung NICHT auf Eilzuschlag verzichten - aber transparent kommunizieren.

### Konstellation B: Komplexer Sachverhalt, Datenraum unsortiert

Mandant uebergibt 200+ Dateien (PDF-Scans, E-Mails, Excel-Listen). Vor jeder fachlichen Bewertung:

1. Datenraum-Index in Excel: Datum, Absender, Empfaenger, Aktenzeichen, kurze Inhaltszeile.
2. Chronologischer Verlauf als Zeitstrahl - Spielraum für Verjährungs- und Ausschlussfristen identifizieren.
3. Loecher im Datenraum gezielt anfordern (Mandantenfragen-Katalog).

### Konstellation C: Interessenkonflikt-Naehe

Frueheres Mandat mit derselben Gegnerin oder gleichem Sachzusammenhang. Prüfung:

1. § 43a Abs. 4 BRAO und § 3 BORA - Sachzusammenhang, nicht nur Personenidentitaet.
2. Einwilligung beider Mandanten in Textform (mit konkreter Beschreibung).
3. Bei Zweifel: Mandat ablehnen und an Kanzleikollegium ueberweisen.

## Mandanten-Erwartungsmanagement

- Realistische Erfolgs- und Kostenprognose (nicht "Wir gewinnen sicher").
- Verfahrensdauer im Bereich Allgemeines Verwaltungs- und Bauplanungsrecht: Erfahrungswerte nach Instanz.
- Vergleichschance vs. streitiges Urteil als Option offen halten.
- Schriftliche Zusammenfassung des Erstgespraechs binnen 48 h.

## Honorarvereinbarung - Best Practices

- RVG-Basis als Default, Stundenhonorar nur mit gesondertem Hinweis nach § 3a RVG.
- Erfolgshonorar nur in den engen Grenzen § 4a RVG.
- Vorschuss in Höhe der voraussichtlichen 1. Instanz.
- Klarstellung: Auslagen-Pauschale, USt, Reisekosten, Sachverstaendigenkosten gesondert.
- Bei PKH/Beratungshilfe-Mandant: schriftliche Belehrung, dass eigene Beitraege möglich sind.

## Mandatsbogen-Muster (Mindestinhalt)

- Mandant (Name, Geburtsdatum, Anschrift, Telefon, E-Mail)
- Gegner (Name, Anschrift, ggf. anwaltliche Vertretung)
- Kurzbeschreibung Sachverhalt (5-10 Saetze)
- Ziel des Mandats (eine Zeile)
- Strittige Fragen (bullet)
- Geprueft: Konflikt - GwG - Vollmacht
- Streitwert (Schaetzung)
- Honorarvereinbarung (RVG/Stunde/Pauschale)
- Frist-Liste
- Aktenanlage Datum
- Naechster-Schritt

## Leitentscheidungen Mandatsannahme / Erstkontakt

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Cross-Refs

- `vergleichsverhandlung-strategie` (im selben Plugin) für den Fall, dass aussergerichtliche Loesung angestrebt wird.
- `schriftsatzkern-substantiierung` (im selben Plugin) für den Schriftsatzaufbau, wenn Klage/Widerspruch eingereicht wird.
- Kanzlei-Allgemein-Plugin `kanzlei-allgemein` für Konflikt-, GwG- und PEP-Prüfroutinen.

---

## Skill: `erstpruefung-und-mandatsziel`

_Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel


## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 28 Abs. 1 VwVfG` — Anhörung vor belastender Verwaltungsentscheidung.
- `§ 37 Abs. 1 VwVfG` — Bestimmtheit des Verwaltungsakts.
- `§ 39 Abs. 1 VwVfG` — Begruendungspflicht.
- `§ 40 VwVfG` — Ermessensausübung und Ermessensfehler.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist, soweit Widerspruchsverfahren vorgesehen.
- `§ 74 Abs. 1 VwGO` — Klagefrist.
- `§ 80 Abs. 5 VwGO` — Eilrechtsschutz gegen Vollziehung.
- `§ 123 Abs. 1 VwGO` — einstweilige Anordnung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** VwGO, VwVfG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Fachanwalt** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `fachanwalt-verwaltungsrecht-widerspruchsschrift`

_Widerspruchsschrift nach §§ 68 ff. VwGO gegen belastenden Verwaltungsakt formulieren: Mandant hat Bescheid erhalten und will innerhalb der Frist Widerspruch einlegen. Normen: § 68 VwGO (Vorverfahren), § 70 Abs. 1 VwGO (Frist 1 Monat), § 80 Abs. 1 VwGO (aufschiebende Wirkung), § 58 Abs. 2 VwGO (Jahresfrist ohne Rechtsbehelfsbelehrung). Prüfraster: Statthaftigkeit (Bundesland?), Fristberechnung, aufschiebende Wirkung vs. sofortige Vollziehung, Begründung. Output Widerspruchsschrift. Abgrenzung: Anfechtungsklage direkt (kein Widerspruch statthaft) siehe fachanwalt-verwaltungsrecht-anfechtungsklage; Eilantrag siehe eilantrag-80-abs-5-vwgo._

# Widerspruchsschrift

## Kernsachverhalt

Gegen einen belastenden Verwaltungsakt ist als Vorverfahren — sofern nicht durch Bundes- oder Landesrecht ausgeschlossen — zunächst Widerspruch einzulegen. Erst nach Erlass des Widerspruchsbescheids oder Ablauf der Entscheidungsfrist ist die Anfechtungsklage zulässig. Das Widerspruchsverfahren bietet die Chance der vollständigen Überprüfung des Verwaltungsakts auf Rechtmäßigkeit und Zweckmäßigkeit und ermöglicht eine frühzeitige Einigung ohne Klageverfahren.

## Kaltstart-Rückfragen

1. Welcher Verwaltungsakt — welche Behörde, Datum, Zustellungsdatum? Ist die Rechtsbehelfsbelehrung ordnungsgemäß?
2. Ist das Widerspruchsverfahren im Bundesland und Sachgebiet vorgesehen — oder wurde es durch Landesgesetz ausgeschlossen (§ 68 Abs. 1 Satz 2 VwGO i.V.m. Landesrecht; z.B. NRW, Bayern, Niedersachsen für bestimmte Gebiete)?
3. Hat der Verwaltungsakt aufschiebende Wirkung — oder entfällt sie nach § 80 Abs. 2 VwGO (öffentliche Abgaben, Polizei, gesetzlicher Ausschluss, Sofortvollzug)?
4. Welche formellen Mängel sind erkennbar — fehlende Anhörung § 28 VwVfG, mangelhafte Begründung § 39 VwVfG, Zuständigkeitsmangel?
5. Welche materiellen Mängel bestehen — Tatbestand nicht erfüllt, Ermessensfehler §§ 40 VwVfG, 114 VwGO, Unverhältnismäßigkeit?
6. Soll parallel Eilrechtsschutz beantragt werden — § 80 Abs. 5 VwGO bei Sofortvollzug oder § 80 Abs. 4 VwGO Antrag bei Behörde?
7. Ist eine Hinzuziehung des Bevollmächtigten für das Vorverfahren nach Landesrecht erforderlich und kostenpflichtig?
8. Ist ein Widerspruchsgebühr-Regime im Bundesland anwendbar — Kosten des Vorverfahrens nach VwVfG oder Landesgebührengesetz?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Auszüge)

**§ 68 Abs. 1 VwGO** — Vor Erhebung der Anfechtungsklage sind Rechtmäßigkeit und Zweckmäßigkeit des Verwaltungsakts in einem Vorverfahren nachzuprüfen. Einer solchen Nachprüfung bedarf es nicht, wenn ein Gesetz dies bestimmt oder wenn der Abhilfebescheid oder der Widerspruchsbescheid erstmalig eine Beschwer enthält.

**§ 70 Abs. 1 VwGO** — Der Widerspruch ist innerhalb eines Monats, nachdem der Verwaltungsakt dem Beschwerten bekanntgegeben worden ist, schriftlich, in elektronischer Form nach § 3a VwVfG oder zur Niederschrift bei der Behörde zu erheben, die den Verwaltungsakt erlassen hat.

**§ 58 Abs. 2 VwGO** — Ist die Rechtsbehelfsbelehrung unterblieben oder unrichtig erteilt, so ist die Einlegung des Rechtsbehelfs innerhalb eines Jahres seit Zustellung zulässig.

**§ 79 Abs. 1 VwGO** — Gegenstand der Anfechtungsklage ist der ursprüngliche Verwaltungsakt in der Gestalt, die er durch den Widerspruchsbescheid gefunden hat.

**§ 28 Abs. 1 VwVfG** — Bevor ein Verwaltungsakt erlassen wird, der in Rechte eines Beteiligten eingreift, ist diesem Gelegenheit zu geben, sich zu den für die Entscheidung erheblichen Tatsachen zu äußern.

**§ 39 Abs. 1 VwVfG** — Ein schriftlicher oder elektronischer sowie ein schriftlich oder elektronisch bestätigter Verwaltungsakt ist mit einer Begründung zu versehen.

**§ 40 VwVfG** — Ist die Behörde ermächtigt, nach ihrem Ermessen zu handeln, hat sie ihr Ermessen entsprechend dem Zweck der Ermächtigung auszuüben und die gesetzlichen Grenzen des Ermessens einzuhalten.

**§ 45 Abs. 1 Nr. 3 VwVfG** — Eine Verletzung von Verfahrens- oder Formvorschriften, die nicht den Verwaltungsakt nach § 44 nichtig macht, ist unbeachtlich, wenn … die erforderliche Begründung nachträglich gegeben wird; dies gilt auch nach § 28 (Anhörung).

**§ 45 Abs. 2 VwVfG** — Handlungen nach Absatz 1 können bis zum Abschluss der letzten Tatsacheninstanz eines verwaltungsgerichtlichen Verfahrens nachgeholt werden.

**§ 114 VwGO** — Soweit die Verwaltungsbehörde ermächtigt ist, nach ihrem Ermessen zu handeln, prüft das Gericht auch, ob der Verwaltungsakt rechtswidrig ist, weil die gesetzlichen Grenzen des Ermessens überschritten sind oder von dem Ermessen in einer dem Zweck der Ermächtigung nicht entsprechenden Weise Gebrauch gemacht ist.

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Leitsatz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema Widerspruch


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Norm | Inhalt |
|---|---|---|---|
| 1 | Statthaftigkeit Widerspruchsverfahren | § 68 VwGO + Landesrecht | Nicht ausgeschlossen durch Landes- oder Bundesrecht? |
| 2 | Klagebefugnis analog | § 42 Abs. 2 VwGO | Adressat oder Drittbetroffener mit möglicher Rechtsverletzung |
| 3 | Widerspruchsfrist | § 70 Abs. 1 VwGO | 1 Monat ab Bekanntgabe; § 58 Abs. 2: 1 Jahr bei Belehrungsfehler |
| 4 | Form des Widerspruchs | § 70 Abs. 1 VwGO | Schriftlich, elektronisch oder zur Niederschrift |
| 5 | Zuständige Ausgangsbehörde | § 70 VwGO | Widerspruch an Behörde, die VA erlassen hat |
| 6 | Aufschiebende Wirkung | § 80 Abs. 1 VwGO | Besteht sie? Entfällt nach § 80 Abs. 2 VwGO? |
| 7 | Formelle Rechtmäßigkeit des VA | §§ 28, 39 VwVfG | Anhörung, Begründung, Zuständigkeit, Form |
| 8 | Heilbarkeit formeller Fehler | § 45 VwVfG | Nachholbarkeit bis Abschluss Widerspruchsverfahren; Gefahr der Heilung |
| 9 | Materielle Rechtmäßigkeit | Spezialgesetze + BGB/VwVfG | Tatbestand der Ermächtigungsgrundlage erfüllt? |
| 10 | Ermessen | §§ 40 VwVfG, 114 VwGO | Nichtgebrauch, Überschreitung, Fehlgebrauch |
| 11 | Verhältnismäßigkeit | Art. 20 GG | Geeignet, erforderlich, angemessen |
| 12 | Zweckmäßigkeit | § 68 VwGO | Widerspruchsverfahren prüft auch Zweckmäßigkeit — Ermessen vollständig überprüfbar |
| 13 | Widerspruchsbehörde zuständig | § 73 VwGO | Ober- oder Aufsichtsbehörde? Oder Ausgangsbehörde selbst? |
| 14 | Hinzuziehungsantrag | §§ 80 VwVfG, Landesrecht | Notwendigkeit des Bevollmächtigten; Kostenfolge |
| 15 | Eilrechtsschutz parallel | §§ 80 Abs. 4, 80 Abs. 5 VwGO | Antrag bei Behörde oder VG |

## Beweislast

| Beweisthema | Beweislastträger | Beweismittel |
|---|---|---|
| Rechtmäßigkeit des Verwaltungsakts | Behörde (trägt Beweislast für anspruchsbegründende Tatsachen) | Verwaltungsakte, Gutachten, Stellungnahmen |
| Fehlende Anhörung § 28 VwVfG | Widerspruchsführer (Rügeobliegenheit) | Akte, eigene Erklärung |
| Mangelhafte Begründung § 39 VwVfG | Widerspruchsführer (aus dem Bescheid ersichtlich) | Bescheid selbst |
| Ermessensfehler | Widerspruchsführer (Rüge) / Behörde (Entlastung) | Begründung des VA, Verwaltungsvorgang |
| Verhältnismäßigkeit | Widerspruchsführer (milderes Mittel behaupten) | Sachverständige, eigene Berechnung |
| Fristversäumnis bei falscher Belehrung | Behörde (muss ordnungsgemäße Belehrung nachweisen) | Zustellungsurkunde, Bescheid |

## Fristen und Verjährung

| Frist | Grundlage | Lauf | Hinweis |
|---|---|---|---|
| Widerspruchsfrist | § 70 Abs. 1 VwGO | 1 Monat ab Bekanntgabe | Bekanntgabe ≠ Zustellung; ggf. Dreitagesfiktion § 41 Abs. 2 VwVfG |
| Verlängerte Widerspruchsfrist | § 58 Abs. 2 VwGO | 1 Jahr bei fehlerhafter oder fehlender Belehrung | Gilt auch bei fehlendem Hinweis auf Adresse der Behörde |
| Klage nach Widerspruch | § 74 VwGO | 1 Monat ab Zustellung Widerspruchsbescheid | Bei Untätigkeit: 3 Monate nach Einlegung Widerspruch → Untätigkeitsklage § 75 VwGO |
| Untätigkeitsklage | § 75 VwGO | 3 Monate nach Einlegung Widerspruch | Bei Fristversäumnis kein Rechtsverlust, aber beachten |
| Heilung formeller Fehler | § 45 Abs. 2 VwVfG | Bis Abschluss letzter Tatsacheninstanz | Behörde kann Anhörung und Begründung nachreichen |
| Verjährung materieller Schadensersatz | § 195 BGB | 3 Jahre ab Kenntnis | Parallelansprüche aus § 839 BGB i.V.m. Art. 34 GG |

## Typische Gegenargumente

| Gegenargument der Behörde | Gegenstrategie |
|---|---|
| "Anhörungsmangel geheilt — Widerspruch ist Nachholung" | § 45 Abs. 1 Nr. 3 VwVfG: Heilung nur durch eigenständige, nicht nur pro forma erfolgte Anhörung; bloße Übersendung des Bescheids genügt nicht |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Widerspruchsverfahren ausgeschlossen" | Landespezifische Ausnahmen genau prüfen; bei Ausschluss nur in bestimmten Sachgebieten prüfen ob hier ein solches vorliegt |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Widerspruch gegen Verwaltungsakt einlegen | Widerspruchsschrift nach Pruefschema; Template unten |
| Variante A — Widerspruchsverfahren nicht Pflicht direkter Klageweg | Klagefrist pruefen; ggf. direkt Anfechtungsklage ohne Widerspruch |
| Variante B — Mandant will Widerspruch nur zur Fristwahrung | Kurzwiderspruch ohne Begruendung zuerst; Begruendung nachreichen |
| Variante C — Behoerde zeigt Kooperationsbereitschaft | Informelles Gespraech vor Widerspruch; Widerspruch als letzte Option |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1: Vollständige Widerspruchsschrift

```
[Kanzlei]
[Anschrift]
[Datum]

An die [Ausgangsbehörde]
[Anschrift]
Aktenzeichen der Behörde: [Az.]

Widerspruch nach § 68 VwGO

In der Verwaltungssache
des [Vorname Name]
[Anschrift]
— Widerspruchsführer —

Verfahrensbevollmächtigte: Rechtsanwältinnen und Rechtsanwälte [Kanzlei]

gegen

den Bescheid der [Behörde] vom [Datum], Aktenzeichen [Az.],
zugestellt am [Datum]

legen wir namens und in Vollmacht des Widerspruchsführers

Widerspruch

ein und beantragen:

1. Den Bescheid vom [Datum] aufzuheben.

2. [Hilfsweise: Bescheid mit folgendem Inhalt zu erlassen: ...]

3. Die Hinzuziehung des Bevollmächtigten für das Vorverfahren
   gemäß § 80 Abs. 2 VwVfG für notwendig zu erklären.

Begründung

I. Zulässigkeit
Der Widerspruch ist nach § 68 VwGO statthaft. Das
Widerspruchsverfahren ist im Land [X] im Sachgebiet [Y]
nicht ausgeschlossen. Der Bescheid wurde dem Widerspruchsführer
am [Datum] zugestellt. Die Widerspruchsfrist von einem Monat
(§ 70 Abs. 1 VwGO) ist daher bis zum [Datum] gewahrt.

II. Formelle Rechtswidrigkeit

1. Anhörungsmangel § 28 VwVfG
Vor Erlass des Bescheids wurde dem Widerspruchsführer keine
Gelegenheit zur Stellungnahme gegeben. Der Widerspruchsführer
hat zu keinem Zeitpunkt eine Anhörungsmitteilung erhalten.
Der Mangel ist beachtlich.

2. Begründungsmangel § 39 VwVfG
Der Bescheid enthält keine ausreichende rechtliche Begründung.
Die Behörde beschränkt sich auf den Hinweis, [Zitat]. Eine
Auseinandersetzung mit den konkreten Umständen des Einzelfalls
fehlt.

III. Materielle Rechtswidrigkeit

1. Tatbestand nicht erfüllt
Die Voraussetzungen des § [X Spezialgesetz] liegen nicht vor.
Die Behörde geht davon aus, dass [Sachverhaltsbehauptung Behörde].
Tatsächlich ist jedoch [zutreffender Sachverhalt]. Dies belegen
[Anlage X].

2. Ermessensfehler § 40 VwVfG / § 114 VwGO
Soweit der Bescheid auf Ermessen gestützt ist, wurde es nicht
oder fehlerhaft ausgeübt:
a) Ermessensnichtgebrauch: aus der Begründung ergibt sich, dass
   die Behörde keine Ermessenserwägungen angestellt hat.
b) Ermessensfehlgebrauch: relevante Belange wie [Belang] wurden
   nicht berücksichtigt.

3. Unverhältnismäßigkeit
Der Eingriff ist nicht verhältnismäßig:
— Geeignetheit: [ggf. bestreiten].
— Erforderlichkeit: Das mildere Mittel [Bezeichnung] wäre ebenso
   wirksam und weniger belastend.
— Angemessenheit: die Schwere des Eingriffs [Beschreibung] überwiegt
   das verfolgte Ziel.

IV. Eilrechtsschutz
Parallel hierzu wird beim Verwaltungsgericht [Ort] ein Antrag nach
§ 80 Abs. 5 VwGO eingereicht, da die sofortige Vollziehung die
[Existenz / wirtschaftliche Grundlage] des Widerspruchsführers
gefährdet.

Mit freundlichen kollegialen Grüßen

Anlagen:
- Bescheid (Anlage W1)
- Vollmacht (Anlage W2)
- Belege Sachverhalt (Anlagen W3 ff.)
```

### Baustein 2: Widerspruch mit Sofortvollzug-Antrag § 80 Abs. 4 VwGO

```
An die [Ausgangsbehörde]

Widerspruch und Antrag auf Aussetzung der sofortigen Vollziehung

I. Widerspruch
[wie Baustein 1]

II. Antrag nach § 80 Abs. 4 VwGO
Wir beantragen zugleich gemäß § 80 Abs. 4 VwGO, die Vollziehung
des angefochtenen Bescheids auszusetzen.

Die sofortige Vollziehung würde [konkrete Folgen schildern].
Angesichts der dargelegten erheblichen Erfolgsaussichten des
Widerspruchs und der schwerwiegenden Konsequenzen der sofortigen
Vollziehung überwiegt das Aussetzungsinteresse des
Widerspruchsführers.

Sollte die Behörde dem Antrag nicht innerhalb von [5] Werktagen
stattgeben, wird der Widerspruchsführer das Verwaltungsgericht
anrufen (§ 80 Abs. 5 VwGO).
```

### Baustein 3: Taktischer Hinweis-Schriftsatz bei drohender Heilung

```
An die [Ausgangsbehörde]

Stellungnahme zur nachgeholten Anhörung

Sehr geehrte Damen und Herren,

wir nehmen Stellung zu Ihrem Schreiben vom [Datum], mit dem Sie
nach Einlegung des Widerspruchs eine Anhörung nachgeholt haben.

1. Wir machen geltend, dass die nachgeholte Anhörung die formelle
   Rechtswidrigkeit des Bescheids im Kern nicht beseitigt, da
   [Begründung: z.B. Ermessenserwägungen grundlegend neu bewertet
   werden müssten / Sachverhalt nicht hinreichend aufgeklärt].

2. Wir halten an dem Widerspruch vollumfänglich fest.

3. Unabhängig von der Frage der Heilung bleibt der Bescheid aus
   den materiellen Gründen (s.o.) rechtswidrig.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Streitwert und Kosten

| Position | Berechnung | Hinweis |
|---|---|---|
| Streitwert Widerspruchsverfahren | § 52 GKG; Auffangwert EUR 5.000; bei beziffertem Anspruch der Anspruchsbetrag | Für Kostenerstattung aus § 80 VwVfG relevant |
| Gebühr Widerspruchsverfahren | Landesgebührenrecht; meist EUR 50–500 bei Abweisung; keine Gebühr bei Abhilfe | Wenn Widerspruch Erfolg hat: Erstattung der anwaltlichen Kosten |
| Hinzuziehungsantrag | § 80 VwVfG; notwendig wenn Sach- und Rechtslage komplex | Ohne Antrag kein Kostenerstattungsanspruch |
| Anwaltsvergütung | RVG Nr. 2300 VV (Geschäftsgebühr); 1,3 bis 2,5-fach je nach Schwierigkeit | Erstattungsfähig bei Obsiegen |
| Kosten Klageverfahren danach | GKG Anlage 1; plus RVG-Gebühren | Widerspruchsverfahren als Sachurteilsvoraussetzung unerlässlich |

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Frist fast abgelaufen | Widerspruch ohne Begründung einlegen; Begründung nachreichen; Fristwahrung hat Vorrang |
| Anhörungsmangel erkannt | Rügen aber beachten: Behörde kann nachholen → eigene Einwendungen früh substanziieren |
| Sofortvollzug angeordnet | § 80 Abs. 4 VwGO-Antrag bei Behörde + § 80 Abs. 5 VwGO parallel VG |
| Ermessensfehler eindeutig | Substanziierte Rüge; keine allgemeine Formulierung; konkrete Erwägungen als fehlend bezeichnen |
| Widerspruchsverfahren ausgeschlossen | Unmittelbar Klage erheben; Frist § 74 VwGO einhalten |
| Chance auf Abhilfe hoch | Frühe Kontaktaufnahme mit Sachbearbeiter; einvernehmliche Lösung suchen; spart Kosten |

## Anschluss-Skills

- `fachanwalt-verwaltungsrecht-einstweiliger-rechtsschutz` — Eilrechtsschutz parallel zum Widerspruch
- `eilantrag-80-abs-5-vwgo` — Vertiefung Schriftsatz § 80 Abs. 5 VwGO
- `energieanlagen-bimschg-genehmigung-verfahren` — Widerspruch gegen BImSchG-Bescheid
- `energietrassen-planfeststellung-rechtsschutz` — Einwendungen im Planfeststellungsverfahren

## Aktuelle Leitentscheidungen (v14.2 Ergaenzung)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen

- VwGO §§ 42, 58, 68–79, 80, 113, 114
- VwVfG §§ 28, 35, 39, 40, 41, 43, 44, 45, 80
- GKG § 52
- RVG Nr. 2300 VV
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

---

## Skill: `fachanwalt-verwaltungsrecht-beamten-disziplinarverfahren`

_Beamten-Disziplinarverfahren führen oder verteidigen: Beamter hat Dienstvergehen begangen oder ist Dienstherr bei Einleitung Disziplinarverfahren. Normen: BBG/BeamtStG, Bundesdisziplinargesetz BDG, Landesdisziplinargesetze. Prüfraster: Dienstvergehen-Tatbestand, Disziplinarmassnahmen (Verweis bis Entfernung aus Beamtenverhältnis), Anhoerung, VG-Klage. Output Anhoerungsschrift, Klageschrift, Verteidigungskonzept. Abgrenzung: Beamtenrecht materiell (Befoerderung, Besoldung) siehe mandat-triage-verwaltungsrecht; Anfechtungsklage allgemein siehe fachanwalt-verwaltungsrecht-anfechtungsklage._

# Beamten-Disziplinarverfahren

## Zweck

Verteidigung Beamten bei Disziplinar-Vorwurf.

## 1) Rechtsgrundlagen

- BBG (Bundesbeamten-Gesetz)
- BeamtStG (Beamtenstatusgesetz)
- Bundes-DG / Landes-DG (Disziplinargesetze)

## 2) Dienstpflicht-Verletzungen

### Beispiele

- Verletzung Verschwiegenheits-Pflicht
- Verspaetete Diensterscheinung
- Drogen-Konsum
- Privat-Strafraten mit Bezug
- Beleidigungen
- Unerlaubte Nebentaetigkeit

### Schwere

- Leichter Verstoß: Verweis
- Mittel: Geldbuße / Kürzung Bezüge
- Schwer: Aberkennung Ruhegehalt
- Sehr schwer: Entfernung aus Dienst

## 3) Disziplinar-Maßnahmen

| Maßnahme | Pflicht-Voraussetzung |
|---|---|
| Verweis | leichter Verstoß |
| Geldbuße | bis 1 Monatsbezüge |
| Kürzung Bezüge | befristet bis 5 Jahre |
| Zurueckstufung | dauerhafte Demotion |
| Entfernung Dienst | schwere Verstöße |
| Aberkennung Ruhegehalt | bei Ruhe-Beamten |

## 4) Verfahren

### Schritt 1 — Voruntersuchung

- Dienstvorgesetzter prüft Vorwurf
- Anhörung Beamter

### Schritt 2 — Förmliches Disziplinarverfahren

- Eröffnung durch Dienstherr
- Ermittlungsfuhrer
- Beweisaufnahme

### Schritt 3 — Disziplinarmaßnahme

- Bescheid mit Begründung
- Bei schwerer Maßnahme: Klage VG Pflicht

### Schritt 4 — Klage VG

- Disziplinargericht (im VG-Gefuege)
- Disziplinarklage Dienstherr
- Vollumfaengliche Prüfung

## 5) Beamten-Strategie

### Sofort-Maßnahmen

- Schweige-Recht (in Disziplinar-Verfahren begrenzt)
- Anwalt einschalten
- Pflicht-Aussage nur zu Sachen, die nicht selbst-belasten

### Vorbereitung

- Akten-Einsicht
- Gegen-Beweise
- Milderungs-Faktoren (Krankheit, Belastung)

### Vergleichs-Möglichkeit

- Einstellung gegen Auflage
- Anwendung Mildere-Maßnahme

## 6) Schwerwiegende Folgen

### Bei Aberkennung Ruhegehalt

- Verlust Pensionsanspruch
- Sozialer Sturz

### Bei Entfernung aus Dienst

- Wegfall Versorgung
- Verlust Status
- Schwere persönliche Folge

## 7) Strafverfahren parallel

### Bei Straf-Tat

- Strafverteidigung im Vorder-Grund
- Disziplinar typisch erst nach Strafurteil
- Bindung Disziplinar-Verfahren an Strafurteil § 22 BDG

### Praxis

- Strafmilderung -> Disziplinar-Erleichterung
- Bei Freispruch: Disziplinar oft eingestellt

## 8) Workflow

### Phase 1 — Erstgespräch

- Vorwurfs-Aufnahme
- Verteidigungs-Strategie

### Phase 2 — Anhörung

- Schriftliche Stellungnahme
- Beweise

### Phase 3 — Bei Bescheid

- Klage Disziplinar-VG
- Frist meist 1 Monat

### Phase 4 — Verhandlung

- Vor Disziplinarkammer
- Beweisaufnahme
- Urteil

## 9) Honorar

- Anwaltsgebuehren nach RVG
- Bei Erfolg: Erstattung durch Dienstherr (begrenzt)
- Beamtenbund-Mitgliedschaft typisch hilfreich

## 10) Typische Fehler

1. **Unüberlegte Aussage** in Voruntersuchung
2. **Klage-Frist 1 Monat verpasst**
3. **Milderungs-Faktoren nicht dargelegt**
4. **Strafverfahren ohne Disziplinar-Beratung**

## 11) BVerwG-Linien

- BVerwG laufende Disziplinar-Rspr.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Aktuelle BVerwG-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Anschluss

- `fachanwalt-verwaltungsrecht-orientierung` — Triage
- `fachanwalt-strafrecht-orientierung` — bei parallelem Strafverfahren
- `widerspruch-oder-klage-erstpruefung` — bei VG-Triage

---

## Skill: `fachanwalt-verwaltungsrecht-drittanfechtung-umwelt`

_Drittanfechtung umweltrechtlicher Genehmigungen (BImSchG, BauGB) durch Nachbarn oder Umweltverband: Klagebefugnis und materielle Gründe prüfen. Normen: § 42 Abs. 2 VwGO (Schutznorm-Theorie), § 5 BImSchG (Nachbarschutz), UmwRG (Verbandsklage), UVP-Pflicht. Prüfraster: Klagebefugnis Dritter, drittschützende Normen, UVP-Fehler, Verbandsklage. Output Klageschrift-Entwurf, Klagebefugungs-Gutachten. Abgrenzung: BImSchG-Genehmigung Betreiber siehe energieanlagen-bimschg-genehmigung-verfahren; Bauleitplanung Normenkontrolle siehe fachanwalt-verwaltungsrecht-normenkontrolle-47-vwgo._

# Drittanfechtung Umwelt-Genehmigung

## Zweck

Klage von Nachbarn / Verbänden gegen umweltrechtliche Genehmigungen.

## 1) Klagebefugnis § 42 II VwGO

### Schutznorm-Theorie

- Norm muss auch Dritten schuetzen
- BImSchG § 5 schuetzt Nachbarn
- Bei reinen Allgemeinwohl-Normen: keine Klagebefugnis

### Bei Verbänden

- Umwelt-Verbands-Klage UmwRG
- Anerkennung BfN

### Praxis-Konstellationen

- Tierhaltungs-Anlage
- Windkraft-Anlage
- Straßen-/Schienen-Planfeststellung
- Industriebetrieb

## 2) Prüfungs-Punkte

### Materiell

- Genehmigungs-Voraussetzungen § 6 BImSchG
- Immissions-Schutz § 5 BImSchG
- UVP-Pflicht
- Naturschutz

### Verfahrens

- Beteiligungs-Verfahren
- Anhörung
- Sachverständigen-Prüfung

### Verfahrensvorschriften

- Vorabbescheid-Aufhebung
- Wesentliche Änderung
- Teil-Genehmigung

## 3) Verfahrens-Vorschriften

### Förmliches Verfahren § 10 BImSchG

- Bekanntmachung
- Auslegung 1 Monat
- Erörterungs-Termin
- Bescheid mit Begründung

### Vereinfachtes Verfahren § 19 BImSchG

- Bei kleineren Anlagen
- Keine Bürgerbeteiligung
- Schneller

## 4) UVP-Prüfung

### Pflicht / Vor-Prüfung

- UVPG Anlage 1
- Schwellenwerte
- Allgemeine UVP / Standortbezogene UVP / Vor-UVP

### Bei Versäumnis

- Genehmigung anfechtbar
- Auflagen-Defizit

## 5) Workflow

### Phase 1 — Bescheid-Prüfung

- Vollständigkeit
- Auflagen
- Begründung

### Phase 2 — Klage-Strategie

- Widerspruchs-Verfahren (Landes-AusfG)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Eilantrag § 80 V VwGO bei Sofortvollzug

### Phase 3 — Beweisaufnahme

- Sachverständigen-Gutachten
- Eigenstudien (Geruch, Larm, Bioaerosole)
- Vergleichs-Anlagen

### Phase 4 — Urteil

- Aufhebung Genehmigung
- Auflagen-Änderung
- Klage abgewiesen

## 6) Aufschiebende Wirkung

### Sofortvollzug § 80 II VwGO

- Bei wirtschaftlicher Bedeutung typisch
- Eilantrag § 80 V VwGO

### Erfolgsaussichten Eil

- Wahrscheinlichkeit Hauptsache-Erfolg
- Eigene Schädigung vs. AG-Interesse

## 7) Verbands-Klage UmwRG

### Voraussetzungen

- BfN-anerkannt
- Klage-Frist 1 Monat
- Beteiligungs-Verfahren genutzt

### Reichweite

- Nicht nur eigene Rechte
- Auch Umweltbelange
- Klimaschutz im aktuellen Fokus

## 8) Typische Fehler

1. **Klagebefugnis nicht ausreichend dargetan**
2. **Eilantrag versäumt** — Anlage geht in Betrieb
3. **Sachverständiger zu spaet**
4. **UVP-Pflicht übersehen**

## 9) BVerwG-Linien

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 10) Honorar

- Streitwert nach wirtschaftlichem Interesse
- Bei Vereinen oft NGO-Finanzierung
- VKH-Antrag möglich

## Aktuelle BVerwG-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Anschluss

- `testakten/umweltrecht-industrieanlage-genehmigung` — bei vertiefter Verteidigung
- `fachanwalt-agrarrecht-tierhaltung-genehmigung` — bei Stallneubau-Bezug
- `fachanwalt-verwaltungsrecht-orientierung` — Triage

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

