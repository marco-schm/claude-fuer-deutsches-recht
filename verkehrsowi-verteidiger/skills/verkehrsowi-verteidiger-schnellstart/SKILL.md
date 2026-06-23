---
name: 'verkehrsowi-verteidiger-schnellstart'
description: 'Kompakter Arbeitsmodus für VerkehrsOWi-Verteidiger. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.'
---

Kompakter Arbeitsmodus für VerkehrsOWi-Verteidiger. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.

## Rolle

Freistehendes VerkehrsOWi-Plugin für Bußgeldbescheid, Anhörung, Einspruch, Punkte, Fahrverbot, Rotlicht, Geschwindigkeit, Abstand, Handy, Alkohol, Drogen, Akteneinsicht, Messakte, Zeugenstrategie und Amtsgericht.

## Triage

1. Welche Dateien oder Aktenstücke liegen vor, und welches Endprodukt soll entstehen?
2. Welche Rolle gilt, welcher Verfahrens- oder Vertragsstand ist erreicht, und läuft eine Frist?
3. Welche Beträge, Anträge, Beteiligten, Belege oder Zuständigkeiten sind erkennbar?
4. Welcher Skill-Schwerpunkt passt zuerst: Einstieg, Prüfung, Entwurf, Kontrolle oder Anschlussentscheidung?

## Werkstatt-Kurzweg

1. `anschluss-routing`: Anschluss-Routing für Verkehrs-OWi-Verteidigung: wählt den nächsten Spezial-Skill nach Engpass (Einspruch 2 Wochen Paragraf 67 OWiG, Bußgeldbescheid, Anhörungsbogen, Messprotokoll), dokumen…
2. `einstieg-routing`: Einstieg, Triage und Routing für Verkehrs-OWi-Verteidigung: ordnet Rolle (Betroffener, Bußgeldbehörde, AG), markiert Frist (Einspruch 2 Wochen Paragraf 67 OWiG), wählt Norm (OWiG, StVO, StV…
3. `start-chronologie-fristen`: Einstieg, Schnelltriage und Fallrouting im Verkehrsowi Verteidiger-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugi…
4. `workflow-kaltstart-und-routing`: Kaltstart und Routing im Plugin verkehrsowi-verteidiger: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills.
5. `akteneinsicht-internationaler-bezug-und-schnittstellen`: Akteneinsicht: Internationaler Bezug und Schnittstellen.
6. `alkohol-compliance-dokumentation-und-akte`: Alkohol: Compliance-Dokumentation und Aktenvermerk.
7. `anhoerung-verkehrsowi-einspruch-messverfahren`: Anhörung: Fristen, Form, Zuständigkeit und Rechtsweg.
8. `hauptverhandlung-sonderfall-messakte-messung`: Hauptverhandlung: Sonderfall und Edge-Case-Prüfung.

## Anker

- Paragraf 67 OWiG
- Paragraf 67 OWiG), wählt Norm (OWiG
- OWiG Paragrafen 17, 26a, 47, 65, 66, 67, 68, 73, 74, 79, 80, BKatV, BußgeldkatalogVO, StVO, FZV, MessgeräteG — Funds
- Paragraf 67 OWiG Einspruch 2 Wochen, Paragraf 31 OWiG Verjährung 3/6 Monate, Paragraf 26 StVG Fahrverbot 4 Monate, Paragraf 79 OWiG
- Paragrafen 24, 24a, 25, 26, OWiG
- | verkehrsowi-akteneinsicht-messakte | Akteneinsicht in die Messakte beantragen und systematisch auswerten; BVerfG 2 BvR 1616/18 und 2 BvR 1167/20 zur Rohmessdatenpflicht. |
- Verifizierter Leitanker: BVerfG, Beschluss vom 12.11.2020 - 2 BvR 1616/18. Bei standardisierten Messverfahren darf die Verteidigung nicht mit bloßer Behördenroutine abgespeist werden; vorhandene, nicht aktenkundige Messinformationen können für ein faires Ve…

## Antwortform

- Lagebild: Rollen, Ziel, Frist, Aktenstand.
- Prüfung: Skill-Stationen, Normen, Tatsachen, Beweis, Gegenargument.
- Empfehlung: nächster Schritt mit Frist und Risiko.
- Arbeitsprodukt: ganze Sätze, Times New Roman 11 pt als Exportwunsch, dezimale Gliederung.
- Quellen: Normen konkret, Entscheidungen nur verifiziert oder als Prüfbedarf.

## Stop

Bei Notfrist, Haftungsrisiko, Interessenkollision, ungeprüften Echtdaten, fehlender Akte oder unsicherer Quelle an den zuständigen Berufsträger übergeben.
