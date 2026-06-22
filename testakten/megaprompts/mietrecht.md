# Megaprompt: mietrecht

## Zusammensetzung

Dieser Megaprompt enthaelt top-10 von 64 Skills des Plugins `mietrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Mietrecht (Wohnraum/Gewerbe): ordnet Rolle (Mieter, Vermieter, Hausverwaltung), markier…
2. **mandat-triage-mietrecht** — Strukturierte Eingangs-Abfrage für mietrechtliche Mandate. Klaert Mandantenrolle (Vermieter Mieter WEG-Eigentuemer Verwa…
3. **nebenkostenabrechnung-erstellen** — Vermieter- und Hausverwaltungssicht — Workflow für rechtssichere Betriebskostenabrechnungen nach § 556 BGB und BetrKV. D…
4. **eigenbedarfskuendigung-erstellen** — Vermietersicht — entwerfe eine ordentliche Kündigung wegen Eigenbedarfs nach § 573 Abs. 2 Nr. 2 BGB. Prüfroutine deckt b…
5. **lage-ausstattung-mahnung-zahlungsverzug** — Strukturierte Datenerhebung für die Einordnung in den Mietspiegel — Adresse Baujahr Wohnflaeche Bad Kueche Heizung Wohnu…
6. **mahnung-zahlungsverzug-mieter** — Vermietersicht — verfasse Mahnung und ggf. fristlose Kündigung bei Zahlungsverzug des Mieters. Prüfroutine deckt Verzug …
7. **mieteranfragen-beantworten** — Vermieter- und Hausverwaltungssicht — beantworte Mieteranfragen sachlich und ehrlich. Deckt typische Themen ab (Mietmind…
8. **mieterhoehung-widersprechen** — Mietersicht — prüfe ein Mieterhoehungsverlangen nach ortsueblicher Vergleichsmiete (§§ 558 ff. BGB) auf Form Frist Kappu…
9. **mieterhoehungsverlangen-erstellen** — Vermietersicht — verfasse ein Mieterhoehungsverlangen auf ortsuebliche Vergleichsmiete (§ 558a BGB) in Textform mit ordn…
10. **mietsenkungsverlangen** — Mietersicht — prüfe eine laufende oder bei Vertragsschluss vereinbarte Miete auf Verstoß gegen die Mietpreisbremse (§§ 5…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Mietrecht (Wohnraum/Gewerbe): ordnet Rolle (Mieter, Vermieter, Hausverwaltung), markiert Frist (§ 573c BGB Kündigung 3 Mon.), wählt Norm (BGB §§ 535/536/543/558/573 ff., WEG, BetrKV) und Zuständigkeit (Amtsgericht Belegenheit), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Mietrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `amtlichen-amtsgericht-sonderfall` — Amtlichen Amtsgericht Sonderfall
- `amtsgericht-sonderfall-und-edge-case` — Amtsgericht Sonderfall und Edge Case
- `ausschliesslich-dokumentenmatrix-und-lueckenliste` — Ausschließlich Dokumentenmatrix und Lueckenliste
- `betriebskostenabrechnung-belege-und-formelpruefer` — Betriebskostenabrechnung Belege und Formelpruefer
- `bundesland-datenerhebung-grossstadt` — Bundesland Datenerhebung Grossstadt
- `datenerhebung-zahlen-schwellen-und-berechnung` — Datenerhebung Zahlen Schwellen und Berechnung
- `eigenbedarfskuendigung-erstellen` — Eigenbedarfskuendigung Erstellen
- `erstellung-fehlerkatalog` — Erstellung Fehlerkatalog
- `grossstadt-mietspiegel-und-kappung` — Grossstadt Mietspiegel und Kappung
- `klageentwurf-amtsgericht-miet-gewerbemiete` — Klageentwurf Amtsgericht Miet Gewerbemiete
- `klageentwurf-beweislast-und-darlegungslast` — Klageentwurf Beweislast und Darlegungslast
- `lage-ausstattung-mahnung-zahlungsverzug` — Lage Ausstattung Mahnung Zahlungsverzug
- `mahnung-zahlungsverzug-mieter` — Mahnung Zahlungsverzug Mieter
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: § 573c BGB Kündigung 3 Monate, § 558b BGB Zustimmung Mieterhöhung Ende 2. Folgemonat, § 24 Abs. 4 WEG Ladung 3 Wochen, § 556 BGB Nebenkostenabrechnung 12 Monate.
- Fachpfad wählen: zentrale Anker im Mietrecht und WEG-Recht sind BGB §§ 535, 536, 543, 558, 558a, 558b, 573, 573c, 574, 556, 556a, 556b, BetrKV, WEG §§ 24, 25, 27. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Vermieter, Mieter, Hausverwaltung, WEG-Verwaltung, Amtsgericht der Belegenheit, Mieterverein, Eigentümergemeinschaft.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `mandat-triage-mietrecht`

_Strukturierte Eingangs-Abfrage für mietrechtliche Mandate. Klaert Mandantenrolle (Vermieter Mieter WEG-Eigentuemer Verwalter) Gegenstandsart (Wohnraum Gewerbe WEG) Sachgebiet (Kündigung Mieterhoehung Mietminderung Modernisierung Nebenkostenabrechnung Mietkaution-Rückforderung Eigenbedarf Sanierun..._

# Mandat-Triage Mietrecht

## Aktenstart statt Formularstart

Wenn zu **Mandat Triage Mietrecht** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde für **Mietrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsbereich

Strukturierte Eingangs-Abfrage für mietrechtliche Mandate. Klaert Mandantenrolle (Vermieter Mieter WEG-Eigentümer Verwalter) Gegenstandsart (Wohnraum Gewerbe WEG) Sachgebiet (Kündigung Mieterhoehung Mietminderung Modernisierung Nebenkostenabrechnung Mietkaution-Rückforderung Eigenbedarf Sanierung Räumung WEG-Beschluss WEG-Hausgeld-Klage). Fristen-Sofort-Check Kündigungs-Frist nach § 573c BGB Räumungs-Frist § 721 ZPO WEG-Klage ein Monat § 45 WEG Modernisierung-Ankündigung drei Monate vorher Mieterhoehung Zustimmungs-Frist zwei Monate § 558b BGB. Eskalation Telefon-Sofort bei Räumungstermin laufender Kündigungs-Frist. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandat-Triage Mietrecht` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Ablauf — sieben Fragen

### Frage 1 — Mandantenrolle?

- Vermieter (Privat / Wohnungsunternehmen)
- Mieter
- WEG-Eigentümer (in eigener Sache)
- WEG-Verwalter / Hausverwaltung
- Sondereigentums-Verwalter
- Untermieter

### Frage 2 — Gegenstandsart?

- Wohnraum
- Gewerbe
- Garage / Stellplatz (separat oder im Mietvertrag enthalten)
- WEG (Sondereigentum + Gemeinschaftseigentum)
- Pacht
- Mischmietvertrag

### Frage 3 — Sachgebiet?

- **Kündigung** (ordentlich außerordentlich Eigenbedarf Zahlungsverzug)
- Räumung
- **Mieterhöhung** (Vergleichsmiete Modernisierung)
- **Überhöhte Ausgangsmiete / Mietwucher** (Mietpreisbremse, § 5 WiStrG 1954, § 291 StGB)
- **Mietminderung** (Mangel)
- Modernisierung
- **Nebenkostenabrechnung** (Erstellung Prüfung)
- **Mietkaution** Rückforderung
- **Schönheitsreparaturen** Anspruch
- Mietmangel-Anspruch
- WEG-Beschluss-Anfechtung
- WEG-Hausgeld-Klage / Forderung
- Räumungsfrist
- Anschlussraum (Garage Stellplatz)
- Untermiete

### Frage 4 — Akute Eilbedürftigkeit?

- **Räumungstermin** binnen Tagen — Räumungsschutz
- **Kündigung gestern erhalten** Klage-Frist nach Vorbemerkung
- **Eigenbedarfsräumung droht** Räumungsklage zugestellt
- **Modernisierung morgen** unzumutbar
- **Mietminderungs-Stopp** Vermieter klagt Mietrückstand
- **Schimmelbefall lebensbedrohlich**
- **WEG-Beschluss-Anfechtung** ein-Monats-Frist

### Frage 5 — Vertragsbasis?

- Schriftlicher Mietvertrag (Datum)
- Mündlicher Mietvertrag
- Wohnraum-Mietvertrag mit gestaffelten Mieten / Indexmiete
- Gewerbemietvertrag
- WEG-Gemeinschaftsordnung
- Teilungserklärung

### Frage 6 — Frist?

- **Kündigungs-Frist Vermieter** § 573c BGB drei Monate (bei langer Mietdauer länger)
- **Kündigungs-Frist Mieter** drei Monate (nicht abhängig von Mietdauer)
- **Räumungsfrist Vollstreckung** § 721 ZPO Gewährung
- **Mieterhöhungs-Zustimmungsfrist § 558b BGB** zwei Monate
- **Mietminderungs-Anzeige** § 536c BGB unverzüglich
- **Betriebskostenabrechnung** § 556 Abs. 3 BGB zwölf Monate
- **WEG-Beschluss-Anfechtung** § 45 WEG ein Monat

