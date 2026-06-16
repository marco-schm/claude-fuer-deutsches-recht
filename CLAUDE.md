# CLAUDE.md – Repository-Leitfaden für das Modell

Dieses Repository enthält Plugins für deutsche Kanzleien. Wenn du in diesem Repository arbeitest oder hieraus Skills lädst, halte dich an die folgenden Regeln.

## Sprache

- **Alle Ausgaben auf Deutsch.** Englische Begriffe nur, wenn etabliert (z. B. "Letter of Intent", "Term Sheet", "Due Diligence", "Discovery") – aber stets erklärt.
- Du-Form gegenüber Mandanten nur, wenn ausdrücklich vom Mandat vorgegeben; sonst Sie-Form.
- Behördensprache nüchtern, klar, prägnant.

## Methodik

- Standard ist der **Gutachtenstil** für interne Memos und Mandantenbriefe mit Begründungsanspruch.
- **Urteilsstil** für Schriftsätze, Beschlüsse, knappe Vermerke.
- Anspruchsgrundlagenprüfung in der Reihenfolge: Vertrag – c.i.c. – GoA – dinglich – Delikt – Bereicherung.
- Auslegung nach den vier klassischen Methoden (grammatikalisch, systematisch, historisch, teleologisch) zzgl. verfassungs- und unionsrechtskonformer Auslegung.
- Siehe [`references/methodik-buergerliches-recht.md`](./references/methodik-buergerliches-recht.md).

## Quellen und Zitierweise

- **Verbindlich:** [`references/zitierweise.md`](./references/zitierweise.md).
- Jede juristische Aussage wird belegt.
- Rechtsprechung: Gericht, Entscheidungsform, Datum, Aktenzeichen, Fundstelle, Randnummer.
- Kommentare: Bearbeiter, "in:" Kommentar, Auflage, Jahr (ggf. Stand), Norm, Randnummer.
- Aufsätze: Autor, Zeitschrift, Jahrgang, Anfangsseite (konkrete Seite).
- Reihenfolge: Rspr. vor Lit., neueste zuerst.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- **Leitentscheidungs-Anker:** [`references/leitentscheidungen-anker.md`](./references/leitentscheidungen-anker.md) ist die kuratierte Themen-Anker-Liste je Rechtsgebiet. Sie ersetzt nicht die Live-Verifikation, aber sie liefert sichere Sucheinstiege ohne Modellwissens-Halluzination.

## Gliederung und Nummerierung (verbindlich für alle Vorlagen und Verträge)

Diese Regel gilt **dauerhaft und für jedes Werkzeug**, das in diesem Repository arbeitet – Claude, Codex, Perplexity, Cloud und jedes weitere Modell. Sie ist nicht verhandelbar.

- **Ausschließlich dezimale Gliederung:** `1`, dann `1.1`, dann `1.1.1`, dann `1.1.1.1` und so weiter, beliebig tief.
- **Niemals** römische Ziffern (`I`, `II`), Großbuchstaben (`A`, `B`, `C`), Kleinbuchstaben (`a`, `b`) oder gemischte Verlags-Gliederungen (`A. I. 1. a) aa)`). Genau diese Schemata sind verboten, weil man sich darin nicht zurechtfindet.
- **Leerzeile zwischen Gliederungspunkt und seinem Inhalt sowie zwischen Gliederungsebenen.** Überschrift bzw. Nummer und der folgende Text/Unterpunkt werden durch eine Leerzeile getrennt, sonst ist es nicht lesbar.
- **Einrückung sparsam.** Nur leicht einrücken, gerade so viel, dass die Hierarchie sichtbar bleibt und es gut aussieht – nie so tief, dass das Dokument zerfleddert wirkt.

Gilt für alle Vorlagen, Verträge, Memos, Schriftsätze und sonstigen Dokumente in diesem Repository.

## Verboten

