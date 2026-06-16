# Megaprompt: fachanwalt-agrarrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 78 Skills des Plugins `fachanwalt-agrarrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Fachanwalt Agrarrecht: ordnet Rolle (Landwirt, Verpächter/Pächter, Behörde), markiert F…
2. **mandat-triage-agrarrecht** — Eingangs-Abfrage für agrarrechtliche Mandate — Landwirt fragt nach Pacht Hof-Erbfolge EU-Förderung Tierhaltungs-Genehmig…
3. **fachanwalt-agrarrecht-orientierung** — Anwalt will ueberblicken welche Normen und Mandate das Agrarrecht umfasst oder Fachanwaltschaft vorbereiten. Orientierun…
4. **orientierung-fachanwaltschaft-mandat** — Anwalt will überblicken welche Normen und Mandate das Agrarrecht umfasst oder Fachanwaltschaft vorbereiten: Orientierung…
5. **erstgespraech-mandatsannahme** — Strukturierter Erstgespraechsleitfaden für Agrar-, Forst- und Lebensmittelrecht: Erfassung der Konstellation, Konflikt- …
6. **erstpruefung-und-mandatsziel** — Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.
7. **fachanwalt-agrarrecht-verhandlung-landpacht-schlichtung** — Landwirt und Verpaechter streiten über Pacht oder Hof-Erbe und muessen Einigung außergerichtlich versuchen. Prüfraster P…
8. **fachanwalt-agrarrecht-hoefe-uebergabe** — Hofuebergabe nach HoefeO (Hamburg Niedersachsen NRW Schleswig-Holstein). Hofeigenschaft § 1 HoefeO Mindestwirtschaftswer…
9. **fachanwalt-agrarrecht-duenge-ordnungswidrigkeit** — Ordnungswidrigkeit nach Duengeverordnung DueV verteidigen. Bußgeldtatbestaende § 13a Abs. 2 DueG i.V.m. § 14 DueV. Aufze…
10. **fachanwalt-agrarrecht-gap-direktzahlungen-antrag** — Beratung zum Sammelantrag GAP-Direktzahlungen nach der GAP-Reform 2023. Konditionalitaet (GLOEZ-Standards) Oeko-Regelung…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Fachanwalt Agrarrecht: ordnet Rolle (Landwirt, Verpächter/Pächter, Behörde), markiert Frist (Pachtjahr Kündigungsfristen), wählt Norm (BLG, LwAnpG, GAP-Förderung) und Zuständigkeit (Landwirtschaftsbehörden Länder), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Fachanwalt Agrarrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `agrar-einfuehrung-rechtsquellen` — Agrar Einfuehrung Rechtsquellen
- `agrar-jagdpacht-streit-spezial` — Agrar Jagdpacht Streit Mandantenfragen
- `agrar-tierhaltung-spezial-tieg` — Agrar Tierhaltung Erstgespraech
- `agrar-wolfsschaden-spezial` — Agrar Wolfsschaden Cross Glozez Foerderung
- `agrarerbe-pflichtteil-paragraf-2316-bgb-hoefeordnung` — Agrarerbe Pflichtteil Paragraf 2316 BGB Hoefeordnung
- `agrarflaeche-erwerbsbeschraenkung-paragraf-9-grdstvg-hofstelle` — Agrarflaeche Erwerbsbeschraenkung Paragraf 9 Grdstvg Hofstelle
- `agrarfoerderung-fid-ablehnung-paragraf-9-invekos` — Agrarfoerderung FID Ablehnung Paragraf 9 Invekos
- `agrarinvest-bonusverwirkung-paragraf-49-vwvfg-grw` — Agrarinvest Bonusverwirkung Paragraf 49 Vwvfg GRW
- `workflow-mandantenkommunikation` — Agrarrecht Mandantenkommunikation Redteam Qualitygate Hoeferecht
- `anerbenrecht-risikoampel-und-gegenargumente` — Anerbenrecht BGB Spezial Compliance
- `cross-zahlen-schwellen-und-berechnung` — Cross Duengeverordnung Interessen Erbrecht
- `direktzahlungen-quellenkarte` — Direktzahlungen Quellenkarte
- `duengeverordnung-rote-gebiete-paragraf-13a-duev-derogation` — Duengeverordnung Rote Gebiete Paragraf 13A Duev Derogation
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Fachanwalt Agrarrecht sind BGB, §§ 581 ff. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `mandat-triage-agrarrecht`

_Eingangs-Abfrage für agrarrechtliche Mandate — Landwirt fragt nach Pacht Hof-Erbfolge EU-Förderung Tierhaltungs-Genehmigung Duenge-Bußgeld oder Direktzahlungen-Kuerzung: Eingangs-Abfrage für agrarrechtliche Mandate — Landwirt fragt nach Pacht Hof-Erbfolge E..._

# Eingangs-Abfrage für agrarrechtliche Mandate — Landwirt fragt nach Pacht Hof-Erbfolge EU-Förderung Tierhaltungs-Genehmigung Duenge-Bußgeld oder Direktzahlungen-Kuerzung


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GrdstVG Genehmigung 1 Monat (verlängerbar), GAP-Antrag bis 15.05. jährlich (Mehrfachantrag), BGB § 594a Landpacht-Kündigung 2. Werktag im 3. Pachtjahr.
- Tragende Normen verifizieren: FAO § 14b, BGB §§ 581 ff. (Landpacht), GrdstVG, Landwirtschaftsanpassungsgesetz (LwAnpG), HöfeO, EU-GAP-VO (2021/2115, 2021/2116, 2021/2117), MarktorganisationsG, BNatSchG, DüV, AwSV — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Landwirt, Bundesanstalt für Landwirtschaft und Ernährung (BLE), Landwirtschaftskammer, Genehmigungsbehörde nach GrdstVG, Landpächter/-verpächter, Amtsgericht Landwirtschaftsgericht.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Mehrfachantrag (Flächenförderung), Pachtvertrag, GrdstVG-Genehmigung, Düngeplan, Cross-Compliance-Nachweis, Hofübergabevertrag — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Eingangs-Abfrage für agrarrechtliche Mandate — Landwirt fragt nach Pacht Hof-Erbfolge EU-Förderung Tierhaltungs-Genehmigung Duenge-Bußgeld oder Direktzahlungen-Kuerzung. Klaert Sachgebiet (Landpacht HoefeO GAP ELER Tierhaltung Pflanzenschutz Duenge-VO Hofnachfolge) und Mandantenrolle (Landwirt Verpaechter Paechter Erbe Genossenschaft). Sofort-Fristen Sammelantrag 15. Mai Pachtvertragsanzeige § 2 LPachtVG OWiG-Einspruch zwei Wochen. Normen §§ 581 ff. BGB HoefeO GAP-VO 2021/2115 DueV. Eskalation Telefon-Sofort bei Sammelantragsfrist Tierseuche. Output Triage-Memo Fristen-Ampel Routing zu landpacht-und-hoferbfolge-prüfen. Abgrenzung zu erstgespraech-mandatsannahme (Mandatsaufnahme-Leitfaden).

### Mandat-Triage Agrarrecht

## Ablauf — sieben Fragen

### Frage 1 — Mandantenrolle?

- Landwirt selbstbewirtschaftend
- Verpächter (Landwirt oder anderer Eigentümer)
- Pächter
- Hof-Erbe (Anerbe)
- Weichender Erbe
- Junglandwirt-Hofnachfolge
- Genossenschaft / Maschinenring
- Förderbescheid-Adressat
- Verband (Bauernverband)
- Behörde / Landwirtschaftsamt (selten)

### Frage 2 — Sachgebiet?

- Landpacht
- Höfeerbfolge / Hofübergabe
- ELER / GAP Sammelantrag
- Cross Compliance
- Tierhaltung Tiergesundheit
- Pflanzenschutz
- Düngeverordnung
- Wasserrecht im Außenbereich
- Naturschutz / FFH-Gebiet
- Bio-Zertifizierung
- Direktvermarktung Hofladen
- Genossenschaftsrecht
- Agrarstrukturrecht / Reichssiedlungsgesetz
- Jagdpacht / Jagdrecht
- Fischerei
- Bauplanungsrecht Außenbereich § 35 BauGB

### Frage 3 — Akute Eilbedürftigkeit?

