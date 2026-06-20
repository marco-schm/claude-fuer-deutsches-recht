# Megaprompt: fachanwalt-versicherungsrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 91 Skills des Plugins `fachanwalt-versicherungsrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Anwalts-Dashboard Fachanwalt Versicherungsrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspr…
2. **mandat-triage-versicherungsrecht** — Strukturierte Eingangs-Abfrage für versicherungsrechtliche Mandate mit Fristen-Sofort-Check: Anwendungsfall neues Versic…
3. **fachanwalt-versicherungsrecht-orientierung** — Orientierung im Versicherungsvertragsrecht für Mandate und Fachanwaltschaft nach FAO. Anwendungsfall Kanzlei will Versic…
4. **orientierung-mandat-fachanwaltschaft** — Orientierung im Versicherungsvertragsrecht für Mandate und Fachanwaltschaft nach FAO: Anwendungsfall Kanzlei will Versic…
5. **erstgespraech-mandatsannahme** — Strukturierter Erstgespraechsleitfaden für Versicherungsvertragsrecht (Personen- und Sachversicherung): Erfassung der Ko…
6. **erstpruefung-und-mandatsziel** — Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.
7. **fachanwalt-versicherungsrecht-cyber-loesegeld-sanktionsrecht** — Cyber-Versicherung bei Ransomware mit Sanktionsrisiko und Geldwäscherecht. Anwendungsfall Unternehmen erhaelt Erpressung…
8. **fachanwalt-versicherungsrecht-ombudsmann-gdv-schlichtung** — Außergerichtliche Schlichtung über Versicherungs-Ombudsmann oder PKV-Ombudsmann als Alternative zur Klage. Anwendungsfal…
9. **fachanwalt-versicherungsrecht-berufsunfaehigkeit-klage** — Klage bei abgelehnter Berufsunfähigkeitsversicherungs-Leistung. Anwendungsfall BU-Versicherung hat Leistungsantrag abgel…
10. **fachanwalt-versicherungsrecht-leistungsablehnung-pruefen** — Ablehnung des Versicherers prüfen nach §§ 1 28 VVG Obliegenheitsverletzung und Risikoausschluss. Anwendungsfall Versiche…

---

## Skill: `einstieg-routing`

_Anwalts-Dashboard Fachanwalt Versicherungsrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt bleibt im Driver Seat._

# Anwalts-Dashboard Fachanwalt Versicherungsrecht

> Leistungsablehnung, BU, D&O, Rechtsschutz, Obliegenheiten — Bedingungen prüfen, Obliegenheit prüfen, Beweislast verteilen.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 12 VVG: 1 Monat** (a. F.) ist überholt; Klagefrist gibt es nicht mehr. Aber: § 195 BGB Verjährung 3 Jahre. § 28 IV VVG: Obliegenheitsverletzung — Belehrungspflicht des Versicherers. § 19 VVG: Anzeigepflicht vorvertraglich; Rücktritt 1 Monat ab Kenntnis. § 14 VVG: Fälligkeit nach Erhebung der nötigen Erhebungen. | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Versicherungsleistung aus jeweiligem Vertrag (BU, D&O, RS, Kasko, Haftpflicht, KH); §§ 1, 100, 115 VVG; § 86 VVG Regress; § 28 VVG Obliegenheitsverletzung; § 19 VVG Anzeigepflicht; § 215 VVG Gerichtsstand. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | § 215 VVG: Wohnsitz Versicherungsnehmer (zwingend für Verbraucher). Sonst §§ 12, 17 ZPO. Bei BU/PKV häufig LG (Streitwert). | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🟠 Verjährung 3 Jahre ab Kenntnis (§ 199 BGB). 🔴 D&O Claims-made: Eintrittsdatum innerhalb Versicherungsperiode — Melde-Obliegenheit!
- **Beweislage:** 🔴 Obliegenheit § 28 VVG: Belehrungserfordernis und Kausalitätsgegenbeweis. 🟠 Anzeigepflicht § 19 VVG: Vorvertragliche Fragen Wortlaut konkret abgleichen.
- **Wirtschaftlich:** 🔴 BU-Anerkennung: Rückwirkung der Leistungspflicht bei verspäteter Anerkenntnis. 🟠 RS: Stichentscheid-/Schiedsgutachten.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **BU-Leistung verweigert** | `versr-bu-leistungspruefung-spezial` | Definition Beruf, Prognose 6 Monate, Verweisung, Anerkenntnisstrategie |
| D&O-Anspruch / Claims-made | `versr-d-und-o-spezialfall` | Versicherungsfall-Definition, Anzeigepflicht, Verteidigungskosten |
| Rechtsschutzdeckung verweigert | `versr-rechtsschutz-deckungsklage-spezial` | Deckungsklage § 3 ARB, Stichentscheid, vorvertraglich |
| Obliegenheitsverletzung Vorwurf | `versr-obliegenheitsverletzung-praxis` | Belehrungserfordernis § 28 IV VVG, Kausalitätsgegenbeweis |
| Anzeigepflicht § 19 VVG / Rücktritt | `versr-vvg-anzeigepflicht-19-arglist` | Frage-/Fragebogenklarheit, Arglist, Rücktritt 1 Monat |

## Norm-Radar (live verifizieren)

- **§ 1 VVG** — Hauptleistung des Versicherers
- **§ 19 VVG** — vorvertragliche Anzeigepflicht; Rücktritt
- **§ 28 VVG** — Obliegenheitsverletzung; Belehrungserfordernis
- **§ 100 VVG** — Haftpflichtversicherung: Versicherungsschutz
- **§ 115 VVG** — Direktanspruch gegen KH-Versicherer
- **§ 215 VVG** — Gerichtsstand am Wohnsitz VN

## Genau eine Rückfrage (nur wenn nötig)

> Welche **Sparte** (BU · D&O · KH/Haftpflicht · RS · Sachversicherung) — und welcher **Streitpunkt**: Deckung, Obliegenheit, Anzeigepflicht oder Höhe?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **BU-Anerkenntnis / Nachprüfung** — BGH IV. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Anzeigepflicht § 19 VVG; Arglistanfechtung** — BGH IV. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Obliegenheitsverletzung § 28 VVG; Belehrungserfordernis Abs. 4** — BGH IV. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **D&O; Versicherungsfall (Claims-made)** — BGH IV. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

---

## Skill: `mandat-triage-versicherungsrecht`

_Strukturierte Eingangs-Abfrage für versicherungsrechtliche Mandate mit Fristen-Sofort-Check: Anwendungsfall neues Versicherungsmandat geht ein und muss schnell tria..._

# Strukturierte Eingangs-Abfrage für versicherungsrechtliche Mandate mit Fristen-Sofort-Check


## Aktenstart statt Formularstart

Wenn zu **Klage Versicherer Triage Versicherungsrecht** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Fachanwalt Versicherungsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierte Eingangs-Abfrage für versicherungsrechtliche Mandate mit Fristen-Sofort-Check. Anwendungsfall neues Versicherungsmandat geht ein und muss schnell triagiert werden. Normen § 195 BGB Verjährung drei Jahre §§ 12 14 VVG Fälligkeit Schadensmeldung AVB-Klagefristen. Prüfraster Sparte Ereignis Stichtag Deckungsablehnung Höhe Frist-Sofort-Check Eskalation bei BU-Ablehnung oder lebensbedrohlichen Krankheitskosten. Output Triage-Ergebnis mit Routing zu deckungsanfrage-prüfen und Fristen-Eskalationshinweis. Abgrenzung zu deckungsanfrage-prüfen und erstgespraech-mandatsannahme.

### Mandat-Triage Versicherungsrecht

## Ablauf — sieben Fragen

### Frage 1 — Versicherungsnehmer oder Anspruchsteller?

- Versicherungsnehmer gegen eigene Versicherung (Erstrisikomandant)
- Geschädigter gegen Haftpflichtversicherer (Direktanspruch § 115 VVG)
- Versicherer als Mandant (Deckungsklage)
- Vermittler-Haftung

### Frage 2 — Sparte?

- KFZ-Vollkasko / Teilkasko / Haftpflicht
- Privathaftpflicht
- Hausrat / Gebäude
- Berufshaftpflicht
- Lebensversicherung (Erlebensfall Todesfall)
- Berufsunfähigkeit BU
- Krankenversicherung gesetzlich / privat
- Krankentagegeld
- Pflegeversicherung
- Rechtsschutz
- Insassenunfallversicherung
- Rentenversicherung (privat)
- Industrieversicherung Sonder-Industriedeckungen
- D&O Direktoren- und Manager-Haftpflicht
- Cyber-Versicherung

### Frage 3 — Akute Eilbedürftigkeit?

- BU-Ablehnung — kein Einkommen drohend
- Krankenversicherung weigert lebenswichtige Behandlung
- Hausrat-Brand kein Vorschuss
- Gewerbe-Betriebsunterbrechung
- Rechtsschutz-Deckungsablehnung mit drohender Verjährung Hauptverfahren

### Frage 4 — Versicherungsfall genau?

- Datum Ereignis
- Schadens-Höhe geschätzt
- Anzeige beim Versicherer Datum
- Bisherige Reaktion (Ablehnung Stillschweigen Teilzahlung)

### Frage 5 — Bedingungswerk?

- Police vorhanden?
- AVB welche Fassung?
- Tarif konkret bezeichnet?
- Risikofragebogen beim Vertragsschluss vorhanden?
- Versicherungsbeginn — technisch / formell

### Frage 6 — Frist?

- **Verjährung Versicherungsleistung** drei Jahre § 195 BGB ab Schluss des Jahres der Anspruchsentstehung und Kenntnis (§ 199 BGB)
- **AVB-Klagefrist** früher § 12 Abs. 3 VVG sechs Monate — seit VVG-Reform 2008 entfallen; aber manche älteren Verträge prüfen
- **Anzeigefrist** Schaden je nach AVB sieben Tage bis sofort
- **Wahrung der Frist durch Klage** bei Verjährung

### Frage 7 — Hauptaktenstand?

- Vollständiger Schriftwechsel?
- Bedingungswerk komplett?
- Schadensgutachten vorhanden?
- Bei BU ärztliches Gutachten?

## Routing-Matrix

| Sparte/Vorgang | Folge-Skill | Frist |
|---|---|---|
| Deckungsablehnung Sachsparte | `deckungsanfrage-pruefen` | drei Jahre Verjährung |
| BU-Ablehnung | `deckungsanfrage-pruefen` plus medizinische Gegenbegutachtung | drei Jahre |
| Leben Todesfall | `deckungsanfrage-pruefen` | drei Jahre |
| Krankenversicherung medizinische Notwendigkeit | (Skill kv-prüfung — perspektivisch) | drei Jahre |
| Rechtsschutz Deckungsablehnung | (Skill rs-deckung — perspektivisch) | drei Jahre |
| Direktanspruch Geschädigter | Skill aus `fachanwalt-verkehrsrecht` `unfall-haftungsquote-berechnen` | drei Jahre |
| Vermittlerhaftung | (Skill vermittler-haftung — perspektivisch) | drei Jahre |
| Industrieversicherung | (Skill industriedeckung — perspektivisch) | drei Jahre |

## Mandatsannahme

- **Konflikt-Check** — keine Mandate auf beiden Seiten der Versicherungs-Beziehung
- **Streitwert** ab EUR 10000 LG
- **Rechtsschutz-Deckungsanfrage** prüfen vor Mandatsannahme
- **Komplexität** AVB-Auslegung BGH-Urteilskette

## Eskalation

