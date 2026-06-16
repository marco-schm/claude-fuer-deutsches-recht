# Megaprompt: krankenkassenrecht-krankenversicherung

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 160 Skills (gekuerzt fuer Chat-Fenster) des Plugins `krankenkassenrecht-krankenversicherung`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlaegt …
2. **kinderleistungen-sozialpaediatrie-therapie-und-schulbegle** — Krankenversicherungsleistungen für Kinder: sozialpädiatrische Zentren, Therapien, Schulbegleitung – Abgrenzung GKV, Eing…
3. **leistungsbescheid-lesen-fuer-laien** — Krankenversicherungs-Bescheide verständlich erklärt: Aufbau, Ablehnungsgründe, Rechtsbehelfsbelehrung und konkrete nächs…
4. **krankenversicherung-klagebegruendung-sozialgericht** — Klagebegründung vor dem Sozialgericht in Krankenversicherungssachen: Struktur, Beweisführung, Gesundheitsakten als Bewei…
5. **krankenversicherung-selbststaendige-mindestbeitrag** — Krankenversicherungsbeitrag für freiwillig versicherte Selbstständige: Mindestbeitrag, Einkommensnachweise, Spitzabrechn…
6. **telemedizin-epa-erezept-und-datenschutz** — Digitalisierung im Gesundheitswesen: Telemedizin, elektronische Patientenakte (ePA), elektronisches Rezept (eRezept) – G…
7. **studentische-krankenversicherung-altersgrenzen** — Pflichtversicherung Studierender (§ 5 Abs. 1 Nr. 9 SGB V): Altersgrenze 25 Jahre, Fachsemesterlimit, Urlaubssemester, En…
8. **abrechnung-goae-goz-und-erstattung** — Ärztliche (GOÄ) und zahnärztliche (GOZ) Abrechnung: Steigerungsfaktoren, Analogleistungen, Begründungspflichten und Erst…

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlaegt passende Fachmodule aus diesem Plugin vor und fuehrt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext ord..._

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Krankenkassenrecht Krankenversicherung** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Krankenkassen- und Krankenversicherungsrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen. Tragende Normen (SGB V, VVG §§ 192 ff., MB/KK) werden nicht aus Modellwissen finalisiert, sondern über die zugelassenen Live-Quellen geprüft.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Sofortrisiken zuerst markieren** — Fristen, Zustellung, Form, Zuständigkeit, Beweis-, Kosten- und Haftungsrisiken benennen.
2. **Aktenlandkarte bauen** — Welche Dateien sind Original, welche nur Behauptung; was fehlt für einen verwertbaren nächsten Schritt?
3. **Rolle klären** — Mandant, Gegner, Behörde, Gericht, betroffene Stelle; mit welchem Ziel und welcher Reichweite?
4. **Ziel bestimmen** — Prüfung, Entwurf, Antrag, Anmeldung, Schriftsatz, Verteidigung, Dashboard, Memo, Red-Team?
5. **Rechtsquellen trennen** — Normtext, Behördenpraxis, Rechtsprechung, Vertrag, technischer Standard und Praxisroutine getrennt halten.
6. **Fachmodule auswählen** — Drei bis sieben passende Skills aus diesem Plugin nennen mit Begründung, warum sie jetzt nützlich sind.
7. **Erste verwertbare Ausgabe liefern** — Kurze Lagekarte mit nächstem Schritt oder erstem Entwurf, statt einer langen abstrakten Abhandlung.

## Fachlicher Anker — Krankenkassen- und Krankenversicherungsrecht

Tragende Anker: SGB V, VVG §§ 192 ff., MB/KK. Tatsächliche Fundstellen werden über dejure.org, openJur, gesetze-im-internet.de, BGH-/BVerfG-/EuGH-/EuG-Datenbank live geprüft und nicht aus Modellwissen finalisiert.

---

## Skill: `kinderleistungen-sozialpaediatrie-therapie-und-schulbegle`

_Krankenversicherungsleistungen für Kinder: sozialpädiatrische Zentren, Therapien, Schulbegleitung – Abgrenzung GKV, Eingliederungshilfe (SGB IX/SGB XII), Schnittstellen im Krankenkassen-/Krankenversicherungsrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprec..._

# Kinderleistungen: Sozialpädiatrie, Therapie und Schulbegleitung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Skill-Zweck

Kinder mit Entwicklungsstörungen, Behinderungen oder chronischen Erkrankungen benötigen oft komplexe Versorgung. Kläre **welche Leistungen die Krankenkasse schuldet** – und wo die Abgrenzung zu Eingliederungshilfe, Schule und Jugendhilfe liegt.

## Rechtlicher Rahmen

- **§ 43a SGB V** – Sozialpädiatrische Zentren (SPZ): Frühförderung, Diagnostik
- **§ 30 SGB V** – Krankenhausbehandlung für Kinder und Jugendliche
- **§ 32 SGB V** – Heilmittel: Ergo-, Logo-, Physiotherapie für Kinder
- **§ 37 SGB V** – Häusliche Krankenpflege, auch bei Kindern
- **§ 2 SGB IX** – Behinderungsbegriff, ICF-orientiert
- **§ 112 SGB IX** – Schulbegleitung als Eingliederungshilfe (nach SGB IX Teil 2)
- **§ 35a SGB VIII** – Eingliederungshilfe Jugendhilfe (seelische Behinderung)
- **Frühförderungs-VO** – Komplexleistung Frühförderung (GKV + Eingliederungshilfe)
- BSG B 3 KR 6/14 R (SPZ-Leistungen), BSG B 8 SO 23/17 R (Schulbegleitung)

