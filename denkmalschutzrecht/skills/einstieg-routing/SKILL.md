---
name: einstieg-routing
description: "Einstiegsskill für das Denkmalschutzrecht-Plugin. Sortiert das Mandat, klärt Belegenheit des Objekts und damit das anwendbare Landesgesetz, ermittelt Rolle (Eigentümer, Erwerber, Behörde, Nachbar, Förderantragsteller), Fristen und gewünschtes Arbeitsprodukt. Routet anschließend in die passenden Querschnitts- und Landesskills."
---

# Einstieg — Routing im Denkmalschutzrecht

## Zweck und Anwendungsfall

Erster Anlaufpunkt für jeden Fall im Denkmalschutzrecht. Da Denkmalschutz Landesrecht ist, scheitert jede Bearbeitung ohne klare Belegenheit. Dieser Skill stellt die unverzichtbaren Mandatsfragen, identifiziert das einschlägige Landesgesetz und benennt den nächsten Skill.

## Eingaben

- **Objekt:** genaue Belegenheit (Straße, Hausnummer, Gemeinde, Kreis, Bundesland); Art (Baudenkmal, Bodendenkmal, bewegliches Denkmal, Ensemble, archäologische Reservation).
- **Schutzstatus:** eingetragen in die Denkmalliste? UNESCO-Welterbe? Ensembleschutz? Erhaltungssatzung nach Paragraf 172 BauGB?
- **Mandantenrolle:** Eigentümerin, Erwerberin, Mieterin, Nachbarin, Verband, Förderantragstellerin, Adressatin eines Bescheids, Beschwerdeführerin.
- **Konkrete Maßnahme oder Frage:** Sanierung, Umbau, Abbruch, Verkauf, steuerliche Förderung, Widerspruch gegen einen Bescheid, Verfahren wegen einer Ordnungswidrigkeit.
- **Fristen:** Anhörungsfrist, Widerspruchsfrist, Klagefrist, Erlaubnisfrist, Eilbedürftigkeit.

## Ablauf / Checkliste

1. Belegenheit feststellen und damit das anwendbare Landesgesetz benennen (Baden-Württemberg DSchG-BW, Bayern BayDSchG, Berlin DSchG-Bln, Brandenburg BbgDSchG, Bremen DSchG-Brem, Hamburg DSchG-HA, Hessen HDSchG, Mecklenburg-Vorpommern DSchG-MV, Niedersachsen NDSchG, Nordrhein-Westfalen DSchG-NRW, Rheinland-Pfalz DSchPflG, Saarland SDSchG, Sachsen SächsDSchG, Sachsen-Anhalt DSchG-LSA, Schleswig-Holstein DSchG-SH, Thüringen ThürDSchG).
2. Schutzstatus klären: in der Denkmalliste eingetragen oder nicht; nachrichtliche Eintragung oder konstitutive Eintragung; Ensemble- oder Einzelschutz.
3. Mandantenrolle und konkretes Begehren benennen.
4. Fristen markieren (Widerspruch typischerweise ein Monat ab Bekanntgabe, abweichende Landesfristen beachten).
5. Routing-Entscheidung treffen:
   - Querschnittsfragen (Eigentümerstellung, Erlaubnis, Förderung, Enteignung) → in die jeweiligen Querschnittsskills.
   - Landesspezifische Verfahren (zuständige Behörde, Verfahrenswege, Bußgeldrahmen) → in den Landesskill.

## Quellenpflicht

Anwendbares Landesgesetz immer aus der amtlichen Landesgesetz-Datenbank zitieren; siehe references/zitierweise.md. Keine Paragrafen aus dem Modellwissen übernehmen, ohne sie zuvor in der jeweiligen Landesgesetzes-Datenbank verifiziert zu haben.

## Ausgabeformat

Eine knappe Routing-Notiz mit den Punkten Belegenheit, Landesgesetz, Schutzstatus, Rolle, Frage, Frist, Empfehlung für den nächsten Skill.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Beispiel

Mandantin Müller-Schenk besitzt ein 1898 errichtetes Eckwohnhaus in München-Schwabing, eingetragen in die Denkmalliste, plant Innenausbau und Dachterrasse. Routing: Belegenheit Bayern, Landesgesetz BayDSchG, Schutzstatus eingetragen, Rolle Eigentümerin, Begehren Erlaubnis nach Art. 6 BayDSchG, Frist offen. Nächster Skill: `denkmalschutz-bayern-baydschg` und `erlaubnis-pflichtige-massnahmen`.
