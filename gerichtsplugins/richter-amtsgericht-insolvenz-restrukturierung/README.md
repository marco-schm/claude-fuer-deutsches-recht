# Insolvenz- und Restrukturierungsgericht am Amtsgericht

> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

## Rolle

Insolvenzrichter oder Restrukturierungsrichter am Amtsgericht (Paragraf 2 InsO, Paragrafen 34 ff. StaRUG)

## Rechtsrahmen

InsO, StaRUG, EuInsVO 2015/848, ZPO, GVG, RPflG, GKG, InsVV

## Inhalt

- **10 Skills** (siehe `skills/`)
- **Megaprompt** (`MEGAPROMPT.md`)
- **Miniprompt** (`MINIPROMPT.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-eroeffnungsantrag-pruefen-insolvenz** — Prüfung des Eröffnungsantrags Paragrafen 13-15 InsO, Zulässigkeit, Insolvenzgrund (Paragrafen 17-19 InsO), Verfahrens
- **02-sicherungsmassnahmen-vor-eroeffnung** — Sicherungsmaßnahmen Paragraf 21 InsO: vorläufiger Insolvenzverwalter (stark oder schwach), Verfügungsbeschraenkungen,
- **03-eroeffnungsbeschluss-und-verwalterbestellung** — Eröffnungsbeschluss Paragraf 27 InsO, Bestellung Insolvenzverwalter, Bestimmung Berichts-, Prüfungs- und Schlusstermin
- **04-glaeubigerversammlung-und-pruefungstermin** — Gläubigerversammlung Paragrafen 74 ff. InsO, Berichtstermin Paragraf 156, Prüfungstermin Paragraf 176, Feststellung zu
- **05-restschuldbefreiung-und-schlusstermin** — Schlusstermin Paragraf 197 InsO, Schlussverteilung, Restschuldbefreiungsverfahren Paragrafen 286 ff. InsO, Versagungsgru
- **06-eigenverwaltung-und-schutzschirm** — Eigenverwaltung Paragrafen 270 ff. InsO, Eigenverwaltungsplanung Paragraf 270a, Schutzschirmverfahren Paragraf 270d, Sac
- **07-insolvenzplan-bestaetigen** — Insolvenzplanverfahren Paragrafen 217 ff. InsO: Vorprüfung Paragraf 231, Anhörung, Erlaeuterungs- und Abstimmungstermi
- **08-starug-restrukturierungssache-anzeigen** — Anzeige Restrukturierungssache Paragrafen 31 ff. StaRUG, Restrukturierungsbeauftragter Paragraf 73 StaRUG, Restrukturie
- **09-starug-stabilisierungsanordnung** — Stabilisierungsanordnung Paragrafen 49 ff. StaRUG (Vollstreckungs- und Verwertungssperre), Voraussetzungen, Dauer (drei
- **10-starug-planbestaetigung-und-folgen** — Planabstimmung Paragrafen 17 ff. StaRUG, gruppeninternes Mehrheitserfordernis, gruppenübergreifender Cramdown Paragraf

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

Viele Gerichte werden Claude und Anthropic auf absehbare Zeit nicht produktiv einsetzen können — das wissen wir. Der Wert dieses Plugins liegt darin, dass **Megaprompt und Miniprompt portabel** sind: Sie funktionieren in jedem KI-Tool mit ausreichendem Kontextfenster und Datei-Upload (z.B. einem behoerdlich freigegebenen On-Premise-System). Wer im Gericht bereits eine zugelassene KI-Umgebung hat, kann den Megaprompt oder Miniprompt zusammen mit weiteren Instruktionen dort einsetzen, soweit das jeweilige Hausrecht und die Datenschutzfreigabe das erlauben.

### Verwendung auf eigene Gefahr

Die Nutzung erfolgt **auf eigene Gefahr und eigene Verantwortung**. Es handelt sich um ein Capability-Experiment. Die Frage, ob und wie der hier abgebildete Workflow rechtssicher betrieben werden kann, ist im Einzelfall zu prüfen — und kann auch zu dem Ergebnis fuehren, dass es nicht geht. Wir wollen das wissen, indem wir es bauen und ausprobieren.


## Quellenhygiene

- Keine erfundenen Aktenzeichen.
- Rechtsprechung nur mit Aktenzeichen + Datum + Verfahrensbezeichnung.
- Bei Unsicherheit lieber Lueckenliste als Erfindung.
- Vor Verwendung Aktenzeichen in offiziellen Datenbanken (Bundesgerichte, juris frei, Bundesverfassungsgericht.de) live verifizieren.

## Lizenz

Dual-lizenziert MIT und Apache-2.0.
