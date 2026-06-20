#!/usr/bin/env python3
"""Generiert die globale SKILLS.md (Skill-Gesamtuebersicht) aus dem Repo.

Wird bei jeder Release-Vorbereitung gelaufen. Garantiert, dass jeder neue
Skill, der irgendwo unter <plugin>/skills/<skill>/SKILL.md angelegt wird,
automatisch in der SKILLS.md auftaucht — mit:

- Direkt-Download des SKILL.md als rohe Markdown-Datei (im Browser per
  Rechtsklick "Ziel speichern unter" oder "?raw=1" laedt sofort herunter).
- Pro Plugin: ZIP-Download-Link auf das Release-Asset
  https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/<plugin>.zip
- Oben prominenter Hinweis: Skills sind reine Markdown-Prompts und
  funktionieren per Copy-Paste in jedem Chatbot.

Idempotent: schreibt SKILLS.md neu. Liest Version aus marketplace.json.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
GH_OWNER = "Klotzkette"
GH_REPO = "claude-fuer-deutsches-recht"
GH_BLOB = f"https://github.com/{GH_OWNER}/{GH_REPO}/blob/main"
GH_RAW = f"https://raw.githubusercontent.com/{GH_OWNER}/{GH_REPO}/main"
GH_RELEASE = f"https://github.com/{GH_OWNER}/{GH_REPO}/releases/latest/download"
SKILLS_INDEX_DIR = REPO_ROOT / "skills-index"


def clean_description(desc: str) -> str:
    """Entfernt alte Generator-/Konsolidierungsfloskeln aus Tabellenbeschreibungen."""
    desc = re.sub(
        r"\s+[—-]\s*Arbeitskontext:\s*[^.]+,\s*Schwerpunkt\s+[^.]+\.?",
        "",
        desc,
    )
    desc = re.sub(r"\s+im Plugin\s+[^.:\"`|]+(?=[:.])", "", desc)
    desc = re.sub(r"\s+im Plugin\s+[^\"`|]+$", "", desc)
    desc = re.sub(r"\s{2,}", " ", desc)
    return desc.strip()


def read_description(skill_md: Path) -> str:
    with skill_md.open("r", encoding="utf-8") as fh:
        first = fh.readline()
        if first.strip() != "---":
            return ""
        frontmatter_lines: list[str] = []
        for idx, line in enumerate(fh, start=1):
            if idx > 200:
                return ""
            if line.strip() == "---":
                break
            frontmatter_lines.append(line)
        else:
            return ""
    fm = "".join(frontmatter_lines)
    if not fm:
        return ""
    desc = ""
    for line in fm.splitlines():
        if line.startswith("description:"):
            desc = line.split(":", 1)[1].strip()
            break
    if not desc:
        return ""
    if desc.startswith('"') and desc.endswith('"'):
        desc = desc[1:-1]
    desc = clean_description(desc.replace("\n", " ").strip())
    desc = desc.replace("|", "\\|").strip()
    if len(desc) > 280:
        desc = desc[:277].rstrip() + "..."
    return desc


def collect_plugins() -> list[tuple[str, list[str]]]:
    """Liest Plugin-Reihenfolge aus marketplace.json und scannt jeden Plugin-Ordner."""
    market = json.loads((REPO_ROOT / ".claude-plugin" / "marketplace.json").read_text())
    out: list[tuple[str, list[str]]] = []
    for plugin in market["plugins"]:
        name = plugin["name"]
        skills_dir = REPO_ROOT / name / "skills"
        if not skills_dir.is_dir():
            continue
        skills = sorted(
            d.name
            for d in skills_dir.iterdir()
            if d.is_dir() and (d / "SKILL.md").is_file()
        )
        if skills:
            out.append((name, skills))
    return out


def header(total_skills: int, total_plugins: int, version: str) -> str:
    megazip = f"{GH_RELEASE}/alle-plugins-megazip.zip"
    komplett = f"{GH_RELEASE}/alles-komplettpaket.zip"
    alle_md = f"{GH_RELEASE}/alle-skills-markdown.zip"
    alle_minis = f"{GH_RELEASE}/alle-unified-mini-prompts.zip"
    return f"""# Skill-Gesamtuebersicht

