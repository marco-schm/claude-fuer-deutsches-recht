# Megaprompt: fachanwalt-medizinrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 158 Skills (gekuerzt fuer Chat-Fenster) des Plugins `fachanwalt-medizinrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Anwalts-Dashboard Fachanwalt Medizinrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Z…
2. **mandat-triage-medizinrecht** — Strukturierte Eingangs-Abfrage für medizinrechtliche Mandate: Klaert Mandantenrolle (Patient Arzt Krankenhaus Heilberufl…
3. **fachanwalt-medizinrecht-orientierung** — Orientierung im Medizinrecht — FAO Voraussetzungen Normen typische Mandate Fristen verifizierbare Quellen. Arzthaftung §…
4. **orientierung-mandat-fachanwaltschaft** — Orientierung im Medizinrecht — FAO Voraussetzungen Normen typische Mandate Fristen verifizierbare Quellen: Arzthaftung §…
5. **erstgespraech-mandatsannahme** — Erstgespraeach und Mandatsannahme im Arzthaftungs- Berufs- und Vertragsarztrecht: Anwendungsfall Patient oder Arzt melde…
6. **erstpruefung-und-mandatsziel** — Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.
7. **fachanwalt-medizinrecht-honorarvertrag-kv** — Honorarstreitigkeiten mit Kassenärztlicher Vereinigung begleiten: Anwendungsfall Vertragsarzt erhaelt Honorar-Bescheid m…
8. **fachanwalt-medizinrecht-behandlungsvertrag-630a** — Behandlungsvertrag nach §§ 630a-h BGB und Patientenrechte prüfen: Anwendungsfall Patient behauptet Behandlungsfehler ode…

---

## Skill: `einstieg-routing`

_Anwalts-Dashboard Fachanwalt Medizinrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt bleibt im Driver Seat._

# Anwalts-Dashboard Fachanwalt Medizinrecht

> Behandlungsfehler, Aufklärungsmangel, Approbation, MVZ, Apothekenrecht — drei Welten: Haftung, Berufsrecht, Vergütung.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | Keine klassische 2-Wochen-Frist im Patientenrecht, aber: § 199 BGB Verjährung 3 Jahre ab Kenntnis (regelmäßig). § 41 BÄO i. V. m. VwGO: 1 Monat Widerspruch gegen Approbationsbescheid. § 80 V VwGO: Eilantrag bei Ruhensanordnung. § 287 ZPO/§ 287a ZPO Beweismaßerleichterung Patientenseite. | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Behandlungsvertrag § 630a BGB · Aufklärung § 630e BGB · Dokumentation § 630f BGB · Beweisrechtsumkehr § 630h BGB · Schmerzensgeld § 253 II BGB · Schadensersatz §§ 280, 823 BGB · Approbation §§ 3, 5 BÄO · Verträge mit Krankenkassen § 75 SGB V. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Zivilklage Patient ↔ Arzt: LG (regelmäßig Spezialkammer Arzthaftung). Berufsrechtliche Sache: VG / OVG (§ 40 VwGO). Schlichtungsstelle Ärztekammer fakultativ. | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🟠 Verjährung Patientenanspruch tickt ab Kenntnis (§ 199 BGB) — Schweigen der Klinik schiebt die Frist NICHT hinaus. 🔴 Approbationswiderruf: 1 Monat Widerspruch + Aufschiebenhebungsantrag § 80 V VwGO.
- **Beweislage:** 🔴 Dokumentationslücke § 630h III BGB: Beweisrechtsumkehr zugunsten Patient. 🟠 Aufklärungsbeweis trägt der Arzt (§ 630h II BGB) — Aufklärungsbogen lückenlos prüfen.
- **Wirtschaftlich:** 🔴 Approbationsentzug = Berufsende — Eilrechtsschutz und parallel Strafverteidigung (z. B. § 95 BtMG, § 263 StGB). 🟠 MVZ-Anstellung: Wettbewerbsverbot und Übergangsversorgung.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Behandlungsfehler-Verdacht prüfen** | `behandlungsfehler-anspruch-pruefen` | Anspruchsgrundlagen § 630a/h BGB, Beweisrechtsumkehr, Sachverständige |
| Aufklärungspflichtverletzung | `aufklaerungspflicht-paragraf-630e-bgb` | Aufklärungsumfang, Zeitpunkt, Beweislast § 630h II BGB |
| Schlichtungsstelle prüfen | `gutachterkommission-aek-schlichtung` | Verfahrensvorteile, Hemmung der Verjährung § 204 I Nr. 4 BGB |
| Approbationsbescheid angreifen | `approbations-widerspruch` | Widerspruch 1 Monat, Aufschubantrag § 80 V VwGO, Berufseingriffsabwehr |
| Akteneinsicht / Befundherausgabe | `befundherausgabe-epa-akte` | Anspruch § 630g BGB, ePA-Spezifika, Verweigerung Vermerkbarkeit |

## Norm-Radar (live verifizieren)

- **§ 630a BGB** — Behandlungsvertrag
- **§ 630e BGB** — Aufklärungspflicht
- **§ 630f BGB** — Dokumentationspflicht
- **§ 630h BGB** — Beweislast bei Behandlungsfehler
- **§ 3 BÄO** — Approbation; Voraussetzungen und Widerruf
- **§ 199 BGB** — Verjährungsbeginn

## Genau eine Rückfrage (nur wenn nötig)

> Geht es um **Patient ↔ Behandler (Haftung)**, **Arzt/MVZ ↔ Behörde (Berufsrecht)** oder um **Vergütung / Kassenzulassung**?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Aufklärungspflicht § 630e BGB; Beweislast § 630h II BGB** — BGH VI. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Grober Behandlungsfehler; Beweislastumkehr § 630h V BGB** — BGH VI. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Dokumentationspflicht § 630f BGB; Folgen Lücken** — BGH VI. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Recht auf selbstbestimmtes Sterben** — BVerfG 2. Senat (Urteil v. 26.02.2020, 2 BvR 2347/15) — *live verifizieren auf* `bundesverfassungsgericht.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

---

## Skill: `mandat-triage-medizinrecht`

_Strukturierte Eingangs-Abfrage für medizinrechtliche Mandate: Klaert Mandantenrolle (Patient Arzt Krankenhaus Heilberufler Pharma Krankenkasse) Sachgebiet (Behandlungsfehler Aufklärungspflicht-Ve..._

# Strukturierte Eingangs-Abfrage für medizinrechtliche Mandate


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; BGB §§ 630a-h, MBO-Ä, GKV-Vorgaben, SGB V, PrüfvV, HeilberufsG der Länder; SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierte Eingangs-Abfrage für medizinrechtliche Mandate. Klaert Mandantenrolle (Patient Arzt Krankenhaus Heilberufler Pharma Krankenkasse) Sachgebiet (Behandlungsfehler Aufklärungspflicht-Verletzung Honorarstreit GOAe EBM Approbationsrecht Krankenhausrecht Heilmittelwerberecht Vertragsarztrecht KV-Recht Apotheken- und Arzneimittelrecht Pharmastrafrecht) Sofort-Fristen-Check Verjährung drei Jahre § 195 BGB ab Kenntnis Hoechstfrist dreissig Jahre Personenschaden § 199 Abs. 2 BGB Approbations-Widerruf-Verfahren Vorlaeufige Ruhensanordnung. Eskalation Telefon-Sofort bei Approbations-Verlust drohend. Routing zu behandlungsfehler-anspruch-prüfen.

### Mandat-Triage Medizinrecht

## Fachkern: Mandat-Triage Medizinrecht
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.

## Ablauf — acht Fragen

### Frage 1 — Mandantenrolle?

- Patient (Anspruch auf Schadensersatz)
- Niedergelassener Arzt (Verteidigung Honorar Approbation)
- Krankenhaus / Klinik (Haftpflicht Vertragsklinik)
- Hebamme / Pflegefachkraft
- Heilberufler (Heilpraktiker)
- Pharma- Medizinprodukte-Unternehmen
- Krankenkasse (Regress)
- Apotheker

### Frage 2 — Sachgebiet?

- Behandlungsfehler / Aufklärungsfehler / Dokumentation
- Wirtschaftliche Aufklärung § 630c Abs. 3 BGB
- Honorar GOÄ EBM
- Approbation Widerruf Ruhen Versagung
- Berufsrechtliches Verfahren Berufsgericht
- Vertragsarztrecht (Zulassung KV-Recht Plausibilitätsprüfung)
- Krankenhausrecht (Krankenhausplanung Vergütung Wahlleistung)
- Heilmittelwerberecht (HWG)
- Apotheken- Arzneimittelrecht
- Medizinprodukterecht MDR
- Pharmastrafrecht (Korruption im Gesundheitswesen § 299a § 299b StGB)
- Datenschutz im Gesundheitswesen

### Frage 3 — Akute Eilbedürftigkeit?

- Approbations-Widerruf / Ruhensanordnung sofort vollziehbar
- Strafverfahren Pharma-Korruption
- Existenzbedrohung Praxis
- Personenschaden akut vor Verjährung
- Krankenkassen-Regress drohend mit Verjährung
- Patientenverfügung lebensbedrohlich

### Frage 4 — Verfahrensstand?

- Beratungsbedarf (vor Klage Anzeige)
- Schlichtungsstelle Ärztekammer läuft
- Klage erhoben (LG bei Behandlungsfehler typisch Streitwert über EUR 10000 jetzt LG)
- Strafverfahren Ermittlungs- Anklage Hauptverhandlung
- Approbationsverfahren Widerspruch Klage Verwaltungsgericht
- Berufsgerichtliches Verfahren

### Frage 5 — Beteiligte?

- Behandler einzeln (Hauptverantwortlich)
- Behandler-Team Krankenhaus
- Haftpflichtversicherer
- Krankenkasse
- Krankenkassenverband KV
- Patientenanwalt Gegnerseite
- Sachverständigen-Gutachter

### Frage 6 — Dokumente?

- Patientenakte vollständig (Recht § 630g BGB)
- Aufklärungsbögen
- Gutachten Schlichtungsstelle MDK
- Strafanzeige Akten StA
- Approbationsakte Behörde

### Frage 7 — Frist?

- **Behandlungsfehler-Verjährung** drei Jahre / dreißig Jahre § 195 199 BGB
- **Strafverfahren** Verjährung je nach Tat
- **Approbationsanfechtung** ein Monat § 70 VwGO Widerspruch / ein Monat Klage
- **Schlichtungsstelle** keine Frist aber Hemmung Verjährung
- **Krankenkassen-Regress** vier Jahre § 199 SGB X

### Frage 8 — Versicherungs- und Vertragslage?

- Berufshaftpflicht Arzt / Klinik
- Rechtsschutz Patient
- Vertragsklinik-Vereinbarung
- Privat-/Kassenpatient

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Behandlungsfehler-Patient | `behandlungsfehler-anspruch-pruefen` |
| Behandlungsfehler-Arzt-Verteidigung | `behandlungsfehler-anspruch-pruefen` (Beweislast-Sicht) |
| Honorarstreit GOÄ EBM | (Skill arzt-honorar — perspektivisch) |
| Approbation-Widerruf | weiter an `mandat-triage-verwaltungsrecht` plus |
| KV-Plausibilitätsprüfung Regress | (Skill kv-regress — perspektivisch) |
| Pharma-Korruption § 299a StGB | weiter an `mandat-triage-strafrecht` plus |
| Heilmittelwerberecht | (Skill hwg-werberecht — perspektivisch) |
| Datenschutz Gesundheitswesen | weiter an `datenschutzrecht`-Plugin |

## Mandatsannahme

- **Konflikt-Check** — Patient/Arzt/Klinik/KK selbe Sache strikte Trennung
- **Streitwert** Schaden Schmerzensgeld
- **Sachverständigen-Bedarf** Patientenakten-Auswertung medizinisch
- **Versicherungsdeckung** Berufshaftpflicht Arzt prüfen
- **Schweigepflicht** § 203 StGB — Aufhebung durch Patient erforderlich

## Eskalation

- **Telefon-Sofort** Approbations-Ruhensanordnung sofort vollziehbar
- **Binnen einer Stunde** Polizei-Vernehmung Arzt Strafverfahren
- **Heute** Patientenakte anfordern § 630g BGB Schlichtungsantrag
- **Diese Woche** Klage-Erstentwurf Sachverständigenauftrag

## Ausgabe

- `triage-protokoll-medizinrecht.md`
- Aktenanlage
- Frist im Fristenbuch
- Schweigepflichtsentbindung als Entwurf
- Patientenakten-Anforderung § 630g BGB Entwurf
- Mandatsvereinbarung mit Honorarvereinbarung
- Empfehlung Folge-Skill

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen

- BGB §§ 195 199 253 630a–630h 823
- StGB §§ 203 222 229 299a 299b
- SGB V § 66 SGB X §§ 116 199
- BGH VI. Zivilsenat 5. Strafsenat
- Literatur nur bei vom Nutzer bereitgestellter oder lizenziert live geprüfter Quelle; keine Kommentarblindzitate.

## Vertiefung — Rechtsprechung und Normenkette

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Ergänzung — Wichtige Normen Triage-Routing

- § 195 BGB (regelmäßige Verjährung 3 Jahre) i.V.m. § 199 Abs. 1 BGB (Kenntnis-Beginn) und § 204 BGB (Hemmung durch Klage, Schlichtungsantrag, Mahnbescheid)
- § 630g BGB (Einsichtsrecht Patientenakte — unverzüglich zu gewähren, Kopien auf Kosten des Patienten)
- § 116 SGB X (Übergang Schadensersatzanspruch auf Sozialversicherungsträger)
- § 299a StGB (Bestechlichkeit im Gesundheitswesen), § 299b StGB (Bestechung im Gesundheitswesen)
- §§ 203, 204 StGB (Schweigepflicht, Schweigepflichtentbindung obligatorisch vor Aktenweitergabe)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `fachanwalt-medizinrecht-orientierung`

_Orientierung im Medizinrecht — FAO Voraussetzungen Normen typische Mandate Fristen verifizierbare Quellen. Arzthaftung §§ 630a ff. BGB (Patientenrechtegesetz seit 2013) Vertragsarztrecht SGB V Berufsrecht Aerzte (Berufsordnung Heilberufsgesetze Laender) Krankenhausrecht KHG Pflegeversicherungsrecht SGB XI Medizinprodukterecht MPDG Apothekenrecht ApoG. Schnittstelle Plugin fachanwalt-sozialrecht und kanzlei-allgemein._

# Fachanwalt für Medizinrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 60 Fälle in den letzten drei Jahren, davon mindestens 15 streitige.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Patientenrechte | §§ 630a–630h BGB (Behandlungsvertrag Aufklärung Dokumentation Beweislast) |
| Schadensrecht | §§ 249 ff. BGB §§ 823 ff. BGB Schmerzensgeld § 253 BGB |
| Krankenversicherung | SGB V §§ 27 ff. (Leistungen) §§ 73 ff. (Vertragsärzte) |
| Pflegeversicherung | SGB XI |
| Berufsrecht Ärzte | Berufsordnung der Ärztekammern Heilberufsgesetze der Länder |
| Krankenhaus | KHG KHEntgG |
| Medizinprodukte | MPDG (EU-MDR) |
| Apothekenrecht | ApoG ApBetrO Arzneimittelgesetz AMG |

## Typische Mandate

- Arzthaftung (Behandlungsfehler Aufklärungsfehler Dokumentationsmangel)
- Patientenanspruch auf Krankenversicherung-Leistungen (siehe `fachanwalt-sozialrecht`)
- Vertragsarztrecht (Zulassung Disziplinar Wirtschaftlichkeitsprüfung)
- Ärztliche Berufsrechtsverfahren
- Krankenhaus-Abrechnungsstreit (DRG)
- Medizinprodukteanmeldung Marktüberwachung
- Pflegeheim und Heimvertrag

## Fristen

- **Verjährung Schadensersatz Arzthaftung** regelmäßig drei Jahre ab Kenntnis (§ 195 BGB) Höchstfrist zehn Jahre (§ 199 Abs. 2 BGB).
- **Widerspruchsfrist Krankenkasse** ein Monat (§ 84 SGG).
- **Beschwerdefristen Ärztekammer** verfahrensrechtlich prüfen.
- **Vertragsarztzulassung** Klagefrist gegen Beschluss des Zulassungsausschusses ein Monat (§ 96 Abs. 4 SGB V iVm SGG).

## Hauptgerichte

- Sozialgericht (Krankenversicherung).
- Zivilgericht (Arzthaftung): Landgericht regelmäßig Streitwertgrenze 10.000 EUR (Streitwertgrenze AG ab 01.01.2026).
- Verwaltungsgericht (Berufsrecht Krankenhausrecht).
- BGH VI. Zivilsenat (Arzthaftung) und Bundessozialgericht.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- ARGE Medizinrecht DAV.
- Deutsche Gesellschaft für Medizinrecht.

## Schnittstellen

- **fachanwalt-sozialrecht** bei SGB V SGB XI.
- **kanzlei-allgemein** Fristen Versand.
- **fachanwalt-strafrecht** bei Vorwurf Behandlungsfehler mit strafrechtlichem Bezug.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Paragrafenkette

Arzthaftung: §§ 630a, 630b, 630c, 630d, 630e, 630f, 630g, 630h BGB → § 823 Abs. 1 BGB → § 253 BGB (Schmerzensgeld) → §§ 195, 199 BGB (Verjährung)

Vertragsarztrecht: §§ 95, 87b, 106, 106d, 81 Abs. 5 SGB V → § 51 SGG → §§ 84, 87 SGG

Berufsrecht: § 5 BÄO (Widerruf Approbation) → §§ 6a, 8 BÄO → Heilberufsgesetze der Länder → MBO-Ä

Krankenhausrecht: KHG, KHEntgG, § 108 SGB V (Zulassung) → DRG-Abrechnungsregelungen

Medizinprodukte: MPDG (Umsetzung EU-MDR 2017/745) → § 97 AMG (Arzneimittelhaftung analog)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Fristen-Übersicht

| Mandatstyp | Frist | Norm |
|---|---|---|
| Arzthaftungs-Verjährung | 3 Jahre ab Kenntnis | §§ 195, 199 BGB |
| Arzthaftungs-Höchstfrist (Personenschaden) | 30 Jahre | § 199 Abs. 2 BGB |
| Widerspruch Krankenkasse / KV | 1 Monat | § 84 SGG |
| Klage Sozialgericht | 1 Monat nach Widerspruchsbescheid | § 87 SGG |
| Widerruf Approbation — Widerspruch VwGO | 1 Monat | § 70 VwGO |
| Klage Verwaltungsgericht (Approbation) | 1 Monat | § 74 VwGO |

## Triage — Sofortprüfung (Fachanwalt Medizinrecht — Orientierung)

1. **Mandantenrolle klären:** Patient (Anspruchsteller), Arzt/Heilberufler (Verteidigungs-Mandat), Krankenhaus, Kasse?
2. **Sachgebiet identifizieren:**
   - Arzthaftung → `behandlungsfehler-anspruch-pruefen` oder `aufklaerungsfehler-beweisstrategie`
   - Vertragsarztrecht → `fachanwalt-medizinrecht-kassenarztrecht`
   - Approbationsrecht → `fachanwalt-medizinrecht-approbations-widerspruch`
   - Off-Label / GKV-Leistungsrecht → `fachanwalt-medizinrecht-off-label-use-erstattung-gkv-long-covid`
   - Schlichtung Ärztekammer → `fachanwalt-medizinrecht-gutachterkommission-aek-schlichtung`
3. **Eilbedürftigkeit prüfen:**
   - Approbationsruhensanordnung sofort vollziehbar → Eilantrag § 80 Abs. 5 VwGO / § 86b SGG binnen 24 h.
   - Verjährung läuft in < 4 Wochen → Hemmungshandlung sofort (Klage, Mahnbescheid, Anmeldung Schlichtungsstelle).
4. **Rechtsweg bestimmen:** Sozialgericht (Vertragsarzt, KV, GKV), Zivilgericht (Arzthaftung, GOÄ), Verwaltungsgericht (Berufsrecht, Approbation), Landesberufsgericht (Berufsrecht).

**Routing:**
```
Sachgebiet?
├─ Behandlungsfehler / Aufklärung → behandlungsfehler-anspruch-pruefen
├─ Vertragsarztrecht / KV → fachanwalt-medizinrecht-kassenarztrecht
├─ Approbation / Widerruf → fachanwalt-medizinrecht-approbations-widerspruch
├─ GKV-Leistungsstreit → fachanwalt-sozialrecht
├─ Honorar GOÄ → fachanwalt-medizinrecht-honorarvertrag-kv
└─ Schlichtung Ärztekammer → fachanwalt-medizinrecht-gutachterkommission-aek-schlichtung
```

---

## Skill: `orientierung-mandat-fachanwaltschaft`

_Orientierung im Medizinrecht — FAO Voraussetzungen Normen typische Mandate Fristen verifizierbare Quellen: Arzthaftung §§ 630a ff. BGB (Patientenrecht..._

# Orientierung im Medizinrecht — FAO Voraussetzungen Normen typische Mandate Fristen verifizierbare Quellen


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; BGB §§ 630a-h, MBO-Ä, GKV-Vorgaben, SGB V, PrüfvV, HeilberufsG der Länder; SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung im Medizinrecht — FAO Voraussetzungen Normen typische Mandate Fristen verifizierbare Quellen. Arzthaftung §§ 630a ff. BGB (Patientenrechtegesetz seit 2013) Vertragsarztrecht SGB V Berufsrecht Aerzte (Berufsordnung Heilberufsgesetze Länder) Krankenhausrecht KHG Pflegeversicherungsrecht SGB XI Medizinprodukterecht MPDG Apothekenrecht ApoG. Schnittstelle Plugin fachanwalt-sozialrecht und kanzlei-allgemein.

### Fachanwalt für Medizinrecht — Orientierung

## Fachkern: Fachanwalt für Medizinrecht — Orientierung
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 60 Fälle in den letzten drei Jahren, davon mindestens 15 streitige.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Patientenrechte | §§ 630a–630h BGB (Behandlungsvertrag Aufklärung Dokumentation Beweislast) |
| Schadensrecht | §§ 249 ff. BGB §§ 823 ff. BGB Schmerzensgeld § 253 BGB |
| Krankenversicherung | SGB V §§ 27 ff. (Leistungen) §§ 73 ff. (Vertragsärzte) |
| Pflegeversicherung | SGB XI |
| Berufsrecht Ärzte | Berufsordnung der Ärztekammern Heilberufsgesetze der Länder |
| Krankenhaus | KHG KHEntgG |
| Medizinprodukte | MPDG (EU-MDR) |
| Apothekenrecht | ApoG ApBetrO Arzneimittelgesetz AMG |

## Typische Mandate

- Arzthaftung (Behandlungsfehler Aufklärungsfehler Dokumentationsmangel)
- Patientenanspruch auf Krankenversicherung-Leistungen (siehe `fachanwalt-sozialrecht`)
- Vertragsarztrecht (Zulassung Disziplinar Wirtschaftlichkeitsprüfung)
- Ärztliche Berufsrechtsverfahren
- Krankenhaus-Abrechnungsstreit (DRG)
- Medizinprodukteanmeldung Marktüberwachung
- Pflegeheim und Heimvertrag

## Fristen

- **Verjährung Schadensersatz Arzthaftung** regelmäßig drei Jahre ab Kenntnis (§ 195 BGB) Höchstfrist zehn Jahre (§ 199 Abs. 2 BGB).
- **Widerspruchsfrist Krankenkasse** ein Monat (§ 84 SGG).
- **Beschwerdefristen Ärztekammer** verfahrensrechtlich prüfen.
- **Vertragsarztzulassung** Klagefrist gegen Beschluss des Zulassungsausschusses ein Monat (§ 96 Abs. 4 SGB V iVm SGG).

## Hauptgerichte

- Sozialgericht (Krankenversicherung).
- Zivilgericht (Arzthaftung): Landgericht regelmäßig Streitwertgrenze 10.000 EUR (Streitwertgrenze AG ab 01.01.2026).
- Verwaltungsgericht (Berufsrecht Krankenhausrecht).
- BGH VI. Zivilsenat (Arzthaftung) und Bundessozialgericht.

## Berufsverband

- ARGE Medizinrecht DAV.
- Deutsche Gesellschaft für Medizinrecht.

## Schnittstellen

- **fachanwalt-sozialrecht** bei SGB V SGB XI.
- **kanzlei-allgemein** Fristen Versand.
- **fachanwalt-strafrecht** bei Vorwurf Behandlungsfehler mit strafrechtlichem Bezug.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Paragrafenkette

Arzthaftung: §§ 630a, 630b, 630c, 630d, 630e, 630f, 630g, 630h BGB → § 823 Abs. 1 BGB → § 253 BGB (Schmerzensgeld) → §§ 195, 199 BGB (Verjährung)

Vertragsarztrecht: §§ 95, 87b, 106, 106d, 81 Abs. 5 SGB V → § 51 SGG → §§ 84, 87 SGG

Berufsrecht: § 5 BÄO (Widerruf Approbation) → §§ 6a, 8 BÄO → Heilberufsgesetze der Länder → MBO-Ä

Krankenhausrecht: KHG, KHEntgG, § 108 SGB V (Zulassung) → DRG-Abrechnungsregelungen

Medizinprodukte: MPDG (Umsetzung EU-MDR 2017/745) → § 97 AMG (Arzneimittelhaftung analog)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Fristen-Übersicht

| Mandatstyp | Frist | Norm |
|---|---|---|
| Arzthaftungs-Verjährung | 3 Jahre ab Kenntnis | §§ 195, 199 BGB |
| Arzthaftungs-Höchstfrist (Personenschaden) | 30 Jahre | § 199 Abs. 2 BGB |
| Widerspruch Krankenkasse / KV | 1 Monat | § 84 SGG |
| Klage Sozialgericht | 1 Monat nach Widerspruchsbescheid | § 87 SGG |
| Widerruf Approbation — Widerspruch VwGO | 1 Monat | § 70 VwGO |
| Klage Verwaltungsgericht (Approbation) | 1 Monat | § 74 VwGO |

## Triage — Sofortprüfung (Fachanwalt Medizinrecht — Orientierung)

1. **Mandantenrolle klären:** Patient (Anspruchsteller), Arzt/Heilberufler (Verteidigungs-Mandat), Krankenhaus, Kasse?
2. **Sachgebiet identifizieren:**
 - Arzthaftung → `behandlungsfehler-anspruch-pruefen` oder `aufklaerungsfehler-beweisstrategie`
 - Vertragsarztrecht → `fachanwalt-medizinrecht-kassenarztrecht`
 - Approbationsrecht → `fachanwalt-medizinrecht-approbations-widerspruch`
 - Off-Label / GKV-Leistungsrecht → `fachanwalt-medizinrecht-off-label-use-erstattung-gkv-long-covid`
 - Schlichtung Ärztekammer → `fachanwalt-medizinrecht-gutachterkommission-aek-schlichtung`
3. **Eilbedürftigkeit prüfen:**
 - Approbationsruhensanordnung sofort vollziehbar → Eilantrag § 80 Abs. 5 VwGO / § 86b SGG binnen 24 h.
 - Verjährung läuft in < 4 Wochen → Hemmungshandlung sofort (Klage, Mahnbescheid, Anmeldung Schlichtungsstelle).
4. **Rechtsweg bestimmen:** Sozialgericht (Vertragsarzt, KV, GKV), Zivilgericht (Arzthaftung, GOÄ), Verwaltungsgericht (Berufsrecht, Approbation), Landesberufsgericht (Berufsrecht).

**Routing:**
```
Sachgebiet?
├─ Behandlungsfehler / Aufklärung → behandlungsfehler-anspruch-pruefen
├─ Vertragsarztrecht / KV → fachanwalt-medizinrecht-kassenarztrecht
├─ Approbation / Widerruf → fachanwalt-medizinrecht-approbations-widerspruch
├─ GKV-Leistungsstreit → fachanwalt-sozialrecht
├─ Honorar GOÄ → fachanwalt-medizinrecht-honorarvertrag-kv
└─ Schlichtung Ärztekammer → fachanwalt-medizinrecht-gutachterkommission-aek-schlichtung
```

---

## Skill: `erstgespraech-mandatsannahme`

_Erstgespraeach und Mandatsannahme im Arzthaftungs- Berufs- und Vertragsarztrecht: Anwendungsfall Patient oder Arzt meldet sich mit unstrukturiertem Sachverhalt zu Behandlungsfehler Approbationsproblem oder KV-Streit: Erstgespraeach und Mandatsannahme im Arz..._

# Erstgespraeach und Mandatsannahme im Arzthaftungs- Berufs- und Vertragsarztrecht: Anwendungsfall Patient oder Arzt meldet sich mit unstrukturiertem Sachverhalt zu Behandlungsfehler Approbationsproblem oder KV-Streit


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; BGB §§ 630a-h, MBO-Ä, GKV-Vorgaben, SGB V, PrüfvV, HeilberufsG der Länder; SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Erstgespraeach und Mandatsannahme im Arzthaftungs- Berufs- und Vertragsarztrecht: Anwendungsfall Patient oder Arzt meldet sich mit unstrukturiertem Sachverhalt zu Behandlungsfehler Approbationsproblem oder KV-Streit. § 630a BGB Behandlungsvertrag, § 43a BRAO Interessenkonflikte, § 3a RVG Honorar. Prüfraster Konstellation einordnen Arzthaftung Berufsrecht oder Vertragsarztrecht, Interessenkonflikt-Check, Vollmacht einholen, Streitwert und Gebührenvereinbarung, Fristen-Erstprognose. Output Mandats-Aufnahmeprotokoll mit Einordnung Sofortmassnahmen und Handlungsweichen. Abgrenzung zu Mandat-Triage-Medizinrecht und zu Erstgespraeach-Strafrecht.

### Erstgespraech und Mandatsannahme im Arzthaftungs-, Berufs- und Vertragsarztrecht

## Fachkern: Erstgespraech und Mandatsannahme im Arzthaftungs-, Berufs- und Vertragsarztrecht
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Arzthaftungs-, Berufs- und Vertragsarztrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klären, Konflikt- und GwG-Prüfung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Arzthaftungs-, Berufs- und Vertragsarztrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klägerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Behandlungsfehler, Aufklaerung, Sozialrecht/SGB V, Praxisuebernahme, MBO-AE
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Arzthaftungsklage, Klage Sozialgericht (KV-/MDK-Streit), Berufsrechtsbeschwerde). Frist-Alarm an die Vorbereitung weitergeben.

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

Standard-Streitwerte im Bereich Arzthaftungs-, Berufs- und Vertragsarztrecht:

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

- BORA, BRAO, FAO für Fachanwaltschaft Arzthaftungs-, Berufs- und Vertragsarztrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- §§ 630a ff. BGB, MBO-AE, SGB V, MPDG, GOAE, BAEO (für fachliche Erstpruefung).
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

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Arzthaftungs-, Berufs- und Vertragsarztrecht). Handlungs-Sequenz:

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
- Verfahrensdauer im Bereich Arzthaftungs-, Berufs- und Vertragsarztrecht: Erfahrungswerte nach Instanz.
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

## Vertiefung — Normenkette und Rechtsprechung Erstgespräch Medizinrecht

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normenkette Erstgespräch / Mandatsannahme

§ 630g BGB (Einsichtsrecht Patientenakte) → §§ 10, 11 GwG (Identifizierungspflicht RA-Mandat) → §§ 43a, 45 BRAO (Interessenkonflikt, Verschwiegenheit) → §§ 3, 3a RVG (Vergütungsvereinbarung, Stundenhonorar) → § 9 RVG (Vorschuss) → §§ 195, 199 BGB (Verjährung im Mandat sichern) → § 204 BGB (Hemmung: Klage, Mahnbescheid, Schlichtungsantrag § 278 BGB analog)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `erstpruefung-und-mandatsziel`

_Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; BGB §§ 630a-h, MBO-Ä, GKV-Vorgaben, SGB V, PrüfvV, HeilberufsG der Länder; SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.

## Fachkern: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.

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

## Skill: `fachanwalt-medizinrecht-honorarvertrag-kv`

_Honorarstreitigkeiten mit Kassenärztlicher Vereinigung begleiten: Anwendungsfall Vertragsarzt erhaelt Honorar-Bescheid mit Kuestzungen oder Wirtschaftlichkeits- oder Plausibilitaetsprüfung laeuft. EBM Einheitlicher Bewertungsmassstab, RLV Regelleistungsvolumen, QZV qualifikationsgebundene Zusatzleistungen, § 106 SGB V Wirtschaftlichkeitsprüfung. Prüfraster Honorar-Bescheid prüfen, Wirtschaftlichkeitsprüfung-Status, Plausibilitaets-Grenzwerte, Widerspruch und Klage-Optionen. Output Widerspruchs-Schriftsatz mit Begründung für KV-Honorarstreit. Abgrenzung zu Kassenarztrecht für allgemeine Vertragsarztzulassung und zu Schriftsatzkern._

# Honorarvertrag Kassenärztliche Vereinigung

## Zweck

Mandate für Vertragsärzte bei Honorar-Streitigkeiten mit Kassenärztlicher Vereinigung (KV).

## 1) Eingangs-Abfrage

1. Fachgruppe (Allgemein, Internist, Chirurg, Psychiater)?
2. Honorar-Bescheid-Stand?
3. Wirtschaftlichkeits-Prüfung laufend?
4. Plausibilitaets-Prüfung?
5. Niederlassung neu / etabliert?
6. KV-Region?

## 2) Honorar-System

### EBM (Einheitlicher Bewertungsmasstab)

- Punktwert × Punkte = Honorar
- Pauschalen, Versicherten-Pauschale, Zusatzleistungen

### Regelleistungsvolumen (RLV)

- Quartalsweise Budget pro Arzt
- Bei UEberschreitung: gestaffelt geringere Vergütung
- Berechnung nach Vorgaben KV

### Qualifikationsgebundene Zusatzleistungen (QZV)

- Spezielle Leistungen außerhalb RLV
- Voraussetzung: Genehmigung Qualifikation

## 3) Prüfverfahren

### Plausibilitaets-Prüfung

- Bei Auffaelligkeiten (z.B. zu viele Patienten/Tag)
- Stichproben aus Abrechnungs-Daten
- Folge: Honorar-Kürzung bei Bestätigung

### Wirtschaftlichkeits-Prüfung § 106 SGB V

- Bei Mehr-Verordnung Heilmittel/Arzneimittel
- Vergleich Fachgruppen-Durchschnitt
- Bei UEberschreitung: Regress-Verfahren

### Honoraranfechtung

- Anwaltliche Prüfung der KV-Daten
- Vergleich Eigen-Berechnung
- Beweis-Anbringen

## 4) Workflow Widerspruch

### Schritt 1 — Bescheid-Prüfung

- Berechnungs-Grundlagen
- Fachgruppen-Vergleich
- RLV-Berechnung

### Schritt 2 — Eigene Berechnung

- Patienten-Statistik
- Leistungs-Spiegel
- Vergleich Vorquartale

### Schritt 3 — Widerspruch

- Binnen 1 Monat
- An KV
- Begründung mit Daten

### Schritt 4 — Klage

- Sozialgericht (SG)
- Streitwert nach Differenz-Honorar

## 5) Wirtschaftlichkeits-Prüfung

### Stufen

1. **Beratung** (formlos, ohne Sanktion)
2. **Statistische Prüfung** (Fachgruppen-Vergleich)
3. **Regress** (Rückzahlung)
4. **Maßnahmen-Klage** SG

### Verteidigung

- Praxisbesonderheiten geltend machen
- Patienten-Klientel besonders behandeln
- Behandlungs-Notwendigkeit nachweisen

## 6) Niederlassungs-Sache

### Zulassung § 95 SGB V

- KV-Bezirk hat Vertragsarzt-Bedarf
- Bedarfsplanung
- Bei Bedarfs-Mangel: Zulassungs-Ablehnung

### Praxis-Verkauf / Übergabe

- Kollegial-Praxis vs. Praxis-Sitz-Verkauf
- KV-Genehmigung erforderlich
- Bewertung Goodwill nach BAG-Aerztl.-Vereinigung

## 7) Honorar-Auseinandersetzung Praxis-Aufgabe

- KV-Endabrechnung
- Rückforderungen
- Sonderfälle (Krankheit, Pensionierung)

## 8) Typische Fehler

1. **Widerspruchs-Frist 1 Monat versäumt**
2. **Praxisbesonderheiten** nicht dokumentiert
3. **Patienten-Statistik** unvollständig
4. **RLV-Berechnung** nicht überprüft

## 9) Sozialgericht

- Kostenfrei für KV-Streitigkeiten (keine Gerichtskosten)
- Rechtsanwaltskosten nach RVG
- Aufschiebende Wirkung Widerspruch — bei Bescheiden meist sofort vollziehbar

## 10) BSG-Linien

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Anschluss

- `fachanwalt-medizinrecht-behandlungsvertrag-630a` — bei Behandlung
- `fachanwalt-sozialrecht-orientierung` — bei SG-Triage
- `fachanwalt-medizinrecht-orientierung` — Plugin-Triage

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Paragrafenkette

§ 87b SGB V (Honorarverteilungsmaßstab) → § 106 SGB V (Wirtschaftlichkeitsprüfung) → § 106a SGB V (Qualitätsprüfung) → § 106d SGB V (Plausibilitätsprüfung) → § 95 SGB V (Zulassung) → § 95 Abs. 6 SGB V (Zulassungsentziehung) → § 51 SGG (Sozialgerichtsweg) → § 86b SGG (Einstweiliger Rechtsschutz).

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Fristen

| Frist | Dauer | Norm |
|---|---|---|
| Widerspruch beim Berufungsausschuss | 1 Monat ab Bescheid | § 96 Abs. 4 SGB V |
| Klage beim SG | 1 Monat ab Berufungsausschussbescheid | § 87 SGG |
| Aussetzungsantrag bei sofort vollziehbarem Bescheid | unverzüglich | § 86b Abs. 1 SGG |

## Triage — Sofortprüfung

Bevor losgelegt wird, kläre:

1. **Welches Quartal ist betroffen?** — Widerspruchsfrist berechnen; KV-Bescheid enthält oft knappe Fristen.
2. **Praxisbesonderheiten dokumentiert?** — Patientenstruktur, Krankheitsbilder, Schwerpunktversorgung als Belege vorbereiten.
3. **RLV-Berechnung nachvollziehbar?** — Eigene Berechnung mit KV-Daten abgleichen; Differenz als Argumentationsgrundlage.
4. **Wirtschaftlichkeitsprüfung oder Plausibilitätsprüfung?** — Unterschiedliche Verfahren, unterschiedliche Verteidigungswege.
5. **Zulassung gefährdet?** — Bei Mehrfachverstößen parallel Verhältnismäßigkeitsprüfung § 95 Abs. 6 SGB V vorbereiten.

**Entscheidungsbaum:**
- Plausibilitätsprüfung → Anhörung § 24 SGB X nutzen; Stichprobenpatienten konkret darstellen
- Wirtschaftlichkeitsprüfung → Praxisbesonderheiten konkret belegen; Vergleichsgruppe rügen
- Zulassungsentziehung → Verhältnismäßigkeit (Ruhen als mildere Maßnahme); Eilantrag § 86b SGG
- Regress-Bescheid → Widerspruch beim Berufungsausschuss; parallel Aussetzung beantragen
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Widerspruch Honorarbescheid KV | Widerspruchsschreiben; Template unten |
| Variante A — Richtgroessen-Regress droht | Beratung vor Bescheid; Stellungnahme im Anhoerungs-Stadium |
| Variante B — Zulaessige Mehrfachabrechnung streitig | GOAe / EBM-Kommentar pruefen; Nachweisdokumentation |
| Variante C — Zulassungsentziehung droht | Sofortiger Widerspruch + Eilantrag; Strafverfahren koordinieren |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template Widerspruch Honorarbescheid

**Adressat:** KV / Berufungsausschuss — Tonfall: sachlich-juristisch

```
An die Kassenärztliche Vereinigung [Bundesland]
Widerspruchsstelle

Widerspruch gegen den Honorarbescheid Quartal [Q/JJJJ]
Az. [...]

I. Sachverhalt
Die Praxis [Name, LANR] hat im Quartal [Q/JJJJ] aufgrund folgender
Praxisbesonderheiten das Regelleistungsvolumen ueberschritten:
[Schwerpunktversorgung; atypische Patientenstruktur; Belegaerztliche Taetigkeit]

II. Rechtsfehler
1. Die Berechnung des RLV nach § 87b SGB V weicht von der
   Fachgruppenentwicklung ab; unsere Gegenberechnung ergibt EUR [Differenz].
2. Praxisbesonderheiten wurden nicht beruecksichtigt (Belege Anlagen K1-K3).

III. Antrag
Aufhebung des Honorarbescheids und Neuberechnung unter Beruecksichtigung
der Praxisbesonderheiten.

IV. Aussetzung Vollziehung
Bei sofortiger Vollziehbarkeit beantragen wir Aussetzung § 86b Abs. 1 SGG.

Anlagen: Patientenstatistik, Diagnoseprofile, eigene RLV-Berechnung, Vollmacht
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `fachanwalt-medizinrecht-behandlungsvertrag-630a`

_Behandlungsvertrag nach §§ 630a-h BGB und Patientenrechte prüfen: Anwendungsfall Patient behauptet Behandlungsfehler oder Aufklärungsmangel oder Arzt braucht Vertragsdokumentation. §§ 630a-h BGB Behandlungsvertrag, § 630h BGB Beweislastumkehr bei grobem Behandlungsfehler, § 630g BGB Akteneinsichtsrecht. Prüfraster Behandlungsstandard § 630a Abs. 2, Aufklärungspflicht § 630e, Dokumentationspflicht § 630f, Beweislast und Umkehr bei grobem Fehler. Output Prüfprotokoll Behandlungsvertrag mit Anspruchsgrundlagen und Beweislage. Abgrenzung zu Behandlungsfehler-Anspruch-Prüfen und zu Gutachterkommission._

# Behandlungsvertrag §§ 630a-h BGB

## Zweck

Rechtliche Beziehung Arzt-Patient seit Patientenrechtegesetz 2013 kodifiziert. Pflichten, Beweisregeln, Patientenrechte.

## 1) Pflichten Behandelnder

### Behandlung nach Stand med. Wissenschaft § 630a II BGB

- Sorgfaltspflicht des allg. anerkannten fachlichen Standards
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Aufklärung § 630e BGB

- **Vor** Behandlung
- Inhalt: Art, Umfang, Verlauf, Folgen, Risiken, Alternativen
- **Eigenhaendige Unterschrift** des Patienten empfohlen

### Einwilligung § 630d BGB

- Aufklärungsbasiert
- Bei Notfall: mutmassliche Einwilligung
- Bei Minderjaehrigen: Eltern, ggf. Einsichtsfähigkeit ab 14

### Dokumentation § 630f BGB

- **Patientenakte** in Schriftform / elektronisch
- Pflichten: Anamnese, Diagnose, Behandlung, Aufklärung, Befunde
- Aufbewahrung 10 Jahre

## 2) Beweislast-Umkehr bei groben Behandlungsfehlern § 630h V BGB

### Voraussetzung

- **Grober Behandlungsfehler**: Verstoß gegen elementare Behandlungsregel
- Geeignet, festgestellte Gesundheitsverletzung herbeizuführen

### Folge

- Arzt muss beweisen, dass Fehler **nicht** kausal war
- Praktisch sehr schwer

### Beispiele (BGH-Linie)

- Röntgen-Befund übersehen
- Reanimation unterbrochen
- Operation am falschen Bein
- Hygiene-Standards grob verletzt

## 3) Aufklärungsmangel

### Voraussetzungen

- Aufklärung unterblieb oder unvollständig
- Hypothetische Einwilligung des Patienten widerlegt

### Folge

- Eingriff ist **rechtswidrig** (auch bei korrekter Durchführung)
- Schadensersatz + Schmerzensgeld

### Beweislast

- Arzt muss Aufklärung beweisen (Schriftform empfohlen)

## 4) Patientenrechte

### Akteneinsicht § 630g BGB

- Patient kann Akteneinsicht verlangen
- Kostenpflichtige Kopie (typisch 0,50/Seite)
- Bei Verweigerung: Klage am Amtsgericht

### Schweigepflicht § 203 StGB

- Strafrechtliche Pflicht
- Ausnahmen: Einwilligung, gesetzliche Pflicht (Infektionsschutz)

## 5) Workflow Behandlungsfehler-Mandat

### Schritt 1 — Sachverhaltsaufnahme

- Behandlungs-Verlauf
- Mangel-Beschreibung
- Gesundheitsfolge

### Schritt 2 — Akteneinsicht

- Antrag § 630g BGB
- Bei Verweigerung: Klage

### Schritt 3 — Vorgutachten

- MDK (gesetzlich Versicherte)
- Privatgutachten
- Schlichtungs-Stelle der Ärztekammer

### Schritt 4 — Verhandlung / Klage

- Vergleich mit Versicherer
- Bei Streit: LG (Streitwert + 5.000 EUR Grenze)
- Beweisaufnahme Sachverständiger

## 6) Schadensersatz / Schmerzensgeld

- Behandlungs-Mehrkosten
- Verdienstausfall
- Erwerbsminderungs-Rente bei Dauerschaden
- Schmerzensgeld nach BGH-Schmerzensgeld-Tabelle

## 7) Verjaehrung

- 3 Jahre ab Kenntnis Patient
- Hoechstens 30 Jahre ab Eintritt der Verletzung
- § 199 BGB

## 8) Typische Fehler

1. **Aufklärungs-Beweis fehlt** Arztes -> rechtswidriger Eingriff
2. **Akteneinsicht verweigert** -> Schaden Patient
3. **MDK-Gutachten als alleinige Grundlage** — oft Mandanten-feindlich

## 9) BGH-Linien

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Anschluss

- `behandlungsfehler-anspruch-pruefen` — Prüfraster
- `fachanwalt-medizinrecht-approbations-widerspruch` — bei AErzte-Mandat
- `aufklaerungsfehler-beweisstrategie` — Beweis-Strategie

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Paragrafenkette

§ 630a BGB (Behandlungsvertrag) → § 630a Abs. 2 BGB (Standardpflicht) → § 630e BGB (Aufklärung) → § 630d BGB (Einwilligung) → § 630f BGB (Dokumentation) → § 630g BGB (Akteneinsicht) → § 630h BGB (Beweislast) → § 280 Abs. 1 BGB (Schadensersatz) → § 823 Abs. 1 BGB (Delikt) → § 253 Abs. 2 BGB (Schmerzensgeld).

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage — Sofortprüfung bei Mandatsannahme

Bevor losgelegt wird, kläre sofort:

1. **Welche Frist droht?** — Verjährung läuft 3 Jahre ab Jahresende der Kenntnis (§§ 195, 199 BGB); bei unbekanntem Fehler absolute Höchstfrist 30 Jahre.
2. **Dokumentation angefordert?** — § 630g BGB; ohne vollständige Akte keine Begutachtung möglich.
3. **GKV oder Privatpatient?** — Bei GKV: MDK-Gutachten parallel beantragen (§ 66 SGB V); Regressinteresse GKV (§ 116 SGB X) koordinieren.
4. **Grobes Verschulden erkennbar?** — Bei Beweislastumkehr § 630h Abs. 5 BGB ist die Klagestrategie anders als ohne.
5. **Schlichtungsverfahren sinnvoll?** — Ärztekammer-Schlichtung hemmt Verjährung und liefert kostenloses Sachverständigengutachten.

**Entscheidungsbaum:**
- Grobes Verschulden eindeutig → Direktklage (§ 630h Abs. 5 BGB als zentrales Argument)
- Sachverhalt ungeklärt → Schlichtung zuerst
- Verjährung in < 3 Monaten → sofort Hemmungsmaßnahme (Güteantrag, Klage)
- Tod des Patienten → Erbenklage; Schmerzensgeld vererbt (§ 253 BGB n.F.)
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Behandlungsvertrag § 630a Erstberatung | Mandantenschreiben nach Erstgespraech; Template unten |
| Variante A — Privatpatient will Kosten reduzieren | GOAe-Minderung aushandeln; Beratung Honorarrecht |
| Variante B — GKV-Versicherter ausserhalb Leistungskatalog | Kostenuebernahmeregelung pruefen; Widerspruch gegen Ablehnung |
| Variante C — Behandlungsabbruch durch Arzt | Aufhebungsvereinbarung; Weiterbehandlungspflicht pruefen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template Mandantenschreiben nach Erstgespräch

**Adressat:** Mandant — Tonfall: verständlich-erklärend

```
Sehr geehrte/r [MANDANT],

nach Durchsicht der Unterlagen und unserem Gespraeach halte ich folgendes
zum Mandat fest:

Sachverhalt: [Behandlung Datum Einrichtung Fehler]
Naechste Schritte:
1. Anforderung der vollstaendigen Patientenakte bei [EINRICHTUNG] § 630g BGB
   Frist: 14 Tage — wir schreiben heute noch.
2. Schlichtungsantrag bei der [AERZTEKAMMER] — kostenlos; hemmt Verjaehrung.
3. Verjaehrungsfrist beachten: Aktuell laeuft sie bis [DATUM].
Kosten: [STREITWERT] — Ihre Rechtsschutzversicherung pruefe ich.
Mit freundlichen Gruessen
[KANZLEI]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

