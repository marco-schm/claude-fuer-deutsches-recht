# Megaprompt: fachanwalt-arbeitsrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 119 Skills (gekuerzt fuer Chat-Fenster) des Plugins `fachanwalt-arbeitsrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Anwalts-Dashboard Fachanwalt Arbeitsrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Z…
2. **fachanwalt-arbeitsrecht-orientierung** — Orientierung im Individualarbeitsrecht und kollektiven Arbeitsrecht für Mandate und Fachanwaltschaft nach § 10 FAO. Anwe…
3. **orientierung-mandat-fachanwaltschaft** — Orientierung im Individualarbeitsrecht und kollektiven Arbeitsrecht für Mandate und Fachanwaltschaft nach § 10 FAO: Anwe…
4. **erstgespraech-mandatsannahme** — Strukturierter Erstgespraechsleitfaden für Individual- und kollektives Arbeitsrecht: Erfassung der Konstellation, Konfli…
5. **erstpruefung-und-mandatsziel** — Fachanwalt Erstprüfung und Mandatsziel: systematische Erstaufnahme im arbeitsrechtlichen Mandat, Rollenklärung, Zielform…
6. **fachanwalt-arbeitsrecht-betriebsratsanhoerung** — Betriebsratsanhoerung nach § 102 BetrVG vor jeder Kündigung. Anwendungsfall Kündigung soll ausgesprochen werden und BR-A…
7. **fachanwalt-arbeitsrecht-aufhebungsvertrag-sperrzeit** — Aufhebungsvertrag mit Sperrzeit-Vermeidung nach § 159 SGB III bei Eigeninitiative oder drohender Kündigung. Anwendungsfa…
8. **fachanwalt-arbeitsrecht-verhandlung-guete-abfindung-arbg** — Gueteverhandlung im Arbeitsgerichtsverfahren nach § 54 ArbGG mit Auflösungsantrag und Abfindungsstrategie. Anwendungsfal…

---

## Skill: `einstieg-routing`

_Anwalts-Dashboard Fachanwalt Arbeitsrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt bleibt im Driver Seat._

# Anwalts-Dashboard Fachanwalt Arbeitsrecht

> Kündigung, Aufhebungsvertrag, Befristung, Betriebsrat, Betriebsübergang — sieben Eilfristen, ein Klagestrang.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 4 KSchG: 3 Wochen** ab Zugang Kündigung. Daneben § 626 II BGB (außerordentlich, 2 Wochen ab Kenntnis), § 15 IV AGG (2 Monate Geltendmachung), § 17 KSchG (Massenentlassungsanzeige), § 9 MuSchG, § 613a VI BGB (1 Monat Widerspruch). | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Kündigungsschutz §§ 1, 4, 7 KSchG · Lohn §§ 611a, 614, 615 BGB (Annahmeverzug) · Schadensersatz §§ 280 I, 823 BGB · AGG-Entschädigung §§ 7, 15 AGG · Betriebsübergang § 613a BGB. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Arbeitsgericht am Arbeitsort (§ 48 ArbGG, § 17 ZPO). Streitwert KSchG-Klage: 1/4 Bruttojahresgehalt (§ 42 II GKG). | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Kündigung mit laufender 3-Wochen-Frist: heute Klageschrift. 🟠 Aufhebungsvertrag mit Widerrufsoption: 14 Tage prüfen. 🟢 Lohnklage ohne Verfallsklausel.
- **Beweislage:** 🟠 Zugang der Kündigung trägt der Arbeitgeber (§ 130 BGB); Zustellungsnachweis sichern. 🔴 Bei mündlicher Kündigung: Zeugen organisieren.
- **Wirtschaftlich:** 🔴 Lohnverlust > 3 Monate + Verlust SV-Pflicht: Eilantrag Weiterbeschäftigung (§ 102 V BetrVG) prüfen. 🟠 Abfindung ≈ 0,5 Monatsgehälter pro BJ als Verhandlungsstart.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Kündigung erhalten — Schutzklage prüfen** | `ar-kuendigungspruefung-workflow` | Klageschrift mit Anträgen, Streitwertangabe, Antrag auf vorläufige Weiterbeschäftigung |
| Aufhebungsvertrag angeboten | `ar-aufhebungsvertrag-praxis` | Risikomatrix, Abfindungs-Range, Sperrzeit § 159 SGB III |
| Befristung soll geprüft werden | `befristung-tzbfg` | Sachgrund- vs. sachgrundlose Befristung, Anschlussverbot § 14 II 2 TzBfG |
| Betriebsrats-Beteiligung streitig | `beteiligung-betriebsrat-102-betrvg` | Anhörungsfehler, Heilung, Folge der Unwirksamkeit |
| Betriebsübergang im Raum | `ar-betriebsuebergang-spezial` | Widerspruchsfrist § 613a VI BGB (1 Monat), Informationsanspruch |

## Norm-Radar (live verifizieren)

- **§ 4 KSchG** — 3-Wochen-Frist Kündigungsschutzklage
- **§ 626 BGB** — außerordentliche Kündigung, 2-Wochen-Frist Abs. 2
- **§ 1 KSchG** — Sozialwidrigkeit; KSchG-Anwendung ab 10 AN (Kleinbetrieb)
- **§§ 611a, 615 BGB** — Arbeitsvertrag, Annahmeverzug
- **§ 613a BGB** — Betriebsübergang; Widerspruchsrecht Abs. 6
- **§ 102 BetrVG** — Anhörung Betriebsrat; Folge der Unwirksamkeit

## Genau eine Rückfrage (nur wenn nötig)

