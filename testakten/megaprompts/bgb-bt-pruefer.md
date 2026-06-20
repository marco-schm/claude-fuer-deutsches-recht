# Megaprompt: bgb-bt-pruefer

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 108 Skills (gekuerzt fuer Chat-Fenster) des Plugins `bgb-bt-pruefer`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Einstieg, Schnelltriage und Skill-Routing für BGB-BT-Fälle: Anspruchsziel, Vertragstyp, gesetzliches Schuldverhältnis, S…
2. **kaufrecht-beweislast-verjaehrung-digitale-elemente** — Prüft im Kaufrecht die Beweislast für den Sachmangel bei Gefahrübergang, die B2C-Vermutung des § 477 BGB nach BGH, Urtei…
3. **amtlicher-bgb-auftrag-unentgeltliche** — Amtlicher Normcheck für BGB-BT-Fälle: prüft Vertragstypen, Leistungsstörung, AGB, Verbraucherrecht, digitale Produkte, K…
4. **dokumente-intake** — Dokumentenintake für BGB Besonderer Teil — Prüfungsschemata: sortiert Verträge, Lieferscheine, Rechnungen, prüft Datum, …
5. **kaufrecht-sachmangel-paragraph-434** — Prüft Sachmangel § 434 BGB mit subjektiven, objektiven und Montageanforderungen, Aliud-Lieferung, Gefahrübergang, B2C-Be…
6. **kaufrecht-schadensersatz-aufwendungsersatz** — Prüft Schadensersatz §§ 437 Nr. 3 und 280 ff. BGB sowie Aufwendungsersatz § 284 BGB beim Kaufrecht mit Schwerpunkt Sachm…
7. **kaufrecht-nacherfuellung-ruecktritt-minderung** — Prüft Nacherfüllung § 439 BGB, Rücktritt § 437 Nr. 2 BGB, Minderung, Schadensersatz, Beweislast für den Sachmangel bei G…
8. **kaufrecht-gefahruebergang-und-versendung** — Prüft Gefahrübergang § 446 BGB, Versendungskauf § 447 BGB, Verbrauchsgüterkauf-Ausnahmen, Beweislast für den Mangel bei …

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Skill-Routing für BGB-BT-Fälle: Anspruchsziel, Vertragstyp, gesetzliches Schuldverhältnis, Störung, Beweise, Fristen und Output._

# BGB BT Kommandocenter

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Bgb Bt Prüfer** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Sofortstart

1. Kläre Rolle, Ziel, Gegner, Frist, Dokumente und gewünschtes Arbeitsprodukt.
2. Zerlege den Fall in Tatsachen, Normen, Streitpunkte, Beweisfragen und methodische Wertungen.
3. Liefere zuerst eine Kurzantwort mit Risikoampel, danach den Prüfpfad.
4. Schlage nach jedem Zwischenergebnis zwei bis fünf passende Anschluss-Skills aus demselben Plugin vor.

## Rechts- und Quellenanker

BGB amtlich prüfen: https://www.gesetze-im-internet.de/bgb/. Je nach Skill insbesondere §§ 241 ff., 249 ff., 280 ff., 433 ff., 488 ff., 535 ff., 581 ff., 611 ff., 631 ff., 662 ff., 675 ff., 677 ff., 765 ff., 812 ff., 823 ff. BGB.
Bei tragenden Normfragen `amtlicher-bgb-bt-normcheck` zuschalten; er nutzt den neuen BGB-BT-Normkern und routet in ZPO-Durchsetzung, wenn ein Klage-, Mahn- oder Eilprodukt entstehen soll.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Quellen

- https://www.gesetze-im-internet.de/bgb/
- https://www.bundesgerichtshof.de/
- https://dejure.org/gesetze/BGB

---

## Skill: `kaufrecht-beweislast-verjaehrung-digitale-elemente`

_Prüft im Kaufrecht die Beweislast für den Sachmangel bei Gefahrübergang, die B2C-Vermutung des § 477 BGB nach BGH, Urteile vom 06.05.2026 - VIII ZR 73/24 und VIII ZR 257/23, die Verjährung nach § 438 BGB, digitale Elemente und die B2B-Abgrenzung mit § 377 HGB._

# Kaufrecht: Beweislast, Verjährung und digitale Elemente

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 433, 434, 437, 438, 446, 474, 475b, 475c, 477 sowie bei beiderseitigem Handelskauf HGB §§ 343, 344, 377 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur und die BGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachkern: Kaufrecht: Beweislast, Verjährung und digitale Elemente
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Zweck

Beweislastumkehr nach § 477 BGB, Verjährungsfristen nach § 438 BGB und besondere Regeln für Ware mit digitalen Elementen (§§ 475b ff. BGB) prüfen.

## Normanker

