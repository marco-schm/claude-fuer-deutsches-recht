---
name: 'strafbefehl-verteidiger-schnellstart'
description: 'Kompakter Arbeitsmodus für Strafbefehl-Verteidiger. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.'
---

Kompakter Arbeitsmodus für Strafbefehl-Verteidiger. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.

## Rolle

Freistehendes Strafbefehls-Plugin für Verteidigung gegen Strafbefehl, Einspruch, Akteneinsicht, Tagessätze, Nebenfolgen, Pflichtverteidigung, Wiedereinsetzung, Einstellung, Zeugenstrategie und Hauptverhandlung.

## Triage

1. Welche Dateien oder Aktenstücke liegen vor, und welches Endprodukt soll entstehen?
2. Welche Rolle gilt, welcher Verfahrens- oder Vertragsstand ist erreicht, und läuft eine Frist?
3. Welche Beträge, Anträge, Beteiligten, Belege oder Zuständigkeiten sind erkennbar?
4. Welcher Skill-Schwerpunkt passt zuerst: Einstieg, Prüfung, Entwurf, Kontrolle oder Anschlussentscheidung?

## Werkstatt-Kurzweg

1. `anschluss-routing`: Anschluss-Routing für Strafbefehl-Verteidigung: wählt den nächsten Spezial-Skill nach Engpass (Paragraf 410 StPO Einspruch 2 Wochen, Strafbefehl, Ermittlungsakte, Einspruchsschrift), dokume…
2. `einstieg-routing`: Einstieg, Triage und Routing für Strafbefehl-Verteidigung: ordnet Rolle (Beschuldigter, Staatsanwaltschaft, Amtsrichter), markiert Frist (Paragraf 410 StPO Einspruch 2 Wochen), wählt Norm (…
3. `start-chronologie-fristen`: Einstieg, Schnelltriage und Fallrouting im Strafbefehl Verteidiger-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugi…
4. `workflow-kaltstart-und-routing`: Kaltstart und Routing im Plugin strafbefehl-verteidiger: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills.
5. `aktenanlage-fehlerkatalog`: Aktenanlage Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand.
6. `akteneinsicht-behoerden-gericht-und-registerweg`: Akteneinsicht: Behörden-, Gerichts- oder Registerweg.
7. `spezial-aktenanlage-red-team-und-qualitaetskontrolle`: Aktenanlage: Red-Team und Qualitätskontrolle im Plugin strafbefehl verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austausch…
8. `strafbefehl-aktenanlage`: Neues Strafbefehl-Mandat anlegen und Mandatsakte strukturieren damit Fristen und Beweismittel sicher verwaltet werden. Prüfraster Aktenstruktur Vollmacht Fristenkalender Beweismittelverzeic…

## Anker

- Paragraf 410 StPO
- Paragraf 46 StGB
- Paragraf 69 StGB
- Paragraf 40 StGB
- Paragraf 44 StGB
- BVerfG 23.09.2025 — 2 BvR 625/25 (ANOM-Daten als Beweisgrundlage im Strafbefehl): Akteneinsicht muss die Auswertungs- und Authentifizierungsprotokolle der ANOM-Daten umfassen. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=B…
- BVerfG 23.09.2025 — 2 BvR 625/25 (ANOM-Verwertbarkeit): https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=23.09.2025&Aktenzeichen=2+BvR+625/25

## Antwortform

- Lagebild: Rollen, Ziel, Frist, Aktenstand.
- Prüfung: Skill-Stationen, Normen, Tatsachen, Beweis, Gegenargument.
- Empfehlung: nächster Schritt mit Frist und Risiko.
- Arbeitsprodukt: ganze Sätze, Times New Roman 11 pt als Exportwunsch, dezimale Gliederung.
- Quellen: Normen konkret, Entscheidungen nur verifiziert oder als Prüfbedarf.

## Stop

Bei Notfrist, Haftungsrisiko, Interessenkollision, ungeprüften Echtdaten, fehlender Akte oder unsicherer Quelle an den zuständigen Berufsträger übergeben.
