# Megaprompt: fachanwalt-familienrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 154 Skills (gekuerzt fuer Chat-Fenster) des Plugins `fachanwalt-familienrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Anwalts-Dashboard Fachanwalt Familienrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, …
2. **mandat-triage-familienrecht** — Eingangs-Triage für familienrechtliche Mandate: Routing zu Scheidung, Sorge, Umgang, Unterhalt, Zugewinn oder Versorgung…
3. **fachanwalt-familienrecht-orientierung** — Orientierung im Fachanwaltsrecht Familienrecht: FAO-Voraussetzungen, Kerngebiete, Verfahren nach FamFG und BGB ueberblic…
4. **orientierung-fristen-form-und-zustaendigkeit** — Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg im Familienrecht: fachlich vertieftes Modul mit Normenradar (BG…
5. **orientierung-mandat-fachanwaltschaft** — Orientierung im Fachanwaltsrecht Familienrecht: FAO-Voraussetzungen, Kerngebiete, Verfahren nach FamFG und BGB überblick…
6. **erstgespraech-mandatsannahme** — Strukturierter Erstgespraechsleitfaden für Familien-, Kindschafts- und Versorgungsausgleichsrecht: Erfassung der Konstel…
7. **erstpruefung-und-mandatsziel** — Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/…
8. **fachanwalt-familienrecht-zugewinnausgleich-berechnen** — Zugewinnausgleich nach §§ 1372-1390 BGB berechnen: Trennung oder Scheidung erfordert Aufstellung von Anfangs- und Endver…

---

## Skill: `einstieg-routing`

_Anwalts-Dashboard Fachanwalt Familienrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt bleibt im Driver Seat._

# Anwalts-Dashboard Fachanwalt Familienrecht

> Trennung, Unterhalt, Versorgungsausgleich, Sorge- und Umgangsrecht — meist Verbundverfahren, meist im Hintergrund das Kindeswohl.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | Keine 3-Wochen-Frist wie im ArbR, aber: § 1565 II BGB (Härtefall-Scheidung vor Trennungsjahr), §§ 1666, 1666a BGB i. V. m. § 49 FamFG (Kindeswohlgefährdung — sofort), § 36 GewSchG (Gewaltschutz — sofortige Wirksamkeit). | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Scheidung §§ 1564 ff. BGB · Trennungsunterhalt § 1361 BGB · Nachehelicher Unterhalt §§ 1569 ff. BGB · Kindesunterhalt §§ 1601 ff. BGB · Zugewinn §§ 1372 ff. BGB · Versorgungsausgleich §§ 1, 9 VersAusglG · Sorge §§ 1671, 1684 BGB · Umgang § 1684 BGB. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Familiengericht (Abt. AG) am Aufenthalt des Kindes oder gemeinsamen Wohnsitzes (§§ 122, 152, 232 FamFG). Anwaltszwang in Ehesachen (§ 114 FamFG). | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Kindeswohlgefährdung: sofort Eilantrag (§ 49 FamFG). 🔴 Häusliche Gewalt: Schutzanordnung § 1 GewSchG. 🟠 Trennungsjahr: Datum dokumentieren (Beweis!).
- **Beweislage:** 🟠 Trennungszeitpunkt — Indizien (Kontotrennung, Schlafzimmer, schriftliche Erklärung). 🔴 Sorgekonflikt: Beweismittel sorgsam (kein Aufschaukeln, Verfahrensbeistand respektieren).
- **Wirtschaftlich:** 🟠 Hohes Vermögen: Zugewinn parallel zur Scheidung (Verbund). 🔴 Drohende Verschiebung von Vermögen: § 1379 BGB Auskunft + § 1390 BGB Anfechtung.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Trennung — Trennungsjahr / Folgen** | `famr-trennungsjahr-praxis` | Trennungszeitpunkt dokumentieren, Trennungsunterhalt vorbereiten |
| Kindesunterhalt zu prüfen | `kindesunterhalt-mindestsatz-paragraf-1612a-bgb` | Mindestunterhalt, Düsseldorfer Tabelle, Mangelfall-Berechnung |
| Versorgungsausgleich offen | `famr-versorgungsausgleich-spezial` | Auskunftsverfahren VAB-Fragebogen, Halbteilung, Ausschluss |
| Gewaltschutz / Umgang in Konflikt | `gewaltschutz-und-umgang-schnittstelle` | GewSchG-Anordnung, Schnittstelle Umgang § 1684 BGB |
| Kindeswohlgefährdung — Eilantrag | `famr-kindeswohlgefaehrdung-eilantrag-spezial` | Eilantrag § 1666 BGB, Verfahrensbeistand, Jugendamt |

## Norm-Radar (live verifizieren)

- **§ 1565 BGB** — Scheidungsvoraussetzung, Trennungsjahr
- **§ 1361 BGB** — Trennungsunterhalt
- **§ 1612a BGB** — Mindestkindesunterhalt
- **§ 1666 BGB** — Maßnahmen bei Kindeswohlgefährdung
- **§ 1684 BGB** — Umgangsrecht / Umgangspflicht
- **§ 1 VersAusglG** — Halbteilungsgrundsatz

## Genau eine Rückfrage (nur wenn nötig)

> Geht es vorrangig um **Trennungs-/Scheidungsfolgen (Unterhalt, Zugewinn, VA)** oder um eine **akute Kindes- bzw. Gewaltschutz-Sache** (dann sofortiger Eilantrag)?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Ehevertrag; Kernbereichslehre, Wirksamkeitskontrolle** — BGH XII. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Wechselmodell; Anordnungsfähigkeit durch Familiengericht** — BGH XII. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Kindeswohlgefährdung § 1666 BGB; Eingriffsschwelle** — BVerfG 1. Senat — *live verifizieren auf* `bundesverfassungsgericht.de`
- **Düsseldorfer Tabelle (Unterhalt; jährliche Aktualisierung)** — OLG Düsseldorf — *live verifizieren auf* `olg-duesseldorf.nrw.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

---

## Skill: `mandat-triage-familienrecht`

_Eingangs-Triage für familienrechtliche Mandate: Routing zu Scheidung, Sorge, Umgang, Unterhalt, Zugewinn oder Versorgungsausgleich: Eingangs-Triage für familienrechtliche Mandate: Routing zu Scheidung, Sorge, Umgang, Unterhalt, Zugewinn oder Versorgungsausg..._

# Eingangs-Triage für familienrechtliche Mandate: Routing zu Scheidung, Sorge, Umgang, Unterhalt, Zugewinn oder Versorgungsausgleich


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: FamFG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Eingangs-Triage für familienrechtliche Mandate: Routing zu Scheidung, Sorge, Umgang, Unterhalt, Zugewinn oder Versorgungsausgleich. Normen: § 63 FamFG (Beschwerde 1 Monat), § 1600b BGB (Vaterschaftsanfechtung 2 Jahre), § 1666 BGB (Kindeswohlgefaehrdung Eilantrag). Prüfraster: Konflikt-Check, Eilbedürftigkeit (Gewaltschutz, Sorge-Eilantrag), Streitwert, Komplexitaet. Output Triage-Protokoll, Fristen-Ampel, Folge-Skill-Empfehlung. Abgrenzung: Detailberechnung siehe Fachmodule; Schriftsatzkern siehe schriftsatzkern-substantiierung.

### Mandat-Triage Familienrecht

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandat-Triage Familienrecht` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Mandat-Triage Familienrecht
- **Normen-/Quellenanker:** BGB Familienrecht, FamFG, VersAusglG, Unterhaltsrecht, Zugewinn, Gewaltschutz, Kindschaft, internationale Verordnungen und Vollstreckung.
- **Entscheidende Weiche:** Beteiligte, Kind/Unterhalt/Vermögen/Versorgung, Frist, Auskunft, Beleg, Eilbedarf und familiengerichtliche Verfahrensart trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Aktuelle Rechtsprechung (Triage-Orientierung, Stand 05/2026)

Verifizierte Eckpfeiler — Live-Verifikation vor Verwendung in Schriftsätzen zwingend:

- BGH 22.01.2025 - XII ZB 148/24 (Elternunterhalt, Selbstbehalt; Familienselbstbehalt)
- BVerfG 07.10.2025 - 1 BvR 746/23 (Umgangsausschluss: Begründungsanforderungen bei längerer Dauer)
- BVerfG 28.08.2025 - 1 BvR 1473/25 (Sorgerecht im einstweiligen Anordnungsverfahren; PAS-Maßstäbe)
- Düsseldorfer Tabelle 2026 (in Kraft seit 01.01.2026)

Weitere Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe über bundesgerichtshof.de, bundesverfassungsgericht.de, dejure.org oder openjur.de mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ablauf — sieben Fragen in fester Reihenfolge

### Frage 1 — Wer ruft an und für wen?

- Selbst Betroffener
- Eltern eines Kindes
- Anderer Anwalt (Verweisungsmandat)
- Gericht (Verfahrensbeistand)

**Routing:** Bei Verweisungsmandat sofort an aufnehmenden Anwalt. Bei Verfahrensbeistand separater Vermerk.

### Frage 2 — Akute Eilbedürftigkeit?

- Häusliche Gewalt — Schutzanordnung gewünscht
- Kindeswohl unmittelbar gefährdet
- Kind drohend ins Ausland verbracht (HKÜ-Fall)
- Wegweisung dringend
- Sorgerecht-Eilbedürftigkeit

**Eskalation:** Bei JA — Telefon-Sofort an Anwalt; binnen ein Stunde Eilantrag-Vorbereitung. Skill `mandat-triage-familienrecht` wechselt sofort in Eilmodus.

### Frage 3 — Hauptanliegen?

- Scheidung
- Sorgerecht
- Umgangsrecht
- Kindesunterhalt
- Ehegattenunterhalt
- Zugewinnausgleich
- Versorgungsausgleich
- Vaterschaft (Anerkennung Anfechtung)
- Ehevertrag Scheidungsfolgenvereinbarung
- Adoption
- Betreuung Vorsorgevollmacht

### Frage 4 — Stand des Verfahrens?

- Außergerichtlich keine Anzeige
- Schreiben des Gegners liegt vor
- Gerichtliches Verfahren läuft (Aktenzeichen Gericht)
- Erstinstanz abgeschlossen — Beschwerde erwogen

### Frage 5 — Familienstatus?

- Verheiratet
- Getrennt lebend (Datum der Trennung)
- Geschieden
- Lebenspartnerschaft
- Nichtehelich

### Frage 6 — Wirtschaftliche Verhältnisse?

- Nettoeinkommen beide Eheleute geschätzt
- Vermögen geschätzt (Immobilie Sparvermögen Unternehmensbeteiligungen)
- Streitwert-Schätzung

**Routing PKH:** Bei knappem Einkommen Hinweis auf Prozesskostenhilfe-Antrag. Sozialrechtliche Bedürftigkeits- und Leistungsfragen bei Bedarf an `fachanwalt-sozialrecht` routen; PKH-Antrag sonst als eigener Entwurf.

### Frage 7 — Fristen?

- Letztes Anwaltsschreiben oder Beschluss empfangen am ?
- Beschwerdefrist § 63 FamFG ein Monat
- Vaterschaftsanfechtung § 1600b BGB zwei Jahre ab Kenntnis

## Routing-Matrix

| Hauptanliegen | Folge-Skill | Frist-Sofort-Check |
|---|---|---|
| Scheidung | (Skill scheidungsverbund-vorbereiten — perspektivisch) | Versorgungsausgleichs-Auskunft anfordern |
| Kindesunterhalt | `unterhalt-duesseldorfer-tabelle` | Verzug § 1613 BGB durch Auskunftsschreiben |
| Ehegattenunterhalt | `unterhalt-duesseldorfer-tabelle` | Verzug § 1613 BGB |
| Sorge / Umgang | (Skill kindeswohl-prüfung — perspektivisch) | Eilantrag prüfen |
| Zugewinn | (Skill zugewinnausgleich-berechnen — perspektivisch) | Stichtag Zustellung Scheidungsantrag |
| Versorgungsausgleich | (Skill versorgungsausgleich — perspektivisch) | Auskunft DRV / Versorgungsträger |
| Vaterschaft | (Skill vaterschafts-verfahren — perspektivisch) | § 1600b BGB Zwei-Jahres-Frist |
| Gewaltschutz | EILMODUS — Antrag GewSchG Skill `mandat-triage-familienrecht` wechselt | sofort |

## Mandatsannahme-Kriterien

- **Konflikt-Check** — keine Beratung des Gegners im selben Sachverhalt (§ 43a Abs. 4 BRAO)
- **Streitwert** über EUR 30000 OLG Familiensenat erste Instanz bei Verbund
- **Komplexität** bei Auslandsbezug Selbstständigen-Einkommen Unternehmens-Beteiligungen Gesellschafter-Streit

## Sofort-Fristen-Check

- Empfangsdatum letzter Beschluss notieren
- Bei Beschluss eingegangen heute: Beschwerdefrist nach FamFG (§§ 63, 64 FamFG i.V.m. ZPO) — Zugang nach Vier-Tages-Fiktion (§ 270 ZPO n.F., seit 1.1.2025 PostModG; bis 31.12.2024 drei Tage), danach Lauf der Beschwerdefrist von einem Monat (§ 63 FamFG)
- Eintrag in `fristenbuch.yaml` (Skill `kanzlei-allgemein`)

## Eskalationspfad

- **Telefon-Sofort** Gewaltschutz Kindeswohlgefährdung HKÜ-Verbringung
- **Binnen einer Stunde** Eilantrag-Sorgerecht Wegweisung
- **Heute** Versorgungsausgleichs-Auskunft Verzug-Schreiben
- **Diese Woche** Schriftsatz-Erstentwurf Verbund-Antrag

## Ausgabe

- `triage-protokoll-familienrecht.md` strukturiert nach den sieben Fragen
- Aktenanlage mit Az-Vorschlag
- Frist-Eintrag im Fristenbuch
- Empfehlung Folge-Skill plus zwei Sätze Begründung
- Mandantenbrief-Entwurf mit Sachstand und nächsten Schritten

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen

- §§ 111 ff. FamFG (Familiensachen)
- BGH XII. Zivilsenat
- Wendl/Dose
- Schwab Familienrecht

---

## Skill: `fachanwalt-familienrecht-orientierung`

_Orientierung im Fachanwaltsrecht Familienrecht: FAO-Voraussetzungen, Kerngebiete, Verfahren nach FamFG und BGB ueberblicken. Normen: FamFG (Beschluss statt Urteil, Verbund § 137 FamFG), §§ 23a und 23b GVG (Familiengericht), BGB Familienrecht. Prüfraster: Sachgebiet (Scheidung, Sorge, Umgang, Unterhalt, Zugewinn, VA), Verfahrenstypen, Eilbedürftigkeit. Output Orientierungs-Memo, Routing zu Spezialskills. Abgrenzung: Mandats-Triage siehe mandat-triage-familienrecht; Detailbearbeitungen siehe Spezialskills._

# Fachanwalt für Familienrecht — Orientierung

## Aktuelle Rechtsprechung (Orientierung Familienrecht, Stand 05/2026)

Verifizierte Eckpfeiler — Live-Verifikation vor Verwendung in Schriftsätzen zwingend:

- BGH, Beschluss vom 22.01.2025 - XII ZB 148/24 (Elternunterhalt; Selbstbehalt verheirateter Unterhaltspflichtiger)
- BVerfG, Beschluss vom 07.10.2025 - 1 BvR 746/23 (Begründungsanforderungen bei mehrjährigem Umgangsausschluss)
- BVerfG, Beschluss vom 28.08.2025 - 1 BvR 1473/25 (Sorgerecht im einstweiligen Anordnungsverfahren; PAS)
- BVerfG, Beschluss vom 09.04.2025 - 1 BvR 1618/24 (internationale Zuständigkeit nach KSÜ, Sorgerechtswirkungen)
- Düsseldorfer Tabelle 2026 (in Kraft seit 01.01.2026, OLG Düsseldorf, Pressemitteilung 01.12.2025; Mindestunterhalt nach 7. MUVÄndV vom 15.11.2024, BGBl. 2024 I Nr. 359)

Weitere Entscheidungen nicht aus Modellwissen zitieren; vor Ausgabe über bundesgerichtshof.de, bundesverfassungsgericht.de, dejure.org, openjur.de verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## FAO-Voraussetzungen (§ 5 Abs. 1 FAO)

- **Theoretischer Lehrgang** 120 Stunden (§ 4 FAO).
- **Drei Klausuren** zum Familienrecht (§ 4a FAO).
- **120 Fälle** in den letzten drei Jahren vor Antrag, davon mindestens 60 streitige Fälle (§ 5 FAO).
- **Anmeldung** bei der Rechtsanwaltskammer.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| BGB Familienrecht | §§ 1297 ff. BGB (Ehe Scheidung) §§ 1601 ff. BGB (Unterhalt) §§ 1626 ff. BGB (Elterliche Sorge) §§ 1684 ff. BGB (Umgangsrecht) §§ 1740 ff. BGB (Adoption) §§ 1773 ff. BGB (Vormundschaft) |
| Verfahrensrecht | FamFG §§ 111 ff. (Familiensachen) § 137 FamFG (Scheidungsverbund) §§ 151 ff. FamFG (Kindschaftssachen) |
| Versorgungsausgleich | VersAusglG |
| Lebenspartnerschaft | LPartG |
| Gerichtsverfassung | § 23a GVG (Familiengericht beim AG) § 23b GVG |
| EU- und Völkerrecht | Brüssel IIb-VO (EU) 2019/1111 |

## Typische Mandate

- Scheidung im Verbund (Scheidung + Versorgungsausgleich + Folgesachen)
- Sorgerechtsverfahren bei getrennt lebenden Eltern
- Umgangsrechtsstreit
- Kindesunterhalt nach Düsseldorfer Tabelle
- Ehegattenunterhalt (Trennungs- und nachehelicher Unterhalt)
- Zugewinnausgleich
- Ehevertrag und Scheidungsfolgenvereinbarung
- Gewaltschutz nach GewSchG

## Wichtige Fristen

- **Beschwerde** § 63 FamFG — ein Monat.
- **Sofortige Beschwerde** § 64 FamFG — zwei Wochen.
- **Wiedereinsetzung** § 17 FamFG.
- **Versorgungsausgleichs-Anträge** parallel zum Scheidungsverfahren.
- **Anfechtungsfristen** Vaterschaft § 1600b BGB — zwei Jahre ab Kenntnis.

## Hauptgericht

- **Familiengericht** beim Amtsgericht (§ 23a Abs. 1 Nr. 1 GVG).
- **OLG-Familiensenat** als Beschwerdegericht (§ 119 GVG).
- **BGH XII. Zivilsenat** in Familiensachen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- Deutscher Anwaltverein DAV Arbeitsgemeinschaft Familienrecht.
- Deutsche Gesellschaft für Familienrecht.

## Schnittstellen zu anderen Plugins

- **kanzlei-allgemein** für Fristenbuch Timesheet Versand-Vor-Check.
- **methodenlehre-buergerliches-recht** und **zitierweise-deutsches-recht** als Hausstandards.

## Hinweis

Dieses Plugin liefert nur die Orientierung. Tiefe Mandatsbearbeitung erfordert die Expertise des Fachanwalts für Familienrecht.

---

## Skill: `orientierung-fristen-form-und-zustaendigkeit`

_Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitspro..._

# Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: FamFG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

### Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Spezialwissen: Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg
- **Normen-/Quellenanker:** FamFG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Orientierung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `orientierung-mandat-fachanwaltschaft`

_Orientierung im Fachanwaltsrecht Familienrecht: FAO-Voraussetzungen, Kerngebiete, Verfahren nach FamFG und BGB überblicken: Normen:..._

# Orientierung im Fachanwaltsrecht Familienrecht: FAO-Voraussetzungen, Kerngebiete, Verfahren nach FamFG und BGB überblicken


## Arbeitsbereich

Einstieg in den **Fachanwaltsbereich Familienrecht**. Er klärt zunächst die Verfahrensart (Scheidung, Sorge, Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz, Personenstandsfolgen nach SBGG) und routet anschließend in die tragende Prüfungslinie. Im Mittelpunkt stehen Kindeswohlgefährdung nach § 1666 BGB, Familienmediation nach § 156 FamFG und Cochemer Praxis, der Scheidungsantrag (§§ 1564 ff. BGB, § 133 FamFG) sowie die personenstandsrechtlichen Folgen nach SBGG. Die Prüfungslinien bauen aufeinander auf — zuerst das in der Akte tatsächlich tragende Feld bestimmen, dann ergänzend nur die Felder heranziehen, die der Sachverhalt wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: FamFG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung im Fachanwaltsrecht Familienrecht: FAO-Voraussetzungen, Kerngebiete, Verfahren nach FamFG und BGB überblicken. Normen: FamFG (Beschluss statt Urteil, Verbund § 137 FamFG), §§ 23a und 23b GVG (Familiengericht), BGB Familienrecht. Prüfraster: Sachgebiet (Scheidung, Sorge, Umgang, Unterhalt, Zugewinn, VA), Verfahrenstypen, Eilbedürftigkeit. Output Orientierungs-Memo, Routing zu Fachmodule. Abgrenzung: Mandats-Triage siehe mandat-triage-familienrecht; Detailbearbeitungen siehe Fachmodule.

### Fachanwalt für Familienrecht — Orientierung

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fachanwalt für Familienrecht — Orientierung` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Fachanwalt für Familienrecht — Orientierung
- **Normen-/Quellenanker:** BGB Familienrecht, FamFG, VersAusglG, Unterhaltsrecht, Zugewinn, Gewaltschutz, Kindschaft, internationale Verordnungen und Vollstreckung.
- **Entscheidende Weiche:** Beteiligte, Kind/Unterhalt/Vermögen/Versorgung, Frist, Auskunft, Beleg, Eilbedarf und familiengerichtliche Verfahrensart trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Aktuelle Rechtsprechung (Orientierung Familienrecht, Stand 05/2026)

Verifizierte Eckpfeiler — Live-Verifikation vor Verwendung in Schriftsätzen zwingend:

- BGH, Beschluss vom 22.01.2025 - XII ZB 148/24 (Elternunterhalt; Selbstbehalt verheirateter Unterhaltspflichtiger)
- BVerfG, Beschluss vom 07.10.2025 - 1 BvR 746/23 (Begründungsanforderungen bei mehrjährigem Umgangsausschluss)
- BVerfG, Beschluss vom 28.08.2025 - 1 BvR 1473/25 (Sorgerecht im einstweiligen Anordnungsverfahren; PAS)
- BVerfG, Beschluss vom 09.04.2025 - 1 BvR 1618/24 (internationale Zuständigkeit nach KSÜ, Sorgerechtswirkungen)
- Düsseldorfer Tabelle 2026 (in Kraft seit 01.01.2026, OLG Düsseldorf, Pressemitteilung 01.12.2025; Mindestunterhalt nach 7. MUVÄndV vom 15.11.2024, BGBl. 2024 I Nr. 359)

Weitere Entscheidungen nicht aus Modellwissen zitieren; vor Ausgabe über bundesgerichtshof.de, bundesverfassungsgericht.de, dejure.org, openjur.de verifizieren.

## FAO-Voraussetzungen (§ 5 Abs. 1 FAO)

- **Theoretischer Lehrgang** 120 Stunden (§ 4 FAO).
- **Drei Klausuren** zum Familienrecht (§ 4a FAO).
- **120 Fälle** in den letzten drei Jahren vor Antrag, davon mindestens 60 streitige Fälle (§ 5 FAO).
- **Anmeldung** bei der Rechtsanwaltskammer.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| BGB Familienrecht | §§ 1297 ff. BGB (Ehe Scheidung) §§ 1601 ff. BGB (Unterhalt) §§ 1626 ff. BGB (Elterliche Sorge) §§ 1684 ff. BGB (Umgangsrecht) §§ 1740 ff. BGB (Adoption) §§ 1773 ff. BGB (Vormundschaft) |
| Verfahrensrecht | FamFG §§ 111 ff. (Familiensachen) § 137 FamFG (Scheidungsverbund) §§ 151 ff. FamFG (Kindschaftssachen) |
| Versorgungsausgleich | VersAusglG |
| Lebenspartnerschaft | LPartG |
| Gerichtsverfassung | § 23a GVG (Familiengericht beim AG) § 23b GVG |
| EU- und Völkerrecht | Brüssel IIb-VO (EU) 2019/1111 |

## Typische Mandate

- Scheidung im Verbund (Scheidung + Versorgungsausgleich + Folgesachen)
- Sorgerechtsverfahren bei getrennt lebenden Eltern
- Umgangsrechtsstreit
- Kindesunterhalt nach Düsseldorfer Tabelle
- Ehegattenunterhalt (Trennungs- und nachehelicher Unterhalt)
- Zugewinnausgleich
- Ehevertrag und Scheidungsfolgenvereinbarung
- Gewaltschutz nach GewSchG

## Wichtige Fristen

- **Beschwerde** § 63 FamFG — ein Monat.
- **Sofortige Beschwerde** § 64 FamFG — zwei Wochen.
- **Wiedereinsetzung** § 17 FamFG.
- **Versorgungsausgleichs-Anträge** parallel zum Scheidungsverfahren.
- **Anfechtungsfristen** Vaterschaft § 1600b BGB — zwei Jahre ab Kenntnis.

## Hauptgericht

- **Familiengericht** beim Amtsgericht (§ 23a Abs. 1 Nr. 1 GVG).
- **OLG-Familiensenat** als Beschwerdegericht (§ 119 GVG).
- **BGH XII. Zivilsenat** in Familiensachen.

## Berufsverband

- Deutscher Anwaltverein DAV Arbeitsgemeinschaft Familienrecht.
- Deutsche Gesellschaft für Familienrecht.

## Schnittstellen zu anderen Plugins

- **kanzlei-allgemein** für Fristenbuch Timesheet Versand-Vor-Check.
- **methodenlehre-buergerliches-recht** und **zitierweise-deutsches-recht** als Hausstandards.

## Hinweis

Dieses Plugin liefert nur die Orientierung. Tiefe Mandatsbearbeitung erfordert die Expertise des Fachanwalts für Familienrecht.

---

## Skill: `erstgespraech-mandatsannahme`

_Strukturierter Erstgespraechsleitfaden für Familien-, Kindschafts- und Versorgungsausgleichsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen: Strukturierter E..._

# Strukturierter Erstgespraechsleitfaden für Familien-, Kindschafts- und Versorgungsausgleichsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: FamFG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierter Erstgespraechsleitfaden für Familien-, Kindschafts- und Versorgungsausgleichsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.

### Erstgespraech und Mandatsannahme im Familien-, Kindschafts- und Versorgungsausgleichsrecht

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erstgespraech und Mandatsannahme im Familien-, Kindschafts- und Versorgungsausgleichsrecht` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Erstgespraech und Mandatsannahme im Familien-, Kindschafts- und Versorgungsausgleichsrecht
- **Normen-/Quellenanker:** BGB Familienrecht, FamFG, VersAusglG, Unterhaltsrecht, Zugewinn, Gewaltschutz, Kindschaft, internationale Verordnungen und Vollstreckung.
- **Entscheidende Weiche:** Beteiligte, Kind/Unterhalt/Vermögen/Versorgung, Frist, Auskunft, Beleg, Eilbedarf und familiengerichtliche Verfahrensart trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Aktuelle Rechtsprechung (Familienrecht Erstgespräch)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Familien-, Kindschafts- und Versorgungsausgleichsrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klären, Konflikt- und GwG-Prüfung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Familien-, Kindschafts- und Versorgungsausgleichsrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klägerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Scheidung, Unterhalt, ZGW, VA, Sorge/Umgang, Gewaltschutz, EheVertrag
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Scheidungsantrag, Unterhaltsklage, Sorgerechtsantrag, VA-Beschwerde). Frist-Alarm an die Vorbereitung weitergeben.

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

