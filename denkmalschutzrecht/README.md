# Denkmalschutzrecht — Bundesweiter Rahmen und sechzehn Landesgesetze


<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`denkmalschutzrecht`) | [`denkmalschutzrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/denkmalschutzrecht.zip) |
| **Alle Skills als Markdown** | [`denkmalschutzrecht-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/denkmalschutzrecht-skills-markdown.zip) |
| **Unified Mini Prompt** (Sparversion bis 7.500 Zeichen) | [`denkmalschutzrecht-unified-mini-prompt.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/denkmalschutzrecht-unified-mini-prompt.md) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

Plugin für die anwaltliche Bearbeitung von Mandaten im deutschen Denkmalschutzrecht. Strukturiert in drei Schichten:

1. **Allgemeiner Teil** — bundesstaatlicher Rahmen (Art. 73 GG, Art. 14 GG, Verwaltungsverfahrensrecht, Welterbe).
2. **Querschnittsskills** — Denkmaleigenschaft, Eintragung, Erlaubnis, Förderung, Enteignung und Entschädigung; sie greifen unabhängig vom Bundesland.
3. **Sechzehn Bundesländer-Skills** — je ein eigener Skill pro Landesgesetz, mit Gesetzesbezeichnung, zuständigen Behörden und den landestypischen Verfahrensbesonderheiten.

## Aufbau und Anwendung

Die Allgemein-Skills helfen, einen Fall zu sortieren und ihn vom GG- und EU-Rahmen aus zu erden. Sobald klar ist, in welchem Bundesland das Objekt belegen ist, wird der landesspezifische Skill (`denkmalschutz-<bundesland>-<gesetzkuerzel>`) zugeschaltet — er enthält die konkreten Norm-Anker des jeweiligen Landesgesetzes und die zuständige Behördenkette.

## Quellenhygiene

Konkrete Paragrafenzitate, Aktenzeichen und Fundstellen werden ausnahmslos in den amtlichen Landesgesetzes-Datenbanken (typischerweise unter `landesrecht.<land>.de` oder `gesetze-im-internet.de` für Bundesrecht) live verifiziert; das Plugin nennt die Gesetzesabkürzungen und das verbindliche Suchregime, nicht aber halluzinierte Randnummern oder Fundstellen aus Modellwissen.

## Sicherheitsabstand

Denkmalschutzrecht ist Landesrecht. Bei jedem Mandat ist als allererstes das anwendbare Landesgesetz zu identifizieren — danach erst die einschlägigen Paragrafen prüfen. Skills, die einen Sachverhalt ohne Belegenheit beurteilen, sind unzulässig.

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Unified Mini Prompt und Mega-Prompt

Für normale Chatbots ohne Plugin-Installation gibt es den **Unified Mini Prompt**: eine einzelne Markdown-Datei bis 7.500 Zeichen, die den Kern-Workflow dieses Plugins verdichtet und als Release-Asset direkt herunterladbar ist.

- **Sparversion herunterladen:** [`denkmalschutzrecht-unified-mini-prompt.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/denkmalschutzrecht-unified-mini-prompt.md)
- **Großer Mega-Prompt nur zur Anschauung im Repo:** [`testakten/megaprompts/denkmalschutzrecht.md`](../testakten/megaprompts/denkmalschutzrecht.md) (55 KB)

Der große Mega-Prompt wird nicht als installierbares Plugin und nicht als CoWork-Uploadmaterial ausgeliefert. Für echte Plugin-Nutzung bitte das Plugin-ZIP verwenden; für Ein-Datei-Nutzung den Unified Mini Prompt.

<!-- END megaprompt-und-vorlagen (autogen) -->