## Leistungsabgrenzung

| Leistung | Rechtsträger | Rechtsgrundlage |
|---------|-------------|-----------------|
| Sozialpädiatrisches Zentrum (SPZ) | GKV | § 43a SGB V |
| Frühförderung (unter 6 J.) | GKV + Eingliederungshilfe (Komplexleistung) | Frühförderungs-VO |
| Schulbegleitung | Eingliederungshilfe (Landkreis/Stadt) | § 112 SGB IX |
| Logopädie, Ergo, PT | GKV | § 32 SGB V |
| Schulkindergarten/Förderschule | Land/Schulträger | Schulrecht |
| Psychotherapie | GKV | § 27 Abs. 1, § 92 SGB V |

## Prüfprogramm

### Schritt 1 – SPZ-Versorgung (§ 43a SGB V)
- SPZ durch Krankenkasse zu genehmigen
- Indikation: geistige Entwicklungsstörung, Zerebralparese, Autismus-Spektrum-Störung, ADHS (schwer)
- Ärztliche Überweisung durch Kinder- und Jugendarzt oder Kinderpsychiater
- Wartezeiten SPZ: oft 12–24 Monate; einstweiliger Rechtsschutz bei dringendem Bedarf

### Schritt 2 – Frühförderung (Frühförderungs-VO)
- Kind unter 6 Jahre
- Komplexleistung: GKV übernimmt medizinisch-therapeutische Anteile; Eingliederungshilfe übernimmt pädagogische Anteile
- Antrag beim örtlichen Frühförderzentrum oder Jugendamt

### Schritt 3 – Heilmittel für Kinder (§ 32 SGB V)
- Grundsätzlich gleiche Voraussetzungen wie bei Erwachsenen (Heilmittel-RL)
- Bei Kindern: Verordnungsmengen häufig höher; besonderer Verordnungsbedarf für chronische Verläufe
- Langfristversorgung: Antrag bei Kasse bis 4 Wochen vor Ablauf

### Schritt 4 – Schulbegleitung (§ 112 SGB IX)
- GKV ist NICHT zuständig für Schulbegleitung (außer in sehr engen Ausnahmen)
- Zuständig: Eingliederungshilfeträger (Landkreis/kreisfreie Stadt)
- Antrag beim Sozialamt, Jugendamt (§ 35a SGB VIII bei seelischer Behinderung) oder Schulamt
- Abgrenzung: rein pflegerische Maßnahmen in Schule können GKV-Leistung sein (§ 37 SGB V)

### Schritt 5 – Psychotherapie für Kinder
- Kinder und Jugendlichenpsychotherapeut: GKV-Kassenzulassung erforderlich
- ADHS: Diagnose, Ausschlussdiagnostik, Leitliniengerechte Behandlung
- Systemisches Versagen: § 13 Abs. 3 SGB V wenn kein Kassentherapeut innerhalb vertretbarer Frist verfügbar

## Typische Fallen

- **Schulbegleitung bei GKV beantragen**: GKV lehnt rechtmäßig ab; Antrag muss beim Eingliederungshilfeträger gestellt werden.
- **Frühförderungs-Komplexleistung**: Oft unklar wer federführend ist; Frühförderstelle koordiniert, nicht GKV direkt.
- **SPZ-Kapazität erschöpft**: Kasse muss auf Veranlassung des Arztes prüfen ob Alternativversorgung möglich; einstweiliger Rechtsschutz.
- **Psychotherapie-Warteliste**: Systemversagen bei > 3 Monaten Wartezeit → Kostenerstattung Privattherapeut möglich (BSG).

## Output-Formate

- SPZ-Antrag mit Begründung
- Widerspruch gegen Heilmittelablehnung bei Kind
- Schulbegleitungsantrag (Eingliederungshilfe, Muster)
- Systemversagen-Schreiben (Psychotherapie)
- Übersicht Zuständigkeiten (Tabelle)

## Quellen

