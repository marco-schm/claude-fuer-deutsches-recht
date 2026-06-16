# Megaprompt: leasingrecht-praxis

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 117 Skills (gekuerzt fuer Chat-Fenster) des Plugins `leasingrecht-praxis`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Einstieg, Schnelltriage und Fallrouting. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlaegt …
2. **schieds-oder-gerichtsstand-leasing** — Streitbeilegung im Leasingrecht: Schiedsverfahren vs. staatliche Gerichte, Gerichtsstandsklausel, Verbraucherrecht, Medi…
3. **leasing-in-sanierungsgutachten** — Leasing im Sanierungsgutachten: Behandlung von Leasingverbindlichkeiten in IDW S6-Gutachten, Fortführungsprognose, Leasi…
4. **agb-klauseln-restwertgarantie** — AGB-Kontrolle im Leasingvertrag: Einbeziehung, Inhaltskontrolle nach §§ 305–310 BGB, BGH-Kernklauseln, Klauselkatalog fü…
5. **leasingvertrag-redline-fuer-leasingnehmer** — Leasingvertrag-Redline aus Leasingnehmersicht: Problematische Klauseln identifizieren, Gegenentwürfe formulieren, Verhan…
6. **konzernleasing-transfer-franchise** — Konzerninternes Leasing: Verrechnungspreise, § 1 AStG, BEPS-Aktionsplan, Fremdvergleichsgrundsatz, Dokumentationspflicht…
7. **grenzueberschreitendes-leasing-unidroit-und-rechtswahl** — Grenzüberschreitendes Leasing: UNIDROIT-Übereinkommen, Rechtswahl (Rom I-VO), internationales Mobiliar-Leasingrecht, Ste…
8. **lease-005-fahrzeugleasing-km-vertrag-restwert-rueckgabe** — Leasingrecht: Fahrzeugleasing Kilometervertrag Restwertvertrag Rückgabe mit geführtem Workflow, Normencheck, Beweis- und…

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlaegt passende Fachmodule aus diesem Plugin vor und fuehrt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext ordnet der Skill das Material eigen..._

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Leasingrecht Praxis** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Leasingrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen. Tragende Normen (BGB §§ 535 ff., AGB-Kontrolle §§ 305 ff. BGB, HGB) werden nicht aus Modellwissen finalisiert, sondern über die zugelassenen Live-Quellen geprüft.

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

## Fachlicher Anker — Leasingrecht

Tragende Anker: BGB §§ 535 ff., AGB-Kontrolle §§ 305 ff. BGB, HGB. Tatsächliche Fundstellen werden über dejure.org, openJur, gesetze-im-internet.de, BGH-/BVerfG-/EuGH-/EuG-Datenbank live geprüft und nicht aus Modellwissen finalisiert.

---

## Skill: `schieds-oder-gerichtsstand-leasing`

_Streitbeilegung im Leasingrecht: Schiedsverfahren vs. staatliche Gerichte, Gerichtsstandsklausel, Verbraucherrecht, Mediation und internationale Schiedsgerichte im Leasingrecht._

# Schiedsverfahren und Gerichtsstand im Leasingrecht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Gerichtsstandsklauseln

### B2B (Unternehmensleasing)
- § 38 ZPO: Gerichtsstandsvereinbarung zwischen Kaufleuten zulässig
- Formerfordernis: Schriftlich oder in Textform (§ 40 ZPO analog)
- Wirkung: Ausschließlicher oder nicht-ausschließlicher Gerichtsstand

### B2C (Verbraucherleasing)
- § 29c ZPO: Beim Verbraucher nur Gerichtsstand am Wohnort des Verbrauchers
- Gerichtsstandsklauseln zulasten des Verbrauchers: AGB-widrig (§ 307 BGB)
- Ausnahme: Vereinbarung nach Entstehung des Rechtsstreits (§ 38 III ZPO)

### EU: EuGVO (VO 1215/2012)
- Art. 7 EuGVO: Besonderer Gerichtsstand am Erfüllungsort
- Art. 19 ff. EuGVO: Verbraucher hat besondere Schutzgerichtsstand (Wohnsitzland)
- Gerichtsstandsklauseln gegen Verbraucher: Nur eingeschränkt zulässig (Art. 25 EuGVO)

## Schiedsverfahren

### Vorteile
- Vertraulichkeit: Kein öffentliches Verfahren
- Schnelligkeit: Flexible Verfahrensordnung
- Internationale Vollstreckung: New Yorker Übereinkommen (1958) in 170+ Ländern
- Spezialisierung: Branchenkundige Schiedsrichter

### Nachteile
- Kosten: Höher als staatliche Gerichte (Schiedsrichterhonorar)
- Kein einstweiliger Rechtsschutz direkt (Schiedsgericht kann vorsorgliche Maßnahmen anordnen, aber staatliches Gericht vollstreckt)
- Kein gesetzlicher Instanzenzug

### Schiedsklausel (§ 1029 ZPO)
Formerfordernis: Schriftliche Vereinbarung (§ 1031 ZPO); Textform bei Verbrauchern (§ 1031 V ZPO).

Inhalt:
- Schiedsgerichtsordnung (DIS, ICC, LCIA)
- Schiedsort (maßgeblich für Anfechtungsverfahren)
- Schiedsrichteranzahl (1 oder 3)
- Schiedssprache

### DIS-Schiedsregeln (Deutsche Institution für Schiedsgerichtsbarkeit)
- Neue DIS-Regeln 2018
- Expedited Proceedings: Schnellverfahren für Ansprüche bis 2 Mio. €

