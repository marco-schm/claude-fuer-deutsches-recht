# Megaprompt: fachanwalt-erbrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 97 Skills des Plugins `fachanwalt-erbrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Anwalts-Dashboard Fachanwalt Erbrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zustä…
2. **mandat-triage-erbrecht** — Erbrechtsmandat schnell einordnen und Sofortmassnahmen bestimmen: §§ 1922 1944 2303 BGB §§ 342 ff. FamFG. Prüfraster: Er…
3. **fachanwalt-erbrecht-orientierung** — Erbrechtsmandat einordnen Bearbeitungsroute bestimmen und erste Prioritaeten setzen. §§ 1922 2229 2303 BGB § 43a BRAO. P…
4. **erstgespraech-mandatsannahme** — Erstgespraech im Erbrechtmandat strukturieren und Sachverhalt vollständig aufnehmen: §§ 1922 ff. BGB Erbfolge § 43a BRAO…
5. **erstpruefung-und-mandatsziel** — Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG…
6. **fachanwalt-erbrecht-pflichtteilsberechnung** — Pflichtteilsanspruch berechnen wenn Erblasser nahe Angehoerige vom Erbe ausgeschlossen hat. §§ 2303 2311 2314 BGB Pflich…
7. **fachanwalt-erbrecht-pflichtteilsergaenzung-2325** — Pflichtteilsergaenzungsanspruch nach § 2325 BGB berechnen wenn Erblasser Schenkungen gemacht hat. § 2325 BGB Pflichtteil…
8. **fachanwalt-erbrecht-erbschaftsausschlagung** — Erbschaftsausschlagung erlaeutern und Erklärung formulieren wenn Erbe ueberschuldet ist oder sonstige Gründe vorliegen. …
9. **fachanwalt-erbrecht-testamentsentwurf** — Testament oder Erbvertrag entwerfen wenn Mandant Nachlassplanung vornehmen moechte. §§ 2229 2231 2247 BGB Testament §§ 2…
10. **fachanwalt-erbrecht-verhandlung-mediation-erbengemeinschaft** — Streit in der Erbengemeinschaft durch Verhandlung oder Mediation lösen. §§ 2032 2042 2047 BGB Erbengemeinschaft. Prüfras…

---

## Skill: `einstieg-routing`

_Anwalts-Dashboard Fachanwalt Erbrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt bleibt im Driver Seat._

# Anwalts-Dashboard Fachanwalt Erbrecht

> Erbfall, Pflichtteil, Erbschein, Erbengemeinschaft, Testament — Ausschlagungsfrist tickt ab Kenntnis. Wer beerbt wen, wann?
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 1944 BGB: 6 Wochen** Ausschlagung ab Kenntnis von Anfall und Berufungsgrund (6 Monate bei Auslandsbezug). § 1954 BGB: Anfechtung der Annahme/Ausschlagung 6 Wochen. § 2306 BGB: Ausschlagungsrecht bei Beschwerung 6 Wochen. § 2082 BGB: Anfechtung Testament 1 Jahr ab Kenntnis. § 2332 BGB: Pflichtteils-Verjährung 3 Jahre. | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Erbe §§ 1922, 1942 BGB · Pflichtteil §§ 2303 ff. BGB · Pflichtteilsergänzung §§ 2325 ff. BGB · Auskunft § 2314 BGB · Auseinandersetzung §§ 2042 ff. BGB · Erbschein §§ 2353 ff. BGB · Vermächtnis §§ 2147 ff. BGB. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Nachlassgericht am letzten gewöhnlichen Aufenthalt (§ 343 FamFG). Streitige Erbsachen: LG/AG nach Streitwert (§ 27 ZPO). | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Ausschlagungsfrist 6 Wochen läuft ab Kenntnis; Akten dokumentieren. 🟠 Pflichtteilsergänzung (10-Jahresfrist § 2325 III BGB) und Pflichtteils-Verjährung (3 Jahre) gegen Schenkungen verfolgen.
- **Beweislage:** 🟠 Pflichtteils-Auskunft § 2314 BGB lückenhaft → notarielles Verzeichnis erzwingen. 🔴 Testament: Testierfähigkeit Beweis (medizinische Akten, Zeugen, ggf. Sachverständige).
- **Wirtschaftlich:** 🔴 Nachlassinsolvenz droht → § 1980 BGB Antrag (binnen 3 Monaten), Erbenhaftungsbeschränkung. 🟠 Hoher Nachlasswert: Pflichtteilsanspruch parallel zu Auseinandersetzung.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Pflichtteil berechnen / geltend machen** | `pflichtteil-berechnen` | Pflichtteilsquote, Wertermittlung, Auskunftsverfahren § 2314 BGB |
| Ausschlagung der Erbschaft | `erbschaftsausschlagung` | 6-Wochen-Frist § 1944 BGB, notarielle/gerichtliche Erklärung |
| Testament auslegen | `testament-auslegung-und-andeutung` | Andeutungstheorie, Auslegungsregeln, ergänzende Auslegung |
| Erbschein beantragen | `erbschein-antrag` | Antrag, Glaubhaftmachung, eidesstattliche Versicherung |
| Erbengemeinschaft blockiert | `erbengemeinschaft-blockade-auseinandersetzung` | Teilungsklage, Vermittlungsverfahren §§ 363 ff. FamFG |

## Norm-Radar (live verifizieren)

- **§ 1944 BGB** — Ausschlagungsfrist 6 Wochen
- **§ 2303 BGB** — Pflichtteilsanspruch
- **§ 2314 BGB** — Auskunftsanspruch des Pflichtteilsberechtigten
- **§ 2325 BGB** — Pflichtteilsergänzung; 10-Jahres-Abschmelzung
- **§ 2353 BGB** — Erbschein
- **§ 1980 BGB** — Antrag Nachlassinsolvenz

## Genau eine Rückfrage (nur wenn nötig)

> Vertreten Sie **Erbe(n), Pflichtteilsberechtigte oder Vermächtnisnehmer** — und steht eine **Frist** (Ausschlagung, Anfechtung) oder eine **Verteilungsfrage** im Vordergrund?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Pflichtteilsergänzung § 2325 BGB; 10-Jahres-Abschmelzung** — BGH IV. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Pflichtteilsstrafklausel (Berliner Testament); Auslegung** — BGH IV. Zivilsenat — *live verifizieren auf* `bundesgerichtshof.de`
- **Erbschaftsteuer; Verschonungsregelungen** — BVerfG 1. Senat (Urteil v. 17.12.2014, 1 BvL 21/12) — *live verifizieren auf* `bundesverfassungsgericht.de`
- **Digitaler Nachlass (Facebook-Konto)** — BGH III. Zivilsenat (Urteil v. 12.07.2018, III ZR 183/17) — *live verifizieren auf* `bundesgerichtshof.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

---

## Skill: `mandat-triage-erbrecht`

_Erbrechtsmandat schnell einordnen und Sofortmassnahmen bestimmen: §§ 1922 1944 2303 BGB §§ 342 ff. FamFG. Prüfraster: Erbfolge Testament Ausschlagungsfrist Pflichtteil Nachlassinsolvenz. Outp..._

# Erbrechtsmandat schnell einordnen und Sofortmassnahmen bestimmen


## Aktenstart statt Formularstart

Wenn zu **Erbfall Eu Mandat Triage Pflichtteil Auskunft** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Fachanwalt Erbrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

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
- Tragende Normen verifizieren: AO §§ 38, 42, 90, 93, 153, 162, 164, 169-171, 173, 233a, 370-378, UStG, EStG, KStG, GewStG, GrEStG, ErbStG, FGO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Erbrechtsmandat schnell einordnen und Sofortmassnahmen bestimmen. §§ 1922 1944 2303 BGB §§ 342 ff. FamFG. Prüfraster: Erbfolge Testament Ausschlagungsfrist Pflichtteil Nachlassinsolvenz. Output: Triage-Memo Sofortmassnahmen Fristen-Ampel. Abgrenzung: Triage; Detailarbeit in Spezialist-Skills.

### Mandat-Triage Erbrecht

## Fachlicher Kern — Erbrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandat-Triage Erbrecht` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 1922 ff., 1937, 1942 ff., 1953, 1967, 2032 ff., 2042, 2050 ff., 2078, 2084, 2203 ff., 2303 ff., 2314, 2325, 2333; FamFG §§ 343 ff.; EuErbVO.
- **Verifizierte Anker:** BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteil, Entstehung und Verjährung bei postmortaler Vaterschaftsfeststellung); BGH, Beschluss vom 15.01.2025 - IV ZR 166/24 (Auskunftspflichten bei Pflichtteil/Testamentsvollstreckung); Rechtsprechung zu notariellen Nachlassverzeichnissen nur mit Aktenzeichen/Quelle ausgeben.
- **Arbeitsmodus:** Erst Erbfolge, Ausschlagung, Nachlassbestand, Haftung und Fristen sichern; dann Pflichtteil, Auskunft/Wertermittlung, Testamentsauslegung, Erbengemeinschaft und internationale Anknüpfung trennen.
- **Outputpflicht:** Nachlassmatrix, Pflichtteils-/Ergänzungstabelle, Auskunftsverlangen, Erbscheinsantrag, Teilungsplan oder Klagebaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Aktuelle Rechtsprechung (Triage-Orientierung, Stand 05/2026)

