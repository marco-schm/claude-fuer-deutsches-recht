# Megaprompt: legistik-werkstatt

## Zusammensetzung

Dieser Megaprompt enthaelt top-8 von 254 Skills (gekuerzt fuer Chat-Fenster) des Plugins `legistik-werkstatt`.

## Inhaltsverzeichnis

1. einstieg-routing — Einstieg, Triage und Routing für Legistik-Werkstatt (Gesetzgebung): ordnet Rolle (Ressort, Bundesrat, Bundestag), markie…
2. kaltstart-triage — Einstieg, Schnelltriage und Fallrouting im Legistik Werkstatt-Plugin für Bundesministerien, Bundestag, Fraktionen, Lande…
3. legistik-erstpruefung-und-mandatsziel — Legistik: Erstprüfung, Rollenklärung und Mandatsziel.
4. legw-bmleh-agrar-und-foerderungsrecht-gak-gap — Sachbereich Agrar- und Foerderungsrecht (GAK; GAP) im Geschaeftsbereich BMLEH: Normbestand (GAKG; AgrarZahlG; InVeKoSV; …
5. legw-bmi-auslaender-und-staatsangehoerigkeitsrecht — Sachbereich Auslaender- und Staatsangehoerigkeitsrecht im Geschaeftsbereich BMI: Normbestand (AufenthG; AsylG; StAG; Fre…
6. legw-bmwe-aussenwirtschaft-und-investitionspruefung — Sachbereich Aussenwirtschaft und Investitionspruefung im Geschaeftsbereich BMWE: Normbestand (AWG; AWV (Abschnitt 5); FD…
7. legw-rmap-evaluierung-und-aenderung — Lebenszyklus einer Rulemap-Norm: Versionierung; Aenderung im Builder per Drag-and-Drop; Evaluation nach NKRG und GGO; Wi…
8. begruendung-allgemein-und-besonders — Zweiteilige Begründung zu einem Gesetzesentwurf oder einer Verordnung verfassen. Anwendungsfall Referentenentwurf oder K…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Legistik-Werkstatt (Gesetzgebung): ordnet Rolle (Ressort, Bundesrat, Bundestag), markiert Frist (Beteiligungsfristen), wählt Norm (GGO Bundesregierung, Handbuch der Rechtsförmlichkeit (HdR)) und Zuständigkeit (BMJ), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet Legistik Werkstatt vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `aa-ausfuhrkontrolle` — AA Ausfuhrkontrolle
- `aa-ausfuhrkontrolle-und-aussenwirtschaftsdimension` — AA Ausfuhrkontrolle und Aussenwirtschaftsdimension
- `aa-eu-bmi-verwaltungsverfahren` — AA EU BMI Verwaltungsverfahren
- `aa-eu-grundlagen-und-ratsverfahren` — AA EU Grundlagen und Ratsverfahren
- `aa-konsular-bmas-arbeitsrecht` — AA Konsular Bmas Arbeitsrecht
- `aa-konsular-und-passrecht` — AA Konsular und Passrecht
- `aa-sanktionsumsetzung-internationale` — AA Sanktionsumsetzung Internationale
- `aa-sanktionsumsetzung-und-internationale-abkommen` — AA Sanktionsumsetzung und Internationale Abkommen
- `aa-voelkerrecht-und-vertragsgesetzgebung` — AA Voelkerrecht und Vertragsgesetzgebung
- `aenderungs-formular-portal-einreichungslogik` — Änderungs Formular Portal Einreichungslogik
- `aenderungs-formular-portal-und-einreichung` — Änderungs Formular Portal und Einreichung
- `baut-quellenkarte` — Baut Quellenkarte
- `begruendung-allgemein-und-besonders` — Begruendung Allgemein und Besonders
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Normenanker

Arbeitsfokus: Einstieg und Routing. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 20 Abs. 3 GG` — Gesetzesbindung.
- `Art. 76 Abs. 1 GG` — Gesetzesinitiative.
- `Art. 77 Abs. 1 GG` — Gesetzesbeschluss.
- `Art. 80 Abs. 1 GG` — Verordnungsermächtigung.
- `Art. 84 Abs. 1 GG` — Verwaltungsvollzug.
- `§ 42 Abs. 1 GGO` — Gesetzgebungsvorhaben.
- `§ 43 Abs. 1 GGO` — Ressortabstimmung.
- `§ 44 Abs. 1 GGO` — Gesetzesfolgen.
- `§ 45 GGO` — Beteiligung.
- `§ 46 GGO` — Rechtsförmlichkeit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Legistik Werkstatt sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `kaltstart-triage`

_Einstieg, Schnelltriage und Fallrouting im Legistik Werkstatt-Plugin für Bundesministerien, Bundestag, Fraktionen, Landesministerien, Landtage und sonstige Normgeber. Fragt Startbahn, Institution, Bundesland, Ressort, Fraktion, Verfahrensstand, Fristen, Unterlagen, Risiken und Wunsch-Output ab, s_

## Aktenstart statt Formularstart

Wenn zu Kaltstart Triage bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für Legistik Werkstatt eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin Legistik Werkstatt. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

Plugin-Fokus: Legistik-Werkstatt für Bundesministerien, Bundestag, Fraktionen, einzelne parlamentarische Initiativen in Fraktionsstärke, Landesministerien, Landesregierungen, Landtage, kommunale Rechtsämter, Kammern, Hochschulen und sonstige Normgeber. Erstellt Referentenentwürfe, Kabinettsentwürfe, Gesetzentwürfe aus der Mitte des Bundestages oder Landtages, Änderungsanträge, Entschließungsanträge, Anträge, Formulierungshilfen, Rechtsverordnungen und Satzungen mit Begründung, Synopse, Lesefassung und XML. Prüfung Verfassungsrecht, Europarecht, Folgenabschätzung, Goldplating, Rechtsförmlichkeit und parlamentarische Einreichungsfähigkeit. DOCX im passenden Regierungs-, Parlaments- oder HdR-Layout.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

Pflicht-Reihenfolge bei stummem Upload:

1. Eil- und Fristenscan: Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. Material-Klassifikation: Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. Kontextanker: Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. Rechts- und Arbeitsthema: Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. Routing: Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. Nur eine Rückfrage: Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

Was du bei stummem Upload nicht machst:

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

Antwortformat bei stummem Upload:

- Erkannt: [Materialart, Absender/Aktenzeichen falls sichtbar]
- Frist zuerst: [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- Einordnung: [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- Primärer Pfad: Wähle nach Aktenlage den nächsten passenden Skill und begründe in einem Satz, welche Frist, Zuständigkeit, Beweislast oder welches Arbeitsprodukt dadurch geklärt wird.
- Alternativen: `...`, `...`
- Nächster Schritt: [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Startbahn klären: Wer steuert das Vorhaben?

Vor jedem Entwurf zuerst die institutionelle Startbahn bestimmen. Danach erst Normebene, Entwurfsformat und Fachmodule auswählen.

| Startbahn | Typische Nutzer | Typische Outputs | Sofort zu klären |
|---|---|---|---|
| Bundesressort / Bundesregierung | Bundesministerium, Bundeskanzleramt, nachgeordnete Fachvorbereitung | Eckpunkte, Referentenentwurf, Kabinettsentwurf, Rechtsverordnung, Ressortabstimmung, NKR-Unterlagen | Ressort, Referat, Federführung, Mitzeichnung, Kabinetts- oder Hausleitungsauftrag, GGO-/HdR-Format |
| Bundestag / Fraktion / Abgeordnete | Koalitionsfraktion, Oppositionsfraktion, Gruppe oder Abgeordnete in erforderlicher Stärke | Gesetzentwurf aus der Mitte des Bundestages, Änderungsantrag, Entschließungsantrag, Antrag, Formulierungshilfe, Ausschussfassung | Fraktion/Gruppe, Regierungs- oder Oppositionsrolle, laufende Drucksache, Ausschuss, Lesung, Einreichungsform, GO-BT-Anforderungen |
| Landesregierung / Landesministerium | Landesministerium, Staatskanzlei, Landesregierung | Landesreferentenentwurf, Landesverordnung, Kabinettsvorlage, Landtagsdrucksache | Bundesland, Ressort, Landesverfassung, Landes-Geschäftsordnung, Verkündungsblatt, Beteiligungsregeln |
| Landtag / Landtagsfraktion | Regierungsfraktion, Oppositionsfraktion, Gruppe, Ausschuss | Landesgesetzentwurf aus der Mitte des Landtags, Änderungsantrag, Entschließungsantrag, Antrag | Bundesland, Landtag, Fraktion, Verfahrensstand, Geschäftsordnung des Landtags, Haushalts- und Zuständigkeitsfragen |
| Sonstiger Normgeber | Kommune, Kammer, Hochschule, Sozialversicherungsträger, Zweckverband | Satzung, Verordnung, Verwaltungsvorschrift, Bekanntmachung, Beschlussvorlage | Rechtsgrundlage, Aufsicht, Organ, Bekanntmachungsform, Genehmigungserfordernis |

Wenn die Startbahn unklar ist, frage genau eine Entscheidungsfrage: "Kommt das Vorhaben aus einem Ministerium, aus dem Bundestag/Landtag oder von einem sonstigen Normgeber?"

### 2. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle / Institution | Wer fragt: Bundesministerium, Bundestagsfraktion, Abgeordneter, Oppositionsfraktion, Landesministerium, Landtagsfraktion, Kommune, Kammer, Hochschule, Verband? | Verfahrensrecht, Ton und Einreichungsform hängen daran. |
| Gebietskörperschaft | Bund oder welches Bundesland? Bei sonstigen Normgebern: welche Gemeinde/Kammer/Hochschule und welches Aufsichtsrecht? | Landesrecht und Geschäftsordnungen unterscheiden sich stark. |
| Ressort / Fraktion / Organ | Welches Ministerium, Referat, Ausschuss, Fraktion, Gruppe, Organ oder Gremium steuert? | Zuständigkeit, Federführung und formaler Absender müssen getrennt werden. |
| Ziel | Was soll entstehen: Eckpunkte, Referentenentwurf, Kabinettsmappe, Gesetzentwurf aus der Mitte, Änderungsantrag, Entschließungsantrag, Antrag, Rechtsverordnung, Satzung, Synopse, Lesefassung, XML? | Output sofort sauber ausrichten. |
| Verfahrensstand | Vorfeld, Ressortabstimmung, Kabinett, 1./2./3. Lesung, Ausschuss, Vermittlung, Landesverfahren, Satzungsbeschluss? | Der richtige Skill hängt am Stadium. |
| Sachverhalt | Welches Problem, welche Adressaten, welche Regelungsalternativen und welche politischen Vorgaben sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Kabinettstermine, Ausschussfristen, Drucksachenschluss, Landtagsfristen, Anhörungsfristen, EU-Fristen oder Verkündungstermine? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Entwürfe, Drucksachen, Änderungsanträge, Synopsen, Kabinettsvorlagen, Stellungnahmen, Tabellen oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Kompetenzmangel, Verfassungsbruch, EU-Verstoß, Haushaltsproblem, Vollzugsdefizit, NKR-/Erfüllungsaufwand, Reputationsschaden oder politische Angreifbarkeit? | Priorität und Vorsicht einstellen. |
| Format | Regierungsstil, BT-/Landtagsdrucksache, Fraktionspapier, Ministeriumsvermerk, kurze Sprechfassung, DOCX, PDF, XML? | Ergebnis direkt verwendbar machen. |

### 3. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. Startbahn: Bund, Bundestag, Land, Landtag oder sonstiger Normgeber festlegen.
2. Eilprüfung: Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
3. Sachverhaltskern: In drei bis sieben Sätzen festhalten, was sicher ist, was politisch gewollt ist, was rechtlich streitig ist und was fehlt.
4. Arbeitsmodus wählen: Kurzprüfung, Deep Dive, Entwurf, Änderungsantrag, parlamentarischer Antrag, Kabinettsmappe, Synopse, Aktenextraktion, Red Team oder Rendern.
5. Fachmodule vorschlagen: Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
6. Nächsten Schritt anbieten: Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
7. Qualitätsgate: Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, formaler Absender, nächster Handlungsschritt.

### 4. Routing-Regeln

- Schlage immer zuerst Skills aus diesem Plugin vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: wofür, wann, welcher Input fehlt und was als Output kommt.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem Minimalpfad starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.
- Bei parlamentarischen Vorhaben immer trennen: Wer liefert fachlich zu, wer ist formaler Initiator, wer unterzeichnet, welches Parlament und welche Geschäftsordnung gelten.
- Bei Ländern immer das Bundesland abfragen und die jeweilige Landesverfassung, Geschäftsordnung der Landesregierung, Geschäftsordnung des Landtags und Verkündungsregeln als offene Prüfposten führen.
- Bei Oppositionsvorhaben nicht mit Kabinetts-, Ressort- oder NKR-Pflichten arbeiten, als wären sie formale Einreichungsvoraussetzungen. Stattdessen parlamentarische Zulässigkeit, Kompetenz, Haushaltswirkung, Verfassungsrecht, EU-Recht und politische Angreifbarkeit prüfen.

### 5. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

Kurzbild
- Ziel: [...]
- Rolle/Perspektive: [...]
- Startbahn: [Bundesressort / Bundestag / Landesministerium / Landtag / sonstiger Normgeber]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

Vorgeschlagener Workflow
1. [...]
2. [...]
3. [...]

Passende Skills aus diesem Plugin
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

Nächste Frage
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 6. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `begruendung-allgemein-und-besonders` | Zweiteilige Begründung zu einem Gesetzesentwurf oder einer Verordnung verfassen. Anwendungsfall Referentenentwurf oder Kabinettsentwurf ist fertig und Begründung muss nach HdR-Schema aufgebaut werden. Allgemeiner Teil… |
| `dokumente-rendern-docx-pdf` | Legistische Dokumente als DOCX oder PDF im Erscheinungsbild der Bundesregierung, des Bundestages, eines Landes oder eines Landtags rendern. Anwendungsfall fertiger Entwurf, parlamentarische Vorlage, Synopse oder Lesefassung soll lieferfähig ausgegeben werden. |
| `europarechtskonformitaet` | Gesetzesentwurf oder Verordnung auf Vereinbarkeit mit EU-Recht prüfen. Anwendungsfall Referent oder Verband fragt ob nationales Vorhaben mit EU-Recht vereinbar ist oder ob Notifizierungspflicht besteht. Primaerrecht… |
| `folgenabschaetzung-erfuellungsaufwand` | Erfuellungsaufwand für Buerger Wirtschaft und Verwaltung ermitteln und darstellen. Anwendungsfall Referentenentwurf soll NKR-konformes Vorblatt und Begründung erhalten oder NKR verlangt Nachbesserung. Methodik… |
| `folgenabschaetzung-nachhaltigkeit` | Weitere Folgen und Nachhaltigkeitsprüfung für Gesetzesentwurf erstellen. Anwendungsfall Referentenentwurf benoetigt Vorblatt Abschnitt G und Begründung A.VI.6 zu Nachhaltigkeitsfolgen. UN-SDGs prüfen welche betroffen… |
| `formulierungshilfe-bauen` | Formulierungshilfe, Änderungsantrag, Gesetzentwurf aus der Mitte des Bundestages oder Landtages, Entschließungsantrag oder parlamentarischen Antrag bauen. Geeignet für Ministerialzulieferungen, Koalitionsfraktionen, Oppositionsfraktionen, Gruppen oder Abgeordnete in der erforderlichen Stärke. |
| `gesetzesentwurf-kabinett` | Kabinettsentwurf der Bundesregierung oder Landesregierung aus dem Referentenentwurf nach Ressortabstimmung erstellen. Anwendungsfall Ressortabstimmung und Verbandeanhoerung sind abgeschlossen Kabinettsvorlage muss… |
| `gesetzgebungskompetenz-pruefen` | Gesetzgebungskompetenz nach Art. 70 bis 74 GG prüfen bevor Entwurf aufgesetzt wird. Anwendungsfall Referent oder Verband fragt ob Bund oder Land regelungsbefogt ist. Ausschließliche Bundeskompetenz Art. 71 i.V.m. 73… |
| `goldplating-vermeiden` | Goldplating bei nationaler EU-Richtlinien-Umsetzung identifizieren und bewerten. Anwendungsfall Referentenentwurf setzt EU-Richtlinie um und muss auf ueberschiessende nationale Regelungen über den… |
| `inkrafttreten-uebergangsrecht` | Inkrafttretens- und Übergangsregelung für Gesetze und Verordnungen formulieren. Anwendungsfall Entwurf ist inhaltlich fertig Artikel Inkrafttreten und Übergangsrecht müssen noch ergaenzt werden. Standardformel… |
| `legistik-auftragsaufnahme` | Legistischen Auftrag strukturiert aufnehmen: Startbahn, Bundesland, Ressort, Fraktion, formalen Initiator, Adressaten, Eingriffstiefe, Dringlichkeit, Entwurfstyp und Beteiligte klären. |
| `lesefassung-konsolidiert` | Konsolidierte Lesefassung des geaenderten Stammgesetzes nach Inkrafttreten erstellen. Anwendungsfall Fachreferat Vollzugsbehoerde oder Anwalt will wissen wie das Gesetz nach Änderung aussieht ohne… |
| `normenkartierung` | Alle durch ein legistisches Vorhaben beruehrten Normen kartieren und Änderungsmatrix aufbauen. Anwendungsfall neues Regelungsvorhaben soll vorbereitet werden alle betroffenen Gesetze Verordnungen und Verweisketten… |
| `normenkontrollrat-kmu-check` | Vorlage an Nationalen Normenkontrollrat NKR vorbereiten und KMU-Check durchführen. Anwendungsfall Referentenentwurf muss vor Kabinettsbefassung dem NKR vorgelegt werden. Standard-Kostenmodell SKK Buerokratiekosten.… |
| `normhierarchie-routing` | Richtige Startbahn und Normebene bestimmen: Bundesgesetz, Landesgesetz, Rechtsverordnung, Satzung, Verwaltungsvorschrift, parlamentarischer Antrag oder Entschließungsantrag. |
| `referentenentwurf-bauen` | Vollständigen Referentenentwurf des Bundes oder Landes aufbauen, wenn ein Bundes- oder Landesministerium den Entwurf steuert. Klärt Bundesland, Ressort, GGO oder Landesvorgaben und HdR-/Landesstil. |
| `satzungskompetenz-pruefen` | Satzungskompetenz für Koerperschaften und Anstalten des öffentlichen Rechts prüfen. Anwendungsfall Gemeinde Kammer Hochschule oder Sozialversicherungstraeger will Satzung erlassen und Rechtsgrundlage muss geprüft… |
| `schulung-legistik` | Trainerleitfaden für Legistik-Schulung mit der Arbeitsakte elektronisches Pflichtpostfach. Anwendungsfall Referenten oder Mitarbeiter von Verbanden sollen legistische Kernkompetenz in zwei Tagen Inhouse-Schulung oder… |
| `synopse-erstellen` | Synopse als Dreispalten-Tabelle bisheriges Recht neues Recht Änderungsbefehl erstellen. Anwendungsfall Ressortabstimmung Bundestag oder Bundesrat brauchen vergleichende Darstellung um Änderungen schnell zu erfassen.… |
| `terminologie-konsistenz` | Terminologie-Konsistenz im legistischen Entwurf prüfen und Begriffstabelle aufbauen. Anwendungsfall Entwurf enthaelt neue Legaldefinitionen oder Referent prüft ob Begriffe konsistent verwendet werden und keine… |
| `verbaendeanhoerung-ressortabstimmung` | Verbandeanhoerung und Ressortabstimmung nach GGO steuern und auswerten. Anwendungsfall Referentenentwurf ist fertig und muss Verbaenden und Ressorts zugeleitet werden vor Kabinettsbefassung. Anschreiben Liste zu… |
| `verfassungsmaessigkeit-quercheck` | Querschnittsprüfung Verfassungsmäßigkeit eines Gesetzesentwurfs oder einer Verordnung. Anwendungsfall Entwurf soll vor Ressortabstimmung oder NKR-Vorlage verfassungsrechtlich abgesichert werden oder Verband prüft… |
| `verordnungsermaechtigung-art80` | Verordnungsermaechtigung nach Art. 80 Abs. 1 GG prüfen bevor Rechtsverordnung entworfen wird. Anwendungsfall geplante Rechtsverordnung und Anwalt oder Referent fragt ob Ermaechtigungsgrundlage genuegend bestimmt ist.… |
| `xml-paralleldarstellung` | Maschinenlesbare Paralleldarstellung eines Gesetzesentwurfs in LegalDocML.de oder eNorm-XML erstellen. Anwendungsfall eGesetzgebung BMJ Bundesgesetzblatt online oder automatisierte Weiterverarbeitung erfordert… |
| `zirkelschluss-pruefen` | Zirkelschluesse und kreisfreie Verweisketten im legistischen Entwurf aufspueren. Anwendungsfall Entwurf enthaelt viele Querverweise und soll auf ungewollte Zirkel und tautologische Definitionen geprüft werden. Direkte… |

## Worum geht es?

Die Legistik-Werkstatt ist ein Plugin für Referentinnen und Referenten in Bundesministerien und Landesministerien, für Bundestags- und Landtagsfraktionen, für Oppositionsarbeit, Ausschussarbeit, kommunale und kammerliche Normgeber, Verfassungsrechtlerinnen und Verfassungsrechtler sowie für fachlich zuliefernde Verbände. Sie hilft, Gesetzesentwürfe, Änderungsanträge, Entschließungsanträge, Rechtsverordnungen und Satzungen zu erstellen, zu prüfen und in den jeweils passenden Regierungs- oder Parlamentsprozess einzubringen.

Das Plugin deckt alle Phasen des Gesetzgebungsverfahrens ab: von der Auftragsaufnahme über den Referentenentwurf, die Ressortabstimmung, Verbandeanhoerungen, die Kabinettsreife, Synopsen und Lesefassungen bis zur XML-Paralleldarstellung. Es enthaelt ausserdem Quercheckmodule für Verfassungsmaessigkeit, Europarechtskonformitaet, Erfuellungsaufwand und Goldplating-Vermeidung.

## Wann brauchen Sie diese Skill?

- Ein Referat im Bundesministerium erstellt einen Referentenentwurf und braucht eine strukturierte Auftragsaufnahme mit Regelungszielen.
- Eine Bundestagsfraktion will einen Gesetzentwurf aus der Mitte des Bundestages oder einen Änderungsantrag zu einer laufenden Drucksache bauen.
- Eine Oppositionsfraktion braucht einen formal tragfähigen Antrag, Entschließungsantrag oder Alternativentwurf mit klarer Begründung und Angriffsfestigkeit.
- Ein Landesministerium oder eine Landtagsfraktion arbeitet in einem bestimmten Bundesland und muss Landesverfassung, Landes-Geschäftsordnung, Landtagsverfahren und Verkündungsregeln sauber mitführen.
- Eine Normenkontrollrats-Vorlage muss fristgerecht vorbereitet und mit einem KMU-Check versehen werden.
- Ein Ministerium will einen bestehenden Entwurf auf Verfassungsmaessigkeit und Europarechtskonformitaet prüfen.
- Eine Rechtsverordnung wird entworfen und die Verordnungsermaechtigung nach Art. 80 GG muss geprueft werden.
- Nach Inkrafttreten soll eine konsolidierte Lesefassung des geaenderten Stammgesetzes erstellt werden.

## Fachbegriffe (kurz erklaert)

- HdR — Handbuch der Rechtsfoermlichkeit; Leitfaden des Bundesjustizministeriums für die Formulierung von Rechtstexten.
- GGO — Gemeinsame Geschäftsordnung der Bundesministerien; regelt Verfahren und Fristen für die Ressortabstimmung.
- NKR — Nationaler Normenkontrollrat; unabhaengiges Gremium, das Erfuellungsaufwand und buerokratische Belastungen prüft.
- Gesetzentwurf aus der Mitte — Parlamentarische Gesetzesinitiative, die nicht von der Bundesregierung oder Landesregierung, sondern aus dem Parlament kommt; im Bund typischerweise durch eine Fraktion oder Abgeordnete in der erforderlichen Stärke.
- Formulierungshilfe — Fachlicher Zuliefertext, häufig aus einem Ministerium, der formal als parlamentarische Vorlage, Änderungsantrag oder Ausschussfassung weiterverwendet werden kann; formaler Initiator und fachlicher Verfasser sind sauber zu trennen.
- Goldplating — Ueberimplementierung von EU-Richtlinien: nationale Zusatzanforderungen über das EU-Mindestmass hinaus.
- Synopse — Gegenueberststellung von bisherigem Recht, neuem Recht und Änderungsbefehl in einer Dreispalten-Tabelle.
- LegalDocML — Maschinenlesbares XML-Format für deutsche Rechtstexte; Standard des Bundesjustizministeriums.
- Normenkartierung — Systematische Erfassung aller durch ein Vorhaben beruehrten Normen und ihrer Änderungsbedarfe.
- Kabinettsentwurf — Abgestimmter Regierungsentwurf, der dem Kabinett zur Beschlussfassung vorgelegt wird.

## Rechtsgrundlagen

- Art. 70-74 GG (Gesetzgebungskompetenzen Bund und Länder)
- Art. 80 Abs. 1 GG (Verordnungsermaechtigung)
- Art. 76-78 GG (Gesetzgebungsverfahren im Bund)
- Geschäftsordnung des Deutschen Bundestages, insbesondere Vorlagen aus der Mitte des Bundestages
- Landesverfassungen, Geschäftsordnungen der Landesregierungen und Geschäftsordnungen der Landtage
- GGO (Gemeinsame Geschäftsordnung der Bundesministerien)
- Art. 288 AEUV (Wirkung von EU-Verordnungen und Richtlinien)
- Art. 267 AEUV (Vorabentscheidungsverfahren EuGH)

## Schritt-für-Schritt: Einstieg ins Plugin

1. Startbahn klären: Bundesressort, Bundestag, Landesressort, Landtag oder sonstiger Normgeber.
2. Legistischen Auftrag aufnehmen und Regelungsziele klären (`legistik-auftragsaufnahme`).
3. Normhierarchie und Kompetenzgrundlage bestimmen (`normhierarchie-routing`, `gesetzgebungskompetenz-pruefen`).
4. Geeigneten Entwurfstyp auswaehlen: Referentenentwurf, Kabinettsentwurf, Gesetzentwurf aus der Mitte, Änderungsantrag, Antrag, Rechtsverordnung oder Satzung.
5. Quercheck-Module nutzen: Verfassungsmaessigkeit, Europarecht, Goldplating, Erfuellungsaufwand, Rechtsförmlichkeit und parlamentarische Zulässigkeit.
6. Ressortabstimmung, Verbändeanhörung, parlamentarische Einbringung oder Satzungsbeschluss steuern, dann zur lieferfähigen Fassung führen.

## Skill-Tour (was gibt es hier?)

- `legistik-auftragsaufnahme` — Legistischen Auftrag strukturiert aufnehmen und in Regelungsziele umwandeln.
- `normhierarchie-routing` — Richtige Startbahn und Normebene bestimmen: Regierung, Parlament, Gesetz, Verordnung, Satzung oder Antrag.
- `gesetzgebungskompetenz-pruefen` — Gesetzgebungskompetenz nach Art. 70-74 GG prüfen bevor Entwurf aufgesetzt wird.
- `satzungskompetenz-pruefen` — Satzungskompetenz für Koerperschaften und Anstalten des öffentlichen Rechts prüfen.
- `verordnungsermaechtigung-art80` — Verordnungsermaechtigung nach Art. 80 Abs. 1 GG prüfen bevor Rechtsverordnung entworfen wird.
- `referentenentwurf-bauen` — Vollstaendigen Referentenentwurf des Bundes oder Landes aufbauen.
- `gesetzesentwurf-kabinett` — Kabinettsentwurf nach Ressortabstimmung aus dem Referentenentwurf erstellen.
- `formulierungshilfe-bauen` — Formulierungshilfe, Änderungsantrag, Gesetzentwurf aus der Mitte, Entschließungsantrag oder Antrag für Bundestag und Landtage aufbauen.
- `begruendung-allgemein-und-besonders` — Zweiteilige Begruendung zu Gesetzesentwurf oder Verordnung (Allgemeiner Teil, Besonderer Teil) verfassen.
- `verfassungsmaessigkeit-quercheck` — Querschnittspruefung Verfassungsmaessigkeit eines Gesetzesentwurfs oder einer Verordnung.
- `europarechtskonformitaet` — Gesetzesentwurf oder Verordnung auf Vereinbarkeit mit EU-Recht prüfen.
- `goldplating-vermeiden` — Goldplating bei nationaler EU-Richtlinien-Umsetzung identifizieren und bewerten.
- `folgenabschaetzung-erfuellungsaufwand` — Erfuellungsaufwand für Buerger, Wirtschaft und Verwaltung ermitteln und darstellen.
- `folgenabschaetzung-nachhaltigkeit` — Weitere Folgen und Nachhaltigkeitspruefung für Gesetzesentwurf erstellen.
- `normenkontrollrat-kmu-check` — Vorlage an den NKR vorbereiten und KMU-Check durchfuehren.
- `normenkartierung` — Alle durch ein legistisches Vorhaben beruehrten Normen kartieren und Änderungsmatrix aufbauen.
- `terminologie-konsistenz` — Terminologie-Konsistenz im legistischen Entwurf prüfen und Begriffstabelle aufbauen.
- `zirkelschluss-pruefen` — Zirkelschluesse und kreisfreie Verweisketten im legistischen Entwurf aufspueren.
- `inkrafttreten-uebergangsrecht` — Inkrafttretens- und Uebergangsregelungen für Gesetze und Verordnungen formulieren.
- `verbaendeanhoerung-ressortabstimmung` — Verbandeanhoerung und Ressortabstimmung nach GGO steuern und auswerten.
- `synopse-erstellen` — Synopse als Dreispalten-Tabelle (bisheriges Recht, neues Recht, Änderungsbefehl) erstellen.
- `lesefassung-konsolidiert` — Konsolidierte Lesefassung des geaenderten Stammgesetzes nach Inkrafttreten erstellen.
- `xml-paralleldarstellung` — Maschinenlesbare Paralleldarstellung in LegalDocML.de oder eNorm-XML erstellen.
- `dokumente-rendern-docx-pdf` — Legistische Dokumente als DOCX oder PDF im offiziellen HdR-Layout rendern.
- `schulung-legistik` — Trainerleitfaden für Legistik-Fortbildungen mit der Arbeitsakte erstellen.

## Worauf besonders achten

- Kompetenzgrundlage zuerst: Ohne geklarte Gesetzgebungskompetenz nach Art. 70 ff. GG darf kein Entwurf aufgesetzt werden.
- Startbahn sauber halten: Ministerielle Fachzulieferung, formaler parlamentarischer Initiator und politischer Auftraggeber dürfen nicht vermischt werden.
- Landesmodus ernst nehmen: Ohne Bundesland keine verlässliche Aussage zu Landesverfassung, Landtagsgeschäftsordnung, Kabinettsverfahren und Verkündung.
- Goldplating ist politisch und juristisch heikel: Nationale Mehrbelastungen über EU-Mindestanforderungen hinaus müssen explizit begruendet werden.
- NKR-Fristen sind verbindlich: Vorlage muss mit vollstaendigen Erfuellungsaufwands-Angaben rechtzeitig erfolgen.
- Terminologie-Konsistenz ist elementar: Verschiedene Begriffe für dasselbe Konzept können zu Auslegungsstreitigkeiten fuehren.
- Uebergangsrecht nicht vergessen: Altfallregelungen und Bestandsschutz sichern Rechtsicherheit und vermeiden Verfassungsruegen.

## Typische Fehler

- Referentenentwurf ohne Verfassungsmaessigkeits-Check: Entwurf wird in der Ressortabstimmung oder im Parlament wegen Grundrechtsverletzung zurueckgewiesen.
- Bundestags- oder Landtagsinitiative ohne klaren formalen Initiator: Der Text ist fachlich brauchbar, aber nicht einreichungsfähig.
- Landesentwurf nach Bundes-Schablone: Landeszuständigkeiten, Zitierregeln, Verkündungsblatt oder Landtagsformat werden falsch.
- Verordnungsermaechtigung zu unbestimmt: Art. 80 Abs. 1 GG verlangt Inhalt, Zweck und Ausmass — Blankoermaechtigung ist nichtig.
- Goldplating unerkannt: Nationale Umsetzung geht über die Richtlinienpflichten hinaus, ohne dass dies im Entwurf kenntlich gemacht wird.
- Synopse fehlt: Ressortabstimmung und parlamentarische Beratung werden durch fehlende Gegenueberststellung ernsthaft erschwert.
- Inkrafttreten ohne Uebergangsrecht: Adressaten können sich nicht rechtzeitig auf neue Pflichten einstellen.

## Quellen und Aktualitaet

- Stand: 05/2026
- GG (Grundgesetz) in der zum Stand-Datum geltenden Fassung
- GGO (Gemeinsame Geschäftsordnung der Bundesministerien) in der geltenden Fassung
- HdR (Handbuch der Rechtsfoermlichkeit) 3. Auflage des Bundesjustizministeriums
- Geschäftsordnung des Deutschen Bundestages und einschlägige Landtags-Geschäftsordnungen jeweils aktuell prüfen

---

## Skill: `legistik-erstpruefung-und-mandatsziel`

_Legistik: Erstprüfung, Rollenklärung und Mandatsziel._

# Legistik: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu Legistik Erstpruefung Und Mandatsziel bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für Legistik Werkstatt eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Normenanker

Arbeitsfokus: Legistik: Erstprüfung, Rollenklärung und Mandatsziel. Prüfe diese Anker am Sachverhalt; ergänze nur Normen, die denselben Output, dieselbe Frist oder dieselbe Beweisfrage tragen:

- `Art. 20 Abs. 3 GG` — Gesetzesbindung.
- `Art. 76 Abs. 1 GG` — Gesetzesinitiative.
- `Art. 77 Abs. 1 GG` — Gesetzesbeschluss.
- `Art. 80 Abs. 1 GG` — Verordnungsermächtigung.
- `Art. 84 Abs. 1 GG` — Verwaltungsvollzug.
- `§ 42 Abs. 1 GGO` — Gesetzgebungsvorhaben.
- `§ 43 Abs. 1 GGO` — Ressortabstimmung.
- `§ 44 Abs. 1 GGO` — Gesetzesfolgen.
- `§ 45 GGO` — Beteiligung.
- `§ 46 GGO` — Rechtsförmlichkeit.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: GGO Ressortbeteiligung i.d.R. 4 Wochen, NKR-Stellungnahme 4 Wochen, Bundesrat 1. Durchgang 6 Wochen / 9 Wochen, Vermittlungsausschuss nach Bedarf.
- Tragende Normen verifizieren: GGO §§ 40-49 (Rechtsetzungsverfahren), Handbuch der Rechtsförmlichkeit (BMJ), NKR-Gesetz, BGleiG, IT-Konsolidierungs-Konzept, eNorm-Standard, GG Art. 76, 77, 78 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Ressort (BMJ und Fachressort), Bundeskanzleramt, Bundesrat, NKR, Bundestagsausschüsse, Bundesregierung, Wissenschaftliche Dienste, Lobbyregister.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Referentenentwurf, BT-Drucksache, Gesetzesfolgenabschätzung, NKR-Stellungnahme, Verbändeanhörungs-Stellungnahme, Synopse, Erfüllungsaufwandsberechnung — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Spezialwissen: Legistik: Erstprüfung, Rollenklärung und Mandatsziel
- Normen-/Quellenanker: XML.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. Fallbild bilden: Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. Rechtsrahmen setzen: Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld Legistik prüfen.
3. Prüfpunkte abarbeiten: Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. Risiko bewerten: Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. Anschluss bauen: Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `legw-bmleh-agrar-und-foerderungsrecht-gak-gap`

_Sachbereich Agrar- und Foerderungsrecht (GAK; GAP) im Geschaeftsbereich BMLEH: Normbestand (GAKG; AgrarZahlG; InVeKoSV; DueV; OeLG; BWaldG-Bezuege; AgrarStatG.); Akteure (BLE; Laender-Landwirtschaftsministerien; Generaldirektion AGRI; BMEL/BMLEH.); EU-Bezug (GAP-Reform; Direktzahlungen-VO; ELER-VO; Konditionalitaet.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-bmleh (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-bmleh (Heranfuehrung)._

# Agrar- und Foerderungsrecht (GAK; GAP) (BMLEH)

> Vierter und tiefster Skill in der Ressort-Kette: Sachfeld-Kompass fuer das Spezialthema Agrar- und Foerderungsrecht (GAK; GAP) im Geschaeftsbereich BMLEH. Liefert dem Normgeber Normbestand, Akteure, EU-Bezug und Pruefpunkte fuer dieses eine Sachfeld.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme`
- Ressort-Kompass aus `legw-ressort-bmleh`
- Aufgabenmatrix aus `legw-ressortaufgaben-bmleh`
- Konkrete Sachfrage oder konkretes Normvorhaben in diesem Sachbereich

## Normbestand

Kernbestand des Sachfelds: GAKG; AgrarZahlG; InVeKoSV; DueV; OeLG; BWaldG-Bezuege; AgrarStatG.

Pruefreihenfolge: Verfassungsrang vor Bundesgesetz vor Rechtsverordnung vor Verwaltungsvorschrift. Bei EU-Bezug zuerst Unionsrecht (Vorrang und Anwendungsbefehl), dann nationale Umsetzungs- und Begleitnormen.

## Akteure und Aufsicht

BLE; Laender-Landwirtschaftsministerien; Generaldirektion AGRI; BMEL/BMLEH.

Akteurskarte erstellen: federfuehrende Einheit im Haus; mitzeichnende Ressorts; nachgeordnete Behoerden im Vollzug; betroffene Laenderbehoerden; Verbaende; wissenschaftliche Beiraete; zustaendige Gerichtsbarkeit.

## EU- und voelkerrechtlicher Bezug

GAP-Reform; Direktzahlungen-VO; ELER-VO; Konditionalitaet.

Pruefen: einschlaegige Verordnung oder Richtlinie? Umsetzungsfrist? Notifizierungspflicht? Beihilferechtlicher Vorbehalt? Vorabentscheidungsverfahren absehbar?

## Typische Legistik-Aufgaben

Direktzahlungen; Konditionalitaet; OeKo-Regelungen; Foerderung im 2. Saeule (ELER); Antragsverfahren.

Schrittfolge fuer den Normgeber:

1. Sachverhalt und Regelungsziel in diesem Sachfeld pruefen
2. Vorhandene Normen kartieren; Lueckenanalyse
3. Eingriffsintensitaet und Adressatenkreis bestimmen
4. Verfassungs- und Europarechtskonformitaet pruefen
5. Tatbestand und Rechtsfolge sauber fassen; Bestimmtheit pruefen
6. Vollzugs- und Aufsichtsstruktur kontrollieren
7. Begleit- und Folgenormen (Verordnungen; Verwaltungsvorschriften) mitplanen

## Stolpersteine und Pruefpunkte

EU-Konformitaet; Sanktionen bei Verstoessen; Doppelfoerderung; Strukturwandel.

Erweiterte Pruefpunkte: Bestimmtheitsgebot; Verhaeltnismaessigkeit; Rueckwirkungsverbot; Gleichheitssatz; Datenschutz-Grundverordnung bei Datenverarbeitung; Wechselwirkungen zu anderen Ressorts; Befristung und Evaluation.

## Output

Sachfeld-Kompass:

```
Sachfeld:           Agrar- und Foerderungsrecht (GAK; GAP)
Ressort:            BMLEH
Kernnormen:         GAKG; AgrarZahlG; InVeKoSV; DueV; OeLG; BWaldG-Bezuege; AgrarStatG.
Akteure/Aufsicht:   BLE; Laender-Landwirtschaftsministerien; Generaldirektion AGRI; BMEL/BMLEH.
EU/Voelkerrecht:    GAP-Reform; Direktzahlungen-VO; ELER-VO; Konditionalitaet.
Pruefpunkte:        <verfassungs-/europarechtlich; bestimmt; verhaeltnismaessig>
Stolpersteine:      <Sachfeld-spezifisch>
Naechste Skills:    legw-ressortaufgaben-bmleh; normhierarchie-routing;
                    normenkartierung; verfassungsmaessigkeit-quercheck;
                    europarechtskonformitaet; rechtsfolgenabschaetzung
```

## Anschluss an die Legistik-Kette

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-bmleh` -> `legw-ressortaufgaben-bmleh` -> `legw-bmleh-agrar-und-foerderungsrecht-gak-gap` (hier) -> `normhierarchie-routing` und Querprueferei.

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

---

## Skill: `legw-bmi-auslaender-und-staatsangehoerigkeitsrecht`

_Sachbereich Auslaender- und Staatsangehoerigkeitsrecht im Geschaeftsbereich BMI: Normbestand (AufenthG; AsylG; StAG; FreizuegG/EU; AZRG; AsylbLG (mit BMAS).); Akteure (BAMF; Auslaenderbehoerden; Bundespolizei.); EU-Bezug (GEAS; Dublin-VO; Rueckfuehrungs-RL; Visa-Kodex; Schengen.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-bmi (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-bmi (Heranfuehrung)._

# Auslaender- und Staatsangehoerigkeitsrecht (BMI)

> Vierter und tiefster Skill in der Ressort-Kette: Sachfeld-Kompass fuer das Spezialthema Auslaender- und Staatsangehoerigkeitsrecht im Geschaeftsbereich BMI. Liefert dem Normgeber Normbestand, Akteure, EU-Bezug und Pruefpunkte fuer dieses eine Sachfeld.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme`
- Ressort-Kompass aus `legw-ressort-bmi`
- Aufgabenmatrix aus `legw-ressortaufgaben-bmi`
- Konkrete Sachfrage oder konkretes Normvorhaben in diesem Sachbereich

## Normbestand

Kernbestand des Sachfelds: AufenthG; AsylG; StAG; FreizuegG/EU; AZRG; AsylbLG (mit BMAS).

Pruefreihenfolge: Verfassungsrang vor Bundesgesetz vor Rechtsverordnung vor Verwaltungsvorschrift. Bei EU-Bezug zuerst Unionsrecht (Vorrang und Anwendungsbefehl), dann nationale Umsetzungs- und Begleitnormen.

## Akteure und Aufsicht

BAMF; Auslaenderbehoerden; Bundespolizei.

Akteurskarte erstellen: federfuehrende Einheit im Haus; mitzeichnende Ressorts; nachgeordnete Behoerden im Vollzug; betroffene Laenderbehoerden; Verbaende; wissenschaftliche Beiraete; zustaendige Gerichtsbarkeit.

## EU- und voelkerrechtlicher Bezug

GEAS; Dublin-VO; Rueckfuehrungs-RL; Visa-Kodex; Schengen.

Pruefen: einschlaegige Verordnung oder Richtlinie? Umsetzungsfrist? Notifizierungspflicht? Beihilferechtlicher Vorbehalt? Vorabentscheidungsverfahren absehbar?

## Typische Legistik-Aufgaben

Aufenthaltszwecke ordnen; Schutzstatus; Familiennachzug; Einbuergerung; Abschiebung; Datenuebermittlung zwischen Behoerden.

Schrittfolge fuer den Normgeber:

1. Sachverhalt und Regelungsziel in diesem Sachfeld pruefen
2. Vorhandene Normen kartieren; Lueckenanalyse
3. Eingriffsintensitaet und Adressatenkreis bestimmen
4. Verfassungs- und Europarechtskonformitaet pruefen
5. Tatbestand und Rechtsfolge sauber fassen; Bestimmtheit pruefen
6. Vollzugs- und Aufsichtsstruktur kontrollieren
7. Begleit- und Folgenormen (Verordnungen; Verwaltungsvorschriften) mitplanen

## Stolpersteine und Pruefpunkte

EU-rechtliche Mindeststandards; Kettenduldungen; Grundrechte Art. 6 GG; Voelkerrecht; sichere Herkunftsstaaten.

Erweiterte Pruefpunkte: Bestimmtheitsgebot; Verhaeltnismaessigkeit; Rueckwirkungsverbot; Gleichheitssatz; Datenschutz-Grundverordnung bei Datenverarbeitung; Wechselwirkungen zu anderen Ressorts; Befristung und Evaluation.

## Output

Sachfeld-Kompass:

```
Sachfeld:           Auslaender- und Staatsangehoerigkeitsrecht
Ressort:            BMI
Kernnormen:         AufenthG; AsylG; StAG; FreizuegG/EU; AZRG; AsylbLG (mit BMAS).
Akteure/Aufsicht:   BAMF; Auslaenderbehoerden; Bundespolizei.
EU/Voelkerrecht:    GEAS; Dublin-VO; Rueckfuehrungs-RL; Visa-Kodex; Schengen.
Pruefpunkte:        <verfassungs-/europarechtlich; bestimmt; verhaeltnismaessig>
Stolpersteine:      <Sachfeld-spezifisch>
Naechste Skills:    legw-ressortaufgaben-bmi; normhierarchie-routing;
                    normenkartierung; verfassungsmaessigkeit-quercheck;
                    europarechtskonformitaet; rechtsfolgenabschaetzung
```

## Anschluss an die Legistik-Kette

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-bmi` -> `legw-ressortaufgaben-bmi` -> `legw-bmi-auslaender-und-staatsangehoerigkeitsrecht` (hier) -> `normhierarchie-routing` und Querprueferei.

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

---

## Skill: `legw-bmwe-aussenwirtschaft-und-investitionspruefung`

_Sachbereich Aussenwirtschaft und Investitionspruefung im Geschaeftsbereich BMWE: Normbestand (AWG; AWV (Abschnitt 5); FDI-Screening-VO (EU); KrWaffKG.); Akteure (BMWE; BMI; AA; BMF; Bundeskanzleramt.); EU-Bezug (FDI-Screening-VO; sektorale EU-Schwellen; Pruefberichte an EU.); typische Legistik-Aufgaben und Pruefpunkte. Output Sachfeld-Kompass mit Normhierarchie; Akteurskarte; Pruefliste; Anschlusspfaden. Anschluss legw-ressortaufgaben-bmwe (Aufgaben) und normhierarchie-routing (Normwahl). Abgrenzung zu legw-ressort-bmwe (Heranfuehrung)._

# Aussenwirtschaft und Investitionspruefung (BMWE)

> Vierter und tiefster Skill in der Ressort-Kette: Sachfeld-Kompass fuer das Spezialthema Aussenwirtschaft und Investitionspruefung im Geschaeftsbereich BMWE. Liefert dem Normgeber Normbestand, Akteure, EU-Bezug und Pruefpunkte fuer dieses eine Sachfeld.

## Eingaben

- Auftragsblatt aus `legistik-auftragsaufnahme`
- Ressort-Kompass aus `legw-ressort-bmwe`
- Aufgabenmatrix aus `legw-ressortaufgaben-bmwe`
- Konkrete Sachfrage oder konkretes Normvorhaben in diesem Sachbereich

## Normbestand

Kernbestand des Sachfelds: AWG; AWV (Abschnitt 5); FDI-Screening-VO (EU); KrWaffKG.

Pruefreihenfolge: Verfassungsrang vor Bundesgesetz vor Rechtsverordnung vor Verwaltungsvorschrift. Bei EU-Bezug zuerst Unionsrecht (Vorrang und Anwendungsbefehl), dann nationale Umsetzungs- und Begleitnormen.

## Akteure und Aufsicht

BMWE; BMI; AA; BMF; Bundeskanzleramt.

Akteurskarte erstellen: federfuehrende Einheit im Haus; mitzeichnende Ressorts; nachgeordnete Behoerden im Vollzug; betroffene Laenderbehoerden; Verbaende; wissenschaftliche Beiraete; zustaendige Gerichtsbarkeit.

## EU- und voelkerrechtlicher Bezug

FDI-Screening-VO; sektorale EU-Schwellen; Pruefberichte an EU.

Pruefen: einschlaegige Verordnung oder Richtlinie? Umsetzungsfrist? Notifizierungspflicht? Beihilferechtlicher Vorbehalt? Vorabentscheidungsverfahren absehbar?

## Typische Legistik-Aufgaben

Sektoren festlegen; Pruefverfahren; Untersagung oder Auflagen; Mitberatung im Bundes-sicherheitsrat.

Schrittfolge fuer den Normgeber:

1. Sachverhalt und Regelungsziel in diesem Sachfeld pruefen
2. Vorhandene Normen kartieren; Lueckenanalyse
3. Eingriffsintensitaet und Adressatenkreis bestimmen
4. Verfassungs- und Europarechtskonformitaet pruefen
5. Tatbestand und Rechtsfolge sauber fassen; Bestimmtheit pruefen
6. Vollzugs- und Aufsichtsstruktur kontrollieren
7. Begleit- und Folgenormen (Verordnungen; Verwaltungsvorschriften) mitplanen

## Stolpersteine und Pruefpunkte

Zeitknappheit; Geheimhaltung; Wechselbezug zur Ausfuhrkontrolle; Klage vor BVerwG.

Erweiterte Pruefpunkte: Bestimmtheitsgebot; Verhaeltnismaessigkeit; Rueckwirkungsverbot; Gleichheitssatz; Datenschutz-Grundverordnung bei Datenverarbeitung; Wechselwirkungen zu anderen Ressorts; Befristung und Evaluation.

## Output

Sachfeld-Kompass:

```
Sachfeld:           Aussenwirtschaft und Investitionspruefung
Ressort:            BMWE
Kernnormen:         AWG; AWV (Abschnitt 5); FDI-Screening-VO (EU); KrWaffKG.
Akteure/Aufsicht:   BMWE; BMI; AA; BMF; Bundeskanzleramt.
EU/Voelkerrecht:    FDI-Screening-VO; sektorale EU-Schwellen; Pruefberichte an EU.
Pruefpunkte:        <verfassungs-/europarechtlich; bestimmt; verhaeltnismaessig>
Stolpersteine:      <Sachfeld-spezifisch>
Naechste Skills:    legw-ressortaufgaben-bmwe; normhierarchie-routing;
                    normenkartierung; verfassungsmaessigkeit-quercheck;
                    europarechtskonformitaet; rechtsfolgenabschaetzung
```

## Anschluss an die Legistik-Kette

- `legistik-auftragsaufnahme` -> `legw-ressort-router` -> `legw-ressort-bmwe` -> `legw-ressortaufgaben-bmwe` -> `legw-bmwe-aussenwirtschaft-und-investitionspruefung` (hier) -> `normhierarchie-routing` und Querprueferei.

## Abgrenzung

Abgrenzung zu legistik-auftragsaufnahme (Erstaufnahme), normhierarchie-routing (Normwahl), normenkartierung (Bestand), verfassungsmaessigkeit-quercheck (Verfassungsfragen), europarechtskonformitaet (EU-Bezug), folgenabschaetzung-* (Folgenabschaetzung). Dieser Skill dient als Sachfeld-Kompass; er ersetzt nicht die Normprueferei, sondern liefert das Sachverstaendnis fuer den Normgeber.

## Quellenregel

Alle Quellen aus dem Bestand: gesetze-im-internet.de; bundestag.de; bundesrat.de; bundesregierung.de; bmj.de; bundesverfassungsgericht.de; bundesgerichtshof.de; bverwg.de; eur-lex.europa.eu; dejure.org; openjur.de; normenkontrollrat.bund.de. Keine Sekundaerblogs oder Webportale. Jede Norm mit voller Fundstelle und Datum.

---

## Skill: `legw-rmap-evaluierung-und-aenderung`

_Lebenszyklus einer Rulemap-Norm: Versionierung; Aenderung im Builder per Drag-and-Drop; Evaluation nach NKRG und GGO; Wirkungskontrolle; Rueckkopplung aus dem Vollzug. Output Aenderungs- und Evaluationsplan mit Zustaendigkeiten; Auslaufdaten und KPI. Anschluss legw-rechtsfolgenabschaetzung-leitfaden. Abgrenzung zur reinen Gesetzgebungstechnik; hier wird die Pflege im Zeitverlauf organisiert._

# Evaluierung und Aenderung von Rulemap-Normen

> Skill aus der Rulemap-Subkette der Legistik-Werkstatt. Schliesst die Normsetzung an die Rulemapping-Methode an (Rulemapping-Group; Prof. Breidenbach; SPRIN-D).

## Eingaben

- Validierte Rulemap im Echtbetrieb
- Berichte aus Vollzug und Gerichtsbarkeit
- Evaluationsklausel der Norm (sofern vorhanden)

## Kern der Methode

Rulemaps werden im Builder per No-Code gepflegt; Aenderungen sind versionierbar und reviewbar. Die Evaluation orientiert sich an Wirkungskontrolle und Erfuellungsaufwand (NKRG-Anforderungen) und stellt fest; ob das Regelungsziel erreicht wird.

## Vorgehen

1. Versionierungsschema festlegen (z.B. semantisch; Datum; Zustaendige)
2. Aenderungsanlass dokumentieren (Vollzug; Gericht; politischer Auftrag)
3. Aenderung im Builder vornehmen; Validierung erneut durchlaufen
4. Evaluation nach Standardrahmen NKRG durchfuehren
5. Bericht an Hausleitung und ggf. Parlament uebermitteln

## Pruefpunkte

Pruefen: ist jede Aenderung rueckverfolgbar? Bleibt der parlamentarische Vorbehalt gewahrt? Wird die Norm trotz Modellpflege materiell richtig gehalten?

## Output

```
Skill:              legw-rmap-evaluierung-und-aenderung
Thema:              Evaluierung und Aenderung von Rulemap-Normen
Ergebnis:           <Artefakt gemaess Kern und Vorgehen>
Naechste Skills:    siehe Description-Verweise
```

## Abgrenzung

Abgrenzung zur klassischen Legistik-Kette: Die legw-rmap-Skills schliessen die Normsetzung an die Rulemap-Methode an. Sie ersetzen nicht die normhierarchische Pruefung, die verfassungs- oder europarechtliche Quercheckung oder die Begruendung; sie liefern die Bruecke von der Norm zur maschinenlesbaren Entscheidungslogik.

## Quellen Stand 06/2026

Quellen Stand 06/2026: Rulemapping-Group (Berlin; gegruendet von Prof. Dr. Stephan Breidenbach; Bundesagentur fuer Sprunginnovationen SPRIN-D als Investor; Equity-Runde April 2025; eingesetzt im BMJ). Methodenbeschreibung unter rulemapping.com und rulemapping.org; Builder kostenlos verfuegbar. Begleitend: Bundesregierung-Modernisierungsagenda Oktober 2025; SPRIND-Projektseite. Plus Bestandsquellen: gesetze-im-internet.de; bundestag.de; bundesregierung.de; bmj.de; normenkontrollrat.bund.de; bundesverfassungsgericht.de; bundesgerichtshof.de; eur-lex.europa.eu.

---

## Skill: `begruendung-allgemein-und-besonders`

_Zweiteilige Begründung zu einem Gesetzesentwurf oder einer Verordnung verfassen. Anwendungsfall Referentenentwurf oder Kabinettsentwurf ist fertig und Begründung muss nach HdR-Schema aufgebaut werden. Allgemeiner Teil A Anlass und Ziel B wesentlicher Inhalt C Alternativen D Erfuellungsaufwand E w..._

# Begründung allgemein und besonders

> Eine gute Begründung erleichtert Auslegung und Vollzug, eine schlechte führt zu Streit.

## Aufbau

### Teil A - Allgemeiner Teil

#### A.I. Zielsetzung und Notwendigkeit der Regelungen

Was soll erreicht werden? Warum ist eine Regelung erforderlich?

#### A.II. Wesentlicher Inhalt des Entwurfs

In zehn bis zwanzig Sätzen den Kern des Entwurfs darstellen.

#### A.III. Alternativen

Welche Alternativen wurden erwogen, warum verworfen?

#### A.IV. Gesetzgebungskompetenz

Verweis auf Art. 70 ff. GG bzw. Landeskompetenz. Erforderlichkeitsklausel Art. 72 Abs. 2 GG, falls einschlaegig.

#### A.V. Vereinbarkeit mit dem Recht der Europaeischen Union und mit völkerrechtlichen Verträgen

Bezug zu Primärrecht (EUV / AEUV / Charta), Sekundärrecht (RL / VO), EuGH-Rechtsprechung. Notifizierungspflicht 2015/1535?

#### A.VI. Gesetzesfolgen

- A.VI.1. Rechts- und Verwaltungsvereinfachung
- A.VI.2. Nachhaltigkeitsaspekte (SDG-Bezug)
- A.VI.3. Haushaltsausgaben ohne Erfüllungsaufwand
- A.VI.4. Erfüllungsaufwand (Bürger / Wirtschaft / Verwaltung)
- A.VI.5. Weitere Kosten
- A.VI.6. Weitere Gesetzesfolgen (gleichstellungspolitisch, demografisch, geschlechtsspezifisch, oekologisch)

#### A.VII. Befristung, Evaluierung

#### A.VIII. Vereinbarkeit mit den Zielen des Klimaschutzgesetzes

### Teil B - Besonderer Teil

Pro Artikel und pro Paragraf:

- Was wird geändert?
- Warum?
- Wie ist die Änderung zu verstehen (Auslegungshinweise)?
- Welche bestehende Rechtsprechung war Hintergrund?
- Welche Auslegungsfragen sind absehbar?

Beispiel - Zu Artikel 1 Nummer 2 (Paragraf 33a HGB - neu):

"Mit Paragraf 33a HGB wird die Pflicht zur Vorhaltung eines elektronischen Pflichtpostfachs eingeführt. Adressaten sind alle im Handelsregister eingetragenen Unternehmen sowie Unternehmen, die nach Artikel 33 DSA als sehr große Online-Plattform (VLOP) oder sehr große Online-Suchmaschine (VLOSE) eingestuft sind. Die Norm konkretisiert die seit der ZPO-Reform 2024 bestehenden Zustellverpflichtungen. ... Die Auswahl der Adressaten über den DSA-Schwellenwert von 45 Millionen Nutzern stellt sicher, dass die Pflicht keine kleinen und mittleren Unternehmen überraschend trifft. ..."

## Stilfragen

- Vergangenheitsform vermeiden, Praesens verwenden
- Keine politischen Bewertungen ("ist dringend notwendig"), nur sachliche Begründung
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine überfluessigen Floskeln

## Prüfliste

- [ ] Teil A.I bis A.VIII vollständig
- [ ] Teil B für jeden geänderten Paragrafen
- [ ] Rechtsprechung zitiert wo passend
- [ ] Erfüllungsaufwand mit Zahlen
- [ ] EU-Bezug und Notifizierung adressiert

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§ 39 VwVfG (Begruendungspflicht Verwaltungsakt) — § 41 VwVfG (Heilung von Begruendungsmaengeln) — § 76 GGO (Begruendung Referentenentwurf) — §§ 1-4 UVPG (Umwelt-Begruendungspflichten) — § 35 BauGB (Begruendung Abwaegungsergebnis Bauleitplanung)

## Ausgabe

Markdown-Datei "Begruendung.md".

<!-- BEGIN ausformulierungspflicht (autogen) -->
> Ausformulierungspflicht. Das Endprodukt wird in vollständigen, ausformulierten Sätzen geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Anschluss

`synopse-erstellen`.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

