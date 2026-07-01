---
name: beihilfe-bayern-baybhv
description: "Wenn es um Beihilfe für bayerische Beamte nach der Bayerischen Beihilfeverordnung (BayBhV) geht: klärt Beihilfeberechtigung, Bemessungssatz, Personenkreis und Krankenversicherungsart (PKV/GKV freiwillig/GKV Pflicht) inkl. Tarifbeschäftigte und Angehörige; liefert Prüfraster, Fristen-/Risikoampel und Sofortschritte mit Antrags- oder Widerspruchsentwurf."
---

# Beihilfe Bayern (BayBhV)

## Arbeitsweg

> ⚠️ **PFLICHT-FETCH vor jeder Antwort** — Normen nicht aus Modellwissen zitieren:
> 1. GET https://www.gesetze-bayern.de/Content/Document/BayBhV/true → relevante §§ extrahieren
> 2. GET https://www.lff.bayern.de/formulare/beihilfe/ → aktuelle Formulare und Merkblätter prüfen
> 3. Erst danach antworten.

- Rolle klären: Wer handelt (Beamter, Ruhestandsbeamter, Hinterbliebener, Angehöriger, Tarifbeschäftigter), welche KV-Art, welcher Output (Antrag, Widerspruch, Klage, Beratung)?
- Fristen zuerst markieren: Widerspruch 1 Monat (VwGO § 70); Klage 1 Monat nach Widerspruchsbescheid; Antragsausschlussfrist BayBhV live prüfen.
- **Keine BBhV-Normen auf Bayern übertragen** — BayBhV und BBhV sind eigenständige Verordnungen.
- Zuständige Stelle: Bayerisches Landesamt für Finanzen (LfF); Rechtsweg VG Bayern → BayVGH → BVerwG.

## 1. Zweck und Anwendungsfall

Einstiegs- und Kern-Skill für die Beihilfe bayerischer Beamter, Ruhestandsbeamter, Richter und ihrer berücksichtigungsfähigen Angehörigen nach der **Bayerischen Beihilfeverordnung (BayBhV)**. Grenzt Landesrecht Bayern sauber vom Bundesrecht (BBhV) ab und verweist für Detailfragen auf die thematischen Bayern-Skills.

## 2. Abgrenzung Bund/Bayern

- Bayerische Beamte richten sich **ausschließlich** nach der BayBhV, nicht nach der BBhV des Bundes.
- Bund-Beihilfe-Skills nur als Systematikvergleich — nie als bayerische Norm zitieren.
- Für andere Länder: `landesrecht-16-laender-routenplan`.

## 3. Eingaben

- Statusgruppe (aktiver Beamter / Ruhestand / Hinterbliebener / Angehöriger / Tarifbeschäftigter)
- Krankenversicherungsart (PKV Restkostenversicherung / GKV freiwillig / GKV Pflicht)
- Art der Aufwendung (Krankheit, Zahnbehandlung, Arznei-/Hilfsmittel, Krankenhaus, Reha, Pflege)
- Bemessungssatz laut Bescheid und PKV-Tarif
- Beihilfebescheid und Rechnungen
- Datum von Aufwendung, Rechnung, Bescheid und Zugang (für Fristen)

## 3a. Pflicht-Routing: Statusgruppe × Krankenversicherungsart

> ⚠️ Diesen Block **vor §§ 7 ff.** abarbeiten. Beihilfeanspruch und Bemessungssatz hängen
> nicht allein von der BayBhV ab, sondern von der Kombination aus Statusgruppe und KV-Art.
> Rechtsquellen: BayBhV §§ 2, 3, 46; BayBG Art. 96; §§ 249/257 SGB V; TV-L Bayern.
> Alle Beträge und Sätze über gesetze-bayern.de live verifizieren.

### Schritt 1 — Statusgruppe feststellen (BayBhV § 2)

- **(A) Aktiver Beamter / Ruhestandsbeamter / Richter / Hinterbliebener (Witwe/Waise)**
  → Beihilfeberechtigung dem Grunde nach gegeben → weiter mit Schritt 2A
- **(B) Tarifbeschäftigter des Freistaats Bayern**
  → Kein Beihilfeanspruch nach BayBhV → weiter mit Schritt 2B
- **(C) Berücksichtigungsfähiger Angehöriger (BayBhV § 3)**
  → Ehegatte/Lebenspartner oder im Familienzuschlag berücksichtigtes Kind
  → Keine Einkommensgrenze (§ 4 BayBhV aufgehoben); KV-Art des Angehörigen entscheidend
  → weiter mit Schritt 2C

> ⚠️ Nicht beihilfeberechtigt nach § 2: Ehrenbeamte, Dienstverhältnisse unter 1 Jahr, Europaparlamentarier.

---

### Schritt 2A — Beamter: Krankenversicherungsart

| KV-Art | Beihilfeanspruch | Hinweis | Rechtsquelle |
|---|---|---|---|
| **PKV Restkostenversicherung** | Ja, voll nach Bemessungssatz (Schritt 3) | Ziel: Beihilfe + PKV = 100 % | BayBhV § 46; BayBG Art. 96 |
| **GKV freiwillig versichert** | Ja — nur **Restkosten**: Beihilfe erstattet was GKV nicht übernimmt (Differenzkostenerstattung, 100 %) | GKV-Erstattungsnachweis vor Antrag einholen; verbleibender Betrag oft gering | BayBhV § 46 |
| **GKV pflichtversichert** | Nur bei bestimmten Beamtengruppen (z. B. Beamte auf Widerruf unter Jahresarbeitsentgeltgrenze) | Im Regelfall kein Anspruch — § 2 BayBhV live prüfen | BayBhV § 2 |

