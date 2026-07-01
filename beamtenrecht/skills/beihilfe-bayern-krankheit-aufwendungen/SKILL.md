---
name: beihilfe-bayern-krankheit-aufwendungen
description: "Wenn es um beihilfefähige Aufwendungen im Krankheitsfall nach der Bayerischen Beihilfeverordnung (BayBhV §§ 7–28) geht: prüft ärztliche, zahnärztliche (inkl. Implantate § 17), psychotherapeutische Leistungen (§§ 10–12), Arznei-/Hilfsmittel, Sehhilfen und Krankenhaus auf Notwendigkeit, Angemessenheit und Ausschlüsse; liefert Prüfraster und Widerspruchsbausteine."
---

# Beihilfe Bayern – Aufwendungen im Krankheitsfall (BayBhV §§ 7–28)

## Arbeitsweg

> ⚠️ **PFLICHT-FETCH vor jeder Antwort:**
> GET https://www.gesetze-bayern.de/Content/Document/BayBhV/true → relevante §§ extrahieren
> GET https://www.lff.bayern.de/formulare/beihilfe/ → Formulare und Merkblätter prüfen
> Keine BBhV-Normen des Bundes auf Bayern übertragen (andere Verordnung, andere Regeln).

- Leistungsart und Kürzungsgrund zuerst klären.
- Fristen: Widerspruch gegen Bescheid **1 Monat** (VwGO § 70); Antragsausschlussfrist live prüfen.
- Zuständige Stelle: LfF; Rechtsweg VG Bayern → BayVGH → BVerwG.
- Dokumente: Rechnungen mit GOÄ/GOZ-Ziffern, ärztliche Verordnung, Beihilfebescheid.

## 1. Zweck und Anwendungsfall

Detail-Skill zu den Krankheitsaufwendungen der BayBhV. Einstieg über `beihilfe-bayern-baybhv`.

## 2. Eingaben

- Leistungsart (ärztlich / zahnärztlich / Psychotherapie / Arznei-Hilfsmittel / Krankenhaus)
- Rechnungen mit Gebührenziffern und Steigerungssätzen
- Ärztliche Verordnung / Notwendigkeitsbescheinigung
- Beihilfebescheid mit Kürzungsbegründung

## 3. Grundsatz der Beihilfefähigkeit (§ 7 BayBhV)

**Drei kumulative Voraussetzungen:**
1. **Medizinisch notwendig** — dem Grunde nach
2. **Wirtschaftlich angemessen** — der Höhe nach (Maßstab: GOÄ/GOZ-Schwellenwert)
3. **Nicht ausdrücklich ausgeschlossen** — Negativliste prüfen

**GOÄ/GOZ-Angemessenheit:** Nur Gebühren bis zum **Schwellenwert des Gebührenrahmens** gelten als angemessen; Überschreitung erfordert schriftliche Begründung durch den Arzt.

### Nicht anerkannte Behandlungsmethoden (§ 7 Abs. 5 BayBhV i. V. m. Anlage 2)

| Kategorie | Regelung |
|---|---|
| **Anlage 2 Nr. 1** | Vollständiger Ausschluss — keine Beihilfe |
| **Anlage 2 Nr. 2** | Teilausschluss mit definierten Ausnahmevoraussetzungen |

> ⚠️ Neue/experimentelle Methoden (z. B. ACP/PRP-Behandlung, Stoßwellentherapie ohne Zulassung,
> Ozontherapie) → **Anlage 2 live prüfen**. Sind sie dort gelistet: kein Beihilfeanspruch.
> Sind sie nicht gelistet: Beihilfefähigkeit nach § 7 Abs. 1 (Notwendigkeit + Angemessenheit) prüfen.
> Bei Unsicherheit: **vor Behandlung schriftlich beim LfF anfragen**.

## 4. Ärztliche Leistungen (§§ 8 ff. BayBhV)

- GOÄ-Leistungen bis Schwellenwert: beihilfefähig
- Überschreitung des Schwellenwerts: nur mit schriftlicher ärztlicher Begründung
- Hausbesuche, Telemedizin: Kosten für Telekommunikationsendgeräte **nicht** beihilfefähig (§ 7)

## 5. Zahnärztliche Leistungen (§§ 14, 17 BayBhV)