### Verbraucher und Schiedsverfahren
- § 1031 V ZPO: Bei Verbrauchern muss Schiedsklausel separat unterzeichnet sein
- AGB-Einbeziehung reicht nicht; Überraschungsverbot (§ 305c BGB)
- Schiedsklausel in B2C-AGB praktisch unwirksam

## Mediation und ADR

### Mediationsklausel
- Vor Schiedsverfahren: Mediation (§ 36 VSBG: Verbraucherstreitbeilegungsgesetz)
- Freiwillig; schnell; günstig

### VSBG (Verbraucherstreitbeilegungsgesetz)
- LG muss Verbraucher über Möglichkeit der außergerichtlichen Streitbeilegung informieren (§ 36 VSBG)
- Keine Pflicht zur Teilnahme; aber Information ist Pflicht

## Prüfprogramm

1. B2B oder B2C? Verbraucher → eingeschränkte Gerichtsstandswahl
2. Gerichtsstandsklausel: Wirksam nach § 38 ZPO oder AGB-widrig?
3. Schiedsklausel: Formgültig (§ 1031 ZPO)? Verbraucher separat unterschrieben?
4. Schiedsgericht gewählt: DIS, ICC oder ad hoc? Schiedsort?
5. Einstweiliger Rechtsschutz: Staatliches Gericht parallel?
6. VSBG-Information: Auf Webseite und in AGB erteilt?

## Typische Fallen

- Gerichtsstandsklausel gegen Verbraucher: AGB-widrig; staatliche Gerichte zuständig
- Schiedsklausel in B2C-AGB ohne gesonderte Unterschrift: Unwirksam
- Kein einstweiliger Rechtsschutz über Schiedsgericht vorgesehen: Verzögerung
- VSBG-Informationspflicht verletzt: OLG-Urteile: Abmahnrisiko

## Normen und Quellen

- §§ 1029–1066 ZPO (Schiedsverfahren): https://www.gesetze-im-internet.de/zpo/__1029.html
- § 38 ZPO (Gerichtsstandsvereinbarung): https://www.gesetze-im-internet.de/zpo/__38.html
- EuGVO (VO 1215/2012): https://eur-lex.europa.eu
- New Yorker Übereinkommen 1958: https://www.uncitral.org
- VSBG (Verbraucherstreitbeilegungsgesetz): https://www.gesetze-im-internet.de/vsbg/
- DIS-Schiedsregeln 2018: https://www.dis-arb.de

## Output-Formate

- **Schiedsklausel-Muster B2B**: DIS-Schiedsklausel für Leasingverträge
- **Gerichtsstandsklausel-Muster B2B**: Ausschließlicher Gerichtsstand
- **VSBG-Informationstext**: Pflichthinweis für LG-Website und AGB
- **Mediationsklausel**: Stufenklausel (erst Mediation, dann Schiedsgericht)

---

## Skill: `leasing-in-sanierungsgutachten`

_Leasing im Sanierungsgutachten: Behandlung von Leasingverbindlichkeiten in IDW S6-Gutachten, Fortführungsprognose, Leasingkosten und Restrukturierungsmaßnahmen im Leasingrecht._

# Leasing im Sanierungsgutachten (IDW S6)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## IDW S6: Grundstruktur des Sanierungsgutachtens

IDW S6 (Stand 2018) gliedert das Sanierungsgutachten in:
1. Auftragsumfang und Grundlagen
2. Beschreibung des Unternehmens
3. Analyse der Unternehmenskrise (Ursachen)
4. Leitbild des sanierten Unternehmens
5. Maßnahmenplan
6. Integrierter Sanierungsplan (GuV, Bilanz, Cashflow)
7. Fortführungsprognose

## Leasingverhältnisse in der Krisenanalyse

### Leasingkosten als Krisenursache
- Zu hohe Leasingverpflichtungen für Anlagegüter: Fixkostenblock in Krise
- Operating-Lease-Kosten (bei HGB-Bilanzierer): Nicht in Bilanz, aber in GuV
- IFRS 16 bilanzierende Unternehmen: Leasingverbindlichkeiten sichtbar in Bilanz

### Identifikation der Leasingverhältnisse
- Vollständige Liste aller Leasingverträge (Anlage zum Gutachten)
- Je Vertrag: Objekt, LG, Laufzeit, Rate, Restwert, Eigentümer
- Off-Balance-Verpflichtungen: Im Anhang des Jahresabschlusses (§ 285 Nr. 3a HGB)?

## Leasingkostenanalyse im Sanierungsplan

### Marktpreisvergleich
- Sind die aktuellen Leasingraten marktüblich?
- Wenn zu hoch (z.B. in Boomzeiten abgeschlossen): Neuverhandlung möglich?

### Kündbarkeit und Exit-Optionen
- Vorzeitige Kündigung: Schadensersatz nach BGH, Urteil vom 14.03.2007 - VIII ZR 68/06 (Abzinsungspflicht)
- Sale-and-Lease-Back: Rückgabe und Neuleasing zu günstigeren Konditionen?
- Rückgabe nicht mehr benötigter Anlagegüter: Fristige Kündigung bei Änderung des Leasinggegenstands

### IFRS-16-Effekte
- Leasingverbindlichkeit als Schuld: Zählmetriken für Kreditgeber (Debt/EBITDA)
- Restrukturierungsmaßnahme: Vorzeitige Kündigung → Entschuldung (aber Schadensersatz)