- **Telefon-Sofort** lebensbedrohliche KV-Ablehnung
- **Binnen einer Stunde** drohende Verjährung
- **Heute** Stellungnahme an Versicherung Rechtsschutz-Deckungsanfrage
- **Diese Woche** Klage-Erstentwurf

## Ausgabe

- `triage-protokoll-versicherungsrecht.md`
- Aktenanlage
- Rechtsschutz-Deckungsanfrage als Entwurf
- Frist im Fristenbuch
- Mandatsvereinbarung mit Honorarvereinbarung über RVG
- Empfehlung Folge-Skill

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen

- VVG §§ 1 ff.
- BGB §§ 195 199 305 ff.
- BGH IV. Zivilsenat
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Vertiefung — Rechtsprechung und Normenkette Triage

### Leitsatz-Zitate (Stand Mai 2026)

Vor Versand jeweils Volltext in juris.bundesgerichtshof.de oder dejure.org aufrufen:

- BGH IV ZR 32/24, Urt. v. 12.3.2025 — Krankentagegeld; Klauselersetzung nach Intransparenz unzulässig (Pressemitteilung Nr. 47/25 v. 12.3.2025)
- BGH IV ZR 70/25 — PKV-Beitragsanpassung; Mitteilungspflicht
- BGH IV ZR 86/24, Urt. v. 15.10.2025 — PKV-Beitragsanpassung; Prüfungsmaßstab
- BGH IV ZR 153/20, Urt. v. 14.7.2021 — Versicherungsfall BU nach Ablauf der sechs-monatigen Prognosezeit
- BGH VI ZR 183/22, Urt. v. 28.1.2025 — DSGVO-Schadensersatz Art. 82 hat nur Ausgleichs-, keine Straffunktion

### Normen-Ergänzung

§ 195 BGB (Verjährung 3 Jahre) i.V.m. § 199 BGB (Kenntnis-Beginn) → § 203 BGB (Hemmung Verhandlungen) → § 28 VVG (Obliegenheit Schadensanzeige) → § 115 VVG (Direktklage Haftpflicht) → § 204 BGB (Hemmung Mahnbescheid, Klage, Schlichtungsantrag) → § 214 VVG (Ombudsmann-Verjährungshemmung)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `fachanwalt-versicherungsrecht-orientierung`

_Orientierung im Versicherungsvertragsrecht für Mandate und Fachanwaltschaft nach FAO. Anwendungsfall Kanzlei will Versicherungsmandat beurteilen oder Anwalt bereitet sich auf Fachanwaltsprüfung Versicherungsrecht vor. Normen VVG VAG GDV-Musterbedingungen AVB-Sparten BU KV LV Sach-Haftpflicht D-und-O. Prüfraster Sparten Normen FAO-Voraussetzungen verifizierbare Quellen typische Mandate Fristen. Output Rechtsgebietsuebersicht Normen verifizierbare Quellen und Routing zu Versicherungsmandats-Skills. Abgrenzung zu mandat-triage-versicherungsrecht und fachanwalt-versicherungsrecht-deckungsklage._

# Fachanwalt für Versicherungsrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 80 Fälle in den letzten drei Jahren, davon mindestens 40 streitige.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Versicherungsvertrag | VVG §§ 1 ff. Anzeigepflicht §§ 19 ff. Praemienpflicht § 33 Leistungspflicht §§ 100 ff. |
| Versicherungsaufsicht | VAG |
| Pflichtversicherung Kfz | PflVG |
| Berufsunfähigkeit | §§ 172 ff. VVG |
| Krankenversicherung privat | §§ 192 ff. VVG MB/KK |
| Lebensversicherung | §§ 150 ff. VVG |
| Allgemeines Vertragsrecht | §§ 305 ff. BGB AGB-Kontrolle |
| Verjährung | § 195 BGB (drei Jahre) — Sonderregel § 12 VVG aufgehoben |

## Typische Mandate

- BU-Streitigkeiten (Leistungsablehnung)
- Krankheitskostenversicherung (Erstattung Pflegestufen)
- Lebensversicherung (Rückkaufswert Auszahlung im Todesfall)
- Hausratversicherung (Einbruchsdiebstahl Wasserschaden)
- Haftpflichtversicherung (Deckungsstreit)
- D-und-O-Versicherung für Organe Geschäftsleiter
- Berufshaftpflicht Anwaltshaftpflicht

## Fristen

- **Klagefrist** keine spezifische — Verjährung drei Jahre (§ 195 BGB).
- **Beschwerdefrist** zum BaFin gegen Versicherer regelmäßig keine Frist.
- **Anzeigepflichten** Versicherungsnehmer Unverzueglich (§ 19 VVG).
- **Frist nach Schadensfall** vertraglich vereinbart (Obliegenheiten § 28 VVG).

## Hauptgerichte

- Amtsgericht Landgericht (regulaere ZPO-Streitwertgrenze 10.000 EUR ab 01.01.2026).
- OLG / BGH IV. Zivilsenat für Versicherungssachen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- ARGE Versicherungsrecht DAV.

## Schnittstellen

- **kanzlei-allgemein** für Fristen und Versand.
- **fachanwalt-verkehrsrecht** bei Kfz-Haftpflicht.
- **fachanwalt-medizinrecht** bei Krankenversicherung.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate (Stand Mai 2026; offene Quellen)

Vor Versand jeweils Volltext in offener Quelle aufrufen (juris.bundesgerichtshof.de, dejure.org, openjur.de):

1. **BGH, Urt. v. 12.3.2025, IV ZR 32/24** — Krankentagegeldversicherung: Klauselersetzung nach Unwirksamkeit nicht ohne Weiteres zulässig; Versicherer kann unwirksame Tagessatz-Herabsetzung nicht durch im Kern gleiche neue Klausel ersetzen. Pressemitteilung Nr. 47/25 vom 12.3.2025.
2. **BGH, IV ZR 70/25, 2025** — PKV-Beitragsanpassung: Mitteilungsschreiben muss die konkrete Rechnungsgrundlage benennen (§ 203 Abs. 5 VVG).
3. **BGH, IV ZR 86/24, Urt. v. 15.10.2025** — Beitragsanpassung PKV; Prüfungsmaßstab. Quelle: bundesgerichtshof.de.
4. **BGH, Urt. v. 14.7.2021, IV ZR 153/20** — Versicherungsfall BU: Eintritt nach Ablauf der bedingungsgemäßen sechs-monatigen Prognosezeit.
5. **BGH, Urt. v. 28.1.2025, VI ZR 183/22** — DSGVO-Schadensersatz hat reine Ausgleichsfunktion; SCHUFA-Meldung bei streitiger Forderung unzulässig.

### Paragrafenkette (Überblick VVG-Struktur)

§§ 1–21 VVG (allgemeine Vorschriften, Informationspflichten, Widerruf) → §§ 28–32 VVG (Obliegenheiten, Rechtsfolgen) → §§ 74–99 VVG (Schadensversicherung) → §§ 100–112 VVG (Haftpflichtversicherung) → §§ 150–171 VVG (Lebensversicherung) → §§ 172–177 VVG (Berufsunfähigkeitsversicherung) → §§ 192–215 VVG (Krankenversicherung, Ombudsmann) → §§ 305–310 BGB (AGB-Kontrolle AVB) → § 215 VVG (örtliche Zuständigkeit Klage VN)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Fristen-Übersicht

| Bereich | Frist | Norm |
|---|---|---|
| Verjährung Versicherungsleistung | 3 Jahre ab Schluss Kenntnisjahr | §§ 195, 199 BGB |
| Widerruf (korrekte Belehrung) | 30 Tage | § 8 Abs. 1 VVG |
| Widerruf Lebensversicherung (falsche/fehlende Belehrung) | unbegrenzt (EuGH/BGH-Linie; Volltext vor Versand verifizieren) | § 8 VVG, EuGH C-209/12 (Endress) |
| Anzeigepflicht-Schadensfall | laut AVB (meist unverzüglich) | § 28 VVG |
| Hemmung durch Schlichtungsantrag | bis Entscheidung Ombudsmann | § 204 BGB i.V.m. § 214 VVG |

## Triage — Orientierungs-Routing

1. **Sachgebiet/Sparte identifizieren** (BU → `fachanwalt-versicherungsrecht-berufsunfaehigkeit-klage`; LV → `fachanwalt-versicherungsrecht-lebensversicherung-rueckkauf`; D&O → `fachanwalt-versicherungsrecht-do-deckungsabwehr`; Cyber → `fachanwalt-versicherungsrecht-cyber-loesegeld-sanktionsrecht`).
2. **Ablehnungsschreiben eingegangen?** → `fachanwalt-versicherungsrecht-leistungsablehnung-pruefen`.
3. **Klage vorbereiten?** → `fachanwalt-versicherungsrecht-deckungsklage` + `klage-versicherer-strategie`.
4. **Schlichtung zuerst?** → `fachanwalt-versicherungsrecht-ombudsmann-gdv-schlichtung`.
5. **Regress-Abwehr gegen Sozialversicherungsträger?** → `fachanwalt-versicherungsrecht-regress-abwehr`.

---

## Skill: `orientierung-mandat-fachanwaltschaft`

_Orientierung im Versicherungsvertragsrecht für Mandate und Fachanwaltschaft nach FAO: Anwendungsfall Kanzlei will Versicherungsmandat beurteilen oder Anwalt bereitet sich..._

# Orientierung im Versicherungsvertragsrecht für Mandate und Fachanwaltschaft nach FAO


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung im Versicherungsvertragsrecht für Mandate und Fachanwaltschaft nach FAO. Anwendungsfall Kanzlei will Versicherungsmandat beurteilen oder Anwalt bereitet sich auf Fachanwaltsprüfung Versicherungsrecht vor. Normen VVG VAG GDV-Musterbedingungen AVB-Sparten BU KV LV Sach-Haftpflicht D-und-O. Prüfraster Sparten Normen FAO-Voraussetzungen verifizierbare Quellen typische Mandate Fristen. Output Rechtsgebietsuebersicht Normen verifizierbare Quellen und Routing zu Versicherungsmandats-Skills. Abgrenzung zu mandat-triage-versicherungsrecht und fachanwalt-versicherungsrecht-deckungsklage.

### Fachanwalt für Versicherungsrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 80 Fälle in den letzten drei Jahren, davon mindestens 40 streitige.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Versicherungsvertrag | VVG §§ 1 ff. Anzeigepflicht §§ 19 ff. Praemienpflicht § 33 Leistungspflicht §§ 100 ff. |
| Versicherungsaufsicht | VAG |
| Pflichtversicherung Kfz | PflVG |
| Berufsunfähigkeit | §§ 172 ff. VVG |
| Krankenversicherung privat | §§ 192 ff. VVG MB/KK |
| Lebensversicherung | §§ 150 ff. VVG |
| Allgemeines Vertragsrecht | §§ 305 ff. BGB AGB-Kontrolle |
| Verjährung | § 195 BGB (drei Jahre) — Sonderregel § 12 VVG aufgehoben |

## Typische Mandate

- BU-Streitigkeiten (Leistungsablehnung)
- Krankheitskostenversicherung (Erstattung Pflegestufen)
- Lebensversicherung (Rückkaufswert Auszahlung im Todesfall)
- Hausratversicherung (Einbruchsdiebstahl Wasserschaden)
- Haftpflichtversicherung (Deckungsstreit)
- D-und-O-Versicherung für Organe Geschäftsleiter
- Berufshaftpflicht Anwaltshaftpflicht

## Fristen

