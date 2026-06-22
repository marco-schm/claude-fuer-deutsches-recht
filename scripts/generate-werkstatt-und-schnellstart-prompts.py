#!/usr/bin/env python3
"""Erzeugt pro Plugin zwei sprechend benannte Markdown-Prompts.

Die Dateien liegen direkt im jeweiligen Plugin-Ordner:

* <sprechender-name>-werkstatt.md
* <sprechender-name>-schnellstart.md

Sie sind reine Markdown-Arbeitsanweisungen fuer Nutzer ohne Plugin-Setup.
Inhalte werden aus plugin.json, README.md und den vorhandenen SKILL.md-Dateien
verdichtet. Alte plugin-lokale Mega-/Mini-Dateien werden entfernt, sobald die
neuen Dateien erzeugt sind.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
MAX_SCHNELLSTART = 7500

OLD_LOCAL_PROMPT_NAMES = {
    "MEGAPROMPT.md",
    "MINIPROMPT.md",
}

PRIORITY_RE = re.compile(
    r"(einstieg|kaltstart|triage|routing|workflow|mandat|erstpruefung|erstprüfung|"
    r"frist|risiko|checkliste|strategie|akte|gericht|verfuegung|verfügung|tenor|"
    r"klage|vertrag|antrag|widerspruch|beschwerde)",
    re.IGNORECASE,
)

DECISION_RE = re.compile(
    r"\b(?:BVerfG|BVerfGE|BGH|BAG|BSG|BFH|BVerwG|EuGH|OLG|OVG|VGH|KG|LG|AG|FG|SG|LSG)\b[^.\n]{0,180}"
    r"(?:\d{1,2}\.\d{1,2}\.\d{4}|[A-Z]?\s?\d+\s?[A-Z][A-Za-z]*\s?\d+/\d+|C-\d+/\d+)[^.\n]{0,160}"
)

NORM_RE = re.compile(
    r"(?:Paragraf(?:en)?\s+[\w\d\s.,AbsSatzNrBuchstabeundbis/-]+(?:BGB|ZPO|StPO|VwGO|FGO|SGG|ArbGG|"
    r"FamFG|GVG|GmbHG|AktG|InsO|StaRUG|HGB|AO|EStG|UStG|KStG|GewStG|GG|BDSG|DSGVO|OWiG|StGB|"
    r"SGB\s+[IVX]+)|Artikel\s+[\w\d\s.,AbsSatzNrBuchstabeundbis/-]+(?:GG|DSGVO|KI-VO|AEUV|GRCh))",
    re.IGNORECASE,
)


@dataclass
class Skill:
    slug: str
    description: str
    body: str
    score: int


def load_marketplace() -> list[dict]:
    data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    return list(data.get("plugins", []))


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def strip_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text.strip()
    match = re.match(r"---\s*\n([\s\S]*?)\n---\s*\n?", text)
    if not match:
        return "", text.strip()
    return match.group(1), text[match.end():].strip()


def frontmatter_description(frontmatter: str) -> str:
    for line in frontmatter.splitlines():
        if line.startswith("description:"):
            value = line.split(":", 1)[1].strip()
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            return value.strip()
    return ""


def title_from_readme(directory: Path, fallback: str) -> str:
    readme = directory / "README.md"
    if readme.is_file():
        for line in readme.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("# "):
                return clean_text(line[2:].strip(), 90)
    return human_title(fallback)


def first_readme_signal(directory: Path) -> str:
    readme = directory / "README.md"
    if not readme.is_file():
        return ""
    text = readme.read_text(encoding="utf-8", errors="ignore")
    text = re.sub(r"<!-- BEGIN [^\n]*?-->\s*[\s\S]*?<!-- END [^\n]*?-->", "", text)
    for block in re.split(r"\n\s*\n", text):
        b = clean_text(strip_markdown(block.strip()), 620)
        if len(b) < 120:
            continue
        if b.startswith("#") or b.startswith("|"):
            continue
        if "Download" in b or "latest/download" in b:
            continue
        return b
    return ""


def strip_markdown(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"__([^_]+)__", r"\1", text)
    return text


def clean_text(text: str, limit: int | None = None) -> str:
    replacements = {
        "Claude-Code-Plugin": "Plugin-Setup",
        "Claude Code": "Plugin-Setup",
        "Claude": "Chat-System",
        "OpenAI": "KI-Anbieter",
        "Megaprompts": "Werkstatt-Prompts",
        "Megaprompt": "Werkstatt-Prompt",
        "Miniprompts": "Schnellstart-Prompts",
        "Miniprompt": "Schnellstart-Prompt",
        "Codex Iuris Canonici": "CIC",
        "Codex": "Kodex",
        "Cursor": "Editor",
        "Aider": "Editor",
        "Continue": "Editor",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = text.replace("§", "Paragraf")
    text = text.replace("→", "->")
    text = text.replace("✓", "")
    text = text.replace("★", "")
    text = text.replace("<", "[").replace(">", "]")
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\s+", " ", text).strip()
    if limit and len(text) > limit:
        return text[: limit - 1].rstrip(" ,.;:-") + "…"
    return text


def human_title(slug: str) -> str:
    words = [w for w in re.split(r"[-_]+", slug) if w]
    small = {"und", "oder", "mit", "fuer", "für", "im", "am", "zur", "zum", "der", "die", "das"}
    out = []
    for word in words:
        if word in small:
            out.append({"fuer": "für"}.get(word, word))
        elif len(word) <= 3 and word.isalpha():
            out.append(word.upper())
        else:
            out.append(word[:1].upper() + word[1:])
    return " ".join(out)


def prompt_stem(plugin_name: str) -> str:
    replacements = {
        "liquiditaetsplanung": "liquiditaetsplaner",
        "staatsanwaltschaft-praxis-einstieg": "staatsanwaltschaft-einstieg",
        "staatsanwaltschaft-amtsanwaltschaft": "staatsanwaltschaft-amtsanwaltschaft",
    }
    if plugin_name in replacements:
        return replacements[plugin_name]
    if plugin_name.startswith("richter-"):
        return plugin_name.removeprefix("richter-")
    return plugin_name


def collect_skills(directory: Path) -> list[Skill]:
    skills: list[Skill] = []
    skills_dir = directory / "skills"
    if not skills_dir.is_dir():
        return skills
    for skill_md in sorted(skills_dir.glob("*/SKILL.md")):
        text = skill_md.read_text(encoding="utf-8", errors="ignore")
        fm, body = strip_frontmatter(text)
        desc = clean_text(frontmatter_description(fm), 520)
        slug = skill_md.parent.name
        score = len(desc)
        if PRIORITY_RE.search(slug):
            score += 1200
        if PRIORITY_RE.search(desc):
            score += 600
        if "## Normenanker" in body or "## Anker-Rechtsprechung" in body or "## Normen & Rechtsprechung" in body:
            score += 300
        skills.append(Skill(slug=slug, description=desc, body=body, score=score))
    return sorted(skills, key=lambda s: (-s.score, s.slug))


def extract_norms(skills: list[Skill], max_items: int = 10) -> list[str]:
    found: list[str] = []
    for skill in skills:
        sample = skill.description + "\n" + skill.body[:5000]
        for match in NORM_RE.findall(sample):
            item = clean_text(match, 180)
            if item and item not in found:
                found.append(item)
            if len(found) >= max_items:
                return found
    return found


def extract_decisions(skills: list[Skill], max_items: int = 5) -> list[str]:
    found: list[str] = []
    for skill in skills:
        for match in DECISION_RE.findall(skill.body):
            item = clean_text(match, 240)
            if "BeckRS" in item or "juris" in item:
                continue
            if item and item not in found:
                found.append(item)
            if len(found) >= max_items:
                return found
    return found


def selected_skills(skills: list[Skill], limit: int) -> list[Skill]:
    return skills[:limit]


def build_werkstatt(plugin: dict, directory: Path, stem: str) -> str:
    name = plugin["name"]
    manifest = json.loads((directory / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    title = title_from_readme(directory, name)
    description = clean_text(plugin.get("description") or manifest.get("description") or "", 900)
    readme_signal = first_readme_signal(directory)
    skills = collect_skills(directory)
    core = selected_skills(skills, 12)
    norms = extract_norms(skills, 10)
    decisions = extract_decisions(skills, 5)

    role_target = description or readme_signal or f"Dieses Werkzeug bearbeitet den Arbeitsbereich {human_title(name)}."
    lines: list[str] = [
        f"# {title} — Werkstatt-Prompt",
        "",
        f"Dieser Werkstatt-Prompt verdichtet das Plugin `{name}` zu einem tragfähigen Ein-Datei-Arbeitsmodus. Er dient dazu, Akten, Fragen und Entwürfe im Zuschnitt von {title} zu ordnen, rechtlich zu prüfen und in verwertbare Arbeitsprodukte zu überführen.",
        "",
        "## Rolle",
        "",
        f"- Du arbeitest im Rollenbild dieses Plugins: {role_target}",
        "- Du ersetzt kein installiertes Plugin, sondern bildest dessen Arbeitslogik als Markdown-Prompt nach.",
        "- Du fragst nicht mechanisch alles ab, sondern liest zuerst vorhandene Dateien, erkennt Rollen, Fristen, Anträge, Zahlen, Zuständigkeiten und Lücken.",
        "- Du bist kein Ersatz für die menschliche Endprüfung. Du lieferst vorbereitende Analyse, Formulierungshilfe, Prüfpfade und Qualitätskontrolle.",
        "",
        "## Werkstattlogik",
        "",
    ]

    stationen = [
        ("Akteninventar", "Welche Dateien, Parteien, Behörden, Gerichte, Verträge, Anträge, Fristen und Beträge sind vorhanden?"),
        ("Rollenklärung", "Aus welcher Perspektive wird gearbeitet und welches Ergebnis soll am Ende stehen?"),
        ("Rechtsrahmen", "Welche Normen, Zuständigkeiten, Verfahren, Fristen und Beweislasten tragen den Fall?"),
        ("Tatsachenmatrix", "Welche Tatsachen sind belegt, streitig, nur behauptet oder noch offen?"),
        ("Prüfpfad", "Welche Tatbestandsmerkmale, Einwendungen, Ausnahmen und Anschlussfragen sind in richtiger Reihenfolge zu prüfen?"),
        ("Risikoampel", "Welche Punkte sind sofort kritisch, welche sind heilbar, welche benötigen Live-Quelle oder Rückfrage?"),
        ("Arbeitsprodukt", "Welches konkrete Dokument wird geliefert: Memo, Schriftsatz, Tabelle, Checkliste, Klausel, Tenor, Antrag oder Antwortentwurf?"),
        ("Gegenprüfung", "Welche Gegenargumente, Beweisprobleme, Zuständigkeitsfragen und Fristfallen müssen vor Abgabe geprüft werden?"),
        ("Quellenabgleich", "Welche Normen und Entscheidungen werden vor Verwendung live aus amtlichen oder frei zugänglichen Quellen nachgezogen?"),
        ("Anschlussentscheidung", "Was ist der nächste realistische Schritt: Rückfrage, Entwurf, Eskalation, Vergleich, Antrag, Fristnotiz oder Ablage?"),
    ]
    for idx, (heading, explanation) in enumerate(stationen, 1):
        lines += [
            f"{idx}. **{heading}**",
            f"   - Eingang: {explanation}",
            "   - Prüfung: arbeite nur mit Tatsachen, die aus Akte, Nutzerangabe oder klar markierter Annahme stammen.",
            "   - Arbeitsprodukt: formuliere in ganzen Sätzen, nicht als Stichwortgerüst.",
            "   - Anschluss: benenne den nächsten Skill-Gedanken oder die nächste praktische Handlung.",
        ]

    lines += [
        "",
        "## Pflicht-Workflow am Anfang",
        "",
        "- Wenn Dateien vorliegen, beginne mit einem Akteninventar und einer Rollen-/Zielhypothese. Frage erst danach nach Lücken.",
        "- Wenn keine Dateien vorliegen, stelle höchstens drei Startfragen: Rolle, Zielprodukt, Frist oder Dringlichkeit. Default ist ein kurzes Prüf-Memo mit Handlungsempfehlung.",
        "- Wenn der Nutzer ein Dokument will, liefere sofort eine ausformulierte erste Fassung und markiere offene Tatsachen in eckigen Klammern.",
        "",
        "## Quellen-Disziplin",
        "",
        "- Benenne Normen konkret mit Gesetz, Paragraf, Absatz, Satz, Nummer oder Buchstabe, soweit das Material sie trägt.",
        "- Verwende Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine Blindzitate aus Datenbanken, Kommentaren oder Aufsätzen.",
        "- Wenn eine Entscheidung nicht sicher verifiziert ist, schreibe ausdrücklich: Rechtsprechung live prüfen, Aktenzeichen nicht aus Modellwissen einsetzen.",
        "- Aktualität ist Teil des Outputs: prüfe bei laufenden Fristen, Gesetzesänderungen, Übergangsrecht, Landesrecht und Unionsrecht, ob der Stand noch trägt.",
    ]
    if norms:
        lines.append("- Aus dem Plugin übernommene Normanker:")
        for norm in norms:
            lines.append(f"  - {norm}")
    else:
        lines.append("- Das Plugin enthält keine belastbare Normliste im Ausgangsmaterial; ziehe Normen erst aus Akte, Skills oder Live-Quelle nach.")

    lines += [
        "",
        "## Leitentscheidungen",
        "",
    ]
    if decisions:
        for dec in decisions:
            lines.append(f"- {dec}. Vor Verwendung live nachziehen und auf den konkreten Fall zuschneiden.")
    else:
        lines.append("- Keine belastbare Leitentscheidung aus den vorhandenen Skills übernommen. Zitiere Entscheidungen nur nach Live-Verifikation mit Gericht, Datum und Aktenzeichen.")

    lines += [
        "",
        "## Prüfraster oder Indizienliste",
        "",
    ]
    for idx, skill in enumerate(core, 1):
        title = human_title(skill.slug)
        desc = skill.description or "Arbeite diesen Teilbereich anhand der Akte, der einschlägigen Normen, Fristen, Beweisfragen und des Zielprodukts ab."
        lines += [
            f"{idx}. **{title}**",
            f"   - Fachlicher Fokus: {clean_text(desc, 420)}",
            "   - Eingaben: relevante Aktenstücke, Fristen, Zahlen, Rollen, Vorentscheidungen und offene Belege.",
            "   - Prüfung: Tatbestand, Zuständigkeit, Verfahren, Beweislast, Einwendungen, Rechtsfolge und Gegenargumente trennen.",
            "   - Output: ein nutzbares Teilprodukt mit Kurzfazit, Begründung und nächstem Schritt.",
        ]
    if not core:
        lines += [
            "1. **Plugin-Grundprüfung**",
            "   - Fachlicher Fokus: Sachverhalt strukturieren, Rechtsrahmen bestimmen und verwertbares Arbeitsprodukt liefern.",
            "   - Eingaben: Akte, Nutzerziel, Frist und gewünschte Textsorte.",
            "   - Prüfung: Tatsachen, Normen, Risiken und offene Punkte trennen.",
            "   - Output: Memo, Tabelle oder Entwurf in ganzen Sätzen.",
        ]

    lines += [
        "",
        "## Antwortform",
        "",
        "- **Lagebild:** Wer will was von wem, seit wann, mit welcher Frist und welchem Risiko?",
        "- **Prüfung:** Normen, Tatbestandsmerkmale, Beweisfragen, Gegenargumente und Rechtsfolge in richtiger Reihenfolge.",
        "- **Empfehlung:** konkrete nächste Handlung, nicht nur abstrakte Rechtslage.",
        "- **Arbeitsprodukt:** gewünschtes Dokument vollständig ausformulieren; Tabellen nur dort einsetzen, wo sie schneller erfassbar sind.",
        "- **Quellen:** Normen konkret benennen, Rechtsprechung nur live verifiziert oder als Prüfbedarf markieren.",
        "- **Stop-Kriterien:** unklare Identität, laufende Notfrist, Straf-/Haftungsrisiko, Datenschutzproblem, Interessenkollision oder fehlende Akte.",
        "",
        "## Eigenheiten dieses Plugins",
        "",
        f"- Der Arbeitsmodus ist auf `{name}` zugeschnitten; antworte nicht wie ein allgemeiner Rechtsassistent.",
        "- Nutze die Sprache der vorhandenen Skills: erst ordnen, dann prüfen, dann ausformulieren.",
        "- Vermeide Rückfragen, wenn die Information aus der Akte ablesbar ist.",
        "- Trenne sichere Erkenntnisse von Hypothesen und fehlenden Belegen.",
        "- Formuliere Ergebnisse so, dass sie unmittelbar in Kanzlei-, Behörden-, Gerichts- oder Unternehmensarbeit weiterverwendbar sind.",
        "- Baue bei komplexen Fällen eine kleine Entscheidungs- oder Fristenmatrix ein.",
    ]
    if readme_signal:
        lines.append(f"- Materieller Schwerpunkt aus dem README: {readme_signal}")

    lines += [
        "",
        "## Skelette",
        "",
        "### Skelett 1: Akteninventar und Startverfügung",
        "",
        "Ich habe die Unterlagen zunächst inventarisiert. Erkennbar sind [Rollen], [zentrale Dokumente], [Fristen] und [offene Belege]. Ich arbeite ab jetzt in folgender Reihenfolge: erst Zuständigkeit und Verfahrenslage, dann materielle Prüfung, dann Beweis- und Fristenmatrix, anschließend das gewünschte Arbeitsprodukt.",
        "",
        "### Skelett 2: Kurz-Memo mit Empfehlung",
        "",
        "Kurzfazit: [Ergebnis in einem Satz]. Tragend sind [Normen] und [Tatsachen]. Kritisch sind [Risiken]. Ich empfehle als nächsten Schritt [konkrete Handlung], weil [Begründung]. Vor Abgabe sind noch [Quellen oder Belege] zu prüfen.",
        "",
        "### Skelett 3: Ausformulierter Dokumentenbaustein",
        "",
        "Namens und im Auftrag von [Rolle] wird Folgendes vorgetragen: [Tatsachenkern]. Rechtlich folgt daraus [Subsumtion]. Die Gegenseite wird voraussichtlich einwenden [Gegenargument]; dem ist entgegenzuhalten [Antwort]. Daraus ergibt sich [Antrag, Tenor, Klausel, Verfügung oder Empfehlung].",
        "",
    ]
    return "\n".join(lines).rstrip() + "\n"


def build_schnellstart(plugin: dict, directory: Path, stem: str) -> str:
    name = plugin["name"]
    title = title_from_readme(directory, name)
    manifest = json.loads((directory / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    description = clean_text(plugin.get("description") or manifest.get("description") or "", 360)
    skills = collect_skills(directory)
    core = selected_skills(skills, 8)
    norms = extract_norms(skills, 4)
    decisions = extract_decisions(skills, 2)

    lines: list[str] = [
        f"# {title} — Schnellstart",
        "",
        f"Ich bin der kompakte Arbeitsmodus für `{name}`. Ich ordne Akten und Fragen in diesem Fachzuschnitt, prüfe quellenbewusst und liefere sofort ein verwertbares Arbeitsprodukt.",
        "",
        "## Rolle",
        "",
        description or f"Arbeite im Themenfeld {human_title(name)} mit präziser Triage, Normenprüfung, Risikoampel und ausformulierter Antwort.",
        "",
        "## Triage",
        "",
        "1. Liegen Dateien oder Aktenstücke vor? Dann zuerst inventarisieren und Rollen, Fristen, Beträge, Anträge und Lücken auslesen.",
        "2. Welche Perspektive gilt: Berater, Gericht, Behörde, Unternehmen, Verbraucher, Verband oder Selbstvertreter?",
        "3. Welches Produkt soll entstehen: Memo, Schriftsatz, Antrag, Tabelle, Klausel, Checkliste, Verfügung, Tenor oder E-Mail?",
        "4. Gibt es eine laufende Frist, einen Zuständigkeitsstreit, eine Beweisfrage oder ein Haftungsrisiko?",
        "",
        "## Werkstatt-Kurzweg",
        "",
        "1. Akte lesen, vorhandene Informationen nutzen und keine unnötigen Startfragen stellen.",
        "2. Streit- oder Prüfgegenstand in einem Satz festlegen.",
        "3. Normen, Verfahren, Zuständigkeit, Fristen und Beweislast trennen.",
        "4. Tatbestand und Rechtsfolge entlang der einschlägigen Skills prüfen.",
        "5. Gegenargumente, fehlende Belege und Eskalationspunkte markieren.",
        "6. Das gewünschte Arbeitsprodukt in ganzen Sätzen ausformulieren.",
        "7. Quellen- und Fristencheck als kurze Schlusskontrolle liefern.",
        "",
        "## Anker",
        "",
    ]
    if norms:
        lines.append("Pflichtnormen aus dem Plugin-Material:")
        for norm in norms:
            lines.append(f"- {norm}")
    else:
        lines.append("- Normen erst aus Akte, Skill-Material oder Live-Quelle bestimmen; keine Scheinanker setzen.")
    if decisions:
        lines.append("Leitentscheidungen nur nach Live-Prüfung verwenden:")
        for dec in decisions:
            lines.append(f"- {dec}")
    else:
        lines.append("- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle zitieren.")

    lines += [
        "",
        "## Kernmodule",
        "",
    ]
    for skill in core:
        lines.append(f"- **{human_title(skill.slug)}:** {clean_text(skill.description, 240) or 'Fachmodul aus dem Plugin auf den konkreten Fall anwenden.'}")
    if not core:
        lines.append("- **Grundprüfung:** Sachverhalt strukturieren, Rechtsrahmen bestimmen, Risiko bewerten, Arbeitsergebnis ausformulieren.")

    lines += [
        "",
        "## Antwortform",
        "",
        "Lagebild, Prüfpfad, Ergebnis, Empfehlung, Arbeitsprodukt, offene Punkte, Quellencheck.",
        "",
        "## Stop",
        "",
        "Bei Notfrist, Straf-/Haftungsrisiko, Interessenkollision, personenbezogenen Echtdaten in ungeprüften Systemen oder unsicherer Quelle Übergabe an einen Berufsträger verlangen.",
        "",
    ]
    text = "\n".join(lines).rstrip() + "\n"
    if len(text) <= MAX_SCHNELLSTART:
        return text
    # Kürzen ohne Strukturverlust.
    while len(text) > MAX_SCHNELLSTART and core:
        core = core[:-1]
        lines = lines[: lines.index("## Kernmodule") + 2]
        for skill in core:
            lines.append(f"- **{human_title(skill.slug)}:** {clean_text(skill.description, 160) or 'Fachmodul fallbezogen anwenden.'}")
        lines += [
            "",
            "## Antwortform",
            "",
            "Lagebild, Prüfpfad, Ergebnis, Empfehlung, Arbeitsprodukt, offene Punkte, Quellencheck.",
            "",
            "## Stop",
            "",
            "Bei Notfrist, Haftungsrisiko, Interessenkollision oder unsicherer Quelle Übergabe an einen Berufsträger verlangen.",
            "",
        ]
        text = "\n".join(lines).rstrip() + "\n"
    if len(text) > MAX_SCHNELLSTART:
        text = text[: MAX_SCHNELLSTART - 2].rstrip() + "\n"
    return text


def remove_old_local_files(directory: Path, plugin_name: str, keep: set[Path]) -> list[str]:
    removed: list[str] = []
    candidates = list(OLD_LOCAL_PROMPT_NAMES)
    candidates.extend([f"{plugin_name}-megaprompt.md", f"{plugin_name}-miniprompt.md"])
    for path in directory.iterdir():
        if not path.is_file():
            continue
        if path in keep:
            continue
        if path.name in candidates or path.name.endswith("-megaprompt.md") or path.name.endswith("-miniprompt.md"):
            path.unlink()
            removed.append(path.name)
    return removed


def validate_prompt(path: Path, schnellstart: bool) -> list[str]:
    text = path.read_text(encoding="utf-8")
    problems: list[str] = []
    if not text.endswith("\n"):
        problems.append("Datei endet nicht mit Leerzeile")
    if text.startswith("---"):
        problems.append("YAML-Frontmatter ist verboten")
    if len(re.findall(r"^# ", text, flags=re.MULTILINE)) != 1:
        problems.append("Datei braucht exakt eine H1")
    if "§" in text:
        problems.append("Paragrafenzeichen gefunden")
    if "<" in text or ">" in text:
        problems.append("spitze Klammer gefunden")
    if re.search(r"[\U0001F300-\U0001FAFF]", text):
        problems.append("Emoji gefunden")
    forbidden = ["Claude", "OpenAI", "Codex", "Cursor", "Aider", "Continue"]
    for word in forbidden:
        if word in text:
            problems.append(f"verbotener KI-Hilfsname gefunden: {word}")
    if schnellstart and len(text) > MAX_SCHNELLSTART:
        problems.append(f"Schnellstart zu lang: {len(text)} Zeichen")
    if not schnellstart and len(text.splitlines()) < 150:
        problems.append(f"Werkstatt zu kurz: {len(text.splitlines())} Zeilen")
    return problems


def main() -> int:
    plugins = load_marketplace()
    coverage: list[dict[str, str]] = []
    problems: list[str] = []
    for plugin in plugins:
        name = plugin["name"]
        directory = plugin_dir(plugin)
        stem = prompt_stem(name)
        werkstatt = directory / f"{stem}-werkstatt.md"
        schnellstart = directory / f"{stem}-schnellstart.md"

        werkstatt.write_text(build_werkstatt(plugin, directory, stem), encoding="utf-8")
        schnellstart.write_text(build_schnellstart(plugin, directory, stem), encoding="utf-8")
        remove_old_local_files(directory, name, {werkstatt, schnellstart})

        for path, is_schnell in [(werkstatt, False), (schnellstart, True)]:
            for problem in validate_prompt(path, is_schnell):
                problems.append(f"{path.relative_to(REPO)}: {problem}")

        coverage.append(
            {
                "plugin": name,
                "werkstatt": str(werkstatt.relative_to(directory)),
                "schnellstart": str(schnellstart.relative_to(directory)),
            }
        )

    if problems:
        print("Prompt-Validierung fehlgeschlagen:")
        for problem in problems[:80]:
            print(f"  - {problem}")
        raise SystemExit(1)

    print(f"Werkstatt-/Schnellstart-Prompts erzeugt: {len(coverage)} Plugins")
    print(f"Schnellstart max: {max(len((plugin_dir(p) / (prompt_stem(p['name']) + '-schnellstart.md')).read_text(encoding='utf-8')) for p in plugins)} Zeichen")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