- **Sammelantrag-Frist** 15. Mai (Vorlage) — verspätet bedeutet Förderverlust oder Kürzung
- **Tierseuche** ASP MKS Geflügelpest Anordnung Maßregelung
- **Behördliche Untersagung** Tierhaltung Düngung Direktvermarktung
- **Pacht-Kündigung** in laufendem Jahr
- **Cross Compliance Vor-Ort-Kontrolle** kritischer Befund
- **Rückforderung Fördermittel** mit Vollziehung
- **Eilantrag gegen Wolfsentnahme-Verbot**

### Frage 4 — Stand?

- Beratungsbedarf vor Antrag / Vertrag
- Antrag gestellt — wartet auf Bescheid
- Bescheid liegt vor — Frist offen
- Widerspruchs-/Klageverfahren
- Behördliche Anordnung sofortig vollziehbar
- Strafverfahren (z. B. Tierschutz § 17 TierSchG)
- Notarielle Abwicklung (Hofübergabe)

### Frage 5 — Bundesland?

- Höfeerbrecht je Bundesland verschieden
- Bayern: Bayerisches Höferecht
- BW: BWHöfeG
- NDS NRW SH: HöfeO
- HE RH-Pfalz: eigene HöfeO
- Sonstige: allg. Erbrecht
- Land-Recht Naturschutz Wasser

### Frage 6 — Frist?

- **Sammelantrag** 15. Mai (Vorlage länderspezifisch)
- **Pachtvertragsanzeige** § 2 LPachtVG ein Monat
- **Hofübergangs-Anzeige** Landwirtschaftsbehörde
- **Hofeserbschaft** Höferolle-Anpassung sechs Monate
- **Verjährungs-Standard** drei Jahre § 195 BGB
- **Widerspruchsfrist** ein Monat § 70 VwGO

### Frage 7 — Wirtschaftliche Verhältnisse?

- Betriebsgröße (Hektar Tiere Umsatz)
- Förderung-Volumen
- Versicherung Berufshaftpflicht Landwirt
- Erbschaftsteuer-Aspekt bei Hofübergabe

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Landpachtvertrag Hofeserbfolge | `landpacht-und-hoferbfolge-pruefen` |
| Förderbescheid Widerspruch / Klage | `landpacht-und-hoferbfolge-pruefen` ELER plus `mandat-triage-verwaltungsrecht` |
| Tierhaltungs-Streit Tierschutz | (Skill tierhaltung-tierschutz — perspektivisch) |
| Bio-Zertifizierung | (Skill bio-zertifizierung — perspektivisch) |
| Direktvermarktung | (Skill direktvermarktung-recht — perspektivisch) |
| Jagdpacht | (Skill jagdrecht — perspektivisch) |
| Genossenschaft | weiter an `gesellschaftsrecht`-Plugin |
| Strafverfahren TierSchG | weiter an `mandat-triage-strafrecht` |
| Hofübergabe steuerlich | weiter an `anw-mandat-triage-steuerrecht` plus ErbSt |

## Mandatsannahme

- **Konflikt-Check** — bei Höfeerbschaft kein Doppelmandat Anerbe / weichender Erbe
- **Streitwert** Hofeswert / Pachtwert / Förderhöhe
- **Versicherungs-Deckung** Berufshaftpflicht Landwirt prüfen
- **Notarbedarf** Hofübergabe

## Eskalation

- **Telefon-Sofort** Sammelantragsfrist Tierseuche Vor-Ort-Kontrolle Polizei
- **Binnen einer Stunde** Eilantrag VG gegen Anordnung
- **Heute** Pachtvertragsanzeige Sammelantrag-Vorbereitung
- **Diese Woche** Klage Erstentwurf Hofübergabe-Notarvorbereitung

## Ausgabe

- `triage-protokoll-agrarrecht.md`
- Aktenanlage
- Frist im Fristenbuch (Sammelantrag Pachtvertrag-Anzeige etc.)
- Mandatsvereinbarung mit Honorar
- Empfehlung Folge-Skill

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen

- BGB §§ 585 ff. 1922 ff.
- HöfeO LPachtVG
- VO (EU) 2021/2115 GAP-Strategieplan
- TierSchG TierGesG
- BauGB § 35
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Vertiefung — Rechtsprechung und Normenkette Triage

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung Triage-Routing

LwVG §§ 1 ff. (Zuständigkeit Landwirtschaftsgericht) → § 70 VwGO (Widerspruch Förderbescheid) → §§ 195, 199 BGB (Verjährung Pacht, Abfindung) → § 203 BGB (Hemmung durch Verhandlungen) → GrdstVG (Grundstücksverkehr-Genehmigung) → LPachtVG § 2 (Pachtanzeige-Frist)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `fachanwalt-agrarrecht-orientierung`

_Anwalt will ueberblicken welche Normen und Mandate das Agrarrecht umfasst oder Fachanwaltschaft vorbereiten. Orientierung HoefeO Anerbenrecht Landpachtrecht §§ 581 ff. BGB GVG-Grund EU-Agrarpolitik GAP Direktzahlungen Duengerecht Tierschutz Pflanzenschutz Naturschutz Forstrecht. FAO-Voraussetzungen typische Mandate Notfristen Sammelantrag 15. Mai. Output Orientierungs-Übersicht mit Norm-Landkarte und Routing zu Spezial-Skills. Abgrenzung: mandat-triage-agrarrecht für konkreten Mandats-Einstieg._

# Fachanwalt für Agrarrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 30 Fälle in den letzten drei Jahren, davon mindestens 15 streitige.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Höferecht | HöfeO (Nordrhein-Westfalen Niedersachsen Schleswig-Holstein Hamburg) Anerbenrechte anderer Länder |
| Landpacht | BGB §§ 581 ff. (Landpachtvertrag) §§ 585 ff. (Landpachtverträge über landwirtschaftliche Grundstücke) LPachtVG (Landpachtverkehrsgesetz) |
| Grundstücksverkehr | GrdstVG (Grundstücksverkehrsgesetz) Genehmigungspflicht bei Verkauf landwirtschaftlicher Flächen |
| EU-Agrarpolitik | GAP EU-Direktzahlungen-Verordnung 2021/2115 Konditionalitaet Cross-Compliance |
| Duenge- und Pflanzenschutz | DueV (Düngeverordnung) PflSchG (Pflanzenschutzgesetz) |
| Tierschutz | TierSchG TierSchNutztV |
| Tierseuchen | TierGesG |
| Naturschutz | BNatSchG (Bundesnaturschutzgesetz) NatSchG Land |
| Wasser | WHG (Wasserhaushaltsgesetz) |
| Forst | BWaldG Landesforstgesetze |
| Agrar-Förderung | EU-Gemeinschaftliche Strategien Agrarförderung Land |

## Typische Mandate

- Hofübergabe / Erbsachen mit landwirtschaftlichem Bezug
- Landpachtstreit Kündigung Pachtzins Pachtverlängerung
- Grundstücksverkehr Genehmigungsverfahren nach GrdstVG
- EU-Förderbescheide Direktzahlung Cross-Compliance-Korrektur
- Düngeverordnung-Verstöße
- Tierseuchen-Bescheide Tierseuchen-Tilgung
- Pflanzenschutzmittel-Rückruf
- Naturschutz-Streit Eingriffsregelung

## Fristen

- **Hofübergabe** Hofbezugnahme nach Erbfall — siehe Höfeordnung Anerbenrechte.
- **Landpachtkündigung** § 585 BGB iVm Landpachtvertrag (oft jaehrlich zu festgelegten Terminen).
- **GrdstVG** Genehmigungsverfahren läuft über Landwirtschaftsbehörde.
- **Widerspruch gegen Förderbescheid** ein Monat (VwGO § 70 / SGG § 84 je nach Behörde).

## Hauptforen

- **Landwirtschaftsgericht** (beim AG / LG je Bundesland — Landwirtschaftsverfahren-Gesetz LwVG).
- **Verwaltungsgericht** bei öffentlich-rechtlichen Förderbescheiden.
- **BGH** Senat für Landwirtschaftssachen (V. Zivilsenat).
- **EuGH** bei GAP-Vorabentscheidungen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- Deutsche Gesellschaft für Agrarrecht.

## Schnittstellen