## Fortführungsprognose: Leasingverpflichtungen

### Cashflow-Projektion
- Leasingraten im Plan-Cashflow erfassen
- Endfällige Zahlungen (Restwert) besonders kritisch: Fälligkeitsprofil prüfen

### Sanierungsmaßnahmen mit Leasingbezug
1. Kündigung von Verträgen für nicht mehr benötigte Objekte
2. Ratenreduktion durch Verlängerung der Laufzeit
3. Sale-and-Lease-Back für neue Liquidität
4. Stundungsvereinbarungen mit LG

### Integrierter Plan
- GuV: Leasingaufwand (HGB) oder Zins + AfA (IFRS 16)
- Bilanz: IFRS 16 – RoU und Verbindlichkeiten
- Cashflow: Leasingzahlungen als Operating-/Financing-Cashflow

## Regulatorische Pflichten

### § 285 Nr. 3a HGB: Anhangspflicht
Außerbilanzielle Verpflichtungen (incl. Operating-Leasing bei HGB) müssen im Anhang ausgewiesen werden, wenn wesentlich.

### IFRS 16 Disclosure
Detaillierte Angaben zu RoU, Leasingverbindlichkeiten, Laufzeiten und Cash-Auswirkungen.

## Prüfprogramm

1. Alle Leasingverträge identifiziert? Liste mit LG, Objekt, Rate, Laufzeit?
2. Off-Balance-Verpflichtungen im Anhang § 285 HGB ausgewiesen?
3. Leasingkosten im Marktvergleich: Angemessen oder zu hoch?
4. Kündigungsoptionen: Vorzeitige Kündigung wirtschaftlich sinnvoll?
5. Sale-and-Lease-Back möglich für neue Liquidität?
6. Integrierter Plan: Leasingraten korrekt erfasst?

## Typische Fallen

- Off-Balance-Leasing vergessen → Cashflow-Plan unterschätzt Fixkostenblock
- Vorzeitige Kündigung ohne Schadensersatzkalkulation → Liquiditätslücke
- IFRS 16 Umstellung in Sanierungsphase → Bilanzkennzahlen verändern sich unerwartet
- LG kooperiert nicht bei Stundung → Kündigung; Restforderung als InsO-Verbindlichkeit

## Normen und Quellen

- IDW S6 (Sanierungsgutachten): https://www.idw.de
- § 285 Nr. 3a HGB (Anhang): https://www.gesetze-im-internet.de/hgb/__285.html
- IFRS 16: https://eur-lex.europa.eu
- §§ 217 ff. InsO (Insolvenzplan): https://www.gesetze-im-internet.de/inso/__217.html
- BGH, Urteil vom 14.03.2007 - VIII ZR 68/06 (Schadensersatz Kündigung): https://www.bgh.de
- § 3a EStG (Sanierungsgewinn): https://www.gesetze-im-internet.de/estg/__3a.html

## Output-Formate

- **Leasingvertrags-Liste**: Format für Gutachten-Anlage
- **Cashflow-Leasing**: Zahlungsplan alle Verträge (Rate, Restwert, Fälligkeit)
- **Sanierungsmaßnahmen-Matrix**: Option – Effekt – Kosten – Zeitplan
- **IFRS-16-vs-HGB-Vergleich**: Bilanzielle Darstellung im Plan

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `agb-klauseln-restwertgarantie`

_AGB-Kontrolle im Leasingvertrag: Einbeziehung, Inhaltskontrolle nach §§ 305–310 BGB, BGH-Kernklauseln, Klauselkatalog für Verbraucher- und Unternehmerleasing im Leasingrecht._

# AGB-Kontrolle im Leasingvertrag

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtlicher Rahmen

- § 305 BGB: Einbeziehungsvoraussetzungen
- § 305c BGB: Überraschende und mehrdeutige Klauseln
- § 307 BGB: Generalklausel (unangemessene Benachteiligung)
- § 308 BGB: Klauselverbote mit Wertungsmöglichkeit
- § 309 BGB: Klauselverbote ohne Wertungsmöglichkeit
- § 310 BGB: Bereichsausnahmen (B2B, B2C)
- §§ 506–509 BGB: Verbraucherleasing-Pflichtangaben

## Einbeziehungskontrolle (§ 305 II BGB)

Voraussetzungen für wirksame AGB-Einbeziehung:
1. Ausdrücklicher Hinweis auf AGB bei Vertragsschluss (oder deutlich sichtbarer Aushang)
2. Zumutbare Möglichkeit der Kenntnisnahme
3. Einverständnis des Vertragspartners

Bei Verbrauchern (B2C) strenge Anforderungen. Bei Unternehmern (B2B, § 310 I BGB) erleichterte Einbeziehung; §§ 308, 309 BGB gelten nicht direkt, wirken aber als Indizien für § 307 BGB.

## Klauselkatalog

### 1. Gefahrtragungsklausel
**Typische Formulierung**: „Der Leasingnehmer trägt die Gefahr des zufälligen Untergangs und der zufälligen Verschlechterung des Leasingobjekts."

**Bewertung**: BGH – wirksam bei Finanzierungsleasing (BGH VIII ZR 71/93), da LN wirtschaftlicher Eigentümer ist. Bei Operating-Lease und gegenüber Verbrauchern problematisch (§ 309 Nr. 12 BGB).

