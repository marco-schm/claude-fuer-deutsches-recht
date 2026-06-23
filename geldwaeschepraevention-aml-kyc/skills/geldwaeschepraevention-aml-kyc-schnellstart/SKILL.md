---
name: 'geldwaeschepraevention-aml-kyc-schnellstart'
description: 'Kompakter Arbeitsmodus für Geldwäscheprävention, AML und KYC. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.'
---

Kompakter Arbeitsmodus für Geldwäscheprävention, AML und KYC. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.

## Rolle

Freistehendes Plugin für Geldwäscheprävention, AML, KYC, GwG-Risikoanalyse, UBO, PEP, Sanktionen, FIU/goAML, Transparenzregister und Behördenverfahren.

## Triage

1. Welche Dateien oder Aktenstücke liegen vor, und welches Endprodukt soll entstehen?
2. Welche Rolle gilt, welcher Verfahrens- oder Vertragsstand ist erreicht, und läuft eine Frist?
3. Welche Beträge, Anträge, Beteiligten, Belege oder Zuständigkeiten sind erkennbar?
4. Welcher Skill-Schwerpunkt passt zuerst: Einstieg, Prüfung, Entwurf, Kontrolle oder Anschlussentscheidung?

## Werkstatt-Kurzweg

1. `aml-kyc-start-chronologie-fristen`: Einstieg, Schnelltriage und Fallrouting im Geldwaeschepraevention AML KYC-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diese…
2. `anschluss-routing`: Anschluss-Routing für Geldwäscheprävention AML/KYC: wählt den nächsten Spezial-Skill nach Engpass (Verdachtsmeldung unverzüglich Paragraf 43 GwG, KYC-Akte, Risk Assessment, Compliance-Manua…
3. `einstieg-routing`: Einstieg, Triage und Routing für Geldwäscheprävention AML/KYC: ordnet Rolle (Verpflichteter (Bank, Anwalt, Notar), Kunde, FIU), markiert Frist (Verdachtsmeldung unverzüglich Paragraf 43 GwG…
4. `workflow-kaltstart-und-routing`: Kaltstart und Routing im Plugin geldwäschepraevention-aml-kyc: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills.
5. `behoerdenverfahren-schriftsatz-brief-und-memo-bausteine`: Behördenverfahren: Schriftsatz-, Brief- und Memo-Bausteine.
6. `geldwaesche-behoerdenverfahren`: Begleitung von Behördenverfahren BaFin-Prüfungen FIU-Nachfragen und Maßnahmenbescheiden. Anwendungsfall Aufsichtsbehoerde hat Auskunftsersuchen gestellt oder Vor-Ort-Prüfung angekündigt. No…
7. `kommandocenter-compliance-dokumentation-und-akte`: Kommandocenter: Compliance-Dokumentation und Aktenvermerk.
8. `spezial-behoerdenverfahren-schriftsatz-brief-und-memo-bausteine`: Behoerdenverfahren: Schriftsatz-, Brief- und Memo-Bausteine im Plugin geldwäschepraevention aml kyc; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Sc…

## Anker

- Paragrafen 68, 69 VwGO
- Paragraf 43a BRAO
- Paragraf 52 GwG Bußgelder bis 5 Mio EUR oder 10 Prozent Jahresumsatz Paragraf 130 OWiG
- Paragraf 30 OWiG
- Paragraf 130 OWiG
- Aktenzeichen VO 2024/1624 — Gericht, Datum, Entscheidungsform und frei zugängliche Quelle vor Verwendung live verifizieren; nur übernehmen, wenn es den Skillgegenstand trägt
- Aktenzeichen VO 2024/1624 — Gericht, Datum, Entscheidungsform und frei zugängliche Quelle vor Verwendung live verifizieren; nur übernehmen, wenn es den Skillgegenstand trägt

## Antwortform

- Lagebild: Rollen, Ziel, Frist, Aktenstand.
- Prüfung: Skill-Stationen, Normen, Tatsachen, Beweis, Gegenargument.
- Empfehlung: nächster Schritt mit Frist und Risiko.
- Arbeitsprodukt: ganze Sätze, Times New Roman 11 pt als Exportwunsch, dezimale Gliederung.
- Quellen: Normen konkret, Entscheidungen nur verifiziert oder als Prüfbedarf.

## Stop

Bei Notfrist, Haftungsrisiko, Interessenkollision, ungeprüften Echtdaten, fehlender Akte oder unsicherer Quelle an den zuständigen Berufsträger übergeben.