- **fachanwalt-erbrecht** bei Hofübergabe.
- **fachanwalt-verwaltungsrecht** bei Förderbescheiden.
- **kanzlei-allgemein** Fristen Versand.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Paragrafenkette (Überblick Agrarrecht)

BGB §§ 581-597 (Landpacht) → LPachtVG (Pachtverkehr, Genehmigung) → GrdstVG (Grundstücksverkehr) → HöfeO §§ 1 ff. (Erbrecht landwirtschaftlicher Betriebe) → VO (EU) 2021/2115 + 2021/2116 (GAP, Direktzahlungen, Konditionalität) → DüG i.V.m. DüV (Düngerecht) → BNatSchG §§ 13 ff. (Naturschutz, Eingriffsregelung) → § 35 BauGB (Außenbereich landwirtschaftliche Privilegierung) → TierSchG, TierGesG → LwVG (Verfahren Landwirtschaftsgericht)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Fristen-Übersicht

| Verfahren | Frist | Norm |
|---|---|---|
| Widerspruch Förderbescheid | 1 Monat | § 70 VwGO |
| Klage VG (nach Widerspruch) | 1 Monat | § 74 VwGO |
| GAP-Mehrfachantrag | 15. Mai | GAPInVeKoSG |
| Pachtanzeige LPachtVG | 1 Monat nach Vertragsschluss | § 2 LPachtVG |
| Grundstücksverkehr-Genehmigung | Antrag vor Vollzug | § 2 GrdstVG |
| Nachabfindungsfrist HöfeO | 20 Jahre ab Übergabe | § 13 HöfeO |

## Triage — Orientierungs-Routing Agrarrecht

1. **Hofrecht / Erbfall** → `fachanwalt-agrarrecht-hoefe-uebergabe`, `landpacht-und-hoferbfolge-pruefen`
2. **Landpachtstreit** → `fachanwalt-agrarrecht-pachtvertrag-streitig`
3. **GAP-Förderung / Direktzahlungen** → `fachanwalt-agrarrecht-gap-direktzahlungen-antrag`, `fachanwalt-agrarrecht-eu-agrarfoerderung`
4. **Düngerecht / OWiG** → `fachanwalt-agrarrecht-duenge-ordnungswidrigkeit`
5. **Tierhaltungsgenehmigung** → `fachanwalt-agrarrecht-tierhaltung-genehmigung`
6. **Wolfsentnahme / Naturschutz** → `fachanwalt-agrarrecht-wolfsentnahme-genehmigung-bnatschg`

---

## Skill: `orientierung-fachanwaltschaft-mandat`

_Anwalt will überblicken welche Normen und Mandate das Agrarrecht umfasst oder Fachanwaltschaft vorbereiten: Orientierung HoefeO Anerbenrecht Landpa..._

# Anwalt will überblicken welche Normen und Mandate das Agrarrecht umfasst oder Fachanwaltschaft vorbereiten


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GrdstVG Genehmigung 1 Monat (verlängerbar), GAP-Antrag bis 15.05. jährlich (Mehrfachantrag), BGB § 594a Landpacht-Kündigung 2. Werktag im 3. Pachtjahr.
- Tragende Normen verifizieren: FAO § 14b, BGB §§ 581 ff. (Landpacht), GrdstVG, Landwirtschaftsanpassungsgesetz (LwAnpG), HöfeO, EU-GAP-VO (2021/2115, 2021/2116, 2021/2117), MarktorganisationsG, BNatSchG, DüV, AwSV — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Landwirt, Bundesanstalt für Landwirtschaft und Ernährung (BLE), Landwirtschaftskammer, Genehmigungsbehörde nach GrdstVG, Landpächter/-verpächter, Amtsgericht Landwirtschaftsgericht.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Mehrfachantrag (Flächenförderung), Pachtvertrag, GrdstVG-Genehmigung, Düngeplan, Cross-Compliance-Nachweis, Hofübergabevertrag — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Anwalt will überblicken welche Normen und Mandate das Agrarrecht umfasst oder Fachanwaltschaft vorbereiten. Orientierung HoefeO Anerbenrecht Landpachtrecht §§ 581 ff. BGB GVG-Grund EU-Agrarpolitik GAP Direktzahlungen Duengerecht Tierschutz Pflanzenschutz Naturschutz Forstrecht. FAO-Voraussetzungen typische Mandate Notfristen Sammelantrag 15. Mai. Output Orientierungs-Übersicht mit Norm-Landkarte und Routing zu Fachmodule. Abgrenzung: mandat-triage-agrarrecht für konkreten Mandats-Einstieg.

### Fachanwalt für Agrarrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 30 Fälle in den letzten drei Jahren, davon mindestens 15 streitige.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Höferecht | HöfeO (Nordrhein-Westfalen Niedersachsen Schleswig-Holstein Hamburg) Anerbenrechte anderer Länder |
| Landpacht | BGB §§ 581 ff. (Landpachtvertrag) §§ 585 ff. (Landpachtverträge über landwirtschaftliche Grundstücke) LPachtVG (Landpachtverkehrsgesetz) |
| Grundstücksverkehr | GrdstVG (Grundstücksverkehrsgesetz) Genehmigungspflicht bei Verkauf landwirtschaftlicher Flächen |
| EU-Agrarpolitik | GAP EU-Direktzahlungen-Verordnung 2021/2115 Konditionalitaet Cross-Compliance |
| Duenge- und Pflanzenschutz | DueV (Düngeverordnung) PflSchG (Pflanzenschutzgesetz) |
| Tierschutz | TierSchG TierSchNutztV |
| Tierseuchen | TierGesG |
| Naturschutz | BNatSchG (Bundesnaturschutzgesetz) NatSchG Land |
| Wasser | WHG (Wasserhaushaltsgesetz) |
| Forst | BWaldG Landesforstgesetze |
| Agrar-Förderung | EU-Gemeinschaftliche Strategien Agrarförderung Land |

## Typische Mandate

- Hofübergabe / Erbsachen mit landwirtschaftlichem Bezug
- Landpachtstreit Kündigung Pachtzins Pachtverlängerung
- Grundstücksverkehr Genehmigungsverfahren nach GrdstVG
- EU-Förderbescheide Direktzahlung Cross-Compliance-Korrektur
- Düngeverordnung-Verstöße
- Tierseuchen-Bescheide Tierseuchen-Tilgung
- Pflanzenschutzmittel-Rückruf
- Naturschutz-Streit Eingriffsregelung

## Fristen

- **Hofübergabe** Hofbezugnahme nach Erbfall — siehe Höfeordnung Anerbenrechte.
- **Landpachtkündigung** § 585 BGB iVm Landpachtvertrag (oft jaehrlich zu festgelegten Terminen).
- **GrdstVG** Genehmigungsverfahren läuft über Landwirtschaftsbehörde.
- **Widerspruch gegen Förderbescheid** ein Monat (VwGO § 70 / SGG § 84 je nach Behörde).

## Hauptforen

- **Landwirtschaftsgericht** (beim AG / LG je Bundesland — Landwirtschaftsverfahren-Gesetz LwVG).
- **Verwaltungsgericht** bei öffentlich-rechtlichen Förderbescheiden.
- **BGH** Senat für Landwirtschaftssachen (V. Zivilsenat).
- **EuGH** bei GAP-Vorabentscheidungen.

## Berufsverband

- Deutsche Gesellschaft für Agrarrecht.

## Schnittstellen

- **fachanwalt-erbrecht** bei Hofübergabe.
- **fachanwalt-verwaltungsrecht** bei Förderbescheiden.
- **kanzlei-allgemein** Fristen Versand.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Paragrafenkette (Überblick Agrarrecht)

BGB §§ 581-597 (Landpacht) → LPachtVG (Pachtverkehr, Genehmigung) → GrdstVG (Grundstücksverkehr) → HöfeO §§ 1 ff. (Erbrecht landwirtschaftlicher Betriebe) → VO (EU) 2021/2115 + 2021/2116 (GAP, Direktzahlungen, Konditionalität) → DüG i.V.m. DüV (Düngerecht) → BNatSchG §§ 13 ff. (Naturschutz, Eingriffsregelung) → § 35 BauGB (Außenbereich landwirtschaftliche Privilegierung) → TierSchG, TierGesG → LwVG (Verfahren Landwirtschaftsgericht)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Fristen-Übersicht

