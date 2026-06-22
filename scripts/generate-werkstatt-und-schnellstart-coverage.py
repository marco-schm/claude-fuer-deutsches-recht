#!/usr/bin/env python3
"""Schreibt docs/werkstatt-und-schnellstart-coverage.md."""

from __future__ import annotations

import json
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
DOCS = REPO / "docs"
RELEASE_BASE = "https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download"


def prompt_stem(plugin_name: str) -> str:
    if plugin_name == "liquiditaetsplanung":
        return "liquiditaetsplaner"
    if plugin_name == "staatsanwaltschaft-praxis-einstieg":
        return "staatsanwaltschaft-einstieg"
    if plugin_name.startswith("richter-"):
        return plugin_name.removeprefix("richter-")
    return plugin_name


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def source_label(path: Path) -> str:
    if not path.is_file():
        return "fehlt"
    text = path.read_text(encoding="utf-8", errors="ignore")
    if "Dieser Werkstatt-Prompt verdichtet das Plugin" in text or "Ich bin der kompakte Arbeitsmodus" in text:
        return "auto"
    return "lokal"


def main() -> int:
    DOCS.mkdir(exist_ok=True)
    plugins = json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]
    ok = 0
    lines = [
        "# Werkstatt- und Schnellstart-Coverage",
        "",
        "Diese Tabelle zeigt, ob jedes Plugin eine ausführliche Werkstatt-Datei, eine kompakte Schnellstart-Datei und die zugehörigen Release-Asset-ZIPs besitzt.",
        "",
        "| Plugin | Werkstatt-Datei | Werkstatt-Quelle | Schnellstart-Datei | Schnellstart-Quelle | Werkstatt-ZIP-Asset | Schnellstart-ZIP-Asset |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for plugin in plugins:
        name = plugin["name"]
        directory = plugin_dir(plugin)
        stem = prompt_stem(name)
        werkstatt = directory / f"{stem}-werkstatt.md"
        schnellstart = directory / f"{stem}-schnellstart.md"
        if werkstatt.is_file() and schnellstart.is_file():
            ok += 1
        werkstatt_rel = werkstatt.relative_to(REPO)
        schnellstart_rel = schnellstart.relative_to(REPO)
        lines.append(
            f"| `{name}` | [`{werkstatt.name}`](../{werkstatt_rel.as_posix()}) | {source_label(werkstatt)} | "
            f"[`{schnellstart.name}`](../{schnellstart_rel.as_posix()}) | {source_label(schnellstart)} | "
            f"[`{name}-werkstatt.zip`]({RELEASE_BASE}/{name}-werkstatt.zip) | "
            f"[`{name}-schnellstart.zip`]({RELEASE_BASE}/{name}-schnellstart.zip) |"
        )
    percent = 100 if not plugins else round(ok * 100 / len(plugins), 2)
    lines += [
        "",
        f"Gesamtcoverage: {ok} von {len(plugins)} Plugins, also {percent} Prozent.",
        "",
    ]
    (DOCS / "werkstatt-und-schnellstart-coverage.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Coverage geschrieben: {ok}/{len(plugins)} Plugins")
    return 0 if ok == len(plugins) else 1


if __name__ == "__main__":
    raise SystemExit(main())