Standard-Streitwerte im Bereich Familien-, Kindschafts- und Versorgungsausgleichsrecht:

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

- BORA, BRAO, FAO für Fachanwaltschaft Familien-, Kindschafts- und Versorgungsausgleichsrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- §§ 1297 ff. BGB, FamFG, VersAusglG, UVG, GewSchG, IntFamRVG (für fachliche Erstpruefung).
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

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Familien-, Kindschafts- und Versorgungsausgleichsrecht). Handlungs-Sequenz:

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
- Verfahrensdauer im Bereich Familien-, Kindschafts- und Versorgungsausgleichsrecht: Erfahrungswerte nach Instanz.
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

---

## Skill: `erstpruefung-und-mandatsziel`

_Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodu..._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: FamFG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Familienrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/VersAusglG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

### Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel

## Fachlicher Kern — Familienrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 1360a, 1361, 1565 ff., 1570 ff., 1601 ff., 1626 ff., 1684, 1687, 1687a; FamFG §§ 49 ff., 76, 86 ff., 112 ff.; VersAusglG §§ 1, 2, 5, 10 ff., 27, 51; GewSchG.
- **Verifizierte Anker:** BGH, Beschluss vom 02.04.2025 - XII ZB 576/24 (Abänderung Versorgungsausgleich nach Tod, § 51 VersAusglG, § 88 Abs. 2 SGB VI); BGH, Beschluss vom 18.10.2023 - XII ZB 197/23 (Abänderung nur bei Veränderung, nicht Fehlerkorrektur der Ausgangsentscheidung).
- **Arbeitsmodus:** Zuerst Verfahrenstyp und Eilbedarf klären: Sorge/Umgang, Unterhalt, Zugewinn, Versorgungsausgleich, Gewaltschutz; danach Kindesschutz, Titel, Fristen, Auskünfte, Beleglage und Vollstreckbarkeit.
- **Outputpflicht:** Eilvermerk, Unterhalts-/Zugewinntabelle, Antragsentwurf, Jugendamts-/Gegnerbrief, Vergleichsvorschlag oder Mandantenfahrplan.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** FamFG.

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

