# Richter Amtsgericht Zivilsachen

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`richter-amtsgericht-zivil`) | [`richter-amtsgericht-zivil.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-amtsgericht-zivil.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Direkt loslegen ohne Plugin-Setup

Wer kein Claude-Code-Plugin nutzen kann, bekommt hier zwei mundgerecht zugeschnittene Markdown-Prompts. Beide funktionieren in jedem Chatbot deiner Wahl als Instant-Personalisierung. Du klickst auf den Download, die Datei landet im Download-Ordner, dann ziehst du sie in ChatGPT, Gemini, Mistral, Le Chat oder ein anderes System. Fertig.

| Prompt | Wofür | Direkt-Download |
| --- | --- | --- |
| **Richter Amtsgericht Zivilsachen-Werkstatt** | Vollständiger Arbeits-Prompt mit Werkstattlogik, Pflicht-Schritten, Quellen-Disziplin und Antwort-Skeletten. Darf lang sein. | [`richter-amtsgericht-zivil-werkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-amtsgericht-zivil-werkstatt.zip) |
| **Richter Amtsgericht Zivilsachen-Schnellstart** | Kompakter Einstiegs-Prompt, höchstens 7.500 Zeichen. Für den schnellen Wurf in einen Chat. | [`richter-amtsgericht-zivil-schnellstart.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-amtsgericht-zivil-schnellstart.zip) |

Wer die Markdown-Datei lieber im Browser ansehen statt herunterladen will:
- [`amtsgericht-zivil-werkstatt.md`](./amtsgericht-zivil-werkstatt.md) (im Browser ansehen)
- [`amtsgericht-zivil-schnellstart.md`](./amtsgericht-zivil-schnellstart.md) (im Browser ansehen)
<!-- END direkt-loslegen (autogen) -->

> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 8 Buchstabe a der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die richterliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".

## Rolle

Amtsrichter in Zivilsachen (Streitwert bis 10.000 Euro, sonstige Zuständigkeiten nach Paragraf 23 GVG)

## Rechtsrahmen

ZPO, BGB, GVG, RPflG, GKG, RVG

## Inhalt

- **10 Skills** (siehe `skills/`)
- **Werkstatt-Prompt** (`amtsgericht-zivil-werkstatt.md`)
- **Schnellstart-Prompt** (`amtsgericht-zivil-schnellstart.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-eingangspruefung-zustaendigkeit** — Prüfung Zuständigkeit (Paragraf 23 GVG sachlich, Paragrafen 12 ff. ZPO örtlich), Klagezustellung, Pflichtangaben Para
- **02-streitwert-und-gerichtskosten** — Streitwertbestimmung Paragrafen 3-9 ZPO, GKG-Anlage 1 (KV 1210, 1211, 1220), vorläufige Streitwertfestsetzung, GKG-Vors
- **03-akte-erstdurchsicht** — Strukturierte Erstdurchsicht: Parteien, Antrag, Lebenssachverhalt, Anspruchsgrundlagen sammeln, Beweismittel listen, Str
- **04-relation-zivilrecht-klein** — Echte Relation: Klägerstation (Schluessigkeit der Anspruchsgrundlage), Beklagtenstation (Erheblichkeit der Einwendungen
- **05-beweisaufnahme-kleine-zivilkammer** — Beweisbeschluss formulieren (Paragrafen 358-360 ZPO), Zeugenladung, Sachverständigenauswahl, Beweistermin protokolliere
- **06-tenor-und-kostenentscheidung** — Tenor formulieren (Hauptsache, Nebenforderungen, Zinsen, Kosten Paragraf 91 ZPO, vorläufige Vollstreckbarkeit Paragrafe
- **07-urteilsentwurf-paragraf-313** — Urteilsentwurf nach Paragraf 313 ZPO: Rubrum, Tenor, Tatbestand (gestraffter Vortrag), Entscheidungsgründe (Begründeth
- **08-versaeumnisurteil-und-anerkenntnis** — Versaeumnisurteil Paragrafen 330-347 ZPO, Anerkenntnisurteil Paragraf 307 ZPO, Verzichtsurteil Paragraf 306 ZPO, Einspru
- **09-vergleich-und-erledigung** — Prozessvergleich Paragraf 794 Abs. 1 Nr. 1 ZPO, Vergleich im Termin, schriftlicher Vergleich Paragraf 278 Abs. 6 ZPO, Er
- **10-entscheidungsvorschlag-zur-richterlichen-pruefung** — Strukturierter Entscheidungsvorschlag für den Richter: Tenor-Vorschlag, tragende Gründe in Stichpunkten, Risikohinweis

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