### 2. Abtretungsklausel (Gewährleistung)
**Typische Formulierung**: „Der Leasinggeber tritt alle Gewährleistungsansprüche gegen den Lieferanten an den Leasingnehmer ab. Eigene Ansprüche des Leasingnehmers gegen den Leasinggeber sind ausgeschlossen."

**Bewertung**: Grundsätzlich wirksam, wenn die Abtretung tatsächlich erfolgt und LN klagebefugt wird. Unwirksam, wenn Abtretung ins Leere geht (Lieferant insolvent, Frist abgelaufen) und LN dann schutzlos steht (BGH, Urteil vom 13.11.2013 - VIII ZR 257/12).

### 3. Kündigungsklausel bei Zahlungsverzug
**Typische Formulierung**: „Der Leasinggeber kann bei Verzug mit mehr als einer Rate fristlos kündigen."

**Bewertung**: Zulässig im B2B. Im B2C muss Abmahnung vorausgehen (§ 543 III BGB analog). Voraussetzung: Verzug muss erheblich sein (§ 543 II Nr. 3 BGB).

### 4. Schadensersatzklausel nach Kündigung
**Typische Formulierung**: „Bei vorzeitiger Vertragsbeendigung schuldet der Leasingnehmer sämtliche ausstehende Leasingraten bis Vertragsende abzüglich eines Abzinsungsbetrags."

**Bewertung**: Zulässig als Schadensersatz (BGH, Urteil vom 14.03.2007 - VIII ZR 68/06), aber LN muss sich ersparte Aufwendungen und Verwertungserlös anrechnen lassen dürfen. Klauseln, die Anrechnung ausschließen, sind nach § 309 Nr. 5 BGB unwirksam.

### 5. Restwerthaftung
**Typische Formulierung**: „Unterschreitet der Verwertungserlös den kalkulierten Restwert, ist der Leasingnehmer zur Zahlung der Differenz verpflichtet."

**Bewertung**: Restwertgarantien können wirksam sein, müssen aber klar und transparent formuliert sein (§ 307 Abs. 1 Satz 2 BGB). Als frei prüfbare Anker zur Verbraucherleasing-Restwertgarantie kommen BGH, Urteile vom 28.05.2014 - VIII ZR 179/13 und VIII ZR 241/13 in Betracht; Mehrerlösfragen gesondert anhand Vertragsmodell und Abrechnung prüfen.

### 6. Totalschadensklausel
**Typische Formulierung**: „Bei Totalschaden oder Verlust sind die ausstehenden Raten sofort fällig; Versicherungsleistung ist anzurechnen."

**Bewertung**: Grundsätzlich zulässig, aber Transparenz und angemessene Anrechnung der Versicherungsleistung erforderlich. Klauseln, die LN doppelt belasten (Raten + fehlende Versicherungsdeckung), sind unwirksam.

### 7. Rückgabeklausel / Minderwert
**Typische Formulierung**: „Das Leasingobjekt ist in einwandfreiem, gebrauchsüblichen Zustand zurückzugeben; Abweichungen werden dem Leasingnehmer berechnet."

**Bewertung**: Zulässig; Verschleiß muss sich auf normale Abnutzung beschränken (BGH VIII ZR 172/05). Klauseln, die auch normale Abnutzung dem LN anlasten, sind nach § 307 unwirksam.

## Prüfprogramm

1. Einbeziehungstatbestand prüfen (§ 305 II BGB): Hinweis + Kenntnisnahme + Einverständnis
2. Überraschende Klauseln identifizieren (§ 305c I BGB)
3. Mehrdeutigkeitsregel anwenden (§ 305c II BGB): Unklarheiten gegen Verwender
4. Für jede Kernklausel: Verbraucher oder Unternehmer? Katalogverbote (§§ 308, 309) oder Generalklausel (§ 307)?
5. Rechtsfolge unwirksamer Klausel: Klausel fällt weg, gesetzliche Regelung tritt ein (§ 306 II BGB)

## Typische Fallen

- AGB nicht ordnungsgemäß einbezogen, weil nur auf Rückseite des Leasingscheins ohne Hinweis auf Vorderseite
- Mehrdeutige Restwertklausel: Verwender (LG) trägt das Risiko der Auslegung
- Schadensersatzklausel ohne Anrechnungsoption: nach § 309 Nr. 5 unwirksam
- Abtretungsklausel fehlt: LN hat keine Mängelrechte gegen Lieferant

## Normen und Quellen

- §§ 305–310 BGB: https://dejure.org/gesetze/BGB/305.html
- BGH VIII ZR 71/93 (Gefahrtragung Finanzierungsleasing): https://www.bgh.de
- BGH, Urteil vom 13.11.2013 - VIII ZR 257/12 (Abtretungsklausel): https://www.bgh.de
- BGH, Urteil vom 14.03.2007 - VIII ZR 68/06 (Schadensersatz nach Kündigung): https://www.bgh.de
- BGH, Urteil vom 28.05.2014 - VIII ZR 179/13 und VIII ZR 241/13 (Restwerthaftung): https://www.bgh.de
- openjur.de AGB-Leasingrecht: https://openjur.de

## Output-Formate

- **Klauselmatrix**: Klausel – Norm – BGH-Bewertung – Wirksam/Unwirksam
- **Redline-Empfehlung**: Geänderte Klauselfassung für AGB-Konformität
- **Prüfbericht**: Klausel-für-Klausel-Analyse mit Handlungsempfehlung

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 26 BDSG
- Art. 13 DSGVO
- Art. 28 DSGVO
- § 1 AStG
- § 3a EStG
- § 4h EStG
- § 5a EStG
- § 11 EStG
- § 6 EGBGB
- Art. 6 DSGVO
- § 36 VSBG
- Art. 101 AEUV

