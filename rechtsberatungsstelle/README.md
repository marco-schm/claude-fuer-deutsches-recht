# Plugin für die studentische Rechtsberatungsstelle

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`rechtsberatungsstelle`) | [`rechtsberatungsstelle.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/rechtsberatungsstelle.zip) |
| **Alle Skills als Markdown** | [`rechtsberatungsstelle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/rechtsberatungsstelle-skills-markdown.zip) |
| **Unified Mini Prompt** (Sparversion bis 7.500 Zeichen) | [`rechtsberatungsstelle-unified-mini-prompt.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/rechtsberatungsstelle-unified-mini-prompt.md) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Rechtsberatungsstelle Köln-Kalk — Monatsmix August 2026, Dr. Pellbach-Tannenfels** (`rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach`) | [Gesamt-PDF lesen](../testakten/rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach/gesamt-pdf/rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach_gesamt.pdf) | [`testakte-rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-rechtsberatungsstelle-koeln-quartier-kalk-q3-2026-monatsmix-pellbach.zip) |
| **Akte Reimers: Verbraucherinsolvenz, ehemaliger Geschäftsführer und Schuldenbereinigungsplan** (`verbraucherinsolvenz-reimers-ehemaliger-gf-schuldenbereinigung`) | [Gesamt-PDF lesen](../testakten/verbraucherinsolvenz-reimers-ehemaliger-gf-schuldenbereinigung/gesamt-pdf/verbraucherinsolvenz-reimers-ehemaliger-gf-schuldenbereinigung_gesamt.pdf) | [`testakte-verbraucherinsolvenz-reimers-ehemaliger-gf-schuldenbereinigung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verbraucherinsolvenz-reimers-ehemaliger-gf-schuldenbereinigung.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

*KI-gestützte Unterstützung für universitäre Refugee Law Clinics, studentische Rechtsberatungen und Pro-Bono-Initiativen – mit klaren RDG-Grenzen.*

Ein Plugin für Einrichtungen, in denen Studierende – unter Anleitung zur Anleitung berechtigter Volljuristen – unentgeltliche Rechtsberatung für Menschen leisten, die sich anwaltliche Hilfe nicht leisten können oder keinen Zugang dazu haben: Aufenthalts- und Asylrecht, Sozialrecht (SGB II/XII, SGB IX), Mietrecht, Verbraucherrecht, Familienrecht.

**Jede Ausgabe ist ein Entwurf für die Analyse durch Studierende und die Freigabe durch den anleitenden Volljuristen – gekennzeichnet, gestuft und protokolliert. Das Plugin gibt Struktur; die Studierenden denken juristisch; der Anleiter prüft und gibt frei. Nichts verlässt die Beratungsstelle ohne Durchlaufen dieses Aufsichtsmodells.**

---

## Wichtiger Hinweis: Rechtliche Grenzen nach dem RDG

> **Diese Beratungsstelle erbringt Rechtsdienstleistungen ausschließlich im Rahmen von § 6 Abs. 2 Nr. 2 RDG (unentgeltliche Rechtsdienstleistungen durch Volljuristen anleitungsberechtigt) oder § 8 RDG (Verbraucherzentralen, Sozialberatung). Jede entgeltliche Rechtsdienstleistung durch Nicht-Zugelassene ist nach § 3 RDG untersagt und nach § 20 RDG bußgeldbewehrt.**

**Für Studierende gilt:**
- Rechtliche Auskünfte dürfen nur unter Anleitung und Aufsicht eines zur Anleitung berechtigten Volljuristen erteilt werden (§ 6 Abs. 2 Nr. 2 RDG).
- Schriftsätze, Stellungnahmen und Widersprüche sind **Entwürfe** – keine fertigen, abzusendenden Dokumente.
- Jede strategische Entscheidung (Klage ja/nein, Rücknahme, Vergleich) liegt beim anleitenden Anwalt.
- Das Mandat liegt formal beim Anleiter, nicht beim Studierenden.
- Verschwiegenheit nach § 43a Abs. 2 BRAO analog, § 203 StGB – auch nach Semesterende.

---

## Das Problem, das dieses Plugin löst

Beratungsstellen sind strukturell kapazitätsbeschränkt. Ein anleitender Jurist betreut 5–12 Studierende. Jede Studierende trägt eine Handvoll Mandate, während sie gleichzeitig Lehrveranstaltungen besucht. Studierende wechseln jedes Semester. Verwaltungsaufgaben – Intake-Protokoll, Erstentwürfe, Rechercheansätze, Statusberichte, Semesterübergaben – verschlingen Stunden, die besser in die juristische Analyse investiert wären. Das Ergebnis: lange Wartelisten, begrenzte Fallzahlen, Ratsuchende, die aufgeben.

Dieses Plugin senkt die Zeitkosten für alles **rund um die Rechtsarbeit**, damit dieselben Studierenden und ihr Anleiter deutlich mehr Mandanten sinnvoll betreuen können – und die Studierenden mehr Zeit für Analyse und Strategie haben, die das Kernanliegen studentischer Rechtsbildung ausmacht.

**Es beschleunigt die nicht-lehrenden Teile. Es bewahrt die analytische Arbeit.** Das ist das Gestaltungsprinzip.

---

## Wer nutzt das Plugin?

| Rolle | Startet | Erhält |
|---|---|---|
| **Anleitender Volljurist** | `/kaltstart-interview` (einmalig), `/anleiter-pruefwarteschlange` (wenn formelle Prüfung aktiviert) | Konfigurierter Beratungsstellenkontext, Prüfung studentischer Arbeit |
| **Studierende** | `/einarbeitung` (Semesterbeginn), dann `/mandant-aufnahme`, `/entwurf`, `/memo`, `/recherche-start`, `/status`, `/mandantenbrief` | Strukturierte Arbeitshilfen, Entwürfe, Rechercheeinstiege |
| **Mandant** | – | Empfängt fertig geprüfte Briefe (Studierender + Anleiter haben freigegeben) |

---

## Schnellstart

```
/rechtsberatungsstelle:rechtsberatungsstelle-kaltstart-interview   # Anleiter: Beratungsstelle konfigurieren
/rechtsberatungsstelle:einarbeitung                   # Studierender: Einarbeitung zum Semesterbeginn
/rechtsberatungsstelle:mandant-aufnahme          # Neues Mandat aufnehmen
/rechtsberatungsstelle:memo                   # Gutachtenstil-Memo erstellen
/rechtsberatungsstelle:entwurf                  # Schriftsatz entwerfen
/rechtsberatungsstelle:fristen              # Fristen prüfen
/rechtsberatungsstelle:mandantenbrief          # Mandantenbrief in einfacher Sprache
/rechtsberatungsstelle:semester-uebergabe       # Semesterübergabe vorbereiten
```

---

## Beratungsstellentypen, die dieses Plugin unterstützt

### Universitäre Refugee Law Clinics (RLC)

Hochschulverankerte Kliniken wie die **Refugee Law Clinic Berlin** (HU Berlin/FU Berlin), die **Refugee Law Clinic Bremen** (Universität Bremen) oder die **Refugee Law Clinic Köln** (Universität zu Köln) beraten Asylsuchende und Geduldete zu Fragen des AsylG, AufenthG und SGB II. Besonderheiten:
- Kurze Fristen (§§ 36, 74 AsylG): Klagen gegen BAMF-Bescheide oft binnen 1–2 Wochen nach Zustellung.
- Sprachbarrieren: Dolmetscher-Koordination ist Teil des Intakes.
- Schnittstellen zu § 76b SGB IX (Eingliederungshilfe für Geflüchtete).

### Studentische Rechtsberatung nach § 6 Abs. 2 Nr. 2 RDG

Allgemeine studentische Beratungsstellen an Universitäten (oft "JuRI", "Jura hilft" o. ä.). Fokus: SGB II (Bürgergeld), Mietrecht, Verbraucherrecht, Familienrecht. Betrieb ausschließlich unter Aufsicht zugelassener Anwälte oder habilitierter Volljuristen.

### AnwVer/DAV Pro-Bono-Initiativen

Anwaltsverein-getragene Pro-Bono-Programme (z. B. **Pro Bono Berlin e. V.**, **DAV Pro Bono**): hier beraten zugelassene Anwälte direkt, die Plugin-Komponenten `entwurf`, `memo` und `recherche-start` unterstützen die Mandatsarbeit.

### Verbraucherzentralen (§ 8 RDG)

Verbraucherzentralen besitzen eine Sondererlaubnis nach § 8 Abs. 1 Nr. 4 RDG. Das Plugin unterstützt Standardfälle: Mieterhöhung, Kündigung, AGB-Kontrolle (§§ 305 ff. BGB), Energiekosten-Nachforderungen.

### Sozialberatung

Anerkannte Beratungsträger (AWO, Caritas, Diakonie, DRK, Paritätischer) arbeiten nach § 8 Abs. 1 Nr. 4 RDG. Schwerpunkte: SGB II, SGB XII, SGB IX, Rentenrecht (§ 109 SGB VI), Pflegegeld (§ 76b SGB IX).

---

## Beispiele: Pro-Bono-Initiativen in Berlin und Bremen

| Initiative | Ort | Schwerpunkt | Rechtsgrundlage |
|---|---|---|---|
| Refugee Law Clinic Berlin (HU/FU) | Berlin | AsylG, AufenthG, SGB II | § 6 II Nr. 2 RDG |
| Pro Bono Berlin e. V. | Berlin | Zivilrecht, Mietrecht, Familienrecht | Zugelassene Anwälte |
| Berliner Mieterverein – Rechtsberatung | Berlin | Mietrecht | § 8 I Nr. 3 RDG (Verband) |
| Refugee Law Clinic Bremen | Bremen | AsylG, AufenthG | § 6 II Nr. 2 RDG |
| Verbraucherzentrale Bremen | Bremen | Verbraucherrecht, Mietrecht | § 8 I Nr. 4 RDG |
| JuRI – Juristische Interessenvertretung (Uni Bremen) | Bremen | SGB II, allg. Zivilrecht | § 6 II Nr. 2 RDG |
| Caritas Berlin – Migrationsberatung | Berlin | AufenthG, SGB II | § 8 I Nr. 4 RDG |

---

## Fachbereiche und Skills

| Skill | Zweck | Primäre Normen |
|---|---|---|
| `leitfaden-erstellen` | Leitfaden zum Aufbau einer Beratungsstelle | RDG, BRAO |
| `mandanten-kommunikations-log` | Mandantenkommunikations-Logbuch | § 43a BRAO, § 203 StGB |
| `mandant-aufnahme` | Intake mit RDG-Konfliktprüfung | § 6 II Nr. 2 RDG |
| `mandantenbrief` | Mandantenbrief in einfacher Sprache | BORA |
| `rechtsberatungsstelle-kaltstart-interview` | Ersteinrichtung der Beratungsstelle | RDG, BRAO |
| `rechtsberatungsstelle-anpassen` | Beratungsstellenprofil anpassen | – |
| `fristen` | Fristenkontrolle | § 84 SGG, § 74 VwGO, §§ 36, 74 AsylG |
| `entwurf` | Schriftsatzentwurf | ZPO, VwGO, SGG |
| `formular-erzeugung` | Formularerstellung (PKH, BerHG, KSchG) | §§ 114 ff. ZPO, BerHG |
| `memo` | Memo im Gutachtenstil | – |
| `einfache-sprache-briefe` | Einfache Sprache | BORA |
| `einarbeitung` | Einarbeitung Studierende | § 6 II Nr. 2 RDG |
| `recherche-start` | Rechercheeinstieg | juris, Beck-Online, gesetze-im-internet.de |
| `semester-uebergabe` | Semesterübergabe | – |
| `status` | Statusbericht | – |
| `anleiter-pruefwarteschlange` | Aufsichts-Reviewqueue | § 6 II Nr. 2 RDG, § 43a BRAO |

---

## Qualitätssicherung

Alle studentischen Outputs tragen den Vermerk:

> **[KI-GESTÜTZTER ENTWURF – Analyse durch Studierende und Freigabe durch anleitenden Volljuristen erforderlich. Kein Versand ohne Prüfung.]**

Nur der anleitende Jurist kann diesen Vermerk entfernen. Dokumente, die diesen Vermerk tragen, dürfen nicht unmittelbar an Mandanten oder Behörden gesendet werden.

---

## Zitierweise

Alle juristischen Quellen folgen `../references/zitierweise.md`. Beispiele:
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Krenzler, in: Krenzler (Hrsg.), RDG, 2. Aufl. 2021, § 6 Rn. 45.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 59 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anlaufstellen-beweislast-anleiter-bono` | Anlaufstellen: Beweislast, Darlegungslast und Substantiierung im Rechtsberatungsstelle. |
| `anleiter-formular-portal-und-einreichung` | Anleiter: Formular, Portal und Einreichungslogik im Rechtsberatungsstelle. |
| `anleiter-pruefwarteschlange` | 'Supervisoren-Prüfwarteschlange — studentische Arbeitsergebnisse warten hier auf die Supervisoren-Freigabe, bevor sie an Mandanten oder Gerichte gehen. Nur aktiv, wenn das Supervisionsmodell 'formelle Prüfwarteschlange' gewählt wurde; an... |
| `anpassen` | Rechtsberatungsstelle-Plugin an spezifische Kanzlei oder Uni anpassen: Anwendungsfall neue Rechtsberatungsstelle moechte Plugin konfigurieren mit eigenen Rechtsgebieten Zielgruppe und Verfahrensregeln. BeratungsHiG, BRAO, hochschulspezif... |
| `anschluss-router` | Einstieg, Schnelltriage und Fallrouting im Rechtsberatungsstelle-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei D... |
| `bono-erstpruefung-und-mandatsziel` | Bono: Erstprüfung, Rollenklärung und Mandatsziel im Rechtsberatungsstelle. |
| `briefe-erstberatung-rdg-konform` | Briefe: Zahlen, Schwellenwerte und Berechnung im Rechtsberatungsstelle. |
| `dokumente-intake` | Dokumentenintake für Rechtsberatungsstelle (RDG): sortiert Beratungshilfeschein, Vermögenserklärung, Bescheide Sozialleistungen, prüft Datum, Absender, Frist und Beweiswert (Einkommensnachweise, Bescheide); markiert Lücken; berücksichtig... |
| `einarbeitung` | Semestereinarbeitung für neue studentische Berater — Einführung in die Beratungsstellenstruktur, RDG-Grundlagen, Toolwalkthrough und Übungsaufgaben vor dem ersten echten Mandat. Liest das vom Supervisor hinterlegte Handbuch und vermittel... |
| `einfache-sprache-briefe` | Anwalts- und Behördenbriefe in leichte oder einfache Sprache übersetzen: Anwendungsfall Mandant mit sprachlichen Einschraenkungen oder geringem Bildungsniveau soll Schreiben von Behörde Gericht oder Gegenseite verstehen. BeratungsHiG kos... |
| `einstieg-routing` | Einstieg, Triage und Routing für Rechtsberatungsstelle (RDG): ordnet Rolle (Hilfesuchender, Berater, Amtsgericht), markiert Frist (Beratungshilfe-Antrag vor Tätigkeit), wählt Norm (RDG, BeratungshilfeG, Prozesskostenhilfe ZPO §§ 114 ff.)... |
| `entwurf-einarbeitung-einfache-sprache` | Erstellt einen Erstentwurf häufiger Schriftstücke der Rechtsberatungsstelle — Rechtsgebiet-spezifische Muster (Widerspruchsschreiben, Mietrechtsbriefe, Klageschriften im Beratungshilfe-Kontext, Mahnschreiben), § 6 RDG-konforme Formulieru... |
| `erstberatung-rdg-grenzen-und-triage` | Erstberatung mit RDG-Grenzen und Triage: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Rechtsberatungsstelle. |
| `erzeugung-leitfaden-erstellen-mandanten` | Formulare und Antragsdokumente für Rechtsberatungsstelle erstellen: Anwendungsfall Mandant braucht ausgefuellten Antrag Vollmacht Widerspruch oder Schriftsatz für Behörde oder Gericht. BeratungsHiG Beratungsschein, BRAO, Formulare Sozial... |
| `fristen-fristenkontrolle-rdg` | Fristenmanagement für die Rechtsberatungsstelle — Fristen eintragen, gesamtübergreifende Übersicht abrufen, aktualisieren, als erledigt markieren oder schließen. Warnt bei konfigurierbaren Schwellenwerten (Standard: 14/7/3/1 Tage); überf... |
| `fristen-risikoampel-mandantenkommunikation` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Rechtsberatungsstelle. |
| `fristenkontrolle-behoerden-gericht-und-registerweg` | Fristenkontrolle: Behörden-, Gerichts- oder Registerweg im Rechtsberatungsstelle. |
| `kaltstart-interview` | Rechtsberatungsstelle Kaltstart und Erst-Konfiguration: Anwendungsfall neue Rechtsberatungsstelle oder neues Semester startet und Plugin muss mit Rechtsgebieten Hochschule Anleiter und Beratungsregeln eingerichtet werden. BeratungsHiG §... |
| `konform-dokumentenmatrix-und-lueckenliste` | Konform: Dokumentenmatrix, Lückenliste und Nachforderung im Rechtsberatungsstelle. |
| `leitfaden-erstellen` | Leitfaden und Merkblatt für Rechtsberatungsstelle erstellen: Anwendungsfall Studenten der Rechtsberatungsstelle brauchen praxistaugliche Leitfaeden für häufige Mandats-Konstellationen in leicht verstaendlicher Sprache. BeratungsHiG niedr... |
| `mandant-aufnahme` | Mandantenaufnahme in der Rechtsberatungsstelle strukturieren: Anwendungsfall Student nimmt erstmals Mandanten auf und muss Sachverhalt strukturiert erfassen Rechtsgebiet einordnen und naechste Schritte bestimmen. BeratungsHiG § 2 Beratun... |
| `mandanten-kommunikations-log` | Mandantenkommunikation dokumentieren und Kommunikations-Log führen: Anwendungsfall Rechtsberatungsstelle muss Beratungsgespraeache E-Mails und Entscheidungen vollständig und datenschutzkonform dokumentieren. DSGVO Datenschutz studentisch... |
| `mandantenbrief-memo-rbs-beratungshilfe` | Mandantenbrief für Rechtsberatungsstelle verfassen: Anwendungsfall Rechtsberatungsstelle muss Mandanten über Ergebnis der Beratung informieren oder Schreiben an Gegenseite Behörde oder Gericht vorbereiten. BeratungsHiG niedrigschwellige... |
| `mandantenfreundliche-quellenkarte-check` | Mandantenfreundliche Quellenkarte Check: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `mandantenintake-mandatsuebergabe` | Mandantenintake: Risikoampel, Gegenargumente und Verteidigungslinien im Rechtsberatungsstelle. |
| `mandatsuebergabe-international-schnittstellen` | Mandatsuebergabe: Internationaler Bezug und Schnittstellen im Rechtsberatungsstelle. |
| `memo` | Erstellt ein Gutachten-Gerüst nach der deutschen Gutachtenmethode (Obersatz — Definition/Norm — Subsumtion — Ergebnis) mit gekennzeichneten Recherchelücken — das Gerüst, nicht die Analyse selbst. Normblöcke sind mit RECHERCHE ERFORDERLIC... |
| `output-waehlen` | Output-Wahl für Rechtsberatungsstelle (RDG): stimmt Adressat (Hilfesuchender, Berater, Amtsgericht), Frist (Beratungshilfe-Antrag vor Tätigkeit) und Form auf den Zweck ab — typische Outputs: Erstberatungsmemo, Beratungshilfeantrag, Weite... |
| `pro-bono-mandatsuebergabe` | Pro-Bono-Mandatsübergabe mit Fristen und Zuständigkeiten: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Rechtsberatungsstelle. |
| `pruefwarteschlange-red-rbst-recherche` | Prüfwarteschlange: Red-Team und Qualitätskontrolle im Rechtsberatungsstelle. |
| `quellen-livecheck` | Quellen-Live-Check für Rechtsberatungsstelle (RDG): prüft Normen (RDG, BeratungshilfeG, Prozesskostenhilfe ZPO §§ 114 ff.) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Amtsgericht und Quellenhygiene nach refere... |
| `rbs-beratungshilfe-und-pkh-praxis` | Beratungshilfe BerHG und PKH in der Praxis: Antrag beim Amtsgericht, Berechtigung Einkommen, Vermoegen, Wahrnehmungsbefugnis Anwalt. Schnittstelle PKH-Antrag. Mustertexte und Berechtigungsnachweise im Rechtsberatungsstelle. |
| `rbs-einfuehrung-rdg-rbst-anlaufstellen` | Rechtsberatungsstelle einfuehrend: typische Beratungsfelder Mietrecht, Sozialrecht, Familienrecht, Arbeitsrecht, Verbraucherrecht. Schutzfunktion für Beratungsberechtigte, Schnittstelle Beratungshilfe BerHG. Entscheidungstabelle im Recht... |
| `rbs-rdg-grenzen-spezial` | Spezialfall RDG-Grenzen: was darf eine Rechtsberatungsstelle, ehrenamtlich vs. Anwalt, Erlaubnistatbestaende. Schnittstelle Verbraucherschuldnerberatung, Mieterverein, Sozialverband. Prüfraster und Mandanteninformation im Rechtsberatungs... |
| `rbst-anlaufstellen-bauleiter` | Bauleiter Anlaufstellen Rechtsberatung: Beratungshilfe, Prozesskostenhilfe, Schuldnerberatung, Mietervereine, Verbraucherzentrale. Prüfraster für Mandant und Sozialberatung im Rechtsberatungsstelle. |
| `rbst-beratungshilfe-prozesskostenhilfe` | Leitfaden Beratungshilfe und Prozesskostenhilfe: Antragsvoraussetzungen, Vermoegen, Erfolgsaussicht, Eigenbeitrag. Prüfraster für Mandant und Rechtsanwalt im Rechtsberatungsstelle. |
| `rbst-mandantenkommunikation-entscheidungsvorlage` | Rbst: Mandantenkommunikation und Entscheidungsvorlage im Rechtsberatungsstelle. |
| `rbst-niedrigschwellige-onlineberatung-spezial` | Spezialfall niedrigschwellige Onlineberatung mit KI-Unterstuetzung: Hinweispflichten, Verbraucherschutz, Datenschutz, Haftung. Prüfraster für Anbieter im Rechtsberatungsstelle. |
| `rbst-rdg-grenzen-spezial` | Spezialfall RDG-Grenzen für Nichtanwaelte: Verbraucherzentrale, Mietervereine, Inkassodienstleister, Legal-Tech. Prüfraster für Erlaubnispflicht im Rechtsberatungsstelle. |
| `rdg-fristen-form-und-zustaendigkeit` | RDG: Fristen, Form, Zuständigkeit und Rechtsweg im Rechtsberatungsstelle. |
| `recherche-mehrparteien-konflikt-und-interessen` | Recherche: Mehrparteienkonflikt und Interessenmatrix im Rechtsberatungsstelle. |
| `recherche-start-rechtsberatungsstelle` | Recherchefahrplan für eine Rechtsfrage — einschlägige Normen, Rechtsprechungsbereiche, verifizierbare Quellen, Suchbegriffe für amtliche/freie Quellen oder lizenzierte Datenbanken/dejure. Hinweise und Rahmen, KEINE geprüften Belege; Stud... |
| `rechtsberatung-uebergabe-schriftsatz-brief-memo-bausteine-status` | Übergabe: Schriftsatz-, Brief- und Memo-Bausteine im Rechtsberatungsstelle. |
| `rechtsberatungsstellen` | Rechtsberatungsstelle: Compliance-Dokumentation und Aktenvermerk im Rechtsberatungsstelle. |
| `rechtsberatungsstellen-tatbestand-beweis-und-belege` | Rechtsberatungsstellen: Tatbestandsmerkmale, Beweisfragen und Beleglage im Rechtsberatungsstelle. |
| `semester-uebergabe` | Semesterabschluss-Übergabe — das Gegenstück zu `/einarbeitung`. Erstellt fallbezogene Übergabenotizen und eine Kohorten-Gesamtübersicht, damit die abgehende Kohorte die laufenden Mandate unter Wahrung des Mandatsgeheimnisses sauber an di... |
| `semesterende-verhandlung-vergleich-und-eskalation` | Semesterende: Verhandlung, Vergleich und Eskalation im Rechtsberatungsstelle. |
| `sonderfall-edge-case` | Kaltstart: Sonderfall und Edge-Case-Prüfung: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verf... |
| `spezial-mandantenfreundliche-livequellen-check` | Mandantenfreundliche: Livequellen- und Rechtsprechungscheck. |
| `spezial-pruefwarteschlange-red-team-und-qualitaetskontrolle` | Pruefwarteschlange: Red-Team und Qualitätskontrolle. |
| `spezial-uebergabe-schriftsatz-brief-und-memo-bausteine` | Uebergabe: Schriftsatz-, Brief- und Memo-Bausteine. |
| `status` | Fallstatuszusammenfassung nach Zielgruppe — mandantengerichtet (verständliche Sprache), intern (für den Supervisor) oder gerichts-/behördengerichtet (formale Schriftsatzform per Verfahrensordnung). Gleiche Fakten, unterschiedliche Darste... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Rechtsberatungsstelle (RDG): trennt fehlende Tatsachen von fehlenden Belegen (Beratungshilfeschein, Vermögenserklärung, Bescheide Sozialleistungen), nennt pro Lücke Beweisthema, Beschaffungsweg (Amtsgeri... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router: schlägt nach der ersten Prüfung die passenden Fachmodule aus demselben Plugin vor im Rechtsberatungsstelle. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Rechtsberatungsstelle. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Rechtsberatungsstelle. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Rechtsberatungsstelle. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Unified Mini Prompt und Mega-Prompt

Für normale Chatbots ohne Plugin-Installation gibt es den **Unified Mini Prompt**: eine einzelne Markdown-Datei bis 7.500 Zeichen, die den Kern-Workflow dieses Plugins verdichtet und als Release-Asset direkt herunterladbar ist.

- **Sparversion herunterladen:** [`rechtsberatungsstelle-unified-mini-prompt.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/rechtsberatungsstelle-unified-mini-prompt.md)
- **Großer Mega-Prompt nur zur Anschauung im Repo:** [`testakten/megaprompts/rechtsberatungsstelle.md`](../testakten/megaprompts/rechtsberatungsstelle.md) (137 KB)

Der große Mega-Prompt wird nicht als installierbares Plugin und nicht als CoWork-Uploadmaterial ausgeliefert. Für echte Plugin-Nutzung bitte das Plugin-ZIP verwenden; für Ein-Datei-Nutzung den Unified Mini Prompt.

<!-- END megaprompt-und-vorlagen (autogen) -->
