# Richterliche Verfeinerung — Bericht v365.0.0

Dieser Bericht dokumentiert die Aenderungen an den 13 Gerichts-Plugins im Loop zu v365.0.0, nennt je Plugin ein konkretes Nutzenversprechen und empfiehlt eine Reihenfolge zum Testen. Die inhaltliche Skill-Anreicherung (Anker-Rechtsprechung, Pruefungsschemata, Fallstricke, Tenor-Bausteine) war in v358 bis v364 vorbereitet; v365 ergaenzt Wertgrenzen-Korrektheit, generisches Maskulinum und Verifikation.

## Aenderungen je Plugin

| Plugin | Aenderung in v365 | Nutzenversprechen |
|---|---|---|
| `relationstechnik-zivilrecht` | Entgendert; 20-Stationen-Relation und Tenor-/Urteilsbausteine verifiziert | Spart dem Berichterstatter mehrere Stunden beim Aufbau einer grossen Relation samt Urteilsentwurf |
| `richter-amtsgericht-zivil` | Wertgrenze 10.000 Euro (Paragraf 23 GVG 2026); entgendert | Spart pro Zivilsache rund 20 bis 40 Minuten bei Zustaendigkeit, Streitwert und Beweisbeschluss |
| `richter-landgericht-zivilkammer` | Zustaendigkeit ab 10.001 Euro; entgendert | Spart Zeit beim Relationsaufbau und der Abgrenzung Kammer gegen Einzelrichter |
| `richter-amtsgericht-straf` | Entgendert | Beschleunigt Eroeffnungspruefung, Beweiswuerdigung und Strafzumessung |
| `richter-landgericht-strafkammer` | Entgendert | Strukturiert grosse Strafkammer, Maszregeln und Revisionspruefung |
| `richter-arbeitsgericht` | Entgendert | Bereitet Gueteverhandlung, Kuendigungsschutz und Beschlussverfahren vor |
| `richter-verwaltungsgericht` | Entgendert | Ordnet Klagearten und Eilrechtsschutz (80, 123 VwGO) |
| `richter-finanzgericht` | Entgendert | Fuehrt durch AdV, Schaetzung und Revisionszulassung |
| `richter-sozialgericht` | Entgendert | Unterstuetzt Amtsermittlung und einstweiligen Rechtsschutz |
| `richter-familiengericht` | Entgendert | Deckt Scheidung, Versorgungsausgleich, Sorge, Umgang, Unterhalt, Gewaltschutz |
| `richter-amtsgericht-insolvenz-restrukturierung` | Entgendert | Trennt InsO-Eroeffnung und StaRUG-Restrukturierung |
| `richter-amtsgericht-handelsregister` | Entgendert | Beschleunigt Eintragungspruefung und Zwischenverfuegung |
| `richter-bverfg-verfassungsbeschwerden` | Entgendert; Mitarbeitersicht verifiziert | Strukturiert Annahmevorpruefung und Grundrechtspruefung fuer das Votum |

## Empfohlene Reihenfolge zum Testen

1. `relationstechnik-zivilrecht` — die methodische Klammer fuer alle zivilrechtlichen Rollen; hier zeigt sich der groesste Hebel (vollstaendige Relation und Urteilsentwurf).
2. `richter-amtsgericht-zivil` und `richter-landgericht-zivilkammer` — die Relationstechnik in der konkreten Instanz, jetzt mit korrekter Wertgrenze 2026.
3. `richter-familiengericht` — breit gefaecherte Materie (Scheidung bis Gewaltschutz), guter Stresstest.
4. `richter-arbeitsgericht`, `richter-sozialgericht`, `richter-verwaltungsgericht`, `richter-finanzgericht` — die Fachgerichtsbarkeiten mit jeweils eigener Verfahrensordnung.
5. `richter-amtsgericht-straf` und `richter-landgericht-strafkammer` — Strafverfahren von der Eroeffnung bis zur Revision.
6. `richter-amtsgericht-insolvenz-restrukturierung` und `richter-amtsgericht-handelsregister` — die staerker formalisierten Register- und Insolvenzmaterien.
7. `richter-bverfg-verfassungsbeschwerden` — die Sondersicht des wissenschaftlichen Mitarbeiters.

## Zusammenspiel mit der Anwaltsperspektive

Die Gerichts-Plugins bilden die richterliche Sicht ab. Das Gegenstueck aus Anwalts- und Selbstvertreter-Sicht auf dieselben Normen (Klage, Streitwert, Wertgrenzen Paragraf 23 GVG, Beweisrecht, Berufung Paragraf 511 ZPO, Prozesskostenhilfe Paragraf 114 ZPO) liefert das Plugin `selbstvertreter-amtsgericht`. Beide Perspektiven auf denselben Normbestand ergeben zusammen ein vollstaendiges Bild des Verfahrens.

## Offene Empfehlung fuer den naechsten Loop

Die in v358 bis v364 angereicherten Skill-Inhalte sind inhaltlich vorhanden. Ein kuenftiger Loop kann je Skill die Querverweise (Weiter mit) und die Copy-Paste-Textbausteine weiter vereinheitlichen und je Plugin eine zweite Testakte ergaenzen. Jede dort genannte Rechtsprechung ist vor produktiver Verwendung einzeln an amtlicher Quelle zu verifizieren.
