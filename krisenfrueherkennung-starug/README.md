# Krisenfrüherkennung und StaRUG-Management

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Krisenfrüherkennung und Krisenmanagement nach StaRUG: Pflicht zum 24-Monats-Frühwarnsystem nach § 1 StaRUG, § 102 StaRUG Warnpflicht der Berater, Geschäftsführerhaftung, drohende Zahlungsunfähigkeit, integrierte Planung, Restrukturierungsplan und Stabilisierungsanordnung.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`krisenfrueherkennung-starug.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/krisenfrueherkennung-starug.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/krisenfrueherkennung-starug/krisenfrueherkennung-starug-werkstatt.md" download><code>krisenfrueherkennung-starug-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/krisenfrueherkennung-starug/krisenfrueherkennung-starug-schnellstart.md" download><code>krisenfrueherkennung-starug-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | Krisenfrüherkennung & StaRUG – Vier Varianten: [Gesamt-PDF](../testakten/krisenfrueherkennung-starug-vier-varianten/gesamt-pdf/krisenfrueherkennung-starug-vier-varianten_gesamt.pdf), [`testakte-krisenfrueherkennung-starug-vier-varianten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-krisenfrueherkennung-starug-vier-varianten.zip), [`testakte-krisenfrueherkennung-starug-vier-varianten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-krisenfrueherkennung-starug-vier-varianten-einzelpdfs.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du Eroeffnungsgrund und Fortbestehensprognose belastbar bestimmen und den naechsten Verfahrensschritt wählen.
**Plugin-Slug:** `krisenfrueherkennung-starug`
**Version:** 3.2.1
**Autor:** Klotzkette

---

## Installation

1. ZIP aus dem Release herunterladen.
2. Plugin-Umgebung öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `krisenfrueherkennung-starug.zip` hochladen.
5. Mit einem konkreten Auftrag starten, zum Beispiel: `Prüfe unser Frühwarnsystem nach § 1 StaRUG und bewerte die GF-Haftung.`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

## Kernbotschaft

> Krisenfrüherkennung ist keine betriebswirtschaftliche Kür, sondern gesetzliche Pflicht mit direkter persönlicher Haftungskonsequenz. § 1 StaRUG verlangt einen 24-Monats-Planungshorizont. Wer die Datenlage nicht im Griff hat, verliert in der Krise das Heft des Handelns und den Zugriff auf moderne Sanierungswerkzeuge.

---

## Überblick

Dieses Plugin bietet kanzleitaugliche Werkzeuge für Geschäftsführer, Restrukturierungsberater, Steuerberater, Wirtschaftsprüfer und Rechtsanwälte im Bereich der gesetzlichen Krisenfrüherkennung nach § 1 StaRUG. Der Fokus liegt auf dem 24-Monats-Planungshorizont, der persönlichen Haftung der Geschäftsführung und der praktischen Anwendung der StaRUG-Sanierungswerkzeuge.

## Zielgruppe

- Geschäftsführer und Vorstände mittelständischer Unternehmen
- Restrukturierungsberater und Insolvenzverwalter
- Steuerberater und Wirtschaftsprüfer mit Mandantenwarnpflicht nach § 102 StaRUG
- Rechtsanwälte im Sanierungs- und Insolvenzrecht
- Compliance-Beauftragte

---

## Skills-Übersicht

### Block A — Rechtliche Grundlagen & Pflichten

| Skill | Thema |
|---|---|
| `paragraph-1-starug-pflichten-und-24-monats-horizont` | § 1 StaRUG Volltext-Auslegung, 24-Monats-Planungshorizont, Abgrenzung § 18 InsO |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg` | Persönliche Haftung, Business Judgment Rule in der Krise, Beweislastumkehr |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

### Block B — 24-Monats-Frühwarnsystem aufbauen

| Skill | Thema |
|---|---|
| `fruehwarnsystem-architektur-zwei-jahres-horizont` | IDW S 6 + IDW PS 340 n.F., Risiko-Inventar, KPI-Kaskade, Eskalationsstufen |
| `rollierende-liquiditaetsplanung-24-monate-template` | Zweijahres-Liquiplan, wöchentliche + monatliche Granularität, Stresstests |
| `integrierte-planung-guv-bilanz-cashflow` | Drei-Statement-Modell, Working-Capital-Modellierung, Investitions-/Finanzierungsplan |
| `kennzahlenset-und-ampelsystem-starug-konform` | Frühwarn-KPIs, Ampelsystem rot/gelb/grün mit numerischen Schwellen |

### Block C — Krisenstadien-Diagnostik

| Skill | Thema |
|---|---|
| `krisenstadien-stakeholder-strategie-ergebnis-liquiditaet` | IDW S 6 Stadienlehre, Diagnose-Checklisten je Stadium |
| `drohende-zahlungsunfaehigkeit-paragraph-18-inso` | Prognosezeitraum, Wahrscheinlichkeitsmaßstab, Abgrenzung §§ 17/19 InsO |
| `fortbestehensprognose-zweistufig` | Positive Fortführungsprognose IDW S 11, Dokumentationspflicht |
| `insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist` | § 15a InsO Triggerlogik, Maximalfrist, strafrechtliche Sanktion |

### Block D — StaRUG-Werkzeuge nutzen

| Skill | Thema |
|---|---|
| `restrukturierungsplan-architektur-paragraph-7ff-starug` | Planbestandteile, Gruppenbildung § 9, Mehrheit § 25, gerichtliche Bestätigung |
| `stabilisierungsanordnung-und-vollstreckungssperre` | §§ 49-59 StaRUG, Voraussetzungen, Antragsmuster |
| `cross-class-cram-down-und-absolute-priority` | § 26 StaRUG, gerichtliche Plan-Bestätigung, Schlechterstellungsverbot |
| `restrukturierungsbeauftragter-und-sachwalter` | § 73 StaRUG, Auswahl, Aufgaben, Honorar-Festsetzung |

### Block E — Kanzlei- und Geschäftsführer-Werkzeuge

| Skill | Thema |
|---|---|
| `dokumentationspflicht-und-protokollierung-geschaeftsfuehrung` | Krisenprotokoll, Sitzungs-Templates, Beweissicherung |
| `mandantenbrief-warnung-paragraph-102-starug-template` | Volltext-Templates § 102-StaRUG-Warnung, Eskalationsstufen |
| `restructuring-lounge-impulsvortrag-toolkit` | Foliensätze, Talking-Points, Q&A-Fallnetz für Vortragsformate |

---

## Rechtlicher Hinweis

Alle in diesem Plugin verwendeten Personen, Kanzleinamen und Mandantennamen sind fiktiv. Das Plugin dient der allgemeinen rechtlichen Information und ersetzt keine individuelle Rechtsberatung im Einzelfall.

---

## Rechtsgrundlagen (Kernreferenzen)

- §§ 1, 7-9, 25, 26, 29-31, 49-59, 73, 102 StaRUG
- §§ 15a, 17, 18, 19 InsO
- § 43 GmbHG
- § 93 AktG
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- IDW S 6 (Sanierungskonzepte)
- IDW S 11 (Beurteilung des Vorliegens von Insolvenzeröffnungsgründen)
- IDW PS 340 n.F. (Risikofrüherkennungssysteme)

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `anschluss-routing`, `dokumente-intake`, `einstieg-routing`, `start-chronologie-fristen`, `workflow-kaltstart-und-routing` |
| 2. Unterlagen, Sachverhalt und Quellen | `ampelsystem-beweislast-und-darlegungslast`, `dokumentationspflicht-und-protokollierung-geschaeftsfuehrung`, `geschaeftsfuehrerhaftung-quellenkarte-check`, `krisenmanagement-tatbestand-beweis-und-belege`, `quellen-livecheck`, `restrukturierungsplan-formular-portal-und-einreichung`, `spezial-geschaeftsfuehrerhaftung-livequellen-check`, `unterlagen-luecken`, `workflow-chronologie-und-belegmatrix`, `workflow-unterlagen-lueckenliste`, `zahlungsunfaehigkeit-compliance-dokumentation-und-akte` |
| 3. Prüfung, Anspruch und Subsumtion | `gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg`, `krisenstadien-fristennotiz-starug-gf-haftung`, `monats-risikoampel-und-gegenargumente`, `workflow-fristen-und-risikoampel` |
| 4. Gestaltung, Strategie und Verhandlung | `integrierte-planung-kennzahlenset-ampelsystem`, `kfe-restrukturierungsbeauftragter`, `krisenstadien-stakeholder-strategie-ergebnis-liquiditaet`, `pflicht-planung-restrukturierungsplan`, `planung-internationaler-bezug-und-schnittstellen`, `restrukturierungsbeauftragter-und-sachwalter`, `restrukturierungsplan-architektur-rollierende`, `rollierende-liquiditaetsplanung-24-monate-template` |
| 5. Verfahren, Behörde und Gericht | `fruehwarnsystem-behoerden-gericht-und-registerweg`, `insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist`, `stabilisierungsanordnung-und-vollstreckungssperre`, `starug-fristen-form-und-zustaendigkeit`, `starug-stabilisierungsanordnung-vollstreckungsstopp`, `warnpflicht-schriftsatz-brief-und-memo-bausteine` |
| 6. Ergebnis, Schreiben und Kommunikation | `mandantenbrief-warnung-paragraph-starug`, `mandantenkommunikation-redteam`, `output-waehlen` |
| 7. Kontrolle, Qualität und Gegenprüfung | `workflow-redteam-qualitygate` |
| 8. Spezialmodule und Schnittstellen | `berater-drohende-fruehwarnsystem`, `cross-class-cram-down-und-absolute-priority`, `drohende-zahlen-schwellen-und-berechnung`, `drohende-zahlungsunfaehigkeit`, `fortbestehensprognose-zweistufig`, `fruehwarnsystem-architektur-zwei-jahres-horizont`, `integrierte-interessen-kennzahlenset`, `kennzahlenset-mandantenentscheidung`, `kennzahlenset-und-ampelsystem-starug-konform`, `kfe-fruherkennungssystem-bauleiter`, `kfe-krisenstab-cross-class`, `kfe-krisenstab-massnahmen-leitfaden`, `kfe-stabilisierungsanordnung-spezial`, `konform-sonderfall-und-edge-case`, `krisenfrueherkennung-krisenmanagement-monats`, `paragraph-1-starug-pflichten-und-24-monats-horizont`, `paragraph-102-starug-warnpflicht-bei-rechtsberatern`, `pflichtenkollision-shift-restructuring-lounge`, ... plus 2 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 58 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ampelsystem-beweislast-und-darlegungslast` | Ampelsystem: Beweislast, Darlegungslast und Substantiierung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `anschluss-routing` | Anschluss-Routing für Krisenfrüherkennung StaRUG: wählt den nächsten Spezial-Skill nach Engpass (Frühzeitige Indikatoren, Liquiditätsplan, Frühwarn-Indikatoren, Sanierungskonzept IDW S 6), dokumentiert Router-Entscheidung mit Begründung. |
| `berater-drohende-fruehwarnsystem` | Berater: Verhandlung, Vergleich und Eskalation. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `cross-class-cram-down-und-absolute-priority` | Cross-Class-Cram-Down und Absolute-Priority-Rule im StaRUG-Plan: Gericht soll Plan gegen ablehnende Gläubiger-Gruppen bestätigen. Normen: § 26 StaRUG (Cram-Down-Voraussetzungen), § 30 StaRUG (Schlechterstellungsverbot), § 31 StaRUG (Obst... |
| `dokumentationspflicht-und-protokollierung-geschaeftsfuehrung` | Krisenprotokollierung der Geschäftsführung für Haftungsschutz: GmbH-Geschäftsführer oder AG-Vorstand will Entscheidungen in der Krise dokumentieren. Normen: § 43 GmbHG (Sorgfaltspflicht und Haftung), § 93 Abs. 2 S. 2 AktG (Beweislastumke... |
| `dokumente-intake` | Dokumentenintake für Krisenfrüherkennung StaRUG: sortiert Liquiditätsplan, Frühwarn-Indikatoren, Sanierungskonzept IDW S 6, prüft Datum, Absender, Frist und Beweiswert (Forderungen offen, Bankenrunde-Protokolle); markiert Lücken; berücks... |
| `drohende-zahlen-schwellen-und-berechnung` | Drohende: Zahlen, Schwellenwerte und Berechnung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `drohende-zahlungsunfaehigkeit` | Drohende Zahlungsunfähigkeit nach § 18 InsO feststellen: Berater oder GF prüft ob StaRUG-Zugangsberechtigung besteht. Normen: § 18 InsO (drohende ZU), § 17 InsO (aktuelle ZU), § 19 InsO (Überschuldung), § 1 StaRUG (Zugangsberechtigung).... |
| `einstieg-routing` | Einstieg, Triage und Routing für Krisenfrüherkennung StaRUG: ordnet Rolle (Geschäftsführung, Aufsichtsrat, Berater (WP, RA)), markiert Frist (Frühzeitige Indikatoren), wählt Norm (StaRUG § 1 Krisenfrüherkennung, § 18 InsO drohende ZU) un... |
| `fortbestehensprognose-zweistufig` | Zweistufige Fortbestehensprognose nach IDW S 11 erstellen: Unternehmen ist möglicherweise ueberschuldet und braucht positive Fortführungsprognose. Normen: § 19 InsO (Überschuldungsbegriff modifiziert), IDW S 11 (Fortbestehensprognose-Sta... |
| `fruehwarnsystem-architektur-zwei-jahres-horizont` | StaRUG-konformes Fruehwarnsystem mit 24-Monats-Horizont architektieren: Unternehmen will § 1 StaRUG Krisenfrueherkennung implementieren. Normen: § 1 StaRUG (Frueherkennungspflicht), IDW S 6 (Sanierungsstandard), IDW PS 340 n.F. (Risikoma... |
| `fruehwarnsystem-behoerden-gericht-und-registerweg` | Fruehwarnsystem: Behörden-, Gerichts- oder Registerweg. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `geschaeftsfuehrerhaftung-quellenkarte-check` | Geschäftsführerhaftung Quellenkarte Check: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `gf-haftung-paragraph-43-gmbhg-und-paragraph-93-aktg` | Geschäftsführerhaftung bei Krisenversagen prüfe und begrenzen: GF oder Berater will Haftungsrisiken einschaetzen und Enthaftungsstrategien entwickeln. Normen: § 43 GmbHG (Sorgfaltspflicht), § 93 AktG (Vorstandshaftung), § 93 Abs. 2 S. 2... |
| `insolvenzantragspflicht-paragraph-15a-inso-und-drei-wochen-frist` | Insolvenzantragspflicht nach § 15a InsO und Drei-Wochen-Frist: GF prüft ob Insolvenzantrag gestellt werden muss. Normen: § 15a InsO (Antragspflicht), § 15a Abs. 4 InsO (Strafbarkeit), § 18 InsO (drohende ZU als StaRUG-Tor), § 1 StaRUG (F... |
| `integrierte-interessen-kennzahlenset` | Integrierte: Mehrparteienkonflikt und Interessenmatrix. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `integrierte-planung-kennzahlenset-ampelsystem` | Integriertes Drei-Statement-Modell (GuV/Bilanz/Cashflow) für StaRUG-Planung erstellen: Sanierungsberater braucht konsistentes Planungsmodell. Normen: IDW S 6 (Sanierungsstandard), IDW S 11 (Fortbestehensprognose), HGB §§ 242 ff. (Jahresa... |
| `kennzahlenset-mandantenentscheidung` | Kennzahlenset: Mandantenkommunikation und Entscheidungsvorlage. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `kennzahlenset-und-ampelsystem-starug-konform` | StaRUG-konformes KPI-Set und Ampelsystem für Krisenfrueherkennung definieren: Berater oder GF braucht messbare Schwellenwerte für Krisen-Monitoring. Normen: § 1 StaRUG (Frueherkennungspflicht), IDW PS 340 n.F. Prüfraster: Liquiditaetsrei... |
| `kfe-fruherkennungssystem-bauleiter` | Bauleiter Frueherkennungssystem § 1 StaRUG: Risikolandkarte, Indikatoren, Eskalationsstufen, Berichtswege an Geschäftsleitung und Aufsichtsorgan. Prüfraster für mittelstaendische GmbH im Krisenfrueherkennung Starug. |
| `kfe-krisenstab-cross-class` | Leitfaden Krisenstab und Sofortmassnahmen: Kommunikation Bank / Lieferant / Mitarbeiter / Mandanten, Treasury, Liquiditaetssteuerung. Prüfraster für Geschäftsleitung im Krisenfrueherkennung Starug. |
| `kfe-krisenstab-massnahmen-leitfaden` | Leitfaden Krisenstab und Sofortmassnahmen: Kommunikation Bank / Lieferant / Mitarbeiter / Mandanten, Treasury, Liquiditaetssteuerung. Pruefraster fuer Geschaeftsleitung. |
| `kfe-restrukturierungsbeauftragter` | Spezialfall Restrukturierungsbeauftragter §§ 73 ff. StaRUG: Bestellung, Aufgaben, Haftung, Kosten. Prüfraster für Geschäftsleitung und Gläubigerausschuss im Krisenfrueherkennung Starug. |
| `kfe-stabilisierungsanordnung-spezial` | Spezialfall Stabilisierungsanordnung §§ 49 ff. StaRUG: Verwertungs- und Vollstreckungssperre, Voraussetzungen, Befristung. Prüfraster für Antragsteller und betroffene Gläubiger im Krisenfrueherkennung Starug. |
| `konform-sonderfall-und-edge-case` | Konform: Sonderfall und Edge-Case-Prüfung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `krisenfrueherkennung-krisenmanagement-monats` | Krisenfrueherkennung: Erstprüfung, Rollenklärung und Mandatsziel. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `krisenmanagement-tatbestand-beweis-und-belege` | Krisenmanagement: Tatbestandsmerkmale, Beweisfragen und Beleglage. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `krisenstadien-fristennotiz-starug-gf-haftung` | Krisenstadien: Fristennotiz und nächster Schritt. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `krisenstadien-stakeholder-strategie-ergebnis-liquiditaet` | IDW-S-6-Krisenstadien diagnostizieren und Handlungskorridore bestimmen: Berater oder GF will Krisenstadium und passende Maßnahmen ermitteln. Normen: IDW S 6 (Sanierungsstandard: Stakeholder-, Strategie-, Produkt-, Ertrags-, Liquiditaetsk... |
| `mandantenbrief-warnung-paragraph-starug` | Mandantenbrief Warnung Paragraph 102 StaRUG Template: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung im Krisenfrueherkennung Starug. |
| `mandantenkommunikation-redteam` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Krisenfrueherkennung Starug. |
| `monats-risikoampel-und-gegenargumente` | Monats: Risikoampel, Gegenargumente und Verteidigungslinien. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `output-waehlen` | Output-Wahl für Krisenfrüherkennung StaRUG: stimmt Adressat (Geschäftsführung, Aufsichtsrat, Berater (WP, RA)), Frist (Frühzeitige Indikatoren) und Form auf den Zweck ab — typische Outputs: Frühwarn-Indikatoren-Set, Restrukturierungsplan... |
| `paragraph-1-starug-pflichten-und-24-monats-horizont` | § 1 StaRUG Krisenfrueherkenungspflicht und 24-Monats-Horizont erklären und umsetzen: GF oder Berater fragt was StaRUG konkret verlangt. Normen: § 1 StaRUG (Frueherkennungspflicht GmbH/AG), § 18 InsO (drohende ZU als StaRUG-Zugang). Prüfr... |
| `paragraph-102-starug-warnpflicht-bei-rechtsberatern` | Paragraph 102 StaRUG Warnpflicht Bei Rechtsberatern: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung im Krisenfrueherkennung Starug. |
| `pflicht-planung-restrukturierungsplan` | Pflicht: Dokumentenmatrix, Lückenliste und Nachforderung. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `pflichtenkollision-shift-restructuring-lounge` | Pflichtenkollision Und Shift Of Fiduciary Duties: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung im Krisenfrueherkennung Starug. |
| `planung-internationaler-bezug-und-schnittstellen` | Planung: Internationaler Bezug und Schnittstellen. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `quellen-livecheck` | Quellen-Live-Check für Krisenfrüherkennung StaRUG: prüft Normen (StaRUG § 1 Krisenfrüherkennung, § 18 InsO drohende ZU) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Restrukturierungsgericht und Quellenhygiene n... |
| `restructuring-lounge-impulsvortrag-toolkit` | Toolkit für Impulsvorträge zu Krisenfrüherkennung und StaRUG: Foliensatz-Gliederung, Talking-Points, juristische Kernbotschaften, Q-und-A-Fallnetz, Formathinweise für Veranstaltungen wie Branchenlounge-Formate im Krisenfrueherkennung Sta... |
| `restrukturierungsbeauftragter-und-sachwalter` | Restrukturierungsbeauftragter und Sachwalter nach § 73 StaRUG: GF oder Gläubigervertreter prüft Bestellung und Aufgaben. Normen: § 73 StaRUG (Restrukturierungsbeauftragter), §§ 74-77 StaRUG (Pflichtbeauftragung), § 76 StaRUG (Sachwalter)... |
| `restrukturierungsplan-architektur-rollierende` | StaRUG-Restrukturierungsplan nach §§ 7 ff. StaRUG architektieren: Schuldner oder Berater plant außergerichtliche Sanierung unter StaRUG. Normen: §§ 7 ff. StaRUG (Planbestandteile), § 9 StaRUG (Gruppenbildung), § 25 StaRUG (Mehrheitserfor... |
| `restrukturierungsplan-formular-portal-und-einreichung` | Restrukturierungsplan: Formular, Portal und Einreichungslogik. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `rollierende-liquiditaetsplanung-24-monate-template` | Rollierende 24-Monats-Liquiditaetsplanung nach StaRUG erstellen: Sanierungsberater oder GF braucht Liquiditaets-Forecast. Normen: § 1 StaRUG (24-Monats-Horizont), Fortbestehensprognose, Sanierungskonzept. Prüfraster: Woechentliche Granul... |
| `spezial-geschaeftsfuehrerhaftung-livequellen-check` | Geschaeftsfuehrerhaftung: Livequellen- und Rechtsprechungscheck. |
| `stabilisierungsanordnung-und-vollstreckungssperre` | Stabilisierungsanordnung und Vollstreckungssperre nach §§ 49-59 StaRUG beantragen: Schuldner braucht Schutz vor Einzelvollstreckung waehrend Restrukturierung: Stabilisierungsanordnung und Vollstreckungssperre nach §§ 49-59 StaRUG beantra... |
| `stakeholder-warnpflicht-zahlungsunfaehigkeit` | Stakeholder: Abschlussprodukt und Übergabe. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Krisenfrueherkennung Starug-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan.... |
| `starug-fristen-form-und-zustaendigkeit` | StaRUG: Fristen, Form, Zuständigkeit und Rechtsweg. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `starug-stabilisierungsanordnung-vollstreckungsstopp` | Stabilisierungsanordnung: Red-Team und Qualitätskontrolle: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche Frist, Zustellung, Schwelle, Zahlung, Sank... |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Krisenfrüherkennung StaRUG: trennt fehlende Tatsachen von fehlenden Belegen (Liquiditätsplan, Frühwarn-Indikatoren, Sanierungskonzept IDW S 6), nennt pro Lücke Beweisthema, Beschaffungsweg (Restrukturier... |
| `warnpflicht-schriftsatz-brief-und-memo-bausteine` | Warnpflicht: Schriftsatz-, Brief- und Memo-Bausteine. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Krisenfrueherkennung Starug. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Krisenfrueherkennung Starug. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Krisenfrueherkennung Starug. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `zahlungsunfaehigkeit-compliance-dokumentation-und-akte` | Zahlungsunfaehigkeit: Compliance-Dokumentation und Aktenvermerk. Liefert ein belastbares Arbeitsprodukt mit Rückfragen, Normencheck und nächstem Schritt. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
