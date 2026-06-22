#!/usr/bin/env python3
"""Baut echte Download-ZIPs fuer Werkstatt- und Schnellstart-Prompts.

Erzeugt im Zielordner:

* <plugin>-werkstatt.zip
* <plugin>-schnellstart.zip
* alle-werkstatt-prompts.zip
* alle-schnellstart-prompts.zip
"""

from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"


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


def list_plugins() -> list[dict]:
    return json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]


def write_single_zip(out_dir: Path, plugin_name: str, prompt_path: Path, kind: str) -> Path:
    zip_path = out_dir / f"{plugin_name}-{kind}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(prompt_path, arcname=prompt_path.name)
    return zip_path


def build_combined(out_dir: Path, files: list[tuple[str, Path]], name: str) -> Path:
    zip_path = out_dir / name
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for plugin_name, path in files:
            zf.write(path, arcname=f"{plugin_name}/{path.name}")
    return zip_path


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: build-werkstatt-und-schnellstart-bundles.py <output-dir>", file=sys.stderr)
        return 2
    out_dir = Path(sys.argv[1]).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    werkstatt_files: list[tuple[str, Path]] = []
    schnellstart_files: list[tuple[str, Path]] = []
    missing: list[str] = []

    for plugin in list_plugins():
        name = plugin["name"]
        directory = plugin_dir(plugin)
        stem = prompt_stem(name)
        werkstatt = directory / f"{stem}-werkstatt.md"
        schnellstart = directory / f"{stem}-schnellstart.md"
        if not werkstatt.is_file() or not schnellstart.is_file():
            missing.append(name)
            continue
        write_single_zip(out_dir, name, werkstatt, "werkstatt")
        write_single_zip(out_dir, name, schnellstart, "schnellstart")
        werkstatt_files.append((name, werkstatt))
        schnellstart_files.append((name, schnellstart))

    if missing:
        print("Fehlende Prompt-Dateien:", file=sys.stderr)
        for name in missing:
            print(f"  - {name}", file=sys.stderr)
        return 1

    build_combined(out_dir, werkstatt_files, "alle-werkstatt-prompts.zip")
    build_combined(out_dir, schnellstart_files, "alle-schnellstart-prompts.zip")
    print(f"Werkstatt-/Schnellstart-Bundles gebaut: {len(werkstatt_files)} Plugins")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
