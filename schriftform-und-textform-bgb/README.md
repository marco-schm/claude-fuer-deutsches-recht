# Schriftform und Textform im BGB

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Dies ist eines von 229 Plugins aus dem Repo [`claude-fuer-deutsches-recht`](https://github.com/Klotzkette/claude-fuer-deutsches-recht). Das Repo ist von vornherein als **Plugin-Sammlung für Claude Code und Claude Cowork** gebaut: jedes Plugin enthält eine Familie zusammenhängender Skills (`SKILL.md`-Dateien), passende Hilfsdateien, Prüfrastern, Vorlagen und in vielen Fällen eine eigene Testakte. Der vorgesehene Hauptweg ist also: **Plugin in Claude Code / Cowork installieren**, am besten über den Marketplace, alternativ als einzelnes Plugin-ZIP. Dann läuft das Plugin in seiner natürlichen Umgebung mit allen Skills, Werkzeugen und Testdaten.

Damit das Plugin aber auch dann brauchbar bleibt, wenn jemand Claude Code / Cowork gerade nicht nutzen kann oder will (anderer Chatbot, Browser-Nutzung, schneller Test, Schulung, kein Setup zur Hand), gibt es zusätzlich zwei reine **Markdown-Prompts**, die ohne Plugin-Setup funktionieren: einen ausführlichen **Werkstatt-Prompt** und einen kompakten **Schnellstart-Prompt** (höchstens 7500 Zeichen). Beide sind eine einzelne `.md`-Datei, die man in jeden geeigneten Chatbot ziehen, einfügen oder per Copy-and-Paste verwenden kann.

## Downloads

In dieser Reihenfolge gedacht: zuerst der vorgesehene Plugin-Weg für Claude Code / Cowork, danach die Markdown-Alternativen für alles andere, am Schluss die zugehörigen Testakten.

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg, für Claude Code / Cowork) | ZIP | [`schriftform-und-textform-bgb.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/schriftform-und-textform-bgb.zip) |
| Großer Prompt (Werkstatt, Alternative ohne Plugin-Setup) | Markdown | [`schriftform-und-textform-bgb-werkstatt.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/schriftform-und-textform-bgb/schriftform-und-textform-bgb-werkstatt.md) |
| Kleiner Prompt (Schnellstart, höchstens 7500 Zeichen, Spar-Alternative) | Markdown | [`schriftform-und-textform-bgb-schnellstart.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/schriftform-und-textform-bgb/schriftform-und-textform-bgb-schnellstart.md) |
| Testakte(n) als ZIP | ZIP | [`testakte-schriftform-maklervertrag-muenchen-eheleute-haspelbeck.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-schriftform-maklervertrag-muenchen-eheleute-haspelbeck.zip) (Schriftform-Maklervertrag – Eheleute Haspelbeck-Türkenfeld); [`testakte-schriftform-mietkuendigung-bielefeld-online-pferdedrescher.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-schriftform-mietkuendigung-bielefeld-online-pferdedrescher.zip) (Schriftform der Wohnraumkündigung — Pferdedrescher-Riesenstein ./. Eberhart-Wolframshausen) |

> Marketplace-Hinweis: Wer mehrere Plugins gleichzeitig will, fügt nicht jedes Plugin einzeln hinzu, sondern den ganzen Marketplace über `marketplace.json` aus dem [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest). Dann sind alle 229 Plugins in Claude Code / Cowork verfügbar und können einzeln aktiviert werden.
<!-- END direkt-loslegen (autogen) -->

**Plugin-Slug:** `schriftform-und-textform-bgb`
**Version:** 3.2.1
**Autor:** Klotzkette

## Installation

1. ZIP aus dem Release herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `schriftform-und-textform-bgb.zip` hochladen.
5. Mit einem konkreten Auftrag starten, zum Beispiel: `Prüfe ob unser Maklervertrag der Textform § 126b BGB genügt.`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

## Überblick

Umfassender Workflow-Organisator für Schriftform- und Textform-Erfordernisse im deutschen Zivilrecht. Das Plugin trennt Papierform, qES, Textform, beA/ERV, gerichtliche Zustellung und prozessuale Formfiktion und bietet kanzleitaugliche Orientierung für alle wesentlichen Formerfordernisse des BGB.

## Arbeitsrechtlicher Form-Sonderfall: Befristung

Die Befristungsabrede nach § 14 Abs. 4 TzBfG bleibt ein strenger Schriftformfall. Textform nach § 126b BGB, E-Mail, PDF-Scan, eingescannte Unterschrift, einfache elektronische Signatur und nicht qualifizierte Signaturportal-Workflows genügen nicht. Formwirksam sind nur Papieroriginale mit eigenhändiger Unterschrift beider Parteien oder eine echte qES beider Parteien nach § 126a BGB, jeweils vor Arbeitsaufnahme.

Der Formmangel führt nicht nur zu einem Beweisproblem, sondern materiell zu § 16 Satz 1 TzBfG: Die Befristung ist unwirksam und der Arbeitsvertrag gilt als unbefristet. Die gerichtliche Kontrolle läuft über § 17 TzBfG. Leitanker für die Skillarbeit sind ArbG Berlin, Urteil vom 28.09.2021 - 36 Ca 15296/20, LAG Berlin-Brandenburg, Urteil vom 16.03.2022 - 23 Sa 1133/21, und ArbG Gera, Urteil vom 07.03.2024 - 2 Ca 936/23.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **§ 130e ZPO und § 46h ArbGG seit 17.07.2024** — Formfiktion für klar erkennbare Willenserklärungen in elektronischen vorbereitenden Schriftsätzen, auch wenn elektronische Form materiell eigentlich ausgeschlossen ist.

## Skill-Verzeichnis

### Block A — Formvorschriften-Grundlagen

| Skill | Inhalt |
|-------|--------|
| `formerfordernisse-im-bgb-ueberblick` | Systematik §§ 125-129 BGB, Nichtigkeit § 125 BGB, Heilung |
| `schriftform-paragraph-126-bgb-eigenhaendige-unterschrift` | Originalunterschrift, Namenszeichnung, Faksimile, BGH-Linie |
| `elektronische-form-paragraph-126a-bgb-qes` | qES, eIDAS, Zertifikatskette, Zugang, beA-Abgrenzung, § 130e ZPO und § 46h ArbGG |
| `textform-paragraph-126b-bgb-dauerhafter-datentraeger` | E-Mail, WhatsApp, SMS, PDF als dauerhafter Datenträger |
| `notarielle-beurkundung-und-oeffentliche-beglaubigung` | § 128, § 129 BGB, BeurkG, GmbH, Grundstück, Erbvertrag |

### Block B — Zugang der formgerechten Erklärung

| Skill | Inhalt |
|-------|--------|
| `zugang-empfangsbeduerftiger-willenserklaerung-paragraph-130-bgb` | Zugangslehre, Machtbereich, Annahmeverweigerung |
| `zugang-formgerechter-erklaerung-bgh-viii-zr-159-23` | qES-Zugang, Transfervermerk § 298 Abs. 3 ZPO, Lehrsatz |
| `kuendigung-per-schriftsatz-zustellung-formfragen` | beA, qES, § 130a ZPO, § 130e ZPO, § 46h ArbGG, Zustellung, Vollmacht und § 174 BGB |
| `mandantenwarnung-qes-per-email-whatsapp-und-zugang` | Mandantenmemo: Mail-Anhänge prüfen, IT-Hinweise |

### Block C — Spezielle Formerfordernisse

| Skill | Inhalt |
|-------|--------|
| `maklervertrag-paragraph-656a-bgb-textform-bgh-i-zr-202-25` | § 656a BGB: E-Mail, Signaturhinweis, Textform und Verifizierungspflicht |
| `wohnraummiete-kuendigung-paragraph-568-bgb` | § 568, qES-Zugang, Begründungspflicht, Praxisempfehlung |
| `gewerberaummiete-paragraph-550-bgb-langzeitform` | Langzeitform, Heilung, ordentliche Kündigung bei Verstoß |
| `buergschaft-verbraucherdarlehen-und-andere-strenge-formen` | § 766, § 492, § 311b BGB, strenge Formen |
| `arbeitsrecht-befristung-und-aufhebung-paragraph-14-tzbfg-623-bgb` | § 14 Abs. 4 TzBfG, § 623 BGB, Aufhebungsvertrag |

### Block D — Workflow-Organisator

| Skill | Inhalt |
|-------|--------|
| `form-checker-fuer-vertrag-oder-willenserklaerung` | Entscheidungsbaum, Konsequenzen, Klausel-Vorschlag |
| `klauselgenerator-formvorbehalt-und-aenderungsvorbehalt` | Schriftformklausel, doppelte Schriftformklausel, AGB-Falle |
| `prozessablauf-papier-vs-elektronisch` | Workflow-Schritte: Papier, qES-Direktversand, beA-Schriftsatz mit Formfiktion und Textform |
| `dokumentations-und-beweisarchitektur` | Zugangsnachweis, qES-Validierung, TR-RESISCAN |

### Block E — Anspruchsgrundlagen-Modul

| Skill | Inhalt |
|-------|--------|
| `anspruchsformulierungen-bei-formverstoss` | § 812 BGB, Räumungsklage, Feststellungsklage, c.i.c. |
| `verteidigungsstrategie-bei-formangriff` | Heilung, § 242 BGB, Beweislast, Treuwidrigkeit |
| `mandantenkorrespondenz-form-und-zugang-templates` | Mandantenbriefe, Checklisten, Warnmemos |

## Hinweis

Alle Skills sind kanzleitauglich formuliert und enthalten vollständige Klauseltexte, Mandantenmemos und Querverweise auf aktuelle BGH-Rechtsprechung. Das Plugin ersetzt keine individuelle Rechtsberatung.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 60 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `amtlicher-formkern-bgb-zpo-check` | Amtlicher Formkern-Check für BGB und ZPO: trennt Schriftform, Textform, elektronische Form, qES, beA/EGVP, § 130e ZPO, Zustellung, Zugang und Beweiskraft elektronischer Dokumente im Schriftform Und Textform Bgb. |
| `anschluss-routing` | Anschluss-Routing für Schriftform/Textform BGB: wählt den nächsten Spezial-Skill nach Engpass (Form vor Wirksamkeit, Vertrag, Unterschrift, qualifizierte e-Signatur), dokumentiert Router-Entscheidung mit Begründung. |
| `anspruchsformulierungen-formverstoss` | Anspruchsformulierungen Bei Formverstoss: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung im Schriftform Und Textform Bgb. |
| `arbeitsrecht-befristung-schriftform-checker` | Arbeitgeber oder Arbeitnehmer fragt, ob Befristung, Kündigung oder Aufhebungsvertrag wegen Formverstoß unwirksam ist. Prüft § 14 Abs. 4 TzBfG, § 623 BGB, § 126 BGB, qES bei Befristung, direkte elektronische Form, § 46h ArbGG, § 174 BGB u... |
| `befristungsabrede-qes-rechtsprechung` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Schriftform Und Textform Bgb. |
| `befristungsabrede-qes-rechtsprechung-stand-2026` | Aktuelle Rechtsprechung zur elektronischen Signatur bei Befristungsabreden nach § 14 Abs. 4 TzBfG. Prüft Scan, einfache E-Signatur, echte qES, ArbG-Gera-Linie, § 623 BGB, § 46h ArbGG als Sonderpfad und Mandantenhinweise für Arbeitgeber u... |
| `bgb-mehrparteien-konflikt-und-interessen` | BGB: Mehrparteienkonflikt und Interessenmatrix. |
| `buergschaft-verbraucherdarlehen-und-andere-strenge-formen` | Mandant hat Buergschaft oder Darlehensvertrag unterschrieben und fragt ob er noch gebunden ist wenn die Form nicht korrekt eingehalten wurde. §§ 766 492 484 311b BGB strenge Formerfordernisse. Prüfraster: Buergschaft § 766 BGB Schriftfor... |
| `checklisten-schriftsatz-brief-und-memo-bausteine` | Checklisten: Schriftsatz-, Brief- und Memo-Bausteine. |
| `dokumentations-und-beweisarchitektur` | Anwalt oder Kanzlei muss sicherstellen dass Formerklärungen beweissicher dokumentiert und archiviert werden. Beweissicherung Willenserklärungen Formrecht. Prüfraster: Zugang § 130 BGB nachweisen Originalurkunden aufbewahren qES-Validieru... |
| `dokumente-intake` | Dokumentenintake für Schriftform/Textform BGB: sortiert Vertrag, Unterschrift, qualifizierte e-Signatur, prüft Datum, Absender, Frist und Beweiswert (Empfangsbestätigung, Versandbeleg); markiert Lücken; berücksichtigt Mandatsgeheimnis §... |
| `einstieg-routing` | Einstieg, Triage und Routing für Schriftform/Textform BGB: ordnet Rolle (Vertragsparteien), markiert Frist (Form vor Wirksamkeit), wählt Norm (§§ 126/126a und 126b BGB, § 127 BGB, § 130 BGB Zugang) und Zuständigkeit (Zivilgerichte), leit... |
| `elektronische-paragraph-formerfordernisse` | Elektronische Form Paragraph 126a BGB Qes: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung im Schriftform Und Textform Bgb. |
| `empfangsbeduerftiger-international` | Dokumentation: Verhandlung, Vergleich und Eskalation. |
| `empfangsbeduerftiger-international-schnittstellen` | Empfangsbeduerftiger: Internationaler Bezug und Schnittstellen. |
| `form-checker-fuer-vertrag-oder-willenserklaerung` | Mandant hat Vertrag oder Willenserklärung und fragt: Welche Form ist vorgeschrieben wurde sie eingehalten und was passiert wenn nicht? Form-Checker BGB. Prüfraster: gesetzliche vs. gewillkuerte Form Formhierarchie Nichtigkeitsfolge § 125... |
| `formerfordernisse-erstpruefung-und-mandatsziel` | Formerfordernisse: Erstprüfung, Rollenklärung und Mandatsziel. |
| `formerfordernisse-im-bgb-ueberblick` | Systematik der Formerfordernisse im BGB: gesetzliche vs. gewillkürte Form, §§ 125-129 BGB, Nichtigkeitsfolge § 125 BGB, Heilungsmöglichkeiten, Formhierarchie von Textform bis notarielle Beurkundung — Einstieg und Überblick für die Kanzle... |
| `formwahl-zugang-live-prozessablauf` | Formwahl, Zugang und Beweisrisiko im BGB und Prozessrecht: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Schriftform Und Textform Bgb. |
| `gewerberaummiete-paragraph-550-bgb-langzeitform` | Gewerbemieter oder Vermieter fragt: Ist ein laenger als 1 Jahr laufender Gewerberaummietvertrag wegen Schriftform-Verstoß vorzeitig kündbar? § 550 BGB Langzeitform Gewerberaummietvertrag. Prüfraster: Schriftformerfordernis Mietvertraege... |
| `klauselgenerator-formvorbehalt-maklervertrag` | Klauselgenerator Formvorbehalt Und Änderungsvorbehalt: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung im Schriftform Und Textform Bgb. |
| `kuendigung-per-mandantenkorrespondenz-zugang` | Anwalt versendet oder empfängt eine Kündigung per Schriftsatz und fragt nach Formwirksamkeit. Prüft Schriftform, beA, qES, § 130a ZPO, § 130e ZPO, § 46h ArbGG, § 173 ZPO, § 186 ZPO, § 298 Abs. 3 ZPO und § 174 BGB. Output: Form- und Zugan... |
| `live-zahlen-schwellen-und-berechnung` | Live: Zahlen, Schwellenwerte und Berechnung. |
| `maklervertrag-paragraph-656a-bgb-textform-bgh-i-zr-202-25` | Workflow-Skill zu Maklervertrag, § 656a BGB und Textform. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; behauptete Rechtsprechung zu I ZR 202/25 nie ohne Live-Pruefung zitieren. |
| `mandantenkorrespondenz-form-und-zugang-templates` | Mandantenkorrespondenz Form Und Zugang Templates: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung im Schriftform Und Textform Bgb. |
| `mandantenwarnung-qes-per-email-whatsapp-und-zugang` | Mandantenwarnung Qes Per Email Whatsapp Und Zugang: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung im Schriftform Und Textform Bgb. |
| `notarielle-beurkundung-prozessablauf-papier` | Mandant muss einen Vertrag notar-beurkunden lassen (GmbH-Kauf Grundstueckskauf Ehevertrag) und fragt nach Ablauf und Kosten. §§ 128 129 BGB Beurkundungsgesetz. Prüfraster: Beurkundungspflicht § 311b BGB Grundstueck § 15 GmbHG GmbH-Anteil... |
| `output-waehlen` | Output-Wahl für Schriftform/Textform BGB: stimmt Adressat (Vertragsparteien), Frist (Form vor Wirksamkeit) und Form auf den Zweck ab — typische Outputs: Schriftform-Memo, Vertrags-Markup, Zugangsnachweis-Plan. |
| `paragraph-fehlerkatalog` | Paragraph Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `prozessablauf-mandantenentscheidung` | Prozessablauf: Mandantenkommunikation und Entscheidungsvorlage. |
| `prozessablauf-papier-vs-elektronisch` | Kanzlei oder Mandant muss zwischen Papier, qES, Textform, beA-Schriftsatz oder Formfiktion wählen. Prüft Originalunterschrift, qES-Direktversand, § 130e ZPO, § 46h ArbGG, Textform per E-Mail, Zustellung und Beweisarchitektur. Output: kon... |
| `prozessordnungen-textform-verifikation` | Prozessordnungen: Behörden-, Gerichts- oder Registerweg. |
| `quellen-livecheck` | Quellen-Live-Check für Schriftform/Textform BGB: prüft Normen (§§ 126/126a und 126b BGB, § 127 BGB, § 130 BGB Zugang) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Zivilgerichte und Quellenhygiene nach reference... |
| `rechtsprechung-livecheck-formfragen` | Livecheck verifizierter Rechtsprechung zu Schriftform, qES und beA: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Schriftform Und Textform Bgb. |
| `rechtsprechung-quellenkarte` | Rechtsprechung Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `schriftform-fristen-form-und-zustaendigkeit` | Schriftform: Fristen, Form, Zuständigkeit und Rechtsweg. |
| `schriftform-paragraph-126-bgb-eigenhaendige-unterschrift` | Vertragspartner bestreitet Schriftform wegen fehlender oder unzureichender Unterschrift. § 126 BGB Schriftform eigenhaendige Namenszeichnung. Prüfraster: Namenszeichnung vs. Paraphe Urkundeneinheit bei mehrseitigen Vertraegen Blankounter... |
| `schriftform-textform-bgb-start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Schriftform Und Textform Bgb-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan... |
| `schriftform-und-textform-bgb-schnellstart` | 'Kompakter Arbeitsmodus für Schriftform und Textform im BGB. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.' |
| `sftf-arbeitsvertraege-nachweisgesetz` | Spezialfall Schriftform im Arbeitsverhaeltnis nach Nachweisgesetzaenderung 2022: schriftliche Aushaendigung, Bussgeld, Befristung. Prüfraster für Arbeitgeber im Schriftform Und Textform Bgb. |
| `sftf-doppelschriftform-aufhebung-spezial` | Spezialfall Aufhebung der doppelten Schriftform durch Individualabrede: BGH-Rechtsprechung, Auslegung, Beweisrisiko. Prüfraster für langlaufende Vertraege im Schriftform Und Textform Bgb. |
| `sftf-elektronische-signatur-leitfaden` | Leitfaden qualifizierte elektronische Signatur eIDAS: Vertrauensdienst, eID, Fernsignatur. Prüfraster für Vertraege und behoerdliche Verfahren im Schriftform Und Textform Bgb. |
| `sftf-formvorgaben-bgb-interessen-checklisten` | Bauleiter Formvorgaben BGB § 126 sowie § 126a sowie § 126b: Schriftform, elektronische Form, Textform. Prüfraster Vertraege Wohnraum, Arbeit, Verbraucher im Schriftform Und Textform Bgb. |
| `spezial-paragraph-red-team-und-qualitaetskontrolle` | Paragraph: Red-Team und Qualitätskontrolle. |
| `spezial-rechtsprechung-livequellen-und-rechtsprechungscheck` | Rechtsprechung: Livequellen- und Rechtsprechungscheck. |
| `textform-dokumentenmatrix-und-lueckenliste` | Textform: Dokumentenmatrix, Lückenliste und Nachforderung. |
| `textform-paragraph-verteidigungsstrategie` | Textform Paragraph 126b BGB Dauerhafter Datentraeger: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung im Schriftform Und Textform Bgb. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Schriftform/Textform BGB: trennt fehlende Tatsachen von fehlenden Belegen (Vertrag, Unterschrift, qualifizierte e-Signatur), nennt pro Lücke Beweisthema, Beschaffungsweg (Zivilgerichte), Frist und Ersatz... |
| `verifikation-compliance-dokumentation-und-akte` | Verifikation: Compliance-Dokumentation und Aktenvermerk. |
| `verteidigungsstrategie-bei-formangriff` | Mandant wird von Vertragspartner mit Formmangel-Einwand konfrontiert und Anwalt muss Verteidigung aufbauen. Verteidigung Formverstoß §§ 125 242 BGB. Prüfraster: Heilungsmöglichkeiten nach Vollzug (§ 311b BGB) Nachholung der Form § 242 BG... |
| `willenserklaerung-zivilrecht-zugang` | Willenserklaerung: Formular, Portal und Einreichungslogik. |
| `wohnraummiete-kuendigung-paragraph-568-bgb` | Wohnraummiete Kuendigung Paragraph 568 BGB: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung im Schriftform Und Textform Bgb. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Schriftform Und Textform Bgb. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Schriftform Und Textform Bgb. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |
| `zivilrecht-tatbestand-beweis-und-belege` | Zivilrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage. |
| `zugang-empfangsbeduerftiger-formgerechter` | Mandant fragt: Wann gilt Kündigung Mahnung oder sonstige Erklärung als zugegangen und ab wann laeuft die Frist? § 130 BGB Zugang. Prüfraster: Machtbereichslehre Möglichkeit der Kenntnisnahme Zugangsvereitelung Annahmeverweigerung Briefka... |
| `zugang-formgerechter-erklaerung-bgh-viii-zr-159-23` | Workflow-Skill zu zugang formgerechter erklaerung bgh viii zr 159 23. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `zugang-risikoampel-und-gegenargumente` | Zugang: Risikoampel, Gegenargumente und Verteidigungslinien. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