> Liegt eine **Kündigung mit Zugangsdatum** vor — oder ist der Triggerpunkt ein anderer (Befristung, Lohn, Aufhebungsvertrag, AGG)?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Kündigungsschutz § 1 KSchG; Sozialwidrigkeit** — BAG 2. Senat — *live verifizieren auf* `bundesarbeitsgericht.de`
- **Betriebsübergang § 613a BGB; Identitätswahrung** — BAG 8. Senat (Spijkers-/Süzen-Linie) — *live verifizieren auf* `bundesarbeitsgericht.de + EuGH curia.europa.eu`
- **Befristung ohne Sachgrund; Vorbeschäftigung § 14 II 2 TzBfG** — BAG 7. Senat; BVerfG 1. Senat — *live verifizieren auf* `bundesarbeitsgericht.de + bundesverfassungsgericht.de`
- **AGG-Entschädigung § 15 II; 2-Monats-Frist** — BAG 8. Senat — *live verifizieren auf* `bundesarbeitsgericht.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

## Aktuelle BAG-Linie 2025/2026 (live verifizieren vor Schriftsatzverwendung)

Drei aktuelle Leitentscheidungen, die über das Arbeitsrecht in den letzten zwoelf Monaten besonders weit ausstrahlen:

| Entscheidung | Tragende Aussage | Skill-Vertiefung |
| --- | --- | --- |
| **BAG, Urt. v. 23.10.2025 - 8 AZR 300/24** | **Equal Pay - Paarvergleich genuegt.** Eine einzige besser bezahlte Vergleichsperson des anderen Geschlechts mit gleicher oder gleichwertiger Arbeit reicht, um die Vermutung des $ 22 AGG auszuloesen. Der Arbeitgeber muss konkret darlegen, dass die Differenz ausschließlich auf objektiven, geschlechtsneutralen Gruenden beruht. Pauschale Hinweise auf Medianwerte, Durchschnittsbetrachtungen oder Verhandlungsgeschick reichen nicht. Art. 157 AEUV bekommt damit Schaerfe. | `bag-equal-pay-paarvergleich` (fachanwalt-arbeitsrecht) / `bag-equal-pay-paarvergleich-8azr30024` (arbeitsrecht) |
| **BAG, Urt. v. 03.06.2025 - 9 AZR 104/24** | **Kein Verzicht auf gesetzlichen Mindesturlaub.** Im bestehenden Arbeitsverhaeltnis können Arbeitnehmer:innen auf den gesetzlichen Mindesturlaub nicht wirksam verzichten - auch nicht durch gerichtlichen Vergleich. Gilt selbst dann, wenn die Beendigung bereits feststeht und absehbar ist, dass der Urlaub krankheitsbedingt nicht mehr genommen werden kann. Ausgleichs-/Erledigungs-/Abgeltungsklauseln müssen sauber zwischen gesetzlichem Mindesturlaub, vertraglichem Mehrurlaub und bereits entstandener Urlaubsabgeltung unterscheiden. | `bag-mindesturlaub-kein-verzicht` (fachanwalt-arbeitsrecht) / `bag-mindesturlaub-kein-verzicht-9azr10424` (arbeitsrecht) |
| **BAG, Urt. v. 25.03.2026 - 5 AZR 108/25** | **Pauschale Freistellungsklauseln in Arbeitsvertragsformularen unwirksam.** Eine formularmaessige Freistellungsklausel, die dem Arbeitgeber das einseitige Recht gibt, Beschäftigte nach Kuendigung unter Fortzahlung der Vergütung freizustellen, ist nach AGB-Kontrolle unwirksam, wenn sie Arbeitnehmer:innen unangemessen benachteiligt. Freistellung bleibt im konkreten Fall möglich - braucht aber einen tragfaehigen Grund (ueberwiegende schutzwuerdige Arbeitgeberinteressen). Die pauschale Vorratsklausel reicht nicht. | `bag-freistellungsklausel-unwirksam` (fachanwalt-arbeitsrecht) / `bag-freistellungsklausel-unwirksam-5azr10825` (arbeitsrecht) |

> Diese drei Aktenzeichen sind Sucheinstieg. Vor Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle (bundesarbeitsgericht.de, dejure.org) live verifizieren - Datum, Aktenzeichen, Randnummer, Fortgeltung. Spezial-Skills oben enthalten Prüfschemata, Klagebausteine und Verteidigungsmuster.

---

## Skill: `fachanwalt-arbeitsrecht-orientierung`

_Orientierung im Individualarbeitsrecht und kollektiven Arbeitsrecht für Mandate und Fachanwaltschaft nach § 10 FAO. Anwendungsfall Kanzlei will Arbeitsrechtsmandat beurteilen oder Anwalt bereitet sich auf Fachanwaltsprüfung vor. Normen BGB §§ 611a ff. KSchG BetrVG TVG BUrlG EFZG TzBfG AGG ArbGG. Prüfraster Individualarbeitsrecht Kollektivarbeitsrecht Diskriminierungsschutz Verfahren ArbGG LAG BAG verifizierbare Quellen. Output Rechtsgebietsuebersicht mit Normenhierarchie Pflichtliteratur und Mandatstriage-Hinweisen. Abgrenzung zu erstgespraech-mandatsannahme und mandat-triage-Skill._

# Fachanwalt für Arbeitsrecht — Orientierung

## FAO-Voraussetzungen (§ 10 FAO)

- Lehrgang 120 Stunden + drei Klausuren.
- 100 Fälle in den letzten drei Jahren aus dem Arbeitsrecht; davon mindestens 50 Mandate im Individualarbeitsrecht, mindestens 10 Mandate im Kollektivarbeitsrecht, mindestens 20 rechtsförmliche Verfahren.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Individualarbeitsrecht | BGB §§ 611a ff. (Arbeitsvertrag); KSchG (Kündigungsschutz); BUrlG (Urlaub); EFZG (Entgeltfortzahlung); TzBfG (Teilzeit und Befristung); NachwG (Nachweisgesetz, idF Aug. 2022); MuSchG; BEEG; ArbZG; ArbStättV |
| Kollektivarbeitsrecht | BetrVG (Betriebsverfassung); TVG (Tarifvertrag); MitbestG; DrittelbG; SprAuG |
| Diskriminierung | AGG (§§ 1, 7, 15) |
| Arbeitsschutz | ArbSchG; ArbStättV; ArbMedVV |
| Insolvenz | InsO §§ 113, 125 ff. |
| Verfahren | ArbGG (Arbeitsgerichtsgesetz) |
| Internationale Bezüge | Rom I-VO; AEntG; AÜG |

## Typische Mandate

- Kündigungsschutzklage (§ 4 KSchG).
- Aufhebungsvertrag (Verhandlung, Sozialplan).
- Befristungskontrollklage (§ 17 TzBfG).
- Sozialplan / Interessenausgleich nach § 112 BetrVG (Kollektivseite).
- Betriebsratsanhörung nach § 102 BetrVG.
- Zeugnisstreitigkeit (§ 109 GewO).
- AGG-Entschädigungsklage (§ 15 AGG).
- Lohn- und Gehaltsklage.
- Mobbing und Schadensersatzklage (§ 280 Abs. 1 BGB iVm Schutzpflicht § 241 Abs. 2 BGB).

## Fristen (Auswahl)

- **Kündigungsschutzklage** § 4 KSchG — drei Wochen ab Zugang der schriftlichen Kündigung.
- **Befristungskontrollklage** § 17 TzBfG — drei Wochen nach vereinbartem Ende.
- **AGG-Entschädigung** § 15 Abs. 4 AGG — schriftliche Geltendmachung binnen zwei Monaten; Klagefrist § 61b ArbGG drei Monate.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Anhörung des Betriebsrats** § 102 BetrVG — eine Woche bei ordentlicher, drei Tage bei außerordentlicher Kündigung.
- **Sozialplanverhandlungen** § 112 Abs. 2, 3 BetrVG — Einigungsstelle nach Scheitern.

## Hauptgerichte

- Arbeitsgericht (ArbG) — erste Instanz, Kammern.
- Landesarbeitsgericht (LAG) — Berufungsinstanz.
- Bundesarbeitsgericht (BAG) — Revisionsinstanz, Erfurt.
- BVerfG bei Grundrechtsfragen.
- EuGH bei unionsrechtlichen Fragen (Befristung, Arbeitszeit, Gleichbehandlung).

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- Arbeitsgemeinschaft Arbeitsrecht im DAV.

## Schnittstellen

- **`arbeitsrecht`** für operative Mandatsführung, Vorlagen.
- **`kanzlei-allgemein`** für Fristen und Versand.
- **`fachanwalt-sozialrecht`** bei Schnittstellen zur Arbeitslosenversicherung und Sperrzeit.
- **`fachanwalt-insolvenz-sanierungsrecht`** bei Betriebsübergang § 613a BGB und Insolvenz.

## Aktuelle Rechtsprechung - Ueberblick wichtiger Leitentscheidungen (Stand Mai 2026)

Folgende Leitentscheidungen sind im aktuellen Plugin-Stand mit offener Quelle (dejure.org / bundesarbeitsgericht.de) belegt:

- **BAG, 23.10.2025 - 8 AZR 300/24** (Paarvergleich Equal Pay): Ein einzelner Vergleichskollege des anderen Geschlechts genuegt zur Vermutung nach § 22 AGG. Siehe Skill `fachanwalt-arbeitsrecht-bag-equal-pay-paarvergleich`.
- **BAG, 03.06.2025 - 9 AZR 104/24** (kein Urlaubsverzicht durch Prozessvergleich): Mindesturlaub waehrend laufenden Arbeitsverhaeltnisses nicht disponibel. Siehe Skill `fachanwalt-arbeitsrecht-bag-mindesturlaub-kein-verzicht`.
- **BAG, 25.03.2026 - 5 AZR 108/25** (Freistellungsklausel unwirksam): Pauschale formularmaessige Freistellungsklausel verstoesst gegen § 307 BGB. Siehe Skill `fachanwalt-arbeitsrecht-bag-freistellungsklausel-unwirksam`.
- **BAG, 01.04.2026 - 6 AZR 152/22 und 6 AZR 157/22** (Massenentlassung): Fehlerhafte oder verfruehte Massenentlassungsanzeige fuehrt zur Unwirksamkeit aller Kuendigungen. Siehe Skill `fachanwalt-arbeitsrecht-massenentlassung-17-kschg`.
- **EuGH, 30.10.2025 - C-134/24 und C-402/24** (Massenentlassung): Keine Heilung fehlender oder verfruehter Anzeige nach Kuendigungsausspruch.
- **BAG, 20.02.2025 - 8 AZR 61/24** (DSGVO-Schadensersatz): "Stoergefuehl" allein begruendet keinen Anspruch nach Art. 82 DSGVO.
- **BAG, 18.06.2025 - 7 AZR 50/24** (Befristung Betriebsratsmitglieder): § 14 Abs. 2 TzBfG anwendbar; Schadensersatz auf Folgevertrag bei Mandatsbenachteiligung.
- **BAG, 22.09.2022 - 8 AZR 4/21** (NachweisG): Schadensersatz neben Bussgeld bei Pflichtverletzung des Arbeitgebers nach NachwG.
- **BAG, 13.09.2022 - 1 ABR 22/21** (Arbeitszeiterfassung): Pflicht des Arbeitgebers zur systematischen Arbeitszeiterfassung aus § 3 Abs. 2 Nr. 1 ArbSchG.

Vor Schriftsatzverwendung jeweils Volltext und ggf. neuere Rechtsprechung in offenen Quellen (dejure.org, openjur.de, bundesarbeitsgericht.de) verifizieren.

## Paragrafenkette Kernbereiche Individualarbeitsrecht

- § 611a BGB — Arbeitsvertrag
- § 626 BGB — Außerordentliche Kündigung
- §§ 1 ff. KSchG — Kündigungsschutz; § 4 KSchG — Klagefrist drei Wochen
- § 102 BetrVG — Betriebsratsanhörung
- §§ 1, 3 BUrlG — Urlaubsanspruch; § 7 Abs. 3 BUrlG — Verfall
- § 14 TzBfG — Befristung; § 17 TzBfG — Kontrollklage drei Wochen

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `orientierung-mandat-fachanwaltschaft`

_Orientierung im Individualarbeitsrecht und kollektiven Arbeitsrecht für Mandate und Fachanwaltschaft nach § 10 FAO: Anwendungsfall Kanzlei wi..._

# Orientierung im Individualarbeitsrecht und kollektiven Arbeitsrecht für Mandate und Fachanwaltschaft nach § 10 FAO


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung im Individualarbeitsrecht und kollektiven Arbeitsrecht für Mandate und Fachanwaltschaft nach § 10 FAO. Anwendungsfall Kanzlei will Arbeitsrechtsmandat beurteilen oder Anwalt bereitet sich auf Fachanwaltsprüfung vor. Normen BGB §§ 611a ff. KSchG BetrVG TVG BUrlG EFZG TzBfG AGG ArbGG. Prüfraster Individualarbeitsrecht Kollektivarbeitsrecht Diskriminierungsschutz Verfahren ArbGG LAG BAG verifizierbare Quellen. Output Rechtsgebietsuebersicht mit Normenhierarchie Pflichtliteratur und Mandatstriage-Hinweisen. Abgrenzung zu erstgespraech-mandatsannahme und mandat-triage-Skill.

### Fachanwalt für Arbeitsrecht — Orientierung

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Fachanwalt für Arbeitsrecht — Orientierung` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## FAO-Voraussetzungen (§ 10 FAO)

