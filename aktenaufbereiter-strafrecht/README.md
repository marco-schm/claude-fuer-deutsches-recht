# Aktenaufbereiter Strafrecht
Wenn du das hier oeffnest, willst du einen Tatvorwurf entlang von Beweiswuerdigung und Strafzumessung durchdringen und einen verwertbaren Schriftsatz bauen.

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Dies ist eines von 229 Plugins aus dem Repo [`claude-fuer-deutsches-recht`](https://github.com/Klotzkette/claude-fuer-deutsches-recht). Das Repo ist von vornherein als **Plugin-Sammlung für Claude Code und Claude Cowork** gebaut: jedes Plugin enthält eine Familie zusammenhängender Skills (`SKILL.md`-Dateien), passende Hilfsdateien, Prüfrastern, Vorlagen und in vielen Fällen eine eigene Testakte. Der vorgesehene Hauptweg ist also: **Plugin in Claude Code / Cowork installieren**, am besten über den Marketplace, alternativ als einzelnes Plugin-ZIP. Dann läuft das Plugin in seiner natürlichen Umgebung mit allen Skills, Werkzeugen und Testdaten.

Damit das Plugin aber auch dann brauchbar bleibt, wenn jemand Claude Code / Cowork gerade nicht nutzen kann oder will (anderer Chatbot, Browser-Nutzung, schneller Test, Schulung, kein Setup zur Hand), gibt es zusätzlich zwei reine **Markdown-Prompts**, die ohne Plugin-Setup funktionieren: einen ausführlichen **Werkstatt-Prompt** und einen kompakten **Schnellstart-Prompt** (höchstens 7500 Zeichen). Beide sind eine einzelne `.md`-Datei, die man in jeden geeigneten Chatbot ziehen, einfügen oder per Copy-and-Paste verwenden kann.

## Downloads

In dieser Reihenfolge gedacht: zuerst der vorgesehene Plugin-Weg für Claude Code / Cowork, danach die Markdown-Alternativen für alles andere, am Schluss die zugehörigen Testakten.

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg, für Claude Code / Cowork) | ZIP | [`aktenaufbereiter-strafrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aktenaufbereiter-strafrecht.zip) |
| Großer Prompt (Werkstatt, Alternative ohne Plugin-Setup) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/aktenaufbereiter-strafrecht/aktenaufbereiter-strafrecht-werkstatt.md" download><code>aktenaufbereiter-strafrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart, höchstens 7500 Zeichen, Spar-Alternative) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/aktenaufbereiter-strafrecht/aktenaufbereiter-strafrecht-schnellstart.md" download><code>aktenaufbereiter-strafrecht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`testakte-sammelakte-bandentaeter-eg-juwel-stuttgart-koffer-raub.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sammelakte-bandentaeter-eg-juwel-stuttgart-koffer-raub.zip) (EG Juwel Stuttgart — Sammelverfahren bandenmaessiger schwerer Raub, Königstrasse) |

> Marketplace-Hinweis: Wer mehrere Plugins gleichzeitig will, fügt nicht jedes Plugin einzeln hinzu, sondern den ganzen Marketplace über `marketplace.json` aus dem [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest). Dann sind alle 229 Plugins in Claude Code / Cowork verfügbar und können einzeln aktiviert werden.
<!-- END direkt-loslegen (autogen) -->

