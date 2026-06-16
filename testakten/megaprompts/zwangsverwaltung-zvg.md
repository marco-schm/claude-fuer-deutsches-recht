# Megaprompt: zwangsverwaltung-zvg

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 58 Skills des Plugins `zwangsverwaltung-zvg`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Zwangsverwaltung ZVG: ordnet Rolle (Gläubiger, Schuldner Eigentümer, Zwangsverwalter), …
2. **zwangsverwaltung-erstpruefung-und-mandatsziel** — Zwangsverwaltung: Erstprüfung, Rollenklärung und Mandatsziel.
3. **aktenanlage-objektcockpit** — Aktenanlage und Objektcockpit für den Zwangsverwalter nach §§ 146 ff. ZVG. Anwendungsfall Zwangsverwaltungsauftrag geht …
4. **berichtswesen-besitzuebernahme-bestellung** — Berichterstattung an das Vollstreckungsgericht in der Zwangsverwaltung nach §§ 153 154 ZVG. Anwendungsfall Zwangsverwalt…
5. **besitzuebernahme** — Besitzerlangung über das Zwangsverwaltungsobjekt nach § 150 ZVG. Anwendungsfall Zwangsverwalter nimmt erstmals Besitz am…
6. **bestellung-beschlagnahme** — Prüft Bestellungsbeschluss und Beschlagnahme am Anfang einer Zwangsverwaltung nach §§ 146-149 ZVG. Anwendungsfall Anordn…
7. **betriebskosten-hausgeld-bieterangebot** — Betriebskosten Hausgeld und laufende Objektkosten in der Zwangsverwaltung. Anwendungsfall Zwangsverwalter muss Nebenkost…
8. **bieterangebot-bewertung** — Bewertet Zwangsversteigerungsobjekte aus Investorensicht für Bieterentscheidung. Anwendungsfall Investor erwaeegt Kauf i…
9. **glaeubiger-schuldner-kommunikation** — Schriftwechsel in der Zwangsverwaltung mit Schuldner Gläubiger Mieter Gericht Versicherern und Dienstleistern. Anwendung…
10. **instandhaltung-sicherung** — Instandhaltung Sicherung und Gefahrenabwehr am Zwangsverwaltungsobjekt. Anwendungsfall Objekt weist Sicherheitsmaengel a…
11. **kommandocenter** — Kommandocenter für Zwangsverwaltung — Triage und Routing zu allen ZVG-Skills. Anwendungsfall Zwangsverwalter oeffnet Plu…
12. **konten-kassenfuehrung-miet-pachtverwaltung** — Kontenführung und Buchführung des Treuhandkontos in der Zwangsverwaltung. Anwendungsfall Zwangsverwalter muss Einnahmen …
13. **miet-und-pachtverwaltung** — Miet- und Pachtverwaltung in der Zwangsverwaltung einschließlich Vertragsuebernahme und Zahlungseinzug. Anwendungsfall Z…
14. **mieteinzug-rueckstaende** — Mieteinzug und Rückstandsbehandlung in der Zwangsverwaltung. Anwendungsfall Mieter zahlt nicht und Zwangsverwalter muss …
15. **oeffentliche-lasten** — Öffentliche Lasten und grundstuecksbezogene Abgaben in der Zwangsverwaltung. Anwendungsfall Grundsteuer Erschließungsgeb…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Zwangsverwaltung ZVG: ordnet Rolle (Gläubiger, Schuldner Eigentümer, Zwangsverwalter), markiert Frist (Beschwerde gegen Anordnung), wählt Norm (ZVG §§ 146 ff., BGB §§ 1135 ff. Pflichten) und Zuständigkeit (Amtsgericht Vollstreckungsgericht), leitet zum passenden S..._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Zwangsverwaltung Zvg** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `aktenanlage-objektcockpit` — Aktenanlage Objektcockpit
- `berichte-beschlagnahme-mietverwaltung-besitz` — Berichte Beschlagnahme Mietverwaltung Besitz
- `berichtswesen-besitzuebernahme-bestellung` — Berichtswesen Besitzuebernahme Bestellung
- `beschlagnahme-fristen-form-und-zustaendigkeit` — Beschlagnahme Fristen Form und Zustaendigkeit
- `beschlagnahme-mietverwaltung-start` — Beschlagnahme Mietverwaltung Start
- `beschlagnahme-oeffentliche-lasten` — Beschlagnahme Oeffentliche Lasten
- `besitz-dokumentenmatrix-und-lueckenliste` — Besitz Dokumentenmatrix und Lueckenliste
- `besitzuebernahme` — Besitzuebernahme
- `bestellung-beschlagnahme` — Bestellung Beschlagnahme
- `betriebskosten-hausgeld-bieterangebot` — Betriebskosten Hausgeld Bieterangebot
- `bieterangebot-bewertung` — Bieterangebot Bewertung
- `bieterangebote-mieten-oeffentliche` — Bieterangebote Mieten Oeffentliche
- `gate-fehlerkatalog` — Gate Fehlerkatalog
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Zwangsverwaltung Zvg sind ZVG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `zwangsverwaltung-erstpruefung-und-mandatsziel`

_Zwangsverwaltung: Erstprüfung, Rollenklärung und Mandatsziel._

# Zwangsverwaltung: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu **Zwangsverwaltung Erstpruefung Und Mandatsziel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Zwangsverwaltung Zvg** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 5 Abs. 3 Satz 1 GG` — Wissenschaftsfreiheit.
- `Art. 12 Abs. 1 GG` — Berufswahl- und Ausbildungsbezug.
- `Art. 3 Abs. 1 GG` — Gleichbehandlung und Bewertungsfairness.
- `§ 2 HRG` — Aufgaben der Hochschulen.
- `§ 4 HRG` — Freiheit von Forschung, Lehre und Studium.
- `§ 7 HRG` — Ziel des Studiums.
- `§ 15 HRG` — Prüfungen und Leistungspunktsystem.
- `§ 16 HRG` — Prüfungsordnungen.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist.
- `§ 123 Abs. 1 VwGO` — Eilrechtsschutz bei Studien-/Prüfungsentscheidungen.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: Zwangsverwaltung: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** ZVG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Zwangsverwaltung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `aktenanlage-objektcockpit`

_Aktenanlage und Objektcockpit für den Zwangsverwalter nach §§ 146 ff. ZVG. Anwendungsfall Zwangsverwaltungsauftrag geht ein und Objekt muss komplett erfasst werden. Normen §§ 146 152 ZVG Bestellung § 154 ZVG Pflichten § 155 ZVG Einnahmen Ausgaben. Prüfraster Objektkarte Beteiligtenregister Mieter..._

# Aktenanlage und Objektcockpit

## Arbeitsbereich

Aktenanlage und Objektcockpit für den Zwangsverwalter nach §§ 146 ff. ZVG. Anwendungsfall Zwangsverwaltungsauftrag geht ein und Objekt muss komplett erfasst werden. Normen §§ 146 152 ZVG Bestellung § 154 ZVG Pflichten § 155 ZVG Einnahmen Ausgaben. Prüfraster Objektkarte Beteiligtenregister Mieterliste Lasten Treuhandkonto Fristen Berichte Wiedervorlagen. Output Vollständiges Objektcockpit als Arbeitsbasis für alle Folge-Skills der Zwangsverwaltung. Abgrenzung zu zvg-bestellung-beschlagnahme (rechtlicher Bestellvorgang) und zvg-miet-und-pachtverwaltung. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Startet bei

- eine neue Zwangsverwaltung übernommen wird
- Bestandsakten unvollständig sind
- Berichte und Rechnungslegung aufgebaut werden müssen

## Eingaben

- Bestellungsurkunde, Grundbuchdaten, Objektunterlagen
- Mietverträge, Betriebskosten, Versicherungen, öffentliche Lasten
- Kontodaten und Gerichtsvorgaben

## Workflow