- **Klagefrist** keine spezifische — Verjährung drei Jahre (§ 195 BGB).
- **Beschwerdefrist** zum BaFin gegen Versicherer regelmäßig keine Frist.
- **Anzeigepflichten** Versicherungsnehmer Unverzueglich (§ 19 VVG).
- **Frist nach Schadensfall** vertraglich vereinbart (Obliegenheiten § 28 VVG).

## Hauptgerichte

- Amtsgericht Landgericht (regulaere ZPO-Streitwertgrenze 10.000 EUR ab 01.01.2026).
- OLG / BGH IV. Zivilsenat für Versicherungssachen.

## Berufsverband

- ARGE Versicherungsrecht DAV.

## Schnittstellen

- **kanzlei-allgemein** für Fristen und Versand.
- **fachanwalt-verkehrsrecht** bei Kfz-Haftpflicht.
- **fachanwalt-medizinrecht** bei Krankenversicherung.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate (Stand Mai 2026; offene Quellen)

Vor Versand jeweils Volltext in offener Quelle aufrufen (juris.bundesgerichtshof.de, dejure.org, openjur.de):

1. **BGH, Urt. v. 12.3.2025, IV ZR 32/24** — Krankentagegeldversicherung: Klauselersetzung nach Unwirksamkeit nicht ohne Weiteres zulässig; Versicherer kann unwirksame Tagessatz-Herabsetzung nicht durch im Kern gleiche neue Klausel ersetzen. Pressemitteilung Nr. 47/25 vom 12.3.2025.
2. **BGH, IV ZR 70/25, 2025** — PKV-Beitragsanpassung: Mitteilungsschreiben muss die konkrete Rechnungsgrundlage benennen (§ 203 Abs. 5 VVG).
3. **BGH, IV ZR 86/24, Urt. v. 15.10.2025** — Beitragsanpassung PKV; Prüfungsmaßstab. Quelle: bundesgerichtshof.de.
4. **BGH, Urt. v. 14.7.2021, IV ZR 153/20** — Versicherungsfall BU: Eintritt nach Ablauf der bedingungsgemäßen sechs-monatigen Prognosezeit.
5. **BGH, Urt. v. 28.1.2025, VI ZR 183/22** — DSGVO-Schadensersatz hat reine Ausgleichsfunktion; SCHUFA-Meldung bei streitiger Forderung unzulässig.

### Paragrafenkette (Überblick VVG-Struktur)

§§ 1–21 VVG (allgemeine Vorschriften, Informationspflichten, Widerruf) → §§ 28–32 VVG (Obliegenheiten, Rechtsfolgen) → §§ 74–99 VVG (Schadensversicherung) → §§ 100–112 VVG (Haftpflichtversicherung) → §§ 150–171 VVG (Lebensversicherung) → §§ 172–177 VVG (Berufsunfähigkeitsversicherung) → §§ 192–215 VVG (Krankenversicherung, Ombudsmann) → §§ 305–310 BGB (AGB-Kontrolle AVB) → § 215 VVG (örtliche Zuständigkeit Klage VN)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Fristen-Übersicht

| Bereich | Frist | Norm |
|---|---|---|
| Verjährung Versicherungsleistung | 3 Jahre ab Schluss Kenntnisjahr | §§ 195, 199 BGB |
| Widerruf (korrekte Belehrung) | 30 Tage | § 8 Abs. 1 VVG |
| Widerruf Lebensversicherung (falsche/fehlende Belehrung) | unbegrenzt (EuGH/BGH-Linie; Volltext vor Versand verifizieren) | § 8 VVG, EuGH C-209/12 (Endress) |
| Anzeigepflicht-Schadensfall | laut AVB (meist unverzüglich) | § 28 VVG |
| Hemmung durch Schlichtungsantrag | bis Entscheidung Ombudsmann | § 204 BGB i.V.m. § 214 VVG |

## Triage — Orientierungs-Routing

1. **Sachgebiet/Sparte identifizieren** (BU → `fachanwalt-versicherungsrecht-berufsunfaehigkeit-klage`; LV → `fachanwalt-versicherungsrecht-lebensversicherung-rueckkauf`; D&O → `fachanwalt-versicherungsrecht-do-deckungsabwehr`; Cyber → `fachanwalt-versicherungsrecht-cyber-loesegeld-sanktionsrecht`).
2. **Ablehnungsschreiben eingegangen?** → `fachanwalt-versicherungsrecht-leistungsablehnung-pruefen`.
3. **Klage vorbereiten?** → `fachanwalt-versicherungsrecht-deckungsklage` + `klage-versicherer-strategie`.
4. **Schlichtung zuerst?** → `fachanwalt-versicherungsrecht-ombudsmann-gdv-schlichtung`.
5. **Regress-Abwehr gegen Sozialversicherungsträger?** → `fachanwalt-versicherungsrecht-regress-abwehr`.

---

## Skill: `erstgespraech-mandatsannahme`

_Strukturierter Erstgespraechsleitfaden für Versicherungsvertragsrecht (Personen- und Sachversicherung): Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen: Strukturier..._

# Strukturierter Erstgespraechsleitfaden für Versicherungsvertragsrecht (Personen- und Sachversicherung): Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierter Erstgespraechsleitfaden für Versicherungsvertragsrecht (Personen- und Sachversicherung): Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.

### Erstgespraech und Mandatsannahme im Versicherungsvertragsrecht (Personen- und Sachversicherung)

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Versicherungsvertragsrecht (Personen- und Sachversicherung) (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klären, Konflikt- und GwG-Prüfung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Versicherungsvertragsrecht (Personen- und Sachversicherung):

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klägerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Berufsunfaehigkeit, Unfallversicherung, Sachversicherung, RSV, Haftpflicht
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Deckungsklage, Klage BU/UB, Klage Sachversicherung, RSV-Deckungsklage). Frist-Alarm an die Vorbereitung weitergeben.

### 2. Konflikt-Prüfung und GwG-Check (5 Min.)

- Konflikt-Check über Mandantsystem: Gegnerin, Streitgegenstand, frueherer Mandant?
- GwG-Identifizierung: amtlicher Lichtbildausweis (Ausweisscan), bei juristischer Person Handelsregister-/Transparenzregister-Auszug, ggf. wirtschaftlich Berechtigte/n.
- Risikobewertung (niedrig/mittel/hoch) abhaengig von Mandatscharakter, Bargeld, Auslandsbezug.
- Doku im Mandatsbogen (Pflicht nach §§ 10 ff. GwG i.V.m. § 2 Abs. 1 Nr. 10 GwG für RA-Mandate).

### 3. Vollmacht und Schweigepflichtentbindung

- Allgemeine Prozess-/Aussenvollmacht (BORA, ZPO, FamFG, je nach Fachgebiet).
- Spezielle Vollmachten: ggf. Akteneinsicht Strafakte, KV-Abrechnungsdaten, Sozialdaten (Schweigepflichtentbindung gegenueber Krankenkasse, Arzt, Behörde).
- Bei Eheleuten/GbR/GmbH: einzelvollmachtgebende Person und Vertretungsmacht klären.

### 4. Streitwert und Gebührenvereinbarung

Standard-Streitwerte im Bereich Versicherungsvertragsrecht (Personen- und Sachversicherung):

- Skizze: Streitwert grob abschaetzen (z.B. Hauptforderung, ggf. + Zinsen, Nebenforderungen).
- RVG-Pauschalrechnung (Berechnungstool im Plugin) oder Stundenhonorarvereinbarung.
- Beratungshilfe-/Prozesskostenhilfe-Antrag prüfen, wenn wirtschaftlich angezeigt.
- Vorschussanforderung nach § 9 RVG.

### 5. Strategie-Erstskizze

Drei Weichen am Ende des Erstgespraechs:

- **Mandat annehmen:** vollstaendig (Prüfung + Schriftsatz) oder begrenzt (nur Prüfung/Gutachten).
- **Verweisen:** wenn Spezialgebiet ausserhalb der Fachanwaltschaft, oertlich unzuständig oder Konflikt.
- **Ablehnen:** offensichtlich aussichtslos, GwG-Hit, Bauchgefuehl-Vorsicht.

## Pflicht-Output am Ende

1. **Mandatsbogen** mit Beteiligten, Konflikt-Check, GwG-Status, Streitwert.
2. **Frist-Liste** (Sofortfristen, Verjährung, Ausschlussfristen, Beweisanforderungs-Fristen).
3. **Anlagenverzeichnis** des uebergebenen Datenraums (Stand erstes Sortieren).
4. **Naechster-Schritt-Plan:** binnen 24/48/72 h, Owner, Output.
5. **Honorarvereinbarung** unterschrieben oder Vorbehalt notiert.

## Relevante Rechtsgrundlagen und Standards

- BORA, BRAO, FAO für Fachanwaltschaft Versicherungsvertragsrecht (Personen- und Sachversicherung).
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- VVG, AVB, BU-/UV-Bedingungen, ARB, PflVG (für fachliche Erstpruefung).
- DSGVO und BDSG für den Umgang mit Mandantendaten (Art. 6 DSGVO als Rechtsgrundlage, Art. 9 ggf. Gesundheitsdaten).

## Typische Fehler im Erstgespraech

- Frist uebersehen, weil Mandantin sie nicht selber genannt hat (immer aus jedem Schreiben Frist herausziehen).
- Konflikt-Check nur nach Personennamen, nicht nach Sachzusammenhang (gleiche Liegenschaft, gleicher Sachverhalt).
- Vollmachtsumfang unklar -> später Streit mit Mandantin über Befugnisse.
- Honorarvereinbarung muendlich -> Beweisnot bei Streitwert-/Honorar-Streit.
- GwG: kein Lichtbildausweis erfasst, kein Aktenvermerk über Risikobewertung.

## Praxis-Checkliste

- [ ] Personalien und Rolle aller Beteiligten erfasst
- [ ] Konflikt-Check durchgefuehrt
- [ ] GwG: Identifizierung + Risikobewertung notiert
- [ ] Allgemeine Vollmacht unterschrieben
- [ ] Speziale Vollmacht / Entbindungserklaerung (wo noetig) unterschrieben
- [ ] Streitwert geschaetzt
- [ ] Honorarvereinbarung unterschrieben oder ausdruecklich auf RVG verwiesen
- [ ] Fristenliste angelegt und in Kalender eingetragen
- [ ] Mandatsbogen vollstaendig
- [ ] Naechster-Schritt-Plan dem Mandanten kommuniziert (E-Mail-Zusammenfassung)

## Konkrete Praxis-Konstellationen

### Konstellation A: Eilbeduerftigkeit

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Versicherungsvertragsrecht (Personen- und Sachversicherung)). Handlungs-Sequenz:

1. Sofort-Vollmacht und Sofort-Akteneinsicht (per beA, ELSTER, Behördenportal).
2. Antrag auf Wiedereinsetzung (§ 233 ZPO, § 60 VwGO, § 110 AO) als Reserve dokumentieren.
3. Spaeteste-Stunde-Versand-Plan: beA bevorzugt, mit qualifizierter Signatur und Empfangsbekenntnis.
4. Honorarvereinbarung NICHT auf Eilzuschlag verzichten - aber transparent kommunizieren.

### Konstellation B: Komplexer Sachverhalt, Datenraum unsortiert

Mandant uebergibt 200+ Dateien (PDF-Scans, E-Mails, Excel-Listen). Vor jeder fachlichen Bewertung:

1. Datenraum-Index in Excel: Datum, Absender, Empfaenger, Aktenzeichen, kurze Inhaltszeile.
2. Chronologischer Verlauf als Zeitstrahl - Spielraum für Verjährungs- und Ausschlussfristen identifizieren.
3. Loecher im Datenraum gezielt anfordern (Mandantenfragen-Katalog).

### Konstellation C: Interessenkonflikt-Naehe

Frueheres Mandat mit derselben Gegnerin oder gleichem Sachzusammenhang. Prüfung:

1. § 43a Abs. 4 BRAO und § 3 BORA - Sachzusammenhang, nicht nur Personenidentitaet.
2. Einwilligung beider Mandanten in Textform (mit konkreter Beschreibung).
3. Bei Zweifel: Mandat ablehnen und an Kanzleikollegium ueberweisen.

## Mandanten-Erwartungsmanagement

- Realistische Erfolgs- und Kostenprognose (nicht "Wir gewinnen sicher").
- Verfahrensdauer im Bereich Versicherungsvertragsrecht (Personen- und Sachversicherung): Erfahrungswerte nach Instanz.
- Vergleichschance vs. streitiges Urteil als Option offen halten.
- Schriftliche Zusammenfassung des Erstgespraechs binnen 48 h.

## Honorarvereinbarung - Best Practices

- RVG-Basis als Default, Stundenhonorar nur mit gesondertem Hinweis nach § 3a RVG.
- Erfolgshonorar nur in den engen Grenzen § 4a RVG.
- Vorschuss in Höhe der voraussichtlichen 1. Instanz.
- Klarstellung: Auslagen-Pauschale, USt, Reisekosten, Sachverstaendigenkosten gesondert.
- Bei PKH/Beratungshilfe-Mandant: schriftliche Belehrung, dass eigene Beitraege möglich sind.

## Mandatsbogen-Muster (Mindestinhalt)

- Mandant (Name, Geburtsdatum, Anschrift, Telefon, E-Mail)
- Gegner (Name, Anschrift, ggf. anwaltliche Vertretung)
- Kurzbeschreibung Sachverhalt (5-10 Saetze)
- Ziel des Mandats (eine Zeile)
- Strittige Fragen (bullet)
- Geprueft: Konflikt - GwG - Vollmacht
- Streitwert (Schaetzung)
- Honorarvereinbarung (RVG/Stunde/Pauschale)
- Frist-Liste
- Aktenanlage Datum
- Naechster-Schritt

## Cross-Refs

- `vergleichsverhandlung-strategie` (im selben Plugin) für den Fall, dass aussergerichtliche Loesung angestrebt wird.
- `schriftsatzkern-substantiierung` (im selben Plugin) für den Schriftsatzaufbau, wenn Klage/Widerspruch eingereicht wird.
- Kanzlei-Allgemein-Plugin `kanzlei-allgemein` für Konflikt-, GwG- und PEP-Prüfroutinen.

## Vertiefung — Normenkette und Rechtsprechung Erstgespräch Versicherungsrecht

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normenkette Erstgespräch / Mandatsannahme Versicherungsrecht

§ 6 VVG (Beratungspflicht Versicherer; Anwalt analog für Mandant) → §§ 195, 199, 203, 204 BGB (Verjährung, Hemmung) → § 215 VVG (Zuständigkeit bei Klage) → §§ 43a, 45 BRAO (Konfliktprüfung) → §§ 3, 3a RVG (Vergütungsvereinbarung) → §§ 10, 11 GwG (Identifizierungspflicht) → § 9 RVG (Vorschuss)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `erstpruefung-und-mandatsziel`

_Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel


## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 241 Abs. 2 BGB` — Rücksichtnahme-, Schutz- und Organisationspflichten.
- `§ 242 BGB` — Treu und Glauben als Korrektiv enger Klausel- und Anspruchsarbeit.
- `§ 280 Abs. 1 BGB` — Pflichtverletzung, Vertretenmuessen, Schaden.
- `§ 286 Abs. 1 BGB` — Verzug und Fristlogik.
- `§ 195 BGB` — regelmäßige Verjährung.
- `§ 199 Abs. 1 BGB` — Beginn der regelmäßigen Verjährung.
- `§ 253 Abs. 2 ZPO` — Bestimmtheit von Antrag und Klagegrund.
- `§ 138 Abs. 1 ZPO` — Wahrheitspflicht und vollstaendiger Tatsachenvortrag.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** VVG, VAG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Fachanwalt** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `fachanwalt-versicherungsrecht-cyber-loesegeld-sanktionsrecht`

_Cyber-Versicherung bei Ransomware mit Sanktionsrisiko und Geldwäscherecht. Anwendungsfall Unternehmen erhaelt Erpressung durch Ransomware und prüft Lösegeldzahlung auf Versicherungsdeckung und Sanktionsrechtsverstoesse. Normen VVG Cyber-Deckung EU-Sanktions-VO 833/2014 269/2014 OFAC-Advisory § 261 StGB Geldwäsche AWG § 34 Aussenwirtschaftsstrafrecht. Prüfraster Deckungsschutz Versicherer Lösegeldzahlung Sanktionsprüfung Empfaenger OFAC-Screening Strafrechtsrisiko BaFin-Meldung. Output Cyber-Schadenprotokoll mit Sanktionsprüfung Deckungsanalyse und Handlungsempfehlung für oder gegen Lösegeldzahlung. Abgrenzung zu fachanwalt-it-recht-cyber-vorfall-sofortmassnahmen und fachanwalt-versicherungsrecht-deckungsklage._

# Cyber-Lösegeld bei Ransomware mit Sanktions-Risiko

## Zweck

Spezial-Mandat: Mandant hat Cyber-Versicherung, wurde Opfer eines Ransomware-Angriffs. Eine Lösegeldzahlung wird erwogen oder wurde bereits geleistet. Der Versicherer verweigert Deckung mit Verweis auf Sanktionsrisiko (OFAC Specially Designated Nationals List, EU-Russland-Sanktionen, Lazarus Group Nordkorea). Dieser Skill begleitet sowohl die versicherungsrechtliche Deckungsklage als auch die strafrechtliche Risikobewertung.

## Kaltstart-Rückfragen

1. Liegt der vollständige Versicherungsvertrag (Cyber-Police) mit GDV-Musterbedingungen oder individuellen Klauseln vor — insbesondere: Enthält die Police eine Sanctions Limitation Clause?
2. Welche Indizien liegen zur Identität des Angreifers vor — Crypto-Wallet-Adresse, Tor-Adresse, Kommunikation, Malware-Signatur?
3. Wurde ein Chainalysis- oder Elliptic-Screening der Wallet-Adresse durchgeführt, und liegt ein Treffer auf der OFAC SDN List oder EU-Sanktionslisten vor?
4. Wann wurde das Lösegeld gezahlt (falls bereits erfolgt) oder wann wird die Zahlung erwogen?
5. Hat der Mandant Bezug zu den USA (US-Tochtergesellschaft, US-Kunden, US-Korrespondenzbank), der OFAC-Extraterritorialität auslösen könnte?
6. Wurde das BSI (bei KRITIS) und das LKA Cybercrime informiert?
7. Welche Backup-Optionen bestehen — wurde eine Datenwiederherstellung ohne Zahlung versucht?
8. Liegt das Ablehnungsschreiben des Versicherers vor und auf welche Klausel stützt dieser sich?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Sanktionsrecht

- **VO (EU) 833/2014** — Russland-Wirtschaftssanktionen (Sektorsanktionen, Finanztransaktionen mit Bezug zu Russland); zahlreiche Erweiterungspakete 2022–2025.
- **VO (EU) 269/2014** — Russland-Personensanktionen; Vermögenseinfrierung gelisteter Personen.
- **OFAC SDN List** (USA) — Specially Designated Nationals; 50-%-Regel: Unternehmen zu 50 % oder mehr im Eigentum einer SDN-gelisteten Person gilt selbst als SDN.
- **§§ 17, 18 AWG** — Embargo-Verstöße; Freiheitsstrafe bis 10 Jahre bei Vorsatz; Ordnungswidrigkeitenrahmen § 81 AWV.
- **OFAC Advisory vom 21.09.2021 zu Ransomware** — Lösegeld-Zahlungen an sanktionierte Akteure können selbst US-Sanktionsverstöße sein; strenge Haftung (strict liability) — guter Glaube keine Verteidigung.
- **Chainalysis Sanctions Screening** / **Elliptic** — forensische Tools zur Wallet-Rückverfolgung; Screening-Ergebnis ist dokumentationspflichtiger Compliance-Nachweis.

### Versicherungsrecht

- **§ 81 VVG** — Herbeiführung des Versicherungsfalls; Eigenverschulden des VN; quotale Kürzung bei grober Fahrlässigkeit.
- **§ 28 VVG** — Obliegenheitsverletzung; Kein-Backup-Vorwurf des Versicherers.
- **Sanctions Limitation Clause** in Cyber-Policen — typische Formulierung: "Der Versicherer erbringt keine Leistungen, die ihn oder seinen Rückversicherer einem Verstoß gegen Sanktionsrecht aussetzen würden." Prüfung auf Unwirksamkeit nach § 307 BGB Transparenzgebot.
- **GDV-Musterbedingungen Cyber AVB 2022** — Standarddeckung Ransomware als Versicherungsfall (§ 1 AVB Cyber); Deckungsausschluss nur bei vorsätzlicher Herbeiführung.

### Strafrecht

- **§ 261 StGB** — Geldwäsche; Lösegeld kann aus erpresserischer Bedrohung stammen (Vortat); Strafbarkeit auch bei Leichtfertigkeit.
- **§ 89c StGB** — Terrorismusfinanzierung (bei OFAC-gelisteten Gruppen: Hamas, Lazarus Group / Nordkorea, Hizballah).
- **§ 18 AWG** — Strafrechtliche Sanktionsverletzung bei Zahlung an SDN-gelistete Empfänger.

### Leitentscheidungen (Stand Mai 2026)

Verifizierte Anker (Volltext vor Versand in offener Quelle aufrufen):

| Gericht | Aktenzeichen / Quelle | Datum | Kernaussage |
|---|---|---|---|
| BGH IV. ZS | IV ZR 32/24 (juris.bundesgerichtshof.de) | 12.3.2025 | Klauselersetzung nach Intransparenz unzulässig (übertragbar auf Cyber-AVB-Anpassungen) |
| BGH VI. ZS | VI ZR 183/22 (juris.bundesgerichtshof.de) | 28.1.2025 | DSGVO-Schadensersatz hat nur Ausgleichs-, keine Straffunktion (relevant für Cyber-Schadensersatz Drittansprüche) |
| EuGH | C-300/21 (curia.europa.eu) | 4.5.2023 | Art. 82 DSGVO setzt konkret nachgewiesenen Schaden voraus |
| OFAC SDN-Liste | sanctionssearch.ofac.treas.gov | laufend | US-Sanktionsliste; bei Match Zahlung verboten |
| EU-Sanktionsliste | sanctionsmap.eu | laufend | EU-Sanktionen; VO (EU) 269/2014, 833/2014, MiCA-Begleitregelung |

Konkrete BGH-Rechtsprechung zu Cyber-AVB ist bisher dünn; OLG-Entscheidungen vor Versand in openjur.de oder nrwe.de prüfen.

## Prüfschema in Tabellenform


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

