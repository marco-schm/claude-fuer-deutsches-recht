# Megaprompt: fachanwalt-migrationsrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 460 Skills (gekuerzt fuer Chat-Fenster) des Plugins `fachanwalt-migrationsrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Fachanwalt Migrationsrecht: ordnet Rolle (Mandant Ausländer/Geflüchteter, ABH, BAMF), m…
2. **mandat-triage-migrationsrecht** — Eingangs-Abfrage für migrationsrechtliche Mandate — Mandant ist Asylsuchender Geduldeter oder fragt nach Aufenthaltstite…
3. **fachanwalt-migrationsrecht-orientierung** — Anwalt will ueberblicken welche Normen und Mandate das Migrationsrecht umfasst oder Fachanwaltschaft vorbereiten. Orient…
4. **orientierung-fachanwaltschaft-mandat** — Anwalt will überblicken welche Normen und Mandate das Migrationsrecht umfasst oder Fachanwaltschaft vorbereiten: Orienti…
5. **erstgespraech-mandatsannahme** — Strukturierter Erstgespraechsleitfaden für Ausländer-, Asyl- und Staatsangehoerigkeitsrecht: Erfassung der Konstellation…
6. **erstpruefung-und-mandatsziel** — Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.
7. **fachanwalt-migrationsrecht-asyl-folgeantrag-71** — Asylantrag wurde abgelehnt und Mandant will neuen Antrag stellen oder hat neue Beweise oder Lage hat sich geaendert. Prü…
8. **fachanwalt-migrationsrecht-familiennachzug** — Mandant will Ehegatten Kinder oder Eltern nach Deutschland holen und fragt nach Voraussetzungen und Verfahren. Prüfraste…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Fachanwalt Migrationsrecht: ordnet Rolle (Mandant Ausländer/Geflüchteter, ABH, BAMF), markiert Frist (§ 74 AsylG Klagefrist 2 Wochen / 1 Mon.), wählt Norm (AufenthG, FreizügG/EU, AsylG, StAG, Aufenthaltsverordnung, EU-Familienzusammenführungs-RL) und Zuständigkeit..._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Fachanwalt Migrationsrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `abschiebehaft-paragraf-62-aufenthg` — Abschiebehaft Paragraf 62 Aufenthg
- `einstieg-schnelltriage-fallrouting` — Abschiebungsabwehr Sofort Arbeitgeber
- `arbeitgeberwechsel` — Arbeitgeberwechsel Asyl Anhoerung Asylg
- `asylantrag-folgeverfahren-paragraf-71-asylg` — Asylantrag Folgeverfahren Paragraf 71 Asylg
- `aufenthalt-paragraf-25a-aufenthg` — Aufenthalt Paragraf 25A Aufenthg
- `aufenthaltstitel-antrag` — Aufenthaltstitel
- `workflow-aufenthaltstitel-router` — Aufenthaltstitel Ausweisung Start
- `aufenthaltstitel-pruefung` — Aufenthaltstitel Erstgespraech Mandatsannahme
- `ausweisung-paragrafe-53-55-aufenthg` — Ausweisung Paragrafe 53 55 Aufenthg
- `ba-zustimmung-beschaeftigung` — BA Zustimmung Beschäftigungsduldung
- `blaue-karte-eu-mobilitaet` — Blaue Karte Bleiberecht 25A Chancenaufenthalt
- `workflow-botschaft-visumtermin` — Botschaft Visumtermin Dokumentenstapel
- `datenschutz-sicherheit-migration` — Datenschutz Sicherheit Daueraufenthalt EU
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Fachanwalt Migrationsrecht sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `mandat-triage-migrationsrecht`

_Eingangs-Abfrage für migrationsrechtliche Mandate — Mandant ist Asylsuchender Geduldeter oder fragt nach Aufenthaltstitel Familiennachzug Abschiebungsabwehr Ausweisung oder Einbuergerung: Eingangs-Abfrage für migrationsrechtliche Mandate — Mandant ist Asyls..._

# Eingangs-Abfrage für migrationsrechtliche Mandate — Mandant ist Asylsuchender Geduldeter oder fragt nach Aufenthaltstitel Familiennachzug Abschiebungsabwehr Ausweisung oder Einbuergerung


## Aktenstart statt Formularstart

Wenn zu **Familiennachzug Orientierung Mandat Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Fachanwalt Migrationsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: AufenthG §§ 4, 5, 7, 8, 9, 16a-16g, 18a-18g, 19c, 25, 27-36, 50, 53-55, 58, 60, 60a-60d, 81, 84, 95; AsylG §§ 13, 24-30, 34-38, 71, 74, 77; FreizügG/EU §§ 2-5; StAG §§ 4, 5, 8-10, 12a, 25, 30; AsylbLG §§ 1, 3, 6; VwGO §§ 74, 80, 123; Dublin-III-VO Art. 3, 17, 21-29; einschlägige EU-Richtlinien/GEAS-Normstand live prüfen; keine BeckRS-/juris-Blindzitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Eingangs-Abfrage für migrationsrechtliche Mandate — Mandant ist Asylsuchender Geduldeter oder fragt nach Aufenthaltstitel Familiennachzug Abschiebungsabwehr Ausweisung oder Einbuergerung. Sofort-Fristen § 74 AsylG zwei-Wochen-Klagefrist § 36 AsylG ein-Wochen-Frist Eilantrag § 80 Abs. 5 VwGO bei Abschiebungsandrohung. Normen AufenthG AsylG § 27 AufenthG Familiennachzug. Eskalation Telefon-Sofort bei Abschiebung in 24 Stunden Haft Dublin-Überstellung. Output Triage-Memo Fristen-Ampel Routing zu aufenthaltstitel-prüfung und Fachmodule. Abgrenzung zu erstgespraech-mandatsannahme (Mandatsaufnahme-Leitfaden).

### Mandat-Triage Migrationsrecht

## Ablauf — sieben Fragen

### Frage 1 — Akute Eilbedürftigkeit?

- **Abschiebung angekündigt / im Gange** — sofortiger Eilrechtsschutz
- **Abschiebungs-Haft** — Haftbeschwerde
- **Dublin-Überstellung** in einen anderen EU-Staat
- **Asylklage-Frist** zwei Wochen § 74 AsylG
- **Visum-Ablehnung** Klage drei Monate / mit Remonstration
- **Ausreisepflicht-Frist abgelaufen**
- **Aktuelle Festnahme** an Grenze oder im Inland

**Bei JA:** Telefon-Sofort an Anwalt — Eilantrag § 80 Abs. 5 VwGO innerhalb Stunden.

### Frage 2 — Mandantenstatus aktuell?

- Asylsuchend (Aufenthaltsgestattung)
- Asyl anerkannt (Aufenthaltserlaubnis nach § 25 AufenthG)
- Subsidiär geschützt
- Abschiebungs-Verbot (§ 60 Abs. 5 oder Abs. 7 AufenthG)
- Geduldet (§ 60a AufenthG)
- Aufenthaltserlaubnis besitzend (Zweck spezifisch)
- Niederlassungserlaubnis
- Daueraufenthalt-EU
- Unerlaubt eingereist / illegal aufhältig
- EU-Bürger Freizügigkeit
- Drittstaatsangehöriger anderweitig

### Frage 3 — Vorgang?