1. **Akte aufsetzen** - Objekt, Beteiligte, Aktenzeichen, Bestallung und Zuständigkeiten erfassen.
2. **Register bauen** - Mieter/Pächter, Lasten, Verträge, Versicherungen, Dienstleister und Schlüssel erfassen.
3. **Finanzen** - Treuhandkonto, Sollmieten, Istmieten, Ausgaben und Vorschusslogik anlegen.
4. **Berichte** - Besitzerlangungsbericht, Monats- und Jahresrechnung vormerken.

## Ausgabe

- Objektkarte
- Rent Roll
- Lasten- und Versicherungsregister
- Wiedervorlagen

## Qualitätsgates

- jede Nutzungseinheit mit Sollmiete
- öffentliche Lasten separat
- Buchführung getrennt

## Rote Schwellen

- fehlende Bestallungsurkunde
- Objektzugang ungeklärt
- kein Treuhandkonto

## Interne Vorlagen

- assets/templates/zvg-objektkarte.md
- assets/templates/mieterliste-rent-roll.md

## Amtliche Erstquellen

- § 2 ZwVwV
- § 13 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Aktenanlage/Objektcockpit

§ 152 ZVG (Pflichten Zwangsverwalter) → § 153 ZVG (Nutzungen) → §§ 2-5 ZwVwV (Aufgaben Verwalter) → § 13 ZwVwV (Buchführung) → § 14 ZwVwV (Rechnungslegung) → § 154 ZVG (Gerichtliche Aufsicht) → § 159 ZVG (Aufhebung Zwangsverwaltung)

## Triage Aktenanlage

Kläre bei Übernahme:
1. Liegt die vollständige Bestellungsurkunde vor? (Pflichtdokument — ohne keine Legitimation)
2. Grundbuchauszug aktuell (max. 3 Monate alt)?
3. Alle Nutzungseinheiten mit Mietverträgen erfasst?
4. Treuhandkonto bei einer Bank eröffnet und dem Gericht benannt?
5. Etwaige Vorlasten (Grundschulden Grundpfandrechte) aus Abt. III Grundbuch erfasst?

## Output-Template Objektkarte (Auszug)

```
OBJEKTKARTE — ZWANGSVERWALTUNG
Aktenzeichen Vollstreckungsgericht: [AZ]
Bestellungsurkunde vom: [DATUM]

Objekt: [ADRESSE, GRUNDBUCHBEZEICHNUNG]
Gemarkung / Flurstück: [...]
Grundbuch: Amtsgericht [X], Blatt [Y]

BETEILIGTE
Schuldner: [NAME, ADRESSE]
Gläubiger: [NAME, ADRESSE, FORDERUNG]
Vollstreckungsgericht: AG [ORT], Richter/Rechtspfleger: [NAME]
Zwangsverwalter: [NAME, BÜRO, TELEFON]

NUTZUNGSEINHEITEN
Nr. | Lage | Mieter | Nettomiete | NK-Vorauszahlung | Vertrag vom
1 | ... | ... | ... | ... | ...

TREUHANDKONTO: [BANK, IBAN]
LETZTER GERICHT-BERICHT: [DATUM]
NÄCHSTER BERICHT FÄLLIG: [DATUM]
```

---

## Skill: `berichtswesen-besitzuebernahme-bestellung`

_Berichterstattung an das Vollstreckungsgericht in der Zwangsverwaltung nach §§ 153 154 ZVG. Anwendungsfall Zwangsverwalter muss Besitzerlangungsbericht Sachstandsbericht Monatsbericht oder Entscheidungsvorlage erstellen. Normen § 153 ZVG Pflichten § 155 ZVG Einnahmen Ausgaben § 161 ZVG Rechnungsl..._

# Berichtswesen an das Vollstreckungsgericht

## Arbeitsbereich

Berichterstattung an das Vollstreckungsgericht in der Zwangsverwaltung nach §§ 153 154 ZVG. Anwendungsfall Zwangsverwalter muss Besitzerlangungsbericht Sachstandsbericht Monatsbericht oder Entscheidungsvorlage erstellen. Normen § 153 ZVG Pflichten § 155 ZVG Einnahmen Ausgaben § 161 ZVG Rechnungslegung. Prüfraster Besitzerlangung Sachstand Einnahmen Ausgaben Mieter offene Fragen Gerichtsbeschluss-Bedarf. Output Gerichtskonformer Bericht mit Darstellung Einnahmen Ausgaben Mietsituation und Handlungsempfehlungen. Abgrenzung zu zvg-rechnungslegung (Jahresrechnung) und zvg-gläubiger-schuldner-kommunikation. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Startet bei

- Besitzerlangungsbericht fällig ist
- Gericht Sachstand oder Entscheidungsvorlage verlangt
- wesentliche Ereignisse im Objekt auftreten

## Eingaben

- Objektkarte, Besitzprotokoll, Rent Roll
- Kontostand, Rückstände, Maßnahmen, Risiken
- gerichtliche Verfügung

## Workflow

1. **Adressat und Anlass** - Berichtstyp, Zeitraum und konkrete gerichtliche Frage bestimmen.
2. **Faktenblock** - Objekt, Nutzung, Mieten, Lasten, Maßnahmen, Konto und Risiken aktualisieren.
3. **Entscheidungsbedarf** - Zustimmung, Vorschuss, Maßnahme oder Verteilung klar herausstellen.
4. **Anlagen** - Fotos, Konto, Belege und Tabellen referenzieren.

## Ausgabe

- Besitzerlangungsbericht
- Sachstandsbericht
- Gerichtliche Entscheidungsvorlage

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Qualitätsgates

- § 3 ZwVwV-Bericht vollständig
- Zahlen mit Anlagen
- offene Ermittlungen benannt

## Rote Schwellen

- Gefahr oder Versicherungslücke nicht gemeldet
- Vorschussbedarf verschwiegen
- Bericht ohne Kontostand

## Interne Vorlagen

- assets/templates/monatsbericht-gericht.md
- assets/templates/besitzuebernahme-protokoll.md

## Amtliche Erstquellen

- § 3 ZwVwV
- § 16 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Berichtswesen

§ 153 ZVG (Pflichten laufende Verwaltung) → § 154 ZVG (Gerichtliche Aufsicht) → § 3 ZwVwV (Besitzerlangungsbericht) → § 14 ZwVwV (Jahresrechnung) → § 15 ZwVwV (Schlussrechnung) → § 20 ZwVwV (Vergütung)

## Triage Berichtswesen

1. Wann war der Besitzerlangungstermin? (2-Wochen-Frist für Besitzerlangungsbericht)
2. Welche Berichtsfrequenz hat das Gericht vorgegeben? (Monatlich / Quartalsweise / Jährlich)
3. Sind alle Mieter und Nutzungseinheiten im Bericht vollständig erfasst?
4. Wurden wesentliche Veränderungen (Leerstand Kündigung Mietausfall) zeitnah gemeldet?

## Output-Template Besitzerlangungsbericht (Auszug)

**Adressat:** Amtsgericht / Vollstreckungsgericht — Tonfall formell-berichtend

```
An das Amtsgericht [ORT]
Vollstreckungsgericht
Aktenzeichen: [AZ]

Besitzerlangungsbericht
Zwangsverwaltung [ADRESSE]

Sehr geehrte Damen und Herren,

gemäß § 3 ZwVwV erstattet der Unterzeichner Bericht über die Besitzerlangung
am [DATUM]:

1. Zustand des Objekts: [BESCHREIBUNG]
2. Nutzungseinheiten: [TABELLE MIETER/EINHEITEN]
3. Vorgefundene Mängel/Sofortmaßnahmen: [LISTE]
4. Laufende Verträge (Versicherung Dienstleister): [LISTE]
5. Besondere Vorkommnisse: [GGFS. SCHULDNER ANWESEND / ZUGANG VERWEIGERT]
6. Treuhandkonto: Eröffnet bei [BANK], IBAN [X].

[DATUM, UNTERSCHRIFT ZWANGSVERWALTER]
```

---

## Skill: `besitzuebernahme`

