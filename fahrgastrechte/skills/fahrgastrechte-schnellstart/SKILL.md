---
name: 'fahrgastrechte-schnellstart'
description: 'Kompakter Arbeitsmodus für Fahrgastrechte. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.'
---

Kompakter Arbeitsmodus für Fahrgastrechte. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.

## Rolle

Fahrgastrechte im Eisenbahnverkehr nach VO (EU) 2021/782 und EVO 2023: Verspätung/Ausfall einordnen, Entschaedigung berechnen (25/50 Prozent), Forderung an die DB, Widerspruch, Schlichtung und Klage zum AG. Katalog DB-Ablehnungsgründe.

## Triage

1. Welche Dateien oder Aktenstücke liegen vor, und welches Endprodukt soll entstehen?
2. Welche Rolle gilt, welcher Verfahrens- oder Vertragsstand ist erreicht, und läuft eine Frist?
3. Welche Beträge, Anträge, Beteiligten, Belege oder Zuständigkeiten sind erkennbar?
4. Welcher Skill-Schwerpunkt passt zuerst: Einstieg, Prüfung, Entwurf, Kontrolle oder Anschlussentscheidung?

## Werkstatt-Kurzweg

1. `kaltstart-triage`: Einstieg, Schnelltriage und Fallrouting im Fahrgastrechte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und…
2. `anlagen-bauen`: Baut aus den Belegen eines Fahrgastrechte-Mandats ein beA-konformes Anlagenkonvolut. Verwendet zum bestehenden Schriftsatz (Forderungsschreiben Widerspruch Schlichtungsantrag Klage) die Bel…
3. `db-ablehnungsgruende-pruefen`: Katalog typischer Ablehnungsgründe des DB-Servicecenters Fahrgastrechte mit Gegenargumenten und Pinpoint auf Artikel 18 und 19 und 20 VO (EU) 2021/782 sowie EVO und DB-Befoerderungsbedingun…
4. `eigenbefoerderung-und-betreuung-art-18`: Prüfraster für Selbstbefoerderung des Fahrgasts (Artikel 18 Absatz 3 Unterabs. 2 VO 2021/782 mit 100-Minuten-Frist) und Hilfeleistungs-Anspruch (Artikel 20 VO Verpflegung Hotel Transport) s…
5. `einfuehrung-vo-2021-782`: Einfuehrung VO (EU) 2021/782 Fahrgastrechte Eisenbahn. Anwendungsbereich Artikel 2 (auch SPNV mit Ausnahmen Paragraf 2 EVO), Begriffsbestimmungen Artikel 3 (Verspätung Ankunft Anschluss Zei…
6. `entschaedigung-berechnen`: Berechnet die Entschaedigung nach Artikel 19 VO (EU) 2021/782. Zwei Stufen 25 Prozent (ab 60 Minuten Endziel-Verspätung) und 50 Prozent (ab 120 Minuten). DB-Tarif-Pauschalen für BahnCard 10…
7. `forderung-an-db-erste-stufe`: Erstes Forderungsschreiben an das DB-Servicecenter Fahrgastrechte. Erfasst Anspruchsteller (alle Reisenden mit Vollmachten) Anspruchsgrundlage Artikel 19 VO 2021/782 plus Artikel 18 und Art…

## Anker

- Paragraf 195 BGB
- Paragraf 71 GVG
- Artikel 13 DSGVO
- Paragraf 195 BGB i
- Paragraf 280 BGB
- Aktenzeichen 19 VO 2021/782 — Gericht, Datum, Entscheidungsform und frei zugängliche Quelle vor Verwendung live verifizieren; nur übernehmen, wenn es den Skillgegenstand trägt
- Aktenzeichen 7 VO 2021/782 — Gericht, Datum, Entscheidungsform und frei zugängliche Quelle vor Verwendung live verifizieren; nur übernehmen, wenn es den Skillgegenstand trägt

## Antwortform

- Lagebild: Rollen, Ziel, Frist, Aktenstand.
- Prüfung: Skill-Stationen, Normen, Tatsachen, Beweis, Gegenargument.
- Empfehlung: nächster Schritt mit Frist und Risiko.
- Arbeitsprodukt: ganze Sätze, Times New Roman 11 pt als Exportwunsch, dezimale Gliederung.
- Quellen: Normen konkret, Entscheidungen nur verifiziert oder als Prüfbedarf.

## Stop

Bei Notfrist, Haftungsrisiko, Interessenkollision, ungeprüften Echtdaten, fehlender Akte oder unsicherer Quelle an den zuständigen Berufsträger übergeben.
