# Telekommunikationsrecht

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Großes Telekommunikationsrecht-Plugin für TKG, Bundesnetzagentur, Internetanschlüsse, Anbieterwechsel, Kundenschutz, Netzregulierung, Frequenzen, Nummerierung, Sonderkartellrecht, Datenschutz und Sicherheitsanforderungen.

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

Schneller Weg: Für eine erste Ergebnisrichtung den Schnellstart laden, für einen tragfähigen Arbeitsmodus die Werkstatt. Beide Prompts sollen mit einem konkreten Arbeitsprodukt beginnen, nur eng nachfragen und nicht in einer Materialinventur hängen bleiben.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`telekommunikationsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/telekommunikationsrecht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/telekommunikationsrecht/telekommunikationsrecht-werkstatt.md" download><code>telekommunikationsrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/telekommunikationsrecht/telekommunikationsrecht-schnellstart.md" download><code>telekommunikationsrecht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) und [`alle-testakten-einzelpdfs.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten-einzelpdfs.zip) (zentrale Sammlung) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen prüfen und ein verwertbares Arbeitsprodukt erhalten.
Großes Arbeitsplugin für Telekommunikationsrecht: vom defekten Internetanschluss bis zur Beschlusskammer der Bundesnetzagentur, vom Glasfaserausbau bis zu Frequenzen, Nummerierung, Netzneutralität, Sicherheitsvorfall und Sonderkartellrecht.

## Was dieses Plugin gut kann

- Verbraucher- und Geschäftskundenfälle zu Anschluss, Störung, Anbieterwechsel, Rufnummer und SLA sauber dokumentieren.
- BNetzA-Verfahren mit Akteneinsicht, Anhörung, Geschäftsgeheimnissen, Stellungnahmen und Eilrechtsschutz führen.
- Marktanalyse, Zugang, Entgelt, Frequenzen, Nummerierung, Open Access und Missbrauchsaufsicht fachlich trennen.
- Datenschutz, Standort-/Verkehrsdaten, IT-Sicherheit, NIS2/BSI und Notfallkommunikation integrieren.

## Startlogik

Beginne mit `tk-allgemeiner-kaltstart`. Der Skill trennt Verbraucherstreit, Geschäftskunden-SLA, Netzbetrieb, Frequenz, Nummerierung, Marktmacht, Infrastruktur, Datenschutz/Sicherheit und BNetzA-Verfahren. Danach wird nur gezielt in Spezial-Skills verzweigt.

## Rechtsweg-Kompass

Telekommunikationsrecht ist gemischt: Vertragliche Ansprüche laufen regelmäßig zivilrechtlich; regulierungsrechtliche Maßnahmen der Bundesnetzagentur sind öffentlich-rechtlich; Missbrauchs- und Wettbewerbsfragen können zivil-, verwaltungs- oder kartellrechtliche Schnittstellen haben. Deshalb prüft jeder streitige Skill zuerst Bescheid, Anspruch, Norm und Rechtsbehelfsbelehrung.

## Quellenhygiene

TKG, Nebengesetze, EU Electronic Communications Code, BNetzA-Verfügungen und Verwaltungspraxis werden live geprüft. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle.

<!-- BEGIN SKILLS-LOGIC (auto-generated) -->

## Orientierung nach Arbeitslogik

Diese Navigation ordnet die Skills nach typischen Arbeitsschritten. Die alphabetische Komplettliste bleibt darunter erhalten.

| Arbeitsphase | Typische Skills |
| --- | --- |
| 1. Einstieg und Fallrouting | `eu-eecc-router`, `kaltstart-routing`, `routerfreiheit-tk-rufnummernmissbrauch`, `zustaendigkeits-router-bnetza-vg-lg` |
| 2. Unterlagen, Sachverhalt und Quellen | `beschwerde-tk-beweisplan`, `beweisplan-messung-stoerung-protokoll`, `vorratsdaten-tk-wegerecht` |
| 3. Prüfung, Anspruch und Subsumtion | `marktanalyse-tk-meldepflicht`, `redteam-regulierungsrisiko` |
| 4. Gestaltung, Strategie und Verhandlung | `behoerdenkommunikation-kooperationsstrategie`, `glasfaser-tk-infrastruktursharing`, `infrastruktursharing-open-access`, `mindestvertragslaufzeit-tk-umzug`, `umzug-vertragsanpassung` |
| 5. Verfahren, Behörde und Gericht | `abhoerschnittstellen-sicherheitsbehoerden`, `eilrechtsschutz-bnetza-beschluss`, `output-beschwerde-antrag-klage`, `zivilklage-tk-abhoerschnittstellen` |
| 8. Spezialmodule und Schnittstellen | `abmahnung-tk-anbieterwechsel`, `anbieterwechsel-rufnummernmitnahme`, `anschlussbereitstellung-tk`, `bauarbeiten-kabelschaden`, `bundesnetzagentur-tk-zustaendigkeits`, `callcenter-tk-campusnetze`, `campusnetze-private-5g`, `cloud-tk-cookies`, `cookies-telemedien-ttdsg-tdddg`, `datacenter-tk-eilrechtsschutz`, `entgeltgenehmigung-tk-eu`, `frequenznutzung-tk-frequenzzuteilung`, `frequenzzuteilung-auktionsdesign`, `iot-tk-kartellrecht`, `kartellrecht-schnittstelle-gwb-eu`, `meldepflicht-it-sicherheitsvorfall`, `missbrauchsaufsicht-tk-mitnutzung`, `mitnutzung-gebaeude-netze`, ... plus 21 weitere |

