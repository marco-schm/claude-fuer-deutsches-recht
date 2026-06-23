# gebrauchsmusterrecht

Wenn du das hier oeffnest, willst du deinen Fall strukturieren, die einschlaegigen Normen pruefen und ein verwertbares Arbeitsprodukt erhalten.

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Dies ist eines von 229 Plugins aus dem Repo [`claude-fuer-deutsches-recht`](https://github.com/Klotzkette/claude-fuer-deutsches-recht). Das Repo ist von vornherein als **Plugin-Sammlung für Claude Code und Claude Cowork** gebaut: jedes Plugin enthält eine Familie zusammenhängender Skills (`SKILL.md`-Dateien), passende Hilfsdateien, Prüfrastern, Vorlagen und in vielen Fällen eine eigene Testakte. Der vorgesehene Hauptweg ist also: **Plugin in Claude Code / Cowork installieren**, am besten über den Marketplace, alternativ als einzelnes Plugin-ZIP. Dann läuft das Plugin in seiner natürlichen Umgebung mit allen Skills, Werkzeugen und Testdaten.

Damit das Plugin aber auch dann brauchbar bleibt, wenn jemand Claude Code / Cowork gerade nicht nutzen kann oder will (anderer Chatbot, Browser-Nutzung, schneller Test, Schulung, kein Setup zur Hand), gibt es zusätzlich zwei reine **Markdown-Prompts**, die ohne Plugin-Setup funktionieren: einen ausführlichen **Werkstatt-Prompt** und einen kompakten **Schnellstart-Prompt** (höchstens 7500 Zeichen). Beide sind eine einzelne `.md`-Datei, die man in jeden geeigneten Chatbot ziehen, einfügen oder per Copy-and-Paste verwenden kann.

## Downloads

In dieser Reihenfolge gedacht: zuerst der vorgesehene Plugin-Weg für Claude Code / Cowork, danach die Markdown-Alternativen für alles andere, am Schluss die zugehörigen Testakten.

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg, für Claude Code / Cowork) | ZIP | [`gebrauchsmusterrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gebrauchsmusterrecht.zip) |
| Großer Prompt (Werkstatt, Alternative ohne Plugin-Setup) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gebrauchsmusterrecht/gebrauchsmusterrecht-werkstatt.md" download><code>gebrauchsmusterrecht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart, höchstens 7500 Zeichen, Spar-Alternative) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/gebrauchsmusterrecht/gebrauchsmusterrecht-schnellstart.md" download><code>gebrauchsmusterrecht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`testakte-gebrauchsmusterrecht-schnellverschluss-sensorhalter.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gebrauchsmusterrecht-schnellverschluss-sensorhalter.zip) (Schnellverschluss S-14: Sensorhalter, Gebrauchsmusterabzweigung und Messeoffenbarung) |

> Marketplace-Hinweis: Wer mehrere Plugins gleichzeitig will, fügt nicht jedes Plugin einzeln hinzu, sondern den ganzen Marketplace über `marketplace.json` aus dem [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest). Dann sind alle 229 Plugins in Claude Code / Cowork verfügbar und können einzeln aktiviert werden.
<!-- END direkt-loslegen (autogen) -->

Dieses Plugin behandelt das deutsche Gebrauchsmuster als schnelles, ungeprüft eingetragenes technisches Schutzrecht. Es führt durch Anmeldung, Recherche, Abzweigung, Schutzfähigkeit, Verletzung und Löschung, ohne die gefährliche Abkürzung zu nehmen: Eintragung ist noch kein belastbarer Rechtsbestand.

## Arbeitsmodus

Der Einstieg ist bewusst niedrigschwellig: Uploads, Bilder, Verträge oder bloße Stichworte reichen. Das Plugin fragt zuerst nach den wenigen Punkten, die wirklich entscheiden: Frist, Produkt, Territorium, Registerstand, Veröffentlichungsdatum, Vertrag und gewünschter Output. Danach schlägt es passende Spezialskills aus diesem Plugin und angrenzenden Plugins vor.

