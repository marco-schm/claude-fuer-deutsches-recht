# Megaprompt: fachanwalt-handels-gesellschaftsrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 94 Skills des Plugins `fachanwalt-handels-gesellschaftsrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Anwalts-Dashboard Fachanwalt Handels- und Gesellschaftsrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfris…
2. **fachanwalt-handels-gesellschaftsrecht-orientierung** — Einstieg in den Skill-Verbund Handels- und Gesellschaftsrecht. FAO § 14i Voraussetzungen 80 Faelle davon 40 rechtsfoerml…
3. **erstgespraech-mandatsannahme** — Strukturierter Erstgespraechsleitfaden für Handels- und Gesellschaftsrecht: Erfassung der Konstellation, Konflikt- und G…
4. **erstpruefung-und-mandatsziel** — Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit…
5. **fachanwalt-handels-gesellschaftsrecht-squeeze-out-verfahren** — Mehrheitsaktionaer will Minderheitsaktionaere aus AG herausdrangen oder Minderheitsaktionaer wird herausgedraengt. Squee…
6. **fachanwalt-handels-gesellschaftsrecht-ma-due-diligence-findings** — Anwalt hat Datensichtung abgeschlossen und muss Due-Diligence-Bericht für M&A-Transaktion strukturieren. M&A Due Diligen…
7. **fachanwalt-hgr-dis-schiedsverfahren-streit** — Gesellschafter streiten und wollen Schiedsverfahren statt Klage oder laufendes Schiedsverfahren managen. DIS-Schiedsverf…
8. **fachanwalt-handels-gesellschaftsrecht-holding-strukturplanung** — Holding-Strukturplanung: § 8b KStG Schachtelprivileg (95 % steuerfreier Exit), Varianten Einzel-Holding, Vermögens-Holdi…
9. **fachanwalt-hgr-dlt-pilotregime-token** — EU-DLT-Pilotregime VO 2022/858 (anwendbar 23.3.2023, verlängert voraussichtlich bis 23.3.2029) für DLT-basierte Wertpapi…
10. **output-waehlen** — Output-Wahl für Fachanwalt Handels- und Gesellschaftsrecht: stimmt Adressat (Gesellschafter/Aktionäre, Vorstand/Geschäft…

---

## Skill: `einstieg-routing`

_Anwalts-Dashboard Fachanwalt Handels- und Gesellschaftsrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt bleibt im Driver Seat._

# Anwalts-Dashboard Fachanwalt Handels- und Gesellschaftsrecht

> Gesellschafterstreit, Geschäftsführerhaftung, Anfechtungsklage, M&A, Handelsvertreterausgleich — Beteiligungsverhältnisse und Beschlüsse zuerst klären.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 246 AktG: 1 Monat** Anfechtungsklage Hauptversammlungsbeschluss. § 256 AktG (Nichtigkeitsklage). GmbH-Beschlüsse: analog 1 Monat (h. M., kein gesetzlicher Frist, vertragliche Regelungen prüfen). § 89b HGB: Ausgleichsanspruch Handelsvertreter 1 Jahr nach Ende. § 161 II AktG: Erklärung Corporate Governance jährlich. | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Anfechtung Beschluss § 243 AktG · Nichtigkeit § 241 AktG · GF-Haftung §§ 43 GmbHG, 93 AktG · Treuepflicht (st. Rspr.) · Wettbewerbsverbot § 88 AktG · Auskunft § 51a GmbHG · Handelsvertreterausgleich § 89b HGB · Einsicht Kommanditist § 166 HGB. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | LG Kammer für Handelssachen (§§ 95, 96 GVG) — auf Antrag (§ 98 GVG). Schiedsklauseln verbreitet → vorab Schiedsvereinbarung prüfen (§ 1029 ZPO). | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Anfechtungsklage Hauptversammlungsbeschluss § 246 AktG (1 Monat ab Beschlussfassung). 🟠 Ausgleichsanspruch HV § 89b III HGB Geltendmachung 1 Jahr nach Vertragsbeendigung.
- **Beweislage:** 🟠 Beschlussfassung: Protokoll, Versammlungsleitung, Beschlussverfahren. 🔴 GF-Haftung: Geschäftsvorfall, Vorteilsabsicht, Kausalität — Buchhaltung sichern.
- **Wirtschaftlich:** 🔴 Insolvenzantragspflicht § 15a InsO (3 Wochen ab Eintritt Zahlungsunfähigkeit) — parallel zur Geschäftsführerhaftung mitdenken. 🟠 M&A: Due-Diligence-Findings als Verhandlungsmasse.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Geschäftsführerhaftung im Raum** | `gmbh-gf-haftung-paragraf-43-gmbhg` | Pflichtverstoß, Schaden, Verschulden, Entlastung § 46 Nr. 5 GmbHG |
| Hauptversammlungsbeschluss anfechten | `aktionaersklage-anfechtung-paragraf-243-aktg` | 1-Monatsfrist § 246 AktG, Anfechtungsbefugnis |
| Gesellschafterstreit GmbH | `gesellschafterstreit` | Ausschluss, Einziehung, Treuepflichtklage |
| Handelsvertreterausgleich § 89b HGB | `handelsvertreterausgleich` | Voraussetzungen, Berechnung, Geltendmachungs-Frist |
| M&A Due-Diligence Befunde | `ma-due-diligence-findings` | Risikoclustering, SPA-Anpassungen, Earn-out-/MAC-Klauseln |

## Norm-Radar (live verifizieren)

- **§ 243 AktG** — Anfechtbarkeit Hauptversammlungsbeschluss
- **§ 246 AktG** — 1-Monatsfrist Anfechtungsklage
- **§ 43 GmbHG** — Geschäftsführerhaftung
- **§ 51a GmbHG** — Auskunftsrecht des GmbH-Gesellschafters
- **§ 89b HGB** — Handelsvertreterausgleich
- **§ 15a InsO** — Insolvenzantragspflicht

## Genau eine Rückfrage (nur wenn nötig)

> Steht ein **Beschluss zur Anfechtung** im Raum, **Haftung eines Organs** oder ein **Vertragsstreit** (Handelsvertreter, M&A) im Vordergrund?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **GmbH-Geschäftsführerhaftung § 43 GmbHG; Business Judgement Rule** — BGH II. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Hauptversammlungsbeschluss-Anfechtung § 243 AktG; 1-Monats-Frist § 246 AktG** — BGH II. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Handelsvertreterausgleich § 89b HGB; Berechnung** — BGH VII./VIII. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Grenzüberschreitender Formwechsel** — EuGH C-106/16 (Polbud, 25.10.2017) — *live verifizieren auf* `curia.europa.eu`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

---

## Skill: `fachanwalt-handels-gesellschaftsrecht-orientierung`

_Einstieg in den Skill-Verbund Handels- und Gesellschaftsrecht. FAO § 14i Voraussetzungen 80 Faelle davon 40 rechtsfoermlich. HGB AktG GmbHG PartGG UmwG MoPeG. Typische Mandate Gründung Satzungsaenderung Geschäftsführerhaftung M&A Beschlussanfechtung Umwandlung. verifizierbare Quellen; Literatur nur bei Nutzerquelle oder lizenziertem Live-Zugriff. Output: Routing zu Folge-Skill. Abgrenzung zu fachanwalt-handels-gesellschaftsrecht-gesellschafterstreit (Streit) und fachanwalt-handels-gesellschaftsrecht-orientierung._

# Orientierung Handels- und Gesellschaftsrecht

## Kaltstart-Rückfragen

1. Welche Rechtsform (Einzelkaufmann, OHG, KG, GmbH, AG, GmbH Co. KG, GbR nach MoPeG, eG)?
2. Mandantenrolle: Gesellschafter, Geschäftsführer, Vorstand, Aufsichtsrat, Gesellschaft, Aktionär, Anteilskäufer?
3. Worum geht es: Gründung, Strukturmaßnahme (Umwandlung, M&A), Streit unter Gesellschaftern, Haftung Organperson, Handelsrecht (Handelsvertreter, Kaufmannsgeschäfte)?
4. Bestehen Satzung, Gesellschaftsvertrag, Geschäftsordnung Vorstand/Aufsichtsrat, Anstellungsverträge?
5. Liegt aktuelle Frist (Anfechtungsklage AktG vier Wochen § 246; GmbH analog regelmäßig einen Monat, Einzelfall)?
6. Krisensituation: drohende Zahlungsunfähigkeit § 18 InsO, Antragspflicht § 15a InsO?

## FAO § 14i — Voraussetzungen

- **Theoretischer Lehrgang:** 120 Zeitstunden Handels- und Gesellschaftsrecht (FAO § 4).
- **Praktischer Nachweis:** 80 Fälle in den letzten drei Jahren, davon mindestens 40 rechtsförmlich; verteilt auf die Bereiche Handelsrecht, Kapitalgesellschaftsrecht, Personengesellschaftsrecht, Umwandlungsrecht und Konzernrecht (§ 5 Abs. 1 lit. j FAO).
- **Bereiche § 14i FAO:** HGB Handelsstand, Handelsgeschäfte, Handelskauf; Kapitalgesellschaftsrecht (GmbHG, AktG); Personengesellschaftsrecht (OHG, KG, GbR/MoPeG); Konzernrecht; Umwandlungsrecht (UmwG); kapitalmarktrechtliche Bezüge.

## Maßgebliche Normen

- **HGB:** Kaufmannsbegriff §§ 1 ff.; Firmenrecht §§ 17 ff.; Prokura §§ 48 ff.; Handelsregister § 8 ff. iVm FamFG; Handelsgeschaefte §§ 343 ff.; Handelsvertreterrecht §§ 84 ff.; Bilanzrecht §§ 238 ff. Seit MoPeG (01.01.2024) gilt fuer OHG/KG das neue Beschlussmaengelrecht §§ 110-115 HGB (Anfechtungsmodell, Frist drei Monate, Klage gegen die Gesellschaft).
- **GmbHG:** Gruendung §§ 1 ff., Stammkapital § 5, Geschaeftsfuehrerpflichten §§ 35 ff., Geschaeftsfuehrerhaftung § 43, Gesellschafterversammlung §§ 47 ff., Anteilsabtretung § 15. Online-Beurkundung Gruendung seit DiRUG (01.08.2022), erweitert auf Kapitalerhoehung und Satzungsaenderungen seit DiREG (01.08.2023; nur bei einstimmigem Beschluss). § 16a BeurkG.
- **AktG:** Gruendung §§ 1 ff., Hauptversammlung §§ 118 ff. (virtuelle HV § 118a AktG nach G v. 20.07.2022), Beschlussanfechtung §§ 241 ff., Vorstandshaftung § 93 AktG, Aufsichtsrat §§ 95 ff.
- **PartGG** und **MoPeG-GbR-Recht** (Gesetz zur Modernisierung des Personengesellschaftsrechts; BGBl. I 2021, 3436; in Kraft 01.01.2024) mit eGbR-Registereintragung (§§ 707 ff. BGB); Voreintragungspflicht bei Grundstuecksgeschaeften nach § 707b BGB bestaetigt durch BGH, Beschl. v. 03.07.2025 — V ZB 17/24.
- **UmwG:** Verschmelzung §§ 2 ff., Spaltung §§ 123 ff., Formwechsel §§ 190 ff.; UmRUG (Umwandlungsrichtlinie-Umsetzungsgesetz, in Kraft 01.03.2023) — grenzueberschreitende Umwandlungen jetzt mit harmonisierten Verfahren.
- **InsO Schnittstellen:** § 15a InsO (Antragspflicht, Hoechstfristen 3 Wochen ZU / 6 Wochen UE); § 15b InsO Zahlungsverbot ab Insolvenzreife (§ 64 GmbHG a.F. und § 92 II AktG a.F. aufgehoben durch SanInsFoG vom 22.12.2020, BGBl. I 2020, 3256, in Kraft 01.01.2021; rechtsformneutral ersetzt durch § 15b InsO).

## Typische Mandate

- Gründungs- und Satzungsberatung; Notarvorbereitung.
- M&A: Share Deal (SPA), Asset Deal, Due Diligence, Garantien.
- Anteilsabtretung GmbH § 15 Abs. 3 GmbHG; Vinkulierung Aktien § 68 Abs. 2 AktG.
- Beschlussanfechtung HV / Gesellschafterversammlung.
- Geschäftsführerhaftung §§ 43 GmbHG, 93 AktG.
- Restrukturierung, Umwandlung, Spaltung.
- Streit zwischen Gesellschaftern (Hinauskündigungsklauseln, Abfindung).
- Handelsvertreterausgleich § 89b HGB.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Maßgebliche Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Übergabe

- Bei Krisenfällen Schnittstelle zum Plugin `insolvenzrecht` und zu `fachanwalt-insolvenz-sanierungsrecht`.
- Bei steuerlichen Bezügen (Organschaft, Verschmelzung steuerneutral § 11 UmwStG) Schnittstelle zum Plugin `steuerrecht-anwalt-und-berater` und `steuerrecht-anwalt-und-berater`.
- Bei IP-Beziehungen (Markenübertragung, Lizenz im Joint Venture) Schnittstelle zum Plugin `fachanwalt-gewerblicher-rechtsschutz`.
- Zitierweise nach `zitierweise-deutsches-recht` v3.0 (Az.-Marker, BGH-Pinpoint mit Rn., Hierarchie BGH vor OLG vor LG).

## Vertiefung — Ergänzende Rechtsprechung 2020-2024

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Ergänzende Literatur

- K. Schmidt, Gesellschaftsrecht, 5. Aufl. 2021: MoPeG-Neukommentierung GbR-Recht ab 2024; Vergleich Personengesellschaft/Kapitalgesellschaft.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

---

## Skill: `erstgespraech-mandatsannahme`

_Strukturierter Erstgespraechsleitfaden für Handels- und Gesellschaftsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen: Strukturierter Erstgespraechsleitfaden..._

# Strukturierter Erstgespraechsleitfaden für Handels- und Gesellschaftsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: HGB §§ 1-7, 17-37 (Firma/Register), 48-58 (Prokura), 84-92c (Handelsvertreter), 343 ff. (Handelsgeschäfte), 373 ff. (Handelskauf); HGB §§ 84-92c, EuGH zu Ausgleichsanspruch, BGB §§ 305 ff.; § 14i. HGB. AktG. GmbHG. PartGG. UmwG. Geschäftsführerhaftung; § 89b HGB. MoPeG GbR seit 2024. Schnittstellen kanzlei-allgemein — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierter Erstgespraechsleitfaden für Handels- und Gesellschaftsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.

### Erstgespraech und Mandatsannahme im Handels- und Gesellschaftsrecht

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erstgespraech und Mandatsannahme im Handels- und Gesellschaftsrecht` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Handels- und Gesellschaftsrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klären, Konflikt- und GwG-Prüfung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Handels- und Gesellschaftsrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klägerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Gruendung, Anteilsuebertragung, Gesellschafterstreit, GF-Haftung, M&A
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Anfechtungs-/Nichtigkeitsklage GV-Beschluss, Auskunftsklage, Squeeze-out). Frist-Alarm an die Vorbereitung weitergeben.

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

Standard-Streitwerte im Bereich Handels- und Gesellschaftsrecht:

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

- BORA, BRAO, FAO für Fachanwaltschaft Handels- und Gesellschaftsrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- HGB, GmbHG, AktG, UmwG, GenG, GwG (für fachliche Erstpruefung).
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

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Handels- und Gesellschaftsrecht). Handlungs-Sequenz:

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
- Verfahrensdauer im Bereich Handels- und Gesellschaftsrecht: Erfahrungswerte nach Instanz.
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

## Vertiefung — Normenkette und Rechtsprechung Erstgespräch HGR

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normenkette Erstgespräch HGR

§ 246 AktG (Monatsfrist Anfechtungsklage AG) → § 47 GmbHG (analoge Anfechtungsfrist GmbH) → § 15 GmbHG (Anteilsabtretung notariell) → §§ 43a, 45 BRAO (Interessenkonflikt bei GmbH-Gesellschaft + GF) → §§ 3, 3a RVG (Honorarvereinbarung) → §§ 10, 11 GwG (GwG-Pflichten bei GmbH/AG-Mandaten) → § 15a InsO (Insolvenzantragspflicht — im Erstgespräch auf Krisensignale prüfen)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `erstpruefung-und-mandatsziel`

_Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzb..._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: HGB §§ 1-7, 17-37 (Firma/Register), 48-58 (Prokura), 84-92c (Handelsvertreter), 343 ff. (Handelsgeschäfte), 373 ff. (Handelskauf); HGB §§ 84-92c, EuGH zu Ausgleichsanspruch, BGB §§ 305 ff.; § 14i. HGB. AktG. GmbHG. PartGG. UmwG. Geschäftsführerhaftung; § 89b HGB. MoPeG GbR seit 2024. Schnittstellen kanzlei-allgemein — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Handels- und Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (HGB/GmbHG/AktG/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

### Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** FAO, HGB, AktG, GmbHG, PartGG, UmwG, MoPeG.

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

## Skill: `fachanwalt-handels-gesellschaftsrecht-squeeze-out-verfahren`

_Mehrheitsaktionaer will Minderheitsaktionaere aus AG herausdrangen oder Minderheitsaktionaer wird herausgedraengt. Squeeze-out §§ 327a ff. AktG. Prüfraster: 95-Prozent-Schwelle Barabfindung gerichtliche Festsetzung. WpUG-Squeeze-out nach Übernahmeangebot. Verschmelzungs-Squeeze-out § 62 Abs. 5 UmwG. Spruchverfahren SpruchG. Output: Ablaufplan und Schriftsatzvorlagen Squeeze-out und Spruchverfahren. Abgrenzung zu fachanwalt-handels-gesellschaftsrecht-gesellschafterstreit (GmbH-Streit) und fachanwalt-hgr-dis-schiedsverfahren-streit._

# Squeeze-out Verfahren

## Zweck

Bei AG: Ausschluss Minderheits-Aktionaere durch Hauptaktionaer mit > 95 % der Anteile gegen Barabfindung.

## 1) Drei Varianten

### 1. Aktienrechtlicher Squeeze-out §§ 327a ff. AktG

- 95 % der Stimmrechte des Hauptaktionaers
- Hauptversammlungs-Beschluss mit einfacher Mehrheit
- Eintragung HR, dann Aktienübergang an Hauptaktionaer
- Barabfindung gerichtlich kontrollierbar (Spruchverfahren)

### 2. WpUG-Squeeze-out §§ 39a-c WpUG

- Nach erfolgreichem UEbernahmeangebot
- Schwelle: 95 % des stimmberechtigten Kapitals
- 3-Monats-Frist nach Ende Annahmefrist
- Antrag beim LG (Landgericht des Sitzes der Ziel-Gesellschaft)

### 3. Verschmelzungs-Squeeze-out § 62 V UmwG

- Bei konzerninterner Verschmelzung
- Schwellenwert 90 %
- Schneller als § 327a AktG

## 2) Eingangs-Abfrage

1. Welche Variante (Aktien-, WpUG-, Verschmelzungs-)?
2. Aktuelle Beteiligungs-Höhe Hauptaktionaer?
3. Streubesitz-Aktionaere (Anzahl)?
4. Ziel-Gesellschaft börsennotiert?
5. Eigene Stellung — Hauptaktionaer oder Minderheits-Aktionaer?

## 3) Verfahren § 327a-f AktG

### Schritt 1 — Verlangen § 327a AktG

- Hauptaktionaer mit 95 % verlangt Ausschluss
- Mit Bewertungs-Gutachten und Barabfindungs-Angebot

### Schritt 2 — Vorbereitung HV

- Prüfer bestellt durch LG
- Pruefbericht mit Bewertung
- Prüfer prüft Angemessenheit der Abfindung

### Schritt 3 — Hauptversammlung

- Beschluss mit **einfacher Mehrheit** des vertretenen Kapitals
- Tagesordnung mit Squeeze-out-Punkt
- Beschluss-Protokoll notariell

### Schritt 4 — Eintragung HR

- Anfechtungsfrist 1 Monat
- Bei Anfechtungs-Klage: Freigabeverfahren § 327e III AktG möglich

### Schritt 5 — Aktien-Übergang

- Mit Eintragung im HR
- Hauptaktionaer wird Allein-Aktionaer
- Minderheits-Aktionaere erhalten Barabfindung

## 4) Barabfindung — Bewertung

### Bewertungsgrundlage IDW S 1

- Ertragswert-Methode Standard
- Multiplikator-Methode subsidiaer
- Borsenkurs als Untergrenze (BVerfG DAT/Altana; BGH Stollwerck)

### Prüfer-Bericht

- Gerichtlich bestellter Prüfer
- Prüfung der Angemessenheit
- Bei Streit: Stellungnahme

## 5) Spruchverfahren SpruchG

### Antragsfrist

- 3 Monate ab Eintragung im HR

### Verfahren

- LG (Landgericht) am Sitz der Gesellschaft
- Spezialisierte Kammer (Handelskammer)
- Sachverständige Bewertung
- Verfahren kann **mehrere Jahre** dauern

### Kostenrisiko

- Bei Erfolg: Gesellschaft traegt Kosten
- Bei Misserfolg: Antragsteller-Anteil

### Erhöhung

- Bei nachgewiesen niedriger Erstabfindung: Aufschlag (typisch 10-30 %)
- Verzinsung gemäß § 305 III AktG

## 6) Anfechtungsklage

### Grunde

- Verfahrensfehler bei HV
- Fehlerhafte Bewertung
- Sittenwidrigkeit § 138 BGB
- Bewertungs-Prüfer-Mangel

### Risiken Anfechtungs-Klage

- Klage hemmt Eintragung HR (Klagewirkung)
- Bei missbraeuchlicher Klage: Schadensersatz Gesellschaft
- Freigabeverfahren § 327e III AktG: Anfechtung wird außer Wirksam gestellt

## 7) Freigabeverfahren

### Antragsberechtigung

- Gesellschaft, Hauptaktionaer

### Voraussetzung

- Klage erscheint offensichtlich unbegründet
- Wirtschaftliche Schäden bei Verzoegerung überwiegen

### Folge

- Eintragung HR trotz Klage
- Klage wird in Schadensersatz umgewandelt

## 8) Hauptaktionaers-Strategie

### Vorbereitung

- Bewertungs-Gutachten früh
- Prüfer-Auswahl (BGH-Linie zu Unabhängigkeit)
- HV-Vorbereitung sorgfaeltig

### Risikomanagement

- Freigabe-Antrag bei Anfechtungsklage
- Vergleichs-Bereitschaft bei "Beruhms-Kläger"-Konstellation

## 9) Minderheits-Aktionaers-Strategie

### Defensive Position

- Prüfer-Bericht kritisch würdigen
- Eigene Bewertung einholen
- Spruchverfahren-Antrag binnen 3 Monaten

### Offensive Position (selten)

- Anfechtungsklage bei Verfahrensfehlern
- Risiko: Freigabe-Antrag und Verlust

## 10) Typische Fehler

1. **Prüfer-Auswahl mangelhaft** — Bewertung anfechtbar
2. **Spruchverfahrens-Frist 3 Monate verpasst** — keine Erhöhung
3. **Anfechtungs-Klage als Druckmittel** missbraucht — Schadensersatz-Risiko
4. **Borsenkurs als Untergrenze ignoriert** — BGH-Linie
5. **Freigabeverfahren versäumt** Hauptaktionaer — Verzoegerung

## 11) BGH-Linien

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Anschluss

- `fachanwalt-handels-gesellschaftsrecht-ma-due-diligence-findings` — bei verbundener M&A
- `corporate-kanzlei` — bei voll-Big-Law-Mandat
- `gesellschaftsgruender-gesellschafterstreit-eilantraege` — bei Verfahrens-Streit

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Paragrafenkette

§§ 327a-f AktG (Squeeze-out Verfahren) → §§ 39a-c WpUG (WpUG-Squeeze-out) → § 62 Abs. 5 UmwG (Verschmelzungs-Squeeze-out) → SpruchG (Spruchverfahren Barabfindung) → § 246 AktG (Anfechtungsklage 1-Monat-Frist) → § 246a AktG (Freigabeverfahren) → IDW S 1 (Bewertungsstandard Ertragswert) → Art. 14 GG (Eigentumsgarantie, verfassungskonforme Barabfindung)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

### Normquellen und offene Datenbankverweise

- §§ 327a-f AktG: https://www.gesetze-im-internet.de/aktg/__327a.html
- §§ 39a-c WpUG: https://www.gesetze-im-internet.de/wp_g/__39a.html
- § 62 V UmwG: https://www.gesetze-im-internet.de/umwg_1995/__62.html
- SpruchG: https://www.gesetze-im-internet.de/spruchg/
- Aktuelle Squeeze-out-Spruchverfahrens-Linie (Fundstellen vor Verwendung live pruefen): https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Schlagwort=Squeeze-out — keine Aktenzeichen aus Modellwissen.
- BVerfG DAT/Altana (Beschl. v. 27.04.1999 — 1 BvR 1613/94; BVerfGE 100, 289 — Boersenkurs als grundsaetzliche Untergrenze der Abfindung ausscheidender Aktionaere; Art. 14 GG): https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/DE/1999/04/rs19990427_1bvr161394.html
## Triage — Sofortprüfung Squeeze-out

1. **Beteiligungsschwelle prüfen:** > 95 % (§ 327a AktG oder WpUG § 39a) oder > 90 % (UmwG § 62)?
2. **Rolle des Mandanten:** Hauptaktionär (Verfahren einleiten) oder Minderheitsaktionär (Anfechtung + Spruchverfahren)?
3. **Anfechtungsklage (Minderheitsaktionär):** 1-Monat-Frist § 246 AktG ab Beschlussfassung; Freigabeverfahren § 246a AktG durch Hauptaktionär?
4. **Spruchverfahren:** Angemessenheit der Barabfindung; Börsenkurs vs. Ertragswert IDW S 1; Gutachter im Verfahren.
5. **Freigabeverfahren:** Interessenabwägung; Vollziehungsinteresse des Hauptaktionärs vs. Verlustrisiko Minderheitsaktionäre.

---

## Skill: `fachanwalt-handels-gesellschaftsrecht-ma-due-diligence-findings`

_Anwalt hat Datensichtung abgeschlossen und muss Due-Diligence-Bericht für M&A-Transaktion strukturieren. M&A Due Diligence Report Legal Tax Commercial. Prüfraster: Red Flags Yellow Flags Green Findings strukturiert Risikobewertung Materialitaet aufschiebende Bedingungen Garantien Kaufpreisanpassung Disclosure Schedules. Output: Findings-Report Risikomatrix. Abgrenzung zu fachanwalt-handels-gesellschaftsrecht-holding-strukturplanung (Strukturierung) und vergleichsverhandlung-strategie._

# M&A Due Diligence Findings

## Zweck

Strukturierte Erfassung von DD-Befunden, Bewertung und Auswirkung auf Kaufvertrag (SPA), Garantien, Kaufpreis-Anpassung.

## 1) Eingangs-Abfrage

1. Deal-Phase: vor Letter of Intent, vor LOI, nach LOI?
2. Deal-Volumen?
3. Zielunternehmen-Branche und Komplexitaet?
4. Eigene Rolle: Kaeufer-Beratung oder Verkaeufer-Beratung?
5. Bisheriger Datenraum (VDR)-Zugang?

## 2) DD-Bereiche

| Bereich | Schwerpunkt |
|---|---|
| Legal | Verträge, Litigation, Compliance, Korruption, GwG, KartellR |
| Tax | Steuerliche Risiken, Verlustvortraege, Verrechnungspreise, Steuerstrafrecht |
| Commercial | Markt-Position, Kunden-Konzentration, Wettbewerb |
| Financial | Bilanz, GuV, Cash-Flow, EBITDA-Adjustments |
| Operational | Lieferketten, IT, HR, Compliance |
| Environmental | Altlasten, Umweltauflagen |

## 3) Findings-Klassifizierung

### Red Flag

- Deal-killer
- Beispiel: laufende Strafverfolgung des CEO wegen Korruption
- Beispiel: ausstehende Verkaeufer-Eigentums-Streitigkeit

### Yellow Flag

- Materielle, aber loesbare Risiken
- Beispiel: laufende ungeklärte Steuerprüfung
- Beispiel: Bestehender Kündigungsschutz-Prozess wesentlicher MA

### Green Flag

- Üblich-akzeptables Risiko
- Beispiel: kleinere Marken-Klagen
- Beispiel: routinemaessige Steuer-Veranlagungen

## 4) Materialitaets-Schwellen

### Vertraglich definiert

- Kaufpreis-Anpassungs-Schwelle (typisch 1-3 % des EV)
- Garantie-Auszahlungs-Schwelle (de minimis 50-200 K)
- Cap-Limit Garantie (typisch 10-30 % Kaufpreis)

### Praxis

- Single-Item-Threshold
- Aggregations-Threshold
- Cap (Maximum-Haftung)

## 5) Verkaeufer-Auskunft (Disclosure)

### Disclosure Schedules

- Anhaenge zum SPA mit konkreten Ausnahmen
- Bekannte Risiken offenbart
- Was offenbart ist, ist nicht garantiebewehrt

### Disclosure Letter

- Allgemeine Disclosure mit Verweis auf VDR-Inhalt
- BGH-Linie zur Auskunfts-Reichweite

### Vorsicht bei Knowledge-Qualifiers

- "To the seller's knowledge" — limitiert Garantie
- "Material" qualifier — Schwellen-Frage

## 6) Workflow

### Phase 1 — VDR-Strukturierung

- Indexierung
- Prüf-Listen je Bereich
- Q&A-Liste

### Phase 2 — Findings-Erfassung

- Excel-Master-Liste mit:
  - Bereich, Subbereich
  - Finding-Beschreibung
  - Klassifizierung (Red/Yellow/Green)
  - Materialitaet (EUR-Wert oder %-Auswirkung)
  - Lösungs-Vorschlag

### Phase 3 — Risiko-Matrix

- Wahrscheinlichkeit (Niedrig/Mittel/Hoch)
- Auswirkung (Niedrig/Mittel/Hoch)
- Risk-Score

### Phase 4 — Kaufvertrags-Konsequenzen

- Aufschiebende Bedingung (Condition Precedent)
- Spezifische Garantie + Indemnity
- Kaufpreis-Reduzierung
- Escrow / Holdback

## 7) Aufschiebende Bedingungen (CPs)

### Typische CPs

- Kartellrechtliche Freigabe BKartA / EU-Kommission
- BaFin / Investitionsprüfung AWG
- Wesentliche Mitarbeiter-Zustimmung
- Drittpartei-Zustimmungen (Change-of-Control-Klauseln)
- Materielle Nicht-Veränderung (MAC-Klausel)

## 8) Garantien (Reps & Warranties)

### Standard-Garantien

- Eigentum am Aktiva
- Bilanz-Richtigkeit
- Steuer-Konformität
- Litigation
- Compliance
- IP
- Mitarbeiter
- Verträge

### Indemnities

- Spezifische Risiken (nicht durch Garantie gedeckt)
- Beispiel: Steuer-Risiko aus laufender Prüfung
- Beispiel: Umwelt-Altlasten-Sanierung

### Verzogenheit

- Verjaehrung Garantien: 18-36 Monate
- Steuer-Garantien: 7 Jahre (Steuerverjaehrung)

## 9) Kaufpreis-Anpassung

### Mechanismen

- Locked-Box-Mechanismus (fester KP zum Effective Date)
- Closing-Account-Mechanismus (Anpassung nach Closing-Bilanz)
- Earn-out (Erfolgsabhängig)

### Bei DD-Befunden

- Direct Reduction
- Escrow (Verkaeufer-Haftung)
- Spezial-Indemnity

## 10) Typische Fehler

1. **Findings nicht klassifiziert** — Risiko unentdeckt
2. **Materialitaet nicht beziffert** — Garantie-Schwellen nicht greifbar
3. **Knowledge-Qualifier ignoriert** — Verkaeufer entzieht sich Haftung
4. **CP-Erfüllung nicht überwacht** — Closing verschoben
5. **Verjaehrungs-Frist falsch verhandelt** — Garantie nicht greifbar

## 11) Reporting-Templates

### Executive Summary

- Top-5 Findings
- Deal-Empfehlung
- Wichtigste Verhandlungs-Punkte

### Detailed Findings Report

- Pro Bereich strukturiert
- Mit Begründung und Quellenangaben (VDR-Dok-Nummer)

## Anschluss

- `corporate-kanzlei` — Big-Law-Begleitung
- `gesellschaftsrecht/skills/dd-findings-extraktion` — bei reiner Befund-Extraktion
- `fachanwalt-handels-gesellschaftsrecht-holding-strukturplanung` — bei Strukturierung

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Paragrafenkette

§§ 311, 241 BGB (Garantien als eigenständige Haftungsversprechen) → § 442 BGB (Kenntnis des Käufers, Ausschluss Gewährleistung) → §§ 280, 281 BGB (Schadensersatz bei Garantieverletzung) → § 275 BGB (Unmöglichkeit bei MAC) → §§ 437, 439-441 BGB (Kaufrechtliche Gewährleistung — subsidiär bei Share Deal ohne Garantien) → § 123 BGB (Anfechtung wegen arglistiger Täuschung) → § 15 GmbHG (Anteilsabtretung, Formerfordernis) → §§ 17 ff. AktG (Aktienübertragung)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Fristen-Übersicht

| Situation | Frist | Norm |
|---|---|---|
| Anzeige Garantieverletzung (i.d.R. vertraglich) | laut SPA (typisch 30-90 Tage) | SPA-Klausel |
| Verjährung Garantieansprüche | laut SPA (typisch 12-36 Monate) | SPA-Klausel / § 195 BGB |
| Anfechtung wegen arglistiger Täuschung | 1 Jahr ab Kenntnis | § 124 BGB |
| MAC-Ausübung | vor Closing oder laut Vertragsklausel | SPA-MAC-Klausel |

## Triage — Sofortprüfung M&A Due Diligence

1. **Deal-Phase:** Pre-LOI (vertrauliche Erstinformation) → LOI (Exklusivität) → DD-Phase → SPA-Verhandlung → Signing → Closing?
2. **Eigene Rolle:** Käufer-Beratung (Red-Flag-Identifikation, Preisanpassung) oder Verkäufer-Beratung (Disclosure Schedule, Warranty & Indemnity Insurance)?
3. **Scope der DD:** Full DD (Legal/Tax/Financial/Commercial/Operational) oder nur Legal/Tax? Ressourcen anpassen.
4. **Red Flags identifizieren:** Laufende Rechtsstreitigkeiten, unbekannte Steuerschulden, fehlende Compliance-Dokumentation, Kartellverdacht, offene Behördenverfahren.
5. **Kaufpreisauswirkung:** Jeder Red Flag hat einen USD/EUR-Wert → Price Chip, Escrow, Earn-Out-Anpassung oder Kaufvertragsbedingung (Condition Precedent)?

**Entscheidungsbaum DD-Befund:**
```
Red Flag identifiziert?
├─ Hoch (Material): Closing-Bedingung oder Kaufpreisreduktion
│   ├─ Quantifizierbar → Spezifische Entschädigung (Indemnity) im SPA
│   └─ Nicht quantifizierbar → MAC-Klausel, Rücktrittsrecht verhandeln
├─ Mittel (Yellow): Garantie-Abdeckung im SPA ausreichend?
│   └─ W&I-Versicherung als Alternative prüfen
└─ Niedrig (Green): Nur in Protokoll; kein SPA-Einfluss
```

## Output-Template — DD-Befund (Red Flag)

```
DD-BEFUND [RED FLAG / YELLOW FLAG / GREEN]

Titel: [KURZTITEL, z.B. "Steuerprüfung 2021-2023 offen"]
Datum: [DATUM]
Erstellt von: [ANWALT/IN]
DD-Bereich: [LEGAL / TAX / FINANCIAL / COMMERCIAL]

SACHVERHALT
[Beschreibung des Befunds, Quelle (Dokument/Datenraum-Referenz)]

RECHTLICHE QUALIFIKATION
[Anwendbare Norm, Rechtsprechung, Risikobewertung]

QUANTIFIZIERUNG
Bestes Szenario:    EUR [MIN]
Realistisch:        EUR [REAL]
Schlimmstes Szenario: EUR [MAX]

EMPFEHLUNG
[ ] Closing-Bedingung (Condition Precedent)
[ ] Kaufpreisreduktion: EUR [BETRAG]
[ ] Spezifische Indemnity / Escrow-Betrag: EUR [BETRAG]
[ ] Garantie-Abdeckung im SPA
[ ] W&I-Versicherung

OFFENE PUNKTE
[Liste der noch benötigten Dokumente oder Klärungen]
```

<!-- AUDIT 27.05.2026 | Bundle 022 | Task 4
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Status: WRONG_TOPIC
Erdgaspreiserhöhungen (keine stillschweigende Zustimmung bei vorbehaltloser Zahlung,
§ 4 AVBGasV) – nichts mit M&A, Disclosure Schedules oder § 442 BGB zu tun.
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Maßnahme: Leitsatz-Zitat aus Abschnitt "Vertiefung – Aktuelle Rechtsprechung" gelöscht.
-->

---

## Skill: `fachanwalt-hgr-dis-schiedsverfahren-streit`

_Gesellschafter streiten und wollen Schiedsverfahren statt Klage oder laufendes Schiedsverfahren managen. DIS-Schiedsverfahren Gesellschafterstreit. Prüfraster: DIS-Schiedsordnung ICC HGB GmbH-Streit Squeeze-out-Verhandlung § 327a AktG M&A Earn-Out-Streitigkeiten DIS Expedited Rules. Output: Strategie-Memo Schiedsverfahren und Einleitungskorrespondenz. Abgrenzung zu fachanwalt-handels-gesellschaftsrecht-gesellschafterstreit (Staatsgericht-Klage) und vergleichsverhandlung-strategie._

# Gesellschafterstreit / DIS-Schiedsverfahren

## Zweck

Gesellschafterkonflikte (GmbH, AG, KG) lösen sich oft im Schiedsverfahren — DIS (Deutsche Institution für Schiedsgerichtsbarkeit), ICC, ad-hoc. Vorteil: vertraulich, Endgültigkeit, Spezialisten als Schiedsrichter. Nachteil: teuer. Vergleichsverhandlungen sind regelmäßig der eigentliche Lösungs-Pfad.

## Eingaben

- Streit-Konstellation (Mitgesellschafter, Mehrheits-/Minderheits)
- Streitgegenstand (Beschluss-Anfechtung, Gewinnverwendung, Geschäftsführung, Ausschluss)
- Schiedsklausel im Gesellschaftsvertrag (DIS-Standard?)
- Streitwert (typisch ab 500.000 EUR DIS sinnvoll)
- M&A-Klausel (Earn-Out, MAC, Reps & Warranties)

## Rechtlicher Rahmen

- **§§ 1025-1066 ZPO** — Schiedsgerichtsverfahren; siehe Modernisierungsvorhaben (BMJ-Referentenentwurf 01.02.2024, Diskontinuitaet Ende 20. WP, Stand pruefen): https://www.bmj.de/SharedDocs/Gesetzgebungsverfahren/DE/2023_Modernisierung_Schiedsverfahrensrecht.html
- **DIS-Schiedsgerichtsordnung 2018** (in Kraft seit 01.03.2018; weiterhin geltende Fassung): https://www.disarb.org/werkzeuge-und-tools/dis-regelwerke
- **DIS Ergaenzende Regeln fuer beschleunigte Schiedsverfahren** und DIS-Mediationsordnung 2020: https://www.disarb.org/werkzeuge-und-tools/dis-regelwerke
- **DIS-ERGeS** (Ergaenzende Regeln fuer gesellschaftsrechtliche Streitigkeiten 2018) — wichtig fuer Beschlussmaengelstreite in der Schiedsklausel.
- BGH-Linie zur Schiedsfaehigkeit von Beschlussmaengelstreitigkeiten (vor Verwendung gegen offene Quelle pruefen):
  - "Schiedsfaehigkeit II" — BGH, Urt. v. 06.04.2009 — II ZR 255/08 (GmbH; Mindestanforderungen): https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=06.04.2009&Aktenzeichen=II+ZR+255/08
  - "Schiedsfaehigkeit III" — BGH, Beschl. v. 06.04.2017 — I ZB 23/16: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Aktenzeichen=I+ZB+23/16
  - "Schiedsfaehigkeit IV" — BGH, Beschl. v. 23.09.2021 — I ZB 13/21 (Personenhandelsgesellschaft, Anpassungsbedarf Schiedsklauseln): https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=23.09.2021&Aktenzeichen=I+ZB+13/21
  - Folge: nach MoPeG/Beschlussmaengelrecht §§ 110 ff. HGB n.F. ggf. Anpassung von Schiedsklauseln in Personengesellschaftsvertraegen erforderlich.
- **ICC Rules 2021** (in Kraft seit 01.01.2021): https://iccwbo.org/dispute-resolution/dispute-resolution-services/arbitration/rules-procedure/2021-arbitration-rules/
- **§ 47 GmbHG** — Beschlussanfechtung (Frist 1 Monat): https://www.gesetze-im-internet.de/gmbhg/__47.html
- **§§ 110-115 HGB n.F. (MoPeG, in Kraft 01.01.2024)** — Beschlussmaengelrecht Personengesellschaften: https://www.gesetze-im-internet.de/hgb/__110.html
- **§§ 327a-f AktG** — Squeeze-Out (Spruchverfahren): https://www.gesetze-im-internet.de/aktg/__327a.html
- **§ 287 ZPO** — Schaetzungs-Befugnis bei Bewertungsstreit: https://www.gesetze-im-internet.de/zpo/__287.html
- **§ 273a ZPO n.F.** (Justizstandort-Staerkungsgesetz; in Kraft 01.04.2025) — prozessualer Geheimnisschutz auch in Schieds-Aufhebungs- und Vollstreckbarerklaerungsverfahren vor staatlichen Gerichten: https://www.gesetze-im-internet.de/zpo/__273a.html

## ADR-Pfade

### Pfad 1 — Direkt-Verhandlung Gesellschafter

- Bei kleineren Gesellschaftsformen (GmbH 2-4 Gesellschafter)
- Vorteil: Bewahrung Geschäftsbeziehung
- Anwaltlich begleitet, ohne Verbands-Beteiligung

### Pfad 2 — Mediation Gesellschafter-Streit

- DIS-Mediator/in
- Speziell bei familien-/freundes-basierten GmbH
- 5-15 Sitzungen
- Resultat: Auseinandersetzungs-Vereinbarung + Beteiligungs-Verkauf

### Pfad 3 — DIS Schiedsverfahren

- Schiedsklausel im Gesellschaftsvertrag oder ad-hoc-Vereinbarung
- Schiedsgericht 1-3 Schiedsrichter
- 12-18 Monate Dauer
- Endgültige Entscheidung

### Pfad 4 — DIS Expedited Rules

- Streitwert ≤ 1 Mio. EUR
- Vereinfacht
- 6 Monate Dauer

### Pfad 5 — Spruchverfahren bei Squeeze-Out

- Bewertungsstreit nach § 327f AktG
- LG-Spruchkammer
- Sachverständigen-Bewertung

## Workflow

### Phase 1 — Sachverhalts- und Klausel-Analyse

- Gesellschaftsvertrag-Prüfung (Schiedsklausel? DIS oder ICC?)
- Beschluss-Protokolle
- Geschäftsführungs-Konflikte dokumentiert?
- Wertentwicklung Beteiligung

### Phase 2 — Vorgerichtliche Strategie

- Anwalts-Schreiben mit Anspruchsbegründung
- Vergleichsangebot mit Optionen (Verkauf, Earn-Out, Sanierungs-Plan)
- Frist 30 Tage

### Phase 3 — Schiedsverfahrens-Einleitung

- DIS-Antrag (Online-Portal)
- Verfahrenseröffnung 14 Tage
- Schiedsrichter-Auswahl

### Phase 4 — Schiedsverfahren

- Schriftsatz-Wechsel
- Beweisaufnahme (Sachverständige Unternehmens-Bewertung)
- Anhörung
- Schiedsspruch

### Phase 5 — Vollstreckung

- Schiedsspruch vollstreckbar nach Anerkennung LG
- Bei Ausland: New Yorker Übereinkommen 1958

## Strategie und Taktik

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Vergleichs-Druck**: DIS-Schiedsrichter regen oft Vergleich an (50-60 % Vergleichs-Quote)
- **Bewertung Sachverständigen-Streit**: zwei Gutachter, dann Schiedsgutachter
- **Earn-Out-Klausel**: harte Definition KPIs zwingend; sonst typischer Konflikt-Anker
- **Squeeze-Out**: Spruchverfahren ist Standard; Vergleich oft 110-130 % der Abfindung

## Querverweise

- `fachanwalt-handels-gesellschaftsrecht-orientierung` — Triage
- `fachanwalt-handels-gesellschaftsrecht-squeeze-out-verfahren` — Spruchverfahren
- `fachanwalt-handels-gesellschaftsrecht-ma-due-diligence-findings` — M&A
- `fachanwalt-hgr-dlt-pilotregime-token` — Token-Aktien

## Quellen und Updates

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Paragrafenkette

§§ 1029-1066 ZPO (Schiedsgerichtsverfahren) → § 1059 ZPO (Aufhebung Schiedsspruch) → §§ 1060, 1061 ZPO (Vollstreckbarerklärung) → § 47 GmbHG (Beschlussanfechtung, Parallelverfahren) → § 246 AktG (Anfechtungsfrist) → DIS-Schiedsgerichtsordnung 2018 → DIS Expedited Rules 2021

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage — Sofortprüfung DIS-Schiedsverfahren

1. **Schiedsklausel prüfen:** Im Gesellschaftsvertrag vorhanden? DIS-Standard oder ad-hoc? DIS Expedited Rules?
2. **Streitwert:** Ab 500.000 EUR DIS sinnvoll; darunter eher ordentliches Gericht (Kosten-Nutzen-Abwägung).
3. **Verfahrenseinleitung:** Schiedsantrag nach DIS-Ordnung § 3 (Schiedsklage); Schiedsrichterbestellung (3 Schiedsrichter ab 1 Mio. EUR, 1 Einzelschiedsrichter darunter).
4. **Vollstreckung ausländischer Schiedssprüche:** New Yorker UN-Übereinkommen (UNÜ 1958) — 170 Vertragsstaaten; Vollstreckbarerklärung § 1061 ZPO.

---

## Skill: `fachanwalt-handels-gesellschaftsrecht-holding-strukturplanung`

_Holding-Strukturplanung: § 8b KStG Schachtelprivileg (95 % steuerfreier Exit), Varianten Einzel-Holding, Vermögens-Holding, Doppel-Holding mit Familienstiftung. Gewerbesteuerkürzung § 9 Nr. 1 S. 2 GewStG Immobilien-Holding. Zeitreihenfolge Holding vor Gründung der Tochter. Wegzugsbesteuerung § 6 AStG. Pflichtteilsschutz § 2325 BGB. Praktische Rechenbeispiele Exit-Vorteil. GmbH-Gründungsaufwand, Notarkosten. Schriftsatzvorlagen Anteilsübertragungsvertrag, Holding-GmbH-Gründung._

## Mandantenfragen beim Kaltstart

1. Wie ist die aktuelle Struktur — Einzelunternehmen, einfache GmbH, GmbH & Co. KG, AG?
2. Welche Aktivitäten sollen über die Holding abgewickelt werden — operatives Geschäft, M&A-Beteiligungen, Immobilienvermögen, Familienerbfolge?
3. Wie hoch ist der geschätzte Unternehmenswert und in welchem Zeithorizont ist ein Exit oder eine Unternehmensübertragung geplant?
4. Besteht eine Nachfolgeplanung innerhalb der Familie — Übertragung an Kinder, Stiftungsgründung?
5. Ist die Holding-GmbH bereits gegründet, oder muss sie neu gegründet werden (Zeitreihenfolge beachten)?
6. Gibt es Auslandsbezug (Gesellschafter wohnt im Ausland, geplanter Wegzug — § 6 AStG Wegzugsbesteuerung)?
7. Sind pflichtteilsrelevante Schenkungen geplant (§ 2325 BGB 10-Jahres-Frist)?
8. Soll eine Familienstiftung als oberste Ebene eingesetzt werden (Pflichtteils- und Erbschaftsteuervorteile)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|------|--------|
| § 8b Abs. 2 KStG | Schachtelprivileg Veräußerung: 95 % des Veräußerungsgewinns steuerfrei bei der Holding-GmbH |
| § 8b Abs. 1 KStG | Schachtelprivileg Dividenden: 95 % der Dividende steuerfrei bei mindestens 10 % Beteiligung |
| § 8b Abs. 3 S. 1 KStG | Hinzurechnung 5 % als nichtabziehbare Betriebsausgaben (Schein-Betriebsausgabe) |
| § 8b Abs. 4 KStG | Mindestbeteiligung 10 % zu Beginn des Kalenderjahres für Dividenden-Schachtelprivileg |
| § 9 Nr. 1 S. 2 GewStG | Erweiterte Gewerbesteuerkürzung: Immobilien-Holding mit ausschließlich Verwaltung von Immobilien; volle GewSt-Befreiung der Mieterträge |
| § 8 GewStG | Hinzurechnungen (Zinsen, Mieten, Pachten) beim operativen Unternehmen |
| § 6 AStG | Wegzugsbesteuerung: Entstrickung stiller Reserven bei Wegzug ins Ausland mit GmbH-Anteilen (stille Reserven sofort besteuert) |
| § 2325 BGB | Pflichtteilsergänzungsanspruch: Schenkungen innerhalb der letzten 10 Jahre werden Nachlasswert hinzugerechnet |
| § 2303 BGB | Pflichtteilsanspruch: 1/2 des gesetzlichen Erbteils als Minimalanspruch |
| §§ 80 ff. BGB | Stiftungsgründung (Bundes-Stiftungsrecht); Landesstiftungsgesetze |
| § 58 KStG | Stiftungen: Thesaurierungsfreibetrag EUR 5.000/Jahr |
| § 3 Nr. 2 GrEStG | Grunderwerbsteuer-Befreiung bei Grundstücksübertragung auf Personengesellschaft unter bestimmten Bedingungen |
| § 6a GrEStG | Konzernklausel: Umstrukturierungen im Konzern grunderwerb-steuerfrei (95 %-Beteiligung, 5-Jahres-Behaltefrist) |
| § 17 EStG | Veräußerungsgewinn bei wesentlicher Beteiligung (> 1 %): 25 % Abgeltungssteuer oder Teileinkünfteverfahren § 3 Nr. 40 EStG |

## Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---------|-------------|-------|-------------|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |
| OFD Frankfurt | S 2241 A – 11 – St 211 | 2019 | Praktische Anwendung § 8b KStG: Kettenausschüttung Tochter → Holding → Privat |

## Struktur-Varianten im Vergleich

| Variante | Struktur | Steuerlicher Kernvorteil | Besondere Eignung |
|---------|---------|--------------------------|-----------------|
| A — Einzel-Holding | Privatperson → Holding-GmbH → Operative GmbH | § 8b KStG: 95 % steuerfreier Exit | Klassisches Start-up; einmaliger Exit-Fokus |
| B — Vermögens-Holding | Privatperson → Vermögens-Holding → [Operative + Immobilien + Beteiligungen] | § 8b KStG + § 9 Nr. 1 S. 2 GewStG kombiniert | Konglomerats-Vermögensverwaltung |
| C — Doppel-Holding | Familienstiftung → Holding-GmbH 1 → Holding-GmbH 2 → Operative Töchter | Pflichtteils-Schutz; Generationen-Trennung; Erbschaftsteuer-Optimierung | Familienunternehmen; Nachfolge |
| D — GmbH & Co. KG-Holding | Privatperson (Kommanditist) → KG als Holding → Tochtergesellschaften | Gewerbesteuerliche Transparenz; § 15 EStG | Mittelstand mit KG-Tradition |

## Rechenbeispiel Exit-Vorteil

### Ohne Holding (Direktverkauf GmbH-Anteile)

```
Kaufpreis Anteile:                      EUR 10.000.000
Anschaffungskosten:                   ./. EUR  1.000.000
Veräußerungsgewinn:                     EUR  9.000.000

Teileinkünfteverfahren § 3 Nr. 40 EStG: 60 % steuerpflichtig = EUR 5.400.000
Einkommensteuer ca. 42 %:             ./. EUR  2.268.000
Solidaritätszuschlag 5,5 %:          ./. EUR    124.740

Netto-Erlös:                            EUR  7.607.260
```

### Mit Holding (§ 8b KStG)

```
Holding-GmbH verkauft Anteile:          EUR 10.000.000
Anschaffungskosten:                   ./. EUR  1.000.000
Veräußerungsgewinn:                     EUR  9.000.000

§ 8b Abs. 2 KStG: 95 % steuerfrei       EUR  8.550.000
5 % Schein-Betriebsausgabe:             EUR    450.000 steuerpflichtig
KSt 15 % + Soli + GewSt ca. 30 %:    ./. EUR    135.000

Netto-Holding-Vermögen:                 EUR  9.865.000

Vorteil gegenüber Direktverkauf:        EUR  2.257.740 (Steueraufschub)

Bei späterer Ausschüttung Holding → Privat:
§ 20 EStG Abgeltungssteuer 25 %:      ./. EUR  2.221.250 (auf Netto-9.865.000)
Tatsächlicher Nettoerlös Privat:        EUR  7.393.750

Steueraufschub-Vorteil (Reinvestition): Erheblich bei mehrjährigem
Aufschub; Zinseffekt auf EUR 2.258.000 über 5–10 Jahre
```

## Prüfschema Holding-Aufbau

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.


| Schritt | Prüfpunkt | Norm | Rechtsfolge |
|---------|-----------|------|-------------|
| 1 | Zeitreihenfolge: Holding VOR operativer GmbH? | § 8b KStG; Umwandlungsrecht | Nachträgliche Holding: Einbringungsaufwand und ggf. Sperrfrist |
| 2 | Mindestbeteiligung 10 % für § 8b KStG? | § 8b Abs. 4 KStG | Stichtag = Beginn des Wirtschaftsjahres der Dividende |
| 3 | Erweiterte Kürzung § 9 Nr. 1 S. 2 GewStG anwendbar? | § 9 Nr. 1 S. 2 GewStG | Ausschließlich Immobilienverwaltung; keine gewerbliche Beimengung |
| 4 | § 6a GrEStG Konzernklausel bei Umstrukturierung? | § 6a GrEStG | 95 %-Beteiligung ununterbrochen 5 Jahre vor und nach Umstrukturierung |
| 5 | Wegzug ins Ausland geplant? | § 6 AStG | Stille Reserven bei GmbH-Anteilen sofort versteuert; Ratenzahlung möglich |
| 6 | Pflichtteilsrelevante Schenkungen? | § 2325 BGB | 10-Jahres-Frist läuft; Nießbrauchsvorbehalt stoppt Frist nicht |
| 7 | Familienstiftung als oberste Ebene? | §§ 80 ff. BGB; § 58 KStG | Pflichtteils-Schutz; Erbschaftsteuerpflicht Stiftungsgründung beachten |
| 8 | GmbH-Gründungsaufwand und laufende Pflichten? | GmbHG; HGB | Bilanzierungspflicht; Offenlegung; Jahresabschluss Holding |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Holding-Struktur planen | Struktur-Varianten-Vergleich; Anteilsuebertragungsvertrag unten |
| Variante A — Exit-Optimierung im Vordergrund | § 8b KStG-Vorteil berechnen; Holding prioritaer empfehlen |
| Variante B — Haftungsschutz vorrangig | Operative Risiken in Tochter-GmbH halten; Holding schirmt ab |
| Variante C — Erbschaft / Unternehmensnachfolge | Familienpool-Holding und Niesbrauchsvorbehalt pruefen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatz-Bausteine

### Anteilsübertragungsvertrag (Operative GmbH auf Holding-GmbH)

```
ANTEILSÜBERTRAGUNGSVERTRAG

Parteien:
Übertragender: [Name/GmbH], [Anschrift] (nachfolgend "Übertragender")
Erwerber: [Holding-GmbH], vertreten durch Geschäftsführer [Name] (nachfolgend "Holding")

§ 1 Übertragungsgegenstand
Der Übertragende ist Inhaber eines Geschäftsanteils von EUR [Betrag] (nominal)
an der [Operative GmbH], [Sitz], HRB [Nr.] (nachfolgend "Gesellschaft").
Der Übertragende überträgt diesen Geschäftsanteil auf die Holding.

§ 2 Kaufpreis / Einbringungswert
[Variante A - Kauf:]
Die Holding zahlt einen Kaufpreis von EUR [Betrag] (Verkehrswert).
Zahlbar bis zum [Datum] auf Konto [IBAN].

[Variante B - Einbringung gegen Gesellschafterrechte:]
Die Einbringung erfolgt gegen Gewährung neuer Gesellschafterrechte an der
Holding gemäß §§ 20, 21 UmwStG zu Buchwerten [alternativ: zu Verkehrswerten].
Steuerliche Behandlung nach UmwStG (Einbringungsgewinnbesteuerung prüfen).

§ 3 Notarielle Form
Dieser Vertrag bedarf der notariellen Beurkundung (§ 15 Abs. 3 GmbHG).
Beurkundung durch Notar [Name], [Ort], am [Datum].

§ 4 Gewährleistung
Der Übertragende gewährleistet, dass der Geschäftsanteil frei von Rechten
Dritter, nicht verpfändet und nicht mit Treuhandpflichten belastet ist.

[Ort, Datum]
[Unterschriften]
```

### Holding-GmbH-Gründung (Checkliste Anwaltsmandat)

```
Checkliste Holding-GmbH-Gründung:

Schritt 1: Vorab
[ ] Firmenrecherche beim Handelsregister (Namensexklusivität)
[ ] Geschäftsadresse festlegen
[ ] Geschäftsführer(in) benennen (kein Berufsverbot § 6 Abs. 2 GmbHG)

Schritt 2: Notartermin
[ ] Gesellschaftsvertrag (Satzung) vorbereiten:
    - Firma: [Name] Holding GmbH
    - Stammkapital: mind. EUR 25.000 (§ 5 GmbHG)
    - Gesellschafterzweck: "Erwerb, Verwaltung und Veräußerung von
      Unternehmensbeteiligungen"
    - Geschäftsführer(-in) benennen
    - Stammeinlagen aufteilen
[ ] Notarielle Beurkundung Gesellschaftsvertrag + Geschäftsführerbestellung
[ ] Gründungsprotokoll

Schritt 3: Anmeldung
[ ] Handelsregistereintragung (durch Notar)
[ ] Stammkapital mind. EUR 12.500 einzahlen vor Anmeldung (§ 7 Abs. 2 GmbHG)
[ ] Steuerliche Anmeldung beim Finanzamt (USt-IdNr.; KSt-Voranmeldung)

Schritt 4: Post-Gründung
[ ] Geschäftskonto eröffnen (Holding getrennt von Operativ-GmbH)
[ ] Konzernstruktur beim Steuerberater hinterlegen
[ ] Cash-Pooling-Vertrag prüfen (Zinsmarktverhältnisse § 8 Abs. 3 KStG)

Kosten ca.:
- Notar Gründung: EUR 500–1.000 (Stammkapital EUR 25.000)
- Gerichtsgebühr HReg: ca. EUR 150
- Steuerberater Strukturberatung: EUR 3.000–15.000 je Komplexität
- Anwaltshonorar: EUR 5.000–30.000 je Komplexität
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]