## Skill: `fachanwalt-familienrecht-zugewinnausgleich-berechnen`

_Zugewinnausgleich nach §§ 1372-1390 BGB berechnen: Trennung oder Scheidung erfordert Aufstellung von Anfangs- und Endvermögen. Normen: § 1373 BGB (Zugewinn), § 1374 BGB (Anfangsvermögen inkl. Privilegierungen Abs. 2), § 1376 BGB (Bewertungsstichtag Endvermögen), § 1379 BGB (Auskunftsanspruch), § 254 ZPO (Stufenklage). Prüfraster: Anfangsvermögen/Endvermögen, Erbschaft-/Schenkungsprivileg, negatives Anfangsvermögen seit 2009, Verfuegungsbeschraenkungen § 1365 BGB, Verjährung 3 Jahre. Output Berechnungs-Schema, Auskunftsstufe. Abgrenzung: Versorgungsausgleich siehe fachanwalt-familienrecht-versorgungsausgleich; Scheidungsantrag siehe fachanwalt-familienrecht-scheidungsantrag-stellen._

# Zugewinnausgleich berechnen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Kaltstart-Rückfragen

1. Wann wurde die Ehe geschlossen, wann wurde Trennung erklärt, wann Zustellung des Scheidungsantrags (Stichtag § 1384 BGB für Endvermögen)?
2. Welchen Güterstand hatten die Eheleute — gesetzlicher Güterstand der Zugewinngemeinschaft oder ehevertraglich modifiziert?
3. Welches Vermögen hatte jeder Ehegatte bei Eheschließung (Anfangsvermögen § 1374 BGB) — Belege, Bewertungen?
4. Welches Vermögen besteht zum Stichtag (Konten, Immobilien, Unternehmen, Lebensversicherungen, Kfz, Schulden)?
5. Gab es Erbschaften, Schenkungen, Schmerzensgeld während der Ehe? Diese sind privilegiert (§ 1374 Abs. 2 BGB) und werden dem Anfangsvermögen hinzugerechnet.