| Nr. | Prüfschritt | Norm | Konsequenz |
|---|---|---|---|
| 1 | Versicherungsfall Ransomware in AVB definiert? | GDV AVB Cyber; Police | Versicherungsfall "IT-Sicherheitsverletzung" umfasst Ransomware |
| 2 | Sanctions Limitation Clause vorhanden? | Police Individualklausel | Klausel prüfen auf Unwirksamkeit § 307 BGB |
| 3 | Erpresser auf OFAC SDN List? | OFAC SDN List; Chainalysis | SDN-Match → Zahlung verboten; kein Versicherungsschutz für verbotene Handlung |
| 4 | Erpresser auf EU-Sanktionslisten? | VO (EU) 269/2014; 833/2014 | EU-Sanktionsrecht unabhängig von US-OFAC |
| 5 | Kein SDN-Match — Sanktionsrisiko dennoch? | OFAC 50-%-Regel | Indirekte Sanktionierung prüfen; Compliance-Memo |
| 6 | US-Bezug des Mandanten? | AWG; OFAC-Jurisdiktion | Extraterritorialität bei US-Kunden/Bankkonto |
| 7 | Backup-Versuch vor Zahlung? | § 28 VVG Obliegenheit | Fehlender Backup-Versuch → Obliegenheitsverletzung-Risiko |
| 8 | BSI/LKA informiert? | § 8b BSIG; Polizei | Pflicht bei KRITIS; ggf. rechtfertigend für Zahlung |
| 9 | Lösegeldzahlung strafbar § 261 StGB? | § 261 StGB | Vortat Erpressung: Vortatanknüpfung ja; Strafbarkeit bei Leichtfertigkeit |
| 10 | § 89c StGB Terrorismusfinanzierung? | § 89c StGB | Bei OFAC-gelisteten Terrorgruppen |
| 11 | DSGVO-Meldepflichten und mögliche Drittansprüche geprüft? | Art. 33, 34, 82 DSGVO | Meldefristen 72 Stunden Aufsichtsbehörde; Schadensersatz nach Art. 82 nur bei konkretem Schaden (EuGH C-300/21) |
| 12 | Grob fahrlässige Herbeiführung § 81 VVG? | § 81 VVG | Sicherheitspflichten verletzt? Kein Backup? |
| 13 | Deckungsklage LG-Sitz des Versicherers? | § 215 VVG; § 71 GVG | LG bei Streitwert ab EUR 10000 |
| 14 | Parallele Strafverteidigung nötig? | §§ 17, 18 AWG; § 261 StGB | Bei Zahlung an SDN: sofort Strafverteidiger |
| 15 | Compliance-Dokumentation für Akten? | AWG; OFAC Advisory | Screening-Ergebnis und Entscheidungsweg dokumentieren |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Cyber-Loesegeld-Zahlung und Sanktionsrecht pruefend | Sanktionspruefung + Deckungsanalyse nach Schema; Schriftsatz unten |
| Variante A — Zahlung bereits erfolgt Genehmigung nachtraeglich | OFAC-Antrag rueckwirkend stellen; Dokumentation sichern |
| Variante B — Versicherer verweigert Deckung wegen Sanktionsklausel | Deckungsklage parallel; Sanktionsrecht-Verteidigung separat |
| Variante C — Keine Zahlung geplant Wiederherstellung Vorrang | IT-Forensik und Wiederherstellung statt Loesegeldzahlung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1 — Schadensanzeige und Deckungsanforderung

```
An [Versicherer Cyber]
Versicherungsnummer: [Nr]
Schadenummer: [neu]

Betr.: Ransomware-Vorfall vom [Datum]
       Deckungsanforderung und Compliance-Memo

Sehr geehrte Damen und Herren,

wir vertreten die [Unternehmen GmbH]. Am [Datum] wurde unsere
Mandantin Opfer eines Ransomware-Angriffs durch die Gruppe
[Bezeichnung], der zu Datenverschlüsselung und Betriebsausfall
führte. Einzelheiten ergeben sich aus dem Forensik-Bericht
vom [Datum], Anlage K1.

I. Versicherungsfall

Nach § [X] AVB Cyber liegt ein Versicherungsfall (IT-Sicherheits-
verletzung durch Cyber-Angriff) vor. Lösegeldforderung in Höhe
von EUR/USD [Betrag].

II. Sanctions-Compliance

Vor jeder Lösegeld-Entscheidung hat unsere Mandantin ein
Sanctions Screening durchgeführt:
- Wallet-Analyse durch Chainalysis Reactor am [Datum]:
  Kein direkter OFAC SDN-Match; Risikostufe [X] (Anlage K2).
- Keine Übereinstimmung mit EU-Sanktionslisten
  (VO (EU) 833/2014; VO (EU) 269/2014) (Anlage K3).
- Compliance-Memo der Rechtsabteilung vom [Datum] (Anlage K4).

Die Zahlung war daher rechtlich zulässig. Ihre Sanctions
Limitation Clause greift nicht ein, da kein sanktionierter
Empfänger vorliegt.

III. Deckungsanforderung

Wir fordern Sie auf, die Police-Leistungen wie folgt zu erbringen:
1. Lösegeldsumme EUR [X]
2. Betriebsunterbrechungsschaden EUR [Y] pro Tag × [Z] Tage
3. Forensik- und Wiederherstellungskosten EUR [Z]
4. Anwaltskosten EUR [...]

Bitte bestätigen Sie die Deckung bis [Datum + 2 Wochen].

[Rechtsanwälte]
```

### Baustein 2 — Deckungsklage: Sanctions Limitation Clause unwirksam

```
IV. SANCTIONS LIMITATION CLAUSE UNWIRKSAM

Die Beklagte stützt ihre Ablehnung auf die Sanctions Limitation
Clause in § [X] der Police, die lautet:
"[Wortlaut der Klausel]."

Diese Klausel ist unwirksam gemäß § 307 Abs. 1 Satz 2 BGB
(Transparenzgebot), weil ein durchschnittlicher Versicherungsnehmer
nicht erkennen kann,
a) welche Sanktionslisten konkret gemeint sind (US-OFAC, EU, UN,
   Bundesbank?),
b) welcher Standard für eine "Sanktionierung" gilt (SDN-Direkteintrag,
   50-%-Regel, Sektorsanktion?), und
c) ab welchem Grad der Verbindung zwischen Angreifer und Sanctions-Liste
   die Klausel auslöst.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
klar und verständlich formuliert sein; bei Unklarheit gilt
§ 305c Abs. 2 BGB zugunsten des Versicherungsnehmers.

Hilfsweise: Selbst wenn die Klausel wirksam wäre, greift sie im
Streitfall nicht ein, weil das Chainalysis-Screening eindeutig
keinen SDN-Match ergeben hat (Anlage K2).
```

### Baustein 3 — Compliance-Memo vor Lösegeldzahlung (Musterstruktur)