- Asylantrag stellen
- Asyl-Folgeantrag § 71 AsylG
- Asyl-Klage gegen BAMF
- Visum-Erteilung beantragen / klagen
- Aufenthaltstitel-Verlängerung
- Niederlassungserlaubnis beantragen
- Familiennachzug-Verfahren
- Abschiebung verhindern / Eilrechtsschutz
- Duldung beantragen § 60a AufenthG
- Einbürgerung
- Ausweisung anfechten
- Identitätsklärung
- Dublin-Verfahren

### Frage 4 — Stand des Verfahrens?

- Antrag noch nicht gestellt — Beratungsbedarf
- Antrag gestellt — wartet auf Bescheid
- Anhörung BAMF Ausländerbehörde
- Bescheid liegt vor — Klagefrist offen
- Klage erhoben (Az VG)
- Berufung / OVG
- Eilantrag § 80 Abs. 5 VwGO oder § 123 VwGO
- Bundesverfassungsgericht Verfassungsbeschwerde

### Frage 5 — Familienverhältnisse?

- Familie in Deutschland (Ehegatte Kinder)
- Familie im Herkunftsland
- Minderjährig
- Familien-Asylanerkennung § 26 AsylG
- Beistandsgemeinschaft mit deutschen Familienangehörigen
- Kindeswohl

### Frage 6 — Frist?

- **Asylklage** zwei Wochen § 74 AsylG
- **Asyl-Eilantrag** bei sofortiger Vollziehung sofort
- **Visum-Remonstration** keine Frist aber zeitnah
- **Klage gegen Visum-Versagung** ein Monat § 74 VwGO
- **Aufenthaltstitel-Antrag** vor Ablauf des bestehenden Titels — fiktive Fortgeltung § 81 Abs. 4 AufenthG
- **Einbürgerungs-Frist** keine

### Frage 7 — Sprache und Dolmetscher?

- Muttersprache
- Deutsch-Kenntnisse
- Dolmetscher-Bedarf für Mandantengespräch
- Mandanten-Dokumente Übersetzungsbedarf

## Routing-Matrix

| Vorgang | Folge-Skill |
|---|---|
| Aufenthaltstitel-Verlängerung / Neuantrag | `aufenthaltstitel-pruefung` |
| Asylantrag / Klage | (Skill asyl-anhoerung-und-klage — perspektivisch) |
| Visum-Klage | weiter an `mandat-triage-verwaltungsrecht` plus Migrationsspezifikum |
| Familiennachzug | `aufenthaltstitel-pruefung` plus Familiennachzugs-Schwerpunkt |
| Abschiebung-Eilrechtsschutz | EILMODUS sofort |
| Ausweisung anfechten | (Skill ausweisung-anfechten — perspektivisch) |
| Einbürgerung | (Skill einbürgerung-staag — perspektivisch) |

## Eilmodus Abschiebung

Bei drohender Abschiebung:

1. Sofort Mandant identifizieren — wo? Abschiebehaft / Ausreise gefordert?
2. Ausländerakte-Auskunft sofort beantragen
3. Eilantrag VG § 123 VwGO mit Sofortvollziehbarkeits-Aussetzung
4. Hilfsweise Verfassungsbeschwerde
5. Folgeantrag § 71 AsylG wenn neue Tatsachen / Beweise
6. Petition Härtefall-Kommission

## Mandatsannahme

- **Konflikt-Check** — keine Doppelvertretung Behörde / Mandant
- **Prozesskostenhilfe** § 166 VwGO iVm § 114 ZPO häufig
- **Streitwert** § 52 GKG Asyl typisch EUR 5000
- **Beratungshilfe** außergerichtlich
- **Sprache** Dolmetscher

## Eskalation

- **Telefon-Sofort** Abschiebung morgen Überstellung Dublin morgen Festnahme Grenze
- **Binnen einer Stunde** Eilantrag § 80 Abs. 5 VwGO
- **Heute** Asyl-Klage Frist zwei Wochen
- **Diese Woche** Aufenthaltstitel-Antrag Niederlassungs-Antrag

## Ausgabe

- `triage-protokoll-migrationsrecht.md`
- Aktenanlage mit Sprache und Dolmetscher-Bedarf
- Frist im Fristenbuch (Asyl zwei Wochen Klage ein Monat)
- PKH-Antrag-Entwurf
- Mandatsvereinbarung
- Empfehlung Folge-Skill plus eventuell Härtefall-Kommission

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen

- AufenthG AsylG StAG VwGO §§ 80 123
- DublinIII-VO (EU) 604/2013
- BVerwGE Std.Spruch
- Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle; keine Kommentarblindzitate.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Vertiefung: Rechtsprechung und Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen-Kette Triage

- **§ 36 AsylG** — 1-Woche-Klagefrist bei offensichtlich unbegruedet; § 74 Abs. 1 AsylG — 2-Wochen-Klagefrist
- **§§ 80 Abs. 5, 123 VwGO** — Eilrechtsschutzoptionen
- **§ 52 GKG** — Streitwert (Abs. 2: EUR 5.000 Regelwert Asyl)
- **§ 83b AsylG** — Gerichtskostenfreiheit im Asylverfahren
- **§§ 166 VwGO, 114 ZPO** — PKH im Verwaltungsverfahren
- **§ 71 AsylG** — Folgeantrag bei Wiederaufgreifensgruenden

## Output-Template: Triage-Protokoll Migrationsrecht

**Adressat:** Kanzlei-intern
**Tonfall:** Strukturiert; aktionsorientiert

```
TRIAGE-PROTOKOLL MIGRATIONSRECHT
Datum: [DATUM] — Anruf / Walk-in / E-Mail
Bearbeiterin: [RA-NAME]

1. MANDANT
Name: [NAME, geb. DATUM, Staatsang.]
Aufenthaltsstatus: [Gestattung / Duldung / AE § X / NE / illegal]
Sprache / Dolmetscher: [SPRACHE; Dolmetscher erforderlich: ja/nein]

2. AKUTE EILBEDUERFTIGKEIT (Checkboxen)
[ ] Abschiebung angekuendigt — Datum: [...]
[ ] Asylklage-Frist 2 Wochen — laeuft ab: [DATUM]
[ ] § 36 AsylG 1-Woche-Frist — laeuft ab: [DATUM]
[ ] Dublin-Ueberstellung droht
[ ] Abschiebehaft
[ ] Sonstige Eilbeduerftigkeit: [...]

3. VORGANG
[ ] Asylantrag / BAMF-Anhörung
[ ] Asyl-Klage
[ ] Folgeantrag § 71 AsylG
[ ] Aufenthaltstitel-Antrag / Verlaengerung
[ ] Familiennachzug
[ ] Abschiebungsabwehr Eilantrag
[ ] Ausweisung Widerspruch
[ ] Einbuergerung
[ ] Grenzverfahren GEAS

4. FRISTEN IM KALENDER
Naechste Frist: [DATUM — Art der Frist]
PKH-Antrag: [gestellt / noch nicht / nicht erforderlich]

5. ROUTING
Folge-Skill: [konkreter naechster Migrationsrecht-Skill, z.B. BAMF-Anhoerung, Asylklage, Familiennachzug, Aufenthaltstitel, Abschiebungsschutz, Ausweisung oder Einbuergerung]
Eskalation: [ ] Sofort-Telefon [ ] Heute [ ] Diese Woche

Aktennummer: [AZ]
```

---

## Skill: `fachanwalt-migrationsrecht-orientierung`

