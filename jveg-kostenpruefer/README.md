# JVEG-Kostenprüfer
Wenn du das hier oeffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen pruefen und ein verwertbares Arbeitsprodukt erhalten.

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Dies ist eines von 229 Plugins aus dem Repo [`claude-fuer-deutsches-recht`](https://github.com/Klotzkette/claude-fuer-deutsches-recht). Das Repo ist von vornherein als **Plugin-Sammlung für Claude Code und Claude Cowork** gebaut: jedes Plugin enthält eine Familie zusammenhängender Skills (`SKILL.md`-Dateien), passende Hilfsdateien, Prüfrastern, Vorlagen und in vielen Fällen eine eigene Testakte. Der vorgesehene Hauptweg ist also: **Plugin in Claude Code / Cowork installieren**, am besten über den Marketplace, alternativ als einzelnes Plugin-ZIP. Dann läuft das Plugin in seiner natürlichen Umgebung mit allen Skills, Werkzeugen und Testdaten.

Damit das Plugin aber auch dann brauchbar bleibt, wenn jemand Claude Code / Cowork gerade nicht nutzen kann oder will (anderer Chatbot, Browser-Nutzung, schneller Test, Schulung, kein Setup zur Hand), gibt es zusätzlich zwei reine **Markdown-Prompts**, die ohne Plugin-Setup funktionieren: einen ausführlichen **Werkstatt-Prompt** und einen kompakten **Schnellstart-Prompt** (höchstens 7500 Zeichen). Beide sind eine einzelne `.md`-Datei, die man in jeden geeigneten Chatbot ziehen, einfügen oder per Copy-and-Paste verwenden kann.

## Downloads

In dieser Reihenfolge gedacht: zuerst der vorgesehene Plugin-Weg für Claude Code / Cowork, danach die Markdown-Alternativen für alles andere, am Schluss die zugehörigen Testakten.

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg, für Claude Code / Cowork) | ZIP | [`jveg-kostenpruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/jveg-kostenpruefer.zip) |
| Großer Prompt (Werkstatt, Alternative ohne Plugin-Setup) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/jveg-kostenpruefer/jveg-kostenpruefer-werkstatt.md" download><code>jveg-kostenpruefer-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart, höchstens 7500 Zeichen, Spar-Alternative) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/jveg-kostenpruefer/jveg-kostenpruefer-schnellstart.md" download><code>jveg-kostenpruefer-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`testakte-jveg-zeugin-berger-lg-tuebingen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-jveg-zeugin-berger-lg-tuebingen.zip) (Akte JVEG Zeugenentschädigung – Dr. Sophia Berger / LG Tübingen); [`testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip) (Akte LG Regensburg — Sieglinger gegen Burgwald Energietechnik GmbH) |

> Marketplace-Hinweis: Wer mehrere Plugins gleichzeitig will, fügt nicht jedes Plugin einzeln hinzu, sondern den ganzen Marketplace über `marketplace.json` aus dem [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest). Dann sind alle 229 Plugins in Claude Code / Cowork verfügbar und können einzeln aktiviert werden.
<!-- END direkt-loslegen (autogen) -->

Freistehendes Cowork-Plugin zur Prüfung von Kosten, Vorschüssen, Entschädigungen und Vergütungen nach dem Justizvergütungs- und -entschädigungsgesetz. Es ist auf echte Aktenarbeit zugeschnitten: Unterlagen strippen, Anspruchsart erkennen, JVEG-Positionen rechnen, Belege prüfen, Gerichtsschreiben angreifen oder bestätigen und am Ende ein belastbares Schreiben samt Rechenprotokoll erzeugen.

Die Beispielakte enthält den Fall der Zeugin Sophia Berger vor dem Landgericht Tübingen, Az. 7 O 118/23, mit Vorschussantrag, Gerichtsschreiben, anwaltlichem Schriftsatz und Word-Abschrift.

## Was das Plugin prüft

- Vorschuss nach § 3 JVEG
- Geltendmachung, Erlöschen, Wiedereinsetzung und Verjährung
- Fahrtkosten nach § 5 JVEG
- Tagegeld und Übernachtung nach § 6 JVEG
- sonstige notwendige Aufwendungen nach § 7 JVEG
- Zeugenentschädigung nach §§ 19 bis 22 JVEG
- Sachverständigen-, Dolmetscher- und Übersetzervergütung
- Kürzungs- und Wegfallrisiken nach § 8a JVEG
- Festsetzungs-, Beschwerde- und Ergänzungsschreiben

## Grundworkflow

1. Akte hochladen: Ladung, Antrag, Gerichtsschreiben, Belege, Rechnung oder Schriftsatz.
2. Rolle bestimmen: Zeuge, Sachverständiger, Dolmetscher, Übersetzer, Dritter oder ehrenamtlicher Richter.
3. Frist und Belehrung prüfen.
4. Jede Kostenposition mit Norm, Beleg und Rechenweg erfassen.
5. Kappungen und Doppelposten prüfen.
6. Beleglücken freundlich als Rückfragen ausgeben.
7. Rechenblatt, Prüfbericht und passendes Gerichtsschreiben erzeugen.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| jveg-kommandocenter | Startet die JVEG-Kostenprüfung, trennt Rolle, Anspruchsart, Frist, Belege, Rechenweg und gewünschten Output. |
| jveg-aktenstripper | Liest Gerichtsschreiben, Anträge, Rechnungen, Belege und Kostenfestsetzungsunterlagen in eine prüfbare JVEG-Datenmatrix aus. |
| jveg-anspruchsberechtigung | Kläert, ob Zeuge, Dritter, Sachverständiger, Dolmetscher, Übersetzer, Protokollperson oder ehrenamtlicher Richter betroffen ist. |
| jveg-fristen-erloeschen | Prüft Geltendmachung, Drei-Monats-Frist, Belehrung, Wiedereinsetzung, Verjährung und sichere Fristennotizen. |
| jveg-vorschuss | Prüft Vorschussanträge nach § 3 JVEG mit Schwerpunkt erhebliche Fahrtkosten, Übernachtung und Teilleistungen. |
| jveg-zeugenentschaedigung | Rechnet und plausibilisiert Zeugenentschädigung nach §§ 19 bis 22 JVEG. |
| jveg-fahrtkosten | Prüft Bahn, Flug, eigenes Kfz, Kilometerpauschale, Parkkosten, Auslandsanreise und Wirtschaftlichkeit. |
| jveg-uebernachtung-aufwand | Prüft Tagegeld, notwendige Übernachtung, BRKG-Anknüpfung, Belege und gerichtliche Obergrenzen. |
| jveg-verdienstausfall-haushalt-zeit | Trennt Verdienstausfall, Haushaltsführungsnachteile und Zeitversäumnis, damit keine Doppelberechnung entsteht. |
| jveg-sonstige-aufwendungen-belege | Prüft sonstige notwendige bare Auslagen, Begleitpersonen, Vertretung, Kopien, Dateien und Belegfähigkeit. |
| jveg-sachverstaendigenrechnung | Prüft Sachverständigenvergütung: Honorargruppe, erforderliche Zeit, Reisezeit, Nebenkosten, § 8a-Risiken und Vorschussüberlauf. |
| jveg-dolmetscher-uebersetzer | Prüft Dolmetscher- und Übersetzervergütung, Stundensatz, Zeilen-/Textumfang, Reisezeiten und Sprach-/Terminlogik. |
| jveg-kuerzung-wegfall-8a | Findet Kürzungs- und Wegfallrisiken: Verwertbarkeit, Hinweisobliegenheit, Befangenheit, Vorschussüberschreitung und Mängel. |
| jveg-gerichtsschreiben-pruefung | Prüft Gerichtsschreiben und Kostenbeamtenargumente auf Tatbestandsfehler, Ermessensfehler, Beleganforderungen und Antwortbedarf. |
| jveg-rechenblatt | Erstellt ein prüfbares Rechenblatt mit Norm, Eingabewert, Kappung, Beleg, Rechenschritt und Ergebnis. |
| jveg-antragsgenerator | Erzeugt Vorschuss-, Nachzahlungs-, Festsetzungs- und Ergänzungsschreiben mit Anlagen- und Belegliste. |
| jveg-festsetzung-beschwerde | Führt durch gerichtliche Festsetzung, Erinnerung/Beschwerdeprüfung, Beschwer, Frist und knappe Angriffsmittel. |
| jveg-quality-gate | Letzte Prüfung vor Versand: Normstand, Mathematik, Belege, keine Doppelposten, Fristen, Ton und eindeutiger Antrag. |

## Beispiel Berger

Die Beispielakte bildet einen realistisch aussehenden Vorschussstreit ab: Barcelona nach Tübingen, 2.500 km Hin- und Rückfahrt, zwei Übernachtungen, geltend gemachter Verdienstausfall und gerichtliche Ablehnung des Vorschusses wegen angeblich fehlender Bedürftigkeit. Das Plugin markiert insbesondere, dass § 3 JVEG bei erheblichen Fahrtkosten und sonstigen Aufwendungen ansetzt und die Kostenpositionen getrennt nach Erstattungsfähigkeit, Vorschussfähigkeit und Belegstatus geprüft werden müssen.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 61 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aktenstripper` | JVEG-relevante Daten aus Gerichtsakten und Gutachterunterlagen extrahieren: Termine, Stunden, Auslagen. Normen: §§ 2 ff. JVEG. Prüfraster: Terminsprotokoll, Stundennachweis, Belegstruktur. Output: Extrahierter Datensatz für Kostenprüfung... |
| `anschluss-routing` | Anschluss-Routing für JVEG-Kostenprüfer: wählt den nächsten Spezial-Skill nach Engpass (Entschädigungsantrag binnen 3 Monaten, SV-Rechnung, Reisekostenabrechnung, Stundennachweise), dokumentiert Router-Entscheidung mit Begründung. |
| `anspruchsberechtigung-antragsgenerator` | Anspruchsberechtigung nach JVEG prüfen: Sachverständiger, Zeuge, Dolmetscher, Anwalt. Normen: §§ 1 2 JVEG. Prüfraster: Personenkategorie, Beauftragung durch Gericht, Verfahrensart. Output: Prüfergebnis Anspruchsberechtigung JVEG. Abgrenz... |
| `antragsgenerator` | Antrag auf gerichtliche Kostenfestsetzung nach JVEG erstellen: Verguetungsantrag, Anlagen, Fristen. Normen: §§ 2 4 JVEG. Prüfraster: Antragsfrist, Formerfordernis, Anlagenliste. Output: Kostenfestsetzungsantrag nach JVEG. Abgrenzung: nic... |
| `belegfeste-formular-portal-und-einreichung` | Belegfeste: Formular, Portal und Einreichungslogik. |
| `beschwerde-dolmetscher-sonderfall` | Beschwerde: Internationaler Bezug und Schnittstellen. |
| `dokumente-intake` | Dokumentenintake für JVEG-Kostenprüfer: sortiert SV-Rechnung, Reisekostenabrechnung, Stundennachweise, prüft Datum, Absender, Frist und Beweiswert (Aktennotizen, Reiseplanung); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO. |
| `dolmetscher-sonderfall-und-edge-case` | Dolmetscher: Sonderfall und Edge-Case-Prüfung. |
| `dolmetscher-uebersetzer` | Verguetung für gerichtliche Dolmetscher und Übersetzer nach JVEG berechnen. Normen: §§ 9 11 JVEG, Anlage 1 JVEG. Prüfraster: Stundenverguetung, Mindestwartezeit, Anfahrt, schriftliche Übersetzung je Seite. Output: Verguetungsberechnung D... |
| `dolmetscher-uebersetzer-fahrtkosten` | Spezialfall Dolmetscher- und Übersetzerverguetung JVEG: Stundenhonorar, Zeilenhonorar, schwierige Texte, Eilauftraege. Prüfraster Auftragsannahme im Jveg Kostenpruefer. |
| `dolmetscherkosten-zahlen-schwellen-und-berechnung` | Dolmetscherkosten: Zahlen, Schwellenwerte und Berechnung. |
| `einstieg-routing` | Einstieg, Triage und Routing für JVEG-Kostenprüfer: ordnet Rolle (Sachverständiger, Gericht, Bezirksrevisor), markiert Frist (Entschädigungsantrag binnen 3 Monaten), wählt Norm (JVEG, ZPO §§ 91 ff.) und Zuständigkeit (Gericht), leitet zu... |
| `fahrtkosten` | Fahrtkosten nach JVEG berechnen: eigenes Fahrzeug, öffentliche Verkehrsmittel, Flug. Normen: § 5 JVEG. Prüfraster: Wegstrecke, Verkehrsmittelwahl, Parkgebühren, Taxikosten. Output: Fahrtkosten-Berechnung JVEG. Abgrenzung: nicht Übernacht... |
| `fahrtkosten-festsetzung-interessen` | Fahrtkosten: Behörden-, Gerichts- oder Registerweg. |
| `festsetzung-beschwerde` | Beschwerde gegen JVEG-Kostenfestsetzungsbeschluss einlegen: Zulässigkeit, Frist, Begründung. Normen: § 4 Abs. 3 JVEG, §§ 569 ff. ZPO. Prüfraster: Beschwerdewert, Beschwerdefrist, Verfahrensart. Output: Beschwerdeschrift JVEG. Abgrenzung:... |
| `festsetzung-mehrparteien-konflikt-und-interessen` | Festsetzung: Mehrparteienkonflikt und Interessenmatrix. |
| `freistehender-erstpruefung-und-mandatsziel` | Freistehender: Erstprüfung, Rollenklärung und Mandatsziel. |
| `fristen-erloeschen` | Antragsfristen nach JVEG prüfen: drei Monate Ausschlussfrist für Verguetungsantrag. Normen: § 2 Abs. 1 JVEG. Prüfraster: Fristbeginn, Fristende, Wiedereinsetzungsmöglichkeit. Output: Fristenprüfung JVEG mit Empfehlung. Abgrenzung: nicht... |
| `gate-beweislast-jveg-quality` | Gate: Beweislast, Darlegungslast und Substantiierung. |
| `gate-rechenblatt` | Qualitaets-Gate für JVEG-Kostenberechnungen: Vollständigkeits- und Konsistenzprüfung aller Positionen. Normen: JVEG. Prüfraster: Vollständigkeit, Rechenfehler, Normzitate, Belegpflicht. Output: Quality-Gate-Prüfbericht JVEG. Abgrenzung:... |
| `gerichtsschreiben-kuerzung-wegfall` | Gerichtsschreiben zur JVEG-Kostenkuerzung rechtlich prüfen und widersprechen. Normen: §§ 2 4 JVEG, GKG. Prüfraster: Kuerzungsbegründung, fehlerhafte Berechnung, Widerspruchsmöglichkeit. Output: Widerspruchsschreiben gegen JVEG-Kuerzung.... |
| `jveg-dolmetscher-uebersetzer-spezial` | Spezialfall Dolmetscher- und Uebersetzerverguetung JVEG: Stundenhonorar, Zeilenhonorar, schwierige Texte, Eilauftraege. Pruefraster Auftragsannahme. |
| `jveg-kostenpruefer-schnellstart` | 'Kompakter Arbeitsmodus für JVEG-Kostenprüfer. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.' |
| `jveg-tatbestand-beweis-und-belege` | JVEG: Tatbestandsmerkmale, Beweisfragen und Beleglage. |
| `jveg-zeugenentschaedigung` | Zeugenentschaedigung nach JVEG berechnen: Fahrtkosten, Zeitversaeumnis, Verdienstausfall. Normen: §§ 19 ff. JVEG. Prüfraster: tatsaechliche Kosten, Zeitaufwand, Pauschalen. Output: Zeugenentschaedigungs-Berechnung. Abgrenzung: nicht Sach... |
| `kommandocenter` | Navigationszentrum für alle JVEG-Kostenprüfer-Skills: Weiterleitung je Personenkategorie und Verfahrensschritt. Normen: JVEG. Prüfraster: Einordnung Personenkategorie, aktueller Verfahrensschritt, Delegierung. Output: Navigationshinweis... |
| `kostenfestsetzung-belege-und-fristen` | Kostenfestsetzung mit Belegen, Fristen und Erinnerung: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Jveg Kostenpruefer. |
| `kostenfestsetzung-kostenpruefer` | Fristen: Compliance-Dokumentation und Aktenvermerk. |
| `kostenpruefer-fristen-form-und-zustaendigkeit` | Kostenpruefer: Fristen, Form, Zuständigkeit und Rechtsweg. |
| `kuerzung-wegfall-8a` | Kuerzung oder Wegfall der JVEG-Verguetung nach § 8a JVEG prüfen: fehlerhafte Gutachten, Verspaetung. Normen: § 8a JVEG. Prüfraster: Verschulden, Kausalität, Kuerzungsumfang. Output: Prüfergebnis Kuerzung § 8a JVEG mit Begründung. Abgrenz... |
| `mandantenkommunikation-redteam-qualitygate` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Jveg Kostenpruefer. |
| `output-waehlen` | Output-Wahl für JVEG-Kostenprüfer: stimmt Adressat (Sachverständiger, Gericht, Bezirksrevisor), Frist (Entschädigungsantrag binnen 3 Monaten) und Form auf den Zweck ab — typische Outputs: JVEG-Prüfung, Erinnerung gegen Festsetzung, Besch... |
| `pruefung-sachverstaendigengutachten-ki-deklaration` | KI-Deklaration in Sachverständigengutachten prüfen: Hat der Sachverständige KI-Nutzung offengelegt? Normen: §§ 404 ff. ZPO, JVEG. Prüfraster: Deklarationspflicht, Methodentransparenz, Beeinflussung des Gutachtenwertes. Output: Prüfergebn... |
| `quality-mandantenkommunikation-entscheidungsvorlage` | Quality: Mandantenkommunikation und Entscheidungsvorlage. |
| `quellen-livecheck` | Quellen-Live-Check für JVEG-Kostenprüfer: prüft Normen (JVEG, ZPO §§ 91 ff.) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Gericht und Quellenhygiene nach references/quellenhygiene.md. |
| `rechenblatt` | JVEG-Verguetungsberechnung in strukturiertem Rechenblatt erstellen: alle Kostenpositionen je Kategorie. Normen: §§ 5 bis 12 JVEG. Prüfraster: Stunden, Fahrtkosten, Auslagen, Verguetungssaetze. Output: Ausfuellbares Rechenblatt JVEG. Abgr... |
| `rechenprotokolle-fehlerkatalog` | Rechenprotokolle Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `sachverstaendigen-quellenkarte` | Sachverstaendigen Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `sachverstaendigenrechnung` | Sachverständigenrechnung nach JVEG prüfen oder erstellen: Stundenverguetung, Nebenkosten, Festbetrag. Normen: §§ 8 9 JVEG, Anlage 1 JVEG. Prüfraster: Verguetungshoehe, Berichtumfang, Auslagen. Output: Geprufte Sachverständigenrechnung. A... |
| `sachverstaendigenrechnung-bauleiter` | Bauleiter Sachverstaendigenrechnung JVEG: Honorargruppen, Zeitaufwand, Auslagen, Mehrwertsteuer. Prüfraster Sachverstaendiger und Kostenfestsetzung im Jveg Kostenpruefer. |
| `sonstige-aufwendungen-uebernachtung` | Sonstige Aufwendungen nach § 7 JVEG prüfen und belegen: Porto, Kopierkosten, technische Geräte. Normen: § 7 JVEG. Prüfraster: Belegpflicht, angemessene Hoehe, Erstattungsfähigkeit. Output: Aufwendungsnachweis JVEG. Abgrenzung: nicht Fahr... |
| `spezial-rechenprotokolle-red-team-und-qualitaetskontrolle` | Rechenprotokolle: Red-Team und Qualitätskontrolle. |
| `spezial-sachverstaendigen-livequellen-und-rechtsprechungscheck` | Sachverstaendigen: Livequellen- und Rechtsprechungscheck. |
| `spezial-uebersetzer-fristennotiz-und-naechster-schritt` | Uebersetzer: Fristennotiz und nächster Schritt. |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im JVEG Kostenpruefer-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Doku... |
| `uebernachtung-aufwand` | Übernachtungs- und Verpflegungskosten nach JVEG berechnen: Pauschalen und Einzelnachweise. Normen: § 6 JVEG. Prüfraster: Übernachtungserfordernis, Hotelkosten, Verpflegungspauschalen. Output: Übernachtungskosten-Nachweis JVEG. Abgrenzung... |
| `uebernachtung-verdienstausfall-vorschuss` | Uebernachtung: Schriftsatz-, Brief- und Memo-Bausteine. |
| `uebersetzer-fristennotiz-jveg` | Übersetzer: Fristennotiz und nächster Schritt. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für JVEG-Kostenprüfer: trennt fehlende Tatsachen von fehlenden Belegen (SV-Rechnung, Reisekostenabrechnung, Stundennachweise), nennt pro Lücke Beweisthema, Beschaffungsweg (Gericht), Frist und Ersatznachweis. |
| `verdienstausfall-haushalt-zeit` | Verdienstausfall und Zeitversaeumnis nach §§ 20 ff. JVEG für Zeugen und Sachverständige berechnen. Normen: §§ 20 21 22 JVEG. Prüfraster: tatsaechlicher Verdienstausfall, Stundensatz, Haushaltsführung. Output: Verdienstausfall-Berechnung... |
| `verdienstausfall-verhandlung-vergleich-und-eskalation` | Verdienstausfall: Verhandlung, Vergleich und Eskalation. |
| `vorschuss-kostenrisiko` | Vorschuss auf JVEG-Verguetung beantragen: Voraussetzungen, Formerfordernis, Verfahren. Normen: § 3 JVEG. Prüfraster: Vorschusshoehe, Belegpflicht, Auszahlungsverfahren. Output: Vorschussantrag nach JVEG. Abgrenzung: nicht Kostenfestsetzu... |
| `vorschuss-kostenrisiko-spezial` | Spezialfall Vorschuss und Kostenrisiko § 17 JVEG: Vorschussverlangen Sachverstaendiger, Verzicht des Gerichts, Folgen bei Nichteinzahlung. Prüfraster für Verfahrensbeteiligte im Jveg Kostenpruefer. |
| `vorschuss-risikoampel-und-gegenargumente` | Vorschuss: Risikoampel, Gegenargumente und Verteidigungslinien. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Jveg Kostenpruefer. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Jveg Kostenpruefer. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Jveg Kostenpruefer. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `zeugenentschaedigung` | Checkliste Zeugenentschaedigung JVEG: Verdienstausfall, Fahrtkosten, Aufwandsentschaedigung, Kinderbetreuung. Prüfraster für Zeuge und Geschäftsstelle im Jveg Kostenpruefer. |
| `zeugenentschaedigung-dokumentenmatrix-und-lueckenliste` | Zeugenentschaedigung: Dokumentenmatrix, Lückenliste und Nachforderung: Zeugenentschaedigung: Dokumentenmatrix, Lückenliste und Nachforderung. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