### Frage 7 — Wirtschaftliche Verhältnisse?

- Miete-Volumen
- Eigenkapital (Mietkaution Selbstbeteiligung)
- Rechtsschutz Mieter Vermieter
- PKH bei Mieter

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Eigenbedarfskündigung erstellen | `eigenbedarfskuendigung-erstellen` |
| Mieterhöhung — Vermieter | `mieterhoehungsverlangen-erstellen` |
| Mieterhöhung — Mieter | `mieterhoehung-pruefen-widersprechen` |
| Mietsenkungsverlangen | `mietsenkungsverlangen` |
| Mietpreisüberhöhung / Mietwucher | `mietpreisueberhoehung-wistrg-1954-mietwucher` |
| Nebenkosten erstellen | `nebenkostenabrechnung-erstellen` |
| Nebenkosten prüfen | `nebenkostenabrechnung-pruefen` |
| Klage am AG | `klageentwurf-amtsgericht` |
| Mahnung Zahlungsverzug | `mahnung-zahlungsverzug-mieter` |
| Mieteranfragen beantworten | `mieteranfragen-beantworten` |
| Lage und Ausstattung erheben | `lage-und-ausstattung-erheben` |
| WEG-Beschluss-Anfechtung | `weg-beschluss-anfechten` |
| Mietkaution-Rückforderung | (Skill mietkaution-rueckforderung — perspektivisch) |
| Mietminderung wegen Mangel | (Skill mietminderung-prüfen — perspektivisch) |

## Mandatsannahme

- **Konflikt-Check** — keine Doppelmandate Mieter/Vermieter
- **Streitwert** Wohnraum Jahresmiete EUR (KSchG-Streitwert vergleichbar)
- **AG-Zuständigkeit** Wohnraummietsachen nach Paragraf 23 Nummer 2a GVG ausschließlich und streitwertunabhängig beim Amtsgericht; in erster Instanz kein Anwaltszwang nach Paragraf 78 Absatz 1 Satz 1 ZPO im Umkehrschluss.
- **Versicherungs-Deckung** Mietrechtsschutz häufig

## Eskalation

- **Telefon-Sofort** Räumungstermin Räumungsklage Schimmel
- **Binnen einer Stunde** WEG-Beschluss-Anfechtung Frist läuft heute
- **Heute** Kündigungs-Widerspruch Mieterhöhungs-Antwort
- **Diese Woche** Klageschrift Räumungsschutz

## Ausgabe

- `triage-protokoll-mietrecht.md`
- Aktenanlage
- Frist im Fristenbuch
- Mandatsvereinbarung mit Honorar
- Empfehlung Folge-Skill

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Quellen

- BGB §§ 535 ff. 558 558b 573c 556
- WEG §§ 14 19 20 44 45
- ZPO § 721 (Räumungsfrist)
- BGH VIII. Zivilsenat und V. Zivilsenat nur mit Datum, Aktenzeichen und frei prüfbarer Quelle

## Aktuelle Rechtsprechung — Leitsaetze (Triage-Relevant)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `nebenkostenabrechnung-erstellen`

_Vermieter- und Hausverwaltungssicht — Workflow für rechtssichere Betriebskostenabrechnungen nach § 556 BGB und BetrKV. Deckt Abrechnungszeitraum Zugangsfrist (zwoelf Monate) Umlagefähigkeit Verteilerschluessel HeizkostenV Vorauszahlungen und Mindestinhalt ab. Hinweise zu typischen Fehlerquellen die zur Unwirksamkeit führen. Erzeugt eine Mustergliederung und Prüfroutine vor Versand. Disclaimer im Skill und vor jedem Versand-Schritt._

# Nebenkostenabrechnung erstellen (Vermieter / Hausverwaltung)

## Disclaimer (Schlüsselstelle)

Der nachstehende Workflow ist eine Arbeitsgrundlage. Vor Versand einer Abrechnung mit groesserer Nachforderung oder bei strittigen Verteilerschlüsseln ist eine Prüfung durch einen Fachanwalt für Mietrecht oder eine erfahrene Hausverwaltung empfohlen.

## Workflow

### Schritt 1 — Rechtsgrundlagen sichern

- Mietvertraegliche Umlagevereinbarung prüfen (Verweis auf BetrKV genügt).
- Abrechnungszeitraum festlegen (maximal zwölf Monate).
- Zugangsfrist beachten: innerhalb von **zwölf Monaten nach Ende des Abrechnungszeitraums** beim Mieter eingegangen (§ 556 Abs. 3 Satz 2 BGB), sonst Nachforderungsausschluss.

### Schritt 2 — Gesamtkosten erfassen

- Belege je Kostenart sortieren (siebzehn Arten nach § 2 BetrKV plus sonstige Betriebskosten falls vertraglich vereinbart).
- Nicht umlagefähig herausrechnen: Verwaltung, Instandhaltung und Instandsetzung, Bankgebuehren.
- Brennstoff-Vorrat zum Stichtag bewerten.

### Schritt 3 — Verteilerschlüssel

- Wohnfläche, Personenzahl, Wohneinheit oder Verbrauch nach Mietvertrag und § 556a BGB.
- Änderung des Schlüssels nur unter den Voraussetzungen des § 556a Abs. 2 BGB.
- **Heizkosten und Warmwasser**: mindestens fünfzig Prozent verbrauchsabhängig nach § 7 HeizkostenV — empfohlen siebzig Prozent.

### Schritt 4 — Mieteranteil berechnen

- Wohnfläche oder andere Bezugsgroesse je Mieter dokumentieren.
- Anteil je Kostenart berechnen.
- Vorauszahlungen des Mieters abziehen.
- Saldo (Guthaben oder Nachforderung) ausweisen.

### Schritt 5 — Mindestinhalt der Abrechnung

- Abrechnungszeitraum.
- Zusammenstellung der Gesamtkosten je Position.
- Angabe und Erläuterung des Verteilerschlüssels je Position.
- Berechnung des Mieteranteils.
- Abzug der Vorauszahlungen.
- Saldo mit Fälligkeit und Zahlungsweg.
- Hinweis auf Einwendungsfrist nach § 556 Abs. 3 Satz 5 BGB.

### Schritt 6 — Anpassung der Vorauszahlungen (§ 560 Abs. 4 BGB)

- Bei dauerhaften Änderungen können Vermieter und Mieter durch Erklärung in Textform die Vorauszahlung auf eine angemessene Höhe anpassen.
- Empfehlung: separates Schreiben, getrennt von der Abrechnung.

### Schritt 7 — Prüfroutine vor Versand

- Rechnerische Prüfung der Summen.
- Plausibilität je Position (Vorjahresvergleich).
- Verteilerschlüssel mit Mietvertrag abgeglichen.
- Heizkostenabrechnung enthält den nach HeizkostenV vorgeschriebenen Verbrauchsanteil.
- Belege können kurzfristig zur Einsicht bereitgestellt werden (§ 556 Abs. 4 BGB).
- Versand nachweisbar (Einschreiben oder Bote).

## Ausgabe

Mustergliederung der Abrechnung als Markdown plus Checkliste vor Versand. Vor der finalen Freigabe Disclaimer wiederholen.

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

## Aktuelle Rechtsprechung — Leitsaetze (Stand 05/2026, verifiziert dejure.org)

- BGH 09.04.2008, VIII ZR 84/07 — Mindestanforderungen Betriebskostenabrechnung (dejure.org/2008,5921; BGHZ 176, 191)
- BGH 12.11.2014, VIII ZR 112/14 — Beweislast Vermieter fuer rechtzeitigen Zugang innerhalb der 12-Monatsfrist (dejure.org/2014,33617)
- BGH 06.04.2016, VIII ZR 78/15 — Beleg-Einsichtsrecht des Mieters umfasst auch Datennachvollziehbarkeit (dejure.org/2016,8164)
- HeizkostenV-Novelle 2022 (BGBl. I S. 2206) — fernablesbare Zaehler, unterjaehrige Verbrauchsinfo, Kuerzungsrecht § 12 HeizkostenV bei Verstoss
- CO2KostAufG (BGBl. I 2022 S. 2030, in Kraft 01.01.2023) — Stufenmodell zur Aufteilung der CO2-Kosten zwischen Vermieter und Mieter nach Gebaeudeenergieeffizienz

Weitere Entscheidungen vor Ausgabe ueber dejure.org / bundesgerichtshof.de verifizieren.

## Paragrafenkette

§ 556 BGB, BetrKV, HeizkostenV — Abrechnungsfrist, Umlagefaehigkeit, Verteilerschluessel

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `eigenbedarfskuendigung-erstellen`