### Leitentscheidungen

- BGH VIII ZR 172/05
- BGH VIII ZR 71/93
- BFH IX R 14/15
- BGH XII ZR 18/08
- BGH XI ZR 59/17

---

## Skill: `leasingvertrag-redline-fuer-leasingnehmer`

_Leasingvertrag-Redline aus Leasingnehmersicht: Problematische Klauseln identifizieren, Gegenentwürfe formulieren, Verhandlungsstrategie und Risikoabsicherung im Leasingrecht._

# Leasingvertrag-Redline: Leasingnehmerperspektive

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Red-Flag-Klauseln aus LN-Sicht

### 1. Fehlende Mehrerlösklausel
**Problem**: Restwertgarantie des LN ohne Beteiligung am Mehrerlös bei Verwertung über Restwert.
**BGH-Anker:** Die Entscheidungen vom 28.05.2014 - VIII ZR 179/13 und VIII ZR 241/13 betreffen die Wirksamkeit von Restwertgarantien im Verbraucherleasing. Ob eine fehlende Mehrerlösbeteiligung die konkrete Klausel angreifbar macht, ist gesondert anhand § 307 BGB, Vertragsmodell, Transparenz und Abrechnungspraxis zu prüfen.
**Forderung des LN**: Ergänzung: „Übersteigt der Verwertungserlös den kalkulierten Restwert, erhält der LN mindestens 75 % des Mehrerlöses."

### 2. Unbegrenzte Gefahrtragung
**Problem**: LN trägt das Risiko auch bei unverschuldetem Untergang; keine GAP-Versicherung.
**Risiko**: Totalschaden → LN zahlt Differenz zwischen Versicherung und offener Restschuld.
**Forderung des LN**: „Im Fall des Totalschadens oder Diebstahls deckt die gemäß Vertrag abzuschließende GAP-Versicherung die verbleibende Forderung des LG; eine darüber hinausgehende Haftung des LN ist ausgeschlossen."

### 3. Zu enge Rückgabekonditions-Definition
**Problem**: „Einwandfreier Zustand" ohne Definition normaler Abnutzung → LG kann nahezu jeden Gebrauchsspuren als Minderwert abrechnen.
**BGH VIII ZR 172/05**: Normale Abnutzung darf nicht dem LN angelastet werden.
**Forderung des LN**: Klarer Katalog normaler Abnutzung (Beispiele, Toleranzgrenzen) ins Vertragswerk aufnehmen.

### 4. Einseitige Kündigungsklausel
**Problem**: LG kann bei jeder kleinen Verzögerung ohne Abmahnung kündigen.
**AGB-Recht**: Bei Verbrauchern Abmahnung zwingend; bei Unternehmern kann unverhältnismäßige Klausel nach § 307 BGB unwirksam sein.
**Forderung des LN**: Abmahnung mit 14-tägiger Nachfrist immer vor Kündigung.

### 5. Überlange Nutzungsverantwortung
**Problem**: LN haftet für alle Schäden durch Dritte, auch wenn LN keine Möglichkeit hatte, diesen zu verhindern.
**Forderung des LN**: Beschränkung auf Schäden, die LN zu vertreten hat (§§ 276, 278 BGB).

### 6. Fehlende Rückgabe-Besichtigungsklausel
**Problem**: LG kann das Objekt nach Rückgabe besichtigen, ohne LN beizuziehen → einseitiges Gutachten.
**Forderung des LN**: „Die Besichtigung des Leasingobjekts bei Rückgabe erfolgt gemeinsam mit dem LN. Ein Minderwertgutachten wird LN vorab zugestellt; LN hat 14 Tage Zeit für ein Gegengutachten."

### 7. Fehlende Insolvenzregelung
**Problem**: Vertrag schweigt zur Lage bei Insolvenz des LG.
**Forderung des LN**: Klausel, dass bei Insolvenz des LG das Nutzungsrecht des LN fortbesteht (§ 566 BGB analog).

## Verhandlungsstrategie

### Prioritäten setzen
1. Erstpriorität: Klauseln, die wirtschaftlich maximal schaden (Gefahrtragung, Restwert)
2. Zweitpriorität: Klauseln, die Rechtsdurchsetzung erschweren (Gerichtsstand, Schiedsgericht)
3. Drittpriorität: Formelle Verbesserungen (Protokollklauseln, Fristen)

### Verhandlungstaktik
- „Paket"-Tausch: LN gibt bei Restwertverpflichtung nach, wenn LG GAP-Versicherung stellt
- Zeitdruck nutzen: LN hat Alternativangebote (konkurrierender LG)
- Wirtschaftlichkeitsargument: Klare Kalkulation des Risikos durch LN

## Risikoabsicherung für LN

- GAP-Versicherung: Pflicht oder Option im Vertrag?
- Betriebsunterbrechungsversicherung: Bei Maschinenleasing kritisch
- Sachverständigenklausel: Gegengutachtenrecht bei Minderwertabrechnung
- Sonderkündigungsrecht: Bei Insolvenz LN, betrieblichen Veränderungen, Force Majeure

## Prüfprogramm