- Präjudizienbindungs-Argumente. In Deutschland gibt es keine Präjudizienbindung (außer § 31 BVerfGG).
- Vorprozessuale Beweiserhebung im deutschen Recht ist auf eng begrenzte gesetzliche Instrumente beschränkt: §§ 142, 144, 421–432 ZPO, § 810 BGB, § 242 BGB, Art. 15 DSGVO, Auskunfts- und Stufenklage (§ 254 ZPO).
- Halluzinierte Aktenzeichen oder Fundstellen. Bei Unsicherheit: kennzeichnen und Verifizierung in amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang empfehlen.
- Mandantengeheimnis-Verletzung (§ 43a Abs. 2 BRAO, § 203 StGB). Mandantendaten nur in Tools mit AVV.

## Standardstruktur für Memos

1. Sachverhalt (knapp)
2. Frage(n)
3. Kurzantwort (1 Satz)
4. Rechtliche Bewertung (Gutachtenstil)
5. Gesamtergebnis
6. Risiken / offene Punkte
7. Quellenverzeichnis (gem. references/zitierweise.md)

## Standardstruktur für Mandantenkommunikation

- Anrede + Bezug ("In dem Mandat … / In Sachen …")
- Sachstand
- Empfehlung
- Nächste Schritte / Frist
- Kostenhinweis (RVG/Honorarvereinbarung)
- Unterschrift mit Berufsbezeichnung

## Gliederung und Nummerierung von Vorlagen und Verträgen (verbindlich)

Diese Regel gilt **ausnahmslos und für alle Zeiten** für jede Vorlage, jeden Vertrag, jedes Vertragsmuster und jedes formatierte Dokument in diesem Repository – unabhängig davon, welches Werkzeug es erzeugt (Claude, Perplexity, Codex oder andere).

- **Nur dezimale Nummerierung.** Gegliedert wird ausschließlich nach dem Schema `1`, dann `1.1`, dann `1.1.1`, dann `1.1.1.1` und so weiter in beliebiger Tiefe.
- **Verboten** sind römische Ziffern (`I.`, `II.`, `III.`), Großbuchstaben (`A.`, `B.`, `C.`), Kleinbuchstaben als Gliederungsebene (`a)`, `b)`) und jede gemischte Verlagsgliederung (`§ 1 I. 1. a) aa)`), wie sie viele deutsch-juristische Verlage verwenden. Solche Schemata machen Dokumente unauffindbar und sind hier untersagt.
- **Leerzeile zwischen Gliederungspunkt und Inhalt.** Sobald ein Punkt Unterpunkte oder darunterliegenden Text hat, steht zwischen der Gliederungsüberschrift und dem folgenden Punkt/Absatz immer eine Leerzeile. Ohne Leerzeile ist das Dokument nicht lesbar.
- **Maßvoll einrücken.** Eingerückt wird nur so viel, dass die Hierarchie klar erkennbar bleibt und das Dokument sauber aussieht – nicht mehr. Übertriebene Einrückung lässt Dokumente zerfleddert wirken und ist zu vermeiden.
- Diese Regelung ist von hoher Priorität. Bei Konflikt mit einer abweichenden Gliederung in einer Altvorlage gilt diese Regel; die Altvorlage ist anzupassen.

## Ausformulierungspflicht für Verträge, Vorlagen und juristische Dokumente (verbindlich)

Diese Regel gilt **ausnahmslos und für alle Zeiten** für jedes Dokument, das ein Skill, ein Plugin oder ein anderes Werkzeug in diesem Repository als Endprodukt erzeugt — Verträge, Vertragsmuster, Klausel-Sets, Schriftsätze, Bescheide, Beschlüsse, Verfügungen, Memos, Mandantenbriefe, Vollmachten, Anschreiben, Vermerke, Stellungnahmen, NDA-Texte, AGB-Entwürfe, Vereinbarungen, Anträge, Erwiderungen und alle vergleichbaren Endprodukte — unabhängig davon, welches Werkzeug es erzeugt (Claude, Perplexity, Codex oder andere).

