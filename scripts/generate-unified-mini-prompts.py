#!/usr/bin/env python3
"""Erzeugt pro Plugin eine Schnellstart-Kompatibilitaetsdatei.

Ziel:
- eine einzelne Markdown-Datei pro Plugin,
- maximal 7.500 Zeichen inkl. Leerzeichen,
- ueber Sammel-ZIP und Komplettpaket herunterladbar,
- nutzbar in ChatGPT, Claude, Gemini, Mistral, Le Chat usw.,
- keine installierbare Plugin-Datei und kein Ersatz fuer die vollstaendigen
  Skills.

Ausgabe:
    unified-mini-prompts/<plugin>.md

Der Ordnername bleibt aus Kompatibilitaetsgruenden bestehen. Inhaltlich gewinnt
die plugin-lokale Datei <sprechender-name>-schnellstart.md.
"""

from __future__ import annotations

import json
import re
import textwrap
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "unified-mini-prompts"
MAX_CHARS = 7500
SOFT_MAX = 7350


PRIORITY_RE = re.compile(
    r"(einstieg|kaltstart|triage|routing|workflow|mandat|erstpruefung|erstprüfung|"
    r"checkliste|fristen|quality|red-team|risiko|strategie|dashboard|akte|akten)",
    re.IGNORECASE,
)


