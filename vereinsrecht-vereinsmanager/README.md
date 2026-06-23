# Vereinsrecht und Vereinsmanager

Wenn du das hier oeffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen pruefen und ein verwertbares Arbeitsprodukt erhalten.

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Dies ist eines von 229 Plugins aus dem Repo [`claude-fuer-deutsches-recht`](https://github.com/Klotzkette/claude-fuer-deutsches-recht). Das Repo ist von vornherein als **Plugin-Sammlung für Claude Code und Claude Cowork** gebaut: jedes Plugin enthält eine Familie zusammenhängender Skills (`SKILL.md`-Dateien), passende Hilfsdateien, Prüfrastern, Vorlagen und in vielen Fällen eine eigene Testakte. Der vorgesehene Hauptweg ist also: **Plugin in Claude Code / Cowork installieren**, am besten über den Marketplace, alternativ als einzelnes Plugin-ZIP. Dann läuft das Plugin in seiner natürlichen Umgebung mit allen Skills, Werkzeugen und Testdaten.

Damit das Plugin aber auch dann brauchbar bleibt, wenn jemand Claude Code / Cowork gerade nicht nutzen kann oder will (anderer Chatbot, Browser-Nutzung, schneller Test, Schulung, kein Setup zur Hand), gibt es zusätzlich zwei reine **Markdown-Prompts**, die ohne Plugin-Setup funktionieren: einen ausführlichen **Werkstatt-Prompt** und einen kompakten **Schnellstart-Prompt** (höchstens 7500 Zeichen). Beide sind eine einzelne `.md`-Datei, die man in jeden geeigneten Chatbot ziehen, einfügen oder per Copy-and-Paste verwenden kann.

## Downloads

In dieser Reihenfolge gedacht: zuerst der vorgesehene Plugin-Weg für Claude Code / Cowork, danach die Markdown-Alternativen für alles andere, am Schluss die zugehörigen Testakten.

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg, für Claude Code / Cowork) | ZIP | [`vereinsrecht-vereinsmanager.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/vereinsrecht-vereinsmanager.zip) |
| Großer Prompt (Werkstatt, Alternative ohne Plugin-Setup) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vereinsrecht-vereinsmanager/vereinsrecht-vereinsmanager-werkstatt.md" download><code>vereinsrecht-vereinsmanager-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart, höchstens 7500 Zeichen, Spar-Alternative) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/vereinsrecht-vereinsmanager/vereinsrecht-vereinsmanager-schnellstart.md" download><code>vereinsrecht-vereinsmanager-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) |

> Marketplace-Hinweis: Wer mehrere Plugins gleichzeitig will, fügt nicht jedes Plugin einzeln hinzu, sondern den ganzen Marketplace über `marketplace.json` aus dem [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest). Dann sind alle 229 Plugins in Claude Code / Cowork verfügbar und können einzeln aktiviert werden.
<!-- END direkt-loslegen (autogen) -->

Arbeitsplugin für Vereinsvorstände, Schriftführer, Kassenwarte, Gründergruppen und Mitglieder: vom Kegelclub bis zum großen gemeinnützigen Träger, vom nicht eingetragenen Verein bis zum e. V. und zum seltenen wirtschaftlichen Verein.

## Arbeitsidee

- Gründung, Satzung, Register, Vorstand, Mitgliederversammlung und Protokolle.
- Satzungsänderungen, Wahlen, Umlaufbeschlüsse, hybride und virtuelle Versammlungen.
- Gemeinnützigkeit, Spenden, Mittelverwendung, Zweckbetrieb und Finanzamt.
- Konflikte, Ausschluss, Haftung, Datenschutz, Veranstaltungen und Auflösung.
- Erzeugt Einladungen, Tagesordnungen, Beschlussvorschläge, Protokolle, Registeranmeldungs-Pakete und Rundbriefe.

## Quellenhygiene

Bundesrecht, Landesrecht, kommunale Satzungen, Parteisatzungen, Vereinsregisterpraxis, Wahlleiterhinweise und Formulare müssen bei echter Verwendung live geprüft werden. Keine Literatur- oder Datenbankfundstellen aus Modellwissen.

## Lizenz

Apache-2.0 OR MIT. Siehe Repository-Stammverzeichnis.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 59 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anfechtung-beschluss` | Prüft fehlerhafte Einladung, Tagesordnung, Mehrheit, Stimmrecht, Befangenheit und Vorgehen gegen Beschlüsse im Vereinsrecht Vereinsmanager. |
| `aufloesung-liquidation-beschlussvorlagen` | Begleitet Auflösung, Liquidatoren, Sperrjahr, Vermögensanfall, Register und Finanzamt im Vereinsrecht Vereinsmanager. |
| `beschlussvorlagen` | Formuliert rechtssichere Beschlussvorschläge für Versammlung, Vorstand oder Ausschuss im Vereinsrecht Vereinsmanager. |
| `datenschutz-mitgliederliste` | Regelt Mitgliederverwaltung, Verteiler, Fotos, WhatsApp-Gruppen, Cloud, Einwilligung und Löschung im Vereinsrecht Vereinsmanager. |
| `delegierte-abteilungen-entlastung-vorstand` | Gestaltet Delegiertenversammlung, Sparten, Abteilungen, Jugendordnung und interne Kompetenzen im Vereinsrecht Vereinsmanager. |
| `ehrenamtspauschale-uebungsleiter` | Erklärt steuerfreie Pauschalen, Voraussetzungen, Dokumentation, Kombination und Grenzen im Vereinsrecht Vereinsmanager. |
| `entlastung-vorstand` | Erklärt Entlastung, Reichweite, Interessenkonflikte und Beschlussformulierung im Vereinsrecht Vereinsmanager. |
| `foerdermittel-verein` | Prüft Zuwendungsbescheid, Eigenanteil, Vergabe, Verwendungsnachweis, Rückforderung und Satzungszweck im Vereinsrecht Vereinsmanager. |
| `foerderverein-schule-fusion-vereine` | Regelt Gemeinnützigkeit, Schulförderung, Kita-Nähe, Mittelverwendung, Datenschutz und Interessenkonflikte im Vereinsrecht Vereinsmanager. |
| `fusion-vereine` | Prüft Zusammenschluss, Vermögensübertragung, Mitgliederzustimmung, Satzungen und Registerpfad im Vereinsrecht Vereinsmanager. |
| `gemeinnuetzigkeit-antrag` | Bereitet Satzungsprüfung, Feststellung nach AO, Finanzamt-Kommunikation und Zuwendungsbestätigungen vor im Vereinsrecht Vereinsmanager. |
| `geschaeftsordnung-vorstand-gruendung` | Regelt Sitzungen, Beschlüsse, Ressorts, Zeichnungsrechte, Protokolle und Eilentscheidungen im Vereinsrecht Vereinsmanager. |
| `gruendung-eingetragener-verein` | Führt zur e.-V.-Gründung: sieben Mitglieder, Satzung, Gründungsprotokoll, Vorstand, notarielle Anmeldung, Vereinsregister im Vereinsrecht Vereinsmanager. |
| `gruendung-nicht-eingetragen` | Begleitet Gründung und Grundordnung eines nicht eingetragenen Vereins mit Mindestregeln, Haftungs- und Kontofragen im Vereinsrecht Vereinsmanager. |
| `haftung-vorstand-ehrenamtspauschale` | Prüft Sorgfalt, Ressortverteilung, Ehrenamtspauschale, Versicherung, Innenhaftung und Außenhaftung im Vereinsrecht Vereinsmanager. |
| `hilfsverein-wohlfahrt-hybride-virtuelle` | Prüft mildtätige Zwecke, Bedürftigkeitsnachweis, Hilfeleistungen, Datenschutz und Zweckbetrieb im Vereinsrecht Vereinsmanager. |
| `hybride-virtuelle-versammlung` | Prüft § 32 BGB, Satzung, Teilnahme-/Abstimmungsrechte, technische Hinweise, Identität und Protokoll im Vereinsrecht Vereinsmanager. |
| `kaltstart-triage` | Einstieg und Routing für Gründung, Satzung, Vorstand, Mitgliederversammlung, Register, Gemeinnützigkeit, Finanzen, Haftung, Konflikte und Auflösung. |
| `kassenwart-finanzen` | Strukturiert Kassenführung, Vier-Augen-Prinzip, Belege, Konten, Budget und Bericht im Vereinsrecht Vereinsmanager. |
| `kegelclub-freizeitverein-verein-kulturverein` | Minimalregeln für kleine Freizeitvereine: Kasse, Beiträge, Protokoll, Haftung, Austritt und Streitvermeidung im Vereinsrecht Vereinsmanager. |
| `konflikt-im-verein` | Moderiert Streit: Vorstand vs. Mitglieder, Akteneinsicht, Sonderversammlung, Abwahl, Ausschluss und Vergleich im Vereinsrecht Vereinsmanager. |
| `kulturverein` | Spezialfragen Kultur: Veranstaltungen, Künstlerverträge, GEMA, Fördermittel, Spenden, Gemeinnützigkeit im Vereinsrecht Vereinsmanager. |
| `minderjaehrige-verein-mitgliederversammlung` | Prüft Mitgliedschaft, Zustimmung Eltern, Aufsicht, Fotos, Schutzkonzept und Kinderschutz im Vereinsrecht Vereinsmanager. |
| `mitgliederversammlung-einberufung` | Erstellt Einladung, Fristcheck, Tagesordnung, Beschlussgegenstände und Versandnachweis im Vereinsrecht Vereinsmanager. |
| `mitgliedsbeitraege` | Gestaltet Beitragsordnung, Fälligkeit, Mahnung, Sozialklausel, Umlagen und Beitragserhöhung im Vereinsrecht Vereinsmanager. |
| `mitgliedschaft-aufnahme-beendigung-notarielle` | Regelt Aufnahme, Ablehnung, Rechte, Pflichten, Beiträge, Datenschutz und Minderjährige im Vereinsrecht Vereinsmanager. |
| `mitgliedschaft-beendigung` | Prüft Austritt, Beitragsrückstand, Ausschlussverfahren, Anhörung, Fairness und Dokumentation im Vereinsrecht Vereinsmanager. |
| `notarielle-anmeldung` | Bereitet Notartermin und Registeranmeldung für Gründung, Vorstand, Satzungsänderung und Auflösung vor im Vereinsrecht Vereinsmanager. |
| `ordnungen-verein-protokoll` | Entwirft Beitragsordnung, Geschäftsordnung, Wahlordnung, Ehrenordnung, Datenschutzordnung und Jugendordnung im Vereinsrecht Vereinsmanager. |
| `protokoll-mitgliederversammlung` | Erstellt Protokoll mit Anwesenheit, Versammlungsleitung, Beschlussfähigkeit, Abstimmung, Ergebnissen und Anlagen im Vereinsrecht Vereinsmanager. |
| `registergericht-rueckfrage` | Beantwortet Zwischenverfügung oder Rückfrage des Vereinsregisters mit Anlagen und Korrekturpfad im Vereinsrecht Vereinsmanager. |
| `ruecklagen-mittelverwendung-rundbrief` | Erklärt zeitnahe Mittelverwendung, freie Rücklage, Projektrücklage, Vermögensbindung und Nachweis im Vereinsrecht Vereinsmanager. |
| `rundbrief-mitglieder` | Erstellt klare Rundbriefe zu Versammlung, Beiträgen, Konflikten, Satzungsänderungen und Projekten im Vereinsrecht Vereinsmanager. |
| `satzung-grundstruktur` | Entwirft oder prüft Vereinszweck, Name, Sitz, Mitgliedschaft, Beiträge, Organe, Vorstand, Versammlung, Beschlüsse, Auflösung im Vereinsrecht Vereinsmanager. |
| `satzungsaenderung-satzungszweck` | Plant Satzungsänderung: Synopse, Einladung, Mehrheit, Protokoll, Register, Finanzamt bei Gemeinnützigkeit im Vereinsrecht Vereinsmanager. |
| `satzungszweck-gemeinnuetzigkeit` | Gleicht Vereinszweck mit AO-Gemeinnützigkeit, Selbstlosigkeit, Ausschließlichkeit, Unmittelbarkeit und Vermögensbindung ab im Vereinsrecht Vereinsmanager. |
| `sonderversammlung-minderheit` | Prüft Minderheitenverlangen, Einberufung durch Mitglieder, Tagesordnung und gerichtliche Hilfe im Vereinsrecht Vereinsmanager. |
| `spenden-zuwendungsbestaetigung-sportverein` | Prüft Geld-/Sachspenden, Spendenquittung, Aufwandsspende, Sponsoring-Abgrenzung und Haftung im Vereinsrecht Vereinsmanager. |
| `sponsoring-und-werbung` | Trennt Spende, Sponsoring, wirtschaftlicher Geschäftsbetrieb, Umsatzsteuer und Vertrag im Vereinsrecht Vereinsmanager. |
| `sportverein` | Spezialfragen Sportverein: Abteilungen, Trainer, Minderjährige, Schutzkonzept, Hallenzeiten, Verbandsrecht, Beiträge im Vereinsrecht Vereinsmanager. |
| `tagesordnung-erstellen` | Baut klare Tagesordnung mit Beschlussgegenständen, Wahlen, Berichten, Entlastung, Satzungsänderungen und Anträgen im Vereinsrecht Vereinsmanager. |
| `transparenzregister-gwg-umlaufbeschluss` | Prüft Transparenzregisterdaten, wirtschaftlich Berechtigte, Registerabgleich und Meldepflichten im Vereinsrecht Vereinsmanager. |
| `umlaufbeschluss` | Prüft Beschlüsse ohne Versammlung, Textform, Einstimmigkeit oder Satzungsregel, Dokumentation und Grenzen im Vereinsrecht Vereinsmanager. |
| `veranstaltung-planen` | Prüft Genehmigungen, Sicherheit, GEMA, Ausschank, Jugendschutz, Datenschutz, Versicherung und Verträge im Vereinsrecht Vereinsmanager. |
| `verein-als-zweckbetrieb-anfechtung-beschluss` | Routet Minijob, Übungsleiter, Ehrenamtspauschale, Arbeitsvertrag, Sozialversicherung und Lohnsteuer im Vereinsrecht Vereinsmanager. |
| `verein-dokumentenpaket-politik-social-media` | Baut aus Auftrag komplette Dokumente: Einladung, Tagesordnung, Beschluss, Protokoll, Rundbrief und Anlagenliste im Vereinsrecht Vereinsmanager. |
| `verein-livequellen-check` | Sammelt aktuelle amtliche Quellen zu BGB, AO, Registergericht, Finanzamt, Landesrecht und Satzung vor Ausgabe. |
| `verein-redteam-qualitygate` | Letzte Prüfung von Satzung, Einladung, Protokoll, Beschluss, Registeranmeldung oder Finanzamtsschreiben. |
| `verein-und-politik` | Warnt bei politischer Betätigung, Gemeinnützigkeit, Neutralität, Veranstaltungen und Parteispendennähe im Vereinsrecht Vereinsmanager. |
| `verein-und-social-media` | Regelt Impressum, Bildrechte, Datenschutz, Adminrechte, Krisenpost und Löschung im Vereinsrecht Vereinsmanager. |
| `vereinsrecht-vereinsmanager-schnellstart` | 'Kompakter Arbeitsmodus für Vereinsrecht und Vereinsmanager. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.' |
| `vereinsvermoegen-konto-versicherung-verein` | Hilft bei Kontoeröffnung, Zeichnungsberechtigung, Barkasse, Inventar, Zuschüssen und Vermögensbindung im Vereinsrecht Vereinsmanager. |
| `versicherung-verein` | Ordnet Vereinshaftpflicht, Veranstalterhaftpflicht, D&O, Unfallversicherung, Kfz und Vermögensschaden im Vereinsrecht Vereinsmanager. |
| `vorstand-rollen` | Klärt BGB-Vorstand, erweiterter Vorstand, Geschäftsführung, Ressorts, Vertretungsmacht und Innen-/Außenverhältnis im Vereinsrecht Vereinsmanager. |
| `vorstandswahl-vorstandswechsel-register` | Bereitet Wahlordnung, Kandidaturen, geheime/offene Abstimmung, Amtszeit, Annahme, Protokoll und Registeranmeldung vor im Vereinsrecht Vereinsmanager. |
| `vorstandswechsel-register` | Erstellt Registerpaket für Vorstandsänderung mit Protokollauszug, Anmeldung, Beglaubigung und Nachweisen im Vereinsrecht Vereinsmanager. |
| `wirtschaftlicher-verein` | Prüft, ob der seltene wirtschaftliche Verein oder eine andere Rechtsform besser passt; warnt vor Register- und Genehmigungsrisiken im Vereinsrecht Vereinsmanager. |
| `zweckaenderung` | Prüft strenge Anforderungen an Zweckänderung, Mitgliederschutz, Register und Gemeinnützigkeit: Prüft strenge Anforderungen an Zweckänderung, Mitgliederschutz, Register und Gemeinnützigkeit. |
| `zweckbetrieb` | Prüft Zweckbetrieb, wirtschaftlichen Geschäftsbetrieb, Sportveranstaltung, Wohlfahrt, Kultur und Steuerfolgen im Vereinsrecht Vereinsmanager. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
