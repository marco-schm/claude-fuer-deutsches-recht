#!/usr/bin/env python3
"""Fuegt pro Plugin einen Direkt-loslegen-Block fuer Prompt-Downloads ein.

Der Block steht nach dem H1 und nach einer vorhandenen Sofort-Download-Sektion.
Alte Megaprompt-Hinweisbloecke werden entfernt, damit die README nicht zwei
konkurrierende Ein-Datei-Pfade beschreibt.
"""

from __future__ import annotations

import json
import re
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"

BEGIN = "<!-- BEGIN direkt-loslegen (autogen) -->"
END = "<!-- END direkt-loslegen (autogen) -->"
OLD_MEGA_BEGIN = "<!-- BEGIN megaprompt-und-vorlagen (autogen) -->"
OLD_MEGA_END = "<!-- END megaprompt-und-vorlagen (autogen) -->"
SOFORT_END = "<!-- END plugin-sofort-download-section (autogen) -->"
RELEASE_BASE = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download"


def prompt_stem(plugin_name: str) -> str:
    if plugin_name == "liquiditaetsplanung":
        return "liquiditaetsplaner"
    if plugin_name == "staatsanwaltschaft-praxis-einstieg":
        return "staatsanwaltschaft-einstieg"
    if plugin_name.startswith("richter-"):
        return plugin_name.removeprefix("richter-")
    return plugin_name


def human_title(slug: str) -> str:
    words = [w for w in re.split(r"[-_]+", slug) if w]
    out = []
    for word in words:
        if word in {"und", "oder", "mit", "im", "am", "zur", "zum", "der", "die", "das"}:
            out.append(word)
        elif word == "fuer":
            out.append("für")
        elif len(word) <= 3:
            out.append(word.upper())
        else:
            out.append(word[:1].upper() + word[1:])
    return " ".join(out)


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def readme_title(directory: Path, fallback: str) -> str:
    readme = directory / "README.md"
    if readme.is_file():
        for line in readme.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    return human_title(fallback)


def block(plugin_name: str, directory: Path) -> str:
    stem = prompt_stem(plugin_name)
    title = readme_title(directory, plugin_name)
    werkstatt_file = f"{stem}-werkstatt.md"
    schnellstart_file = f"{stem}-schnellstart.md"
    display = title.replace("`", "").strip()
    return f"""{BEGIN}
## Direkt loslegen ohne Plugin-Setup

Wer kein Claude-Code-Plugin nutzen kann, bekommt hier zwei mundgerecht zugeschnittene Markdown-Prompts. Beide funktionieren in jedem Chatbot deiner Wahl als Instant-Personalisierung. Du klickst auf den Download, die Datei landet im Download-Ordner, dann ziehst du sie in ChatGPT, Gemini, Mistral, Le Chat oder ein anderes System. Fertig.

| Prompt | Wofür | Direkt-Download |
| --- | --- | --- |
| **{display}-Werkstatt** | Vollständiger Arbeits-Prompt mit Werkstattlogik, Pflicht-Schritten, Quellen-Disziplin und Antwort-Skeletten. Darf lang sein. | [`{plugin_name}-werkstatt.zip`]({RELEASE_BASE}/{plugin_name}-werkstatt.zip) |
| **{display}-Schnellstart** | Kompakter Einstiegs-Prompt, höchstens 7.500 Zeichen. Für den schnellen Wurf in einen Chat. | [`{plugin_name}-schnellstart.zip`]({RELEASE_BASE}/{plugin_name}-schnellstart.zip) |

Wer die Markdown-Datei lieber im Browser ansehen statt herunterladen will:
- [`{werkstatt_file}`](./{werkstatt_file}) (im Browser ansehen)
- [`{schnellstart_file}`](./{schnellstart_file}) (im Browser ansehen)
{END}"""


def strip_old_blocks(text: str) -> str:
    for begin, end in [(BEGIN, END), (OLD_MEGA_BEGIN, OLD_MEGA_END)]:
        if begin in text and end in text:
            text = re.sub(
                r"\n*" + re.escape(begin) + r"[\s\S]*?" + re.escape(end) + r"\n*",
                "\n",
                text,
                count=1,
            )
    return text


def insert_position(text: str) -> int:
    if SOFORT_END in text:
        pos = text.index(SOFORT_END) + len(SOFORT_END)
        while pos < len(text) and text[pos] == "\n":
            pos += 1
        return pos
    match = re.search(r"^# .+$", text, flags=re.MULTILINE)
    if not match:
        return 0
    pos = match.end()
    while pos < len(text) and text[pos] == "\n":
        pos += 1
    return pos


def inject(plugin: dict) -> str:
    name = plugin["name"]
    directory = plugin_dir(plugin)
    readme = directory / "README.md"
    if not readme.is_file():
        return "SKIPPED"
    text = readme.read_text(encoding="utf-8")
    stripped = strip_old_blocks(text)
    pos = insert_position(stripped)
    new_text = stripped[:pos].rstrip() + "\n\n" + block(name, directory) + "\n\n" + stripped[pos:].lstrip()
    if new_text == text:
        return "UNCHANGED"
    readme.write_text(new_text, encoding="utf-8")
    return "UPDATED" if BEGIN in text else "INSERTED"


def main() -> int:
    plugins = json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]
    counts = {"INSERTED": 0, "UPDATED": 0, "UNCHANGED": 0, "SKIPPED": 0}
    for plugin in plugins:
        status = inject(plugin)
        counts[status] += 1
        if status in {"INSERTED", "UPDATED"}:
            print(f"{status:8s} {plugin['name']}")
    print(
        f"Fertig: {counts['INSERTED']} neu, {counts['UPDATED']} aktualisiert, "
        f"{counts['UNCHANGED']} unveraendert, {counts['SKIPPED']} uebersprungen"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