| Verfahren | Frist | Norm |
|---|---|---|
| Widerspruch Förderbescheid | 1 Monat | § 70 VwGO |
| Klage VG (nach Widerspruch) | 1 Monat | § 74 VwGO |
| GAP-Mehrfachantrag | 15. Mai | GAPInVeKoSG |
| Pachtanzeige LPachtVG | 1 Monat nach Vertragsschluss | § 2 LPachtVG |
| Grundstücksverkehr-Genehmigung | Antrag vor Vollzug | § 2 GrdstVG |
| Nachabfindungsfrist HöfeO | 20 Jahre ab Übergabe | § 13 HöfeO |

## Triage — Orientierungs-Routing Agrarrecht

1. **Hofrecht / Erbfall** → `fachanwalt-agrarrecht-hoefe-uebergabe`, `landpacht-und-hoferbfolge-pruefen`
2. **Landpachtstreit** → `fachanwalt-agrarrecht-pachtvertrag-streitig`
3. **GAP-Förderung / Direktzahlungen** → `fachanwalt-agrarrecht-gap-direktzahlungen-antrag`, `fachanwalt-agrarrecht-eu-agrarfoerderung`
4. **Düngerecht / OWiG** → `fachanwalt-agrarrecht-duenge-ordnungswidrigkeit`
5. **Tierhaltungsgenehmigung** → `fachanwalt-agrarrecht-tierhaltung-genehmigung`
6. **Wolfsentnahme / Naturschutz** → `fachanwalt-agrarrecht-wolfsentnahme-genehmigung-bnatschg`

---

## Skill: `erstgespraech-mandatsannahme`

_Strukturierter Erstgespraechsleitfaden für Agrar-, Forst- und Lebensmittelrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen: Strukturierter Erstgespraechsleitf..._

# Strukturierter Erstgespraechsleitfaden für Agrar-, Forst- und Lebensmittelrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GrdstVG Genehmigung 1 Monat (verlängerbar), GAP-Antrag bis 15.05. jährlich (Mehrfachantrag), BGB § 594a Landpacht-Kündigung 2. Werktag im 3. Pachtjahr.
- Tragende Normen verifizieren: FAO § 14b, BGB §§ 581 ff. (Landpacht), GrdstVG, Landwirtschaftsanpassungsgesetz (LwAnpG), HöfeO, EU-GAP-VO (2021/2115, 2021/2116, 2021/2117), MarktorganisationsG, BNatSchG, DüV, AwSV — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Landwirt, Bundesanstalt für Landwirtschaft und Ernährung (BLE), Landwirtschaftskammer, Genehmigungsbehörde nach GrdstVG, Landpächter/-verpächter, Amtsgericht Landwirtschaftsgericht.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Mehrfachantrag (Flächenförderung), Pachtvertrag, GrdstVG-Genehmigung, Düngeplan, Cross-Compliance-Nachweis, Hofübergabevertrag — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierter Erstgespraechsleitfaden für Agrar-, Forst- und Lebensmittelrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.

### Erstgespraech und Mandatsannahme im Agrar-, Forst- und Lebensmittelrecht

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Agrar-, Forst- und Lebensmittelrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klären, Konflikt- und GwG-Prüfung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Agrar-, Forst- und Lebensmittelrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klägerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Hofnachfolge, GAP-Direktzahlungen, Landpachtvertrag, Tierhaltung/TierSchG, Lebensmittelrecht
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Klage/Widerspruch im Agrarverwaltungs- oder Pachtprozess). Frist-Alarm an die Vorbereitung weitergeben.

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

Standard-Streitwerte im Bereich Agrar-, Forst- und Lebensmittelrecht:

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

- BORA, BRAO, FAO für Fachanwaltschaft Agrar-, Forst- und Lebensmittelrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- §§ 585 ff. BGB, GAP-DZ-VO, BTSchG, BNatSchG, BImSchG, LFGB (für fachliche Erstpruefung).
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

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Agrar-, Forst- und Lebensmittelrecht). Handlungs-Sequenz:

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
- Verfahrensdauer im Bereich Agrar-, Forst- und Lebensmittelrecht: Erfahrungswerte nach Instanz.
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

## Vertiefung — Normenkette und Rechtsprechung Erstgespräch Agrarrecht

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normenkette Erstgespräch Agrarrecht

LwVG §§ 1 ff. (Zuständigkeit klären) → §§ 70, 74 VwGO (Fristen Förderbescheide sofort prüfen) → GrdstVG (Genehmigungspflicht prüfen) → §§ 10, 11 GwG (GwG-Identifizierung, bes. GbR) → §§ 3, 3a RVG (Honorarvereinbarung) → § 9 RVG (Vorschuss) → §§ 195, 199 BGB (Verjährungsstand sofort ermitteln)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `erstpruefung-und-mandatsziel`

_Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel


## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; landesrechtliche Wald-, Jagd-, Naturschutz- und Landwirtschaftsregeln live ergänzen, wenn sie den konkreten Auftrag tragen:

- `§ 581 Abs. 1 BGB` — Pachtvertrag als Grundtyp.
- `§ 585 Abs. 1 BGB` — Landpachtvertrag.
- `§ 594a Abs. 1 BGB` — Kündigung und Fristen im Landpachtrecht.
- `§ 1 GrdstVG` — Genehmigungspflicht im landwirtschaftlichen Grundstücksverkehr.
- `§ 9 GrdstVG` — Versagungsgründe.
- `§ 1 HöfeO` — Hofeigenschaft.
- `§ 5 HöfeO` — Hoferbenstellung und Wirtschaftsfähigkeit live prüfen.
- `§ 9 BWaldG` — Waldumwandlung.
- `§ 11 BWaldG` — ordnungsgemäße Bewirtschaftung des Waldes.
- `§ 14 BWaldG` — Betreten des Waldes.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GrdstVG Genehmigung 1 Monat (verlängerbar), GAP-Antrag bis 15.05. jährlich (Mehrfachantrag), BGB § 594a Landpacht-Kündigung 2. Werktag im 3. Pachtjahr.
- Tragende Normen verifizieren: FAO § 14b, BGB §§ 581 ff. (Landpacht), GrdstVG, Landwirtschaftsanpassungsgesetz (LwAnpG), HöfeO, EU-GAP-VO (2021/2115, 2021/2116, 2021/2117), MarktorganisationsG, BNatSchG, DüV, AwSV — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Landwirt, Bundesanstalt für Landwirtschaft und Ernährung (BLE), Landwirtschaftskammer, Genehmigungsbehörde nach GrdstVG, Landpächter/-verpächter, Amtsgericht Landwirtschaftsgericht.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Mehrfachantrag (Flächenförderung), Pachtvertrag, GrdstVG-Genehmigung, Düngeplan, Cross-Compliance-Nachweis, Hofübergabevertrag — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** HöfeO, BGB, GAP, EU.

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

## Skill: `fachanwalt-agrarrecht-verhandlung-landpacht-schlichtung`

_Landwirt und Verpaechter streiten über Pacht oder Hof-Erbe und muessen Einigung außergerichtlich versuchen. Prüfraster Pachtvertrags-Vergleich LPachtVG Pachtanpassung § 593 BGB Landwirtschaftskammer-Schlichtung. ADR-Wege Hofuebergabe-Mediation Schlichtungsformate im Pachtgewerbe. Normen §§ 581 ff. BGB § 593 BGB Pachtanpassung LPachtVG. Output Verhandlungs-Strategie-Memo Schlichtungsantrag Vergleichs-Skript. Abgrenzung: fachanwalt-agrarrecht-pachtvertrag-streitig für streitiges Gerichtsverfahren._

# Verhandlung und Schlichtung im Agrarrecht

## Zweck

Kommunikations- und Verhandlungsstrategie für agrarrechtliche Mandate: Landpacht-Anpassungen, Hofübergabe-Konflikte, Förderstreitigkeiten BLE/EGFL/ELER, Wolfsrisse-Entschädigungs-Verhandlung. Schwerpunkt auf den agrarrechtlich typischen Schlichtungs- und Vergleichsorganen — Landwirtschaftskammer, Bauernverband, Pachtrichter beim Landwirtschaftsgericht.

## Mandantenfragen — Kaltstart

