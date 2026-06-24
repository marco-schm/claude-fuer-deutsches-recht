#!/usr/bin/env python3
"""Baut Release-Assets für Werkstatt- und Schnellstart-Prompts.

Erzeugt im Zielordner:
  - alle-werkstatt-prompts.zip
  - alle-schnellstart-prompts.zip
  - je Plugin die einzelne <plugin>-werkstatt.md
  - je Plugin die einzelne <plugin>-schnellstart.md
"""

from __future__ import annotations

import json
import shutil
import sys
import zipfile
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def list_plugins() -> list[dict]:
    return json.loads(MARKETPLACE.read_text(encoding="utf-8"))["plugins"]


def copy_and_zip(out_dir: Path, suffix: str, bundle_name: str) -> int:
    plugins = list_plugins()
    copied: list[Path] = []
    for plugin in plugins:
        name = plugin["name"]
        src = plugin_dir(plugin) / f"{name}-{suffix}.md"
        if not src.is_file():
            raise FileNotFoundError(f"{src}: Prompt-Datei fehlt")
        dst = out_dir / src.name
        shutil.copy2(src, dst)
        copied.append(dst)

    bundle = out_dir / bundle_name
    with zipfile.ZipFile(bundle, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
        for path in sorted(copied, key=lambda p: p.name):
            zipf.write(path, arcname=path.name)
    return len(copied)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: build-werkstatt-schnellstart-sammelzips.py <output-dir>", file=sys.stderr)
        return 2

    out_dir = Path(sys.argv[1]).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    werkstatt = copy_and_zip(out_dir, "werkstatt", "alle-werkstatt-prompts.zip")
    schnellstart = copy_and_zip(out_dir, "schnellstart", "alle-schnellstart-prompts.zip")
    print(f"Werkstatt-Prompts als Markdown-Assets gebaut: {werkstatt}")
    print(f"Schnellstart-Prompts als Markdown-Assets gebaut: {schnellstart}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
