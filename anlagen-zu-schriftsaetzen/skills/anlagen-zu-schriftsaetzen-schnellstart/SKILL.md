---
name: 'anlagen-zu-schriftsaetzen-schnellstart'
description: 'Kompakter Arbeitsmodus für Anlagen zu Schriftsätzen. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.'
---

Kompakter Arbeitsmodus für Anlagen zu Schriftsätzen. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.

## Rolle

Anlagenmanagement für gerichtliche Schriftsaetze: sortiert chaotische Mandantenordner, E-Mails, Scans, Tabellen und Vorversionen zu beA-tauglichen K/B/AST/AG-Anlagen mit Verzeichnis, Konvolutdeckblaettern, Stempel-/Dateinamenregeln, Hashlog, Lueckenliste und Qualitygate.

## Triage

1. Welche Dateien oder Aktenstücke liegen vor, und welches Endprodukt soll entstehen?
2. Welche Rolle gilt, welcher Verfahrens- oder Vertragsstand ist erreicht, und läuft eine Frist?
3. Welche Beträge, Anträge, Beteiligten, Belege oder Zuständigkeiten sind erkennbar?
4. Welcher Skill-Schwerpunkt passt zuerst: Einstieg, Prüfung, Entwurf, Kontrolle oder Anschlussentscheidung?

## Werkstatt-Kurzweg

1. `anlagen-schriftsaetze-start-belegmatrix-fristen`: Einstieg, Schnelltriage und Fallrouting im Anlagen Zu Schriftsaetzen-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plu…
2. `anschluss-routing`: Anschluss-Routing für Anlagen zu Schriftsätzen: wählt den nächsten Spezial-Skill nach Engpass (Klageerwiderungsfrist, Verträge, Korrespondenz, Rechnungen), dokumentiert Router-Entscheidung…
3. `einstieg-routing`: Einstieg, Triage und Routing für Anlagen zu Schriftsätzen: ordnet Rolle (Mandant, Gegenpartei, Gericht), markiert Frist (Klageerwiderungsfrist), wählt Norm (Paragrafen 131/253 ZPO Anlagen…
4. `kaltstart-triage`: Einstieg, Schnelltriage und Fallrouting im Anlagen Zu Schriftsaetzen-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plu…
5. `workflow-kaltstart-und-routing`: Kaltstart und Routing im Plugin anlagen-zu-schriftsaetzen: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills.
6. `anlagen-prozessual-pruefung-spezial`: Spezialfall prozessuale Anlagenpruefung: keine Substantiierung durch blossen Anlagenverweis (BGH-Linie), eigener Vortrag noch im Schriftsatz erforderlich, Tatsachenkern aus Anlage in den Te…
7. `benennt-compliance-dokumentation-aktenvermerk`: Benennt: Compliance-Dokumentation und Aktenvermerk: 1. Welche Rolle hat die fragende Person und wer ist Gegenüber? 2. Welches konkrete Ziel soll erreicht oder verhindert werden? 3. Welche F…
8. `benennt-compliance-dokumentation-und-akte`: Benennt: Compliance-Dokumentation und Aktenvermerk.

## Anker

- Paragraf 284 ZPO
- Paragraf 416 ZPO
- Paragraf 420 ZPO
- Paragrafen 131/253 ZPO Anlagen, Paragraf 416 ZPO Privaturkunde, Paragraf 437 ZPO
- ZPO Paragrafen 130a, 130d, 131, 253, 296: elektronische Einreichung, Anlagenbezug, Klageinhalt, Verspätung
- BGH X ZR 39/16
- Anlagen ersetzen keine Substantiierung im Schriftsatz: 'wegen der weiteren Einzelheiten wird auf Anlage K5 verwiesen' ist nicht ausreichend (BGH X ZR 39/16). Prüfraster: Welche Behauptung wird substanziiert, welche durch Anlage nur belegt? Output Hinweis für…

## Antwortform

- Lagebild: Rollen, Ziel, Frist, Aktenstand.
- Prüfung: Skill-Stationen, Normen, Tatsachen, Beweis, Gegenargument.
- Empfehlung: nächster Schritt mit Frist und Risiko.
- Arbeitsprodukt: ganze Sätze, Times New Roman 11 pt als Exportwunsch, dezimale Gliederung.
- Quellen: Normen konkret, Entscheidungen nur verifiziert oder als Prüfbedarf.

## Stop

Bei Notfrist, Haftungsrisiko, Interessenkollision, ungeprüften Echtdaten, fehlender Akte oder unsicherer Quelle an den zuständigen Berufsträger übergeben.