## Beweislast / Steuerliche Dokumentation

| Thema | Nachweis | Dokument |
|-------|---------|---------|
| § 8b KStG Beteiligungsquote 10 % | Gesellschafterliste zum Stichtag | Notarielle Gesellschafterliste; HR-Auszug |
| Erweiterte Kürzung § 9 Nr. 1 S. 2 GewStG | Ausschließlich Immobilienverwaltung | GewSt-Erklärung; Gesellschaftsvertrag ohne gewerbliche Klausel |
| Wegzugsbesteuerung § 6 AStG (Ratenzahlung) | Antrag + Sicherheitsleistung | Antrag beim FA; Bürgschaft oder Grundpfandrecht |
| Pflichtteilsergänzung § 2325 BGB (10 Jahre) | Schenkungsdatum | Schenkungsvertrag notariell; Steuerbescheid SchenkSt |
| Konzernklausel § 6a GrEStG | 95 % Beteiligungsdurchgängigkeit | Beteiligungsstruktur 5 Jahre vor + nach Umstrukturierung |

## Fristen

| Frist | Inhalt | Norm |
|-------|--------|------|
| 10 Jahre | Pflichtteilsergänzungsanspruch bei Schenkungen | § 2325 BGB |
| 5 Jahre | § 6a GrEStG Konzernklausel: Behaltefrist vor und nach Umstrukturierung | § 6a GrEStG |
| 7 Jahre | Aufbewahrungspflicht Buchhaltungsunterlagen Holding | § 257 HGB |
| 5 Jahre | Körperschaftsteuer-Festsetzungsfrist | § 169 Abs. 2 Nr. 2 AO |
| 10 Jahre | FA-Festsetzung bei leichtfertiger Steuerverkürzung | § 169 Abs. 2 Nr. 1 AO |

