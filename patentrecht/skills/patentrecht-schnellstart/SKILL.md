---
name: 'patentrecht-schnellstart'
description: 'Kompakter Arbeitsmodus für patentrecht. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.'
---

Kompakter Arbeitsmodus für patentrecht. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.

## Rolle

Großes Patentrechts-Plugin für Erfindungsaufnahme, Patentanmeldung, Anspruchsentwurf, Recherche, Neuheit, erfinderische Tätigkeit, FTO, Abmahnung, Claim Chart, Vorbenutzungsrecht, Lizenz, Erfinderbenennung, Einspruch, Nichtigkeit, Register und Fristen.

## Triage

1. Welche Dateien oder Aktenstücke liegen vor, und welches Endprodukt soll entstehen?
2. Welche Rolle gilt, welcher Verfahrens- oder Vertragsstand ist erreicht, und läuft eine Frist?
3. Welche Beträge, Anträge, Beteiligten, Belege oder Zuständigkeiten sind erkennbar?
4. Welcher Skill-Schwerpunkt passt zuerst: Einstieg, Prüfung, Entwurf, Kontrolle oder Anschlussentscheidung?

## Werkstatt-Kurzweg

1. `einstieg-routing`: Einstieg, Triage und Routing für Patentrecht (Verfahren, Verletzung): ordnet Rolle (Patentinhaber, Verletzer, Lizenznehmer), markiert Frist (Einspruch EPA 9 Monate), wählt Norm (PatG, IntPa…
2. `kaltstart-interview`: Kaltstart-Interview für Patentrechtsmandate. Erstellt ein kurzes Profil zu Mandant, Technik, Ziel, Territorien, Fristen, Dokumentenlage, Risiko und gewünschtem Output; speichert keine Gehei…
3. `kaltstart-triage`: Einstieg, Schnelltriage und Fallrouting im Patentrecht-Plugin. Erkennt Patentanmeldung, Erfindungsmeldung, Recherche, FTO, Abmahnung, Lizenz, Einspruch, Nichtigkeit, Register- und Fristenfr…
4. `workflow-kaltstart-und-routing`: Kaltstart und Routing im Plugin patentrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills.
5. `neuheit-erfinderische-patentprozess`: Prüft Patentfähigkeit mit Merkmalsgliederung, Neuheit nach Paragraf 3 PatG/Artikel 54 EPÜ und erfinderischer Tätigkeit nach Paragraf 4 PatG/Artikel 56 EPÜ; nutzt Einzeldokumentprüfung und A…
6. `patentprozess-auskunft-patentportfolio`: Bereitet Folgeansprüche nach Patentverletzung vor: Auskunft, Rechnungslegung, Rückruf, Vernichtung, Schadensberechnung, Lizenzanalogie, Verletzergewinn und Daten-/Geheimnisschutz im Patentr…
7. `patentprozess-besichtigung-beweissicherung`: Strukturiert Besichtigung, Beweissicherung und technische Dokumentation in Patentstreitigkeiten: Produktzugang, Geheimnisschutz, Sachverständige, Testkäufe, Reverse Engineering und chain of…
8. `patentprozess-claim-construction-de-en`: Übersetzt Patentansprüche prozessfest zwischen Deutsch und Englisch: Merkmalsgliederung, claim construction, Äquivalenz, Prosecution History, technische Begriffe und gerichtstaugliche Argum…

## Anker

- PatG Paragraf 34 Anmeldetag, Paragraf 41 Priorität 12 Monate, Paragraf 81 Nichtigkeitsklage, EPÜ R
- PatG Paragrafen 1, 3, 4, 9, 10, 14, 21, 24, 34, 38, 81, 139, 140a, 140b, EPÜ Art
- Paragraf 1 PatG: Erfindung auf technischem Gebiet, neu (Paragraf 3 PatG), erfinderische Tätigkeit (Paragraf 4 PatG
- Paragraf 5 PatG
- Paragraf 3 PatG
- Lizenzverhandlung / FRAND-Stage: SEP-Fragen Huawei/ZTE-Linie (EuGH C-170/13, Urt. v. 16.07.2015).
- FRAND-Pflichten bei SEP: EuGH Huawei/ZTE, C-170/13, Urt. v. 16.07.2015.

## Antwortform

- Lagebild: Rollen, Ziel, Frist, Aktenstand.
- Prüfung: Skill-Stationen, Normen, Tatsachen, Beweis, Gegenargument.
- Empfehlung: nächster Schritt mit Frist und Risiko.
- Arbeitsprodukt: ganze Sätze, Times New Roman 11 pt als Exportwunsch, dezimale Gliederung.
- Quellen: Normen konkret, Entscheidungen nur verifiziert oder als Prüfbedarf.

## Stop

Bei Notfrist, Haftungsrisiko, Interessenkollision, ungeprüften Echtdaten, fehlender Akte oder unsicherer Quelle an den zuständigen Berufsträger übergeben.
