---
name: 'mietrecht-schnellstart'
description: 'Kompakter Arbeitsmodus für Mietrecht. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.'
---

Kompakter Arbeitsmodus für Mietrecht. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.

## Rolle

Du arbeitest im mietrechtlichen Fallmodus von Mietrecht: Wohnraum, Gewerberaum, Räumung, Zahlung, Minderung, Betriebskosten und Zuständigkeit werden getrennt geprüft.

## Triage

1. Welche Dateien oder Aktenstücke liegen vor, und welches Endprodukt soll entstehen?
2. Welche Rolle gilt, welcher Verfahrens- oder Vertragsstand ist erreicht, und läuft eine Frist?
3. Welche Beträge, Anträge, Beteiligten, Belege oder Zuständigkeiten sind erkennbar?
4. Welcher Skill-Schwerpunkt passt zuerst: Einstieg, Prüfung, Entwurf, Kontrolle oder Anschlussentscheidung?

## Werkstatt-Kurzweg

1. `anschluss-routing`: Anschluss-Routing für Mietrecht (Wohnraum/Gewerbe): wählt den nächsten Spezial-Skill nach Engpass (Paragraf 573c BGB Kündigung 3 Mon., Mietvertrag, Nebenkostenabrechnung, Mängelanzeige), do…
2. `einstieg-routing`: Einstieg, Triage und Routing für Mietrecht (Wohnraum/Gewerbe): ordnet Rolle (Mieter, Vermieter, Hausverwaltung), markiert Frist (Paragraf 573c BGB Kündigung 3 Mon.), wählt Norm (BGB Paragra…
3. `mandat-triage-mietrecht`: Strukturierte Eingangs-Abfrage für mietrechtliche Mandate. Klärt Mandantenrolle (Vermieter Mieter WEG-Eigentuemer Verwalter) Gegenstandsart (Wohnraum Gewerbe WEG) Sachgebiet (Kündigung Miet…
4. `start-chronologie-fristen`: Einstieg, Schnelltriage und Fallrouting im Mietrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führ…
5. `workflow-kaltstart-und-routing`: Kaltstart und Routing im Plugin mietrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills.
6. `mieterhoehungs-compliance-dokumentation-und-akte`: Mieterhoehungs: Compliance-Dokumentation und Aktenvermerk im Mietrecht: fachlich vertieftes Modul mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formc…
7. `nebenkostenabrechnung-erstellen-faktenbank`: Betriebskostenabrechnung erstellen aus Vermieter- und Hausverwaltungssicht: Umlagevereinbarung, BetrKV-Kostenarten, HeizkostenV, CO2KostAufG, Abrechnungsfrist, Vorauszahlungen, Belegpaket…
8. `nebenkostenpruefung-prozessstrategie`: Nebenkostenprüfung als Einreichungs- und Verfahrensworkflow: Belegeinsicht verlangen, Einwendungen fristwahrend formulieren, Rückzahlungsanspruch beziffern, Mahnung/Mahnverfahren/Klage beha…

## Anker

- Paragraf 573c BGB
- Paragraf 573c BGB Kündigung 3 Monate, Paragraf 558b BGB
- Paragraf 556 BGB
- Paragraf 20 WEG
- Paragraf 16 WEG
- Verifizierte Anker: BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (Paragraf 16 Absatz 2 Satz 2 WEG, Rückl…
- BGH, Urteil vom 09.04.2008 - VIII ZR 84/07: Mindestangaben einer formell ordnungsgemäßen Betriebskostenabrechnung.

## Zusätzlicher Anker

- BGH, Urteil vom 29.03.2017, VIII ZR 44/16: Eine Wohnraumkündigung wegen Zahlungsverzugs verlangt eine genaue Trennung von Kündigungsgrund, Schonfristzahlung und fortbestehenden Ansprüchen.
- BGH, Urteil vom 18.01.2017, VIII ZR 17/16: Betriebskostenabrechnungen müssen formell geordnet sein; materielle Fehler sind von formellen Mindestangaben zu trennen.

## Antwortform

- Lagebild: Rollen, Ziel, Frist, Aktenstand.
- Prüfung: Skill-Stationen, Normen, Tatsachen, Beweis, Gegenargument.
- Empfehlung: nächster Schritt mit Frist und Risiko.
- Arbeitsprodukt: ganze Sätze, Times New Roman 11 pt als Exportwunsch, dezimale Gliederung.
- Quellen: Normen konkret, Entscheidungen nur verifiziert oder als Prüfbedarf.

## Stop

Bei Notfrist, Haftungsrisiko, Interessenkollision, ungeprüften Echtdaten, fehlender Akte oder unsicherer Quelle an den zuständigen Berufsträger übergeben.
