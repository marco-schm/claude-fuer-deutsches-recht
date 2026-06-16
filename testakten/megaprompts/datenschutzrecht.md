# Megaprompt: datenschutzrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 365 Skills (gekuerzt fuer Chat-Fenster) des Plugins `datenschutzrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Datenschutzrecht DSGVO/BDSG: ordnet Rolle (Verantwortlicher, Auftragsverarbeiter, Betro…
2. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting im Datenschutzrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und …
3. **dsgvo-erstpruefung-und-mandatsziel** — DSGVO: Erstprüfung, Rollenklärung und Mandatsziel: DSGVO: Erstprüfung, Rollenklärung und Mandatsziel.
4. **datenschutz-schadensersatz-art-82-dsgvo-gerichtsstreit** — Schadensersatzklage nach Art. 82 DSGVO materieller und immaterieller Schaden vor deutschen Zivilgerichten. EuGH C-300/21…
5. **datenschutz-mandatssteckbrief-fristen-rollen** — Datenschutzrechtliches Mandat strukturieren und Arbeitsbereich abgrenzen. Art. 5 24 DSGVO §§ 1 ff. BDSG. Prüfraster: Man…
6. **datenschutz-schadensersatz-art-82-dsgvo** — Schadensersatzklage nach Art. 82 DSGVO materieller und immaterieller Schaden vor deutschen Zivilgerichten. EuGH C-300/21…
7. **anpassen** — Bestehende Datenschutzdokumentation oder Richtlinien an neue Anforderungen oder Verarbeitungstätigkeiten anpassen. Art. …
8. **anwendungsfall-triage** — Datenschutzrechtlichen Sachverhalt einordnen und Bearbeitungsroute bestimmen. Art. 2 3 DSGVO Anwendungsbereich § 1 BDSG.…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Datenschutzrecht DSGVO/BDSG: ordnet Rolle (Verantwortlicher, Auftragsverarbeiter, Betroffener), markiert Frist (Art. 33 Meldung 72h), wählt Norm (DSGVO Art. 5/6/13/15/28/32/33/35, BDSG, TTDSG) und Zuständigkeit (BfDI Bund), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Datenschutzrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `anpassen` — Anpassen
- `einstieg-schnelltriage-fallrouting` — Anschluss
- `anwendungsfall-triage` — Anwendungsfall Triage
- `art-9-besondere-kategorien` — ART 9 Besondere Kategorien
- `dsv-art-9-besondere-kategorien` — ART Besondere Aufnahme Statusinformation
- `aufnahme-statusinformation` — Aufnahme Statusinformation
- `auskunft-behoerden-gerichts-registerweg` — Auskunft Behoerden Gerichts Registerweg
- `avv-art-26-joint-controllership-deutsch` — AVV ART 26 Joint Controllership Deutsch
- `avv-art-28-dsgvo-grundtatbestand` — AVV ART 28 DSGVO Grundtatbestand
- `avv-art-28-mindestinhalte-checkliste` — AVV ART 28 Mindestinhalte Checkliste
- `avv-audit-und-kontrollrechte` — AVV Audit und Kontrollrechte
- `avv-cloud-und-subverarbeitung-art-28-iv` — AVV Cloud und Subverarbeitung ART 28 IV
- `avv-eu-kommission-musterklauseln-2021-915` — AVV EU Kommission Musterklauseln 2021 915
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Datenschutzrecht sind Art. 15, Art. 33, Art. 44, BDSG, DSGVO, TDDDG. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im Datenschutzrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig:..._

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Datenschutzrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Datenschutzrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** DSGVO/BDSG/TDDDG – PIA/DPIA, AVV-Review als Verantwortlicher und Auftragsverarbeiter, Auskunftsersuchen Art. 15, Datenpannenmeldung Art. 33/34, Drittlandstransfer Art. 44 ff., US-Transfer mit DPF/SCC/TIA, Behördenpaket, Drift-Monitoring.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** `passender-datenschutz-skill` — [warum dieser Arbeitsgang hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `anwendungsfall-triage` | Datenschutzrechtlichen Sachverhalt einordnen und Bearbeitungsroute bestimmen. Art. 2 3 DSGVO Anwendungsbereich § 1 BDSG. Prüfraster: Anwendungsbereich personenbezogene Daten Verantwortlicher Auftragsverarbeiter… |
| `avv-pruefung` | Auftragsverarbeitungsvertrag nach Art. 28 DSGVO prüfen oder erstellen wenn Dritter Daten im Auftrag verarbeitet. Art. 28 DSGVO AVV-Pflicht § 62 BDSG. Prüfraster: Pflichtinhalte Art. 28 Abs. 3 Weisungsgebundenheit… |
| `datenpanne-meldung` | Datenpanne nach Art. 33 34 DSGVO melden wenn Sicherheitsverletzung personenbezogener Daten vorliegt. Art. 33 34 DSGVO Meldepflichten § 65 BDSG. Prüfraster: Meldepflicht 72-Stunden-Frist Schwere Risikobewertung… |
| `datenschutzrecht-anpassen` | Bestehende Datenschutzdokumentation oder Richtlinien an neue Anforderungen oder Verarbeitungstätigkeiten anpassen. Art. 5 24 DSGVO Rechenschaftspflicht. Prüfraster: Bestandsaufnahme Lueckenanalyse DSGVO-Anforderungen… |
| `datenschutzrecht-kaltstart-interview` | Neues Datenschutzmandat durch strukturiertes Erstgespraech aufnehmen. Art. 5 6 DSGVO Grundsaetze § 26 BDSG Beschäftigtendaten. Prüfraster: Verarbeitungszweck Datenarten betroffene Personen Empfaenger… |
| `datenschutzrecht-mandat-arbeitsbereich` | Datenschutzrechtliches Mandat strukturieren und Arbeitsbereich abgrenzen. Art. 5 24 DSGVO §§ 1 ff. BDSG. Prüfraster: Mandatsumfang Zuständigkeiten Fristen Risikostufe externe Datenschutzberatung. Output:… |
| `drittlandstransfer-pruefung` | Datentransfer in Drittlaender außerhalb EU und EWR auf Zulässigkeit prüfen. Art. 44 ff. DSGVO Kapitel V Drittlandstransfer. Prüfraster: Angemessenheitsbeschluss SCC BCR Schrems-II-Folgen Transfer Impact Assessment… |
| `us-transfer-tia-dokumentation` | US-Drittlandtransfer mit EU-US Data Privacy Framework, DPF-Listing, Schrems-I/II-Historie, SCC/BCR-Ausweichpfad, Transfer Impact Assessment, supplementary measures und Review-Kalender dokumentieren. |
| `standardvertragsklauseln-scc-paket` | Standardvertragsklauseln vorbereiten: Modul 1-4 wählen, Annex I-III ausfüllen, Subprozessoren, TOMs, AVV-Schnittstelle, TIA-Andockung und Unterzeichnungspaket erstellen. |
| `drittlandtransfer-behoerdenpaket-output` | Aus Transferregister, DPF/SCC/TIA, TOMs und Subprozessoren ein druckreifes Paket samt Antwortentwurf für deutsche Datenschutzaufsichtsbehörden bauen. |
| `dsb-bestellungspflicht-pruefung` | Bestellungspflicht für Datenschutzbeauftragten prüfen. Art. 37 DSGVO § 38 BDSG Bestellungspflicht. Prüfraster: Schwellenwerte Art. 37 Abs. 1 Betriebsgroe Verarbeitungsart Pflichtbestellung freiwillige Bestellung.… |
| `dsfa-erstellung` | Datenschutz-Folgenabschaetzung nach Art. 35 DSGVO durchführen wenn hohes Risiko für Betroffene vorliegt. Art. 35 36 DSGVO DSFA § 67 BDSG. Prüfraster: Risikobewertung Verarbeitungsbeschreibung Notwendigkeit… |
| `dsgvo-auskunft` | Auskunftsersuchen nach Art. 15 DSGVO prüfen und beantworten wenn Betroffener Auskunft verlangt. Art. 15 12 DSGVO Betroffenenrechte. Prüfraster: Identitätsnachweis Vollständigkeitsprüfung Auskunftsinhalt Fristen… |
| `dsgvo-auskunft-antwort` | DSGVO-Auskunftsantwort an Betroffenen vollständig und rechtskonform gestalten. Art. 15 12 Abs. 3 DSGVO Antwortpflicht. Prüfraster: Antwortinhalt Format Fristen Klarheit Weglassungsgründe Begleitschreiben. Output:… |
| `joint-controller-vereinbarung` | Joint-Controller-Vereinbarung nach Art. 26 DSGVO erstellen wenn zwei oder mehr Verantwortliche gemeinsam entscheiden. Art. 26 DSGVO Gemeinsame Verantwortlichkeit. Prüfraster: gemeinsame Zwecke und Mittel… |
| `ki-verordnung-compliance` | KI-Systeme auf Anforderungen der KI-VO und Datenschutz prüfen. KI-VO Risikoklassen Art. 5 9 DSGVO Einwilligung. Prüfraster: Risikoklasse Verbote Hochrisiko-KI Dokumentationspflichten DSGVO-Schnittmengen… |
| `mandantendaten-ki` | Datenschutzkonforme Verwendung von Mandantendaten beim Einsatz von KI-Tools in der Kanzlei prüfen. Art. 5 6 DSGVO BRAO § 43a Verschwiegenheit. Prüfraster: Rechtsgrundlage Zweckbindung Vertraulichkeit Anwaltsprivileg… |
| `regulierungs-luecken-analyse` | Regulatorische Luecken im Datenschutzrecht identifizieren und Handlungsoptionen aufzeigen. Art. 5 6 24 DSGVO BDSG. Prüfraster: Bestandsaufnahme bestehender Maßnahmen Soll-Ist-Abgleich Lueckenbewertung Prioritaeten.… |
| `richtlinien-monitor` | Datenschutzrichtlinien und Unternehmensanweisungen auf Aktualitaet und Konformität monitoren. Art. 24 32 DSGVO TOMs §§ 4 ff. BDSG. Prüfraster: Richtlinienbestand Änderungsbedarf neue Verarbeitungstätigkeiten… |
| `verarbeitungsverzeichnis-vvt-generator` | Verzeichnis der Verarbeitungstätigkeiten nach Art. 30 DSGVO erstellen oder aktualisieren. Art. 30 DSGVO VVT-Pflicht. Prüfraster: Pflichtangaben Art. 30 Abs. 1 Verantwortlicher Zweck Kategorien Empfaenger Fristen… |

## Worum geht es?

Dieses Plugin unterstuetzt Rechtsanwaelte und Datenschutzbeauftragte bei der Bearbeitung datenschutzrechtlicher Mandate nach DSGVO und BDSG. Es deckt den vollstaendigen ab: von der ersten Triage über Auftragsverarbeitungsvertraege, Datenschutz-Folgenabschaetzungen und Auskunftsersuchen bis zu Datenpannenmeldungen, Drittlandstransfers, US-Transfer-Dokumentation und der laufenden Richtlinienpflege.

Der Anwendungsbereich umfasst Unternehmen als Verantwortliche (Art. 4 Nr. 7 DSGVO), Auftragsverarbeiter (Art. 4 Nr. 8 DSGVO) und gemeinsam Verantwortliche (Art. 26 DSGVO), sowie den Einsatz von KI-Tools im Kanzleialltag.

## Wann brauchen Sie diese Skill?

- Ein Unternehmen erhaelt ein Auskunftsersuchen nach Art. 15 DSGVO und braucht eine rechtskonforme Antwort.
- Ein Datenschutzbeauftragter muss eine Datenpanne nach Art. 33 DSGVO binnen 72 Stunden an die Aufsichtsbehoerde melden.
- Eine Kanzlei prüft, ob ein IT-Dienstleister einen Auftragsverarbeitungsvertrag nach Art. 28 DSGVO benoetigt.
- Ein Unternehmen will Daten in ein Drittland (USA, Indien) uebertragen und braucht einen Transfer-Impact-Assessment.
- Eine Aufsichtsbehoerde fragt nach US-Transfer, DPF-Listing, SCC, TIA und Schrems-II-Dokumentation.
- Eine Behörde oder Kanzlei prüft, ob KI-Werkzeuge datenschutzkonform eingesetzt werden können.

## Fachbegriffe (kurz erklaert)

- **DSGVO** — Datenschutz-Grundverordnung (EU 2016/679); einheitliches EU-Datenschutzrecht für Verarbeitung personenbezogener Daten.
- **BDSG** — Bundesdatenschutzgesetz; ergaenzt die DSGVO im deutschen Recht, insbesondere für Beschäftigtendatenschutz (§ 26 BDSG).
- **TDDDG** — Telekommunikation-Digitale-Dienste-Datenschutzgesetz; Nachfolger des TTDSG, regelt Cookies und Online-Tracking.
- **AVV** — Auftragsverarbeitungsvertrag nach Art. 28 DSGVO; Pflichtvertrag, wenn ein Dritter Daten im Auftrag verarbeitet.
- **DSFA** — Datenschutz-Folgenabschaetzung (Data Protection Impact Assessment, DPIA) nach Art. 35 DSGVO; Pflicht bei hohem Risiko.
- **Drittland** — Staat ausserhalb des EWR, in den Datentransfers nur unter bestimmten Voraussetzungen zulässig sind (Art. 44 ff. DSGVO).
- **VVT** — Verzeichnis der Verarbeitungstaetigkeiten nach Art. 30 DSGVO; Dokumentationspflicht für Verantwortliche und Auftragsverarbeiter.
- **DSB** — Datenschutzbeauftragter; Pflichtposition nach Art. 37 DSGVO und § 38 BDSG ab bestimmten Schwellenwerten.

## Rechtsgrundlagen

- Art. 5 DSGVO (Grundsaetze der Verarbeitung)
- Art. 6 DSGVO (Rechtmaessigkeit der Verarbeitung)
- Art. 12-23 DSGVO (Betroffenenrechte)
- Art. 26 DSGVO (Joint Controller)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 30 DSGVO (Verzeichnis der Verarbeitungstaetigkeiten)
- Art. 33-34 DSGVO (Meldepflicht bei Datenpannen)
- Art. 35-36 DSGVO (Datenschutz-Folgenabschaetzung)
- Art. 37-39 DSGVO (Datenschutzbeauftragter)
- Art. 44-49 DSGVO (Drittlandstransfer)
- § 26 BDSG (Beschäftigtendatenschutz)
- § 38 BDSG (Pflicht zur Bestellung eines DSB)

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klären: Verantwortlicher, Auftragsverarbeiter oder gemeinsam Verantwortlicher?
2. Sachverhalt einordnen und Bearbeitungsroute bestimmen (Skill `anwendungsfall-triage`).
3. Mandat strukturieren und Arbeitsbereich abgrenzen (`datenschutzrecht-kaltstart-interview` oder `datenschutzrecht-mandat-arbeitsbereich`).
4. Passenden Fachskill auswaehlen (z. B. AVV, DSFA, Drittlandstransfer, Datenpanne).
5. Eilfristen prüfen: Datenpannenmeldung 72-Stunden-Frist, Auskunftspflicht einen Monat ab Ersuchen.

## Skill-Tour (was gibt es hier?)

- `anwendungsfall-triage` — Datenschutzrechtlichen Sachverhalt einordnen und Bearbeitungsroute bestimmen.
- `datenschutzrecht-kaltstart-interview` — Neues Datenschutzmandat durch strukturiertes Erstgespraech aufnehmen.
- `datenschutzrecht-mandat-arbeitsbereich` — Datenschutzrechtliches Mandat strukturieren und Arbeitsbereich abgrenzen.
- `datenschutzrecht-anpassen` — Bestehende Datenschutzdokumentation oder Richtlinien an neue Anforderungen anpassen.
- `avv-pruefung` — Auftragsverarbeitungsvertrag nach Art. 28 DSGVO prüfen oder erstellen.
- `joint-controller-vereinbarung` — Joint-Controller-Vereinbarung nach Art. 26 DSGVO erstellen, wenn zwei oder mehr Verantwortliche gemeinsam entscheiden.
- `dsfa-erstellung` — Datenschutz-Folgenabschaetzung nach Art. 35 DSGVO durchfuehren bei hohem Risiko.
- `datenpanne-meldung` — Datenpanne nach Art. 33 und 34 DSGVO melden bei Sicherheitsverletzung personenbezogener Daten.
- `dsgvo-auskunft` — Auskunftsersuchen nach Art. 15 DSGVO prüfen und Bearbeitungsstrategie bestimmen.
- `dsgvo-auskunft-antwort` — DSGVO-Auskunftsantwort an Betroffenen vollstaendig und rechtskonform gestalten.
- `drittlandstransfer-pruefung` — Datentransfer in Drittlaender ausserhalb EU und EWR auf Zulaessigkeit prüfen.
- `us-transfer-tia-dokumentation` — US-Transfer mit DPF, SCC/BCR-Ausweichpfad, TIA und ergänzenden Maßnahmen dokumentieren.
- `standardvertragsklauseln-scc-paket` — SCC-Modulwahl, Annex I-III, Subprozessoren und TOMs behördenfest vorbereiten.
- `drittlandtransfer-behoerdenpaket-output` — Deckvermerk, Anlagenverzeichnis, Behördenantwort und Maßnahmenplan ausgeben.
- `dsb-bestellungspflicht-pruefung` — Bestellungspflicht für Datenschutzbeauftragten nach Art. 37 DSGVO und § 38 BDSG prüfen.
- `verarbeitungsverzeichnis-vvt-generator` — Verzeichnis der Verarbeitungstaetigkeiten nach Art. 30 DSGVO erstellen oder aktualisieren.
- `ki-verordnung-compliance` — KI-Systeme auf Anforderungen der KI-VO und Datenschutz gemeinsam prüfen.
- `mandantendaten-ki` — Datenschutzkonforme Verwendung von Mandantendaten beim Einsatz von KI-Tools in der Kanzlei prüfen.
- `regulierungs-luecken-analyse` — Regulatorische Luecken im Datenschutzrecht identifizieren und Handlungsoptionen aufzeigen.
- `richtlinien-monitor` — Datenschutzrichtlinien und Unternehmensanweisungen auf Aktualitaet und Konformitaet monitoren.

## Worauf besonders achten

- Datenpannenmeldung nach Art. 33 DSGVO hat eine 72-Stunden-Frist ab Kenntnisnahme — keine Verzoegerung durch interne Abstimmungsrunden.
- Drittlandstransfer ohne Rechtsgrundlage (Angemessenheitsbeschluss oder Standardvertragsklauseln) ist ein bussgeldrelevanter Verstoss.
- Auftragsverarbeitungsvertraege müssen vor Beginn der Verarbeitung vorliegen — nicht erst nach Vertragsschluss.
- § 26 BDSG-Beschäftigtendatenschutz hat engere Grenzen als die DSGVO-Generalklausel — gesondert prüfen.
- Cookies und Tracking unterliegen zusaetzlich dem TDDDG — einwilligungspflichtige Dienste nicht mit Art. 6 Abs. 1 lit. f DSGVO rechtfertigen.

## Typische Fehler

- Auftragsverarbeitungsvertrag fehlt: Unternehmen gibt Daten an Cloud-Anbieter weiter ohne AVV nach Art. 28 DSGVO.
- DSFA-Pflicht verkannt: Hochrisiko-Verarbeitung (z. B. Profilbildung, Scoring) wird ohne Folgenabschaetzung gestartet.
- Auskunftsantwort unvollstaendig: Betroffener erhaelt keine Information über Empfaenger oder Speicherdauer.
- Drittlandstransfer nach Schrems II nicht geprueft: Alte Safe-Harbor- oder Privacy-Shield-Grundlage wird weiter verwendet.
- DSB-Bestellungspflicht nicht erkannt: Unternehmen beschäftigt mehr als 20 Personen mit Datenverarbeitung, bestellt aber keinen DSB.

## Quellen und Aktualitaet

- Stand: 05/2026
- DSGVO (EU 2016/679) in der zum Stand-Datum geltenden Fassung
- BDSG in der geltenden Fassung
- TDDDG in der geltenden Fassung
- Standardvertragsklauseln der EU-Kommission (2021/914)
- EU-US Data Privacy Framework-Angemessenheitsbeschluss der EU-Kommission vom 10.07.2023 und offizielle DPF-Participant-Search.

---

## Skill: `dsgvo-erstpruefung-und-mandatsziel`

_DSGVO: Erstprüfung, Rollenklärung und Mandatsziel: DSGVO: Erstprüfung, Rollenklärung und Mandatsziel._

# DSGVO: Erstprüfung, Rollenklärung und Mandatsziel


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO; BDSG; TDDDG; Art. 44 ff — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** DSGVO: Erstprüfung, Rollenklärung und Mandatsziel.

## Spezialwissen: DSGVO: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** DSGVO, BDSG, TDDDG, PIA, DPIA, AVV, Art. 15, Art. 33, Art. 44, US, DPF, SCC.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **DSGVO** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## DSGVO-Erstprüfung: 7-Schritte-Matrix
1. **Personenbezug:** Liegen Daten i.S.d. Art. 4 Nr. 1 vor? Pseudonymisierung ohne Schlüssel = noch personenbezogen (BGH); Anonymisierung technisch oft nicht belastbar.
2. **Rolle:** Verantwortlicher (Art. 4 Nr. 7) — entscheidet über Mittel und Zwecke; Auftragsverarbeiter (Art. 4 Nr. 8) — verarbeitet auf Weisung; Gemeinsame Verantwortliche (Art. 26).
3. **Rechtsgrundlage Art. 6:** Einwilligung (lit. a), Vertrag (lit. b), gesetzliche Pflicht (lit. c), berechtigtes Interesse (lit. f) — letzteres mit LIA.
4. **Besondere Kategorien Art. 9?** Gesundheit, Religion, sexuelle Orientierung, biometrische ID, ethnische Herkunft — eigene Rechtsgrundlage.
5. **DSFA-Pflicht Art. 35?** Bei voraussichtlich hohem Risiko (Profiling, sensible Daten, neue Technologien, Beobachtung öffentl. Bereich).
6. **Drittlandstransfer:** EU/EWR/Adäquanzbeschluss → frei. USA → DPF/SCC + TIA. Sonstige → SCC + TIA.
7. **Ziel:** Compliance-Aufbau, Auskunft beantworten, Datenpanne melden, Behörde verteidigen?

## Trade-off
Einwilligung (Art. 6 Abs. 1 lit. a) ist klar, aber jederzeit widerrufbar (Art. 7 Abs. 3) — bei laufender Verarbeitung problematisch (z. B. KI-Modell-Training). Berechtigtes Interesse (lit. f) ist robuster, aber abwägungsanfällig — dokumentierte LIA (Legitimate Interest Assessment) ist Pflicht.

---

## Skill: `datenschutz-schadensersatz-art-82-dsgvo-gerichtsstreit`

_Schadensersatzklage nach Art. 82 DSGVO materieller und immaterieller Schaden vor deutschen Zivilgerichten. EuGH C-300/21 Oesterreichische Post C-340/21 Bulgarian Sofia C-687/21 MediaMarkt C-741/21 juris GmbH C-456/22 VX gegen Saale. Sieben-Fragen-Diagnose Anspruchsteller oder Anspruchsgegner Verstoss konkret Kausalitaet Schadensart Beweislast Verjaehrung Anspruchskonkurrenz. Schritt-fuer-Schritt fuer Klage und Verteidigung. Mustertexte Klageschrift Klageerwiderung Vergleichsvorschlag. Abgrenzung: keine Bussgeldverteidigung._

# Datenschutz Schadensersatz — Gerichtsstreit nach Art. 82 DSGVO

## Zweck

Dieser Skill bearbeitet Schadensersatzansprueche nach Art. 82 DSGVO vor deutschen Zivilgerichten — sowohl auf Klaeger- als auch auf Beklagtenseite. Er konzentriert sich auf den materiellen und immateriellen Schaden, die Kausalitaet zum DSGVO-Verstoss und die Beweislastverteilung nach der inzwischen verfestigten EuGH-Rechtsprechung.

## Wann brauchen Sie diesen Skill / Kaltstart-Fragen

Sie brauchen den Skill, sobald (a) ein Betroffener Schadensersatz vom Mandanten verlangt oder (b) der Mandant gegen einen Verantwortlichen vorgehen will.

Sieben-Fragen-Diagnose:

1. **Anspruchsteller oder Anspruchsgegner?** Andere Schritte je nach Seite.
2. **Welcher konkrete Verstoss?** Norm und Sachverhalt — nicht pauschal "DSGVO verletzt".
3. **Kausalitaet:** Welcher Schaden hat sich aus welchem Verstoss konkret entwickelt? Kausalkette schriftlich.
4. **Schadensart:** Materiell (Vermoegen) und/oder immateriell (Gefuehl, Kontrollverlust, Sorge)? Hoehe geschaetzt?
5. **Beweislast:** Wer muss was beweisen — Verantwortlicher entlastet sich nach Art. 82 III DSGVO, dass er nicht verantwortlich ist; Klaeger muss Verstoss und Schaden darlegen.
6. **Verjaehrung:** Art. 82 selbst regelt nichts; nach BGH-Rspr. § 195 BGB drei Jahre ab Kenntnis.
7. **Anspruchskonkurrenz:** UWG, BDSG § 83, deliktische Ansprueche §§ 823 ff. BGB?

## Rechtlicher Rahmen

- **Art. 82 I DSGVO** Jede Person, die einen materiellen oder immateriellen Schaden erlitten hat, hat Anspruch gegen den Verantwortlichen oder Auftragsverarbeiter.
- **Art. 82 II DSGVO** Verantwortlicher haftet fuer Schaeden aus Verarbeitungen; Auftragsverarbeiter nur bei Pflichtverletzung gegen DSGVO-Auftragsverarbeiterspflichten oder Weisung.
- **Art. 82 III DSGVO** Entlastung des Verantwortlichen oder Auftragsverarbeiters bei Nachweis, in keinerlei Hinsicht verantwortlich.
- **Art. 82 IV DSGVO** Gesamtschuld bei mehreren Verantwortlichen.
- **EuGH C-300/21 Oesterreichische Post** (Urteil 04.05.2023): Kein blosser Verstoss reicht; konkreter Schaden notwendig; keine Erheblichkeitsschwelle.
- **EuGH C-340/21 Bulgarian Sofia** (Urteil 14.12.2023): Auch blosse Sorge vor Datenmissbrauch kann immaterieller Schaden sein; Verantwortlicher hat TOM-Pflicht und Beweislast fuer Geeignetheit; Hackerangriff allein entlastet nicht.
- **EuGH C-687/21 MediaMarkt** (Urteil 25.01.2024): Befuerchtungen Betroffener koennen Schaden begruenden; konkretes Ausmass und Kausalitaet sind zu pruefen.
- **EuGH, Urt. v. 11.04.2024 - C-741/21 (juris GmbH):** Verschulden und Schaden — Art. 82 DSGVO setzt Verschulden voraus; Hoehe nach nationalem Recht, aber unter Beachtung Effektivitaet und Aequivalenz.
- **EuGH C-456/22 VX/Saale** (Urteil 14.12.2023): Schadensersatz hat kompensatorische und keine Straffunktion; auch geringe Schadenshoehen moeglich.
- **BGH VI ZR 1148/22** (Urteil 18.11.2024): Bei DSGVO-Verstoss zeitnah Kontrollverlust und Folgen darzulegen; pauschale Behauptung reicht nicht.
- **Art. 79 II DSGVO** Gerichtsstand am Sitz des Verantwortlichen oder gewoehnlichen Aufenthaltsort des Betroffenen.
- **§ 195 BGB** drei Jahre.

## Mandantenfuehrung Schritt-fuer-Schritt

### Klaegerseite

1. **Zuerst:** Beleg-Akte anlegen — Mailverkehr, Screenshots, Auskunftsersuchen nach Art. 15 DSGVO mit Antwort.
2. **Als zweites:** Schadensdarstellung konkretisieren — Gefuehlssituation, zeitlicher Verlauf, Folgen (Sorge, Kontrollverlust, Aengste, konkrete Aufwendungen).
3. **Als drittes:** Klage einreichen — Gerichtsstand Art. 79 II DSGVO, regelmaessig Amtsgericht bis 5.000 EUR.

### Beklagtenseite

1. **Zuerst:** Klageerwiderungsfrist sichern (§ 277 ZPO).
2. **Als zweites:** Tatbestand pruefen — Verstoss nachweisbar? TOM Art. 32 dokumentiert? Belege fuer entlastenden Nachweis Art. 82 III?
3. **Als drittes:** Kausalitaet und Schaden bestreiten — Erhalt von Spam-Mails, Wechselgefuehle ohne konkrete Folge sind nach EuGH C-300/21 nicht ausreichend; aber Sorge kann nach EuGH C-340/21 reichen.
4. **NICHT vorschnell anerkennen:** Auch nicht "aus Goodwill", da Praezedenz fuer weitere Verfahren.
5. **Vergleich erwaegen:** Bei klarer Beweislast lieber Vergleich als Praezedenzurteil.

## Trade-off-Matrix

| Variante | Vorteil | Nachteil |
|---|---|---|
| Klage mit hohem Streitwert | Maximale Forderung | Hohe Vorschuesse, Risiko Klageabweisung |
| Streitwertbegrenzung Amtsgericht | Schnell, kostenarm | Reicht oft nicht fuer Praezedenz |
| Vergleich vor Klage | Schnelle Erledigung | Keine Klaerung, Wiederholungsrisiko |
| Vollstaendige Verteidigung | Praezedenz, klare Rechtslage | Reputationsrisiko, Folgeklagen |

## Mustertexte

### Klageschrift (Kerntext)

> Klage wegen Schadensersatzes nach Art. 82 DSGVO
>
> Klaeger: [Person, Anschrift]
> Beklagte: [Verantwortlicher, Anschrift]
> Streitwert: vorlaeufig [Betrag]
>
> Antrag: Die Beklagte wird verurteilt, an die Klaegerseite [Betrag] nebst Zinsen in Hoehe von fuenf Prozentpunkten ueber dem Basiszinssatz seit Rechtshaengigkeit zu zahlen.
>
> Begruendung:
> I. Sachverhalt (konkret Vorfall, Datum, Datenkategorie).
> II. Rechtlicher Rahmen (Art. 82 I DSGVO, EuGH C-300/21, EuGH C-340/21).
> III. Konkrete Pflichtverletzung (DSGVO-Norm).
> IV. Kausaler Schaden (immateriell mit Sorge, Kontrollverlust; materiell mit konkretem Betrag).
> V. Hoehe (Begruendung der Schaetzung).
> VI. Gerichtsstand Art. 79 II DSGVO.

### Klageerwiderung — Kernpunkte

> 1. Verstoss bestreiten oder relativieren (welche DSGVO-Norm konkret und Subsumtion).
> 2. Schaden bestreiten: blosse Sorge ohne Substanz reicht nach BGH VI ZR 1148/22 nicht; konkrete Folgen notwendig.
> 3. Kausalitaet bestreiten — auch bei TOM-Pflichtverletzung muss Schaden konkret aus Verletzung resultieren.
> 4. Entlastung Art. 82 III: TOM Art. 32 lagen vor (Anlage), Massnahmen waren angemessen.
> 5. Verjaehrung pruefen (§ 195 BGB).
> 6. Hilfsweise Minderung der Hoehe (EuGH C-456/22: kompensatorisch, nicht praeventiv).

## Typische Fehler

- Pauschale Schadensbehauptung "Kontrollverlust" ohne konkrete Substanz (BGH VI ZR 1148/22).
- TOM-Pflicht Art. 32 unterschaetzt — Beklagte muss Massnahmen aktiv belegen.
- Verschuldensfrage nach EuGH C-741/21 uebersehen.
- Streitwert zu hoch angesetzt — bei AG-Zustaendigkeit Vorbehalt.
- Verjaehrung nicht gerueckpruefte (§ 195 BGB drei Jahre ab Kenntnis).

**Was triggert hohe Schadensersatzbetraege?** Art. 9-Daten, Massenvorfall, nachweisbare Kettenfolge (Identitaetsdiebstahl), fehlende Reaktion des Verantwortlichen, kein DSB.

## Querverweise

- `datenschutz-erstgespraech-mandantenmatrix-7-fragen`
- `datenschutz-auskunftsersuchen-art-15-praxis`
- `datenschutz-bussgeldverfahren-art-83-dsgvo-verteidigung`
- `dsr-schadensersatz-art82-spezial`
- `datenschutz-datenpanne-art-33-34-72h-incident-response`

## Quellen Stand 06/2026

- DSGVO Art. 79, 82, 83.
- BGB § 195, § 199, § 823, § 826.
- BGH VI ZR 1148/22, Urteil 18.11.2024 (zu pauschalen Behauptungen Kontrollverlust).
- EuGH C-300/21 Oesterreichische Post, Urteil 04.05.2023.
- EuGH C-340/21 Bulgarian Sofia, Urteil 14.12.2023.
- EuGH C-687/21 MediaMarkt, Urteil 25.01.2024.
- EuGH, Urt. v. 11.04.2024 - C-741/21 (juris GmbH), vor Ausgabe über curia.europa.eu verifizieren.
- EuGH C-456/22 VX gegen Saale, Urteil 14.12.2023.
- Keine Aufsatzfundstellen aus Modellwissen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

---

## Skill: `datenschutz-mandatssteckbrief-fristen-rollen`

_Datenschutzrechtliches Mandat strukturieren und Arbeitsbereich abgrenzen. Art. 5 24 DSGVO §§ 1 ff. BDSG. Prüfraster: Mandatsumfang Zuständigkeiten Fristen Risikostufe externe Datenschutzberatung. Output: Mandatssteckbrief Arbeitsplan Rollenverteilung. Abgrenzung: nicht für inhaltliche Datenschutzprüfung._

# Datenschutzmandat: Steckbrief, Fristen, Rollen und Kontexttrennung

## Zweck

Isolation von Datenschutzmandaten in Mehrmandat-Kanzleien: Jeder Mandant erhält einen eigenen Arbeitsbereich mit eigener Mandatsdatei (`mandat.md`). Skills lesen das kanzlei-weite Praxisprofil (`CLAUDE.md`) für kanzleiweite Regeln und die mandatsspezifische Datei für mandatsspezifische Fakten. Kontext, Erkenntnisse und Ausgaben fließen nicht zwischen Mandaten durch.

**Nur relevant für Mehrmandat-Kanzleien.** Bei internem Unternehmenseinsatz (ein Verantwortlicher) ist dieser Skill deaktiviert; Skills verwenden das Praxisprofil direkt.

Beachte: Mandantendaten unterliegen § 43a Abs. 2 BRAO, § 203 StGB. Mandatsisolation ist datenschutz- und berufsrechtliche Pflicht.

## Eingaben

- Befehlsform: `neu | liste | wechsle [Mandat-ID] | schließe [Mandat-ID] | keins`
- Bei `neu`: Mandantenname, kurze Beschreibung des Datenschutzmandats, Mandats-ID (Kürzel)
- Bei `wechsle`: Mandat-ID des Zielmandats

## Ablauf

### `neu` – Neues Mandat anlegen

1. Mandat-ID vergeben (Kürzel, z.B. `mand-2024-04-mueller-dsfa`).
2. Verzeichnis anlegen: `~/.claude/plugins/config/claude-fuer-deutsches-recht/datenschutzrecht/mandate/[mandat-id]/`
3. Leere `mandat.md` mit Pflichtfeldern anlegen (s. Struktur unten).
4. Aktives Mandat in Praxisprofil auf neue ID setzen.
5. Bestätigung ausgeben: "Mandat [ID] angelegt. Alle folgenden Skill-Aufrufe arbeiten in diesem Mandatskontext."

### `liste` – Mandatsübersicht

Alle Verzeichnisse unter `mandate/` auflisten:
| Mandat-ID | Mandant | Beschreibung | Status | Letzte Aktivität |
|---|---|---|---|---|
| … | … | … | offen / abgeschlossen | Datum |

### `wechsle [Mandat-ID]` – Mandat wechseln

1. Mandat-ID aus Liste verifizieren.
2. Aktives Mandat in Praxisprofil auf neue ID setzen.
3. Bestätigung ausgeben; laufende offene Aufgaben im alten Mandat nennen, falls vorhanden.

### `schließe [Mandat-ID]` – Mandat abschließen

1. Status in `mandat.md` auf "abgeschlossen" und Abschlussdatum setzen.
2. Aktives Mandat zurücksetzen (auf "keins").
3. Ausgabedateien des Mandats sind weiter zugänglich, werden aber nicht mehr von Skills aktiv gelesen.

### `keins` – Kanzlei-Kontext (kein aktives Mandat)

Skills arbeiten im kanzlei-weiten Praxisprofil ohne mandatsspezifischen Kontext. Sinnvoll für allgemeine Kanzlei-Konfiguration oder Skills die sich auf die gesamte Kanzlei beziehen (z.B. Policy-Monitor für kanzlei-interne Richtlinien).

## Matter.md-Struktur

```markdown
# Mandat: [Mandat-ID]

## Mandant
- **Name:** [Mandantenname]
- **Rechtsform:** [GmbH / AG / Einzelperson / öffentliche Stelle]
- **Branche:** [Branche]
- **Hauptniederlassung:** [Bundesland]
- **Rolle Mandant:** [Verantwortlicher / Auftragsverarbeiter / beides]

## Mandatsbeschreibung
[Kurzbeschreibung: Was ist der Auftrag? Welches datenschutzrechtliche Vorhaben?]

## Zuständige Aufsichtsbehörde (Mandant)
[BfDI / LfDI [Bundesland]]

## Ansprechpartner
- **Mandant:** [Name, E-Mail]
- **DSB Mandant:** [Name oder "nicht bestellt"]
- **Kanzlei intern:** [zuständige·r Anwalt/Anwältin]

## Abweichungen vom Kanzlei-Praxisprofil
[Nur aufführen, was beim Mandanten anders ist als im kanzlei-weiten Profil]
- Rechtsgrundlage: [...]
- AVV-Positionen: [...]
- DSFA-Auslöser: [...]

## Systemliste Mandant (für Betroffenenanfragen Art. 15 DSGVO)
- [System 1]
- [System 2]

## Verarbeitungsverzeichnis
[Pfad oder "noch nicht bereitgestellt"]

## Ausgaben dieses Mandats
[Ordnerpfad oder Auflistung erstellter Dokumente]

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Status
offen / abgeschlossen
**Abgeschlossen am:** [Datum]
```

## Quellen und Zitierweise

Verbindlich nach `../../references/zitierweise.md`.

- § 43a Abs. 2 BRAO (Verschwiegenheitspflicht Rechtsanwalt)
- § 203 StGB (Verletzung von Privatgeheimnissen, Berufsgeheimnisträgerpflicht)
- Art. 28, 29 DSGVO (Auftragsverarbeitung bei Nutzung externer Systeme)
- Art. 25 DSGVO (Datenschutz durch Technikgestaltung – Mandatsisolation als TOMs)
- Zuck, in: Zuck/Lenz, Anwaltsrecht, 2. Aufl. 2018, § 43a BRAO Rn. 15 ff. (Berufsgeheimnis).

## Ausgabeformat

- Kurzbestätigungen (angelegt, gewechselt, geschlossen) als einzeilige Statusnachricht
- Mandatsübersicht als Tabelle
- `mandat.md` als vollständig befülltes Dokument

## Risiken / typische Fehler

- **Mandatsisolation nicht gewährleistet:** Wenn Skills ohne aktives Mandat auf mandatsspezifische Daten zugreifen oder mandatsübergreifend aggregieren, verletzt dies § 43a Abs. 2 BRAO und Art. 5 Abs. 1 lit. f DSGVO (Integrität und Vertraulichkeit).
- **Keine Löschung abgeschlossener Mandate:** Ordner nicht löschen – Aktenaufbewahrungspflicht nach § 50 Abs. 1 BRAO (6 Jahre nach Ablauf des Kalenderjahres, in dem das Mandat endete).
- **Mandant ist selbst AV:** Wenn der Mandant selbst Auftragsverarbeiter eines Dritten ist, kann das Datenschutzmandat vertikale Sub-AV-Fragen berühren (Art. 28 Abs. 2 Satz 2 DSGVO). In `mandat.md` explizit vermerken.
- **Aktives Mandat nicht zurückgesetzt:** Nach Mandatswechsel immer prüfen, dass kein unbeabsichtigter Mandatskontext aktiv ist. Standardbefehl `keins` nach Mandatsabschluss empfohlen.

## Quellen / Updates

Stand: 05/2026. Aktualität prüfen bei Änderungen der BRAO (Aktenaufbewahrungspflicht § 50 BRAO), StGB § 203 oder DSGVO-Anforderungen an technische Isolation.

**Querverweise:**
- `datenschutzrecht/skills/mandantendaten-ki/SKILL.md` — Mandatsisolation bei KI-Diensten
- `datenschutzrecht/skills/avv-pruefung/SKILL.md` — Mandatsspezifische AVV-Prüfung

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage zu Beginn

1. Wie viele Mandate/Mandanten sind gleichzeitig aktiv?
2. Sind die Mandate datenschutzrechtlich voneinander zu isolieren (unterschiedliche Verantwortliche)?
3. Liegt ein Interessenkonflikt zwischen Mandaten vor?
4. Sollen mandatsspezifische Praxisprofile (unterschiedliche AVV-Playbooks) genutzt werden?

## Output-Template — Mandatsarbeitsbereich-Status

**Adressat:** Kanzlei intern — Tonfall: sachlich-strukturiert

```
Mandatsarbeitsbereich-Übersicht [DATUM]
Aktive Arbeitsbereich-IDs:
- [ID_1]: [MANDANT/PROJEKT] | Status: aktiv/geschlossen | Kontext: isoliert
- [ID_2]: [MANDANT/PROJEKT] | Status: aktiv | Kontext: isoliert

Aktuell aktiver Kontext: [ID_X]
Sicherheitshinweis: Kontextleak zwischen Mandaten wurde verhindert.
Letzter Wechsel: [DATUM, UHRZEIT]
```

---

## Skill: `datenschutz-schadensersatz-art-82-dsgvo`

_Schadensersatzklage nach Art. 82 DSGVO materieller und immaterieller Schaden vor deutschen Zivilgerichten. EuGH C-300/21 Oesterreichische Post C-340/21 Bulgarian Sofia C-687/21 MediaMarkt C-741/21 juris GmbH C-456/22 VX gegen Saale. Sieben-Fragen-Diagnose Anspruchsteller oder Anspruchsgegner Verstoss..._

# Datenschutz Schadensersatz — Gerichtsstreit nach Art. 82 DSGVO

## Wann dieses Modul hilft / Kaltstart-Fragen

Sie brauchen den Skill, sobald (a) ein Betroffener Schadensersatz vom Mandanten verlangt oder (b) der Mandant gegen einen Verantwortlichen vorgehen will.

Sieben-Fragen-Diagnose:

1. **Anspruchsteller oder Anspruchsgegner?** Andere Schritte je nach Seite.
2. **Welcher konkrete Verstoss?** Norm und Sachverhalt — nicht pauschal "DSGVO verletzt".
3. **Kausalitaet:** Welcher Schaden hat sich aus welchem Verstoss konkret entwickelt? Kausalkette schriftlich.
4. **Schadensart:** Materiell (Vermögen) und/oder immateriell (Gefuehl, Kontrollverlust, Sorge)? Höhe geschaetzt?
5. **Beweislast:** Wer muss was beweisen — Verantwortlicher entlastet sich nach Art. 82 III DSGVO, dass er nicht verantwortlich ist; Kläger muss Verstoss und Schaden darlegen.
6. **Verjährung:** Art. 82 selbst regelt nichts; nach BGH-Rspr. § 195 BGB drei Jahre ab Kenntnis.
7. **Anspruchskonkurrenz:** UWG, BDSG § 83, deliktische Ansprueche §§ 823 ff. BGB?

## Rechtlicher Rahmen

- **Art. 82 I DSGVO** Jede Person, die einen materiellen oder immateriellen Schaden erlitten hat, hat Anspruch gegen den Verantwortlichen oder Auftragsverarbeiter.
- **Art. 82 II DSGVO** Verantwortlicher haftet für Schaeden aus Verarbeitungen; Auftragsverarbeiter nur bei Pflichtverletzung gegen DSGVO-Auftragsverarbeiterspflichten oder Weisung.
- **Art. 82 III DSGVO** Entlastung des Verantwortlichen oder Auftragsverarbeiters bei Nachweis, in keinerlei Hinsicht verantwortlich.
- **Art. 82 IV DSGVO** Gesamtschuld bei mehreren Verantwortlichen.
- **EuGH C-300/21 Oesterreichische Post** (Urteil 04.05.2023): Kein blosser Verstoss reicht; konkreter Schaden notwendig; keine Erheblichkeitsschwelle.
- **EuGH C-340/21 Bulgarian Sofia** (Urteil 14.12.2023): Auch blosse Sorge vor Datenmissbrauch kann immaterieller Schaden sein; Verantwortlicher hat TOM-Pflicht und Beweislast für Geeignetheit; Hackerangriff allein entlastet nicht.
- **EuGH C-687/21 MediaMarkt** (Urteil 25.01.2024): Befürchtungen Betroffener können Schaden begruenden; konkretes Ausmass und Kausalitaet sind zu prüfen.
- **EuGH, Urt. v. 11.04.2024 - C-741/21 (juris GmbH):** Verschulden und Schaden — Art. 82 DSGVO setzt Verschulden voraus; Höhe nach nationalem Recht, aber unter Beachtung Effektivitaet und Äquivalenz.
- **EuGH C-456/22 VX/Saale** (Urteil 14.12.2023): Schadensersatz hat kompensatorische und keine Straffunktion; auch geringe Schadenshoehen möglich.
- **BGH VI ZR 1148/22** (Urteil 18.11.2024): Bei DSGVO-Verstoss zeitnah Kontrollverlust und Folgen darzulegen; pauschale Behauptung reicht nicht.
- **Art. 79 II DSGVO** Gerichtsstand am Sitz des Verantwortlichen oder gewoehnlichen Aufenthaltsort des Betroffenen.
- **§ 195 BGB** drei Jahre.

## Mandantenfuehrung Schritt-für-Schritt

### Klägerseite

1. **Zuerst:** Beleg-Akte anlegen — Mailverkehr, Screenshots, Auskunftsersuchen nach Art. 15 DSGVO mit Antwort.
2. **Als zweites:** Schadensdarstellung konkretisieren — Gefuehlssituation, zeitlicher Verlauf, Folgen (Sorge, Kontrollverlust, Aengste, konkrete Aufwendungen).
3. **Als drittes:** Klage einreichen — Gerichtsstand Art. 79 II DSGVO, regelmaessig Amtsgericht bis 5.000 EUR.

### Beklagtenseite

1. **Zuerst:** Klageerwiderungsfrist sichern (§ 277 ZPO).
2. **Als zweites:** Tatbestand prüfen — Verstoss nachweisbar? TOM Art. 32 dokumentiert? Belege für entlastenden Nachweis Art. 82 III?
3. **Als drittes:** Kausalitaet und Schaden bestreiten — Erhalt von Spam-Mails, Wechselgefuehle ohne konkrete Folge sind nach EuGH C-300/21 nicht ausreichend; aber Sorge kann nach EuGH C-340/21 reichen.
4. **NICHT vorschnell anerkennen:** Auch nicht "aus Goodwill", da Praezedenz für weitere Verfahren.
5. **Vergleich erwaegen:** Bei klarer Beweislast lieber Vergleich als Praezedenzurteil.

## Trade-off-Matrix

| Variante | Vorteil | Nachteil |
|---|---|---|
| Klage mit hohem Streitwert | Maximale Forderung | Hohe Vorschuesse, Risiko Klageabweisung |
| Streitwertbegrenzung Amtsgericht | Schnell, kostenarm | Reicht oft nicht für Praezedenz |
| Vergleich vor Klage | Schnelle Erledigung | Keine Klärung, Wiederholungsrisiko |
| Vollstaendige Verteidigung | Praezedenz, klare Rechtslage | Reputationsrisiko, Folgeklagen |

## Mustertexte

### Klageschrift (Kerntext)

> Klage wegen Schadensersatzes nach Art. 82 DSGVO
>
> Kläger: [Person, Anschrift]
> Beklagte: [Verantwortlicher, Anschrift]
> Streitwert: vorlaeufig [Betrag]
>
> Antrag: Die Beklagte wird verurteilt, an die Klägerseite [Betrag] nebst Zinsen in Höhe von fuenf Prozentpunkten über dem Basiszinssatz seit Rechtshaengigkeit zu zahlen.
>
> Begruendung:
> I. Sachverhalt (konkret Vorfall, Datum, Datenkategorie).
> II. Rechtlicher Rahmen (Art. 82 I DSGVO, EuGH C-300/21, EuGH C-340/21).
> III. Konkrete Pflichtverletzung (DSGVO-Norm).
> IV. Kausaler Schaden (immateriell mit Sorge, Kontrollverlust; materiell mit konkretem Betrag).
> V. Höhe (Begruendung der Schaetzung).
> VI. Gerichtsstand Art. 79 II DSGVO.

### Klageerwiderung — Kernpunkte

> 1. Verstoss bestreiten oder relativieren (welche DSGVO-Norm konkret und Subsumtion).
> 2. Schaden bestreiten: blosse Sorge ohne Substanz reicht nach BGH VI ZR 1148/22 nicht; konkrete Folgen notwendig.
> 3. Kausalitaet bestreiten — auch bei TOM-Pflichtverletzung muss Schaden konkret aus Verletzung resultieren.
> 4. Entlastung Art. 82 III: TOM Art. 32 lagen vor (Anlage), Maßnahmen waren angemessen.
> 5. Verjährung prüfen (§ 195 BGB).
> 6. Hilfsweise Minderung der Höhe (EuGH C-456/22: kompensatorisch, nicht praeventiv).

## Typische Fehler

- Pauschale Schadensbehauptung "Kontrollverlust" ohne konkrete Substanz (BGH VI ZR 1148/22).
- TOM-Pflicht Art. 32 unterschaetzt — Beklagte muss Maßnahmen aktiv belegen.
- Verschuldensfrage nach EuGH C-741/21 uebersehen.
- Streitwert zu hoch angesetzt — bei AG-Zuständigkeit Vorbehalt.
- Verjährung nicht gerueckpruefte (§ 195 BGB drei Jahre ab Kenntnis).

**Was triggert hohe Schadensersatzbetraege?** Art. 9-Daten, Massenvorfall, nachweisbare Kettenfolge (Identitaetsdiebstahl), fehlende Reaktion des Verantwortlichen, kein DSB.

## Quellen Stand 06/2026

- DSGVO Art. 79, 82, 83.
- BGB § 195, § 199, § 823, § 826.
- BGH VI ZR 1148/22, Urteil 18.11.2024 (zu pauschalen Behauptungen Kontrollverlust).
- EuGH C-300/21 Oesterreichische Post, Urteil 04.05.2023.
- EuGH C-340/21 Bulgarian Sofia, Urteil 14.12.2023.
- EuGH C-687/21 MediaMarkt, Urteil 25.01.2024.
- EuGH, Urt. v. 11.04.2024 - C-741/21 (juris GmbH), vor Ausgabe über curia.europa.eu verifizieren.
- EuGH C-456/22 VX gegen Saale, Urteil 14.12.2023.
- Keine Aufsatzfundstellen aus Modellwissen.

---

## Skill: `anpassen`

_Bestehende Datenschutzdokumentation oder Richtlinien an neue Anforderungen oder Verarbeitungstätigkeiten anpassen. Art. 5 24 DSGVO Rechenschaftspflicht. Prüfraster: Bestandsaufnahme Lueckenanalyse DSGVO-Anforderungen BDSG-Besonderheiten Anpassungsbedarf. Output: Anpassungsprotokoll ueberarbeitete..._

# Customize – Praxisprofil anpassen

## Eingaben

- Welcher Abschnitt soll geändert werden? (frei formuliert oder Menüauswahl)
- Neuer Wert oder neue Position
- Optional: Beleg für die Änderung (z.B. neues Gerichtsurteil, neue EDSA-Leitlinie, Managemententscheidung)

## Ablauf

1. **Abschnitt identifizieren.** Nutzer nennt, was geändert werden soll. Bei Unklarheit eine strukturierte Liste der änderbaren Bereiche anzeigen:
 - Organisationsdaten (Name, Rechtsform, Standort)
 - Zuständige Aufsichtsbehörde
 - Rolle (Verantwortlicher / Auftragsverarbeiter)
 - Datenschutzbeauftragte·r (Name, intern/extern)
 - Rechtsgrundlagen-Übersicht (Art. 6/9 DSGVO)
 - AVV-Playbook (Klausel-Positionen, Deal-Breaker)
 - Drittlandtransfer-Mechanismen (SCC, DPF, BCR)
 - Systemliste für Betroffenenanfragen
 - DSFA-Format und Auslöser
 - Datenschutzerklärungsangaben
 - Ausgaben-Konfiguration (Ordner, Namenskonvention)
 - Integrations-Einstellungen

2. **Aktuellen Wert zeigen.** Den aktuellen Wert aus `CLAUDE.md` lesen und ausgeben, damit der Nutzer die Änderung klar gegen den Ist-Zustand vergleichen kann.

3. **Änderung vorbereiten.** Neuen Wert formulieren. Bei normativen Änderungen (z.B. neue Aufsichtsbehörde wegen Art. 56 DSGVO) die Rechtsgrundlage der Änderung nennen.

4. **Bestätigung einholen.** Den geplanten Schreibvorgang explizit bestätigen lassen – vor dem Überschreiben.

5. **Schreiben.** `CLAUDE.md` an der betroffenen Stelle aktualisieren. Rest unverändert lassen.

6. **Zusammenfassung.** Was wurde geändert, was blieb unverändert, gibt es Folgeaktionen (z.B. Datenschutzerklärung aktualisieren nach geänderter Systemliste)?

## Quellen und Zitierweise

Verbindlich nach `../../references/zitierweise.md`.

- Art. 56 DSGVO (federführende Aufsichtsbehörde)
- Art. 37 DSGVO, § 38 BDSG (DSB-Benennungspflicht)
- Art. 28 DSGVO (AVV-Mindestanforderungen für Playbook-Änderungen)
- Art. 46, 47, 49 DSGVO (Drittlandtransfer-Mechanismen)
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Beispiel

**Situation:** Das Unternehmen zieht seinen Hauptsitz von Bayern nach Hessen.

**Analyse:**
Die Zuständigkeit der Aufsichtsbehörde richtet sich nach der Hauptniederlassung in der EU, Art. 56 Abs. 1 DSGVO. Mit Umzug nach Hessen wechselt die federführende Aufsichtsbehörde vom Bayerischen Landesamt für Datenschutzaufsicht (BayLDA) zum Hessischen Beauftragten für Datenschutz und Informationsfreiheit (HBDI). Für laufende Aufsichtsverfahren beim BayLDA ist der Wechsel mit Hauptniederlassungsverlegung dem BayLDA mitzuteilen (Art. 60 Abs. 1 DSGVO analog, h.M.).

**Änderung:**
```
Zuständige Aufsichtsbehörde: HBDI (zuvor: BayLDA)
Rechtsgrundlage: Art. 56 Abs. 1 DSGVO
Datum: [Umzugsdatum]
Folgeaktionen: Laufende Verfahren beim BayLDA auf HBDI übertragen; Datenschutzerklärung (Aufsichtsbehördenverweis) aktualisieren; Kontaktdaten HBDI in CLAUDE.md einpflegen.
```

## Risiken / typische Fehler

- **Teilaktualisierung vergessen:** Wer den DSB wechselt, muss auch die Datenschutzerklärung und ggf. das Verarbeitungsverzeichnis (Art. 30 Abs. 1 lit. a DSGVO: Name und Kontakt DSB) aktualisieren.
- **AVV-Playbook ohne Begründung:** Änderungen an Klauselpositionen sollten mit Datum und Anlass dokumentiert werden (Präzedenzfall, Gerichtsurteil, Managemententscheidung), damit spätere Prüfer die Position nachvollziehen können.
- **Integrations-Änderungen ohne Test:** Neue Connector-Einstellung erst nach erfolgreichem Test-Aufruf als ✓ markieren.
- **Überschreiben von Mandats-Ebene:** Wenn Mandat-Arbeitsbereiche aktiviert sind, prüfen, ob die Änderung das Praxisprofil oder nur ein einzelnes Mandat betrifft. Mandat-Ebene überschreibt Praxisprofil nur für dieses Mandat.

## Quellen / Updates

Stand: 05/2026. Bei BDSG-Novellen, neuen BRAO-Regeln oder Aufsichtsbehörden-Neustrukturierungen Skill aktualisieren.

**Querverweise:**
- `datenschutzrecht/skills/datenschutzrecht-kaltstart-interview/SKILL.md` — Vollständige Neukonfiguration
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — Drittlandtransfer-Mechanismen im Praxisprofil

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage zu Beginn

1. Was genau soll geändert werden? (Aufsichtsbehörde / AVV-Dealbreaker / Systemliste / DSB)
2. Hat die Änderung Auswirkungen auf andere Dokumente (Datenschutzerklärung, VVT, DSFA)?
3. Liegt ein Beleg (Urteil, EDSA-Leitlinie, Managemententscheidung) für die Änderung vor?
4. Betrifft die Änderung das Praxisprofil oder nur ein einzelnes Mandat?

## Output-Template — Änderungsbestätigung

**Adressat:** Datenschutzbeauftragter / Kanzlei intern — Tonfall: sachlich-strukturiert

```
Praxisprofil-Änderungsprotokoll [DATUM]
Abschnitt: [ABSCHNITT]
Alter Wert: [ALTER WERT]
Neuer Wert: [NEUER WERT]
Beleg/Rechtsgrundlage: [NORM / BESCHLUSS / DATUM]
Folgeaktionen:
- Datenschutzerklaerung aktualisieren: [ja/nein]
- VVT aktualisieren: [ja/nein]
- Aufsichtsbehoerde informieren: [ja/nein]
- Weitere: [...]
Durchgefuehrt von: [SACHBEARBEITER]
```

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 DSGVO (Grundsätze der Verarbeitung)
- Art. 6, 9 DSGVO (Rechtsgrundlagen, besondere Datenkategorien)
- Art. 13, 14 DSGVO (Informationspflichten)
- Art. 15 DSGVO (Auskunftsrecht)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 33, 34 DSGVO (Meldepflichten bei Verletzung)
- Art. 82 DSGVO (Schadensersatz)
- Art. 83 DSGVO (Bußgelder)
- §§ 4, 20, 41 BDSG (Aufsicht, Rechtsweg, Strafvorschriften)

### Leitentscheidungen

- EuGH C-300/21 (immaterieller Schaden Art. 82 DSGVO)
- EuGH C-634/21 (automatisierte Bonitätsbewertung Schufa)
- EuGH C-26/22 (Datenschutzbehörden-Befugnisse)
- EuGH C-807/21 (Bußgeldhaftung juristischer Personen)
- BVerfG 1 BvR 16/13 (Recht auf Vergessen I)

### Anwendung im Skill

- Rechtsgrundlage nach Art. 6 DSGVO sauber waehlen; berechtigte Interessen nach Art. 6 Abs. 1 lit. f DSGVO mit dokumentierter Abwaegung.
- Bei Datenpannen die 72-Stunden-Frist nach Art. 33 DSGVO einhalten; Risikoabwaegung Art. 34 DSGVO separat dokumentieren.
- Auskunftsanspruch Art. 15 DSGVO nicht mit Kopie nach Art. 15 Abs. 3 DSGVO verwechseln; EuGH C-307/22 Reichweite beachten.

---

## Skill: `anwendungsfall-triage`

_Datenschutzrechtlichen Sachverhalt einordnen und Bearbeitungsroute bestimmen. Art. 2 3 DSGVO Anwendungsbereich § 1 BDSG. Prüfraster: Anwendungsbereich personenbezogene Daten Verantwortlicher Auftragsverarbeiter Drittland. Output: Triage-Memo Bearbeitungsroute Normenmap. Abgrenzung: Einstieg und T..._

# Datenschutz-Triage neuer Verarbeitungsvorgänge

## Aktenstart statt Formularstart

Wenn zu **Anwendungsfall Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Datenschutzrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Eingaben

- Beschreibung des Verarbeitungsvorgangs (Datenarten, Zweck, Betroffenenkreis)
- Datenkategorien (Art. 4 Nr. 1, Art. 9 DSGVO); Beschäftigtendaten (§ 26 BDSG)?
- Neu erhoben oder Zweckänderung bei vorhandenen Daten (Art. 5 Abs. 1 lit. b DSGVO)?
- Auftragsverarbeiter / Drittland-Übermittlung?
- Automatisierte Entscheidungsfindung (Art. 22 DSGVO)?
- Cookies / Endgerätezugriff (§§ 24 ff. TDDDG)?

## Rechtlicher Rahmen

### Kernvorschriften

- **DSGVO:** Art. 5 (Grundsätze), Art. 6 (Rechtsgrundlagen), Art. 9 (besondere
 Kategorien), Art. 13/14 (Informationspflichten), Art. 17 (Löschrecht), Art. 22
 (automatisierte Entscheidungen), Art. 25 (Privacy by Design/Default), Art. 28 (AVV),
 Art. 30 (Verarbeitungsverzeichnis), Art. 32 (TOM), Art. 35 (DSFA), Art. 44 ff.
 (Drittlandtransfer).
- **BDSG:** § 22 (Gesundheits-/Sozialdaten), § 26 (Beschäftigtendatenschutz), § 38
 (betrieblicher DSB).
- **TDDDG (ehem. TTDSG):** §§ 24 ff. — Einwilligung für Cookies/Endgerätezugriffe.
- **Art. 35 Abs. 4 DSGVO** i. V. m. DSK-Positivliste — nationale Pflichttatbestände.

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 — Ungültigkeit EU-US-Privacy-Shield; Standardvertragsklauseln erfordern Transfer
 Impact Assessment; maßgeblich für Art. 44 ff. DSGVO.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 — Automatisiertes Scoring als Entscheidung i. S. d. Art. 22 DSGVO, wenn Dritte
 maßgeblich darauf abstellen; zentral für Triage von KI-/Scoring-Vorhaben.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 — Datenschutzrechtliche Haftung Art. 82 DSGVO; Beweislastverteilung.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 *(Recht auf Vergessen I)* — Datenschutz als Teil des allgemeinen Persönlichkeitsrechts
 (Art. 2 Abs. 1 i. V. m. Art. 1 Abs. 1 GG); Abwägung mit Kommunikationsfreiheiten.

### Kommentare

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
 — DSFA-Pflicht, Schwellenwerte, Verhältnis zu nationalen Listen.
- `Simitis/Hornung/Spiecker (Hrsg.), DSGVO, 2. Aufl. 2022, Art. 6 Rn. 30 ff.`
 — Rechtsgrundlagen; berechtigtes Interesse als Auffangtatbestand.
- `Gola (Hrsg.), DSGVO, 3. Aufl. 2022, Art. 22 Rn. 5 ff.`
 — Automatisierte Entscheidungsfindung; Abgrenzung zu Profiling.
- `Paal/Pauly (Hrsg.), DS-GVO BDSG, 3. Aufl. 2021, Art. 25 DSGVO Rn. 7 ff.`
 — Privacy by Design und Privacy by Default als Entwurfspflicht.
- `Ehmann/Selmayr (Hrsg.), DS-GVO, 2. Aufl. 2018, Art. 35 Rn. 25 ff.`
 — Anwendungsbereich der DSFA; Verhältnis zu Art. 5, 25 DSGVO.

## Ablauf

### Schritt 1: Verarbeitungsvorgang klären

Bei vager Beschreibung zuerst nachfragen: Datenkategorien (Art. 9?), Betroffenenkreis
(Beschäftigte → § 26 BDSG!), Zweck, Neu oder Zweckänderung, Auftragsverarbeiter,
automatisierte Entscheidung (Art. 22), Endgerätezugriff (§ 24 TDDDG).

### Schritt 2: Hausinternes DSA-Raster

Konfiguriertes Prüfraster aus CLAUDE.md lesen. Trigger erfüllt → mindestens
**DSA ERFORDERLICH**. Nicht erfüllt → weiter mit Schritt 3.

### Schritt 3: DSFA-Pflichtprüfung (Art. 35 DSGVO)

**Pflichttatbestände (Art. 35 Abs. 3, DSK-Positivliste):**
- Systematische automatisierte Bewertung persönlicher Aspekte inkl. Profiling mit
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Umfangreiche Verarbeitung besonderer Datenkategorien (Art. 9 DSGVO).
- Systematische umfangreiche Überwachung öffentlich zugänglicher Bereiche.

**Starke Indikatoren (kein Pflichttatbestand, aber DSFA dringend empfohlen):**
neue Technologie, Kinderdaten, Zusammenführung getrennter Datensätze,
Diskriminierungspotenzial, Cross-Context-Tracking, verhaltensbasierte Werbung.

Pflichttatbestand erfüllt → **DSFA PFLICHT**. Nur Indikatoren → **DSA ERFORDERLICH**.

### Schritt 4: Datenschutzrichtlinien-Abgleich

Vorhaben gegen konfigurierte Richtlinien prüfen. Typische Konflikte:
Datenkategorie nicht in Richtlinie erfasst; Drittlandweitergabe ohne Grundlage
(Art. 44 ff. DSGVO); Löschfristen (Art. 17) überschritten; Zweckbindung (Art. 5
Abs. 1 lit. b) verletzt; Betroffenenrechte unvollständig.

Direkter Konflikt → **STOPP**. Konflikt muss aufgelöst sein vor Fortführung.

### Schritt 5: Klassifikation und Ausgabe

```
Kurzergebnis: [DSFA PFLICHT / DSA ERFORDERLICH / FREIGABE / STOPP — ein Satz]

VORGANG: [wie verstanden]
KLASSIFIKATION: [...]
Hausinternes DSA-Raster ausgelöst? [Ja / Nein]
DSFA-Pflicht (Art. 35 DSGVO)? [Ja — Tatbestand / Nein / N/A]
Richtlinienkonflikt? [Keiner / Ja — konkreter Konflikt]
Begründung: [1–3 Sätze]
```

*Voraussetzungen bei DSA / DSFA:*

| Anforderung | Verantwortlich | Erledigt? |
|---|---|---|
| Datenschutzprüfung / DSFA (Art. 35 DSGVO) | DSB | ☐ |
| Berechtigtes-Interesse-Abwägung (Art. 6 Abs. 1 lit. f) | DSB / Legal | ☐ |
| DSB-Konsultation (DSFA-Pflichtverfahren) | DSB | ☐ |
| AVV (Art. 28 DSGVO) | Legal | ☐ |
| Richtlinienaktualisierung vor Launch | DSB | ☐ |
| Eintrag Verarbeitungsverzeichnis (Art. 30) | DSB | ☐ |

**Rechtsgrundlage (Art. 6 DSGVO):** [lit. a Einwilligung / lit. b Vertrag /
lit. c rechtliche Verpflichtung / lit. f berechtigte Interessen — oder "unklar"]

Nach Klassifikation immer anbieten: "Soll ich jetzt direkt mit der DSFA beginnen?"

*Bei STOPP:*
Konflikt benennen. Optionen: (A) Vorhaben umgestalten, (B) Richtlinie aktualisieren
(Vereinbarkeit mit Rechtsgrundlage prüfen). Keinen Weg vorschlagen, wenn keiner besteht.

### Schritt 6: Weiterleitung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 KI-Folgenabschätzung erwägen.
- **Beschäftigtendatenschutz:** § 26 BDSG und Mitbestimmung (§§ 87 Abs. 1 Nr. 6,
 94 BetrVG) prüfen.

## Beispiel

**Vorgang:** ML-basiertes Kreditscoring für Bestandskunden; Ergebnis fließt in
automatisierte Kreditentscheidung.

**Klassifikation:** DSFA PFLICHT — Art. 35 Abs. 3 lit. a DSGVO: systematische
automatisierte Bewertung persönlicher Aspekte mit erheblichen Auswirkungen
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
(Schufa-Scoring) reicht es, dass Dritte maßgeblich auf das Scoring abstellen.
DSB-Konsultation und Verarbeitungsverzeichnis-Eintrag (Art. 30) zwingend.

## Risiken und typische Fehler

- **"Anonymisiert" = FREIGABE:** Pseudonymisierte Daten bleiben personenbezogen
 (Art. 4 Nr. 1 DSGVO). Re-Identifikationsrisiko konkret prüfen.
- **"Wir machen das ähnlich":** Bestehende, nie geprüfte Verarbeitungen legitimieren
 keine neue. Bei anderem Umfang/Zweck/Kategorie: neu triagen.
- **"Nur ein Pilot":** Pilot mit echten Personendaten unterliegt denselben Anforderungen.
- **"Der Anbieter regelt Datenschutz":** AVV nach Art. 28 zwingend; Triage bleibt beim
 Verantwortlichen (Art. 4 Nr. 7 DSGVO).
- **Inferred Data übersehen:** Score, Risikoklasse, Präferenz = personenbezogenes Datum.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Quellenpflicht

Jede Klassifikation muss nennen: einschlägige DSGVO-/BDSG-Normen mit Artikel/Absatz,
DSK-Listenfundstelle bei DSFA-Pflicht, einschlägige Rechtsprechung in korrekter
Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

Beispiel Rechtsprechung:
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Beispiel Kommentar:
Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Quellen / Updates

Stand: 05/2026. Aktualität prüfen bei Änderungen der DSK-Blacklist/Whitelist (Art. 35 Abs. 4/5 DSGVO), neuen EDSA-Leitlinien zur DSFA sowie KI-VO-Umsetzungsakten.

**Querverweise:**
- `datenschutzrecht/skills/dsfa-erstellung/SKILL.md` — vollständige DSFA bei positiver Triage
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — bei Drittlandbezug in der Triage
- `datenschutzrecht/skills/avv-pruefung/SKILL.md` — bei Auftragsverarbeitung als Verarbeitungsbestandteil

## Aktuelle Rechtsprechung (Ergaenzung v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Output-Template — Triage-Ergebnis

**Adressat:** Datenschutzbeauftragter / Prozessverantwortlicher — Tonfall: sachlich-strukturiert

```
Datenschutz-Triage-Ergebnis [DATUM]
Verarbeitungsvorgang: [BEZEICHNUNG]
Beschreibung: [KURZBESCHREIBUNG]

Einstufung: FREIGABE / DSA ERFORDERLICH / DSFA PFLICHT / STOPP

Rechtsgrundlage: Art. [X] DSGVO [§ BDSG optional]
Verantwortlichkeit: Art. 24 (allein) / Art. 26 (gemeinsam) / Art. 28 (Auftragsverarbeitung)
Drittlandbezug: ja (→ Drittlandprüfung) / nein
DSFA-Pflicht: ja (Grund: [...]) / nein (Begründung: [...])

Naechste Schritte:
1. [AKTION]
2. [AKTION]

Frist: [DATUM]
Verantwortlich: [PERSON / ROLLE]
```

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 5 DSGVO (Grundsätze der Verarbeitung)
- Art. 6, 9 DSGVO (Rechtsgrundlagen, besondere Datenkategorien)
- Art. 13, 14 DSGVO (Informationspflichten)
- Art. 15 DSGVO (Auskunftsrecht)
- Art. 28 DSGVO (Auftragsverarbeitung)
- Art. 32 DSGVO (Sicherheit der Verarbeitung)
- Art. 33, 34 DSGVO (Meldepflichten bei Verletzung)
- Art. 82 DSGVO (Schadensersatz)
- Art. 83 DSGVO (Bußgelder)
- §§ 4, 20, 41 BDSG (Aufsicht, Rechtsweg, Strafvorschriften)

### Leitentscheidungen

- EuGH C-300/21 (immaterieller Schaden Art. 82 DSGVO)
- EuGH C-634/21 (automatisierte Bonitätsbewertung Schufa)
- EuGH C-26/22 (Datenschutzbehörden-Befugnisse)
- EuGH C-807/21 (Bußgeldhaftung juristischer Personen)
- BVerfG 1 BvR 16/13 (Recht auf Vergessen I)

### Anwendung im Skill

- Rechtsgrundlage nach Art. 6 DSGVO sauber waehlen; berechtigte Interessen nach Art. 6 Abs. 1 lit. f DSGVO mit dokumentierter Abwaegung.
- Bei Datenpannen die 72-Stunden-Frist nach Art. 33 DSGVO einhalten; Risikoabwaegung Art. 34 DSGVO separat dokumentieren.
- Auskunftsanspruch Art. 15 DSGVO nicht mit Kopie nach Art. 15 Abs. 3 DSGVO verwechseln; EuGH C-307/22 Reichweite beachten.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