```
COMPLIANCE-MEMO — RANSOMWARE LÖSEGELDZAHLUNG
Vertraulich — Anwaltlich vertretene Angelegenheit

Datum: [Datum]
Mandant: [Unternehmen]

I. Sachverhalt
[Datum/Uhrzeit Angriff], Verschlüsselung [X] Systeme,
Lösegeldforderung [Betrag] in Bitcoin an Wallet [Adresse].

II. Screening-Ergebnis
Chainalysis Reactor-Analyse vom [Datum]:
- Direkte OFAC SDN Prüfung: kein Match
- Indirekte Sanktionsverbindung (50-%-Regel): kein Befund
- EU-Sanktionslisten (VO 269/2014; VO 833/2014): kein Match
- UN-Sanktionslisten: kein Match
Ergebnis: Sanktionsrechtliches Risikolevel = NIEDRIG

III. Strafrechtliche Bewertung
§ 261 StGB Geldwäsche: Vortat Erpressung liegt vor;
Strafbarkeit bei Leichtfertigkeit denkbar. Keine Leichtfertigkeit,
da Screening-Pflichten erfüllt.

§ 89c StGB: Keine Anhaltspunkte für Terrorgruppe.

IV. AWG
§ 17/18 AWG: Bei fehlendem SDN-Match kein Verstoss;
US-Bezug gering (kein US-Konto/US-Tochter).

V. Empfehlung
Unter Berücksichtigung des Screener-Ergebnisses und der
mangelnden Backup-Verfügbarkeit für [X Systeme] ist eine
kontrollierte Lösegeldzahlung rechtlich vertretbar.
Dokumentation für Rückversicherer und BaFin anlegen.

[Rechtsanwälte / Compliance Officer]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Beweislast und Darlegungslast

| Frage | Beweislast |
|---|---|
| Versicherungsfall (Ransomware als IT-Sicherheitsverletzung) | Kläger (VN) |
| Sanctions Limitation Clause anwendbar | Versicherer |
| SDN-Match tatsächlich vorhanden | Versicherer (muss konkrete Liste und Eintrag benennen) |
| Screening ordnungsgemäß durchgeführt | VN (Chainalysis-Bericht, Datum, Methodik) |
| Obliegenheitsverletzung (kein Backup-Versuch) | Versicherer |
| Sanctions Limitation Clause wirksam | Versicherer (Transparenztest) |

## Fristen und Verjährung

| Frist | Dauer | Anker | Norm |
|---|---|---|---|
| Schadensanzeige | unverzüglich (24–48 Stunden) | Angriffserkenntnis | Police; § 30 VVG |
| BSI-Meldung (KRITIS) | 24 Stunden Frühwarnung | Ersterkenntnis | § 8b BSIG |
| NIS2-Meldung | 72 Stunden | Ersterkenntnis | NIS2UmsuCG |
| Verjährung Versicherungsanspruch | 3 Jahre | Jahresende Kenntnis | §§ 195, 199 BGB |
| OFAC SDGT-Meldepflicht (US-Bezug) | 10 Werktage nach Zahlung | Zahlung | OFAC Reg. 31 CFR Part 501 |
| Verjährung AWG-Verstöße | 5 Jahre | §§ 17, 18 AWG | § 31 OWiG |

## Typische Gegenargumente und Reaktion

| Einwand Versicherer | Reaktion |
|---|---|
| SDN-Match vorhanden | Screening-Bericht vorlegen; konkrete Wallet-Rückverfolgung durch SV; Versicherer muss Match beweisen |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Kein Backup = grobe Fahrlässigkeit | § 28 Abs. 3 VVG: Kausalität; Backup-Fehler muss kausal für konkrete Lösegeldhöhe sein |
| Lösegeld = Vorsatz § 81 VVG | Keine Vorsatz-Herbeiführung des Angriffs durch VN; Zahlung als Notreaktion |
| Kein Versicherungsfall — "vorsätzliche Tat Dritter" | Drittangriff ist Versicherungsfall; kein Vorsatz des VN |
| Deckung ausgeschlossen wegen § 261 StGB | § 261 StGB schützt VN nicht; Versicherer kann nicht auf Strafbarkeit des VN verweisen, die er durch eigene Deckungsverweigerung erst veranlasst hat |

## Streitwert und Kosten

- Versicherungsleistung: Lösegeld + Betriebsunterbrechung + Forensikkosten; oft EUR 100000 bis mehrere Mio. EUR.
- LG-Verfahren obligatorisch bei Streitwert über EUR 10000 (§ 71 GVG).
- Sachverständige für Blockchain-Forensik: EUR 5000–20000 je nach Umfang.
- OFAC-Lizenz für US-Bezug: Antragstellung bei OFAC, USD 150–500; Bearbeitung 30–90 Tage.

## Strategische Empfehlung

- **Vor Zahlung:** Immer Chainalysis-Screening; Compliance-Memo erstellen; Versicherer frühzeitig informieren.
- **Bei SDN-Match:** Keine Zahlung; Versicherer und BSI/LKA informieren; OFAC-Specific License beantragen falls US-Bezug.
- **Deckungsklage:** Sanctions Limitation Clause auf Transparenz angreifen; SV für Blockchain-Forensik beauftragen.
- **Strafverteidigung parallel:** Bei Verdacht eines AWG-Verstoßes sofort Parallelverteidiger beiziehen.

## Anschluss-Skills

- `deckungsanfrage-pruefen` — allgemeines Deckungsprüfschema
- `klage-versicherer-strategie` — Klagestrategie nach Ablehnung
- `fachanwalt-versicherungsrecht-deckungsklage` — Klageschrift

## Quellen

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Paragrafenkette

§ 261 StGB (Geldwäsche, n.F. seit 2021) → § 16 AWG (Verstöße gegen Außenwirtschaftsgesetz bei Sanktionsbruch) → Art. 4 VO 833/2014, Art. 2 VO 269/2014 (Russland-Sanktionen, Bereitstellungsverbot) → OFAC SDN-Liste (US-Treasury, extraterritoriale Wirkung) → § 134 BGB (Nichtigkeit bei Gesetzesverstößen) → §§ 100 ff. VVG (Haftpflichtversicherung Cyber) → § 1 VVG i.V.m. Cyber-AVB (Versicherungsfall Definition) → § 81 VVG (Ausschluss vorsätzliche Schadenverursachung)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Fristen-Übersicht

| Maßnahme | Frist | Rechtsgrundlage |
|---|---|---|
| Meldung Ransomware-Vorfall an BSI | unverzüglich (KRITIS-Unternehmen) | § 8b BSIG |
| Geldwäsche-Meldepflicht | unverzüglich | § 43 GwG |
| Schadensanzeige Cyber-Versicherer | laut AVB (meist 7-14 Tage) | AVB Cyber |
| OFAC-Meldepflicht bei sanktionierten Empfängern | unverzüglich | OFAC-Regularien |

## Triage — Sofortprüfung Ransomware / Cyber-Lösegeld

1. **Identität des Angreifers prüfen:** Bekannte Ransomware-Gruppe auf OFAC SDN-Liste (z.B. Evil Corp, Conti-Affiliates)? → Bei OFAC-Listing: Zahlung ohne Lizenz verboten; Versicherer verweigert ggf. Deckung.
2. **EU-Sanktionsrecht prüfen:** Empfänger auf VO 269/2014 oder VO 833/2014 gelistet? → § 134 BGB, § 16 AWG-Risiko.
3. **Cyber-Versicherungspolice prüfen:** Lösegeld-Zahlungen ausdrücklich gedeckt? Sanktions-Ausschlussklausel in AVB?
4. **Geldwäscheprüfung:** § 261 StGB n.F. — kennt oder muss Zahler wissen, dass Empfänger aus Straftaten stammt? Interne AML-Prüfung dokumentieren.
5. **Meldepflichten erfüllt:** BSI (KRITIS), BaFin (regulierte Unternehmen), Staatsanwaltschaft (§ 261 StGB)?

**Entscheidungsbaum:**
```
Ransomware-Angriff + Lösegeld-Forderung?
├─ Angreifer auf OFAC-SDN-Liste? → Zahlung ohne US-Lizenz verboten
│   └─ Versicherer: Deckungsausschluss prüfen (§ 134 BGB + AVB)
├─ Angreifer auf EU-Sanktionsliste? → § 16 AWG + VO 269/2014
│   └─ Behördliche Genehmigung (BAW) erforderlich?
├─ Angreifer nicht gelistet → Geldwäsche-Risiko § 261 StGB prüfen
│   └─ AML-Prüfung dokumentieren; Meldepflicht § 43 GwG?
└─ Cyber-AVB analysieren → Lösegeld gedeckt? Sanktions-Klausel?
```

---

## Skill: `fachanwalt-versicherungsrecht-ombudsmann-gdv-schlichtung`

_Außergerichtliche Schlichtung über Versicherungs-Ombudsmann oder PKV-Ombudsmann als Alternative zur Klage. Anwendungsfall Streitwert bis 10000 EUR oder Mandant will Klage vermeiden und Schlichtung versuchen. Normen §§ 214 ff. VVG Schlichtungsverfahren § 204 BGB Hemmung Verjährung VSBG Verbraucherstreitbeilegungsgesetz § 84 VVG Sachverständigenverfahren. Prüfraster Zuständigkeit Ombudsmann Streitwert Schlichtungsantrag Beschwerdewortlaut PKV-Ombudsmann BaFin-Verbraucherbeschwerde. Output Schlichtungsantrag mit Sachverhaltsdarstellung Normbezug und Zuständigkeitsprüfung. Abgrenzung zu fachanwalt-versicherungsrecht-deckungsklage und klage-versicherer-strategie._

# Versicherungs-Ombudsmann / GDV-Schlichtung

## Zweck

Versicherungsrechts-Streit (Leistung, Anpassung, Kündigung) ist häufig im außergerichtlichen Schlichtungsverfahren günstig zu lösen: **Versicherungs-Ombudsmann e.V.** für PKV/Kompositversicherer, **PKV-Ombudsmann** für private Kranken/Pflege, **BaFin-Beschwerde** als Aufsichts-Eingang, **Sachverständigen-Verfahren § 84 VVG** bei Schadenhöhe-Streit.

## Eingaben

- Versicherungssparte (Sach, Haftpflicht, Leben, BU, PKV, Pflege, Rente)
- Streitgegenstand (Leistungsablehnung, Beitragsanpassung, Kündigung, Schadenhöhe)
- Versicherer (Verband: GDV Mitgliedschaft?)
- Streitwert (≤ 10.000 EUR: Ombudsmann-Verbindlichkeit Versicherer)
- Mandant (Verbraucher / Unternehmer)

## Rechtlicher Rahmen

- **§§ 1 ff. VVG** — Versicherungsvertragsgesetz
- **§ 6 VVG** — Beratungspflicht
- **§ 84 VVG** — Sachverständigen-Verfahren
- **§ 213 VVG** — Anfechtung wegen Anzeigepflichtverletzung
- **§ 203 VVG** — Beitragsanpassung PKV
- **§ 14 UKlaG** — Schlichtungs-Pflicht Verbraucher
- **VSBG** — Verbraucherstreitbeilegungs-Gesetz
- **Versicherungs-Ombudsmann-Verfahrensordnung 2021** (geändert 2024)

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## ADR-Pfade

### Pfad 1 — Versicherungs-Ombudsmann (VVR e.V.)

- Bis 10.000 EUR: Versicherer-Bindung an Spruch (sofern Mitglied)
- Bis 100.000 EUR: Schlichtungs-Vorschlag (nicht bindend)
- Zuständigkeit: alle Sparten außer PKV/Pflege (eigener Ombudsmann)
- Kostenfrei für Verbraucher
- Frist Beschwerde: 6 Monate nach Versicherer-Ablehnung

### Pfad 2 — Ombudsmann PKV / Pflege (PKV-Ombudsmann e.V.)

- Privater Kranken/Pflege-Vers.
- Verfahrens-Dauer 3-6 Monate
- Schlichtungs-Vorschlag

### Pfad 3 — BaFin-Beschwerde

- Aufsichts-Behörde
- Kein Einzelfall-Spruch, aber Hinweis-Wirkung
- Bei systemischen Mängeln effektiv

### Pfad 4 — Sachverständigen-Verfahren § 84 VVG

- Bei Schadenhöhe-Streit (Hausrat, Gebäude, Kfz)
- Versicherer + Vers.-Nehmer benennen je 1 Sachverständigen
- Obmann bei Dissens
- Bindend (sofern nicht offenbar erheblich falsch)

## Workflow

### Phase 1 — Versicherer-Korrespondenz

- Schadensanzeige (Fristen je nach Sparte)
- Versicherer-Position abwarten
- Schriftliche Ablehnung als Eingang

### Phase 2 — Beschwerde-Vorbereitung

- Versicherungsbedingungen (AVB) analysieren
- Anzeigepflicht-Erfüllung dokumentieren
- Streitwert ermitteln

### Phase 3 — Ombudsmann-Antrag

- Online-Antrag bei VVR e.V. / PKV-Ombudsmann
- Sachverhalt + AVB + Versicherer-Korrespondenz
- Vollmacht Anwalt (möglich)

### Phase 4 — Schlichtungs-Verfahren

- Versicherer-Stellungnahme (4 Wochen)
- ggf. mündliche Erörterung
- Schlichtungs-Spruch / Vorschlag

### Phase 5 — Klage bei Scheitern

- LG / AG je Streitwert
- Bei PKV-Anpassung: spezialisierte Kammern

## Strategie und Taktik

- **Ombudsmann zuerst** — billig, schnell, oft erfolgreich
- **§ 213 VVG Anfechtung**: Anzeigepflicht-Verletzung sehr genau prüfen — Versicherer hat enge Belehrungs-Pflichten
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Sachverständigen-Verfahren**: bei klar bezifferbarem Schaden günstig; bei rechtlichen Fragen ungeeignet
- **BU-Versicherung**: 50-%-Berufsunfähigkeits-Anforderung; Sachverständigen-Strategie kritisch

## Querverweise

- `fachanwalt-versicherungsrecht-orientierung` — Triage
- `fachanwalt-versicherungsrecht-leistungsklage-vvg` — Klage
- `fachanwalt-versicherungsrecht-cyberversicherung-nis2` — Sonderfall
- `fachanwalt-bank-kapitalmarktrecht-ombudsmann-bafin-schlichtung` — Bank-Variante

## Quellen und Updates

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§ 214 VVG (Ombudsmann-Schlichtung, Verjährungshemmung) → § 204 Abs. 1 Nr. 4 BGB (Hemmung durch Schlichtungsantrag) → § 84 VVG (Sachverständigen-Verfahren) → VSBG (Verbraucherstreitbeilegungsgesetz) → VomVO (Verordnung über Versicherungsombudsmann) → § 6 VomVO (Bindungswirkung für Versicherer bis 10.000 EUR)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `fachanwalt-versicherungsrecht-berufsunfaehigkeit-klage`

_Klage bei abgelehnter Berufsunfähigkeitsversicherungs-Leistung. Anwendungsfall BU-Versicherung hat Leistungsantrag abgelehnt oder Verweisung auf andere Tätigkeit ausgesprochen. Normen §§ 172 ff. VVG BU-Versicherung § 15 VVG Anzeigepflicht BAG-Begriff Berufsunfähigkeit 50-Prozent-Grenze. Prüfraster Begriff Berufsunfähigkeit letzte berufliche Tätigkeit Verweisung zumutbare andere Tätigkeit Gutachtenstreit Prüfverfahren. Output Klageschrift-Baustein mit Leistungsantrag Sachverständigenantrag Feststellungsantrag und Durchsetzungsstrategie. Abgrenzung zu fachanwalt-versicherungsrecht-deckungsklage und fachanwalt-versicherungsrecht-leistungsablehnung-prüfen._

# Berufsunfähigkeit-Klage

## Zweck

Mandate von Versicherungs-Nehmern bei abgelehnter Berufsunfähigkeit (BU).

## 1) BU-Begriff

### Definition

- **Berufsunfähigkeit** = > **50 % Beeintraechtigung** in der letzten beruflichen Tätigkeit
- Beruf wie vor Eintritt
- Dauerhaft (typisch > 6 Monate prognostiziert)

### Abstrakte vs. konkrete BU

- Abstrakt: alle Berufe gleichwertiger Art
- Konkret: spezifischer letzter Beruf
- Heute meist konkret

## 2) Verweisungs-Klausel

### Standard

- "Wenn Versicherter zumutbare andere Tätigkeit ausueben kann, ist nicht BU"
- Verweisung auf vergleichbare Berufe

### Verweisungslinie nach BGH-Rechtsprechung

- Seit dem grundlegenden Wandel der BGH-Rechtsprechung ist nur die **konkrete Verweisung** auf eine tatsächlich ausgeübte Vergleichstätigkeit zulässig. Abstrakte Verweisung allein auf eine theoretisch denkbare Tätigkeit reicht nicht.
- Konkretisierende Anforderungen vor Verwendung des Versicherer-Verweisungsargumentes in juris.bundesgerichtshof.de und dejure.org verifizieren; nicht aus Modellwissen.
- Wichtige Linie (Stand Mai 2026): Bedingungen, die Versicherungsschutz auf Bürotätigkeit mit > 90 % Schreibtischanteil begrenzen, sind intransparent und benachteiligend (BGH IV. ZS, st. Rspr. — konkrete Entscheidung mit Aktenzeichen und Datum vor Ausgabe verifizieren).

## 3) Ablehnungs-Gründe Versicherer

### Pflichtverletzung Anzeige-Pflicht § 19 VVG

- Vorerkrankungen nicht angegeben
- Bei Schwer-Verstoß: Vertrags-Anpassung / Aufhebung

### Mangelnder Beweis BU

- Gutachten beantwortet nicht 50 %-Schwelle
- Eigene Schädigung

### Verweisung

- Andere zumutbare Tätigkeit ausueubar
- Konkret bestätigt

## 4) Workflow


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

### Phase 1 — Beratung Vers.-Nehmer

- Vertragsprüfung (BU-Klausel)
- Erkrankungs-Stand
- Bisherige Korrespondenz

### Phase 2 — Versicherer-Antrag

- Vollständige Antrags-Unterlagen
- Ärztliche Atteste
- Berufs-Beschreibung

### Phase 3 — Prüfung Versicherer

- Aktenkundige Vorerkrankungen
- Gutachter-Einsatz
- Entscheidung

### Phase 4 — Bei Ablehnung

- Schriftliche Begründung verlangen
- Eigenes Gutachten
- Klage AG / LG je Streitwert

### Phase 5 — Klage

- Streitwert: jaehrliche Rente × Vermutungs-Dauer (oft 5-10 Jahre)
- Sachverständigen-Beweis
- Beweisaufnahme

## 5) Sachverständigen-Strategie

### Eigener SV

- Privatgutachten
- Vorbereitung Mandant

### Gerichtlicher SV

- Vom Gericht bestellt
- Beide Seiten konnen Fragen stellen
- Erfaehrung-Massstab

### Beweis-Niveau

- 50 %-Schwelle muss klar dargelegt sein
- Funktional-Defizite

## 6) Anzeige-Pflicht-Verletzung

### Folgen § 19 VVG

- Bei grober Fahrlaessigkeit: Vertrags-Änderung
- Bei Vorsatz: Aufhebung
- Bei einfachem Verstoß: ggf. nur Pruemien-Anpassung

### Prüfung

- Welche Frage falsch beantwortet?
- Welche Vorerkrankung verschwiegen?
- Kausalitaet mit aktueller BU

## 7) Vergleichs-Verhandlung

### Standard-Ergebnisse

- Einmal-Zahlung statt Renten-Auszahlung (40-60 % Renten-Barwert)
- Anpassung Rente-Höhe
- Befristete Rente mit Nachprüfung

### Vorteile

- Schneller
- Planungs-Sicherheit
- Kein Klage-Risiko

## 8) Aktualität — BGH-Linien (Stand Mai 2026)

Verifizierte Aktenzeichen mit offener Quelle (vor Versand jeweils Volltext aufrufen):

- BGH IV ZR 153/20, Urt. v. 14.7.2021 — Versicherungsfall BU: Eintritt erst nach Ablauf des sechs-monatigen Prognosezeitraums. Quelle: juris.bundesgerichtshof.de
- BGH IV ZR 19/18, Urt. v. 26.6.2019 — Vergleichsverweisung; tatsächlich erzieltes Einkommen ist nicht ohne Weiteres auf Vergleichszeitpunkt fortzuschreiben. Quelle: juris.bundesgerichtshof.de
- BGH IV ZR 32/24, Urt. v. 12.3.2025 — Krankentagegeldversicherung: einseitige Tagessatz-Herabsetzung durch Klauselersetzung nach § 164 Abs. 1 VVG unzulässig; Bedeutung auch für Bedingungswechsel in BU/PKV-Klauselgestaltung. Pressemitteilung Nr. 47/25 vom 12.3.2025. Quelle: bundesgerichtshof.de Pressemitteilungen
- BGH IV ZR 70/25, 2025 — PKV-Beitragsanpassung: Begründung der Beitragsanpassung muss konkrete Rechnungsgrundlage benennen; sonst Rückforderung. Quelle: juris.bundesgerichtshof.de (Volltext vor Versand verifizieren)
- BGH IV ZR 86/24, Urt. v. 15.10.2025 — PKV-Beitragsanpassung; Prüfungsmaßstab. Quelle: bundesgerichtshof.de (Volltext-Verifikation Pflicht)

## 9) Honorar

- Beratung 500-1.500 EUR pauschal
- Klage nach Streitwert
- Erfolgs-Vereinbarung bei Beratung möglich

## 10) Typische Fehler

1. **Anzeige-Pflichten unvollständig** bei Antragstellung
2. **Privatgutachten ohne BU-Spezialisten**
3. **Verweisung-Klausel nicht angefochten**
4. **Verjaehrung 3 Jahre** versäumt

## Anschluss

- `fachanwalt-versicherungsrecht-lebensversicherung-rueckkauf` — bei LV
- `fachanwalt-versicherungsrecht-do-deckungsabwehr` — bei D&O
- `fachanwalt-sozialrecht-krankengeld-aussteuerung` — bei KG-Bezug

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate (Stand Mai 2026)

Verifizierte Aktenzeichen mit Anker zu offener Quelle. Volltext vor Versand erneut aufrufen und Randnummer einsetzen:

1. **Versicherungsfall BU**: BGH, Urt. v. 14.7.2021, IV ZR 153/20 — Eintritt des Versicherungsfalls erst nach Ablauf der bedingungsgemäßen Prognosezeit (sechs Monate). Offene Quelle: juris.bundesgerichtshof.de
2. **Vergleichstätigkeit / Verweisung**: BGH, Urt. v. 26.6.2019, IV ZR 19/18 — Tatsächlich erzieltes Einkommen aus Verweisungstätigkeit nicht ohne weiteres auf Vergleichszeitpunkt fortzuschreiben. Quelle: juris.bundesgerichtshof.de
3. **AVB-Auslegung Maßstab**: st. Rspr. BGH IV. ZS — Auslegung aus Sicht eines durchschnittlichen, verständigen Versicherungsnehmers ohne versicherungsrechtliche Spezialkenntnisse. Konkrete Entscheidung mit Aktenzeichen vor Versand in offener Quelle verifizieren.
4. **Klauselersetzung nach Intransparenz**: BGH, Urt. v. 12.3.2025, IV ZR 32/24 — Nach Unwirksamkeit einer Bedingung darf der Versicherer keine im Kern identische neue Bedingung einseitig einführen (zur Krankentagegeldversicherung; übertragbar). Pressemitteilung Nr. 47/25 vom 12.3.2025.

### Paragrafenkette

§§ 172 ff. VVG (BU-Versicherung) → § 19 VVG (Anzeigepflicht) → § 28 VVG (Obliegenheitsverletzung) → § 81 VVG (vorsätzliche/grob fahrlässige Herbeiführung) → § 286 ZPO (freie Beweiswürdigung Gutachten) → § 287 ZPO (Schadensschätzung) → § 402 ZPO (Sachverständiger) → § 195 BGB (Verjährung 3 Jahre) → § 203 BGB (Hemmung durch Verhandlungen) → § 256 ZPO (Feststellungsklage bei laufender Rente)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
### Fristen-Übersicht

| Situation | Frist | Norm |
|---|---|---|
| BU-Leistungsantrag beim Versicherer | laut AVB (typisch unverzüglich) | § 28 VVG, AVB |
| Verjährung BU-Rentenanspruch | 3 Jahre ab Fälligkeit/Kenntnis | § 195, 199 BGB |
| Hemmung durch Verhandlungen | läuft bis Abbrucherklärung | § 203 BGB |
| Feststellungsklage (laufende Rente) | kein strikter Ablauf | § 256 ZPO |
| Nachprüfungsverfahren (Verbesserung) | laut AVB | AVB-BU |

## Triage — Sofortprüfung BU-Mandat

1. **Vollständige Berufsbeschreibung sichern:** Was genau tat der Mandant in den letzten 6 Monaten vor BU-Eintritt? (Tätigkeitsauflistung, Prozentzeitenverteilung).
2. **50-%-Schwelle dokumentieren:** Ärztliche Gutachten zu verbliebener Leistungsfähigkeit; Privatgutachten beauftragen.
3. **Verweisung des Versicherers prüfen:** Konkret oder abstrakt? Übt Mandant die Verweisungstätigkeit tatsächlich aus?
4. **Anzeigepflichtverletzungseinwand prüfen:** Welche Frage wurde falsch beantwortet? Belehrung nach § 19 Abs. 5 VVG erfolgt? Kausalität zwischen Vorerkrankung und eingetretener BU?
5. **Rückwirkende Rente berechnen:** Rente ab Eintritt BU × Monate zurück = Hauptforderung; dazu Verzugszinsen.

**Entscheidungsbaum:**
```
Ablehnung Versicherer?
├─ Verweisung → konkret oder abstrakt?
│   └─ Abstrakt → unzulässig nach st. Rspr. BGH IV. ZS
│       (konkrete Entscheidung in juris.bundesgerichtshof.de
│        verifizieren und Randnummer einsetzen)
│   └─ Konkret → übt Mandant Verweisungstätigkeit tatsächlich aus?
├─ Bestreiten BU-Grad → 50-%-Schwelle ärztlich belegen
│   └─ Privatgutachten + gerichtliches Gutachten beantragen
├─ Anzeigepflichtverletzung → Belehrung erfolgt nach § 19 Abs. 5 VVG?
│   └─ Nein → Rücktritt / Anfechtung des Versicherers unwirksam
│   └─ Ja → Kausalität zwischen Vorerkrankung und BU?
└─ Verjährung → Verhandlungen dokumentieren (§ 203 BGB Hemmung)
```
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Klage gegen BU-Versicherer wegen Leistungsablehnung | BU-Klageschrift nach Pruefschema; Template unten |
| Variante A — Erstantrag noch nicht vollstaendig gestellt | Nachbeibringung Unterlagen zuerst; Klage danach |
| Variante B — Vergleich wirtschaftlich attraktiver als Prozess | Vergleichsverhandlung vor Klageerhebung; Klage als Druckmittel |
| Variante C — BU nur voruebergehend Reaktivierung moeglich | Teilleistung akzeptieren und beobachten statt Vollklage |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Output-Template — Klageschrift BU-Versicherung (Skizze)

```
[MANDANT] (Kläger) gegen [VERSICHERER] (Beklagte)
Az.: [AZ LG]