_Anwalt will ueberblicken welche Normen und Mandate das Migrationsrecht umfasst oder Fachanwaltschaft vorbereiten. Orientierung AufenthG AsylG GFK Genfer Fluechtlingskonvention 1951 Dublin-VO EU-Verfahrens-RL Qualifikations-RL 2011/95 StAG Einbuergerung. Notfristen § 36 AsylG ein-Wochen-Frist bei ablehnenden BAMF-Bescheiden § 74 AsylG zwei-Wochen-Klagefrist. FAO-Voraussetzungen Normen typische Mandate verifizierbare Quellen. Output Orientierungs-Übersicht mit Norm-Landkarte und Routing zu Spezial-Skills. Abgrenzung: mandat-triage-migrationsrecht für konkreten Mandats-Einstieg._

# Fachanwalt für Migrationsrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 50 Fälle in den letzten drei Jahren, davon mindestens 30 streitige Verfahren.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Aufenthaltsrecht | AufenthG §§ 1 ff. (Aufenthaltstitel) § 60 (Abschiebungsverbote) § 25 (humanitaer) § 81 (Antragstellung Fiktionswirkung) |
| Asylrecht | AsylG §§ 3 ff. (Fluechtlingsstatus) § 4 (subsidiaerer Schutz) § 36 (beschleunigtes Verfahren) § 74 (Klagefrist) |
| Genfer Konvention | GFK 1951 Art. 1A (Fluechtlingsbegriff) Art. 33 Refoulementverbot |
| EU-Recht | Dublin III VO (EU 604/2013) Qualifikations-RL 2011/95 Verfahrens-RL 2013/32 Aufnahme-RL 2013/33 Rückführungs-RL 2008/115 |
| Staatsangehoerigkeit | StAG (Einbürgerung Anspruchseinbürgerung Ermessenseinbürgerung) |
| Beschaeftigungsmigration | Beschaeftigungsverordnung BeschV Fachkraefteeinwanderungsgesetz |
| Verfahrensrecht | VwGO (Klage gegen BAMF / Ausländerbehörde) AsylG (Sonderverfahren) |

## Typische Mandate

- Asylantrag und Asylklage
- Aufenthaltstitel-Verlängerung und -Versagung
- Abschiebungsverfahren Eilrechtsschutz § 80 Abs. 5 VwGO / § 123 VwGO
- Familiennachzug §§ 27 ff. AufenthG
- Einbürgerung StAG §§ 10 ff. (acht Jahre / verkürzbar)
- Aufenthaltsverfestigung (Niederlassungserlaubnis Daueraufenthalt EU)
- Duldung § 60a AufenthG
- Ausländerrecht und Strafrecht (Ausweisung nach Straftat)
- Dublin-Verfahren Überstellung in anderen EU-Mitgliedstaat

## Notfristen

- **Klagefrist § 36 AsylG-Bescheid** — **eine Woche** ab Bekanntgabe.
- **Klagefrist sonstiger Asyl-Bescheid** zwei Wochen oder ein Monat je nach Bescheidart.
- **Klage Ausländerbehörde** ein Monat (§ 74 VwGO).
- **Eilrechtsschutz** sofort bei drohender Abschiebung.
- **Wiedereinsetzung** § 60 VwGO zwei Wochen.

## Hauptgerichte

- Verwaltungsgericht — Asyl- und Ausländerrecht.
- OVG / VGH — Berufung Berufungszulassung.
- BVerwG Leipzig — Revision.
- EuGH — Vorabentscheidung bei EU-rechtlichen Fragen.
- EGMR — Strassburg bei Konventionsverletzungen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- ARGE Migrationsrecht DAV.
- Pro Asyl als Fachöffentlichkeit.

## Schnittstellen

- **rechtsberatungsstelle** bei pro-bono-Beratungsstellen.
- **fachanwalt-verwaltungsrecht** bei VG-Verfahren.
- **kanzlei-allgemein** Notfristen Versand.
- **fachanwalt-strafrecht** bei Ausweisung nach Straftat.

## Vertiefung: Rechtsprechung und Leitsaetze

Rechtsprechung im Mandat live verifizieren. Aktuelle Linien zur Orientierung (Stand 05/2026):