_Besitzerlangung über das Zwangsverwaltungsobjekt nach § 150 ZVG. Anwendungsfall Zwangsverwalter nimmt erstmals Besitz am Objekt und muss alle Tatsachen dokumentieren. Normen § 150 ZVG Besitzuebernahme § 151 ZVG Rechte und Pflichten § 535 BGB Mietverhältnisse. Prüfraster Vor-Ort-Termin Objektbesch..._

# Besitzerlangung und Objektaufnahme

## Arbeitsbereich

Besitzerlangung über das Zwangsverwaltungsobjekt nach § 150 ZVG. Anwendungsfall Zwangsverwalter nimmt erstmals Besitz am Objekt und muss alle Tatsachen dokumentieren. Normen § 150 ZVG Besitzuebernahme § 151 ZVG Rechte und Pflichten § 535 BGB Mietverhältnisse. Prüfraster Vor-Ort-Termin Objektbeschreibung Nutzungen Rechte Mobilien Forderungen Lasten Ausgaben Schlüssel. Output Besitzerlangungsbericht mit Objektprotokoll Fotodokumentation Schlüsselliste und Meldung ans Gericht. Abgrenzung zu zvg-aktenanlage-objektcockpit und zvg-berichtswesen-gericht. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Startet bei

- Objekt erstmals betreten oder übernommen wird
- Schlüssel, Zustand und Mieter zu erfassen sind
- Sofortmaßnahmen wegen Gefahr oder Versicherung nötig sind

## Eingaben

- Bestallung, Objektadresse, Schlüsselinfo
- Mieter- und Pächterdaten
- Fotos, Zählerstände, Versicherungen, Dienstleister

## Workflow

1. **Termin vorbereiten** - Beteiligte informieren, Zutritt, Zeugen, Kamera und Checkliste sichern.
2. **Objekt aufnehmen** - Nutzungsart, Zustand, Drittrechte, Mobilien, Forderungen, Lasten und Ausgaben protokollieren.
3. **Gefahren sichern** - Versicherung, Wasser, Strom, Brand, Verkehrssicherung und Notdienst prüfen.
4. **Bericht einreichen** - Besitzerlangungsbericht ans Gericht und Nachermittlungen vormerken.

## Ausgabe

- Besitzübernahmeprotokoll
- Objektzustandsbericht
- Sofortmaßnahmenliste

## Qualitätsgates

- § 3 ZwVwV-Punkte vollständig abgefragt
- Fotos/Belege referenziert
- Nachermittlungen terminiert

## Rote Schwellen

- akute Gefahrenstelle
- fehlende Gebäudeversicherung
- Schuldner verweigert Zugang

## Interne Vorlagen

- assets/templates/besitzuebernahme-protokoll.md
- assets/templates/instandhaltung-gefahrensicherung.md

## Amtliche Erstquellen

- § 3 ZwVwV
- § 152 ZVG

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Besitzübernahme

§ 150 ZVG (Besitzeinweisung durch Gericht) → § 152 ZVG (Rechte und Pflichten ab Besitzerlangung) → § 3 ZwVwV (Besitzerlangung und Bericht) → § 858 BGB (verbotene Eigenmacht) → § 869 BGB (Besitzschutz Zwangsverwalter) → § 154 ZVG (Gerichtshilfe bei Verweigerung)

## Triage Besitzübernahme

1. Liegt die Bestallungsurkunde des Gerichts vor? (Legitimation für Vor-Ort-Termin)
2. Sind alle Mieter vorab informiert worden? (Schreiben mind. 3 Tage vorher)
3. Wer begleitet den Termin? (Zeuge empfohlen bei unklarer Situation, ggf. Schlüsseldienst)
4. Sind Versicherungsnachweise bereits angefordert? (Gebäudeversicherung Pflicht ab Besitzerlangung)
5. Fotodokumentation vorbereitet? (Zustands-Beweis für spätere Haftungsfragen)

## Output-Template Besitzübernahmeprotokoll (Auszug)

```
Besitzübernahmeprotokoll
Zwangsverwaltung [ADRESSE]
Aktenzeichen: [AZ]
Datum/Uhrzeit des Termins: [DATUM] [UHRZEIT]
Anwesende: [ZWANGSVERWALTER, ZEUGE, ggf. SCHULDNER, MIETER]

1. Schlüsselübergabe: [JA/NEIN, wer übergeben, Anzahl Schlüsselsätze]
2. Zählerstände: Strom [X], Gas [Y], Wasser [Z]
3. Vorgefundene Schäden (Fotos als Anhang): [LISTE]
4. Mieter angetroffen: [JA/NEIN, Name, Einheit]
5. Sofortmaßnahmen erforderlich: [LISTE]
6. Schuldner anwesend: [JA/NEIN, Reaktion]

Unterschrift Zwangsverwalter: ___________________
Unterschrift Zeuge: ___________________
```

---

## Skill: `bestellung-beschlagnahme`

_Prüft Bestellungsbeschluss und Beschlagnahme am Anfang einer Zwangsverwaltung nach §§ 146-149 ZVG. Anwendungsfall Anordnungsbeschluss des Vollstreckungsgerichts liegt vor und Bestellung muss rechtlich geprüft werden. Normen § 146 ZVG Anordnung § 148 ZVG Beschlagnahme § 149 ZVG Wirkung Umfang. Prü..._

# Bestellung und Beschlagnahme

## Arbeitsbereich

Prüft Bestellungsbeschluss und Beschlagnahme am Anfang einer Zwangsverwaltung nach §§ 146-149 ZVG. Anwendungsfall Anordnungsbeschluss des Vollstreckungsgerichts liegt vor und Bestellung muss rechtlich geprüft werden. Normen § 146 ZVG Anordnung § 148 ZVG Beschlagnahme § 149 ZVG Wirkung Umfang. Prüfraster Beschluss Bestallung Objekt Schuldner Gläubiger Rang Umfang Weisungen des Gerichts. Output Prüfliste Beschluss mit Vollständigkeitsvermerk und naechsten Schritten für Besitzuebernahme. Abgrenzung zu zvg-besitzuebernahme und zvg-aktenanlage-objektcockpit. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Startet bei

- Anordnungs- oder Beitrittsbeschluss eingeht
- Bestallungsurkunde ausgestellt wurde
- unklar ist, welche Rechte und Forderungen erfasst sind

## Eingaben

- Anordnungsbeschluss, Beitritte, Bestallung
- Grundbuch, Forderungsaufstellung, Gläubigerangaben
- gerichtliche Weisungen

## Workflow

1. **Beschlussdaten** - Gericht, Aktenzeichen, Objekt, Schuldner, Gläubiger und Forderung erfassen.
2. **Umfang** - Grundstück, Zubehör, Nutzungen, Forderungen und Rechte bestimmen.
3. **Rang und Beitritt** - betreibende Gläubiger und spätere Beitritte dokumentieren.
4. **Weisungen** - gerichtliche Weisungen und Zustimmungsvorbehalte vormerken.

## Ausgabe

- Beschlussprüfvermerk
- Beschlagnahmeumfang
- Rang- und Gläubigerliste

## Qualitätsgates

- Objektbezeichnung stimmt mit Grundbuch
- Bestellung nicht überdehnt
- Beitritte separat geführt

## Rote Schwellen

- falsches Objekt
- unklare Ranglage
- fehlende Bestallung

## Interne Vorlagen

- assets/templates/bestellungs-und-beschlagnahmecheck.md
- assets/templates/zvg-objektkarte.md

## Amtliche Erstquellen

- § 150 ZVG
- § 2 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Bestellung/Beschlagnahme

§ 146 ZVG (Anordnung Zwangsverwaltung) → § 147 ZVG (Beschlagnahme) → § 148 ZVG (Wirkung Beschlagnahme) → § 150 ZVG (Besitzeinweisung) → § 20 ZVG (Wirkung auf Verfügungen) → § 23 ZVG (Beschlagnahme Früchte) → § 57 ZVG (Mieterschutz bei Beschlagnahme)

## Triage Bestellung/Beschlagnahme

