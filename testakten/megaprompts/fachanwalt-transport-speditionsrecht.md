# Megaprompt: fachanwalt-transport-speditionsrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 77 Skills des Plugins `fachanwalt-transport-speditionsrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Fachanwalt Transport- und Speditionsrecht: ordnet Rolle (Absender, Frachtführer, Empfän…
2. **mandat-triage-transport-speditionsrecht** — Ersteinordnung neuer Mandate im Transport- und Speditionsrecht: Vertragstyp, national vs: international. Normen: §§ 407 …
3. **fachanwalt-transport-speditionsrecht-orientierung** — Orientierungs-Skill Transport- und Speditionsrecht: richtigen Skill anhand Sachverhalt auswaehlen. Normen: §§ 407 ff. HG…
4. **orientierung-mandat-fachanwaltschaft** — Orientierungs-Skill Transport- und Speditionsrecht: richtigen Skill anhand Sachverhalt auswaehlen: Normen: §§ 407 ff. HG…
5. **erstgespraech-mandatsannahme** — Erstgespraeches-Aufnahme im Transport- und Speditionsrecht strukturiert durchführen: Sachverhalt, Vertragstyp, Schadenst…
6. **erstpruefung-und-mandatsziel** — Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.
7. **fachanwalt-transport-autonome-lkw-konvois-haftung-1d-stvg** — Haftung bei autonomen LKW-Konvois nach § 1d StVG analysieren: Fahrzeughalterhaftung, KI-Systemfehler. Normen: § 1d StVG,…
8. **fachanwalt-transport-speditionsrecht-ladungsschaden** — Ladungsschaden im Gueterverkehr prüfen und geltend machen: Nachweis, Schadensberechnung, Haftungslimits. Normen: §§ 425 …
9. **fachanwalt-transport-adr-gefahrgut** — Gefahrguttransport-Haftung und ADR-Verstoss klaeren: Gefahrgutkennzeichnung, Verantwortlichkeiten, Bußgelder. Normen: AD…
10. **fachanwalt-transport-speditionsrecht-lieferverzug** — Lieferverzug im Gueterverkehr prüfen: Verspaetungsschaden, Haftungshoechstbetrag, Fristen. Normen: §§ 423 425 HGB, Art. …

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Fachanwalt Transport- und Speditionsrecht: ordnet Rolle (Absender, Frachtführer, Empfänger), markiert Frist (CMR Klage 1 Jahr / 3 Jahre Vorsatz), wählt Norm (HGB §§ 407 ff. Frachtrecht, CMR (Straße), Montrealer Übk. (Luft)) und Zuständigkeit (Handelsgericht), leit..._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Fachanwalt Transport Speditionsrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `transport-autonome-lkw-konvois-haftung-1d-stvg` — Autonome LKW CMR Schadensregulierung
- `cmr-haftung-art-17-cmr` — CMR Haftung ART 17 CMR
- `cmr-haftung` — CMR Haftung Ladungsschaden
- `cotif-schriftsatz-brief-und-memo-bausteine` — Cotif Fachanwalt Haager
- `workflow-mandantenkommunikation` — FA Transport Spedition Mandant Redteam
- `einstieg-schnelltriage-fallrouting` — FA Transport Spedition Start Chronologie Fristen
- `frachtfuehrerhaftung-paragraf-425-hgb` — Frachtfuehrerhaftung Paragraf 425 HGB
- `gefahrgut-adr-paragraf-9-gefstoffvo` — Gefahrgut ADR Paragraf 9 Gefstoffvo
- `hgb-dokumentenmatrix-und-lueckenliste` — HGB Kabotage Beweislast Kanzlei RED Team Korrektur
- `ladungsschaden-art-23-cmr` — Ladungsschaden ART 23 CMR
- `lieferverzug` — Lieferverzug Orientierung Mandat Triage
- `luftfracht-monteral-uebereinkommen` — Luftfracht Monteral Uebereinkommen
- `marktzugang-sonderfall-edge-case` — Marktzugang Sonderfall Montrealer
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Fachanwalt Transport Speditionsrecht sind HGB, §§ 407 ff, §§ 453 ff. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `mandat-triage-transport-speditionsrecht`

_Ersteinordnung neuer Mandate im Transport- und Speditionsrecht: Vertragstyp, national vs: international. Normen: §§ 407 454 HGB, CMR. Prüfraster: Vertragstyp, Schadens..._

# Ersteinordnung neuer Mandate im Transport- und Speditionsrecht: Vertragstyp, national vs


## Aktenstart statt Formularstart

Wenn zu **Lieferverzug Orientierung Mandat Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Fachanwalt Transport Speditionsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

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
- Tragende Normen verifizieren: §§ 407 ff. Frachtvertrag — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Ersteinordnung neuer Mandate im Transport- und Speditionsrecht: Vertragstyp, national vs. international. Normen: §§ 407 454 HGB, CMR. Prüfraster: Vertragstyp, Schadenstyp, Dringlichkeit, Fristen. Output: Mandat-Triage-Protokoll Transport-Speditionsrecht. Abgrenzung: nicht Erstgespraeches-Aufnahme.

### Mandat-Triage Transport- und Speditionsrecht

## Ablauf — sieben Fragen

### Frage 1 — Mandantenrolle?

- Versender / Verlader
- Empfänger
- Frachtführer
- Spediteur
- Lager-Betreiber
- Versicherer (Cargo Verkehrshaftung)
- Subunternehmer / Nachunternehmer

### Frage 2 — Verkehrsträger?

- Straße — Lkw
- Schiene — Eisenbahn
- Wasser — Binnen / See
- Luft
- Multimodal — kombiniert
- Lager / Umschlag

### Frage 3 — Geografie?

- Inland
- Grenzüberschreitend EU
- Grenzüberschreitend Drittstaat
- Transit

### Frage 4 — Akute Eilbedürftigkeit?

- **Reklamationsfrist** läuft (sofort / sieben / einundzwanzig Tage)
- **Verjährungsfrist** ein Jahr läuft ab
- **Gefahrgut-Zwischenfall** ADR-Meldung
- **Embargo / Sanktionen** plötzlich greifend
- **Beschlagnahme Zoll** Akut
- **Frachtgut nicht ausgehändigt** wegen Frachtstreit
- **Versicherungs-Stichtag** läuft

### Frage 5 — Sachgebiet?

- Verlust Sendung
- Beschädigung Sendung
- Lieferfrist-Überschreitung
- Frachtforderung Frachtführer
- Speditionsvergütung
- Multimodal-Vertrag
- Gefahrgut-Recht
- Zollrecht
- Lagerlogistik
- Transport-Versicherungs-Streit
- Frachtbrief-Fälschung

### Frage 6 — Frist?

- **Reklamation Verlust erkennbar Beschädigung** sofort schriftlich
- **Reklamation verdeckter Schaden** sieben Tage CMR Art. 30 / § 438 HGB
- **Reklamation Verzug** einundzwanzig Tage
- **Verjährung CMR** ein Jahr / drei Jahre bei Vorsatz
- **Verjährung HGB** ein Jahr / drei Jahre
- **Versicherungs-Anspruch** drei Jahre § 195 BGB
- **CMR-Klage** ein Jahr nach Ablieferung

### Frage 7 — Wirtschaftliche Verhältnisse?

- Versicherung Cargo Verkehrshaftung
- Schadenshöhe vs. SDR-Begrenzung
- Streitwert für Klage
- Bei Spedition: ADSp-Geltung

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Schadensersatz Frachtführer | `frachtfuehrerhaftung-pruefen` |
| Speditionsverhalten | `frachtfuehrerhaftung-pruefen` plus ADSp Spezifika |
| Frachtforderung-Klage | (Skill frachtforderung — perspektivisch) |
| Multimodal-Vertrag | (Skill multimodal — perspektivisch) |
| Gefahrgut ADR | (Skill gefahrgut-adr — perspektivisch) |
| Zollrecht | weiter an `mandat-triage-verwaltungsrecht` plus |
| Versicherungs-Streit | weiter an `mandat-triage-versicherungsrecht` |