Aktenaufbereiter für die Strafverteidigung. Bringt große Strafakten in den Griff durch sechs Excel-fähige Übersichten — Aktenvorblatt; Personenverzeichnis; Tatkomplexe; Beziehungen; Chronologie; Fristen. Fortlaufend ergänzbar. Erkennt Lücken und Widersprüche. Kein Ersatz für Aktenlektüre.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `aktenaufbereiter-strafrecht` | Strukturierte Aufbereitung strafrechtlicher Akten für die Verteidigung. Erzeugt sechs Übersichten — Aktenvorblatt mit Blattangaben; Personenverzeichnis mit Rolle und Erstnennung; Tatkomplex- und Vorwurfsverzeichnis … |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 60 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aktenaufbereiter-erstpruefung-und-mandatsziel` | Aktenaufbereiter: Erstprüfung, Rollenklärung und Mandatsziel. |
| `aktenaufbereiter-strafrecht` | Strafverteidiger erhaelt Strafakte nach § 147 StPO Akteneinsicht und will diese strukturiert aufbereiten. Wirtschaftsstrafverfahren BtM-Verfahren Vermögensdelikte komplexe Strafverfahren. Sechs Übersichten: Aktenvorblatt Personenverzeich... |
| `aktenaufbereiter-strafrecht-schnellstart` | 'Kompakter Arbeitsmodus für Aktenaufbereiter Strafrecht. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.' |
| `akteneinsicht-uebersicht` | Akteneinsicht systematisch auswerten: Aktenbestandteile (Haupt-, Sonder-, Beweismittelakte), Bandzaehlung, Aktenblattzahl je Band, fehlende Aktenstuecke, Verschluss-Sachen, Tonbaender/Datentraeger, polizeiliche Spurenakten. Fuehrt Pruef-... |
| `akteneinsicht-uebersicht-aktenvorblatt` | Akteneinsicht systematisch auswerten: Aktenbestandteile (Haupt-, Sonder-, Beweismittelakte), Bandzaehlung, Aktenblattzahl je Band, fehlende Aktenstuecke, Verschluss-Sachen, Tonbaender/Datentraeger, polizeiliche Spurenakten. Fuehrt Prüf-C... |
| `aktenlektuere-fristennotiz-und-naechster-schritt` | Aktenlektuere: Fristennotiz und nächster Schritt. |
| `aktenvorblatt-erstellen` | Erstes Aktenvorblatt für eine Strafakte erstellen: Mandant, Vorwurf nach Anklageschrift oder Strafanzeige, Tatzeitraum, zuständiges Gericht/Staatsanwaltschaft, Aktenzeichen, Verteidiger, U-Haft-Status, naechste Termine, Hauptrisiken. Aus... |
| `aktenvorblatt-schriftsatz-brief-und-memo-bausteine` | Aktenvorblatt: Schriftsatz-, Brief- und Memo-Bausteine. |
| `anklageschrift-zerlegen` | Anklageschrift in arbeitsfaehige Bausteine zerlegen: Tatvorwurf je Anklagepunkt, vorgeworfene Norm, wesentliche Tatsachen, Beweismittel je Punkt, Liste der Beweismittel, Verteidigungsansatzpunkte je Punkt. Output Tabelle und kommentierte... |
| `anschluss-routing` | Anschluss-Routing für Strafrechtliche Aktenaufbereitung: wählt den nächsten Spezial-Skill nach Engpass (Anklage-Erwiderungsfrist, Ermittlungsakte, Anklageschrift, Hauptverhandlungsprotokoll), dokumentiert Router-Entscheidung mit Begründung. |
| `aussageanalyse-aussagepsychologie` | Zeugenaussage mit aussagepsychologischen Realkennzeichen analysieren: logische Konsistenz, quantitative Detailfuelle, Detailverknuepfung, Selbstbelastung, ungewoehnliche Details, Nichtsteuerungsmerkmale. Hypothesentest Falschaussage. Sin... |
| `beweismittel-katalog-beweisverwertungsverbote` | Beweismittel-Katalog für die Verteidigung: Urkunden, Augenschein, Zeugen, Sachverstaendige, Beschuldigtenaussage, Spuren, Datentraeger, Telekommunikationsueberwachung, Observation. Beweisthema, Beweismittel, Fundstelle in der Akte, Bewei... |
| `beweisverwertungsverbote-pruefen` | Beweisverwertungsverbote prüfen: § 136a StPO (verbotene Vernehmungsmethoden), § 252 StPO (Aussageverweigerung Angehoeriger), § 100a/d StPO (TKUe ohne Voraussetzungen), Belehrungsfehler § 136 StPO, Zufallsfunde § 108 StPO, Kernbereich pri... |
| `beziehungen-spezial-chronologie-ergaenzbar` | Beziehungen: Zahlen, Schwellenwerte und Berechnung. |
| `beziehungsmatrix-personen-taten` | Beziehungen zwischen Personen und Tatkomplexen sichtbar machen: Wer hat wem etwas getan, wer war wann wo, wer sagt was zu welchem Tatkomplex. Matrix-Tabelle mit Tatkomplexen als Spalten und Personen als Zeilen. Markiert Beziehungstyp (Ta... |
| `chronologie-compliance-dokumentation-und-akte` | Chronologie: Compliance-Dokumentation und Aktenvermerk. |
| `chronologie-strafverfahren` | Chronologie aller Verfahrensschritte: Tatzeitpunkt, Anzeige, Vernehmungen, Durchsuchungen, Festnahme, U-Haft-Befehle, Anklage, Hauptverhandlungstermine, Urteile, Rechtsmittel. Datum, Zeit, Behörde/Gericht, Art, Beleg in der Akte (Aktenbl... |
| `dokumente-intake` | Dokumentenintake für Strafrechtliche Aktenaufbereitung: sortiert Ermittlungsakte, Anklageschrift, Hauptverhandlungsprotokoll, prüft Datum, Absender, Frist und Beweiswert (Zeugenaussagen, Tatortfotos); markiert Lücken; berücksichtigt Mand... |
| `einstieg-routing` | Einstieg, Triage und Routing für Strafrechtliche Aktenaufbereitung: ordnet Rolle (Mandant/Beschuldigter, Staatsanwaltschaft, Verletzte/Zeugen), markiert Frist (Anklage-Erwiderungsfrist), wählt Norm (§§ 147 StPO Akteneinsicht, § 200 StPO... |
| `ergaenzbar-formular-portal-und-einreichung` | Ergaenzbar: Formular, Portal und Einreichungslogik. |
| `erkennt-fehlerkatalog` | Erkennt Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `ersatz-sonderfall-excel-faehige` | Ersatz: Sonderfall und Edge-Case-Prüfung. |
| `excel-dokumentenmatrix-und-lueckenliste` | Excel: Dokumentenmatrix, Lückenliste und Nachforderung. |
| `faehige-risikoampel-und-gegenargumente` | Faehige: Risikoampel, Gegenargumente und Verteidigungslinien. |
| `fortlaufend-luecken-personenverzeichnis` | Fortlaufend: Internationaler Bezug und Schnittstellen. |
| `fristen-mehrparteien-konflikt-und-interessen` | Fristen: Mehrparteienkonflikt und Interessenmatrix. |
| `fristenliste-strafverfahren-aktenlektuere` | Fristenliste für ein Strafverfahren: Einspruch gegen Strafbefehl § 410 StPO, Berufung § 314 StPO, Revision § 341 sowie § 345 StPO, Rechtsmittel § 311 StPO, Wiedereinsetzung § 44 StPO, Untersuchungshaft-Prüfung § 117 sowie § 121 StPO. Dat... |
| `kronzeugen-regelung-opferzeugen-besondere` | Spezialfall Kronzeugenregelung § 46b StGB: Aufklaerungshilfe oder Verhinderung schwerer Straftaten, Voraussetzungen Konnex, Ausschluss von § 100a StPO Katalogtaten, Strafrahmenverschiebung. Prüfraster für Verteidigerstrategie und Verhand... |
| `luecken-mandantenkommunikation-entscheidungsvorlage` | Luecken: Mandantenkommunikation und Entscheidungsvorlage. |
| `mandant-redteam-gate` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Strafrechts-Aktenaufbereiter. |
| `opferzeugen-besondere-faelle` | Opferzeugen bei Sexualdelikten, Kindern, Schutzschriftsachen behandeln: Nebenklage § 395 StPO, Verletztenrechte §§ 406d ff. StPO, audiovisuelle Vernehmung § 58a StPO, Zeugenbeistand § 68b StPO, Ausschluss des Beschuldigten § 247 StPO. Ve... |
| `output-waehlen` | Output-Wahl für Strafrechtliche Aktenaufbereitung: stimmt Adressat (Mandant/Beschuldigter, Staatsanwaltschaft, Verletzte/Zeugen), Frist (Anklage-Erwiderungsfrist) und Form auf den Zweck ab — typische Outputs: Verteidigungsschrift, Beweis... |
| `personenverzeichnis-aufbau` | Personenverzeichnis für eine Strafakte systematisch aufbauen: Beschuldigte, Mitbeschuldigte, Zeugen, Geschaedigte, Sachverstaendige, Dolmetscher, Vertreter. Fuer jede Person Rolle, Aussagestatus, Adresse, Verteidiger, Verbindung zu Tatko... |
| `personenverzeichnis-verhandlung-vergleich-und-eskalation` | Personenverzeichnis: Verhandlung, Vergleich und Eskalation. |
| `quellen-livecheck` | Quellen-Live-Check für Strafrechtliche Aktenaufbereitung: prüft Normen (§§ 147 StPO Akteneinsicht, § 200 StPO Anklageschrift, § 397a StPO Nebenklage) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Staatsanwaltsch... |
| `revision-rechtsfehler-aktenaufbereiter` | Revisionsschrift vorbereiten: § 344 StPO Revisionsantraege, § 337 StPO Rechtsfehler. Sachruege und Verfahrensruege. Typische Verfahrensruegen: § 244 Abs. 2 StPO (Aufklaerungsruege), § 261 StPO (Beweiswuerdigung), § 265 StPO (Hinweispflic... |
| `sechs-u-haft-aussageanalyse` | Sechs: Fristen, Form, Zuständigkeit und Rechtsweg. |
| `spezial-erkennt-red-team-und-qualitaetskontrolle` | Erkennt: Red-Team und Qualitätskontrolle. |
| `spezial-tatkomplexe-livequellen-und-rechtsprechungscheck` | Tatkomplexe: Livequellen- und Rechtsprechungscheck. |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Aktenaufbereiter Strafrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan.... |
| `strafakte-quality-gate` | Quality-Gate für eine aufbereitete Strafakte: Vollstaendigkeit (alle Baende, Aktenblattzahl), Konsistenz (Personenverzeichnis gegen Anklageschrift), Suchbarkeit (OCR, Volltext), Sensibilitaet (verschluss-Sachen separat). Output Prüfliste... |
| `strafakte-uebergabe-vorbereiten` | Strafakte für Übergabe an Sozietaetskollegin, Wahlverteidiger oder Pflichtverteidiger sauber vorbereiten: Inhaltsverzeichnis, Personenverzeichnis, Tatkomplex-Liste, Chronologie, offene Fristen, naechste Termine. Output kompaktes Handover... |
| `strafbefehl-einspruchsstrategie` | Strafbefehl § 410 StPO: Einspruchsstrategie prüfen. 2-Wochen-Frist, vollstaendiger oder beschraenkter Einspruch (nur Rechtsfolgenausspruch), Folge: Hauptverhandlung. Prüfraster: Beweislage, Verschlechterungsverbot § 411 Abs. 4 StPO greif... |
| `strafrecht-strafverteidigung-uebersichten` | Strafrecht: Abschlussprodukt und Übergabe. |
| `strafverteidigung-tatbestand-beweis-und-belege` | Strafverteidigung: Tatbestandsmerkmale, Beweisfragen und Beleglage. |
| `strafzumessung-deutsches-strafrecht` | Strafzumessung § 46 StGB systematisch: Schuld, Strafmilderungs- und Strafschaerfungsgruende, § 46a StGB Taeter-Opfer-Ausgleich, § 46b StGB Aufklaerungshilfe, § 49 StGB besondere gesetzliche Milderungsgruende, Verhältnis Geld-/Freiheitsst... |
| `tatkomplexe-quellenkarte` | Tatkomplexe Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `tatkomplexe-uebersicht` | Tatkomplexe einer Strafakte gliedern: bei mehreren Taten oder Serienvorwurf jede Tat als eigenen Komplex mit Tatzeit, Tatort, Tathandlung, beteiligten Personen, Beweismitteln, Verfahrensstand. Fuer eine Anklageschrift werden die Anklagep... |
| `u-haft-fristenwacht` | U-Haft-Fristen ueberwachen: 6-Monats-Prüfung § 121 StPO durch das OLG, Haftpruefung § 117 StPO und Haftbeschwerde § 117 Abs. 1 StPO, Aussetzung gegen Auflagen § 116 StPO. Prüfraster: dringender Tatverdacht, Haftgrund, Verhältnismäßigkeit... |
| `uebersichten-behoerden-gericht-und-registerweg` | Uebersichten: Behörden-, Gerichts- oder Registerweg. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Strafrechtliche Aktenaufbereitung: trennt fehlende Tatsachen von fehlenden Belegen (Ermittlungsakte, Anklageschrift, Hauptverhandlungsprotokoll), nennt pro Lücke Beweisthema, Beschaffungsweg (Staatsanwal... |
| `vermoegensabschoepfung-dritt-einziehung` | Spezialfall Dritt-Arrest in der Vermögensabschoepfung §§ 111e ff. StPO: Arrest gegen Konten Dritter (Ehepartner, Briefkasten-Gesellschaft), Glaubhaftmachung, Verhältnismäßigkeit, einstweilige Beschwerde § 304 StPO. Prüfraster und Schrift... |
| `vermoegensabschoepfung-einziehung` | Vermögensabschoepfung §§ 73 ff. StGB prüfen und angreifen: Brutto-Prinzip, erweiterte Einziehung § 73a StGB, Wertersatzeinziehung § 73c StGB, gutglaeubige Dritte § 73e StGB. Prüfraster, Antragsentwurf gegen Einziehung, Saemtliche Sichers... |
| `verstaendigung-deal-strategie` | Verstaendigung im Strafverfahren § 257c StPO vorbereiten: Anregung an das Gericht, Ober- und Untergrenze Strafe, Gestaendnis-Inhalt, kein Geschäft ueber Schuldspruch. Prüfraster: BGH 1 StR 70/13 und BVerfG 2 BvR 2628/10. Output Verstaend... |
| `widersprueche-beweislast-strafakte-gate` | Widersprueche: Beweislast, Darlegungslast und Substantiierung. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Strafrechts-Aktenaufbereiter. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Strafrechts-Aktenaufbereiter. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Strafrechts-Aktenaufbereiter. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
