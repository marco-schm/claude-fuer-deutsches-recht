# Berichtspflichten-Erlediger
Wenn du das hier oeffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen pruefen und ein verwertbares Arbeitsprodukt erhalten.

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Dies ist eines von 229 Plugins aus dem Repo [`claude-fuer-deutsches-recht`](https://github.com/Klotzkette/claude-fuer-deutsches-recht). Das Repo ist von vornherein als **Plugin-Sammlung für Claude Code und Claude Cowork** gebaut: jedes Plugin enthält eine Familie zusammenhängender Skills (`SKILL.md`-Dateien), passende Hilfsdateien, Prüfrastern, Vorlagen und in vielen Fällen eine eigene Testakte. Der vorgesehene Hauptweg ist also: **Plugin in Claude Code / Cowork installieren**, am besten über den Marketplace, alternativ als einzelnes Plugin-ZIP. Dann läuft das Plugin in seiner natürlichen Umgebung mit allen Skills, Werkzeugen und Testdaten.

Damit das Plugin aber auch dann brauchbar bleibt, wenn jemand Claude Code / Cowork gerade nicht nutzen kann oder will (anderer Chatbot, Browser-Nutzung, schneller Test, Schulung, kein Setup zur Hand), gibt es zusätzlich zwei reine **Markdown-Prompts**, die ohne Plugin-Setup funktionieren: einen ausführlichen **Werkstatt-Prompt** und einen kompakten **Schnellstart-Prompt** (höchstens 7500 Zeichen). Beide sind eine einzelne `.md`-Datei, die man in jeden geeigneten Chatbot ziehen, einfügen oder per Copy-and-Paste verwenden kann.

## Downloads

In dieser Reihenfolge gedacht: zuerst der vorgesehene Plugin-Weg für Claude Code / Cowork, danach die Markdown-Alternativen für alles andere, am Schluss die zugehörigen Testakten.

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg, für Claude Code / Cowork) | ZIP | [`berichtspflichten-erlediger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berichtspflichten-erlediger.zip) |
| Großer Prompt (Werkstatt, Alternative ohne Plugin-Setup) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/berichtspflichten-erlediger/berichtspflichten-erlediger-werkstatt.md" download><code>berichtspflichten-erlediger-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart, höchstens 7500 Zeichen, Spar-Alternative) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/berichtspflichten-erlediger/berichtspflichten-erlediger-schnellstart.md" download><code>berichtspflichten-erlediger-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) |

> Marketplace-Hinweis: Wer mehrere Plugins gleichzeitig will, fügt nicht jedes Plugin einzeln hinzu, sondern den ganzen Marketplace über `marketplace.json` aus dem [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest). Dann sind alle 229 Plugins in Claude Code / Cowork verfügbar und können einzeln aktiviert werden.
<!-- END direkt-loslegen (autogen) -->

Praxisplugin für mittelständische Betriebe, die ihre Berichtspflichten nicht lieben müssen, sie aber elegant, fristgerecht und belegbar erledigen wollen. Es sammelt Pflichten aus Statistik, Steuer, Sozialversicherung, Umwelt, Produktrecht, Lieferkette, Datenschutz, Arbeitsschutz und Aufsicht in einem operativen Workflow.

## Leitplanke

Das Plugin ist kein Bürokratie-Jubelchor. Es hilft, Berichtspflichten zu vermeiden, wenn sie nicht bestehen, und sie sauber zu erledigen, wenn sie bestehen. Keine freiwillige Übererfüllung, keine Fantasiezahlen, keine Portalabgabe ohne menschliche Freigabe.

## Was dieses Plugin gut kann

- Pflichten schnell identifizieren: Muss ich wirklich melden, an wen, bis wann, mit welchen Daten?
- Fristen, Portale, Rollen, Datenquellen und Versandnachweise in ein Board bringen.
- Meldungen vorbereiten, plausibilisieren, freigeben und dokumentieren.
- Überzogene oder freiwillige Datenanforderungen höflich, aber bestimmt begrenzen.

## Startlogik

Beginne mit dem allgemeinen Kaltstart-Skill. Er fragt Rolle, Ziel, Frist, Unterlagen, Risiken und gewünschten Output ab. Danach werden nur passende Spezial-Skills vorgeschlagen.

## Quellenhygiene

Normtexte werden aus amtlichen Quellen geprüft. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle verwendet. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 58 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abfallnachweis-nachwv-api-zugang` | Abfallrechtliche Nachweise: gefährliche Abfälle, eANV, Register, Entsorgungsnachweise, Begleitscheine und Abfallbilanz im Berichtspflichten. |
| `api-portal-zugang-rollen` | Behördenportale/API-Zugänge: ELSTER, IDEV, LUCID, ear, BAFA, DEHSt, Bundesbank, Rollen, Vertreter und Offboarding im Berichtspflichten. |
| `arbeitsschutz-unterweisung-nachweise` | Unterweisung, Gefährdungsbeurteilung, Betriebsanweisung, Prüfnachweise und Behördenkontrolle im Berichtspflichten. |
| `arbeitsunfall-dguv-audit-trail` | Arbeitsunfall/Berufskrankheit melden: Drei-Tage-Regel, Unfallanzeige, Betriebsrat, Fachkraft, Berufsgenossenschaft und Dokumentation im Berichtspflichten. |
| `audit-trail-freigabe` | Audit-Trail für Meldungen: Version, Quelle, Berechnung, Prüfung, Freigabe, Versand und Korrekturhistorie im Berichtspflichten. |
| `ausland-tochter-emissionshandel-tehg` | Auslandstochter/deutsches Unternehmen: AWV, Konzernbericht, Lieferkette, Steuer, Beschäftigte und Statistik-Schnittstellen im Berichtspflichten. |
| `aussenhandel-intrastat-battg` | Intrastat/Außenhandelsstatistik: Eingänge/Versendungen, Schwellen, Warennummer, Ursprungsland, Lieferbedingung und Korrekturmeldung im Berichtspflichten. |
| `battg-batterieregister-mengen` | Batterierecht: Registrierung, Geräte-/Industriebatterien, Rücknahme, Mengenmeldung, neue EU-Batterieverordnung-Schnittstelle im Berichtspflichten. |
| `baugenehmigung-baustatistik` | Baustatistik und Bauunterlagen: Genehmigung, Baubeginn, Fertigstellung, Nutzfläche, Kosten und Statistikbogen im Berichtspflichten. |
| `bauwirtschaft-soka-behg` | Bauwirtschaft: SOKA-BAU, Urlaubskasse, Mindestlohn, Nachunternehmer, Baustellenmeldungen und Dokumentation im Berichtspflichten. |
| `behg-brennstoffemissionen` | Nationaler Brennstoffemissionshandel: Verantwortlicher, Brennstoffmengen, Emissionsbericht, Zertifikate und DEHSt im Berichtspflichten. |
| `behoerdenkommunikation` | Saubere Behördenkommunikation bei Berichtspflichten: Rückfrage, Fristverlängerung, Korrektur, Nichtzuständigkeit und Nachweis im Berichtspflichten. |
| `berichtspflichten-erlediger-schnellstart` | 'Kompakter Arbeitsmodus für Berichtspflichten-Erlediger. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.' |
| `berichtspflichten-register-und-fristenboard` | Zentrales Fristen- und Zuständigkeitsboard für wiederkehrende Unternehmensmeldungen: Statistik, Steuer, Sozialversicherung, Umwelt, Produkt, Lieferkette und Aufsicht im Berichtspflichten. |
| `bundesbank-awv-z4-z5` | Außenwirtschaftsmeldungen an die Bundesbank: Z4/Z5/Z10, Zahlungs- und Forderungsbestände, Schwellen, Fristen und Meldebefreiungen im Berichtspflichten. |
| `bussgeld-vermeidung-heilung` | Verspätete/falsche Meldungen: Selbstkorrektur, Fristverlängerung, Anhörung, Bußgeldabwehr und Governance-Fix im Berichtspflichten. |
| `chemikalien-reach-csddd-vorschau-csrd` | Chemikalienrecht: Registrierung, Sicherheitsdatenblatt, CLP-Einstufung, Meldungen, nachgeschalteter Anwender und Stoffbeschränkungen im Berichtspflichten. |
| `csddd-vorschau-lieferkette` | CSDDD-Vorschau: künftige EU-Sorgfaltspflichten, Vertragskaskaden, Klimaplan und Übergangsmanagement im Berichtspflichten. |
| `csrd-esrs-lagebericht` | Nachhaltigkeitsberichterstattung: Anwendungsbereich, doppelte Wesentlichkeit, Datenpunkte, Lagebericht, Prüfung und mittelständische Lieferkettenschnittstelle im Berichtspflichten. |
| `datenminimierung-geheimnisschutz` | Schutz von personenbezogenen Daten und Geschäftsgeheimnissen bei Meldungen, Statistiken und Kundenfragebögen im Berichtspflichten. |
| `elektrog-ear-mengenmeldung` | ElektroG: Herstellerregistrierung, Gerätearten, Mengenmeldungen, Rücknahme, Bevollmächtigter und Marktplatzrisiko im Berichtspflichten. |
| `emissionshandel-tehg-dehst` | EU-Emissionshandel: Monitoringkonzept, jährlicher Emissionsbericht, Verifizierung, Abgabe von Zertifikaten und DEHSt-Fristen im Berichtspflichten. |
| `energieaudit-edl-entsendungen-a1-eudr` | Energieaudit-/Energiemanagementpflichten, Nicht-KMU-Prüfung, Umsetzungspläne und Nachweise im Berichtspflichten. |
| `entsendungen-a1-mindestlohn` | Entsendungen und Auslandseinsätze: A1, Meldepflichten, Mindestlohn, Arbeitszeit, Sozialversicherung und Nachweise im Berichtspflichten. |
| `eudr-entwaldung-due-diligence` | EUDR: relevante Rohstoffe/Produkte, Sorgfaltserklärung, Geolokalisierung, Risikobewertung und Lieferantendaten im Berichtspflichten. |
| `fuhrpark-telemetrie-datenschutz` | Fuhrparkdaten: Fahrer, Unfall, Fahrtenbuch, Maut, Tachograf, Telematik, Datenschutz und Steuer-/Arbeitsrecht im Berichtspflichten. |
| `gefahrstoffverzeichnis-gefstoffv` | Gefahrstoffverzeichnis, Betriebsanweisungen, Unterweisung, Sicherheitsdatenblätter und behördliche Nachweise im Berichtspflichten. |
| `geschaeftsfuehrer-dashboard` | Management-Dashboard: Top-Fristen, Bußgeldrisiken, Verantwortliche, offene Behördenfragen und Entlastungsmaßnahmen im Berichtspflichten. |
| `handwerk-gefahrstoffe-asbest` | Handwerksbetriebe: Asbest-/Gefahrstoffarbeiten, Anzeigen, Sachkunde, Schutzmaßnahmen und Dokumentation im Berichtspflichten. |
| `hinweisgeberschutz-jahresreport-idev` | Hinweisgeberstelle: Fallregister, Rückmeldefristen, Vertraulichkeit, Maßnahmen, Statistik und Geschäftsleitungsreport im Berichtspflichten. |
| `idev-estatistik-core` | Elektronische Statistikmeldungen über IDEV/eSTATISTIK.core: Zugang, Rollen, Importdateien, Plausibilitätsprüfung, Versandnachweis und interne Ablage im Berichtspflichten. |
| `immobilien-gebaeudeenergie-geg` | Gebäudeenergie: Energieausweis, Nachrüstpflichten, Heizungsdaten, Förder-/Meldeunterlagen und Vermieter-/Eigentümerpflichten im Berichtspflichten. |
| `jahresabschluss-bundesanzeiger-keine` | Offenlegung beim Unternehmensregister/Bundesanzeiger: Größenklasse, Frist, Erleichterung, Ordnungsgeld und Korrektur im Berichtspflichten. |
| `kaltstart-routing` | Einstieg für mittelständische Betriebe: Berichtspflichten, Statistikmeldungen, Portale, Fristen, Zuständigkeiten, Datenquellen und Vermeidungs-/Vereinfachungsoptionen schnell sortieren. |
| `keine-pflicht-begruendet-ablehnen` | Wenn keine Berichtspflicht besteht: rechtssicher antworten, ohne unnötig Daten zu liefern oder Konflikt zu eskalieren im Berichtspflichten. |
| `ki-einsatz-lohnsteuer` | KI-gestützte Berichtserstellung: Datenextraktion, Plausibilität, Red Flags, Freigabe und keine ungeprüfte Behördenabgabe im Berichtspflichten. |
| `konjunktur-und-produktionsstatistik` | Produktions-, Monats-, Jahres- und Konjunkturstatistiken für produzierende Betriebe: Erzeugnisse, Mengen, Umsätze, Auftragseingang im Berichtspflichten. |
| `konzern-mutter-lebensmittel-haccp` | Konzernweite Berichtspflichten: Schwellen, Konsolidierung, UBO, CSRD, LkSG, Statistik und Portale pro Gesellschaft im Berichtspflichten. |
| `lebensmittel-haccp-rueckverfolgung` | Lebensmittelbetriebe: HACCP, Eigenkontrollen, Rückverfolgbarkeit, Meldung unsicherer Lebensmittel und Behördenkommunikation im Berichtspflichten. |
| `lksg-bafa-bericht` | Lieferkettensorgfalt: Risikoanalyse, Beschwerdeverfahren, Präventionsmaßnahmen, Bericht/BAFA und Lieferantendokumentation im Berichtspflichten. |
| `lohnsteuer-sozialversicherung-meldungen` | Lohnsteueranmeldung, DEÜV-Meldungen, Beitragsnachweise, Sofortmeldungen und Jahresmeldungen koordinieren im Berichtspflichten. |
| `lucid-verpackg-maschinen-ce` | VerpackG: LUCID-Registrierung, Systembeteiligung, Datenmeldung, Vollständigkeit und Marktplatz-/Fulfillment-Konstellationen im Berichtspflichten. |
| `maschinen-ce-konformitaetsakte` | Maschinen/Anlagen: CE, Konformitätserklärung, technische Dokumentation, Risikobeurteilung und Marktüberwachung im Berichtspflichten. |
| `mindestlohndokumentation-arbeitszeit` | Mindestlohndokumentation, Arbeitszeitaufzeichnung, Branchenpflichten und Zollkontrolle im Berichtspflichten. |
| `mutterschutz-gefaehrdungsbeurteilung` | Mutterschutz: Gefährdungsbeurteilung, Meldung an Aufsicht, Schutzmaßnahmen und Dokumentation im Berichtspflichten. |
| `nachweisordner-dokumentenmatrix` | Dokumentenmatrix für Berichtspflichten: Datenquelle, Beleg, Berechnung, Freigabe, Abgabe, Versandnachweis und Aufbewahrung im Berichtspflichten. |
| `nis2-bsi-incident` | IT-Sicherheitsmeldungen: NIS2/BSI, Geschäftsleitung, Incident-Kategorien, Fristen, Nachbericht und Beweissicherung im Berichtspflichten. |
| `produktsicherheit-rueckruf-market` | Produktsicherheitsrecht: gefährliches Produkt, Rückruf, Safety Gate, Marktüberwachung, Händler-/Herstellerrolle und Dokumentation im Berichtspflichten. |
| `saisonkalender-mittelstand-stichprobe` | Jahresrhythmus typischer Berichtspflichten im Mittelstand: monatlich, quartalsweise, jährlich, ad hoc im Berichtspflichten. |
| `schwerbehindertenanzeige-sgb-verpackg` | Jährliche Anzeige beschäftigter schwerbehinderter Menschen und Ausgleichsabgabe im Berichtspflichten. |
| `statistik-anfrage-redteam` | Amtliche oder quasi-amtliche Datenanforderung kritisch prüfen: Rechtsgrundlage, Umfang, Geheimnisse, Datenschutz, Frist und Antwortstrategie. |
| `stichprobe-und-befreiung-kleine-unternehmen` | Prüft bei Statistik- und Berichtspflichten, ob kleine/mittlere Unternehmen wegen Schwellen, Stichprobe, Bagatelle, einmaliger Auswahl oder Härte entlastet werden können im Berichtspflichten. |
| `transparenzregister-gwg-ubo` | Transparenzregister: wirtschaftlich Berechtigte, Meldefiktion, Änderungen, Unstimmigkeitsmeldung, Bußgeldrisiko und Konzernfälle im Berichtspflichten. |
| `trinkwasser-legionellen-umsatzsteuer` | Trinkwasserpflichten: Legionellenprüfung, Anzeige, Betreiberpflicht, Mieterinformation und Maßnahmenplan im Berichtspflichten. |
| `umsatzsteuer-voranmeldung-elster` | USt-Voranmeldung als Berichtspflicht: Frist, Dauerfristverlängerung, Beleglogik, innergemeinschaftliche Lieferungen und Korrektur im Berichtspflichten. |
| `verdienststatistik-verdstatg` | Verdienst-/Entgeltstatistik: Auswahl, Beschäftigtengruppen, Entgeltbestandteile, Arbeitszeit, Datenschutz und Plausibilität im Berichtspflichten. |
| `verpackg-vollstaendigkeitserklaerung` | Vollständigkeitserklärung nach VerpackG: Schwellen, Mengen, Prüfer, Abgabe und Korrektur im Berichtspflichten. |
| `wp-stb-koordination` | Koordination mit Steuerberater, Wirtschaftsprüfer, Lohnbüro und Fachabteilungen bei überlappenden Berichtspflichten im Berichtspflichten. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