### 5a) Zahnersatz / Material- und Laborkosten (§ 14 BayBhV)

> ⚠️ **Häufiger Fehler:** HKP-Pflicht aus GKV- oder BBhV-Praxis auf Bayern übertragen → falsch.

- **Kein Heil- und Kostenplan (HKP) vor Behandlung erforderlich**
- **Material- und Laborkosten** (GOZ § 9, inkl. Edelmetall/Keramik): nur **60 % beihilfefähig**
  Gilt für Leistungen GOZ Anlage 1 Abschn. C (Pos. 2150–2320), F und K
- Zahnarzthonorar (GOZ): nach allgemeinen Regeln beihilfefähig (nicht 60 %-begrenzt)

### 5b) Implantate (§ 17 BayBhV) — Kernregeln

**Grundsatz:** Max. **2 Implantate pro Kieferhälfte** beihilfefähig —
**einschließlich bereits vorhandener Implantate** (Bestandsimplantate zählen mit zur 2er-Grenze).
Kosten für darüber hinausgehende Implantate werden anteilig gekürzt.

**Ausnahmen — volle Beihilfefähigkeit über 2/Kieferhälfte hinaus:**
1. **Angeborene Nichtanlage**: weniger als 8 Zähne pro Kiefer → gutachterliche Feststellung
2. **Schwere Kieferdefekte**: nach Fraktur oder chirurgischer Resektion, Kauffunktion nicht anders wiederherstellbar → gutachterliche Feststellung

**Suprakonstruktionen** (Kronen, Brücken): immer beihilfefähig nach GOZ-Standardsätzen, unabhängig von der Implantatanzahl. 60 %-Regel (§ 14) gilt für Material-/Laborkosten.

**Pflichtformular LfF H930** (verifiziert aus LfF-Originalformular):
- Mit der **Rechnung einzureichen** (nicht vor Behandlung)
- Zahnschema (Befund + Plan/Behandlung) vom Zahnarzt auszufüllen
- Bereits vorhandene Implantate mit Eingliederungsdatum angeben
- Ohne H930: LfF kann 2er-Grenze nicht prüfen → Kürzungsrisiko

> ⚠️ Vor Behandlung: Zahnarzt darauf hinweisen, dass H930 zur Rechnung beizulegen ist.
> Bestandsimplantate in anderen Kieferhälften können neue Beihilfefähigkeit einschränken.

## 6. Psychotherapie (§§ 10–12 BayBhV)

### 6a) Psychosomatische Grundversorgung (§ 10 BayBhV)

| Methode | Kontingent | Format |
|---|---|---|
| Verbale Intervention | bis **25 Sitzungen** | Einzelbehandlung |
| Autogenes Training / Progressive Muskelentspannung | bis **12 Sitzungen** | Einzel oder Gruppe |
| Hypnose | bis **12 Sitzungen** | Einzelbehandlung |

Verbale Intervention und Übungsverfahren dürfen nicht in derselben Sitzung kombiniert werden.

### 6b) Tiefenpsychologische und analytische Therapie (§ 11 BayBhV)

| Altersgruppe | Tiefenpsychologisch | Analytisch | Ausnahme (+) |
|---|---|---|---|
| **Erwachsene (21+)** | 60 Einzel / 60 Gruppe | 160 Einzel / 80 Gruppe | +40 / +140 |
| **Jugendliche (14–20)** | 90 Einzel / 60 Gruppe | 90 Einzel / 60 Gruppe | +90 |
| **Kinder (< 14)** | 70 Einzel / 60 Gruppe | 70 Einzel / 60 Gruppe | +80 |

Therapiebeginn vor 21 Jahren kann nach Volljährigkeit fortgeführt werden.
EMDR: zusätzliche Weiterbildung in Traumatherapie erforderlich.

### 6c) Verhaltenstherapie (§ 12 BayBhV)

| Format | Kontingent | Ausnahme |
|---|---|---|
| Einzelbehandlung | **60 Sitzungen** | +20 Sitzungen |
| Gruppenbehandlung | **60 Sitzungen** | +20 Sitzungen |

Gilt für alle Altersgruppen; Therapeutenqualifikation nach § 12 erforderlich.