1. **Was ist das Streitziel — Vertragsbeendigung oder Fortführung?** — Fundamentaler Unterschied in der Strategie; bei Fortführungswillen ist Schlichtung zwingend voranzustellen.
2. **Wie lange bestehen die Vertragsbeziehungen?** — Langjährige Pacht- und Familien­beziehungen verlangen behutsame Kommunikation; harte Konfrontation zerstört langfristige Kooperation.
3. **Gibt es eine Schiedsklausel im Pachtvertrag?** — Schiedsvertrag bindet die Parteien; VG-Klageweg ausgeschlossen.
4. **Wurde bereits LWK-Schlichtung beantragt?** — § 23 LwVG-Pflichtversuch vor Klage; ggf. Klage unzulässig ohne Nachweis.
5. **Was ist das wirtschaftliche Interesse des Mandanten?** — Jährliche Pachtdifferenz x verbleibende Laufzeit = Barwert des Streits; Kosten-Nutzen vor Klage prüfen.
6. **Haben Dritte (Kinder, Geschwister) Interesse am Hof?** — Hofstreitigkeiten in Erbengemeinschaft erfordern notarielle Auseinandersetzungs-Vereinbarung.
7. **Laufen parallele Förderverfahren?** — Bei laufenden ELER-Verpflichtungen Streit um Pacht­preis mit Rückforderungsrisiko verknüpft; Koordination nötig.
8. **Ist ein Herdenschutzstreit (Wolf) parallel anhängig?** — Entschädigungs-Verhandlung mit dem Land läuft über andere Behörden als Pachtrecht.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtlicher Rahmen

- **§ 593 BGB** — Pachtzins-Anpassung: beidseitig; Maßstab ortsübliche Pacht, LWK-Statistik als Anhaltspunkt.
- **§ 2 LPachtVG** — Anzeigepflicht Pachtvertrag.
- **§ 4 LPachtVG** — Beanstandungsrecht der LWK; schützt vor ungesunder Bodenverteilung.
- **§ 13 LwVG** — Landwirtschaftsgericht beim Amtsgericht: ausschließliche Zuständigkeit für Pacht- und Höfe-Sachen.
- **§ 23 LwVG** — Pflichtiger Schlichtungsversuch: Klage unzulässig ohne vorherigen Schlichtungsversuch.
- **§ 278 ZPO** — Güteverhandlung; gilt auch im Landwirtschaftsgericht.
- **§ 24 BBodSchG** — Kostenausgleich bei Bodensanierung; relevant bei Kontext Altlasten-Streit.

### Leitentscheidungen

| Gericht | Aktenzeichen | Kernaussage |
|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Kommunikations-Pfade

### Pfad 1 — Landwirtschaftskammer-Schlichtungsstelle

- In den meisten Bundesländern eingerichtet (LWK Niedersachsen, NRW, RLP, BW)
- Außergerichtliche Schlichtung in Pacht- und Förder-Sachen
- Vorteil: agrarpolitisch erfahrene Schlichter, oft Landwirte oder Berater
- Kosten: Kammergebühren 100–500 EUR
- Typische Dauer: 4–8 Wochen bis Einigung oder Protokoll des Scheiterns

### Pfad 2 — Bauernverband-Vermittlung

- Bei innerverbandlichen Konflikten oder zwischen Verbandsmitgliedern
- Informell; Vorteil: persönliches Vertrauen, grundsätzlich kostenlos
- Keine Vollstreckung des Einigungsergebnisses ohne notarielle Urkunde

### Pfad 3 — Pachtrichter und Landwirtschaftsgericht § 23 LwVG

- Pflichtiger Schlichtungsversuch vor Klage in Pacht- und Höfe-Sachen
- Landwirtschaftsgericht beim AG (mit ehrenamtlichen landwirtschaftlichen Beisitzern § 2 LwVG)
- Vergleich vor Pachtrichter ist vollstreckbarer Titel (§ 794 Abs. 1 Nr. 1 ZPO)
- Verfahren: Schriftlicher Antrag → Ladung beider Parteien → Schlichtungstermin → Protokoll
- Bei Scheitern: Bescheinigung für Klage-Zulässigkeit

### Pfad 4 — Mediation Hofübergabe

- Familieninterne Mediation bei Hofnachfolge; Mediator oft aus LWK-Beratungsdienst oder freier Mediator (§§ 1 ff. MediationsG)
- Gesprächsstruktur: Bedürfnisse der Übernehmer, der weichenden Erben, der Übergeber
- Ergebnis: Hofübergabe-Vertrag notariell mit Altenteil, Wohnrecht, Rückforderungsklauseln, Pflichtteilsverzicht
- Steuervorteil: Befreiung § 13 Abs. 1 Nr. 4a ErbStG bei Betriebsübernahme

### Pfad 5 — BLE / Landwirtschaftsamt-Korrespondenz

- Bei Förder-Streitigkeiten (GAP, ELER, Cross-Compliance-Kürzung)
- Widerspruch → Widerspruchsbescheid → VG-Klage
- Viele Fälle sind außergerichtlich einigungsfähig bei konkreter Sachverhalts-Darlegung

## Workflow

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.


### Phase 1 — Sachverhalts-Klärung mit Mandant

- Konflikthistorie (oft jahrelange Beziehung)
- Wirtschaftliche Tragweite (Hof-Existenz vs. einmaliger Schaden)
- Beziehungs-Diagnose (Können Parteien künftig kooperieren?)
- Gewünschtes Ergebnis (Anpassung vs. Beendigung)

### Phase 2 — Vorgerichtliche Korrespondenz

- Anwaltsschreiben an Gegenseite: Sachverhaltsdarstellung ohne Vorwürfe
- Vergleichs-Angebot mit konkreter Zahl + Frist (typisch 21 Tage)
- Androhung Schlichtungsantrag + ggf. Klage

### Phase 3 — Schlichtungsversuch § 23 LwVG

- Schriftlicher Antrag beim Landwirtschaftsgericht (oder LWK)
- Vorab: Sachverhalts-Kurzdarstellung + Angebot
- Anhörung beider Parteien durch Pachtrichter
- Vergleichsvorschlag durch Pachtrichter
- Protokoll bei Scheitern (Voraussetzung Klage-Zulässigkeit)

### Phase 4 — Klage (bei Scheitern)

- Klage Landwirtschaftsgericht (Wert bis 5.000 EUR: AG; darüber: LG mit Kammer für Handelssachen — nein; Landwirtschaftssache: AG-Landwirtschaftsgericht als Sonderkammer)
- Beweisaufnahme (ortsübliche Pacht durch LWK-Statistik + Sachverständiger)
- Zwischenurteil bei Frist-Fragen

### Phase 5 — Vollstreckung / Umsetzung

- Vergleichs-Vollstreckung über § 794 ZPO
- Bei Hofübergabe: notarielle Beurkundung des Übergabevertrags

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Landpachtkonflikt verhandeln | Fuenfstufiger Pfad-Ueberblick; Schriftsatzbausteine unten |
| Variante A — beide Seiten einigungsbereit | Direkter Pfad 1 (Schlichtungsstelle) ohne Gericht |
| Variante B — Pachtverhaeltnis sehr festgefahren | Gerichtlicher Weg § 23 LwVG vorbereiten |
| Variante C — Hofuebergabe involviert | Pfad 4 Mediation Hofuebergabe; familienrechtliche Aspekte beachten |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatz-Bausteine

### Außergerichtliches Anpassungs-Schreiben § 593 BGB

```
[Kanzlei]                                           [Ort, Datum]

[Gegenseite]
[Anschrift]

Pachtvertrag vom [Datum], Flur [Bezeichnung]
Anpassungs-Verlangen § 593 BGB

Sehr geehrte Damen und Herren,

aus dem Pachtvertrag vom [Datum] ueber [ha] [Kulturart]
machen wir namens und in Vollmacht unserer Mandantschaft
den Anpassungs-Anspruch nach § 593 BGB geltend.

Seit Vertragsschluss ist die ortsübliche Vergleichspacht
in der Region [Region] von [Betrag EUR/ha] auf
[Betrag EUR/ha] gestiegen (LWK-Pachtstatistik [Jahr],
Gutachterausschuss-Beschluss [Nr.]). Die Differenz beträgt
[EUR/ha × ha × Laufzeit = Gesamtbetrag].

Wir bitten um Zustimmung zur Anpassung auf
EUR [neuer Betrag] je Hektar ab [Datum].

Im Falle keiner Einigung binnen [21 Tage] werden wir
Schlichtungsversuch nach § 23 LwVG beim Landwirtschafts-
gericht [Ort] anregen.

[Rechtsanwalt/-anwaeltin, Fachanwalt fuer Agrarrecht]
```