Verifizierte Eckpfeiler — Live-Verifikation vor Verwendung in Schriftsätzen zwingend:

- BGH 12.03.2025 - IV ZR 88/24 (Pflichtteilsanspruch nichteheliches Kind; § 2317 Abs. 1 BGB maßgebend trotz Ausübungssperre)
- BGH 02.07.2025 - IV ZR 93/24 (Zuwendung an behandelnden Arzt; Berufsordnung kein § 134 BGB-Verbot; Testierfreiheit; § 138 BGB Einzelfallprüfung)

Anhängig: BVerfG 1 BvR 804/22 zur Verfassungsmäßigkeit der erbschaftsteuerlichen Begünstigung von Betriebsvermögen (Stand 05/2026 nicht entschieden).

Weitere Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe über bundesgerichtshof.de, bundesverfassungsgericht.de, dejure.org oder openjur.de verifizieren.

## Ablauf — sieben Fragen

### Frage 1 — Vorsorge oder Abwicklung?

- Vorsorge (Erblasser lebt — Testament Erbvertrag Vorsorgevollmacht)
- Abwicklung (Erblasser verstorben — Erbschein Pflichtteil Auseinandersetzung)
- Streit über Lebzeit-Schenkungen

### Frage 2 — Mandantenrolle?

- Erblasser (vor Tod)
- Erbe (Alleinerbe Miterbe)
- Pflichtteilsberechtigter (enterbt oder zu wenig erhalten)
- Vermächtnisnehmer
- Testamentsvollstrecker
- Erblasser-Gläubiger
- Nachlassgläubiger
- Finanzamt (selten — vertretbar nur unter strikter Trennung)

### Frage 3 — Akute Eilbedürftigkeit?

- **Ausschlagungsfrist** läuft (sechs Wochen ab Kenntnis § 1944 BGB; sechs Monate bei Auslandsbezug oder Erblasser-Wohnsitz Ausland)
- **Erbenhaftung droht** — überschuldeter Nachlass
- **Vorrätige Nachlassgegenstände** akut zu sichern
- **Beerdigung organisatorisch** offen
- **Erbschaftsteuer-Anzeige** drei Monate § 30 ErbStG
- **Räumung Wohnung** Mietvertrag Erblasser
- **Patientenverfügung Vorsorge** akut benötigt — meist `betreuungsrecht`-Plugin

### Frage 4 — Vorgang konkret?

- Erbschein-Antrag
- Testamentseröffnung
- Testamentsanfechtung
- Erbauseinandersetzung (Teilungsversteigerung)
- Pflichtteils-Anspruch
- Vermächtnis-Anspruch
- Auflagen-Erfüllung
- Erbschaftsausschlagung
- Nachlassinsolvenz
- Erbschaftsteuer
- Testamentsvollstreckung

### Frage 5 — Verfügungen?

- Testament öffentlich oder eigenhändig
- Berliner Testament
- Erbvertrag notariell
- Patientenverfügung Vorsorgevollmacht
- Schenkungsversprechen Schenkungsverträge
- Lebensversicherung mit Bezugsberechtigung

### Frage 6 — Familienverhältnisse?

- Ehegatte / eingetragener Lebenspartner — Güterstand!
- Abkömmlinge (eheliche nichteheliche adoptiert)
- Eltern — sofern keine Abkömmlinge
- Geschwister Verwandte zweite Ordnung
- Patchwork-Konstellation

### Frage 7 — Wirtschaftliche Verhältnisse?

- Nachlasswert geschätzt
- Schulden
- Schenkungen letzte zehn Jahre
- Pflichtteils-Verzichts-Verträge
- Erbschaftsteuer-Belastung
- Mandanten-Vermögen (PKH-Bedürftigkeit)

## Routing-Matrix

| Vorgang | Folge-Skill |
|---|---|
| Pflichtteil | `pflichtteil-berechnen` |
| Vorsorge Testament-Vertragsentwurf | (Skill testament-erbvertrag-entwurf — perspektivisch) |
| Erbschein-Antrag | (Skill erbschein-antrag — perspektivisch) |
| Testamentsanfechtung | (Skill testamentsanfechtung — perspektivisch) |
| Erbauseinandersetzung | (Skill erbauseinandersetzung — perspektivisch) |
| Ausschlagung überschuldet | (Skill ausschlagung-nachlassinsolvenz — perspektivisch) |
| Erbschaftsteuer | weiter an `anw-mandat-triage-steuerrecht` ErbSt-Spezifikum |
| Testamentsvollstreckung | (Skill testamentsvollstreckung — perspektivisch) |

## Mandatsannahme

- **Konflikt-Check** — keine doppelte Vertretung Miterben gegeneinander
- **Streitwert** Nachlasswert oder Pflichtteils-Forderungs-Höhe
- **Komplexität** Auslandsbezug Unternehmensbeteiligung Stiftungs-Errichtung

## Sofort-Fristen

- **Ausschlagung** sechs Wochen § 1944 BGB
- **Pflichtteils-Verjährung** drei Jahre § 2332 BGB
- **Erbschaftsteuer-Anzeige** drei Monate § 30 ErbStG
- **Erbschaftsteuer-Erklärung** mind. ein Monat nach Aufforderung
- **Anfechtung Testament** ein Jahr ab Kenntnis § 2082 BGB

## Eskalation

- **Telefon-Sofort** Ausschlagungsfrist läuft heute / morgen — überschuldeter Nachlass
- **Binnen einer Stunde** Erbenhaftung droht
- **Heute** Auskunftsschreiben § 2314 BGB Erbschein-Antrag-Vorbereitung
- **Diese Woche** Pflichtteils-Stufenklage Testamentsentwurf

## Ausgabe

- `triage-protokoll-erbrecht.md`
- Aktenanlage
- Frist im Fristenbuch (Ausschlagung Pflichtteils-Verjährung Erbschaftsteuer)
- Mandatsvereinbarung mit Honorarvereinbarung
- Empfehlung Folge-Skill
- Hinweis Sachverständigen-Bewertung Immobilie Unternehmen wenn relevant

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen

- BGB §§ 1922 ff. 1944 2303 ff. 2332 § 2082
- ErbStG § 30
- BGH IV. Zivilsenat
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Burandt/Rojahn Erbrecht

---

## Skill: `fachanwalt-erbrecht-orientierung`

_Erbrechtsmandat einordnen Bearbeitungsroute bestimmen und erste Prioritaeten setzen. §§ 1922 2229 2303 BGB § 43a BRAO. Prüfraster: Erbfolge Testament Pflichtteil Ausschlagung Nachlassinsolvenz Fristen. Output: Mandat-Einordnung Normenmap naechste Schritte. Abgrenzung: Orientierungsskill; Detailarbeit in Spezialist-Skills._

# Fachanwalt für Erbrecht — Orientierung

## Aktuelle Rechtsprechung (Orientierung Erbrecht, Stand 05/2026)

Verifizierte Eckpfeiler — Live-Verifikation vor Verwendung in Schriftsätzen zwingend:

- BGH, Urteil vom 12.03.2025 - IV ZR 88/24: Pflichtteilsanspruch nichteheliches Kind; § 2317 Abs. 1 BGB maßgebend trotz Ausübungssperre § 1600d Abs. 5 BGB.
- BGH, Urteil vom 02.07.2025 - IV ZR 93/24: Zuwendung von Todes wegen an behandelnden Arzt nicht wegen Verstoß gegen ärztliche Berufsordnung unwirksam; Testierfreiheit (Art. 14 GG) überwiegt; § 138 BGB bleibt Einzelfallprüfung.

Anhängig zur Verfassungsmäßigkeit der erbschaftsteuerlichen Verschonung von Betriebsvermögen: BVerfG 1 BvR 804/22 (Stand 05/2026 noch nicht entschieden); Beobachtung empfohlen.

