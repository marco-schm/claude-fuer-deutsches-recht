#!/usr/bin/env python3
"""Fuegt in jede <plugin>/README.md eine kurze Megaprompt-Hinweissektion ein,
sofern ein passender Megaprompt unter testakten/megaprompts/<plugin>.md
existiert und der Block noch nicht vorhanden ist.

Idempotent ueber HTML-Marker. Position: ans Ende der Datei (gleich der
ueblichen Konvention; move-megaprompt-block-to-end.py kann den Block
spaeter umsortieren).
"""
from __future__ import annotations
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MEGA_DIR = REPO / "testakten" / "megaprompts"

BEGIN = "<!-- BEGIN megaprompt-und-vorlagen (autogen) -->"
END = "<!-- END megaprompt-und-vorlagen (autogen) -->"

RELEASE_BASE = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download"


def block_for(plugin: str, kb: int, local_mega_kb: int | None) -> str:
    local_line = ""
    if local_mega_kb is not None:
        local_line = (
            f"- **Handgepflegter Werkstatt-Mega-Prompt im Plugin-Ordner:** "
            f"[`{plugin}-megaprompt.md`](./{plugin}-megaprompt.md) ({local_mega_kb} KB) "
            "\u2014 kuratiert, dichter als das automatisch erzeugte Bundle.\n"
        )
    return f"""{BEGIN}
## Experimentell: dieses Plugin auch ohne Claude Code

### Unified Mini Prompt und Mega-Prompt

Für normale Chatbots ohne Plugin-Installation gibt es den **Unified Mini Prompt**: eine einzelne Markdown-Datei bis 7.500 Zeichen, die den Kern-Workflow dieses Plugins verdichtet. Die Einzeldatei liegt im Repo; als echter Datei-Download gibt es zusätzlich das Sammel-ZIP aller Mini-Prompts.

- **Sparversion öffnen:** [`unified-mini-prompts/{plugin}.md`](../unified-mini-prompts/{plugin}.md)
- **Alle Mini-Prompts als ZIP herunterladen:** [`alle-unified-mini-prompts.zip`]({RELEASE_BASE}/alle-unified-mini-prompts.zip)
{local_line}- **Großer Mega-Prompt nur zur Anschauung im Repo:** [`testakten/megaprompts/{plugin}.md`](../testakten/megaprompts/{plugin}.md) ({kb} KB)

Der große Mega-Prompt wird nicht als installierbares Plugin und nicht als CoWork-Uploadmaterial ausgeliefert. Für echte Plugin-Nutzung bitte das Plugin-ZIP verwenden; für Ein-Datei-Nutzung den Unified Mini Prompt.

{END}
"""


def process(plugin_dir: Path) -> str:
    readme = plugin_dir / "README.md"
    if not readme.exists():
        return "skip-no-readme"
    mega = MEGA_DIR / f"{plugin_dir.name}.md"
    if not mega.exists():
        return "skip-no-megaprompt"
    text = readme.read_text(encoding="utf-8")
    kb = max(1, mega.stat().st_size // 1024)
    local_mega = plugin_dir / f"{plugin_dir.name}-megaprompt.md"
    local_kb = max(1, local_mega.stat().st_size // 1024) if local_mega.exists() else None
    new_block = block_for(plugin_dir.name, kb, local_kb)
    if BEGIN in text:
        # Update vorhandenen Block (z. B. Groessenangabe)
        new_text = re.sub(
            re.escape(BEGIN) + r".*?" + re.escape(END) + r"\n?",
            new_block,
            text,
            count=1,
            flags=re.DOTALL,
        )
        if new_text == text:
            return "unchanged"
        readme.write_text(new_text, encoding="utf-8")
        return "updated"
    # Anfuegen ans Ende
    sep = "" if text.endswith("\n") else "\n"
    readme.write_text(text + sep + "\n" + new_block, encoding="utf-8")
    return "added"


def main() -> None:
    added = updated = unchanged = skipped = 0
    for p in sorted(REPO.iterdir()):
        if not p.is_dir():
            continue
        if p.name.startswith(".") or p.name.startswith("_"):
            continue
        if p.name in {"scripts", "testakten", "docs", "audits", "node_modules",
                      "recherche", "references", "skills-index", "tests",
                      "anthropic-lessons", "anlagen-zu-schriftsaetzen-archiv"}:
            continue
        result = process(p)
        if result == "added":
            added += 1
            print(f"  added: {p.name}")
        elif result == "updated":
            updated += 1
        elif result == "unchanged":
            unchanged += 1
        else:
            skipped += 1
    print(f"\nadded={added} updated={updated} unchanged={unchanged} skipped={skipped}")


if __name__ == "__main__":
    main()