## Gegenargumente und Reaktion

| Gegenargument | Herkunft | Reaktion |
|--------------|---------|----------|
| "§ 8b KStG Beteiligung < 10 %" | Finanzamt | Stichtag = Beginn des Wirtschaftsjahres; unterjährigen Erwerb so planen, dass Jahresbeginn überschritten |
| "Gewerbliche Beimengung schadet § 9 Nr. 1 S. 2 GewStG" | Finanzamt | Nebentätigkeiten aus Immobilien-GmbH ausgliedern; reine Verwaltungsgesellschaft sicherstellen |
| "Wegzugsbesteuerung bei Wohnsitzwechsel" | Steuerberater/Mandant | § 6 AStG Ratenzahlung bei EU/EWR-Wohnsitz; Rückkehroption innerhalb 7 Jahre |
| "Holding nach operativer GmbH gegründet — Umwandlung nötig" | Mandant | §§ 20, 21 UmwStG: Einbringung zu Buchwerten möglich; Sperrfrist 7 Jahre beachten |
| "Pflichtteils-Schutz durch Stiftung fraglich" | Erbe | Stiftung muss seit > 10 Jahren bestehen für vollständigen Schutz; BGH-Linie beachten |
| "Doppelbesteuerung Holding → Privat" | Mandant | Holding thesauriert; Ausschüttung strategisch planen; Vermögensaufbau in Holding günstiger als Direkteinnahme |

