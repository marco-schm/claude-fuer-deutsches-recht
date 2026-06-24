#!/usr/bin/env python3
"""Baut die Testakten-ZIPs fuer Releases.

Die ZIPs enthalten die Arbeitsdateien und das Gesamt-PDF, aber keine
repo-internen README-, Download- oder Vorfuehrseiten. Damit entspricht der
Download eher einem echten Aktenordner als einer Demo-Mappe.
"""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path

from testakte_file_filter import include_in_working_dump

REPO_ROOT = Path(__file__).resolve().parent.parent
TESTAKTEN = REPO_ROOT / "testakten"
SKIP_DIRS = {
    "megaprompts",
}


def iter_export_files(testakte_dir: Path):
    for path in sorted(testakte_dir.rglob("*"), key=lambda p: str(p.relative_to(testakte_dir)).lower()):
        if include_in_working_dump(path, testakte_dir, include_gesamt_pdf=True):
            yield path


def add_testakte(zipf: zipfile.ZipFile, testakte_dir: Path) -> int:
    count = 0
    for path in iter_export_files(testakte_dir):
        arcname = Path(testakte_dir.name) / path.relative_to(testakte_dir)
        zipf.write(path, arcname.as_posix())
        count += 1
    return count


def build_single(testakte_dir: Path, dist: Path) -> tuple[Path, int]:
    out = dist / f"testakte-{testakte_dir.name}.zip"
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
        count = add_testakte(zipf, testakte_dir)
    return out, count


def main() -> None:
    dist = Path(sys.argv[1]) if len(sys.argv) > 1 else REPO_ROOT / "dist"
    dist.mkdir(parents=True, exist_ok=True)
    dirs = sorted(d for d in TESTAKTEN.iterdir() if d.is_dir() and d.name not in SKIP_DIRS)
    if not dirs:
        print("Keine Testakten gefunden.")
        return

    total_files = 0
    for d in dirs:
        out, count = build_single(d, dist)
        if count == 0:
            raise SystemExit(f"{d}: keine exportfaehigen Dateien")
        total_files += count
        print(f"Baue {out.name}: {count} Dateien")

    all_out = dist / "alle-testakten.zip"
    with zipfile.ZipFile(all_out, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
        all_count = 0
        for d in dirs:
            all_count += add_testakte(zipf, d)
    print(f"Baue {all_out.name}: {all_count} Dateien aus {len(dirs)} Testakten")
    print(f"Fertig: {len(dirs)} Einzel-ZIPs, {total_files} Dateien")


if __name__ == "__main__":
    main()
