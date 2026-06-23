# Handelsrecht HGB
Wenn du das hier oeffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen pruefen und ein verwertbares Arbeitsprodukt erhalten.

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Dies ist eines von 229 Plugins aus dem Repo [`claude-fuer-deutsches-recht`](https://github.com/Klotzkette/claude-fuer-deutsches-recht). Das Repo ist von vornherein als **Plugin-Sammlung für Claude Code und Claude Cowork** gebaut: jedes Plugin enthält eine Familie zusammenhängender Skills (`SKILL.md`-Dateien), passende Hilfsdateien, Prüfrastern, Vorlagen und in vielen Fällen eine eigene Testakte. Der vorgesehene Hauptweg ist also: **Plugin in Claude Code / Cowork installieren**, am besten über den Marketplace, alternativ als einzelnes Plugin-ZIP. Dann läuft das Plugin in seiner natürlichen Umgebung mit allen Skills, Werkzeugen und Testdaten.

Damit das Plugin aber auch dann brauchbar bleibt, wenn jemand Claude Code / Cowork gerade nicht nutzen kann oder will (anderer Chatbot, Browser-Nutzung, schneller Test, Schulung, kein Setup zur Hand), gibt es zusätzlich zwei reine **Markdown-Prompts**, die ohne Plugin-Setup funktionieren: einen ausführlichen **Werkstatt-Prompt** und einen kompakten **Schnellstart-Prompt** (höchstens 7500 Zeichen). Beide sind eine einzelne `.md`-Datei, die man in jeden geeigneten Chatbot ziehen, einfügen oder per Copy-and-Paste verwenden kann.

## Downloads

In dieser Reihenfolge gedacht: zuerst der vorgesehene Plugin-Weg für Claude Code / Cowork, danach die Markdown-Alternativen für alles andere, am Schluss die zugehörigen Testakten.

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg, für Claude Code / Cowork) | ZIP | [`handelsrecht-hgb.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/handelsrecht-hgb.zip) |
| Großer Prompt (Werkstatt, Alternative ohne Plugin-Setup) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/handelsrecht-hgb/handelsrecht-hgb-werkstatt.md" download><code>handelsrecht-hgb-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart, höchstens 7500 Zeichen, Spar-Alternative) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/handelsrecht-hgb/handelsrecht-hgb-schnellstart.md" download><code>handelsrecht-hgb-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`testakte-handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona.zip) (Handelsrecht HGB — Elbwerft Solar: eGbR, OHG-Statuswechsel, KG und Handelskauf); [`testakte-handelsvertreterrecht-provisionsausgleich-nordstern-medtech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsvertreterrecht-provisionsausgleich-nordstern-medtech.zip) (Akte Nordstern MedTech Vertrieb - Provision, Buchauszug und Ausgleich) |

> Marketplace-Hinweis: Wer mehrere Plugins gleichzeitig will, fügt nicht jedes Plugin einzeln hinzu, sondern den ganzen Marketplace über `marketplace.json` aus dem [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest). Dann sind alle 229 Plugins in Claude Code / Cowork verfügbar und können einzeln aktiviert werden.
<!-- END direkt-loslegen (autogen) -->

Reines HGB-Plugin für Handelsrecht: Kaufmann, Handelsregister, Firma, Prokura, Handlungsvollmacht, Handelsgeschäfte, Handelskauf, Handelsvertreter, Makler, Kommission, Fracht, Spedition, Lager, Handelsbücher sowie OHG/KG einschließlich MoPeG-Statuswechsel von GbR zu OHG.

Das Plugin ist bewusst **kein** Gesellschaftsrechts-Fachanwaltsplugin, sondern ein schneller HGB-Arbeitsbegleiter: Es erklärt Einsteigern den Handelsrechtsmechanismus und liefert Profis sofort Register-, Vertrags-, Prozess- und Beweisoutputs.

## Kaltstart

1. Ist jemand Kaufmann oder Handelsgesellschaft?
2. Geht es um Register/Firma/Vertretung oder um ein Handelsgeschäft?
3. Gibt es eine OHG/KG, eine eGbR mit Statuswechsel oder eine faktisch kaufmännische Tätigkeit?
4. Welche handelsrechtliche Sonderregel verschiebt das BGB-Ergebnis?
5. Was soll herauskommen: Registeranmeldung, Gutachten, Klagebaustein, Vertragsklausel, Rügebrief, Protokoll?

## Quellenanker

- HGB amtlich/frei: https://www.gesetze-im-internet.de/hgb/
- BGB für Personengesellschaftsgrundlagen: https://www.gesetze-im-internet.de/bgb/
- Register-/Verfahrensschnittstellen: FamFG, HRV, BeurkG, GmbHG, AktG je nach Fall live prüfen.

## Demonstrationsakte

`handelsrecht-hgb-kommanditgesellschaft-egbr-statuswechsel-altona` zeigt eine wachsende Solartechnik-GbR, die durch kaufmännischen Geschäftsbetrieb und Register-/Finanzierungsdruck in OHG/KG-Strukturen rutscht. Dazu kommen Prokura, Handelskauf, § 377 HGB, Firmenfortführung und ein Streit um Kommanditistenhaftung.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 57 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anfanger-erklaerung-handelsbrauch` | Erklärt Handelsrecht laienverständlich: Warum Kaufmannsrecht strenger, schneller und registerorientierter ist im Handelsrecht Hgb. |
| `firma-paragraphen-firmenfortfuehrung` | Prüft Firmenbildung, Kennzeichnungskraft, Irreführung, Rechtsformzusatz und Geschäftsbriefe im Handelsrecht Hgb. |
| `firmenfortfuehrung-paragraphen-21-25-hgb` | Prüft Firmenfortführung, Unternehmenserwerb, Haftung und Haftungsausschluss im Handelsrecht Hgb. |
| `formkaufmann-paragraph-gmbh-co` | Prüft Kaufmannseigenschaft kraft Rechtsform bei Handelsgesellschaften und juristischen Personen im Handelsrecht Hgb. |
| `frachtvertrag-paragraphen-speditionsvertrag` | Prüft Frachtvertrag, Frachtbrief, Haftung, Verlust/Beschädigung, Lieferfrist und Haftungsgrenzen im Handelsrecht Hgb. |
| `gmbh-und-co-kg-hgb` | Prüft HGB-Struktur der GmbH & Co. KG: Firma, Vertretung, Haftung, Register und Publizität im Handelsrecht Hgb. |
| `handelsbuecher-paragraph-handelsgeschaefte` | Prüft Buchführungspflicht, Handelsbriefe, Belegfunktion und Prozessbeweis im Handelsrecht Hgb. |
| `handelsgeschaefte-paragraphen-343-344` | Prüft beiderseitige/einseitige Handelsgeschäfte und Vermutung geschäftlicher Zugehörigkeit im Handelsrecht Hgb. |
| `handelskauf-fristenampel-hgb` | Macht Fristenampel für Rüge, Lieferung, Fixgeschäft, Annahmeverzug, Verjährung und Beweise im Handelsrecht Hgb. |
| `handelskauf-paragraphen-handelsmakler` | Prüft Fixhandelskauf, Annahmeverzug, Spezifikationskauf, Untersuchungs- und Rügeobliegenheit im Handelsrecht Hgb. |
| `handelsmakler-paragraphen-93-104-hgb` | Prüft Handelsmakler, Schlussnote, Tagebuch, Provision und Haftung im Handelsrecht Hgb. |
| `handelsrecht-hgb-schnellstart` | 'Kompakter Arbeitsmodus für Handelsrecht HGB. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.' |
| `handelsregister-paragraphen-8-16-hgb` | Prüft Handelsregister, Einsicht, Bekanntmachung, negative/positive Publizität und Eintragungswirkung im Handelsrecht Hgb. |
| `handelsvertreter-paragraph-provision` | Prüft Handelsvertreterstatus, Abgrenzung Angestellter/Makler/Vertragshändler im Handelsrecht Hgb. |
| `handelsvertreter-provision` | Prüft Provisionsanspruch, Entstehen, Fälligkeit, Stornoreserve und Abrechnung im Handelsrecht Hgb. |
| `handelsvertreterausgleich-paragraph` | Prüft Ausgleichsanspruch, Unternehmervorteile, Billigkeit, Höchstgrenze und Ausschlüsse im Handelsrecht Hgb. |
| `handlungsgehilfen-und-wettbewerbsverbot` | Prüft Handlungsgehilfe, Wettbewerbsverbot, Karenz und arbeitsrechtliche Schnittstellen im Handelsrecht Hgb. |
| `handlungsvollmacht-paragraph-geschaeftsbriefe` | Prüft Artvollmacht, Gattungsvollmacht, Spezialvollmacht und Grenzen im Handelsrecht Hgb. |
| `hgb-compliance-geschaeftsbriefe-impressum` | Prüft Pflichtangaben auf Geschäftsbriefen, E-Mails, Rechnungen und Webseiten im Handelsrecht Hgb. |
| `hgb-red-team` | Findet Gegenargumente in Handelsrechtsfällen: Nichtkaufmann, Vertretungsmangel, verspätete Rüge, Registerpublizität, Firmenirreführung. |
| `international-cisg-handelsregister` | Prüft HGB bei internationalem Handelskauf, CISG-Abgrenzung, Rom I und Gerichtsstand im Handelsrecht Hgb. |
| `jahresabschluss-hgb-grundlagen` | Prüft Aufstellung, Unterzeichnung, Gliederung, Offenlegung und Größenklassen in Grundzügen im Handelsrecht Hgb. |
| `kaltstart-triage` | Einstieg, Schnelltriage und Skill-Routing für HGB-Fälle: Kaufmann, Register, Firma, Vertretung, Handelsgeschäft, OHG/KG, Handelskauf und Handelsbücher. |
| `kannkaufmann-paragraphen-kaufmaennisches` | Prüft freiwillige Eintragung kleiner Gewerbe sowie Land-/Forstwirtschaft im Handelsrecht Hgb. |
| `kaufmaennisches-bestaetigungsschreiben` | Prüft Voraussetzungen und Wirkung des kaufmännischen Bestätigungsschreibens im Handelsrecht Hgb. |
| `kaufmann-paragraph-kg-begriff` | Prüft Istkaufmann und Handelsgewerbe nach Art und Umfang im Handelsrecht Hgb. |
| `kg-begriff-kommanditist` | Prüft KG, Komplementär, Kommanditist, Hafteinlage, Pflichteinlage und Haftsumme im Handelsrecht Hgb. |
| `kg-haftung-ohg-vertretung` | Prüft Außenhaftung, Einlage, Rückzahlung, Registerpublizität und Wiederaufleben im Handelsrecht Hgb. |
| `kommission-paragraphen-ladenvollmacht` | Prüft Kommissionsgeschäft, Selbsteintritt, Ausführung, Provision, Pfandrecht im Handelsrecht Hgb. |
| `ladenvollmacht-paragraph-56-hgb` | Prüft Laden-/Warenlagerangestellte und Verkehrsschutz im Handelsrecht Hgb. |
| `lagergeschaeft-paragraphen-maengelruege` | Prüft Lagerhalter, Lagerschein, Haftung, Herausgabe und Pfandrecht im Handelsrecht Hgb. |
| `livequellen-hgb` | Zwingt HGB-Normen und Rechtsprechung vor Ausgabe zu aktueller freier Quellenprüfung. |
| `maengelruege-paragraph-377-hgb` | Prüft beim beiderseitigen Handelskauf die Untersuchungs- und Rügeobliegenheit nach § 377 HGB, Wareneingangskontrolle, Beweislast für Mangel bei Gefahrübergang, offene und verdeckte Mängel, Rechtsverlust und die klare Abgrenzung zur nur i... |
| `ohg-anmeldung-begriff` | Prüft Anmeldung, Statuswechsel aus Gesellschaftsregister, Registerlogik und Fehlerfolgen im Handelsrecht Hgb. |
| `ohg-begriff-und-entstehung-paragraph-105` | Prüft OHG nach MoPeG: Betrieb eines Handelsgewerbes unter gemeinschaftlicher Firma und BGB-Verweis im Handelsrecht Hgb. |
| `ohg-gesellschafterwechsel-prokura` | Prüft Eintritt, Ausscheiden, Nachhaftung, Abfindung und Registereintragung im Handelsrecht Hgb. |
| `ohg-vertretung-und-haftung` | Prüft Vertretung, Geschäftsführung, persönliche Haftung und Einwendungen der Gesellschafter im Handelsrecht Hgb. |
| `prokura-paragraphen-48-53-hgb` | Prüft Erteilung, Umfang, Grenzen, Gesamtprokura, Filialprokura und Registereintragung im Handelsrecht Hgb. |
| `prozessuale-beweisfragen-rechtsabteilung` | Prüft Handelsbücher, Bestätigungsschreiben, Registerauszug, Zeugen aus Organisation und Urkundenbeweis im Handelsrecht Hgb. |
| `rechtsabteilung-handelskauf-maengelruege-nach-377-hgb` | Rechtsabteilungs-Fachmodul für B2B-Handelskauf und § 377 HGB: Wareneingangskontrolle, Rügefristen, Serienfehler, Beweislast für Mangel bei Gefahrübergang und Abgrenzung zur nur im B2C geltenden § 477-BGB-Vermutung. |
| `rechtsabteilung-kaufmaennisches` | Rechtsabteilungs-Fachmodul für Kaufmännisches Bestätigungsschreiben im Konzernalltag: Schweigen, E-Mail-Thread und Bestellplattform werden auf Bindungswirkung geprüft. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungs... |
| `rechtsabteilung-kommissionsgeschaeft-und-plattformhaendler` | Rechtsabteilungs-Fachmodul für Kommissionsgeschäft und Plattformhändler: Kommission, Eigenhandel und Marktplatzrolle werden rechtlich sortiert. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Handelsrecht Hgb. |
| `rechtsabteilung-lagerhalter-unternehmenskauf` | Rechtsabteilungs-Fachmodul für Lagerhalter- und Speditionshaftung: Schaden, Haftungsgrenzen und Regressketten werden schnell berechnet. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Handelsrecht Hgb. |
| `rechtsabteilung-prokura-registerbeanstandung` | Rechtsabteilungs-Fachmodul für Prokura und Grundstücksgeschäft: Registerlage, Spezialvollmacht und Gutglaubensschutz werden geprüft. Mit Normen, Rechtsprechungsanker, Belegmatrix und schneller Handlungsoption im Handelsrecht Hgb. |
| `register-gutachten-klage` | Erstellt Registeranmeldungsskizze, Gutachten, Klagebaustein, Rügebrief, Protokoll oder Mandantenbrief. |
| `registerakte-handelsstreit` | Sortiert Registerauszüge, Gesellschafterlisten, Vollmachten, Notarentwürfe und Beanstandungen im Handelsrecht Hgb. |
| `registerbeanstandung-und-beschwerde` | Prüft Zwischenverfügung, Beanstandung, Nachbesserung und Beschwerde gegen Registergericht im Handelsrecht Hgb. |
| `registerpublizitaet-paragraph-scheinkaufmann` | Prüft negative und positive Publizität des Handelsregisters im Handelsrecht Hgb. |
| `sanierung-krise-jahresabschluss-grundlagen` | Prüft handelsrechtliche Pflichten in Unternehmenskrise: Buchführung, Register, Haftung, Gesellschafterwechsel, Fortführung im Handelsrecht Hgb. |
| `scheinkaufmann-und-rechtsschein` | Prüft Rechtsschein kaufmännischen Auftretens und Vertrauensschutz im Handelsrecht Hgb. |
| `speditionsvertrag-paragraphen-453-466-hgb` | Prüft Spediteur, Besorgung der Versendung, Selbsteintritt, Sammelladung, Haftung im Handelsrecht Hgb. |
| `stille-gesellschaft-zweigniederlassung` | Prüft stille Beteiligung, Gewinn/Verlust, Auskunft, Insolvenz und Abgrenzung partiarisches Darlehen im Handelsrecht Hgb. |
| `unternehmenskauf-hgb-haftung` | Prüft Firmenfortführung, Handelsgeschäft, Prokura, Vertragsübernahme und Haftungsrisiken im Asset Deal im Handelsrecht Hgb. |
| `workflow-handelsbrauch-beweis` | Prüft Handelsbrauch, Verkehrssitte, kaufmännisches Bestätigungsschreiben und Beweisfragen im Handelsrecht Hgb. |
| `workflow-hgb-erstpruefung` | Prüft in fünf Schritten, ob ein HGB-Fall vorliegt und welche Sonderregeln das BGB überlagern im Handelsrecht Hgb. |
| `workflow-verhandlung-handelsstreit` | Macht Verhandlungsplan bei Liefer-, Register-, Handelsvertreter- oder Gesellschafterstreit im Handelsrecht Hgb. |
| `zweigniederlassung-und-niederlassung` | Prüft Haupt-/Zweigniederlassung, Firma, Register, Geschäftsbriefe und Vertretung im Handelsrecht Hgb. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