## Streitwert und Kosten

**Notar- und Gründungskosten:**
- Holding-GmbH-Gründung (Stammkapital EUR 25.000): Notargebühr ca. EUR 500–1.000 nach GNotKG; Handelsregistergebühr ca. EUR 150.
- Anteilsübertragung (Kaufpreis EUR 1 Mio.): Notargebühr nach GNotKG ca. EUR 2.000–4.000 (nach Gebührentabelle).

**Steuerberater:** Strukturberatung EUR 3.000–15.000 je Komplexität; laufende Buchhaltung Holding EUR 1.500–5.000/Jahr.

**Anwaltliche Beratung:** Gesellschaftsrechtliche Strukturierung EUR 5.000–30.000 (abhängig von Komplexität, Beteiligungszahl, Stiftungsgründung).

**Steuerlicher Exit-Vorteil (Rechenbeispiel EUR 9 Mio. Gewinn):**
- Direktverkauf Privatperson: ca. EUR 2,4 Mio. Steuern.
- Verkauf durch Holding: ca. EUR 135.000 Steuern im Jahr des Exits.
- Vorteil: EUR 2,25 Mio. Steueraufschub (zusätzlicher Investitionsspielraum).

## Strategische Empfehlung

| Situation | Empfehlung | Begründung |
|-----------|------------|-----------|
| Junges Start-up vor erstem Investor | Holding-GmbH zuerst gründen, dann operative GmbH darunter | § 8b KStG-Vorteil ab erster Runde sichergestellt |
| Bestehende GmbH, Exit in 5 Jahren | Einbringung in Holding nach §§ 20, 21 UmwStG; Sperrfrist 7 Jahre beachten | Frühzeitige Umstrukturierung spart Steuern bei Exit |
| Immobilienvermögen strukturieren | Eigenständige Immobilien-GmbH unter Vermögens-Holding; § 9 Nr. 1 S. 2 GewStG | Volle GewSt-Befreiung der Mieterträge; keine operative Beimengung |
| Familienunternehmen mit Nachfolge | Familienstiftung + Holding; frühzeitige Schenkung Anteile an Kinder (10-Jahres-Frist § 2325 BGB) | Pflichtteils- und ErbSt-Optimierung kombiniert |
| Gesellschafter plant Wegzug | § 6 AStG-Beratung vor Wohnsitzverlegung; Ratenzahlung in EU | Wegzugsbesteuerung frühzeitig planen |