- EuGH, Urt. v. 05.03.2026 — C-458/24 (Daraa) — Zuständigkeitsübergang nach Dublin III, wenn der ersuchende Mitgliedstaat die Überstellung binnen 6 Monaten nicht durchführt; einseitige Erklärung Italiens ohne Rücküberstellungsfähigkeit nicht ausreichend für automatischen Übergang. Verifikation über [curia.europa.eu](https://curia.europa.eu/).
- GEAS-Reform: Asylverfahrensverordnung (EU) 2024/1348, Grenzverfahrensverordnung (EU) 2024/1349, Asyl- und Migrationsmanagementverordnung (EU) 2024/1351, Screening-VO (EU) 2024/1356, Qualifikations-VO (EU) 2024/1347, EURODAC-VO (EU) 2024/1358, Krisen-VO (EU) 2024/1359. **Anwendbarkeit ab 12.06.2026.** Stichtagsregelung: Verfahrensrecht (Art. 79 Abs. 3 AVV-VO) gilt für ab dem 12.06.2026 eingereichte Anträge; materielles Statusrecht (Qualifikations-VO) gilt mangels Übergangsregelung ab 12.06.2026 auch in laufenden Altverfahren.
- BVerfG, Beschluss vom 14.11.2024 — 1 BvL 3/22 (PolG NRW Observation) — Spillover ins Migrationsrecht relevant bei Datenverarbeitung über Schutzsuchende.

## Normen-Kette Migrationsrecht

- **AsylG §§ 3, 3a, 3b, 4** — Fluchtlingsstatus, Verfolgungshandlungen/-gruende, subsidiaerer Schutz
- **AufenthG §§ 25, 60, 60a, 81** — Humanitaere Aufenthaltstitel, Abschiebungsverbote, Duldung, Fiktionswirkung Antrag
- **§§ 74 AsylG, 74 VwGO, 36 AsylG** — Klagefristen (1 Woche / 2 Wochen / 1 Monat)
- **VwGO §§ 80 Abs. 5, 123** — Eilrechtsschutz aufschiebende Wirkung und einstweilige Anordnung
- **Dublin III-VO (EU) 604/2013** Art. 3 Abs. 2 — systemische Maengel; Art. 17 — Selbsteintrittsrecht
- **GFK 1951** Art. 1A Fluechtlingsbegriff; Art. 33 Refoulementverbot

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage vor Bearbeitung

Bevor losgelegt wird, klaere:
1. Akute Frist — §-36-AsylG-1-Woche-Frist bereits angelaufen? Wenn ja: Sofort-Eilantrag.
2. Mandantenstatus exakt — Aufenthaltsgestattung, Duldung, bestehender Titel, EU-Buerger?
3. Besteht bereits Bescheid — BAMF oder Auslaenderbehoerde?
4. Familienangehoerige in Deutschland mit Titel — Relevant fuer Art. 6 GG / § 60a AufenthG?
5. Gesundheitszustand Mandant — Attests-Bedarf fuer Reiseunfaehigkeit / psych. Erkrankung?

## Output-Template: Orientierungs-Memo Migrationsrecht

**Adressat:** Mandant (zur persoenlichen Erklaerung) oder internes Kanzlei-Memo
**Tonfall:** Verstaendlich-erklaerend

```
ORIENTIERUNGS-MEMO MIGRATIONSRECHT
Kanzlei: [KANZLEI]
Mandant: [NAME, GEBURTSDATUM, NATIONALITAET]
Datum: [DATUM]

1. AKTUELLER STATUS
   Aufenthaltsstatus: [Gestattung / Duldung / AE § ... / NE]
   Laufendes Verfahren: [BAMF-Az. / VG-Az.]

2. MOEGLICHE ANSPRUECHE / ROUTEN
   a) Asylrechtliche Route: [Erstantrag / Folgeantrag § 71 AsylG / Klage]
   b) Humanitaerer Aufenthaltstitel: [§ 25 Abs. ... AufenthG]
   c) Abschiebungsschutz: [§ 60 Abs. 5 / Abs. 7 AufenthG / § 60a]
   d) Familiennachzug: [§§ 27 ff. AufenthG — Grundvoraussetzungen gegeben?]

3. NAECHSTE SCHRITTE
   - [Schritt 1 mit Frist und Verantwortlichem]
   - [Schritt 2]

4. FRISTEN
   Naechste Klagefrist: [DATUM]
   Titelablauf: [DATUM]

5. KOSTEN
   PKH-Antrag: [gestellt / noch nicht gestellt / nicht erforderlich]
   Beratungshilfe: [ja / nein]
```

<!-- AUDIT 27.05.2026
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Fehler: Skill behauptete das Urteil betreffe AsylRL/DublinVO — falsch.
Tatsaechlicher Gegenstand: ne bis in idem (Art. 50 GRCh) im Steuerstrafrecht
(Steuerhinterziehung, Doppelbestrafung durch steuerliche und strafrechtliche Sanktionen).
Der allgemeine Grundsatz zu Art. 51 GRCh (Anwendungsbereich der Charta) ist korrekt
und fuer das Migrationsrecht methodisch relevant; Urteil verifiziert auf
dejure.org/2013,2363 (NJW 2013, 1415).
-->

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `orientierung-fachanwaltschaft-mandat`

_Anwalt will überblicken welche Normen und Mandate das Migrationsrecht umfasst oder Fachanwaltschaft vorbereiten: Orientierung AufenthG AsylG G..._

# Anwalt will überblicken welche Normen und Mandate das Migrationsrecht umfasst oder Fachanwaltschaft vorbereiten


## Aktenstart statt Formularstart

Wenn zu **Familiennachzug Orientierung Mandat Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Fachanwalt Migrationsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: AufenthG §§ 4, 5, 7, 8, 9, 16a-16g, 18a-18g, 19c, 25, 27-36, 50, 53-55, 58, 60, 60a-60d, 81, 84, 95; AsylG §§ 13, 24-30, 34-38, 71, 74, 77; FreizügG/EU §§ 2-5; StAG §§ 4, 5, 8-10, 12a, 25, 30; AsylbLG §§ 1, 3, 6; VwGO §§ 74, 80, 123; Dublin-III-VO Art. 3, 17, 21-29; einschlägige EU-Richtlinien/GEAS-Normstand live prüfen; keine BeckRS-/juris-Blindzitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Anwalt will überblicken welche Normen und Mandate das Migrationsrecht umfasst oder Fachanwaltschaft vorbereiten. Orientierung AufenthG AsylG GFK Genfer Fluechtlingskonvention 1951 Dublin-VO EU-Verfahrens-RL Qualifikations-RL 2011/95 StAG Einbuergerung. Notfristen § 36 AsylG ein-Wochen-Frist bei ablehnenden BAMF-Bescheiden § 74 AsylG zwei-Wochen-Klagefrist. FAO-Voraussetzungen Normen typische Mandate verifizierbare Quellen. Output Orientierungs-Übersicht mit Norm-Landkarte und Routing zu Fachmodule. Abgrenzung: mandat-triage-migrationsrecht für konkreten Mandats-Einstieg.

### Fachanwalt für Migrationsrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 50 Fälle in den letzten drei Jahren, davon mindestens 30 streitige Verfahren.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Aufenthaltsrecht | AufenthG §§ 1 ff. (Aufenthaltstitel) § 60 (Abschiebungsverbote) § 25 (humanitaer) § 81 (Antragstellung Fiktionswirkung) |
| Asylrecht | AsylG §§ 3 ff. (Fluechtlingsstatus) § 4 (subsidiaerer Schutz) § 36 (beschleunigtes Verfahren) § 74 (Klagefrist) |
| Genfer Konvention | GFK 1951 Art. 1A (Fluechtlingsbegriff) Art. 33 Refoulementverbot |
| EU-Recht | Dublin III VO (EU 604/2013) Qualifikations-RL 2011/95 Verfahrens-RL 2013/32 Aufnahme-RL 2013/33 Rückführungs-RL 2008/115 |
| Staatsangehoerigkeit | StAG (Einbürgerung Anspruchseinbürgerung Ermessenseinbürgerung) |
| Beschäftigungsmigration | Beschäftigungsverordnung BeschV Fachkraefteeinwanderungsgesetz |
| Verfahrensrecht | VwGO (Klage gegen BAMF / Ausländerbehörde) AsylG (Sonderverfahren) |

## Typische Mandate

- Asylantrag und Asylklage
- Aufenthaltstitel-Verlängerung und -Versagung
- Abschiebungsverfahren Eilrechtsschutz § 80 Abs. 5 VwGO / § 123 VwGO
- Familiennachzug §§ 27 ff. AufenthG
- Einbürgerung StAG §§ 10 ff. (acht Jahre / verkürzbar)
- Aufenthaltsverfestigung (Niederlassungserlaubnis Daueraufenthalt EU)
- Duldung § 60a AufenthG
- Ausländerrecht und Strafrecht (Ausweisung nach Straftat)
- Dublin-Verfahren Überstellung in anderen EU-Mitgliedstaat

## Notfristen

- **Klagefrist § 36 AsylG-Bescheid** — **eine Woche** ab Bekanntgabe.
- **Klagefrist sonstiger Asyl-Bescheid** zwei Wochen oder ein Monat je nach Bescheidart.
- **Klage Ausländerbehörde** ein Monat (§ 74 VwGO).
- **Eilrechtsschutz** sofort bei drohender Abschiebung.
- **Wiedereinsetzung** § 60 VwGO zwei Wochen.

## Hauptgerichte

- Verwaltungsgericht — Asyl- und Ausländerrecht.
- OVG / VGH — Berufung Berufungszulassung.
- BVerwG Leipzig — Revision.
- EuGH — Vorabentscheidung bei EU-rechtlichen Fragen.
- EGMR — Strassburg bei Konventionsverletzungen.

## Berufsverband

- ARGE Migrationsrecht DAV.
- Pro Asyl als Fachöffentlichkeit.

## Schnittstellen

- **rechtsberatungsstelle** bei pro-bono-Beratungsstellen.
- **fachanwalt-verwaltungsrecht** bei VG-Verfahren.
- **kanzlei-allgemein** Notfristen Versand.
- **fachanwalt-strafrecht** bei Ausweisung nach Straftat.

## Vertiefung: Rechtsprechung und Leitsaetze

Rechtsprechung im Mandat live verifizieren. Aktuelle Linien zur Orientierung (Stand 05/2026):

- EuGH, Urt. v. 05.03.2026 — C-458/24 (Daraa) — Zuständigkeitsübergang nach Dublin III, wenn der ersuchende Mitgliedstaat die Überstellung binnen 6 Monaten nicht durchführt; einseitige Erklärung Italiens ohne Rücküberstellungsfähigkeit nicht ausreichend für automatischen Übergang. Verifikation über [curia.europa.eu](https://curia.europa.eu/).
- GEAS-Reform: Asylverfahrensverordnung (EU) 2024/1348, Grenzverfahrensverordnung (EU) 2024/1349, Asyl- und Migrationsmanagementverordnung (EU) 2024/1351, Screening-VO (EU) 2024/1356, Qualifikations-VO (EU) 2024/1347, EURODAC-VO (EU) 2024/1358, Krisen-VO (EU) 2024/1359. **Anwendbarkeit ab 12.06.2026.** Stichtagsregelung: Verfahrensrecht (Art. 79 Abs. 3 AVV-VO) gilt für ab dem 12.06.2026 eingereichte Anträge; materielles Statusrecht (Qualifikations-VO) gilt mangels Übergangsregelung ab 12.06.2026 auch in laufenden Altverfahren.
- BVerfG, Beschluss vom 14.11.2024 — 1 BvL 3/22 (PolG NRW Observation) — Spillover ins Migrationsrecht relevant bei Datenverarbeitung über Schutzsuchende.

## Normen-Kette Migrationsrecht

- **AsylG §§ 3, 3a, 3b, 4** — Fluchtlingsstatus, Verfolgungshandlungen/-gruende, subsidiaerer Schutz
- **AufenthG §§ 25, 60, 60a, 81** — Humanitaere Aufenthaltstitel, Abschiebungsverbote, Duldung, Fiktionswirkung Antrag
- **§§ 74 AsylG, 74 VwGO, 36 AsylG** — Klagefristen (1 Woche / 2 Wochen / 1 Monat)
- **VwGO §§ 80 Abs. 5, 123** — Eilrechtsschutz aufschiebende Wirkung und einstweilige Anordnung
- **Dublin III-VO (EU) 604/2013** Art. 3 Abs. 2 — systemische Maengel; Art. 17 — Selbsteintrittsrecht
- **GFK 1951** Art. 1A Fluechtlingsbegriff; Art. 33 Refoulementverbot

## Triage vor Bearbeitung

Bevor losgelegt wird, klaere:
1. Akute Frist — §-36-AsylG-1-Woche-Frist bereits angelaufen? Wenn ja: Sofort-Eilantrag.
2. Mandantenstatus exakt — Aufenthaltsgestattung, Duldung, bestehender Titel, EU-Buerger?
3. Besteht bereits Bescheid — BAMF oder Ausländerbehoerde?
4. Familienangehoerige in Deutschland mit Titel — Relevant für Art. 6 GG / § 60a AufenthG?
5. Gesundheitszustand Mandant — Attests-Bedarf für Reiseunfaehigkeit / psych. Erkrankung?

## Output-Template: Orientierungs-Memo Migrationsrecht

**Adressat:** Mandant (zur persönlichen Erklaerung) oder internes Kanzlei-Memo
**Tonfall:** Verstaendlich-erklaerend

```
ORIENTIERUNGS-MEMO MIGRATIONSRECHT
Kanzlei: [KANZLEI]
Mandant: [NAME, GEBURTSDATUM, NATIONALITAET]
Datum: [DATUM]

1. AKTUELLER STATUS
 Aufenthaltsstatus: [Gestattung / Duldung / AE § ... / NE]
 Laufendes Verfahren: [BAMF-Az. / VG-Az.]

2. MOEGLICHE ANSPRUECHE / ROUTEN
 a) Asylrechtliche Route: [Erstantrag / Folgeantrag § 71 AsylG / Klage]
 b) Humanitaerer Aufenthaltstitel: [§ 25 Abs. ... AufenthG]
 c) Abschiebungsschutz: [§ 60 Abs. 5 / Abs. 7 AufenthG / § 60a]
 d) Familiennachzug: [§§ 27 ff. AufenthG — Grundvoraussetzungen gegeben?]

3. NAECHSTE SCHRITTE
 - [Schritt 1 mit Frist und Verantwortlichem]
 - [Schritt 2]

4. FRISTEN
 Naechste Klagefrist: [DATUM]
 Titelablauf: [DATUM]

5. KOSTEN
 PKH-Antrag: [gestellt / noch nicht gestellt / nicht erforderlich]
 Beratungshilfe: [ja / nein]
```

<!-- AUDIT 27.05.2026
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Fehler: Skill behauptete das Urteil betreffe AsylRL/DublinVO — falsch.
Tatsaechlicher Gegenstand: ne bis in idem (Art. 50 GRCh) im Steuerstrafrecht
(Steuerhinterziehung, Doppelbestrafung durch steuerliche und strafrechtliche Sanktionen).
Der allgemeine Grundsatz zu Art. 51 GRCh (Anwendungsbereich der Charta) ist korrekt
und für das Migrationsrecht methodisch relevant; Urteil verifiziert auf
dejure.org/2013,2363 (NJW 2013, 1415).
-->

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `erstgespraech-mandatsannahme`

_Strukturierter Erstgespraechsleitfaden für Ausländer-, Asyl- und Staatsangehoerigkeitsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen: Strukturierter Erstge..._

# Strukturierter Erstgespraechsleitfaden für Ausländer-, Asyl- und Staatsangehoerigkeitsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: AufenthG §§ 4, 5, 7, 8, 9, 16a-16g, 18a-18g, 19c, 25, 27-36, 50, 53-55, 58, 60, 60a-60d, 81, 84, 95; AsylG §§ 13, 24-30, 34-38, 71, 74, 77; FreizügG/EU §§ 2-5; StAG §§ 4, 5, 8-10, 12a, 25, 30; AsylbLG §§ 1, 3, 6; VwGO §§ 74, 80, 123; Dublin-III-VO Art. 3, 17, 21-29; einschlägige EU-Richtlinien/GEAS-Normstand live prüfen; keine BeckRS-/juris-Blindzitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierter Erstgespraechsleitfaden für Ausländer-, Asyl- und Staatsangehoerigkeitsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.

### Erstgespraech und Mandatsannahme im Ausländer-, Asyl- und Staatsangehoerigkeitsrecht

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Ausländer-, Asyl- und Staatsangehoerigkeitsrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klären, Konflikt- und GwG-Prüfung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Ausländer-, Asyl- und Staatsangehoerigkeitsrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klägerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Aufenthaltstitel, Asyl, Abschiebung, Einbuergerung, FamNachzug, FreizuegigG/EU
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Klage VG (Asyl/AufenthG), Eilantrag § 80 Abs. 5 VwGO, Einbuergerungsklage). Frist-Alarm an die Vorbereitung weitergeben.

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

Standard-Streitwerte im Bereich Ausländer-, Asyl- und Staatsangehoerigkeitsrecht:

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

- BORA, BRAO, FAO für Fachanwaltschaft Ausländer-, Asyl- und Staatsangehoerigkeitsrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- AufenthG, AsylG, StAG, FreizuegigG/EU, BeschV, EU-RL 2008/115/EG (für fachliche Erstpruefung).
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

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Ausländer-, Asyl- und Staatsangehoerigkeitsrecht). Handlungs-Sequenz:

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
- Verfahrensdauer im Bereich Ausländer-, Asyl- und Staatsangehoerigkeitsrecht: Erfahrungswerte nach Instanz.
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