Weitere Rechtsprechung nicht aus Modellwissen zitieren; vor Ausgabe über bundesgerichtshof.de, dejure.org oder openjur.de verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 80 Fälle in den letzten drei Jahren, davon mindestens 60 erbrechtliche Fälle einschließlich 20 streitiger Verfahren.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Erbrecht BGB | §§ 1922 ff. BGB (Erbfolge) §§ 2064 ff. (Testament) §§ 2274 ff. (Erbvertrag) §§ 2303 ff. (Pflichtteil) §§ 2147 ff. (Vermächtnis) §§ 2032 ff. (Erbengemeinschaft Auseinandersetzung) |
| Nachlassverfahren | FamFG §§ 342 ff. (Nachlassgericht beim AG) |
| Erbschaftsteuer | ErbStG Bewertungsgesetz |
| Internationales Erbrecht | EU-ErbVO (Verordnung EU Nr. 650/2012) Europaeisches Nachlasszeugnis |
| Pflichtteilsentziehung | §§ 2333 ff. BGB |

## Typische Mandate

- Testamentsentwurf und Erbvertragsentwurf
- Erbscheinantrag und -anfechtung
- Pflichtteilsstreit (Auskunfts- und Wertfeststellungsklage Stufenklage § 254 ZPO)
- Erbauseinandersetzung
- Testamentsanfechtung (§ 2078 BGB)
- Schenkung und Pflichtteilsergänzungsanspruch (§ 2325 BGB)
- Erbschaftsteuer-Bescheid (siehe steuerrecht-anwalt-und-berater)
- Internationale Erbfälle und EU-ErbVO

## Fristen

- **Erbschaftsannahme oder -ausschlagung** § 1944 BGB — sechs Wochen ab Kenntnis vom Erbfall und Berufungsgrund; bei Auslandsaufenthalt sechs Monate.
- **Anfechtung Erbschaftsannahme/-ausschlagung** § 1954 BGB — sechs Wochen.
- **Pflichtteilsanspruch** Verjährung drei Jahre ab Kenntnis (§ 2332 BGB iVm § 195 BGB).
- **Anfechtung Testament** § 2082 BGB — ein Jahr ab Kenntnis.
- **Schenkungsfrist Pflichtteilsergänzung** § 2325 BGB — zehn Jahre (mit Abschmelzungsmodell).

## Hauptgerichte

- Nachlassgericht beim Amtsgericht (§ 342 FamFG).
- Beschwerdegericht: Landgericht / OLG.
- BGH IV. Zivilsenat für Erbsachen.
- Finanzgericht bei Erbschaftsteuer.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- ARGE Erbrecht DAV.
- Deutsche Vereinigung für Erbrecht und Vermögensnachfolge DVEV.

## Schnittstellen

- **kanzlei-allgemein** Fristen Versand.
- **steuerrecht-anwalt-und-berater** bei Erbschaftsteuer.
- **gesellschaftsrecht** bei Unternehmensnachfolge.

---

## Skill: `erstgespraech-mandatsannahme`

_Erstgespraech im Erbrechtmandat strukturieren und Sachverhalt vollständig aufnehmen: §§ 1922 ff. BGB Erbfolge § 43a BRAO. Prüfraster: Erblasser Testament gesetzliche Erben..._

# Erstgespraech im Erbrechtmandat strukturieren und Sachverhalt vollständig aufnehmen


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: AO §§ 38, 42, 90, 93, 153, 162, 164, 169-171, 173, 233a, 370-378, UStG, EStG, KStG, GewStG, GrEStG, ErbStG, FGO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Erstgespraech im Erbrechtmandat strukturieren und Sachverhalt vollständig aufnehmen. §§ 1922 ff. BGB Erbfolge § 43a BRAO. Prüfraster: Erblasser Testament gesetzliche Erben Pflichtteilsberechtigte Nachlassbestand Fristen. Output: Mandat-Steckbrief Sachverhaltsprotokoll fehlende Unterlagen. Abgrenzung: Einstiegs-Skill; inhaltliche Arbeit in Spezialist-Skills.

### Erstgespraech und Mandatsannahme im Erb- und Pflichtteilsrecht

## Fachlicher Kern — Erbrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erstgespraech und Mandatsannahme im Erb- und Pflichtteilsrecht` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 1922 ff., 1937, 1942 ff., 1953, 1967, 2032 ff., 2042, 2050 ff., 2078, 2084, 2203 ff., 2303 ff., 2314, 2325, 2333; FamFG §§ 343 ff.; EuErbVO.
- **Verifizierte Anker:** BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteil, Entstehung und Verjährung bei postmortaler Vaterschaftsfeststellung); BGH, Beschluss vom 15.01.2025 - IV ZR 166/24 (Auskunftspflichten bei Pflichtteil/Testamentsvollstreckung); Rechtsprechung zu notariellen Nachlassverzeichnissen nur mit Aktenzeichen/Quelle ausgeben.
- **Arbeitsmodus:** Erst Erbfolge, Ausschlagung, Nachlassbestand, Haftung und Fristen sichern; dann Pflichtteil, Auskunft/Wertermittlung, Testamentsauslegung, Erbengemeinschaft und internationale Anknüpfung trennen.
- **Outputpflicht:** Nachlassmatrix, Pflichtteils-/Ergänzungstabelle, Auskunftsverlangen, Erbscheinsantrag, Teilungsplan oder Klagebaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Erstgespraech und Mandatsannahme im Erb- und Pflichtteilsrecht

- **Spezialfrage (Erstgespraech und Mandatsannahme im Erb- und Pflichtteilsrecht):** Erblasser Testament gesetzliche Erben Pflichtteilsberechtigte Nachlassbestand Fristen. Output: Mandat-Steckbrief Sachverhaltsprotokoll fehlende Unterlagen. Abgrenzung: Einstiegs-Skill; inhaltliche Arbeit in Spezialist-Skills.
- **Arbeitsweise:** Erst Sachverhalt, Norm, Frist, Zuständigkeit und Beweis klären; Rechtsprechung nur verifiziert als tragenden Beleg einsetzen.

## Aktuelle Rechtsprechung (Erbrecht Erstgespräch)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Erb- und Pflichtteilsrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klären, Konflikt- und GwG-Prüfung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Erb- und Pflichtteilsrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klägerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Testament, Erbschein, Pflichtteil, Erbauseinandersetzung, Vermaechtnis, ErbStG
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Pflichtteilsklage, Erbschein-Antrag/Beschwerde, Erbenfeststellungsklage). Frist-Alarm an die Vorbereitung weitergeben.

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

Standard-Streitwerte im Bereich Erb- und Pflichtteilsrecht:

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

- BORA, BRAO, FAO für Fachanwaltschaft Erb- und Pflichtteilsrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- §§ 1922 ff. BGB, FamFG, ErbStG, BeurkG (für fachliche Erstpruefung).
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

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Erb- und Pflichtteilsrecht). Handlungs-Sequenz:

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
- Verfahrensdauer im Bereich Erb- und Pflichtteilsrecht: Erfahrungswerte nach Instanz.
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

_Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt: Fac..._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: AO §§ 38, 42, 90, 93, 153, 162, 164, 169-171, 173, 233a, 370-378, UStG, EStG, KStG, GewStG, GrEStG, ErbStG, FGO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel im Erbrecht: fachlich vertieftes Modul mit Normenradar (BGB/FamFG/EuErbVO), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt.

### Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel

## Fachlicher Kern — Erbrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 1922 ff., 1937, 1942 ff., 1953, 1967, 2032 ff., 2042, 2050 ff., 2078, 2084, 2203 ff., 2303 ff., 2314, 2325, 2333; FamFG §§ 343 ff.; EuErbVO.
- **Verifizierte Anker:** BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteil, Entstehung und Verjährung bei postmortaler Vaterschaftsfeststellung); BGH, Beschluss vom 15.01.2025 - IV ZR 166/24 (Auskunftspflichten bei Pflichtteil/Testamentsvollstreckung); Rechtsprechung zu notariellen Nachlassverzeichnissen nur mit Aktenzeichen/Quelle ausgeben.
- **Arbeitsmodus:** Erst Erbfolge, Ausschlagung, Nachlassbestand, Haftung und Fristen sichern; dann Pflichtteil, Auskunft/Wertermittlung, Testamentsauslegung, Erbengemeinschaft und internationale Anknüpfung trennen.
- **Outputpflicht:** Nachlassmatrix, Pflichtteils-/Ergänzungstabelle, Auskunftsverlangen, Erbscheinsantrag, Teilungsplan oder Klagebaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** BGB, EU, ErbVO.

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

## Skill: `fachanwalt-erbrecht-pflichtteilsberechnung`

_Pflichtteilsanspruch berechnen wenn Erblasser nahe Angehoerige vom Erbe ausgeschlossen hat. §§ 2303 2311 2314 BGB Pflichtteil. Prüfraster: Pflichtteilsberechtigter Nachlasswert Bewertung Auskunftsanspruch Ergaenzungsanspruch Abzuege. Output: Pflichtteilsberechnung Auskunftsklage-Entwurf. Abgrenzung: nicht für Pflichtteilsergaenzungsanspruch (fachanwalt-erbrecht-pflichtteilsergaenzung-2325)._