- Lehrgang 120 Stunden + drei Klausuren.
- 100 Fälle in den letzten drei Jahren aus dem Arbeitsrecht; davon mindestens 50 Mandate im Individualarbeitsrecht, mindestens 10 Mandate im Kollektivarbeitsrecht, mindestens 20 rechtsförmliche Verfahren.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Individualarbeitsrecht | BGB §§ 611a ff. (Arbeitsvertrag); KSchG (Kündigungsschutz); BUrlG (Urlaub); EFZG (Entgeltfortzahlung); TzBfG (Teilzeit und Befristung); NachwG (Nachweisgesetz, idF Aug. 2022); MuSchG; BEEG; ArbZG; ArbStättV |
| Kollektivarbeitsrecht | BetrVG (Betriebsverfassung); TVG (Tarifvertrag); MitbestG; DrittelbG; SprAuG |
| Diskriminierung | AGG (§§ 1, 7, 15) |
| Arbeitsschutz | ArbSchG; ArbStättV; ArbMedVV |
| Insolvenz | InsO §§ 113, 125 ff. |
| Verfahren | ArbGG (Arbeitsgerichtsgesetz) |
| Internationale Bezüge | Rom I-VO; AEntG; AÜG |

## Typische Mandate

- Kündigungsschutzklage (§ 4 KSchG).
- Aufhebungsvertrag (Verhandlung, Sozialplan).
- Befristungskontrollklage (§ 17 TzBfG).
- Sozialplan / Interessenausgleich nach § 112 BetrVG (Kollektivseite).
- Betriebsratsanhörung nach § 102 BetrVG.
- Zeugnisstreitigkeit (§ 109 GewO).
- AGG-Entschädigungsklage (§ 15 AGG).
- Lohn- und Gehaltsklage.
- Mobbing und Schadensersatzklage (§ 280 Abs. 1 BGB iVm Schutzpflicht § 241 Abs. 2 BGB).

## Fristen (Auswahl)

- **Kündigungsschutzklage** § 4 KSchG — drei Wochen ab Zugang der schriftlichen Kündigung.
- **Befristungskontrollklage** § 17 TzBfG — drei Wochen nach vereinbartem Ende.
- **AGG-Entschädigung** § 15 Abs. 4 AGG — schriftliche Geltendmachung binnen zwei Monaten; Klagefrist § 61b ArbGG drei Monate.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Anhörung des Betriebsrats** § 102 BetrVG — eine Woche bei ordentlicher, drei Tage bei außerordentlicher Kündigung.
- **Sozialplanverhandlungen** § 112 Abs. 2, 3 BetrVG — Einigungsstelle nach Scheitern.

## Hauptgerichte

- Arbeitsgericht (ArbG) — erste Instanz, Kammern.
- Landesarbeitsgericht (LAG) — Berufungsinstanz.
- Bundesarbeitsgericht (BAG) — Revisionsinstanz, Erfurt.
- BVerfG bei Grundrechtsfragen.
- EuGH bei unionsrechtlichen Fragen (Befristung, Arbeitszeit, Gleichbehandlung).

## Berufsverband

- Arbeitsgemeinschaft Arbeitsrecht im DAV.

## Schnittstellen

- **`arbeitsrecht`** für operative Mandatsführung, Vorlagen.
- **`kanzlei-allgemein`** für Fristen und Versand.
- **`fachanwalt-sozialrecht`** bei Schnittstellen zur Arbeitslosenversicherung und Sperrzeit.
- **`fachanwalt-insolvenz-sanierungsrecht`** bei Betriebsübergang § 613a BGB und Insolvenz.

## Aktuelle Rechtsprechung - Überblick wichtiger Leitentscheidungen (Stand Mai 2026)

Folgende Leitentscheidungen sind im aktuellen Plugin-Stand mit offener Quelle (dejure.org / bundesarbeitsgericht.de) belegt:

- **BAG, 23.10.2025 - 8 AZR 300/24** (Paarvergleich Equal Pay): Ein einzelner Vergleichskollege des anderen Geschlechts genuegt zur Vermutung nach § 22 AGG. Siehe Skill `fachanwalt-arbeitsrecht-bag-equal-pay-paarvergleich`.
- **BAG, 03.06.2025 - 9 AZR 104/24** (kein Urlaubsverzicht durch Prozessvergleich): Mindesturlaub waehrend laufenden Arbeitsverhaeltnisses nicht disponibel. Siehe Skill `fachanwalt-arbeitsrecht-bag-mindesturlaub-kein-verzicht`.
- **BAG, 25.03.2026 - 5 AZR 108/25** (Freistellungsklausel unwirksam): Pauschale formularmäßige Freistellungsklausel verstoesst gegen § 307 BGB. Siehe Skill `fachanwalt-arbeitsrecht-bag-freistellungsklausel-unwirksam`.
- **BAG, 01.04.2026 - 6 AZR 152/22 und 6 AZR 157/22** (Massenentlassung): Fehlerhafte oder verfruehte Massenentlassungsanzeige fuehrt zur Unwirksamkeit aller Kuendigungen. Siehe Skill `fachanwalt-arbeitsrecht-massenentlassung-17-kschg`.
- **EuGH, 30.10.2025 - C-134/24 und C-402/24** (Massenentlassung): Keine Heilung fehlender oder verfruehter Anzeige nach Kuendigungsausspruch.
- **BAG, 20.02.2025 - 8 AZR 61/24** (DSGVO-Schadensersatz): "Stoergefuehl" allein begruendet keinen Anspruch nach Art. 82 DSGVO.
- **BAG, 18.06.2025 - 7 AZR 50/24** (Befristung Betriebsratsmitglieder): § 14 Abs. 2 TzBfG anwendbar; Schadensersatz auf Folgevertrag bei Mandatsbenachteiligung.
- **BAG, 22.09.2022 - 8 AZR 4/21** (NachweisG): Schadensersatz neben Bussgeld bei Pflichtverletzung des Arbeitgebers nach NachwG.
- **BAG, 13.09.2022 - 1 ABR 22/21** (Arbeitszeiterfassung): Pflicht des Arbeitgebers zur systematischen Arbeitszeiterfassung aus § 3 Abs. 2 Nr. 1 ArbSchG.

Vor Schriftsatzverwendung jeweils Volltext und ggf. neuere Rechtsprechung in offenen Quellen (dejure.org, openjur.de, bundesarbeitsgericht.de) verifizieren.

## Paragrafenkette Kernbereiche Individualarbeitsrecht

- § 611a BGB — Arbeitsvertrag
- § 626 BGB — Außerordentliche Kündigung
- §§ 1 ff. KSchG — Kündigungsschutz; § 4 KSchG — Klagefrist drei Wochen
- § 102 BetrVG — Betriebsratsanhörung
- §§ 1, 3 BUrlG — Urlaubsanspruch; § 7 Abs. 3 BUrlG — Verfall
- § 14 TzBfG — Befristung; § 17 TzBfG — Kontrollklage drei Wochen

---

## Skill: `erstgespraech-mandatsannahme`

_Strukturierter Erstgespraechsleitfaden für Individual- und kollektives Arbeitsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen: Strukturierter Erstgespraechsl..._

# Strukturierter Erstgespraechsleitfaden für Individual- und kollektives Arbeitsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierter Erstgespraechsleitfaden für Individual- und kollektives Arbeitsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.

