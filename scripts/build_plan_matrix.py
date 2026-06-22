#!/usr/bin/env python3
"""
Generate the programs decision matrix for plan_generator.md Section C.1.

Usage:
  python3 scripts/build_plan_matrix.py

Prints a Markdown table to stdout. Copy-paste into plan_generator.md Section C.1.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROGRAMS_FILE = ROOT / "index" / "programs.json"


def main() -> None:
    programs = json.load(PROGRAMS_FILE.open())

    rows: list[tuple[str, str, str, str, str]] = []
    for pid, p in programs.items():
        rows.append((
            p.get("system", ""),
            p.get("level", ""),
            pid,
            p.get("name", ""),
            p.get("periodization") or "—",
        ))

    rows.sort(key=lambda r: (r[0], r[1], r[2]))

    print("| system | level | program_id | name | periodization |")
    print("|--------|-------|------------|------|---------------|")
    for system, level, pid, name, period in rows:
        print(f"| {system} | {level} | {pid} | {name} | {period} |")


if __name__ == "__main__":
    main()