# Pflichtteilsberechnung — Auskunft und Stufenklage

## Mandantenfragen beim Kaltstart

1. Wer ist der Erblasser, wann ist der Erbfall eingetreten und wo war der letzte gewöhnliche Aufenthalt?
2. In welchem Verhältnis steht der Mandant zum Erblasser (Abkömmling, Ehegatte, Elternteil)? Wurde er durch Testament oder Erbvertrag enterbt oder mit weniger als der Hälfte des gesetzlichen Erbteils bedacht?
3. Wer sind die übrigen pflichtteilsberechtigten und erbenden Personen? Gibt es Adoptivkinder, Stiefkinder, Halbgeschwister?
4. Hat der Erblasser in den letzten zehn Jahren vor dem Erbfall Schenkungen oder gemischte Schenkungen getätigt (Pflichtteilsergänzung § 2325 BGB)?
5. Liegt das Bestandsverzeichnis nach § 2314 BGB schon vor oder muss es erst eingefordert werden?
6. Haben die Erben die Auskunft verweigert, unvollständig erteilt oder die Bewertung blockiert?
7. Ist Verjährung drohend — Erbfall + 3 Jahre Jahresende § 2332 BGB?
8. Bestehen Anzeichen für verschleierte Schenkungen (Übertragungen unter Nießbrauch, Schenkungen an Lebensgefährten)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|------|--------|
| § 2303 BGB | Pflichtteil als Geldanspruch — Hälfte des gesetzlichen Erbteils; Pflichtteilsberechtigte |
| § 2305 BGB | Ergänzungsanspruch bei zu geringer Bedachtung |
| § 2311 BGB | Bewertungsstichtag — Todestag; maßgeblicher Verkehrswert |
| § 2314 BGB | Auskunftsanspruch — Bestandsverzeichnis; SV-Bewertung auf Verlangen; Kosten trägt Nachlass |
| § 2315 BGB | Anrechnung von Vorausempfängen mit Anrechnungsbestimmung |
| § 2316 BGB | Ausgleichung unter Abkömmlingen |
| § 2325 BGB | Pflichtteilsergänzung — Schenkungen letzter 10 Jahre; 10 %-Abschmelzung je Jahr |
| § 2327 BGB | Anrechnung Eigengeschenke des Pflichtteilsberechtigten |
| § 2329 BGB | Direktanspruch gegen Beschenkte wenn Nachlass insufficient |
| § 2332 BGB | Verjährung — 3 Jahre ab Kenntnis; 30 Jahre absolut § 199 Abs. 3a BGB |

## Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---------|-------------|-------|-------------|
| BGH IV. Zivilsenat | IV ZR 88/24 | 12.03.2025 | Für die Entstehung des Pflichtteilsanspruchs nach § 199 Abs. 1 Nr. 1 BGB ist § 2317 Abs. 1 BGB auch dann maßgebend, wenn der Berechtigte zum Zeitpunkt des Erbfalls aufgrund der gesetzlichen Ausübungssperre in § 1600d Abs. 5 BGB an einer erfolgreichen Anspruchsdurchsetzung gehindert ist (nichteheliches Kind, Vaterschaftsfeststellung). Quelle: bundesgerichtshof.de bzw. dejure.org. |
| BGH IV. Zivilsenat | IV ZR 93/24 | 02.07.2025 | Eine Zuwendung von Todes wegen an den behandelnden Arzt des Erblassers ist nicht deshalb unwirksam, weil sie gegen ein berufsständisches Zuwendungsverbot der ärztlichen Berufsordnung (§ 32 Abs. 1 S. 1 BO) verstößt. Berufsrecht ist kein Verbotsgesetz i.S.d. § 134 BGB; Testierfreiheit (Art. 14 GG) überwiegt. Sittenwidrigkeit (§ 138 BGB) bleibt Einzelfallprüfung. Quelle: bundesgerichtshof.de Pressemitteilung 122/2025. |
| Weitere Rechtsprechung | Live-Verifikation erforderlich | - | keine weitere Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema — Stufenweise Durchsetzung

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.


| Phase | Schritt | Maßnahme | Norm |
|-------|---------|---------|------|
| Vorbereitung | 1 | Pflichtteilsberechtigung feststellen | § 2303 BGB |
| Vorbereitung | 2 | Erbquote + Pflichtteilsquote berechnen | §§ 1924 ff., 2303 BGB |
| Auskunft | 3 | Auskunftsschreiben § 2314 BGB senden | § 2314 Abs. 1 BGB |
| Auskunft | 4 | Frist setzen: 4 Wochen; notarielles Verzeichnis fordern | § 2314 Abs. 1 Satz 3 BGB |
| Auskunft | 5 | SV-Bewertung fordern für Immobilien/Unternehmen | § 2314 Abs. 1 Satz 2 BGB |
| Klage | 6 | Stufenklage erheben wenn Auskunft verweigert/unvollständig | § 254 ZPO |
| Klage | 7 | Auskunftsstufe — Verzeichnis vollständig einholen | Stufe 1 |
| Klage | 8 | Versicherungsstufe — eidesstattliche Versicherung | Stufe 2 |
| Klage | 9 | Zahlungsstufe — Pflichtteilsbetrag beziffern und einklagen | Stufe 3 |
| Sicherung | 10 | Direktanspruch § 2329 BGB gegen Beschenkte | § 2329 BGB |

## Bestandsverzeichnis § 2314 BGB — Auskunftsinhalt

Das Bestandsverzeichnis muss enthalten:

**Aktiva:**
- Alle Bankkonten und Wertpapierdepots (Saldo Todestag)
- Immobilien (Grundstücksbezeichnung, Grundbuchauszug, Wertangabe)
- Unternehmensbeteiligungen mit Gesellschaftsvertrag und Bewertung
- Krypto-Assets und digitale Vermögenswerte
- Hausrat, Fahrzeuge, Schmuck
- Lebensversicherungen (Rückkaufswert, Bezugsberechtigte)
- Offene Forderungen, Darlehen an Dritte

**Passiva:**
- Verbindlichkeiten Kreditinstitute
- Steuerschulden (Einkommensteuer, Grundsteuer)
- Unterhaltsverpflichtungen
- Beerdigungskosten § 1968 BGB
- Sonstige Verbindlichkeiten

**Schenkungen:**
- Alle Schenkungen letzter 10 Jahre § 2325 BGB
- Gemischte Schenkungen (Kaufpreis erheblich unter Verkehrswert)
- Schenkungen unter Nießbrauchsvorbehalt
- Schenkungen an Ehegatten (unbegrenzte Frist!)

**Ausgleichungen:**
- Vorausempfänge mit Anrechnungsbestimmung § 2315 BGB
- Ausgleichungspflichtige Zuwendungen § 2316 BGB

## Berechnungsschema

```
PFLICHTTEILSBERECHNUNG

Schritt 1: Nettonachlass
   Aktiva zum Todestag:              EUR [A]
 - Erblasserschulden:                EUR [B]
 - Beerdigungskosten:                EUR [C]
 = Nettonachlass:                    EUR [D]

Schritt 2: Ergänzungsmasse § 2325 BGB
   Schenkung 1 [Datum]:
   Nominalwert / bereinigter Wert:   EUR [X]
   Abschmelzung [Y]%:                EUR [Z] (= Ansatz)

   Schenkung 2 [Datum]:
   Niederstwertvergleich:
     Bereinigter Schenkungswert:     EUR [X1]
     Erbfall-Wert:                   EUR [X2]
     Anzusetzender Wert:             EUR [min(X1,X2)]
   Abschmelzung [Y]%:                EUR [Z2]

   Summe Ergänzungsmasse:            EUR [E]

Schritt 3: Pflichtteilsquote
   Gesetzlicher Erbteil:             [X/Y]
   Pflichtteilsquote:                [X/2Y]

Schritt 4: Pflichtteil
   Nettonachlass × Quote:            EUR [F]

Schritt 5: Pflichtteilsergänzung
   Ergänzungsmasse × Quote:          EUR [G]

Schritt 6: Anrechnung § 2315 BGB
   Vorausempfang mit Anrechnung:   - EUR [H]

Schritt 7: Anrechnung Eigengeschenk § 2327 BGB
   Erhaltene Schenkung vom Erblasser:- EUR [I]

GESAMT-PFLICHTTEILSANSPRUCH:         EUR [F+G-H-I]
Zinsen § 291 BGB ab Klagezustellung:  Basiszins + 5 %
```

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Pflichtteil berechnen und durchsetzen | Stufenklage-Bausteine unten; Auskunft zuerst |
| Variante A — Erbe zahlt freiwillig wenn Berechnung klar | Aussergerichtliche Geltendmachung zuerst; Klage als Backup |
| Variante B — Erblasser hat viel verschenkt | Pflichtteilsergaenzung § 2325 BGB pruefen; 10-Jahres-Frist |
| Variante C — Stufenklage zu aufwaendig | Direktklage auf Zahlung wenn Grundlage klar; Auskunft nachfassen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatz-Bausteine