ANTRÄGE
1. Die Beklagte wird verurteilt, an den Kläger rückständige BU-Rente
   für den Zeitraum [MONAT/JAHR] bis [MONAT/JAHR] von EUR [BETRAG]
   nebst Zinsen 5 Prozentpunkte über Basiszins seit [DATUM] zu zahlen.
2. Es wird festgestellt, dass die Beklagte verpflichtet ist, dem Kläger
   ab [DATUM] eine monatliche BU-Rente von EUR [MONATSBETRAG] zu zahlen
   und die Prämien zu erlassen (§ __ AVB), solange Berufsunfähigkeit
   im Sinne der AVB vorliegt.

BEGRÜNDUNG
1. BU-Definition (§ __ AVB): Kläger übte zuletzt die Tätigkeit
   [BERUFSBEZEICHNUNG konkret] aus. Tätigkeitsprofil: [Liste mit %].
2. 50-%-Schwelle: Laut Privatgutachten Dr. [NAME] vom [DATUM]
   (Anlage K3) ist Kläger zu [X]% beeinträchtigt.
3. Verweisung verfehlt: Versicherer verweist auf [Beruf] — nicht
   konkret ausgeübt vom Kläger; abstrakte Verweisung nach st. Rspr.
   des BGH IV. ZS unzulässig (konkrete Entscheidung mit Aktenzeichen
   und Datum vor Versand in juris.bundesgerichtshof.de oder
   dejure.org verifizieren und Randnummer einfügen).