Automatisch generierte Gesamtuebersicht aller **{total_skills} Skills** in **{total_plugins} Plugins**.

Stand: `{version}`.

## ⬇️ Alle Skills auf einmal herunterladen

| Paket | Inhalt | Download |
| --- | --- | --- |
| **Alle Skills als Markdown** | Reine `SKILL.md`-Dateien aller {total_plugins} Plugins plus Unified Mini Prompts — als echte Datei-Downloads | [`alle-skills-markdown.zip`]({alle_md}) |
| **Alle Unified Mini Prompts** | Pro Plugin ein kompakter Ein-Datei-Prompt bis 7.500 Zeichen fuer Chatbots ohne Plugin-Installation | [`alle-unified-mini-prompts.zip`]({alle_minis}) |
| **Alle Plugins (installierbar)** | Alle {total_plugins} Plugin-ZIPs in einem Archiv (fuer Claude Code) | [`alle-plugins-megazip.zip`]({megazip}) |
| **Komplettpaket (alles)** | Plugins + Skill-Markdowns + Testakten + Uebersichten | [`alles-komplettpaket.zip`]({komplett}) |

Das Markdown-Paket reicht, wenn man die vollstaendigen Skills in ChatGPT, Gemini, Mistral, Le Chat oder Perplexity nutzen will. Die Unified Mini Prompts sind die Sparvariante: ein kurzer Workflow pro Plugin, wenn man nur eine einzige Markdown-Datei verwenden moechte. Das Plugin-Paket ist fuer Claude-Code-/Cowork-Nutzer. Das Komplettpaket enthaelt zusaetzlich Testakten und alle Repo-Uebersichten.

Wer nur **ein bestimmtes Plugin** will: weiter unten in der Plugin-Tabelle pro Plugin eigene Links (Plugin-ZIP, Markdown-ZIP **und** Unified Mini Prompt als Repo-Markdown).

## Worum es hier geht: alles nur grosse Prompts

Diese Skills sind am Ende **nichts weiter als grosse, sehr sorgfaeltig formulierte System-Prompts in Markdown**. Sie wurden fuer das Claude-Code-Plugin-System geschrieben, **funktionieren aber in jedem anderen Chatbot genauso**.

So benutzt man einen Skill ausserhalb von Claude Code:

1. Unten in der Plugin-Tabelle auf das gewuenschte Plugin klicken — die Detailseite mit allen Skills oeffnet sich.
2. Auf der Detailseite oben auf **Markdown-ZIP** klicken — die `<plugin>-skills-markdown.zip` landet direkt im Download-Ordner. Entpacken, gewuenschte `SKILL.md` oeffnen.
3. **Entweder** den kompletten Text mit `Strg+A` / `Cmd+A` kopieren und in den Chat einfuegen (ChatGPT, Mistral, Gemini, DeepSeek, Le Chat, ...).
4. **Oder** die einzelne `SKILL.md` als Anhang in den Chatbot ziehen.
5. Danach die eigene Frage / das eigene Dokument hinterherschicken — der Chatbot uebernimmt die Rolle aus dem Skill.

**Hinweis zu Browser-Links:** `[Markdown]` zeigt die Datei im Browser an (zum Lesen oder Kopieren). `[Raw .md]` oeffnet den Rohtext — GitHub liefert ihn als `text/plain` aus, manche Browser zeigen ihn deshalb als Text statt als Download. **Wenn ein echter Datei-Download gewuenscht ist, immer das Plugin-Markdown-ZIP nehmen.**

So bekommt man die komplette Sammlung als installierbares ZIP:

- In der Plugin-Tabelle unten in der Spalte **Plugin-ZIP** auf den Download-Link klicken. Das laedt eine ZIP-Datei mit **allen** Skills dieses Plugins inkl. Hilfsdateien, Pruefrastern und Vorlagen — direkt in Claude Code installierbar.
- Wer kein Claude Code nutzt, nimmt stattdessen **Markdown-ZIP** — das enthaelt nur die `SKILL.md` und den Unified Mini Prompt als reine Markdown-Dateien zum Einlesen in beliebige Chatbots.
- Wer nur schnell eine einzige Datei ausprobieren will, nimmt **Unified Mini Prompt**. Das ist bewusst nicht die volle Skilltiefe, sondern der verdichtete Arbeitsmodus des jeweiligen Plugins. Wegen des GitHub-Limits von 1000 Release-Assets liegen die Einzel-Mini-Prompts im Repo; als echter Datei-Download gibt es zusätzlich `alle-unified-mini-prompts.zip`.