1. Datum des Zustellungsbeschlusses und Datum der Zustellung an Schuldner? (Beschlagnahme ab Zustellung)
2. Wurden Mieter über die Beschlagnahme informiert? (Zahlungspflicht Miete an Zwangsverwalter)
3. Hat Schuldner vor Beschlagnahme Mieten im Voraus vereinnahmt? (§ 153 ZVG Rückforderung prüfen)
4. Liegt eine eingetragene Grundschuld oder Hypothek vor? (Gläubiger-Rang für Ausschüttungen)

## Output-Template Mieter-Benachrichtigung nach Beschlagnahme

**Adressat:** Mieter — Tonfall sachlich-erklärend

```
[ZWANGSVERWALTER, ADRESSE]

An [MIETER NAME]
[ADRESSE MIETWOHNUNG]

[ORT], [DATUM]

Betreff: Zwangsverwaltung — Zahlungsanweisung für Miete

Sehr geehrte/r Herr/Frau [NAME],

über das Grundstück [ADRESSE, GRUNDBUCHBEZEICHNUNG] wurde durch Beschluss
des Amtsgerichts [ORT] vom [DATUM] (AZ [X]) die Zwangsverwaltung angeordnet.
Ich wurde zum Zwangsverwalter bestellt.

Ab sofort ist die monatliche Miete von [BETRAG] EUR ausschließlich auf
folgendes Treuhandkonto zu zahlen:
IBAN: [X], BIC: [Y], Bank: [Z], Verwendungszweck: [AZ + IHRE EINHEIT]

Zahlungen an den Eigentümer haben nach Beschlagnahme keine schuldbefreiende
Wirkung mehr (§ 148 ZVG).

Mit freundlichen Grüßen
[ZWANGSVERWALTER]
```

---

## Skill: `betriebskosten-hausgeld-bieterangebot`

_Betriebskosten Hausgeld und laufende Objektkosten in der Zwangsverwaltung. Anwendungsfall Zwangsverwalter muss Nebenkosten prüfen WEG-Hausgeld bezahlen und Betriebskostenabrechnung erstellen. Normen § 155 ZVG Ausgaben § 16 WEG Hausgeld BetrKV Betriebskostenarten. Prüfraster Nebenkosten Dienstleis..._

# Betriebskosten, Hausgeld und laufende Objektkosten

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Startet bei

- WEG-Hausgeld, Betriebskosten oder Versorgerrechnungen eingehen
- Abrechnungen erstellt oder geprüft werden müssen
- Liquiditätsengpass bei laufender Verwaltung entsteht

## Eingaben

- Hausgeldabrechnung, Wirtschaftsplan, Versorgerverträge
- Betriebskostenbelege, Dienstleisterrechnungen
- Mieter-Vorauszahlungen und Leerstände

## Workflow

1. **Kosten erfassen** - laufende Kosten, öffentliche Lasten, Hausgeld, Dienstleister und Versorger trennen.
2. **Umlage prüfen** - umlagefähige und nicht umlagefähige Positionen markieren.
3. **Liquidität** - Fälligkeiten mit Mieten und Vorschussbedarf abgleichen.
4. **Abrechnung** - Betriebskosten- oder WEG-Schnittstellen für Bericht vorbereiten.

## Ausgabe

- Kostenmatrix
- Zahlungsplan
- Abrechnungsvorbereitung

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Qualitätsgates

- öffentliche Lasten separat
- Umlagefähigkeit geprüft
- Fälligkeit belegt

## Rote Schwellen

- Versorgungssperre
- Hausgeldrückstand mit Verwalterdruck
- unwirtschaftlicher Dienstleister

## Interne Vorlagen

- assets/templates/betriebskosten-hausgeld.md
- assets/templates/konto-kassenbuch.md

## Amtliche Erstquellen

- §§ 9, 13, 15 ZwVwV
- § 155 ZVG

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Betriebskosten/Hausgeld

§ 153 ZVG (laufende Ausgaben) → § 155 ZVG (Verteilungsplan) → § 10 Abs. 1 Nr. 2 ZVG (Rangklasse Hausgeld) → §§ 8-10 ZwVwV (Ausgaben Verwaltung) → § 16 Abs. 2 WEG (Kostentragung Wohnungseigentuemer) → §§ 556-556d BGB (Betriebskosten Mietverhältnis)

## Triage Betriebskosten/Hausgeld

1. Handelt es sich um eine WEG-Einheit? (Hausgeld-Rückstände haben Vorrang in § 10 ZVG)
2. Sind laufende Betriebskostenvorauszahlungen in den Mietverträgen ausgewiesen?
3. Welche Betriebskosten zahlt der Zwangsverwalter direkt? (Versicherung Grundsteuer Energie)
4. Liegen Hausgeld-Rückstände aus der Zeit vor Beschlagnahme vor?

## Schritt-für-Schritt-Betriebskostenabrechnung ZVG

1. Alle Kostenpositionen mit Belegen erfassen (Heizung Wasser Müll Hausmeister)
2. Umlageschlüssel aus Mietverträgen und WEG-Beschlüssen prüfen
3. Abrechnungszeitraum festlegen (Kalenderjahr oder Verwaltungszeitraum)
4. Soll-Vorauszahlungen der Mieter gegen tatsächliche Kosten abgleichen
5. Nachzahlungen oder Guthaben berechnen und Mieter informieren
6. Überschüsse in Verteilungsplan nach § 155 ZVG einbeziehen

---

## Skill: `bieterangebot-bewertung`

_Bewertet Zwangsversteigerungsobjekte aus Investorensicht für Bieterentscheidung. Anwendungsfall Investor erwaeegt Kauf in Zwangsversteigerung und benoetigt strukturierte Wertbewertung. Normen § 74a ZVG geringstes Gebot § 81 ZVG Sicherheitsleistung §§ 44 ff. ZVG bestehenbleibende Rechte. Prüfraste..._

# Bieterangebot Bewerten

## Arbeitsbereich

Bewertet Zwangsversteigerungsobjekte aus Investorensicht für Bieterentscheidung. Anwendungsfall Investor erwaeegt Kauf in Zwangsversteigerung und benoetigt strukturierte Wertbewertung. Normen § 74a ZVG geringstes Gebot § 81 ZVG Sicherheitsleistung §§ 44 ff. ZVG bestehenbleibende Rechte. Prüfraster Verkehrswert geringstes Gebot Sicherheitsleistung bestehenbleibende Rechte Mietlage Sanierungsrisiko Bietlimit. Output Investoren-Bewertungsreport mit empfohlenem Bietlimit Risikoeinschaetzung und Finanzierungsgrundlage. Abgrenzung zu zvg-versteigerungsteilnahme und zvg-verkauf-versteigerung-schnittstelle. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Startet bei

- "Ist dieses Versteigerungsangebot attraktiv?"
- "Welches Bietlimit ist plausibel?"
- "Was bedeutet Mindestgebot?"
- "Wie bewerte ich Gutachten, Grundbuch und Mietvertrag?"

## Workflow

1. **Unterlagen inventarisieren**: Bekanntmachung, Gutachten, Grundbuch, Teilungserklärung, Mietvertrag, Hausgeld, Protokolle, Baulasten, Energie, Versicherungen.
2. **Rechtsbegriffe sauberziehen**: Umgangssprachlich "Mindestgebot" meist vom rechtlichen "geringsten Gebot" unterscheiden.
3. **Wertbasis prüfen**: Verkehrswert, Stichtag, Innen-/Außenbesichtigung, Bewertungsverfahren, Abschläge, Vergleichsdaten, Marktrisiko.
4. **Lasten prüfen**: Abteilung II, Abteilung III soweit bekannt, bestehenbleibende Rechte, Rückstände, öffentliche Lasten, WEG-Hausgeld, Sonderumlagen.
5. **Nutzung prüfen**: Mietvertrag, tatsächliche Nutzung, Klingel-/Briefkasten-Abweichungen, Renovierungsabreden, Kündigungs-/Räumungsrisiko.
6. **Bietlimit rechnen**: Maximalbudget minus Sicherheitsabschlag, Erwerbsnebenkosten, Sanierung, Leerstand, Prozesskosten, Finanzierungspuffer und bestehenbleibende Rechte.
7. **Ampel ausgeben**: GRÜN nur bei belegtem Wert, klaren Lasten und ausreichendem Puffer; sonst GELB/ROT mit Nachforderungen.