## Praxisblöcke

| Block | Wofür? |
| --- | --- |
| Kaltstart | Technik, Produkt, Frist, Offenbarung, Patentbezug und Ziel klären |
| Anmeldung | Formalien, Ansprüche, Beschreibung, Zeichnungen, Abzweigung und Schonfrist |
| Rechtsbestand | Neuheit, erfinderischer Schritt, Ausschlüsse, Recherche und Löschung |
| Durchsetzung | Verletzung, eV, Abmahnung, Klage, Auskunft und Schadensersatz |
| Verwertung | Lizenzen, Übertragung, Insolvenz, Start-up-Strategie und internationale Alternativen |

## Quellen- und Zitierhygiene

- Offizielle Normtexte, Amtsinformationen und Register zuerst: keine erfundenen Fundstellen, keine BeckRS-/juris-Blindzitate, keine Paywall-Literatur als scheinbare Quelle.
- Register-, Gebühren-, Formular- und Fristenfragen immer live prüfen.
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugänglicher oder amtlicher Quelle verwenden.
- Bei ausländischem Recht Local-Counsel-Prüfbedarf offen kennzeichnen.

## Verhältnis zu anderen Plugins

- `markenrecht-fashion-luxus` für tiefe Marken-, Plattform- und Counterfeit-Fragen.
- `gewerblicher-rechtsschutz` und `fachanwalt-gewerblicher-rechtsschutz` für breiten IP-Kontext.
- `patentrecht` und `gebrauchsmusterrecht` für technische Schutzrechte.
- `produktrecht`, `ecommerce-recht` und `datenschutzrecht` für Produkt-, Shop- und Datenfragen.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 51 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abmahnung-gebrauchsmuster-abzweigung` | Abmahnung wegen Gebrauchsmuster vorbereiten oder verteidigen: Rechtsbestand, Unterlassung, Kosten, Fristen, Schutzschrift und Löschungsangriff im Gebrauchsmusterrecht. |
| `abzweigung-aus-patentanmeldung` | Abzweigung aus Patentanmeldung prüfen: Fristen, Anmeldetag, Inhalt, strategischer Schnellschutz und Kollisionsrisiken mit eigener Offenbarung im Gebrauchsmusterrecht. |
| `anspruchsfassung-gebrauchsmuster` | Schutzansprüche für Gebrauchsmuster strukturieren: Merkmale, unabhängiger Anspruch, Unteransprüche, Stütze, Varianten und Klarheit im Gebrauchsmusterrecht. |
| `arbeitnehmererfindung-und-inhaberschaft` | Arbeitnehmererfindung, Erfinderstellung und Inhaberschaft prüfen: Meldung, Inanspruchnahme, Rechtekette, Vergütung und Dokumentation im Gebrauchsmusterrecht. |
| `auskunft-schadensersatz-geheimhaltung` | Auskunft, Schadensersatz und Rechnungslegung nach Gebrauchsmusterverletzung prüfen: Verletzergewinn, Lizenzanalogie, konkreter Schaden und Datenumfang im Gebrauchsmusterrecht. |
| `auslandsroute-kein-beschreibung-zeichnungen` | Auslandsroute erklären: kein einheitliches EU-Gebrauchsmuster, nationale Utility Models, Patent/PCT, lokale Besonderheiten und Counsel-Briefing im Gebrauchsmusterrecht. |
| `beschreibung-und-zeichnungen` | Beschreibung und Zeichnungen prüfen: Offenbarung, Bezugszeichen, Ausführungsbeispiele, Varianten, technische Wirkung und Konsistenz mit Ansprüchen im Gebrauchsmusterrecht. |
| `beschwerde-bpatg-besichtigung-beschlagnahme` | Beschwerde zum Bundespatentgericht im Gebrauchsmusterrecht prüfen: Beschwerdegegenstand, Fristen, Begründung, neue Belege und Kostenrisiko im Gebrauchsmusterrecht. |
| `besichtigung-beschlagnahme-und-beweissicherung` | Besichtigung, Beschlagnahme und technische Beweissicherung bei Gebrauchsmusterverletzung: Produktzugang, Musterkauf, technische Analyse, Sachverständige, Geheimnisschutz, Chain of Custody und Vorbereitung von Verletzung oder Verteidigung... |
| `chemie-biotech-china-utility` | Chemie-, Pharma-, Biotech- und Stoffschutz im Gebrauchsmusterrecht einordnen: Schutzgegenstand, Ausschlüsse, Erzeugnisbezug und Patentroute im Gebrauchsmusterrecht. |
| `china-utility-model-vergleich` | China Utility Model als Vergleich und Counsel-Briefing: schneller Schutz, Produktbezug, Durchsetzung, lokale Prüfung und Kollisionsrisiken im Gebrauchsmusterrecht. |
| `computerprogramm-verfahrensausschluss` | Computerprogramm-, Verfahrens- und Methodenabgrenzung prüfen: wann Gebrauchsmuster ausscheidet und ob Patent, Urheberrecht oder Geheimhaltung besser passt im Gebrauchsmusterrecht. |
| `cross-license-verletzung-anspruchsmerkmale` | Vergleich und Cross-License im Gebrauchsmusterstreit: Unterlassung, Restbestand, Lizenz, Nichtigkeit, Kosten, Geheimhaltung und technische Änderung im Gebrauchsmusterrecht. |
| `doppelschutz-patent-dpma-anmeldung` | Doppelschutz Patent/Gebrauchsmuster koordinieren: parallele Rechte, Abzweigung, Durchsetzung, Nichtigkeitsrisiko und Vergleichsstrategie im Gebrauchsmusterrecht. |
| `dpma-anmeldung-formalien` | DPMA-Gebrauchsmusteranmeldung vorbereiten: Antrag, Beschreibung, Schutzansprüche, Zeichnungen, Gebühren, DPMAdirekt und Registereintragung im Gebrauchsmusterrecht. |
| `einstweilige-verfuegung-fto-schutzbereich` | Einstweilige Verfügung aus Gebrauchsmuster vorbereiten oder abwehren: Dringlichkeit, Rechtsbestand, Recherche, Verletzung, Glaubhaftmachung und Vollziehung im Gebrauchsmusterrecht. |
| `fto-und-schutzbereich` | Freedom-to-Operate und Schutzbereich bei Gebrauchsmustern prüfen: Anspruchsmerkmale, Registerstand, Rechtsbestand, Produktvergleich und Design-around im Gebrauchsmusterrecht. |
| `gebrauchsmuster-kaltstart-interview` | Geführtes Kaltstart-Interview für Gebrauchsmuster: Erfindung, Unterlagen, Veröffentlichung, Patentfamilie, Stand der Technik, Gegner, Budget und gewünschter Output. |
| `gebrauchsmusterrecht-schnellstart` | 'Kompakter Arbeitsmodus für gebrauchsmusterrecht. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.' |
| `geheimhaltung-vor-anmeldung` | Geheimhaltung vor Anmeldung steuern: NDA, interne Freigabe, Pitchdeck, Förderantrag, Lieferant, Messe und Open-Source-Repo im Gebrauchsmusterrecht. |
| `gutachten-rechtsbestand-insolvenz-verwertung` | Rechtsbestands- und Verletzungsgutachten für Gebrauchsmuster erstellen: Anspruchsauslegung, Stand der Technik, erfinderischer Schritt, Verletzung und Risiko im Gebrauchsmusterrecht. |
| `insolvenz-und-verwertung` | Gebrauchsmuster in Insolvenz, Distressed M&A und Verwertung prüfen: Massezuordnung, Lizenzfortbestand, Verkauf, Bewertung und Rechtsbestandsrisiko im Gebrauchsmusterrecht. |
| `japan-utility-klageantraege-verletzung` | Japanisches Utility Model als Vergleich prüfen: Registrierung, technischer Bericht, Durchsetzungsvoraussetzungen und lokale Counsel-Fragen im Gebrauchsmusterrecht. |
| `kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Gebrauchsmusterrecht: klärt technische Lehre, Offenbarung, Anmeldung, Abzweigung, Recherche, Registerstand, Verletzung, Löschung und passende Fachmodule. |
| `klageantraege-verletzung` | Klageanträge bei Gebrauchsmusterverletzung bauen: Unterlassung, Auskunft, Rechnungslegung, Vernichtung, Rückruf und Schadensersatzfeststellung im Gebrauchsmusterrecht. |
| `lizenzvertrag-gebrauchsmuster` | Gebrauchsmusterlizenz prüfen oder entwerfen: Schutzrecht, Know-how, Territory, Field of Use, Royalty, Audit, Rechtsbestand, Kündigung und Nichtigkeitsrisiko im Gebrauchsmusterrecht. |
| `local-counsel-loeschung-erwiderung` | Local-Counsel-Briefing für ausländische Utility-Model-Fragen erstellen: technische Lehre, Priorität, Offenbarung, Produkt, Gegner und gewünschte Maßnahme im Gebrauchsmusterrecht. |
| `loeschung-erwiderung-inhaber` | Erwiderung des Inhabers im Löschungsverfahren: Verteidigung, Hilfsanträge, Beschränkung, Belege und Vergleichsoptionen im Gebrauchsmusterrecht. |
| `loeschungsantrag-dpma-mandantenmemo` | Löschungsantrag beim DPMA vorbereiten: fehlende Schutzfähigkeit, Stand der Technik, unzulässige Erweiterung, Antrag, Begründung und Kosten im Gebrauchsmusterrecht. |
| `mandantenmemo-gebrauchsmusterstrategie` | Mandantenmemo zur Gebrauchsmusterstrategie: Schnellschutz, Rechtsbestandsrisiko, Kosten, Fristen, Patentbezug, Durchsetzung und nächste Schritte im Gebrauchsmusterrecht. |
| `messeveroeffentlichung-prototyp-muendliche` | Messeveröffentlichung und Prototypvorführung prüfen: öffentliche Zugänglichkeit, Schonfrist, Beweise, Fotografien, Besucher, Angebot und Vertrieb im Gebrauchsmusterrecht. |
| `muendliche-verhandlung-dpma` | Mündliche Verhandlung im DPMA-Löschungsverfahren vorbereiten: Streitpunkte, Stand der Technik, Anspruchsfassung, Beweismittel und Vergleich im Gebrauchsmusterrecht. |
| `neuheit-erfinderischer-patent-gebrauchsmuster` | Neuheit und erfinderischer Schritt nach GebrMG prüfen: Stand der Technik, öffentliche Zugänglichkeit, Merkmalsgliederung und Angriffsfestigkeit im Gebrauchsmusterrecht. |
| `neuheitsschonfrist-eigene-offenbarung` | Neuheitsschonfrist für eigene Offenbarungen prüfen: Messe, Pitchdeck, Website, Verkauf, Testkunde, Geheimhaltung und Sechsmonatsfenster im Gebrauchsmusterrecht. |
| `patent-oder-gebrauchsmuster-route` | Patent oder Gebrauchsmuster entscheiden: Geschwindigkeit, Kosten, Prüfung, Schutzdauer, Verfahren, Ausschlüsse, Durchsetzung und internationale Strategie im Gebrauchsmusterrecht. |
| `prioritaet-anmeldetag-produktlaunch-neuheit` | Priorität und Anmeldetag im Gebrauchsmusterrecht prüfen: Paris-Priorität, Patentbezug, Offenbarungsidentität und Fristen im Gebrauchsmusterrecht. |
| `produktlaunch-und-neuheit` | Produktlaunch und Neuheit koordinieren: Veröffentlichung, Messe, Pilotkunde, Website, NDA, Gebrauchsmusteranmeldung und Patentfolge im Gebrauchsmusterrecht. |
| `qualitygate-gebrmg` | Qualitygate für Gebrauchsmusteroutputs: Normen, DPMAregister, Fristen, Recherche, Stand der Technik, Rechtsprechung, Paywall-Vermeidung und offene Tatsachen. |
| `recherche-nach-schutzgegenstand-ausschluesse` | Recherche nach § 7 GebrMG vorbereiten und auswerten: DPMA-Rechercheantrag, Stand der Technik, Trefferbewertung und Rechtsbestandsrisiko im Gebrauchsmusterrecht. |
| `registerstand-aufrechterhaltung-lizenzvertrag` | Registerstand, Fälligkeiten und Aufrechterhaltung prüfen: DPMAregister, Laufzeit, Gebühren, Umschreibung, Löschung, Fristen und Portfolioüberwachung im Gebrauchsmusterrecht. |
| `schutzgegenstand-und-ausschluesse` | Schutzgegenstand und Ausschlüsse prüfen: technische Erfindung, Erzeugnis, Verfahren, biologische Verfahren, Softwareabgrenzung und bloße Idee im Gebrauchsmusterrecht. |
| `stand-technik-startup-schnellschutz` | Stand-der-Technik-Belegpaket bauen: Dokumente, öffentliche Benutzung, Internetarchiv, Produktkatalog, Messe, Zeugen und Datumsnachweise im Gebrauchsmusterrecht. |
| `startup-schnellschutz` | Schnellschutzstrategie für Start-ups und KMU: Gebrauchsmuster, Patent, Geheimhaltung, defensive Veröffentlichung, Investorenkommunikation und Budget im Gebrauchsmusterrecht. |
| `technische-laborbuch-teilloeschung` | Technische Dokumentation, Laborbuch und Entwicklungsakte auswerten: Erfinder, Datum, Varianten, Tests, Prototypen und Beweiswert im Gebrauchsmusterrecht. |
| `teilloeschung-und-hilfsantraege` | Teil-Löschung, Beschränkung und Hilfsanträge taktisch prüfen: Verteidigung engerer Ansprüche, Offenbarungsstütze und Marktwert im Gebrauchsmusterrecht. |
| `uebertragung-sicherheit-us-provisional` | Übertragung, Sicherheiten und Registerumschreibung prüfen: Rechtekette, Abtretung, Pfand, Asset Deal, Closing und Registervollzug im Gebrauchsmusterrecht. |
| `us-provisional-vs-gebrauchsmuster` | US-Provisional, Design Patent und deutsches Gebrauchsmuster vergleichen: Zweck, Fristen, Offenbarung, Kosten und spätere Durchsetzung im Gebrauchsmusterrecht. |
| `verletzung-anspruchsmerkmale` | Gebrauchsmusterverletzung anhand Anspruchsmerkmalen prüfen: wortsinngemäße Benutzung, Äquivalenznähe, Belege, Produktanalyse und Beweislast im Gebrauchsmusterrecht. |
| `vernichtung-rueckruf-vorbenutzungsrecht` | Vernichtung, Rückruf und Entfernung aus Vertriebswegen prüfen: Bestände, Verhältnismäßigkeit, Dritte, Ersatzteile und Vergleichslösungen im Gebrauchsmusterrecht. |
| `vorbenutzungsrecht` | Vorbenutzungsrecht und gutgläubige Nutzung prüfen: eigener Entwicklungsstand, Benutzungsvorbereitung, Beweisunterlagen und Reichweite im Gebrauchsmusterrecht. |
| `zoll-und-plattformdurchsetzung` | Zoll- und Plattformdurchsetzung bei Gebrauchsmusterverletzung prüfen: Produktmerkmale, Registerrecht, technische Prüfung, DSA, Marktplätze und Beweissicherung: Zoll- und Plattformdurchsetzung bei Gebrauchsmusterverletzung prüfen: Produkt... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