### Erstgespraech und Mandatsannahme im Individual- und kollektives Arbeitsrecht

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Erstgespraech und Mandatsannahme im Individual- und kollektives Arbeitsrecht` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Individual- und kollektives Arbeitsrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klären, Konflikt- und GwG-Prüfung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Individual- und kollektives Arbeitsrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klägerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Kuendigung, Abmahnung, Befristung, Aufhebungsvertrag, Lohn, Urlaub, BR-Sachen
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Kuendigungsschutzklage, Befristungskontrollklage, Zahlungsklage Arbeitsgericht). Frist-Alarm an die Vorbereitung weitergeben.

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

Standard-Streitwerte im Bereich Individual- und kollektives Arbeitsrecht:

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

- BORA, BRAO, FAO für Fachanwaltschaft Individual- und kollektives Arbeitsrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- KSchG, TzBfG, BetrVG, BGB, EFZG, BUrlG, AGG, NachwG (für fachliche Erstpruefung).
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

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Individual- und kollektives Arbeitsrecht). Handlungs-Sequenz:

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
- Verfahrensdauer im Bereich Individual- und kollektives Arbeitsrecht: Erfahrungswerte nach Instanz.
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

## Audit-Hinweis (27.05.2026)

Im Halluzinations-Audit 2026-05-27 wurden in diesem Skill folgende
Aktenzeichen geprueft und korrigiert:

## Cross-Refs

- `vergleichsverhandlung-strategie` (im selben Plugin) für den Fall, dass aussergerichtliche Loesung angestrebt wird.
- `schriftsatzkern-substantiierung` (im selben Plugin) für den Schriftsatzaufbau, wenn Klage/Widerspruch eingereicht wird.
- Kanzlei-Allgemein-Plugin `kanzlei-allgemein` für Konflikt-, GwG- und PEP-Prüfroutinen.

## Aktuelle Rechtsprechung (Stand Mai 2026)

Im Plugin verifizierte Leitentscheidungen mit offener Quelle (dejure.org / bundesarbeitsgericht.de):

- BAG, 23.10.2025 - 8 AZR 300/24 (Paarvergleich Equal Pay)
- BAG, 03.06.2025 - 9 AZR 104/24 (Mindesturlaub kein Verzicht)
- BAG, 25.03.2026 - 5 AZR 108/25 (Freistellungsklausel unwirksam)
- BAG, 01.04.2026 - 6 AZR 152/22 + 157/22 (Massenentlassung)
- EuGH, 30.10.2025 - C-134/24 + C-402/24 (Massenentlassung)

Weitere Entscheidungen siehe Themenskills. Im Erstgespraech keine Rechtsprechung aus Modellwissen zitieren; bei Bedarf vor Verwendung in dejure.org / openjur.de / bundesarbeitsgericht.de verifizieren.

## Paragrafenkette Fristen Arbeitsrecht

- **§ 4 KSchG** — Klage auf Kündigungsschutz: drei Wochen ab Zugang der schriftlichen Kündigung
- **§ 17 TzBfG** — Befristungskontrollklage: drei Wochen ab vereinbartem Ende
- **§ 15 Abs. 4 AGG** — Geltendmachung AGG-Entschädigung schriftlich innerhalb zwei Monate
- **§ 61b ArbGG** — Klage auf AGG-Entschädigung: drei Monate ab schriftlicher Geltendmachung
- **§ 102 Abs. 2 BetrVG** — Betriebsratsanhörung: eine Woche ordentlich, drei Tage außerordentlich

## Triage — Erstgespräch-Einstieg

1. Liegt eine sofortige Klagefrist vor? (Kündigung → § 4 KSchG, Befristungsende → § 17 TzBfG)
2. GwG-Identifizierung abgeschlossen? (Lichtbildausweis, bei juristischer Person Handelsregister)
3. Interessenkonflikt geprüft? (§ 43a Abs. 4 BRAO)
4. Honorarvereinbarung: RVG oder Stundensatz? Vorschuss anfordern!
5. Welche weiteren Fristen sind aus den vorgelegten Unterlagen erkennbar?

---

## Skill: `erstpruefung-und-mandatsziel`

_Fachanwalt Erstprüfung und Mandatsziel: systematische Erstaufnahme im arbeitsrechtlichen Mandat, Rollenklärung, Zielformulierung, Interessenkonflikt-Check, Mandatsumfang, Kostenhinweis RVG, erste Risikoampel: Fachanwalt Erstprüfung und Mandatsziel: systema..._

# Fachanwalt Erstprüfung und Mandatsziel: systematische Erstaufnahme im arbeitsrechtlichen Mandat, Rollenklärung, Zielformulierung, Interessenkonflikt-Check, Mandatsumfang, Kostenhinweis RVG, erste Risikoampel.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: KSchG; BetrVG; TzBfG; EntgTranspG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt Erstprüfung und Mandatsziel: systematische Erstaufnahme im arbeitsrechtlichen Mandat, Rollenklärung, Zielformulierung, Interessenkonflikt-Check, Mandatsumfang, Kostenhinweis RVG, erste Risikoampel.

### Spezial: Fachanwalt Erstprüfung und Mandatsziel

## Fachlicher Kern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Spezial: Fachanwalt Erstprüfung und Mandatsziel` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Einstieg
Wenn ein Mandat vorliegt oder angeboten wird, folgende Punkte klären:

1. **Wer ist der Mandant?** Name, Stellung (Arbeitnehmer, Arbeitgeber, Betriebsrat, Gewerkschaft)?
2. **Was ist das Kernproblem?** Kündigung, Vergütung, Diskriminierung, Betriebsverfassung, Vertragsgestaltung?
3. **Gibt es laufende Fristen?** 3-Wochen-Frist § 4 KSchG, § 17 TzBfG, AGG-Frist § 15 Abs. 4 AGG?
4. **Interessenkonflikt?** Vertritt die Kanzlei oder die Fachanwältin/den Fachanwalt bereits die Gegenseite?
5. **Was ist das Ziel des Mandanten?** Bestandsschutz, Abfindung, Schadensersatz, Vertragsänderung?

## Phase 1: Interessenkonflikt-Prüfung (§ 43a BRAO, § 3 BORA)

### Prüfpflicht
Vor jeder Mandatsannahme muss geprüft werden:
- Vertritt die Kanzlei die Gegenseite in derselben oder einer verwandten Angelegenheit?
- Hat ein Anwalt der Kanzlei früher die Gegenseite beraten?
- Gibt es sonstige Interessenkollisionen (Eigeninteressen, familiäre Verbindungen)?

**Rechtsfolge Verstoß:** § 356 StGB (Parteiverrat); berufsrechtliche Sanktionen; Anwaltsvertrag nichtig.

### Dokumentation
Interessenkonflikt-Check in der Kanzleisoftware; schriftliche Bestätigung der Prüfung in der Akte.

## Phase 2: Sachverhaltsaufnahme

### Grunddaten

| Feld | Inhalt |
|---|---|
| Mandantenname | |
| Arbeitgeber/Arbeitnehmer | |
| Betriebsname und -ort | |
| Branche | |
| Betriebsgröße (ca.) | |
| Beginn Arbeitsverhältnis | |
| Letzte Vergütung (brutto) | |
| Besonderer Kündigungsschutz? | |
| Besteht Betriebsrat? | |
| Kündigung erhalten? Datum? | |

### Fristenüberblick (sofort beim Erstgespräch)
- Liegt eine Kündigung vor? → § 4 KSchG-Frist berechnen
- Ist das Befristungsende abgelaufen? → § 17 TzBfG-Frist
- Diskriminierungsfall? → § 15 Abs. 4 AGG-Frist (2 Monate)

## Phase 3: Mandatsziel und Interessenlage

### Mandatsziel klären — vier Grundoptionen

| Option | Beschreibung | Typisch wenn |
|---|---|---|
| Bestandsschutz | Fortsetzung des Arbeitsverhältnisses erzwingen | Mandant will unbedingt weiterarbeiten |
| Abfindung | Hohe Abfindung aushandeln; schnelle Einigung | Neue Stelle in Aussicht; wirtschaftliches Interesse |
| Beides prüfen lassen | Strategie offen halten; im Gütermin entscheiden | Lage noch unklar |
| Schadensersatz/Entschädigung | AGG-Ansprüche, EntgTranspG, sonstige Ansprüche | Diskriminierung, Mobbing, verweigerte Gehaltserhöhung |

### Fragen zur Interessenlage
- Will der Mandant nach Verfahrensabschluss im Betrieb bleiben, oder lieber weg?
- Wie ist die finanzielle Situation? Kann er/sie sich eine Prozessdauer von 6–18 Monaten leisten?
- Besteht Rechtschutzversicherung? (Falls ja: Deckungsanfrage stellen)
- Wie ist das Verhältnis zum Arbeitgeber/Vorgesetzten — sachlich oder eskaliert?

## Phase 4: Erste Risikoampel

### Grün — Starke Position
- Formfehler bei der Kündigung (kein Original, fehlende Vollmacht, keine BR-Anhörung)
- Sonderkündigungsschutz (Schwangerschaft, Elternzeit, Betriebsrat) ohne behördliche Zustimmung
- Massenentlassungsanzeige fehlerhaft (post-BAG 6 AZR 152/22)
- Befristungsabrede nicht schriftlich oder nach Dienstantritt unterzeichnet

### Gelb — Mittlere Lage
- KSchG anwendbar; Kündigung hat Angriffspunkte, aber Ausgang unsicher
- Sozialauswahl ist anfechtbar, aber dokumentiert
- Sachgrundbefristung ist schwach, aber nicht offensichtlich unwirksam