## Anspruchsgrundlagen und Berechnung

- Gesetzlicher Güterstand: Zugewinngemeinschaft (§ 1363 BGB), Vermögensmassen bleiben getrennt, Ausgleich erst bei Beendigung.
- Beendigung durch Tod, Scheidung oder Vereinbarung; Ausgleichsforderung als Geldanspruch (§ 1378 Abs. 1 BGB).
- Anfangsvermögen (§ 1374 BGB) = Aktiva − Passiva bei Eheschließung; Erbschaften, Schenkungen, Ausstattung nach § 1374 Abs. 2 BGB werden hinzugerechnet (privilegierter Erwerb).
- Endvermögen (§ 1375 BGB) = Aktiva − Passiva am Stichtag § 1384 BGB (Rechtshängigkeit des Scheidungsantrags). Illoyale Vermögensminderungen werden hinzugerechnet (§ 1375 Abs. 2 BGB).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Zugewinn = Endvermögen − Anfangsvermögen (nicht negativ — § 1373 BGB).
- Ausgleichsforderung = (Zugewinn des Höhergewinnenden − Zugewinn des Wenigergewinnenden) ÷ 2 (§ 1378 Abs. 1 BGB).
- Begrenzung: Ausgleichsforderung wird durch Vermögen des Schuldners am Stichtag begrenzt (§ 1378 Abs. 2 BGB).
- Auskunftsanspruch zu drei Stichtagen Trennung, Beendigung und ergänzend Anfangsvermögen (§ 1379 BGB seit 2009) — Stufenklage § 254 ZPO.
- Verjährung Ausgleichsforderung: drei Jahre § 195 BGB ab Kenntnis der Beendigung des Güterstands (§ 199 BGB).

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Beweislast