### Auskunftsanforderung § 2314 BGB

```
An die Erben nach [Name Erblasser]
[Adresse]

Auskunfts- und Wertermittlungsanspruch nach § 2314 BGB

Sehr geehrte Damen und Herren,

namens und in Vollmacht unseres Mandanten — [Name] als
Pflichtteilsberechtigter nach dem am [Datum] verstorbenen
[Erblasser] — fordern wir Sie auf, binnen vier Wochen
ein notarielles Nachlassverzeichnis nach § 2314 Abs. 1
Satz 3 BGB vorzulegen.

Das Verzeichnis muss enthalten:
1. Sämtliche Aktiva und Passiva des Nachlasses zum Todestag
   [Datum], bewertet nach §§ 2311, 2311a BGB
2. Sämtliche Schenkungen des Erblassers der letzten zehn
   Jahre nach § 2325 BGB (auch gemischte Schenkungen,
   Schenkungen unter Nießbrauchsvorbehalt, Schenkungen
   an den Ehegatten ohne zeitliche Begrenzung)
3. Ausgleichungspflichtige Zuwendungen nach §§ 2315,
   2316 BGB

Hinsichtlich der Bewertung von Immobilien und
Unternehmensbeteiligungen verlangen wir bereits jetzt
die Hinzuziehung eines vereidigten Sachverständigen
nach § 2314 Abs. 1 Satz 2 BGB.
Die Kosten trägt der Nachlass (§ 2314 Abs. 2 BGB).

Nach fruchtlosem Fristablauf werden wir Stufenklage
nach § 254 ZPO erheben.

Mit freundlichen Grüßen
[Kanzlei]
```

### Stufenklage § 254 ZPO

```
[Landgericht / Amtsgericht]
Abteilung: [Kammer]

Klage

Kläger: [Name, Adresse] — Pflichtteilsberechtigter
Beklagte: [Namen, Adressen] — Erben

wegen: Pflichtteil (Stufenklage § 254 ZPO)

I. AUSKUNFTSSTUFE
   Die Beklagten werden als Gesamtschuldner verurteilt,
   durch Vorlage eines notariellen Nachlassverzeichnisses
   Auskunft über den Bestand des Nachlasses nach
   [Erblasser] zum Todestag [Datum] zu erteilen,
   einschließlich aller Schenkungen der letzten zehn Jahre
   nach § 2325 BGB.

II. VERSICHERUNGSSTUFE
   Die Beklagten werden als Gesamtschuldner verurteilt,
   die Richtigkeit des vorgelegten Verzeichnisses
   an Eides statt zu versichern.

III. ZAHLUNGSSTUFE
   Die Beklagten werden als Gesamtschuldner verurteilt,
   an den Kläger den sich aus der Auskunft ergebenden
   Pflichtteilsanspruch nebst Zinsen in Höhe von fünf
   Prozentpunkten über dem Basiszinssatz ab
   Klagezustellung zu zahlen.

IV. STREITWERT AUSKUNFTSSTUFE
   25 % des voraussichtlichen Hauptanspruchs.
   Vorläufiger Streitwert: EUR [Betrag].
```

### Direktanspruch gegen Beschenkte § 2329 BGB