**Wichtig:** Wenn irgendwo im Repo ein neuer Skill angelegt wird (also ein neuer Ordner `<plugin>/skills/<skill>/SKILL.md`), erscheint er beim naechsten Lauf von `scripts/generate-skills-md.py` automatisch -- sowohl in dieser Liste als auch auf der jeweiligen Plugin-Detailseite. Es kann also nichts fehlen.

Die Detailseiten liegen unter [`skills-index/`](skills-index/) -- eine eigene `.md`-Datei pro Plugin. So bleibt diese Hauptseite klein und laedt schnell, statt mit {total_skills} Tabellenzeilen den Browser-Renderer von GitHub zu ueberfordern.

"""


def plugin_overview_table(plugins: list[tuple[str, list[str]]]) -> str:
    lines = [
        "## Alle Plugins",
        "",
        "Pro Plugin: Klick auf den Namen oeffnet die Detailseite mit allen Skills, Beschreibungen und Einzel-Downloads. **Plugin-ZIP** laedt die installierbare Claude-Code-/Cowork-Sammlung. **Markdown-ZIP** laedt die reinen `SKILL.md`-Dateien plus Unified Mini Prompt. **Mini-Prompt** ist eine einzelne Markdown-Datei bis 7.500 Zeichen im Repo; echte Datei-Downloads liegen im Sammel-ZIP.",
        "",
        "| Plugin | Skills | Detailseite | Plugin-ZIP | Markdown-ZIP | Mini-Prompt |",
        "| --- | ---: | --- | --- | --- | --- |",
    ]
    for name, skills in plugins:
        zip_url = f"{GH_RELEASE}/{name}.zip"
        md_url = f"{GH_RELEASE}/{name}-skills-markdown.zip"
        mini_url = f"unified-mini-prompts/{name}.md"
        detail = f"skills-index/{name}.md"
        lines.append(
            f"| **{name}** | {len(skills)} | [Skills ansehen]({detail}) | [Plugin]({zip_url}) | [Markdown]({md_url}) | [Mini]({mini_url}) |"
        )
    lines.append("")
    return "\n".join(lines)


def plugin_detail_page(name: str, skills: list[str], version: str) -> str:
    skills_dir = REPO_ROOT / name / "skills"
    plugin_zip = f"{GH_RELEASE}/{name}.zip"
    md_zip = f"{GH_RELEASE}/{name}-skills-markdown.zip"
    mini_prompt = f"../unified-mini-prompts/{name}.md"
    plugin_readme = f"{GH_BLOB}/{name}/README.md"
    lines = [
        f"# {name}",
        "",
        f"**{len(skills)} Skills** · Stand `{version}`",
        "",
        f"- [← Zurueck zur Gesamtuebersicht](../SKILLS.md)",
        f"- [Plugin-README]({plugin_readme})",
        "",
        "## ⬇️ Downloads",
        "",
        "| Paket | Inhalt | Link |",
        "| --- | --- | --- |",
        f"| **Unified Mini Prompt** | Eine einzelne Markdown-Datei bis 7.500 Zeichen: Sparversion des Plugin-Workflows fuer Chatbots ohne Plugin-Installation | [{name}.md]({mini_prompt}) |",
        f"| **Markdown-ZIP** | Alle `SKILL.md`-Dateien plus Unified Mini Prompt als reine Markdown — echter Datei-Download fuer ChatGPT, Gemini, Mistral, Le Chat usw. | [{name}-skills-markdown.zip]({md_zip}) |",
        f"| **Plugin-ZIP** | Installierbares Claude-Code-Plugin (Skills + Hilfsdateien + Pruefrastern + Vorlagen) | [{name}.zip]({plugin_zip}) |",
        "",
        "## So benutzt man einen Skill",
        "",
        "Skills sind reine Markdown-Prompts und funktionieren in jedem Chatbot (ChatGPT, Mistral, Gemini, DeepSeek, Le Chat, ...).",
        "",
        "- **Schnelltest mit einer Datei:** den Unified Mini Prompt oben oeffnen oder aus `alle-unified-mini-prompts.zip` herunterladen und als Markdown-Datei in den Chatbot ziehen.",
        "- **Volle Markdown-Tiefe:** das Markdown-ZIP oben herunterladen, entpacken, gewuenschte `SKILL.md` als Anhang in den Chatbot ziehen oder kopieren.",
        "- **Im Browser lesen:** in der Tabelle unten `[Markdown]` klicken — die `SKILL.md` oeffnet sich auf GitHub. Inhalt mit `Strg+A` / `Cmd+A` kopieren und einfuegen.",
        "- **`[Raw .md]`** zeigt den Rohtext. Manche Browser zeigen das als Text statt als Download — fuer echte Downloads das Markdown-ZIP oben nehmen.",
        "",
        "## Skills in diesem Plugin",
        "",
        "| Skill | Beschreibung | Browser-Ansicht |",
        "| --- | --- | --- |",
    ]
    for s in skills:
        skill_md = skills_dir / s / "SKILL.md"
        desc = read_description(skill_md)
        rel_md = f"{name}/skills/{s}/SKILL.md"
        blob_url = f"{GH_BLOB}/{rel_md}"
        raw_url = f"{GH_RAW}/{rel_md}"
        lines.append(
            f"| [`{s}`]({blob_url}) | {desc} | [Markdown]({blob_url}) · [Raw .md]({raw_url}) |"
        )
    lines.append("")
    return "\n".join(lines)


def write_detail_index(plugins: list[tuple[str, list[str]]], version: str) -> str:
    """Schreibt skills-index/README.md mit Liste aller Detailseiten."""
    lines = [
        "# Skills-Index: Detailseiten pro Plugin",
        "",
        f"Eine Detailseite pro Plugin mit allen Skills, Beschreibungen und Einzel-Downloads. Stand: `{version}`.",
        "",
        "Die Aufteilung verhindert, dass GitHubs Markdown-Renderer bei 2600+ Tabellenzeilen abstuerzt oder die Seite endlos neu laedt.",
        "",
        "- [← Zurueck zur Gesamtuebersicht](../SKILLS.md)",
        "",
        "## Alle Detailseiten",
        "",
    ]
    for name, skills in plugins:
        lines.append(f"- [{name}](./{name}.md) ({len(skills)} Skills)")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    plugins = collect_plugins()
    total_skills = sum(len(skills) for _, skills in plugins)
    total_plugins = len(plugins)
    version = (
        "v" + json.loads((REPO_ROOT / ".claude-plugin" / "marketplace.json").read_text())["version"]
    )

    # 1) Schlanke Hauptseite SKILLS.md
    main_text = (
        header(total_skills, total_plugins, version)
        + plugin_overview_table(plugins)
    )
    main_text = main_text.rstrip() + "\n"
    out_main = REPO_ROOT / "SKILLS.md"
    out_main.write_text(main_text, encoding="utf-8")

    # 2) Detailseiten pro Plugin
    SKILLS_INDEX_DIR.mkdir(exist_ok=True)
    # Alte Detailseiten loeschen, falls Plugins entfernt wurden
    current_names = {name for name, _ in plugins} | {"README"}
    for old in SKILLS_INDEX_DIR.glob("*.md"):
        if old.stem not in current_names:
            old.unlink()
    for name, skills in plugins:
        page = plugin_detail_page(name, skills, version)
        (SKILLS_INDEX_DIR / f"{name}.md").write_text(page.rstrip() + "\n", encoding="utf-8")
    # Index der Detailseiten
    idx = write_detail_index(plugins, version)
    (SKILLS_INDEX_DIR / "README.md").write_text(idx.rstrip() + "\n", encoding="utf-8")

    print(
        f"SKILLS.md: {len(main_text)} Zeichen ({total_plugins} Plugins). "
        f"skills-index/: {total_plugins} Detailseiten + Index. "
        f"Insgesamt {total_skills} Skills, Stand {version}."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
