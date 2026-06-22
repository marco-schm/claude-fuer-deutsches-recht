# Megaprompt: forderungsmanagement-klagewerkstatt

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 84 Skills des Plugins `forderungsmanagement-klagewerkstatt`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Dokumentengetriebene Ersttriage einer Forderungsakte: wertet zuerst Ordner, ZIP, Rechnungen, Mahnungen, Kontoauszuege, M…
2. **spezial-klagewerkstatt-erstpruefung-und-mandatsziel** — Klagewerkstatt: Erstprüfung, Rollenklärung und Mandatsziel im Plugin forderungsmanagement klagewerkstatt; schärft Rollen…
3. **klagevorlage-aus-eigenen-mustern** — Kanzlei will einmalig ihre eigenen Klagemuster in ein wiederverwendbares Plugin destillieren. Lernlauf Klagewerkstatt. P…
4. **inkasso-zahlungsklage-ersteller** — Gläubiger hat offene Forderung die er vor Gericht einklagen will. Zahlungsklage Forderungsmanagement §§ 286 ff. BGB ZPO.…
5. **forderung-gegen-verbraucher** — Forderung gegen Verbraucher: Verbraucherschutzregeln nach § 13 BGB, AGB-Kontrolle §§ 305-309 BGB, Widerrufsrecht bei Fer…
6. **anspruchsschriftsatz-bausteine** — Bausteinkatalog für eine Anspruchsbegruendung in Klage oder Schriftsatz. Liefert Vorlagen für Rubrum Antrag Tatbestand A…
7. **forderung-arzthonorar-goae** — Arzthonorar nach GOAE und GOZ einklagen: Faelligkeit § 12 GOAE mit Rechnungserteilung mit Mindestinhalten Diagnose GOAE-…
8. **forderung-gegen-gmbh-gesellschafter** — Forderung gegen GmbH-Gesellschafter persoenlich: § 13 Abs. 2 GmbHG Trennungsprinzip Haftung nur Gesellschaftsvermoegen. …
9. **forderung-gegen-insolventen-schuldner** — Forderung gegen insolventen Schuldner: Anmeldung zur Insolvenztabelle § 174 InsO binnen Anmeldefrist mit Grund und Hoehe…
10. **forderung-im-ausland-vollstrecken** — Forderung im EU-Ausland vollstrecken: Bruessel Ia VO 1215/2012 (Anerkennung ohne Exequatur), Europaeischer Vollstreckung…

---

## Skill: `kaltstart-triage`

_Dokumentengetriebene Ersttriage einer Forderungsakte: wertet zuerst Ordner, ZIP, Rechnungen, Mahnungen, Kontoauszuege, Mahnbescheid, Widerspruch oder Klageentwurf aus, bildet eine Aktenhypothese und fragt danach nur echte Luecken ab. Pinpoints ZPO 253/688 ff.; BGB 271/286/288/362/195/199; GVG 23/71._

# Kaltstart-Triage Forderungssache

Eingangsroutine für jede neue Forderungsakte. Ziel ist nicht ein Formularinterview, sondern eine belastbare Aktenhypothese mit moeglichst wenigen Rueckfragen.

## Grundsatz: Akte zuerst, Fragen danach

Wenn ein Ordner, eine ZIP-Datei oder mehrere Dokumente vorhanden sind, wird zuerst `aktenordner-schnellstart` ausgefuehrt. Aus Dateinamen, Briefkoepfen, Vollmacht, Rechnung, Mahnung, Kontoauszug, Mahnbescheid, Widerspruch, Klageentwurf und gerichtlichen Schreiben werden Mandant, Gegner, Forderungsart, Betrag, Zahlungslage, Mahnstand und Fristen rekonstruiert.

Der erste Output lautet nicht "Bitte beantworten Sie sieben Fragen", sondern:

```text
Ich sehe in der Akte vorlaeufig Folgendes:
- mutmasslicher Mandant:
- mutmasslicher Schuldner:
- Forderung / Restforderung:
- Stand Mahnung, Mahnbescheid, Klage oder Vollstreckung:
- auffaellige Risiken:
Ich frage jetzt nur noch die Punkte ab, die aus den Unterlagen nicht sicher folgen.
```

## Nur noch echte Luecken fragen

| Luecke | Frage | Nur stellen, wenn |
|---|---|---|
| Rolle unklar | "Ich vermute, du bist auf Seite [Gläubiger/Schuldner]. Stimmt das?" | Vollmacht, Briefkopf oder Anschreiben widerspruechlich |
| Ziel unklar | "Soll ich eintreiben, abwehren, vergleichen oder nur sortieren?" | kein Mandatsziel aus Mail/Anschreiben erkennbar |
| Frist unklar | "Gibt es eine Frist ausserhalb der Akte?" | gerichtliche Frist oder Verjaehrungsdruck nicht sicher |
| Zahlung unklar | "Ist nach dem letzten Kontoauszug noch etwas bezahlt worden?" | Kontoauszug endet vor aktueller Aktenlage |
| Gegner unklar | "Ist diese Anschrift noch aktuell?" | Zustellung, Umzug, HR-Auszug oder Insolvenzfund unsicher |

Mehr als drei Startfragen sind nur erlaubt, wenn Fristversaeumnis oder falsche Partei droht.

## Routing in drei Spuren

| Befund | Spur | Folgeskill |
|---|---|---|
| Akte ungeordnet oder Dokumentenlage unklar | Akteninventar | aktenordner-schnellstart oder dokumente-intake |
| Forderung schluessig, faellig, Schuldner bekannt, kein ernstliches Bestreiten | Mahnbescheid | mahnbescheid-online |
| Bestreiten wahrscheinlich oder Anspruch muss begruendet werden | Zahlungsklage | zahlungsklage-erstellen |
| Hauptforderung bezahlt, nur Kosten/Zinsen offen | Klageblocker | klagefreigabe-belegte-forderung |
| Forderung wackelig, Belege unklar, Vergleich wirtschaftlich sinnvoll | aussergerichtliche Mahnung oder Vergleich | mahnung-aussergerichtlich-stufenmodell |
| Titel liegt bereits vor | Vollstreckung | zwangsvollstreckung-überblick |

## Risikoampel Erstbewertung

| Ampel | Auslöser |
|---|---|
| gruen | Forderung dokumentiert Schuldner solvent Verjährung in weiter Ferne Zustellung gesichert |
| gelb | Belege luckenhaft Verjährung im laufenden Jahr Schuldner zahlungssaeumig |
| rot | Verjährung tritt in den naechsten sechzig Tagen ein Schuldner verzogen oder insolvent Belegstand schwach |

Rote Ampel triggert sofort Skill verjaehrung-prüfen und gegebenenfalls Mahnbescheid noch am gleichen Werktag.

## Startprodukt

Die Triage endet immer mit einem knappen Arbeitsplan:

| Punkt | Inhalt |
|---|---|
| Aktenbefund | Was liegt vor, was fehlt |
| Parteienhypothese | Mandant, Gegner, Vertreter, Anschriften, Beleg |
| Forderungsmatrix | Hauptforderung, Nebenforderung, Zinsen, Zahlungen, Rest |
| Chronologie | Vertrag, Leistung, Rechnung, Mahnung, Zahlung, Verfahren |
| Fristenampel | Verjaehrung, Widerspruch, Einspruch, gerichtliche Verfuegung |
| Naechster Skill | genau ein Hauptskill und maximal zwei Alternativen |

## Norm-Pinpoints

- ZPO 253 Abs. 2 Klage Pflichtbestandteile
- ZPO 688 ff. Mahnverfahren
- ZPO 690 Mahnbescheidsantrag
- ZPO 696 Abgabe nach Widerspruch
- ZPO 699 700 Vollstreckungsbescheid
- BGB 271 Faelligkeit
- BGB 286 Verzug
- BGB 288 Verzugszinsen
- BGB 362 Erfuellung
- BGB 195 199 Verjährung
- Paragraf 23 Nummer 1 GVG ab 2026 allgemeine Amtsgerichtsgrenze zehntausend Euro; Paragraf 23 Nummer 2a GVG hält Wohnraummietsachen streitwertunabhängig beim Amtsgericht.

## Quellen