### Schlichtungsantrag § 23 LwVG

```
An das Landwirtschaftsgericht beim AG [Ort]
Schlichtungsantrag nach § 23 LwVG

Antragsteller: [Mandant]
Antragsgegner: [Gegenseite]

Streitgegenstand: Pachtpreisanpassung § 593 BGB
Pachtvertrag vom [Datum], Objekt [Bezeichnung]

Sachverhalt:
[Kurze neutrale Darstellung des Konflikts]

Angebot:
[Konkretes Anpassungs-Angebot]

Wir bitten um Anberaumung eines Schlichtungstermins.

[Rechtsanwalt/-anwaeltin]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]


## Strategie und Taktik

| Konstellation | Empfehlung |
|---|---|
| Familien-Hofstreit | Mediation vorrangig; Zerstörung der Eltern-Kind-Beziehung oft schlimmer als Rechtsverlust |
| Pächter will Hof zurückgeben | Kündigungs-Zeitplan prüfen; bei Verstoß gegen Bewirtschaftungs-Pflicht vorzeitige außerordentliche Kündigung möglich |
| Verpächter will höhere Pacht | LWK-Statistik-Gutachten einholen; Klage erst wenn Vergleich eindeutig scheitert |
| Förder-Streit mit Behörde | Sachverhalts-Klarstellung mit Belegen; oft einfach lösbar außergerichtlich |
| Wolfsriss-Entschädigung | Riss-Protokoll + Marktwert-Gutachten als Verhandlungs-Grundlage; Verhandlung mit Landwirtschafts-Ministerium |

## Beweislast und Darlegungslast

- Bei § 593 BGB-Anpassung: Verlangende Partei legt Verhältnisänderung dar (LWK-Statistik, Bodenrichtwert).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Im Schlichtungsverfahren: kein formelles Beweisverfahren; Glaubhaftmachung und Unterlagen genügen.

## Fristen

| Frist | Dauer | Rechtsgrundlage |
|---|---|---|
| Reaktionsfrist bei außergerichtlichem Schreiben | 14–21 Tage (Praxis) | Eigene Fristsetzung |
| Schlichtungsantrag vor Klage | Keine starre Frist; vor Klageerhebung | § 23 LwVG |
| Kündigung ordentlich | 2 Jahre vor Pachtjahresende | § 594a BGB |
| Klage nach Schlichtungs-Scheitern | Keine Ausschluss-Frist; Verjährung § 195 BGB (3 Jahre) | §§ 195, 199 BGB |

## Streitwert und Kosten

- Pacht-Anpassungs-Klage: dreifacher Jahresmehrwert der begehrten Anpassung (§ 41 Abs. 1 ZPO).
- Schlichtungsverfahren: Kammergebühr LWK ca. 100–300 EUR + Reisekosten Rechtsanwalt.
- Klage Landwirtschaftsgericht: GKG-Tabelle; Anwalt nach RVG.
- Wirtschaftlichkeitsprüfung immer: Bei Pachtdifferenz < 500 EUR/Jahr übersteigen Kosten oft den Nutzen.

## Anschluss-Skills

- `landpacht-und-hoferbfolge-pruefen` — Tiefenprüfung des Pachtvertrags
- `fachanwalt-agrarrecht-wolfsentnahme-genehmigung-bnatschg` — Behörden-Kommunikation Wolf
- `sammelantrag-gap-checkliste` — GAP-Förder-Widerspruchsverfahren

## Quellen

- BGB §§ 585–597 (Landpacht), §§ 195, 199 (Verjährung)
- LPachtVG §§ 2, 4, 13
- LwVG §§ 2, 13, 23
- MediationsG §§ 1 ff.
- ZPO §§ 278, 794
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Ergänzung — Aktuelle Rechtsprechung 2022-2024

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `fachanwalt-agrarrecht-hoefe-uebergabe`

_Hofuebergabe nach HoefeO (Hamburg Niedersachsen NRW Schleswig-Holstein). Hofeigenschaft § 1 HoefeO Mindestwirtschaftswert. Hoferbe § 4 HoefeO Anerbenfolge. Hofuebergabe zu Lebzeiten als Hofesvertrag formbedürftig § 311b BGB. Pflichtteilsergaenzungsanspruch der weichenden Erben § 12 HoefeO Hofeswert nicht Verkehrswert. Bewirtschaftungspflicht Nachabfindung § 13 HoefeO. Hofverbund Nachhaltigkeit._

# Höfe-Übergabe

## Kaltstart-Rückfragen

1. In welchem Bundesland liegt der Hof (HöfeO gilt nur Hamburg, Niedersachsen, NRW, Schleswig-Holstein)?
2. Liegt Hofeigenschaft im Grundbuch eingetragen vor (Hoffolgevermerk § 6 HöfeO)?
3. Welche weichenden Geschwister gibt es und welche Pflichtteilsansprüche drohen?
4. Soll die Übergabe zu Lebzeiten erfolgen oder im Erbfall geregelt werden?
5. Welche Vorbehalte (Altenteil, Wohnrecht, Pflegevereinbarung) sind gewünscht?

## Anspruchsgrundlagen

- Hofeigenschaft § 1 HöfeO — land- oder forstwirtschaftliche Besitzung mit Wirtschaftsfähigkeit; Mindestwirtschaftswert (i.d.R. ab 10.000 EUR Einheitswert), Eintragung Hoffolgevermerk.
- Anerbenfolge § 4 HöfeO — ein Hoferbe; Reihenfolge in §§ 5-7 HöfeO.
- Hofesvertrag — Übergabe zu Lebzeiten formbedürftig nach § 311b Abs. 1 BGB (notarielle Beurkundung).
- Hofeswert § 12 HöfeO — 1,5-facher Einheitswert (nicht Verkehrswert) — Privilegierung des Hoferben.
- Abfindung weichende Erben § 12 Abs. 2 HöfeO nach Hofeswert.
- Nachabfindungsanspruch § 13 HöfeO — bei Veräußerung oder Aufgabe innerhalb 20 Jahre nach Übergabe.
- Bewirtschaftungspflicht § 17 HöfeO — keine Nachabfindung wenn nach 20 Jahren bewirtschaftet.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Beweislast und Frist

- Hoferbe trägt Beweislast für Hofeseigenschaft und Anerbenfolge.
- Weichende Erben tragen Beweislast für Pflichtteils- und Nachabfindungsansprüche.
- Frist Nachabfindung § 13 HöfeO: 20 Jahre ab Hofübergabe — Nachabfindung bei Veräußerung/Aufgabe.
- Verjährung Pflichtteilsansprüche § 195 BGB drei Jahre ab Kenntnis.

## Prüfschema

```
1. Bundesland-Zustaendigkeit (HoefeO oder Landesrecht)
2. Hofeigenschaft und Hoffolgevermerk § 6 HoefeO
3. Hofeswert § 12 HoefeO (1 5-facher Einheitswert) berechnen
4. Anerbenfolge § 4 HoefeO
5. Pflichtteils- und Abfindungsansprueche § 12 HoefeO
6. Altenteilsleistungen § 14 HoefeO
7. Notarieller Hofesvertrag § 311b BGB
8. Nachabfindung § 13 HoefeO 20-Jahresfrist
9. Steuerliche Auswirkungen ErbStG GrEStG einbeziehen
```

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Schreibvorlage notarieller Hofesvertrag (Eckpunkte)

```
Notarieller Hofesvertrag (UR-Nr.: [...])

I. Vertragsparteien
1. Uebergeber: [Name Anschrift] Eigentuemer des im Grundbuch von [Ort]
   Blatt [Nr] eingetragenen Hofes Gemarkung [...] Flurstuecke [...]
2. Uebernehmer: [Name Anschrift] — Sohn/Tochter des Uebergebers,
   Hoferbe nach § 4 HoefeO

II. Hofesgegenstand
Der Hof umfasst saemtliche Grundstuecke gemaess Anlage K1
(Grundbuchauszug) sowie das lebende und tote Inventar gemaess
Anlage K2.