## Ausgabe

- Bieterangebots-Matrix
- Bietlimit mit Annahmen
- offene Fragen an Gericht, Verwalter, WEG-Verwaltung, Bank oder Sachverständigen
- Entscheidung: beobachten, nachrecherchieren, bieten, nicht bieten

## Qualitätsgates

- Keine Gewährleistungsannahmen: ZVG-Erwerb ist kein normaler Kaufvertrag.
- Geringstes Gebot und 5/10-/7/10-Grenzen werden getrennt erläutert.
- Sicherheitsleistung wird auf Basis des Verkehrswerts geprüft.
- Bietlimit enthält Finanzierung und Liquidität, nicht nur Kaufpreis.

## Rote Schwellen

- Nur Außenbesichtigung und zugleich hoher Sanierungshebel
- unklare tatsächliche Nutzung oder gewerbliche Hinweise in Wohnraum
- bestehenbleibende Rechte nicht verstanden
- Angebot drängt zu schneller Zahlung außerhalb klarer Gerichts-/Notarstruktur

## Interne Vorlage

- `assets/templates/bieterangebot-bewertung.md`

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Bieterangebot/Versteigerungsschnittstelle

§ 152 ZVG (Verwalterpflichten) → § 56 ZVG (Übergabe an Ersteher) → § 57 ZVG (Mieterschutz bei Eigentumsübergang) → § 57a ZVG (Sonderkündigungsrecht Ersteher) → §§ 566-566e BGB (Kauf bricht nicht Miete) → § 155 ZVG (Verteilungsplan bis Versteigerung)

## Triage Bieterangebot/Versteigerung

1. Ist ein Versteigerungstermin angesetzt? (Auftrag des Gerichts, Mieterliste und Zustands-Bericht vorzubereiten)
2. Sind alle Mietverhältnisse vollständig dokumentiert? (Laufzeit Miete Rückstände)
3. Gibt es Anhaltspunkte für Mietrechte die dem Bieter nicht bekannt sein könnten?
4. Plant der Ersteher eine Eigennutzung? (Sonderkündigungsrecht § 57a ZVG prüfen)

## Output-Template Versteigerungsinfo-Bericht (Auszug)

```
Information für Bieter im Versteigerungsverfahren
AZ: [X]
Objekt: [ADRESSE]
Stand: [DATUM]

Vermietungsstand:
Nr. | Mieter | Einheit | Nettomiete | NK-VZ | Vertragsende | Rückstände
1 | [...] | [...] | [...] | [...] | [unbefristet] | [BETRAG]

Sonderrechte: [Vorkaufsrechte Vormerkungen etc.]
Technischer Zustand: [ZUSAMMENFASSUNG]
Zu beachten für Ersteher: Mietverhältnisse gehen gem. §§ 566 BGB über;
Sonderkündigungsrecht § 57a ZVG nur innerhalb von 2 Wochen nach Zuschlag.
```

---

## Skill: `glaeubiger-schuldner-kommunikation`

_Schriftwechsel in der Zwangsverwaltung mit Schuldner Gläubiger Mieter Gericht Versicherern und Dienstleistern. Anwendungsfall Zwangsverwalter muss formgerechte Schreiben an alle Beteiligten erstellen. Normen §§ 150 151 ZVG § 154 ZVG Pflichten § 543 BGB Kündigung § 535 BGB Mietrecht. Prüfraster Ad..._

# Gläubiger-, Schuldner- und Drittschuldnerkommunikation

## Arbeitsbereich

Schriftwechsel in der Zwangsverwaltung mit Schuldner Gläubiger Mieter Gericht Versicherern und Dienstleistern. Anwendungsfall Zwangsverwalter muss formgerechte Schreiben an alle Beteiligten erstellen. Normen §§ 150 151 ZVG § 154 ZVG Pflichten § 543 BGB Kündigung § 535 BGB Mietrecht. Prüfraster Adressat Anlass Normbezug Ton Fristen Dokumentation. Output Schreibenpaket mit Vorlagen für alle typischen Kommunikationsanlaesse in der Zwangsverwaltung. Abgrenzung zu zvg-berichtswesen-gericht (nur Gericht) und zvg-miet-und-pachtverwaltung. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Startet bei

- Mieter, Schuldner, Gläubiger oder Behörden informiert werden müssen
- Konflikte über Zutritt, Mieten oder Maßnahmen entstehen
- Gerichtskommunikation vorbereitet wird

## Eingaben

- Rolle und Adressat
- Beschluss, Objekt, Anlass, gewünschte Reaktion
- Frist, Belege und Tonalität

## Workflow

1. **Adressat klären** - Rolle, Rechte, Pflichten und Zustellweg bestimmen.
2. **Kernbotschaft** - Was ist passiert, was wird verlangt, bis wann, mit welcher Folge.
3. **Belege** - Beschluss, Bestallung, Konto, Fotos oder Tabellen beifügen.
4. **Nachhalten** - Wiedervorlage, Antwortauswertung und Eskalation setzen.

## Ausgabe

- Schreibenentwurf
- Anlagenliste
- Wiedervorlage

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Qualitätsgates

- keine Drohung ohne Grundlage
- Zahlstelle eindeutig
- Adressat nicht verwechselt

## Rote Schwellen

- Schuldner blockiert Objektzugang
- Mieter zahlen falsch
- Gläubiger drängt auf unzulässige Sonderzahlung

## Interne Vorlagen

- assets/templates/schuldner-glaeubiger-kommunikation.md
- assets/templates/mieterliste-rent-roll.md

## Amtliche Erstquellen

- § 4 ZwVwV
- § 16 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Gläubiger-Schuldner-Kommunikation

§ 154 ZVG (Aufsicht durch Gericht) → § 153 Abs. 2 ZVG (Auskunftspflicht) → §§ 13-15 ZwVwV (Buchführung Rechnungslegung) → § 20 ZwVwV (Vergütung und Rechenschaft) → § 242 BGB (Treu und Glauben, Auskunftsanspruch analog)

## Triage Kommunikation

1. Wer ist betreibender Gläubiger? (Alle Gläubiger in Rangklassen nach § 10 ZVG erfassen)
2. Liegt eine Bevollmächtigung des Gläubigers vor? (Ansprechpartner/Kanzlei)
3. Kommuniziert der Schuldner kooperativ? (Verweigerung → Gerichtsantrag)
4. Haben weitere Gläubiger beigetreten?

## Output-Template Gläubigerinfo-Schreiben (Auszug)

**Adressat:** Betreibender Gläubiger — Tonfall formell-berichtend

```
An [GLÄUBIGER / BEVOLLMÄCHTIGTE KANZLEI]
[ADRESSE]

Zwangsverwaltung [ADRESSE], AZ [X]
Quartalsbericht [QUARTAL/JAHR]

Sehr geehrte Damen und Herren,

zum Stand der Zwangsverwaltung berichte ich:

Einnahmen [QUARTAL]: [BETRAG]
Ausgaben [QUARTAL]: [BETRAG]
Kontostand per [DATUM]: [BETRAG]
Ausschüttungsfähiger Betrag nach Rücklage: [BETRAG]

Besondere Vorkommnisse: [LEERSTAND REPARATUR RECHTSTREIT]

Nächster Auszahlungsantrag: [DATUM]

[UNTERSCHRIFT ZWANGSVERWALTER]
```

---

## Skill: `instandhaltung-sicherung`

_Instandhaltung Sicherung und Gefahrenabwehr am Zwangsverwaltungsobjekt. Anwendungsfall Objekt weist Sicherheitsmaengel auf oder Notmassnahmen sind erforderlich. Normen § 154 ZVG Pflicht zur Erhaltung § 823 BGB Verkehrssicherungspflicht BauO-Länder. Prüfraster Verkehrssicherungspflicht Notmassnahm..._

