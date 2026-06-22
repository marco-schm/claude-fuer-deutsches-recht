# Arbeitsgericht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`richter-arbeitsgericht`) | [`richter-arbeitsgericht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-arbeitsgericht.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Direkt loslegen ohne Plugin-Setup

Wer kein Claude-Code-Plugin nutzen kann, bekommt hier zwei mundgerecht zugeschnittene Markdown-Prompts. Beide funktionieren in jedem Chatbot deiner Wahl als Instant-Personalisierung. Du klickst auf den Download, die Datei landet im Download-Ordner, dann ziehst du sie in ChatGPT, Gemini, Mistral, Le Chat oder ein anderes System. Fertig.

| Prompt | Wofür | Direkt-Download |
| --- | --- | --- |
| **Arbeitsgericht-Werkstatt** | Vollständiger Arbeits-Prompt mit Werkstattlogik, Pflicht-Schritten, Quellen-Disziplin und Antwort-Skeletten. Darf lang sein. | [`richter-arbeitsgericht-werkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-arbeitsgericht-werkstatt.zip) |
| **Arbeitsgericht-Schnellstart** | Kompakter Einstiegs-Prompt, höchstens 7.500 Zeichen. Für den schnellen Wurf in einen Chat. | [`richter-arbeitsgericht-schnellstart.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-arbeitsgericht-schnellstart.zip) |

Wer die Markdown-Datei lieber im Browser ansehen statt herunterladen will:
- [`arbeitsgericht-werkstatt.md`](./arbeitsgericht-werkstatt.md) (im Browser ansehen)
- [`arbeitsgericht-schnellstart.md`](./arbeitsgericht-schnellstart.md) (im Browser ansehen)
<!-- END direkt-loslegen (autogen) -->

> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 8 Buchstabe a der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die richterliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".

## Rolle

Arbeitsrichter als Vorsitzender einer Kammer (mit zwei ehrenamtlichen Richtern aus Arbeitgeber- und Arbeitnehmerkreis) Paragraf 16 ArbGG

## Rechtsrahmen

ArbGG, BGB, KSchG, BetrVG, TzBfG, AGG, EFZG, BUrlG, GVG, ZPO

## Inhalt

- **10 Skills** (siehe `skills/`)
- **Werkstatt-Prompt** (`arbeitsgericht-werkstatt.md`)
- **Schnellstart-Prompt** (`arbeitsgericht-schnellstart.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-zustaendigkeit-und-guetetermin** — Sachliche Zuständigkeit Paragraf 2 ArbGG, örtliche Zuständigkeit Paragraf 48 ArbGG i.V.m. Paragrafen 12 ff. ZPO, Klag
- **02-kuendigungsschutzklage-pruefen** — Kündigungsschutzklage Paragraf 4 KSchG: Klagefrist 3 Wochen, Kündigungsgründe (personenbedingt verhaltensbedingt betr
- **03-zahlungsklage-lohn-und-gehalt** — Zahlungsklage: faelliger Arbeitslohn, Annahmeverzug Paragrafen 615 BGB, Urlaubsabgeltung Paragraf 7 Abs. 4 BUrlG, Entgel
- **04-betriebsuebergang-und-tarif** — Betriebsübergang Paragraf 613a BGB, Eintritt in Arbeitsverhältnisse, Widerspruchsrecht, Informationspflichten Abs. 5;
- **05-befristung-und-teilzeit** — Befristungskontrolle TzBfG: sachgrundlose Befristung Paragraf 14 Abs. 2, Sachgrundbefristung Paragraf 14 Abs. 1, Zweckbe
- **06-agg-diskriminierung** — AGG Paragraf 7: Benachteiligungsverbot, geschuetzte Merkmale Paragraf 1, Beweislastregel Paragraf 22, Entschaedigung und
- **07-einstweilige-verfuegung-arbeitsrecht** — Einstweilige Verfügung im Arbeitsrecht: Verfügungsanspruch und -grund Paragraf 940 ZPO, Schutz von Beschaeftigungsansp
- **08-betriebsverfassung-beschlussverfahren** — Beschlussverfahren Paragrafen 80 ff. ArbGG: Beteiligte, Verfahrensgegenstand (Mitbestimmung Paragraf 87 BetrVG, Einigung
- **09-urteil-arbeitsgericht** — Urteil Paragraf 60 ArbGG i.V.m. Paragrafen 313 ZPO, Tenor, Tatbestand, Entscheidungsgründe, Streitwert (3 Bruttomonatsg
- **10-entscheidungsvorschlag-arbeitsgericht** — Strukturierter Entscheidungsvorschlag: Tenor-Skizze, Kündigungsprüfungsschema, Anspruchsprüfung, Vergleichsvorschlag

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

Viele Gerichte werden Claude und Anthropic auf absehbare Zeit nicht produktiv einsetzen können — das wissen wir. Der Wert dieses Plugins liegt darin, dass **Werkstatt-Prompt und Schnellstart-Prompt portabel** sind: Sie funktionieren in jedem KI-Tool mit ausreichendem Kontextfenster und Datei-Upload (z.B. einem behoerdlich freigegebenen On-Premise-System). Wer im Gericht bereits eine zugelassene KI-Umgebung hat, kann den Werkstatt-Prompt oder Schnellstart-Prompt zusammen mit weiteren Instruktionen dort einsetzen, soweit das jeweilige Hausrecht und die Datenschutzfreigabe das erlauben.

### Verwendung auf eigene Gefahr

Die Nutzung erfolgt **auf eigene Gefahr und eigene Verantwortung**. Es handelt sich um ein Capability-Experiment. Die Frage, ob und wie der hier abgebildete Workflow rechtssicher betrieben werden kann, ist im Einzelfall zu prüfen — und kann auch zu dem Ergebnis fuehren, dass es nicht geht. Wir wollen das wissen, indem wir es bauen und ausprobieren.

## Quellenhygiene

- Keine erfundenen Aktenzeichen.
- Rechtsprechung nur mit Aktenzeichen + Datum + Verfahrensbezeichnung.
- Bei Unsicherheit lieber Lueckenliste als Erfindung.
- Vor Verwendung Aktenzeichen in offiziellen Datenbanken (Bundesgerichte, juris frei, Bundesverfassungsgericht.de) live verifizieren.

## Lizenz

Dual-lizenziert MIT und Apache-2.0.