## Anschluss-Skills

- `fachanwalt-handels-gesellschaftsrecht-gesellschafterstreit` — Gesellschafterstreit in der Holding-Struktur
- `fachanwalt-handels-gesellschaftsrecht-geschaeftsfuehrerhaftung` — GF-Haftung in mehrstufiger Holding
- `fachanwalt-erbrecht-pflichtteilsberechnung` — Pflichtteilsansprüche bei Holding-Schenkung
- `fachanwalt-insolvenz-sanierungsrecht-restrukturierungsplan` — Holding-Restrukturierung bei Krise

## Quellen

- § 8b KStG: https://www.gesetze-im-internet.de/kstg_1977/__8b.html
- § 9 GewStG: https://www.gesetze-im-internet.de/gewstg/__9.html
- § 6a GrEStG: https://www.gesetze-im-internet.de/grestg_1983/__6a.html
- § 6 AStG: https://www.gesetze-im-internet.de/astg/__6.html
- UmwStG: https://www.gesetze-im-internet.de/umwstg_2006/
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `fachanwalt-hgr-dlt-pilotregime-token`

_EU-DLT-Pilotregime VO 2022/858 (anwendbar 23.3.2023, verlängert voraussichtlich bis 23.3.2029) für DLT-basierte Wertpapierinfrastruktur. Tokenisierte Aktien und elektronische Wertpapiere (eWpG). Plattformtypen DLT-MTF (500 Mio. EUR) / DLT-TSS (6 Mrd. EUR) / DLT-SS. BaFin-Lizenzverfahren. Krypto-Wertpapierregister § 16 eWpG. Schwellenwerte, Compliance-Workflow, Risikomatrix, DORA-Schnittstelle, MiCA-Abgrenzung. Schriftsatzvorlagen BaFin-Antrag, Smart-Contract-Checkliste._

