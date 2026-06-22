# Staatsanwaltschaft und Amtsanwaltschaft

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`staatsanwaltschaft-amtsanwaltschaft`) | [`staatsanwaltschaft-amtsanwaltschaft.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/staatsanwaltschaft-amtsanwaltschaft.zip) |
| **Alle Skills als Markdown** | [`alle-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-skills-markdown.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN direkt-loslegen (autogen) -->
## Direkt loslegen ohne Plugin-Setup

Wer kein Claude-Code-Plugin nutzen kann, bekommt hier zwei mundgerecht zugeschnittene Markdown-Prompts. Beide funktionieren in jedem Chatbot deiner Wahl als Instant-Personalisierung. Du klickst auf den Download, die Datei landet im Download-Ordner, dann ziehst du sie in ChatGPT, Gemini, Mistral, Le Chat oder ein anderes System. Fertig.

| Prompt | Wofür | Direkt-Download |
| --- | --- | --- |
| **Staatsanwaltschaft und Amtsanwaltschaft-Werkstatt** | Vollständiger Arbeits-Prompt mit Werkstattlogik, Pflicht-Schritten, Quellen-Disziplin und Antwort-Skeletten. Darf lang sein. | [`staatsanwaltschaft-amtsanwaltschaft-werkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/staatsanwaltschaft-amtsanwaltschaft-werkstatt.zip) |
| **Staatsanwaltschaft und Amtsanwaltschaft-Schnellstart** | Kompakter Einstiegs-Prompt, höchstens 7.500 Zeichen. Für den schnellen Wurf in einen Chat. | [`staatsanwaltschaft-amtsanwaltschaft-schnellstart.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/staatsanwaltschaft-amtsanwaltschaft-schnellstart.zip) |

Wer die Markdown-Datei lieber im Browser ansehen statt herunterladen will:
- [`staatsanwaltschaft-amtsanwaltschaft-werkstatt.md`](./staatsanwaltschaft-amtsanwaltschaft-werkstatt.md) (im Browser ansehen)
- [`staatsanwaltschaft-amtsanwaltschaft-schnellstart.md`](./staatsanwaltschaft-amtsanwaltschaft-schnellstart.md) (im Browser ansehen)
<!-- END direkt-loslegen (autogen) -->

> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Strafverfolgung und Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 6 (Strafverfolgung) und Nr. 8 Buchstabe a (Justiz) der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die staatsanwaltschaftliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".

## Rolle

Staatsanwaltschaft oder Amtsanwaltschaft bei Amtsgericht und Landgericht (Paragraf 141 GVG, Paragraf 142 GVG, Paragraf 143 GVG). Das Plugin bildet das Dezernat von der Erstdurchsicht des Ermittlungsvorgangs bis zur Strafvollstreckung ab.

## Rechtsrahmen

StPO, StGB, GVG, JGG, OWiG, RiStBV, OrgStA, StVollstrO, BZRG, RVG

## Inhalt

- **28 Skills** (siehe `skills/`)
- **Werkstatt-Prompt** (`staatsanwaltschaft-amtsanwaltschaft-werkstatt.md`)
- **Schnellstart-Prompt** (`staatsanwaltschaft-amtsanwaltschaft-schnellstart.md`)
- **Testakten** (`testakte/README.md`) — aus staatsanwaltschaftlicher Sicht

## Skill-Liste

- **01-akte-erstdurchsicht-und-anfangsverdacht** — Erstdurchsicht, Anfangsverdacht (Paragraf 152 Abs. 2 StPO), Verjaehrung, Ermittlungsrichtung
- **02-zustaendigkeit-sta-und-amtsanwaltschaft** — Sachliche und oertliche Zustaendigkeit, Abgrenzung Staatsanwalt und Amtsanwalt nach OrgStA
- **03-ermittlungsfuehrung-und-ermittlungsanweisung** — Sachleitung (Paragrafen 161, 163 StPO), Ermittlungsanweisung an die Polizei, Ermittlungsplan
- **04-durchsuchung-und-beschlagnahme-antrag** — Antrag Durchsuchung (Paragrafen 102 ff. StPO) und Beschlagnahme (Paragrafen 94 ff. StPO), Richtervorbehalt
- **05-haftbefehlsantrag-und-untersuchungshaft** — Haftbefehlsantrag (Paragrafen 112 ff. StPO), Haftgruende, Verhaeltnismaessigkeit, Haftverschonung
- **06-vorlaeufige-festnahme-und-eilkompetenz** — Vorlaeufige Festnahme (Paragraf 127 StPO), Eilkompetenz, Vorfuehrung (Paragraf 128 StPO)
- **07-telekommunikationsueberwachung-und-verdeckte-massnahmen** — TKUe (Paragraf 100a StPO) und verdeckte Massnahmen, Katalogtat, Subsidiaritaet, Kernbereichsschutz
- **08-beschuldigtenvernehmung-und-belehrung** — Vernehmung (Paragrafen 136, 163a StPO), Belehrung, verbotene Methoden (Paragraf 136a StPO)
- **09-sachverstaendige-und-koerperliche-untersuchung** — Gutachtenauftrag (Paragrafen 73 ff. StPO), koerperliche Untersuchung (Paragraf 81a StPO)
- **10-einstellung-mangels-tatverdacht-paragraf-170** — Einstellung mangels hinreichenden Tatverdachts (Paragraf 170 Abs. 2 StPO), Bescheide
- **11-einstellung-aus-opportunitaet-paragraf-153-und-153a** — Einstellung wegen Geringfuegigkeit und gegen Auflagen (Paragrafen 153, 153a StPO)
- **12-teileinstellung-paragraf-154-und-154a** — Beschraenkung der Verfolgung (Paragrafen 154, 154a StPO)
- **13-strafbefehlsantrag-paragraf-407** — Strafbefehlsantrag (Paragrafen 407 ff. StPO), zulaessige Rechtsfolgen, Tatkonkretisierung
- **14-anklageschrift-paragraf-200** — Anklageschrift (Paragraf 200 StPO), Anklagesatz, wesentliches Ermittlungsergebnis, Eroeffnungsantrag
- **15-antrag-beschleunigtes-verfahren-paragraf-417** — Beschleunigtes Verfahren (Paragrafen 417 ff. StPO), Eignung, Rechtsfolgenbegrenzung
- **16-sicherungsverfahren-und-massregeln** — Sicherungsverfahren (Paragrafen 413 ff. StPO), Massregeln (Paragrafen 63, 64 StGB), Gefaehrlichkeitsprognose
- **17-einziehung-und-vermoegensabschoepfung** — Einziehung (Paragrafen 73 ff. StGB), Vermoegensarrest (Paragraf 111e StPO), Wertersatz
- **18-jugendsache-und-diversion-paragraf-45-jgg** — Jugendsache, Diversion (Paragraf 45 JGG), Heranwachsende (Paragraf 105 JGG)
- **19-sitzungsdienst-und-fragerecht-hauptverhandlung** — Sitzungsvertretung (Paragraf 226 StPO), Fragerecht (Paragraf 240 StPO), Erklaerungen (Paragraf 257 StPO)
- **20-plaedoyer-und-schlussvortrag-paragraf-258** — Schlussvortrag (Paragraf 258 StPO), Beweiswuerdigung, Strafzumessungsantrag (Paragraf 46 StGB)
- **21-rechtsmittel-der-staatsanwaltschaft** — Berufung, Revision, Beschwerde, zugunsten und zuungunsten (Paragraf 296 Abs. 2 StPO)
- **22-strafvollstreckung-paragraf-451** — Vollstreckung durch die Staatsanwaltschaft (Paragrafen 449 ff. StPO), Ladung, Aufschub
- **23-klageerzwingung-und-beschwerdebescheid-paragraf-172** — Bescheid (Paragraf 171 StPO), Klageerzwingungsverfahren (Paragraf 172 StPO)
- **24-abschlussverfuegung-und-entscheidungsvorschlag** — Abschlussverfuegung, Gesamtwuerdigung, Verfuegungstechnik, Markierung als Vorschlag
- **25-adhaesionsverfahren-paragraf-403** — Adhaesionsantrag (Paragrafen 403 ff. StPO), Eignung zur Mitverhandlung, Abtrennung
- **26-opferschutz-nebenklage-und-verletztenrechte** — Opferschutz (Paragrafen 406d ff. StPO), Nebenklage (Paragrafen 395 ff. StPO), psychosoziale Prozessbegleitung
- **27-wiederaufnahme-zuungunsten-paragraf-362** — Wiederaufnahme zuungunsten (Paragraf 362 StPO), formale Anforderungen, ne bis in idem
- **28-internationale-rechtshilfe-und-eu-haftbefehl** — EuHb (Paragrafen 78 ff. IRG), EEA (Paragrafen 91a ff. IRG), klassische Rechtshilfe

## Wichtiger Hinweis vor Verwendung

**Experimentelles Plugin — Vorsicht.** Dieses Plugin ist ein Funktionsexperiment für den Einsatz von KI bei deutschen Strafverfolgungsbehoerden. Es geht hier um die **Capability**, nicht um eine Produktivempfehlung.

### Rechtliche Einordnung der KI-Verordnung (KI-VO, VO (EU) 2024/1689)

- **Art. 6 Abs. 2 i.V.m. Anhang III Nr. 6 KI-VO**: KI-Systeme, die im Bereich **Strafverfolgung** zur Bewertung von Beweismitteln, zur Risikoeinschaetzung oder zur Aufklaerung von Straftaten eingesetzt werden, sind grundsaetzlich **Hochrisiko-KI**.
- **Art. 6 Abs. 2 i.V.m. Anhang III Nr. 8 lit. a KI-VO**: Soweit das System im Auftrag einer Justizbehoerde bei der **Recherche und Auslegung von Sachverhalten und Rechtsvorschriften** sowie bei der **Anwendung des Rechts** verwendet wird, gilt es ebenfalls als Hochrisiko-KI.
- **Aber Art. 6 Abs. 3 KI-VO**: Ein KI-System gilt **nicht** als Hochrisiko-KI, wenn es nur eine **vorbereitende Aufgabe** wahrnimmt (z.B. Vorbereitung von Verfuegungsentwuerfen, reine Recherche ohne Subsumtion).
- **Notifizierungspflicht**: Auch im Ausnahmefall des Art. 6 Abs. 3 ist der Anbieter bzw. Betreiber verpflichtet, das KI-System bei der zuständigen Aufsicht zu **registrieren** (Art. 49 Abs. 2 KI-VO).
- Die Einordnung ist im Einzelfall zu prüfen. Sobald das System konkrete Antragsvorschlaege produziert, die Subsumtion vornimmt oder die staatsanwaltschaftliche Würdigung ersetzt, wird die Schwelle zur Hochrisiko-KI überschritten.

### Art. 22 DSGVO — Verbot ausschliesslich automatisierter Entscheidung

Die staatsanwaltschaftliche Letztentscheidung muss zwingend bei einem Menschen liegen. **Keine Maschine erhebt Anklage, beantragt Haft oder stellt ein.** Diese Skills sind ausschliesslich **Unterstuetzung** der staatsanwaltschaftlichen Arbeit, niemals deren Ersatz. Der Dezernent prüft, gewichtet, entscheidet — die KI bereitet vor und macht Vorschlaege.

### Objektivitaetspflicht

- **Paragraf 160 Abs. 2 StPO**: Die Staatsanwaltschaft hat nicht nur die zur Belastung, sondern auch die zur Entlastung dienenden Umstaende zu ermitteln. Jede KI-Ausgabe ist auf diese Ausgewogenheit zu prüfen; eine einseitig belastende Vorbereitung widerspricht dem gesetzlichen Auftrag.

### Aktengeheimnis und Datenschutz

- **Paragraf 353b StGB** (Verletzung von Dienstgeheimnissen) und die beamtenrechtliche Verschwiegenheitspflicht (**Paragraf 37 BeamtStG** für Landesbeamte, **Paragraf 67 BBG** für Bundesbeamte) sind strikt zu wahren.
- Akteninhalte duerfen nicht ungeprüft an externe KI-Anbieter übermittelt werden. Vor jeder Verwendung ist zu prüfen, ob die genutzte KI-Umgebung den Datenschutz und das Aktengeheimnis gewaehrleistet.
- **Schatten-KI ist ausdrücklich abgelehnt.** Dieses Plugin soll keine Hilfe sein, KI an behoerdlichen Datenschutz- und IT-Richtlinien vorbei einzusetzen.

### Weisungsgebundenheit und Revisionssicherheit

- Die Staatsanwaltschaft ist weisungsgebunden (Paragrafen 146, 147 GVG); die KI ersetzt weder Weisung noch dezernatliche Verantwortung.
- Saemtliche Arbeitsergebnisse müssen revisionssicher dokumentiert werden: Wer hat wann welche KI-Ausgabe genutzt, welche Änderungen wurden danach durch den Dezernenten vorgenommen, welche Akten- und Promptbestandteile lagen zugrunde?
- Die KI-Ausgabe muss als KI-Ausgabe erkennbar bleiben (Markierung, Versionierung); die staatsanwaltschaftliche Bearbeitung ist zu dokumentieren.
- Aufbewahrungsfristen nach Aktenordnung und ggf. KI-VO-Logging-Pflichten beachten.

### Realismus-Hinweis

Viele Behoerden werden Claude und Anthropic auf absehbare Zeit nicht produktiv einsetzen können — das wissen wir. Der Wert dieses Plugins liegt darin, dass **Werkstatt-Prompt und Schnellstart-Prompt portabel** sind: Sie funktionieren in jedem KI-Tool mit ausreichendem Kontextfenster und Datei-Upload (z.B. einem behoerdlich freigegebenen On-Premise-System). Wer bereits eine zugelassene KI-Umgebung hat, kann den Werkstatt-Prompt oder Schnellstart-Prompt zusammen mit weiteren Instruktionen dort einsetzen, soweit Hausrecht und Datenschutzfreigabe das erlauben.

### Verwendung auf eigene Gefahr

Die Nutzung erfolgt **auf eigene Gefahr und eigene Verantwortung**. Es handelt sich um ein Capability-Experiment. Die Frage, ob und wie der hier abgebildete Workflow rechtssicher betrieben werden kann, ist im Einzelfall zu prüfen — und kann auch zu dem Ergebnis fuehren, dass es nicht geht. Wir wollen das wissen, indem wir es bauen und ausprobieren.

## Quellenhygiene

- Keine erfundenen Aktenzeichen.
- Rechtsprechung nur mit Aktenzeichen + Datum + Verfahrensbezeichnung.
- Bei Unsicherheit lieber Lueckenliste als Erfindung.
- Vor Verwendung Aktenzeichen in offiziellen Datenbanken (Bundesgerichte, juris frei, Bundesverfassungsgericht.de) live verifizieren.

## Lizenz

Dual-lizenziert MIT und Apache-2.0.
