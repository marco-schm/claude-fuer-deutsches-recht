# _GERICHTE_EXPERIMENTAL — Legal-AI-Plugins für Gerichte

> **Experimentelle Plugin-Sammlung für den moeglichen Einsatz von KI an deutschen Gerichten.**
> Capability-Experiment. Keine Produktivempfehlung.

## Plugins in diesem Ordner

| Plugin | Rolle |
|---|---|
| `richter-amtsgericht-zivil` | Amtsrichter:in in Zivilsachen (Streitwert bis 5.000 Euro, sonstige Zuständigkeiten nach Paragraf 23 GVG) |
| `richter-amtsgericht-straf` | Strafrichter:in oder Schöffengericht am Amtsgericht (Paragraf 24 GVG, Paragraf 25 GVG, Paragrafen 28-30 GVG) |
| `richter-amtsgericht-insolvenz-restrukturierung` | Insolvenzrichter:in oder Restrukturierungsrichter:in am Amtsgericht (Paragraf 2 InsO, Paragrafen 34 ff. StaRUG) |
| `richter-amtsgericht-handelsregister` | Registerrichter:in oder Rechtspfleger:in für Handelsregister, Genossenschaftsregister, Partnerschaftsregister, Vereinsregister |
| `richter-landgericht-zivilkammer` | Vorsitzende:r oder Berichterstatter:in einer Zivilkammer (Paragraf 71 GVG, Streitwert ab 5.001 Euro; auch sonstige Zuständigkeiten Paragrafen 71-74 GVG) sowie zweite Instanz Berufung Paragraf 511 ZPO |
| `richter-landgericht-strafkammer` | Vorsitzende:r oder Berichterstatter:in einer großen oder kleinen Strafkammer (Paragraf 74 GVG, Paragraf 76 GVG); Schwurgericht Paragraf 74 Abs. 2 GVG |
| `richter-verwaltungsgericht` | Verwaltungsrichter:in als Einzelrichter:in oder Kammer (Paragrafen 4-6 VwGO) |
| `richter-finanzgericht` | Finanzrichter:in als Einzelrichter oder Senat (Paragraf 5 FGO) |
| `richter-sozialgericht` | Sozialrichter:in als Einzelrichter:in oder Kammer (Paragrafen 12, 31 SGG); mit ehrenamtlichen Richtern in muendlicher Verhandlung |
| `richter-arbeitsgericht` | Arbeitsrichter:in als Vorsitzende:r einer Kammer (mit zwei ehrenamtlichen Richtern aus Arbeitgeber- und Arbeitnehmerkreis) Paragraf 16 ArbGG |
| `richter-familiengericht` | Familienrichter:in am Amtsgericht (Paragraf 23a Abs. 1 Nr. 1 GVG i.V.m. Paragraf 23b GVG) für Ehe-, Kindschafts-, Unterhalts-, Versorgungsausgleichs-, Gewaltschutz- und sonstige Familiensachen nach FamFG |
| `richter-bverfg-verfassungsbeschwerden` | Wissenschaftliche:r Mitarbeiter:in oder Berichterstatter:in in einer Kammer beider Senate des Bundesverfassungsgerichts (Paragrafen 93a-93d BVerfGG) |
| `relationstechnik-zivilrecht` | Jede:r Zivilrechtler:in (Richter, Referendar, Anwalt) der eine große Relation aufbauen will |

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


## Aufbau jedes Plugins

- `.claude-plugin/plugin.json` — Plugin-Manifest
- `README.md` — Plugin-Beschreibung mit vollständigem Vorspruch
- `MEGAPROMPT.md` — vollständiger Arbeits-Prompt, portabel
- `MINIPROMPT.md` — Kompaktversion
- `skills/` — 10 (richterliche Plugins) oder 20 (Relationstechnik) Skills
- `testakte/README.md` — fiktive Testakte aus Richtersicht

## Warum dieser Ordner separat steht

Die richterliche Funktion ist eine besonders sensible Anwendung von KI. Aktengeheimnis, richterliche Unabhaengigkeit, Art. 22 DSGVO und KI-VO setzen einen strengen Rahmen. Wir bilden hier die Werkzeuge ab, **damit wir wissen, was geht**. Die Frage, ob und wie das im Echtbetrieb rechtssicher genutzt werden kann, ist in jedem Gericht und in jedem Verfahren neu zu prüfen.

## Lizenz

Dual-lizenziert MIT und Apache-2.0.
