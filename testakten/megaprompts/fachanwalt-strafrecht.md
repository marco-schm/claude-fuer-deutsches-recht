# Megaprompt: fachanwalt-strafrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 240 Skills (gekuerzt fuer Chat-Fenster) des Plugins `fachanwalt-strafrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Anwalts-Dashboard Fachanwalt Strafrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zus…
2. **mandat-triage-strafrecht** — Strukturierte Eingangs-Abfrage für Strafmandate: Klaert Verfahrensstadium (Ermittlungs- Zwischen- Hauptverfahren Vollstr…
3. **fachanwalt-strafrecht-orientierung** — Orientierung im Strafrecht-Mandat und Workflow-Routing: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss St…
4. **orientierung-mandat-fachanwaltschaft** — Orientierung im Strafrecht-Mandat und Fallrouting: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafre…
5. **orientierung-fristen-form-und-zustaendigkeit** — Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg: Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg.
6. **erstgespraech-mandatsannahme** — Erstgespraeach und Mandatsannahme im Strafrecht: Anwendungsfall Beschuldigter oder Verdaechtiger meldet sich nach Polize…
7. **erstpruefung-und-mandatsziel** — Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.
8. **fachanwalt-strafrecht-zeugenbeistand** — Zeugenbeistand im Strafverfahren für Zeugen mit eigenem Rechtsinteresse: Anwendungsfall Person ist als Zeuge geladen hat…

---

## Skill: `einstieg-routing`

_Anwalts-Dashboard Fachanwalt Strafrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt bleibt im Driver Seat._

# Anwalts-Dashboard Fachanwalt Strafrecht

> Vorladung, Durchsuchung, U-Haft, Anklage, Revision — Verfahrensphase entscheidet alles. Identität des Beschuldigten zuerst klären.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 311 II StPO: 1 Woche** sofortige Beschwerde. § 314 StPO: Berufung 1 Woche ab Verkündung. § 341 StPO: Revision 1 Woche ab Verkündung; § 345 StPO: Begründung 1 Monat ab Zustellung. § 33a StPO (Haftprüfung jederzeit). § 67 OWiG: Einspruch Bußgeld 2 Wochen. | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Hier kein klassischer Anspruch: Tatvorwurf benennen (Norm + StGB- bzw. Nebenstrafrechts-§). Mitwirkung: Akteneinsicht § 147 StPO, Beweisantrag § 244 StPO, Verteidigerwahl § 137 StPO, Pflichtverteidigung § 140 StPO. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | AG Strafrichter / Schöffengericht (§§ 24 ff. GVG), LG große Strafkammer (§ 74 GVG), OLG (Staatsschutz, § 120 GVG). Bei Jugendlichen: JGG-Spruchkörper. | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Sofortige Beschwerde (1 Woche), Revisionsfrist (1 Woche / 1 Monat) tickt ab Verkündung/Zustellung. 🟠 Hauptverhandlung in 30 Tagen — Beweisanträge vorbereiten.
- **Beweislage:** 🟠 Beschuldigtenaussage NIE ohne Akteneinsicht. 🔴 Belastungszeugen: Konfrontationsrecht Art. 6 III d EMRK ausnutzen. 🟢 Selbstanzeige § 371 AO nur nach umfassender Aktenlage.
- **Wirtschaftlich:** 🔴 Berufstauglichkeit gefährdet (Beamte, Heilberufe, Approbation): parallel berufsrechtliche Schiene mitdenken. 🟠 Vermögensabschöpfung §§ 73 ff. StGB im Blick.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Untersuchungshaft / Haftbefehl** | `strafr-haftpruefung-haftbeschwerde-workflow` | Haftbeschwerde § 304 StPO, Haftprüfung § 117 StPO, mündliche Verhandlung erzwingen |
| Akteneinsicht & Strategie | `akteneinsicht-beantragen` | Antrag § 147 StPO, Wahl Verfahrensschiene, ggf. Schweigen / Einlassungsmemo |
| Beweisantrag vorbereiten | `strafr-dysfunk-beweisantrag-fundament` | Substantiierte Tatsachenbehauptung, Beweismittel, Konnexität |
| Revision prüfen | `revisionsbegruendung-paragraf-344-stpo` | Sach- vs. Verfahrensrüge, absolute Revisionsgründe § 338 StPO |
| Wirtschafts-/Vermögensabschöpfung | `strafr-vermoegensabschoepfung-spezial` | Einziehung §§ 73 ff. StGB, vermögenssichernde Maßnahmen § 111b StPO |

## Norm-Radar (live verifizieren)

- **§ 147 StPO** — Akteneinsicht des Verteidigers
- **§ 137 StPO** — Recht auf Verteidiger jederzeit
- **§ 244 StPO** — Beweisantragsrecht
- **§ 117 StPO** — Haftprüfung
- **§ 341 StPO** — Revisions-Einlegungsfrist (1 Woche)
- **§ 73 StGB** — Einziehung von Taterträgen

## Genau eine Rückfrage (nur wenn nötig)

> Welche **Verfahrensphase** läuft (Ermittlung · Anklage · Hauptverhandlung · Rechtsmittel · Vollstreckung), und sitzt der Mandant **in Haft**?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Verständigung § 257c StPO; Mitteilungspflichten** — BVerfG 2. Senat; BGH-Strafsenate — *live verifizieren auf* `bundesverfassungsgericht.de + bundesgerichtshof.de`
- **Beweisantragsrecht § 244 StPO; Konnexität** — BGH-Strafsenate — *live verifizieren auf* `bundesgerichtshof.de`
- **Faires Verfahren / Konfrontationsrecht Art. 6 III d EMRK** — EGMR — *live verifizieren auf* `hudoc.echr.coe.int`
- **Einziehung §§ 73 ff. StGB; verfassungsrechtliche Grenzen** — BVerfG / BGH-Strafsenate — *live verifizieren auf* `bundesverfassungsgericht.de + bundesgerichtshof.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

---

## Skill: `mandat-triage-strafrecht`

_Strukturierte Eingangs-Abfrage für Strafmandate: Klaert Verfahrensstadium (Ermittlungs- Zwischen- Hauptverfahren Vollstreckung) Tatvorwurf nach Strafrahmen (Vergehen Verbrechen) Haftsituation (Untersuchungsha..._

# Strukturierte Eingangs-Abfrage für Strafmandate


## Aktenstart statt Formularstart

Wenn zu **Mandat Triage Plaedoyer Vorbereitung** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Fachanwalt Strafrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

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
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierte Eingangs-Abfrage für Strafmandate. Klaert Verfahrensstadium (Ermittlungs- Zwischen- Hauptverfahren Vollstreckung) Tatvorwurf nach Strafrahmen (Vergehen Verbrechen) Haftsituation (Untersuchungshaft Vollzug Hausverbot) Beschuldigtenrechte § 136 § 137 § 140 § 141 StPO Pflichtverteidiger-Bestellung Mitbeschuldigte (Konflikt-Check § 43a BRAO § 146 StPO). Sofort-Fristen-Check Haftprüfung § 117 StPO, Haftbeschwerde § 304 StPO, Akteneinsicht § 147 StPO, Rechtsmittel und U-Haft-Eskalation. Routing zu Akteneinsicht, Haftmanagement und Strafprozess-Cockpit.

### Mandat-Triage Strafrecht

## Ablauf — acht Fragen

### Frage 1 — Wer ruft an und für wen?

- Beschuldigter selbst
- Angehöriger
- Polizei (selten — Notdienst)
- Anderer Anwalt (Vertretung)

### Frage 2 — Akute Eilbedürftigkeit?

- Festnahme erfolgt — Vorführung läuft heute
- Untersuchungshaft seit Stunden / Tagen
- Durchsuchung läuft / steht bevor
- Aussage bei Polizei für heute terminiert
- Hauptverhandlung beginnt morgen

**Eskalation:** Festnahme U-Haft Durchsuchung → Telefon-Sofort an Anwalt; binnen einer Stunde Beistand; Anwesenheit bei Vernehmung Pflicht.

### Frage 3 — Verfahrensstadium?

- Ermittlungsverfahren bei Polizei (kein Aktenzeichen StA noch nicht)
- Ermittlungsverfahren bei Staatsanwaltschaft (Az StA vorhanden)
- Zwischenverfahren (Anklage zugestellt — Eröffnungsbeschluss?)
- Hauptverfahren (Hauptverhandlungstermin)
- Berufung / Revision
- Strafvollstreckung
- Strafvollzug (Vollzugsplan Lockerungen Strafaussetzung)

### Frage 4 — Tatvorwurf?

- Norm (§ ggf. StGB Nebengesetz)
- Strafrahmen — Vergehen unter ein Jahr Vergehen ab ein Jahr Verbrechen ab ein Jahr Mindeststrafe (§ 12 StGB)
- Bei Verbrechen oder Strafrahmen ab ein Jahr — notwendige Verteidigung § 140 StPO

### Frage 5 — Haftsituation?

- In Freiheit
- Vorgeführt — Vorführungsbeschluss / Haftbefehl?
- Untersuchungshaft — Haftgründe (Flucht-, Verdunkelungs-, Wiederholungs-)
- Strafvollzug

### Frage 6 — Mitbeschuldigte?

- Wer ist mitbeschuldigt?
- Ist Mitbeschuldigter bereits anwaltlich vertreten?
- Konflikt-Check § 43a Abs. 4 BRAO § 146 StPO Mehrfachverteidigung verboten

### Frage 7 — Aktenstand?

- Aktenstand nachgefragt?
- Akteneinsicht beantragt § 147 StPO
- Bei U-Haft haftrelevante Informationen nach § 147 Abs. 2 S. 2 StPO sichern; in der Regel Akteneinsicht

### Frage 8 — Wirtschaftliche Verhältnisse / Pflichtverteidigung?

- Pflichtverteidigung § 140 § 141 StPO bei notwendiger Verteidigung
- Vergütung nach RVG plus eventuell Honorarvereinbarung

## Routing-Matrix

| Verfahrensstadium | Folge-Skill | Frist-Sofort-Check |
|---|---|---|
| U-Haft | `strafprozess-haft-und-besuchsmanagement` | Haftprüfung § 117 StPO, Haftbeschwerde § 304 StPO, Sechs-Monats-Kontrolle § 121 StPO |
| Vorfeld Durchsuchung | Beschwerde § 304 StPO | ggf. nicht statthaft wenn beendet — Feststellungsantrag |
| Polizei-Vernehmung steht an | Verteidigerbeistand § 168c StPO | Termin verlegen oder begleiten |
| Anklage zugestellt | Stellungnahme zur Eröffnung | Frist nach § 201 StPO |
| Anzeige/Anklage § 188 StGB | `strafrecht-spezial-188-stgb-easy-verteidigung` | Strafantrag/besonderes öffentliches Interesse § 194 StGB, vollständiger Äußerungskontext, Art. 5 GG |
| Strafbefehl § 188 StGB | `strafrecht-spezial-188-stgb-anklage-und-strafbefehl` | Einspruch § 410 StPO binnen zwei Wochen ab Zustellung |
| Hauptverhandlung | `akteneinsicht-strafrecht-auswerten` | Beweisanträge vor Schluss Beweisaufnahme |
| Berufung/Revision | `strafprozess-rechtsmittel-und-notfristencockpit` | Berufung/Revision Einlegung binnen 1 Woche; Revisionsbegründung § 345 StPO gesondert berechnen |

## Konflikt-Check

- Mehrfachverteidigung verboten § 146 StPO
- § 43a Abs. 4 BRAO Interessenkollision
- Frühere Vertretung von Mitbeschuldigtem oder Geschädigtem prüfen

## Sofort-Fristen

- **Haftprüfung** § 117 Abs. 1 StPO — jederzeit
- **Haftbeschwerde** § 304 StPO — keine gesetzliche Wochenfrist wie bei sofortiger Beschwerde, aber praktisch sofort vorbereiten
- **Sechs-Monats-Prüfung** OLG § 121 StPO
- **Einspruch Strafbefehl** § 410 StPO zwei Wochen
- **Berufung** § 314 StPO eine Woche
- **Revision** § 341 StPO eine Woche; Revisionsbegründung § 345 StPO grundsätzlich ein Monat nach Ablauf der Einlegungsfrist, bei späterer Urteilszustellung ab Zustellung

## Eskalationspfad

- **Telefon-Sofort** Vorführung Untersuchungshaft Durchsuchung Vernehmung-Termin heute
- **Binnen einer Stunde** Anfahrt zur Vernehmung — Verteidigerbeistand
- **Heute** Akteneinsichtsantrag § 147 StPO, Haftprüfung § 117 StPO oder Haftbeschwerde § 304 StPO prüfen
- **Diese Woche** Stellungnahme Anklage Berufungseinlegung

## Ausgabe

- `triage-protokoll-strafrecht.md` mit acht Fragen
- Aktenanlage Az-Vorschlag
- Fristenbuch-Eintrag (Hauptfrist Vorfrist)
- Mandatsvereinbarung Vorlage mit Pflichtverteidigerbestellungs-Antrag falls notwendig
- Empfehlung Folge-Skill plus Begründung

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen

- StPO §§ 117 121 137 140 141 146 147 168c 201 304 314 341 410
- StGB § 12 (Verbrechen-Vergehen)
- BRAO § 43a
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Aktuelle Rechtsprechung Mandat-Triage

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen Triage-Check

- § 112 StPO — Haftbefehl (Flucht-, Verdunkelungs-, Wiederholungsgefahr)
- § 117 StPO — Haftpruefungsantrag (jederzeit)
- § 118a StPO — Haftpruefungstermin mit muendlicher Verhandlung
- § 140 StPO — notwendige Verteidigung (Bestellungsgrunde)
- § 141 StPO — Pflichtverteidiger-Bestellung (Zeitpunkt, Ablauf)
- § 146 StPO — Verbot Mehrfachverteidigung
- §§ 10 ff. GwG — Identifizierungspflichten Sorgfaltspflichten Rechtsanwalt

---

## Skill: `fachanwalt-strafrecht-orientierung`

_Orientierung im Strafrecht-Mandat und Workflow-Routing: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafrechts-Konstellation einordnen und richtigen Spezial-Skill finden. § 136 StPO Belehrung, § 137 StPO Verteidigerrecht, StGB Straftatbestaende. Prüfraster Deliktstyp allgemeines oder Wirtschaftsstrafrecht, Verfahrensstand Ermittlung Anklage Hauptverhandlung, Mandantenrolle Beschuldigter Zeuge Nebenklaeger. Output Mandat-Einordnung mit Weiterleitung zum richtigen Workflow-Skill. Abgrenzung zu Mandat-Triage-Strafrecht für ausführliche Erstaufnahme._

# Fachanwalt für Strafrecht — Orientierung

## FAO-Voraussetzungen

- **Theoretischer Lehrgang** 120 Stunden.
- **Drei Klausuren** zum Strafrecht.
- **60 Fälle** in den letzten drei Jahren, davon mindestens 40 Hauptverhandlungen mit eigener Beteiligung.
- Anmeldung bei der Rechtsanwaltskammer.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| StGB Allgemeiner Teil | §§ 1 ff. StGB |
| StGB Besonderer Teil | §§ 80 ff. StGB |
| Strafverfahren | StPO §§ 1 ff. |
| Strafvollstreckung | StVollstrO StVollzG |
| Nebenstrafrecht | BtMG WaffG AO § 370 (Steuerhinterziehung) |
| Strafrecht Wirtschaft | §§ 263 263a 266 299 StGB GwG |
| Jugendstrafrecht | JGG |
| Beruf Strafverteidiger | § 137 StPO § 138 StPO § 142 StPO Pflichtverteidigung § 140 StPO |

## Typische Mandate

- Ermittlungsverfahren Erstvernehmung
- Untersuchungshaft (§§ 112 ff. StPO Haftprüfungsantrag § 117 StPO Haftbeschwerde § 304 StPO)
- Hauptverhandlung Strafrichter Schöffengericht Schwurgericht
- Verteidigung in Wirtschaftsstrafsachen (Wirtschaftsstrafkammer Landgericht)
- Berufung Revision Verfassungsbeschwerde
- Strafvollstreckung Bewährung Reststrafenaussetzung

## Notfristen

- **Berufung** § 314 StPO — **eine Woche** Notfrist.
- **Revision** § 341 StPO — **eine Woche** Notfrist.
- **Revisionsbegründung** § 345 StPO — **ein Monat**.
- **Beschwerde** § 311 StPO — **eine Woche**.
- **Verfassungsbeschwerde** § 93 BVerfGG — **ein Monat**.
- **Wiedereinsetzung** § 44 StPO — eine Woche.

## Hauptgerichte

- **Amtsgericht** Strafrichter § 25 GVG (Vergehen Privatklage oder keine höhere Strafe als zwei Jahre zu erwarten) Schöffengericht § 28 GVG (bis vier Jahre Straferwartung).
- **Landgericht** Große Strafkammer Wirtschaftsstrafkammer Schwurgericht.
- **OLG** Berufungs- und Revisionsinstanz; Anklage erstinstanzlich bei Staatsschutzdelikten.
- **BGH 1.–5. Strafsenat** Revisionsinstanz.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- Deutscher Strafverteidiger e. V. (DSV).
- Vereinigung Berliner Strafverteidiger.
- Strafverteidigervereinigung Niedersachsen / NRW / Bayern.

## Schnittstellen

- **aktenaufbereiter-strafrecht** für Aktenaufbereitung.
- **kanzlei-allgemein** für Fristenbuch und Versand.

## Hinweis

Plugin fuer Fachanwaltschaft-Orientierung. Tiefe Verteidigung erfordert die Erfahrung des Fachanwalts; insbesondere bei Schwurgerichts- und Wirtschaftsstrafrecht.

## Zentrale Strafrecht-Normen im Ueberblick

- §§ 1-2 StGB — Gesetzlichkeitsprinzip; keine Strafe ohne Gesetz (nullum crimen)
- §§ 13-16 StGB — Begehungs-/Unterlassungsdelikt, Vorsatz, Irrtum
- §§ 20-21 StGB — Schuldunfaehigkeit, verminderte Schuldfaehigkeit
- §§ 46-49 StGB — Strafzumessung, besonderer Milderungsgrund
- § 78 StGB — Verjaehrungsfristen (z.B. 30 Jahre bei Mord)
- §§ 112-130 StPO — Untersuchungshaft, Haftbefehl, Haftgruende, Haftpruefung
- §§ 136-136a StPO — Beschuldigtenbelehrung, Aussageverweigerungsrecht, Beweisverwertungsverbote
- §§ 140-142 StPO — notwendige Verteidigung, Pflichtverteidiger

## Aktuelle Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `orientierung-mandat-fachanwaltschaft`

_Orientierung im Strafrecht-Mandat und Fallrouting: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafrechts-Konstellation einordnen und passendes Fachmodul finden: Orientierung im Strafrecht-Mandat und Fallrouting: Anwendungsfall Strafverte..._

# Orientierung im Strafrecht-Mandat und Fallrouting: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafrechts-Konstellation einordnen und passendes Fachmodul finden


## Arbeitsbereich

**Orientierung** ordnet den Fall über die tragenden Prüfungslinien: Orientierung im Strafrecht-Mandat und Fallrouting, Untersuchungshaft und Haftprüfung nach §§ 112 ff, Verständigung § 257c StPO und Taeter-Opfer-Ausgleich § 46a. Arbeite zuerst die tragende Rechtsfrage heraus; Nebenaspekte werden nur verarbeitet, soweit sie Frist, Zuständigkeit, Beweislast oder das konkrete Arbeitsprodukt tatsächlich beeinflussen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung im Strafrecht-Mandat und Fallrouting: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafrechts-Konstellation einordnen und passendes Fachmodul finden. § 136 StPO Belehrung, § 137 StPO Verteidigerrecht, StGB Straftatbestaende. Prüfraster Deliktstyp allgemeines oder Wirtschaftsstrafrecht, Verfahrensstand Ermittlung Anklage Hauptverhandlung, Mandantenrolle Beschuldigter Zeuge Nebenklaeger. Output Mandat-Einordnung mit Weiterleitung zur richtigen Prüfungslinie. Abgrenzung zu Mandat-Triage-Strafrecht für ausführliche Erstaufnahme.

### Fachanwalt für Strafrecht — Orientierung

## FAO-Voraussetzungen

- **Theoretischer Lehrgang** 120 Stunden.
- **Drei Klausuren** zum Strafrecht.
- **60 Fälle** in den letzten drei Jahren, davon mindestens 40 Hauptverhandlungen mit eigener Beteiligung.
- Anmeldung bei der Rechtsanwaltskammer.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| StGB Allgemeiner Teil | §§ 1 ff. StGB |
| StGB Besonderer Teil | §§ 80 ff. StGB |
| Strafverfahren | StPO §§ 1 ff. |
| Strafvollstreckung | StVollstrO StVollzG |
| Nebenstrafrecht | BtMG WaffG AO § 370 (Steuerhinterziehung) |
| Strafrecht Wirtschaft | §§ 263 263a 266 299 StGB GwG |
| Jugendstrafrecht | JGG |
| Beruf Strafverteidiger | § 137 StPO § 138 StPO § 142 StPO Pflichtverteidigung § 140 StPO |

## Typische Mandate

- Ermittlungsverfahren Erstvernehmung
- Untersuchungshaft (§§ 112 ff. StPO Haftprüfungsantrag § 117 StPO Haftbeschwerde § 304 StPO)
- Hauptverhandlung Strafrichter Schöffengericht Schwurgericht
- Verteidigung in Wirtschaftsstrafsachen (Wirtschaftsstrafkammer Landgericht)
- Berufung Revision Verfassungsbeschwerde
- Strafvollstreckung Bewährung Reststrafenaussetzung

## Notfristen

- **Berufung** § 314 StPO — **eine Woche** Notfrist.
- **Revision** § 341 StPO — **eine Woche** Notfrist.
- **Revisionsbegründung** § 345 StPO — **ein Monat**.
- **Beschwerde** § 311 StPO — **eine Woche**.
- **Verfassungsbeschwerde** § 93 BVerfGG — **ein Monat**.
- **Wiedereinsetzung** § 44 StPO — eine Woche.

## Hauptgerichte

- **Amtsgericht** Strafrichter § 25 GVG (Vergehen Privatklage oder keine höhere Strafe als zwei Jahre zu erwarten) Schöffengericht § 28 GVG (bis vier Jahre Straferwartung).
- **Landgericht** Große Strafkammer Wirtschaftsstrafkammer Schwurgericht.
- **OLG** Berufungs- und Revisionsinstanz; Anklage erstinstanzlich bei Staatsschutzdelikten.
- **BGH 1.–5. Strafsenat** Revisionsinstanz.

## Berufsverband

- Deutscher Strafverteidiger e. V. (DSV).
- Vereinigung Berliner Strafverteidiger.
- Strafverteidigervereinigung Niedersachsen / NRW / Bayern.

## Schnittstellen

- **aktenaufbereiter-strafrecht** für Aktenaufbereitung.
- **kanzlei-allgemein** für Fristenbuch und Versand.

## Hinweis

Plugin für Fachanwaltschaft-Orientierung. Tiefe Verteidigung erfordert die Erfahrung des Fachanwalts; insbesondere bei Schwurgerichts- und Wirtschaftsstrafrecht.

## Zentrale Strafrecht-Normen im Überblick

- §§ 1-2 StGB — Gesetzlichkeitsprinzip; keine Strafe ohne Gesetz (nullum crimen)
- §§ 13-16 StGB — Begehungs-/Unterlassungsdelikt, Vorsatz, Irrtum
- §§ 20-21 StGB — Schuldunfaehigkeit, verminderte Schuldfaehigkeit
- §§ 46-49 StGB — Strafzumessung, besonderer Milderungsgrund
- § 78 StGB — Verjährungsfristen (z.B. 30 Jahre bei Mord)
- §§ 112-130 StPO — Untersuchungshaft, Haftbefehl, Haftgruende, Haftpruefung
- §§ 136-136a StPO — Beschuldigtenbelehrung, Aussageverweigerungsrecht, Beweisverwertungsverbote
- §§ 140-142 StPO — notwendige Verteidigung, Pflichtverteidiger

## Aktuelle Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `orientierung-fristen-form-und-zustaendigkeit`

_Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg: Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg._

# Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg.

## Spezialwissen: Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg
- **Normen-/Quellenanker:** StPO.

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

## Strafrecht-Orientierung Fristen / Form / Zuständigkeit Bausteine
- **Sachliche Zuständigkeit GVG:**
 - **Strafrichter § 25 GVG:** Privatklagen § 374 StPO; allgemein bis Freiheitsstrafe 2 Jahre, sofern nicht hoeher beantragt.
 - **Schoeffengericht § 28 GVG:** bis Freiheitsstrafe 4 Jahre; alle Strafsachen, die nicht zu hoher Strafkammer oder Strafrichter gehoeren.
 - **Große Strafkammer § 76 GVG:** alle Strafsachen ab 4 Jahre erwarteter Freiheitsstrafe; bestimmte Wirtschaftsstrafsachen.
 - **Schwurgericht § 74 II GVG:** Toetungsdelikte §§ 211 ff. StGB, Eingriff in Verkehr mit Todesfolge.
 - **Oberlandesgericht § 120 GVG:** Staatsschutzdelikte (Hochverrat, Landesverrat, Terror).
- **Oertliche Zuständigkeit StPO:**
 - **§ 7 StPO:** Tatort - regelmaessig massgeblich.
 - **§ 8 StPO:** Wohnsitz Beschuldigter.
 - **§ 9 StPO:** Ergreifungsort.
 - **§ 13 StPO:** Verbundene Verfahren.
- **Fristen-Übersicht (StPO):**
 - **Einspruch Strafbefehl § 410 StPO: 2 Wochen** ab Zustellung.
 - **Berufung § 314 StPO: 1 Woche** ab Verkuendung; Begruendung optional.
 - **Revision § 341 StPO: 1 Woche** Einlegung + § 345 StPO **1 Monat** Begruendung ab Zustellung schriftliche Urteilsausfertigung.
 - **Beschwerde § 311 StPO: 1 Woche** sofortige; § 304 StPO einfache unbefristet.
 - **Wiedereinsetzung § 44 StPO: 1 Woche** ab Wegfall des Hindernisses.
 - **Klageerzwingungsverfahren § 172 II StPO: Antrag 1 Monat** ab Bescheid GenStA.
- **Form-Re-Check:**
 - **Schriftform** zwingend für Rechtsmittel (Berufung, Revision, Beschwerde) und Einspruch.
 - **Unterschrift** Verteidiger / Mandant.
 - **Vollmacht** bei Vertretung.
 - **Begruendungs-Pflicht** Revision (Sach- oder Verfahrensruege; § 344 II StPO Substantiierung Verfahrensruege).
- **Rechtsweg:**
 - AG -> LG (Berufung § 312 StPO) -> OLG (Revision § 333 StPO bei LG-Urteil 1. Instanz oder Berufungsurteil).
 - **Sprungrevision § 335 StPO** möglich (Sprung Berufung).
 - **Wiederaufnahme § 359 StPO** bei neuen Tatsachen / Beweismitteln.
- **EMRK Art. 6:** angemessene Verfahrensdauer als Korrektiv (Strafmilderung BGH-Linie).

---

## Skill: `erstgespraech-mandatsannahme`

_Erstgespraeach und Mandatsannahme im Strafrecht: Anwendungsfall Beschuldigter oder Verdaechtiger meldet sich nach Polizeivorladung oder Festnahme und Strafverteidiger muss Mandat strukturiert aufnehmen: Erstgespraeach und Mandatsannahme im Strafrecht: Anwen..._

# Erstgespraeach und Mandatsannahme im Strafrecht: Anwendungsfall Beschuldigter oder Verdaechtiger meldet sich nach Polizeivorladung oder Festnahme und Strafverteidiger muss Mandat strukturiert aufnehmen


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Erstgespraeach und Mandatsannahme im Strafrecht: Anwendungsfall Beschuldigter oder Verdaechtiger meldet sich nach Polizeivorladung oder Festnahme und Strafverteidiger muss Mandat strukturiert aufnehmen. § 136 StPO Belehrung Schweigerecht, § 137 StPO Verteidigerrecht, § 147 StPO Akteneinsicht. Prüfraster Konflikt-Check, Schweigerecht kommunizieren, Sachverhalt aufnehmen, Akteneinsicht beantragen, Honorarvereinbarung treffen. Output Mandats-Aufnahmeprotokoll mit Sofortmassnahmen-Liste und Belehrungsprotokoll. Abgrenzung zu Wahlverteidiger-Mandat für spezifischen Mandatstyp und zu Mandat-Triage.

### Erstgespraech und Mandatsannahme im Allgemeines und Wirtschaftsstrafrecht

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Allgemeines und Wirtschaftsstrafrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; oft mit Vorladung, Strafbefehl, Durchsuchungsbeschluss, Anklageschrift, U-Haft-Anordnung, Anhörung als Zeuge oder Anklageschrift mit Nebenklage-Option.
- Vor jeder weiteren Bearbeitung: erst Annahme klären, Rolle bestimmen (Beschuldigte/r, Verletzte/r oder Nebenklage, Zeuge/in mit Beistand), Konflikt- und GwG-Prüfung, Vollmacht, Gebührenvereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Rollenklarheit und Konstellation (10-15 Min.)

Erste Frage: Wofür braucht Mandantschaft Sie?

- **Beschuldigte oder Angeklagte** - Verteidigung im Strafverfahren.
- **Verletzte oder Anzeigeerstattende** - Beratung, Strafanzeige, Akteneinsicht der Verletzten, ggf. Nebenklage-Anschluss.
- **Zeuginnen oder Zeugen** - Zeugenbeistand gemäß § 68b StPO, Auskunftsverweigerungsrecht gemäß § 55 StPO.
- **Insolvenzverwalter/Geschäftsführung** mit StA-Berlin-Beruehrung - paralleles Insolvenz-/Strafverfahren.

Standard-Fragenraster:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle und Aktenzeichen StA / Gericht).
- Tatvorwurf in einem Satz (StGB-Paragraf, OWiG, Nebenstrafrecht).
- Konkrete fachliche Stossrichtung: Akteneinsicht, Beschuldigtenvernehmung, U-Haft, Strafbefehl-Einspruch, Hauptverhandlung, Revision, Anklage gegen Beschuldigte/n als Nebenklage.
- Bisherige Korrespondenz (Vorladung, Anhörungsbogen, Durchsuchung, Bescheide).
- **Fristenscreening sofort:** Einspruch gegen Strafbefehl 2 Wochen (§ 410 Abs. 1 StPO), Revisionseinlegung 1 Woche (§ 341 StPO), Revisionsbegruendung 1 Monat (§ 345 StPO), Klageerzwingung 1 Monat (§ 172 Abs. 2 StPO), Antrag auf gerichtliche Entscheidung (§ 23 EGGVG) 1 Monat, Beschwerdefristen § 311 StPO.

### 2. Konflikt-Prüfung und GwG-Check (5 Min.)

- Konflikt-Check über Mandantsystem: Mit-Beschuldigte, Verletzte, frueheres Mandat?
- Bei Mehrfach-Beschuldigten zwingend pro Person eigene Verteidigung (§ 146 StPO).
- GwG-Identifizierung: amtlicher Lichtbildausweis, bei juristischer Person Handelsregister-/Transparenzregister-Auszug, ggf. wirtschaftlich Berechtigte/n.
- Risikobewertung (niedrig/mittel/hoch) abhaengig von Auslandsbezug, Vermögensherkunft, Tatvorwurf (insbesondere § 261 StGB Geldwaesche, § 370 AO Steuerhinterziehung).
- Doku im Mandatsbogen (Pflicht nach §§ 10 ff. GwG, BRAK-Identifizierungsleitfaden).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 3. Vollmacht und Akteneinsicht

- Strafprozessvollmacht (§§ 137 ff. StPO, BORA, RVG).
- Akteneinsichtsantrag gemäß § 147 StPO (Verteidigung) oder § 406e StPO (Verletzten-/Nebenklagevertretung) oder ohne Sondervorschrift für Zeugenbeistand.
- Bei Pflichtverteidigerbestellung Antrag gemäß § 141 StPO frueh stellen (Belehrung gemäß § 136 Abs. 1 S. 3 StPO).
- Bei Nebenklage: Anschlusserklaerung gemäß § 396 StPO und Prüfung der Nebenklage-Befugnis gemäß § 395 StPO.

### 4. Gebührenvereinbarung im Strafverfahren

Strafrechtsspezifische Gebührentatbestaende statt zivilrechtlicher Streitwert-Logik:

- **RVG-Strafsachen-Tatbestaende** (VV-RVG Teil 4 Abschnitt 1): Grundgebuehr Nr. 4100, Verfahrensgebuehr Ermittlungsverfahren Nr. 4104, Verfahrensgebuehr Gerichtsverfahren erster Instanz Nr. 4106 oder 4112 bzw. 4118 je nach Gericht, Terminsgebuehr Nr. 4108 bzw. Nr. 4114 bzw. Nr. 4120, Hauptverhandlungstag-Zuschlag bei Strafkammer.
- **Bei Bussgeldverfahren:** VV-RVG Teil 5 (Nrn. 5100 ff.).
- **Pflichtverteidigung:** Festgebuehren gemäß RVG-Tabelle Teil 4 Abschnitt 1 mit besonderem Gebührentatbestand für den bestellten Verteidiger.
- **Vereinbarungshonorar / Stundenhonorar:** zulässig nach § 3a RVG mit Schriftform und ausdruecklichem Hinweis; oberhalb der gesetzlichen Gebuehr ueblich bei Wirtschaftsstrafrecht.
- **Erfolgshonorar:** nur in engen Grenzen gemäß § 4a RVG; im Strafverfahren regelmaessig problematisch (kein Erfolg im klassischen Sinne, Risiko des Wertungs-Widerspruchs).
- **Vorschuss:** Vorschussanforderung nach § 9 RVG, in Strafsachen ueblich pro Instanz oder pro Hauptverhandlungstag.
- **Bei Nebenklage:** Gebühren VV-RVG Teil 4 Abschnitt 2 (Nrn. 4124 ff.). Streitwert-Äquivalent nur für adhaesionsrechtliche Anspruche relevant.
- **Bei Adhaesion (§§ 403 ff. StPO):** Gebühren VV-RVG Teil 4 Abschnitt 6 (Nrn. 4143-4147), berechnet nach Gegenstandswert des geltend gemachten Anspruchs.

### 5. Strategie-Erstskizze

Drei Weichen am Ende des Erstgespraechs:

- **Mandat annehmen:** vollstaendig (Verteidigung durch alle Instanzen) oder begrenzt (nur Akteneinsicht und Gutachten, nur Erstellung Einspruch gegen Strafbefehl, nur Zeugenbeistand für einen Vernehmungstermin).
- **Verweisen:** wenn Spezialgebiet ausserhalb (Wirtschaftsstrafrecht vs. allgemeines Strafrecht), oertlich unzuständig oder Mehrfachbeschuldigtenkonstellation.
- **Ablehnen:** Konflikt mit § 146 StPO, GwG-Hit beim Honorar, fehlende Vertrauensbasis.

## Pflicht-Output am Ende

1. **Mandatsbogen** mit Beteiligten, Rolle, Konflikt-Check, GwG-Status, Tatvorwurf, Aktenzeichen.
2. **Frist-Liste** (Einspruch, Revisionseinlegung, Revisionsbegruendung, Beschwerdefristen, Anschluss-Frist Nebenklage, U-Haft-Prüfungsfristen § 121 StPO).
3. **Anlagenverzeichnis** des uebergebenen Datenraums (Bescheide, Schreiben, Anhörungsbogen).
4. **Naechster-Schritt-Plan:** binnen 24 / 48 / 72 h, Owner, Output (Akteneinsicht stellen, Pflichtverteidigerbeiordnung beantragen, U-Haft-Beschwerde).
5. **Honorarvereinbarung** unterschrieben oder Hinweis auf RVG-Festgebuehr / Pflichtverteidiger-Beiordnung.

## Relevante Rechtsgrundlagen und Standards

- BORA, BRAO, FAO Strafrecht (§ 13 FAO).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- StGB, StPO, BtMG, AO (§§ 369 ff.), OWiG, JGG, Nebenstrafrecht (StVG, WaffG, KCanG, AWG, WiStrG 1954).
- RVG mit VV-RVG Teil 4 (Strafsachen) und Teil 5 (Bussgeldsachen).
- DSGVO und BDSG für den Umgang mit Mandanten- und Verletzten-Daten.

## Typische Fehler im Erstgespraech

- Rolle der Mandantschaft nicht klar getrennt - Mehrfachvertretung Beschuldigter und Nebenklaegerin im gleichen Verfahren ist berufsrechtswidrig.
- Frist uebersehen, weil Mandantschaft sie nicht selber genannt hat (immer aus jedem Schreiben Frist herausziehen, insbesondere Strafbefehl mit Zustellungsdatum).
- Pflichtverteidiger-Antrag erst spaet gestellt - Vergutungsrisiko für Wahlverteidiger bis Beiordnung.
- Akteneinsicht zu spaet beantragt - Hauptverhandlungsvorbereitung leidet.
- Honorarvereinbarung muendlich oder ohne § 3a-RVG-Form - Honorar nur in Höhe der gesetzlichen Gebuehr durchsetzbar.
- GwG-Prüfung verfehlt - Risiko § 261 StGB beim Honorar-Bezug aus inkriminierter Quelle.

## Praxis-Checkliste

- [ ] Rolle der Mandantschaft eindeutig festgestellt
- [ ] Personalien und Aktenzeichen aller Beteiligten erfasst
- [ ] Konflikt-Check durchgefuehrt (auch Mit-Beschuldigte gemäß § 146 StPO)
- [ ] GwG: Identifizierung + Risikobewertung notiert
- [ ] Strafprozessvollmacht unterschrieben
- [ ] Akteneinsicht beantragt (§ 147 oder § 406e StPO)
- [ ] Pflichtverteidigerbestellung beantragt, soweit Voraussetzungen vorliegen (§ 140 StPO)
- [ ] Honorarvereinbarung schriftlich (§ 3a RVG) oder Hinweis auf RVG-Festgebuehr
- [ ] Fristenliste angelegt und in Kalender eingetragen
- [ ] Mandatsbogen vollstaendig
- [ ] Naechster-Schritt-Plan kommuniziert (E-Mail-Zusammenfassung)

## Konkrete Praxis-Konstellationen

### Konstellation A: Strafbefehl mit Einspruchsfrist

Mandantschaft bringt Strafbefehl am Donnerstag, Einspruchsfrist 2 Wochen ab Zustellung. Handlungs-Sequenz:

1. Zustellungsdatum aus Strafbefehl auslesen (Zustellungsurkunde, EB).
2. Akteneinsicht (§ 147 StPO) sofort schicken.
3. Einspruch fristwahrend einlegen, Begruendung nachreichen.
4. Wiedereinsetzung in den vorigen Stand (§§ 44 ff. StPO) als Reserve dokumentieren.

### Konstellation B: U-Haft

Mandantschaft sitzt seit Wochen in U-Haft. Pflichtverteidiger noch nicht beantragt.

1. Pflichtverteidigerbestellung beantragen (§ 140 Abs. 1 Nr. 4 StPO).
2. Akteneinsicht beantragen, soweit § 147 Abs. 2 StPO nicht entgegensteht.
3. Haftpruefung (§ 117 StPO) oder Haftbeschwerde (§ 304 StPO).
4. Mandantengespraech in der JVA terminieren (Sprecherlaubnis).

### Konstellation C: Verletzte/r mit Nebenklage-Option

Mandantschaft ist Opfer einer Sexualstraftat oder schweren Koerperverletzung.

1. Akteneinsichtsantrag für Verletztenvertretung (§ 406e StPO).
2. Prüfung Nebenklagebefugnis (§ 395 StPO).
3. Antrag auf Beiordnung als Opferanwalt (§ 397a StPO).
4. Adhaesion (§§ 403 ff. StPO) und psychosoziale Prozessbegleitung (§ 406g StPO) erwaegen.
5. Cross-Ref: `fachanwalt-strafrecht-nebenklage-opfervertretung`.

### Konstellation D: Zeuge mit Auskunftsverweigerungsrecht

Mandantschaft hat Vorladung als Zeuge in einem Verfahren erhalten, ist aber selber Mit-Beschuldigte/r in anderer Sache.

1. Prüfung § 55 StPO (Selbstbelastungsgefahr) und § 52 StPO (Angehoerigenstellung).
2. Zeugenbeistand gemäß § 68b StPO; Beiordnung gemäß § 68b Abs. 2 StPO bei Bedrohung.
3. Vorbereitung der Aussage und Auskunftsverweigerung in der Vernehmung.
4. Cross-Ref: `fachanwalt-strafrecht-zeugenbeistand`.

### Konstellation E: Wirtschaftsstrafverfahren mit Insolvenzantrag der StA

Mandantschaft ist Geschäftsführer/in einer GmbH; StA hat Insolvenzantrag gemäß § 14 InsO gestellt, parallel laeuft Strafverfahren wegen Insolvenzverschleppung (§ 15a InsO) oder Untreue (§ 266 StGB).

1. Doppelgleisige Strategie: Strafverteidigung + Insolvenzverteidigung.
2. Prüfung Anhörungsantraege im InsO-Verfahren.
3. Vermögensabschoepfung gemäß §§ 73 ff. StGB und Beschlagnahme gemäß § 111b StPO im Auge behalten.
4. Cross-Ref: `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft`.

## Mandanten-Erwartungsmanagement

- Realistische Strafmass- und Bewaehrungs-Prognose (nicht: "Wir bekommen sicher Freispruch").
- Verfahrensdauer: Ermittlungsverfahren Wochen bis Monate, Hauptverhandlung Termine pro Instanz, Revision mehrere Monate.
- Verstaendigungschance gemäß § 257c StPO und Einstellung gemäß § 153a StPO als Option offen halten.
- Schriftliche Zusammenfassung des Erstgespraechs binnen 48 h.

## Mandatsbogen-Muster (Mindestinhalt für Strafsachen)

- Mandantschaft (Name, Geburtsdatum, Anschrift, Telefon, E-Mail).
- Rolle (Beschuldigte, Nebenklaegerin, Zeugin, Insolvenzschuldnerin/GF).
- Aktenzeichen StA / Gericht / Polizei.
- Tatvorwurf (Paragraf, Tatzeit, Tatort).
- Kurzbeschreibung Sachverhalt (5-10 Saetze).
- Ziel des Mandats (eine Zeile).
- Strittige Fragen (bullet).
- Geprueft: Konflikt - GwG - Vollmacht.
- Gebührentatbestaende (Nrn. 4100 ff. VV-RVG / Vereinbarung).
- Frist-Liste.
- Aktenanlage Datum.
- Naechster-Schritt.

## Cross-Refs

- `vergleichsverhandlung-strategie` (im selben Plugin) für Verstaendigung gemäß § 257c StPO, Einstellung gemäß § 153a StPO und Adhaesion.
- `schriftsatzkern-substantiierung` (im selben Plugin) für Verteidigungsschriftsaetze (Einspruch, Revision, Klageerzwingung).
- `fachanwalt-strafrecht-nebenklage-opfervertretung` (im selben Plugin) für Verletzten- und Nebenklagevertretung.
- `fachanwalt-strafrecht-zeugenbeistand` (im selben Plugin) für Zeugenbeistand gemäß § 68b StPO.
- `fachanwalt-strafrecht-adhaesionsverfahren` (im selben Plugin) für Adhaesion.
- `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft` (im selben Plugin) für parallelen Insolvenzantrag der StA.
- `kanzlei-allgemein` für Konflikt-, GwG- und Aktenanlage-Routinen.

## Aktuelle Rechtsprechung Erstgespraech / Mandatsannahme

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Erstgespraech Normen-Check

- § 136 Abs. 1 StPO — Beschuldigtenbelehrung: Schweigerecht, Verteidigerwahl
- § 137 StPO — freie Wahl des Verteidigers
- § 140 StPO — notwendige Verteidigung: Katalog der Pflichtfaelle
- § 146 StPO — Verbot Mehrfachvertretung
- §§ 10-17 GwG — Identifizierung, Risikoeinschaetzung, Dokumentation
- § 261 StGB — Geldwaesche: Strafbarkeit auch des Verteidigers bei Vorsatz/Leichtfertigkeit
- § 3a RVG — schriftliche Honorarvereinbarung; Mindestangaben

---

## Skill: `erstpruefung-und-mandatsziel`

_Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** StPO.

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

## Strafrecht-Fachanwalt Erstpruefung Bausteine
- **Mandantenrolle praezisieren:**
 - **Beschuldigter / Angeklagter:** Verteidigerbestellung § 137 StPO; ggf. notwendige Verteidigung §§ 140-141 StPO.
 - **Geschaedigter / Nebenklage § 395 StPO:** Antrag Anschluss; Antragsdelikte (§§ 174-184k StGB, § 230 StGB, § 263a StGB); Zeugnis-Beistand § 68b StPO.
 - **Adhaesionsverfahren §§ 403-406c StPO:** zivilrechtliche Anspruchsverfolgung im Strafverfahren.
 - **Zeuge:** §§ 52 StPO Angehoerigenzeugnis; § 55 StPO Auskunftsverweigerung; Zeugnisbeistand.
 - **Klageerzwingung § 172 StPO:** Verletzter beantragt Erhebung der öffentlichen Klage.
- **Verfahrensstand-Triage:**
 - **Ermittlungsverfahren:** Akteneinsicht § 147 StPO; Stellungnahme StA; Schweigerecht § 136 StPO.
 - **Zwischenverfahren §§ 199-211 StPO:** Eroeffnungsbeschluss-Prüfung; Einwaende § 201 StPO; Hilfsbeweisantraege.
 - **Hauptverhandlung:** Beweisantraege § 244 StPO; Verstaendigung § 257c StPO; Schlussvortrag.
 - **Rechtsmittel:** Berufung § 314 StPO (1 Woche); Revision §§ 341, 345 StPO (1 Woche / 1 Monat); Beschwerde § 304 StPO.
 - **Vollstreckungsverfahren:** Strafrest § 57 StGB; Bewaehrungswiderruf § 56f StGB.
- **Tatvorwurfsklasse:**
 - **Vergehen § 12 II StGB** (Mindeststrafe unter 1 Jahr): Strafbefehl § 407 StPO möglich.
 - **Verbrechen § 12 I StGB** (Mindeststrafe 1 Jahr): notwendige Verteidigung § 140 I Nr. 2 StPO; Schwurgericht / große Strafkammer.
- **Mandantenziel-Hierarchie:**
 - Schuldspruch vermeiden (Freispruch).
 - Einstellung §§ 153, 153a StPO.
 - Strafmilderung.
 - Bewaehrung sichern (§ 56 StGB).
 - Reputation schuetzen (BZRG, FZR, Berufsrecht).
- **Honoraranfrage / Verguetungsvereinbarung § 3a RVG schriftlich** wenn Wahlanwaltsmandat; bei Pflichtverteidigung Festbetragstarif RVG VV 4100 ff.

---

## Skill: `fachanwalt-strafrecht-zeugenbeistand`

_Zeugenbeistand im Strafverfahren für Zeugen mit eigenem Rechtsinteresse: Anwendungsfall Person ist als Zeuge geladen hat aber eigenes Aussageverweigerungsrecht oder Selbstbelastungsrisiko und benoetigt anwaltlichen Beistand. § 68b StPO Zeugenbeistand, § 55 StPO Auskunftsverweigerungsrecht, § 52 StPO Zeugnisverweigerungsrecht. Prüfraster Auskunftsverweigerungsrecht nach § 55 prüfen, Schutz vor Selbstbelastung, Zeugen-Aussage vorbereiten oder Aussage verweigern, Beistand aktiv ausüben. Output Strategie-Memo für Zeugenbeistand mit Aussagepfaden und Verweigerungs-Optionen. Abgrenzung zu Erstgespraeach für Beschuldigte und zu Nebenklage._

# Zeugenbeistand im Strafverfahren

## Kernsachverhalt & Mandantenfragen

Der Zeugenbeistand ist die anwaltliche Begleitperson eines Zeugen – nicht des Beschuldigten. Die Rolle ist strukturell eigenstaendig: Der Beistand berät den Zeugen, darf aber nicht den Verfahrensverlauf lenken wie ein Verteidiger. Mandantinnen und Mandanten verstehen diese Unterscheidung selten.

**8 Kaltstart-Rückfragen:**

1. Haben Sie eine Ladung erhalten und von wem (Polizei, Staatsanwaltschaft, Gericht)? Bitte Ladungsschreiben vorlegen.
2. Sind Sie selbst beschuldigt oder verdaechtig in derselben Sache oder einer verwandten Sache?
3. Sind Sie mit der/dem Beschuldigten verwandt, verschwägert, verlobt oder verheiratet?
4. Üben Sie einen Beruf aus, der eine gesetzliche Schweigepflicht begründet (Arzt, Rechtsanwalt, Steuerberater, Pfarrer, Psychotherapeut)?
5. Sind Sie Beamter oder Angestellter des öffentlichen Dienstes und benötigen Sie eine Aussagegenehmigung Ihres Dienstherrn?
6. Wurden Ihnen Drohungen gemacht oder fühlen Sie sich durch das Umfeld der/des Beschuldigten gefährdet?
7. Sind Sie zugleich Verletzte/r der dem Verfahren zugrundeliegenden Tat?
8. Haben Sie bereits Angaben gegenüber der Polizei gemacht und wenn ja, in welchem Umfang?

---
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 48 StPO | Pflicht zur Aussage; grundsätzliche Erscheinens- und Aussagepflicht des Zeugen |
| § 52 StPO | Zeugnisverweigerungsrecht der Angehörigen (Ehegatten, Verwandte gerader Linie, Seitenlinie bis 3. Grad) |
| § 53 StPO | Zeugnisverweigerungsrecht der Berufsgeheimnisträger (Ärzte, Anwälte, Steuerberater, Geistliche u.a.) |
| § 53a StPO | Zeugnisverweigerungsrecht beruflicher Gehilfen (z.B. Rechtsanwaltsfachangestellte) |
| § 54 StPO | Aussagegenehmigung für Amtsträger; Versagung mit Begruendungspflicht |
| § 55 StPO | Auskunftsverweigerungsrecht bei Selbstbelastungsgefahr (einzelne Fragen oder ganze Aussage) |
| § 68 StPO | Vernehmung zur Person; Adressanonymisierung Abs. 2 und Abs. 3 |
| § 68a StPO | Beschränkung ehrenrühriger Fragen |
| § 68b StPO | Anwaltlicher Beistand des Zeugen; Beiordnung Abs. 2 bei Schutzbedürftigkeit |
| § 70 StPO | Zwangsmittel bei unberechtigter Zeugnisverweigerung (Ordnungsgeld, Erzwingungshaft) |
| § 97 StPO | Beschlagnahmeverbot bei Berufsgeheimnissen |
| § 136a StPO | Verbotene Vernehmungsmethoden (analog für Zeugen) |
| § 161a StPO | Vernehmung von Zeugen durch die Staatsanwaltschaft |
| § 163a StPO | Vernehmung durch die Polizei |
| § 247 StPO | Entfernung des Angeklagten bei Zeugenvernehmung (Schutzvorschrift) |
| § 406e StPO | Akteneinsicht für Verletzte (analog für Zeugenbeistand anerkannt) |

---

## Leitentscheidungen

| Aktenzeichen | Gericht / Datum | Leitsatz |
|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

---

## Prüfschema Zeugenbeistand

| Schritt | Inhalt | Grundlage |
|---|---|---|
| 1 | Ladung prüfen: Wer lädt (Polizei/StA/Gericht)? Verfahrensstadium? Beweisthema? | § 48, § 161a, § 163a StPO |
| 2 | Zeugnisverweigerungsrecht § 52 StPO: Angehörigeneigenschaft prüfen (Ehe, Verwandtschaft, Lebenspartnerschaft) | § 52 StPO |
| 3 | Zeugnisverweigerungsrecht § 53 StPO: Berufsgeheimnisträger? Entbindungserklärung vorhanden? | § 53, § 53a StPO |
| 4 | Aussagegenehmigung § 54 StPO: Amtsträger? Genehmigung erteilt oder beantragt? | § 54 StPO |
| 5 | Auskunftsverweigerungsrecht § 55 StPO: Welche Fragen beinhalten Selbstbelastungsgefahr? Einzelfragen oder gesamte Aussage betroffen? | § 55 StPO |
| 6 | Akteneinsicht beantragen (analog § 406e StPO oder über § 475 StPO) | § 406e, § 475 StPO |
| 7 | Beiordnungsantrag § 68b Abs. 2 StPO prüfen: Schutzbedürftigkeit, Minderjährigkeit, Gefährdungslage, Verbindung zu Organisierter Kriminalität | § 68b Abs. 2 StPO |
| 8 | Adressanonymisierung § 68 Abs. 2/3 StPO prüfen: Stalking, häusliche Gewalt, Zeugenschutzbedarf | § 68 StPO |
| 9 | Aussage-Chronologie mit Mandantschaft erarbeiten: Was weiß sie/er und aus welcher Quelle? Erinnerungslücken offen lassen | § 68b StPO |
| 10 | Schriftliche Mandantenbelehrung über Rechte (§§ 52, 55 StPO) und Pflichten (§ 48 StPO) | § 48, § 52, § 55 StPO |
| 11 | Vernehmungsbegleitung: Anwesenheit, Wortmeldungsrecht; Schutz vor § 136a-StPO-Methoden; Pausenanträge bei § 55-Konstellationen | § 68b StPO |
| 12 | Protokollkontrolle: Richtigkeit und Vollständigkeit; ggf. Berichtigungsantrag | § 168 S. 2 StPO |
| 13 | Nachbereitung: Zeugen-Memo, Prüfung weiterer Schritte (Beschwerde, Strafanzeige bei Druckausübung) | §§ 162, 306 StPO |

---

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Zeugen-Beistand | Zeugenbeistand-Protokoll; Template unten |
| Variante A — Zeuge wird Beschuldigter | Sofort Aussageverweigerung; Mandatsumwandlung |
| Variante B — Zeuge im Ausland | Internationale Rechtshilfe; Aussagepflicht pruefen |
| Variante C — Behoedenzeuge (Beamter) | Aussagegenehmigung Dienststelle; Amtsgeheimnis |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1 – Beiordnungsantrag § 68b Abs. 2 StPO

```
An das [Gericht / Staatsanwaltschaft]
Aktenzeichen: [...]

Antrag auf Beiordnung als anwaltlicher Zeugenbeistand
gemäß § 68b Abs. 2 StPO

In der Strafsache gegen [Name Beschuldigte/r]
zeige ich die anwaltliche Vertretung der Zeugin / des Zeugen
[Name, Geburtsdatum, Anschrift]
an.

Ich beantrage, mich als anwaltlichen Beistand der Zeugin / des Zeugen
gemäß § 68b Abs. 2 StPO beizuordnen.

Begründung:
Die Beiordnung ist erforderlich, weil [konkret: z.B.
"die Zeugin minderjährig und einem erheblichen Drohungsdruck
durch den Beschuldigten ausgesetzt ist; es liegen Erkenntnisse
vor, dass der Beschuldigte über Mittelsleute Einfluss auf
das Aussageverhalten ausübt (dokumentiert durch SMS-Nachrichten
vom [Datum], Anlage 1)"].

Die Vernehmung ist für den [Termin] vor [Behörde/Gericht]
angesetzt.

[Ort, Datum]
[Unterschrift, Kanzlei]
```

### Baustein 2 – Erklärung Auskunftsverweigerungsrecht § 55 StPO

```
An den/die Vernehmungsbeamten/-beamtin / Vorsitzenden
[Behörde / Gericht]

In der Vernehmung der Zeugin / des Zeugen [Name]
am [Datum], Aktenzeichen [...]

Erklärung gemäß § 55 StPO

Ich erkläre namens und in Vollmacht der Zeugin / des Zeugen
[Name]:

Auf die Frage [ggf. konkrete Frage nennen oder: "betreffend
den Sachverhaltskomplex X"] verweigert die Zeugin / der Zeuge
die Auskunft gemäß § 55 StPO.

Die wahrheitsgemäße Beantwortung würde die Zeugin / den Zeugen
der Gefahr aussetzen, wegen einer Straftat verfolgt zu werden
(§ 55 Abs. 1 StPO). Eine Belehrung gemäß § 55 Abs. 2 StPO
ist [nicht] erfolgt.

Soweit die Vernehmungsperson die Berechtigung dieser
Verweigerung bezweifelt, beantrage ich die Entscheidung
des zuständigen Richters (§ 55 Abs. 2 S. 3 StPO).

[Ort, Datum]
[Unterschrift]
```

### Baustein 3 – Akteneinsichtsantrag (Zeugenbeistand, analog § 406e StPO)

```
An die Staatsanwaltschaft [...]
Aktenzeichen: [...]

Antrag auf Akteneinsicht gemäß § 406e StPO (analog) /
§ 475 StPO

Ich zeige die anwaltliche Vertretung der Zeugin / des Zeugen
[Name] an.

Ich beantrage Einsicht in die Verfahrensakte, insbesondere:
- Anklageschrift / Eröffnungsbeschluss
- Vernehmungsprotokolle
- Sachverständigengutachten
- [weitere konkrete Unterlagen]

Das berechtigte Interesse ergibt sich aus der bevorstehenden
Zeugenvernehmung am [Termin]. Eine sachgerechte Vorbereitung
ist ohne Kenntnis des Verfahrensstands und der bereits vor-
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

[Ort, Datum]
[Unterschrift]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Beweislast

| Konstellation | Beweislast |
|---|---|
| Berechtigung zur Zeugnisverweigerung § 52 StPO | Zeugin/Zeuge behauptet Angehörigeneigenschaft; Gericht prüft von Amts wegen, ggf. eidesstattliche Erklärung |
| Auskunftsverweigerungsrecht § 55 StPO | Zeugin/Zeuge muss Verfolgungsgefahr glaubhaft machen; keine volle Beweispflicht, aber substantiiertes Vorbringen |
| Beiordnung § 68b Abs. 2 StPO | Antragstellerin/Antragsteller trägt Schutzbedürftigkeit vor; Gericht entscheidet nach freiem Ermessen |
| Beschlagnahmeverbot § 97 StPO | Beschuldigtenverteidigung trägt Schutzwürdigkeit vor; Staatsanwaltschaft muss keine Ausnahme beweisen |

---

## Fristen und Verjährung

| Frist | Inhalt | Norm |
|---|---|---|
| Sofort | Beiordnungsantrag vor Vernehmungstermin stellen | § 68b Abs. 2 StPO |
| 2 Wochen | Beschwerde gegen Ablehnung der Beiordnung (§ 306 StPO) | § 311 StPO |
| Vor Aussage | Akteneinsicht rechtzeitig beantragen; Reaktionszeit der Behörde einplanen (3–5 Tage bei StA) | § 406e StPO |
| Sofort in der Vernehmung | § 55-Erklärung muss vor der strittigen Antwort abgegeben werden, nicht nachträglich | § 55 StPO |
| 1 Woche nach Vernehmung | Protokollberichtigung beantragen, wenn Fehler vorliegen | § 168 S. 2 StPO |

---

## Typische Gegenargumente

| Gegenargument | Erwiderung |
|---|---|
| "Die Zeugin muss aussagen, § 48 StPO gilt uneingeschränkt" | § 48 StPO begründet Pflicht, enthält aber keine Aussagepflicht bei Verweigerungsrechten; §§ 52, 53, 55 StPO gehen als lex specialis vor |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Zeugenbeistand darf nicht sprechen" | § 68b Abs. 1 S. 2 StPO erlaubt Beanstandungen; bei Beiordnung auch Erklärungen; BGH hat Erklärungsrecht bestätigt |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Adressanonymisierung ist unverhältnismäßig" | § 68 Abs. 3 StPO erfordert nur drohende Gefahr, nicht bereits eingetretene Schädigung; pauschal aber unzureichend |

---

## Streitwert / Kosten

| Position | Berechnung |
|---|---|
| Wahlmandat Zeugenbeistand | RVG Teil 4 (analog Verteidigergebühren VV 4100 ff.); Mittelgebühr nach Aufwand |
| Beiordnung § 68b Abs. 2 StPO | Pflichtverteidigergebühren nach VV-RVG; Kostentragung durch Staatskasse |
| Akteneinsicht als Nebenleistung | keine gesonderte Gebühr; im Verfahrensgebühren-Rahmen enthalten |
| Mehrere Vernehmungstermine | Terminsgebühr je Termin (VV 4102/4103 je nach Gericht/Behörde) |
| Beschwerdeverfahren | eigenständige Verfahrens- und Terminsgebühr nach Teil 4 VV-RVG |

---

## Typische Konstellationen im Detail

### Konstellation A: Familienmitglied als Zeuge gegen Angehörigen

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Konstellation B: Mit-Beschuldigter als Zeuge im Parallelverfahren

Höchste Vorsicht: § 55 StPO greift für jede einzelne Frage. Vorher Akteneinsicht in Parallelverfahren beantragen. Aussage mit eigener Strafverteidigungsstrategie abstimmen. Beiordnung nach § 68b Abs. 2 StPO beantragen. Bei Kollision Zeugenbeistand/Verteidigung: § 146 StPO beachten – zwei getrennte Mandate.

### Konstellation C: Berufsgeheimnisträger (Arzt, Anwalt, Steuerberater)

Prüfen, ob Entbindungserklärung des Mandanten/Patienten vorliegt. Ohne Entbindung: § 53 StPO geltend machen. Bei Sicherstellung von Unterlagen: § 97 StPO Beschlagnahmeverbot prüfen (nur greift wenn Zeuge selbst nicht verdächtig). Bei vorliegender Entbindung: Aussage auf gedeckten Umfang beschränken; keine freiwillige Ausweitung.

### Konstellation D: Zeuge in Wirtschaftsstrafverfahren

§ 55 StPO regelmäßig einschlägig. Compliance-Untersuchungen (Internal Investigations) vorab analysieren: Verwertungsverbote nach sog. Mannheimer Modell prüfen. Geschäftsgeheimnisse: § 53 StPO greift nur für Berufsgeheimnisträger, nicht pauschal für Unternehmensgeheimnisse. Sicherstellungen nach § 94 StPO im Vorfeld der Vernehmung sind häufig; Beschlagnahmeverbot § 97 StPO prüfen.

### Konstellation E: Whistleblower / Hinweisgeber

HinSchG-Schutz prüfen (Hinweisgeberschutzgesetz 2023). Identitätsschutz und Adressanonymisierung § 68 Abs. 2/3 StPO. Beiordnung § 68b Abs. 2 StPO mit Schutzbedürftigkeit begründen. Repressalienschutz dokumentieren (Art. 19 HinSchG: Verbot der Benachteiligung).

---

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Zeugin hat keine Kenntnisse von der Tat | Offene, ehrliche Aussage mit Begleitung; kein Schweigen ohne Grund (Glaubwürdigkeitsrisiko) |
| Zeugin könnte sich selbst belasten | § 55 StPO konsequent einsetzen; Akteneinsicht vor Aussage zwingend |
| Angehörige/r ist zeugnisverweigerungsberechtigt | Entscheidung ausführlich besprechen; emotionale und strategische Aspekte abwägen; schriftlich dokumentieren |
| Gefährdungslage vorhanden | Adressanonymisierung § 68 StPO + Beiordnung § 68b Abs. 2 StPO gleichzeitig beantragen |
| Amtsträger ohne Genehmigung | Aussage verweigern bis Genehmigung vorliegt; Rechtsweg gegen Versagung (§ 54 Abs. 3 StPO) |
| Zeuge ist auch Verletzter | Nebenklage prüfen; doppelte Mandat-Führung (Zeugenbeistand + Nebenklage) möglich, aber klar trennen |

---

## Anschluss-Skills

- `fachanwalt-strafrecht-nebenklage-opfervertretung` – wenn Zeuge zugleich Verletzter ist
- `fachanwalt-strafrecht-adhaesionsverfahren` – wenn Verletzter zivilrechtliche Ansprüche geltend macht
- `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft` – bei Wirtschaftsstrafverfahren mit Vermögensbezug
- `plaedoyer-vorbereitung-strafverteidigung` – Hauptverhandlungsbegleitung nach Anschluss als Nebenklage

---

## Quellen

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

