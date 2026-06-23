---
name: 'zwangsvollstreckung-schnellstart'
description: 'Kompakter Arbeitsmodus für Zwangsvollstreckung. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.'
---

Kompakter Arbeitsmodus für Zwangsvollstreckung. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.

## Rolle

Plugin Zwangsvollstreckung Paragrafen 704 ff. ZPO: Mahn-/Vollstreckungsbescheid, PfÜB Bank/Arbeit, Paragraf 802l Kontensuche, Vermögensauskunft, Räumung, Paragraf 800 ZPO Notar, Paragraf 201 InsO, ZVG, EU-Kontenpfändung VO 655/2014, Paragraf 765a Härtefall, Schuldnerschutz.

## Triage

1. Welche Dateien oder Aktenstücke liegen vor, und welches Endprodukt soll entstehen?
2. Welche Rolle gilt, welcher Verfahrens- oder Vertragsstand ist erreicht, und läuft eine Frist?
3. Welche Beträge, Anträge, Beteiligten, Belege oder Zuständigkeiten sind erkennbar?
4. Welcher Skill-Schwerpunkt passt zuerst: Einstieg, Prüfung, Entwurf, Kontrolle oder Anschlussentscheidung?

## Werkstatt-Kurzweg

1. `anschluss-routing`: Anschluss-Routing für Zwangsvollstreckung: wählt den nächsten Spezial-Skill nach Engpass (Erinnerung Paragraf 766 ZPO 2 Wochen, Vollstreckungstitel, Pfändungs- und Überweisungsbeschluss (Pf…
2. `einstieg-routing`: Einstieg, Triage und Routing für Zwangsvollstreckung: ordnet Rolle (Gläubiger, Schuldner, Drittschuldner (Arbeitgeber, Bank)), markiert Frist (Erinnerung Paragraf 766 ZPO 2 Wochen), wählt N…
3. `start-chronologie-fristen`: Einstieg, Schnelltriage und Fallrouting im Zwangsvollstreckung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vo…
4. `workflow-kaltstart-und-routing`: Kaltstart und Routing im Plugin zwangsvollstreckung: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills.
5. `raeumung-compliance-dokumentation-und-akte`: Raeumung: Compliance-Dokumentation und Aktenvermerk im Zwangsvollstreckung.
6. `workflow-chronologie-und-belegmatrix`: Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Zwangsvollstreckung.
7. `workflow-fristen-und-risikoampel`: Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Zwangsvollstreckung.
8. `workflow-redteam-qualitygate`: Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Zwangsvollstreckung.

## Anker

- Paragraf 766 ZPO
- Paragraf 766 ZPO 2 Wochen), wählt Norm (ZPO Paragrafen 704 bis 945 (Vollstreckung), GVGA, InsO
- Paragraf 201 InsO, ZVG, EU, Paragraf 765a H, Paragraf 800 ZPO
- Paragraf 800 ZPO
- Paragraf 201 InsO
- Aktenzeichen C-555/18 — Gericht, Datum, Entscheidungsform und frei zugängliche Quelle vor Verwendung live verifizieren; nur übernehmen, wenn es den Skillgegenstand trägt
- Problem : BGH VII ZB 14/20 vom 15.07.2021, NJW 2021, 3046 – Beschluss auf dejure.org nicht auffindbar (NOT_FOUND). Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=15.07.2021&Aktenzeichen=VII+ZB+14%2F20

## Antwortform

- Lagebild: Rollen, Ziel, Frist, Aktenstand.
- Prüfung: Skill-Stationen, Normen, Tatsachen, Beweis, Gegenargument.
- Empfehlung: nächster Schritt mit Frist und Risiko.
- Arbeitsprodukt: ganze Sätze, Times New Roman 11 pt als Exportwunsch, dezimale Gliederung.
- Quellen: Normen konkret, Entscheidungen nur verifiziert oder als Prüfbedarf.

## Stop

Bei Notfrist, Haftungsrisiko, Interessenkollision, ungeprüften Echtdaten, fehlender Akte oder unsicherer Quelle an den zuständigen Berufsträger übergeben.
