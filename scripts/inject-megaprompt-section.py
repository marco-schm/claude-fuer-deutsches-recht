#!/usr/bin/env python3
"""Fuegt in jede <plugin>/README.md die 'Megaprompt'-Sektion ein, sofern
ein passender Megaprompt unter testakten/megaprompts/<plugin>.md existiert
und der Block noch nicht vorhanden ist.

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

RAW_BASE = "https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts"
RELEASE_BASE = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download"


def block_for(plugin: str, kb: int) -> str:
    return f"""{BEGIN}
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt als Datei herunterladen** (empfohlen): [`{plugin}-megaprompt.md`]({RELEASE_BASE}/{plugin}-megaprompt.md) ({kb} KB) — Release-Asset, wird vom Browser als Datei gespeichert.
- Im Browser ansehen: [`{plugin}.md`]({RAW_BASE}/{plugin}.md) — wird als Text gerendert, nicht heruntergeladen.
- Im Repo: [`testakten/megaprompts/{plugin}.md`](../testakten/megaprompts/{plugin}.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

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
    new_block = block_for(plugin_dir.name, kb)
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