## Mandatsannahme

- **Konflikt-Check** — keine Doppelmandate Versender/Frachtführer
- **Streitwert** Sendung-Wert oder Frachtforderung
- **Sachverständigen-Bedarf** Transport- und Verpackungs-SV
- **Versicherungs-Deckung** Verkehrshaftungs-Versicherung Mandant prüfen

## Eskalation

- **Telefon-Sofort** Reklamationsfrist heute / morgen Gefahrgut-Vorfall
- **Binnen einer Stunde** Schriftliche Reklamation Frachtbrief-Bemerkung
- **Heute** Auskunfts-Aufforderung an Frachtführer
- **Diese Woche** Klage vor Verjährungs-Ablauf

## Ausgabe

- `triage-protokoll-transport-spedition.md`
- Aktenanlage mit Verkehrsträger und Anwendung CMR/HGB
- Frist im Fristenbuch (Reklamation Verjährung)
- Reklamations-Schreiben sofort
- Mandatsvereinbarung mit Honorar
- Empfehlung Folge-Skill

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen

- CMR 1956
- HGB §§ 407 ff. 453 ff.
- MÜ CIM CMNI
- ADSp
- BGH I. Zivilsenat
- Koller Transport-/Speditionsrecht

## Aktuelle Rechtsprechung Triage Transport

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `fachanwalt-transport-speditionsrecht-orientierung`

_Orientierungs-Skill Transport- und Speditionsrecht: richtigen Skill anhand Sachverhalt auswaehlen. Normen: §§ 407 ff. HGB, CMR, ADSP. Prüfraster: Vertragsart Fracht vs. Spedition, national vs. international, Schadenstyp. Output: Skillauswahl-Empfehlung Transport-Speditionsrecht. Abgrenzung: kein inhaltlicher Prüf-Skill._

# Fachanwalt für Transport- und Speditionsrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 40 Fälle in den letzten drei Jahren, davon mindestens 25 streitige.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Frachtvertrag | HGB §§ 407 ff. |
| Haftung Frachtführer | HGB §§ 425 ff. (Obhutshaftung Haftungshöchstbetrag § 431) |
| Speditionsvertrag | HGB §§ 453 ff. |
| Lagervertrag | HGB §§ 467 ff. |
| Straßenverkehr international | CMR (Convention relative au contrat de transport international de marchandises par Route) |
| Eisenbahn international | COTIF / CIM (Convention concernant les transports internationaux ferroviaires) |
| Luftverkehr | Montrealer Übereinkommen 1999 |
| Seehandel | Haager Visby Regeln BGB-HGB §§ 476 ff. Hamburg-Regeln (nicht in Deutschland in Kraft) |
| Multimodaler Transport | CMR / CIM in Anwendung |
| AGB Spedition | ADSp 2017 |
| EU-Recht | RL 2009/103 Kfz-Versicherung VO 261/2004 Fluggastrechte |

## Typische Mandate

- Frachtschadens-Klage (Verlust Beschädigung Verspätung)
- Spediteurshaftung
- Haftungshöchstgrenzen § 431 HGB CMR Art. 23 Montrealer Übereinkommen Art. 22
- Reklamations- und Klagefristen
- ADSp-Anwendung (Spediteursklauseln)
- Container-Streitigkeiten in Seehandel
- Pflichtversicherung Kraftverkehr Spediteur Frachtführer
- Internationale Vollstreckung

## Fristen

- **Reklamationsfrist** HGB / CMR / Montrealer:
  - HGB § 438 — sieben Tage bei äußerlich erkennbarem Schaden binnen drei Tagen.
  - CMR Art. 30 — sofort bei Annahme Verluste / Beschädigung; sieben Tage bei nicht erkennbaren.
  - Montrealer Art. 31 — 14 Tage Beschädigung 21 Tage Verspätung.
- **Verjährung Frachtschaden** § 439 HGB — ein Jahr (drei Jahre bei Vorsatz / grob fahrlaessig).
- **CMR Art. 32** — ein Jahr (drei Jahre bei Vorsatz).
- **Klagefrist Fluggast** keine Frist im Montrealer; Verjährung zwei Jahre Art. 35 MontU.

## Hauptgerichte

- Amtsgericht / Landgericht Zivilkammer.
- OLG.
- BGH I. Zivilsenat Transportrecht (Sondersenat).
- Ausländische Gerichte bei Auslandsbezug.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- ARGE Transportrecht DAV.

## Schnittstellen

- **gesellschaftsrecht** bei Spediteur-Gesellschaft.
- **fachanwalt-internationales-wirtschaftsrecht** bei grenzüberschreitenden Transporten.
- **fachanwalt-versicherungsrecht** bei Transportversicherung.
- **kanzlei-allgemein** Fristen Versand.

---

## Skill: `orientierung-mandat-fachanwaltschaft`

_Orientierungs-Skill Transport- und Speditionsrecht: richtigen Skill anhand Sachverhalt auswaehlen: Normen: §§ 407 ff. HGB, CMR, ADSP. Prüfraster: Vertragsart..._

# Orientierungs-Skill Transport- und Speditionsrecht: richtigen Skill anhand Sachverhalt auswaehlen


## Aktenstart statt Formularstart

Wenn zu **Lieferverzug Orientierung Mandat Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Fachanwalt Transport Speditionsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

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
- Tragende Normen verifizieren: §§ 407 ff. Frachtvertrag — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierungs-Skill Transport- und Speditionsrecht: richtigen Skill anhand Sachverhalt auswaehlen. Normen: §§ 407 ff. HGB, CMR, ADSP. Prüfraster: Vertragsart Fracht vs. Spedition, national vs. international, Schadenstyp. Output: Skillauswahl-Empfehlung Transport-Speditionsrecht. Abgrenzung: kein inhaltlicher Prüf-Skill.

### Fachanwalt für Transport- und Speditionsrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 40 Fälle in den letzten drei Jahren, davon mindestens 25 streitige.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Frachtvertrag | HGB §§ 407 ff. |
| Haftung Frachtführer | HGB §§ 425 ff. (Obhutshaftung Haftungshöchstbetrag § 431) |
| Speditionsvertrag | HGB §§ 453 ff. |
| Lagervertrag | HGB §§ 467 ff. |
| Straßenverkehr international | CMR (Convention relative au contrat de transport international de marchandises par Route) |
| Eisenbahn international | COTIF / CIM (Convention concernant les transports internationaux ferroviaires) |
| Luftverkehr | Montrealer Übereinkommen 1999 |
| Seehandel | Haager Visby Regeln BGB-HGB §§ 476 ff. Hamburg-Regeln (nicht in Deutschland in Kraft) |
| Multimodaler Transport | CMR / CIM in Anwendung |
| AGB Spedition | ADSp 2017 |
| EU-Recht | RL 2009/103 Kfz-Versicherung VO 261/2004 Fluggastrechte |

## Typische Mandate

- Frachtschadens-Klage (Verlust Beschädigung Verspätung)
- Spediteurshaftung
- Haftungshöchstgrenzen § 431 HGB CMR Art. 23 Montrealer Übereinkommen Art. 22
- Reklamations- und Klagefristen
- ADSp-Anwendung (Spediteursklauseln)
- Container-Streitigkeiten in Seehandel
- Pflichtversicherung Kraftverkehr Spediteur Frachtführer
- Internationale Vollstreckung

## Fristen

- **Reklamationsfrist** HGB / CMR / Montrealer:
 - HGB § 438 — sieben Tage bei äußerlich erkennbarem Schaden binnen drei Tagen.
 - CMR Art. 30 — sofort bei Annahme Verluste / Beschädigung; sieben Tage bei nicht erkennbaren.
 - Montrealer Art. 31 — 14 Tage Beschädigung 21 Tage Verspätung.
- **Verjährung Frachtschaden** § 439 HGB — ein Jahr (drei Jahre bei Vorsatz / grob fahrlaessig).
- **CMR Art. 32** — ein Jahr (drei Jahre bei Vorsatz).
- **Klagefrist Fluggast** keine Frist im Montrealer; Verjährung zwei Jahre Art. 35 MontU.