## Cross-Refs

- `vergleichsverhandlung-strategie` (im selben Plugin) für den Fall, dass aussergerichtliche Loesung angestrebt wird.
- `schriftsatzkern-substantiierung` (im selben Plugin) für den Schriftsatzaufbau, wenn Klage/Widerspruch eingereicht wird.
- Kanzlei-Allgemein-Plugin `kanzlei-allgemein` für Konflikt-, GwG- und PEP-Prüfroutinen.

## Vertiefung: Rechtsprechung und Normen (Migrationsrecht Mandatsannahme)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen-Kette Erstgespraech

- **§ 10 ff. GwG** — Sorgfaltspflichten und Identifizierung; § 2 Abs. 1 Nr. 10 GwG — Anwendung auf RA-Mandate
- **§ 43a Abs. 4 BRAO / § 3 BORA** — Interessenkonflikt; Doppelvertretung verboten
- **§ 3a RVG** — Honorarvereinbarung; Schriftform; Trennungsgebot RVG-Gebühren / Stundensatz
- **§§ 166 VwGO, 114 ZPO** — Prozesskostenhilfe im Verwaltungsverfahren
- **§ 52 GKG** — Streitwert; Abs. 2 Regelstreitwert 5.000 EUR für Asylklage
- **§ 25 Abs. 6 AsylG** — Recht auf anwaltlichen Beistand bei BAMF-Anhörung

