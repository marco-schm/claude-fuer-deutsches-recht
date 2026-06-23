#!/usr/bin/env python3
"""Synchronisiert pro Plugin den Schnellstart-Prompt als ladbaren Skill.

Quelle ist jeweils <plugin>/<plugin>-schnellstart.md. Ziel ist
<plugin>/skills/<plugin>-schnellstart/SKILL.md. Der H1-Titel der
Schnellstart-Datei wird im Skill-Body entfernt, damit SKILL.md genau eine
Frontmatter-Rolle und danach die H2-Struktur des Prompts enthält.
"""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"

OLD_WRAPPER_PATTERNS = (
    "-schnellstart-skill",
    "-mini-skill",
    "-kleiner-prompt-skill",
)


def load_plugins() -> list[dict]:
    return json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def strip_h1(markdown: str) -> tuple[str, str]:
    lines = markdown.replace("\ufeff", "").splitlines()
    title = ""
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
    body = "\n".join(lines).strip() + "\n"
    return title, body


def sanitize_description(text: str, plugin_name: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("§§", "Paragrafen").replace("§", "Paragraf")
    text = text.replace("<", "[").replace(">", "]")
    text = text.replace('"', "'")
    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\d\s*,\s*\d", lambda m: m.group(0).replace(",", " und "), text)
    if not text:
        text = f"Schnellstart-Skill fuer das Plugin {plugin_name}: kompakter Einstieg, Triage, Kurzweg, Anker, Antwortform und Stop-Kriterium."
    if len(text) > 900:
        text = text[:897].rstrip(" ,.;:-") + "..."
    return text


def yaml_single_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def wrapper_is_old(skill_dir: Path, target_name: str) -> bool:
    if skill_dir.name == target_name:
        return False
    return any(pattern in skill_dir.name for pattern in OLD_WRAPPER_PATTERNS)


def sync_one(plugin: dict) -> str:
    name = plugin["name"]
    directory = plugin_dir(plugin)
    schnellstart = directory / f"{name}-schnellstart.md"
    if not schnellstart.is_file():
        return "MISSING"

    title, body = strip_h1(schnellstart.read_text(encoding="utf-8"))
    first_sentence = ""
    for line in body.splitlines():
        if line.strip() and not line.startswith("#"):
            first_sentence = line.strip()
            break
    desc = sanitize_description(first_sentence or title, name)

    skills_dir = directory / "skills"
    skills_dir.mkdir(exist_ok=True)
    target_dir = skills_dir / f"{name}-schnellstart"
    target_dir.mkdir(exist_ok=True)
    target = target_dir / "SKILL.md"

    content = "\n".join(
        [
            "---",
            f"name: {yaml_single_quote(target_dir.name)}",
            f"description: {yaml_single_quote(desc)}",
            "---",
            "",
            body.rstrip(),
            "",
        ]
    )
    status = "UNCHANGED"
    if not target.is_file() or target.read_text(encoding="utf-8") != content:
        target.write_text(content, encoding="utf-8")
        status = "UPDATED"

    removed = 0
    for child in list(skills_dir.iterdir()):
        if child.is_dir() and wrapper_is_old(child, target_dir.name):
            shutil.rmtree(child)
            removed += 1
    if removed:
        status = f"{status}+REMOVED{removed}"
    return status


def main() -> int:
    counts: dict[str, int] = {}
    for plugin in load_plugins():
        status = sync_one(plugin)
        counts[status] = counts.get(status, 0) + 1
        if status != "UNCHANGED":
            print(f"{status:18s} {plugin['name']}")
    print("Schnellstart-Skills synchronisiert:")
    for key in sorted(counts):
        print(f"  {key}: {counts[key]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