## Hauptgerichte

- Amtsgericht / Landgericht Zivilkammer.
- OLG.
- BGH I. Zivilsenat Transportrecht (Sondersenat).
- Ausländische Gerichte bei Auslandsbezug.

## Berufsverband

- ARGE Transportrecht DAV.

## Schnittstellen

- **gesellschaftsrecht** bei Spediteur-Gesellschaft.
- **fachanwalt-internationales-wirtschaftsrecht** bei grenzüberschreitenden Transporten.
- **fachanwalt-versicherungsrecht** bei Transportversicherung.
- **kanzlei-allgemein** Fristen Versand.

---

## Skill: `erstgespraech-mandatsannahme`

_Erstgespraeches-Aufnahme im Transport- und Speditionsrecht strukturiert durchführen: Sachverhalt, Vertragstyp, Schadenstyp: Normen: §..._

# Erstgespraeches-Aufnahme im Transport- und Speditionsrecht strukturiert durchführen: Sachverhalt, Vertragstyp, Schadenstyp


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: §§ 407 ff. Frachtvertrag — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Erstgespraeches-Aufnahme im Transport- und Speditionsrecht strukturiert durchführen: Sachverhalt, Vertragstyp, Schadenstyp. Normen: §§ 407 ff. HGB, CMR, BRAO. Prüfraster: Sachverhaltserfassung, Frachtvertrag vs. Speditionsauftrag, Interessenlage, Fristen. Output: Erstgespraeches-Protokoll Transport-Speditionsrecht. Abgrenzung: nicht Klageschrift.

### Erstgespraech und Mandatsannahme im Transport-, Speditions- und Logistikrecht

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Transport-, Speditions- und Logistikrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klären, Konflikt- und GwG-Prüfung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Transport-, Speditions- und Logistikrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klägerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Frachtvertrag, CMR, Spediteur, Versicherung, Multimodal, Zoll
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Frachtklage, Klage CMR-Schaden, Klage HGB-Spediteur-Haftung). Frist-Alarm an die Vorbereitung weitergeben.

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

Standard-Streitwerte im Bereich Transport-, Speditions- und Logistikrecht:

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

- BORA, BRAO, FAO für Fachanwaltschaft Transport-, Speditions- und Logistikrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- §§ 407 ff. HGB, CMR, MC, ADSp, RVS-Konvention (für fachliche Erstpruefung).
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

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Transport-, Speditions- und Logistikrecht). Handlungs-Sequenz:

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
- Verfahrensdauer im Bereich Transport-, Speditions- und Logistikrecht: Erfahrungswerte nach Instanz.
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

## Aktuelle Rechtsprechung Erstgespraech Transport

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen Erstgespraech Transport

- §§ 407-413 HGB — Frachtvertrag (Grundlagen, Pflichten, Haftung)
- § 439 HGB — Verjährung (1 Jahr ab Ablieferung; 3 Jahre bei Vorsatz)
- Art. 32 CMR — Verjährung im CMR-Verkehr
- Art. 5 CMR — Frachtbrief als Beweisurkunde
- §§ 10 ff. GwG — Identifizierungspflichten auch im Transportrechtsmandat

---

## Skill: `erstpruefung-und-mandatsziel`

_Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel


## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 241 Abs. 2 BGB` — Rücksichtnahme-, Schutz- und Organisationspflichten.
- `§ 242 BGB` — Treu und Glauben als Korrektiv enger Klausel- und Anspruchsarbeit.
- `§ 280 Abs. 1 BGB` — Pflichtverletzung, Vertretenmuessen, Schaden.
- `§ 286 Abs. 1 BGB` — Verzug und Fristlogik.
- `§ 195 BGB` — regelmäßige Verjährung.
- `§ 199 Abs. 1 BGB` — Beginn der regelmäßigen Verjährung.
- `§ 253 Abs. 2 ZPO` — Bestimmtheit von Antrag und Klagegrund.
- `§ 138 Abs. 1 ZPO` — Wahrheitspflicht und vollstaendiger Tatsachenvortrag.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: §§ 407 ff. Frachtvertrag — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** HGB, CMR, COTIF.

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

## Skill: `fachanwalt-transport-autonome-lkw-konvois-haftung-1d-stvg`

_Haftung bei autonomen LKW-Konvois nach § 1d StVG analysieren: Fahrzeughalterhaftung, KI-Systemfehler. Normen: § 1d StVG, §§ 7 18 StVG, §§ 407 ff. HGB. Prüfraster: Halterhaftung, technisches Versagen, Konvoi-Führer, Regulierung. Output: Haftungsanalyse autonomer LKW. Abgrenzung: nicht klassische Frachtführerhaftung ohne Automatisierung._

# Autonome LKW-Konvois – Haftung § 1d StVG und CMR

## Kernsachverhalt & Mandantenfragen

Platooning – automatisierte LKW-Konvois mit V2V-Kommunikation (Vehicle-to-Vehicle) – ist technisch Realität und rechtlich noch weitgehend ungeklärt. § 1d StVG (eingefügt 2021) schafft einen Rahmen für hochautomatisiertes und vollautomatisiertes Fahren in Deutschland. Die haftungsrechtliche Gemengelage aus StVG (Gefährdungshaftung), Produkthaftungsgesetz (Herstellerhaftung) und CMR (Frachtführerhaftung) erfordert eine sorgfältige Schichtenanalyse.

**8 Kaltstart-Rückfragen:**

1. Auf welcher Automatisierungsstufe (SAE Level 2, 3, 4 oder 5) war das Fahrzeug zum Unfallzeitpunkt?
2. War der autonome Modus aktiviert oder fuhr das Fahrzeug manuell gesteuert?
3. Liegt ein Datenspeicher-Auslesungsprotokoll gemäß § 1g StVG vor (Black-Box-Daten)?
4. Wer war als Technische Aufsicht (Remote-Operator) nach § 1f StVG benannt und hat diese eine Übernahme-Aufforderung erhalten?
5. Welche Fahrzeugmarke und welches Assistenzsystem wurde eingesetzt (Mercedes, MAN, Scania, Volvo, Daimler Truck)?
6. Hat der Hersteller Rückrufe (Recalls) für das betreffende Fahrzeug oder das Assistenzsystem ausgesprochen?
7. War der Transport grenzüberschreitend (CMR anwendbar) oder innerdeutsch (HGB)?
8. Welche Schadensarten sind eingetreten: Personenschaden, Sachschaden an Drittfahrzeug, Ladungsschaden des Auftraggebers?

---
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 1d StVG | Betrieb hochautomatisierter und vollautomatisierter Fahrzeuge; Genehmigungspflicht |
| § 1e StVG | Genehmigungsverfahren beim Kraftfahrt-Bundesamt (KBA) |
| § 1f StVG | Pflichten des Halters: Benennung Technische Aufsicht; Betriebsgebiet; Einsatzbedingungen |
| § 1g StVG | Datenspeicherungspflicht: Black-Box-Mindestdatensatz; Aufbewahrung 6 Monate |
| § 1h StVG | Auskunftspflichten gegenüber Behörden; Unfallmeldung an KBA |
| § 7 StVG | Gefährdungshaftung des Halters; unabhängig von Verschulden und autonomem Modus |
| § 12 StVG | Haftungsbegrenzung: Personenschäden bis 7.5 Mio. EUR; Sachschäden bis 1 Mio. EUR je Ereignis |
| § 18 StVG | Verschuldenshaftung des Fahrers; eingeschränkt bei aktivem autonomen Modus |
| § 1 ProdHaftG | Produkthaftung des Herstellers: verschuldensunabhängig bei Produktfehler |
| § 2 ProdHaftG | Produktbegriff: Hardware und Software als Produkt anerkannt |
| § 3 ProdHaftG | Produktfehler: Sicherheitserwartungen der Allgemeinheit nicht erfüllt |
| § 1 Abs. 2 PflVG | Versicherungspflicht für Kraftfahrzeuge; gilt auch für autonome Fahrzeuge |
| CMR Art. 17 | Frachtführerhaftung: unabhängig von autonomer Steuerung |
| CMR Art. 29 | Qualifiziertes Verschulden: Systemversagen kann Leichtfertigkeit begründen |
| VO (EU) 2022/1426 | Typgenehmigung vollautomatisierter Fahrzeuge (ALKS – Automated Lane Keeping System) |
| VO (EU) 2019/2144 | Allgemeine Sicherheitsanforderungen für Fahrzeuge |