- § 433 BGB: Hauptpflichten aus dem Kaufvertrag
- § 434 BGB: Sachmangel und Beschaffenheitsanforderungen
- § 437 BGB: Rechte des Käufers bei Mängeln
- § 438 BGB: Verjährung der Mängelansprüche
- § 446 BGB: Gefahrübergang bei Übergabe
- § 474 BGB: Verbrauchsgüterkauf
- § 477 BGB: Beweislastumkehr beim Verbrauchsgüterkauf
- §§ 475a–475e BGB: Besondere Vorschriften für Verträge über digitale Produkte
- § 475b BGB: Ware mit digitalen Elementen
- § 475c BGB: dauerhafte Bereitstellung digitaler Elemente
- §§ 327 ff. BGB: Verträge über digitale Produkte (Grundregeln)
- § 377 HGB: Untersuchungs- und Rügeobliegenheit beim beiderseitigen Handelskauf

## Intake

- Ist der Mangel innerhalb von einem Jahr nach Gefahrübergang aufgetreten (§ 477 BGB-Frist)?
- Handelt es sich um Ware mit digitalen Elementen; gilt § 475b oder § 475c BGB?
- Wann wurde der Mangel entdeckt und wann wurden Gewährleistungsansprüche geltend gemacht?
- Liegt Verjährung nach § 438 BGB vor?
- Hat der Verkäufer den Beweis erbracht, dass kein Mangel bei Gefahrübergang vorlag?
- Ist der Käufer Verbraucher oder Unternehmer; greift § 477 BGB überhaupt oder muss im B2B der Zustand bei Gefahrübergang voll bewiesen werden?
- Bei B2B: Gibt es Wareneingangsprotokoll, Prüfbericht, Fotos, Serien-/Chargendaten, Rüge-E-Mail und Rügezugang nach § 377 HGB?

## Beweislastlinie nach BGH vom 06.05.2026

1. Im normalen Kaufrecht muss der Käufer den Sachmangel und dessen Vorliegen bei Gefahrübergang darlegen und beweisen. Der relevante Zeitpunkt ist regelmäßig die Übergabe oder Ablieferung der Sache, nicht erst die spätere Schadensentdeckung.
2. Beim Verbrauchsgüterkauf genügt für § 477 Abs. 1 Satz 1 BGB, dass sich innerhalb eines Jahres seit Gefahrübergang eine Mangelerscheinung zeigt und als Ursache zumindest auch ein Umstand in Betracht kommt, der dem Verkäufer zuzurechnen wäre. Der Verbraucher muss also die Mangelerscheinung beweisen; dass der konkrete technische Defekt schon bei Übergabe sicher feststand, muss er gerade nicht beweisen.
3. Der BGH hat dies in den Urteilen vom 06.05.2026 - VIII ZR 73/24 und VIII ZR 257/23 klargestellt: Weitere denkbare Ursachen wie Fehlgebrauch, äußere Einwirkung oder Zufall kippen § 477 BGB nicht, solange ein Verkäuferrisiko ernsthaft möglich bleibt. Die Vermutung entfällt erst, wenn ausschließlich nicht zurechenbare Ursachen in Betracht kommen oder die Vermutung mit Art der Sache oder des Mangels unvereinbar ist.
4. Der Verkäufer muss die Vermutung voll widerlegen. Bloßes Bestreiten, technische Alternativszenarien oder der Hinweis, es könne "auch etwas anderes" gewesen sein, reichen nicht.
5. Im B2B-Kauf gilt diese Vermutung nicht. Der Unternehmerkäufer trägt die Darlegungs- und Beweislast für den Mangel bei Gefahrübergang und muss beim beiderseitigen Handelskauf zusätzlich die Untersuchung und Rüge nach § 377 HGB sauber belegen.
6. Das praktische B2B-Learning ist keine bloße Prozessfrage: Wareneingangskontrolle, QS-Protokolle, Musteraufbewahrung, Chargen-/Seriennummern, Zustandsfotos, Prüfparameter und eine nachweisbar rechtzeitige Rüge sind Rechtsvorsorge und nicht nur Aufgabe der Fachabteilung.

## Prüfraster

1. Verbrauchsgüterkauf nach § 474 BGB: Voraussetzung für § 477 BGB
2. Beweislastumkehr nach § 477 BGB: Mangelerscheinung innerhalb eines Jahres nach Gefahrübergang löst die Vermutung aus, wenn eine dem Verkäufer zurechenbare Ursache ernsthaft möglich ist
3. Widerlegung der Vermutung: Verkäufer muss beweisen, dass die Sache bei Übergabe mangelfrei war oder ausschließlich eine spätere, nicht zurechenbare Ursache vorliegt
4. Ausnahme: Beweislastumkehr passt nicht mit Art der Sache oder Art des Mangels zusammen
5. Verjährung nach § 438 Abs. 1 BGB: Regelfrist zwei Jahre, fünf Jahre bei Bauwerken, 30 Jahre bei arglistig verschwiegenem Mangel
6. Ware mit digitalen Elementen nach § 475b BGB: Updatepflichten und längere Mängelprüfung
7. Dauerhafte Bereitstellung digitaler Elemente nach § 475c BGB: Verjährung besonders berechnen
8. Verjährungsbeginn: Ablieferung der Sache
9. B2B-Abgrenzung: § 477 BGB nicht anwenden; § 377 HGB, Wareneingangskontrolle und Beweisarchiv gesondert prüfen

## Fallstricke

