---
name: kaltstart-triage
description: "Schnelltriage für ein neues denkmalschutzrechtliches Mandat. Erhebt in einer Sitzung Objektdaten, Schutzstatus, Mandantenrolle, konkrete Maßnahme, drohende Fristen und Eilrisiken. Liefert eine erste Risikoampel und benennt die unverzichtbaren Sofortmaßnahmen (Akteneinsicht, Bauanzeige aussetzen, vorläufige Sicherung)."
---

# Kaltstart — Denkmalschutzrechtliche Triage

## Zweck und Anwendungsfall

Wenn ein Mandat eilbedürftig kommt — typisch ist die Konstellation, dass die Eigentümerin gerade einen Untersagungsbescheid erhalten hat, dass eine Sanierungsmaßnahme an einer Liste eingetragenen Gebäude angegangen wurde, oder dass die Denkmalbehörde eine vorläufige Sicherung angeordnet hat — braucht der Skill alle Tatsachen in einer Sitzung und liefert eine erste Bewertung mit Sofortmaßnahmen.

## Eingaben

- **Objekt:** Anschrift, Baujahr, Lage, Eintragungsstatus.
- **Vorgang:** welcher Bescheid liegt vor (Erlaubnisversagung, Untersagung, Anordnung, Bußgeldbescheid, Eintragung in die Denkmalliste, Förderbescheid)?
- **Mandantenrolle und wirtschaftlicher Hintergrund:** Eigentümerin, Erwerberin, Erbe, Bauträger, Investor.
- **Bereits laufende Arbeiten und tatsächlicher Zustand des Objekts.**
- **Korrespondenz mit der Denkmalbehörde, frühere Anträge, Begründungen.**
- **Fristen:** Widerspruchsfrist, Klagefrist, Eilbedürftigkeit (Witterung, gestoppte Baustelle).

## Ablauf / Checkliste

1. Tatsachen knapp festhalten, in Reihenfolge Objekt — Schutzstatus — Vorgang — Rolle — Frist.
2. Belegenheit und damit Landesgesetz feststellen.
3. Erste Risikoampel: Welche Maßnahme ist erlaubnisfähig, welche ist offensichtlich unzulässig, welche steht im Ermessen der Behörde.
4. Sofortmaßnahmen prüfen:
   - Akteneinsicht beantragen (Verwaltungsverfahrensgesetz des jeweiligen Landes; meist eine Woche bis zwei Wochen Vorlauf).
   - Bauarbeiten aussetzen, soweit der Vorgang darauf zielt.
   - Vorläufige Bauanzeige oder Erlaubnisantrag stellen, wenn eine geplante Maßnahme erst noch in das Verfahren soll.
   - Anhörung verlangen, wenn der Bescheid ohne vorhergehende Anhörung erlassen wurde (Paragraf 28 VwVfG des Bundes; in den Ländern jeweils inhaltsgleich).
5. Folgeskill wählen: Querschnittsskill (Eintragung, Erlaubnis, Förderung) oder Landesskill.

## Quellenpflicht

Konkrete Norm-Anker des Landesgesetzes live aus der amtlichen Landesgesetz-Datenbank ziehen; siehe references/zitierweise.md. BGH-, BVerwG- oder OVG-Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugänglicher Quelle benennen, nicht aus Modellwissen.

## Ausgabeformat

Kurzes Triage-Memo mit fünf Blöcken: Sachverhalt, Frage, Kurzantwort in einem Satz, Sofortmaßnahmen, offene Punkte und nächster Skill.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Beispiel

Eigentümerin Lechner hat ohne Erlaubnis das Dach eines eingetragenen Pfarrhauses in Regensburg eindecken lassen. Untersagungsbescheid mit Beseitigungsanordnung kam vor zehn Tagen. Sofortmaßnahmen: Widerspruch einlegen mit aufschiebender Wirkung beantragen; vorhandene Materialien dokumentieren; nachträglichen Erlaubnisantrag erwägen. Nächster Skill: `denkmalschutz-bayern-baydschg` und `bussgeld-ordnungswidrigkeitsverfahren`.