- Jeder Ehegatte trägt Beweislast für sein Anfangsvermögen und für anspruchsmindernde Tatsachen.
- Vermutung gegen Anfangsvermögen widerlegbar (§ 1377 Abs. 3 BGB): Wenn kein Verzeichnis erstellt wurde gilt das Endvermögen als Zugewinn — Vermutung kann widerlegt werden.
- Illoyale Vermögensminderungen § 1375 Abs. 2 BGB: Beweislast trägt der Ausgleichsberechtigte (Schenkung ohne Anstandspflicht, Vermögensvergeudung, Benachteiligung).

## Berechnungsschema

```
                              Ehegatte A     Ehegatte B
Endvermoegen (Stichtag § 1384)   X1            X2
+ illoyale Minderungen § 1375    +a1           +a2
- Schulden                       -b1           -b2
= Endvermoegen bereinigt         E_A           E_B

Anfangsvermoegen indexiert       Y1            Y2
+ privilegierter Erwerb § 1374   +p1           +p2
= Anfangsvermoegen bereinigt     A_A           A_B

Zugewinn = max(E - A; 0)         Z_A           Z_B

Ausgleichsforderung = (Z_max - Z_min) / 2
Schuldner ist der Ehegatte mit groesserem Zugewinn
```

## Schreibvorlage Auskunftsanforderung § 1379 BGB

