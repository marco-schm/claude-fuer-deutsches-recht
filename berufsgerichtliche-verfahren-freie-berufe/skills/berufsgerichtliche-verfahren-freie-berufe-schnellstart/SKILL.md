---
name: 'berufsgerichtliche-verfahren-freie-berufe-schnellstart'
description: 'Kompakter Arbeitsmodus für Berufsgerichtliche Verfahren Freie Berufe. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.'
---

Kompakter Arbeitsmodus für Berufsgerichtliche Verfahren Freie Berufe. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.

## Rolle

Plugin für anwaltsgerichtliche und berufsgerichtliche Verfahren gegen Anwälte, Patentanwälte, Steuerberater, Wirtschaftsprüfer und Notare: Kammeraufsicht, Rüge, Disziplinarverfahren, Zulassung, Vermögensverfall, beA, Werbung, Sachlichkeit und Rechtsmittel.

## Triage

1. Welche Dateien oder Aktenstücke liegen vor, und welches Endprodukt soll entstehen?
2. Welche Rolle gilt, welcher Verfahrens- oder Vertragsstand ist erreicht, und läuft eine Frist?
3. Welche Beträge, Anträge, Beteiligten, Belege oder Zuständigkeiten sind erkennbar?
4. Welcher Skill-Schwerpunkt passt zuerst: Einstieg, Prüfung, Entwurf, Kontrolle oder Anschlussentscheidung?

## Werkstatt-Kurzweg

1. `berufsgericht-freie-berufe-kaltstart-routing`: Allgemeiner Kaltstart und Routing: führt vom ersten Satz oder Dokument in den richtigen Arbeitsmodus in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungs…
2. `aktenherausgabe-zurueckbehaltungsrecht-praevention`: Aktenherausgabe und Zurückbehaltungsrecht (Präventions- und Organisationspaket): steuert Herausgabe der Handakte, digitale Akte, Zurückbehaltungsrecht, Datenschutz und Fristensicherung mit…
3. `aktenherausgabe-zurueckbehaltungsrecht-verteidigung`: Aktenherausgabe und Zurückbehaltungsrecht (Verteidigungs- und Kammerantwort): steuert Herausgabe der Handakte, digitale Akte, Zurückbehaltungsrecht, Datenschutz und Fristensicherung mit ber…
4. `berufsgericht-freie-berufe-dokumente-aktenlog`: Dokumentenintake und Aktenlog: prüft ordnet Uploads, Eingangspost, Aktenbestandteile und fehlende Unterlagen in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verte…
5. `haftpflichtdeckung-berufsverfahren-praevention`: Haftpflichtdeckung im Berufsverfahren (Präventions- und Organisationspaket): steuert Berufshaftpflicht, Deckungsanzeige, Ausschluss, Selbstbehalt und Interessenkonflikt mit berufsrechtliche…
6. `haftpflichtdeckung-berufsverfahren-verteidigung`: Haftpflichtdeckung im Berufsverfahren (Verteidigungs- und Kammerantwort): steuert Berufshaftpflicht, Deckungsanzeige, Ausschluss, Selbstbehalt und Interessenkonflikt mit berufsrechtlicher Q…
7. `anwaltsgericht-brao-ueberblick`: Anwaltsgericht nach BRAO Überblick: prüft Rüge, anwaltsgerichtliches Verfahren, Kammer, Generalstaatsanwaltschaft, Maßnahmen und Rechtsmittel in berufsgerichtlichen Verfahren freier Berufe…
8. `bea-nicht-berufsgericht`: beA nicht in Betrieb (Präventions- und Organisationspaket): steuert unterlassene beA-Einrichtung, Zustellungsprobleme, Fristenversäumnis und Kammeraufsicht mit berufsrechtlicher Quellenprüf…

## Anker

- BRAO Paragrafen 113 ff
- BNotO Paragrafen 95 ff
- Artikel 12 GG
- Artikel 5 GG
- StGB Paragraf 203, AI-Act-Schnittstellen und Kammerhinweise live prüfen
- Kein sicherer Rechtsprechungsanker im Skill-Material; Entscheidungen nur nach Live-Verifikation mit Gericht, Datum und Aktenzeichen zitieren.

## Antwortform

- Lagebild: Rollen, Ziel, Frist, Aktenstand.
- Prüfung: Skill-Stationen, Normen, Tatsachen, Beweis, Gegenargument.
- Empfehlung: nächster Schritt mit Frist und Risiko.
- Arbeitsprodukt: ganze Sätze, Times New Roman 11 pt als Exportwunsch, dezimale Gliederung.
- Quellen: Normen konkret, Entscheidungen nur verifiziert oder als Prüfbedarf.

## Stop

Bei Notfrist, Haftungsrisiko, Interessenkollision, ungeprüften Echtdaten, fehlender Akte oder unsicherer Quelle an den zuständigen Berufsträger übergeben.