III. Uebergabe
Der Uebergeber uebertraegt den Hof mit Wirkung vom [Datum] auf den
Uebernehmer. Aufgrund der Hofeigenschaft und des Anerbenrechts erfolgt
die Bewertung mit dem 1 5-fachen Einheitswert § 12 HoefeO.

IV. Altenteilsleistungen § 14 HoefeO
Der Uebernehmer gewaehrt dem Uebergeber lebenslang:
- Wohnungsrecht im Altenteilshaus
- monatliche Geldrente EUR [Betrag]
- Pflege bei Krankheit und im Alter
- standesgemaesses Begraebnis

V. Abfindung weichender Geschwister § 12 HoefeO
Die weichenden Geschwister erhalten Abfindungen gemaess Anlage K3.

VI. Bewirtschaftungspflicht § 13 HoefeO
Der Uebernehmer verpflichtet sich den Hof selbst zu bewirtschaften.
Bei Verstoss innerhalb von 20 Jahren entsteht ein Nachabfindungs-
anspruch der weichenden Erben.

VII. Steuern und Kosten
Saemtliche Vertragskosten traegt der Uebernehmer.
```

## Übergabe

- Notarielle Beurkundung § 311b BGB beim Notar veranlassen.
- Eintragung Hoffolgevermerk § 6 HöfeO und Grundbuchumschreibung.
- Pflichtteilsverzichte der weichenden Erben § 2346 BGB notariell einholen.
- Steuerberater hinzuziehen für ErbStG/GrEStG-Optimierung.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§§ 1-7 HöfeO (Hofeigenschaft, Anerbenfolge) → § 12 HöfeO (Hofeswert, Abfindung weichende Erben) → § 13 HöfeO (Nachabfindung 20-Jahre-Frist) → § 14 HöfeO (Altenteilsleistungen) → § 311b Abs. 1 BGB (Formerfordernis notarielle Beurkundung) → § 2346 BGB (Pflichtteilverzicht) → ErbStG §§ 13a, 13b (land- und forstwirtschaftliches Vermögen, Steuerverschonung) → GrEStG § 3 Nr. 6 (Steuerbefreiung Übertragung auf Abkömmlinge)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `fachanwalt-agrarrecht-duenge-ordnungswidrigkeit`

_Ordnungswidrigkeit nach Duengeverordnung DueV verteidigen. Bußgeldtatbestaende § 13a Abs. 2 DueG i.V.m. § 14 DueV. Aufzeichnungs- und Meldepflichten Nmin Stoffstrombilanz § 11a DueG. Sperrfristen Ausbringungsobergrenzen Roter Gebiete Nitratrichtlinie 91/676/EWG. Verfahren OWiG Anhoerung Einspruch binnen zwei Wochen § 67 OWiG. Bußgeldhoehe bis 150 000 EUR. Verjährung § 31 OWiG._

# Düngerechtliche Ordnungswidrigkeit

## Kaltstart-Rückfragen

1. Welcher konkrete Verstoß wird vorgehalten (Sperrfrist, Obergrenze N/P, Ausbringtechnik, Aufzeichnungspflichten, Stoffstrombilanz)?
2. Liegt der Betrieb in einem nitratbelasteten "Roten Gebiet" mit verschärften Auflagen § 13a DüV?
3. Wann ist der Bußgeldbescheid ergangen und welche Bußgeldhöhe wird festgesetzt?
4. Liegen Kontrollprotokoll, Proben und Messprotokolle vor?
5. Wurde innerhalb der Zwei-Wochen-Frist § 67 OWiG Einspruch eingelegt?

## Rechtsgrundlagen

- Düngegesetz (DüG) i.V.m. Düngeverordnung (DüV).
- Bußgeldtatbestände § 13a Abs. 2 DüG i.V.m. § 14 DüV — bis zu 150.000 EUR.
- Sperrfristen § 6 DüV — Stickstoff- und Phosphathaltige Düngemittel nur in bestimmten Zeiträumen.
- Ausbringungsobergrenzen 170 kg N/ha pro Jahr aus organischem Dünger § 6 Abs. 4 DüV.
- Stoffstrombilanz § 11a DüG — Pflicht je nach Betriebsgröße/Tierhaltung.
- Rote Gebiete § 13a DüV — verschärfte Auflagen (20% reduzierte N-Obergrenze, längere Sperrfristen).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Verfahrensrecht OWiG: Anhörung § 55 OWiG, Bußgeldbescheid § 65 OWiG, Einspruch § 67 OWiG.
- Verjährung § 31 OWiG: Ordnungswidrigkeiten bei Geldbußen über 15.000 EUR drei Jahre; sonst zwei Jahre.

## Beweislast und Frist

- Verwaltungsbehörde trägt Beweislast für objektiven und subjektiven Tatbestand (Vorsatz/Fahrlässigkeit § 10 OWiG).
- Betroffener trägt Vortragslast für Rechtfertigungs- und Entschuldigungsgründe (höhere Gewalt, Unzumutbarkeit).
- Einspruchsfrist § 67 OWiG: zwei Wochen ab Zustellung des Bußgeldbescheids — schriftlich oder zur Niederschrift bei der Verwaltungsbehörde.
- Verjährungshemmung durch Anhörung § 33 OWiG.

## Prüfschema

```
1. Tatbestand § 14 DueV identifizieren
2. Objektive Pflichtverletzung — Sperrfrist Obergrenze Ausbringtechnik
3. Subjektive Seite Vorsatz/Fahrlaessigkeit § 10 OWiG
4. Beweismittel der Behoerde (Kontrollprotokoll Proben GIS-Daten)
5. Rechtfertigungsgruende (hoehere Gewalt) und Entschuldigung
6. Rote-Gebiet-Lage § 13a DueV pruefen
7. Bussgeldhoehe verhaeltnismaessig § 17 OWiG
8. Einspruch § 67 OWiG fristwahrend
9. Verjaehrung § 31 OWiG kontrollieren
```

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Schreibvorlage Einspruch

```
An die [Landwirtschaftskammer / zustaendige Bussgeldbehoerde]

Az [...]

Einspruch gegen den Bussgeldbescheid vom [Datum] gemaess § 67 OWiG

Sehr geehrte Damen und Herren,

namens und in Vollmacht unserer Mandantschaft legen wir form- und
fristgerecht Einspruch ein gegen den o.g. Bussgeldbescheid.

Begruendung:

1. Sachverhalt:
Der Bescheid wirft unserer Mandantschaft vor am [Datum] auf der Flaeche
[Schlag-Nr Groesse] gegen § [Norm] DueV verstossen zu haben.

2. Verteidigung:
a) Objektiv: Die ausgebrachte Stickstoffmenge betraegt nach
   Aufzeichnungen [Wert] kg N/ha und damit unter der Obergrenze von
   170 kg N/ha § 6 Abs. 4 DueV. Die Berechnung der Behoerde beruht auf
   einer fehlerhaften Annahme zur Tierzahl (Anlage K1 HIT-Datenbank).
b) Sperrfrist § 6 Abs. 8 DueV: Die Ausbringung erfolgte am [Datum] —
   noch vor Beginn der Sperrfrist (Anlage K2 Wetter- und Bodendaten).
c) Subjektive Seite: Auch bei Annahme eines objektiven Verstosses fehlt
   es an Vorsatz oder Fahrlaessigkeit § 10 OWiG. Unsere Mandantschaft
   stuetzte sich auf die schriftliche Beratung des Pflanzenbauberaters
   vom [Datum] (Anlage K3).
d) Hoehere Gewalt: Aussergewoehnliche Witterung am [Zeitraum] machte
   ein vorgezogenes Ausbringen unaufschiebbar (Anlage K4 DWD-Daten).

3. Anregung:
Hilfsweise — sollte die Behoerde an einem Verstoss festhalten — bitten
wir um Reduzierung der Geldbusse auf das nach § 17 Abs. 3 OWiG
angemessene Mass unter Beruecksichtigung des erstmaligen Verstosses
und der fehlenden Bereicherung.

Wir bitten um Akteneinsicht § 49 OWiG.