## Mandantenfragen beim Kaltstart

1. Welcher Wertpapiertyp soll tokenisiert werden — Inhaberaktie (§ 10 AktG), Namensaktie (§ 67 AktG), Schuldverschreibung oder Investmentanteil?
2. Welches Zielvolumen / welche Marktkapitalisierung ist geplant (relevant für Schwellenwerte DLT-MTF: 500 Mio. EUR; DLT-TSS: 6 Mrd. EUR)?
3. Welcher Plattformtyp ist vorgesehen — nur Handel (DLT-MTF), nur Abwicklung (DLT-SS) oder kombiniert (DLT-TSS)?
4. Ist ein bestehender BaFin-lizenzierter Anbieter als Register-Führer vorgesehen, oder wird eine eigene Lizenz beantragt?
5. Welche DLT-Plattform / Blockchain ist vorgesehen (Permissioned, Permissionless; Ethereum, Polygon, Stellar, dedizierte EU-Chain)?
6. Ist die Satzung der Aktiengesellschaft auf "elektronische Wertpapiere als Krypto-Wertpapiere" ausgerichtet?
7. Sind DORA-Anforderungen (seit 17.1.2025) bereits in der IT-Governance abgebildet?
8. Besteht ein Zeitplan für den Übergang nach Ablauf des Pilotregimes (voraussichtlich verlängert bis 23.3.2029)?

