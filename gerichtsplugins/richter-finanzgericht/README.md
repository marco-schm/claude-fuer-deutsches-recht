# Finanzgericht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`richter-finanzgericht`) | [`richter-finanzgericht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-finanzgericht.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Direkt loslegen ohne Plugin-Setup

Wer kein Claude-Code-Plugin nutzen kann, bekommt hier zwei mundgerecht zugeschnittene Markdown-Prompts. Beide funktionieren in jedem Chatbot deiner Wahl als Instant-Personalisierung. Du klickst auf den Download, die Datei landet im Download-Ordner, dann ziehst du sie in ChatGPT, Gemini, Mistral, Le Chat oder ein anderes System. Fertig.

| Prompt | Wofür | Direkt-Download |
| --- | --- | --- |
| **Finanzgericht-Werkstatt** | Vollständiger Arbeits-Prompt mit Werkstattlogik, Pflicht-Schritten, Quellen-Disziplin und Antwort-Skeletten. Darf lang sein. | [`richter-finanzgericht-werkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-finanzgericht-werkstatt.zip) |
| **Finanzgericht-Schnellstart** | Kompakter Einstiegs-Prompt, höchstens 7.500 Zeichen. Für den schnellen Wurf in einen Chat. | [`richter-finanzgericht-schnellstart.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-finanzgericht-schnellstart.zip) |

Wer die Markdown-Datei lieber im Browser ansehen statt herunterladen will:
- [`finanzgericht-werkstatt.md`](./finanzgericht-werkstatt.md) (im Browser ansehen)
- [`finanzgericht-schnellstart.md`](./finanzgericht-schnellstart.md) (im Browser ansehen)
<!-- END direkt-loslegen (autogen) -->

> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 8 Buchstabe a der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die richterliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".

## Rolle

Finanzrichter als Einzelrichter oder Senat (Paragraf 5 FGO)

## Rechtsrahmen

FGO, AO, EStG, KStG, GewStG, UStG, BewG, FVG, GKG, RVG

## Inhalt

- **10 Skills** (siehe `skills/`)
- **Werkstatt-Prompt** (`finanzgericht-werkstatt.md`)
- **Schnellstart-Prompt** (`finanzgericht-schnellstart.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-zulaessigkeit-finanzgerichtsklage** — Zulässigkeit der Klage Paragrafen 40-65 FGO: Klagearten (Anfechtung Verpflichtung Feststellung Untaetigkeit), Vorverfah
- **02-amtsermittlung-finanzgericht** — Amtsermittlungsgrundsatz Paragraf 76 FGO, Heranziehung der Akten Paragraf 71, Beweismittel, Schaetzungsbefugnis Paragraf
- **03-aussetzung-der-vollziehung** — Aussetzung der Vollziehung Paragraf 69 FGO bzw. Paragraf 361 AO: ernstliche Zweifel an der Rechtmaessigkeit, unbillige H
- **04-steuerbescheid-pruefen** — Prüfung des angegriffenen Steuerbescheids: formelle Rechtmaessigkeit (Begründung Paragraf 121 AO, Bekanntgabe Paragraf
- **05-est-pruefungsschema** — Einkommensteuer-Prüfung: Einkunftsart, Einkunftsermittlung (Paragrafen 4, 5 EStG oder Paragraf 11 EStG), Sonderausgaben
- **06-ust-pruefungsschema** — Umsatzsteuer: Steuerbarkeit Paragraf 1 UStG, Steuerpflicht und Steuerbefreiung Paragraf 4, Bemessungsgrundlage Paragraf
- **07-koerperschaft-und-gewerbesteuer** — Körperschaftsteuer: Subjektsteuerpflicht Paragraf 1 KStG, Einkommensermittlung Paragraf 8 KStG i.V.m. EStG, verdeckte G
- **08-schaetzung-und-betriebspruefung** — Schaetzung Paragraf 162 AO als Beweismittel: aeussere und innere Schaetzung, Zeitreihenvergleich, Geldverkehrsrechnung,
- **09-urteil-finanzgericht-und-revision** — Urteil Paragraf 105 FGO: Tatbestand, Entscheidungsgründe, Tenor; Revision Paragraf 115 FGO an BFH (grundsaetzliche Bede
- **10-entscheidungsvorschlag-finanzgericht** — Strukturierter Entscheidungsvorschlag: Tenor, Prüfungsschema Zulässigkeit Begründetheit, materielle Prüfung der Steu

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
