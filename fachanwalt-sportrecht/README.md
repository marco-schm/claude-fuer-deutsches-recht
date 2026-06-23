# Fachanwalt Sportrecht

Wenn du das hier oeffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen pruefen und ein verwertbares Arbeitsprodukt erhalten.

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Dies ist eines von 229 Plugins aus dem Repo [`claude-fuer-deutsches-recht`](https://github.com/Klotzkette/claude-fuer-deutsches-recht). Das Repo ist von vornherein als **Plugin-Sammlung für Claude Code und Claude Cowork** gebaut: jedes Plugin enthält eine Familie zusammenhängender Skills (`SKILL.md`-Dateien), passende Hilfsdateien, Prüfrastern, Vorlagen und in vielen Fällen eine eigene Testakte. Der vorgesehene Hauptweg ist also: **Plugin in Claude Code / Cowork installieren**, am besten über den Marketplace, alternativ als einzelnes Plugin-ZIP. Dann läuft das Plugin in seiner natürlichen Umgebung mit allen Skills, Werkzeugen und Testdaten.

Damit das Plugin aber auch dann brauchbar bleibt, wenn jemand Claude Code / Cowork gerade nicht nutzen kann oder will (anderer Chatbot, Browser-Nutzung, schneller Test, Schulung, kein Setup zur Hand), gibt es zusätzlich zwei reine **Markdown-Prompts**, die ohne Plugin-Setup funktionieren: einen ausführlichen **Werkstatt-Prompt** und einen kompakten **Schnellstart-Prompt** (höchstens 7500 Zeichen). Beide sind eine einzelne `.md`-Datei, die man in jeden geeigneten Chatbot ziehen, einfügen oder per Copy-and-Paste verwenden kann.

## Downloads

In dieser Reihenfolge gedacht: zuerst der vorgesehene Plugin-Weg für Claude Code / Cowork, danach die Markdown-Alternativen für alles andere, am Schluss die zugehörigen Testakten.

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg, für Claude Code / Cowork) | ZIP | [`fachanwalt-sportrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-sportrecht.zip) |
| Großer Prompt (Werkstatt, Alternative ohne Plugin-Setup) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/fachanwalt-sportrecht/fachanwalt-sportrecht-werkstatt.md" download><code>fachanwalt-sportrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart, höchstens 7500 Zeichen, Spar-Alternative) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/fachanwalt-sportrecht/fachanwalt-sportrecht-schnellstart.md" download><code>fachanwalt-sportrecht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`testakte-doping-uvalkanat-handballerin-cas-lausanne.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-doping-uvalkanat-handballerin-cas-lausanne.zip) (Doping-Verfahren Selin Uvalkanat — Meldonium-Befund, CAS Lausanne, Arbeitsrecht) |

> Marketplace-Hinweis: Wer mehrere Plugins gleichzeitig will, fügt nicht jedes Plugin einzeln hinzu, sondern den ganzen Marketplace über `marketplace.json` aus dem [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest). Dann sind alle 229 Plugins in Claude Code / Cowork verfügbar und können einzeln aktiviert werden.
<!-- END direkt-loslegen (autogen) -->