---

## Skill: `erstpruefung-und-mandatsziel`

_Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: AufenthG §§ 4, 5, 7, 8, 9, 16a-16g, 18a-18g, 19c, 25, 27-36, 50, 53-55, 58, 60, 60a-60d, 81, 84, 95; AsylG §§ 13, 24-30, 34-38, 71, 74, 77; FreizügG/EU §§ 2-5; StAG §§ 4, 5, 8-10, 12a, 25, 30; AsylbLG §§ 1, 3, 6; VwGO §§ 74, 80, 123; Dublin-III-VO Art. 3, 17, 21-29; einschlägige EU-Richtlinien/GEAS-Normstand live prüfen; keine BeckRS-/juris-Blindzitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** AufenthG, AsylG, GFK, VO, RL, StAG, EU.

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

## Qualitätsanker: Identität, Schutzstatus und aktuelle Lageprüfung

- **Verifizierte Rechtsprechungsanker:** BVerwG, Urteil vom 13.12.2023 - 1 C 34.22 und BVerwG, Urteil vom 18.12.2025 - 1 C 27.24 zur Identitätsklärung/Stufenmodell im Einbürgerungsrecht; BVerwG, Urteil vom 16.04.2025 - 1 C 18.24 zur Tatsachenrevision und Art. 4 GRCh/Art. 3 EMRK bei anerkannten Schutzberechtigten in Griechenland.
- **Prüfdisziplin:** Aufenthaltsrecht, Asylrecht, Staatsangehörigkeitsrecht, Freizügigkeit/EU, Dublin/GEAS, Abschiebungsschutz, Familiennachzug und Arbeit/Beschäftigung strikt trennen. Keine Auskunft „nach Gefühl“ über Länderpraxis oder Behördenlaufzeiten.
- **Aktualitätsfilter:** Herkunftsland, Schutzstatus, Dokumentenlage, Identität, Passbeschaffung, Zumutbarkeit, Vulnerabilität und aktuelle Lageberichte/live verfügbare Gerichtsquellen sind tragend; bei Lagefragen immer Datum und Erkenntnisbasis nennen.
- **Output-Pflicht:** Entscheidungsbaum mit Sofortfrist, zuständiger Behörde/Gericht, benötigten Unterlagen, Beweisnot-/Zumutbarkeitsargumenten und nächstem rechtssicheren Schritt.

---

## Skill: `fachanwalt-migrationsrecht-asyl-folgeantrag-71`

_Asylantrag wurde abgelehnt und Mandant will neuen Antrag stellen oder hat neue Beweise oder Lage hat sich geaendert. Prüfraster § 71 AsylG Folgeantrag Voraussetzungen Wiederaufgreifensgründe Aenderung Sachlage neue Beweismittel. Frist drei Monate ab Kenntnis der neuen Umstaende Folge-Folgeantrag Dublin-III-Überstellungs-Sperre. Output Folgeantrag-Entwurf mit Begründung neuer Umstaende und Sperr-Argument für Dublin-Überstellung. Abgrenzung: asyl-anhoerung-vorbereiten für Erst-Anhoerung fachanwalt-migrationsrecht-abschiebungsabwehr bei unmittelbarer Gefahr._

# Asyl-Folgeantrag § 71 AsylG

## Zweck

Antrag nach Ablehnung des Erstantrags — nur unter strengen Voraussetzungen.

## 1) Eingangs-Abfrage

1. Erster Asylantrag wann abgelehnt?
2. Aktueller Aufenthaltstitel / Duldung?
3. Neue Sachlage seit Ablehnung (politische Lage Heimatland, persönliche Änderungen)?
4. Neue Beweismittel?
5. Ausreise-Druck (Abschiebung)?

## 2) Voraussetzungen § 71 AsylG iVm § 51 VwVfG

### Wiederaufgreifens-Gründe

- **Änderung Sachlage** (Heimatland, persönlich)
- **Neue Beweismittel**, die zu günstigerer Entscheidung geführt hätten
- **Änderung Rechtslage**

### Frist

- 3 Monate ab Kenntnis des Wiederaufgreifens-Grundes
- Bei Versäumnis: Antrag unzulaessig

### Ergebnis

- BAMF prüft zunächst Zulässigkeit
- Bei Zulässigkeit: Sach-Prüfung wie Erstantrag

## 3) Sachverhalts-Schwerpunkte

### Politische Lage

- Verschlechterung Heimatland (Krieg, Verfolgung)
- Neue Verfolgungs-Gruppen
- Anderer Aspekt (z.B. Sexual-Orientierung outet sich)

### Persönlich

- Konvertierung Religion
- Politische Aktivitäten während Aufenthalt
- Familien-Konstellation

### Beweise

- Neue Dokumente (Drohbriefe, Steckbriefe)
- Zeugenaussagen aus Heimatland
- Medienberichte

## 4) Folge-Folgeantrag

- Auch wiederholt möglich
- Aber: jeder Antrag braucht neue Wiederaufgreifens-Gründe
- Bei missbraeuchlichem Verhalten: Unzulaessigkeit

## 5) Dublin-III VO 604/2013

### Bei Folgeantrag

- Prüfung ob anderer EU-Staat zustaendig
- 6-Monats-Überstellungs-Frist
- Bei Versäumnis: DE-Zuständigkeit

### Aufenthalts-Recht

- Bei Folgeantrag: kein automatisches Aufenthaltsrecht
- Antrag auf Aussetzung Vollstreckung § 80 V VwGO bei VG

## 6) Workflow

### Schritt 1 — Mandanten-Beratung

- Wiederaufgreifens-Grund identifizieren
- Realistische Aussichten-Bewertung
- Risiko fehlender Aussicht: Abschiebung
- Alternative: Aufenthaltstitel humanitaerer Gründe § 25 AufenthG

### Schritt 2 — Antrag BAMF

- Schriftlich, mit Wiederaufgreifens-Grund
- Beweismittel beigefügt
- Dolmetscher bei Vorbringen

### Schritt 3 — Bescheid

