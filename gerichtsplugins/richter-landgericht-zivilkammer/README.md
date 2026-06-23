# Zivilkammer am Landgericht

<!-- BEGIN direkt-loslegen (autogen) -->
## Direkt loslegen ohne Plugin-Setup

Wer kein Plugin-Setup nutzen kann oder will, bekommt trotzdem eine sofort nutzbare Werkzeugkiste. Eine Markdown-Datei reicht: herunterladen, in das eigene Chat-System ziehen, Frage stellen. Die Werkstatt-Datei ist die ausführliche Variante; die Schnellstart-Datei ist die kompakte Variante für den schnellen Einstieg. Plugin und Testakte liegen als ZIP daneben.

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Großer Prompt (Werkstatt) | Markdown | [`richter-landgericht-zivilkammer-werkstatt.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-landgericht-zivilkammer/richter-landgericht-zivilkammer-werkstatt.md) |
| Kleiner Prompt (Schnellstart, höchstens 7500 Zeichen) | Markdown | [`richter-landgericht-zivilkammer-schnellstart.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/richter-landgericht-zivilkammer/richter-landgericht-zivilkammer-schnellstart.md) |
| Plugin als Komplett-ZIP | ZIP | [`richter-landgericht-zivilkammer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-landgericht-zivilkammer.zip) |
| Testakte(n) als ZIP | ZIP | [`richter-landgericht-zivilkammer-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-landgericht-zivilkammer-testakte.zip) |
<!-- END direkt-loslegen (autogen) -->

> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 8 Buchstabe a der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die richterliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".

## Rolle

Vorsitzender oder Berichterstatter einer Zivilkammer (Paragraf 71 GVG, Streitwert ab 10.001 Euro; auch sonstige Zuständigkeiten Paragrafen 71-74 GVG) sowie zweite Instanz Berufung Paragraf 511 ZPO

## Rechtsrahmen

ZPO, BGB, HGB, GVG, GKG, RVG, EGZPO

## Inhalt