- **Vollständig ausformuliert.** Endprodukte werden in vollständigen, grammatikalisch sauberen Sätzen geliefert. Stichworte, Halbsätze, Aufzählungs-Skelette, leere Klauselrümpfe oder reine Informationssammlungen sind als Endprodukt **verboten**. Eine Klausel besteht aus mindestens einem vollständigen Satz, der die Rechtsfolge konkret und subsumtionstauglich anordnet.
- **Crisp und prägnant.** „Vollständig" heißt nicht „aufgebläht". Jeder Satz trägt; rhetorische Füllstücke sind zu vermeiden. Klarheit, juristische Präzision und Lesbarkeit für den Mandanten und das Gericht haben absoluten Vorrang vor Wortzahl.
- **Keine Skelett-Verträge.** Ein Endvertrag ohne Präambel, ohne Definitionen, ohne ausformulierte Hauptpflichten, ohne Leistungsstörungsrecht, ohne Schlussbestimmungen ist kein Endprodukt, sondern eine Gliederung. Solche Skelette gehören in den Skill als Zwischenergebnis, nicht in die Ausgabe an die Nutzerin.
- **Platzhalter sauber markieren.** Wo Mandantsangaben fehlen, werden klar lesbare Platzhalter gesetzt (`[Name der Mandantin]`, `[Betrag in EUR]`, `[Datum TT.MM.JJJJ]`) — nicht aber Sinnsätze weggelassen. Der umgebende Text bleibt vollständig.
- **Frage-Antwort-Phase ist Vorbereitung, nicht Endprodukt.** Die Rückfrage-Phase eines Skills dient der Erhebung fehlender Tatsachen. Sobald genug Tatsachen vorliegen, wird das Endprodukt in **ganzer Sprache** geliefert — nicht in Stichworten, die der Mandant selbst zu Sätzen ausbauen müsste.
- **Strenge Regelung bei neuen Plugins und Skills.** Jedes neu erzeugte Plugin oder Skill, das ein Endprodukt erstellt, muss diese Ausformulierungspflicht im eigenen Ausgabeformat-Block (Innenstruktur Nummer 5) ausdrücklich umsetzen. Das Skill-Werkzeug muss bei jeder Erzeugung darauf prüfen, ob das Ergebnis ausformuliert ist; bei Skelett-Charakter ist das Endprodukt zu verwerfen und in vollständiger Sprache neu zu produzieren.
- **Englisch wenn gewünscht.** Bei zweisprachigen oder englischsprachigen Vorlagen gilt sinngemäß dasselbe: writing needs to be clear, crisp and complete. Keine half-sentences, keine bullet-point-only-Klauseln, keine information-dump-Ausgaben.
- **Diese Regelung ist von hoher Priorität.** Bei Konflikt mit einer abweichenden Stilkonvention in einer Altvorlage gilt diese Regel; die Altvorlage ist beim nächsten Anfassen anzupassen.

## Skill-Konvention

- Jeder Skill liegt unter `<plugin>/skills/<skill-name>/SKILL.md`.
- Frontmatter (YAML) enthält genau `name` und `description`. Keine weiteren Felder (insbesondere kein `triggers`, `when_to_use`, `language`, `rechtsgebiet`, `license`, `argument-hint`, `user-invocable`, `allowed_tools`, `tools`, `model`, `adapted_from`, `version`, `related_skills`).
- `description` höchstens 1024 Zeichen, keine Zahlen-Kommas in `description` oder `plugin.json`-Description (z. B. statt `1,5` schreibe `1.5` oder `eineinhalb`). Skill-`name` ≤ 64 ASCII-Zeichen.
- Innenstruktur:
  1. Zweck und Anwendungsfall
  2. Eingaben
  3. Ablauf / Checkliste
  4. Quellenpflicht (Verweis auf references/zitierweise.md)
  5. Ausgabeformat — bei Skills, die Verträge, Vorlagen, Schriftsätze, Memos oder vergleichbare Endprodukte erzeugen, muss dieser Block ausdrücklich auf die **Ausformulierungspflicht** verweisen: Das Endprodukt wird in vollständigen, ausformulierten Sätzen geliefert; Skelette, Halbsätze und reine Aufzählungs-Auswurfe sind als Endprodukt verboten.
  6. Beispiele
- Skills sollen kanzleitauglich sein, also reproduzierbar und auditierbar.

## Bei Unsicherheit

- Frage nach (Skill, Mandat, Gegenstand, Frist).
- Nenne offene rechtliche Fragen explizit.
- Empfehle Verifizierung in amtliche oder frei zugängliche Quellen; lizenzierte Datenbanken nur bei vorhandenem Zugang.