- § 477 BGB-Frist wurde 2022 von sechs Monaten auf ein Jahr verlängert; altes Recht nicht anwenden.
- Beweislastumkehr schlägt nicht durch, wenn Art des Mangels mit Mängel-bei-Gefahrübergang unvereinbar ist; bloße Alternativursachen reichen nach BGH vom 06.05.2026 aber nicht zur Ablehnung.
- § 477 BGB darf nicht in B2B-Fälle "hineingelesen" werden. Dort entscheidet oft die Qualität der Wareneingangsdokumentation.
- Digitale Elemente mit Updatepflicht verlängern effektiv die Mängelhaftungsphase.
- Arglistig verschwiegener Mangel: dreißigjährige Verjährungsfrist nach § 438 Abs. 3 BGB.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Anschluss-Skills

- kaufrecht-sachmangel-paragraph-434
- kaufrecht-nacherfuellung-ruecktritt-minderung
- verbrauchsgueterkauf-digitales
- kaufrecht-ware-mit-digitalen-elementen-475b

## Quellen

- https://www.gesetze-im-internet.de/bgb/__477.html
- https://www.gesetze-im-internet.de/bgb/__438.html
- https://www.gesetze-im-internet.de/bgb/__475b.html
- https://www.gesetze-im-internet.de/hgb/__377.html
- BGH, Urteile vom 06.05.2026 - VIII ZR 73/24 und VIII ZR 257/23, Pressemitteilung 077/2026: https://www.bundesgerichtshof.de/SharedDocs/Pressemitteilungen/DE/2026/2026077.html

---

## Skill: `amtlicher-bgb-auftrag-unentgeltliche`

_Amtlicher Normcheck für BGB-BT-Fälle: prüft Vertragstypen, Leistungsstörung, AGB, Verbraucherrecht, digitale Produkte, Kauf, Miete, Dienst, Werk, Auftrag, GoA, Bürgschaft, Bereicherung und Delikt gegen die aktuelle BGB-Fassung im BGB BT._

# Amtlicher BGB-BT-Normcheck

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Prüfroute

1. Vertragliche Beziehung bestimmen: Kauf, Miete, Darlehen, Dienst, Werk, Auftrag/Geschäftsbesorgung, Bürgschaft, Vergleich oder Mischvertrag.
2. Gesetzliche Beziehung bestimmen: GoA, Bereicherung, Delikt, Gesamtschuld/Regress.
3. BGB AT als Vorfrage prüfen: Vertragsschluss, Form, Stellvertretung, Anfechtung, Verjährung.
4. Aktuelle Norm live prüfen, wenn sie trägt.
5. ZPO-Durchsetzung prüfen, wenn ein Schriftsatz, Mahnbescheid, Eilantrag oder Beweisverfahren entstehen soll.

## Normlandkarte

| Bereich | Normen | Typischer Output |
| --- | --- | --- |
| Leistungsstörung | §§ 241, 249, 253, 275-304 BGB | Pflichtverletzungs- und Schadensmatrix |
| AGB | §§ 305-310 BGB | Klauselampel |
| Verbraucher/Fernabsatz | §§ 312 ff. BGB | Informations-/Widerrufscheck |
| Digitale Produkte | §§ 327 ff. BGB | Bereitstellungs- und Updateprüfung |
| Kauf | §§ 433-479 BGB | Mängelrechte, Nacherfüllung, Rücktritt, Minderung, Schadensersatz |
| Ware mit digitalen Elementen | §§ 475b, 475c, 476, 477 BGB | Update-, Beweislast- und Abweichungsvereinbarung |
| Miete/Pacht | §§ 535 ff., 581 ff. BGB | Gebrauch, Mangel, Minderung, Kündigung, § 550 BGB |
| Dienst/Behandlung | §§ 611, 611a, 630a ff. BGB | Dienstpflicht, Arbeitnehmerabgrenzung, Behandlungsvertrag |
| Werk/Bau | §§ 631 ff. BGB | Abnahme, Mängelrechte, Kündigung, Vergütung |
| Auftrag/Geschäftsbesorgung | §§ 662 ff., 675 ff. BGB | unentgeltlich/entgeltlich, Geschäftsbesorgung, Zahlungsschnittstelle |
| GoA | §§ 677-687 BGB | berechtigte/unberechtigte/unechte GoA |
| Bürgschaft | §§ 765 ff. BGB | Akzessorietät, Schriftform, Einreden |
| Bereicherung | §§ 812-822 BGB | Leistung/Nichtleistung, Rechtsgrund, Entreicherung |
| Delikt | §§ 823-853 BGB | Rechtsgut, Schutzgesetz, § 826, Verrichtungsgehilfe, Gefährdungsnähe |

## Referenz

Nutze `references/amtlicher-bgb-bt-normkern.md`.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 3 ProdHaftG
- Art. 32 DSGVO
- § 4 ProdHaftG
- § 8 ProdHaftG
- § 2 ProdHaftG
- § 1 ProdHaftG
- § 10 ProdHaftG
- § 9 ProdHaftG
- § 2 WoVermG
- Art. 82 DSGVO

### Leitentscheidungen