# Instandhaltung, Sicherung und Gefahrenabwehr

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Startet bei

- Schäden, Mängel oder Gefahren gemeldet werden
- Reparaturen oder Notmaßnahmen nötig sind
- Budget oder gerichtliche Zustimmung unklar ist

## Eingaben

- Mängelmeldung, Fotos, Kostenvoranschläge
- Versicherung, Mietereinwendungen, Behördenpost
- Kontostand und Vorschusslage

## Workflow

1. **Gefahr einstufen** - akute Gefahr, Substanzerhalt, Komfort oder Modernisierung trennen.
2. **Budget und Zustimmung** - Kosten, Liquidität, Vorschuss und Zustimmungsvorbehalte prüfen.
3. **Beauftragung** - Dienstleister, Leistungsumfang, Dokumentation und Abnahme vorbereiten.
4. **Bericht** - Gericht und Beteiligte über wesentliche Maßnahmen informieren.

## Ausgabe

- Gefahren- und Maßnahmenvermerk
- Beauftragungsentwurf
- Berichtsbaustein

## Qualitätsgates

- Notmaßnahme begründet
- Kosten plausibilisiert
- Fotos und Belege gesichert

## Rote Schwellen

- Verkehrssicherungsrisiko
- Brandschutzmangel
- fehlende Versicherung

## Interne Vorlagen

- assets/templates/instandhaltung-gefahrensicherung.md
- assets/templates/versicherung-und-lasten.md

## Amtliche Erstquellen

- § 1 ZwVwV
- § 9 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Instandhaltung/Sicherung

§ 152 ZVG (Pflicht ordnungsgemäße Verwaltung) → §§ 8-9 ZwVwV (Instandhaltungsmaßnahmen) → § 154 ZVG (Genehmigung größerer Maßnahmen) → § 823 Abs. 1 BGB (Verkehrssicherungspflicht) → § 836 BGB (Haftung Grundstücksbesitzer) → § 278 BGB (Erfüllungsgehilfe)

## Triage Instandhaltung/Sicherung

1. Liegen akute Gefahrenstellen vor? (Sofortmaßnahme ohne Genehmigung möglich)
2. Sind größere Maßnahmen geplant? (Gerichtsgenehmigung erforderlich ab ca. 2.000 EUR netto)
3. Ist die Gebäudeversicherung aktiv und ausreichend?
4. Wer führt die Instandhaltungsarbeiten durch? (Auftragnehmer-Vertrag mit Vergabe-Dokumentation)

## Output-Template Gerichtsantrag Instandhaltung

**Adressat:** Amtsgericht — Tonfall formell-antragend

```
An das Amtsgericht [ORT]
Vollstreckungsgericht
AZ: [X]

Antrag auf Genehmigung einer Instandhaltungsmaßnahme

Sehr geehrte Damen und Herren,

in der Zwangsverwaltung [ADRESSE] beantrage ich die Genehmigung folgender Maßnahme:

Maßnahme: [BESCHREIBUNG]
Grund: [SCHADENSURSACHE, DRINGLICHKEIT]
Kosten: [ANGEBOTE ANLIEGEND — ANLAGE 1-3]
Empfohlenes Angebot: [BIETER, BETRAG]

Die Maßnahme ist zur Abwehr weiterer Schäden und zur Erfüllung der
Verkehrssicherungspflicht unaufschiebbar.

[DATUM, UNTERSCHRIFT]
```

---

## Skill: `kommandocenter`

_Kommandocenter für Zwangsverwaltung — Triage und Routing zu allen ZVG-Skills. Anwendungsfall Zwangsverwalter oeffnet Plugin und will schnell den richtigen starten. Normen §§ 146-161 ZVG Kernvorschriften. Prüfraster Bestellung Beschlagnahme Besitz Mietverwaltung Konto Bericht Rechnungslegung Verte..._

# Zwangsverwaltungs-Kommandocenter

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Startet bei

- ein Zwangsverwaltungsbeschluss eingeht
- Objekt, Mieter, Schuldner oder Gläubiger geordnet werden müssen
- unklar ist, welche Sofortmaßnahmen anstehen

## Eingaben

- Anordnungs- und Bestellungsbeschluss
- Grundstücksdaten, Gläubiger, Schuldner, Mieter
- Mietlisten, Lasten, Versicherungen, Kontoangaben

## Workflow

1. **Beschluss lesen** - Objekt, Schuldner, Gläubiger, Rang und Umfang der Beschlagnahme erfassen.
2. **Sofortplan** - Besitz, Mieterinformation, Konto, Versicherung und Lasten priorisieren.
3. **Objektcockpit** - Rent Roll, Rückstände, Ausgaben, Risiken und Gerichtswiedervorlagen anlegen.
4. **Nächste Aktion** - konkrete Schreiben, Vor-Ort-Termin oder Gerichtsanzeige ausgeben.

## Ausgabe

- Objektkarte
- Sofortmaßnahmenliste
- Kommunikationspaket

## Qualitätsgates

- Bestellung und Objekt exakt erfasst
- keine Zahlung auf Privatkonto
- Mieter und Pächter werden korrekt informiert

## Rote Schwellen

- fehlende Versicherung
- akute Gefahr am Objekt
- Mietzahlungen an Schuldner nach Beschlagnahme

## Interne Vorlagen

- assets/templates/zvg-objektkarte.md
- assets/templates/quality-gate.md

## Amtliche Erstquellen

- §§ 150, 152 ZVG
- §§ 1, 3 ZwVwV

## Ergänzende Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Kommandocenter

§ 154 ZVG (Gerichtliche Aufsicht) → § 20 ZwVwV (Vergütung und Rechenschaft) → §§ 13-15 ZwVwV (Buchführung und Berichte) → § 159 ZVG (Aufhebung Zwangsverwaltung)

## Checkliste Kommandocenter (Monatlich)

| Aufgabe | Fälligkeit | Erledigt |
|---|---|---|
| Sollmieten-Abgleich | Monatsanfang | [ ] |
| Rückstands-Update | Monatsmitte | [ ] |
| Ausgabenbelege gesammelt | Monatsende | [ ] |
| Kontoauszüge abgeglichen | Monatsende | [ ] |
| Gerichtsbericht erstellt (falls fällig) | Gem. Anordnung | [ ] |
| Versicherungsprämien gezahlt | Fälligkeitsdatum | [ ] |
| Grundsteuer-Vorauszahlung | 15.02./15.05./15.08./15.11. | [ ] |
| Hausgeldabrechnung WEG (falls EWZ) | Gem. WEG-Plan | [ ] |

---

## Skill: `konten-kassenfuehrung-miet-pachtverwaltung`

_Kontenführung und Buchführung des Treuhandkontos in der Zwangsverwaltung. Anwendungsfall Zwangsverwalter muss Einnahmen Ausgaben und Saldo des Treuhandkontos nachweisen. Normen § 155 ZVG Einnahmen Ausgaben § 154 ZVG Pflichten Treuhand. Prüfraster Treuhandkonto Soll Ist Einnahmen Ausgaben Belege V..._

# Konten, Kasse und Buchführung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Startet bei

- Treuhandkonto einzurichten ist
- Zahlungen eingehen oder Ausgaben freigegeben werden
- Jahres- oder Schlussrechnung vorbereitet wird

## Eingaben

- Kontoauszüge, Belege, Rent Roll, Ausgaben
- Vorschussanforderungen, Gerichtskosten, Vergütung
- Vorjahressaldo und offene Posten

## Workflow

1. **Konto einrichten** - gesondertes Treuhandkonto und Zahlungsregeln dokumentieren.
2. **Buchen** - Soll- und Isteinnahmen, Ausgaben, Belege und Salden erfassen.
3. **Abgleichen** - Rent Roll, Konto, Belege und Vorschuss laufend abstimmen.
4. **Auskunft** - gerichtsfeste Auskunft und Unterlagenpaket vorbereiten.