- **11 Skills** (siehe `skills/`; inklusive Schnellstart-Skill)
- **Werkstatt-Prompt** (`richter-landgericht-zivilkammer-werkstatt.md`)
- **Schnellstart-Prompt** (`richter-landgericht-zivilkammer-schnellstart.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-eingang-und-besetzung** — Eingangsprüfung Paragraf 522 ZPO bei Berufung, sachliche Zuständigkeit Paragraf 71 GVG (Erste Instanz) und Paragraf 11
- **02-grosse-relation-zivilrecht** — Vollständige zivilrechtliche Relation: Schluessigkeitsprüfung (Klägerstation), Erheblichkeitsprüfung (Beklagtenstati
- **03-fruehe-erste-verfuegung-paragraf-139** — Hinweisverfuegung Paragraf 139 ZPO: Hinweise auf rechtliche Bedenken, Auflagen zur Substantiierung, Ergaenzung des Vortr
- **04-beweisbeschluss-und-sachverstaendiger** — Beweisbeschluss Paragrafen 358-360 ZPO: Beweisthema, Beweismittel, Auswahl des Sachverständigen, Sachverständigenfrage
- **05-zeugenbeweis-und-parteivernehmung** — Zeugenbeweis Paragrafen 373-401 ZPO, Beweisaufnahme im Termin, Belehrung, Glaubhaftigkeit, Parteivernehmung Paragrafen 4
- **06-urteil-grosses-zivilurteil** — Urteilsentwurf nach Paragraf 313 ZPO bei groesserem Streitwert: ausfuehrlicher Tatbestand, gegliederte Entscheidungsgrue
- **07-berufungsverfahren-paragraf-511-ff** — Berufungsverfahren: Zulässigkeit Paragraf 511, Berufungsbegründung Paragraf 520, Prüfungsumfang Paragraf 529, Zurück
- **08-kostenentscheidung-und-streitwert** — Kostenentscheidung Paragrafen 91-101 ZPO, Streitwertfestsetzung Paragrafen 39-51 GKG, Streitwertbeschluss, Änderung der
- **09-vergleich-und-mediation** — Vergleichsgespraech leiten Paragraf 278 ZPO, Mediation Paragraf 278a ZPO, Prozessvergleich Paragraf 794 Abs. 1 Nr. 1, Vo
- **10-entscheidungsvorschlag-kammer** — Strukturierter Entscheidungsvorschlag für die Kammerberatung: Tenor-Vorschlag, tragende Gründe, Beweiswürdigung, Hilf

## Wichtiger Hinweis vor Verwendung

**Experimentelles Plugin — Vorsicht.** Dieses Plugin ist ein Funktionsexperiment für den Einsatz von KI an deutschen Gerichten. Es geht hier um die **Capability**, nicht um eine Produktivempfehlung.

### Rechtliche Einordnung der KI-Verordnung (KI-VO, VO (EU) 2024/1689)

- **Art. 6 Abs. 2 i.V.m. Anhang III Nr. 8 lit. a KI-VO**: KI-Systeme, die von einer Justizbehoerde oder in deren Auftrag bei der **Recherche und Auslegung von Sachverhalten und Rechtsvorschriften** sowie bei der **Anwendung des Rechts auf konkrete Sachverhalte** verwendet werden, sind grundsaetzlich **Hochrisiko-KI**.
- **Aber Art. 6 Abs. 3 KI-VO**: Ein KI-System gilt **nicht** als Hochrisiko-KI, wenn es nur eine **vorbereitende Aufgabe** wahrnimmt (z.B. Vorbereitung von Dokumenten, reine Recherche ohne Subsumtion).
- **Notifizierungspflicht**: Auch im Ausnahmefall des Art. 6 Abs. 3 ist der Anbieter bzw. Betreiber verpflichtet, das KI-System bei der zuständigen Aufsicht zu **registrieren** (Art. 49 Abs. 2 KI-VO).
- Die Einordnung ist im Einzelfall zu prüfen. Sobald das System konkrete Entscheidungsvorschlaege produziert, die Subsumtion vornimmt oder die richterliche Würdigung ersetzt, wird die Schwelle zur Hochrisiko-KI überschritten.

### Art. 22 DSGVO — Verbot ausschliesslich automatisierter Entscheidung

Die richterliche Letztentscheidung muss zwingend bei einem Menschen liegen. **Keine Maschine entscheidet als Richter.** Diese Skills sind ausschliesslich **Unterstuetzung** der richterlichen Arbeit, niemals deren Ersatz. Der Richter prüft, gewichtet, entscheidet — die KI bereitet vor und macht Vorschlaege.

### Aktengeheimnis und Datenschutz

- **Paragraf 353b StGB** (Verletzung von Dienstgeheimnissen) und **Paragraf 43 DRiG** (Amtsverschwiegenheit der Richter) sind strikt zu wahren.
- Akteninhalte duerfen nicht ungeprüfte an externe KI-Anbieter übermittelt werden. Vor jeder Verwendung ist zu prüfen, ob die genutzte KI-Umgebung den Datenschutz und das Aktengeheimnis gewaehrleistet.
- **Schatten-KI ist ausdrücklich abgelehnt.** Dieses Plugin soll keine Hilfe sein, KI an behoerdlichen Datenschutz- und IT-Richtlinien vorbei einzusetzen.

### Revisionssicherheit

- Saemtliche Arbeitsergebnisse müssen revisionssicher dokumentiert werden: Wer hat wann welche KI-Ausgabe genutzt, welche Änderungen wurden danach durch den Richter vorgenommen, welche Akten- und Promptbestandteile lagen zugrunde?
- Die KI-Ausgabe muss als KI-Ausgabe erkennbar bleiben (Markierung, Versionierung); die richterliche Bearbeitung dokumentiert werden.
- Aufbewahrungsfristen nach Aktenordnung der Gerichte und ggf. KI-VO-Logging-Pflichten beachten.

### Realismus-Hinweis

Viele Gerichte werden externe Cloud-Dienste auf absehbare Zeit nicht produktiv einsetzen können. Der Wert dieses Plugins liegt darin, dass **Werkstatt-Prompt und Schnellstart-Prompt portabel** sind: Sie funktionieren in einem behördlich freigegebenen Fachsystem mit ausreichendem Kontextfenster und Datei-Upload. Wer im Gericht bereits eine zugelassene Umgebung hat, kann den Werkstatt-Prompt oder Schnellstart-Prompt dort einsetzen, soweit Hausrecht und Datenschutzfreigabe das erlauben.

### Verwendung auf eigene Gefahr

Die Nutzung erfolgt **auf eigene Gefahr und eigene Verantwortung**. Es handelt sich um ein Capability-Experiment. Die Frage, ob und wie der hier abgebildete Workflow rechtssicher betrieben werden kann, ist im Einzelfall zu prüfen — und kann auch zu dem Ergebnis fuehren, dass es nicht geht. Wir wollen das wissen, indem wir es bauen und ausprobieren.

## Quellenhygiene

- Keine erfundenen Aktenzeichen.
- Rechtsprechung nur mit Aktenzeichen + Datum + Verfahrensbezeichnung.
- Bei Unsicherheit lieber Lueckenliste als Erfindung.
- Vor Verwendung Aktenzeichen in offiziellen Datenbanken (Bundesgerichte, juris frei, Bundesverfassungsgericht.de) live verifizieren.

## Lizenz

Dual-lizenziert MIT und Apache-2.0.