_Vermietersicht — entwerfe eine ordentliche Kündigung wegen Eigenbedarfs nach § 573 Abs. 2 Nr. 2 BGB. Prüfroutine deckt berechtigtes Interesse (Eigennutzung Familienangehoerige Haushaltsangehoerige) konkrete Begründung im Kündigungsschreiben (§ 573 Abs. 3 BGB) Kündigungsfristen nach § 573c BGB (dr..._

# Eigenbedarfskündigung erstellen (Vermieter / Hausverwaltung)

## Arbeitsbereich

Vermietersicht — entwerfe eine ordentliche Kündigung wegen Eigenbedarfs nach § 573 Abs. 2 Nr. 2 BGB. Prüfroutine deckt berechtigtes Interesse (Eigennutzung Familienangehoerige Haushaltsangehoerige) konkrete Begründung im Kündigungsschreiben (§ 573 Abs. 3 BGB) Kündigungsfristen nach § 573c BGB (drei sechs neun Monate je nach Mietdauer) Sperrfristen aus Landesverordnung (drei bis zehn Jahre nach Umwandlung) Sozialklausel des Mieters (§ 574 BGB) und Risiko der Vortaeuschung (Schadensersatz). Erzeugt rechtssicheres Kündigungsschreiben mit Disclaimer. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Eigenbedarfskündigung erstellen (Vermieter / Hausverwaltung)` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Disclaimer (Schlüsselstelle, mehrfach)

Die Eigenbedarfskündigung ist eines der streitanfälligsten Felder des Mietrechts. Eine formell oder materiell fehlerhafte Kündigung ist unwirksam — der Mieter darf in der Wohnung bleiben. Bei späterem Wegfall des Eigenbedarfs vor Auszug droht **Schadensersatz** (BGH-Rspr. zur Vortaeuschung). Vor Versand ist eine fachanwaltliche Prüfung dringend empfohlen. Diese Auto-Erstellung ersetzt nicht die anwaltliche Vertretung.

## Workflow

### Schritt 1 — Berechtigtes Interesse prüfen (§ 573 Abs. 2 Nr. 2 BGB)

- **Eigennutzung** durch den Vermieter selbst.
- **Familienangehörige** — Eltern Kinder Geschwister Ehegatten eingetragene Lebenspartner.
- **Haushaltsangehörige** — Personen die mit dem Vermieter dauerhaft im Haushalt leben (z. B. Pflegekraft Lebensgefährtin).
- Eigenbedarf juristischer Personen (GmbH AG) ist nicht möglich — Kündigung wegen Eigenbedarfs setzt natürliche Person voraus.
- **Konkret** und vernuenftig nachvollziehbar — nicht bloss vorsorglich oder spekulativ.

### Schritt 2 — Begründung im Kündigungsschreiben (§ 573 Abs. 3 BGB)

Die Begründung muss im Schreiben enthalten sein und so konkret sein dass der Mieter die Schlüssigkeit prüfen kann:

- Name der begünstigten Person und Verhältnis zum Vermieter.
- Warum die Wohnung gerade für diese Person benötigt wird.
- Aktuelle Wohnsituation der begünstigten Person.
- Zeitpunkt des Bedarfs.

Pauschale Floskeln wie "wegen Eigenbedarfs" reichen nicht.

### Schritt 3 — Kündigungsfristen (§ 573c BGB)

Je nach Dauer des Mietverhältnisses beim Mieter:

- Bis fünf Jahre: **drei Monate**.
- Fünf bis acht Jahre: **sechs Monate**.
- Ab acht Jahren: **neun Monate**.

Zugang spätestens am dritten Werktag eines Monats für das Ende dieses Monats plus die jeweilige Frist.

### Schritt 4 — Sperrfristen nach Landesverordnung

Bei Umwandlung der Mietwohnung in eine Eigentumswohnung **vor** der Veräußerung an einen neuen Eigentümer gilt nach § 577a BGB eine **Sperrfrist von drei Jahren** ab Veräußerung — in Gebieten mit angespanntem Wohnungsmarkt durch Landesverordnung verlängert auf bis zu **zehn Jahre**. Prüfung in `references/mietspiegel-quellen.md` (Spalte Kündigungssperrfristverordnung).

### Schritt 5 — Sozialklausel (§ 574 BGB)

Der Mieter kann der Kündigung widersprechen wenn:

- Beendigung eine **Härte** bedeutet die auch unter Würdigung der berechtigten Interessen des Vermieters nicht zu rechtfertigen ist.
- Klassische Härtefälle: hohes Alter Krankheit Schwangerschaft fehlender Ersatzwohnraum.
- Widerspruch ist spätestens **zwei Monate vor Ende** der Mietzeit zu erklären (§ 574b Abs. 2 BGB).
- Rechtsfolge: Fortsetzung des Mietverhältnisses für angemessene Zeit (§ 574a BGB).

Der Vermieter muss im Kündigungsschreiben auf das Widerspruchsrecht hinweisen (§ 568 Abs. 2 BGB) — sonst verlängerte Widerspruchsfrist.

### Schritt 6 — Vortaeuschung und Schadensersatz (verifiziert dejure.org)

- **BGH 14.12.2016, VIII ZR 232/15**: Bei Vortaeuschung des Eigenbedarfs haftet der Vermieter dem gekuendigten Mieter auf Schadensersatz nach §§ 280 Abs. 1, 311a Abs. 2 BGB; ersatzfaehig sind Umzugskosten, Maklerkosten, Mehrkosten neuer Mietwohnung und ggf. Anwaltskosten. Quelle: dejure.org/2016,46126 / NJW 2017, 1474.
- **BGH 10.05.2017, VIII ZR 292/15**: Wegfall des Eigenbedarfs nach Ausspruch der Kuendigung — Vermieter muss den Mieter unverzueglich informieren, sonst Schadensersatzpflicht. Quelle: dejure.org/2017,15097.
- **BGH 27.06.2007, VIII ZR 271/06**: Eigenbedarf einer GbR (Aussengesellschaft) — Eigenbedarf kann für die Gesellschafter geltend gemacht werden, sofern die GbR Vermieter ist und der Gesellschafter Eigenbedarf hat. Quelle: dejure.org / NJW 2007, 2845.

### Schritt 7 — Formale Anforderungen (§ 568 Abs. 1 BGB)

- **Schriftform** zwingend — eigenhändige Unterschrift des Vermieters (oder aller Vermieter wenn Personenmehrheit).
- Bei juristischer Person als Vermieter: Unterschrift des organschaftlich Vertretungsberechtigten.
- **Adressierung** alle Mieter namentlich.
- **Zustellung** nachweisbar (Einschreiben mit Rückschein oder Bote mit Zustellungsprotokoll).

## Schreiben-Entwurf

Erzeuge ein Kündigungsschreiben mit:

1. Absender Vermieter mit Anschrift.
2. Adresse aller Mieter namentlich.
3. Bezugnahme auf den Mietvertrag (Datum Mietsache).
4. Kündigungserklärung mit konkretem Endtermin.
5. Begründung nach § 573 Abs. 3 BGB: begünstigte Person Verhältnis Wohnsituation Bedarfslage.
6. Hinweis auf das Widerspruchsrecht des Mieters nach § 574 BGB und die Widerspruchsfrist nach § 574b Abs. 2 BGB.
7. Eigenhaendige Unterschrift aller Vermieter.
8. **Disclaimer** — Hinweis dass der Mieter sich beraten lassen sollte (Mieterverein Fachanwalt).

## Vor Versand (Disclaimer wiederholt)

Vor Versand der Eigenbedarfskündigung: fachanwaltliche Prüfung. Risiko: Unwirksamkeit Schadensersatz strafrechtliche Verfolgung bei Vortaeuschung. Sperrfristen aus Landesverordnung prüfen.

## Aktuelle Rechtsprechung Eigenbedarfskündigung (Stand 05/2026, verifiziert dejure.org)

- BGH, Urt. v. 24.09.2025 – Az. VIII ZR 289/23 — Anforderungen an die Begruendung nach § 573 Abs. 3 BGB sind nicht ueberzogen; Eigenbedarf bleibt wirksam auch wenn der Vermieter zunaechst Eigennutzung waehrend Umbau plant und spaetere Veraeusserung beabsichtigt. Konkretisierung des Maßstabs „ernsthafter, vernuenftiger, nachvollziehbarer Eigennutzungswunsch". Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=24.09.2025&Aktenzeichen=VIII+ZR+289/23
- BGH 14.12.2016, VIII ZR 232/15 — Schadensersatz bei vorgetaeuschtem Eigenbedarf (https://dejure.org/2016,46126)
- BGH 10.05.2017, VIII ZR 292/15 — Mitteilungspflicht bei Wegfall des Eigenbedarfs (https://dejure.org/2017,15097)
- BGH 22.05.2019, VIII ZR 180/18 — Haerteklausel § 574 BGB; Pflicht zur Abwaegung Vermieter-/Mieterinteressen, alters- oder krankheitsbedingte Haerten substantiiert prüfen (https://dejure.org/2019,12824)
- BGH 11.12.2019, VIII ZR 144/19 — Haerteklausel: Hochbetagtes Alter und langjaehrige Verwurzelung können Vertragsfortsetzung tragen; nur ausnahmsweise unbefristete Fortsetzung (https://dejure.org/2019,49075)
- BGH 09.05.2012, VIII ZR 238/11 — „Vorratskündigung"-Verbot; Eigenbedarf muss konkret-bevorstehend sein (https://dejure.org/2012,12036)

Weitere Entscheidungen vor Ausgabe per dejure.org / bundesgerichtshof.de mit Datum und Aktenzeichen verifizieren.

## Paragrafenkette Eigenbedarfskündigung

§ 573 Abs. 2 Nr. 2 BGB (berechtigtes Interesse Eigenbedarf) → § 573 Abs. 3 BGB (Begründungspflicht) → § 573c BGB (Kündigungsfristen) → § 568 Abs. 1 BGB (Schriftform) → § 568 Abs. 2 BGB (Widerspruchshinweis) → § 574 BGB (Sozialklausel Widerspruch) → § 574b BGB (Widerspruchsfrist 2 Monate) → § 577a BGB (Sperrfrist nach Umwandlung) → § 280 BGB (Schadensersatz bei vorgetäuschtem Eigenbedarf)

## Triage vor Erstellung Eigenbedarfskündigung

Kläre vor Beginn:
1. Natürliche Person als Vermieter? (Juristische Personen können keinen Eigenbedarf geltend machen)
2. Berechtigte Person konkret benannt? (Name Verhältnis Wohnsituation Bedarfsgrund)
3. Wurde die Wohnung nach Abschluss des Mietvertrags in Wohnungseigentum umgewandelt? (Sperrfrist § 577a BGB prüfen)
4. Welche Mietdauer liegt vor? (Bestimmt Kündigungsfrist § 573c BGB)
5. Ist der Hinweis auf das Widerspruchsrecht nach § 574 BGB vorbereitet?

## Output-Template Eigenbedarfskündigungsschreiben

**Adressat:** Mieter — Tonfall sachlich-erklärend, Schriftform zwingend

```
[VERMIETER]
[ADRESSE VERMIETER]

An [ALLE MIETER MIT NAMEN]
[ADRESSE MIETWOHNUNG]

[ORT], [DATUM]

Kündigung des Mietverhältnisses wegen Eigenbedarfs

Sehr geehrte/r Herr/Frau [NAME],

hiermit kündige ich das mit Ihnen bestehende Mietverhältnis über die Wohnung
[ANSCHRIFT, LAGE, STOCKWERK, QM] vom [DATUM DES MIETVERTRAGS] gemäß § 573
Abs. 2 Nr. 2 BGB ordentlich zum [KÜNDIGUNGSTERMIN, berechnet nach § 573c BGB].

Begründung (§ 573 Abs. 3 BGB):
Ich benötige die Wohnung für [BEGÜNSTIGTE PERSON, VERHÄLTNIS].
[BEGÜNSTIGTE PERSON] lebt derzeit in [AKTUELLE WOHNSITUATION].
Die aktuelle Unterkunft ist nicht zumutbar, weil [BEDARFSGRUND: zu klein/zu weit/gesundheitliche Gründe/etc.].

Hinweis auf Widerspruchsrecht (§ 574 BGB):
Sie können der Kündigung widersprechen, wenn die Beendigung des Mietverhältnisses
für Sie eine unzumutbare Härte bedeutet. Der Widerspruch muss spätestens zwei Monate
vor Ablauf der Kündigungsfrist schriftlich erfolgen (§ 574b Abs. 2 BGB).

Mit freundlichen Grüßen
[EIGENHAENDIGE UNTERSCHRIFT ALLER VERMIETER]
```

**Hinweis:** Vor Versand fachanwaltliche Prüfung empfohlen.

<!-- AUDIT 27.05.2026
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Quelle: dejure.org. Prufer: Bundle-005-Audit.
-->

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

---

## Skill: `lage-ausstattung-mahnung-zahlungsverzug`

_Strukturierte Datenerhebung für die Einordnung in den Mietspiegel — Adresse Baujahr Wohnflaeche Bad Kueche Heizung Wohnungsausstattung Gebaeudeausstattung. Erfasst alle Merkmale die in qualifizierten Mietspiegeln als Sondermerkmale bewertet werden (Bodenbelag Fenster Balkon Terrasse Aufzug Stellp..._

# Lage und Ausstattung erheben

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Lage und Ausstattung erheben` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

Dieser Skill leitet eine vollständige Datenerhebung an. Ergebnis ist ein strukturiertes Protokoll, das in jeden anderen Skill dieses Plugins einfliesst.

## Disclaimer

Diese Erhebung ersetzt keine Rechtsberatung. Sie ist ein Vorbereitungsschritt für eine spätere rechtliche Prüfung. Bei strittigen Punkten amtliche Quellen heranziehen oder Rechtsrat einholen.

## Workflow

### 1. Adresse und Lage

- Vollständige Adresse (Straße, Hausnummer, PLZ, Ort).
- Stadt-/Stadtteil/Quartier.
- Wohnlagen-Zuordnung nach dem amtlichen Straßenverzeichnis oder Geoportal der Stadt (einfach / mittel / gut). Wenn unklar: Link auf das amtliche Verzeichnis aus references/mietspiegel-quellen.md.

### 2. Gebäude

- Baujahr (laut Mietvertrag, Grundbuchauszug oder Bauakte).
- Letzte umfassende Modernisierung (Jahr, Umfang).
- Anzahl Wohneinheiten.
- Aufzug ja/nein.
- Stellplatz/Garage zur Wohnung gehoerig.
- Energieausweis (Verbrauch oder Bedarf, kWh/(m² · a)).

### 3. Wohnung

- Wohnfläche in m² nach Wohnflächenverordnung (WoFlV).
- Anzahl Zimmer.
- Stockwerk.
- Bodenbelaege je Raum (Parkett, Laminat, Fliesen, Teppich).
- Fenster (Doppel- oder Dreifachverglasung, Holz/Kunststoff).
- Balkon / Loggia / Terrasse (Größe, Ausrichtung).
- Keller / Abstellraum außerhalb der Wohnung.

### 4. Bad

- Anzahl Baeder/WCs.
- Wanne und/oder Dusche.
- Fenster im Bad.
- Bodenheizung.

### 5. Küche

- Einbauküche mitvermietet ja/nein.
- Geräte (Herd, Backofen, Kuehlschrank, Geschirrspueler).

### 6. Heizung und Warmwasser

- Heizungsart (Gas, Fernwaerme, Oel, Waermepumpe).
- Zentral oder Etagenheizung.
- Warmwasserbereitung (zentral, dezentral, über Heizung).

### 7. Mietvertrag

- Vertragsdatum.
- Aktuelle Nettokaltmiete und Vorauszahlungen.
- Indexmiete, Staffelmiete oder Festmiete.
- Schönheitsreparaturklausel (im Original-Wortlaut zitieren).
- Schlüsselgeld, Kaution.

## Ausgabe

Protokoll als Markdown mit den oben genannten Abschnitten plus Quellenangabe (woher stammt jede Information: Mietvertrag, Augenschein, Energieausweis, Straßenverzeichnis). Dieses Protokoll ist Input für alle weiteren Skills.

## Aktuelle Rechtsprechung — Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette

- Ortsueblliche Vergleichsmiete: § 558 BGB
- Begruendungsmittel: § 558a BGB
- Kappungsgrenze: § 558 Abs. 3 BGB

---

## Skill: `mahnung-zahlungsverzug-mieter`

_Vermietersicht — verfasse Mahnung und ggf. fristlose Kündigung bei Zahlungsverzug des Mieters. Prüfroutine deckt Verzug nach § 286 BGB Fälligkeit der Miete (§ 556b Abs. 1 BGB) Mahnschreiben Aufrechnungsverbot fristlose Kündigung nach § 543 Abs. 2 Nr. 3 BGB (eine Monatsmiete plus zwei aufeinanderf..._

# Mahnung und Kündigung bei Zahlungsverzug (Vermieter / Hausverwaltung)

## Arbeitsbereich

Vermietersicht — verfasse Mahnung und ggf. fristlose Kündigung bei Zahlungsverzug des Mieters. Prüfroutine deckt Verzug nach § 286 BGB Fälligkeit der Miete (§ 556b Abs. 1 BGB) Mahnschreiben Aufrechnungsverbot fristlose Kündigung nach § 543 Abs. 2 Nr. 3 BGB (eine Monatsmiete plus zwei aufeinanderfolgende Termine oder Rückstand von zwei Monatsmieten über zwei Termine) hilfsweise ordentliche Kündigung nach § 573 Abs. 2 Nr. 1 BGB und Schonfristzahlung des Mieters nach § 569 Abs. 3 BGB (Nachholung innerhalb von zwei Monaten nach Zustellung der Räumungsklage). Erzeugt gestuftes Schreibenpaket mit Disclaimer. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mahnung und Kündigung bei Zahlungsverzug (Vermieter / Hausverwaltung)` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Disclaimer (Schlüsselstelle, mehrfach)

Eine Zahlungsverzugskündigung ist die mietrechtlich folgenreichste Erklärung. Eine formale oder materielle Fehlkündigung ist unwirksam und kann zu Schadensersatzanspruechen des Mieters führen. Vor Versand einer fristlosen Kündigung ist eine fachanwaltliche Prüfung dringend empfohlen. Diese Auto-Erstellung ersetzt nicht die anwaltliche Vertretung.

## Workflow

### Schritt 1 — Fälligkeit und Verzug prüfen

- **Fälligkeit** der Miete: spätestens am dritten Werktag eines jeden Monats (§ 556b Abs. 1 BGB) — soweit vertraglich nichts anderes vereinbart ist.
- **Verzug** ohne Mahnung tritt nach § 286 Abs. 2 Nr. 1 BGB ein wenn die Miete kalendermaessig bestimmt ist (was bei § 556b BGB der Fall ist).
- Eine Mahnung ist also rechtlich nicht zwingend — als Vorstufe zur Kündigung aber dringend empfohlen (Beweisbarkeit gutes Verhältnis Schonfristoption).

### Schritt 2 — Mahnschreiben

- Sachliche knappe Aufforderung zur Zahlung des konkreten Rückstands.
- Frist zur Zahlung (eine bis zwei Wochen genügen wegen Verzugs).
- Hinweis auf drohende Kündigung wenn nicht gezahlt wird.
- Hinweis auf laufende Verzugszinsen (§ 288 BGB).

### Schritt 3 — Voraussetzungen der fristlosen Kündigung (§ 543 Abs. 2 Nr. 3 BGB)

Die fristlose Kündigung wegen Zahlungsverzugs ist zulässig wenn:

- **Variante a**: der Mieter für **zwei aufeinanderfolgende Termine** mit der Entrichtung der Miete oder eines nicht unerheblichen Teils der Miete im Verzug ist. "Nicht unerheblich" = mehr als eine Monatsmiete.
- **Variante b**: in einem Zeitraum der sich über **mehr als zwei Termine** erstreckt mit einem Betrag in Verzug ist der **zwei Monatsmieten** erreicht.

Was zur Miete zählt: Grundmiete plus Nebenkostenvorauszahlungen plus etwaige Heizkostenvorauszahlungen.

### Schritt 4 — Ordentliche Kündigung als Hilfsantrag (§ 573 Abs. 2 Nr. 1 BGB)

- Hilfsweise zur fristlosen Kündigung ist die ordentliche Kündigung wegen erheblicher schuldhafter Pflichtverletzung zulässig.
- Frist nach § 573c BGB (drei sechs oder neun Monate je nach Mietdauer).
- Empfehlung: in einem Schreiben fristlos hilfsweise ordentlich kündigen.

### Schritt 5 — Formale Anforderungen (§ 568 Abs. 1 BGB)

- **Schriftform** zwingend mit eigenhändiger Unterschrift aller Vermieter.
- **Begründung** im Schreiben — konkrete Aufstellung der rückständigen Monate und Betraege (§ 569 Abs. 4 BGB).
- **Hinweis** auf das Recht des Mieters die Wohnung durch Nachzahlung zu erhalten (§ 569 Abs. 3 Nr. 2 BGB) — Schonfristzahlung innerhalb von **zwei Monaten** nach Zustellung der Raeumungsklage.

### Schritt 6 — Schonfristzahlung des Mieters (§ 569 Abs. 3 Nr. 2 BGB)

- Wenn der Mieter nach Zugang der fristlosen Kündigung aber spätestens bis zum Ablauf von zwei Monaten nach Zustellung der **Raeumungsklage** den gesamten Rückstand begleicht oder eine öffentliche Stelle die Zahlung verbindlich zusagt: **fristlose Kündigung wird unwirksam**.
- Wichtig: die Schonfristzahlung wirkt nur für die fristlose Kündigung — eine hilfsweise erklärte **ordentliche** Kündigung bleibt nach BGH-Rspr. wirksam.
- Schonfristzahlung kann nicht mehrfach in Anspruch genommen werden (§ 569 Abs. 3 Nr. 2 Satz 2 BGB) — bei wiederholtem Zahlungsverzug ist sie ausgeschlossen wenn binnen zwei Jahren bereits einmal angewendet.

### Schritt 7 — Prüfroutine vor Versand

- Rückstandsberechnung dokumentiert (Monat für Monat mit Sollstellung und Zahlung).
- Schwelle eine Monatsmiete plus zwei Termine oder zwei Monatsmieten über zwei Termine erreicht.
- Konkrete Bezifferung des Rückstands im Kündigungsschreiben.
- Alle Vermieter unterzeichnen die Kündigung.
- Zustellung mit Nachweis (Einschreiben mit Rückschein oder Bote).
- Hinweis auf Schonfristzahlung im Schreiben (nicht zwingend aber empfohlen).

## Schreibenpaket

### A. Mahnschreiben

Sachlich kurz. Anrede mit Namen. Bezugnahme auf den Mietvertrag. Konkrete Aufstellung des Rückstands. Frist zur Zahlung. Hinweis auf Verzugszinsen und drohende Kündigung. Höflichkeitsformel.

### B. Fristlose Kündigung mit hilfsweiser ordentlicher Kündigung

1. Absender Vermieter mit Anschrift.
2. Adresse aller Mieter namentlich.
3. Bezugnahme auf den Mietvertrag.
4. Kündigungserklärung — fristlos nach § 543 Abs. 2 Nr. 3 BGB.
5. Hilfsweise ordentliche Kündigung nach § 573 Abs. 2 Nr. 1 BGB mit konkretem Endtermin nach § 573c BGB.
6. Begründung mit konkreter Aufstellung der rückständigen Monate und Betraege.
7. Hinweis auf Schonfristzahlung nach § 569 Abs. 3 Nr. 2 BGB.
8. Hinweis auf Widerspruchsrecht nach § 574 BGB für die hilfsweise ordentliche Kündigung.
9. Eigenhaendige Unterschrift aller Vermieter.

## Hinweis zur Raeumungsklage

Wenn der Mieter nach Ablauf der Kündigungsfrist nicht räumt: **Räumungsklage** zum Amtsgericht am Belegenheitsort nach Paragraf 29a ZPO. Bei Wohnraum ist das Amtsgericht nach Paragraf 23 Nummer 2a GVG ausschließlich und streitwertunabhängig zuständig; das gilt auch für die verbundene Räumungs- und Zahlungsklage. In erster Instanz besteht dort kein Anwaltszwang nach Paragraf 78 Absatz 1 Satz 1 ZPO im Umkehrschluss. Siehe Skill `klageentwurf-amtsgericht`. **Disclaimer** — die Räumungsklage ist anwaltliche Praxis; Selbstvertretung ist beim Amtsgericht zwar möglich, aber nicht empfohlen.

## Vor Versand (Disclaimer wiederholt)

Vor Versand der fristlosen Kündigung: fachanwaltliche Prüfung der Rückstandsberechnung der Schwellenwerte und der Schonfristregelung. Risiko: Unwirksamkeit Schadensersatz Verzug auf eigener Seite. Die Schonfristzahlung kann das gesamte Verfahren wieder neutralisieren — der Vermieter muss dann ordentlich gekündigt haben um den Mieter langfristig loszuwerden.

## Aktuelle Rechtsprechung — Leitsaetze

- BGH, Urt. v. 09.07.2025 – Az. VIII ZR 287/23 — Schonfristzahlung nach § 569 Abs. 3 Nr. 2 BGB heilt nur die fristlose, nicht die ordentliche Kuendigung wegen Zahlungsverzugs. Klarstellung des Streits mit dem LG Berlin II. Folge: Doppelkuendigung (fristlos hilfsweise ordentlich) bleibt die strategisch sichere Loesung für den Vermieter. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=09.07.2025&Aktenzeichen=VIII+ZR+287/23
- BGH, Urt. v. 01.07.2020 – Az. VIII ZR 323/18 — Schonfristzahlung (§ 569 Abs. 3 Nr. 2 BGB) beseitigt nur die fristlose Kuendigung wegen Zahlungsverzugs; eine hilfsweise erklaerte ordentliche Kuendigung nach § 573 Abs. 2 Nr. 1 BGB bleibt wirksam. Ein Ausschluss der Sozialklausel § 574 Abs. 1 Satz 2 BGB greift, weil ein Grund vorliegt, der den Vermieter zur fristlosen Kuendigung berechtigt hätte. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=01.07.2020&Aktenzeichen=VIII+ZR+323/18
- BGH, Beschl. v. 08.12.2021 – Az. VIII ZR 32/20 — Erheblichkeit des Mietrueckstands im Sinne von § 573 Abs. 2 Nr. 1 BGB; massgeblich ist die Gesamthoehe des Rueckstands, nicht die Aufgliederung in einzelne Monatsbetraege. Bestaetigt die Wertungslinie zur ordentlichen Kuendigung neben der fristlosen. Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=08.12.2021&Aktenzeichen=VIII+ZR+32/20
- Weitere Rechtsprechungslinien des VIII. ZS zu § 543, § 569 BGB vor Ausgabe über https://www.bundesgerichtshof.de und https://dejure.org verifizieren.

## Basiszinssatz § 247 BGB und Verzug

- Basiszinssatz zum 01.01.2026: 1,27 Prozent (Bundesbank-Bekanntmachung); B2C-Verzugszinssatz 6,27 Prozent. Quelle: https://www.bundesbank.de/de/presse/pressenotizen/bekanntgabe-des-basiszinssatzes-zum-1-januar-2026-basiszinssatz-bleibt-unveraendert-bei-1-27--973974
- Halbjaehrliche Prüfung am 01.01. und 01.07. erforderlich.

## Paragrafenkette

§§ 543, 569, 573 BGB — Kuendigungsvoraussetzungen Zahlungsverzug; § 286 BGB — Verzug; § 569 Abs. 3 BGB — Schonfrist; § 247 BGB — Basiszinssatz; § 288 BGB — Verzugszinsen.

---

## Skill: `mieteranfragen-beantworten`

_Vermieter- und Hausverwaltungssicht — beantworte Mieteranfragen sachlich und ehrlich. Deckt typische Themen ab (Mietminderung Mangelanzeige Modernisierungsankündigung Schoenheitsreparaturen Hausordnung Kaution Eigenbedarfskündigung Belegeinsicht zur Nebenkostenabrechnung). Anweisung — nicht abwim..._

# Mieteranfragen beantworten (Vermieter / Hausverwaltung)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mieteranfragen beantworten (Vermieter / Hausverwaltung)` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Grundprinzip

**Ehrlich antworten, nicht abwimmeln.** Mieter haben Anspruch auf sachliche Information zur Rechtslage. Verschleierung, Verzoegerung oder pauschale Ablehnung erhöht das Streitrisiko und schaedigt die Reputation der Hausverwaltung.

## Disclaimer (Schlüsselstelle)

Liefert Textbausteine und rechtliche Hinweise. Bei substanziellen Streitfällen, insbesondere bei Mietminderung über zehn Prozent, Kündigung oder Klageandrohung des Mieters, ist eine anwaltliche Prüfung dringend zu empfehlen.

## Typische Anfragen und Antwortlinien

### Mangelanzeige und Mietminderung (§§ 535 Abs. 1, 536 BGB)

- Mangelanzeige bestätigen, Termin zur Besichtigung anbieten.
- Mangel feststellen und Behebung organisieren.
- Mietminderung **kraft Gesetzes** ab Eintritt des Mangels — nicht "genehmigen". Höhe wird im Einzelfall bestimmt.
- Bei unklarer Höhe: Bitte um Hinterlegung des strittigen Betrags oder Zahlung unter Vorbehalt.

### Modernisierungsankündigung (§ 555c BGB)

- Mindestens drei Monate vor Beginn anzeigen.
- Art und Umfang, voraussichtlicher Beginn und Dauer, voraussichtliche Mieterhöhung mitteilen.
- Hinweis auf Sonderkündigungsrecht (§ 555e BGB).

### Schönheitsreparaturen

- Klauseln im Mietvertrag prüfen. Viele ältere Klauseln sind nach BGH unwirksam.
- Bei unwirksamer Klausel: keine Schönheitsreparaturen schulden, kein Abzug von der Kaution.

### Kaution (§ 551 BGB)

- Höhe maximal drei Nettokaltmieten.
- Getrennt vom Vermögen des Vermieters anzulegen.
- Rückzahlung nach Abrechnung aller Forderungen, Frist nach Treu und Glauben in der Regel drei bis sechs Monate.

### Eigenbedarfskündigung (§ 573 Abs. 2 Nr. 2 BGB)

- Berechtigtes Interesse erforderlich (Eigennutzung für sich, Familienangehörige oder Angehörige des Haushalts).
- Begründung im Kündigungsschreiben (§ 573 Abs. 3 BGB) — konkret, nicht pauschal.
- Kündigungssperrfristen nach Landesverordnung beachten (siehe `references/mietspiegel-quellen.md`).

### Belegeinsicht zur Nebenkostenabrechnung (§ 259 BGB, § 556 Abs. 4 BGB)

- Recht des Mieters bestätigen.
- Termin in den Geschäftsräumen anbieten oder Kopien gegen Erstattung übersenden.

## Antwortstil

- Sachliche Anrede, namentlich.
- Bezugnahme auf das konkrete Schreiben und Datum.
- Rechtsgrundlage benennen.
- Lösungsschritt mit Termin oder Frist.
- Höflichkeitsformel zum Schluss.
- **Disclaimer am Ende** der Antwort, falls rechtlich strittig: Hinweis, dass Mieter sich beraten lassen kann (Mieterverein, Anwalt).

## Aktuelle Rechtsprechung — Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `mieterhoehung-widersprechen`

_Mietersicht — prüfe ein Mieterhoehungsverlangen nach ortsueblicher Vergleichsmiete (§§ 558 ff. BGB) auf Form Frist Kappungsgrenze Begründung und entwirf bei Bedarf eine Zustimmungsverweigerung oder Teilzustimmung. Prüfroutine deckt Textform Wartefrist Kappungsgrenze (zwanzig Prozent oder fuenfzeh..._

# Mieterhöhung prüfen und widersprechen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mieterhöhung prüfen und widersprechen` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Disclaimer (Schlüsselstelle)

Diese Prüfung und der nachstehende Entwurf ersetzen **keine Rechtsberatung**. Vor Versand des Schreibens an den Vermieter ist eine anwaltliche oder mietervereinsseitige Kontrolle dringend zu empfehlen. Fristversäumnisse führen zu gesetzlicher Zustimmung nach § 558b Abs. 2 BGB.

## Workflow

### Schritt 1 — Daten beschaffen

- Mieterhöhungsverlangen im Wortlaut.
- Datum des Zugangs (Briefkasten-Eintrag, E-Mail-Empfang).
- Lage- und Ausstattungsprotokoll aus dem Skill `lage-und-ausstattung-erheben`.
- Auszug aus dem aktuellen amtlichen Mietspiegel der Stadt aus `references/mietspiegel-quellen.md`.

### Schritt 2 — Formprüfung

- **Textform** nach § 558a Abs. 1 BGB (Brief, Fax, E-Mail mit Unterschriftstext genügen).
- **Empfängerangabe** alle Mieter namentlich.
- **Begründung** auf Mietspiegel, Sachverständigengutachten oder drei Vergleichswohnungen gestützt (§ 558a Abs. 2 BGB).
- **Beilage** falls Mietspiegelauszug, dann gut lesbar.

### Schritt 3 — Wartefrist und Sperrjahr

- Die neue Miete darf frühestens **fünfzehn Monate** nach Einzug oder nach der letzten Erhöhung verlangt werden (§ 558 Abs. 1 BGB).
- Berechnung dokumentieren.

### Schritt 4 — Kappungsgrenze (§ 558 Abs. 3 BGB)

- Regelgrenze **zwanzig Prozent** in drei Jahren.
- In Gebieten der Kappungsgrenzenverordnung **fünfzehn Prozent** in drei Jahren — Prüfung anhand der Landesverordnung (siehe `references/mietspiegel-quellen.md`).

### Schritt 5 — Materielle Prüfung der ortsüblichen Vergleichsmiete

- Wohnlage einordnen.
- Spanne im qualifizierten Mietspiegel suchen.
- Einordnung innerhalb der Spanne nach Orientierungshilfe (Auf- und Abschlaege für Ausstattungsmerkmale).
- Vergleichsmiete je m² ermitteln, mit Wohnfläche multiplizieren.

### Schritt 6 — Reaktionsfristen

- **Zustimmungsfrist** § 558b Abs. 2 BGB. Ablauf des zweiten Kalendermonats nach Zugang.
- Bei Schweigen: Vermieter kann auf Zustimmung klagen (§ 558b Abs. 2 Satz 2 BGB).

### Schritt 7 — Entwurfsoptionen

- **Volle Zustimmung** wenn Begehren formal und materiell richtig ist.
- **Teilzustimmung** bis zur tatsächlich ortsüblichen Vergleichsmiete.
- **Verweigerung** bei Formfehlern, Verstoß gegen Wartefrist oder Kappungsgrenze.

## Schreiben-Entwurf

Erzeuge ein höflich-bestimmtes Schreiben mit:

1. Bezugnahme auf das Verlangen vom (Datum).
2. Rechtliche Prüfung punktweise (Form, Frist, Kappungsgrenze, ortsübliche Vergleichsmiete).
3. Eindeutige Erklärung (Zustimmung, Teilzustimmung, Verweigerung).
4. Aufforderung zur schriftlichen Bestätigung.
5. **Disclaimer am Ende** — Hinweis, dass dies kein anwaltliches Schreiben ist und der Mieter sich beraten lassen sollte.

## Aktuelle Rechtsprechung — Leitsaetze (Stand 05/2026, verifiziert dejure.org)

- **BGH 28.04.2021, VIII ZR 22/20**: Qualifizierter Mietspiegel (§ 558d BGB) — Anforderungen an wissenschaftliche Erstellung; Vermutungswirkung nur bei substantiierter Erschuetterung des Erstellungsverfahrens (z. B. methodische Maengel) entkraeftbar. Quelle: dejure.org/2021,15412.
- **BGH 21.11.2012, VIII ZR 46/12**: Wirksamkeit des Mieterhoehungsverlangens; Mietspiegelauszug muss beigefuegt sein, wenn das Verlangen darauf gestuetzt wird; sonst formal unwirksam. Quelle: dejure.org/2012,38221.
- **BGH 18.10.2017, VIII ZR 28/17**: Mieterhoehung auf Grundlage Sachverstaendigengutachten — Gutachten muss konkrete Vergleichswohnungen heranziehen, nicht nur Pauschalmietspiegel-Daten. Quelle: dejure.org/2017,40850.
- **BVerfG 25.03.2021, 2 BvF 1/20** (Berliner Mietendeckel-Beschluss): Landesrechtlicher Mietendeckel verfassungswidrig (Bundesrecht abschliessend; §§ 556d ff. BGB Bundeskompetenz). Quelle: bundesverfassungsgericht.de / dejure.org/2021,7050.
- **Gesetzeslage 2026:** Mietpreisbremse § 556d BGB durch Bundesgesetzgeber verlaengert; konkrete Geltungsdauer und Spannungs-Gebiets-Verordnungen der Länder vor Versand prüfen.

Vor Zitieren weiterer Aktenzeichen Live-Verifikation per dejure.org / bundesgerichtshof.de.

## Paragrafenkette

§§ 558, 558a, 558b, 558c, 558d BGB

---

## Skill: `mieterhoehungsverlangen-erstellen`

_Vermietersicht — verfasse ein Mieterhoehungsverlangen auf ortsuebliche Vergleichsmiete (§ 558a BGB) in Textform mit ordnungsgemäßer Begründung (Mietspiegel Sachverständigengutachten oder drei Vergleichswohnungen). Prüfroutine deckt Textform Wartefrist (fuenfzehn Monate seit Einzug oder letzter Er..._

# Mieterhöhungsverlangen erstellen (Vermieter / Hausverwaltung)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mieterhöhungsverlangen erstellen (Vermieter / Hausverwaltung)` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Disclaimer (Schlüsselstelle)

Ein formal oder materiell fehlerhaftes Mieterhöhungsverlangen ist unwirksam — der Mieter darf zustimmen verweigern. Wer die Wartefrist oder die Kappungsgrenze verletzt verliert das Verlangen ganz. Vor Versand großer Mieterhöhungen oder bei zweifelhafter Mietspiegel-Einordnung ist eine fachanwaltliche Prüfung dringend empfohlen.

## Workflow

### Schritt 1 — Daten zusammenstellen

- Aktueller Mietvertrag mit Vertragsdatum.
- Bisherige Nettokaltmiete und Datum der letzten Erhöhung.
- Lage- und Ausstattungsprotokoll aus dem Skill `lage-und-ausstattung-erheben`.
- Auszug aus dem aktuellen amtlichen Mietspiegel der Stadt aus `references/mietspiegel-quellen.md`.
- Bei Begründung durch Vergleichswohnungen: drei konkrete Wohnungen mit Adresse Ausstattung und Höhe der Miete.

### Schritt 2 — Wartefrist (§ 558 Abs. 1 BGB)

- Die neue Miete darf frühestens **fünfzehn Monate** nach Einzug oder nach Wirksamwerden der letzten Erhöhung verlangt werden.
- Berechnung dokumentieren — sonst Risiko der Unwirksamkeit.

### Schritt 3 — Kappungsgrenze (§ 558 Abs. 3 BGB)

- Regelgrenze **zwanzig Prozent** in drei Jahren.
- In Gebieten der Kappungsgrenzenverordnung **fünfzehn Prozent** in drei Jahren (siehe `references/mietspiegel-quellen.md`).
- Berechnung der gesamten Erhöhung gegenüber der vor drei Jahren geschuldeten Miete dokumentieren.

### Schritt 4 — Materielle Begründung

- Ortsübliche Vergleichsmiete aus dem qualifizierten Mietspiegel ermitteln (Spanne + Orientierungshilfe).
- Einordnung der konkreten Wohnung innerhalb der Spanne nachvollziehbar darstellen.
- Wenn kein qualifizierter Mietspiegel vorliegt: einfacher Mietspiegel Sachverständigengutachten oder drei Vergleichswohnungen.

### Schritt 5 — Formale Anforderungen (§ 558a BGB)

- **Textform** ausreichend (Brief Fax E-Mail mit Unterschriftstext).
- **Adressierung** alle im Mietvertrag genannten Mieter namentlich.
- **Erklärung** der Vermieter verlangt Zustimmung zur Erhöhung auf einen konkreten neuen Betrag ab einem konkreten Termin.
- **Begründung** mit Verweis auf Mietspiegel Gutachten oder Vergleichswohnungen.
- **Beilagen** Mietspiegelauszug gut lesbar oder Gutachten als Kopie oder Vergleichswohnungen-Aufstellung.

### Schritt 6 — Wirkungszeitpunkt und Zustimmungsfrist

- Wirksame Erhöhung erfolgt erst mit **Beginn des dritten Kalendermonats nach Zugang** des Verlangens (§ 558b Abs. 1 BGB).
- Mieter hat **Zustimmungsfrist** bis zum Ablauf des zweiten Kalendermonats nach Zugang (§ 558b Abs. 2 BGB).
- Bei Schweigen oder Verweigerung kann Klage auf Zustimmung erhoben werden — Klagefrist drei Monate nach Ablauf der Zustimmungsfrist.

### Schritt 7 — Prüfroutine vor Versand

- Wartefrist fünfzehn Monate erfüllt.
- Kappungsgrenze eingehalten.
- Mietspiegel oder Gutachten oder drei Vergleichswohnungen als Begründung beigefügt.
- Alle Mieter namentlich adressiert.
- Wirksamkeitstermin korrekt berechnet (Beginn des dritten Kalendermonats nach Zugang).
- Bei Mietpreisbremse-Gebiet prüfen ob die neue Miete nach Erhöhung noch innerhalb der Vergleichsmiete plus zehn Prozent liegt.

## Schreiben-Entwurf

Erzeuge ein Schreiben mit:

1. Adresse aller Mieter namentlich.
2. Bezugnahme auf den Mietvertrag (Datum Mietsache).
3. Bisherige Miete und neue Miete in Euro mit Wirksamkeitstermin.
4. Begründung mit Bezug auf den amtlichen Mietspiegel (Stadt Jahr Spaltennummer) oder Gutachten oder Vergleichswohnungen.
5. Berechnung der ortsüblichen Vergleichsmiete und Einordnung der konkreten Wohnung.
6. Nachweis Wartefrist und Kappungsgrenze.
7. Hinweis auf Zustimmungsfrist nach § 558b Abs. 2 BGB.
8. **Disclaimer** — Hinweis dass dies ein Vermieter-Verlangen ist und der Mieter sich beraten lassen kann.

## Hinweis zur Mietpreisbremse

In Gebieten mit Mietpreisbremse darf eine Erhöhung bei bestehendem Mietverhältnis grundsätzlich erfolgen — die Mietpreisbremse begrenzt nur die Neuvermietung. Aber: bei Neuvermietung ist eine Miete über ortsübliche Vergleichsmiete plus zehn Prozent unzulässig (§ 556d BGB). Bei Folgeerhöhungen im laufenden Verhältnis gilt nur die Kappungsgrenze.

## Aktuelle Rechtsprechung — Leitsaetze (Stand 05/2026, verifiziert dejure.org)

- **Berliner Mietendeckel nicht als BGH-Mietrecht zitieren:** Die Kompetenzfrage wurde durch BVerfG, Beschluss vom 25.03.2021 - 2 BvF 1/20, entschieden. Für Mietpreisbremse/Rückzahlung nach §§ 556d ff. BGB immer eine gesondert verifizierte BGH-Entscheidung mit Datum und Aktenzeichen heranziehen.
- **BVerfG 25.03.2021, 2 BvF 1/20, 2 BvL 4/20, 2 BvL 5/20** (Berliner Mietendeckel-Beschluss): Landesrechtlicher Mietendeckel (Berlin) ist mangels Gesetzgebungskompetenz des Landes verfassungswidrig (Bundesrecht abschliessend). Quelle: bundesverfassungsgericht.de / dejure.org/2021,7050.
- **BGH 28.04.2021, VIII ZR 22/20**: Qualifizierter Mietspiegel — Anforderungen an wissenschaftliche Erstellung; Erschuetterung der Vermutungswirkung nur bei substantiierten Maengeln des Mietspiegel-Erstellungsverfahrens. Quelle: dejure.org/2021,15412.
- **BGH 18.03.2020, VIII ZR 64/19** (Bauwerksmaengel als Mietminderungsgrund — vor Mieterhoehungsausgleich prüfen): Erhebliche Maengel mindern auch die Bezugsbasis der Vergleichsmiete. Quelle: dejure.org/2020,4895.
- **Gesetzeslage Mai 2026:** Bei Erstellung Stand der Mietpreisbremsen-Verordnungen der Länder prüfen; Kappungsgrenzenverordnungen je Bundesland; § 556d BGB-Verlaengerung durch Bundesgesetzgeber (Beschluss 2025 — vor Ausgabe Bundesgesetzblatt-Verifikation).

Vor Zitieren weiterer Entscheidungen Live-Verifikation per dejure.org / bundesgerichtshof.de mit Datum und Aktenzeichen.

## Paragrafenkette

§§ 558, 558a, 558b BGB — Begruendungsmittel, Wartefrist, Kappungsgrenze

---

## Skill: `mietsenkungsverlangen`

_Mietersicht — prüfe eine laufende oder bei Vertragsschluss vereinbarte Miete auf Verstoß gegen die Mietpreisbremse (§§ 556d ff. BGB), § 5 WiStrG 1954 (Mietpreisüberhöhung als Ordnungswidrigkeit) und § 291 StGB (Mietwucher als Straftat). Erzeugt eine qualifizierte Rüge nach § 556g Abs. 2 BGB mit B..._

# Mietsenkungsverlangen (Mietpreisbremse, WiStrG 1954, Wucher)

## Arbeitsbereich

Mietersicht — prüfe eine laufende oder bei Vertragsschluss vereinbarte Miete auf Verstoß gegen die Mietpreisbremse (§§ 556d ff. BGB), § 5 WiStrG 1954 (Mietpreisüberhöhung als Ordnungswidrigkeit) und § 291 StGB (Mietwucher als Straftat). Erzeugt eine qualifizierte Rüge nach § 556g Abs. 2 BGB mit Berechnung der zulässigen Miete, Bezugnahme auf den amtlichen Mietspiegel und Aufforderung zur Rückzahlung. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: nur die Fristen des konkreten Rechtsgebiets und der Akte verwenden; Widerspruch, Klage, Einspruch, Rechtsmittel, Verjährung, Verwirkung, Rüge-, Anzeige-, Anmelde- und Ausschlussfristen strikt trennen und nie aus einem anderen Fachgebiet übernehmen.
- Tragende Normen verifizieren: BGB §§ 535-577a, BetrKV, WEG §§ 24, 25, 27, BGB §§ 558, 558a, 558b, 573, 573c — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Miet- und WEG-Recht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mietsenkungsverlangen (Mietpreisbremse, WiStrG 1954, Wucher)` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** BGB §§ 535 ff., 536, 543, 546a, 548, 556, 556a, 558 ff., 573 ff.; BetrKV; HeizkostenV; WEG §§ 18, 19, 20, 23, 24, 28, 44, 45; GEG; CO2KostAufG.
- **Verifizierte Anker:** BGH, Urteil vom 20.01.2016 - VIII ZR 93/15 (formelle Betriebskostenabrechnung); BGH, Urteil vom 15.12.2021 - VIII ZR 66/20 (Belegeinsicht Originale/Kopien); BGH, Urteil vom 14.02.2025 - V ZR 128/23 (§ 16 Abs. 2 Satz 2 WEG, Rücklagen/Kostenverteilung); BGH, Urteil vom 14.02.2025 - V ZR 86/24 (§ 20 WEG, bauliche Veränderung, Vorbefassung/Beschlussersetzung).
- **Arbeitsmodus:** Immer erst Verhältnis Miete/WEG/Gewerbe/Verwaltung trennen, dann Frist, Beschlusskompetenz, Umlagefähigkeit, Belege, Gebrauchsnachteil und Kostenfolge prüfen.
- **Outputpflicht:** Abrechnungsprüftabelle, Beschlussvorschlag, Anfechtungs-/Beschlussersetzungsskizze, Mietermail, Vermieterschreiben oder Verwalter-To-do-Liste.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Disclaimer (Schlüsselstelle)

Mietsenkungsverlangen sind streitanfällig. Die Mietpreisbremse gilt nur in Gebieten mit Landesverordnung (§ 556d Abs. 2 BGB). Vor Versand der qualifizierten Ruege eine anwaltliche oder mietervereinsseitige Prüfung einholen. Fehlerhafte Ruegen können Anspruechen entgegengehalten werden.

## Workflow

### Schritt 1 — Anwendbarkeit der Mietpreisbremse

- Vertragsschluss **nach dem 1. Juni 2015** (§ 556d BGB ist seit dem 1. Juni 2015 in Kraft).
- Wohnung liegt in einem Gebiet mit Landesverordnung nach § 556d Abs. 2 BGB — Prüfung anhand `references/mietspiegel-quellen.md`.
- Verordnung zum Zeitpunkt des Vertragsschlusses gültig.

### Schritt 2 — Ausnahmen prüfen (§§ 556e und 556f BGB)

- **Vormiete** wenn höher, darf weitergegeben werden (§ 556e Abs. 1 BGB).
- **Modernisierung** nach § 556e Abs. 2 BGB.
- **Neubau** Erstbezug nach dem 1. Oktober 2014 ausgenommen (§ 556f Satz 1 BGB).
- **Umfassende Modernisierung** nach § 556f Satz 2 BGB ausgenommen.

### Schritt 3 — Zulässige Miete berechnen

- Ortsübliche Vergleichsmiete nach Mietspiegel ermitteln (Spanne, Einordnung).
- Zulässig: ortsübliche Vergleichsmiete plus **zehn Prozent** (§ 556d Abs. 1 BGB).
- Differenz zur tatsächlich gezahlten Miete berechnen.

### Schritt 4 — Qualifizierte Ruege (§ 556g Abs. 2 BGB)

- **Textform** ausreichend.
- **Tatsachen** angeben, auf denen die Beanstandung beruht (Mietspiegelwerte, Wohnlage, Ausstattung).
- **Rückforderung** erst ab Zugang der Ruege (§ 556g Abs. 1 Satz 3 BGB) — auf zu viel gezahlte Miete.

### Schritt 5 — Auskunftsanspruch (§ 556g Abs. 3 BGB)

- Mieter kann vom Vermieter Auskunft verlangen über Tatsachen, die für die Ausnahmen nach §§ 556e und 556f BGB massgebend sind.

### Schritt 6 — Mietpreisüberhöhung (§ 5 WiStrG 1954)

- **Mehr als 20 Prozent** über den üblichen Entgelten für vergleichbare Wohnräume bei **Ausnutzung eines geringen Angebots** (§ 5 Abs. 2 WiStrG 1954).
- Ordnungswidrigkeit, keine Straftat; Bußgeld bis 50.000 Euro (§ 5 Abs. 3 WiStrG 1954).
- Zusätzlich § 8 WiStrG 1954 prüfen: Abführung des Mehrerlöses an das Land, soweit nicht aufgrund rechtlicher Verpflichtung zurückerstattet wurde.

### Schritt 7 — Wucher (§ 291 StGB)

- **Auffälliges Missverhältnis** Miete zu Leistung **plus** Ausbeutung einer Zwangslage, Unerfahrenheit, Mangel an Urteilsvermögen oder erheblicher Willensschwaeche.
- Straftatbestand — Anzeige möglich, aber nur bei individueller Schwächesituation und vorsätzlicher Ausbeutung; bloß angespannter Wohnungsmarkt reicht dafür nicht.

## Schreiben-Entwurf

Strukturiere die Ruege in Abschnitte:

1. Bezeichnung als qualifizierte Ruege nach § 556g Abs. 2 BGB.
2. Sachverhalt (Mietvertrag, Mietsache, Datum, Höhe der Miete).
3. Gebiet der Mietpreisbremse mit Verordnung (Link).
4. Berechnung der ortsüblichen Vergleichsmiete mit Mietspiegelauszug.
5. Berechnung der zulässigen Miete (plus zehn Prozent).
6. Beanstandeter Mehrbetrag und Aufforderung zur Senkung sowie Rückzahlung ab Zugang.
7. Hilfsweise Hinweise auf § 5 WiStrG 1954 und § 291 StGB falls einschlägig.
8. **Disclaimer am Ende** — kein anwaltliches Schreiben, Empfehlung Rechtsrat einzuholen.

## Aktuelle Rechtsprechung — Leitsaetze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette

§§ 556d, 556e, 556f, 556g BGB — Mietpreisbremse und Rüge; § 5 WiStrG 1954 — Mietpreisüberhöhung; § 8 WiStrG 1954 — Abführung des Mehrerlöses; § 291 StGB — Wucher.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