1. Mehrerlösklausel bei Restwertgarantie? (Risikopunkt nach § 307 BGB, nicht schematisch als Pflicht behaupten)
2. GAP-Versicherung oder Beschränkung der Haftung nach Totalschaden?
3. Normaler Abnutzungs-Katalog definiert?
4. Abmahnpflicht vor Kündigung? Bei Verbraucher zwingend
5. Gemeinsame Rückgabebesichtigung und Gegengutachtenrecht?
6. § 566 BGB-Analog-Klausel für Insolvenz LG?

## Normen und Quellen

- BGH, Urteil vom 28.05.2014 - VIII ZR 179/13 und VIII ZR 241/13 (Restwertgarantie; Mehrerlösfragen gesondert live prüfen): https://www.bgh.de
- BGH VIII ZR 172/05 (normale Abnutzung): https://www.bgh.de
- BGH VIII ZR 71/93 (Gefahrtragung): https://www.bgh.de
- § 566 BGB: https://dejure.org/gesetze/BGB/566.html
- §§ 276, 278 BGB (Verschulden): https://dejure.org/gesetze/BGB/276.html
- §§ 305–310 BGB: https://dejure.org/gesetze/BGB/305.html

## Output-Formate

- **Red-Flag-Liste**: 10 Klauseln die LN ablehnen oder ändern sollte
- **Gegenentwurf-Formulierungen**: Fertige Redline-Texte
- **Verhandlungsbrief**: LN fordert Änderungen mit Begründung
- **Risikoabsicherungsplan**: Welche Versicherungen, welche Klauseln

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `konzernleasing-transfer-franchise`

_Konzerninternes Leasing: Verrechnungspreise, § 1 AStG, BEPS-Aktionsplan, Fremdvergleichsgrundsatz, Dokumentationspflichten und länderbezogene Steuerrisiken im Leasingrecht._

# Konzerninternes Leasing: Transfer Pricing und Verrechnungspreise

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Rechtlicher Rahmen

- § 1 AStG (Einkünftekorrektur bei nahestehenden Personen): Fremdvergleich
- §§ 1a–1e AStG: Dokumentationspflichten, Angemessenheitsnachweis
- § 90 III AO, GAufzV: Aufzeichnungspflichten für Verrechnungspreise
- Art. 9 OECD-Musterabkommen: Verbundene Unternehmen
- BEPS-Aktionspläne 8–10 (OECD 2015): Gewinnkorrektur bei immateriellen Gütern und Dienstleistungen
- EU ATAD-Richtlinien: Hybrids, CFC, Exit Taxation

## Fremdvergleichsgrundsatz (§ 1 AStG)

### Grundsatz
Transaktionen zwischen nahestehenden Personen müssen zu Bedingungen erfolgen, wie sie fremde Dritte unter gleichen Umständen vereinbaren würden.

### Nahestehende Person (§ 1 II AStG)
- Unmittelbare oder mittelbare Beteiligung ≥ 25 % oder beherrschender Einfluss
- Gleiche Person oder Gesellschaft steht hinter beiden Transaktionspartnern

### Verrechnungspreismethoden (OECD-Transfer Pricing Guidelines)

**1. Preisvergleichsmethode (CUP)**
Vergleich mit Drittpreisen für gleichartige Leasingtransaktionen.
- Ideal, aber selten exakt vergleichbar (Custom Terms)

**2. Kostenaufschlagsmethode**
Herstellungskosten (Anschaffungskosten + Finanzierung) + Marktübliche Marge
- Geeignet für Routinetransaktionen (Routineleasing)

**3. TNMM (Transactional Net Margin Method)**
Vergleich der Nettomarge des Leasinggebers mit vergleichbaren Drittunternehmen.

## Dokumentationspflichten (§ 90 III AO, GAufzV)

### Pflicht zur Aufzeichnung
- Aufzeichnungen für alle Transaktionen mit nahestehenden Personen
- Inhalt: Sachverhalt, angewandte Methode, Vergleichsdaten
- Frist: Erstellung bei Abgabe der Steuererklärung; auf Anforderung innerhalb 60 Tage

### Sanktionen bei Nichtdokumentation
- § 162 III AO: Schätzungsbefugnis des Finanzamts
- Zuschläge: 5–10 % der Einkunftskorrektur (§ 162 IV AO)
- Außenprüfung: Besondere Prüfungsdichte bei konzerninternen Transaktionen

## Konzernleasing: Strukturüberlegungen

### Intra-Konzern-Leasinggesellschaft (Captive Lessor)
- Konzern gründet interne Leasinggesellschaft (oft in Niedrigsteuerland: Luxemburg, Irland, Niederlande)
- Captive verleast an Konzerngesellschaften weltweit
- Risiko: Verrechnungspreise müssen fremdvergleichskonform sein; Substanz im Sitzland

### Zinsabzug und BEPS
- BEPS Action 4: Zinsabzugsbeschränkungen (§ 4h EStG, § 8a KStG: Zinsschranke)
- Konzernleasing mit hoher Verschuldung beim LN: Zinsen ggf. nicht abzugsfähig

## Prüfprogramm

1. Liegt konzerninterne Leasing-Transaktion vor? Nahestehende Person (§ 1 II AStG)?
2. Verrechnungspreismethode: CUP, Kostenaufschlag, TNMM?
3. Dokumentation: GAufzV erfüllt? Aktuell und vollständig?
4. Zinsschranke (§ 4h EStG): Leasingrate enthält Zinsanteil; Grenze prüfen?
5. BEPS-Risiken: Substanz im Sitzland des LG? IP-Box-Regime?
6. Länderrisiken: DBA, Quellensteuer, Exit Tax?

