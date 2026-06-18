---
name: quellen-livecheck
description: "Quellenhygiene-Skill für das Denkmalschutzrecht-Plugin. Liefert die kuratierte Suchadressen-Liste für die sechzehn Landesgesetzes-Datenbanken, das Bundesrecht (gesetze-im-internet.de), die Verwaltungsgerichtsbarkeit (BVerwG, OVG-Pakete) und die Welterbe-Quellen (UNESCO, ICOMOS). Verhindert Halluzinationen, indem Paragrafen, Aktenzeichen und Fundstellen vor Verwendung zwingend live verifiziert werden."
---

# Quellen-Livecheck Denkmalrecht

## Anwendungsfall

Vor jeder Ausgabe an Mandantin, Gericht oder Behörde sind die in einem Skill genannten Norm- und Rechtsprechungsanker live zu verifizieren. Dieser Skill listet die zulässigen Suchadressen.

## Landesgesetzes-Datenbanken (alphabetisch)

- Baden-Württemberg — landesrecht-bw.de
- Bayern — gesetze-bayern.de
- Berlin — gesetze.berlin.de
- Brandenburg — bravors.brandenburg.de
- Bremen — transparenz.bremen.de
- Hamburg — landesrecht-hamburg.de
- Hessen — rv.hessenrecht.hessen.de
- Mecklenburg-Vorpommern — landesrecht-mv.de
- Niedersachsen — voris.wolterskluwer-online.de bzw. nds-voris.de
- Nordrhein-Westfalen — recht.nrw.de
- Rheinland-Pfalz — landesrecht.rlp.de
- Saarland — sl.juris.de
- Sachsen — revosax.sachsen.de
- Sachsen-Anhalt — landesrecht.sachsen-anhalt.de
- Schleswig-Holstein — gesetze-rechtsprechung.sh.juris.de
- Thüringen — landesrecht.thueringen.de

## Bundesrecht und Rechtsprechung

- Grundgesetz, BGB, EStG, VwVfG, VwGO, OWiG, StGB — gesetze-im-internet.de
- BVerfG-Entscheidungen — bundesverfassungsgericht.de/Entscheidungen
- BVerwG-Entscheidungen — bverwg.de/entscheidungen
- OVG-Entscheidungen — Landesjustizportal oder landesrechtsprechung.<land>.de

## Welterbe

- UNESCO-Welterbeliste — whc.unesco.org/en/list
- ICOMOS-Berichte und State of Conservation — whc.unesco.org/en/soc
- Operational Guidelines for the Implementation of the World Heritage Convention — whc.unesco.org/en/guidelines

## Ablauf

1. Jedes konkrete Paragrafenzitat und jedes Aktenzeichen vor Ausgabe live in der zuständigen Quelle aufrufen.
2. Fundstelle mit Datum, Aktenzeichen und Quelle dokumentieren.
3. Bei Unsicherheit über die aktuelle Fassung eines Landesgesetzes auf die Landesgesetz-Datenbank verlinken statt frei zitieren.

## Quellenpflicht

Normverweise und Rechtsprechungsanker werden vor Mandatsverwendung live in den amtlichen Datenbanken verifiziert; siehe references/zitierweise.md.

## Ausgabeformat

Strukturierte Stellungnahme in vollständigen Sätzen mit konkreten Norm-Ankern und klarem Bezug zum Mandatsbegehren.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->
