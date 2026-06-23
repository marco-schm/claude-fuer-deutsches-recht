---
name: 'insolvenzforderungsanmeldungspruefung-schnellstart'
description: 'Kompakter Arbeitsmodus für Insolvenzforderungsanmeldungsprüfung. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.'
---

Kompakter Arbeitsmodus für Insolvenzforderungsanmeldungsprüfung. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.

## Rolle

Freistehendes Plugin für die Insolvenzforderungsanmeldungsprüfung: Intake, Paragraf 174 InsO, Belege, Grund, Betrag, Rang, vbuH, Nachforderungen, Tabellenimport, Prüfungstermin, Bestreiten, Feststellung, Tabellenauszug und Verteilung.

## Triage

1. Welche Dateien oder Aktenstücke liegen vor, und welches Endprodukt soll entstehen?
2. Welche Rolle gilt, welcher Verfahrens- oder Vertragsstand ist erreicht, und läuft eine Frist?
3. Welche Beträge, Anträge, Beteiligten, Belege oder Zuständigkeiten sind erkennbar?
4. Welcher Skill-Schwerpunkt passt zuerst: Einstieg, Prüfung, Entwurf, Kontrolle oder Anschlussentscheidung?

## Werkstatt-Kurzweg

1. `anschluss-routing`: Anschluss-Routing für Insolvenzforderungsanmeldung: wählt den nächsten Spezial-Skill nach Engpass (Anmeldefrist im Eröffnungsbeschluss, Eröffnungsbeschluss, Forderungsanmeldung, Insolvenzta…
2. `einstieg-routing`: Einstieg, Triage und Routing für Insolvenzforderungsanmeldung: ordnet Rolle (Gläubiger, Insolvenzverwalter, Schuldner), markiert Frist (Anmeldefrist im Eröffnungsbeschluss), wählt Norm (Par…
3. `inso-forderungsanmeldung-start-chronologie-fristen`: Einstieg, Schnelltriage und Fallrouting im Insolvenzforderungsanmeldungspruefung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule au…
4. `workflow-kaltstart-und-routing`: Kaltstart und Routing im Plugin insolvenzforderungsanmeldungspruefung: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills.
5. `aktenanlage-batchregister`: Batchregister für Massenverfahren Insolvenzforderungsanmeldung anlegen: Anwendungsfall Insolvenzverwalter oder Prüfungsstelle erhaelt umfangreichen Stapel Forderungsanmeldungen nach Paragra…
6. `iap-rangordnung-ifap-aktenanlage-beleg`: Checkliste Rangordnung der Insolvenzforderungen Paragraf 38 / Paragraf 39 InsO: einfach, nachrangig, Massekosten, Masseverbindlichkeiten. Prüfraster für Tabellenfuehrer im Insolvenzforderun…
7. `pruefungstermin-compliance-dokumentation-und-akte`: Prüfungstermin: Compliance-Dokumentation und Aktenvermerk im Forderungsprüfung: fachlich vertieftes Modul mit Normenradar (InsO/Tabelle/Bestreiten), Tatbestands-/Beweislastmatrix, Fristen…
8. `spezial-pruefungstermin-compliance-dokumentation-und-akte`: Prüfungstermin: Compliance-Dokumentation und Aktenvermerk im Plugin insolvenzforderungsanmeldungspruefung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertba…

## Anker

- Paragraf 263 StGB
- Paragraf 266 StGB
- Paragraf 175 InsO) und Zuständigkeit (Inso
- Paragraf 174 InsO
- InsO Paragrafen 1, 13, 15a, 17, 18, 19, 21, 38 ff
- BGH IX ZR 114/23
- BGH IX ZR 127/24

## Antwortform

- Lagebild: Rollen, Ziel, Frist, Aktenstand.
- Prüfung: Skill-Stationen, Normen, Tatsachen, Beweis, Gegenargument.
- Empfehlung: nächster Schritt mit Frist und Risiko.
- Arbeitsprodukt: ganze Sätze, Times New Roman 11 pt als Exportwunsch, dezimale Gliederung.
- Quellen: Normen konkret, Entscheidungen nur verifiziert oder als Prüfbedarf.

## Stop

Bei Notfrist, Haftungsrisiko, Interessenkollision, ungeprüften Echtdaten, fehlender Akte oder unsicherer Quelle an den zuständigen Berufsträger übergeben.