### Rot — Schwache Position
- KSchG nicht anwendbar (Betriebsgröße unter Schwelle, kurze Betriebszugehörigkeit)
- Kündigung formal korrekt; Kündigungsgrund stark (schweres Fehlverhalten mit Beweisen)
- Klagefrist bereits abgelaufen; § 7 KSchG-Fiktion

## Phase 5: Mandatsumfang und Kostenhinweis

### RVG-Werte im Arbeitsrecht
- Streitwert Kündigungsschutzklage: § 42 Abs. 2 GKG = 1 Vierteljahresverdienst
- Abfindungsvergleich: Streitwert kann höher sein (abhängig von Vergleichswert)
- Beratungsgebühr: nach RVG § 34 frei vereinbar oder nach Stundensatz

### Kostenhinweis-Pflicht (§ 49b BRAO, § 3a RVG)
Vor Mandatsannahme: Hinweis auf voraussichtliche Kosten; Vergütungsvereinbarung schriftlich wenn von RVG-Sätzen abgewichen wird.

### Rechtsschutzversicherung
Falls RSV vorhanden: Deckungsanfrage sofort stellen; RSV-Selbstbehalt klären; RSV kann Vergleich beeinflussen (häufig RSV-Limit für Vergleichsabfindung).

## Anschluss-Skills
- `ar-einfuehrung-mandantenanliegen` für Themen-Routing nach Erstprüfung
- `ar-kuendigungspruefung-workflow` wenn Kündigung das Kernproblem ist
- `workflow-kaltstart-und-routing` für weiteres Routing.
- Keine Steuerberatung zur steuerlichen Behandlung von Abfindungen.

---

## Skill: `fachanwalt-arbeitsrecht-betriebsratsanhoerung`

_Betriebsratsanhoerung nach § 102 BetrVG vor jeder Kündigung. Anwendungsfall Kündigung soll ausgesprochen werden und BR-Anhoerung muss korrekt durchgeführt werden. Normen § 102 BetrVG Anhoerungs- und Widerspruchsrecht § 102 Abs. 1 S. 3 BetrVG Unwirksamkeit bei fehlerhafter Anhoerung § 102 Abs. 5 BetrVG Weiterbeschaeftigungsanspruch. Prüfraster vollständige Mitteilung Kündigungsgründe subjektive Determinationstheorie Stellungnahmefrist eine Woche ordentlich drei Tage außerordentlich Widerspruchsgründe. Output Anhoerungsschreiben-Vorlage Empfangsprotokoll und Kündigungs-Timing-Plan. Abgrenzung zu fachanwalt-arbeitsrecht-kündigungsschutzklage und fachanwalt-arbeitsrecht-massenentlassung-17-kschg._

# Anhörung des Betriebsrats (§ 102 BetrVG)

## Zweck

Vollständige und inhaltlich korrekte Betriebsratsanhörung vor jeder Kündigung — aus Arbeitgeber-Sicht als sorgfältige Vorbereitung, aus Arbeitnehmer-Sicht als potenzieller Unwirksamkeitsgrund. Der häufigste Formfehler im deutschen Kündigungsrecht.

## Mandantenfragen — Kaltstart

1. **Gibt es einen Betriebsrat im Betrieb?** — § 1 BetrVG: mindestens 5 wahlberechtigte, 3 wählbare Arbeitnehmer; Betriebsabgrenzung nach § 1 BetrVG beachten.
2. **Welche Kündigung steht bevor — ordentlich, außerordentlich, Änderungs­kündigung?** — Bestimmt Stellungnahme-Frist und Widerspruchsmöglichkeit.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. **Liegt Sonderkündigungsschutz vor?** — MuSchG, BEEG, SGB IX, Datenschutzbeauftragter: Anhörungsschreiben muss ggf. auf Schwerbehinderung, Schwangerschaft etc. eingehen.
5. **Gibt es eine betriebsbedingte Kündigung mit Sozialauswahl?** — Vergleichsgruppe und Sozialauswahlentscheidung im Anhörungsschreiben mitteilen; sonst Anhörung unvollständig.
6. **Ist die Zweiwochenfrist bei außerordentlicher Kündigung gefährdet?** — § 626 Abs. 2 BGB: 2 Wochen ab Kenntnis des Grundes für Arbeitgeber; Anhörung lauft innerhalb dieser Frist.
7. **Wurde die Anhörung bereits dokumentiert?** — Datum der Übergabe / Zusendung an Vorsitzenden des Betriebsrats (§ 26 Abs. 2 BetrVG); Beginn Stellungnahmefrist.
8. **Hat der Betriebsrat Widerspruch eingelegt?** — Wenn ja: Weiterbeschäftigungsanspruch § 102 Abs. 5 BetrVG bis zur Klärung durch Gericht.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 102 Abs. 1 S. 1 BetrVG | Anhörungspflicht vor jeder Kündigung |
| § 102 Abs. 1 S. 3 BetrVG | Unwirksamkeitsfolge bei Unterlassen oder unvollständiger Anhörung |
| § 102 Abs. 2 BetrVG | Stellungnahmefristen: 1 Woche ordentlich, 3 Tage außerordentlich |
| § 102 Abs. 3 BetrVG | Widerspruchsgründe gegen ordentliche Kündigung |
| § 102 Abs. 4 BetrVG | Zustimmungsfiktion bei Schweigen (nach Fristablauf ordentliche Kündigung) |
| § 102 Abs. 5 BetrVG | Weiterbeschäftigungsanspruch bei Widerspruch + Klage |
| § 26 Abs. 2 BetrVG | Vertretung durch Vorsitzenden als Empfangsberechtigten |
| § 79 BetrVG | Verschwiegenheitspflicht; sensible Daten ggf. schwärzen |

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage | Quelle |
|---|---|---|---|---|
| BAG, 2. Senat | 2 AZR 302/96 | 27.02.1997 | Subjektive Determinationstheorie: Der Arbeitgeber muss dem Betriebsrat die Umstaende mitteilen, die seine Kuendigungsentscheidung tatsaechlich bestimmt haben; aus seiner Sicht objektiv unrichtige oder unvollstaendige Angaben fuehren zur Unwirksamkeit der Anhoerung (§ 102 Abs. 1 S. 3 BetrVG) | dejure.org-Vernetzung BAG 27.02.1997 - 2 AZR 302/96 |
| BAG, 2. Senat | 2 AZR 227/97 | 05.02.1998 | Praezisierung: Mitteilungspflicht umfasst auch dem AG bekannte, fuer den AN guenstige Umstaende, soweit sie objektiv relevant sind | dejure.org-Vernetzung BAG 05.02.1998 - 2 AZR 227/97 |
| BAG, 2. Senat | 2 AZR 472/01 | 10.10.2002 | Angabe der Sozialdaten bei verhaltensbedingter Kuendigung; Beginn der Stellungnahmefrist bei ergaenzenden Informationen | dejure.org-Vernetzung BAG 10.10.2002 - 2 AZR 472/01 |

Hinweis: Aktuellere Entscheidungen (Q4/2025 - Q2/2026) zur Anhoerungs-Substantiierung vor Schriftsatzverwendung in offenen Quellen pruefen.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Prüfschema Betriebsratsanhörung

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfpunkt | Norm | Rechtsfolge bei Fehler |
|---|---|---|---|
| 1 | Betriebsrat existiert im Betrieb? | § 1 BetrVG | Keine Anhörungspflicht |
| 2 | Anhörung schriftlich oder in Textform? | § 21a Abs. 2 BetrVG | Formmangel; heilbar? |
| 3 | Zugang beim Vorsitzenden nachweisbar? | § 26 Abs. 2 BetrVG | Frist-Beginn unklar |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 9 | Stellungnahme abgewartet oder Frist abgelaufen? | § 102 Abs. 2 BetrVG | Kündigung vor Fristablauf = unwirksam |
| 10 | Bei Widerspruch: § 102 Abs. 5-Anspruch beachtet? | § 102 Abs. 5 BetrVG | Weiterbeschäftigung möglicherweise einklagbar |

## Mindestinhalt der Anhörung

| Inhaltspunkt | Erforderlich | Beispiel |
|---|---|---|
| Vollständiger Name, Geburtsdatum | Ja | "Max Mustermann, geb. 01.01.1980" |
| Familienstand | Ja | "verheiratet" |
| Unterhaltspflichten | Ja | "2 Kinder" |
| Schwerbehinderung | Ja | "GdB 50" oder "keine" |
| Eintrittsdatum | Ja | "01.09.2015" |
| Tätigkeit / Abteilung | Ja | "Sachbearbeiter Buchhaltung, Abt. Controlling" |
| Bruttomonatsvergütung | Ja | "EUR 4.200 brutto" |
| Kündigungsart und -termin | Ja | "ordentlich zum 31.12.2026" |
| Kündigungsgründe (konkret) | Ja | Sachverhalt mit Daten, nicht nur Bezeichnung |
| Sozialauswahl + Vergleichsgruppe | Bei betriebsbedingter Kündigung | Wer im Vergleich, warum Mandant ausgewählt |
| Abmahnungen (bei verhaltensbedingter) | Ja | Datum, Inhalt, Folge |
| Krankheitszeiten (bei personenbedingter) | Ja | AU-Tage pro Jahr 2023/2024/2025 |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Anhoerungsruege § 102 BetrVG in Klageschrift | Ruege-Baustein nach Template unten |
| Variante A — Anhoerungsmangel klar und offensichtlich | Auf starke Unwirksamkeit setzen; Vergleich auf hohem Niveau |
| Variante B — Anhoerung formell ok aber inhaltlich unvollstaendig | Subjektive Determinationstheorie pruefen; Einzelfall-Argumentation |
| Variante C — Kein Betriebsrat vorhanden | § 102 BetrVG entfaellt; andere Unwirksamkeitsgruende pruefen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schreibvorlage Anhörungsschreiben