---

## Leitentscheidungen

| Aktenzeichen | Gericht / Datum | Leitsatz |
|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

---

## Prüfschema Haftung autonomer LKW-Konvoi

| Schritt | Inhalt | Grundlage |
|---|---|---|
| 1 | Automatisierungsstufe ermitteln: SAE Level 2 (Fahrer steuert), 3 (Systemsteuerung, Fahrer verfügbar), 4 (vollautom., kein Fahrer notwendig im Betriebsgebiet) | § 1d StVG |
| 2 | Aktivierungsstatus prüfen: War autonomer Modus zum Unfallzeitpunkt aktiv? Black-Box-Daten auswerten | § 1g StVG |
| 3 | Halterhaftung nach § 7 StVG: immer gegeben bei Betrieb des Fahrzeugs; keine Exkulpation möglich | § 7 StVG |
| 4 | Technische Aufsicht prüfen: § 1f StVG – war sie benannt? Hat sie auf Übergabeanforderung reagiert? | § 1f StVG |
| 5 | Fahrerhaftung § 18 StVG: Bei aktivem autonomen Modus nur bei Verletzung der Übergabepflicht | § 18 StVG |
| 6 | Herstellerhaftung ProdHaftG: Produktfehler Hard-/Software? Rückruf? Sicherheitserwartungen verletzt? | §§ 1–3 ProdHaftG |
| 7 | CMR-Haftung bei grenzüberschreitendem Transport: Frachtführerhaftung bleibt unabhängig vom Automatisierungsgrad | CMR Art. 17 |
| 8 | Datensicherung: § 1g StVG-Daten anfordern; Aufbewahrungsfrist 6 Monate; bei Löschung: Beweislastumkehr | § 1g StVG |
| 9 | V2V-Kommunikation auswerten: Daten zwischen Konvoi-Fahrzeugen bei Hersteller anfordern | VO 2022/1426 |
| 10 | Versicherungsdeckung prüfen: Kfz-Haftpflicht (PflVG) und ggf. Produkthaftpflichtversicherung des Herstellers | § 1 PflVG |
| 11 | Haftungsteilung ermitteln: Halter × Fahrer × Technische Aufsicht × Hersteller; anteilig nach § 254 BGB | § 254 BGB, § 17 StVG |
| 12 | CMR-Regress gegen Hersteller: Frachtführer haftet gegenüber Auftraggeber; Regress gegen Hersteller nach ProdHaftG möglich | CMR Art. 3, §§ 1 ff. ProdHaftG |

---

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Haftung autonome LKW-Konvois pruefen | Haftungsgutachten; Template unten |
| Variante A — Versicherungsfall klar | Direktklage gegen Versicherer § 115 VVG |
| Variante B — Herstellerdefekt des Fahrsystems | Produkthaftung § 1 ProdHaftG parallel zur StVG-Haftung |
| Variante C — Grenzueberschreitender Unfall EU | CMR-Haftung pruefen; auslaendisches Unfallort-Recht |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1 – Sicherungsantrag Black-Box-Daten § 1g StVG

```
An das Kraftfahrt-Bundesamt (KBA)
Postfach 1263
38022 Wolfsburg

Anforderung von Datenspeicher-Daten gemäß § 1h StVG

In der Sache Unfall vom [Datum] auf [Straße, Ort]
bitte ich um Beauskunftung folgender Datenspeicherdaten
des Fahrzeugs [Kennzeichen, FIN-Nummer]:

Gemäß § 1g StVG i.V.m. § 1h StVG sind die Daten des
verpflichtenden Datenspeichers für 6 Monate aufzubewahren.

Ich bitte um:
1. Kompletten Datensatz § 1g StVG für Zeitraum [X Stunden]
   vor dem Unfall
2. V2V-Kommunikationsprotokolle des Konvois
3. Systemzustand (autonom / manuell) zum Unfallzeitpunkt
4. Übergabeanforderungen an Fahrer / Technische Aufsicht

Die Daten werden benötigt zur Klärung der Haftungsfrage
nach §§ 7, 18 StVG und § 1d ff. StVG in dem anhängigen
Verfahren [Aktenzeichen / Angaben].

[Ort, Datum]
[Unterschrift, Kanzlei]
```

### Baustein 2 – Klage Halterhaftung + Produkthaftung

```
AN DAS LANDGERICHT [...]

Klägerin: [Geschädigte/r, Anschrift]
Beklagte 1: [Halter des autonomen LKW]
Beklagte 2: [Hersteller des Assistenzsystems / Fahrzeugs]

Streitwert: EUR [Schadenbetrag]

KLAGEBEGRÜNDUNG

I. SACHVERHALT

Am [Datum] ereignete sich auf der [Straße] ein Unfall, bei
dem das autonome Konvoi-Fahrzeug der Beklagten 1 [Kennzeichen]
in das Fahrzeug der Klägerin fuhr.
Das Fahrzeug war auf SAE Level [3/4] eingestellt (Anlage K1:
Black-Box-Auszug). Der autonome Modus war aktiviert.

II. HAFTUNG BEKLAGTE 1 (Halter § 7 StVG)

Die Beklagte 1 haftet als Halterin gemäß § 7 StVG.
Halterhaftung ist unabhängig von Schuld oder Automatisie-
rungsgrad; sie entfällt nur bei höherer Gewalt. Höhere Gewalt
liegt nicht vor.

III. HAFTUNG BEKLAGTE 2 (Produkthaftung § 1 ProdHaftG)

Das Assistenzsystem (ALKS gemäß VO 2022/1426) wies zum
Unfallzeitpunkt einen Fehler im Bereich [Beschreibung] auf.
Dieser Fehler führte zu einer Fehlsteuerung des Fahrzeugs.

Der Fehler begründet ein Produktfehler gemäß § 3 ProdHaftG
da das System hinter den berechtigten Sicherheitserwartungen
der Allgemeinheit zurückbleibt.

Beweis: Sachverständigengutachten ist einzuholen.

IV. SCHADENSHÖHE

[Personenschaden: EUR X]
[Sachschaden Fahrzeug: EUR X]
[Verdienstausfall: EUR X]
[Gesamt: EUR X]

V. ANTRAG

Die Beklagten 1 und 2 werden als Gesamtschuldner verurteilt,
an die Klägerin EUR [Betrag] nebst Zinsen zu zahlen.

[Ort, Datum, Unterschrift]
```

### Baustein 3 – Regress des Frachtführers gegen Hersteller