## Rechtsgrundlagen

| Norm | Inhalt |
|------|--------|
| VO (EU) 2022/858 Art. 4 | DLT-MTF (Multilateral Trading Facility): Handel mit DLT-Wertpapieren; Schwelle 500 Mio. EUR Marktkapitalisierung |
| VO (EU) 2022/858 Art. 5 | DLT-SS (Settlement System): Abwicklung; ohne separate Handelsschwelle |
| VO (EU) 2022/858 Art. 6 | DLT-TSS (Trading and Settlement System): Kombination; Schwelle 6 Mrd. EUR Gesamtvolumen |
| VO (EU) 2022/858 Art. 7–9 | Voraussetzungen + Befreiungen von MiFID II / CSDR-Anforderungen |
| VO (EU) 2022/858 Art. 14 | Marktransparenzpflichten auf DLT-Plattformen |
| VO (EU) 2022/858 Art. 16 | Halbjährliche Berichtspflicht an ESMA |
| § 1 eWpG | Elektronisches Wertpapier: Begriffsbestimmung; Krypto-Wertpapier als Unterform |
| § 4 eWpG | Begründung durch Eintragung im Register statt Urkundenausgabe |
| § 11 eWpG | Krypto-Wertpapierregister: DLT-basiertes Register; Pflicht-Inhalte |
| § 16 eWpG | Pflichten des Register-Führers: Integrität, Verfügbarkeit, Vertraulichkeit |
| § 17 eWpG | Übertragung durch Umbuchung im Register; Gutglaubensschutz |
| § 1 Abs. 11 S. 1 Nr. 10 KWG | Krypto-Wertpapier als Finanzinstrument |
| § 1 Abs. 1a Nr. 8 KWG | Kryptoverwahrgeschäft als erlaubnispflichtiges Finanzdienstleistungsgeschäft |
| § 67c AktG | Digitales Aktienregister: Anforderungen bei Namensaktien |
| § 118a AktG | Online-Hauptversammlung mit digitaler Stimmrechtsausübung (DiRUG) |
| VO (EU) 2022/2554 (DORA) | Digital Operational Resilience Act: seit 17.1.2025 für Finanzdienstleister; auch für DLT-Plattformen anwendbar |
| VO (EU) 2023/1114 (MiCA) | Markets in Crypto Assets: ARTs und EMTs; Abgrenzung zu eWpG-Krypto-Wertpapieren wichtig |

## Leitentscheidungen und Regulatorische Quellen

| Quelle | Datum | Kernaussage |
|--------|-------|-------------|
| ESMA Final Report on DLT Pilot Regime | 2022 | Technische Standards; Plattformtypen; Berichtspflichten |
| BaFin-Merkblatt zum DLT-Pilotregime-Antrag | 2023 | Anforderungen BaFin-Antrag; Verfahrensdauer 6 Monate |
| BMF-Schreiben vom 17.11.2022 | 17.11.2022 | Steuerliche Behandlung Krypto-Wertpapiere; KapESt auf Token-Dividenden |
| ESMA Opinion on Review of DLT Pilot | 2024 | Empfehlung zur Verlängerung; Anpassungen für Phase 2 |
| BaFin-Schreiben zu DORA-Umsetzung | 2025 | DORA-Anforderungen für Register-Führer und DLT-Plattformbetreiber |

## DLT-Plattformtypen im Überblick

| Typ | Funktion | Schwelle | MiFID II / CSDR-Befreiung | Typische Nutzung |
|-----|---------|---------|--------------------------|-----------------|
| DLT-MTF | Nur Handel | 500 Mio. EUR Marktkapitalisierung | MiFID II-Lockerungen möglich | Sekundärmarkt für Token-Aktien |
| DLT-SS | Nur Abwicklung | Keine Schwelle | CSDR-Lockerungen | Clearing und Settlement für DLT-Wertpapiere |
| DLT-TSS | Handel + Abwicklung | 6 Mrd. EUR Gesamtvolumen | MiFID II + CSDR kombiniert | Vollständiger DLT-Marktplatz |

## Workflow Tokenisierung einer Aktiengesellschaft

### Phase 1 — Strukturentscheidung und Satzungsänderung

```
1. Rechtsformprüfung: AG, SE oder GmbH?
   - AG bevorzugt (§ 67c AktG digitales Aktienregister)
   - GmbH: Krypto-Wertpapier-Regelung über § 4 eWpG möglich

2. Satzungsanpassung (HV-Beschluss):
   - Aufnahme Klausel: "Die Gesellschaft kann Aktien als elektronische
     Wertpapiere gemäß eWpG begeben."
   - Namens- oder Inhaberaktie: Entscheidung dokumentieren
   - Form der HV-Einberufung und Stimmrechtsausübung digital (§ 118a AktG)

3. Notarielle Beurkundung der Satzungsänderung (§ 130 AktG)
4. Eintragung im Handelsregister
```

### Phase 2 — Krypto-Wertpapierregister einrichten

```
1. Wahl Register-Führer:
   - Bank mit § 1 KWG-Lizenz oder FinTech mit
     Kryptoverwahrerlaubnis (§ 1 Abs. 1a Nr. 8 KWG)
   - Due Diligence: DORA-Compliance, IT-Sicherheitszertifizierung,
     BaFin-Aufsicht aktiv

2. DLT-Plattform:
   - Permissioned (Ethereum Enterprise, Polygon, Stellar, Hyperledger):
     bevorzugt für regulierte Emissionen
   - Permissionless: KYC/AML-Anforderungen schwerer einhaltbar

3. Krypto-Wertpapierregister § 11 eWpG-Anforderungen:
   - Identifier der Token (ISIN digital)
   - Stückelung und Gesamtzahl
   - Inhaber-Verzeichnis (für Namensaktien)
   - Übertragungshistorie (unveränderlich / immutable)

4. Smart Contract-Pflichtfelder:
   - Transferrestriktionen (Whitelist KYC-verifizierter Adressen)
   - Compliance-Layer (AML/CFT nach GwG)
   - Dividendenausschüttungs-Funktion
   - Voting-Integration (§ 118a AktG)
```

### Phase 3 — BaFin-Lizenzantrag (für Plattformbetreiber)

```
Antrag an BaFin für DLT-MTF / DLT-SS / DLT-TSS:

Pflichtinhalte nach VO (EU) 2022/858 Art. 7:

1. Beschreibung der DLT-Infrastruktur:
   - Blockchain-Typ, Konsens-Mechanismus, Nodes
   - Governance-Struktur der Plattform

2. Cybersecurity-Konzept (BaFin BAIT/MaRisk):
   - Penetrationstest-Berichte (monatlich / jährlich)
   - Business Continuity Plan (BCP)
   - DORA-Konformitätsbescheinigung (seit 17.1.2025 Pflicht)

3. Marktintegrität:
   - MAR-Compliance (Insiderhandel, Marktmanipulation)
   - Ad-hoc-Mitteilungspflicht § 17 MAR

4. Transparenzberichte:
   - Halbjährlich an ESMA (Art. 16 VO 2022/858)

5. Übergangsplan nach Ende Pilotregime:
   - Roadmap Übergang zu vollem MiFID II / CSDR oder Schließung

Verfahrensdauer: 6 Monate (BaFin) + ggf. Verlängerung
```