```
[Briefkopf Arbeitgeber]

An den Betriebsrat — Herrn/Frau Vorsitzende/n — Im Hause
                                               [Ort, Datum]

Anhörung gemäss § 102 BetrVG zur beabsichtigten Kündigung

Sehr geehrter Herr / Frau [Vorsitzende/r],

wir beabsichtigen, das Arbeitsverhältnis mit
[Name, geb. [Datum]], [Tätigkeitsbezeichnung],
zu kündigen und hören Sie hierzu vor Ausspruch an.

1. Persönliche Daten
   Name: [Name]
   Geburtsdatum: [Datum]
   Familienstand: [verheiratet / ledig / geschieden]
   Unterhaltspflichten: [Anzahl Kinder; Ehegatte]
   Schwerbehinderung: [ja, GdB [Grad] / nein]

2. Beschäftigungsdaten
   Eintritt: [Datum]
   Tätigkeit: [Bezeichnung]
   Abteilung: [Bezeichnung]
   Brutto-Monatsvergütung: EUR [Betrag]

3. Beabsichtigte Kündigung
   Art: [ordentlich / ausserordentlich / Aenderungs-]
   Kündigungsfrist: [Dauer]
   Datum: [Termin]

4. Kündigungsgründe
   [Vollständige Sachverhaltsschilderung; bei verhaltens-
   bedingt: Pflichtverletzung + Abmahnung(en) mit Daten +
   negative Prognose; bei betriebsbedingt: Wegfall des AP,
   Sozialauswahl Vergleichsgruppe + Ergebnis; bei personen-
   bedingt: AU-Zeiten mit Daten, Prognose, erhebliche
   Betriebsbeeinträchtigung]

5. Anlagen
   [ ] Abmahnung(en) [Datum]
   [ ] Auswertung AU-Zeiten
   [ ] Sozialauswahlübersicht
   [ ] [Sonstiges]

Wir bitten um Stellungnahme binnen [1 Woche / 3 Tage] nach
§ 102 Abs. 2 BetrVG (Frist endet am [Datum]).

[Unterschrift Geschäftsführung / HR-Leitung]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Widerspruchsgründe § 102 Abs. 3 BetrVG

| Widerspruchsgrund | Inhalt |
|---|---|
| Nr. 1 | Sozialwidrige Auswahl (KSchG-Verstoss) |
| Nr. 2 | Freier Arbeitsplatz im Betrieb oder anderen Unternehmen |
| Nr. 3 | Umschulung oder Weiterbildung möglich |
| Nr. 4 | Weiterbeschäftigung unter geänderten Arbeitsbedingungen nach Zustimmung |
| Nr. 5 | Widerspruch eines anderen Betriebsrats dem dieser zugeordnet ist |

**Wichtig:** Widerspruch nur gegen **ordentliche** Kündigung möglich; gegen außerordentliche Kündigung kein gesetzliches Widerspruchsrecht.

## Weiterbeschäftigungsanspruch § 102 Abs. 5 BetrVG

- Voraussetzungen: wirksamer Widerspruch des BR nach § 102 Abs. 3 + Kündigungsschutzklage des Arbeitnehmers
- Arbeitgeber muss Arbeitnehmer bis zur Klärung des Kündigungsstreits weiterbeschäftigen
- AG kann Befreiung beantragen, wenn Kündigung offensichtlich wirksam, Weiterbeschäftigung unverhältnismäßig belastend
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Beweislast und Darlegungslast

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Arbeitnehmer** bei Anhörungsrüge: muss konkreten Mangel darlegen (z.B. fehlende Sozialauswahl, nicht genannte Abmahnung).
- Einwand "subjektiv vollständig": Arbeitgeber kann geltend machen, er habe gutgläubig alle ihm bekannten Gründe mitgeteilt.

## Typische Anhörungsmängel in der Praxis

| Mangel | Häufigkeit | Heilung |
|---|---|---|
| Sozialauswahl nicht erwähnt | Sehr häufig | Nein — führt zu Unwirksamkeit |
| Abmahnung nicht beigefügt | Häufig | Ggf. wenn aus Gründen beschrieben |
| Kündigung vor Fristablauf ausgesprochen | Mittel | Nein — absoluterMangel |
| Schwerbehinderung nicht erwähnt | Häufig | Führt zu Anhörungsmangel wenn bekannt |
| Übergabe nicht an Vorsitzenden | Selten | Fristlauf zweifelhaft |

## Anschluss-Skills

- `fachanwalt-arbeitsrecht-kuendigungsschutzklage` — Klageerhebung nach Anhörungsmangel
- `fachanwalt-arbeitsrecht-betriebsratsbeschluss-heilung` — bei parallelem Beschlussmangel
- `fachanwalt-arbeitsrecht-bag-freistellungsklausel-unwirksam` — bei kombinierter Kündigung und Freistellung

## Quellen

- BetrVG §§ 1, 26, 79, 102
- KSchG §§ 1, 4
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Fitting BetrVG-Kommentar § 102; DKKW BetrVG § 102

<!-- AUDIT 27.05.2026
-->

---

## Skill: `fachanwalt-arbeitsrecht-aufhebungsvertrag-sperrzeit`

_Aufhebungsvertrag mit Sperrzeit-Vermeidung nach § 159 SGB III bei Eigeninitiative oder drohender Kündigung. Anwendungsfall Arbeitgeber und Arbeitnehmer wollen Arbeitsverhältnis auflösen ohne Sperrzeit für Arbeitslosengeld. Normen § 159 SGB III wichtiger Grund Sperrzeitentscheidung § 623 BGB Schriftform § 14 KSchG Klagefrist. Prüfraster Initiativseite wichtiger Grund Abfindung Steuerpflicht Fuenftelregelung Krankenversicherung Wettbewerbsverbot Outplacement. Output Aufhebungsvertrags-Entwurf mit Sperrzeitlegitimerung Steuerklauseln und Verhandlungsstrategie. Abgrenzung zu fachanwalt-arbeitsrecht-kündigungsschutzklage und fachanwalt-arbeitsrecht-verhandlung-guete-abfindung-arbg._

# Aufhebungsvertrag mit Sperrzeit-Vermeidung

## Zweck

Aufhebungsvertrag so gestalten, dass Mandant **keine 12-Wochen-Sperrzeit** durch die Bundesagentur für Arbeit erleidet (§ 159 SGB III).

## 1) Eingangs-Abfrage

1. Wer initiiert? Arbeitgeber oder Arbeitnehmer?
2. Drohende **betriebsbedingte Kündigung**? Konkretisierbar?
3. Beschaeftigungsdauer und Brutto-Jahresgehalt?
4. Anwendbarkeit KSchG (Betrieb > 10 AN, > 6 Monate Beschaeftigung)?
5. Sonderkündigungsschutz (BR, Schwerbehindert, Schwanger, Eltern)?
6. Bestehende Krankheit, BEM-Verfahren?
7. Eltern- / Pflegezeit?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persönlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## 2) Sperrzeit-Vermeidung — wichtige Konstellationen

### Konstellation A: Drohende ordentliche AG-Kündigung

Rechtsprechungsstand: BSG, Urteil vom 12.07.2006 - B 11a AL 47/05 R: Aufhebungsvertrag zur Abwendung einer drohenden, objektiv rechtmaessigen ordentlichen betriebsbedingten Kuendigung des AG bei eingehaltener Kuendigungsfrist begruendet wichtigen Grund i.S.d. § 159 SGB III. Quelle: dejure.org, Vernetzung BSG 12.07.2006 - B 11a AL 47/05 R.

- AG hätte ordentlich kündigen koennen (KSchG-relevanter Grund: betrieblich, personal, verhaltensbedingt)
- Beendigungszeitpunkt nicht früher als bei ordentlicher Kündigung
- Abfindung **nicht höher** als 0,5 Brutto-Monatsentgelte pro Beschaeftigungsjahr (Fachliche Weisungen BA zu § 159 SGB III, Stand 01.01.2024, arbeitsagentur.de)

**Folge**: keine Sperrzeit.

### Konstellation B: Drohende verhaltensbedingte Kündigung

- Schwieriger zu argumentieren, da AN-Mitverschulden
- Bei klarer Pflichtverletzung mit AG-Abmahnung: ggf. wichtiger Grund

### Konstellation C: AN-Initiative aus betrieblichen Gründen

- AN moechte selbst gehen — keine Sperrzeit-Vermeidung
- Ausnahme: wichtiger Grund (Mobbing, Lohnverzug, Gesundheitsgefährdung)

## 3) Faustformel Abfindung

```
Abfindung = 0,5 Brutto-Monatsentgelte × Beschaeftigungsjahre
```

- 5 Jahre Betriebszugehoerigkeit, 4.000 EUR Brutto: 0,5 × 5 × 4.000 = 10.000 EUR
- 20 Jahre, 6.000 EUR: 0,5 × 20 × 6.000 = 60.000 EUR

**Verhandlungs-Spielraum**: 0,75-1,5 Brutto-Monatsgehaelter pro Jahr bei aelteren AN oder schwacher AG-Position.

## 4) Steuer: Fünftel-Regelung § 34 EStG

- Abfindung kann nach **Fünftel-Regelung** versteuert werden, wenn Zusammenballung
- Voraussetzung: Abfindung in einem VZ ausgezahlt
- Antrag in Steuererklärung
- Bei AN mit niedrigerem Einkommen besonders attraktiv

## 5) Krankenversicherung in der Karenzzeit

- Falls AN zu Arbeitslosigkeit zwischen Ausscheiden und neuer Stelle: KV über **Arbeitslosengeld** möglich
- Bei kurzem Arbeitswechsel: Familienversicherung oder freiwillige KV
- **Achtung**: bei Sperrzeit kein ALG -> KV-Liquidität prüfen

## 6) Klausel-Katalog Aufhebungsvertrag

### Pflicht-Klauseln

- Beendigungs-Zeitpunkt
- Abfindung mit Fälligkeit (typisch mit letztem Gehalt)
- Erledigungsklausel (sämtliche Anspruche erledigt)
- Zeugnis-Anspruch (mind. "gut")

### Soll-Klauseln

- **Freistellung** unter Anrechnung Resturlaub
- Verzicht Kündigungsschutzklage
- Wettbewerbsverbot ggf. mit Karenz-Entschädigung
- Outplacement-Kostenübernahme
- **Sperrzeit-Klausel**: "AG bestätigt, dass der Aufhebungsvertrag zur Vermeidung einer ordentlichen Kündigung aus betriebsbedingten Gründen geschlossen wird."

### Sprachregelung

- "Betriebsbedingte Kündigung waere ausgesprochen worden" (Sperrzeit-Schutz)
- Vermeiden: "AN bittet um Aufhebung" (Sperrzeit-Risiko)

### Schlussabsatz Variante A (kooperativ)

Wir sind an einer einvernehmlichen und zügigen Lösung interessiert und stehen für Rückfragen zur Formulierung der Sperrzeit-Klausel zur Verfügung. Eine konstruktive Einigung nutzt beiden Seiten.

### Schlussabsatz Variante B (formal-streng)

Der vorliegende Entwurf entspricht den gesetzlichen Mindestanforderungen zur Sperrzeit-Vermeidung. Abweichungen von der vorgeschlagenen Formulierung bedürfen der ausdrücklichen Zustimmung unserer Kanzlei und werden auf Sperrzeit-Konformität geprüft.

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## 7) Workflow

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkürzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

### Schritt 1 — Mandanten-Beratung

- Sperrzeit-Risiko anhand BA-Hinweise prüfen
- Abfindungs-Verhandlungsrahmen
- Alternative: Kündigungsschutzklage + Vergleich

### Schritt 2 — Vor-Verhandlung

- Mit AG-Vertretung (HR, Rechtsabteilung) Eckpunkte
- Schriftliche Entwurfs-Verhandlung

### Schritt 3 — Bundesagentur-Anfrage (optional)

- Wenn unsicher: Vorab-Sperrzeit-Anfrage bei BA
- Antwort innerhalb 4-6 Wochen

### Schritt 4 — Abschluss

- Schriftform zwingend (§ 623 BGB)
- Notar: nicht erforderlich
- Sofort an BA als Arbeitslosmeldung (3 Monate vor Ende empfohlen)

## 8) Typische Fehler

1. **Sperrzeit-Klausel vergessen**: BA kann trotzdem Sperrzeit verhängen
2. **Abfindung > 0,5 Faustformel**: BA-Risiko erhoeht
3. **Eigene Kündigung statt Aufhebung**: Sperrzeit fast garantiert
4. **Sonderkündigungsschutz übersehen**: Aufhebungsvertrag kann unwirksam sein (Schwangerschaft, BR-Mitglied)
5. **Wettbewerbsverbot ohne Karenz**: bei laufendem Vertrag schaedlich

## 9) BSG-Linien

- **BSG, Urteil vom 12.07.2006 - B 11a AL 47/05 R**: Aufhebungsvertrag zur Abwendung einer drohenden, objektiv rechtmaessigen betriebsbedingten Kuendigung des Arbeitgebers begruendet wichtigen Grund i.S.d. § 144 SGB III a.F. (= heute § 159 SGB III), sofern die Hinnahme der Kuendigung dem Arbeitnehmer nicht zuzumuten ist und die Kuendigungsfrist eingehalten wird. Quelle: dejure.org, Vernetzung BSG 12.07.2006 - B 11a AL 47/05 R.
- **BSG, Urteil vom 02.05.2012 - B 11 AL 6/11 R**: Praezisierung der Anforderungen an die "objektive Rechtmaessigkeit" der drohenden Kuendigung; die Drohung muss konkret und ernsthaft sein. Quelle: dejure.org, Vernetzung BSG 02.05.2012 - B 11 AL 6/11 R.
- **BSG, Urteil vom 17.11.2005 - B 11a/11 AL 69/04 R**: Sondernutzen fuer leitende Angestellte; vermeidende Aufhebungsvereinbarung. Quelle: dejure.org.
- Fachliche Weisungen der Bundesagentur fuer Arbeit zu § 159 SGB III (Stand 01.01.2024, fortlaufend gueltig; arbeitsagentur.de).
- Praxisliterature und neueres BSG-Aktenzeichen ohne offene Quelle nicht zitieren.

## Anschluss

- `fachanwalt-arbeitsrecht-kuendigungsschutzklage` — bei Klage statt Aufhebung
- `fachanwalt-arbeitsrecht-bem-verfahren` — bei Krankheit
- `testakten/kuendigungsschutzklage-weber-techlogix` — Testakte

## Aktuelle Rechtsprechung (Stand Mai 2026)

- BSG, 12.07.2006 - B 11a AL 47/05 R: wichtiger Grund bei drohender objektiv rechtmaessiger betriebsbedingter Kuendigung mit eingehaltener Frist. Quelle: dejure.org.
- BSG, 02.05.2012 - B 11 AL 6/11 R: Drohung muss konkret und ernsthaft sein. Quelle: dejure.org.
- Hinweis: Weitere BSG-Entscheidungen (Q4/2025 - Q2/2026) konnten zum Stand der Aktualisierung nicht ueber dejure.org/openjur.de mit Volltext und konkretem Aktenzeichen verifiziert werden. Anwaltlicher Beratungsstandard: Pruefung der jeweils aktuellen Fachlichen Weisungen der BA zu § 159 SGB III.

## Paragrafenkette

- § 159 SGB III — Sperrzeit
- § 158 SGB III — Ruhen bei Abfindung (wenn Kündigungsfrist nicht eingehalten)
- § 623 BGB — Schriftform Aufhebungsvertrag
- § 34 EStG — Fünftel-Regelung
- § 138 BGB — Sittenwidrigkeit; § 123 BGB — Anfechtung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `fachanwalt-arbeitsrecht-verhandlung-guete-abfindung-arbg`

_Gueteverhandlung im Arbeitsgerichtsverfahren nach § 54 ArbGG mit Auflösungsantrag und Abfindungsstrategie. Anwendungsfall Guetetermin steht an und Vergleich oder Auflösungsantrag soll vorbereitet werden. Normen § 54 ArbGG Gueteverfahren § 9 KSchG Auflösungsantrag § 10 KSchG Abfindungsobergrenzen § 159 SGB III Sperrzeit-Vermeidung. Prüfraster Abfindungsstrategie halbes-Bruttogehalt-Faustformel Vergleichsformulierung Sperrzeit-Klausel Protokollniederschrift Kostenregelung. Output Vergleichsvorschlag-Schreiben Verhandlungsskript Protokoll-Entwurf und Sperrzeit-Formulierungstipp. Abgrenzung zu fachanwalt-arbeitsrecht-aufhebungsvertrag-sperrzeit und vergleichsverhandlung-strategie._

# Güte-Verhandlung Arbeitsgericht / Abfindungs-Vergleich

## Zweck

Arbeitsrechtliche Vergleichsverhandlung im Güte-Verfahren § 54 ArbGG (ca. 90 % aller arbeitsrechtlichen Verfahren enden im Vergleich). Schwerpunkt Abfindungs-Strategie, BA-Sperrzeit-konforme Formulierung, Mediations-Sonderfälle.

## Eingaben

- Mandantenstatus (AG / AN)
- Streitgegenstand (Kündigung KSchG, Aufhebung, Befristung TzBfG, Diskriminierung AGG)
- Bestand Beschäftigungsverhältnis (Dauer, Brutto-Monatsverdienst)
- KSchG-Anwendbarkeit (Betrieb > 10 AN, > 6 Mon. Beschäftigung)
- Sperrzeit-Risiko BA bei Aufhebungsvertrag
- Beziehungs-Kontext (kollegialer Frieden vs. eskalativer Bruch)
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persönlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtlicher Rahmen

- **§ 54 ArbGG** — Güteverhandlung (Pflicht-Termin)
- **§ 9 KSchG** — Auflösung des Arbeitsverhältnisses durch Urteil gegen Abfindung (auf Antrag, wenn Fortsetzung unzumutbar)
- **§ 10 KSchG** — Abfindungsobergrenzen (Regelfall bis 12 Monatsverdienste; bei langer Betriebszugehörigkeit oder höherem Alter bis 15 bzw. 18 Monatsverdienste)
- **§ 1a KSchG** — Abfindungsanspruch bei betriebsbed. Kündigung (Hinweis im Kündigungsschreiben)
- **§ 159 SGB III** — Sperrzeit bei Aufhebungsvertrag (12 Wochen)
- **DurchführungsAnweisungen BA** zur Faustformel (0,5 Brutto/Beschäft.-Jahr)
- **§ 1 TVG** — Tarifliche Abfindungsregelungen
- **§ 779 BGB** — Vergleich

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Kommunikations-/Verhandlungs-Pfade

**Vorab:** Der untenstehende Workflow ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkürzen, umzustellen oder durch ein anderes Skill zu ersetzen — der Workflow ist Leitfaden, nicht Pflichtprogramm.

### Pfad 1 — Vorgerichtliche Anwaltskorrespondenz

- Anwalt-Schreiben mit Kündigungs-Beanstandung + Vergleichsangebot
- Frist 7-14 Tage
- Bei Erfolg: außergerichtlicher Aufhebungsvergleich; Klagefrist § 4 KSchG gewahrt durch eventuelle Klage-Bereitschaft

### Pfad 2 — Güte-Verhandlung § 54 ArbGG

- Pflicht-Termin nach Klageerhebung
- Erörterung durch Vorsitzenden allein (ohne ehrenamtliche Richter)
- Vergleichsvorschlag durch Vorsitzenden
- Niederschrift = vollstreckbar nach § 794 Abs. 1 Nr. 1 ZPO

### Pfad 3 — Mediation in Sonderfällen

- Bossing/Mobbing-Fälle
- Eingruppierungs-Konflikte mit BR
- AGG-Schwerstfälle mit Wertekonflikt
- Externe Mediator/in (DGFM)

## Abfindungs-Faustformel

| Faktor | Ansatz |
|---|---|
| Standard (BA-konform) | 0,5 × Brutto × Beschäft.-Jahre |
| Hartes Verhandeln AN | 0,75 × Brutto × Beschäft.-Jahre |
| Sehr lange Betriebszugehörigkeit / höherer Alter | 1,0 × Brutto × Beschäft.-Jahre |
| Sozialpfan-Abfindung | Tarif-/BV-spezifisch |

## Sperrzeit-Vermeidung BA (kritisch)

- AG-initiierte Beendigung dokumentieren ("Wir hätten ordentlich gekündigt aus betriebsbedingten Gründen")
- Abfindung **nicht höher als 0,5 Brutto × Beschäft.-Jahre**
- Beendigungs-Zeitpunkt entspricht ordentl. Kündigungs-Fristen
- Sprachregelung: NIE "AN bittet um Aufhebung" — IMMER "AG bietet Aufhebung als Alternative zur Kündigung"

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Abfindungsverhandlung in Güteverhandlung | Vergleichsverhandlung nach § 54 ArbGG; Klausel-Katalog unten |
| Variante A — AG signalisiert Vergleichsbereitschaft vor Termin | Vorab-Settlement vor Güteverhandlung um Streitwert zu reduzieren; außergerichtlicher Vergleich anstreben |
| Variante B — Mandant will tatsächlich zurück an den Arbeitsplatz | Standhafte Bestandsforderung; kein Abfindungsangebot annehmen ohne Bestandsprüfung |
| Variante C — Mandant zieht Annahmeverzugslohn der Abfindung vor | Auflaufende Annahmeverzugslohn-Strategie statt Einmalabfindung; § 615 BGB Anspruch sichern |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzulösen — nicht das Mandat in das Schema zu pressen.

## Vergleichs-Klausel-Katalog

```
1. Beendigung [Datum]
2. Abfindung EUR [...] in entsprechender Anwendung der Abfindungsregeln §§ 9 und 10 KSchG
3. Freistellung Abfindung mit Anrechnung Resturlaub
4. Zeugnis: mindestens "gut", Schluesselformulierungen [konkret]
5. Erledigungs-Klausel: saemtliche Anspruche aus Arbeitsverhaeltnis erledigt
6. Kuendigungsschutzklage zuruecknehmen / Klage als erledigt erklaeren
7. Sperrzeit-Verzicht-Erklaerung (formaler Hinweis nicht moeglich, aber:
   "betriebsbedingte Kuendigung waere ausgesprochen worden")
   [ggf. weglassen wenn keine Sperrzeit-Relevanz]