def strip_markdown_link(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def clean(text: str, max_len: int | None = None) -> str:
    text = strip_markdown_link(text)
    text = text.replace("|", "/")
    text = text.replace("—", "-")
    text = re.sub(r"\s+", " ", text).strip()
    if max_len and len(text) > max_len:
        return text[: max_len - 1].rstrip(" ,.;:") + "…"
    return text


def humanize_slug(slug: str) -> str:
    words = [w for w in re.split(r"[-_]+", slug) if w]
    return " ".join(w.capitalize() if len(w) > 3 else w.upper() for w in words)


def frontmatter_description(skill_md: Path) -> str:
    text = skill_md.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        return ""
    m = re.match(r"---\s*\n([\s\S]*?)\n---", text)
    if not m:
        return ""
    fm = m.group(1)
    line = next((line for line in fm.splitlines() if line.startswith("description:")), "")
    if not line:
        return ""
    desc = line.split(":", 1)[1].strip()
    if desc.startswith('"') and desc.endswith('"'):
        desc = desc[1:-1]
    return clean(desc, 260)


def first_readme_paragraph(plugin_dir: Path) -> str:
    readme = plugin_dir / "README.md"
    if not readme.is_file():
        return ""
    text = readme.read_text(encoding="utf-8", errors="ignore")
    text = re.sub(
        r"<!-- BEGIN [^\n]*?-->\s*[\s\S]*?<!-- END [^\n]*?-->",
        "",
        text,
    )
    paragraphs = []
    for block in re.split(r"\n\s*\n", text):
        b = block.strip()
        if not b or b.startswith("#") or b.startswith("|") or b.startswith("<!--"):
            continue
        if "https://github.com/" in b or "Sofort-Downloads" in b:
            continue
        if len(strip_markdown_link(b)) >= 80:
            paragraphs.append(strip_markdown_link(b))
    return clean(paragraphs[0], 420) if paragraphs else ""


def collect_skills(plugin_dir: Path) -> list[dict[str, str | int]]:
    skills_dir = plugin_dir / "skills"
    if not skills_dir.is_dir():
        return []
    items = []
    for skill_md in sorted(skills_dir.glob("*/SKILL.md")):
        slug = skill_md.parent.name
        desc = frontmatter_description(skill_md)
        score = 0
        if PRIORITY_RE.search(slug):
            score += 1000
        if PRIORITY_RE.search(desc):
            score += 500
        score += min(len(desc), 400)
        items.append({"slug": slug, "title": humanize_slug(slug), "desc": desc, "score": score})
    return sorted(items, key=lambda x: (-int(x["score"]), str(x["slug"])))


def marketplace() -> dict:
    return json.loads((REPO_ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))


def prompt_stem(plugin_name: str) -> str:
    if plugin_name == "liquiditaetsplanung":
        return "liquiditaetsplaner"
    if plugin_name == "staatsanwaltschaft-praxis-einstieg":
        return "staatsanwaltschaft-einstieg"
    if plugin_name.startswith("richter-"):
        return plugin_name.removeprefix("richter-")
    return plugin_name


def local_schnellstart(plugin_name: str, plugin_dir: Path) -> Path | None:
    stem = prompt_stem(plugin_name)
    for candidate in [
        plugin_dir / f"{stem}-schnellstart.md",
        plugin_dir / f"{plugin_name}-schnellstart.md",
    ]:
        if candidate.is_file():
            return candidate
    return None


def build_prompt(plugin: dict, plugin_dir: Path, max_modules: int, desc_len: int) -> str:
    name = plugin["name"]
    manifest = json.loads((plugin_dir / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    description = clean(plugin.get("description") or manifest.get("description") or "", 520)
    readme_hint = first_readme_paragraph(plugin_dir)
    skills = collect_skills(plugin_dir)

    selected = skills[:max_modules]

    lines: list[str] = [
        f"# Schnellstart-Prompt: {name}",
        "",
        f"Du bist der kompakte Arbeitsmodus des Legal-Plugins `{name}`. Nutze diesen Prompt, wenn das vollständige Plugin nicht installiert werden kann. Arbeite fallbezogen, quellenbewusst und ohne generische Fülltexte.",
        "",
        "## Zweck",
        "",
        description or f"Bearbeite Fälle und Dokumente im thematischen Zuschnitt des Plugins `{name}`.",
    ]
    if readme_hint:
        lines += ["", f"Praxisfokus: {readme_hint}"]

    lines += [
        "",
        "## Start",
        "",
        "1. Wenn Dateien, Ordnerauszüge oder Aktenstücke vorliegen: zuerst ein kurzes Akteninventar bilden, Parteien/Rollen, Fristen, Anträge, Beträge, Zuständigkeiten, Dokumentarten und Lücken erkennen. Frage nicht nach Daten, die aus der Akte ersichtlich sind.",
        "2. Wenn nichts vorliegt: höchstens fünf gezielte Fragen stellen: Rolle des Nutzers, Ziel, Rechtsordnung, Frist/Dringlichkeit und gewünschtes Arbeitsprodukt.",
        "3. Danach sofort einen Arbeitsplan mit Prioritäten liefern: Sofortmaßnahmen, Prüfpfad, fehlende Belege, Risiken und nächster Output.",
        "",
        "## Arbeitsregeln",
        "",
        "- Deutsches Recht ist Standard; Unionsrecht, Landesrecht, ausländisches Recht oder Soft Law nur einbeziehen, wenn der Fall es trägt.",
        "- Normen konkret benennen, soweit sie fuer den konkreten Vorgang einschlaegig sind. Keine Scheinzitate.",
        "- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarer Quelle verwenden; BeckRS/juris/Literatur nicht blind zitieren.",
        "- Bei unklarer Tatsachenbasis Hypothesen sauber kennzeichnen und Beweis-/Dokumentenbedarf nennen.",
        "- Nicht nur beraten, sondern verwertbare Arbeit liefern: Tabelle, Entscheidungsbaum, Fristenplan, Schriftsatzbaustein, Vertragsklausel, Memo, E-Mail, Checkliste oder Red-Team-Kommentar.",
        "",
        "## Kernmodule",
        "",
    ]
    if selected:
        for item in selected:
            title = clean(str(item["title"]), 72)
            desc = clean(str(item["desc"]), desc_len) or "Bearbeite diesen Teilbereich anhand der Akte, der einschlaegigen Normen, Fristen, Beweisfragen und des gewuenschten Outputs."
            lines.append(f"- **{title}:** {desc}")
    else:
        lines.append("- **Plugin-Arbeitsmodus:** Sachverhalt strukturieren, Normen und Risiken bestimmen, verwertbaren Output erstellen und Quellenhygiene beachten.")

    lines += [
        "",
        "## Ausgabeformat",
        "",
        "Liefere zuerst eine Kurzdiagnose in drei bis sieben Punkten. Danach folgt das eigentliche Arbeitsprodukt in ganzen Sätzen und mit klaren Überschriften. Schließe mit einer knappen Selbstkontrolle: offene Tatsachen, Fristen, Quellenprüfung, Gegenargumente und nächster sinnvoller Schritt.",
        "",
        "## Grenzen",
        "",
        "Keine Rechtsberatung ohne menschliche Prüfung, keine Halluzination von Rechtsprechung, keine vertraulichen Echtdaten in ungeprüfte Systeme. Wenn der Fall hohe Risiken, Fristen, Straf-/Berufsrecht, Insolvenz, Datenschutz, Steuern oder Gerichtsverfahren betrifft, deutlich auf menschliche Endprüfung hinweisen.",
    ]
    return "\n".join(lines).strip() + "\n"


def fit_prompt(plugin: dict, plugin_dir: Path) -> str:
    local = local_schnellstart(plugin["name"], plugin_dir)
    if local is not None:
        text = local.read_text(encoding="utf-8")
        if len(text) > MAX_CHARS:
            raise SystemExit(f"{local}: Schnellstart-Prompt hat {len(text)} Zeichen und ueberschreitet {MAX_CHARS}")
        return text
    for max_modules, desc_len in [(28, 180), (24, 160), (20, 145), (16, 135), (12, 130), (8, 120)]:
        text = build_prompt(plugin, plugin_dir, max_modules=max_modules, desc_len=desc_len)
        if len(text) <= SOFT_MAX:
            return text
    text = build_prompt(plugin, plugin_dir, max_modules=6, desc_len=110)
    if len(text) <= MAX_CHARS:
        return text
    # Letzte Sicherheit: nicht mitten in UTF-8-Bytes schneiden, sondern auf Zeichenebene.
    return text[: MAX_CHARS - 2].rstrip() + "\n"


def write_readme(plugins: list[dict]) -> None:
    lines = [
        "# Schnellstart-Kompatibilitätsdateien",
        "",
        "Ein kompakter Markdown-Prompt pro Plugin, jeweils auf maximal 7.500 Zeichen inkl. Leerzeichen begrenzt. Diese Dateien sind für Nutzer gedacht, die kein Plugin installieren können oder einen schnellen Ein-Datei-Prompt in einem beliebigen Chatbot verwenden wollen.",
        "",
        "Die vollständigen Plugin-ZIPs bleiben der bessere Weg für Plugin-Oberflächen. Die Schnellstart-Prompts sind bewusst Sparvarianten: sie enthalten den Einstieg, den Arbeitsmodus und eine verdichtete Auswahl der wichtigsten Skill-Module.",
        "",
        "| Plugin | Schnellstart-Datei |",
        "| --- | --- |",
    ]
    for plugin in plugins:
        name = plugin["name"]
        lines.append(f"| `{name}` | [`{name}.md`](./{name}.md) |")
    lines.append("")
    (OUT_DIR / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    plugins = marketplace()["plugins"]
    expected = {p["name"] for p in plugins}

    for old in OUT_DIR.glob("*.md"):
        if old.name != "README.md" and old.stem not in expected:
            old.unlink()

    too_long: list[tuple[str, int]] = []
    for plugin in plugins:
        name = plugin["name"]
        source = plugin.get("source", f"./{name}")
        rel = source[2:] if source.startswith("./") else source
        plugin_dir = REPO_ROOT / rel
        prompt = fit_prompt(plugin, plugin_dir)
        if len(prompt) > MAX_CHARS:
            too_long.append((name, len(prompt)))
        (OUT_DIR / f"{name}.md").write_text(prompt, encoding="utf-8")

    write_readme(plugins)
    if too_long:
        for name, length in too_long:
            print(f"ZU LANG: {name} {length}")
        raise SystemExit(1)

    sizes = [len((OUT_DIR / f"{p['name']}.md").read_text(encoding="utf-8")) for p in plugins]
    print(
        f"Schnellstart-Kompatibilitaetsdateien erstellt: {len(plugins)} | "
        f"max={max(sizes)} Zeichen | avg={sum(sizes)//len(sizes)} Zeichen"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
