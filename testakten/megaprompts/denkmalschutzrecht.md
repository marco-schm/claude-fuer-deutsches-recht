# Megaprompt: denkmalschutzrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 31 Skills des Plugins `denkmalschutzrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstiegsskill für das Denkmalschutzrecht-Plugin. Sortiert das Mandat, klärt Belegenheit des Objekts und damit das anwen…
2. **kaltstart-triage** — Schnelltriage für ein neues denkmalschutzrechtliches Mandat. Erhebt in einer Sitzung Objektdaten, Schutzstatus, Mandante…
3. **erstgespraech-mandatsannahme** — Strukturiert das erste Mandantengespräch im Denkmalschutzrecht. Erhebt die Mandatsgrundlage (Vollmacht, Konfliktcheck, H…
4. **unesco-welterbe-und-icomos** — Welterbestätten in Deutschland: völkerrechtlicher Rahmen der UNESCO-Welterbekonvention von 1972, ICOMOS-Begutachtung, Pu…
5. **denkmalschutz-sachsen-anhalt-dschg-lsa** — Denkmalschutzrecht Sachsen-Anhalt nach dem Denkmalschutzgesetz des Landes Sachsen-Anhalt. Skill bündelt zuständige Behör…
6. **verfahrensgrundsaetze-vwvfg** — Verwaltungsverfahrensrecht im Denkmalschutz: Anhörung nach Paragraf 28 VwVfG, schriftlicher Verwaltungsakt mit Begründun…
7. **art-73-gg-laenderzustaendigkeit** — Bundesstaatlicher Rahmen des Denkmalschutzes: Denkmalschutz ist keine konkurrierende Bundesmaterie nach Art. 73 oder 74 …
8. **denkmalschutz-rheinland-pfalz-dschpflg** — Denkmalschutzrecht Rheinland-Pfalz nach dem Denkmalschutz- und -pflegegesetz Rheinland-Pfalz. Skill bündelt zuständige B…
9. **denkmalschutz-niedersachsen-ndschg** — Denkmalschutzrecht Niedersachsen nach dem Niedersächsischen Denkmalschutzgesetz. Skill bündelt zuständige Behörden (Mini…
10. **denkmalschutz-mecklenburg-vorpommern-dschg-m-v** — Denkmalschutzrecht Mecklenburg-Vorpommern nach dem Denkmalschutzgesetz Mecklenburg-Vorpommern. Skill bündelt zuständige …
11. **quellen-livecheck** — Quellenhygiene-Skill für das Denkmalschutzrecht-Plugin. Liefert die kuratierte Suchadressen-Liste für die sechzehn Lande…
12. **foerderung-und-steuerliche-abschreibung** — Förderung von Denkmalsanierung: direkte Zuschüsse der Länder und Kommunen, Bundesförderung über die Beauftragte der Bund…
13. **art-14-gg-eigentum-und-denkmalschutz** — Art. 14 GG im Denkmalschutz: die Eintragung in die Denkmalliste und die daraus folgenden Erhaltungs-, Duldungs- und Verä…
14. **grundbegriffe-und-rechtsquellen** — Grundbegriffe des deutschen Denkmalschutzrechts: Baudenkmal, Bodendenkmal, bewegliches Denkmal, Ensemble, Welterbe, Schu…
15. **denkmalschutz-schleswig-holstein-dschg-sh** — Denkmalschutzrecht Schleswig-Holstein nach dem Denkmalschutzgesetz Schleswig-Holstein. Skill bündelt zuständige Behörden…

---

## Skill: `einstieg-routing`

_Einstiegsskill für das Denkmalschutzrecht-Plugin. Sortiert das Mandat, klärt Belegenheit des Objekts und damit das anwendbare Landesgesetz, ermittelt Rolle (Eigentümer, Erwerber, Behörde, Nachbar, Förderantragsteller), Fristen und gewünschtes Arbeitsprodukt. Routet anschließend in die passenden Querschnitts- und Landesskills._

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

---

## Skill: `kaltstart-triage`

_Schnelltriage für ein neues denkmalschutzrechtliches Mandat. Erhebt in einer Sitzung Objektdaten, Schutzstatus, Mandantenrolle, konkrete Maßnahme, drohende Fristen und Eilrisiken. Liefert eine erste Risikoampel und benennt die unverzichtbaren Sofortmaßnahmen (Akteneinsicht, Bauanzeige aussetzen, vorläufige Sicherung)._

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

---

## Skill: `erstgespraech-mandatsannahme`

_Strukturiert das erste Mandantengespräch im Denkmalschutzrecht. Erhebt die Mandatsgrundlage (Vollmacht, Konfliktcheck, Honorarvereinbarung), das Objekt mit Belegenheit und Schutzstatus, die anstehende Maßnahme und das Mandatsziel. Liefert einen Mandatsannahmevermerk in vollständiger Sprache._

# Erstgespräch — Denkmalschutzrechtliche Mandatsannahme

## Zweck und Anwendungsfall

Das Erstgespräch im Denkmalschutzrecht muss zugleich die Mandatsgrundlage prüfen (Konflikte, Vollmacht, RVG- oder Stundenhonorar) und genug Tatsachen erheben, dass die Kanzlei das anwendbare Landesgesetz und die zuständigen Behörden benennen kann. Dieser Skill führt durch das Gespräch und liefert einen Mandatsannahmevermerk.

## Eingaben

- **Identität der Mandantin** und gegebenenfalls Bevollmächtigung weiterer Gesellschafterinnen oder Miteigentümerinnen.
- **Objektdaten** mit Belegenheit, Eigentumsverhältnissen, Erwerbsdatum, Voreigentum.
- **Schutzstatus** mit Datum der Eintragung, Aktenzeichen der Eintragungsverfügung, Bezugnahme auf die Denkmalliste oder das Inventar.
- **Konkretes Mandatsziel** (Erlaubnis erreichen, Bescheid abwehren, Förderung beantragen, Verkauf vorbereiten, Streit mit Behörde lösen).
- **Konfliktcheck:** keine bestehende Vertretung der Behörde oder eines gegnerischen Eigentümers durch die Kanzlei.
- **Vereinbarung über Honorar und Auslagen.**

## Ablauf / Checkliste

1. Identitätsprüfung und Geldwäsche-Prüfung soweit der Mandatswert nach Paragraf 2 Abs. 1 GwG die Schwelle erreicht.
2. Konfliktcheck nach Paragraf 43a Abs. 4 BRAO durchführen und dokumentieren.
3. Sachverhalt strukturiert aufnehmen; in Zweifelsfällen Belegenheit und Schutzstatus durch eine Voranfrage bei der zuständigen Denkmalbehörde verifizieren.
4. Mandatsziel ausdrücklich festhalten; bei Ermessensentscheidungen das gewünschte Ermessensergebnis und das hilfsweise gewünschte Mindestmaß formulieren.
5. Vollmacht in der für Verwaltungsverfahren passenden Fassung einholen.
6. Honorarvereinbarung schriftlich abschließen (RVG-Maßstab, Stundenhonorar oder Pauschale).
7. Mandatsannahmevermerk anlegen.

## Quellenpflicht

Verweise auf BRAO, RVG und das jeweilige Landesgesetz immer mit Paragrafen, ohne erfundene Randnummern. Siehe references/zitierweise.md.

## Ausgabeformat

Mandatsannahmevermerk in vollständiger Sprache mit den Blöcken Mandantenstammdaten, Objekt, Schutzstatus, Mandatsziel, Konfliktprüfung, Vollmacht, Honorarvereinbarung, nächste Schritte. Platzhalter sind als `[Mandantin Name]`, `[Objektanschrift]` und `[Aktenzeichen Denkmalliste]` zu kennzeichnen.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Beispiel

Mandantin Frau Dr. Helena Volkenrath erbt 2026 ein eingetragenes Bürgerhaus von 1841 in Quedlinburg, Welterbe-Pufferzone, und möchte einen Teil als Ferienwohnung herrichten. Mandatsziel ist die Erlaubnis nach DSchG-LSA für den Innenausbau und die Klärung steuerlicher Förderung nach Paragraf 7i EStG.

---

## Skill: `unesco-welterbe-und-icomos`

_Welterbestätten in Deutschland: völkerrechtlicher Rahmen der UNESCO-Welterbekonvention von 1972, ICOMOS-Begutachtung, Pufferzonen, Managementpläne und die mittelbare Wirkung auf das deutsche Landesrecht. Skill ordnet, was die Welterbe-Eigenschaft für ein konkretes Mandat rechtlich tatsächlich bedeutet (Hinweisfunktion, Bauplanung, behördliche Begründungspflicht) und was sie nicht bedeutet (kein eigenständiger Schutzstatus jenseits des Landesgesetzes)._

# UNESCO-Welterbe und ICOMOS

## Zweck und Anwendungsfall

Welterbestätten verlangen in der Mandatspraxis besondere Aufmerksamkeit, weil die Begründungslast der Behörde höher ist, ICOMOS-Empfehlungen die Bauleitplanung mitprägen und Reputationsrisiken bei Beschädigungen erheblich sind. Der Skill ordnet den völkerrechtlichen Rahmen ein und zeigt, wie er ins deutsche Landesrecht hineinwirkt.

## Rechtlicher Rahmen

- **UNESCO-Welterbekonvention vom 16.11.1972**, ratifiziert durch Deutschland 1976 (BGBl. 1977 II Seite 213). Begründet keinen unmittelbaren Schutzanspruch im innerstaatlichen Recht, verpflichtet aber den Vertragsstaat zur Erhaltung.
- **ICOMOS** als beratendes Gremium der UNESCO begutachtet vor Listenaufnahme und überwacht den Erhaltungszustand. Reactive Monitoring Reports und State of Conservation Reports sind veröffentlicht und im Verfahren verwertbar.
- **Pufferzonen** sind in den Operational Guidelines for the Implementation of the World Heritage Convention vorgesehen; in Deutschland landesrechtlich nicht zwingend, aber regelmäßig als Erhaltungssatzung nach Paragraf 172 BauGB oder als Sichtachsenschutz im Bebauungsplan abgebildet.
- **Wirkung im Landesrecht:** Welterbe-Eigenschaft verschärft die behördliche Begründungspflicht und kann eine atypische Ermessensbindung bewirken; sie ersetzt aber nicht die Eintragung nach dem jeweiligen Landesgesetz.

## Welterbestätten in Deutschland — Beispielfälle (vor Verwendung verifizieren)

Aachener Dom, Würzburger Residenz, Speyerer Dom, Hansestadt Lübeck, Klosterinsel Reichenau, Oberes Mittelrheintal, Quedlinburger Altstadt, Bauhausstätten in Weimar und Dessau, Wattenmeer, Hamburger Speicherstadt und Kontorhausviertel, Naumburger Dom, jüdisch-mittelalterliches Erbe in Speyer, Worms und Mainz (SchUM) und weitere. Liste vor Mandatsverwendung über die UNESCO-Welterbe-Datenbank prüfen.

## Ablauf / Checkliste

1. Klären, ob das Objekt selbst Welterbestätte ist oder in einer ausgewiesenen Pufferzone liegt.
2. Den aktuellen Managementplan und den letzten ICOMOS-Bericht beschaffen (UNESCO-Welterbezentrum, Landesdenkmalbehörde).
3. Bei Erlaubnisverfahren die Welterbe-Eigenschaft in die Begründung einarbeiten; bei behördlicher Versagung prüfen, ob die Welterbe-Argumentation der Behörde tragfähig ist oder ob sie sich auf nicht verbindliche Empfehlungen stützt.
4. Bei drohender De-Listing-Diskussion ICOMOS-Empfehlungen und die State of Conservation-Berichte als Begründungsstoff verwenden.

## Quellenpflicht

Konventionstext aus dem Bundesgesetzblatt zitieren. ICOMOS-Berichte aus dem UNESCO-Welterbezentrum (whc.unesco.org). Operational Guidelines in der aktuellen Fassung verifizieren; siehe references/zitierweise.md.

## Ausgabeformat

Bewertung in vollständigen Sätzen, die den Welterbestatus konkret in das deutsche Verwaltungsverfahren einordnet — keine pauschale Berufung auf den Status ohne landesrechtliche Anbindung.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `denkmalschutz-sachsen-anhalt-dschg-lsa`

_Denkmalschutzrecht Sachsen-Anhalt nach dem Denkmalschutzgesetz des Landes Sachsen-Anhalt. Skill bündelt zuständige Behörden (Ministerium für Wissenschaft, Energie, Klimaschutz und Umwelt; Landesamt für Denkmalpflege und Archäologie Sachsen-Anhalt in Halle; Untere Denkmalschutzbehörden bei den Landkreisen) und die zahlreichen Welterbestätten (Quedlinburg, Wittenberg, Dessauer Gartenreich, Bauhaus, Naumburger Dom, Himmelsscheibe von Nebra)._

# Denkmalschutz Sachsen-Anhalt (DSchG-LSA)

## Zweck und Anwendungsfall

Sachsen-Anhalt ist eines der welterbedichtesten Bundesländer mit Quedlinburg, Wittenberg, Naumburger Dom, Dessauer Gartenreich und Bauhausstätten. Das DSchG-LSA arbeitet mit nachrichtlicher Eintragung; die Verfahrenspraxis ist eng mit der ICOMOS-Begutachtung verzahnt.

## Anwendbares Gesetz

- **Gesetzesbezeichnung**: Denkmalschutzgesetz des Landes Sachsen-Anhalt
- **Abkürzung**: DSchG-LSA
- **Zitiergrundlage**: amtliche Landesgesetz-Datenbank landesrecht.sachsen-anhalt.de

## Zuständige Behörden

- **Oberste Denkmalschutzbehörde**: Ministerium für Wissenschaft, Energie, Klimaschutz und Umwelt des Landes Sachsen-Anhalt
- **Obere Denkmalschutzbehörde**: Landesverwaltungsamt Sachsen-Anhalt in Halle
- **Untere Denkmalschutzbehörde**: Landkreise und kreisfreie Städte (Halle, Magdeburg, Dessau-Roßlau)
- **Fachbehörde**: Landesamt für Denkmalpflege und Archäologie Sachsen-Anhalt in Halle

## Verfahrensbesonderheiten Sachsen-Anhalt

- Welterbestätten: Quedlinburg, Luthergedenkstätten Eisleben und Wittenberg, Naumburger Dom, Dessauer Gartenreich, Bauhausstätten in Dessau.
- Frühmittelalterliches Kulturerbe (Himmelsscheibe von Nebra, Pretziener Wehr).
- Industriekultur Magdeburg, Halle.
- Hoher Bestand an Bodendenkmälern aus dem Salzwirken-Raum.

## Eintragungssystem

- **Systematik**: nachrichtliches Eintragungssystem

## Ablauf / Checkliste

1. Klären, ob das Objekt ein Bau-, Boden- oder bewegliches Denkmal ist.
2. Eintragungsstatus über die Denkmalliste des Landes feststellen — über landesrecht.sachsen-anhalt.de.
3. Zuständige untere Denkmalschutzbehörde am Belegenheitsort kontaktieren.
4. Bei Maßnahmen das Erlaubnisverfahren nach DSchG-LSA starten; bei zugleich bauordnungsrechtlich relevanten Maßnahmen die Kombination mit der Baugenehmigung berücksichtigen.
5. Konkrete Paragrafen vor Ausgabe live in landesrecht.sachsen-anhalt.de verifizieren.

## Quellenpflicht

Sämtliche Paragrafenzitate werden vor Mandatsverwendung in landesrecht.sachsen-anhalt.de live geprüft. Verwaltungsgerichts- und Oberverwaltungsgerichtsrechtsprechung des Landes nur mit Aktenzeichen, Datum und frei zugänglicher Fundstelle benennen.

## Ausgabeformat

Landesrechtliche Stellungnahme in vollständigen Sätzen mit konkreten Paragrafenverweisen aus dem Landesgesetz und den zuständigen Behörden.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Beispiel

Eigentümerin eines Bürgerhauses in Quedlinburg-Altstadt (UNESCO-Welterbe) plant Umnutzung als Ferienwohnung. Zuständig ist der Landkreis Harz als untere Denkmalschutzbehörde mit fachlicher Stellungnahme des Landesamts für Denkmalpflege und Archäologie und ICOMOS-Berücksichtigung.

---

## Skill: `verfahrensgrundsaetze-vwvfg`

_Verwaltungsverfahrensrecht im Denkmalschutz: Anhörung nach Paragraf 28 VwVfG, schriftlicher Verwaltungsakt mit Begründung und Rechtsbehelfsbelehrung nach Paragrafen 35 37 und 39 VwVfG, Bekanntgabe nach Paragraf 41 VwVfG, Rücknahme rechtswidriger und Widerruf rechtmäßiger Verwaltungsakte nach Paragrafen 48/49 VwVfG. Skill zeigt, wie die Landes-VwVfG inhaltsgleich greifen und welche Verfahrensfehler im Denkmalrecht typisch sind._

# Verfahrensgrundsätze nach VwVfG

Im Denkmalschutzverfahren ist die Verwaltungsverfahrensregelung des jeweiligen Landes (Landes-VwVfG) maßgeblich; sie ist inhaltsgleich mit dem Bundes-VwVfG. Folgende Verfahrensregeln werden im Denkmalrecht regelmäßig relevant:

- **Paragraf 28 VwVfG — Anhörung**: vor jedem belastenden Verwaltungsakt zwingend; Heilung im Widerspruchsverfahren grundsätzlich möglich, aber bei wesentlichen Tatsachen nicht.
- **Paragraf 35 VwVfG — Verwaltungsakt**: Eintragung in die Denkmalliste, Erlaubniserteilung oder -versagung, Untersagung, Beseitigungsanordnung — alle sind Verwaltungsakte.
- **Paragraf 37 VwVfG — Bestimmtheit**: Tenor der Anordnung muss die konkrete Maßnahme exakt benennen; pauschale Untersagungen sind anfechtbar.
- **Paragraf 39 VwVfG — Begründung**: Ermessensentscheidungen verlangen eine ausführliche, fallbezogene Begründung; die bloße Wiederholung des Gesetzeswortlauts genügt nicht.
- **Paragraf 41 VwVfG — Bekanntgabe**: Beginn der Widerspruchsfrist; bei elektronischer Bekanntgabe Zustellungsregeln des jeweiligen Landeszustellgesetzes.
- **Paragrafen 48, 49 VwVfG — Rücknahme und Widerruf**: gerade bei Eintragungen, die ohne ausreichende Anhörung ergangen sind, kommt eine Rücknahme nach Paragraf 48 VwVfG in Betracht.

## Typische Verfahrensfehler im Denkmalrecht

- Eintragung ohne vorhergehende Anhörung der Eigentümerin.
- Erlaubnisversagung ohne fallbezogene Ermessensbegründung.
- Beseitigungsanordnung ohne konkrete Beschreibung der zu beseitigenden Maßnahme.
- Untersagung ohne aufschiebende Wirkung trotz fehlender öffentlicher Vollzugsinteressen.

## Ablauf / Checkliste

1. Bescheid auf Anhörung, Begründung, Bestimmtheit und Rechtsbehelfsbelehrung prüfen.
2. Verfahrensfehler dokumentieren und in den Widerspruch einarbeiten.
3. Bei groben Verfahrensfehlern Aussetzung der Vollziehung nach Paragraf 80 Abs. 5 VwGO erwägen.

## Quellenpflicht

Normverweise und Rechtsprechungsanker werden vor Mandatsverwendung live in den amtlichen Datenbanken verifiziert; siehe references/zitierweise.md.

## Ausgabeformat

Strukturierte Stellungnahme in vollständigen Sätzen mit konkreten Norm-Ankern und klarem Bezug zum Mandatsbegehren.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `art-73-gg-laenderzustaendigkeit`

_Bundesstaatlicher Rahmen des Denkmalschutzes: Denkmalschutz ist keine konkurrierende Bundesmaterie nach Art. 73 oder 74 GG, sondern nach Art. 70 GG ausschließlich Sache der Länder. Skill ordnet, welche Aspekte trotzdem bundesrechtlich überlagert sind (Eigentumsgarantie nach Art. 14 GG, Verwaltungsverfahrensrecht, Strafrecht und Ordnungswidrigkeitenrecht, steuerliche Förderung nach EStG, Grundbuch- und Bauplanungsrecht)._

# Art. 70 GG, Art. 73 GG — Länderzuständigkeit im Denkmalschutz

## Zweck und Anwendungsfall

Der Föderalismus erklärt, warum es sechzehn Landesgesetze gibt und warum es kein Bundesdenkmalschutzgesetz gibt. Dieser Skill ordnet die Zuständigkeitslage und zeigt, welche bundesrechtlichen Überlagerungen trotzdem mitzudenken sind.

## Rechtlicher Rahmen

- **Art. 70 GG** Grundregel: Wo der Bund keine Zuständigkeit hat, regeln die Länder.
- **Art. 73 GG** abschließende Bundesaufgaben (Verteidigung, auswärtige Beziehungen, Bundesgrenzschutz, …): Denkmalschutz nicht dabei.
- **Art. 74 GG** konkurrierende Gesetzgebung: Denkmalschutz nicht dabei. Bauplanungsrecht ist in Art. 74 Abs. 1 Nr. 18 GG geregelt; Denkmalschutz daneben.
- **Art. 14 GG** und **Art. 3 GG** wirken in jedes Landesgesetz hinein.

## Bundesrechtliche Überlagerungen, die im Mandat relevant werden

- **Eigentumsgarantie:** Inhalts- und Schrankenbestimmung muss verhältnismäßig sein; bei unzumutbarer Belastung Ausgleichspflicht.
- **Verwaltungsverfahrensrecht:** Landes-VwVfG ist regelmäßig inhaltsgleich mit Bundes-VwVfG; Paragrafen 28 (Anhörung), 35-39 (Verwaltungsakt), 48-50 (Rücknahme, Widerruf) wirken in jedem Verfahren.
- **Strafrecht und Ordnungswidrigkeitenrecht:** Bußgeldtatbestände stehen in jedem Landesgesetz; bei vorsätzlicher Beschädigung kann Paragraf 304 StGB (Sachbeschädigung) hinzutreten.
- **Steuerrecht:** Paragrafen 7i, 10f, 10g, 11b EStG bauen unmittelbar auf der Bescheinigung der Denkmalbehörde nach Landesrecht auf.
- **Bauplanungsrecht:** Paragraf 1 Abs. 6 Nr. 5 BauGB nimmt Denkmalpflege ausdrücklich in die Abwägung auf; Paragraf 172 BauGB regelt die Erhaltungssatzung.
- **Grundbuchrecht:** In manchen Ländern wird der Denkmalstatus im Grundbuch (Abteilung II) oder in einer Liste vermerkt.

## Ablauf / Checkliste

1. Beim Mandat zuerst Landesgesetz feststellen.
2. Prüfen, ob bundesrechtliche Überlagerung greift (Eigentumsfrage, Verfahrensfehler, Steuerrecht, Bauplanungsschnittstelle).
3. Bei Konflikt zwischen Landesgesetz und bundesrechtlicher Vorgabe an die verfassungs- oder unionsrechtskonforme Auslegung denken.

## Quellenpflicht

Norm-Anker aus den amtlichen Datenbanken; GG aus gesetze-im-internet.de; Landesgesetz aus der Landesgesetz-Datenbank. Siehe references/zitierweise.md.

## Ausgabeformat

Knappe Zuständigkeitsanalyse in vollständigen Sätzen, die das anwendbare Landesgesetz benennt und die bundesrechtlichen Überlagerungen aufführt.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `denkmalschutz-rheinland-pfalz-dschpflg`

_Denkmalschutzrecht Rheinland-Pfalz nach dem Denkmalschutz- und -pflegegesetz Rheinland-Pfalz. Skill bündelt zuständige Behörden (Ministerium des Innern und für Sport; Generaldirektion Kulturelles Erbe Rheinland-Pfalz; Untere Denkmalbehörden bei den Landkreisen und kreisfreien Städten) und die Bedeutung des Rheinland-Pfalz-Beschlusses BVerfGE 100 Seite 226 als verfassungsrechtliche Leitentscheidung zum Denkmalschutz._

# Denkmalschutz Rheinland-Pfalz (DSchPflG)

## Zweck und Anwendungsfall

Rheinland-Pfalz ist verfassungsrechtlich bedeutsam: Aus dem DSchPflG erging die Vorlage zum Rheinland-Pfalz-Beschluss BVerfGE 100 Seite 226 (vom 02.03.1999), der die Grundlinie zur Inhaltsbestimmung und Zumutbarkeitsgrenze zog. Welterbestätten Mittelrheintal, Speyerer Dom, Trier-Römische Bauten prägen die Verfahrenspraxis.

## Anwendbares Gesetz

- **Gesetzesbezeichnung**: Denkmalschutz- und -pflegegesetz Rheinland-Pfalz
- **Abkürzung**: DSchPflG
- **Zitiergrundlage**: amtliche Landesgesetz-Datenbank landesrecht.rlp.de

## Zuständige Behörden

- **Oberste Denkmalschutzbehörde**: Ministerium des Innern und für Sport Rheinland-Pfalz
- **Obere Denkmalschutzbehörde**: Generaldirektion Kulturelles Erbe Rheinland-Pfalz (zugleich Fachbehörde) in Mainz
- **Untere Denkmalschutzbehörde**: Landkreise und kreisfreie Städte
- **Fachbehörde**: Generaldirektion Kulturelles Erbe Rheinland-Pfalz (mit Direktion Landesdenkmalpflege)

## Verfahrensbesonderheiten Rheinland-Pfalz

- Welterbestätten: Oberes Mittelrheintal, Dom zu Speyer, römische Baudenkmäler und Liebfrauenkirche in Trier, SchUM-Stätten (Worms, Speyer, Mainz).
- Verfassungsrechtliche Leitentscheidung BVerfGE 100 Seite 226 zum Ausgleich unzumutbarer Inhaltsbestimmung.
- Dichte Weinbau-Kulturlandschaft als Querschnittsthema.
- Bodendenkmäler im römischen Korridor (Trier, Mainz, Speyer).

## Eintragungssystem

- **Systematik**: nachrichtliche Eintragung; Denkmaleigenschaft kraft Gesetzes

## Ablauf / Checkliste

1. Klären, ob das Objekt ein Bau-, Boden- oder bewegliches Denkmal ist.
2. Eintragungsstatus über die Denkmalliste des Landes feststellen — über landesrecht.rlp.de.
3. Zuständige untere Denkmalschutzbehörde am Belegenheitsort kontaktieren.
4. Bei Maßnahmen das Erlaubnisverfahren nach DSchPflG starten; bei zugleich bauordnungsrechtlich relevanten Maßnahmen die Kombination mit der Baugenehmigung berücksichtigen.
5. Konkrete Paragrafen vor Ausgabe live in landesrecht.rlp.de verifizieren.

## Quellenpflicht

Sämtliche Paragrafenzitate werden vor Mandatsverwendung in landesrecht.rlp.de live geprüft. Verwaltungsgerichts- und Oberverwaltungsgerichtsrechtsprechung des Landes nur mit Aktenzeichen, Datum und frei zugänglicher Fundstelle benennen.

## Ausgabeformat

Landesrechtliche Stellungnahme in vollständigen Sätzen mit konkreten Paragrafenverweisen aus dem Landesgesetz und den zuständigen Behörden.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Beispiel

Eigentümerin eines Winzeranwesens im Mittelrheintal-Welterbe plant Erweiterung der Kelterei. Zuständig ist der Rhein-Hunsrück-Kreis als untere Denkmalbehörde mit fachlicher Stellungnahme der Generaldirektion Kulturelles Erbe; ICOMOS-Belange in der Pufferzone berücksichtigen.

---

## Skill: `denkmalschutz-niedersachsen-ndschg`

_Denkmalschutzrecht Niedersachsen nach dem Niedersächsischen Denkmalschutzgesetz. Skill bündelt zuständige Behörden (Ministerium für Wissenschaft und Kultur; Niedersächsisches Landesamt für Denkmalpflege in Hannover; Untere Denkmalschutzbehörden bei den Landkreisen und kreisfreien Städten) und die konstitutive Eintragungssystematik mit besonderem Augenmerk auf das Welterbe Goslar, Hildesheim und das Wattenmeer._

# Denkmalschutz Niedersachsen (NDSchG)

## Zweck und Anwendungsfall

Niedersachsen arbeitet im Grundsatz mit konstitutiver Eintragung; das NDSchG kennt unterschiedliche Schutzkategorien. Die Welterbestätten Goslar (Altstadt und Erzbergwerk Rammelsberg), Hildesheim (Mariendom und Michaeliskirche) und das Wattenmeer prägen die Verfahrenspraxis.

## Anwendbares Gesetz

- **Gesetzesbezeichnung**: Niedersächsisches Denkmalschutzgesetz
- **Abkürzung**: NDSchG
- **Zitiergrundlage**: amtliche Landesgesetz-Datenbank voris.wolterskluwer-online.de / nds-voris.de

## Zuständige Behörden

- **Oberste Denkmalschutzbehörde**: Niedersächsisches Ministerium für Wissenschaft und Kultur
- **Obere Denkmalschutzbehörde**: Niedersächsisches Landesamt für Denkmalpflege (zugleich Fachbehörde) in Hannover
- **Untere Denkmalschutzbehörde**: Landkreise und kreisfreie Städte (Braunschweig, Hannover, Osnabrück, Wolfsburg u. a.)
- **Fachbehörde**: Niedersächsisches Landesamt für Denkmalpflege

## Verfahrensbesonderheiten Niedersachsen

- Konstitutives Eintragungssystem mit klarer Anhörungsregel.
- Welterbestätten Goslar, Hildesheim, Wattenmeer, Fagus-Werk Alfeld.
- Bodendenkmäler in den Küstenregionen mit besonderer Schutzpflicht.
- Energetische Sanierung von Fachwerkbauten ist landesweit besonders konfliktträchtig.

## Eintragungssystem

- **Systematik**: konstitutive Eintragung in das Denkmalverzeichnis

## Ablauf / Checkliste

1. Klären, ob das Objekt ein Bau-, Boden- oder bewegliches Denkmal ist.
2. Eintragungsstatus über die Denkmalliste des Landes feststellen — über voris.wolterskluwer-online.de bzw. nds-voris.de.
3. Zuständige untere Denkmalschutzbehörde am Belegenheitsort kontaktieren.
4. Bei Maßnahmen das Erlaubnisverfahren nach NDSchG starten; bei zugleich bauordnungsrechtlich relevanten Maßnahmen die Kombination mit der Baugenehmigung berücksichtigen.
5. Konkrete Paragrafen vor Ausgabe live in voris.wolterskluwer-online.de / nds-voris.de verifizieren.

## Quellenpflicht

Sämtliche Paragrafenzitate werden vor Mandatsverwendung in voris.wolterskluwer-online.de / nds-voris.de live geprüft. Verwaltungsgerichts- und Oberverwaltungsgerichtsrechtsprechung des Landes nur mit Aktenzeichen, Datum und frei zugänglicher Fundstelle benennen.

## Ausgabeformat

Landesrechtliche Stellungnahme in vollständigen Sätzen mit konkreten Paragrafenverweisen aus dem Landesgesetz und den zuständigen Behörden.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Beispiel

Erwerber eines Fachwerkhauses in der Hildesheimer Altstadt, eingetragenes Baudenkmal nahe Mariendom, plant Innendämmung und neue Heizungsanlage. Zuständig ist die Stadt Hildesheim mit fachlicher Stellungnahme des Niedersächsischen Landesamts für Denkmalpflege.

---

## Skill: `denkmalschutz-mecklenburg-vorpommern-dschg-m-v`

_Denkmalschutzrecht Mecklenburg-Vorpommern nach dem Denkmalschutzgesetz Mecklenburg-Vorpommern. Skill bündelt zuständige Behörden (Ministerium für Wissenschaft, Kultur, Bundes- und Europaangelegenheiten; Landesamt für Kultur und Denkmalpflege in Schwerin; Untere Denkmalschutzbehörden bei den Landkreisen) und das nachrichtliche Eintragungssystem mit besonderem Augenmerk auf maritime und Backsteindenkmale._

# Denkmalschutz Mecklenburg-Vorpommern (DSchG M-V)

## Zweck und Anwendungsfall

Mecklenburg-Vorpommern verfügt über einen besonders hohen Bestand an Backsteingotik, Gutshäusern und Bäderarchitektur. Das DSchG M-V arbeitet mit nachrichtlicher Eintragung. Welterbestätten der Altstädte Stralsund und Wismar prägen die Verfahrenspraxis.

## Anwendbares Gesetz

- **Gesetzesbezeichnung**: Denkmalschutzgesetz Mecklenburg-Vorpommern
- **Abkürzung**: DSchG M-V
- **Zitiergrundlage**: amtliche Landesgesetz-Datenbank landesrecht-mv.de

## Zuständige Behörden

- **Oberste Denkmalschutzbehörde**: Ministerium für Wissenschaft, Kultur, Bundes- und Europaangelegenheiten Mecklenburg-Vorpommern
- **Obere Denkmalschutzbehörde**: Landesamt für Kultur und Denkmalpflege Mecklenburg-Vorpommern in Schwerin (zugleich Fachbehörde)
- **Untere Denkmalschutzbehörde**: Landkreise und kreisfreie Städte (Schwerin, Rostock)
- **Fachbehörde**: Landesamt für Kultur und Denkmalpflege Mecklenburg-Vorpommern, Abteilung Landesdenkmalpflege

## Verfahrensbesonderheiten Mecklenburg-Vorpommern

- Welterbestätten: Altstädte Stralsund und Wismar.
- Hoher Bestand an Gutsanlagen mit oft schwieriger Eigentumslage nach Nachwendeprivatisierung.
- Bäderarchitektur in Heringsdorf, Bansin und Binz unter Ensembleschutz.
- Bodendenkmäler im slawisch-baltischen Raum (Festland und Inseln).

## Eintragungssystem

- **Systematik**: nachrichtliches Eintragungssystem; Denkmaleigenschaft kraft Gesetzes

## Ablauf / Checkliste

1. Klären, ob das Objekt ein Bau-, Boden- oder bewegliches Denkmal ist.
2. Eintragungsstatus über die Denkmalliste des Landes feststellen — über landesrecht-mv.de.
3. Zuständige untere Denkmalschutzbehörde am Belegenheitsort kontaktieren.
4. Bei Maßnahmen das Erlaubnisverfahren nach DSchG M-V starten; bei zugleich bauordnungsrechtlich relevanten Maßnahmen die Kombination mit der Baugenehmigung berücksichtigen.
5. Konkrete Paragrafen vor Ausgabe live in landesrecht-mv.de verifizieren.

## Quellenpflicht

Sämtliche Paragrafenzitate werden vor Mandatsverwendung in landesrecht-mv.de live geprüft. Verwaltungsgerichts- und Oberverwaltungsgerichtsrechtsprechung des Landes nur mit Aktenzeichen, Datum und frei zugänglicher Fundstelle benennen.

## Ausgabeformat

Landesrechtliche Stellungnahme in vollständigen Sätzen mit konkreten Paragrafenverweisen aus dem Landesgesetz und den zuständigen Behörden.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Beispiel

Investorin erwirbt das Gutshaus Schorssow, eingetragenes Baudenkmal, und plant Umnutzung als Hotel. Zuständig ist der Landkreis Rostock als untere Denkmalschutzbehörde mit fachlicher Stellungnahme des Landesamts für Kultur und Denkmalpflege.

---

## Skill: `quellen-livecheck`

_Quellenhygiene-Skill für das Denkmalschutzrecht-Plugin. Liefert die kuratierte Suchadressen-Liste für die sechzehn Landesgesetzes-Datenbanken, das Bundesrecht (gesetze-im-internet.de), die Verwaltungsgerichtsbarkeit (BVerwG, OVG-Pakete) und die Welterbe-Quellen (UNESCO, ICOMOS). Verhindert Halluzinationen, indem Paragrafen, Aktenzeichen und Fundstellen vor Verwendung zwingend live verifiziert werden._

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

---

## Skill: `foerderung-und-steuerliche-abschreibung`

_Förderung von Denkmalsanierung: direkte Zuschüsse der Länder und Kommunen, Bundesförderung über die Beauftragte der Bundesregierung für Kultur und Medien (BKM) und die Deutsche Stiftung Denkmalschutz, vor allem aber die steuerliche Förderung nach Paragrafen 7i und 11b EStG (Vermietung) sowie Paragraf 10f EStG (selbstgenutzt). Skill ordnet das Zusammenspiel von Denkmalbescheinigung und Steuerrecht._

# Förderung und steuerliche Abschreibung

## Steuerliche Förderung — Kern

- **Paragraf 7i EStG (Vermietung)**: erhöhte Absetzungen für Herstellungskosten an Baudenkmälern bis zu 9 Prozent in den ersten acht Jahren und 7 Prozent in den folgenden vier Jahren; voraussetzt, dass die Aufwendungen zur Erhaltung des Denkmals oder seiner sinnvollen Nutzung erforderlich sind und die Denkmalbehörde dies bescheinigt.
- **Paragraf 10f EStG (selbstgenutzt)**: Sonderausgabenabzug für vergleichbare Aufwendungen am selbstgenutzten Baudenkmal, 9 Prozent über zehn Jahre.
- **Paragraf 11b EStG**: bestimmte Erhaltungsaufwendungen können auf zwei bis fünf Jahre verteilt werden.
- **Paragraf 10g EStG**: schutzwürdige Kulturgüter, die nicht selbstgenutzt und nicht vermietet sind.

## Denkmalbescheinigung — zentrales Dokument

Voraussetzung jeder steuerlichen Förderung nach Paragrafen 7i, 10f, 11b EStG ist die **Bescheinigung der Landesdenkmalbehörde**, dass es sich um ein Baudenkmal im Sinne des Landesgesetzes handelt und die Aufwendungen denkmalrechtlich erforderlich waren. Diese Bescheinigung ist Grundlagenbescheid im Sinne des Paragrafen 175 Abs. 1 Satz 1 Nr. 1 AO und bindet das Finanzamt.

## Direkte Förderung

- **Landesförderprogramme**: jedes Bundesland hat eigene Programme; die Anträge gehen über das Landesamt für Denkmalpflege.
- **Bundesförderung**: BKM-Sonderprogramm Denkmalschutz mit jährlich wechselnden Bewerbungsfristen; ohne ausreichende Bauakte selten erfolgreich.
- **Stiftungen**: Deutsche Stiftung Denkmalschutz, Wüstenrot-Stiftung, lokale Bürgerstiftungen.
- **Kommunale Zuschüsse**: viele Städte zahlen anteilige Zuschüsse, oft gekoppelt an Gestaltungssatzungen.

## Ablauf / Checkliste

1. Klären, ob Vermietung, Selbstnutzung oder gemischte Nutzung.
2. Maßnahmen mit der Denkmalbehörde abstimmen, damit die spätere Bescheinigung tatsächlich ergeht.
3. Vor Beginn der Arbeiten Erlaubnis nach Landesgesetz einholen — ohne Erlaubnis keine Bescheinigung.
4. Belege akribisch sammeln, Rechnungen mit Bezug auf das Denkmal kennzeichnen.
5. Bescheinigung nach Abschluss beantragen, vor der nächsten Steuererklärung.
6. Bei Versagung der Bescheinigung Widerspruch und ggf. Klage prüfen.

## Quellenpflicht

Normverweise und Rechtsprechungsanker werden vor Mandatsverwendung live in den amtlichen Datenbanken verifiziert; siehe references/zitierweise.md.

## Ausgabeformat

Strukturierte Stellungnahme in vollständigen Sätzen mit konkreten Norm-Ankern und klarem Bezug zum Mandatsbegehren.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `art-14-gg-eigentum-und-denkmalschutz`

_Art. 14 GG im Denkmalschutz: die Eintragung in die Denkmalliste und die daraus folgenden Erhaltungs-, Duldungs- und Veränderungsverbote sind Inhalts- und Schrankenbestimmung des Eigentums. Skill erklärt Sozialbindung, Zumutbarkeitsgrenze (Rheinland-Pfalz-Beschluss BVerfGE 100 Seite 226), Ausgleichspflicht bei unzumutbarer Belastung und das Eingriffsregime nach Art. 14 Abs. 3 GG bei Enteignung._

# Art. 14 GG — Eigentum und Denkmalschutz

## Zweck und Anwendungsfall

Der Skill erklärt, warum die Eintragung und die Erlaubnispflichten verfassungsrechtlich Inhalts- und Schrankenbestimmung sind, wo die Zumutbarkeitsgrenze liegt und wann eine ausgleichspflichtige Inhaltsbestimmung oder eine Enteignung in Betracht kommt. Tragender Anker ist die Leitentscheidung des BVerfG zum Rheinland-Pfalz-Denkmalschutzgesetz.

## Tragende Leitentscheidung

- **BVerfG, Beschluss vom 02.03.1999, 1 BvL 7/91, BVerfGE 100 Seite 226** — Rheinland-Pfalz-Beschluss: Erhaltungspflichten am Baudenkmal sind Inhaltsbestimmung; wird die Belastung unzumutbar, muss das Landesgesetz einen Ausgleichsmechanismus vorsehen (Übernahmeanspruch, Entschädigung, finanzielle Hilfe). Fundstelle bitte vor Verwendung in der BVerfG-Entscheidungsdatenbank verifizieren.

## Rechtlicher Rahmen

- **Art. 14 Abs. 1 Satz 1 GG** Eigentumsgarantie; **Satz 2** Inhalts- und Schrankenbestimmung durch Gesetz.
- **Art. 14 Abs. 2 GG** Sozialbindung; das öffentliche Interesse am Denkmalschutz ist ein anerkannter Gemeinwohlbelang.
- **Art. 14 Abs. 3 GG** Enteignung nur durch oder aufgrund eines Gesetzes mit ausdrücklicher Regelung von Art und Ausmaß der Entschädigung. Die Landesgesetze enthalten dazu Enteignungs- und Übernahmenormen.
- **Grenze der Zumutbarkeit:** Erhaltungspflicht und Veränderungsverbote dürfen die wirtschaftliche Nutzbarkeit nicht vollständig aufheben. Die meisten Landesgesetze kennen eine Wirtschaftlichkeitsklausel mit Übernahmeanspruch.

## Ablauf / Checkliste

1. Eingriffsintensität feststellen: bloße Veränderungssperre, umfassende Erhaltungspflicht, Untersagung der wirtschaftlichen Nutzung.
2. Zumutbarkeit prüfen anhand der wirtschaftlichen Belastung gegenüber dem zu schützenden Denkmalwert; Wirtschaftlichkeitsgutachten kann erforderlich sein.
3. Ausgleichsmechanismus im Landesgesetz prüfen (typischerweise: finanzielle Hilfen, Übernahmeanspruch, Erlaubnis trotz Schutzes).
4. Bei behaupteter Unzumutbarkeit konkretes Begehren formulieren: Erlaubnis erteilen, Ausgleich gewähren, Übernahme verlangen.

## Quellenpflicht

BVerfG-Aktenzeichen und Fundstelle in der BVerfG-Entscheidungsdatenbank live verifizieren; siehe references/zitierweise.md.

## Ausgabeformat

Verfassungsrechtliche Argumentation in vollständigen Sätzen, die das konkrete Mandatsbegehren mit Art. 14 GG und dem Ausgleichsmechanismus des Landesgesetzes verknüpft.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `grundbegriffe-und-rechtsquellen`

_Grundbegriffe des deutschen Denkmalschutzrechts: Baudenkmal, Bodendenkmal, bewegliches Denkmal, Ensemble, Welterbe, Schutzbereich, Erhaltungssatzung. Rechtsquellen: Landesgesetze als primäres Recht, Art. 73 und Art. 14 GG als bundesstaatlicher Rahmen, Welterbekonvention und Granada-Konvention als völkerrechtlicher Hintergrund, Paragrafen 7i und 11b EStG als bundesrechtliche Förderzuweisungen._

# Grundbegriffe und Rechtsquellen

## Zweck und Anwendungsfall

Wer im Denkmalschutzrecht arbeitet, muss zuerst die Begriffe und die Rechtsquellenpyramide klar haben. Dieser Skill ordnet Bau-, Boden-, bewegliches Denkmal, Ensemble, Erhaltungsbereich und Welterbe gegeneinander ab und benennt das Zusammenspiel von Landesrecht (Hauptregelungsschicht), Bundesrecht (Art. 14 GG, EStG-Förderung) und Völkerrecht (UNESCO-Welterbekonvention, Granada-Konvention).

## Eingaben

- Fragestellung des Mandats, in der ein Begriff oder eine Rechtsquellenfrage offen ist.
- Belegenheit des Objekts.

## Rechtlicher Rahmen

- **Landesrecht** ist die maßgebliche Rechtsschicht für die materielle Schutzentscheidung: Eintragung, erlaubnispflichtige Maßnahmen, Bußgeldtatbestände, Enteignung, Förderzusagen des Landes.
- **Art. 73, 74 GG** weisen den Denkmalschutz ausdrücklich nicht der konkurrierenden Bundesgesetzgebung zu; Zuständigkeit liegt nach Art. 70 GG bei den Ländern.
- **Art. 14 GG** rahmt die Eigentumsgarantie ein: Inhalts- und Schrankenbestimmung durch das Landesgesetz, ggf. Ausgleichspflicht oder Enteignung gegen Entschädigung nach Art. 14 Abs. 3 GG.
- **Paragraf 7i EStG** erlaubt die erhöhte Absetzung von Herstellungskosten bei Baudenkmälern (Vermietung); **Paragraf 11b EStG** gilt für Sonderausgaben bei selbstgenutzten Baudenkmälern; **Paragrafen 10f, 10g EStG** ergänzen den Rahmen.
- **UNESCO-Welterbekonvention 1972**, Bundesgesetzblatt 1977 II Seite 213, durch Deutschland 1976 ratifiziert; **Granada-Konvention 1985** (Schutz des architektonischen Erbes Europas) ergänzt den Rahmen.

## Ablauf / Checkliste

1. Begriff im Mandat identifizieren und gegen die jeweilige Legaldefinition im Landesgesetz prüfen.
2. Rechtsquellenebene zuordnen: Welche Norm regelt die Frage — Landesgesetz, Bundesrecht oder Völkerrecht.
3. Bei steuerlichen Fragen Paragrafen 7i, 10f, 10g, 11b EStG mit dem aktuellen Anwendungserlass und der Bescheinigung der Denkmalbehörde abgleichen.
4. Bei Welterbestätten zusätzlich Pufferzone, Managementplan und Berichtspflicht beachten.

## Quellenpflicht

Begriffsdefinitionen aus dem konkret anwendbaren Landesgesetz zitieren. EStG-Paragrafen aus gesetze-im-internet.de. Konventionstexte aus der amtlichen Bundesgesetzblatt-Fundstelle. Siehe references/zitierweise.md.

## Ausgabeformat

Begriffsbestimmung mit Quelle und Bezug auf die Mandatsfrage in vollständigen Sätzen.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `denkmalschutz-schleswig-holstein-dschg-sh`

_Denkmalschutzrecht Schleswig-Holstein nach dem Denkmalschutzgesetz Schleswig-Holstein. Skill bündelt zuständige Behörden (Ministerium für Allgemeine und Berufliche Bildung, Wissenschaft, Forschung und Kultur; Landesamt für Denkmalpflege Schleswig-Holstein in Kiel; Untere Denkmalschutzbehörden bei den Kreisen und kreisfreien Städten) und die Reform des nachrichtlichen Eintragungsmodells._

# Denkmalschutz Schleswig-Holstein (DSchG-SH)

## Zweck und Anwendungsfall

Schleswig-Holstein hat das DSchG mehrfach novelliert; die Eintragung wirkt jetzt nachrichtlich. Welterbestätten Lübeck und Haithabu prägen die Verfahrenspraxis; die Wattenmeer-Welterbestätte erstreckt sich auf Schleswig-Holstein.

## Anwendbares Gesetz

- **Gesetzesbezeichnung**: Denkmalschutzgesetz Schleswig-Holstein
- **Abkürzung**: DSchG-SH
- **Zitiergrundlage**: amtliche Landesgesetz-Datenbank gesetze-rechtsprechung.sh.juris.de

## Zuständige Behörden

- **Oberste Denkmalschutzbehörde**: Ministerium für Allgemeine und Berufliche Bildung, Wissenschaft, Forschung und Kultur
- **Obere Denkmalschutzbehörde**: Landesamt für Denkmalpflege Schleswig-Holstein in Kiel (zugleich Fachbehörde)
- **Untere Denkmalschutzbehörde**: Kreise und kreisfreie Städte (Kiel, Lübeck, Flensburg, Neumünster)
- **Fachbehörde**: Landesamt für Denkmalpflege Schleswig-Holstein

## Verfahrensbesonderheiten Schleswig-Holstein

- Welterbestätten: Hansestadt Lübeck, archäologisches Grenzlandschaft Haithabu-Danewerk, Wattenmeer.
- Backsteingotik und friesisches Bauen.
- Maritime Denkmale in Kiel, Flensburg.
- Bodendenkmäler in der archäologischen Grenzlandschaft (Schleimündung).

## Eintragungssystem

- **Systematik**: nachrichtliches Eintragungssystem

## Ablauf / Checkliste

1. Klären, ob das Objekt ein Bau-, Boden- oder bewegliches Denkmal ist.
2. Eintragungsstatus über die Denkmalliste des Landes feststellen — über gesetze-rechtsprechung.sh.juris.de.
3. Zuständige untere Denkmalschutzbehörde am Belegenheitsort kontaktieren.
4. Bei Maßnahmen das Erlaubnisverfahren nach DSchG-SH starten; bei zugleich bauordnungsrechtlich relevanten Maßnahmen die Kombination mit der Baugenehmigung berücksichtigen.
5. Konkrete Paragrafen vor Ausgabe live in gesetze-rechtsprechung.sh.juris.de verifizieren.

## Quellenpflicht

Sämtliche Paragrafenzitate werden vor Mandatsverwendung in gesetze-rechtsprechung.sh.juris.de live geprüft. Verwaltungsgerichts- und Oberverwaltungsgerichtsrechtsprechung des Landes nur mit Aktenzeichen, Datum und frei zugänglicher Fundstelle benennen.

## Ausgabeformat

Landesrechtliche Stellungnahme in vollständigen Sätzen mit konkreten Paragrafenverweisen aus dem Landesgesetz und den zuständigen Behörden.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig. Diese Regel folgt der zentralen Vorgabe in der `CLAUDE.md` des Repos und gilt ausnahmslos.
<!-- END ausformulierungspflicht (autogen) -->

## Beispiel

Erwerber eines Kaufmannshauses in der Lübecker Innenstadt-Welterbestätte plant Umnutzung der oberen Stockwerke als Bürofläche. Zuständig ist die Hansestadt Lübeck als untere Denkmalschutzbehörde mit fachlicher Stellungnahme des Landesamts für Denkmalpflege und ICOMOS-Berücksichtigung.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