Schlussabsatz Variante A (kooperativ):
Wir regen an, diesen Vergleich noch vor dem Gütetermin zu unterzeichnen und
den Termin einvernehmlich aufzuheben. Eine frühzeitige Einigung spart beiden
Seiten Kosten und ermöglicht einen geordneten Abschluss.

Schlussabsatz Variante B (formal-streng):
Eine Einigung ist nur auf Basis des vorliegenden Entwurfs möglich. Abweichungen
bedürfen einer gesonderten schriftlichen Vereinbarung. Andernfalls wird das
Verfahren ohne Einschränkung fortgeführt.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## Strategie und Taktik

- **Wer fordert zuerst, gewinnt selten** — AG-Vorschlag zuerst abwarten
- **Anchor mit hoher Forderung**: 1,5 × Brutto, dann auf 1,0 herunter verhandeln
- **Outplacement** als Zusatzwert (5.000-15.000 EUR)
- **Karenzentschädigung Wettbewerb** wenn klausel-relevant
- **Bei AGG-Klagen**: Schadensersatz-Schmerzensgeld als separate Position
- **Sozialplan-Abfindung** kollektiv-rechtlich oft günstiger; nicht mit Individualvergleich kombinieren ohne Klärung

## Querverweise

- `fachanwalt-arbeitsrecht-orientierung` — Triage
- `fachanwalt-arbeitsrecht-aufhebungsvertrag-sperrzeit` — Vertiefung
- `fachanwalt-arbeitsrecht-hinschg-whistleblower-repressalie` — Sonderfall