- BAMF entscheidet binnen Wochen
- Bei Unzulaessigkeit: Aussetzung Anhörung
- Bei Zulässigkeit: persönliche Anhörung

### Schritt 4 — Klage VG bei Ablehnung

- Frist 2 Wochen bei Schnellverfahren
- Frist 1 Monat bei Standard-Bescheid
- Eilantrag § 80 V VwGO bei drohender Abschiebung

## 7) Spezielle Konstellationen

### Konversion

- Christen-Konversion (Iran, Pakistan)
- Pflicht zur Glaubens-Prüfung
- Sachverständiger-Gutachten

### Sexual-Orientierung

- Outet-sich-Argument
- Verfolgung-Risiko Heimatland

### Politische Aktivitäten

- In Deutschland (Exil-Politik)
- Beweis durch Demo-Fotos, Vereins-Mitgliedschaft

## 8) Bundesamt für Migration und Fluechtlinge (BAMF)

### Prozessuale Pflichten

- Anhörung
- Vollständige Aufklärung
- Begründung Bescheid

### Beweisaufnahme

- Auskunft Auswärtiges Amt
- ACCORD-Berichte
- UNHCR-Berichte

## 9) Typische Fehler

1. **3-Monats-Frist verpasst**
2. **Wiederaufgreifens-Grund zu schwach**
3. **Eilantrag versäumt** bei drohender Abschiebung
4. **Folge-Folge-Antrag missbraeuchlich** -> Unzulaessigkeit

## 10) BVerwG-Linien

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Anschluss

- `fachanwalt-migrationsrecht-orientierung` — Triage
- `fachanwalt-migrationsrecht-aufenthaltstitel-antrag` — Alternativ-Titel
- `widerspruch-oder-klage-erstpruefung` — bei VG-Klage

## Vertiefung: Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Normen-Kette Folgeantrag

- **§ 71 Abs. 1 AsylG** iVm **§ 51 Abs. 1-3 VwVfG** — Wiederaufgreifensvoraussetzungen, Frist 3 Monate
- **§ 71 Abs. 5 AsylG** — Abschiebungsandrohung bei Unzulaessigkeit des Folgeantrags
- **§ 51 Abs. 2 VwVfG** — Frist ab Kenntnis des Wiederaufgreifensgrundes
- **§ 36 AsylG** — Klagefrist eine Woche wenn Folgeantrag als unzulaessig beschieden
- **§ 74 Abs. 1 AsylG** — Klagefrist zwei Wochen bei Sachabweisung des Folgeantrags
- **Art. 40 Verfahrens-RL 2013/32** — Folgeantraege; Mitgliedstaat kann Folgeantrag nur ablehnen wenn keine neuen Elemente

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template: Folgeantrag BAMF

**Adressat:** BAMF, Abteilung Wiederaufnahme / Folgeantrag
**Tonfall:** Sachlich-juristisch; Substantiierung der neuen Wiederaufgreifensgruende