## Git- und PR-Verhalten

- Pull Requests in diesem Repo werden **nicht als Draft** erstellt, sondern direkt als „ready" und nach Push **sofort auf `main` gemerged** — es sei denn, der Nutzer fordert ausdrücklich einen Draft oder eine Review-Pause.
- Merges erfolgen per Merge-Commit (kein Squash, kein Rebase), damit die Entwicklungs-History pro Branch erhalten bleibt.
- Force-Push auf `main` oder gemeinsame Branches ist verboten.
- **Codex-Review verbindlich anstoßen — nicht blockierend.** Der Workflow je PR ist exakt:
  1. PR erzeugen (`mcp__github__create_pull_request`). Standard ist `draft: false`. **`draft: true` nur dann**, wenn der Nutzer ausdrücklich einen Draft gefordert hat. Eine reine Review-Pause-Anweisung des Nutzers ändert den Draft-Status **nicht** — der PR bleibt `ready`.
  2. Direkt im Anschluss einen Kommentar mit dem Inhalt `@codex review` posten (`mcp__github__add_issue_comment`). Dieser Schritt erfolgt sofort bei jedem `ready`-PR (also auch bei Review-Pause-PRs). Bei einem echten Draft-PR wird der Kommentar erst gepostet, sobald der PR auf `ready` gesetzt wird.
  3. **Sofort** mergen (`mcp__github__merge_pull_request`, `merge_method: merge`) — **nicht** auf Codex' Antwort warten. **Ausnahme:** Bei einem vom Nutzer ausdrücklich gewünschten Draft **oder** einer Review-Pause wird hier nicht gemerged, sondern auf die Freigabe des Nutzers gewartet.

  Codex läuft im Hintergrund weiter und kommentiert später. Etwaige Findings werden — falls überhaupt nötig — in einem Folge-PR adressiert. Ziel ist eine durchgehende Audit-Spur ohne dass der Workflow blockiert wird. Diese Regel gilt für jeden PR unabhängig vom erzeugenden Werkzeug (Claude, Perplexity, Codex oder andere); die Draft- und Review-Pause-Ausnahmen aus dem ersten Punkt dieses Abschnitts bleiben unberührt.

## Konversationsstil – konzis starten, schnell zum Dokument

Ziel jedes Skills ist die **Produktion eines Dokuments oder Arbeitsergebnisses**, nicht ein langer Chat-Vortrag. Halte dich daran:

- **Erste Antwort: knapp.** Nicht mehr als nötig, um den Sachverhalt einzuordnen und – falls nötig – **eine einzige gezielte Rückfrage** zu stellen.
- **Keine vorgelagerten Theorie-Vorträge.** Keine ausführliche Norm-Wiederholung, kein Lehrbuch-Intro, keine Selbsterklärung, was der Skill jetzt gleich tun wird. Tu es direkt.
- **Sofort zur Dokumentenerzeugung übergehen,** sobald die nötigsten Eingaben vorliegen. Lieber ein erster Entwurf mit klaren "[noch zu klären: …]"-Platzhaltern als eine Rückfrage-Schleife.
- **Ausnahmen – hier darf und soll ausführlich gearbeitet werden:**
  - Echte Subsumtion / Gutachtenstil-Prüfung einer Anspruchsgrundlage.
  - Vergleichstabellen, Gegenüberstellungen, Zitatketten, Chronologien.
  - Risikoanalysen, Mehr-Szenarien-Bewertungen, Beweislastverteilungen.
  - Schriftsatz-, Bescheid- oder Memo-Texte selbst (die dürfen so lang sein wie nötig).
- **Allgemein-Skills sind Einstieg, nicht Vorlesung.** Sie führen das Mandat an, stellen maximal die unverzichtbaren Mandatsfragen, verweisen auf die spezialisierten Skills im selben Plugin und liefern bei klarer Faktenlage sofort den ersten Dokumentenentwurf.
- **Erklären, wenn der Nutzer es verlangt.** Wenn der Nutzer ausdrücklich nach Hintergrund, Begründung oder Methodik fragt, dann ausführlich und im Gutachtenstil – sonst nicht.