## Quellen und Updates

Stand: 05/2026. § 54 ArbGG, KSchG, SGB III. BAG-Linien zur Faustformel. Bei BAG-Linien-Bildung zur HinSchG-Repressalie-Beweislastumkehr separat.

## Aktuelle Rechtsprechung (Stand Mai 2026)

Vergleichs- und abfindungsrelevante Leitentscheidungen:

- **BAG, 03.06.2025 - 9 AZR 104/24**: Pauschale Erledigungsklausel im Vergleich erfasst den gesetzlichen Mindesturlaub nicht; Mindesturlaub gesondert ausweisen. Quelle: dejure.org-Vernetzung.
- **BAG, 25.03.2026 - 5 AZR 108/25**: Pauschale Freistellungsklausel unwirksam (§ 307 BGB); im Vergleich konkret formulieren. Quelle: dejure.org-Vernetzung.
- **BSG, 12.07.2006 - B 11a AL 47/05 R**: Sperrzeit-Vermeidung bei drohender, objektiv rechtmaessiger betriebsbedingter Kuendigung und eingehaltener Frist; Faustformel-Abfindung (0,25 - 0,5 BMG/Beschaeftigungsjahr) marktueblich. Quelle: dejure.org-Vernetzung.
- Faustformel zur Abfindung: 0,5 BMG x Beschaeftigungsjahre (KSchG-Verhandlungsmaszstab); Verhandlungsspielraum 0,25 - 1,5 BMG je nach Prozesschance, Bestandsrisiko und Alter / Schwerbehinderung.
- Vor Vergleichsabschluss aktuelle Rechtsprechung in offenen Quellen pruefen.

## Paragrafenkette

- § 54 ArbGG — Gütetermin (Pflicht)
- § 9 KSchG — Auflösungsantrag
- § 10 KSchG — Abfindungsobergrenzen (12/15/18 Monatsverdienste)
- § 1a KSchG — gesetzlicher Abfindungsanspruch bei betriebsbedingter Kündigung
- § 779 BGB — Vergleich
- § 794 Abs. 1 Nr. 1 ZPO — vollstreckbarer Prozessvergleich

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