## Ausgabe

- Konto- und Kassenbuch
- Soll-Ist-Abgleich
- Belegliste

## Qualitätsgates

- Masse getrennt von Eigenbeständen
- Einzelbuchungen ausgewiesen
- Belege zu jeder Buchung

## Rote Schwellen

- privates Konto
- nicht zuordenbare Bareinnahme
- fehlende Kontoauszüge

## Interne Vorlagen

- assets/templates/konto-kassenbuch.md
- assets/templates/rechnungslegung.md

## Amtliche Erstquellen

- § 13 ZwVwV
- § 14 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Konten/Kassenführung

§ 153 ZVG (Einnahmen aus Nutzungen) → § 152 ZVG (Pflichten Verwaltung) → § 13 ZwVwV (Buchführung) → § 14 ZwVwV (Jahresrechnung) → § 675 BGB (Geschäftsbesorgungsvertrag) → § 667 BGB (Herausgabe Treuhandgelder) → § 280 BGB (Schadensersatz Treuhandvermischung)

## Triage Konten/Kassenführung

1. Ist das Treuhandkonto eindeutig als solches bei der Bank benannt?
2. Ist die Buchführung tagesaktuell oder bestehen Rückstände?
3. Werden Einnahmen und Ausgaben kontengetrennt nach Einnahmenarten geführt?
4. Ist ein Kassenbuch oder Buchhaltungsprogramm im Einsatz?

## Output-Template Kassenbuch-Schema (Auszug)

```
Buchungsjournal Zwangsverwaltung [ADRESSE]
AZ: [X] — Treuhandkonto: [IBAN]

Datum | Buchungstext | Einnahme | Ausgabe | Saldo | Beleg-Nr.
[D] | Miete Jan [MIETER] Einheit 1 | [BETRAG] | — | [X] | K01
[D] | Versicherungsprämie [ANBIETER] | — | [BETRAG] | [X] | A01
[D] | Grundsteuer Vorauszahlung | — | [BETRAG] | [X] | A02

Saldo per [DATUM]: [BETRAG] EUR
Rücklage laufende Kosten: [BETRAG] EUR
Ausschüttungsfähiger Betrag: [BETRAG] EUR
```

---

## Skill: `miet-und-pachtverwaltung`

_Miet- und Pachtverwaltung in der Zwangsverwaltung einschließlich Vertragsuebernahme und Zahlungseinzug. Anwendungsfall Zwangsverwalter uebernimmt bestehende Mietverhältnisse und muss diese weiter verwalten. Normen § 152 ZVG Mieteinzug §§ 535 ff. BGB Mietrecht § 150 ZVG Vorausverfuegungen des Schu..._

# Miet- und Pachtverwaltung

## Arbeitsbereich

Miet- und Pachtverwaltung in der Zwangsverwaltung einschließlich Vertragsuebernahme und Zahlungseinzug. Anwendungsfall Zwangsverwalter uebernimmt bestehende Mietverhältnisse und muss diese weiter verwalten. Normen § 152 ZVG Mieteinzug §§ 535 ff. BGB Mietrecht § 150 ZVG Vorausverfuegungen des Schuldners. Prüfraster Mietvertraege Pachtvertraege Zahlstellen Vorausverfuegungen Kautionen Nebenkosten Nutzungsregelungen. Output Mieterliste mit Vertragsuebersicht Kautionsnachweis und Zahlungsplan für Verteilungsrechnung. Abgrenzung zu zvg-mieteinzug-rückstaende und zvg-räumung-kündigung. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Startet bei

- Mieter oder Pächter vorhanden sind
- Mietzahlungen umzuleiten sind
- Verträge, Kautionen oder Vorausverfügungen unklar sind

## Eingaben

- Miet- und Pachtverträge
- Mieterliste, Zahlungsverlauf, Kautionen
- Schreiben des Schuldners oder der Mieter

## Workflow

1. **Verträge erfassen** - Einheit, Nutzer, Miete, Nebenkosten, Laufzeit, Kaution und Sonderrechte aufnehmen.
2. **Mitteilung** - Mieter/Pächter über Zwangsverwaltung und neue Zahlstelle informieren.
3. **Vorausverfügungen** - Abtretung, Vorauszahlung, Kaution und Rückstände prüfen.
4. **Laufend verwalten** - Anpassungen, Nebenkosten, Mängel, Kündigungen und Kommunikation steuern.

## Ausgabe

- Rent Roll
- Mieterschreiben
- Vertragsrisikomatrix

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Qualitätsgates

- Soll- und Istmiete getrennt
- Kautionen nicht als freie Masse behandelt
- Vorausverfügungen geprüft

## Rote Schwellen

- Zahlung an Schuldner
- fehlender Mietvertrag
- streitiger Besitz

## Interne Vorlagen

- assets/templates/mieterliste-rent-roll.md
- assets/templates/schuldner-glaeubiger-kommunikation.md

## Amtliche Erstquellen

- §§ 4, 5, 6 ZwVwV
- § 152 ZVG

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Miet-/Pachtverwaltung ZVG

§ 152 ZVG (Rechte/Pflichten Verwalter) → § 153 ZVG (Einziehung Nutzungen) → § 57 ZVG (Schutz der Mieter) → §§ 535 566 BGB (Mietrecht) → §§ 8-9 ZwVwV (laufende Verwaltung) → § 581 BGB (Pachtvertrag) → §§ 596-599 BGB (Pächterschutz)

## Triage Miet-/Pachtverwaltung

1. Liegen schriftliche Mietverträge vor? (Alle Einheiten vollständig erfasst)
2. Sind Kautionen hinterlegt? (Pflicht: auf separatem Kautionskonto)
3. Bestehen Sondermietrechte (Wohnrecht Nießbrauch)? (Im Grundbuch Abt. II prüfen)
4. Sind Pachtverhältnisse vorhanden? (Sonderregeln §§ 581 ff. BGB)

## Output-Template Verwaltungsübernahme-Schreiben Miet-/Pachtverhältnis

```
[ZWANGSVERWALTER]

An [MIETER/PÄCHTER]
[ADRESSE]

Mitteilung: Übernahme der Verwaltung

Sehr geehrte/r Herr/Frau [NAME],

ich habe die Zwangsverwaltung über das Grundstück [ADRESSE] übernommen.
Ich trete damit in Ihre/Ihre bestehenden Miet-/Pachtverhältnisse ein
und führe die Verwaltung ab [DATUM] fort.

Die Miete/Pacht ist ab sofort an folgendes Konto zu zahlen:
[IBAN, BIC, BANK, VERWENDUNGSZWECK]

Ihre vertraglichen Rechte bleiben unberührt. Mängelanzeigen richten Sie bitte an:
[KONTAKTDATEN ZWANGSVERWALTER]

[UNTERSCHRIFT]
```

---

## Skill: `mieteinzug-rueckstaende`

_Mieteinzug und Rückstandsbehandlung in der Zwangsverwaltung. Anwendungsfall Mieter zahlt nicht und Zwangsverwalter muss Rückstande einziehen oder Klage einleiten. Normen § 152 ZVG Mieteinzugspflicht § 543 BGB fristlose Kündigung § 286 BGB Verzug. Prüfraster Soll-Ist-Abgleich Mahnung Ratenvereinba..._

# Mieteinzug und Rückstände

## Arbeitsbereich

Mieteinzug und Rückstandsbehandlung in der Zwangsverwaltung. Anwendungsfall Mieter zahlt nicht und Zwangsverwalter muss Rückstande einziehen oder Klage einleiten. Normen § 152 ZVG Mieteinzugspflicht § 543 BGB fristlose Kündigung § 286 BGB Verzug. Prüfraster Soll-Ist-Abgleich Mahnung Ratenvereinbarung Klage Zahlungseingang Kontoabgleich Dokumentation. Output Rückstandsprotokoll mit Mahnhistorie Klageprüfung und Einzugsnachweis für Rechnungslegung. Abgrenzung zu zvg-miet-und-pachtverwaltung und zvg-räumung-kündigung. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Startet bei