```
An [Beschenkter]
[Adresse]

Pflichtteilsergänzungsanspruch nach § 2329 BGB

Sehr geehrte Damen und Herren,

unser Mandant ist Pflichtteilsberechtigter nach dem
am [Datum] verstorbenen [Erblasser].

Der Erblasser hat Ihnen am [Datum] folgende Schenkung
gemacht: [Beschreibung, Wert].

Der Nachlass reicht zur Erfüllung des Pflichtteilsergänzungs-
anspruchs unseres Mandanten nicht aus. Nach § 2329 BGB
kann unser Mandant von Ihnen als Beschenktem Ergänzung
bis zum Wert der Schenkung verlangen.

Betrag: EUR [Pflichtteilsergänzungsanspruch], begrenzt auf
Schenkungswert EUR [Betrag].

Wir fordern Sie auf, bis [Datum] zu zahlen.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]


## Beweislast

| Partei | Beweislastgegenstand | Beweismittel |
|--------|---------------------|--------------|
| Pflichtteilsberechtigter | Berechtigung | Geburtsurkunde, Heiratsurkunde, ggf. Adoptionsurkunde |
| Pflichtteilsberechtigter | Enterbung oder Unterbedachtung | Testament, Erbschein |
| Pflichtteilsberechtigter | Schenkungen § 2325 BGB | Notarverträge, Kontobewegungen, Grundbuchauszüge |
| Erbe | Anrechnungsbestimmung § 2315 BGB | Schriftliche Vereinbarung mit Anrechnungsvorbehalt |
| Erbe | Pflichtteilsverzicht § 2346 BGB | Notarielle Urkunde |
| Erbe | Vollständigkeit und Richtigkeit Bestandsverzeichnis | Eidesstattliche Versicherung Stufe 2 |

## Fristen

| Frist | Auslöser | Dauer | Folge |
|-------|---------|-------|-------|
| Auskunftsanforderung | Möglichst bald nach Erbfall | Praxis: 4 Wochen setzen | Bei Ablehnung: Stufenklage |
| Verjährung Pflichtteil § 2332 BGB | Kenntnis von Erbfall + Verfügung | 3 Jahre ab Jahresende | Anspruchsverlust |
| Absolute Verjährung | Erbfall | 30 Jahre § 199 Abs. 3a BGB | Anspruchsverlust |
| Direktanspruch § 2329 BGB | Schenkungsdatum | 3 Jahre ab Kenntnis | Verjährung gegen Beschenkten |

## Gegenargumente und Reaktion

| Gegenargument Erbe | Reaktion |
|-------------------|---------|
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Nachlass wertlos, kein Pflichtteil" | Ergänzungsanspruch gegen Beschenkte § 2329 BGB; Nachlasswert ≠ Ergänzungsbasis |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Privatverzeichnis reicht" | § 2314 Abs. 1 Satz 3 BGB: auf Verlangen notarielles Verzeichnis; kein Ermessen |

## Streitwert und Kosten

**Streitwert Auskunftsstufe:** 25 % des voraussichtlichen Hauptanspruchs (Praxis der meisten Gerichte)

**Streitwert Zahlungsstufe:** Bezifferter Pflichtteilsanspruch

**Gerichtsgebühren Beispiel EUR 50.000:**
- Auskunftsstufe EUR 12.500 → GKG 3.0 Gebühr ca. EUR 618
- Zahlungsstufe EUR 50.000 → GKG ca. EUR 1.638
- RA-Gebühren: je Partei ca. EUR 3.500–5.500

**SV-Gutachten:** Auf Nachlasskosten § 2314 Abs. 2 BGB — typisch EUR 2.000–6.000 je Immobilie

## Strategische Empfehlung

| Strategie | Empfehlung | Begründung |
|-----------|-----------|------------|
| Verjährungssicherung | Auskunftsschreiben noch vor Ablauf von 2.5 Jahren nach Erbfall | Verjährung droht; Stufenklage hemmt § 204 BGB |
| Notarielles Verzeichnis | Konsequent fordern | Beweiskraft höher; Erbe haftet für Vollständigkeit |
| SV direkt benennen | Bereits im Auskunftsschreiben | Verhindert Verzögerung durch Erben |
| Schenkungsrecherche | Kontoauszüge 10+ Jahre rückwärts | Verschleierte Schenkungen häufig |
| Direktanspruch § 2329 | Beschenkte frühzeitig in Haftung nehmen | Schutz bei Nachlass-Insolvenz |

## Anschluss-Skills

- `pflichtteil-berechnen` — vollständiges Berechnungsraster mit allen Schritten
- `nachlassinsolvenz-erbenhaftung-begrenzen` — wenn Nachlass überschuldet
- `fachanwalt-erbrecht-testamentsvollstreckung` — TV-Auskunftspflicht § 2218 BGB

## Quellen

- BGB §§ 2303–2332, 2314, 2325, 2329, 2332
- ZPO § 254
- BGH, Urteil vom 12.03.2025 - IV ZR 88/24 (Pflichtteilsanspruch nichteheliches Kind; Verjährung): dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=12.03.2025&Aktenzeichen=IV+ZR+88/24
- BGH, Urteil vom 02.07.2025 - IV ZR 93/24 (Zuwendung an Hausarzt; Berufsordnung kein § 134 BGB-Verbot): bundesgerichtshof.de Pressemitteilung 2025/2025122.html
- Weitere Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle (bundesgerichtshof.de, dejure.org, openjur.de) mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Stand: 05/2026

---

## Skill: `fachanwalt-erbrecht-pflichtteilsergaenzung-2325`

_Pflichtteilsergaenzungsanspruch nach § 2325 BGB berechnen wenn Erblasser Schenkungen gemacht hat. § 2325 BGB Pflichtteilsergaenzung § 2329 BGB. Prüfraster: Schenkung innerhalb 10 Jahre Abschmelzung Wertbestimmung Auskunftsanspruch Verjährung. Output: Ergaenzungsberechnung Klageentwurf. Abgrenzung: nicht für einfachen Pflichtteilsanspruch (fachanwalt-erbrecht-pflichtteilsberechnung)._

# Pflichtteilsergänzungsanspruch § 2325 BGB

## Zweck

Mandate von Pflichtteilsberechtigten mit Schenkungs-Verdacht — Ermittlung, Berechnung, Klage.

## 1) Eingangs-Abfrage

1. Erbfall-Datum und Pflichtteilsberechtigung?
2. Bekannte Schenkungen (Immobilie, Konto-Verfügungen, Wertgegenstände)?
3. Ehegatten- oder Verwandten-Schenkungen?
4. Schenkungs-Datum (vs. 10-Jahres-Frist)?
5. Schenker-Behaltungs-Rechte (Niessbrauch, Wohnrecht)?

## 2) Anspruchsgrundlagen

### § 2325 BGB

Pflichtteilsberechtigter erhaelt ergänzenden Pflichtteil aus Schenkungen, die Erblasser **vor dem Erbfall** vorgenommen hat.

### 10-Jahres-Frist § 2325 III BGB

- **Abschmelzung 10 % pro Jahr** seit Schenkung
- Im Jahr 1 nach Schenkung: 100 %
- Im Jahr 5: 50 %
- Im Jahr 10: 0 %
- **Ausnahme Ehegatten-Schenkung**: Frist beginnt erst mit Auflösung der Ehe (Tod, Scheidung)

### Bei Niessbrauch / Wohnrecht

- Etablierte BGH-Linie (Live-Verifikation vor Verwendung): Bei vorbehaltenem Nießbrauch verzichtet der Erblasser nicht auf den "Genuss" des verschenkten Gegenstandes; die 10-Jahres-Frist des § 2325 Abs. 3 BGB beginnt erst mit Wegfall des Nutzungsvorbehalts (vgl. BGH-Rechtsprechung seit IV ZR 132/93 vom 27.04.1994). Für Wohnungsrechte ist eine einzelfallbezogene "Genussverzicht"-Prüfung erforderlich (vgl. BGH IV ZR 474/15 — Quelle vor Verwendung verifizieren).
- Praktisch: Schenkung mit Nießbrauch oder umfassendem Wohnrecht führt häufig dazu, dass die Abschmelzungsfrist nicht oder erst nach Tod des Nutzungsberechtigten anläuft.
- Live-Prüfung: Aktuelle BGH-Rechtsprechung zur Wohnrechts-/Nießbrauchsfrage auf bundesgerichtshof.de und dejure.org verifizieren.

## 3) Berechnung

### Schritt 1 — Pflichtteilsquote

- 1/2 des gesetzlichen Erbteils
- Bei Kindern + Ehegatten-Gesetzliche: Quote berechnen

### Schritt 2 — Nachlass-Wert + Schenkungs-Wert

```
Brutto-Nachlass + Schenkungs-Werte (mit Abschmelzung) = fiktiver Nachlass
Pflichtteil = Pflichtteilsquote × fiktiver Nachlass
Pflichtteilsergaenzung = Pflichtteil aus fiktivem Nachlass - Pflichtteil aus realem Nachlass
```

### Schritt 3 — Niederstwertprinzip § 2325 II BGB

- Schenkungs-Wert: **niedrigster** der beiden:
  - Wert zum Schenkungs-Zeitpunkt (mit Indexierung)
  - Wert zum Erbfalls-Zeitpunkt
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 4) Beispiel

- Vater verschenkt 2018 ein Haus an Tochter, Wert 500 K
- 2024 verstirbt, Sohn ist Pflichtteilsberechtigt
- 6 Jahre seit Schenkung = 40 % Abschmelzung = 60 % anrechenbar = 300 K
- Sohn-Pflichtteilsquote 1/4 (bei Halbgeschwistern und ZGW-Ehegattin)
- Pflichtteilsergänzung 1/4 × 300 K = 75 K

## 5) Auskunftsanspruch § 2314 BGB + Stufenklage § 254 ZPO

### Auskunft

- Pflichtteilsberechtigter kann Auskunft über Schenkungen verlangen
- Nachlass-Verzeichnis durch Erben
- Bei Streit: notarielles Verzeichnis § 2314 I 3 BGB

### Stufenklage

- Stufe 1: Auskunft (Bestand Nachlass + Schenkungen)
- Stufe 2: ggf. eidesstattliche Versicherung
- Stufe 3: Zahlung Pflichtteils-(Ergänzungs-)Betrag

## 6) Workflow

### Phase 1 — Recherche

- Grundbuch-Einsicht (Schenkungs-Eintragungen)
- Kontoausgabe Erblasser (Vermögens-Bewegungen)
- Zeugen-Befragung (Wertgegenstände, Bargeldgaben)
- Niessbrauch-Prüfung

### Phase 2 — Auskunftsverlangen

- Schriftlich an Erben
- 6-Wochen-Frist
- Bei Schweigen: Stufenklage

### Phase 3 — Berechnung + Klage

- Sachverständiger für Immobilien-Bewertung
- Abschmelzungs-Tabelle
- Niederstwertprinzip korrekt anwenden

## 7) Verjaehrung

- **3 Jahre** ab Kenntnis des Erbfalls und der Schenkung
- Hoechstens 30 Jahre ab Erbfall
- Verlust durch Verschwiegenheit-Klauseln: Vorsicht bei Erbverzichtsverträgen

## 8) Typische Fehler

1. **10-Jahres-Frist falsch berechnet** bei Wohnrecht/Niessbrauch
2. **Ehegatten-Schenkungen übersehen** (Frist laueft erst nach Tod)
3. **Niederstwertprinzip ignoriert** (Inflations-Bereinigung)
4. **Auskunftsanspruch versäumt** -> Stufenklage gehindert
5. **Sachverständige-Auswahl ungünstig** (zu hohe / niedrige Werte)

## 9) BGH-Linien und aktuelle Rechtsprechung

**Verifizierte Entscheidung 2025 (Live-Verifikation vor Verwendung):**

- BGH, Urteil vom 12.03.2025 - IV ZR 88/24: Für die Entstehung des Pflichtteilsanspruchs nach § 199 Abs. 1 Nr. 1 BGB ist § 2317 Abs. 1 BGB auch dann maßgebend, wenn der Berechtigte zum Zeitpunkt des Erbfalls aufgrund der gesetzlichen Ausübungssperre in § 1600d Abs. 5 BGB an einer erfolgreichen Anspruchsdurchsetzung gehindert ist. Für den Pflichtteilsanspruch des nichtehelichen Kindes gegenüber dem Vater ist Kenntnis von der wirksamen Anerkennung oder rechtskräftigen Feststellung der Vaterschaft erforderlich. Quelle: bundesgerichtshof.de / dejure.org.

Weitere Entscheidungen nicht aus Modellwissen zitieren; vor Ausgabe über bundesgerichtshof.de, dejure.org oder openjur.de verifizieren.

## Anschluss

- `fachanwalt-erbrecht-erbschaftsausschlagung` — bei Pflichtteilsantritts-Frage
- `fachanwalt-erbrecht-testamentsvollstreckung` — bei Konflikt-TV
- `pflichtteil-berechnen` — Berechnungs-Hilfe

---

## Skill: `fachanwalt-erbrecht-erbschaftsausschlagung`

_Erbschaftsausschlagung erlaeutern und Erklärung formulieren wenn Erbe ueberschuldet ist oder sonstige Gründe vorliegen. §§ 1942 1944 1945 BGB Ausschlagung. Prüfraster: Ausschlagungsfrist sechs Wochen drei Monate Ausland Empfaenger Nachlassgericht Form Anfechtung. Output: Ausschlagungserklärung Antragsentwurf. Abgrenzung: nicht für Pflichtteilsausschlagung oder Erbverzicht._

# Erbschaftsausschlagung

## Zweck

Beratung bei Frage "Erbe annehmen oder ausschlagen" — Frist, Form, Strategien.

## 1) Eingangs-Abfrage

1. Erbfall-Datum und Kenntnis vom Erbfall?
2. Erbe gesetzlich oder testamentarisch?
3. Auslandsbezug Erblasser/Erbe?
4. Bekannte Nachlasswerte (Brutto)?
5. Bekannte Erbschulden?
6. Vorerbschaft / Nacherbschaft?
7. Pflichtteilsberechtigung anderer?

## 2) Frist § 1944 BGB

| Konstellation | Frist |
|---|---|
| Inland | **6 Wochen** nach Kenntnis von Erbfall und Berufungs-Grund |
| Auslands-Wohnsitz Erblasser oder Erbe | **6 Monate** |
| Nicht bekannt Erbfall | Frist beginnt mit Kenntnis |

### Versäumnis

- Frist abgelaufen ohne Ausschlagung = **Erbe angenommen**
- Anfechtung Annahme über § 1954 BGB schwer (Irrtum)

## 3) Form § 1945 BGB

- **Notarielle Beurkundung** oder
- **Erklärung gegenüber Nachlassgericht** (Amtsgericht Erblassers letzter Wohnsitz)
- Beide Wege gleichwertig

### Kosten

- Notar nach GNotKG (typisch 60-200 EUR)
- Nachlassgericht ohne Gebuehr (nur Aktendurchsicht)

## 4) Folgen der Ausschlagung

### Rueckwirkung § 1953 BGB

- Erbe gilt als nie eingetreten
- Nächste Erbordnung tritt ein
- Bei Kind ausschlägt: Enkelkind kann erben (Repraesentations-Prinzip)

### Pflichtteils-Anspruch

- Bei testamentarischer Erbeinsetzung und Ausschlagung: Pflichtteil bleibt
- Erbersatzantritt durch Pflichtteils-Berechtigten

### Bei Sozialhilfe-Beziehern

- **Sozialhilfe-Träger kann Ausschlagung anfechten** § 138 BGB (Sittenwidrigkeit) bei drohender Sozialhilfe-Belastung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 5) Strategische Erwaegungen

### Pro Ausschlagung

- Nachlass-Schulden höher als Aktiva
- Komplexe Auslands-Nachlaesse (Erbschein-Aufwand)
- Bevorzugung nächster Generation (Nachfolge-Planung)
- Vermeidung Verfahrenskosten

### Contra Ausschlagung

- Nachlass-Wert unklar (Sachverständiger?)
- Pflichtteils-Ausnahme möglich
- Bei Vor-/Nacherbschaft: Pflicht-Verzicht ungewollt

## 6) Anfechtung der Ausschlagung § 1954 BGB

### Voraussetzungen

- Irrtum über Inhalt oder Erklärungsbestand
- Irrtum über Eigenschaft (z.B. Nachlasswert)

### Frist

- 6 Wochen ab Kenntnis des Irrtums

### Form

- Wie Ausschlagung: notariell oder Nachlassgericht

### Praxis

- Schwer durchzusetzen — Beweislast
- Beispiel: Nachlasswert wesentlich höher als angenommen, Pflichtangaben zur Inventarisierung

## 7) Workflow

### Schritt 1 — Nachlass-Analyse

- Erblasser-Konten-Recherche
- Grundbuch-Prüfung
- Schulden-Erforschung (Mahnungen, Vollstreckung)
- Versicherungs- und Versorgungs-Ansprueche

### Schritt 2 — Bilanz

- Aktiva vs. Passiva
- Erbschaftssteuer-Anfall prüfen
- Pflichtteils-Risiken

### Schritt 3 — Entscheidung

- Annehmen mit Nachlassverwaltung (§ 1981 BGB)
- Ausschlagen
- Inventarerrichtung § 1993 BGB (Schutz gegen Haftung)

### Schritt 4 — Ausführung

- Notar oder Nachlassgericht
- Schriftliche Bestätigung
- Mitteilung an Mit-Erben

## 8) Auslands-Bezug

### EU-ErbVO (VO (EU) 650/2012)

- Gilt seit 17.8.2015
- Anwendungs-Wahl Erblasser (gewoehnlicher Aufenthalt vs. Heimat-Recht)
- Bei Erblasser im Ausland: oft 6-Monats-Frist § 1944 III BGB

### Erbschein vs. Europaeisches Nachlasszeugnis

- Erbschein national
- ENZ EU-weit

## 9) Typische Fehler

1. **Frist versäumt** durch fehlende Kenntnis-Berechnung
2. **Konkludente Annahme** durch Vermögens-Verfügung (Konten-Abhebung, Wohnungsverkauf)
3. **Auslandsbezug übersehen** (6 Monate Frist!)
4. **Anfechtungs-Frist 6 Wochen verpasst**
5. **Sozialhilfe-Folgen ignoriert** — Anfechtungs-Risiko des Trägers
6. **Mit-Erben nicht informiert** — Querverfahren

## 10) BGH-Linien und aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Anschluss

- `fachanwalt-erbrecht-pflichtteilsergaenzung-2325` — bei Pflichtteilsfrage
- `fachanwalt-erbrecht-testamentsvollstreckung` — bei TV
- `fachanwalt-erbrecht-testamentsentwurf` — bei Nachfolge-Planung

<!-- AUDIT 27.05.2026 bundle_021
-->

---

## Skill: `fachanwalt-erbrecht-testamentsentwurf`

_Testament oder Erbvertrag entwerfen wenn Mandant Nachlassplanung vornehmen moechte. §§ 2229 2231 2247 BGB Testament §§ 2274 ff. BGB Erbvertrag. Prüfraster: Testierfähigkeit Form Erbeinsetung Vermaechtnisse Pflichtteilsreduzierung Testamentsvollstreckung Erbvertragsbindung. Output: Testamentsentwurf oder Erbvertragsentwurf. Abgrenzung: nicht für Pflichtteilsberechnungen._

# Testamentsentwurf

## Aktuelle Rechtsprechung (Stand 05/2026, Live-Verifikation zwingend)

- BGH, Urteil vom 02.07.2025 - IV ZR 93/24: Eine Zuwendung von Todes wegen an den behandelnden Arzt des Erblassers ist nicht deshalb unwirksam, weil sie gegen § 32 Abs. 1 S. 1 (M)BO-Ä verstößt. Berufsordnung ist kein Verbotsgesetz i.S.d. § 134 BGB; Testierfreiheit (Art. 14 GG) überwiegt. Sittenwidrigkeit (§ 138 BGB) bleibt Einzelfallprüfung. — Relevanz: Strukturanaloge Konstellationen bei Zuwendungen an pflegende Personen, Heimleitung, Berufsbetreuer (vgl. § 30 BtOG; OLG Nürnberg-Linie). Quelle: bundesgerichtshof.de PM 2025/2025122.html.
- Weitere Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über bundesgerichtshof.de, dejure.org oder openjur.de mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Kaltstart-Rückfragen

1. Familienstand des Erblassers, Anzahl Kinder, Vorehen, Patchwork? Wer sind die gesetzlichen Erben?
2. Vermögensumfang grob: Immobilien, Unternehmen, Bankvermögen, Lebensversicherungen mit Bezugsrecht?
3. Ehevertrag oder Güterstand? Gibt es bereits ein früheres Testament oder einen Erbvertrag (Bindungswirkung)?
4. Welche Zielsetzung — Versorgung des Ehegatten, Unternehmensfortführung, Behinderung eines Kindes, Pflichtteilsreduzierung, steueroptimierte Übertragung?
5. Sollen Vermächtnisse, Teilungsanordnungen, Auflagen oder Testamentsvollstreckung vorgesehen werden?

## Anspruchsgrundlagen und Normen

- Testierfähigkeit ab 16 Jahren (§ 2229 Abs. 1 BGB), eigenhändiges Testament erst ab 18 (§ 2247 BGB), eigenhändig vollständig handschriftlich mit Ort, Datum, Unterschrift.
- Öffentliches Testament beim Notar (§§ 2231 Nr. 1, 2232 BGB) — beweissicherer, kein Erbscheinerfordernis bei Grundbuchberichtigung (§ 35 GBO).
- Gemeinschaftliches Testament nur unter Ehegatten und eingetragenen Lebenspartnern (§ 2265 BGB), wechselbezügliche Verfügungen § 2270 BGB binden den Überlebenden nach dem ersten Erbfall.
- Berliner Testament § 2269 BGB — gegenseitige Erbeinsetzung mit Schlusserben.
- Erbvertrag §§ 2274 ff. BGB — beidseitige Bindung, nur notariell.
- Pflichtteilsverzicht (§ 2346 Abs. 2 BGB) — nur notariell § 2348 BGB.
- Testamentsvollstreckung §§ 2197–2228 BGB — Verwaltungs-, Abwicklungs- oder Dauervollstreckung.
- Internationales Erbrecht: bei grenzüberschreitenden Bezügen Rechtswahl nach Art. 22 EU-ErbVO (650/2012) möglich.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Gestaltungsregeln

| Klausel | Funktion | Hinweis |
|---|---|---|
| Erbeinsetzung Quote | Wer wird Erbe (§ 2087 Abs. 1 BGB) | "als Alleinerbe" oder "zu Quote x" — keine Einzelgegenstände ohne Quotenangabe |
| Vermächtnis | Einzelgegenstand schuldrechtlich (§ 1939 BGB) | Vermächtnisnehmer ist nicht Erbe |
| Teilungsanordnung § 2048 BGB | Verteilung unter Erben | Berührt nicht die Quote |
| Pflichtteilsstrafklausel | Wer Pflichtteil verlangt verliert Schlusserbenstellung | Üblich im Berliner Testament |
| Wiederverheiratungsklausel | Bedingte Verfügung bei Wiederheirat | Vorsicht — keine sittenwidrige Behinderung |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Schreibvorlage eigenhändiges Berliner Testament

```
Gemeinschaftliches Testament