```
An [Fahrzeughersteller]

Regressforderung nach § 1 ProdHaftG / § 426 BGB

Der Frachtführer [Name] hat gegenüber dem Auftraggeber
[Name] den Ladungsschaden aus dem Unfall vom [Datum]
gemäß CMR Art. 17 reguliert: EUR [Betrag].

Der Schaden wurde verursacht durch einen Fehler des in
dem Fahrzeug [Kennzeichen] eingebauten Assistenzsystems
[Bezeichnung] (Anlage: Sachverständigengutachten).

Wir fordern Sie auf, den regulierten Betrag von EUR [X]
an den Frachtführer zu erstatten (§ 1 ProdHaftG Abs. 3;
§ 426 BGB).

[Ort, Datum, Unterschrift]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Beweislast

| Konstellation | Beweislast |
|---|---|
| Halterhaftung § 7 StVG | Keine Exkulpation möglich; Halter haftet verschuldensunabhängig |
| Fahrerhaftung § 18 StVG | Fahrer muss Verschuldensfreiheit beweisen; bei aktivem autonomem Modus erleichtert |
| Produktfehler § 1 ProdHaftG | Geschädigte/r: Nachweis des Fehlers, Schadens und Kausalität; Hersteller: Entlastungsbeweis nach § 1 Abs. 2/3 ProdHaftG |
| Technische Aufsicht Pflichtverletzung | Kläger muss belegen, dass Übergabeanforderung ausgelöst wurde und nicht (rechtzeitig) reagiert wurde; Black-Box-Daten entscheidend |
| CMR Art. 29 Qualifiziertes Verschulden | Anspruchsteller: Organisationsmangel oder Systemversagen mit Bewusstsein; Frachtführer: Exkulpation durch Wartungsnachweise |

---

## Fristen und Verjährung

| Frist | Inhalt | Norm |
|---|---|---|
| Sofort nach Unfall | Black-Box-Daten sichern (6 Monate Aufbewahrungspflicht) | § 1g StVG |
| 3 Jahre | ProdHaftG: Verjährung des Schadensersatzanspruchs | § 12 ProdHaftG |
| 10 Jahre | ProdHaftG: Ausschlussfrist für Haftungsansprüche ab Inverkehrbringen | § 13 ProdHaftG |
| 3 Jahre | StVG § 7: Verjährung nach §§ 195, 199 BGB | § 195 BGB |
| 1 Jahr | CMR Art. 32: Verjährung Frachtführerhaftung | CMR Art. 32 |
| 6 Monate | § 1g StVG: Aufbewahrungspflicht Datenspeicher; danach darf Frachtführer löschen | § 1g StVG |

---

## Typische Gegenargumente

| Gegenargument | Erwiderung |
|---|---|
| "Frachtführer haftet nicht wegen autonomen Systems" | CMR Art. 17 ist verschuldensunabhängige Obhutshaftung; autonomer Modus ändert Haftungsgrundlage nicht; Frachtführer muss Haftungsausschluss Art. 17 Abs. 2 CMR beweisen |
| "§ 7 StVG greift nicht weil autonomes Fahrzeug kein klassisches Kfz" | § 1d StVG ändert nichts an der Halterhaftung nach § 7 StVG; Halter haftet nach § 7 bei jedem Betrieb des Fahrzeugs |
| "Black-Box-Daten sind nicht zugänglich" | § 1g StVG: Pflicht zur Datenspeicherung; § 1h StVG: Auskunftspflicht gegenüber Behörden; gerichtlicher Herausgabeanspruch bei drohender Vernichtung möglich (§ 809 BGB) |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| "Fahrer hätte eingreifen müssen" | Bei Level 3/4: Fahrer ist nur zur Übernahme verpflichtet wenn System Übergabe anfordert; ohne Anforderung keine Eingreifpflicht |

---

## Streitwert / Kosten

| Position | Berechnung |
|---|---|
| Personenschaden (Halterhaftung § 7 StVG) | Bis 7.5 Mio. EUR/Ereignis nach § 12 StVG; voller Schadenersatz bei Produkthaftung |
| Sachschaden | Bis 1 Mio. EUR/Ereignis nach § 12 StVG; unbegrenzt bei ProdHaftG (§ 10 ProdHaftG gilt nicht für Sachschäden über EUR 500) |
| Ladungsschaden CMR | 8.33 SZR/kg Regelhaftung; unbegrenzt bei Art. 29 CMR |
| Produkthaftungsklage | Aufwändiges Sachverständigenverfahren; Gutachtenkosten EUR 20.000–100.000; als Verfahrenskosten ggf. erstattungsfähig |
| Versicherungsregress | Haftpflichtversicherung schöpft Haftungsgrenzen aus; Produkthaftpflicht des Herstellers separat |

---

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Personenschaden durch autonomen LKW | Primär § 7 StVG (Halter), sekundär ProdHaftG (Hersteller); beide als Gesamtschuldner verklagen |
| Ladungsschaden des Frachtkunden | Direktanspruch gegen Frachtführer aus CMR Art. 17; Frachtführer nimmt Regress gegen Hersteller nach ProdHaftG |
| Black-Box-Daten drohen gelöscht zu werden | Einstweilige Verfügung auf Datensicherung nach § 809 BGB; Sicherungsantrag beim KBA nach § 1h StVG |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Technische Aufsicht hat nicht reagiert | Verschuldenshaftung der benannten Person; ggf. auch des Halters für Auswahl und Überwachung nach § 831 BGB |

---

## Anschluss-Skills

- `fachanwalt-transport-speditionsrecht-cmr-haftung` – grenzüberschreitende CMR-Haftung im Detail
- `frachtfuehrerhaftung-pruefen` – systematische Haftungsanalyse CMR/HGB
- `reklamationsschreiben-cmr-hgb` – Reklamation bei Ladungsschaden
- `fachanwalt-transport-speditionsrecht-ladungsschaden` – HGB-Ladungsschaden ohne autonome Komponente

---

## Quellen

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.


---

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `fachanwalt-transport-speditionsrecht-ladungsschaden`

_Ladungsschaden im Gueterverkehr prüfen und geltend machen: Nachweis, Schadensberechnung, Haftungslimits. Normen: §§ 425 431 HGB, Art. 17 23 CMR. Prüfraster: Schadensnachweis, Haftungsgrenze je Kilogramm, Totalschaden, Sonderinteresse. Output: Ladungsschadens-Prüfergebnis und Anspruchsschreiben. Abgrenzung: nicht Lieferverzug._

# Ladungsschaden – Innerdeutscher Frachtverkehr (HGB)

## Kernsachverhalt & Mandantenfragen

Ein Ladungsschaden im innerdeutschen Strassenfrachtverkehr betrifft täglich Tausende von Transporten. Die HGB-Haftung ist konzeptionell ähnlich wie die CMR, aber nicht identisch. Besonders praxisrelevant: Die Möglichkeit, bei qualifiziertem Verschulden nach § 435 HGB die Haftungsobergrenze von 8.33 SZR/kg zu durchbrechen – was die BGH-Rechtsprechung bei Organisationsmängeln großzügig bejaht.

**8 Kaltstart-Rückfragen:**

1. Handelt es sich um einen innerdeutschen Transport (HGB §§ 425 ff.) oder grenzüberschreitend (dann CMR)?
2. Was ist der Schadenstyp: vollständiger Verlust, Teilverlust (Anzahl fehlender Einheiten), Beschädigung, Verspätung?
3. Wann wurde die Sendung übergeben und wann war der Schaden erkennbar? Sofort erkennbar oder erst nach dem Auspacken?
4. Wurde bei der Annahme ein schriftlicher Vorbehalt in den Frachtbrief eingetragen?
5. Welches Gewicht (Bruttogewicht in kg) und welchen Warenwert (EUR) hat die Sendung?
6. Bestand eine Wertdeklaration nach § 449 HGB im Frachtvertrag?
7. Liegen Hinweise auf Organisationsverschulden des Frachtführers vor (fehlende Scans, unsicherer Parkplatz, kein Zugangsnachweis)?
8. Wurde bereits eine schriftliche Reklamation an den Frachtführer gesandt und wann?

---
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 407 HGB | Frachtvertrag: Grundtatbestand; Beförderungspflicht und Haftungsrahmen |
| § 408 HGB | Frachtbrief: Inhalt und Bedeutung |
| § 409 HGB | Vermutungswirkung des Frachtbriefs für ordnungsgemäße Übernahme |
| § 425 HGB | Obhutshaftung: Verlust, Beschädigung, Verspätung zwischen Übernahme und Ablieferung |
| § 426 HGB | Haftungsausschlüsse: unvermeidbare Ereignisse, Sorgfalt eines ordentlichen Frachtführers |
| § 427 HGB | Privilegierungstatbestände: offene Fahrzeuge, fehlende Verpackung, Tiertransport, Schüttgut |
| § 429 HGB | Schadensumfang: Verkehrswert am Übernahmeort; Borsenpreis oder Marktpreis |
| § 431 HGB | Haftungshöchstbetrag: 8.33 SZR/kg Bruttogewicht; bei Verspätung dreifache Fracht |
| § 432 HGB | Ersatz von Zoll, Steuern und sonstigen Kosten bei vollständigem Verlust |
| § 435 HGB | Qualifiziertes Verschulden: Vorsatz oder Leichtfertigkeit mit Bewusstsein = unbegrenzte Haftung |
| § 437 HGB | Regressansprüche: gegen aufeinanderfolgende Frachtführer und Unterfrachtführer |
| § 438 HGB | Schadensanzeige: sofort / 7 Tage / 21 Tage; Beweiswirkung |
| § 439 HGB | Verjährung: 1 Jahr; 3 Jahre bei Vorsatz oder gleichstehendem Verschulden |
| § 449 HGB | Wertdeklaration: Abweichung vom Haftungshöchstbetrag nach oben |
| § 453 HGB | Speditionsvertrag: Abgrenzung zum Frachtvertrag |
| § 458 HGB | Selbsteintritt des Spediteurs: volle Frachtführerhaftung |
| § 459 HGB | Fixkosten-Spediteur: Frachtführerhaftung bei fest vereinbartem Preis |

---

## Leitentscheidungen

| Aktenzeichen | Gericht / Datum | Leitsatz |
|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |
| Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

---

## Prüfschema Ladungsschaden HGB

| Schritt | Inhalt | Grundlage |
|---|---|---|
| 1 | Anwendbares Recht: innerdeutsch → HGB §§ 407 ff.; grenzüberschreitend → CMR | § 407 HGB, CMR Art. 1 |
| 2 | Frachtführer oder Spediteur: Eigenantritt? Festpreis § 459 HGB? ADSp einbezogen? | §§ 453, 458, 459 HGB |
| 3 | Obhutszeitraum bestimmen: Übernahme am [Datum/Ort] bis Ablieferung am [Datum/Ort] | § 425 HGB |
| 4 | Schadensart: Verlust, Teilverlust, Beschädigung, Verspätung | § 425 Abs. 1 HGB |
| 5 | Haftungsausschlüsse: unvermeidbare Ereignisse, Sorgfalt ordentlicher Frachtführer | § 426 HGB |
| 6 | Privilegierungstatbestände: offenes Fahrzeug, unzureichende Verpackung, Schüttgut | § 427 HGB |
| 7 | Schadensberechnung: Verkehrswert am Übernahmeort × Schadensquote | § 429 HGB |
| 8 | Haftungshöchstbetrag: kg × 8.33 SZR × SDR-Tageskurs (Zahlungstag) | § 431 HGB |
| 9 | Wertdeklaration § 449 HGB prüfen: im Frachtvertrag vereinbart? Höchstbetrag aufgehoben? | § 449 HGB |
| 10 | Qualifiziertes Verschulden § 435 HGB: Organisationsmangel? Fehlende Scans? Unsicherer Stellplatz? | § 435 HGB |
| 11 | Reklamationsfrist § 438 HGB: sofort / 7 Tage / 21 Tage; schriftlich und nachweisbar? | § 438 HGB |
| 12 | Verjährung § 439 HGB: 1 Jahr / 3 Jahre; Hemmung durch Reklamation bis schriftliche Ablehnung | § 439 HGB |
| 13 | ADSp-Prüfung: wirksam einbezogen? Inhaltskontrolle nach §§ 307 ff. BGB | § 449 HGB |
| 14 | Regressansprüche § 437 HGB: gegen Unterfrachtführer; wer hat die Sendung tatsächlich befördert? | § 437 HGB |

---

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Ladungsschaden Frachtrecht pruefen | Schadensanzeige; Template unten |
| Variante A — Verdeckter Schaden (erst nach Oeffnung) | Ruegefristen HGB § 438 / CMR Art. 30 beachten; sieben Tage |
| Variante B — Gesamtladung beschaedigt | Totalverlust-Berechnung; Zeitwert oder Wiederbeschaffungswert |
| Variante C — Zollverschluss beschaedigt | Zollrechtliche Haftung parallel zur Frachtrechtshaftung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1 – Schadensersatzforderung (Vollhaftung § 435 HGB)

```
[Briefkopf]
[Ort, Datum]

