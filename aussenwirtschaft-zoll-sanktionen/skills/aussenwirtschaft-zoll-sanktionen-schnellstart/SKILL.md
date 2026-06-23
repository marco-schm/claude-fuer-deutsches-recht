---
name: 'aussenwirtschaft-zoll-sanktionen-schnellstart'
description: 'Kompakter Arbeitsmodus für Außenwirtschaft, Sanktionen, Zoll und CBAM. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.'
---

Kompakter Arbeitsmodus für Außenwirtschaft, Sanktionen, Zoll und CBAM. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.

## Rolle

Freistehendes Plugin für Außenwirtschaft, Sanktionen, Zoll, Exportkontrolle, BAFA, TARIC, CBAM, Verbrauchsteuer, AWV, AML/KYC und Ermittlungen.

## Triage

1. Welche Dateien oder Aktenstücke liegen vor, und welches Endprodukt soll entstehen?
2. Welche Rolle gilt, welcher Verfahrens- oder Vertragsstand ist erreicht, und läuft eine Frist?
3. Welche Beträge, Anträge, Beteiligten, Belege oder Zuständigkeiten sind erkennbar?
4. Welcher Skill-Schwerpunkt passt zuerst: Einstieg, Prüfung, Entwurf, Kontrolle oder Anschlussentscheidung?

## Werkstatt-Kurzweg

1. `kaltstart-triage`: Einstieg, Schnelltriage und Fallrouting im Aussenwirtschaft Zoll Sanktionen-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus die…
2. `aussenwirtschaft-versandverfahren-ncts`: Unionszollkodex-Versandverfahren (T1/T2) im NCTS (New Computerised Transit System): Eroeffffnung Sicherheitsleistung Transit-Begleitdokument (TAD) Bestimmungsstelle und Freigabe. Besonderhe…
3. `aussenwirtschaft-zollverfahren-bewilligungen`: Zollverfahren und Bewilligungen nach UZK Artikel 211: Uebersicht aktive und passive Veredelung Zolllager Voruebergehende Verwendung Versandverfahren und Endverwendung. Bewilligungsvorausset…
4. `allgemeingenehmigung-agg-antidumping`: Allgemeine Genehmigungen nach AWV: Auffinden und Prüfen der passenden Allgemeingenehmigung (AGG) für kontrollierte Ausfuhren ohne Einzelgenehmigung. Beruecksichtigt EU-Ausfuhrgenehmigungen…
5. `asset-freeze-atlas-ausfuhranmeldung-audit`: Sofortmassnahmen bei Verdacht auf sanktionierten Besitz oder Kontrollverhaeltnis: Einfrieren von Geldern und wirtschaftlichen Ressourcen nach Artikel 2 VO (EU) 269/2014 und Artikel 4 VO (EU…
6. `aussenwirtschaft-abfallverbringung`: Grenzueberschreitende Abfallverbringung nach EU-AbfVerbrV (VO 1013/2006 bzw. VO 1418/2007) und KrWG: Notifizierungsverfahren für Abfaelle der Gruenen/Gelben/Roten Liste, Genehmigungspflicht…
7. `aussenwirtschaft-aeo-bewilligung-monitoring`: AEO-Zugelassener-Wirtschaftsbeteiligter-Bewilligung (Customs Simplification/Security/Full): Monitoring laufender Bewilligungsbedingungen nach Artikel 38-39 UZK und AEOC/AEOS/AEOF. Prüft reg…
8. `aussenwirtschaft-aktive-veredelung`: Zollverfahren aktive Veredelung nach Artikel 256-258 UZK und Artikel 240-262 UZK-DA: Beantragung und Nutzung der Bewilligung beim Hauptzollamt, Mengenueberwachung (INF-Blatt), Ausbeute- und…

## Anker

- Paragraf 130 OWiG
- FGO Paragrafen 40 bis 68: Finanzgerichtliche Klage bei Zollbescheiden
- Paragraf 355 AO i
- Paragraf 355 AO
- Paragraf 68 VwGO
- Tragende Normen verifizieren: AWG, AWV, EU-Dual-Use-VO 2021/821, EU-Sanktionsverordnungen, ZollkodexUnion, IranEmbargoVO, RusslandSanktionenVO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Mod…
- Aktenzeichen 009 VO 2021/821 — Gericht, Datum, Entscheidungsform und frei zugängliche Quelle vor Verwendung live verifizieren; nur übernehmen, wenn es den Skillgegenstand trägt

## Antwortform

- Lagebild: Rollen, Ziel, Frist, Aktenstand.
- Prüfung: Skill-Stationen, Normen, Tatsachen, Beweis, Gegenargument.
- Empfehlung: nächster Schritt mit Frist und Risiko.
- Arbeitsprodukt: ganze Sätze, Times New Roman 11 pt als Exportwunsch, dezimale Gliederung.
- Quellen: Normen konkret, Entscheidungen nur verifiziert oder als Prüfbedarf.

## Stop

Bei Notfrist, Haftungsrisiko, Interessenkollision, ungeprüften Echtdaten, fehlender Akte oder unsicherer Quelle an den zuständigen Berufsträger übergeben.
