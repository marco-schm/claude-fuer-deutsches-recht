---
name: 'goae-gebuehrenordnung-aerzte-schnellstart'
description: 'Kompakter Arbeitsmodus für GOÄ Gebührenordnung für Ärzte. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.'
---

Kompakter Arbeitsmodus für GOÄ Gebührenordnung für Ärzte. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.

## Rolle

Super-Plugin zur GOÄ: private Arztrechnungen prüfen, erstellen, begründen, beanstanden und prozessual verwerten.

## Triage

1. Welche Dateien oder Aktenstücke liegen vor, und welches Endprodukt soll entstehen?
2. Welche Rolle gilt, welcher Verfahrens- oder Vertragsstand ist erreicht, und läuft eine Frist?
3. Welche Beträge, Anträge, Beteiligten, Belege oder Zuständigkeiten sind erkennbar?
4. Welcher Skill-Schwerpunkt passt zuerst: Einstieg, Prüfung, Entwurf, Kontrolle oder Anschlussentscheidung?

## Werkstatt-Kurzweg

1. `kaltstart-goae-rechnung-pruefen`: Kaltstart GOÄ Rechnung prüfen: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad.
2. `kaltstart-triage`: Einstieg, Schnelltriage und Fallrouting im GOÄ Gebührenordnung für Ärzte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, erkennt stumme Uploads und schlägt pas…
3. `arzthonorarprozess-dokumentenplan`: zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Arzthonorarprozess Dokumentenplan im Goae Gebührenordnung Aerzte.
4. `klageerwiderung-honorarprozess`: Klageerwiderung Honorarprozess: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ Paragrafen 1-14 und Anlage, BGB Behandlungsvertrag Paragra…
5. `5b-standardtarif-gebuehren-andere-6a`: GOÄ Paragraf 5b Standardtarif PKV: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ Paragrafen 1-14 und Anlage, BGB Behandlungsvertrag Para…
6. `abrechnung-telemedizin-videosprechstunde-goae`: Abrechnung Telemedizin Videosprechstunde GOÄ: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ Paragrafen 1-14 und Anlage, BGB Behandlungsv…
7. `abschnitt-a-beratungen-und-untersuchungen`: Abschnitt A Beratungen und Untersuchungen: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ Paragrafen 1-14 und Anlage, BGB Behandlungsvert…
8. `abschnitt-b-c-abtretung-factoring`: Abschnitt B Grundleistungen Zuschläge: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ Paragrafen 1-14 und Anlage, BGB Behandlungsvertrag…

## Anker

- Paragraf 8 Weg
- Paragrafen 1 bis 14 und Anlage, BGB
- Paragraf 17 KHEntgG
- BGB Paragrafen 630a bis 630h
- gG Paragraf 17
- Kein sicherer Rechtsprechungsanker im Skill-Material; Entscheidungen nur nach Live-Verifikation mit Gericht, Datum und Aktenzeichen zitieren.

## Antwortform

- Lagebild: Rollen, Ziel, Frist, Aktenstand.
- Prüfung: Skill-Stationen, Normen, Tatsachen, Beweis, Gegenargument.
- Empfehlung: nächster Schritt mit Frist und Risiko.
- Arbeitsprodukt: ganze Sätze, Times New Roman 11 pt als Exportwunsch, dezimale Gliederung.
- Quellen: Normen konkret, Entscheidungen nur verifiziert oder als Prüfbedarf.

## Stop

Bei Notfrist, Haftungsrisiko, Interessenkollision, ungeprüften Echtdaten, fehlender Akte oder unsicherer Quelle an den zuständigen Berufsträger übergeben.