Plugin Fachanwalt für Sportrecht. Orientierung Verbandsrecht der Sportverbände DFB FIFA UEFA IOC DOSB CAS Schiedsverfahren Spielerverträge Doping WADA-Code NADA Sponsoring Persönlichkeitsrechte Sportler Veranstalterhaftung.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `fachanwalt-sportrecht-orientierung` | Orientierung im Sportrecht — FAO Voraussetzungen Normen typische Mandate Fristen Quellenprüfung. Verbandsrecht der Sportverbände DFB FIFA UEFA IOC DOSB Vereinsrecht BGB §§ 21 ff. Schiedsgerichtsbarkeit CAS Court o… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 78 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anschluss-routing` | Anschluss-Routing für Fachanwalt Sportrecht: wählt den nächsten Spezial-Skill nach Engpass (Berufung CAS 21 Tage, Spielerlizenz, Verbandssatzung, Transferregister), dokumentiert Router-Entscheidung mit Begründung. |
| `athletenvertrag-fristennotiz-und-naechster-schritt` | Athletenvertrag: Fristennotiz und nächster Schritt: Athletenvertrag: Fristennotiz und nächster Schritt. |
| `athletenwerbung-paragraf-3-uwg` | Athletenwerbung § 3 uwg: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `cas-berufung-vorbereiten` | Sportler oder Verein will Entscheidung eines Sportverbands vor dem Court of Arbitration for Sport Lausanne anfechten: Art. R49 CAS Code Fri... |
| `cas-dis-sport-verbands-schiedsverfahren` | Sportler Verein oder Verband wird in Schiedsverfahren vor CAS DIS oder Verbands-Schiedsgericht involviert: WADA-Code Anti-Doping FIFA Players Status C... |
| `code-compliance-dokumentation-und-akte` | Code: Compliance-Dokumentation und Aktenvermerk: Code: Compliance-Dokumentation und Aktenvermerk. |
| `dokumente-intake` | Dokumentenintake für Fachanwalt Sportrecht: sortiert Spielerlizenz, Verbandssatzung, Transferregister, prüft Datum, Absender, Frist und Beweiswert (Spielprotokolle, Doping-Analyse Labor); markiert Lücken; berücksichtigt Mandatsgeheimnis... |
| `doping-cas-berufung` | Athlet muss Doping-Sperre vor CAS anfechten oder WADA/NADA legt Berufung gegen Freispruch ein: WADA-Code strict liability Therapeutic Use Exemption Sanktion 2-4 J... |
| `doping-quellenkarte` | Doping Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `doping-strafrecht-paragraf-4-anti-dopg` | Doping Strafrecht § 4 Anti Dopg: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `doping-verfahren` | Athlet steht vor NADA-Disziplinarverfahren wegen positivem Dopingtest und braucht Verteidigung: NADA-Code WADA-Code strict liability Art. 2 Abs. 1 WADA-Code Bewe... |
| `dosb-behoerden-gericht-und-registerweg` | Dosb: Behörden-, Gerichts- oder Registerweg: Dosb: Behörden-, Gerichts- oder Registerweg. |
| `e-sport-anerkennung` | e Sport Anerkennung: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `einstieg-routing` | Einstieg, Triage und Routing für Fachanwalt Sportrecht: ordnet Rolle (Sportler, Verein/Verband, Disziplinarausschuss), markiert Frist (Berufung CAS 21 Tage), wählt Norm (Verbandsrecht (DFB, DOSB), CAS-Code, WADA-Code) und Zuständigkeit (... |
| `einstieg-schnelltriage-fallrouting` | Einstieg, Schnelltriage und Fallrouting im Fachanwalt Sportrecht-Plugin: Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Pl... |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Sport- und Sponsoringrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen: Strukturierter Erstgespra... |
| `erstpruefung-und-mandatsziel` | Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel. |
| `esports-vereinsrecht-dosb-anerkennung` | eSports-Organisator oder Verein fragt ob DOSB-Anerkennung möglich und wie steuerliche Gemeinnuetzigkeit erreichbar ist: § 52 AO Gemeinnue... |
| `eu-sportrecht-art-101-aeuv-eugh-c-333-21` | EU Sportrecht Art 101 Aeuv EuGH C 333 21: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `fachanwalt-sportrecht-cas-dis-sport-verbands-schiedsverfahren` | Sportler Verein oder Verband wird in Schiedsverfahren vor CAS DIS oder Verbands-Schiedsgericht involviert. WADA-Code Anti-Doping FIFA Players Status Committee. Normen CAS Code Art. R27 ff. DIS-Sportschiedsgerichtsordnung FIFA RSTP Art. 1... |
| `fachanwalt-sportrecht-doping-cas-berufung` | Athlet muss Doping-Sperre vor CAS anfechten oder WADA/NADA legt Berufung gegen Freispruch ein. WADA-Code strict liability Therapeutic Use Exemption Sanktion 2-4 Jahre. Normen WADA-Code Art. 2 10 13 CAS Code AntiDopG § 4. Prüfraster Stric... |
| `fachanwalt-sportrecht-doping-verfahren` | Athlet steht vor NADA-Disziplinarverfahren wegen positivem Dopingtest und braucht Verteidigung. NADA-Code WADA-Code strict liability Art. 2 Abs. 1 WADA-Code Beweislastumkehr no fault Art. 10 Abs. 5. Normen AntiDopG § 4 CAS Art. 13. Prüfr... |
| `fachanwalt-sportrecht-esports-vereinsrecht-dosb-anerkennung` | eSports-Organisator oder Verein fragt ob DOSB-Anerkennung möglich und wie steuerliche Gemeinnuetzigkeit erreichbar ist. § 52 AO Gemeinnuetzigkeit § 21 BGB Vereinsrecht. Normen §§ 21 ff. BGB § 52 AO DOSB-Satzung. Prüfraster DOSB-Aufnahme-... |
| `fachanwalt-sportrecht-orientierung` | Anwalt will Fachanwaltschaft Sportrecht erwerben oder Mandat im Sportrecht bearbeiten und braucht Orientierung. FAO-Voraussetzungen typische Mandate Fristen. Normen BGB §§ 21 ff. Vereinsrecht CAS Code WADA-Code DFB-Statuten. Prüfraster N... |
| `fachanwalt-sportrecht-schnellstart` | 'Kompakter Arbeitsmodus für Fachanwalt Sportrecht. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.' |
| `fachanwalt-sportrecht-spielervertrag` | Workflow-Skill zu fachanwalt sportrecht spielervertrag. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `fachanwalt-sportrecht-stadion-hausverbot` | Fan erhaelt bundesweites Stadion-Hausverbot und will dieses anfechten. AGB-Prüfung Vereinsrecht Fanrechte Datenschutz. Normen §§ 305 ff. BGB AGB-Kontrolle BGH Bundesliga-Hausverbot § 25 BGB Vereinsrecht DSGVO Polizei-Datei Gewalttaeter S... |
| `fachanwalt-sportrecht-transferklausel` | Profi-Sportler will Verein wechseln und braucht Prüfung von Transfervertrag Ausstiegsklausel Transferperiode. FIFA/UEFA-Statuten Wechselgebühr. Normen FIFA RSTP Art. 17 18 UEFA-Transferregeln DFB-Lizenzordnung. Prüfraster Ausstiegsklause... |
| `fachanwalt-sportrecht-vereinsstrafrecht` | Workflow-Skill zu fachanwalt sportrecht vereinsstrafrecht. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `fifa-dokumentenmatrix-und-lueckenliste` | Fifa: Dokumentenmatrix, Lückenliste und Nachforderung: Fifa: Dokumentenmatrix, Lückenliste und Nachforderung. |
| `gesellschaftsrecht-beweislast-und-darlegungslast` | Gesellschaftsrecht: Beweislast, Darlegungslast und Substantiierung: Gesellschaftsrecht: Beweislast, Darlegungslast und Substantiierung. |
| `mandat-abschlussprodukt-und-uebergabe` | Mandat: Abschlussprodukt und Übergabe: Mandat: Abschlussprodukt und Übergabe. |
| `mandat-triage-sportrecht` | Sportrechtliches Mandat eintrifft und muss strukturiert erfasst werden: Mandantenrolle Sachgebiet Sofort-Fristen: Verbandsfrist gegen Sanktion... |
| `nada-mehrparteien-konflikt-und-interessen` | Nada: Mehrparteienkonflikt und Interessenmatrix: Nada: Mehrparteienkonflikt und Interessenmatrix. |
| `orientierung-fachanwaltschaft-mandat` | Anwalt will Fachanwaltschaft Sportrecht erwerben oder Mandat im Sportrecht bearbeiten und braucht Orientierung: FAO-Voraussetzungen typische Mand... |
| `output-waehlen` | Output-Wahl für Fachanwalt Sportrecht: stimmt Adressat (Sportler, Verein/Verband, Disziplinarausschuss), Frist (Berufung CAS 21 Tage) und Form auf den Zweck ab — typische Outputs: Verbandsbeschwerde, CAS-Berufung, Vertretung Anhörung. |
| `persoenlichkeitsrechte-formular-portal-und-einreichung` | Persoenlichkeitsrechte: Formular, Portal und Einreichungslogik: Persoenlichkeitsrechte: Formular, Portal und Einreichungslogik. |
| `quellen-livecheck` | Quellen-Live-Check für Fachanwalt Sportrecht: prüft Normen (Verbandsrecht (DFB, DOSB), CAS-Code, WADA-Code) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Verbandsschiedsgerichte und Quellenhygiene nach reference... |
| `schiedsklausel-csport` | Schiedsklausel Csport: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `schiedsverfahren-schriftsatz-brief-und-memo-bausteine` | Schiedsverfahren: Schriftsatz-, Brief- und Memo-Bausteine: Schiedsverfahren: Schriftsatz-, Brief- und Memo-Bausteine. |
| `schnittstelle-mandantenentscheidung` | Schnittstelle: Mandantenkommunikation und Entscheidungsvorlage: Schnittstelle: Mandantenkommunikation und Entscheidungsvorlage. |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Klage ordentliches Gericht/Sportgericht, CAS-/DIS-Schiedsantrag, Antidoping: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau: Substantiiert... |
| `spezial-doping-livequellen-und-rechtsprechungscheck` | Doping: Livequellen- und Rechtsprechungscheck. |
| `spezial-veranstalterhaftung-red-team-und-qualitaetskontrolle` | Veranstalterhaftung: Red-Team und Qualitätskontrolle. |
| `spielervertraege-verhandlung-vergleich-und-eskalation` | Spielervertraege: Verhandlung, Vergleich und Eskalation: Spielervertraege: Verhandlung, Vergleich und Eskalation. |
| `spielervertrag` | Fachanwalt Sportrecht Spielervertrag: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Sportrecht Spielervertrag: ordnet Normen, Nutzerangaben, Fristen, Belege und ver... |
| `sponsoring-internationaler-bezug-und-schnittstellen` | Sponsoring: Internationaler Bezug und Schnittstellen: Sponsoring: Internationaler Bezug und Schnittstellen. |
| `sport-anti-doping` | Sport Anti Doping: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `sportr-anti-doping-praxis` | Anti-Doping in der Praxis: NADA-Code, WADA-Code, Strict Liability, Verfahrensgang vor Schiedsgericht der NADA und CAS in Lausanne: Anti-Doping in der Praxis: NADA-Code, WADA-Code, Strict Liability, Verfahrensgang vor Schiedsgericht der N... |
| `sportr-arbeitsrecht-im-sport-leitfaden` | Leitfaden Arbeitsrecht im Sport: Spielervertrag als befristeter Arbeitsvertrag, Befristungsrecht BAG, Transferregeln FIFA / DFB, Trainerverträge: Leitfaden Arbeitsrecht im Sport: Spielervertrag als befristeter Arbeitsvertrag, Befristungs... |
| `sportr-athletenvertrag-bauleiter` | Bauleiter Athletenvertrag: Verguetung, Image- und Vermarktungsrechte, Trainingspflichten, Wettkampfteilnahme, Dopingklausel, Beendigung: Bauleiter Athletenvertrag: Verguetung, Image- und Vermarktungsrechte, Trainingspflichten, Wettkampft... |
| `sportr-doping-disziplinarverfahren-spezial` | Spezialfall Doping-Disziplinarverfahren CAS / NADA: Beweisregeln, Strict Liability, Whereabouts, Verkuerzungsruende, Therapeutic Use Exemption: Spezialfall Doping-Disziplinarverfahren CAS / NADA: Beweisregeln, Strict Liability, Whereabou... |
| `sportr-einfuehrung-rechtsfelder` | Sportrecht einfuehrend: Sportverbandsrecht, Verbandsstrafrecht, Anti-Doping, Sportarbeitsvertraege (Profisport), Sponsoring, Vermarktung, Persoenlichkeitsrecht Athlet, Fan-Rechte: Sportrecht einfuehrend: Sportverbandsrecht, Verbandsstraf... |
| `sportr-sonderfall-edge-case` | Sportr: Sonderfall und Edge-Case-Prüfung: Sportr: Sonderfall und Edge-Case-Prüfung. |
| `sportr-spielerberater-rechtsverhaeltnis-spezial` | Spezialfall Spielerberater-Rechtsverhaeltnis: FIFA-Reglement RWFC 2023, DFB-Reglement, Klauseln Exclusive Mandate, Commission Cap, Anti-Tampering: Spezialfall Spielerberater-Rechtsverhaeltnis: FIFA-Reglement RWFC 2023, DFB-Reglement, Kla... |
| `sportr-stadionverbot-fanrechte-spezial` | Spezialfall Stadionverbot und Fanrechte: bundesweite und oertliche Stadionverbote, BGH-Rechtsprechung zu Anhörung, gleichbehandlungsrechtliche Aspekte: Spezialfall Stadionverbot und Fanrechte: bundesweite und oertliche Stadionverbote, BG... |
| `sportr-stadionverbot-und-fan-rechte-spezial` | Spezialfall Stadionverbot und Fan-Rechte: Hausrecht des Vereins, bundesweites Stadionverbot, Anhörungspflicht, Klage Anfechtung, Vergleichsverhandlung: Spezialfall Stadionverbot und Fan-Rechte: Hausrecht des Vereins, bundesweites Stadion... |
| `sportrecht-tatbestand-beweis-und-belege` | Sportrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage: Sportrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage. |
| `sportstaetten-immission-paragraf-22-bimschg-bverwg-7-c-21-18` | Sportstaetten Immission Paragraf 22 Bimschg BVerwG 7 C 21 18: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `stadion-hausverbot` | Fan erhaelt bundesweites Stadion-Hausverbot und will dieses anfechten: AGB-Prüfung Vereinsrecht Fanrechte Datenschutz. Normen §§ 305 ff. BGB AGB-Kontrolle BGH Bundesliga-Hausverbot § 25... |
| `transfer-fussball-fifa-rstp-cas-2018-a-22` | Transfer Fussball Fifa Rstp Cas 2018 A 22: fachanwaltlicher Spezialskill mit Normenanker, Fristen-/Zustaendigkeitscheck, Beweisfragen, Rechtsprechungshygiene und direkt nutzbarem Arbeitsprodukt. |
| `transferklausel` | Profi-Sportler will Verein wechseln und braucht Prüfung von Transfervertrag Ausstiegsklausel Transferperiode: FIFA/UEFA-Statuten Wechselgebühr. Nor... |
| `uefa-risikoampel-und-gegenargumente` | Uefa: Risikoampel, Gegenargumente und Verteidigungslinien: Uefa: Risikoampel, Gegenargumente und Verteidigungslinien. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Fachanwalt Sportrecht: trennt fehlende Tatsachen von fehlenden Belegen (Spielerlizenz, Verbandssatzung, Transferregister), nennt pro Lücke Beweisthema, Beschaffungsweg (Verbandsschiedsgerichte), Frist un... |
| `veranstalterhaftung-fehlerkatalog` | Veranstalterhaftung Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `verbandsrecht-fristen-form-und-zustaendigkeit` | Verbandsrecht: Fristen, Form, Zuständigkeit und Rechtsweg: Verbandsrecht: Fristen, Form, Zuständigkeit und Rechtsweg. |
| `verbandsstrafe-anfechten` | Verbandsstrafe Anfechten: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Verbandsstrafe Anfechten: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung... |
| `vereinsstrafrecht` | Fachanwalt Sportrecht Vereinsstrafrecht: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fachanwalt Sportrecht Vereinsstrafrecht: ordnet Normen, Nutzerangaben, Fristen, Belege u... |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für Sport- und Sponsoringrecht: ZOPA, BATNA, Verhandlungsfenster, Druckmittel, Settlement-Skript, Vergleichsentwurf und prozessuale Absicherung (Protokoll-/Anwaltsvergleich): Vergleichsverhandlungs-Strate... |
| `wada-zahlen-schwellen-und-berechnung` | Wada: Zahlen, Schwellenwerte und Berechnung: Wada: Zahlen, Schwellenwerte und Berechnung. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation: Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `zuschauerhaftung-paragraf-9a-veranstg` | Zuschauerhaftung § 9a Veranstg: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |
| `zwangsabstieg-vereinsrecht-paragraf-25-bgb` | Zwangsabstieg Vereinsrecht § 25 BGB: fachanwaltlicher Spezial-Skill mit Normenanker, Tatsachenmatrix, Beweislast, Fristen, Gegenargumenten und belastbarem Arbeitsprodukt; ohne ungeprüfte Aktenzeichen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