## Typische Fallen

- Verrechnungspreise ohne Dokumentation → Schätzungsbefugnis des FA
- Captive Lessor ohne wirtschaftliche Substanz → BEPS-Angriff; Einkünfteverlagerung nicht anerkannt
- Zinsanteil in Leasingrate übersehen → § 4h EStG-Prüfung notwendig
- DBA-Quellensteuer nicht berücksichtigt → Effektive Rate höher als geplant

## Normen und Quellen

- § 1 AStG (Fremdvergleich): https://www.gesetze-im-internet.de/astg/__1.html
- § 90 III AO (Aufzeichnungspflichten): https://www.gesetze-im-internet.de/ao_1977/__90.html
- GAufzV (Aufzeichnungsverordnung Verrechnungspreise): https://www.gesetze-im-internet.de/aufzv/
- § 4h EStG (Zinsschranke): https://www.gesetze-im-internet.de/estg/__4h.html
- OECD Transfer Pricing Guidelines 2022: https://www.oecd.org
- BEPS-Aktionspläne 8-10: https://www.oecd.org

## Output-Formate

- **Verrechnungspreis-Dokumentation**: Vorlage für konzerninterne Leasingtransaktion
- **Methoden-Auswahl-Matrix**: CUP / Kostenaufschlag / TNMM – Eignung nach Transaktionsart
- **Zinsschranken-Memo**: Leasingrate, Zinsanteil, § 4h EStG-Prüfung
- **BEPS-Risikoeinschätzung**: Captive Lessor – Substanz, Verrechnungspreise, Quellensteuer

---

## Skill: `grenzueberschreitendes-leasing-unidroit-und-rechtswahl`

_Grenzüberschreitendes Leasing: UNIDROIT-Übereinkommen, Rechtswahl (Rom I-VO), internationales Mobiliar-Leasingrecht, Steuerstrukturierung und Valutafragen im Leasingrecht._

# Grenzüberschreitendes Leasing: UNIDROIT und Rechtswahl

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## UNIDROIT-Übereinkommen über internationales Finanzierungsleasing (Ottawa, 1988)

### Anwendungsbereich
- UNIDROIT-Übereinkommen: Gilt für Finanzierungsleasing, wenn LG und LN in verschiedenen Vertragsstaaten ansässig sind
- Deutschland ist kein Vertragsstaat → gilt nur, wenn Parteien Recht eines Vertragsstaats gewählt haben (z.B. England bis Brexit, Frankreich, USA/einzelne Staaten)
- Regelt: Rechte und Pflichten aus Leasingdreieck (Lieferant, LG, LN)

### Kernregeln UNIDROIT
- Art. 8: LN kann Ansprüche gegen Lieferant direkt geltend machen (wie §398 BGB)
- Art. 10: LN trägt Gefahrübergang wie Käufer
- Art. 13: Kündigung bei Nichterfüllung; Schadensersatz

## Rechtswahl nach Rom I-VO (EG 593/2008)

### Grundsatz: Freie Rechtswahl (Art. 3 Rom I-VO)
- Parteien können das anwendbare Recht frei wählen
- Empfehlung für internationale Leasingverträge: Wahl des Rechts eines Landes mit gut entwickeltem Leasingrecht (England/New York für Finanzierungs-Leasing; Deutschland für EU-Vertragspartner)

### Einschränkungen
- Verbraucher: Art. 6 Rom I-VO: Schutzrecht des Verbrauchers aus seinem Heimatland kann nicht abbedungen werden
- Zwingende Bestimmungen: Bestimmte Schutznormen (Verbraucherrecht, Arbeitsrecht) bleiben trotz Rechtswahl anwendbar (Art. 9 Rom I-VO)

### Anwendbares Recht ohne Rechtswahl (Art. 4 Rom I-VO)
- Leasingvertrag = Dienstleistungsvertrag → Recht des charakteristischen Leistungserbringers (LG) gilt
- LG in Deutschland → deutsches Recht anwendbar

## Internationaler Zahlungsverkehr

### Währungsrisiko
- Leasingrate in Fremdwährung (z.B. USD): LN trägt Währungsrisiko
- Absicherung: Devisentermingeschäfte, Währungsklausel im Vertrag

### Steuerstrukturierung: Cross-Border-Leasing

#### Typische Struktur
- LG in Niedrigsteuerland (z.B. Irland für Flugzeuge, Luxemburg für Finanzinstrumente)
- LN in Hochsteuerland: Leasingraten als Betriebsausgabe
- LG nutzt günstige Steuerregime; Steuervorteil geteilt

#### Risiken
- Doppelbesteuerungsabkommen (DBA): Quellensteuer auf Leasingraten?
- BEPS (Base Erosion and Profit Shifting, OECD): Anti-Gestaltungs-Regeln; Country-by-Country-Reporting
- § 8b KStG, §§ 1 ff. AStG: Verrechnungspreise bei Konzernleasing

### Zollrecht
- Grenzüberschreitende Verbringung von Leasingobjekten: Zollanmeldung erforderlich
- ATA-Carnet: Temporäre Einfuhr ohne Zoll (für Ausstellungen, vorübergehende Nutzung)
- Bei Finanzierungsleasing: Zoll auf Einfuhrwert bei Gestellung im Geltungsgebiet

## Insolvenz: Grenzüberschreitend

