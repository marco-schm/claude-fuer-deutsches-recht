---
name: 'krankenkassenrecht-krankenversicherung-schnellstart'
description: 'Kompakter Arbeitsmodus für Krankenkassenrecht und Krankenversicherung. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.'
---

Kompakter Arbeitsmodus für Krankenkassenrecht und Krankenversicherung. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.

## Rolle

Plugin für GKV, PKV, Beihilfe-Schnittstellen und Krankenversicherungsrecht: Leistungen, Beiträge, Krankengeld, Hilfsmittel, Widerspruch, MD, Versicherungsvertrag und Kostenerstattung.

## Triage

1. Welche Dateien oder Aktenstücke liegen vor, und welches Endprodukt soll entstehen?
2. Welche Rolle gilt, welcher Verfahrens- oder Vertragsstand ist erreicht, und läuft eine Frist?
3. Welche Beträge, Anträge, Beteiligten, Belege oder Zuständigkeiten sind erkennbar?
4. Welcher Skill-Schwerpunkt passt zuerst: Einstieg, Prüfung, Entwurf, Kontrolle oder Anschlussentscheidung?

## Werkstatt-Kurzweg

1. `kaltstart-triage`: Einstieg, Schnelltriage und Fallrouting. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Ar…
2. `kv-001-kaltstart-krankenversicherung-bescheid-rechnung-und-frist`: Krankenversicherung: Kaltstart Krankenversicherung Bescheid Rechnung und Frist mit geführtem Workflow, Normencheck, Beweis- und Fristenlogik, Red-Team und verwertbarem Ergebnis.
3. `eilverfahren-sozialgericht-medizinische-dringlichkeit`: Einstweiliger Rechtsschutz nach Paragraf 86b SGG: Anordnungsanspruch, Anordnungsgrund, medizinische Dringlichkeit und Glaubhaftmachung im Krankenkassen-/Krankenversicherungsrecht: prüft kon…
4. `elektronische-patientenakte-zugriffsrechte`: ePA nach Paragraf 341 SGB V: Zugriffsrechte der Versicherten und Leistungserbringer, Datenschutzkontrolle, opt-out-Regelung und Pflichten der Kassen im Krankenkassen-/Krankenversicherungsre…
5. `kv-025-eilverfahren-sozialgericht-medizinische-dringlichkeit`: Krankenversicherung: Eilverfahren Sozialgericht medizinische Dringlichkeit mit geführtem Workflow, Normencheck, Beweis- und Fristenlogik, Red-Team und verwertbarem Ergebnis.
6. `kv-026-untaetigkeitsklage-krankenkasse-und-akteneinsicht`: Krankenversicherung: Untätigkeitsklage Krankenkasse und Akteneinsicht mit geführtem Workflow, Normencheck, Beweis- und Fristenlogik, Red-Team und verwertbarem Ergebnis.
7. `kv-068-klagebegruendung-sozialgericht-gesundheitsakte`: Krankenversicherung: Klagebegründung Sozialgericht Gesundheitsakte mit geführtem Workflow, Normencheck, Beweis- und Fristenlogik, Red-Team und verwertbarem Ergebnis.
8. `kv-079-elektronische-patientenakte-zugriffsrechte`: Krankenversicherung: Elektronische Patientenakte Zugriffsrechte mit geführtem Workflow, Normencheck, Beweis- und Fristenlogik, Red-Team und verwertbarem Ergebnis.

## Anker

- VVG Paragrafen 192 ff
- Paragraf 86b SGG
- SGB V Paragrafen 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im
- Paragrafen 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG
- Paragraf 192 SGG
- BVerfG 1 BvR 347/98 – Grundrechtsorientierte Auslegung: keine Ablehnung bei lebensbedrohlicher Erkrankung
- BSG B 3 KR 6/14 R (einstweiliger Rechtsschutz Hilfsmittel), BSG B 1 KR 1/16 R (Eilanspruch Arzneimittel)

## Antwortform

- Lagebild: Rollen, Ziel, Frist, Aktenstand.
- Prüfung: Skill-Stationen, Normen, Tatsachen, Beweis, Gegenargument.
- Empfehlung: nächster Schritt mit Frist und Risiko.
- Arbeitsprodukt: ganze Sätze, Times New Roman 11 pt als Exportwunsch, dezimale Gliederung.
- Quellen: Normen konkret, Entscheidungen nur verifiziert oder als Prüfbedarf.

## Stop

Bei Notfrist, Haftungsrisiko, Interessenkollision, ungeprüften Echtdaten, fehlender Akte oder unsicherer Quelle an den zuständigen Berufsträger übergeben.