4. Anzeigepflicht: Keine Belehrung § 19 Abs. 5 VVG (Anlage K5);
   Rücktrittsrecht des Versicherers ausgeschlossen.
5. Verjährung: Durch Verhandlungen bis [DATUM] gehemmt (§ 203 BGB).

Beweis: K1 Police + AVB, K2 Tätigkeitsbeschreibung, K3 Privatgutachten,
        K4 Ablehnungsschreiben, K5 Antragsformular, K6 Vollmacht
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `fachanwalt-versicherungsrecht-leistungsablehnung-pruefen`

_Ablehnung des Versicherers prüfen nach §§ 1 28 VVG Obliegenheitsverletzung und Risikoausschluss. Anwendungsfall Versicherung hat Schadensantrag abgelehnt und Mandant fragt nach Erfolgsaussichten. Normen § 28 VVG Obliegenheitsverletzung § 19 VVG Anzeigepflichtverletzung § 81 VVG grob fahrlässig § 307 BGB AGB-Kontrolle § 195 BGB Verjährung. Prüfraster Obliegenheitsverletzung Vorsatz grobe Fahrlässigkeit Kausalität Risikoausschluss AVB-Auslegung Verjährung Hemmung. Output Prüfvermerk mit Ablehnungsbegründung Widerspruchspotenzial und Klageschrift-Empfehlung. Abgrenzung zu deckungsanfrage-prüfen und fachanwalt-versicherungsrecht-deckungsklage._

# Leistungsablehnung prüfen

## Kaltstart-Rückfragen

1. Welche Versicherungssparte — Lebens-, Berufsunfähigkeits-, Unfall-, Wohngebäude-, Hausrat-, Haftpflicht-, Kasko-, Rechtsschutz-, Krankenversicherung?
2. Wann trat der Versicherungsfall ein und wann erfolgte Meldung beim Versicherer? Fristen nach AVB?
3. Welche Begründung hat der Versicherer für die Ablehnung — Obliegenheitsverletzung (§ 28 VVG), Risikoausschluss, Anzeigepflichtverletzung (§ 19 VVG), fehlender Versicherungsfall, vorsätzliche Herbeiführung (§ 81 VVG)?
4. Welche Mitteilungs- und Mitwirkungspflichten wurden angeblich verletzt und in welchem Verschuldensgrad?
5. Liegt der vollständige Vertrag mit allen AVB, Antragsformularen und Schadensanzeigen vor?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Anspruchsgrundlagen

- Hauptleistungsanspruch § 1 Satz 1 VVG i. V. m. dem konkreten Versicherungsvertrag.
- Beweislast Versicherungsfall trägt grundsätzlich der Versicherungsnehmer (§ 1 VVG); für Risikoausschluss trägt Versicherer Beweislast.
- Obliegenheitsverletzung § 28 VVG: bei Vorsatz Leistungsfreiheit, bei grober Fahrlässigkeit Kürzung in der Schwere des Verschuldens entsprechend, bei einfacher Fahrlässigkeit keine Folgen.
- Kausalitätserfordernis § 28 Abs. 3 VVG: Versicherer ist nur leistungsfrei wenn die Obliegenheitsverletzung kausal für Eintritt, Feststellung oder Umfang des Versicherungsfalls war — sonst keine Leistungsfreiheit (sog. Kausalitätsgegenbeweis).
- AVB-Auslegung: aus Sicht eines durchschnittlichen, verständigen Versicherungsnehmers ohne versicherungsrechtliche Spezialkenntnisse (st. Rspr. BGH IV. ZS; konkrete Entscheidung mit Aktenzeichen vor Versand in offener Quelle verifizieren).
- Vorsätzliche Herbeiführung § 81 Abs. 1 VVG Leistungsfreiheit; grob fahrlässig § 81 Abs. 2 VVG Kürzung.
- AVB-Auslegung nach §§ 305c, 307 BGB: Klauseln gegen den Verwender bei Mehrdeutigkeit (§ 305c Abs. 2 BGB); Inhaltskontrolle § 307 BGB unangemessene Benachteiligung.
- Verjährung Versicherungsleistung drei Jahre § 195 BGB ab Schluss des Jahres der Fälligkeit und Kenntnis (§ 199 BGB); Hemmung durch Verhandlungen § 203 BGB.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Beweislast und Aufklärung

| Frage | Beweislast |
|---|---|
| Versicherungsfall liegt vor | Versicherungsnehmer |
| Risikoausschluss greift | Versicherer |
| Obliegenheitsverletzung | Versicherer Tatsache und Verschulden |
| Kausalitätsausschluss § 28 Abs. 3 VVG | Versicherungsnehmer |
| Anzeigepflichtverletzung § 19 VVG | Versicherer Frage + Antwort + Verschulden |
| Belehrung § 19 Abs. 5 VVG erfolgt | Versicherer |
| Vorsätzliche Herbeiführung § 81 VVG | Versicherer |

## Prüfschema Ablehnungsschreiben


**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

1. Anspruchsgrundlage benannt
2. Tatsachen für Tatbestandsmerkmal richtig dargestellt
3. AVB-Klausel zitiert mit Quelle (Bedingungswerk Version)
4. Klauselkontrolle § 305c § 307 BGB
5. Kausalitätsfrage geprüft
6. Belehrung dokumentiert (§ 19 Abs. 5, § 28 Abs. 4 VVG)
7. Verjährungseinrede formal richtig
8. Stufung des Verschuldens (Vorsatz, grobe oder einfache Fahrlässigkeit)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Widerspruch gegen Leistungsablehnung | Widerspruchsschreiben nach Pruefschema; Template unten |
| Variante A — Ablehnung formell begruendet Unterlagen fehlen | Unterlagen nachreichen; kein Widerspruch noetig |
| Variante B — Ablehnung materiell Rechtsfrage streitig | Widerspruch mit Rechtsgutachten; ggf. Klage vorbereiten |
| Variante C — Versicherungsombudsmann als guenstigere Alternative | Ombudsmann-Beschwerde statt Widerspruch bei kleinen Betraegen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schreibvorlage Widerspruch gegen Ablehnung

```
An die [Versicherung]
Schadensnummer [Nr]

Sehr geehrte Damen und Herren,

namens und in Vollmacht des Versicherungsnehmers [Name] widersprechen
wir Ihrem Ablehnungsschreiben vom [Datum] und fordern erneut zur
Regulierung auf binnen vier Wochen.

I. Sachverhalt
[chronologische Darstellung des Versicherungsfalls]

II. Anspruch dem Grunde nach
Der Anspruch beruht auf § 1 VVG i.V.m. § __ AVB. Der Versicherungsfall
liegt vor weil [Begruendung].

III. Zur Ablehnungsbegruendung
1. Eine Obliegenheitsverletzung § 28 VVG liegt nicht vor weil
   [Begruendung]. Hilfsweise ist die behauptete Verletzung jedenfalls
   nicht kausal § 28 Abs. 3 VVG fuer Eintritt Feststellung oder
   Umfang des Versicherungsfalls.
2. Eine Anzeigepflichtverletzung § 19 VVG scheitert bereits an der
   fehlenden Belehrung nach § 19 Abs. 5 VVG bzw. ist nicht
   verschuldet.
3. Der zitierte Risikoausschluss in § __ AVB ist intransparent
   § 307 Abs. 1 Satz 2 BGB und benachteiligt den VN unangemessen.

IV. Anspruchshoehe
Die Versicherungsleistung betraegt EUR ____ nach [Berechnungsschema].

V. Frist
Bis zum [Datum + 4 Wochen]. Andernfalls Klageerhebung. Verzugszinsen
5 Prozentpunkte ueber Basiszinssatz § 288 BGB.

Mit kollegialen Gruessen
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen fuer ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.


## Übergabe

- Bei Verhandlungsbereitschaft Verjährungs-Hemmung § 203 BGB dokumentieren.
- Bei BU-Versicherung Sachverständigengutachten zur Berufsunfähigkeit beifügen — Vergleich zwischen zuletzt ausgeübter Tätigkeit und verbliebener Leistungsfähigkeit.
- Bei Kasko Unfallrekonstruktion und Wertgutachten.
- Anschluss: Skill `fachanwalt-versicherungsrecht-deckungsklage` bei Fortbestehen der Ablehnung.

## Vertiefung — Aktuelle Rechtsprechung und Normen

### Leitsatz-Zitate (Stand Mai 2026; offene Quellen)

Vor Versand jeweils Volltext und Randnummer aus offener Quelle ergänzen (juris.bundesgerichtshof.de, dejure.org, openjur.de):

1. **AVB-Auslegung**: BGH IV. ZS, st. Rspr. — Auslegung aus Sicht eines durchschnittlichen, verständigen Versicherungsnehmers ohne versicherungsrechtliche Spezialkenntnisse.
2. **Klauselersetzung nach Intransparenz**: BGH, Urt. v. 12.3.2025, IV ZR 32/24 — Nach Unwirksamkeit einer Bedingung (Tagessatz-Herabsetzung Krankentagegeld) darf der Versicherer keine im Kern identische neue Bedingung einseitig einführen. Pressemitteilung Nr. 47/25 vom 12.3.2025.
3. **PKV-Beitragsanpassung Mitteilungspflicht**: BGH, IV ZR 70/25, 2025 — Mitteilungsschreiben muss konkrete Rechnungsgrundlage (Versicherungsleistungen oder Sterbewahrscheinlichkeiten) benennen, deren Veränderung die Anpassung auslöst (§ 203 Abs. 5 VVG); Live-Verifikation in juris.bundesgerichtshof.de Pflicht.
4. **GDSGVO-Schadensersatz**: BGH, Urt. v. 28.1.2025, VI ZR 183/22 — Art. 82 Abs. 1 DSGVO hat nur Ausgleichs-, keine Straffunktion (unberechtigte SCHUFA-Meldung; 500 EUR immaterieller Schadensersatz). Quelle: juris.bundesgerichtshof.de

### Normen-Ergänzung

§ 28 Abs. 3 VVG (Kausalitätsgegenbeweis) → § 19 Abs. 5 VVG (Belehrungspflicht Versicherer) → § 305c Abs. 2 BGB (unklare AGB gegen Verwender) → § 307 BGB (AGB-Inhaltskontrolle) → § 203 BGB (Hemmung Verjährung durch Verhandlungen)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