<!-- END SKILLS-LOGIC (auto-generated) -->

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 57 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abhoerschnittstellen-sicherheitsbehoerden` | Wenn es um Überwachungsschnittstellen und Behördenauskünfte in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und... |
| `abmahnung-tk-anbieterwechsel` | Wenn es um Abmahnung nach UWG/TKG in Telekommunikationsrecht geht: entwickelt Verhandlungsziel, Vergleichskorridor und Eskalationspfad; liefert einen Einreichungsplan mit Form-, Portal- und Nachweischeck. |
| `anbieterwechsel-rufnummernmitnahme` | Wenn es um Anbieterwechsel und Rufnummernmitnahme in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächst... |
| `anschlussbereitstellung-tk` | Wenn es um Anschlussbereitstellung und Verzug in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `bauarbeiten-kabelschaden` | Wenn es um Kabelschaden durch Bauarbeiten in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `behoerdenkommunikation-kooperationsstrategie` | Wenn es um Behördenkommunikation mit BNetzA in Telekommunikationsrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Verhandlungs- oder Eskalationslinie mit Optionen. |
| `beschwerde-tk-beweisplan` | Wenn es um BNetzA-Beschwerde-Dashboard in Telekommunikationsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `beweisplan-messung-stoerung-protokoll` | Wenn es um Beweisplan: Messung, Störung, Protokoll in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Beweislast- und Substantiierungsmatrix. |
| `bundesnetzagentur-tk-zustaendigkeits` | Wenn es um BNetzA-Verfahren: Akteneinsicht, Anhörung, Fristen in Telekommunikationsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `callcenter-tk-campusnetze` | Wenn es um Werbeanrufe und Callcenter in Telekommunikationsrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `campusnetze-private-5g` | Wenn es um Campusnetze und private 5G-Netze in Telekommunikationsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `cloud-tk-cookies` | Wenn es um Cloud-Telefonie und VoIP in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `cookies-telemedien-ttdsg-tdddg` | Wenn es um Cookies, Telemedien und TDDDG-Schnittstelle in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und n... |
| `datacenter-tk-eilrechtsschutz` | Wenn es um Datacenter Connectivity und Carrier Meet-Me in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und n... |
| `eilrechtsschutz-bnetza-beschluss` | Wenn es um Eilrechtsschutz gegen BNetzA-Beschluss in Telekommunikationsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `entgeltgenehmigung-tk-eu` | Wenn es um Entgeltgenehmigung und Kostenorientierung in Telekommunikationsrecht geht: ordnet Akteninhalt, Belege, Lücken und Nachforderungen; liefert eine Dokumentenmatrix mit Nachforderungsliste. |
| `eu-eecc-router` | Wenn es um EU Electronic Communications Code Router in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachwei... |
| `frequenznutzung-tk-frequenzzuteilung` | Wenn es um Frequenzstörungen und Funkverträglichkeit in Telekommunikationsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `frequenzzuteilung-auktionsdesign` | Wenn es um Frequenzzuteilung und Auktionen in Telekommunikationsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `glasfaser-tk-infrastruktursharing` | Wenn es um Glasfaser-Hausanschluss und Wegerecht in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächste... |
| `infrastruktursharing-open-access` | Wenn es um Infrastruktursharing und Open Access in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem... |
| `iot-tk-kartellrecht` | Wenn es um IoT, M2M und SIM-Karten in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `kaltstart-routing` | Wenn es um Telekommunikationsrecht: Kaltstart und Rechtsweg-Triage in Telekommunikationsrecht geht: klärt Rolle, Ziel, Frist, Unterlagen und den passenden nächsten Fachskill; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, R... |
| `kartellrecht-schnittstelle-gwb-eu` | Wenn es um Kartellrechtliche Schnittstelle GWB/EU in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisf... |
| `marktanalyse-tk-meldepflicht` | Wenn es um Marktanalyse und beträchtliche Marktmacht in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachwe... |
| `meldepflicht-it-sicherheitsvorfall` | Wenn es um IT-Sicherheitsvorfall und Meldepflicht in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächst... |
| `mindestvertragslaufzeit-tk-umzug` | Wenn es um Mindestlaufzeit, Verlängerung, Kündigung in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und näch... |
| `missbrauchsaufsicht-tk-mitnutzung` | Wenn es um TK-Missbrauchsaufsicht als Sonderkartellrecht in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Na... |
| `mitnutzung-gebaeude-netze` | Wenn es um Mitnutzung von Gebäudenetzen und passiver Infrastruktur in Telekommunikationsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `netzneutralitaet-tk-nis2` | Wenn es um Netzneutralität, Zero-Rating und Drosselung in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nach... |
| `nis2-kritis-bsi-schnittstelle` | Wenn es um NIS2, KRITIS und BSI-Schnittstelle in Telekommunikationsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `notfall-tk-notrufpflicht` | Wenn es um Notfall- und Katastrophenkommunikation in Telekommunikationsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `notrufpflicht-112` | Wenn es um Notrufpflicht und Ausfallsicherheit in Telekommunikationsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `nummerierung-tk-open` | Wenn es um Nummerierung und Rufnummernzuteilung in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem... |
| `open-ran-lieferketten` | Wenn es um Open RAN und Lieferketten in Telekommunikationsrecht geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| `output-beschwerde-antrag-klage` | Wenn es um Output-Generator: Beschwerde, Antrag, Klage, Stellungnahme in Telekommunikationsrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung u... |
| `redteam-regulierungsrisiko` | Wenn es um Regulierungsrisiko Red-Team in Telekommunikationsrecht geht: zerlegt Ergebnis, Frist, Zuständigkeit, Beweislast und Gegenposition; liefert eine Gegenprüfung mit Fehler-, Beweis- und Fristencheck. |
| `routerfreiheit-tk-rufnummernmissbrauch` | Wenn es um Routerfreiheit und Endgeräte in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `rufnummernmissbrauch-abschaltung` | Wenn es um Rufnummernmissbrauch, Abschaltung und Inkassoverbot in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risik... |
| `satellite-tk-schlichtung` | Wenn es um Satellitenkommunikation und NTN in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schr... |
| `schlichtung-verbraucher` | Wenn es um Verbraucherschlichtung Telekommunikation in Telekommunikationsrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `sla-tk-standardangebot` | Wenn es um Business-SLA und Ausfall in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `standardangebot-reference-offer` | Wenn es um Standardangebot und Reference Offer in Telekommunikationsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `stoerung-tk-streitbeilegung` | Wenn es um Störung, Minderung und Ausfallentschädigung in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und n... |
| `streitbeilegung-bnetza` | Wenn es um BNetzA-Streitbeilegung zwischen Unternehmen in Telekommunikationsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `towerco-tk-traffic` | Wenn es um TowerCo und Mobilfunkstandortmiete in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem S... |
| `traffic-location-data-privacy` | Wenn es um Verkehrs- und Standortdaten in Telekommunikationsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `umzug-vertragsanpassung` | Wenn es um Umzug und Telekommunikationsvertrag in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfragen. |
| `universalservice-tk-verwaltungsrecht` | Wenn es um Universaldienst und Mindestversorgung in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenargumenten. |
| `verwaltungsrecht-anfechtung-bnetza` | Wenn es um Anfechtung von BNetzA-Beschlüssen in Telekommunikationsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `vorratsdaten-tk-wegerecht` | Wenn es um Vorratsdaten und Speicherpflichten in Telekommunikationsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `wegerecht-oeffentliche-wege` | Wenn es um Wegerecht für öffentliche Wege in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert ein direkt nutzbares Arbeitsprodukt mit Prüfpunkten, Risiken und nächstem Schritt. |
| `wholesale-tk-bauarbeiten` | Wenn es um Wholesale, Reseller und MVNO-Verträge in Telekommunikationsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zivilklage-tk-abhoerschnittstellen` | Wenn es um Zivilklage: Entgelt, Schaden, Vertrag in Telekommunikationsrecht geht: erstellt den passenden Entwurf aus Sachverhalt, Norm, Beweis und Antrag; liefert einen verwertbaren Entwurf mit Anträgen, Begründung und Anlagenlogik. |
| `zugangsregulierung-tk-zusammenschaltung` | Wenn es um Zugangsregulierung und Vorleistungen in Telekommunikationsrecht geht: ordnet Sachverhalt, Norm, Beweislast, Gegenargumente und nächsten Schritt; liefert eine Schnittstellenkarte mit Kollisions-, Zuständigkeits- und Nachweisfra... |
| `zusammenschaltung-interconnection` | Wenn es um Zusammenschaltung und Interconnection in Telekommunikationsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Fristen- und Risikoampel mit Sofortschritten. |
| `zustaendigkeits-router-bnetza-vg-lg` | Wenn es um Zuständigkeit: BNetzA, Verwaltungsgericht, Zivilgericht, Kartellspur in Telekommunikationsrecht geht: prüft Frist, Form, Zuständigkeit, Rechtsweg und Sofortmaßnahmen; liefert eine Tatbestands- oder Anspruchsmatrix mit Gegenarg... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