- [ZPO 253](https://www.gesetze-im-internet.de/zpo/__253.html)
- [BGB 286](https://www.gesetze-im-internet.de/bgb/__286.html)
- [BGB 195](https://www.gesetze-im-internet.de/bgb/__195.html)
- [GVG 23](https://www.gesetze-im-internet.de/gvg/__23.html)

---

## Skill: `spezial-klagewerkstatt-erstpruefung-und-mandatsziel`

_Klagewerkstatt: Erstprüfung, Rollenklärung und Mandatsziel im Plugin forderungsmanagement klagewerkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung._

# Klagewerkstatt: Erstprüfung, Rollenklärung und Mandatsziel

## Aufgabe
Dieser Skill ist ein konkreter Fachbaustein für `forderungsmanagement-klagewerkstatt`. Ausgangspunkt ist: Klagewerkstatt für Forderungsmanagement mit Zuständigkeitsprüfung, Mahnvorlauf, Inkasso-Zahlungsklage und Anspruchs-Gatekeeper: Nur klare, fällige und belegte Forderungen werden zur Klage freigegeben.

Er führt durch **Erstprüfung, Rollenklärung und Mandatsziel** im Themenfeld **Klagewerkstatt**. Ziel ist nicht ein abstrakter Lexikontext, sondern ein belastbares Arbeitsprodukt für die nächste anwaltliche, behördliche, gerichtliche, organisatorische oder mandantenbezogene Entscheidung.


## Fachlicher Zuschnitt

- **Thema:** Klagewerkstatt.
- **Arbeitsfokus:** Erstprüfung, Rollenklärung und Mandatsziel.
- **Plugin-Rahmen:** Klagewerkstatt für Forderungsmanagement mit Zuständigkeitsprüfung, Mahnvorlauf, Inkasso-Zahlungsklage und Anspruchs-Gatekeeper: Nur klare, fällige und b....
- **Qualitätsanspruch:** Antworte nicht mit einer austauschbaren Standard-Checkliste. Nutze die Fachlogik dieses Plugins, benenne die konkret einschlägigen Normgruppen, Behörden, Register, Fristen, Dokumente oder Verfahrenshandlungen und trenne sichere Punkte von Live-Check-Bedarf.
- **Eloquenz und Nutzen:** Führe die Nutzerin oder den Nutzer wie eine erfahrene Fachperson: kurze Orientierung, präzise Rückfragen, dann ein verwertbares Produkt mit Varianten, Gegenargumenten und nächstem Handgriff.

## Kaltstart
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Klagewerkstatt** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

---

## Skill: `klagevorlage-aus-eigenen-mustern`

_Kanzlei will einmalig ihre eigenen Klagemuster in ein wiederverwendbares Plugin destillieren. Lernlauf Klagewerkstatt. Prüfraster: Eigene Muster Urteile Kommentare hochladen Extraktion einer Standardklage-Vorlage Zuständigkeitsprüfung online Sachverhalt-Dialog. Output: Klageschrift DOCX und Markdown plus Mini-Plugin ZIP für naechste Klagen ohne erneute Extraktion. Abgrenzung zu klage-aus-eigenem-skill (Nutzung des Plugins) und inkasso-zahlungsklage-ersteller._

# Klagewerkstatt — Lernlauf aus eigenen Mustern

## Zweck

Dieser Skill ist der **Lernlauf** der Klagewerkstatt. Er macht in einem Durchgang vier Dinge:

1. Aus eigenen Klagemustern, Urteilen, Kommentaren, Aufsätzen und Formatvorlagen wird eine **hauseigene generische Standardklage-Vorlage** destilliert (Markdown + DOCX, mit Platzhaltern).
2. Der Sachverhalt wird im Dialog und aus weiteren hochgeladenen Dokumenten eingesammelt und in die Vorlage gespiegelt.
3. **Online-Prüfung der Zuständigkeit** ist Pflicht: justizadressen.nrw.de und justiz.de Gerichtssuche. Streitwert → AG/LG; Beklagtenadresse → örtliche Zuständigkeit; Sondertatbestände beachten.
4. Aus den extrahierten Hausregeln wird ein **eigenes Mini-Plugin als ZIP** generiert (`klagewerkstatt-<kanzlei>.zip`), das in Claude Code direkt installierbar ist und beim nächsten Mal ohne erneute Extraktion in der hauseigenen Vorlage produziert (siehe Schwester-Skill `klage-aus-eigenem-skill`).

Memo (rechtliche Würdigung) wird **nur auf ausdrückliche Anfrage** erstellt.

## Ablauf

**Schritt 1 — Kanzlei-Profil**
Einmal abfragen und merken:

> Kanzleiname, Rechtsanwältin/Rechtsanwalt mit Anschrift, BeA-SAFE-ID, AGB-Klausel zum Gerichtsstand (sofern für Verbraucher unzulässig nach § 29c ZPO klar abgrenzen), übliche Mandantengruppe (B2B, B2C, gemischt), bevorzugte Zinsformel (Basiszins+5/+9, §§ 288 Abs. 1/2 BGB), Standard-Anlagenliste (z. B. Rechnung, Auftragsbestätigung, Mahnungen, Lieferschein, AGB).

**Schritt 2 — Materialaufnahme (Lernkorpus)**
Den Nutzer bitten, alle einschlägigen Eigenmaterialien hochzuladen oder per Pfad zu nennen:

- Eigene Klage-Muster (mind. 2, gern 5–15) als DOCX, PDF, MD, TXT.
- Urteile zur eigenen Forderungspraxis (Volltexte oder Auszüge).
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Format- und Layout-Vorlagen (Briefkopf-DOCX, Schriftarten, Nummerierung).
- Optional: typische Mahnschreiben, Verzugsbriefe, RVG-Berechnungen.

Bei Schweigen mit den im Plugin liegenden Leervorlagen unter `assets/vorlagen-leer/` arbeiten und das im Endprodukt transparent kennzeichnen.

**Schritt 3 — Extraktion der Hausregeln**
Aus dem Lernkorpus extrahieren (Zusammenfassung am Schluss dem Nutzer vorlegen):

- Aufbau der Klageschrift (Rubrum, Anträge, Begründung, Beweismittel, Anlagen, Schluss).
- Standardklauseln: Antragswortlaut, Zinsantrag, vorgerichtliche RA-Kosten als Nebenforderung, Mahnverzugsbeginn, Verzugszinsen (§§ 286, 288 BGB), Verzugsschaden (§ 280 BGB).
- Tonalität: knapp/ausführlich; aktiv/passiv; Direktanrede des Gerichts.
- Zitierweise: Pinpoint, Randnummer, jüngere BGH-Entscheidungen zuerst, deutsche Kommentartradition.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Anlagenstrategie und Anlagensigel (K1, K2, …).

**Schritt 4 — Hauseigene Standardvorlage erzeugen**
Aus den Hausregeln eine **generische Klage-Vorlage** schreiben:

- Format: Markdown (Vorlage in `assets/vorlagen-leer/standardklage.md`) und parallel DOCX (über `office/docx`-Skill). Layout aus dem mitgelieferten Briefkopf, sonst Klotzkette-Default.
- Platzhalter strikt in geschweiften Doppelklammern: `{{kanzlei.briefkopf}}`, `{{rubrum.klagepartei}}`, `{{rubrum.beklagte}}`, `{{rubrum.bevollmaechtigte}}`, `{{gericht.bezeichnung}}`, `{{gericht.adresse}}`, `{{gericht.bea_safe_id}}`, `{{streitwert.eur}}`, `{{antrag.hauptforderung}}`, `{{antrag.zinsen}}`, `{{antrag.kosten}}`, `{{sachverhalt}}`, `{{rechtliche_würdigung}}`, `{{anlagen.liste}}`, `{{ort_datum}}`, `{{unterschrift}}`.
- Standardabschnitte enthalten Hausregel-Bausteine.

**Schritt 5 — Sachverhalt einsammeln**
Strukturierte Rückfragen (alle als Liste auf einmal stellen, damit der Nutzer in einem Schwung antworten kann):

- Forderungsgrund (Kauf, Werkvertrag, Dienstvertrag, Darlehen, Miete, sonstiges) mit kurzer Vertragsbeschreibung.
- Beklagte(r): Name, Anschrift, Rechtsform, ggf. gesetzliche Vertretung; **Anschrift exakt** für die Zuständigkeitsprüfung.
- Hauptforderung in EUR, Fälligkeitsdatum, etwaige Teilzahlungen.
- Mahnungen mit Datum, Form und Inhalt; Mahnverzugseintritt.
- Vorgerichtliche RA-Kosten als Nebenforderung (Geschäftsgebühr Nr. 2300 VV RVG, Anrechnung Vorbem. 3 Abs. 4 VV RVG).
- Beweismittel: Urkunden, Zeugen, Sachverständige, Parteivernehmung, Augenschein.
- Besonderheiten: Verbrauchereigenschaft des Beklagten, AGB-Gerichtsstand, Erfüllungsort, ausländische Beteiligung (EuGVVO/Brüssel Ia VO 1215/2012).

Zusätzlich Dokumenten-Drop akzeptieren (Rechnungen, Mahnungen, Korrespondenz). Aus diesen Dokumenten Felder automatisch befüllen und die Belegung jeweils kennzeichnen.

**Schritt 6 — Zuständigkeit online prüfen (Pflicht)**

Pflichtschritt vor Auslieferung. Reihenfolge:

1. **Sachliche Zuständigkeit** rechnerisch: Streitwert bis einschließlich 10.000 EUR → Amtsgericht nach Paragraf 23 Nummer 1 GVG; über 10.000 EUR → Landgericht nach Paragraf 71 Absatz 1 GVG. Sondertatbestände beachten: Wohnraummietsachen ausschließlich und streitwertunabhängig Amtsgericht nach Paragraf 23 Nummer 2a GVG, auch bei verbundener Räumungs- und Zahlungsklage; Nachbarschaftsstreitigkeiten Amtsgericht nach Paragraf 23 Nummer 2e GVG; Familiensachen Familiengericht; Handelssachen Kammer für Handelssachen nach Paragrafen 95 und 96 GVG.
2. **Örtliche Zuständigkeit** rechtlich: allgemeiner Gerichtsstand der Beklagten (§§ 12, 13 ZPO). Erfüllungsort (§ 29 ZPO) prüfen — bei Geldschulden Sitz der Klagepartei nur bei qualifizierter Schickschuld, sonst Wohnsitz Beklagte. Verbraucher-Sondertatbestand § 29c ZPO. AGB-Gerichtsstand prüfen, aber bei Verbrauchern nach § 38 ZPO unwirksam.
3. **Online-Adressrecherche** (immer ausführen):
   - Für NRW-Anschriften: `pplx content fetch "https://www.justizadressen.nrw.de/de/justiz/suche?suchbegriff=<PLZ_oder_Ort>"` (PLZ oder Ort der Beklagten). Wenn PLZ allein nicht reicht, mit Ort nachfassen.
   - Bundesweit ergänzend: `pplx content fetch "https://www.justiz.de/onlinedienste/gerichtsverzeichnis_und_orga/index.php"` und Landes-Justizportale.
   - Treffer prüfen und Bezeichnung, Postanschrift, Telefax und — wo bekannt — die BeA-EGVP-SAFE-ID (Bundesweites elektronisches Adressverzeichnis SAFE, abrufbar in beA bzw. unter justiz.de) einsetzen. Wenn keine SAFE-ID gelistet, mit dem Hinweis "EGVP-Adresse über beA-Adressbuch (SAFE-ID) zu ergänzen" markieren.
4. Quelle und Abrufdatum stets im Output ausweisen (Anlage `Zuständigkeitsprüfung`).

**Schritt 7 — Klageschrift erzeugen**

- **Immer**: `Klage-<Beklagte>-<YYYYMMDD>.docx` (über `office/docx`) und Spiegel `Klage-<Beklagte>-<YYYYMMDD>.md`.
- Anlagenkonvolut als Liste mit K-Sigeln; Anlagenkopfbogen optional.
- **Padlet** (auf Wunsch): single-file HTML aus `assets/padlet/klage-padlet.html` mit Live-Vorschau und Pflegefeldern; speichert in `localStorage`.

**Schritt 8 — Eigenes Mini-Plugin als ZIP erzeugen**

Aus den Hausregeln und der Standardvorlage wird ein eigenes Plugin gepackt:

- Skript: `python scripts/plugin_aus_hausregeln.py --kanzlei "<Name>" --vorlage <pfad.md> --regeln <regeln.json> --ziel <ziel.zip>`.
- Inhalt des ZIP:
  - `klagewerkstatt-<slug>/.claude-plugin/plugin.json` (Name `klagewerkstatt-<slug>`, Version 0.1.0).
  - `klagewerkstatt-<slug>/skills/klage-erstellen/SKILL.md` (siehe Schwester-Skill `klage-aus-eigenem-skill` als Bauanleitung; im erzeugten Plugin lebt die Skill-Datei eigenständig).
  - `klagewerkstatt-<slug>/assets/vorlage/standardklage.md` und `.docx`.
  - `klagewerkstatt-<slug>/references/hausregeln.json`, `belegmuster.md`, `anlagenliste.md`, `zustaendigkeit-quellen.md`.
  - `klagewerkstatt-<slug>/README.md` mit Abrufhinweis und Installationsanleitung.
- ZIP-Dateiname `klagewerkstatt-<slug>.zip`. Datei dem Nutzer zum Download geben mit Installationsanweisung für Claude Code (`Customize Plugins → Install from .zip`).

**Schritt 9 — Memo (nur auf Anfrage)**

> Soll ich zusätzlich ein Kurz-Memo im Gutachtenstil mit Anspruchsgrundlagen, Beweislage und Prozessrisiken erstellen?

Bei Zustimmung: zwei Seiten, DOCX oder Markdown.

## Rechtlicher Rahmen

### Pflichtinhalte und Form der Klageschrift
- **§ 253 Abs. 2 ZPO** Klageinhalt (Parteien, Gericht, Anträge, Sachverhalt, Beweismittel).
- **§ 130 ZPO** Form der Schriftsätze; **§ 130a ZPO** elektronisches Dokument; **§ 130d ZPO** Pflicht zur elektronischen Einreichung für Rechtsanwältinnen und Rechtsanwälte (beA).
- **Paragraf 78 Absatz 1 Satz 1 ZPO** Anwaltszwang vor Landgericht und höheren Gerichten; vor dem Amtsgericht in erster Instanz kein Anwaltszwang im Umkehrschluss.
- **§ 12 RVG / Anlage 2 VV RVG**: Gebührentabelle; **Nr. 2300 VV RVG** Geschäftsgebühr; **Vorbem. 3 Abs. 4 VV RVG** Anrechnung 0,65; **Nr. 3100 VV RVG** Verfahrensgebühr.

### Sachliche Zuständigkeit
- **Paragraf 23 Nummer 1 GVG** Amtsgericht bis einschließlich 10.000 EUR.
- **Paragraf 71 Absatz 1 GVG** Landgericht über 10.000 EUR.
- **Paragraf 23 Nummer 2a GVG** Wohnraummietsachen ausschließlich und streitwertunabhängig Amtsgericht, einschließlich verbundener Räumungs- und Zahlungsklagen.

### Örtliche Zuständigkeit
- **§§ 12, 13 ZPO** allgemeiner Gerichtsstand der Beklagten.
- **§ 17 ZPO** Sitz juristischer Personen.
- **§ 29 ZPO** besonderer Gerichtsstand des Erfüllungsortes.
- **§ 29c ZPO** Verbraucherverträge (Wohnsitz Verbraucher).
- **§ 38 ZPO** Gerichtsstandsvereinbarung (zwischen Vollkaufleuten zulässig, gegenüber Verbraucher gemäß § 38 Abs. 3 ZPO eingeschränkt).
- **§ 17 ZPO** Sitz; **§ 24 ZPO** dinglicher Gerichtsstand.
- Bei grenzüberschreitenden Sachverhalten **Brüssel Ia VO (EU) 1215/2012**, insb. Art. 7 Nr. 1 lit. a und b (Erfüllungsort), Art. 17–19 (Verbrauchersachen), Art. 25 (Gerichtsstandsvereinbarung).

### Materielle Anspruchsgrundlagen (Standard)
- **§ 433 Abs. 2 BGB** Kaufpreisanspruch; **§ 631 Abs. 1 BGB** Werklohnanspruch; **§ 611a Abs. 2 BGB** Vergütungsanspruch Dienstvertrag; **§ 535 Abs. 2 BGB** Miete; **§ 488 BGB** Darlehensrückzahlung.
- **§ 286 BGB** Verzug; **§ 288 Abs. 1 BGB** Verzugszinsen 5 Prozentpunkte über Basiszins; **§ 288 Abs. 2 BGB** 9 Prozentpunkte zwischen Unternehmern für Entgeltforderung; **§ 288 Abs. 5 BGB** Verzugspauschale 40 EUR (B2B).
- **§ 280 BGB** Schadensersatz inkl. vorgerichtlicher RA-Kosten.

### Leitentscheidungen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabeformat

1. **Klageschrift** als DOCX (`Klage-<Beklagte>-<YYYYMMDD>.docx`) und Markdown-Spiegel.
2. **Anlage Zuständigkeitsprüfung** mit Online-Quellen und Abrufdatum.
3. **Hauseigenes Mini-Plugin** als ZIP (`klagewerkstatt-<slug>.zip`) mit Standardvorlage, Hausregeln und sofort installierbarem Skill `klage-erstellen`.
4. **Optional**: HTML-Padlet zur Pflege, DOCX-Anlagenkopfbogen, Memo im Gutachtenstil.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Quellenpflicht

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Übergabe

- Bei drohender Zahlungsunfähigkeit der Beklagten an Liquiditätsplanung (`liquiditaetsplanung`) zur Schnellprüfung.
- Bei einstweiligem Rechtsschutz/Mahnverfahren an `prozessrecht` (Plugin) oder das freistehende
  Plugin `zwangsvollstreckung` (`zv-mahnbescheid-online`, `zv-vollstreckungsbescheid-folge`) verweisen.
- Nach Rechtskraft des Titels an `zwangsvollstreckung` zur operativen Durchsetzung (`zv-pfueb-bank`,
  `zv-pfueb-arbeitsentgelt`, `zv-vermoegensauskunft-gv`).
- Wenn der Nutzer beim nächsten Mal nur den Sachverhalt einreichen will: Schwester-Skill `klage-aus-eigenem-skill` mit dem im Schritt 8 erzeugten Plugin verwenden.

---

<!-- AUDIT 27.05.2026 -->
## Audit-Hinweise (27.05.2026)

Drei halluzinierte Rechtsprechungsbelege wurden im Abschnitt "Leitentscheidungen" korrigiert:

| # | Fehlerhaftes AZ | Status | Korrektur |
|---|---|---|---|
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Recherchequelle: dejure.org (Abruf 27.05.2026). Frontmatter unveraendert. Kein Commit.

---

## Skill: `inkasso-zahlungsklage-ersteller`

_Gläubiger hat offene Forderung die er vor Gericht einklagen will. Zahlungsklage Forderungsmanagement §§ 286 ff. BGB ZPO. Prüfraster: Mahnvorlauf Anspruchs-Gatekeeper fällig belegt Teilzahlung Verzug Inkassokosten § 288 BGB Gerichtsortfindung §§ 12 13 29 ZPO. Output: Klage-Entwurf Zahlungsklage für klare fällige belegte Ansprüche. Abgrenzung zu zv-mahnbescheid-online (Mahnverfahren) und klagevorlage-aus-eigenen-mustern (hauseigene Muster)._

# Inkasso-Zahlungsklage-Ersteller

## Triage — kläre vor dem Einsatz

1. Liegt ein vollständiger Mahnvorlauf vor (Rechnung mit Fälligkeit, mindestens eine Mahnung mit Fristsetzung)?
2. Ist die Hauptforderung noch nicht vor Klageeinreichung vollständig bezahlt (Erfüllungskontrolle)?
3. Sind Schuldner-Anschrift und Verbraucher-/Unternehmereigenschaft geklärt (Gerichtsstand § 29c ZPO bei Verbrauchern)?
4. Welche Nebenforderungen (Mahnkosten, Verzugszinsen, Inkassokosten) sollen eingeklagt werden — sind sie belegt und verhältnismäßig?
5. Liegt eine Abtretungskette vor — ist die Aktivlegitimation des Gläubigers/Zessionars lückenlos dokumentiert?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

Paragraf 286 BGB (Verzugseintritt) — Paragraf 288 BGB (Verzugszinsen: +5 Pp. B2C, +9 Pp. B2B) — Paragraf 280 Absatz 2 BGB (Verzugsschaden) — Paragraf 249 BGB (Schadensersatz) — Paragraf 253 ZPO (Klageschrift) — Paragrafen 12, 13, 29, 29c ZPO (örtliche Zuständigkeit) — Paragraf 23 Nummer 1 GVG und Paragraf 71 Absatz 1 GVG (allgemeine Wertzuständigkeit ab 01.01.2026: Amtsgericht bis einschließlich 10.000 EUR, Landgericht darüber; Paragraf 47 EGZPO Übergangsvorschrift) — Paragraf 23 Nummer 2a GVG (Wohnraummietsachen ausschließlich Amtsgericht) — Paragraf 93 ZPO (sofortiges Anerkenntnis, Kostenfolge) — Paragraf 812 BGB (Bereicherungsrecht als Auffanganspruch)

## Basiszinssatz § 247 BGB

- Basiszinssatz zum 01.01.2026: 1,27 Prozent (unveraendert gegenueber 01.07.2025). Bundesbank-Bekanntmachung: https://www.bundesbank.de/de/presse/pressenotizen/bekanntgabe-des-basiszinssatzes-zum-1-januar-2026-basiszinssatz-bleibt-unveraendert-bei-1-27--973974
- Daraus B2C-Verzugszinssatz (§ 288 Abs. 1 BGB) 6,27 Prozent, B2B-Verzugszinssatz (§ 288 Abs. 2 BGB) 10,27 Prozent. Halbjaehrliche Pruefung am 01.01. und 01.07. erforderlich.
- Verzugspauschale § 288 Abs. 5 BGB (B2B): 40 EUR pro Vorgang.

## Aenderungen Zustaendigkeitsrecht ab 01.01.2026

Gesetz zur Änderung des Zuständigkeitsstreitwerts der Amtsgerichte (BGBl. 2025 I Nr. 318 vom 11.12.2025) hebt mit Wirkung ab 01.01.2026 an:

- Sachliche Zuständigkeit Amtsgericht von 5.000 auf 10.000 EUR für allgemeine Forderungssachen nach Paragraf 23 Nummer 1 GVG. Wohnraummietsachen bleiben davon unabhängig nach Paragraf 23 Nummer 2a GVG ausschließlich beim Amtsgericht.
- Berufungssumme § 511 Abs. 2 ZPO von 600 auf 1.000 EUR.
- Wertgrenze Nichtzulassungsbeschwerde § 26 EGZPO von 20.000 auf 25.000 EUR.
- Uebergangsvorschrift § 47 EGZPO regelt Altverfahren.

Quelle: https://www.brak.de/newsroom/news/zivilgerichtsbarkeit-hoehere-wertgrenzen-fuer-zustaendigkeit-und-rechtsmittel-ab-112026/

## Rechtsprechung

- Rechtsprechung zu Verzug und § 286 BGB live ueber https://dejure.org und https://openjur.de pruefen.
- Aktenzeichen und Datum erst nach Verifikation in den Schriftsatz uebernehmen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Dieser Skill baut aus einer Forderungsakte einen sauberen Mahn- und Klageworkflow. **Eingeklagt werden nur Ansprüche, die klar, fällig, durchsetzbar und belegt sind.** Unsichere Positionen werden nicht eingeklagt, sondern als Rückfrage oder Nichtklage-Empfehlung ausgegeben.

## Sofortregeln

1. Nicht alles einklagen, was im Forderungskonto steht — jede Position braucht Anspruchsgrundlage, Betrag, Fälligkeit, Verzug, Beleg und Einwendungskontrolle.
2. Erfüllung blockt: vor Klageeinreichung bezahlte Hauptforderung darf nicht mehr eingeklagt werden.
3. Nebenforderungen sind kein Autopilot: Mahnkosten, Verzugszinsen, Inkassokosten werden einzeln geprüft.
4. Gerichtsort vor Klage: sachliche und örtliche Zuständigkeit sind zu prüfen und zu dokumentieren.
5. Mahnung vor Eskalation: wenn kein ausreichender Mahnvorlauf vorliegt, zuerst Mahnschreiben.

## Pflichtablauf


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

### Schritt 1: Akte aufnehmen

Felder: Gläubiger, Schuldner (Verbraucher/Unternehmer), Forderungsgrund, Hauptforderung, Mahnvorlauf, Verzug, Nebenforderungen, Prozessgeschichte, Gerichtsort.

### Schritt 2: Mahnvorlauf prüfen

Mahnchronologie: Rechnung → Zahlungserinnerung → Mahnung(en) → letzte Mahnung mit Klagehinweis → Inkassoschreiben → Zahlungseingänge.

Ampelbeurteilung: grün (klar), gelb (unklar, nacharbeitbar), rot (rechtlich ungeeignet oder bereits erledigt).

### Schritt 3: Anspruchs-Gatekeeper

Prüfe je Position: Anspruchsgrundlage, Betrag, Fälligkeit, Durchsetzbarkeit, Verzug, Verschulden, Prozessrisiko, Gerichtsort.

- GRÜN → in den Klageantrag.
- GELB → Rückfrage oder Belegbedarf.
- ROT → nicht einklagen, Begründung angeben.

### Schritt 4: Gerichtsort finden

Sachlich: allgemeine Forderung bis einschließlich 10.000 EUR Amtsgericht nach Paragraf 23 Nummer 1 GVG, darüber Landgericht nach Paragraf 71 Absatz 1 GVG. Wohnraummietsachen bleiben nach Paragraf 23 Nummer 2a GVG streitwertunabhängig beim Amtsgericht. Örtlich: Paragrafen 12, 13, 29, 29c ZPO. Online-Abgleich über justiz.de oder justizadressen.nrw.de; Quelle und Abrufdatum dokumentieren.

### Schritt 5: Output bauen

1. Mahnchronologie als Tabelle.
2. Anspruchsmatrix mit Ampel.
3. Klagefreigabe (was wird eingeklagt, was nicht, warum).
4. Gerichtsortprüfung mit Quellenplatzhalter.
5. Klageentwurf nur für grüne Positionen.
6. Beleg- und Anlagenliste mit K-Sigeln.
7. Kosten-/Risiko-Hinweis zu § 93 ZPO.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Zahlungsklage gegen saumigen Schuldner | Mahnverfahren oder Klageschrift nach Schema; Template unten |
| Variante A — Schuldner gibt Ratenzahlung an | Ratenvereinbarung statt Klage; Vollstreckungstitel danach |
| Variante B — Forderung wirtschaftlich zweifelhaft Insolvenz droht | Insolvenzantrag pruefen statt Klage; Klage nur wenn Masse erwartet |
| Variante C — Mandant will Geschaeftsbeziehung erhalten | Aussergerichtliche Einigung zuerst; Klage als letztes Mittel |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template

**Inkasso-Zahlungsklage — Anspruchsmatrix**

Schuldner: [...] | Forderungsstand: [...] EUR | Stand: [Datum]

| Position | Betrag EUR | Ampel | Begründung |
|---|---|---|---|
| Hauptforderung | [...] | GRÜN/ROT | [...] |
| Verzugszinsen | [...] | GRÜN/GELB | ab [...] |
| Mahnkosten | [...] | GRÜN/GELB | Beleg: [...] |
| Inkassokosten | [...] | GRÜN/GELB | Verhältnismäßigkeit: [...] |

**Gerichtsort:** AG/LG [...] — Online-Quelle: [...] — Abrufdatum: [...]

**Klageantrag (nur grüne Positionen):**
Der Beklagte wird verurteilt, an den Kläger [...] EUR nebst Zinsen in Höhe von [...] Prozentpunkten über dem Basiszinssatz seit [...] zu zahlen.

**Empfehlung:** [Klage einreichen / zuerst Mahnung / Positionen [...] nicht einklagen]

---

Hinweis: Keine Rechtsberatung. Mechanische Prüfung anhand vom Nutzer behaupteter Tatsachen. Falsche Normwahl oder unvollständiger Sachverhalt kann das Ergebnis vollständig entwerten.

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `forderung-gegen-verbraucher`

_Forderung gegen Verbraucher: Verbraucherschutzregeln nach § 13 BGB, AGB-Kontrolle §§ 305-309 BGB, Widerrufsrecht bei Fernabsatz §§ 312g und 355 BGB, Belehrungspflicht. Verzugszinsen 5 Prozentpunkte ueber Basiszinssatz § 288 Abs. 1 BGB. Streitwert AG (bis 10000 EUR ab 01.01.2026). Gerichtsstand Wohns..._

# Forderung gegen Verbraucher

Verbraucher (§ 13 BGB) geniessen erhebliche Schutzrechte. Die Verfolgung der Forderung muss diese Schutzvorschriften beachten, sonst droht Klageabweisung oder erhebliche Aufschiebung.

## Verbraucher i.S.d. § 13 BGB

| Definition | Inhalt |
|---|---|
| Natuerliche Person | ja |
| Zwecke nicht ueberwiegend gewerblich/selbständig | ja |
| Doppelnutzung | Schwerpunkt-Prüfung; im Zweifel Verbraucher (BGH VIII ZR 7/02) |
| Vereine | grds. Verbraucher, wenn nicht gewerblich |
| Existenzgruender | nicht Verbraucher (BGH VIII ZR 219/00) |

## AGB-Kontrolle §§ 305-309 BGB

Bei vorformulierten Vertragsbedingungen gegenueber Verbraucher gilt erhoehte Kontrolle:

| Norm | Inhalt |
|---|---|
| § 305 BGB | Einbeziehung in Vertrag (Kenntnisnahme, Hinweis) |
| § 305c BGB | Ueberraschende Klauseln, Unklarheitenregel |
| § 306 BGB | Rechtsfolgen Unwirksamkeit (Vertrag im uebrigen wirksam) |
| § 307 BGB | Inhaltskontrolle (Transparenzgebot, Treu und Glauben) |
| § 308 BGB | Verbotene Klauseln mit Wertungsmoeglichkeit |
| § 309 BGB | Verbotene Klauseln ohne Wertungsmoeglichkeit |

**Beispiele unwirksamer Klauseln**:
- Pauschalierte Mahnkosten über 2,50 EUR (§ 309 Nr. 5 BGB).
- Pauschalierter Schadensersatz unangemessen (§ 309 Nr. 5 BGB).
- Aufrechnungsverbot ausser unbestrittene Forderung (§ 309 Nr. 3 BGB).
- Gerichtsstandsvereinbarung B2C im voraus (§ 38 Abs. 2 ZPO).
- Schiedsklauseln ohne Schriftform und Aufklaerung (§ 1031 Abs. 5 ZPO).

## Widerrufsrecht bei Fernabsatz und ausserhalb Geschäftsraeumen

| Vertragstyp | Norm | Widerrufsfrist |
|---|---|---|
| Fernabsatz (Online-/Telefonkauf) | §§ 312c, 312g BGB | 14 Tage § 355 BGB |
| Ausserhalb Geschäftsraeumen (Haustuer) | § 312b BGB | 14 Tage |
| Verbraucherdarlehen | § 495 BGB | 14 Tage |
| Lebensversicherung | § 8 VVG | 30 Tage |
| Versicherung Auslandsdarlehen | § 495 BGB i.V.m. RL | 30 Tage |

**Belehrungspflicht** (§ 312d, § 356 BGB i.V.m. Anlage 1 EGBGB): Muster-Widerrufsbelehrung. Bei fehlerhafter Belehrung: **Widerrufsfrist beginnt nicht** (BGH VIII ZR 19/14).

**Folge Widerruf:** Rueckabwicklung als Rueckgewaehrschuldverhaeltnis (§ 357 BGB), Frist 14 Tage je Partei.

## Verzug bei Verbraucher § 286 Abs. 3 BGB

| Konstellation | Verzugseintritt |
|---|---|
| Mahnung nach Faelligkeit | mit Zugang Mahnung (§ 286 Abs. 1 BGB) |
| Kalendermäßige Faelligkeit | mit Faelligkeit (§ 286 Abs. 2 Nr. 1 BGB) |
| 30 Tage nach Rechnungszugang | **nur mit Hinweis** in Rechnung (§ 286 Abs. 3 BGB) |

**Achtung:** Ohne Hinweis-Klausel "Bei Nichtzahlung binnen 30 Tagen treten Sie in Verzug" gilt 30-Tage-Regel nicht.

## Zinsen § 288 BGB

| Schuldner | Zinssatz |
|---|---|
| Verbraucher | 5 Prozentpunkte über Basiszinssatz (§ 288 Abs. 1 BGB) |
| Pauschale 40 EUR | gilt NICHT bei Verbraucher (nur B2B) |
| Vertragliche Höhe | nur soweit nicht sittenwidrig (§ 138 BGB), AGB-Kontrolle |

## Gerichtsstand bei Verbraucher

| Klagerichtung | Gerichtsstand |
|---|---|
| Klage gegen Verbraucher | Wohnsitz Verbraucher (§ 29c Abs. 1 S. 1 ZPO ausschließlich bei Haustuer-Geschäft / Verbraucherdarlehen) |
| Klage durch Verbraucher | sein Wohnsitz |
| Vereinbarung im voraus | nur eng zulässig § 38 Abs. 2 ZPO |
| Fernabsatz | allgemeiner Gerichtsstand Verbraucher |

EU-Bezug: Bruessel Ia Art. 17-19 – Klage gegen Verbraucher **nur am Wohnsitz Verbraucher**, ausser am Wohnsitz vereinbart und nach Entstehen Streit.

## Aufrechnungs- und Zurueckbehaltungsrechte

Verbraucher kann nach § 309 Nr. 3 BGB **nicht** durch AGB von Aufrechnungsrecht ausgeschlossen werden, ausser bei unbestrittener oder rechtskraeftiger Gegenforderung.

## Inkassokosten

| Posten | Wirksamkeit |
|---|---|
| Mahnkosten Verbraucher | wie bei B2B, aber Pauschalen begrenzt (§ 309 Nr. 5 BGB) |
| Inkassokosten | nach § 4 RDGEG max. RA-Geschäftsgebuehr |
| Vorgerichtliche RA-Kosten | nur erforderlich UND verhaeltnismaessig (BGH IX ZR 119/04) |

## Verbraucherbauvertrag § 650i BGB

Sonderregeln seit 2018:
- Schriftliche Bau-Beschreibung (§ 650j BGB).
- Verguetungssicherheit Auftragnehmer 7 Prozent (§ 650m BGB).
- Widerrufsrecht 14 Tage (§ 650l BGB).

## Verbraucherdarlehen §§ 491 ff. BGB

- Effektivzinsangabe Pflicht.
- Widerruf 14 Tage nach Vertragsschluss (§ 495 BGB).
- Bei fehlerhafter Belehrung: Widerruf zeitlich unbegrenzt (BGH XI ZR 564/15).

## Klage Strategie

1. **Rechnung prüfen**: Hinweis 30-Tage-Verzug nach § 286 Abs. 3 BGB enthalten?
2. **AGB prüfen**: Klauseln wirksam nach §§ 305 ff. BGB?
3. **Widerrufsbelehrung**: bei Fernabsatz/Haustuer korrekt? Bei Fehler: Widerruf möglich.
4. **Gerichtsstand**: Klage am Wohnsitz Verbraucher.
5. **Streitwert**: i.d.R. AG (unter 10.000 EUR).
6. **Verzugszinsen**: 5 Prozentpunkte über Basiszinssatz, KEINE 40-EUR-Pauschale.
7. **Mahn-/Inkassokosten**: nur erforderlich und verhaeltnismaessig.

## Klageantrag-Muster

```
Es wird beantragt:
1. Der/Die Beklagte wird verurteilt, an die Klaegerin EUR 1.250,80
   nebst Zinsen in Hoehe von 5 Prozentpunkten ueber dem
   Basiszinssatz aus EUR 1.250,80 seit dem 15.04.2026 zu zahlen.
2. Der/Die Beklagte traegt die Kosten des Rechtsstreits.
3. Das Urteil ist vorlaeufig vollstreckbar; dem/der Beklagten wird
   nachgelassen, die Vollstreckung durch Sicherheitsleistung in
   Hoehe von 110 % des jeweils zu vollstreckenden Betrages
   abzuwenden.
```

## Typische Fehler

- Vereinbarter Gerichtsstand bei Verbraucher → § 38 Abs. 2 ZPO unwirksam.
- Pauschale 40 EUR gegen Verbraucher beantragt – nicht zulässig.
- AGB-Pauschalen über 2,50 EUR für Mahnungen – § 309 Nr. 5 BGB.
- Widerrufsbelehrung fehlt / fehlerhaft → Widerruf noch möglich nach Klageerhebung.
- 30-Tage-Verzug ohne Hinweis in Rechnung angenommen.

## Quellen
- BGB § 13 [gesetze-im-internet.de/bgb/__13.html](https://www.gesetze-im-internet.de/bgb/__13.html)
- BGB §§ 305-310 AGB [gesetze-im-internet.de/bgb/__305.html](https://www.gesetze-im-internet.de/bgb/__305.html)
- BGB § 312g Fernabsatz [gesetze-im-internet.de/bgb/__312g.html](https://www.gesetze-im-internet.de/bgb/__312g.html)
- BGB §§ 355-357 Widerruf [gesetze-im-internet.de/bgb/__355.html](https://www.gesetze-im-internet.de/bgb/__355.html)
- BGB § 286 Abs. 3 Verbraucher [gesetze-im-internet.de/bgb/__286.html](https://www.gesetze-im-internet.de/bgb/__286.html)
- ZPO § 29c Verbrauchersache [gesetze-im-internet.de/zpo/__29c.html](https://www.gesetze-im-internet.de/zpo/__29c.html)
- ZPO § 38 Gerichtsstandsverbot Verbraucher [gesetze-im-internet.de/zpo/__38.html](https://www.gesetze-im-internet.de/zpo/__38.html)
- BGH XI ZR 564/15 zur fehlerhaften Widerrufsbelehrung [bundesgerichtshof.de](https://www.bundesgerichtshof.de)

---

## Skill: `anspruchsschriftsatz-bausteine`

_Bausteinkatalog für eine Anspruchsbegruendung in Klage oder Schriftsatz. Liefert Vorlagen für Rubrum Antrag Tatbestand Anspruchsgrund Faelligkeit Verzug Zinsen Verzugsschaden Nebenforderungen Beweis. Pinpoints ZPO 253 Abs. 2 ZPO 130 Schriftsatzform ZPO 138 substantiierter Vortrag BGB 286 288. Lie..._

# Anspruchsschriftsatz Bausteine

Jeder substantiierte Schriftsatz besteht aus etwa zwoelf Modulen. Dieser Skill haelt sie als Bausteine bereit.

## Bausteinkatalog

| Baustein | Pflichtinhalt | Norm |
|---|---|---|
| Rubrum | Bezeichnung der Parteien zustellfaehige Anschriften Prozessbevollmaechtigte | ZPO 130 Nr. 1 ZPO 253 Abs. 2 Nr. 1 |
| Streitwertangabe | Hauptforderung Nebenforderungen ohne Zinsen | GKG 39 GKG 43 |
| Antrag | bestimmter Klageantrag | ZPO 253 Abs. 2 Nr. 2 |
| Tatbestand | Zeitliche Reihenfolge wer wann was | ZPO 138 Abs. 1 |
| Anspruchsgrund Vertrag | Vertragsschluss Leistungspflicht Inhalt | BGB 145 ff |
| Anspruchsgrund gesetzlich | Tatbestandsmerkmale Norm | je Anspruch |
| Faelligkeit | Datum Faelligkeit aus Vertrag oder Gesetz | BGB 271 |
| Verzug | Mahnung oder kalendarische Bestimmung | BGB 286 Abs. 1 oder Abs. 2 |
| Zinsen | Beginn Höhe Norm | BGB 288 |
| Verzugsschaden Pauschale | 40 Euro bei B2B Hauptforderung | BGB 288 Abs. 5 |
| Mahn- und Rechtsverfolgungskosten | Datum Rechnung Belege | BGB 280 BGB 286 |
| Beweis | Zeuge Urkunde Sachverstaendiger Parteivernehmung | ZPO 373 ff |

## Muster Klageantrag

```
Die Beklagte wird verurteilt an die Klaegerin
einen Betrag von [Hauptsumme] Euro nebst Zinsen
in Hoehe von neun Prozentpunkten ueber dem
Basiszinssatz seit [Datum] sowie
vorgerichtliche Rechtsanwaltskosten in Hoehe
von [Betrag] Euro nebst Zinsen in Hoehe von
fuenf Prozentpunkten ueber dem Basiszinssatz
seit Rechtshaengigkeit zu zahlen.
```

## Muster Verzugsbegruendung

```
Die Klaegerin hat die Beklagte mit Schreiben
vom [Datum] zur Zahlung bis zum [Datum]
gemahnt. Anlage K [...]. Die Beklagte befindet
sich seit dem [Datum] in Verzug
Paragraph 286 Absatz 1 BGB.
```

## Substantiierungspflicht

ZPO 138 Abs. 1 verlangt vollstaendigen und der Wahrheit gemäß Vortrag. Pauschales Bestreiten reicht beim Beklagten nicht ZPO 138 Abs. 2. Kläger muss anspruchsbegruendende Tatsachen konkret darlegen mit Datum Ort Personen Belegen.

## Norm-Pinpoints

- ZPO 130 Schriftsatzform
- ZPO 138 Wahrheitspflicht
- ZPO 253 Klage
- ZPO 373 ff Beweismittel
- BGB 286 288

## Quellen

- [ZPO 253](https://www.gesetze-im-internet.de/zpo/__253.html)
- [ZPO 138](https://www.gesetze-im-internet.de/zpo/__138.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 3a RVG
- § 71 GVG
- § 19 GmbHG
- § 8 RVG
- § 4 RDGEG
- § 41 GKG
- § 13 GmbHG
- § 31 GmbHG
- § 9 RVG
- § 23a GVG
- § 23 RVG
- § 215 VVG

### Leitentscheidungen

- BGH II ZR 256/02
- BGH VII ZR 162/00
- EuGH C-377/17
- BGH VIII ZR 261/06
- BGH XI ZR 564/15

---

## Skill: `forderung-arzthonorar-goae`

_Arzthonorar nach GOAE und GOZ einklagen: Faelligkeit § 12 GOAE mit Rechnungserteilung mit Mindestinhalten Diagnose GOAE-Ziffer und Steigerungsfaktor Regel-Schwellenwert sowie bei Ueberschreitung mit schriftlicher Begruendung. Verjährung § 195 BGB drei Jahre. Beweislast Steigerung beim Arzt. Klage..._

# Arzthonorar nach GOAE und GOZ

Geltendmachung des Honoraranspruchs aus Behandlungsvertrag mit Privatpatient. GKV-Patienten: nicht über GOAE, sondern KV-EBM, abrechnen mit KV (anderes Skill).

## Anspruchsgrundlage

| Konstellation | Norm |
|---|---|
| Privatbehandlung Arzt | § 630a BGB Behandlungsvertrag + GOAE |
| Privatbehandlung Zahnarzt | § 630a BGB + GOZ |
| Privatbehandlung Heilberuf (Hebamme, Logo) | je nach Gebührenordnung |
| IGeL-Leistungen GKV-Patient | § 18 BMV-Ä Vereinbarung + GOAE |

## Faelligkeit § 12 GOAE

**Voraussetzungen**:
1. Erteilung einer Rechnung.
2. Rechnung muss enthalten (§ 12 Abs. 2 GOAE):
   - Datum Behandlung
   - Bezeichnung der Leistung mit GOAE-Ziffer
   - Steigerungsfaktor
   - Betrag
   - Bei Schwierigkeitsanstieg über 2,3 (Schwellenwert): **schriftliche, fall- und patientenbezogene Begruendung**.

Faelligkeit tritt **erst mit ordnungsgemaesser Rechnungserteilung** ein. Vor Erteilung kein Verzug.

**§ 10 GOZ Zahnarzt** entsprechend.

## Steigerungsfaktoren

| Bereich | Faktor | Voraussetzung |
|---|---|---|
| Regelfall (Schwellenwert) | 2,3 (1,8 für techn. Leistungen Labor) | keine Begruendung |
| Erhoehung 1,0 - 2,3 | bis 2,3 | keine schriftliche Begruendung |
| Ueberschreitung 2,3 - 3,5 | bis 3,5 | schriftliche Begruendung (Schwierigkeit, Zeitaufwand) |
| Über 3,5 (Hoechstsatz) | mehr als 3,5 | Vereinbarung im Voraus schriftlich (§ 2 GOAE) |
| Laborleistungen | 1,15 oder 1,8 | feste Saetze |

GOZ: vergleichbar mit eigenen Saetzen.

## Honorarvereinbarung § 2 GOAE / § 2 GOZ

**Pflichtform**:
1. Schriftlich.
2. Vor Beginn der Behandlung.
3. Persoenliche Vereinbarung mit Patient.
4. Hinweis auf voraussichtliche Höhe.
5. Hinweis dass GKV/PKV moeglicherweise nicht voll erstattet.

Folge Formmangel: nur Mindestsatz GOAE (1,0).

## Schadensersatz / Schlechtleistung (§ 280, § 630a BGB)

Patient kann Schadensersatz und Minderung des Honorars verlangen bei:
- Behandlungsfehler (§ 630a BGB).
- Aufklaerungspflichtverletzung (§ 630e BGB).
- Dokumentationspflichtverletzung (§ 630f BGB, Beweislastumkehr § 630h BGB).

Arzt kann dann nicht das volle Honorar verlangen, sondern muss sich Schaden anrechnen lassen.

## Rechnungsmuster GOAE-konform

```
Rechnung Nr. ... vom ...
Patient: [Name, Anschrift, GebDatum]
Versichert bei: [PKV / Beihilfe / Selbstzahler]

Datum   GOAE-Ziff.   Bezeichnung       Faktor   Betrag
15.04.  1            Beratung          2,3      EUR 10,72
15.04.  5            Symptombez.UNT    2,3      EUR 19,17
15.04.  267          EKG (Ruhe)        1,8      EUR 18,80
15.04.  35           Sonographie       2,3      EUR 38,33
                                              ---------
                                       Summe   EUR 87,02

Bei Faktor > 2,3 Begruendung: ... (falls anwendbar)
Beihilfefaehig: ja
Beleg für PKV/Beihilfe: bitte Original einreichen.
```

## Klageantrag und Streitwert

Wie reine Geldforderung. Streitwert = Hauptforderung ohne Zinsen (§ 3 ZPO i.V.m. § 4 Abs. 1 ZPO).

**Beispiel:** EUR 1.245,60 Hauptforderung → Amtsgericht (ab 01.01.2026 unter 10.000 EUR, Paragraf 23 Nummer 1 GVG), kein Anwaltszwang in erster Instanz nach Paragraf 78 Absatz 1 Satz 1 ZPO im Umkehrschluss.

## Verjährung

| Anspruch | Frist | Norm |
|---|---|---|
| Honoraranspruch Arzt | 3 Jahre | § 195 BGB |
| Beginn | Schluss des Jahres mit Faelligkeit | § 199 Abs. 1 BGB |

Verjährung beginnt **erst** mit Rechnungsstellung (Faelligkeitsausloeser § 12 GOAE). Vorsicht: Arzt darf Rechnung nicht beliebig verzoegern, sonst u.U. Treu und Glauben (§ 242 BGB).

## Datenschutz

- Im Klageantrag: nur erforderliche Diagnose offenbaren.
- Mandantenschutz § 203 StGB Schweigepflicht beachten.
- Empfehlung: Diagnose pauschal "wegen GOAE-Leistungen erbrachte aerztliche Behandlung" und Rechnung mit Diagnose-Anlage K3.

## Prüfraster Honorarklage

1. **Behandlungsvertrag** geschlossen (§ 630a BGB)?
2. **Privatpatient** oder GKV-Patient? Bei GKV: Anspruch gegen KV, nicht Patient (Ausnahme IGeL).
3. **Rechnung** ordnungsgemaess (§ 12 GOAE) erteilt → Faelligkeit.
4. **Steigerungsfaktor** rechtens, ggf. mit schriftlicher Begruendung?
5. **Vereinbarung** § 2 GOAE bei Faktor über 3,5?
6. **Verzug** durch Mahnung (§ 286 BGB) oder 30-Tage-Regel (§ 286 Abs. 3 BGB) bei Verbraucher mit Hinweis.
7. **Klagegericht** (AG/LG, oertlich Wohnsitz Patient).

## Verteidigung Patient – Standardeinwendungen

| Einwendung | Prüfung |
|---|---|
| Behandlungsfehler | § 280, § 630a BGB Schadensersatz, Minderung |
| Aufklaerungspflichtverletzung | § 630e BGB, Beweislast Arzt |
| Keine Honorarvereinbarung bei Faktor > 3,5 | § 2 GOAE → nur 3,5 max. |
| Rechnung formunzureichend | § 12 GOAE → keine Faelligkeit, keine Verzug |
| Steigerung > 2,3 ohne Begruendung | § 12 GOAE → max. 2,3 |
| Praxis-AGB unwirksam | § 305 ff. BGB |

## Quellen
- GOAE [gesetze-im-internet.de/go__1982/](https://www.gesetze-im-internet.de/go__1982/)
- GOAE § 2 Vereinbarung [gesetze-im-internet.de/go__1982/__2.html](https://www.gesetze-im-internet.de/go__1982/__2.html)
- GOAE § 12 Faelligkeit [gesetze-im-internet.de/go__1982/__12.html](https://www.gesetze-im-internet.de/go__1982/__12.html)
- GOZ Zahnarztgebuehrenordnung [gesetze-im-internet.de/goz_1987/](https://www.gesetze-im-internet.de/goz_1987/)
- BGB § 630a Behandlungsvertrag [gesetze-im-internet.de/bgb/__630a.html](https://www.gesetze-im-internet.de/bgb/__630a.html)
- BGB § 630e Aufklaerung [gesetze-im-internet.de/bgb/__630e.html](https://www.gesetze-im-internet.de/bgb/__630e.html)
- BGB § 630h Beweislast [gesetze-im-internet.de/bgb/__630h.html](https://www.gesetze-im-internet.de/bgb/__630h.html)

---

## Skill: `forderung-gegen-gmbh-gesellschafter`

_Forderung gegen GmbH-Gesellschafter persoenlich: § 13 Abs. 2 GmbHG Trennungsprinzip Haftung nur Gesellschaftsvermoegen. Durchgriff bei § 19 GmbHG (Einlagepflicht) § 31 GmbHG (verbotene Auszahlung), existenzvernichtender Eingriff BGH II ZR 256/02 (Trihotel) und BGH II ZR 3/04 (Bremer Vulkan). Outp..._

# Forderung gegen GmbH-Gesellschafter

Ausgangslage: GmbH zahlt nicht, Forderung steht. Frage: kann der Gesellschafter persoenlich in Anspruch genommen werden?

## Grundsatz Trennungsprinzip § 13 Abs. 2 GmbHG

GmbH haftet **allein mit ihrem Gesellschaftsvermoegen**. Gesellschafter haftet **nicht** persoenlich für Schulden der Gesellschaft. Das Stammkapital ist als Mindesthaftsumme (§ 5 Abs. 1 GmbHG: 25.000 EUR; UG 1 EUR).

## Ausnahmen – wann haftet der Gesellschafter doch?

### 1. § 19 GmbHG Einlagepflicht (Differenzhaftung)

Gesellschafter haftet auf Erbringung der **gezeichneten Einlage**, soweit nicht vollstaendig geleistet:
| Tatbestand | Norm | Folge |
|---|---|---|
| Ausstehende Einlage | § 19 Abs. 1 GmbHG | Anspruch GmbH auf Volleinzahlung |
| Differenz Sacheinlage / Bewertung | § 9 Abs. 1 GmbHG | Differenzhaftung in Geld |
| Verdeckte Sacheinlage | § 19 Abs. 4 GmbHG (seit MoMiG 2008) | bei Anrechnung: Wert prüfen |
| Hin- und Herzahlung | § 19 Abs. 5 GmbHG | bestehende Forderung der GmbH |

Klage: GmbH (in Insolvenz: Insolvenzverwalter) klagt gegen Gesellschafter.

### 2. § 31 GmbHG Rueckzahlung verbotener Auszahlung

| Voraussetzung | Folge |
|---|---|
| Auszahlung an Gesellschafter | Prüfung § 30 GmbHG (Stammkapital-Auszehrung) |
| Verstoss gegen Kapitalerhaltung | Rückforderungsanspruch GmbH |
| Verjährung | 10 Jahre § 31 Abs. 5 GmbHG |

Wirtschaftlicher Hintergrund: GmbH darf bei drohendem Unterschreiten des Stammkapitals nicht an Gesellschafter ausschuetten.

### 3. Existenzvernichtender Eingriff (Haftung wegen § 826 BGB)

**BGH II ZR 256/02 Trihotel** und **II ZR 3/04 Bremer Vulkan**:
- Gesellschafter haftet **deliktisch nach § 826 BGB**, wenn er der GmbH planmaessig betriebsnotwendiges Vermögen entzieht und damit die Existenz der GmbH gefaehrdet.
- Schadensersatz an die GmbH (nicht direkt an Gläubiger).
- In der Insolvenz: Anspruch des Insolvenzverwalters; ohne Insolvenz Pfaendung des Anspruchs der GmbH.

### 4. Materielle Unterkapitalisierung

BGH abgelehnt als eigenen Haftungstatbestand (BGH II ZR 256/02). Nur über § 826 BGB / existenzvernichtenden Eingriff.

### 5. Sittenwidrige vorsaetzliche Schaedigung § 826 BGB

Wenn Gesellschafter direkt den Gläubiger taeuscht (Bonitaetstaeuschung, Eingehungsbetrug). Klage des Gläubigers gegen den Gesellschafter persoenlich.

### 6. Persoenliche Buergschaft, Schuldbeitritt, Garantie

Vertraglicher Haftungsgrund, hat nichts mit GmbH-Recht zu tun. Prüfung Form (§ 766 BGB Schriftform Buergschaft, ausser kaufmaennische Buergschaft § 350 HGB).

### 7. Haftung Geschäftsführer (nicht Gesellschafter, aber oft personenidentisch)

| Anspruchsgrundlage | Norm |
|---|---|
| Steuerhaftung | § 69, § 34 AO |
| Sozialversicherungsbeitraege | § 823 Abs. 2 BGB i.V.m. § 266a StGB |
| Insolvenzverschleppung | § 823 Abs. 2 BGB i.V.m. § 15a InsO |
| Verletzung Vorsorgepflichten | § 43 GmbHG (gegenueber GmbH) |
| Drittschadensliquidation | bei Sonderverbindung Gläubiger |

### 8. Strohmanngeschaeft / Treuhand

Wenn Gesellschafter wirtschaftlich agiert und GmbH nur Mantel ist: gerichtliche Wertung "Strohmanngeschaeft", direkte Haftung. Sehr enger Anwendungsbereich.

### 9. Gesellschafterdarlehen § 39 Abs. 1 Nr. 5 InsO

In der Insolvenz nachrangig. Vorher zurueckgezahltes Gesellschafterdarlehen kann angefochten werden (§ 135 InsO 1 Jahr).

## Prüfraster Forderung gegen GmbH-Gesellschafter

| Schritt | Frage | Beweislast |
|---|---|---|
| 1 | Gegen welche Person Klage – GmbH oder Gesellschafter? | Gläubiger |
| 2 | Vertragliche Haftung Gesellschafter (Buergschaft, Beitritt)? | Gläubiger |
| 3 | Einlage vollstaendig erbracht? | GmbH/Insolvenzverwalter |
| 4 | Verbotene Auszahlung § 30, 31 GmbHG erfolgt? | Insolvenzverwalter |
| 5 | Existenzvernichtender Eingriff (§ 826 BGB)? | Gläubiger/InsVerw |
| 6 | Strohmann/Treuhand? | Gläubiger |
| 7 | Insolvenz GmbH eroeffnet → Anspruchsverlagerung an Insolvenzverwalter | nachpruefen |

## Praxisfall – Inkasso-Strategie

```
Schritt 1: HRB-Auszug Gesellschafter und Geschaeftsfuehrer
Schritt 2: Bilanz pruefen (Bundesanzeiger) -> Eigenkapitalstand
Schritt 3: Insolvenzbekanntmachungen pruefen
Schritt 4: Sofort:
   - GmbH verklagen (Hauptanspruch)
   - bei Insolvenz: § 174 InsO anmelden, an Insolvenzverwalter wenden
Schritt 5: Parallel:
   - Buergschaft/Beitritt pruefen -> Klage Gesellschafter
   - Auffaellige Auszahlungen vor Insolvenz -> Hinweis Insolvenzverwalter
Schritt 6: Bei Verdacht Insolvenzverschleppung
   - Anzeige Staatsanwaltschaft § 15a InsO
   - Schadensersatz § 823 Abs. 2 BGB GfFhr
```

## Insolvenz-Anfechtung Sondervermoegens-Verschiebungen

| Anfechtungsgrund | Norm |
|---|---|
| Vorsaetzliche Gläubigerbenachteiligung | § 133 InsO (10 J., 4 J. Verkuerzung 2017) |
| Unentgeltliche Leistung | § 134 InsO (4 J.) |
| Gesellschafterdarlehen | § 135 InsO (1 J.) |
| Inkongruente Deckung | § 131 InsO (3 Monate) |
| Kongruente Deckung | § 130 InsO (3 Monate) |

## Klageantrag-Muster gegen Gesellschafter aus Buergschaft

```
Es wird beantragt:
1. Der Beklagte wird verurteilt, an die Klaegerin EUR 12.500,00
   aus der Buergschaftsurkunde vom 03.02.2024 (Anlage K2)
   nebst Zinsen in Hoehe von 9 Prozentpunkten ueber dem
   Basiszinssatz seit dem 15.05.2026 zu zahlen.
2. Hilfsweise: Der Beklagte wird verurteilt, an die Klaegerin
   EUR 12.500,00 nebst Zinsen ... aus existenzvernichtendem
   Eingriff (§ 826 BGB) zu zahlen.
3. Der Beklagte traegt die Kosten des Rechtsstreits.
```

## Typische Fehler

- Klage gegen Gesellschafter ohne Anspruchsgrundlage neben § 13 Abs. 2 GmbHG.
- Buergschaft formunwirksam (§ 766 BGB Schriftform).
- Existenzvernichtenden Eingriff zu pauschal vorgetragen; Beweislast hoch.
- Insolvenz uebersehen; danach nur Insolvenzverwalter aktivlegitimiert für Gesellschafteranspruch.

## Quellen
- GmbHG § 13 Trennungsprinzip [gesetze-im-internet.de/gmbhg/__13.html](https://www.gesetze-im-internet.de/gmbhg/__13.html)
- GmbHG § 19 Einlage [gesetze-im-internet.de/gmbhg/__19.html](https://www.gesetze-im-internet.de/gmbhg/__19.html)
- GmbHG § 30, § 31 Kapitalerhaltung [gesetze-im-internet.de/gmbhg/__30.html](https://www.gesetze-im-internet.de/gmbhg/__30.html)
- BGB § 826 [gesetze-im-internet.de/bgb/__826.html](https://www.gesetze-im-internet.de/bgb/__826.html)
- InsO § 15a Insolvenzverschleppung [gesetze-im-internet.de/inso/__15a.html](https://www.gesetze-im-internet.de/inso/__15a.html)
- InsO §§ 129-147 Anfechtung [gesetze-im-internet.de/inso/__129.html](https://www.gesetze-im-internet.de/inso/__129.html)
- BGH II ZR 256/02 Trihotel [bundesgerichtshof.de](https://www.bundesgerichtshof.de)
- BGH II ZR 3/04 Bremer Vulkan [bundesgerichtshof.de](https://www.bundesgerichtshof.de)

---

## Skill: `forderung-gegen-insolventen-schuldner`

_Forderung gegen insolventen Schuldner: Anmeldung zur Insolvenztabelle § 174 InsO binnen Anmeldefrist mit Grund und Hoehe. Aussonderung § 47 InsO. Absonderungsrecht §§ 49-52 InsO. Massenforderung § 55 InsO. Nachrangige § 39 InsO. Vollstreckungsverbot § 89 InsO. Output: Forderungsanmeldung formgere..._

# Forderung gegen insolventen Schuldner

Wenn über das Vermögen des Schuldners ein Insolvenzverfahren eroeffnet ist, gelten ausschließlich die Regeln der InsO. Klage und Vollstreckung sind grundsätzlich gesperrt.

## Insolvenzeroeffnung – Wirkungen

| Wirkung | Norm |
|---|---|
| Verwaltungs-/Verfuegungsbefugnis geht auf Verwalter über | § 80 InsO |
| Anhaengige Prozesse werden unterbrochen | § 240 ZPO |
| Vollstreckung unzulaessig | § 89 InsO |
| Sicherungen 1 Monat vor Eroeffnung unwirksam | § 88 InsO |
| Aufrechnung beschraenkt | §§ 94-96 InsO |

## Schritt 1: Insolvenzeroeffnung erkennen

[insolvenzbekanntmachungen.de](https://www.insolvenzbekanntmachungen.de) – kostenlose amtliche Insolvenzbekanntmachung, durchsuchbar nach Namen, Sitz, Aktenzeichen.

Bei Eroeffnungsbeschluss: Verwalter benannt, Anmeldefrist gesetzt (typisch 6-8 Wochen), Prüfungstermin festgelegt.

## Schritt 2: Forderungsanmeldung § 174 InsO

**Inhalt** (§ 174 Abs. 2 InsO):
| Pflichtangabe | Inhalt |
|---|---|
| Gläubigeranschrift | mit Bankverbindung |
| Forderungsgrund | Vertrag, Datum, Vertragstyp |
| Forderungsbetrag | Hauptforderung in EUR |
| Zinsen | bis Insolvenzeroeffnung |
| Belege | Vertrag, Rechnungen, Mahnungen, Titel |
| Rang | normal, nachrangig, vorrangig |
| Bei Vorzugsrecht | Anmeldung mit Hinweis Sicherungsrecht (§ 174 Abs. 3) |

**Frist:** Anmeldefrist im Eroeffnungsbeschluss. Verspaetete Anmeldung möglich (§ 177 InsO), aber **erhebliche Nachteile**:
- Später Prüfungstermin → Kosten § 187 InsO.
- Schlussverteilung schon ausgekehrt → kein Anteil mehr.

## Anmeldungs-Formular Muster

```
An den Insolvenzverwalter
[Name, Anschrift]
Az. ... AG [Insolvenzgericht] ... IN ...

Schuldner:           [Firma/Name]
Glaeubiger:          [Firma/Name, Anschrift]
Bankverbindung:      IBAN ...

Forderungsanmeldung gemaess § 174 InsO

Hauptforderung:      EUR ...
Verzugszinsen bis Eroeffnung am ... :   EUR ...
Kosten Mahnverfahren:                    EUR ...
Anwaltskosten vorgerichtlich (1,3 GG):  EUR ...
==================================================
Gesamtforderung:                          EUR ...

Forderungsgrund:
Werklohn aus Werkvertrag vom 15.03.2024 ueber Errichtung
Carport. Abnahme am 30.04.2024, Schlussrechnung Nr. R-2024-115
vom 02.05.2024 ueber EUR ... brutto. Verzug ab 01.06.2024
nach Mahnung vom 25.05.2024 (Anlage 4).

Belege:
Anlage 1: Werkvertrag
Anlage 2: Abnahmeprotokoll
Anlage 3: Schlussrechnung
Anlage 4: Mahnung mit Zustellnachweis
Anlage 5: Vollstreckungsbescheid vom 12.10.2025 (sofern vorhanden)

Rang: einfache Insolvenzforderung (§ 38 InsO).

Es wird beantragt, die Forderung zur Tabelle festzustellen.
```

## Forderungs-Raenge

| Rang | Inhalt | Norm |
|---|---|---|
| Massenforderung | nach Eroeffnung begruendet | § 55 InsO |
| Aussonderungsrecht | Eigentum, Anwartschaft | § 47 InsO |
| Absonderungsrecht | Pfandrecht, Sicherheit | §§ 49-52 InsO |
| Einfache Insolvenzforderung | Regelfall | § 38 InsO |
| Nachrangig | Zinsen ab Eroeffnung, Gesellschafterdarlehen | § 39 InsO |
| Ausgeschlossen | bestimmte Sanktionen | § 39 Abs. 1 Nr. 3-5 InsO |

## Aussonderung § 47 InsO

Anspruch auf Herausgabe gehoert nicht zur Masse. Voraussetzung: **dingliches Recht**:
- Eigentum (z.B. nicht gelieferte Sache, Mietgegenstand).
- Eigentumsvorbehalt § 449 BGB.
- Sicherungseigentum (Mobiliar zur Sicherheit uebereignet) – aber Verwertungsrecht des Verwalters § 51 Nr. 1 InsO!

## Absonderung §§ 49-52 InsO

| Sicherungsrecht | Norm |
|---|---|
| Grundpfandrecht | § 49 InsO |
| Pfandrecht (Vermieterpfandrecht, Werkunternehmerpfandrecht) | § 50 InsO |
| Sicherungseigentum, Sicherungsabtretung | § 51 Nr. 1 InsO |
| Forderungspfaendung vor Eroeffnung | § 50 InsO i.V.m. § 804 ZPO |

Folge: Verwalter verwertet, Gläubiger bekommt Erloes (abzgl. Verwertungskostenpauschale § 170, § 171 InsO: 4 % + 5 %).

## Forderung gegen Verbraucher (Verbraucherinsolvenz)

| Phase | Frist |
|---|---|
| Aussergerichtlicher Einigungsversuch | vor Antrag § 305 Abs. 1 Nr. 1 InsO |
| Insolvenzantrag | nach Scheitern |
| Wohlverhaltensphase | 3 Jahre (RegInsO 2020) |
| Restschuldbefreiung | § 286 ff. InsO |

Forderung wird Insolvenzforderung. Nach Restschuldbefreiung erlischt der Anspruch (Naturalobligation).

## Klage waehrend Insolvenz?

| Konstellation | Klage zulässig? |
|---|---|
| Vor Eroeffnung anhaengige Klage | unterbrochen § 240 ZPO, Aufnahme durch Verwalter |
| Nach Anmeldung Forderung im Prüfungstermin bestritten | Klage auf Feststellung § 180 InsO |
| Klage gegen Insolvenzverwalter persoenlich | nur Schadensersatz § 60 InsO |
| Klage gegen Schuldner persoenlich nach Aufhebung | wieder zulässig |
| Gegen Gesellschafter (parallel) | bleibt zulässig (siehe Skill GmbH-Gesellschafter) |

## Bestrittene Forderung – Feststellungsklage § 180 InsO

Wenn Verwalter / anderer Gläubiger im Prüfungstermin die Forderung bestreitet:
- Klage gegen den Bestreitenden auf Feststellung zur Tabelle.
- Zuständigkeit: ordentliches Gericht (idR AG/LG am Insolvenzgericht).
- Streitwert: bei zu erwartender Quote (haeufig nur Bruchteil der Forderung).

## Anfechtung durch Verwalter §§ 129-147 InsO

Verwalter kann zurueckgezahlte Forderungen anfechten:
| Anfechtungsgrund | Frist vor Eroeffnung |
|---|---|
| § 130 InsO kongruente Deckung | 3 Monate |
| § 131 InsO inkongruente Deckung | 3 Monate |
| § 132 InsO unmittelbar nachteiliges Rechtsgeschaeft | 3 Monate |
| § 133 InsO vorsaetzliche Benachteiligung | 4 Jahre (seit 2017) |
| § 134 InsO unentgeltliche Leistung | 4 Jahre |
| § 135 InsO Gesellschafterdarlehen | 1 Jahr |

## Strategie-Check

```
1. insolvenzbekanntmachungen.de pruefen
2. Eroeffnungsbeschluss anfordern (Geschaeftsstelle)
3. Frist Anmeldung notieren
4. Belege zusammenstellen (Vertrag, Rechnung, Mahnung, Titel)
5. Anmeldung absenden (Original + Kopie an Verwalter, Az. notieren)
6. Pruefungstermin abwarten
7. Bei Bestreiten: Feststellungsklage erwaegen
8. Parallel: Sicherheiten verwerten / Aussonderung beantragen
9. Quotenerwartung kalkulieren (oft 0-5 %)
```

## Typische Fehler

- Klage gegen den insolventen Schuldner waehrend Insolvenz → § 87 InsO unzulaessig.
- Vollstreckung trotz Eroeffnung → § 89 InsO Verbot.
- Anmeldung ohne Belege → Aufforderung Nachreichung, Fristverlust.
- Verzugszinsen nach Eroeffnung weiter berechnet → § 39 Abs. 1 Nr. 1 InsO nachrangig.
- Sicherungsrecht nicht angemeldet → kein Absonderungsrecht.

## Quellen
- InsO § 38 [gesetze-im-internet.de/inso/__38.html](https://www.gesetze-im-internet.de/inso/__38.html)
- InsO § 39 Nachrang [gesetze-im-internet.de/inso/__39.html](https://www.gesetze-im-internet.de/inso/__39.html)
- InsO § 47 Aussonderung [gesetze-im-internet.de/inso/__47.html](https://www.gesetze-im-internet.de/inso/__47.html)
- InsO §§ 49-52 Absonderung [gesetze-im-internet.de/inso/__49.html](https://www.gesetze-im-internet.de/inso/__49.html)
- InsO § 89 Vollstreckungsverbot [gesetze-im-internet.de/inso/__89.html](https://www.gesetze-im-internet.de/inso/__89.html)
- InsO § 174 Anmeldung [gesetze-im-internet.de/inso/__174.html](https://www.gesetze-im-internet.de/inso/__174.html)
- InsO § 180 Feststellungsklage [gesetze-im-internet.de/inso/__180.html](https://www.gesetze-im-internet.de/inso/__180.html)
- Insolvenzbekanntmachungen [insolvenzbekanntmachungen.de](https://www.insolvenzbekanntmachungen.de)

---

## Skill: `forderung-im-ausland-vollstrecken`

_Forderung im EU-Ausland vollstrecken: Bruessel Ia VO 1215/2012 (Anerkennung ohne Exequatur), Europaeischer Vollstreckungstitel EuVTVO 805/2004, Europaeischer Zahlungsbefehl EuMVVO 1896/2006, geringfuegige Forderung EuGFVO 861/2007. Drittstaat: Anerkennung nach IPR und bilateralen Abkommen. Output..._

# Forderung im Ausland vollstrecken

Grenzueberschreitende Forderungsdurchsetzung. Die Wahl des Instruments haengt vom Wohnsitz des Schuldners und vom Streitwert ab.

## Instrumenten-Übersicht

| Instrument | Anwendungsbereich | Vorteil |
|---|---|---|
| Bruessel Ia VO (EU 1215/2012) | EU-Anerkennung deutscher Titel | Vollstreckung ohne Exequatur |
| EuVTVO (EG 805/2004) | unbestrittene Forderungen | Bestaetigung als EU-Titel |
| EuMVVO (EG 1896/2006) | grenzueberschreitendes Mahnverfahren | EU-weit ein einheitlich Verfahren |
| EuGFVO (EG 861/2007) | bis 5.000 EUR | vereinfachtes EU-Verfahren |
| Lugano-Uebereinkommen | CH, NO, IS | parallel zu Bruessel Ia |
| Drittstaaten | je Staat | Anerkennungsverfahren noetig |

## Bruessel Ia VO (EU 1215/2012)

**Anwendungsbereich:** Zivil- und Handelssachen mit Bezug zu mehreren MS. Nicht: Familie, Erbe, Insolvenz, Schiedsverfahren, Sozialversicherung, Steuer (Art. 1 Abs. 2).

**Gerichtsstaende (kuerz)**:
| Konstellation | Norm |
|---|---|
| Allgemein: Wohnsitz Bekl. | Art. 4 |
| Vertrag: Erfuellungsort | Art. 7 Nr. 1 |
| Deliktischer Ort: Tatort | Art. 7 Nr. 2 |
| Verbrauchersache | Art. 17-19 |
| Versicherung | Art. 10-16 |
| Arbeitsvertrag | Art. 20-23 |
| Ausschließlich (Grundstueck, Register) | Art. 24 |
| Vereinbarung | Art. 25 (Schriftform, Exklusivitaet) |

**Vollstreckung in anderem MS** (Art. 36-44):
- Anerkennung **automatisch** (kein Exequatur).
- Bestaetigung Formblatt I (Anhang I VO).
- Direktvollstreckung beim ausländischen Vollstreckungsorgan.
- Versagungsgruende beschraenkt (Art. 45): ordre public, Saeumnis ohne ordn. Zustellung, unvereinbares Urteil.

## EuVTVO (EG 805/2004) – Europaeischer Vollstreckungstitel

Bestaetigung **unbestrittener** Forderungen als EU-Titel. Voraussetzungen Art. 6:
1. Forderung im Urspr.-MS unbestritten (Anerkenntnis, Saeumnis, Vergleich).
2. Im Urspr.-MS gerichtlich tituliert.
3. Mindeststandards Zustellung eingehalten.
4. Verbraucher-Schutz beachtet.

Bestaetigung durch Urspr.-Gericht, Formblatt I. In ZielMS direkt vollstreckbar.

## EuMVVO (EG 1896/2006) – Europaeisches Mahnverfahren

| Charakteristikum | Inhalt |
|---|---|
| Antragsformular | Formblatt A |
| Zustaendiges Gericht DE | AG Wedding (Berlin) |
| Online-Antrag möglich | www.online-mahnantrag.de |
| Verteidigungsfrist Bekl. | 30 Tage nach Zustellung |
| Bei Einspruch | Uebergang ins streitige Verfahren (Prüfung Art. 17 EuMVVO) |
| Bei keinem Einspruch | Vollstreckbarerklaerung Formblatt G |
| Vollstreckungsorgan | im Wohnsitz-MS Schuldner |

## EuGFVO (EG 861/2007) – Geringfuegigkeitsverfahren

| Grenzwert | bis 5.000 EUR (ohne Zinsen/Kosten) |
|---|---|
| Antragsformular | Formblatt A |
| Schriftliches Verfahren | keine muendliche Verhandlung ueblich |
| Frist Bekl. für Stellungnahme | 30 Tage |
| Urteil | innerhalb von 30 Tagen nach Stellungnahme |
| Vollstreckung | im anderen MS direkt, Formblatt D |

## Lugano-Uebereinkommen 2007 (CH, NO, IS)

Parallel zu Bruessel Ia, aber alte Fassung mit Exequatur (Vollstreckbarerklaerung im ZielMS noetig). Voraussetzung Anerkennung: rechtskraeftiger Titel im Urspr.-Staat.

## Drittstaaten (ausserhalb EU/Lugano)

| Sachverhalt | Vorgehen |
|---|---|
| Anerkennung deutsches Urteil | §§ 328 ZPO Anerkennung in DE; Anerkennung in Drittstaat nach dort. IPR |
| Bilaterales Abkommen | Verträge z.B. mit Tunesien, Israel, T?rkei (Anerkennungsabkommen) |
| Kein Abkommen | erneute Klage im Drittstaat ueblich |
| Schiedsspruch | New York Convention 1958 (NYÜ) – sehr leistungsfaehig |

## Verfahrensweg-Prüfung Schritt für Schritt

```
1. Schuldner-Sitz ermitteln
   -> EU? Lugano? Drittstaat?

2. Streitwert pruefen
   -> bis 5.000 EUR -> EuGFVO bevorzugen
   -> mehr -> Bruessel Ia oder EuVTVO

3. Forderung unbestritten?
   -> ja  -> EuVTVO Bestaetigung
   -> nein -> EuMVVO (Mahnverfahren) oder Klage Bruessel Ia

4. Forderung bereits tituliert in DE?
   -> Bruessel Ia Direktvollstreckung (Art. 36-44)
   -> EuVTVO Bestaetigung als alternativer Pfad

5. Schuldner reagiert nicht
   -> Vollstreckung mit Formblatt I (Bruessel Ia)
   -> oder Formblatt G (EuMVVO)

6. Schuldner widerspricht
   -> Klage im DE-Inland nach Gerichtsstand Bruessel Ia
   -> oder EuGFVO falls Grenzwert
```

## Form der Zustellung im Ausland

**HZUe 1965** (Haager Zustellungsuebereinkommen) – für Drittstaaten.
**EuZustVO (EU 2020/1784)** seit 01.07.2022 – innerhalb EU:
- Direkte Zustellung Justizbehoerde zu Justizbehoerde.
- Postzustellung mit Einschreiben möglich (Art. 18).
- Diplomatischer Weg (Konsulat) bei Bedarf.
- Übersetzung in Amtssprache des ZielMS.

## Beweismittel im EU-Ausland

| Instrument | Inhalt |
|---|---|
| EuBVO (EU 1206/2001) → Neu: VO 2020/1783 | Beweiserhebung |
| Videokonferenz nach EuBVO | Art. 17 ff. |

## Kosten

| Verfahren | Gerichtskosten |
|---|---|
| EuMVVO | 0,5 nach KV 1100 GKG |
| EuGFVO | wie nationaler kleiner Klageweg |
| Bruessel Ia Vollstreckung | im ZielMS nach dortigem Tarif |
| Anerkennung Drittstaat | Anwalts- und Gerichtskosten lokal |

## Typische Fehler

- Klage in DE gegen Bekl. mit Wohnsitz EU ohne Prüfung Bruessel Ia → ggf. unzuständig.
- EuMVVO bei strittiger Forderung – Widerspruch fuehrt in nationale Klage des Bekl.-MS.
- Übersetzung vergessen → Zustellung schlaegt fehl.
- Schiedsklausel ueberhaupt nicht gepruef → New York Convention besserer Pfad.
- Lugano mit Bruessel verwechselt – Exequatur in CH noch noetig.

## Quellen
- Bruessel Ia VO 1215/2012 [eur-lex.europa.eu/eli/reg/2012/1215](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32012R1215)
- EuVTVO 805/2004 [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32004R0805)
- EuMVVO 1896/2006 [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32006R1896)
- EuGFVO 861/2007 [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32007R0861)
- EuZustVO 2020/1784 [eur-lex.europa.eu](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32020R1784)
- HZUe 1965 [hcch.net](https://www.hcch.net/en/instruments/conventions/full-text/?cid=17)
- New York Convention 1958 [newyorkconvention.org](https://www.newyorkconvention.org/)

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