- Mieteinnahmen fehlen
- Rückstände vor oder nach Beschlagnahme bestehen
- Zahlungen nicht zugeordnet werden können

## Eingaben

- Rent Roll, Kontoauszüge, Mieterkonten
- Rückstandsliste, Mahnungen, Einwendungen
- Mietverträge und Betriebskostenstände

## Workflow

1. **Soll-Ist-Abgleich** - Sollmieten je Einheit mit Zahlungseingängen und Altrückständen matchen.
2. **Rückstände trennen** - beschlagnahmte Nutzungen, Altansprüche und streitige Posten unterscheiden.
3. **Mahnen** - freundliche Zahlungserinnerung, Mahnung, Ratenplan oder Klagevorschlag erstellen.
4. **Gericht berichten** - wesentliche Rückstände und Einziehungsmaßnahmen dokumentieren.

## Ausgabe

- Rückstandsliste
- Mahn- und Klagepaket
- Zahlungsabgleich

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Qualitätsgates

- jede Zahlung einer Einheit zugeordnet
- Alt- und Neurückstände getrennt
- Einwendungen protokolliert

## Rote Schwellen

- Dauerleerstand
- Mietminderung ohne Prüfung
- Kontoauszug fehlt

## Interne Vorlagen

- assets/templates/mieteinzug-rueckstaende.md
- assets/templates/konto-kassenbuch.md

## Amtliche Erstquellen

- § 8 ZwVwV
- § 13 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Mieteinzug/Rückstände

§ 153 ZVG (Einziehung Nutzungen) → § 535 Abs. 2 BGB (Mietzinszahlungspflicht) → § 543 Abs. 2 Nr. 3 BGB (Kündigung wegen Zahlungsverzug) → § 286 BGB (Verzug) → § 288 BGB (Verzugszinsen) → §§ 12-13 ZwVwV (Buchführung Rückstände)

## Triage Mieteinzug/Rückstände

1. Rückstand vor oder nach Beschlagnahme entstanden? (Unterschiedliche Behandlung)
2. Hat der Mieter Einwendungen gegen die Miethöhe erhoben? (Minderung § 536 BGB prüfen)
3. Liegen mehr als zwei Monatsmieten Rückstand vor? (Außerordentliche Kündigung § 543 BGB prüfen)
4. Ist Klage wirtschaftlich sinnvoll? (Insolvenzrisiko des Mieters, Vollstreckbarkeit prüfen)

## Output-Template Mahn-/Kündigungsschreiben ZVG

**Adressat:** rückständiger Mieter — Tonfall scharf-fristsetzend

```
[ZWANGSVERWALTER]
EINSCHREIBEN MIT RÜCKSCHEIN

An [MIETER NAME]
[ADRESSE]

Zwangsverwaltung [ADRESSE], AZ [X]

Mahnung und Fristsetzung / Außerordentliche Kündigung

Sehr geehrte/r Herr/Frau [NAME],

folgende Mietrückstände sind aufgelaufen:
Monat | Betrag | Status
[TABELLE]
Gesamtrückstand: [BETRAG] EUR

Ich fordere Sie auf, den Rückstand bis zum [DATUM] zu zahlen.
[Falls Kündigung: Gleichzeitig kündige ich das Mietverhältnis fristlos nach
§ 543 Abs. 2 Nr. 3 BGB wegen Zahlungsverzugs von mehr als zwei Monatsmieten.
Bitte übergeben Sie die Wohnung spätestens zum [DATUM] geräumt.]

[UNTERSCHRIFT ZWANGSVERWALTER]
```

---

## Skill: `oeffentliche-lasten`

_Öffentliche Lasten und grundstuecksbezogene Abgaben in der Zwangsverwaltung. Anwendungsfall Grundsteuer Erschließungsgebuhren oder Beitraege werden fällig und Zwangsverwalter muss prüfen ob und in welchem Rang zu zahlen ist. Normen § 10 ZVG Rangklassen § 12 GrStG Grundsteuerschuldner § 155 ZVG Au..._

# Öffentliche Lasten und grundstücksbezogene Abgaben

## Arbeitsbereich

Öffentliche Lasten und grundstuecksbezogene Abgaben in der Zwangsverwaltung. Anwendungsfall Grundsteuer Erschließungsgebuhren oder Beitraege werden fällig und Zwangsverwalter muss prüfen ob und in welchem Rang zu zahlen ist. Normen § 10 ZVG Rangklassen § 12 GrStG Grundsteuerschuldner § 155 ZVG Ausgaben. Prüfraster Grundsteuer Abgaben Rang Fälligkeiten Zahlung Nachweis Belegpflicht. Output Lasten-Übersicht mit Rangfolge Zahlungsplan und Nachweis für Gerichtsbericht. Abgrenzung zu zvg-konten-kassenführung und zvg-rechnungslegung. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Startet bei

- Grundsteuer, Gebühren oder Beitragsbescheide eingehen
- Lasten im Besitzerlangungsbericht fehlen
- Verteilung oder Rechnungslegung vorbereitet wird

## Eingaben

- Bescheide, Lastenregister, Kontoauszüge
- Objektdaten, Grundsteuer, Gebühren, WEG-Unterlagen
- Fälligkeiten und Zahlungsnachweise

## Workflow

1. **Lasten erfassen** - Art, Zeitraum, Betrag, Fälligkeit und Behörde aufnehmen.
2. **Rang und Zweck** - öffentliche Last, Betriebskosten, Verwaltungsausgabe oder Schuldneraltlast trennen.
3. **Zahlungsplan** - Liquidität, Vorschussbedarf und Verteilungsauswirkung prüfen.
4. **Nachhalten** - Bescheide, Widerspruchsfristen und Belege ablegen.

## Ausgabe

- Lastenregister
- Zahlungsplan
- Berichtsbaustein

## Qualitätsgates

- Zeitraum sauber abgegrenzt
- Fälligkeit belegt
- Zahlung buchhalterisch zugeordnet

## Rote Schwellen

- Zwangsmaßnahmen der Kommune
- Doppelzahlung
- Beitragsbescheid mit kurzer Frist

## Interne Vorlagen

- assets/templates/versicherung-und-lasten.md
- assets/templates/konto-kassenbuch.md

## Amtliche Erstquellen

- § 3 Abs. 1 Nr. 5 ZwVwV
- § 15 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Öffentliche Lasten

§ 10 Abs. 1 Nr. 3 ZVG (Vorrang öffentlicher Lasten) → § 12 GrStG (Grundsteuerpflicht) → §§ 10-12 ZwVwV (Ausgaben und Rangfolge) → § 155 ZVG (Verteilungsplan) → § 80 AO (Steuerpflichten bei Vermögensverwaltung)

## Triage Öffentliche Lasten

1. Ist die laufende Grundsteuer erfasst und im Zahlungsplan aufgenommen?
2. Bestehen Rückstände bei öffentlichen Lasten aus der Zeit vor Beschlagnahme?
3. Liegen weitere öffentliche Lasten vor (Anliegerbeiträge Erschließungskosten)?
4. Ist eine Umsatzsteueroption für das Grundstück vorhanden? (Auswirkung auf Vorsteuer)

## Ausgaben-Checkliste Öffentliche Lasten

| Posten | Fälligkeit | Betrag | Bezahlt |
|---|---|---|---|
| Grundsteuer Q1 | 15.02. | [...] | [ ] |
| Grundsteuer Q2 | 15.05. | [...] | [ ] |
| Grundsteuer Q3 | 15.08. | [...] | [ ] |
| Grundsteuer Q4 | 15.11. | [...] | [ ] |
| Erschließungs-/Anliegerbeiträge | gem. Bescheid | [...] | [ ] |
| Müllgebühren/Straßenreinigung | gem. Bescheid | [...] | [ ] |
| Kanalgebühren/Wasserversorgung | gem. Bescheid | [...] | [ ] |

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