An [Frachtführer / Spedition, Anschrift]
– Per Einschreiben mit Rückschein –

SCHADENSERSATZFORDERUNG gemäß §§ 425, 435 HGB

Frachtbrief-Nr.: [...]
Transport vom: [Datum]
Von: [Verladeort] Nach: [Entladeort]

Sehr geehrte Damen und Herren,

ich zeige die anwaltliche Vertretung der [Mandantschaft] an.

I. SACHVERHALT

Die Sendung [Bezeichnung], Bruttogewicht [X] kg, Warenwert
EUR [Betrag] (Handelsrechnung Anlage K1), wurde am [Datum]
am Verladeort [Ort] in unversehrtem Zustand übergeben
(Frachtbrief ohne Vorbehalt Anlage K2).

Am [Datum] wurde die Sendung am Zielort [Ort] wie folgt
beschädigt/unvollständig übergeben: [Beschreibung].
Schadensprotokoll Anlage K3, Fotos Anlage K4.

II. REKLAMATION

Reklamation gemäß § 438 HGB erfolgte mit Schreiben vom
[Datum] (Anlage K5, fristgerecht innerhalb 7 Tage nach
Entdeckung des verdeckten Schadens).

III. HAFTUNG

Die Beklagte haftet aus § 425 Abs. 1 HGB. Haftungsaus-
schlüsse § 426 HGB greifen nicht. Hilfsweise: Privilegierung
§ 427 HGB liegt nicht vor, da die Verpackung bei Übernahme
ordnungsgemäß war (Anlage K6: Übernahmefotos).

IV. QUALIFIZIERTES VERSCHULDEN § 435 HGB

Die Beklagte hat leichtfertig im Bewusstsein des wahrschein-
lichen Schadenseintritts gehandelt:
– Kein Eingangsscan bei Übernahme im Depot [Ort]
  Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
– Kein Nachweis des letzten Kontaktpunkts mit der Sendung
– Fahrzeug war [X Stunden] auf unbewachtem Parkplatz abgestellt

Die Haftungsbegrenzung § 431 HGB entfällt.

V. SCHADENSHÖHE

Warenwert: EUR [X] (Anlage K1)
Frachtanteil § 432 HGB (bei Totalverlust): EUR [X]
Zinsen § 352 HGB / § 288 BGB: [X] % ab [Datum]
Gutachterkosten: EUR [X]

GESAMTFORDERUNG: EUR [X]

Wir fordern Zahlung bis [Datum 14 Tage]. Bei Ausbleiben
werden wir klagen. Verjährungsende § 439 HGB: [Datum].

Mit freundlichen Grüßen
[Unterschrift, Kanzlei]
```

### Baustein 2 – Klageerwiderung Frachtführer (Privilegierung § 427 HGB)

```
KLAGEERWIDERUNG

I. PRIVILEG § 427 ABS. 1 NR. 2 HGB (fehlende Verpackung)