- BVerfGE Band 6 Rn 32 (Lüth, Drittwirkung der Grundrechte)
- BVerwG 6 C 12.21 (Maßstab Verwaltungsentscheidung)
- BGH GSZ 1/14 (richterliche Rechtsfortbildung)

---

## Skill: `dokumente-intake`

_Dokumentenintake für BGB Besonderer Teil — Prüfungsschemata: sortiert Verträge, Lieferscheine, Rechnungen, prüft Datum, Absender, Frist und Beweiswert (Urkunden, Zeugen); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO._

# Dokumentenintake

## Aktenstart statt Formularstart

Wenn zu **Dokumente Intake** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Bgb Bt Prüfer** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Einsatzlage

Dieser Dokumenten-Intake für **Bgb Bt Prüfer** ordnet Anlagen, Registerdaten, Korrespondenz, Bescheide, Fristen und Beleglücken zu einer belastbaren Arbeitsakte.

## Fachlandkarte dieses Plugins

- `amtlicher-bgb-auftrag-unentgeltliche` — Amtlicher BGB Auftrag Unentgeltliche
- `anfangercoach-schuldrecht-anspruchslandkarte` — Anfangercoach Schuldrecht Anspruchslandkarte
- `anfangercoach-schuldrecht-bt` — Anfangercoach Schuldrecht BT
- `anspruchslandkarte-vertragstypen` — Anspruchslandkarte Vertragstypen
- `arbeitsnaher-dienstvertrag-bauvertrag` — Arbeitsnaher Dienstvertrag Bauvertrag
- `arbeitsnaher-dienstvertrag-bgb` — Arbeitsnaher Dienstvertrag BGB
- `auftrag-und-unentgeltliche-taetigkeit` — Auftrag und Unentgeltliche Taetigkeit
- `bauvertrag-und-verbraucherbauvertrag` — Bauvertrag und Verbraucherbauvertrag
- `bereicherungsrecht-entreicherung-saldotheorie` — Bereicherungsrecht Entreicherung Saldotheorie
- `bereicherungsrecht-entreicherung-und-saldotheorie` — Bereicherungsrecht Entreicherung und Saldotheorie
- `bereicherungsrecht-leistungskondiktion` — Bereicherungsrecht Leistungskondiktion
- `bereicherungsrecht-nichtleistungskondiktion` — Bereicherungsrecht Nichtleistungskondiktion
- `beweislast-belegmatrix` — Beweislast Belegmatrix

## Arbeitsweg