### Phase 4 — Emittenten-Pflichten

```
1. Prospektpflicht (§ 6 WpPG):
   - Bei öffentlichem Angebot > EUR 8 Mio. in 12 Monaten: Prospektpflicht
   - Ausnahmen: nicht-öffentliche Platzierung, qualifizierte Anleger

2. KYC/AML der Token-Inhaber (GwG):
   - Identifizierungspflicht bei Erwerb
   - Whitelist im Smart Contract

3. Kapitalmarktrecht:
   - Insider-Liste § 26 MAR
   - Ad-hoc-Mitteilung § 17 MAR bei kursrelevanten Informationen
   - Stimmrechtsmitteilungen §§ 33 ff. WpHG bei Schwellenüberschreitung

4. Steuer:
   - Kapitalertragsteuer § 43 EStG auf Token-Dividenden
   - Veräußerungsgewinn: § 17 EStG (> 1 % Beteiligung) oder § 23 EStG
   - BMF-Schreiben 17.11.2022
```

### Phase 5 — Übertragung und Stimmrecht

```
1. Übertragung § 17 eWpG:
   - Umbuchung im Krypto-Wertpapierregister = Eigentumsübergang
   - Gutglaubensschutz für Erwerber

2. Hauptversammlung:
   - Token-Identifikation für Online-HV (§ 118a AktG)
   - Stimmenzählung via Smart Contract
   - Stimmrechtsnachweis per Blockchain-Snapshot zum Stichtag

3. Dividende:
   - Snapshot zum Ausschüttungsstichtag
   - Auszahlung an Token-Adressen (automatisch oder manuell)
   - KapESt-Einbehalt obligatorisch
```

## Risikomatrix

| Konstellation | Risiko | Norm | Maßnahme |
|--------------|--------|------|---------|
| Register-Führer ohne KWG-Lizenz | SEHR HOCH | § 32 KWG; § 1 Abs. 1a Nr. 8 KWG | Lizenzkontrolle vor Vertragsschluss |
| Smart Contract ohne Transfer-Restriktionen | HOCH | GwG; FATF-Standards | Whitelist-Layer einbauen; AML-Compliance |
| Schwelle DLT-MTF überschritten (> 500 Mio. EUR) | HOCH | Art. 4 VO 2022/858 | Übergang zu vollem MiFID II erforderlich oder Volumen reduzieren |
| DORA nicht eingehalten (seit 17.1.2025) | MITTEL-HOCH | VO 2022/2554 Art. 16–20 | ICT-Risikomanagement implementieren; Penetrationstest |
| Pilotregime läuft aus (3/2026 bzw. 3/2029) | MITTEL | VO 2022/858 Art. 18 | Übergangsstrategie 18 Monate vorher definieren |
| Prospektpflicht missachtet | SEHR HOCH | § 6 WpPG | Schwelle EUR 8 Mio. überwachen; Ausnahmen dokumentieren |
| MiCA-ART-Einstufung des Tokens | MITTEL | VO 2023/1114 | Abgrenzung Krypto-Wertpapier (eWpG) vs. Asset-Referenced Token (MiCA) |

## Smart-Contract-Checkliste § 16 eWpG

```
Pflicht-Felder im Krypto-Wertpapierregister:

[ ] Eindeutiger Identifier (ISIN digital oder nationale Kennung)
[ ] Wertpapierart (Aktie/Schuldverschreibung)
[ ] Emittent (Name, LEI-Nummer)
[ ] Gesamtstückelung und Nennwert
[ ] Ausstellungsdatum
[ ] Inhaber-Mapping (für Namensaktien: Adresse → Identität)
[ ] Unveränderlichkeit der Buchungshistorie (Audit Trail)
[ ] Transferrestriktionen (Whitelist / Blacklist)
[ ] Dividendenausschüttungs-Funktion
[ ] Voting-Integration (HV-Stimmrecht § 118a AktG)
[ ] Emergency-Freeze-Funktion (regulatorische Anforderung)
[ ] Interoperabilität mit anderen Registern (§ 17 eWpG Übertragung)
```

## Beweislast

| Beweisthema | Beweislast | Beweismittel |
|------------|-----------|--------------|
| Eigentumsübergang durch Umbuchung | Erwerber | Blockchain-Protokoll; Register-Auszug § 11 eWpG |
| BaFin-Lizenz des Register-Führers | Emittent bei Haftungsklage | BaFin-Lizenzurkunde; öffentliches BaFin-Register |
| Prospektpflicht-Ausnahme | Emittent | Anleger-Protokoll (qualifizierter Anleger); Platzierungsdokumentation |
| DORA-Compliance | Plattformbetreiber | ICT-Risikomanagement-Bericht; Audit-Protokoll |
| Eigentumsstellung für Stimmrecht HV | Aktionär | Snapshot-Zertifikat der Blockchain zum Stichtag |

## Fristen

| Frist | Inhalt | Norm |
|-------|--------|------|
| 6 Monate | BaFin-Lizenzverfahren (ca.) | BaFin-Merkblatt 2023 |
| Halbjährlich | ESMA-Transparenzbericht | Art. 16 VO 2022/858 |
| 17.1.2025 | DORA vollständig anwendbar | VO 2022/2554 |
| 23.3.2029 | Voraussichtliches Ende Pilotregime (verlängert) | VO 2022/858; ESMA-Empfehlung |
| 10 Tage | Meldepflicht bei IT-Vorfällen nach DORA | VO 2022/2554 Art. 19 |

## Strategische Empfehlung

| Situation | Empfehlung | Begründung |
|-----------|------------|-----------|
| Startup will Token-Aktien begeben | DLT-TSS oder DLT-SS mit lizenziertem Register-Führer; eigene BaFin-Lizenz nur bei Volumen > EUR 100 Mio. | Kosten-Nutzen; Lizenz-Outsourcing kostengünstiger |
| Bestehendes Unternehmen will Kapitalerhöhung digital | Satzungsänderung + Krypto-Wertpapierregister + Prospekt-Prüfung | Digitale Emission erhöht Liquidität; Prospektpflicht beachten |
| Pilotregime läuft aus | 18 Monate vorher Übergangsplan: MiFID II-Compliance, CSDR oder Plattformschließung | ESMA-Empfehlung: Übergangsfrist beachten |
| Stimmrechtsausübung digital | Online-HV § 118a AktG + Smart-Contract-Voting + Datenschutz | Effizienzgewinn; Satzungsklausel erforderlich |

## Anschluss-Skills

- `fachanwalt-bank-kapitalmarktrecht-mica-stablecoin-art-16-bafin` — MiCA-Abgrenzung zu Krypto-Wertpapieren
- `fachanwalt-handels-gesellschaftsrecht-holding-strukturplanung` — Holding-Struktur bei Token-Unternehmen
- `sanktions-compliance-pruefung` — Exportkontrolle bei DLT-Plattformen mit Auslandsbezug
- `gerichtsstand-und-rechtswahl-pruefen` — Grenzüberschreitende Token-Angebote

## Quellen

- EU-DLT-Pilotregime VO 2022/858: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32022R0858
- eWpG: https://www.gesetze-im-internet.de/ewpg/
- BaFin DLT-Pilotregime: https://www.bafin.de/DE/Aufsicht/FinTech/DLT-Pilotregime/dlt_pilotregime_node.html
- DORA VO 2022/2554: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32022R2554
- MiCA VO 2023/1114: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32023R1114
- BMF-Schreiben 17.11.2022: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Ertragsteuern/2022-11-17-einzelfragen-zur-ertragsteuerrechtlichen-behandlung-von-elektronischen-wertpapieren.pdf


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

---

## Skill: `output-waehlen`

_Output-Wahl für Fachanwalt Handels- und Gesellschaftsrecht: stimmt Adressat (Gesellschafter/Aktionäre, Vorstand/Geschäftsführung, Aufsichtsrat), Frist (§ 246 AktG Anfechtung 1 Monat) und Form auf den Zweck ab — typische Outputs: Beschlussanfechtung, Squeeze-out-Klage, Geschäftsführerklage._

# Output wählen

## Einsatzlage

Diese Output-Weiche für **Fachanwalt Handels Gesellschaftsrecht** entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist.

## Fachlandkarte dieses Plugins

- `ag-vorstandsvertrag-vorbereiten` — AG Vorstandsvertrag HGR
- `aktionaersklage-anfechtung-paragraf-243-aktg` — Aktionaersklage Anfechtung Paragraf 243 AKTG
- `anfechtungsklage-bgb-gesellschaft-bgh-ii-zr-66-20` — Anfechtungsklage BGB Gesellschaft BGH II ZR 66 20
- `einstieg-schnelltriage-fallrouting` — FA Handels Gesellschaft Start Chronologie Fristen
- `erstpruefung-und-mandatsziel` — Fachanwalt FAO Gesellschafterstreit
- `geschaeftsfuehrerhaftung-zahlen-schwellen-und-berechnung` — Geschäftsführerhaftung Holding
- `gesellschafterstreit` — Gesellschaftsrecht Gesellschafterstreit Eilrechtsschutz
- `gesellschaftervertrag-abschlussprodukt-und-uebergabe` — Gesellschaftsrecht Gesellschaftervertrag Klauseln
- `gmbh-beirat-vetorechte-und-organnaehe` — Gmbh Beirat Vergleichsverhandlung Strategie
- `gmbh-gf-haftung-paragraf-43-gmbhg` — Gmbh GF Haftung Paragraf 43 GMBHG
- `gmbhg-schriftsatz-brief-und-memo-bausteine` — GMBHG Handels Handelsvertreterausgleich
- `workflow-mandantenkommunikation` — Handels Gesellschaftsrecht Mandantenkommunikation Redteam
- `hgb-einsichtsrecht-kommanditist-paragraf-166-hgb-bgh-ii-zr-31-21` — HGB Einsichtsrecht Kommanditist Paragraf 166 HGB BGH II ZR 31 21
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Ergebnistyp bestimmen: Schriftsatz an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen, Mandantenmemo, Risikobericht, Vertragsentwurf, Entscheidungsvorlage, Behörden-Stellungnahme — was braucht der Mandant wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Fachanwalt Handels Gesellschaftsrecht (AktG, GmbHG, HGB, MoPeG, PartGG, UmwG, § 14i, § 89b HGB) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei Mandant ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