Die Sendung war bei Übernahme unzureichend verpackt.
Dies ergibt sich aus: [Frachtbrief-Vermerk "Verpackung mangel-
haft" vom Fahrer eingetragen, Anlage B1; Fotos Anlage B2].

Der Frachtführer hat die Unzulänglichkeit bei Übernahme
dokumentiert und Beförderung unter Vorbehalt durchgeführt.
Das typische Risiko solcher Verpackung hat sich realisiert.

II. KEIN QUALIFIZIERTES VERSCHULDEN § 435 HGB

Der Frachtführer betreibt ein vollständiges Kontrollsystem:
– Eingangsscan bei Übernahme (Anlage B3)
– Ausgangsscan bei Verladung (Anlage B4)
– GPS-Fahrzeugdaten (lückenlose Strecke, Anlage B5)
– Abgesicherter Parkplatz [Standort] mit Videoüberwachung

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

III. HILFSWEISE HAFTUNGSHÖCHSTBETRAG § 431 HGB

Selbst wenn Haftung besteht, ist sie auf § 431 HGB begrenzt:
[X] kg × 8.33 SZR × SDR-Kurs EUR [Z] = EUR [Betrag].

[Ort, Datum, Unterschrift]
```

### Baustein 3 – Regressklage Hauptfrachtführer gegen Unterfrachtführer

```
AN DAS AMTSGERICHT / LANDGERICHT [...]

Kläger: [Hauptfrachtführer]
Beklagter: [Unterfrachtführer]

Streitwert: EUR [bereits gezahlter Betrag]

KLAGE auf Regress gemäß § 437 HGB

Der Kläger hat an den Auftraggeber [Name] EUR [X] als
Schadensersatz für den Ladungsschaden aus dem Transport
vom [Datum] geleistet.

Der Schaden entstand nach Übergabe der Sendung an den
Beklagten als Unterfrachtführer in [Ort] am [Datum]
(Übergabe-Protokoll Anlage K1 ohne Schäden).

Gemäß § 437 HGB (Rückgriff gegenüber Unterfrachtführer)
ist der Beklagte verpflichtet, den Schaden zu erstatten.

ANTRAG:
Der Beklagte wird verurteilt, EUR [X] nebst Zinsen zu zahlen.

[Ort, Datum, Unterschrift]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Beweislast

| Konstellation | Beweislast |
|---|---|
| Übernahme in ordnungsgemäßem Zustand | Absender; erleichtert durch Frachtbrief ohne Frachtführer-Vorbehalt (§ 409 HGB Vermutung) |
| Schaden im Obhutszeitraum | Anspruchsteller; durch Ablieferungsprotokoll und Fotos |
| Haftungsausschluss § 426 HGB | Frachtführer trägt Beweis für unvermeidbare Ereignisse |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

---

## Fristen und Verjährung

| Frist | Inhalt | Norm |
|---|---|---|
| Sofort bei Annahme | Äußerlich erkennbarer Schaden/Verlust: schriftlicher Vorbehalt im Frachtbrief | § 438 Abs. 1 HGB |
| 7 Tage nach Ablieferung | Verdeckter (nicht erkennbarer) Schaden: schriftliche Anzeige | § 438 Abs. 2 HGB |
| 21 Tage nach Ablieferung | Verspätungsanzeige | § 438 Abs. 4 HGB |
| 1 Jahr | Reguläre Verjährung: ab Ablieferungstag (bei Verlust: 30 Tage nach vereinbarter Lieferfrist) | § 439 Abs. 2 HGB |
| 3 Jahre | Verlängerte Verjährung bei Vorsatz oder gleichstehendem Verschulden | § 439 Abs. 1 S. 2 HGB |
| Hemmung | Durch schriftliche Reklamation bis schriftliche Ablehnung | § 439 Abs. 3 HGB |

---

## Typische Gegenargumente

| Gegenargument | Erwiderung |
|---|---|
| "Wir haften maximal 8.33 SZR/kg; mehr ist vertraglich ausgeschlossen" | § 449 HGB: Unterschreitung des gesetzlichen Höchstbetrags nicht wirksam; § 435 HGB-Haftung gilt zwingend bei qualifiziertem Verschulden und kann nicht abbedungen werden |
| "Frachtbrief-Vorbehalt fehlt; Anspruch erloschen" | § 438 HGB begründet nur Beweisvermutung zugunsten Frachtführer, keinen materiellen Anspruchsverlust; Schaden kann trotzdem bewiesen werden |
| "Schaden entstand durch unzureichende Verpackung" | § 427 HGB Abs. 1 Nr. 2: Frachtführer muss beweisen, dass Verpackungsmangel erkennbar war und er Vorbehalt eingetragen hat; stille Übernahme schließt diesen Einwand aus |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Streitwert / Kosten

| Position | Berechnung |
|---|---|
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Vollhaftung § 435 HGB | Voller Warenwert gemäß Handelsrechnung; erheblich höher |
| Anwaltsgebühren Gegenstandswert EUR 30.000 | Ca. EUR 2.400 netto (VV-RVG 2300) |
| Sachverständigengutachten | EUR 1.500–5.000; als Schadensposition bei § 435 HGB-Erfolg erstattungsfähig |
| Gerichtskosten AG (bis EUR 10.000) / LG (über EUR 10.000) | Nach GKG Anlage 2 |

---

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Warenwert viel höher als Haftungslimit | § 435 HGB-Weg: Organisationsmangel recherchieren; Scan-Protokoll anfordern; GPS-Daten sichern |
| Frachtführer hat bereits gezahlt (Regelhaftung) | Prüfen ob § 435 HGB-Differenzbetrag noch geltend machbar; Verjährung beachten |
| Spediteur in der Kette | Ist Spediteur Hauptfrachtführer (Eigenantritt § 458 oder Festpreis § 459 HGB) oder nur Vermittler? |
| Hochwertige Sendung ohne Wertdeklaration | Für künftige Transporte: Art. 24 CMR / § 449 HGB nutzen; Wertdeklaration im Frachtbrief |
| Verspätungsschaden (Produktionsstillstand) | § 431 Abs. 3 HGB: Verspätungshaftung auf dreifache Fracht begrenzt; besonderes Lieferinteresse in Frachtbrief eintragen für höhere Haftung |

---

## Anschluss-Skills

- `reklamationsschreiben-cmr-hgb` – Musterschreiben für Reklamation
- `frachtfuehrerhaftung-pruefen` – Haftungsabgrenzung CMR vs. HGB
- `fachanwalt-transport-speditionsrecht-cmr-haftung` – grenzüberschreitender Transport
- `fachanwalt-transport-autonome-lkw-konvois-haftung-1d-stvg` – Sonderfälle autonomer Transport

---

## Quellen

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `fachanwalt-transport-adr-gefahrgut`

_Gefahrguttransport-Haftung und ADR-Verstoss klaeren: Gefahrgutkennzeichnung, Verantwortlichkeiten, Bußgelder. Normen: ADR, §§ 407 ff. HGB, GefahrgutG. Prüfraster: ADR-Klassen, Kennzeichnungspflicht, Haftungsverteilung. Output: Gefahrgut-Haftungsanalyse und Massnahmenplan. Abgrenzung: nicht allgemeine Frachtführerhaftung HGB._

# ADR-Gefahrgut-Transport

## Zweck

Compliance bei Gefahrgut-Transport, Sanktionen bei Verstoß.

## 1) ADR — Europaeisches UEbereinkommen

### Anwendungs-Bereich

- Straßengueter-Transport
- Internationale und nationale Strecke
- Pflicht ab kleinen Mengen je nach Klasse

### Klassen

- Klasse 1: Explosivstoffe
- Klasse 2: Gase
- Klasse 3: Entzündliche Fluessigkeiten
- Klasse 4.1: Entzündliche Feststoffe
- Klasse 5: Oxidierende Stoffe / Peroxide
- Klasse 6: Giftige / Ansteckende Stoffe
- Klasse 7: Radioaktive Stoffe
- Klasse 8: AEtzende Stoffe
- Klasse 9: Sonstige

## 2) Verpackungs-Gruppen

- I: Hochgefaehrlich
- II: Mittelgefaehrlich
- III: Niedriggefaehrlich

## 3) Kennzeichnung

- UN-Nummer (4-stellig)
- Gefahrgut-Bezeichnung
- Gefahrenklasse-Etiketten
- Orange-Tafel am Fahrzeug

## 4) Gefahrgut-Beauftragter § 3 GbV

### Pflicht-Unternehmen

- Beförderung, Verpackung, Beladung Gefahrgut

### Aufgaben § 8 GbV

- Compliance-Überwachung
- Schulung
- Vorfall-Anzeige
- Jahres-Bericht an Geschäftsleitung

### Qualifikation

- Schulung IHK
- Prüfung
- Fortbildung 5 Jahre

## 5) Anzeige bei Vorfällen

### An wer

- Bundesamt für Materialforschung (BAM)
- Bei schwerem Vorfall: zuständige Landes-Behörde
- Bei Verkehrsunfall: Polizei + Feuerwehr

### Frist

- Schwerer Vorfall: unverzueglich
- Standardvorfall: Jahresbericht

## 6) Workflow Compliance

### Phase 1 — Audit

- Pflicht-Prüfung Gefahrgut-Beauftragter
- Schulungs-Plan Personal
- Verpackungs-Genehmigung prüfen

### Phase 2 — Vorbereitung

- Gefahrgut-Anweisung
- Frachtdokument-Vorlagen
- Notfall-Plan

### Phase 3 — Vorfall

- Sofort-Maßnahmen
- Anwalt einschalten
- Anzeige Behörde

## 7) Sanktionen

### Bußgeld

- Bis 50.000 EUR (§ 17 GGVSEB)
- Bei Vorsatz / Wiederholung: höher

### Strafbarkeit § 328 StGB

- Bei Gefährdung durch ionisierende Strahlung etc.
- Freiheits-Strafe

## 8) Typische Fehler

1. **Gefahrgut-Beauftragter nicht bestellt**
2. **Schulung nicht aktuell**
3. **Kennzeichnung mangelhaft**
4. **Anzeige Behörde versäumt** bei Vorfall

## Anschluss

- `fachanwalt-transport-speditionshaftung-hgb` — bei Haftungs-Frage
- `fachanwalt-transport-cmr-schadensregulierung` — bei int. Transport
- `testakten/umweltrecht-industrieanlage-genehmigung` — bei verbundenen Anlagen

## Aktuelle Rechtsprechung Gefahrgut / ADR

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen ADR / Gefahrgut

- ADR (European Agreement concerning the International Carriage of Dangerous Goods by Road) — Anlage A (Einstufung, Verpackung) und Anlage B (Befoerderungsbedingungen)
- § 3 GbV (Gefahrgutbeauftragtenverordnung) — Bestellpflicht Gefahrgutbeauftragter
- § 35 GGVSEB (Gefahrgutverordnung Strasse, Eisenbahn und Binnenschifffahrt) — Sanktionsnormen
- § 431 HGB — Haftungsbegrenzung Frachtfuehrer (SDR-Betrag; entfaellt bei qualifiziertem Verschulden)
- § 435 HGB — qualifiziertes Verschulden: Vorsatz oder Leichtfertigkeit in Kenntnis wahrscheinlichen Schadenseintritts

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `fachanwalt-transport-speditionsrecht-lieferverzug`

_Lieferverzug im Gueterverkehr prüfen: Verspaetungsschaden, Haftungshoechstbetrag, Fristen. Normen: §§ 423 425 HGB, Art. 19 23 CMR. Prüfraster: Ablieferungsfrist, Verspaetungsschaden, Haftungsgrenze dreifacher Frachtpreis, Verjaebrung. Output: Lieferverzug-Haftungsanalyse. Abgrenzung: nicht Ladungsschaden._

# Lieferverzug

## Kaltstart-Rückfragen

1. Wurde eine konkrete Lieferfrist vereinbart oder gilt eine angemessene Frist § 423 HGB?
2. Inländischer Transport (HGB) oder grenzüberschreitend (CMR)?
3. Wann ist die Ablieferung tatsächlich erfolgt und wie viele Tage Verzug liegen vor?
4. Welcher Schaden ist eingetreten (Vertragsstrafe gegenüber Endkunde, Produktionsausfall, Deckungskäufe)?
5. Wurde die Schadensanzeige binnen 21 Tagen § 438 Abs. 3 HGB erstattet?

## Anspruchsgrundlagen

- Lieferfrist § 423 HGB — vereinbarte Frist oder angemessene Frist; Wegfall des Lieferinteresses führt zu Schadensersatz wegen Nichterfüllung.
- Haftung für Lieferverzug § 425 HGB.
- Höchstbetrag bei reinem Verzugsschaden § 431 Abs. 3 HGB — höchstens dreifache Fracht.
- CMR Art. 19: Lieferverzug wenn vereinbarte Frist überschritten oder bei fehlender Frist die Frist, die einem sorgfältigen Frachtführer billigerweise zugestanden werden muss, überschritten ist.
- CMR Art. 23 Abs. 5: Verzugsentschädigung höchstens Frachtbetrag.
- Wertdeklaration § 449 HGB / Art. 26 CMR durchbricht Höchstbetrag.
- Qualifiziertes Verschulden § 435 HGB / Art. 29 CMR unbegrenzte Haftung.
- Schadensanzeige § 438 Abs. 3 HGB / Art. 30 Abs. 3 CMR: 21 Tage nach Ablieferung — sonst Anspruch erloschen (CMR) bzw. Beweislastnachteil (HGB).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Beweislast und Frist

- Anspruchsteller trägt Beweis für vereinbarte oder angemessene Lieferfrist, Verzug, Schaden und Kausalität.
- Frachtführer trägt Beweis für Entlastung § 426 HGB / Art. 17 Abs. 2 CMR.
- Schadensanzeige § 438 Abs. 3 HGB: binnen 21 Tagen schriftlich.
- CMR Art. 30 Abs. 3 CMR: binnen 21 Tagen schriftlich, sonst Anspruch ausgeschlossen.
- Verjährung § 439 HGB / Art. 32 CMR ein Jahr.

## Prüfschema

```
1. Anwendungsbereich HGB oder CMR?
2. Lieferfrist konkret oder angemessen § 423 HGB / Art. 19 CMR
3. Verzugseintritt + tatsaechliche Ablieferung
4. Schadensanzeige 21 Tage gewahrt?
5. Entlastungsbeweis Frachtfuehrer
6. Schadenshoehe
   - HGB: dreifache Fracht § 431 Abs. 3 HGB
   - CMR: Frachtbetrag Art. 23 Abs. 5 CMR
7. Wertdeklaration § 449 HGB / Art. 26 CMR pruefen
8. Qualifiziertes Verschulden § 435 HGB / Art. 29 CMR
9. Wegfall Lieferinteresse § 423 HGB — Schadensersatz statt Erfuellung
```

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Schreibvorlage Verzugsforderung

```
Sehr geehrte Damen und Herren,

namens und in Vollmacht unserer Mandantschaft machen wir Schadens-
ersatz wegen Lieferverzugs aus dem Frachtvertrag vom [Datum]
(Frachtbrief-Nr. [...]) geltend.

Sachverhalt:
- Vereinbarte Lieferfrist: Ankunft beim Empfaenger spaetestens [Datum/
  Uhrzeit] gemaess Frachtauftrag Ziffer [X] (Anlage K1)
- Tatsaechliche Ablieferung: [Datum/Uhrzeit] = [N] Stunden / Tage
  Verzug
- Schadensanzeige § 438 Abs. 3 HGB / Art. 30 Abs. 3 CMR mit Schreiben
  vom [Datum] (innerhalb 21 Tage)

Haftung:
- Lieferfrist nicht eingehalten § 423 HGB / Art. 19 CMR
- Entlastung § 426 HGB / Art. 17 Abs. 2 CMR nicht ersichtlich
- Hilfsweise Qualifiziertes Verschulden § 435 HGB / Art. 29 CMR durch
  [Pflichtverletzung]

Schaden:
- Vertragsstrafe an Endkunde EUR [Betrag] (Anlage K2)
- Produktionsausfall EUR [Betrag] (Anlage K3)
- Deckungskaeufe EUR [Betrag] (Anlage K4)

Hoechstbetrag bei reinem Verzugsschaden:
- HGB: dreifache Fracht EUR [Betrag]
- CMR: Frachtbetrag EUR [Betrag]
Bei Qualifiziertem Verschulden Vollersatz.

Wir fordern Sie auf binnen 14 Tagen EUR [Betrag] zu erstatten. Die
Verjaehrungsfrist § 439 HGB / Art. 32 CMR endet am [Datum].

Mit freundlichen Gruessen
```

## Übergabe

- Bei Ablehnung: Klage am Frachtführersitz bzw. Ablieferungsort.
- Verjährungsfrist im Aktenkalender notieren.
- Bei größerem Schaden Wertdeklaration § 449 HGB / Art. 26 CMR für künftige Aufträge empfehlen.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