```
[KANZLEI]
[ADRESSE]

Bundesamt fuer Migration und Fluechtlinge
[AUSSENSTELLE]
[ADRESSE]

Re: Asyl-Folgeantrag gemaess § 71 AsylG
    Antragsteller: [NAME, geb. DATUM, Staatsang.]
    BAMF-Aktenzeichen (Erstantrag): [AZ]

Sehr geehrte Damen und Herren,

in Vertretung des o.g. Antragstellers stellen wir hiermit Folgeantrag
gemaess § 71 AsylG und § 51 VwVfG.

I. BISHERIGER VERFAHRENSSTAND
Erstantrag abgelehnt am [DATUM], Bescheid Az. [AZ].
Klage [wurde erhoben / nicht erhoben].

II. WIEDERAUFGREIFENSGRUENDE (§ 51 Abs. 1 Nr. [X] VwVfG)
[Variante A — Aenderung Sachlage:]
Seit der Ablehnung des Erstantrags hat sich die Lage im Herkunftsland
[LAND] wesentlich veraendert: [KONKRETE SCHILDERUNG MIT DATUM].
Belege: UNHCR-Laenderbericht [DATUM] Anlage 1, AA-Bericht [DATUM] Anlage 2.

[Variante B — Neue Beweismittel:]
Es liegen neue Beweismittel vor, die bei der Erstentscheidung nicht
verfuegbar waren: [ATTEST / DOKUMENT / ZEUGNIS]. Anlage 3.

[Variante C — Konversion / LGBTQ / persoenliche Aenderung:]
Der Antragsteller ist am [DATUM] zum [Christentum / Islam / ...] konvertiert.
Bescheinigung beigefuegt Anlage 4. Die innere Uberzeugung ist echt und stabil
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

III. FRIST § 51 ABS. 2 VWVFG
Der Antragsteller hat von dem o.g. Wiederaufgreifensgrund am [DATUM]
Kenntnis erlangt. Die 3-Monats-Frist laeuft bis [DATUM]; dieser Antrag
wird fristgerecht gestellt.

IV. SICHERUNGSMASSNAHMEN
Bei drohender Abschiebung bitten wir um unverzuegliche Bestaetigung
des Folgeantragseingangs (§ 71 Abs. 4 AsylG).

Anlagen: K1 bis K[X]

[KANZLEI], [ORT], [DATUM]
[RA-NAME]
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `fachanwalt-migrationsrecht-familiennachzug`

_Mandant will Ehegatten Kinder oder Eltern nach Deutschland holen und fragt nach Voraussetzungen und Verfahren. Prüfraster §§ 27-36 AufenthG Familiennachzug Lebensunterhalt Wohnraum Sprachkenntnisse A1. Beschleunigtes Visum-Verfahren Familiennachzug zu Schutzbedürftigen nach § 36a AufenthG. Normen § 27 AufenthG Grundsatz § 28 AufenthG Ehegatten § 32 AufenthG Kinder. Output Nachzugs-Prüf-Memo Antragscheckliste Visum-Entwurf Klage-Option bei Ablehnung. Abgrenzung: fachanwalt-migrationsrecht-aufenthaltstitel-antrag für eigenständige Titelerteilung._

# Familiennachzug

## Zweck

Visum / Aufenthaltstitel für Familienangehörige eines in Deutschland lebenden Ausländers / Deutschen.

## 1) Eingangs-Abfrage

1. Wer ist der "Stamm-Inhaber" — Deutscher, EU-Bürger, Drittstaater?
2. Welche Familienangehörige (Ehegatte, Kinder, Eltern)?
3. Aufenthaltstitel des Stamm-Inhabers?
4. Wohnraum / Einkommen Stamm-Inhaber?
5. Sprachkenntnis Antragsteller?
6. Heimatland und deutsche Botschaft zustaendig?

## 2) Familiennachzug nach Konstellation

### Ehegatten-Nachzug § 30 AufenthG

- Stamm-Inhaber: Niederlassungserlaubnis oder bestimmte Aufenthaltstitel
- Ehegatte: 18 Jahre, A1-Sprachkenntnis
- Lebensunterhaltssicherung (Einkommen)
- Wohnraum

### Kinder-Nachzug § 32 AufenthG

- Bis 16. Lebensjahr: Standardweg
- 16-17 Jahre: Voraussetzungen wie Ehegatte
- A1-Pflicht ab 16

### Eltern-Nachzug § 36 II AufenthG

- Nur bei außergewoehnlicher Härte
- Sehr restriktiv

### Familiennachzug zu Schutzbedürftigen

- Anerkannte Fluechtlinge: vereinfachter Nachzug § 36a AufenthG
- Subsidiaer Schutzbedürftige: § 36a AufenthG, monatliches Kontingent 1.000
- Bei Volljaehrigkeit Kind nach Anerkennung Eltern: § 36 I AufenthG

## 3) Voraussetzungen Lebensunterhaltssicherung § 5 I Nr. 1 AufenthG

### Standard

- Netto-Einkommen Stamm-Inhaber muss reichen für:
  - Eigenen Lebensunterhalt
  - Lebensunterhalt aller mitnachziehenden
- Mietkosten + Sozialhilfe-Bedarfssatz als Maßstab

### Ausnahmen

- Schutzbedürftige im Erstjahr
- Familienzusammenführung mit deutschen Staatsangehörigen § 28 AufenthG (geringere Anforderungen)

## 4) Sprachkenntnis A1

### Pflicht

- Bei Ehegatten-Nachzug
- Prüfung Goethe / TELC / OESD
- Vor Visum-Antrag

### Ausnahmen

- Schutzbedürftige
- Behinderung
- EU-Bürger-Familienangehörige
- Klage gegen schwer erfuellbare Anforderung (EGMR-Linie)

## 5) Visum-Verfahren

### Antrag deutsche Botschaft

- Mit Anlagen
- Termin meist 4-12 Wochen Wartezeit
- Beschleunigtes Verfahren BeschAusG (Beauftragten-Verfahren) seit 2020

### Beschleunigtes Verfahren § 81a AufenthG

- Antrag durch AG / Familie in Deutschland
- Ausländerbehoerde stimmt vorab zu
- Visum-Erteilung beschleunigt

### Visum-Ablehnung

- **Klage VG Berlin** (zuständiges Gericht bei Visum)
- Eilantrag § 123 VwGO

## 6) Workflow

### Phase 1 — Vorbereitung

- Lebensunterhalt + Wohnraum kalkulieren
- Sprachkurs Antragsteller buchen
- Dokumente sammeln (Heiratsurkunde, Geburts-, Schul-)

### Phase 2 — Antrag

- Botschaft im Heimatland
- Begleitung durch Anwalt empfohlen
- Bei Schwellen-Land: Vorabzustimmung Ausländerbehoerde

### Phase 3 — Visum erteilt

- Einreise innerhalb der Frist
- Bei Ausländerbehoerde Aufenthaltstitel beantragen
- Aufenthaltstitel zum gleichen Zweck § 28 / 30 / 32 AufenthG

### Phase 4 — Bei Ablehnung

- Klage VG Berlin
- Eilantrag bei dringender Familien-Sache

## 7) Schutz Art. 6 GG / Art. 8 EMRK

### Familienleben

- Verfassungsrechtlicher Schutz
- Prüfung Verhältnismaessigkeit Ablehnung

### Kindeswohl

- Bei Kindern besondere Prüfung
- EGMR-Linie zur Familienzusammenführung

## 8) Typische Fehler

1. **A1-Sprachkenntnis unvollständig nachgewiesen**
2. **Lebensunterhalts-Kalkulation falsch**
3. **Termin Botschaft zu spaet** — Wartezeit unterschaetzt
4. **Vorabzustimmung Ausländerbehoerde versäumt** bei beschleunigtem Verfahren
5. **Klage-Frist 1 Monat versäumt**

## 9) Familiennachzug zu deutschen Staatsangehörigen § 28 AufenthG

### Vereinfacht

- Keine Lebensunterhalts-Pflicht
- Sprachkenntnis erforderlich (mit Ausnahmen)
- Standard-Weg für deutsch-ausländische Ehepaare

## 10) BVerwG-/EuGH-Linien

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Anschluss

- `fachanwalt-migrationsrecht-orientierung` — Triage
- `aufenthaltstitel-pruefung` (Power-Tool) — Prüfraster
- `fachanwalt-migrationsrecht-einbuergerung` — bei Staatsangehoerigkeit

## Vertiefung: Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Normen-Kette Familiennachzug

- **§§ 27, 28, 29, 30, 32, 36 AufenthG** — Grundsatz Familiennachzug, Deutschennachzug, allgemeiner Nachzug, Ehegatten, Kinder, Eltern
- **§ 36a AufenthG** — Familiennachzug zu subsidiaer Schutzberechtigten (Kontingent 1.000/Monat)
- **§ 5 Abs. 1 Nr. 1 AufenthG** — Lebensunterhaltssicherung als Regelerteilungsvoraussetzung
- **§ 81a AufenthG** — beschleunigtes Fachkraefte-Visum-Verfahren
- **Art. 6 GG / Art. 8 EMRK** — verfassungsrechtlicher Familien- und Privatlebensschutz
- **EU-Familienzusammenf.-RL 2003/86/EG** — Rechtsanspruch auf Nachzug bei Fluechtlingen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template: Antragsschreiben Visum Familiennachzug

**Adressat:** Deutsche Botschaft [LAND], Visumstelle
**Tonfall:** Sachlich-begruendend, auf Anspruchsgrundlage hinweisend

```
[KANZLEI]
[ADRESSE]

Deutsche Botschaft [HAUPTSTADT/LAND]
Visumstelle
[ADRESSE]

Re: Visumsantrag Familiennachzug fuer [ANTRAGSTELLER NAME, geb. DATUM]
    zu [STAMMINHABER NAME, AufenthaltsstT/NE, wohnhaft ADRESSE D]
    Visumantrag-Nr.: [falls vorhanden]

Sehr geehrte Damen und Herren,

wir vertreten [STAMMINHABER NAME] und zeigen die anwaltliche Begleitung
des Visumsantrags fuer [FAMILIENANGEHOERIGE(R)] an.

I. SACHVERHALT
[NAME STAMMINHABER] lebt seit [DATUM] in Deutschland (Aufenthaltstitel:
[Art und Gueltigkeit], Anlage 1). Er beantragt Familiennachzug fuer
seine Ehegattin / sein Kind [NAME].

II. ANSPRUCHSGRUNDLAGE
§ [28 / 30 / 32] AufenthG in Verbindung mit Art. 6 GG.

III. VORAUSSETZUNGEN LIEGEN VOR
a) Lebensunterhalt: Netto-Einkommen [BETRAG EUR] (Einkommensnachweise
   Anlage 2). Der Bedarf fuer 2 Personen betraegt nach Sozialrechtssaetzen
   ca. [BETRAG] EUR. Deckung gegeben.
b) Wohnraum: [Groesse m2] — ausreichend fuer [X] Personen (Anlage 3: Mietvertrag).
c) Sprachkenntnis: A1-Zertifikat Anlage 4. [ODER: Ausnahme wegen ...]
d) Keine Ausweisungsinteressen (§ 5 Abs. 1 Nr. 2 AufenthG).

IV. ANLAGEN
1. Aufenthaltstitel / Niederlassungserlaubnis
2. Einkommensnachweise letzter 3 Monate
3. Mietvertrag / Wohnraumnachweis
4. A1-Zertifikat
5. Heiratsurkunde / Geburtsurkunde (beglaubigt und apostilliert)
[...]

Wir bitten um zeitnahe Bearbeitung und stehen fuer Rueckfragen zur Verfuegung.

[KANZLEI], [ORT], [DATUM]
[RA-NAME]
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