- [§ 43a SGB V – Sozialpädiatrisches Zentrum](https://www.gesetze-im-internet.de/sgb_5/__43a.html)
- [§ 112 SGB IX – Schulbegleitung](https://www.gesetze-im-internet.de/sgb_9_2018/__112.html)
- [Frühförderungs-VO](https://www.gesetze-im-internet.de/fruehfoerdv/)
- [§ 35a SGB VIII – Jugendhilfe](https://www.gesetze-im-internet.de/sgb_8/__35a.html)
- [BSG Kinderleistungen](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [G-BA Heilmittel-Richtlinie](https://www.g-ba.de/richtlinien/12/)

---

## Skill: `leistungsbescheid-lesen-fuer-laien`

_Krankenversicherungs-Bescheide verständlich erklärt: Aufbau, Ablehnungsgründe, Rechtsbehelfsbelehrung und konkrete nächste Schritte für Betroffene ohne Rechtskenntnisse im Krankenkassen-/Krankenversicherungsrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprec..._

# Leistungsbescheid lesen für Laien

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Skill-Zweck

Viele Versicherte verstehen Bescheide ihrer Krankenkasse nicht. Dieser Skill erklärt **den Aufbau von GKV-Leistungsbescheiden, typische Ablehnungsgründe in einfacher Sprache und konkrete nächste Schritte**.

## Rechtlicher Rahmen

- **§ 31 SGB X** – Was ist ein Verwaltungsakt (Bescheid)?
- **§ 33 SGB X** – Bestimmtheit und Form des Bescheids
- **§ 35 SGB X** – Begründungspflicht
- **§ 36 SGB X** – Rechtsbehelfsbelehrung (muss im Bescheid stehen)
- **§ 37 SGB X** – Bekanntgabe (3-Tage-Fiktion)
- **§ 84 SGG** – Widerspruchsfrist: 1 Monat

## Bescheid-Aufbau erklärt

| Teil | Was steht darin? | Was bedeutet das? |
|------|-----------------|------------------|
| Kopfzeile | Kassen-Logo, Bescheid-Nr., Datum | Für Identifikation und Fristen wichtig |
| Tenor | Entscheidung (Ablehnung oder Bewilligung) | DAS ist das Ergebnis; hier steht ob Leistung gewährt wird |
| Begründung | Warum hat Kasse so entschieden? | Hier steckt der Angriffspunkt für Widerspruch |
| Rechtsbehelfsbelehrung | Widerspruch innerhalb 1 Monat | Fristbeginn und Adresse der Widerspruchsstelle |

## Prüfprogramm

### Schritt 1 – Datum feststellen
- Datum des Bescheids + 3 Tage = Bekanntgabe (§ 37 SGB X)
- Widerspruchsfrist: 1 Monat ab Bekanntgabe
- Konkretes Fristende notieren: Welcher Tag des Folgemonats?

### Schritt 2 – Tenor lesen
- Was hat die Kasse entschieden? (Ablehnung vollständig? Teilbewilligung? Kürzung?)
- Wird eine konkrete Leistung verweigert? Welche?
- Beträge prüfen: Festzuschuss korrekt? Zuzahlung korrekt?

### Schritt 3 – Begründung verstehen
- Typische Ablehnungsgründe:
 - „Medizinisch nicht notwendig": MDK hat Ablehnung empfohlen
 - „Nicht im Leistungskatalog": kein GKV-Anspruch auf diese Leistung
 - „Wirtschaftlichkeitsgebot": günstigere Alternative verfügbar
 - „Ausschluss nach § 34 SGB V": Lifestyle-Medikament oder ausgeschlossene Leistung
- Normzitate im Bescheid: aufschlagen und nachschlagen

### Schritt 4 – Rechtsbehelfsbelehrung
- Steht eine Belehrung drin? Wenn nicht: Frist verlängert sich auf 1 Jahr
- Adresse der Widerspruchsstelle: oft Kasse selbst oder Widerspruchsausschuss
- Frist ist Eingangs- nicht Absendungsfrist: rechtzeitig ankommen lassen

### Schritt 5 – Nächste Schritte
- Versteht man Ablehnungsgrund nicht: Akteneinsicht beantragen (§ 25 SGB X)
- Frist sichern: Widerspruch fristwahrend einlegen bevor Begründung fertig
- Beratung: Verbraucherzentrale, Sozialverband VdK, unabhängige Patientenberatung (UPD)

## Typische Fallen

- **Bescheid ignorieren**: Frist läuft; nach 1 Monat ist Bescheid bestandskräftig.
- **Rechtsbehelfsbelehrung falsch gelesen**: Frist gilt per Eingang beim Absender; nicht per Poststempel.
- **Begründung nicht verstanden**: Trotzdem Widerspruch einlegen; Begründung kann nachgereicht werden.
- **Bewilligung nicht geprüft**: Manchmal wird Leistung zwar bewilligt, aber fehlerhaft begrenzt.

## Output-Formate

- Bescheid-Erklärungsprotokoll (für Versicherten)
- Widerspruchs-Mustertext (allgemein)
- Fristenkarte
- Akteneinsichtsantrag (einfach)
- Liste Beratungsstellen (regional anpassbar)

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen

- [§ 35 SGB X – Begründungspflicht](https://www.gesetze-im-internet.de/sgb_10/__35.html)
- [§ 36 SGB X – Rechtsbehelfsbelehrung](https://www.gesetze-im-internet.de/sgb_10/__36.html)
- [§ 37 SGB X – Bekanntgabe](https://www.gesetze-im-internet.de/sgb_10/__37.html)
- [§ 84 SGG – Widerspruchsfrist](https://www.gesetze-im-internet.de/sgg/__84.html)
- [Unabhängige Patientenberatung Deutschland (UPD)](https://www.patientenberatung.de)
- [dejure.org § 35 SGB X](https://dejure.org/gesetze/SGB_X/35.html)

---

## Skill: `krankenversicherung-klagebegruendung-sozialgericht`

_Klagebegründung vor dem Sozialgericht in Krankenversicherungssachen: Struktur, Beweisführung, Gesundheitsakten als Beweismittel, Sachverständige und SGG-Prozessrecht im Krankenkassen-/Krankenversicherungsrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung._

# Klagebegründung Sozialgericht: Gesundheitsakte

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Skill-Zweck

Nach erfolglosem Widerspruch folgt die Klage beim Sozialgericht. Dieser Skill bereitet eine **substantiierte Klagebegründung in Krankenversicherungssachen** vor: Struktur, Beweismittel, Gesundheitsakte und Sachverständigenfragen.

## Rechtlicher Rahmen

- **SGG §§ 78–131** – Verfahren beim Sozialgericht
- **§ 103 SGG** – Amtsermittlungsgrundsatz (Gericht erforscht Sachverhalt von Amts wegen)
- **§ 118 SGG i.V.m. ZPO §§ 404–414** – Sachverständige
- **§ 128 SGG** – Freie Beweiswürdigung
- **§ 193 SGG** – Kostenentscheidung
- **§ 183 SGG** – Kostenfreiheit (keine Gerichtskosten für Versicherte!)
- BSG B 1 KR 19/21 R (Beweismaß Krankenversicherungssachen), BSG B 1 KR 22/17 R

## Klagebegründungs-Struktur

| Teil | Inhalt |
|------|--------|
| Sachanträge | Was begehrt die Klägerin konkret? (Leistung, Aufhebung Bescheid) |
| Sachverhalt | Chronologisch; vollständig; mit Beweismitteln |
| Rechtliche Begründung | Norm + BSG-Rechtsprechung + Subsumtion |
| Beweisangebote | Ärztliche Atteste, Sachverständigengutachten, Zeugen |
| Amtsermittlung | Antrag auf gerichtliche Ermittlungen (Beiziehung Akten, Gutachten) |

## Prüfprogramm

### Schritt 1 – Klageerhebung und Form
- Frist: 1 Monat nach Widerspruchsbescheid (§ 87 SGG)
- Form: Schriftlich oder zu Protokoll beim SG
- Kein Anwaltszwang im 1. Instanzgericht (§ 73 SGG)
- Zuständiges Gericht: SG am Wohnort (§ 57 SGG)

### Schritt 2 – Gesundheitsakte zusammenstellen
- Vollständige ärztliche Unterlagen: Arztbriefe, Befundberichte, Laborbefunde
- MDK-Gutachten (falls vorhanden): aus Akteneinsicht
- Behandlungsverläufe: chronologisch; wichtig für Kausalität
- Leitlinien: als Anlage beifügen (AWMF, G-BA)

### Schritt 3 – Klagebegründung formulieren
- Sachverhalt: kurz, präzise, ohne Wertungen
- Rechtliche Begründung: Anspruchsgrundlage benennen, BSG-Urteile zitieren (Aktenzeichen)
- Prüfung des Ablehnungsgrunds: jeden Ablehnungsgrund einzeln entkräften
- Beweisangebote: am Ende jedes strittigen Punkts Beweis anbieten

### Schritt 4 – Beweismittel im Sozialgerichtsverfahren
- Sachverständigengutachten: beantragen (§ 118 SGG) wenn medizinische Fragen streitig
- Zeugen: Arzt als Zeuge laden; selten notwendig wenn Arztbriefe vorliegen
- Amtsermittlung: Gericht von Amts wegen tätig; Hinweis auf notwendige Ermittlungen

### Schritt 5 – Kostenrecht
- Keine Gerichtskosten für Versicherte (§ 183 SGG)
- Anwaltskosten: bei Obsiegen trägt Kasse die außergerichtlichen Kosten (§ 193 SGG)
- Beratungshilfe: für einkommensschwache Kläger

## Typische Fallen

- **Klagefrist versäumt**: 1 Monat ab Widerspruchsbescheid; Wiedereinsetzung bei unverschuldetem Fristversäumnis.
- **Klagebegründung zu allgemein**: „Die Kasse hat unrecht" reicht nicht; konkrete Normen und Sachverhalte.
- **Sachverständigengutachten nicht beantragt**: Gericht kann mangels Antrag Frage offen lassen; aktiv beantragen.
- **BSG-Rechtsprechung falsch zitiert**: BSG-Entscheidungen prüfen ob auf vorliegenden Fall anwendbar; nicht pauschal.

## Output-Formate

- Klageschrift (vollständige Vorlage)
- Beweisantrags-Schreiben
- Sachverständigenfragen-Liste
- Akteneinsichtsantrag beim SG
- Vergleichsangebot-Bewertung

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen

- [§ 87 SGG – Klagefrist](https://www.gesetze-im-internet.de/sgg/__87.html)
- [§ 103 SGG – Amtsermittlung](https://www.gesetze-im-internet.de/sgg/__103.html)
- [§ 183 SGG – Kostenfreiheit](https://www.gesetze-im-internet.de/sgg/__183.html)
- [BSG Prozessrecht](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [Sozialgericht Anleitungen](https://www.sozialgerichtsbarkeit.de)
- [dejure.org SGG § 87](https://dejure.org/gesetze/SGG/87.html)

---

## Skill: `krankenversicherung-selbststaendige-mindestbeitrag`

_Krankenversicherungsbeitrag für freiwillig versicherte Selbstständige: Mindestbeitrag, Einkommensnachweise, Spitzabrechnung und Widerspruch bei überhöhten Beiträgen im Krankenkassen-/Krankenversicherungsrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung._

# Selbstständige: Mindestbeitrag und Einkommensteuerbescheid

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Skill-Zweck

Selbstständige sind in der GKV freiwillig versichert. Kläre **Beitragsbemessung, Mindestbeitrag, Nachweis­pflichten gegenüber der Kasse und Strategien bei überhöhten Beiträgen**.

## Rechtlicher Rahmen

- **§ 240 SGB V** – Beitragsbemessung freiwillig Versicherter; Einkommensbegriff
- **§ 236 SGB V** – Mindestbemessungsgrundlage (2025: 1.178,33 €/Monat)
- **§ 226 Abs. 2 SGB V** – Beitrag aus Arbeitseinkommen + weiteren Einkünften
- **GKV-Spitzenverband – Beitragsverfahrensgrundsätze Selbstzahler** (BVGdS)
- BSG B 12 KR 7/18 R (Beitragsbemessung Selbstständige), BSG B 12 KR 21/11 R
- BVerfG 1 BvR 209/07 (Beitrag freiwillig Versicherter, Verfassungsmäßigkeit)

## Beitragsbemessung Selbstständige

| Einkommensquelle | Beitragspflichtig? |
|-----------------|-------------------|
| Gewinn aus Gewerbebetrieb | Ja (§ 15 EStG) |
| Einkünfte aus selbstständiger Arbeit | Ja (§ 18 EStG) |
| Einkünfte aus Vermietung | Ja |
| Kapitalerträge | Ja, wenn Besteuerung nicht KapErtSt final |
| Kindergeld | Nein |
| Sozialhilfe | Nein |
| Mindestbemessungsgrundlage | 1.178,33 €/Monat (auch wenn Einkommen niedriger) |

## Prüfprogramm

### Schritt 1 – Einkommensnachweise
- Aktuellster Einkommensteuerbescheid als Grundlage (Beitragsverfahrensgrundsätze)
- Neugründung/Einkommensverschlechterung: Prognose-/Schätzungsantrag möglich
- Kasse setzt vorläufigen Beitrag; Spitzabrechnung nach Vorlage des ESt-Bescheids

### Schritt 2 – Mindestbeitrag
- Auch wenn Einkommen unter 1.178,33 €/Monat: Mindestbeitrag gilt
- Ausnahme: hauptberuflich Selbstständige mit sehr niedrigem Einkommen → Härtefallprüfung
- Neugründer: Prognose kann unter Mindestgrundlage liegen wenn glaubhaft; Nachweis erforderlich

### Schritt 3 – Spitzabrechnung
- Vorläufiger Beitrag aus Vorjahreseinkommen → Steueränderungsbescheid eingehen lassen
- Spitzabrechnung: Kasse verrechnet Soll-Beitrag mit tatsächlichem Einkommen
- Nachzahlung oder Erstattung; Verjährung 4 Jahre (§ 25 SGB IV)

### Schritt 4 – Widerspruch bei überhöhtem Beitrag
- Kasse setzt Beitrag auf Mindestbemessungsgrundlage oder höher fest
- Einkommen niedriger: glaubhaft machen + Nachweise
- BSG: Kasse muss alle Einkommensquellen berücksichtigen, aber auch nur diese

### Schritt 5 – Einkommensoptimierung
- Betriebsausgaben mindern Gewinn und damit Beitrag
- Verluste aus anderen Einkunftsarten: seit BSG-Rechtsprechung nicht uneingeschränkt verrechenbar
- Investitionen in Betrieb: steuerrechtliche Minderung wirkt sich auf GKV-Beitrag aus

## Typische Fallen

- **Kein ESt-Bescheid verfügbar**: Kasse setzt Maximalgrundlage; Prognose mit Kontoauszügen, BWA stellen.
- **Nebengewerbe bei Anstellung**: Wenn Nebentätigkeit hauptberuflich selbstständig → Versicherungsfreiheit prüfen (§ 5 Abs. 5 SGB V).
- **Verlustvortrag**: GKV-Beitragsrecht unterscheidet sich von Steuerrecht; Verluste nicht automatisch mindernd.
- **Jahresausgleich vergessen**: Ohne Spitzabrechnung zu viel gezahlter Beitrag verjährt nach 4 Jahren.

## Output-Formate

- Beitragsschätzungsantrag (Neugründung)
- Spitzabrechnungsantrag mit ESt-Bescheid
- Widerspruch gegen Beitragsfestsetzung
- Einkommens-Beitragsberechnung (Tabelle)
- Mindestbeitrag-Härtefallantrag

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen

- [§ 240 SGB V – Beitragsbemessung](https://www.gesetze-im-internet.de/sgb_5/__240.html)
- [GKV-Spitzenverband Beitragsverfahrensgrundsätze](https://www.gkv-spitzenverband.de)
- [BSG B 12 KR 7/18 R](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [§ 236 SGB V – Mindestbeitrag](https://www.gesetze-im-internet.de/sgb_5/__236.html)
- [BVerfG 1 BvR 209/07](https://www.bverfg.de/entscheidungen.html)
- [dejure.org § 240 SGB V](https://dejure.org/gesetze/SGB_V/240.html)

---

## Skill: `telemedizin-epa-erezept-und-datenschutz`

_Digitalisierung im Gesundheitswesen: Telemedizin, elektronische Patientenakte (ePA), elektronisches Rezept (eRezept) – GKV-Leistungsrahmen, Datenschutz und Opt-out im Krankenkassen-/Krankenversicherungsrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung._

# Telemedizin, ePA, eRezept und Datenschutz

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Skill-Zweck

Die Digitalisierung verändert das Krankenversicherungsrecht. Kläre **Telemedizin-Leistungsrahmen, ePA-Regelungen und eRezept-Prozesse** mit besonderem Fokus auf Datenschutz und Opt-out-Rechte.

## Rechtlicher Rahmen

- **§ 291a SGB V** – Telematik-Infrastruktur (TI): Grundlage für ePA, eRezept
- **§ 341 SGB V** – Elektronische Patientenakte (ePA): opt-out ab 2025
- **§ 360 SGB V** – eRezept: Pflicht für GKV-Arzneiverordnungen
- **§ 27 SGB V** – Telemedizin als Krankenbehandlungsform
- **§ 87 SGB V i.V.m. EBM** – Vergütung von Videosprechstunden
- DSGVO Art. 9, BDSG, TSVG (Terminservice- und Versorgungsgesetz 2019)
- BfDI Stellungnahmen zur ePA

## Digitale Versorgungsstruktur

| Element | Rechtsgrundlage | Opt-out möglich |
|---------|-----------------|-----------------|
| ePA (Elektronische Patientenakte) | § 341 SGB V (ab 2025 opt-out) | Ja, Widerspruch jederzeit |
| eRezept | § 360 SGB V | Nein (Pflicht für Arzt) |
| Videosprechstunde | § 87 SGB V, EBM | Ja (Versicherter wählt) |
| eArztbrief | § 291a SGB V | Ja |
| DiGA | § 33a SGB V | Ja (separate Einwilligung) |

## Prüfprogramm

### Schritt 1 – Elektronische Patientenakte (ePA)
- Ab 2025: alle GKV-Versicherten erhalten automatisch ePA (opt-out-Modell)
- Widerspruch: schriftlich an Krankenkasse; kein Grund erforderlich
- Inhalt: Befunde, Diagnosen, Medikationspläne, DiGA-Daten, Mutterpass etc.
- Zugriff: Patient kontrolliert Zugriffsrechte (App der Kasse oder Kiosk-System)

### Schritt 2 – eRezept
- Pflicht für alle GKV-Arzneiverordnungen seit 2024
- Einlösung: Apotheke scannt QR-Code (Papierausdruck oder App)
- Datenschutz: Rezeptdaten zentral gespeichert; Zugriff für Abrechnung und ggf. Auswertung
- Verweigerungsrecht: Versicherter kann analoge Alternative anfordern (wenn technisch nicht möglich)

### Schritt 3 – Videosprechstunde
- GKV-Leistung: Arzt-Patienten-Videokontakt (EBM-Ziffer 01439)
- Plattformzulassung: nur von KBV zertifizierte Anbieter
- Ausnahmen: nicht für erstmaligen Arzt-Patienten-Kontakt (§ 7 Abs. 4 MBOÄ)
- Datenschutz: Ende-zu-Ende-Verschlüsselung erforderlich; DSGVO-Konformität der Plattform

### Schritt 4 – Datenschutz und Opt-out
- Widerspruch ePA: schriftlich, begründungslos, jederzeit widerrufbar
- Datenzugang Dritte (Forschung): pseudonymisiert; Versicherter muss nicht aktiv zustimmen aber kann widersprechen
- Kassenaufsicht (BAS): Aufsicht über Datenschutz bei Kassen (Sozialdaten)
- BfDI: zuständig für föderalen Datenschutz

### Schritt 5 – Telemedizin im Leistungsrecht
- Telemedizinische Behandlung: voller GKV-Leistungsanspruch (§ 27 SGB V)
- Einschränkung: nicht alle Diagnosen telemedizinisch behandelbar; Arzt entscheidet
- Telemonitoring: chronisch kranke Patienten (Herzinsuffizienz: § 137f SGB V)

## Typische Fallen

- **ePA und Arbeitgeber**: Arbeitgeber hat keinen Zugang zur ePA; strikte Trennung.
- **eRezept und Notfall**: Bei Systemausfall Papierrezept als Ersatz; Apotheke kann auf Bedenken reagieren.
- **Videosprechstunde-Plattform nicht zertifiziert**: Arzt haftet bei Nutzung nicht zugelassener Plattform; für Versicherten kein Problem.
- **DiGA-Daten in ePA**: Nur mit expliziter Einwilligung; separates Opt-in erforderlich.

## Output-Formate

- ePA-Widerspruchsschreiben
- Datenschutzerklärung-Checkliste (Telemedizin)
- Videosprechstunden-Einverständnis-Muster
- eRezept-Erklärung (Laienerklärung)
- Kassenaufsichts-Beschwerde (Datenschutz)

## Quellen

- [§ 341 SGB V – ePA](https://www.gesetze-im-internet.de/sgb_5/__341.html)
- [§ 360 SGB V – eRezept](https://www.gesetze-im-internet.de/sgb_5/__360.html)
- [Gematik – ePA und eRezept](https://www.gematik.de)
- [BfDI – Datenschutz Gesundheit](https://www.bfdi.bund.de)
- [dejure.org § 291a SGB V](https://dejure.org/gesetze/SGB_V/291a.html)
- [DSGVO Art. 9](https://dsgvo-gesetz.de/art-9-dsgvo/)

---

## Skill: `studentische-krankenversicherung-altersgrenzen`

_Pflichtversicherung Studierender (§ 5 Abs. 1 Nr. 9 SGB V): Altersgrenze 25 Jahre, Fachsemesterlimit, Urlaubssemester, Ende der Versicherung und Übergangsoptionen im Krankenkassen-/Krankenversicherungsrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung._

# Studentische Krankenversicherung: Altersgrenzen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Skill-Zweck

Studierende sind zu günstigen Konditionen gesetzlich pflichtversichert – aber nur bis zu bestimmten Altersgrenzen. Kläre **Altersgrenzen, Fachsemesterlimits, Übergangslösungen und Folgen des Versicherungsendes**.

## Rechtlicher Rahmen

- **§ 5 Abs. 1 Nr. 9 SGB V** – Versicherungspflicht Studierender an staatlich anerkannten Hochschulen
- **§ 5 Abs. 1 Nr. 9 Satz 2 SGB V** – Altersgrenzen und Semesterlimit
- **§ 190 Abs. 9 SGB V** – Ende der Mitgliedschaft bei Exmatrikulation
- **§ 9 SGB V** – Freiwillige Weiterversicherung nach Studienende
- **§ 226 SGB V** – Beitragsbemessung (Mindestbeitrag für Studierende)
- BSG B 12 KR 9/10 R (Studentische KV, Urlaubssemester), BSG B 12 KR 6/15 R

## Grenzwerte Studentische KV

| Parameter | Wert |
|-----------|------|
| Altersgrenze | 25. Lebensjahr (d.h. bis zum Ende des Semesters in dem 25 wird) |
| Fachsemesterlimit | 14. Fachsemester |
| Beitrag (2025) | Einheitlich ca. 106 €/Monat (ca. 14,6 % von Mindestbemessungsgrundlage) |
| Urlaubssemester | Zählen für Alters-/Semesterlimit |

## Prüfprogramm

### Schritt 1 – Altersgrenzen prüfen
- Vollendung des 25. Lebensjahres: Ende der studentischen KV zum Ende des Semesters
- Verlängerung bei Ableistung von Wehr-/Bundesfreiwilligendienst (§ 5 Abs. 1 Nr. 9 Satz 3 SGB V): je nach Dauer
- Behinderung: keine Altersgrenze wenn Behinderung Studium verzögert hat

### Schritt 2 – Fachsemesterlimit
- Nach dem 14. Fachsemester: Ende der studentischen KV, auch wenn unter 25
- Urlaubssemester zählen mit (BSG bestätigt)
- Ausnahmsweise Verlängerung: wenn studienzeitverlängernd gewirkt hat (Krankheit, Behinderung, Gremientätigkeit)

### Schritt 3 – Übergang nach Studienende
- Exmatrikulation oder Ablauf Grenzen → freiwillige Versicherung (§ 9 SGB V): 3 Monate Beitrittsfrist
- Noch kein Job? Freiwillig versichern mit Mindestbeitrag
- Job sofort: Pflichtmitglied als Arbeitnehmer (§ 5 Abs. 1 Nr. 1 SGB V)
- Familienversicherung möglich wenn Elternteil GKV und Einkommen unter 505 €/Monat

### Schritt 4 – Beitrag Studierender
- Einheitlicher Beitrag ca. 106 €/Monat (Beitrag + Zusatzbeitrag)
- Bei Nebentätigkeit: ab gewisser Höhe erhöhter Beitrag; unter 520 €/Monat kein Einfluss
- Hauptberufliche Selbstständigkeit neben Studium: Versicherungsfreiheit prüfen (§ 5 Abs. 5)

### Schritt 5 – Auslandssemester
- Pflichtversicherung gilt auch bei Auslandssemester an EU-Hochschule (EHIC)
- Außereuropäisches Ausland: prüfen ob EHIC gilt; ggf. Zusatzversicherung
- Auslandspraktikum > 3 Monate: Pflichtversicherung kann enden → freiwillige Weitervesicherung

## Typische Fallen

- **Urlaubssemester als Fachsemester**: Viele Studierende wissen nicht, dass Urlaubssemester zählen.
- **Exmatrikulations-Zeitpunkt**: Mitgliedschaft endet nicht mit Exmatrikulation, sondern mit Ende des Prüfungssemesters.
- **Abschluss und Lücke**: Wer abschlussarbeitet, aber noch eingeschrieben ist: Pflichtversicherung läuft; nach Exmatrikulation sofort handeln.
- **PKV für Studierende**: Günstiger als freiwillige GKV; aber Rückkehr schwieriger; Langzeitperspektive bedenken.

## Output-Formate

- Altersgrenzen-Fristenkalender
- Exmatrikulationsbescheinigung-Checkliste
- Freiwillige GKV-Antrag nach Studium
- Studierendenversicherungs-Berechnung
- Informationsblatt Auslandssemester-Versicherung

## Quellen

- [§ 5 SGB V Nr. 9 – Studierende](https://www.gesetze-im-internet.de/sgb_5/__5.html)
- [§ 190 SGB V – Ende der Mitgliedschaft](https://www.gesetze-im-internet.de/sgb_5/__190.html)
- [§ 9 SGB V – Freiwillige Versicherung](https://www.gesetze-im-internet.de/sgb_5/__9.html)
- [BSG studentische KV](https://www.bsg.bund.de/DE/Entscheidungen/entscheidungen_node.html)
- [GKV-Spitzenverband Studierende](https://www.gkv-spitzenverband.de)
- [dejure.org § 5 SGB V](https://dejure.org/gesetze/SGB_V/5.html)

---

## Skill: `abrechnung-goae-goz-und-erstattung`

_Ärztliche (GOÄ) und zahnärztliche (GOZ) Abrechnung: Steigerungsfaktoren, Analogleistungen, Begründungspflichten und Erstattungsansprüche in der PKV und Beihilfe im Krankenkassen-/Krankenversicherungsrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung._

# Abrechnung GOÄ/GOZ und Erstattung

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Skill-Zweck

PKV und Beihilfe erstatten ärztliche Honorare nach GOÄ und GOZ. Prüfe **Abrechnungsrichtigeit, Steigerungsfaktoren, Analogleistungen und Erstattungsansprüche**.

## Rechtlicher Rahmen

- **GOÄ** (Gebührenordnung für Ärzte) §§ 1–12 + Gebührenverzeichnis
- **GOZ** (Gebührenordnung für Zahnärzte) §§ 1–12 + Gebührenverzeichnis
- **§ 4 GOÄ** – Allgemeine Bestimmungen zu Steigerungsfaktoren (1,0 bis 3,5-fach)
- **§ 6 GOÄ** – Analogleistungen (nicht im Verzeichnis gelistete Leistungen)
- **§ 12 GOÄ** – Rechnungspflichtangaben (fehlende Angaben → Rechnung anfechtbar)
- BGH III ZR 17/18 (GOÄ-Abrechnung, Steigerungsfaktor), BGH III ZR 62/18
- BVerfG 1 BvR 2084/05 (GOÄ und PKV-Erstattung)

## GOÄ-Steigerungsfaktoren

| Faktor | Schwellenwert | Begründungspflicht |
|--------|--------------|-------------------|
| 1,0-fach | Mindestsatz (selten) | Nein |
| 1,8-fach (Regelfall) | Durchschnittliche Schwierigkeit | Nein |
| 2,3-fach | Obergrenze ohne Begründung | Nein |
| > 2,3-fach | Erhöhter Schwellenwert | Ja (auf Rechnung) |
| 3,5-fach | Absolutes Maximum | Ja, ausführlich |

## Prüfprogramm

### Schritt 1 – Rechnungsprüfung formal
- Enthält Rechnung alle Pflichtangaben (§ 12 GOÄ): Datum, Diagnose, Leistungsnummer, Steigerungsfaktor, Begründung bei > 2,3?
- Fehlende Pflichtangaben: Rechnung zurückweisen, neue vollständige Rechnung verlangen
- Digitale Rechnung: muss gleiche Pflichtangaben enthalten

### Schritt 2 – Leistungsverzeichnis prüfen
- Gebührennummer korrekt? GOÄ-Nummernverzeichnis konsultieren
- Doppelabrechnung: GOÄ-Nr. schließt bestimmte andere aus (Ausschlusshinweise im Verzeichnis)
- Zielleistungsprinzip: bei operativen Eingriffen schließen manche Leistungen andere ein (§ 4 Abs. 2a GOÄ)

### Schritt 3 – Steigerungsfaktor prüfen
- > 2,3-fach: Begründung auf Rechnung erforderlich; pauschale Begründungen unzureichend (BGH)
- BGH III ZR 17/18: individuelle Begründung für konkrete Behandlungssituation notwendig
- PKV kann Abzug bei nicht begründetem Faktor vornehmen; Erstattungskürzung

### Schritt 4 – Analogleistungen (§ 6 GOÄ)
- Nicht im Verzeichnis: Abrechnung analog zu ähnlicher Leistung
- Arzt muss in Rechnung kennzeichnen: „analog § 6 GOÄ"
- PKV-Erstattung: PKV prüft ob Analoganwendung plausibel; Ablehnung möglich
- Neue Methoden: oft nur Analogabrechnung möglich bis GOÄ-Reform

### Schritt 5 – Erstattungskürzung durch PKV/Beihilfe
- PKV kürzt: Einzelne Nummern nicht erstattet, Steigerungsfaktor reduziert
- Arzt haftet: keine direkte Haftung gegen PKV; aber Arzt muss Rechnung nicht neu stellen
- Differenz: Versicherter trägt Differenz zwischen Arztrechnung und PKV-Erstattung
- Beihilfe: eigene Erstattungsgrenzen; oft konservativer als PKV

## Typische Fallen

- **Privatarzt-Honorar vor Behandlung**: GOÄ-Honorarvereinbarung schriftlich vor Behandlung; nachträglich unwirksam.
- **IGeL und GOÄ**: IGeL kann nach GOÄ abgerechnet werden; aber Patient muss vorher informiert und einverstanden sein.
- **GOÄ 2024-Reform**: Neue GOÄ in Vorbereitung; Übergangsrecht beachten.
- **Zahnersatz GOZ**: GOZ-Abrechnung für Zahnersatz häufig fehleranfällig; Festzuschuss GKV beachten wenn auch GKV-Mitglied.

## Output-Formate

- GOÄ-Rechnungsprüfungs-Protokoll
- Reklamationsschreiben an Arzt (fehlende Begründung)
- PKV-Erstattungskürzungs-Widerspruch
- Analogleistungs-Überprüfungsanfrage
- GOÄ-Steigerungsfaktor-Begründungs-Checkliste

## Quellen

- [GOÄ – Gebührenordnung Ärzte](https://www.gesetze-im-internet.de/go__1982/)
- [GOZ – Gebührenordnung Zahnärzte](https://www.gesetze-im-internet.de/goz_1988/)
- [§ 12 GOÄ – Rechnungspflicht](https://www.gesetze-im-internet.de/go__1982/__12.html)
- [BGH III ZR 17/18](https://www.bundesgerichtshof.de/DE/Entscheidungen/entscheidungen_node.html)
- [Bundesärztekammer GOÄ](https://www.bundesaerztekammer.de)
- [dejure.org GOÄ](https://dejure.org/gesetze/GO%C3%84)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 192 VVG
- § 204 VVG
- § 193 VVG
- § 84 SGG
- § 86b SGG
- § 203 VVG
- § 88 SGG
- § 6 AsylbLG
- § 152 VAG
- § 205 VVG
- § 153 VAG
- § 4 AsylbLG

### Leitentscheidungen

- BGH IV ZR 255/17
- BGH IV ZR 84/11
- BGH III ZR 17/18
- BGH IV ZR 194/07
- BGH IV ZR 62/16

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