Wir Eheleute [Name 1] geboren am [Datum 1] und [Name 2] geboren am
[Datum 2] beide wohnhaft in [Ort] errichten hiermit folgendes
gemeinschaftliches Testament.

§ 1 Gegenseitige Erbeinsetzung
Wir setzen uns gegenseitig zu alleinigen und unbeschraenkten Erben ein.

§ 2 Schlusserben
Schlusserben des Laengstlebenden werden unsere gemeinsamen Kinder
[Name a] und [Name b] zu gleichen Teilen.

§ 3 Pflichtteilsstrafklausel
Macht ein Kind nach dem Tod des Erstversterbenden seinen Pflichtteil
geltend so ist es auch nach dem Tod des Laengstlebenden auf den
Pflichtteil beschraenkt.

§ 4 Wechselbezueglichkeit
Saemtliche Verfuegungen sind wechselbezueglich § 2270 BGB.

[Ort] [Datum]
[Eigenhaendige Unterschrift Ehegatte 1]
[Eigenhaendige Unterschrift Ehegatte 2]
```

## Übergabe

- Bei Vermögen über Freibeträgen (Ehegatte 500 TEUR Kinder 400 TEUR § 16 ErbStG) Hinweis auf Schenkungs-/Erbschaftsteuerberatung.
- Bei Unternehmensvermögen Nachfolgeregelung gesondert prüfen (Begünstigungen §§ 13a, 13b ErbStG).
- Empfehlung Hinterlegung beim Amtsgericht (§ 2248 BGB) — Hinterlegungsgebühr nach GNotKG (KostO ist durch das 2. KostRMoG vom 23.07.2013, BGBl. I S. 2586, mit Wirkung zum 01.08.2013 außer Kraft getreten).
- Anschluss-Skill bei späterem Erbfall: `fachanwalt-erbrecht-erbschein-antrag`.

---

## Skill: `fachanwalt-erbrecht-verhandlung-mediation-erbengemeinschaft`

_Streit in der Erbengemeinschaft durch Verhandlung oder Mediation lösen. §§ 2032 2042 2047 BGB Erbengemeinschaft. Prüfraster: Erbteile Nachlassbestand Verwaltungsmassnahmen Teilungsklage Auseinandersetzung Erbauseinandersetzungsvertrag. Output: Verhandlungsstrategie Mediationsagenda Auseinandersetzungsvertrag. Abgrenzung: nicht für gerichtliche Teilungsklage._

# Mediation / Vergleich bei Erbengemeinschaft

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Zweck

Erbschafts-Streit ist überwiegend Familien-/Beziehungs-Streit; harte Klage zerstört oft die Beziehungen dauerhaft. Mediation und außergerichtliche Vergleichsverhandlungen sind erbrechtsspezifisch zentral — mit Notar-Vermittlung § 363 FamFG, Schiedsgutachten bei Bewertungs-Streit.

## Eingaben

- Mandantenrolle (Erbe, Pflichtteilsberechtigte, Vermächtnisnehmerin, Testamentsvollstrecker)
- Erbengemeinschafts-Größe (2 bis n Personen)
- Streitgegenstand (Quote, Bewertung Immobilie, Schenkungs-Anrechnung § 2050 BGB, Ausgleichung)
- Familien-Konstellation (Geschwister, Stiefkinder, neue Ehegatten)
- Bestehende Korrespondenz / Konflikt-Stand

## Rechtlicher Rahmen

- **§§ 2032-2057 BGB** — Erbengemeinschaft, Auseinandersetzung
- **§ 2042 BGB** — Auseinandersetzungs-Anspruch
- **§ 2046 BGB** — Schulden vor Auseinandersetzung
- **§ 2050 BGB** — Ausgleichung Schenkung zu Lebzeiten
- **§§ 2314, 2325 BGB** — Pflichtteils-Auskunft + -Ergänzung
- **§ 363 FamFG** — Notarielle Vermittlung Erbauseinandersetzung
- **§§ 1029 ff. ZPO** — Schiedsgerichts-Verfahren
- **MediationsG** — Mediation als Verfahren

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## ADR-Pfade

### Pfad 1 — Familien-Mediation

- DGFM-Erbrechts-Mediator/in
- Kostengünstig (50-150 EUR/h, geteilt)
- Vertraulichkeit
- Vorteil: Familien-Beziehungs-Erhalt
- Resultat: schriftliche Auseinandersetzungs-Vereinbarung

### Pfad 2 — Notarielle Vermittlung § 363 FamFG

- Antrag bei Notar
- Verhandlungs-Termin mit allen Erben
- Notar entwirft Auseinandersetzungs-Vertrag
- Auseinandersetzungsplan rechtlich bindend nach Genehmigung Nachlassgericht
- Vorteil: direkt vollstreckbar (notarielle Urkunde)

### Pfad 3 — Schiedsgutachten Bewertung

- Streit nur über Wert (Immobilie, Unternehmen, Kunstsammlung)
- Sachverständigen-Schiedsgutachten § 317-319 BGB
- Beide Erben einigen sich auf Gutachter
- Spruch bindend (außer "offenbar unbillig")

### Pfad 4 — Klage Nachlassgericht / Familiengericht

- Bei Scheitern aller ADR
- AG Nachlassgericht / Familiengericht
- Wertgutachten gerichtsbestellt
- Langwierig (1-3 Jahre), teuer, beziehungsschädlich

## Workflow

### Phase 1 — Sachverhalts-Klärung

- Nachlass-Inventur (Bewertung Immobilien, Konten, Krypto, Unternehmen)
- Schenkungs-Recherche letzte 10 Jahre (§ 2325 BGB)
- Pflichtteilsberechtigung prüfen
- Familien-Konstellation kartieren

### Phase 2 — Vorgerichtliche Verhandlungs-Phase

- Schreiben an Miterben mit Lösungsangebot
- Bewertungs-Vorschlag (Verkehrswert + Pauschal-Abzug)
- Mediations-Vorschlag

### Phase 3 — ADR-Wahl

- Bei Vertrauensbasis: Mediation
- Bei Bewertungs-Streit: Schiedsgutachten
- Bei harter Auseinandersetzung: § 363 FamFG-Notar

### Phase 4 — Vergleichs-Vertrag

- Notarielle Beurkundung bei Grundstücken § 311b BGB
- Inhalte: Wertaufteilung, Verkauf vs. Übernahme, Ausgleichungs-Zahlungen
- Steuer-Klausel (ErbSt-Pflicht jeweils)
- Vollstreckbarkeits-Klausel

### Phase 5 — Umsetzung

- Grundbuch-Berichtigung
- Konten-Aufteilung
- ErbSt-Erklärung jeder Erbe getrennt

## Strategie und Taktik

- **Bewertungs-Stichtag**: Todesstichtag oder Auseinandersetzungs-Stichtag — verhandelbar
- **Verkehrswert vs. Substanzwert**: typisch 70-90 % des Verkehrswerts bei Substanz
- **Wohnrecht-Bewertung**: Kapitalisierung mit Sterbetafel
- **Krypto-Wallet**: Sonderfall (siehe `fachanwalt-erbrecht-krypto-wallet-nachlass-multisig`)
- **Schenkungs-Anrechnung**: 10-%-Abschmelzung pro Jahr § 2325 III BGB
- **Bei Eskalation**: Pflichtteils-Auskunft § 2314 BGB als Druckmittel
- **Vergleich + Stilllegung**: alle Erben unterschreiben "saemtliche Ansprueche erledigt"

## Querverweise

- `fachanwalt-erbrecht-orientierung` — Triage
- `fachanwalt-erbrecht-pflichtteilsergaenzung-2325` — Vertiefung
- `fachanwalt-erbrecht-erbschaftsausschlagung` — Alternative
- `fachanwalt-erbrecht-krypto-wallet-nachlass-multisig` — Sonderfall

## Quellen und Updates

Stand: 05/2026. § 363 FamFG, MediationsG. BGH-Linien stabil. Bei ErbStG-Reform aktualisieren.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