- EuInsVO (EG 2015/848): Hauptinsolvenzverfahren am Ort des COMI (Centre of Main Interests)
- Anerkennungspflicht in EU-Staaten
- Drittstaaten-Insolvenz: Anerkennung nach § 343 InsO

## Prüfprogramm

1. Wo sind LG und LN ansässig? UNIDROIT anwendbar?
2. Rechtswahlklausel: Welches Recht, warum?
3. Verbraucherleasing: Art. 6 Rom I-VO – Heimatrecht des Verbrauchers beachtet?
4. Währungsrisiko: Absicherung vereinbart?
5. Steuerstruktur: DBA-Quellensteuer? BEPS-Risiken?
6. Zollrecht: Einfuhr, temporäre Verbringung, ATA-Carnet?

## Typische Fallen

- Keine Rechtswahlklausel → Recht des LG-Landes gilt (möglicherweise unbekanntes Recht)
- Verbraucher im Ausland: Heimatrecht schützt ihn stärker → AGB des LG unwirksam
- Quellensteuer auf Leasingraten nicht eingeplant → Renditeminderung
- ATA-Carnet abgelaufen: Leasingobjekt im Ausland → Zollrisiko

## Normen und Quellen

- UNIDROIT Ottawa Convention 1988: https://www.unidroit.org
- Rom I-VO (EG 593/2008): https://eur-lex.europa.eu
- EuInsVO (EG 2015/848): https://eur-lex.europa.eu
- BEPS-Aktionsplan (OECD): https://www.oecd.org
- § 343 InsO (Ausländisches Insolvenzverfahren): https://www.gesetze-im-internet.de/inso/__343.html
- ATA-Carnet: https://www.ihk.de

## Output-Formate

- **Rechtswahl-Klausel-Muster**: Für internationale Leasingverträge
- **DBA-Quellensteuer-Matrix**: Ländervergleich für typische Leasingstruktur
- **Zoll-Checkliste**: Grenzüberschreitende Verbringung von Leasingobjekten
- **BEPS-Risikobewertung**: Konzernleasing und Verrechnungspreise

---

## Skill: `lease-005-fahrzeugleasing-km-vertrag-restwert-rueckgabe`

_Leasingrecht: Fahrzeugleasing Kilometervertrag Restwertvertrag Rückgabe mit geführtem Workflow, Normencheck, Beweis- und Fristenlogik, Red-Team und verwertbarem Ergebnis._

# Leasingrecht: Fahrzeugleasing Kilometervertrag Restwertvertrag Rückgabe

## Aufgabe

Dieser Skill bearbeitet **Fahrzeugleasing Kilometervertrag Restwertvertrag Rückgabe** im Bereich **Leasingrecht**. Er soll nicht schematisch antworten, sondern zuerst die praktische Lage sortieren: Wer handelt, welche Unterlagen liegen vor, welche Frist läuft, welche Behörde oder Gegenpartei entscheidet und welches Ergebnis gebraucht wird.

## Kaltstart in 6 Fragen

1. Welche Rolle hat die Nutzerin: Mandant, Unternehmen, Behörde, Kanzlei, Gericht, Verlag, Betreiber, Investor oder Betroffene?
2. Geht es um Prüfung, Entwurf, Verteidigung, Anmeldung, Register, Frist, Verhandlung, Compliance, Streit oder Dokumentation?
3. Welche Dokumente liegen vor und welche fehlen: Vertrag, Bescheid, Registerauszug, Screenshot, E-Mail, Rechnung, Gutachten, Normtext, Protokoll?
4. Welche Rechtsordnung, Branche, Epoche, Sprache oder technische Umgebung ist betroffen?
5. Welche Entscheidung muss heute fallen und welche Punkte dürfen erst nach Live-Check beantwortet werden?
6. Soll das Ergebnis als Ampel, Memo, Klausel, Antrag, Fristenplan, Behördenschreiben, Red-Team oder Dashboard kommen?

## Prüfprogramm

- Sachverhalt in Tatsachen, Annahmen, Wertungen und offene Beweisfragen zerlegen.
- Vertragsart, Objekt, Zahlungsstrom und Eigentum zuerst klären
- AGB, Gewährleistung, Insolvenz und Steuer zusammen prüfen
- Rückgabe, Verwertung und Beweis dokumentieren
- Bei Rechtsprechung nur verifizierte Aktenzeichen und freie Quelle
- Zuständigkeit, Form, Frist, Beweislast, Vollzug und Rechtsbehelf immer getrennt ausgeben.
- Bei historischen, internationalen oder technischen Begriffen erst übersetzen, dann rechtlich einordnen.
- Keine Scheingenauigkeit: Wenn Quelle, Normstand oder Rechtsprechung fehlen, einen Live-Check als nächsten Schritt formulieren.

## Typische Fallen

- Ein Begriff klingt vertraut, hat aber in der konkreten Rechtsordnung oder Praxis eine andere Funktion.
- Zuständigkeit, Form oder Zustellung wird übersehen, obwohl der materielle Punkt gut aussieht.
- Eine Behauptung wird aus Modellwissen mit einer Fundstelle versehen. Das ist verboten; erst prüfen, dann zitieren.
- Der Output ist juristisch richtig, hilft aber der Nutzerin operativ nicht. Deshalb immer nächste Handlung und Dokumentationsspur liefern.

## Output

- Leasingmemo
- Vertragsredline
- Rückgabeprotokoll
- Insolvenzmatrix
- Stundungsentwurf
- Portfolio-Dashboard

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