> ⚠️ Sonderfall Vorerkrankungsausschluss (§ 46 BayBhV): Ist eine Erkrankung vom PKV-Tarif
> ausgeschlossen, erhöht sich der Bemessungssatz um **20 Prozentpunkte** (max. 90 %), sofern
> das Versicherungsunternehmen die Anforderungen des SGB V erfüllt.

---

### Schritt 2B — Tarifbeschäftigter: Krankenversicherungsart

| KV-Art | Leistung des Arbeitgebers | Rechtsquelle |
|---|---|---|
| **PKV** | Zuschuss = Hälfte der gesetzlichen Beitragssätze, max. Hälfte des tatsächlichen PKV-Beitrags | § 257 Abs. 2 SGB V |
| **GKV freiwillig** | Zuschuss wie bei Pflichtversicherung | § 257 Abs. 1 SGB V |
| **GKV pflichtversichert** | Hälftige Beitragstragung | § 249 SGB V; TV-L |

> ⚠️ Tarifbeschäftigte erhalten **keine Beihilfe nach BayBhV** — weder PKV noch GKV.
> Der Freistaat erfüllt seine Fürsorgepflicht über den KV-Arbeitgeberzuschuss (SGB V).
> Ausnahme: Einzelvertragliche Sonderregelungen — Arbeitsvertrag und TV-L live prüfen.

---

### Schritt 2C — Berücksichtigungsfähiger Angehöriger (BayBhV § 3)

**Wer ist berücksichtigungsfähig?**
- Ehegatte oder Lebenspartner
- Im Familienzuschlag (BayBesG) berücksichtigte Kinder
- Kinder in weiterer Ausbildung nach erstem Abschluss (§ 3 Abs. 2)

**Nicht berücksichtigungsfähig:** Geschwister; Angehörige beihilfeberechtigter Waisen (§ 3 Abs. 3)

> ⚠️ § 4 BayBhV ist **aufgehoben** — es gibt keine Einkommensgrenze mehr für Ehegatten/Lebenspartner.

| KV-Art des Angehörigen | Beihilfefähigkeit | Hinweis |
|---|---|---|
| **PKV** | Ja — Bemessungssatz des Beamten gilt (Schritt 3) | Regelfall |
| **GKV freiwillig** | Ja — nur Restkosten (Differenzkostenerstattung) | GKV-Erstattungsnachweis erforderlich |
| **GKV pflichtversichert** | Eingeschränkt — § 3 BayBhV live prüfen | GKV deckt i. d. R. ab; Beihilfe für verbleibende Aufwendungen prüfen |

---

### Schritt 3 — Bemessungssatz (BayBhV § 46 i. V. m. BayBG Art. 96)

| Personengruppe | Bemessungssatz |
|---|---|
| Beamter ohne berücksichtigungsfähige Angehörige | **50 %** |
| Beamter mit berücksichtigungsfähigen Angehörigen | **70 %** |
| Versorgungsempfänger / Witwen / Witwer / Waisen | **70 %** |
| Berücksichtigungsfähige Kinder | **80 %** |
| Vorerkrankungsausschluss durch PKV (§ 46 BayBhV) | **+20 PP** (max. 90 %) |

> Ziel: Beihilfe + PKV/GKV-Restkosten = 100 % der beihilfefähigen Aufwendungen.

---

### Erst nach diesem Routing weiter mit §§ 7 ff. (Aufwendungsart)

## 4. Aufwendungsart zuordnen — Detail-Skill wählen

- Krankheitsfälle §§ 8–28 → `beihilfe-bayern-krankheit-aufwendungen`
- Reha/Kur §§ 29–30 → `beihilfe-bayern-reha`
- Pflege §§ 31–40 → `beihilfe-bayern-pflege`
- Sonstige Fälle §§ 41–45 (Geburt, Impfung, Vorsorge) → hier prüfen

## 5. Verfahren und Fristen (BayBhV §§ 46 ff.)

- Antragsausschlussfrist: BayBhV live prüfen
- Widerspruch gegen Bescheid: **1 Monat** (VwGO § 70)
- Klage vor VG: **1 Monat** nach Widerspruchsbescheid
- Zuständigkeit: LfF (Festsetzungsstelle)

## 6. Quellenpflicht

- Normen: BayBhV; Art. 96, Art. 86a BayBG; SGB XI (Pflege); §§ 249/257 SGB V (Tarifbeschäftigte); GOÄ/GOZ (Angemessenheit).
- Rspr.: BayVGH und BVerwG — nur nach Live-Check mit Gericht, Datum, Aktenzeichen und freier Quelle.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`; keine BBhV-Normen, keine Blindzitate.

## 7. Ausgabeformat

- Prüfraster Beihilfefähigkeit Bayern mit Bemessungssatz und Fristen-/Risikoampel.
- Bei Streit: Widerspruchs- oder Klageentwurf mit tragenden BayBhV-§§.

## 8. Verifizierte Quellenanker

- BayBhV: https://www.gesetze-bayern.de/Content/Document/BayBhV/true
- BayBG (Art. 86a, Art. 96): https://www.gesetze-bayern.de/Content/Document/BayBG
- LfF Formulare und Merkblätter: https://www.lff.bayern.de/formulare/beihilfe/
