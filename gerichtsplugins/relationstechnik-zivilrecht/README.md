# Relationstechnik Zivilrecht (Praxis-Werkstatt)

<!-- BEGIN direkt-loslegen (autogen) -->
## Direkt loslegen ohne Plugin-Setup

Wer kein Plugin-Setup nutzen kann oder will, bekommt trotzdem eine sofort nutzbare Werkzeugkiste. Eine Markdown-Datei reicht: herunterladen, in das eigene Chat-System ziehen, Frage stellen. Die Werkstatt-Datei ist die ausführliche Variante; die Schnellstart-Datei ist die kompakte Variante für den schnellen Einstieg. Plugin und Testakte liegen als ZIP daneben.

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Großer Prompt (Werkstatt) | Markdown | [`relationstechnik-zivilrecht-werkstatt.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/relationstechnik-zivilrecht/relationstechnik-zivilrecht-werkstatt.md) |
| Kleiner Prompt (Schnellstart, höchstens 7500 Zeichen) | Markdown | [`relationstechnik-zivilrecht-schnellstart.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gerichtsplugins/relationstechnik-zivilrecht/relationstechnik-zivilrecht-schnellstart.md) |
| Plugin als Komplett-ZIP | ZIP | [`relationstechnik-zivilrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/relationstechnik-zivilrecht.zip) |
| Testakte(n) als ZIP | ZIP | [`relationstechnik-zivilrecht-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/relationstechnik-zivilrecht-testakte.zip) |
<!-- END direkt-loslegen (autogen) -->

> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 8 Buchstabe a der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die richterliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".

## Rolle

Jeder Zivilrechtler (Richter, Referendar, Anwalt) der eine große Relation aufbauen will

## Rechtsrahmen

ZPO, BGB, HGB, Methodenlehre des Buergerlichen Rechts (Larenz, Wieacker)

## Inhalt

- **21 Skills** (siehe `skills/`; inklusive Schnellstart-Skill)
- **Werkstatt-Prompt** (`relationstechnik-zivilrecht-werkstatt.md`)
- **Schnellstart-Prompt** (`relationstechnik-zivilrecht-schnellstart.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-akte-erstdurchsicht-zivil** — Strukturierte Erstdurchsicht der Zivilakte: Parteien identifizieren, Antrag isolieren, Lebenssachverhalt extrahieren, be
- **02-parteivortrag-strukturieren** — Kläger- und Beklagtenvortrag in Behauptungen, Bestreiten, Nichtwissen Paragraf 138 Abs. 4 ZPO, Gestaendnis Paragraf 288
- **03-streitstand-erfassen** — Streitiger und unstreitiger Sachverhalt heraussortieren, Geltung von Paragraf 138 Abs. 3 ZPO (Gestaendnisfiktion), Bewei
- **04-klage-antrag-auslegen** — Klageantrag auslegen Paragraf 133 BGB analog, Bestimmtheit Paragraf 253 Abs. 2 Nr. 2 ZPO, Haupt- und Hilfsantraege, Stuf
- **05-anspruchsgrundlagen-identifizieren** — Anspruchsgrundlagen aufstellen: vertraglich, vertragsaehnlich, dinglich, deliktisch, bereicherungsrechtlich; Anspruchssy
- **06-schluessigkeit-pruefen** — Schluessigkeitsprüfung (Klägerstation): liegen die Voraussetzungen der Anspruchsgrundlage nach dem Klägervortrag vor?
- **07-klaegerstation-votum** — Schriftliches Votum der Klägerstation: Anspruchsgrundlage, geprüfte Tatbestandsmerkmale, schluessige Rechtsfolge oder
- **08-beklagtenvortrag-strukturieren** — Beklagtenvortrag ordnen: Bestreiten der Anspruchsvoraussetzungen, Einwendungen (rechtshindernd, rechtsvernichtend), Einr
- **09-einwendungen-einreden-pruefen** — Prüfung der Einwendungen und Einreden: Verjaehrung Paragrafen 194 ff. BGB, Erfuellung Paragrafen 362 ff., Aufrechnung P
- **10-erheblichkeit-pruefen** — Erheblichkeitsprüfung (Beklagtenstation): sind Einwendungen und Einreden rechtlich erheblich? Schluessigkeit + Erheblic
- **11-beklagtenstation-votum** — Schriftliches Votum der Beklagtenstation: erhebliche Einwendungen und Einreden, unerhebliche Verteidigungsmittel, Beweis
- **12-beweisbeduerftige-tatsachen-isolieren** — Beweisbedürftige Tatsachen isolieren: erhebliche und streitige Tatsachen, Trennung von Rechtsfragen und Tatsachenfragen
- **13-beweislastverteilung-pruefen** — Beweislastverteilung nach allgemeinen Regeln (Rosenberg-Formel) und Sondernormen (Paragraf 280 Abs. 1 S. 2 BGB, Paragraf - **14-beweismittel-wuerdigen** — Beweismittel und ihre Würdigung: Augenschein Paragrafen 371 ff. ZPO, Zeuge Paragrafen 373 ff., Sachverständiger Paragr
- **15-beweisstation-votum** — Schriftliches Votum der Beweisstation: Beweisaufnahmebedarf, Beweisbeschluss-Entwurf Paragraf 358a ZPO, antizipierte Bew
- **16-tenor-formulieren** — Tenor formulieren: Hauptsache (Verurteilung zur Zahlung, Herausgabe, Unterlassung, Feststellung), Nebenforderungen (Zins
- **17-tatbestand-schreiben** — Tatbestand Paragraf 313 Abs. 1 Nr. 5 ZPO: gestraffter unstreitiger Sachverhalt, streitiger Klägervortrag, streitiger Be
- **18-entscheidungsgruende-aufbauen** — Entscheidungsgründe aufbauen: Zulässigkeit, Begründetheit (Anspruchsprüfung Schritt für Schritt), Beweiswürdigung,
- **19-nebenentscheidungen-kosten-vorlaeufige-vollstreckbarkeit** — Nebenentscheidungen: Kosten Paragrafen 91 ff. ZPO, Baumbach'sche Formel bei subjektiver Klagehaeufung, vorläufige Volls
- **20-urteilsentwurf-finalisieren** — Urteilsentwurf finalisieren: Rubrum, Tenor, Tatbestand, Entscheidungsgründe, Nebenentscheidungen, Rechtsmittelbelehrung

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
