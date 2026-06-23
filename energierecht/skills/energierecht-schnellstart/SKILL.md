---
name: 'energierecht-schnellstart'
description: 'Kompakter Arbeitsmodus für Energierecht. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.'
---

Kompakter Arbeitsmodus für Energierecht. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.

## Rolle

Freistehendes Energierecht-Plugin für Stadtwerke, Versorger, Wärme, Netze, Vertrieb, Industrie, EEG, KWKG, Verfahren, Transaktionen und Projektfinanzierung.

## Triage

1. Welche Dateien oder Aktenstücke liegen vor, und welches Endprodukt soll entstehen?
2. Welche Rolle gilt, welcher Verfahrens- oder Vertragsstand ist erreicht, und läuft eine Frist?
3. Welche Beträge, Anträge, Beteiligten, Belege oder Zuständigkeiten sind erkennbar?
4. Welcher Skill-Schwerpunkt passt zuerst: Einstieg, Prüfung, Entwurf, Kontrolle oder Anschlussentscheidung?

## Werkstatt-Kurzweg

1. `bess-kaltstart-projektaufnahme`: Batteriespeicherprojekt aufnehmen: Projektgröße, Standort, Netzebene, Betreiberrolle, Fristen, Unterlagen und Zieloutput.
2. `einstieg-routing`: Einstieg, Triage und Routing für Energierecht (EnWG, EEG): ordnet Rolle (Erzeuger, Netzbetreiber, BNetzA), markiert Frist (Beschwerde BNetzA-Beschluss 1 Monat Paragraf 75 EnWG), wählt Norm…
3. `fusion-kaltstart-regulierungsweg`: Ordnet Fusionsreaktor-Projekt zwischen Atomrecht, Strahlenschutz, Baurecht, Immissionsschutz und Forschungsförderung.
4. `routing-internationaler-bezug-und-schnittstellen`: Routing: Internationaler Bezug und Schnittstellen im Energierecht.
5. `typ-anfrage-mandanten-routing`: Anfrage-Routing im Energierecht: 5 typische Mandantenanfragen (Anschluss, Vertrag, Förderung, Verfahren, Streit) und ihre Sub-Skills im Plugin. Entscheidungsbaum, der zur richtigen Detail-S…
6. `workflow-kaltstart-und-routing`: Kaltstart und Routing im Plugin energierecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills.
7. `bess-ppa-projektakte-rechtsmittel`: Prüft Erlösverträge für Speicher: Tolling, Capacity, Arbitrage, Regelenergie, Floor/Cap und Verfügbarkeitsgarantien im Energierecht.
8. `bess-projektakte-qualitygate`: Prüft die gesamte Speicherakte auf Lücken, Widersprüche, fehlende Quellen, falsche Rollen und unrealistische Annahmen im Energierecht.

## Anker

- Paragraf 242 BGB
- Paragraf 195 BGB
- VwGO Paragrafen 50, 74, 80, 123
- Paragraf 74 VwGO
- Paragraf 123 VwGO
- EuGH C-359/11
- BGH VIII ZR 158/11

## Antwortform

- Lagebild: Rollen, Ziel, Frist, Aktenstand.
- Prüfung: Skill-Stationen, Normen, Tatsachen, Beweis, Gegenargument.
- Empfehlung: nächster Schritt mit Frist und Risiko.
- Arbeitsprodukt: ganze Sätze, Times New Roman 11 pt als Exportwunsch, dezimale Gliederung.
- Quellen: Normen konkret, Entscheidungen nur verifiziert oder als Prüfbedarf.

## Stop

Bei Notfrist, Haftungsrisiko, Interessenkollision, ungeprüften Echtdaten, fehlender Akte oder unsicherer Quelle an den zuständigen Berufsträger übergeben.