Mit freundlichen Gruessen
```

## Übergabe

- Bei Aufrechterhaltung: Abgabe an Amtsgericht § 69 OWiG; Hauptverhandlung vorbereiten.
- Bei Vergleichsgespräch: dokumentierte Abrede zur Auflagenerfüllung.
- Künftige Compliance: Düngeplanung mit Stoffstrombilanz revisionssicher dokumentieren.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 14 DüV (Bußgeldtatbestände — Liste der Verstöße) → § 13a DüV (Rote Gebiete: 20%-Reduktion, verlängerte Sperrfristen) → § 11 DüG (Aufzeichnungspflicht) → § 11a DüG (Stoffstrombilanz) → § 31 OWiG (Verjährung: 3 Jahre bei Bußgeld über 15.000 EUR, 2 Jahre darunter) → § 17 OWiG (Zumessung, Verhältnismäßigkeit) → § 49 OWiG (Akteneinsicht)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `fachanwalt-agrarrecht-gap-direktzahlungen-antrag`

_Beratung zum Sammelantrag GAP-Direktzahlungen nach der GAP-Reform 2023. Konditionalitaet (GLOEZ-Standards) Oeko-Regelungen Junglandwirte-Praemie gekoppelte Stuetzung. Sanktionen bei Verstoessen Querprüfung HIT-Datenbank. Antragsfristen 15. Mai mit Verspaetungs-Aenderung. Workflow Vorprüfung Risiko-Check Antragstellung Einspruch._

# Sammelantrag GAP-Direktzahlungen

## Zweck

Beratung bei der Antragstellung für Direktzahlungen nach der GAP-Reform 2023 (VO (EU) 2021/2115; GAPDZG, GAPInVeKoSG). Prüfraster, Risiken, Fristen.

## 1) Eingangs-Abfrage

1. Welche Betriebsgroesse (ha) und Bewirtschaftungsform?
2. Welche Kulturen — Acker, Grünland, Sonderkulturen, Dauerkulturen?
3. Ist der Betrieb **Junglandwirt** (max. 40 Jahre, Hofübernahme < 5 Jahre)?
4. Sind **Oeko-Regelungen** (z.B. Vielfaeltige Kulturen, Bluehstreifen, Agroforst) geplant?
5. Vorjahres-Bescheid und Sanktionen?
6. Tierhaltung mit gekoppelter Stuetzung (Mutterkuh, Mutterschaf, Mutterziege)?

## 2) Konditionalitaet (GLOEZ-Standards)

Die Direktzahlung setzt Einhaltung der **9 GLOEZ-Standards** voraus (Anhang III GAP-DirektZV):

- **GLOEZ 1**: Erhaltung von Dauergrünland
- **GLOEZ 2**: Moorboeden / Feuchtgebiete-Schutz
- **GLOEZ 3**: Verbot Stoppelverbrennung
- **GLOEZ 4**: Gewaesserrandstreifen 3 m
- **GLOEZ 5**: Erosionsschutz Hanglagen
- **GLOEZ 6**: Mindestbodenbedeckung Winter
- **GLOEZ 7**: Fruchtwechsel (durch VO (EU) 2024/1468 — GAP-Vereinfachungsverordnung — geänderter Ausnahmekatalog ab Antragsjahr 2025)
- **GLOEZ 8**: Mindestanteil nicht-produktiver Flächen (durch GAP-Vereinfachungsverordnung 2024 abgesenkt/teilweise als Öko-Regelung in die freiwillige Förderung verschoben — länderspezifisch ab 2025)
- **GLOEZ 9**: Verbot Landschaftselement-Beseitigung

**Anpassungen ab Antragsjahr 2025/2026:** Umverteilungs-Mittel an die 2. Säule der GAP steigen stufenweise — 2025: 12,5 %, 2026: 15 %. Eco-Schemes wurden mit dem Antragsjahr 2025 vereinfacht; je Bundesland und Antragsjahr Einheitsbeträge (Bekanntmachung BMLEH vom 21.08.2025 für 2025). Verifikation der konkreten Einheitsbeträge im laufenden Mandat über [bmleh.de](https://www.bmleh.de/DE/themen/landwirtschaft/eu-agrarpolitik-und-foerderung/direktzahlung/direktzahlungen.html).

## 3) Antragsfristen und Präklusion

- **Hauptantrag**: 15. Mai des Antragsjahres
- **Verspätungs-Frist**: 9. Juni mit 1 % Abzug pro Werktag
- **Änderungs-Frist**: 30. September für Korrekturen
- **Höhere-Gewalt-Anzeige**: 15 Werktage nach Kenntnis

## 4) Sanktionen

| Verstoß | Folge |
|---|---|
| GLOEZ-Verstoß leichte Fahrlaessigkeit | 1-5 % Kürzung |
| GLOEZ-Verstoß grobe Fahrlaessigkeit | 5-15 % Kürzung |
| Vorsatz | 15-100 % Kürzung, Ausschluss |
| Falsche Flächen-Angabe | Differenz-Kürzung + Sanktion 0,75x bis 1,5x |
| Cross-Compliance-Verstoß | Stufenweise Kürzung |

## 5) Oeko-Regelungen (freiwillig, zusätzlich)

- **OEko-Regelung 1**: Vielfalt im Ackerbau (4-6 Kulturen)
- **OEko-Regelung 2**: Bluehstreifen
- **OEko-Regelung 3**: Belassen von Altgrasstreifen
- **OEko-Regelung 4**: Agroforst-Systeme
- **OEko-Regelung 5**: Extensivierung Dauergrünland
- **OEko-Regelung 6**: Bewirtschaftung Mooren
- **OEko-Regelung 7**: Bewirtschaftung Schutzgebieten

Praemien je Hektar variabel; Antrag mit Auswahl OEko-Regelung.

## 6) Querprüfung mit HIT-Datenbank

Bei Tierhaltungs-Praemien: HIT-Datenbank (Herkunfts- und Informationssystem Tier) muss vor Antragstellung aktualisiert sein. Differenzen führen zu Kürzungen.

## 7) Workflow

### Schritt 1 — Vorprüfung

- Vorjahres-Bescheid lesen, Auflagen identifizieren
- Risikobereiche (GLOEZ 7 Fruchtwechsel, GLOEZ 8 4 %-Regel) eruieren
- Bei Junglandwirt: Hofübernahme-Dokumente bereithalten

### Schritt 2 — Antragstellung

- Online über das jeweilige Land (z.B. AAA in BW, iBALIS in BY, INVEKOS-Online in NRW)
- Sammelantrag mit Flächen-Skizze
- OEko-Regelungen separat ankreuzen

### Schritt 3 — Bescheid-Prüfung

- Bei Kürzung: **Widerspruch binnen 1 Monat** (§ 70 VwGO iVm Landes-AusfG)
- Bei groberen Sanktionen: anwaltliche Prüfung der Verschuldensbeurteilung

## 8) Typische Mandats-Konstellationen

- **Flächendifferenz**: Vor-Ort-Kontrolle ergibt 0,7 ha weniger als beantragt — Quotenkürzung droht
- **GLOEZ-Verstoß**: Lkw fährt durch Gewaesserrandstreifen — Sanktion 5-15 %
- **Junglandwirt-Praemie versagt**: Behörde erkennt Hofübernahme nicht an — Widerspruch mit Notar-Urkunde
- **Oeko-Regelung-Anerkennung verweigert**: Bluehstreifen zu schmal — Kompromiss-Verhandlung

## 9) Honorar-Hinweis

Bei laufender Antragsbegleitung: Rahmenvereinbarung empfohlen. Bei Widerspruch / Klage: Streitwert nach Differenzbetrag (entgangene Direktzahlung). RVG-Honorare nach Streitwert berechnet.

## Anschluss

- `fachanwalt-agrarrecht-orientierung` — Triage Mandatsarten
- `fachanwalt-agrarrecht-pachtvertrag-streitig` — bei Pacht-Konflikten
- `landpacht-und-hoferbfolge-pruefen` — bei Generationenwechsel

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

VO (EU) 2021/2115 Art. 14-17 (GLÖZ-Standards, Konditionalität) → VO (EU) 2021/2116 Art. 84-87 (Sanktionen) → Art. 3 VO (EU) 2021/2116 (höhere Gewalt) → GAPDirektZahlV (deutsches Durchführungsrecht) → § 70 VwGO (Widerspruchsfrist) → § 80 Abs. 5 VwGO (einstweiliger Rechtsschutz bei Rückforderung)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

