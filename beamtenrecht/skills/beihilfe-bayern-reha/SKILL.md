---
name: beihilfe-bayern-reha
description: "Wenn es um Beihilfe für Rehabilitationsleistungen und Kuren nach der Bayerischen Beihilfeverordnung (BayBhV §§ 29–30) geht: unterscheidet AHB, stationäre Reha und Kur, prüft Voranerkennungspflicht, Sperrfristen, Tagessätze und Höchstbeträge; liefert Prüfraster und Antrags-/Widerspruchsbausteine."
---

# Beihilfe Bayern – Rehabilitation und Kur (BayBhV §§ 29–30)

## Arbeitsweg

> ⚠️ **PFLICHT-FETCH vor jeder Antwort:**
> GET https://www.gesetze-bayern.de/Content/Document/BayBhV/true → §§ 29–30 extrahieren
> GET https://www.lff.bayern.de/formulare/beihilfe/ → aktuelle Merkblätter prüfen

- Maßnahmentyp zuerst klären (AHB / stationäre Reha / Kur) — Voranerkennungspflicht hängt davon ab.
- Fristen markieren: Voranerkennung **vor** Antritt (bei Reha > 30 Tage und bei Kur); Widerspruch 1 Monat (VwGO § 70).
- Normen: BayBhV §§ 29–30, § 7 — keine BBhV-Normen übertragen.
- Zuständige Stelle: Bayerisches Landesamt für Finanzen (LfF); Rechtsweg VG Bayern.

## 1. Zweck und Anwendungsfall

Detail-Skill zu Reha- und Kurmaßnahmen der BayBhV. Einstieg über `beihilfe-bayern-baybhv`.

## 2. Eingaben

- Art der Maßnahme (AHB / stationäre Reha / Kur / Mütterkur / ambulante Heilkur)
- Dauer der geplanten Maßnahme (relevant für 30-Tage-Grenze bei Reha)
- Ärztliche Bescheinigung / amtsärztliches Gutachten vorhanden?
- Voranerkennung bereits beantragt oder erteilt?
- Frühere Kuren (für Sperrfrist-Prüfung)
- Kostennachweise und Beihilfebescheid

## 3. Maßnahmentyp-Routing (vor allem anderen)

| Maßnahme | Voranerkennung | Ärztliche Unterlage | Rechtsgrundlage |
|---|---|---|---|
| **AHB** (unmittelbar nach KH-Entlassung) | **Nicht erforderlich** | Ärztliche Bescheinigung: Notwendigkeit + ambulante Alternativen unzureichend | BayBhV § 29 |
| **Stationäre Reha ≤ 30 Tage** | Nicht erforderlich | Fachärztliches Attest: Schwere der Erkrankung erfordert stationäre Behandlung | BayBhV § 29 |
| **Stationäre Reha > 30 Tage** | **Pflicht vor Antritt** — Voranerkennung durch LfF mit medizinischer Begründung | Fachärztliches Attest + detaillierte Begründung | BayBhV § 29 |
| **Kur / ambulante Heilkur** | **Pflicht vor Antritt** | Ärztliche Bescheinigung vor Beginn | BayBhV § 30 |
| **Mütterkur / Mutter-Kind-Kur** | **Pflicht vor Antritt** | Ärztliche Bescheinigung | BayBhV § 30 |
| **Suchtbehandlung** | Keine gesonderte Voranerkennung | Ärztliche Bescheinigung der Notwendigkeit | BayBhV § 29 |

> ⚠️ **Nur für Reha > 30 Tage und Kur gilt Voranerkennungspflicht.**
> AHB und Reha ≤ 30 Tage können ohne vorherige Genehmigung angetreten werden.

## 4. Beihilfefähige Aufwendungen

### AHB und stationäre Reha (§ 29 BayBhV)

| Position | Regelung |
|---|---|
| Ärztliche Leistungen und Pflege | Gesondert berechnete Leistungen vollständig beihilfefähig |
| Unterkunft und Verpflegung | Bis zum **niedrigsten Tagessatz** der Einrichtung |
| An-/Abreise | Entfernungspauschale bis **200 €** |
| Begleitung | Beihilfefähig wenn medizinisch notwendig (auch bei familienorientierter Kinder-Reha) |
| Ärztlicher Entlassungsbericht | Beihilfefähig |
| Ambulante Reha — Fahrtkosten | Bis **10 € pro Behandlungstag** oder tatsächliche km-Erstattung |

**Zugelassene Einrichtungstypen (§ 29):**
1. AHB-Einrichtungen (spezialisierte med. Reha-Einrichtungen nach SGB V-Anforderungen)
2. Suchtbehandlungseinrichtungen
3. Allgemeine med. Rehabilitationseinrichtungen (§ 107 Abs. 2 SGB V)

> ⚠️ **Nachrangigkeit DRV**: Stationäre Reha wird häufig vorrangig von der Deutschen
> Rentenversicherung (DRV) übernommen. Beihilfe ist dann nachrangig — DRV-Antrag prüfen,
> ob DRV zuständig ist. Nur die von der DRV nicht gedeckten Restkosten sind beihilfefähig.

### Kur (§ 30 BayBhV)

| Position | Regelung |
|---|---|
| Gesondert berechnete Leistungen | Beihilfefähig |
| Fahrtkosten | Beihilfefähig |
| Kurtaxe | Beihilfefähig |
| Unterkunft und Verpflegung | Bis **26 € pro Tag** |
| Max. beihilfefähige Dauer | **21 Tage** |
| Wartefrist (Erstantrag) | **5 Jahre** Beihilfeberechtigung |
| Sperrfrist | Keine Kur im laufenden + **2 vorangegangenen** Kalenderjahren |
| Ausnahme Sperrfrist | Schwere chronische Erkrankung mit fachärztlicher Dokumentation |

## 5. Medizinische Notwendigkeit prüfen

- Ambulante Alternativen müssen ausgeschöpft sein (§ 29/30)
- Für Reha: Schwere und Art der Erkrankung müssen stationäre Behandlung erfordern
- Für Kur: Gesundheitszustand erheblich beeinträchtigt; ambulante Behandlung unzureichend
- Wiederholungssperrfristen prüfen (bei Kur: 3-Jahres-Zeitraum)

## 6. Ablehnung/Kürzung angreifen

- Kürzungsgrund identifizieren: fehlende Voranerkennung / medizinische Notwendigkeit / Höchstbetrag / Sperrfrist
- Fehlende Voranerkennung bei AHB: Argument, dass § 29 keine Voranerkennung fordert
- Medizinische Notwendigkeit bestreitet: fachärztliches Gegengutachten beschaffen
- Bei Eilbedürftigkeit: einstweiligen Rechtsschutz VG erwägen

## 7. Quellenpflicht

- Normen: BayBhV §§ 7, 29–30; Art. 96 BayBG.
- Rspr.: BayVGH/BVerwG zu Reha-/Kurbeihilfe — nur nach Live-Check.
- Zitierregeln: `beamtenrecht/references/QUELLEN.md`.

## 8. Ausgabeformat

- Prüfraster: Maßnahmentyp → Voranerkennungsstatus → beihilfefähige Aufwendungen → Betrag.
- Antrag auf Voranerkennung oder Widerspruchsentwurf mit tragenden §§.

## 9. Verifizierte Quellenanker

- BayBhV §§ 29–30: https://www.gesetze-bayern.de/Content/Document/BayBhV/true
- BayBG Art. 96: https://www.gesetze-bayern.de/Content/Document/BayBG
- LfF Formulare: https://www.lff.bayern.de/formulare/beihilfe/