```
Sehr geehrte Frau Kollegin sehr geehrter Herr Kollege

namens und in Vollmacht unserer Mandantin fordern wir Ihren Mandanten
auf binnen vier Wochen Auskunft ueber sein Vermoegen § 1379 BGB zu
erteilen und zwar zu folgenden Stichtagen
1. Trennung [Datum]
2. Anfangsvermoegen Eheschliessung [Datum]
3. Endvermoegen Rechtshaengigkeit Scheidungsantrag [Datum]

Die Auskunft hat saemtliche Aktiva und Passiva mit Belegen zu
enthalten Konten Immobilien Beteiligungen Lebensversicherungen
Kfz Schmuck Kunst. Auf Verlangen ist eidesstattliche Versicherung
nach § 260 Abs. 2 BGB abzugeben.

Andernfalls werden wir Stufenklage § 254 ZPO erheben.

Mit kollegialen Gruessen
```

## Übergabe

- Bei Verweigerung: Stufenklage Auskunft + eidesstattliche Versicherung + Zahlung beim Familiengericht (Gueterrechtssache § 261 FamFG; Zuständigkeit § 262 FamFG i.V.m. §§ 23a, 23b GVG).
- Bei Auslandsvermögen Auskunftsanspruch erstreckt sich auch auf ausländisches Vermögen.
- Bei Unternehmenswerten Sachverständigengutachten zur Bewertung notwendig — Kosten regelmäßig vorzustrecken.
- Anschluss: Skill `fachanwalt-familienrecht-scheidungsantrag-stellen` bei Verbund nach § 137 FamFG.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