> ⚠️ Voranerkennungsvoraussetzungen für Psychotherapie: BayBhV §§ 10–12 und
> LfF-Merkblatt live prüfen — Fristen und Antragsverfahren können sich ändern.

## 7. Arznei- und Verbandmittel (§ 18 BayBhV)

**Beihilfefähig:**
- Verschreibungspflichtige Arzneimittel nach Apothekengesetz
- Verbandmittel
- Urin- und Blutteststreifen
- Medizinprodukte zur Anwendung am Menschen (verordnungspflichtig in Textform)
- Hormonelle Verhütungsmittel / IUDs: bis **22 Jahre**; danach nur bei medizinischer Indikation

**Nicht beihilfefähig (§ 18 BayBhV):**
- Mittel gegen Erektionsstörungen, Raucherentwöhnung, Gewichtsreduktion, Haarwuchs
- Alltagsersatzprodukte
- Vitaminsupplemente (außer als zugelassenes Arzneimittel)
- Geriatrika und Tonika

## 8. Hilfsmittel (§ 21 BayBhV)

**Beihilfefähig (Positivliste Anlage 4):**
- Selbstbehandlungs- und Überwachungsgeräte
- Körperersatzstücke (Prothesen)
- Perücken bei krankheitsbedingtem Haarausfall
- Digitale Gesundheitsanwendungen (DiGA) aus offiziellen Registern
- Einweisung in die Nutzung des Hilfsmittels

**Besonderheiten:**
- Verordnung in Textform durch Arzt erforderlich
- Hörgeräte: **4-Jahres-Sperrfrist** für Ersatz (Ausnahme: funktioneller Rückgang)
- Miete: nur beihilfefähig, wenn Mietkosten ≤ Kaufpreis
- Batterien, Linsenreiniger, Geräteschutz: grundsätzlich nicht beihilfefähig
- Nicht gelistete Hilfsmittel > 600 €: Entscheidung durch LfF

## 9. Krankenhausleistungen (§ 28 BayBhV)

**Zugelassene Krankenhäuser (§ 108 SGB V):**
- Vor- und nachstationäre Behandlung: beihilfefähig
- Vollstationäre allgemeine Krankenhausleistungen: beihilfefähig
- **Wahlleistungen** (mit Eigenbeteiligung nach BayBG Art. 96):
  - Gesondert berechnete wahlärztliche Leistungen (Chefarzt/Wahlarzt)
  - Zweibettzimmer

**Nicht zugelassene Krankenhäuser:**
- DRG-Fälle: Basisfallwert × DRG-Bewertungsrelation + Pflegezuschlag
- Sonstige Fälle: vollstationär bis **324,63 € pro Tag**
- Notfallbehandlung im nächstgelegenen geeigneten KH: beihilfefähig

**Unterkunft bei auswärtiger ambulanter Behandlung (§ 27 BayBhV):**
- Bis **26 € pro Tag** (inkl. notwendige Begleitperson)

## 10. Kürzung angreifen

- Kürzungsgrund identifizieren: fehlende Notwendigkeit / Angemessenheit / Ausschluss / Formfehler
- GOÄ/GOZ-Überschreitung: ärztliche Begründung nachholen oder Widerspruch mit Attest
- Nicht anerkannte Methode: Anlage 2 prüfen; ggf. § 7 Abs. 1 argumentieren
- Widerspruchsfrist: **1 Monat** nach Bescheid (VwGO § 70)

## 11. Quellenpflicht

- Normen: BayBhV §§ 7–28; Art. 96 BayBG; GOÄ/GOZ.
- Rspr.: BayVGH/BVerwG — nur nach Live-Check.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`.

## 12. Ausgabeformat

- Prüfraster je Aufwendung: notwendig? angemessen? Ausschluss? beihilfefähiger Betrag?
- Widerspruchsentwurf gegen Kürzung mit tragenden §§.

## 13. Verifizierte Quellenanker

- BayBhV: https://www.gesetze-bayern.de/Content/Document/BayBhV/true
- BayBG Art. 96: https://www.gesetze-bayern.de/Content/Document/BayBG
- LfF Formular H930 (Implantate): https://www.lff.bayern.de/media/v5yeafuj/h930-ergaenzende-angaben-bei-versorgung-mit-implantaten.pdf
- LfF Formulare allgemein: https://www.lff.bayern.de/formulare/beihilfe/
