# Verwaltungsgericht

<!-- BEGIN direkt-loslegen (autogen) -->
## Direkt loslegen ohne Plugin-Setup

Wer kein Plugin-Setup nutzen kann oder will, bekommt trotzdem eine sofort nutzbare Werkzeugkiste. Eine Markdown-Datei reicht: herunterladen, in das eigene Chat-System ziehen, Frage stellen. Die Werkstatt-Datei ist die ausführliche Variante; die Schnellstart-Datei ist die kompakte Variante für den schnellen Einstieg. Plugin und Testakte liegen als ZIP daneben.

Für ausgearbeitete Dokumente gilt als Standard: Times New Roman 11 pt, klare dezimale Gliederung (`1`, `1.1`, `1.1.1`) und vollständig ausformulierte Sätze. Weicht ein amtliches Formular, ein Gerichtslayout oder ein Mandantentemplate davon ab, wird die Abweichung im Arbeitsprodukt benannt.

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Großer Prompt (Werkstatt) | ZIP | [`richter-verwaltungsgericht-werkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-verwaltungsgericht-werkstatt.zip) |
| Kleiner Prompt (Schnellstart, höchstens 7500 Zeichen) | ZIP | [`richter-verwaltungsgericht-schnellstart.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-verwaltungsgericht-schnellstart.zip) |
| Plugin als Komplett-ZIP | ZIP | [`richter-verwaltungsgericht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-verwaltungsgericht.zip) |
| Testakte(n) als ZIP | ZIP | [`richter-verwaltungsgericht-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-verwaltungsgericht-testakte.zip) |

Wer die Markdown-Datei lieber im Browser ansehen statt herunterladen will:
- [`richter-verwaltungsgericht-werkstatt.md`](./richter-verwaltungsgericht-werkstatt.md) (im Browser ansehen)
- [`richter-verwaltungsgericht-schnellstart.md`](./richter-verwaltungsgericht-schnellstart.md) (im Browser ansehen)
<!-- END direkt-loslegen (autogen) -->

> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 8 Buchstabe a der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die richterliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".

## Rolle

Verwaltungsrichter als Einzelrichter oder Kammer (Paragrafen 4-6 VwGO)

## Rechtsrahmen

VwGO, VwVfG, GG, BVerwGG, GKG, RVG, Fachgesetze (BImSchG, BauGB, AsylG, AufenthG)

## Inhalt

- **11 Skills** (siehe `skills/`; inklusive Schnellstart-Skill)
- **Werkstatt-Prompt** (`richter-verwaltungsgericht-werkstatt.md`)
- **Schnellstart-Prompt** (`richter-verwaltungsgericht-schnellstart.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-zulaessigkeit-verwaltungsklage** — Zulässigkeit der Klage: Verwaltungsrechtsweg Paragraf 40 VwGO, Klagearten Paragrafen 42 113 (Anfechtung Verpflichtung F
- **02-amtsermittlung-und-sachverhaltsfeststellung** — Amtsermittlungsgrundsatz Paragraf 86 VwGO, Ladung der Behoerde zur Vorlage der Akten Paragraf 99 VwGO, Sachverhaltsaufkl
- **03-begruendetheit-anfechtungsklage** — Begründetheit Paragraf 113 Abs. 1 VwGO: Rechtmaessigkeit des Verwaltungsakts (Rechtsgrundlage, formelle und materielle
- **04-begruendetheit-verpflichtungsklage** — Verpflichtungsklage Paragraf 113 Abs. 5 VwGO: Anspruch auf Erlass des begehrten VA, Bescheidungsurteil, Spruchreife, Beu
- **05-eilrechtsschutz-paragraf-80-abs-5** — Eilrechtsschutz Paragraf 80 Abs. 5 VwGO: Anordnung oder Wiederherstellung der aufschiebenden Wirkung, Folgenabwaegung, E
- **06-eilrechtsschutz-paragraf-123** — Einstweilige Anordnung Paragraf 123 VwGO: Sicherungs- und Regelungsanordnung, Anordnungsanspruch und -grund, Vorwegnahme
- **07-beweisaufnahme-verwaltungsgericht** — Beweisaufnahme Paragraf 96 VwGO i.V.m. ZPO: Sachverständigenbeweis, Zeugen, Augenschein, Urkunden, Beweiswürdigung Par
- **08-urteilsentwurf-paragraf-117-vwgo** — Urteilsentwurf Paragraf 117 VwGO: Tenor, Tatbestand (Sachverhalt), Entscheidungsgründe (Zulässigkeit, Begründetheit),
- **09-rechtsmittel-vwgo** — Berufung Paragrafen 124 ff. VwGO (Zulassung durch OVG/VGH), Revision Paragraf 132 VwGO (Zulassung durch BVerwG), Nichtzu
- **10-entscheidungsvorschlag-verwaltungsgericht** — Strukturierter Entscheidungsvorschlag: Tenor, Prüfungsschema Zulässigkeit Begründetheit, Argumentation der Behoerde g

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