- Eingangsdokumente nach Typ ordnen: Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets.
- Pro Dokument prüfen: Datum, Absender, Empfänger, Zustellungsnachweis, Fristwirkung, Beweiswert für die Bgb Bt Prüfer-Frage.
- Lücken, Widersprüche, fehlende Anlagen und ungeklärte Zustellungen markieren; bei Original-Beweisbedarf auf Beweissicherung achten.
- Tragende Normen vorläufig zuordnen: BGB — Endfeststellung erst nach Live-Check.
- Sensible Daten nach Berufsrecht, DSGVO und Mandatsgeheimnis behandeln; Akteneinsichts- und Herausgabepflichten gegenüber Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen prüfen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaufrecht-sachmangel-paragraph-434`

_Prüft Sachmangel § 434 BGB mit subjektiven, objektiven und Montageanforderungen, Aliud-Lieferung, Gefahrübergang, B2C-Beweislastumkehr nach § 477 BGB und B2B-Abgrenzung mit Wareneingang und § 377 HGB._

# Kaufrecht: Sachmangel § 434 BGB

## Fachkern: Kaufrecht: Sachmangel § 434 BGB
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Normanker

- § 434 BGB: Sachmangel (subjektive Anforderungen, objektive Anforderungen, Montageanforderungen)
- § 435 BGB: Rechtsmangel
- § 437 BGB: Mängelrechte
- § 438 Abs. 1 Nr. 3 BGB: regelmäßige zweijährige Verjährung der kaufrechtlichen Mängelansprüche
- § 442 BGB: Kenntnis des Käufers
- § 446 BGB: Gefahrübergang bei Übergabe
- §§ 475 und 476 BGB: Verbrauchsgüterkauf (Abweichungsverbot und -ausnahmen)
- § 477 Abs. 1 Satz 1 BGB: Vermutung beim Verbrauchsgüterkauf
- §§ 475a–475e BGB: digitale Elemente
- § 377 HGB: B2B-Untersuchungs- und Rügeobliegenheit beim beiderseitigen Handelskauf

## Intake

- Welche Beschaffenheitsvereinbarung haben die Parteien getroffen?
- Entspricht die Sache der vereinbarten und der objektiv erwarteten Beschaffenheit?
- Liegt eine Aliud-Lieferung (falsche Ware) vor?
- Bestehen Montage- oder Installationsanweisungen, die nicht befolgt wurden?
- Wann war Gefahrübergang und mit welchen Belegen lässt sich der Zustand der Sache genau zu diesem Zeitpunkt rekonstruieren?
- Bei Verbrauchsgüterkauf: liegt eine unzulässige Abweichung nach § 476 BGB vor?
- Bei Unternehmerkäufern: Wurde die Ware bei Eingang untersucht, wurden Mängel unverzüglich gerügt und ist der Zugang der Rüge belegbar?

## Prüfraster

1. Subjektive Anforderungen nach § 434 Abs. 2 Nr. 1 BGB: vereinbarte Beschaffenheit
2. Subjektive Anforderungen nach § 434 Abs. 2 Nr. 2 BGB: Eignung für vertragsgemäßen Verwendungszweck
3. Objektive Anforderungen nach § 434 Abs. 3 BGB: gewöhnliche Verwendung, übliche Beschaffenheit, Erwartungen des Käufers
4. Montageanforderungen nach § 434 Abs. 4 BGB: fehlerhafte Montage durch Verkäufer oder fehlerhafte Anleitung
5. Aliud-Lieferung: andere Ware als geschuldet = Sachmangel
6. Abweichungen beim Verbrauchsgüterkauf: § 476 BGB-Einschränkungen prüfen
7. Digitale Elemente: zusätzliche Anforderungen nach § 475b BGB
8. Kenntnis des Käufers: § 442 BGB als Ausschlussgrund

## Gefahrübergang und Beweislast

1. Der Sachmangel muss rechtlich am Gefahrübergang festgemacht werden. Späterer Ausfall, späterer Verschleiß oder spätere Beschädigung reichen nicht, wenn daraus nicht auf einen Mangel bei Übergabe geschlossen werden kann.
2. Außerhalb des Verbrauchsgüterkaufs trägt der Käufer die volle Darlegungs- und Beweislast dafür, dass die Sache bei Gefahrübergang nicht den Anforderungen des § 434 BGB entsprach. Der Prüfvermerk muss daher immer eine Belegzeile für Übergabe-/Lieferdatum, Zustand, Fotos, Prüfbericht, Seriennummer, Charge und Zeugen enthalten.
3. Beim Verbrauchsgüterkauf nach § 474 BGB greift § 477 Abs. 1 Satz 1 BGB, wenn sich innerhalb eines Jahres eine Mangelerscheinung zeigt. Nach BGH, Urteile vom 06.05.2026 - VIII ZR 73/24 und VIII ZR 257/23, genügt es, dass als Ursache zumindest auch ein dem Verkäufer zurechenbarer Umstand ernsthaft möglich bleibt. Weitere denkbare Ursachen schließen die Vermutung nicht aus.
4. Beim beiderseitigen Handelskauf ersetzt § 477 BGB keine Wareneingangskontrolle. § 377 HGB verlangt Untersuchung und unverzügliche Rüge; versäumt der Käufer dies, gilt die Ware trotz tatsächlichen Mangels grundsätzlich als genehmigt.
5. Die Regelfrist für Mängelansprüche beträgt nach § 438 Abs. 1 Nr. 3 BGB zwei Jahre. Fristberechnung, Hemmung und Neubeginn müssen getrennt von § 377 HGB geprüft werden, weil eine rechtzeitige Rüge die Verjährung nicht automatisch hemmt.

## Fallstricke

- Seit 2022: objektive Anforderungen können nur nach § 476 BGB abbedungen werden (Verbrauchsgüterkauf).
- Aliud-Lieferung ist kein eigenständiger Fall mehr, sondern Sachmangel nach § 434 BGB.
- Werbeaussagen des Herstellers können objektive Anforderungen begründen, wenn Verkäufer sie kannte.
- § 434 BGB ist seit der Schuldrechtsreform 2022 dreistufig (subjektiv, objektiv, Montage); altes Recht nicht anwenden.
- B2B-Mandanten übernehmen manchmal die B2C-Intuition aus § 477 BGB. Im Handelskauf ist das gefährlich: Ohne belastbares Wareneingangs- und Rügearchiv bleibt der Mangel bei Gefahrübergang häufig unbeweisbar.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Anschluss-Skills

- kaufvertrag-grundschema-paragraph-433
- kaufrecht-rechtsmangel-paragraph-435
- kaufrecht-nacherfuellung-ruecktritt-minderung
- kaufrecht-beweislast-verjaehrung-digitale-elemente

## Quellen

- https://www.gesetze-im-internet.de/bgb/__434.html
- https://www.gesetze-im-internet.de/bgb/__437.html
- https://www.gesetze-im-internet.de/bgb/__477.html
- https://www.gesetze-im-internet.de/hgb/__377.html
- https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32019L0771
- BGH, Urteile vom 06.05.2026 - VIII ZR 73/24 und VIII ZR 257/23, Pressemitteilung 077/2026: https://www.bundesgerichtshof.de/SharedDocs/Pressemitteilungen/DE/2026/2026077.html

---

## Skill: `kaufrecht-schadensersatz-aufwendungsersatz`

_Prüft Schadensersatz §§ 437 Nr. 3 und 280 ff. BGB sowie Aufwendungsersatz § 284 BGB beim Kaufrecht mit Schwerpunkt Sachmangel bei Gefahrübergang, § 477 BGB im B2C und § 377 HGB im B2B-Handelskauf._

# Kaufrecht: Schadensersatz und Aufwendungsersatz

## Fachkern: Kaufrecht: Schadensersatz und Aufwendungsersatz
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Normanker

- § 437 Nr. 3 BGB: Schadensersatz und Aufwendungsersatz als Käuferrecht
- § 280 Abs. 1 BGB: Schadensersatz wegen Pflichtverletzung
- § 281 BGB: Schadensersatz statt der Leistung nach Fristsetzung
- § 283 BGB: Schadensersatz bei Unmöglichkeit
- § 284 BGB: Aufwendungsersatz statt Schadensersatz
- § 311a BGB: anfängliche Unmöglichkeit
- § 249 BGB: Naturalrestitution; § 252 BGB: entgangener Gewinn
- § 434 BGB: Sachmangel
- § 438 BGB: Verjährung der Mängelansprüche
- § 446 BGB: Gefahrübergang
- § 477 BGB: Beweislastumkehr beim Verbrauchsgüterkauf
- § 377 HGB: Untersuchungs- und Rügeobliegenheit im Handelskauf

## Intake

- Liegt ein Sachmangel vor, der zum Schadensersatz berechtigt?
- Wurde eine Nachfrist gesetzt und ist sie erfolglos abgelaufen?
- Welche Schäden sind entstanden: Mangelfolgeschäden, entgangener Gewinn, nutzlose Aufwendungen?
- Kommt Aufwendungsersatz nach § 284 BGB in Betracht?
- Liegt anfängliche Unmöglichkeit oder nachträgliche Pflichtverletzung vor?
- Ist die B2C-Vermutung des § 477 BGB eröffnet oder muss der B2B-Käufer Mangel, Gefahrübergang, Kausalität und rechtzeitige Rüge selbst beweisen?

## Prüfraster

1. Pflichtverletzung: Sachmangel bei Gefahrübergang (§ 434 BGB)
2. Vertretenmüssen des Verkäufers: Verschulden nach § 276 BGB
3. Schadensersatz neben der Leistung: § 280 Abs. 1 BGB (Mangelfolgeschäden ohne Fristsetzung)
4. Schadensersatz statt der Leistung: § 281 BGB (Fristsetzung erforderlich, außer § 281 Abs. 2 BGB)
5. Kleiner vs. großer Schadensersatz: kleiner (Verbleib Sache) vs. großer (Rückgabe Sache)
6. Aufwendungsersatz nach § 284 BGB: statt Schadensersatz; vergebliche Aufwendungen im Vertrauen auf Leistungserhalt
7. Differenzhypothese für Schadensberechnung
8. Verjährung: § 438 BGB; Beweislastumkehr § 477 BGB
9. B2B-Handelskauf: § 377 HGB, Wareneingangsdokumentation und Rügezugang als Anspruchsvoraussetzungs- und Beweisrisiko prüfen

## Beweislast und Schadensaufbau

Schadensersatz wegen mangelhafter Kaufsache darf nicht mit dem Schaden beginnen. Zuerst wird belegt, dass bei Gefahrübergang ein Sachmangel vorlag. Beim Verbrauchsgüterkauf hilft § 477 Abs. 1 Satz 1 BGB: Nach BGH, Urteile vom 06.05.2026 - VIII ZR 73/24 und VIII ZR 257/23, reicht eine innerhalb eines Jahres erkennbare Mangelerscheinung, wenn eine Verkäuferursache ernsthaft möglich bleibt. Im B2B-Handelskauf gilt diese Vermutung nicht; dort müssen Wareneingang, Prüfprotokoll, Rügeinhalt, Zugang der Rüge und technischer Ursachenzusammenhang in die Schadensmatrix aufgenommen werden.

## Fallstricke

- Schadensersatz neben der Leistung und statt der Leistung müssen klar getrennt werden.
- Aufwendungsersatz nach § 284 BGB ist kein Schadensersatz; andere Voraussetzungen.
- Mangelfolgeschäden können ohne Fristsetzung geltend gemacht werden.
- § 284 BGB und § 281 BGB schließen sich gegenseitig aus (kein gleichzeitiger Antrag).
- Verkäuferalternativen wie Fehlbedienung, Transportschaden oder nachträglicher Verschleiß sind im B2C erst auf der Widerlegungsebene relevant; im B2B muss der Käufer solche Gegenargumente von Anfang an beweisfest antizipieren.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Anschluss-Skills

- kaufrecht-nacherfuellung-ruecktritt-minderung
- schadensrecht-paragraphen-249-253
- kaufrecht-sachmangel-paragraph-434
- workflow-output-gutachten-klage-brief

## Quellen

- https://www.gesetze-im-internet.de/bgb/__437.html
- https://www.gesetze-im-internet.de/bgb/__280.html
- https://www.gesetze-im-internet.de/bgb/__284.html

---

## Skill: `kaufrecht-nacherfuellung-ruecktritt-minderung`

_Prüft Nacherfüllung § 439 BGB, Rücktritt § 437 Nr. 2 BGB, Minderung, Schadensersatz, Beweislast für den Sachmangel bei Gefahrübergang und die B2C/B2B-Weiche zwischen § 477 BGB und § 377 HGB._

# Kaufrecht: Nacherfüllung, Rücktritt und Minderung

## Fachkern: Kaufrecht: Nacherfüllung, Rücktritt und Minderung
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Normanker

- § 437 BGB: Rechte des Käufers bei Sachmangel
- § 439 BGB: Nacherfüllung (Nachbesserung oder Nachlieferung)
- §§ 440 und 441 BGB: Rücktritt und Minderung
- § 323 BGB: Voraussetzungen des Rücktritts
- § 441 BGB: Minderung
- § 442 BGB: Kenntnis des Käufers vom Mangel
- § 443 BGB: Garantie
- § 438 BGB: Verjährung der Mängelansprüche
- § 446 BGB: Gefahrübergang bei Übergabe
- § 475 BGB: Verbrauchsgüterkauf
- § 477 BGB: Beweislastumkehr beim Verbrauchsgüterkauf
- § 377 HGB: Untersuchungs- und Rügeobliegenheit im Handelskauf

## Intake

- Liegt ein Sachmangel nach § 434 BGB vor?
- Wurde eine angemessene Nachfrist zur Nacherfüllung gesetzt?
- Hat der Verkäufer Nacherfüllung verweigert oder ist sie fehlgeschlagen?
- Wählt der Käufer Rücktritt oder Minderung?
- Besteht zusätzlich ein Schadensersatzanspruch?
- Ist § 477 BGB anwendbar oder handelt es sich um B2B/Handelskauf mit voller Käuferbeweislast und § 377 HGB?

## Prüfraster

1. Sachmangel nach § 434 BGB: subjektive, objektive und Montageanforderungen
2. Nacherfüllungsanspruch nach § 439 BGB: Wahl zwischen Nachbesserung und Nachlieferung
3. Fristsetzung: angemessene Frist mit Ablehnungsandrohung nach § 323 BGB
4. Unmöglichkeit oder Verweigerung der Nacherfüllung: § 440 BGB
5. Rücktritt nach §§ 437 Nr. 2 und 323 BGB: Voraussetzungen, Ausnahmen bei erheblichem Mangel
6. Minderung nach § 441 BGB: Verhältnisrechnung, Rückforderung bei bereits gezahltem Kaufpreis
7. Schadensersatz nach §§ 437 Nr. 3 und 280 BGB: neben oder statt der Leistung
8. Verjährung: § 438 BGB; Beweislastumkehr § 477 BGB
9. B2B-Handelskauf: § 477 BGB nicht anwenden; Wareneingang, Rügezugang und Zustand bei Gefahrübergang nach § 377 HGB belegen

## Beweislast vor Rechtsfolge

Vor Rücktritt, Minderung oder Schadensersatz wird immer die Beweisfrage geklärt: Bei B2C greift § 477 Abs. 1 Satz 1 BGB, wenn innerhalb eines Jahres eine Mangelerscheinung auftritt und eine Verkäuferursache ernsthaft möglich bleibt. Der BGH hat dies mit Urteilen vom 06.05.2026 - VIII ZR 73/24 und VIII ZR 257/23 bestätigt. Bei B2B trägt der Käufer dagegen die volle Last für Mangel und Gefahrübergang; der Output muss deshalb Wareneingangsprotokoll, Prüfbericht, Rügeinhalt, Rügefrist und Rügezugang abfragen.

## Fallstricke

- Rücktritt setzt erheblichen Mangel voraus (§ 323 Abs. 5 Satz 2 BGB); unerheblicher Mangel berechtigt nur zur Minderung.
- Bei Verbrauchsgüterkauf zwei Nachbesserungsversuche sind nicht gesetzlich vorgeschrieben; Einzelfallbeurteilung.
- Minderungsberechnung: Verhältnis mängelfreier Kaufpreis zum tatsächlichen Kaufpreis.
- § 442 BGB schließt Mängelansprüche aus, wenn Käufer Mangel bei Vertragsschluss kannte.
- Ohne tragfähigen Nachweis des Mangels bei Gefahrübergang sind Rücktritt und Minderung im B2B oft prozessual schwach, auch wenn der technische Defekt plausibel wirkt.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Anschluss-Skills

- kaufrecht-sachmangel-paragraph-434
- kaufrecht-gefahruebergang-und-versendung
- kaufrecht-schadensersatz-aufwendungsersatz
- bt-fristen-erklaerungen-zugang

---

## Skill: `kaufrecht-gefahruebergang-und-versendung`

_Prüft Gefahrübergang § 446 BGB, Versendungskauf § 447 BGB, Verbrauchsgüterkauf-Ausnahmen, Beweislast für den Mangel bei Übergabe und die B2B-Folge für Wareneingang und § 377 HGB._

# Kaufrecht: Gefahrübergang und Versendung

## Fachkern: Kaufrecht: Gefahrübergang und Versendung
- **Normen-/Quellenanker:** BGB Besonderer Teil: Kaufrecht, Werk-/Dienstvertrag, Auftrag/Geschäftsbesorgung, Miet-/Leasingnähe, GoA, Bereicherung, Delikt, Verjährung und AGB-Schnittstellen.
- **Entscheidende Weiche:** Anspruchsgrundlage, Vertragstyp/Mischvertrag, Pflichtverletzung, Vertretenmüssen, Schaden, Einwendung und Beweisfrage sauber trennen.
- **Arbeitsprodukt:** Liefere eine fallbezogene `Norm / Tatsache / Beleg / Wertung / Gegenargument / nächster Schritt`-Matrix und einen direkt nutzbaren Textbaustein, wenn der Nutzer einen Entwurf braucht.

## Normanker

- § 446 BGB: Gefahrübergang bei Übergabe der Sache
- § 447 BGB: Versendungskauf, Gefahrübergang bei Übergabe an Transportperson
- § 475 Abs. 2 BGB: Ausnahme beim Verbrauchsgüterkauf (Gefahrübergang erst bei Übergabe)
- § 300 Abs. 2 BGB: Gefahrübergang bei Gläubigerverzug
- §§ 243 und 244 BGB: Gattungsschuld und Konkretisierung

## Intake

- Handelt es sich um einen Versendungskauf nach § 447 BGB?
- Hat der Käufer die Versendung veranlasst oder hat der Verkäufer auf Wunsch des Käufers versandt?
- Liegt ein Verbrauchsgüterkauf vor; gilt § 475 Abs. 2 BGB?
- Ist die Sache auf dem Transportweg beschädigt oder untergegangen?
- War die Sache bereits konkretisiert (bei Gattungsschuld nach § 243 BGB)?

## Prüfraster

1. Gefahrübergang bei Übergabe nach § 446 BGB: Zeitpunkt und Ort der Übergabe
2. Versendungskauf nach § 447 BGB: Käufer hat Versendung veranlasst oder Ort ist kein Erfüllungsort
3. Gefahrübergang beim Versendungskauf: Übergabe an Transportperson, nicht beim Empfänger
4. Verbrauchsgüterkaufausnahme nach § 475 Abs. 2 BGB: Gefahrübergang erst bei Übergabe an Verbraucher
5. Gläubigerverzug: § 300 Abs. 2 BGB kann Gefahrübergang vorziehen
6. Gattungsschuld: Konkretisierung nach § 243 BGB Voraussetzung für Gefahrübergang
7. Folgen des Gefahrübergangs: Käufer trägt Gefahr des zufälligen Untergangs (Preisgefahr und Leistungsgefahr)
8. Beweislast: wer beweist den Zustand bei Gefahrübergang?

## Mangel bei Gefahrübergang als Beweisfrage

1. Der Gefahrübergang ist beim Sachmangel nicht nur ein Risikostichtag, sondern der Beweisstichtag: Der Käufer muss im Grundfall beweisen, dass die Sache gerade zu diesem Zeitpunkt mangelhaft war.
2. Beim Verbrauchsgüterkauf wirkt § 477 Abs. 1 Satz 1 BGB zugunsten des Käufers. Nach BGH, Urteile vom 06.05.2026 - VIII ZR 73/24 und VIII ZR 257/23, genügt eine innerhalb eines Jahres auftretende Mangelerscheinung, wenn zumindest auch eine dem Verkäufer zurechenbare Ursache ernsthaft möglich ist.
3. Bei B2B-Käufen greift § 477 BGB nicht. Dort muss der Unternehmerkäufer den Zustand bei Gefahrübergang mit Wareneingangsprotokoll, Fotos, Messwerten, Serien- oder Chargennummern, Zeugen und Sachverständigengutachten rekonstruieren.
4. Beim beiderseitigen Handelskauf kommt § 377 HGB hinzu: Untersuchung und Rüge sichern nicht nur Rechte, sondern liefern die ersten Beweise für den Zustand bei Gefahrübergang.

## Fallstricke

- Bei Verbrauchsgüterkauf geht Gefahr nicht auf den Verbraucher über, solange Ware nicht übergeben wurde.
- § 447 BGB gilt im Verbrauchsgüterkauf nicht zu Lasten des Käufers.
- Gefahrübergang und Eigentumsverschaffung können zeitlich auseinanderfallen.
- Gläubigerverzug des Käufers (Annahmeverzug) verschiebt Gefahrübergang nach § 300 Abs. 2 BGB.

## Stoppschilder

- Keine Kommentar-, Aufsatz- oder BeckRS/Juris-Blindzitate.
- Tragende Gesetzesstände live gegen amtliche/frei zugängliche Quellen prüfen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und überprüfbarer Quelle verwenden.
- Bei Unsicherheit die Annahme ausdrücklich markieren und eine Rückfrage oder Quellenprüfung auslösen.

## Qualitätsregeln

- § 447 BGB und § 475 Abs. 2 BGB immer im selben Atemzug prüfen.
- Gattungsschuld immer auf Konkretisierung prüfen.
- Gefahrübergang und Eigentumsverschaffung nicht verwechseln.
- B2C-Beweislastumkehr nicht in B2B-Fälle übertragen; im Handelskauf immer § 377 HGB mitprüfen.

## Anschluss-Skills

- kaufvertrag-grundschema-paragraph-433
- kaufrecht-sachmangel-paragraph-434
- kaufrecht-nacherfuellung-ruecktritt-minderung
- bt-fristen-erklaerungen-zugang

## Quellen

- https://www.gesetze-im-internet.de/bgb/__446.html
- https://www.gesetze-im-internet.de/bgb/__447.html
- https://www.gesetze-im-internet.de/bgb/__474.html

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

