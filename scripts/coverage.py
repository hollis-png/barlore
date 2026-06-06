#!/usr/bin/env python3
"""
Print a human-readable coverage report from index/coverage_report.json.

Usage:
  python3 scripts/coverage.py               # full report
  python3 scripts/coverage.py --exercises   # exercise completeness table
  python3 scripts/coverage.py --muscles     # muscle coverage table
  python3 scripts/coverage.py --systems     # system completeness table
  python3 scripts/coverage.py --todo        # priority TODO list only

Run build_index.py first to regenerate coverage_report.json.
"""
import json
import pathlib
import argparse
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPORT_FILE = ROOT / "index" / "coverage_report.json"

TICK  = "✅"
STUB  = "🪨"   # exists but stub
MISS  = "❌"
DASH  = "—"    # not applicable


def load() -> dict:
    if not REPORT_FILE.exists():
        sys.exit("index/coverage_report.json not found.\n"
                 "Run: python3 scripts/build_index.py")
    return json.load(REPORT_FILE.open())


# ── Formatting helpers ────────────────────────────────────────────────────────

def bar(filled: int, total: int, width: int = 20) -> str:
    if total == 0:
        return "[" + " " * width + "] n/a"
    pct = filled / total
    n = round(pct * width)
    return f"[{'█' * n}{'░' * (width - n)}] {filled}/{total} ({pct:.0%})"


def cell(val) -> str:
    """Render a coverage cell value."""
    if val is True:
        return TICK
    if val is False:
        return MISS
    if val == "stub":
        return STUB
    if val == "partial":
        return "🔶"
    if val == "complete":
        return TICK
    if val is None:
        return DASH
    return str(val)


def print_table(headers: list, rows: list, col_width: int = 14):
    widths = [max(len(str(h)), col_width) for h in headers]
    widths[0] = max(len(r[0]) for r in rows) + 2  # name col

    sep = "  "
    header = sep.join(str(h).ljust(w) for h, w in zip(headers, widths))
    print(header)
    print("─" * len(header))
    for row in rows:
        print(sep.join(str(c).ljust(w) for c, w in zip(row, widths)))


# ── Sections ─────────────────────────────────────────────────────────────────

def section_exercises(report: dict):
    exercises = report["exercises"]

    print("\n" + "═" * 72)
    print("  EXERCISE COVERAGE MATRIX")
    print("═" * 72)

    # Status summary first
    by_status = {}
    for ex in exercises.values():
        s = ex.get("status", "unknown")
        by_status[s] = by_status.get(s, 0) + 1

    print(f"\n  Total exercises : {len(exercises)}")
    for s, n in sorted(by_status.items()):
        icon = cell(s)
        print(f"  {icon}  {s:12s} : {n}")

    # Completeness columns: status, EMG, ROM, strength_curve, in programs
    headers = ["exercise", "status", "EMG", "ROM", "curve", "in programs"]

    complete_rows = []
    stub_rows     = []

    for ex_id, ex in sorted(exercises.items()):
        status = ex.get("status", "unknown")
        row = [
            ex_id,
            cell(status),
            TICK if ex.get("has_emg")           else MISS,
            TICK if ex.get("has_rom")            else MISS,
            TICK if ex.get("has_strength_curve") else MISS,
            str(ex.get("program_count", 0)),
        ]
        if status in ("complete", "partial"):
            complete_rows.append(row)
        else:
            stub_rows.append(row)

    if complete_rows:
        print(f"\n  ── Human-reviewed ({len(complete_rows)}) ──\n")
        print_table(headers, complete_rows)

    if stub_rows:
        shown = stub_rows[:30]
        print(f"\n  ── Stubs ({len(stub_rows)}, showing first 30) ──\n")
        print_table(headers, shown)
        if len(stub_rows) > 30:
            print(f"\n  ... and {len(stub_rows) - 30} more stubs")


def section_muscles(report: dict):
    muscle_cov = report["muscle_coverage"]

    print("\n" + "═" * 72)
    print("  MUSCLE COVERAGE")
    print("═" * 72)
    print()

    headers = ["muscle / group", "exercises", "with EMG", "bar"]
    rows = []
    for mid, info in sorted(muscle_cov.items()):
        n_ex  = info["exercise_count"]
        n_emg = info["emg_count"]
        rows.append([
            mid,
            str(n_ex),
            str(n_emg),
            bar(n_emg, n_ex),
        ])

    # Sort by EMG coverage ascending (most gaps first)
    rows.sort(key=lambda r: int(r[1]) - int(r[2]))
    print_table(headers, rows, col_width=10)


def section_systems(report: dict):
    systems = report["system_coverage"]

    print("\n" + "═" * 72)
    print("  SYSTEM COMPLETENESS")
    print("═" * 72)
    print()

    headers = ["system", "index.md", "programs", "ex. coverage", "core links"]
    rows = []
    for sid, info in sorted(systems.items()):
        ex_cov = bar(info["exercises_covered"], info["exercise_count"], width=15)
        rows.append([
            sid,
            cell(info["has_index"]),
            str(info["program_count"]),
            ex_cov,
            str(info["core_refs"]),
        ])
    print_table(headers, rows, col_width=12)


def section_todo(report: dict):
    print("\n" + "═" * 72)
    print("  PRIORITY TODO  (highest-impact gaps)")
    print("═" * 72)
    print()

    exercises = report["exercises"]
    systems   = report["systems_defined"]

    # 1. Exercises with program refs but no EMG (good content, missing quantification)
    want_emg = [
        ex_id for ex_id, ex in exercises.items()
        if not ex.get("has_emg")
        and ex.get("status") in ("partial", "complete")
        and ex.get("program_count", 0) > 0
    ]
    if want_emg:
        print(f"  📊  Add EMG data ({len(want_emg)} exercises in programs but no EMG):")
        for ex_id in want_emg[:10]:
            print(f"       • {ex_id}")
        if len(want_emg) > 10:
            print(f"       … and {len(want_emg) - 10} more")
        print()

    # 2. Reviewed exercises not referenced by any program
    no_program = [
        ex_id for ex_id, ex in exercises.items()
        if ex.get("status") in ("partial", "complete")
        and ex.get("program_count", 0) == 0
    ]
    if no_program:
        print(f"  🔍  Exercises with no program reference ({len(no_program)} reviewed "
              f"exercises not yet used in any program):")
        for ex_id in no_program[:10]:
            print(f"       • {ex_id}")
        if len(no_program) > 10:
            print(f"       … and {len(no_program) - 10} more")
        print()

    # 3. Systems without index.md
    sys_cov = report["system_coverage"]
    no_index = [s for s, info in sys_cov.items() if not info["has_index"]]
    if no_index:
        print(f"  📁  Create index.md for systems: {', '.join(no_index)}")
        print()

    # 4. Systems with no programs yet
    no_programs = [
        s for s, info in sys_cov.items() if info["program_count"] == 0
    ]
    if no_programs:
        print(f"  📋  Systems with no programs yet: {', '.join(no_programs)}")
        print()

    # 5. Stubs to promote (have muscles + instructions, ready for review)
    ready = [
        ex_id for ex_id, ex in exercises.items()
        if ex.get("status") == "stub"
        and ex.get("muscle_count", 0) >= 2
    ]
    print(f"  🪨  Stub exercises ready for first review: {len(ready)}")
    if ready:
        for ex_id in ready[:8]:
            print(f"       • {ex_id}")
        if len(ready) > 8:
            print(f"       … and {len(ready) - 8} more")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--exercises", action="store_true")
    ap.add_argument("--muscles",   action="store_true")
    ap.add_argument("--systems",   action="store_true")
    ap.add_argument("--todo",      action="store_true")
    args = ap.parse_args()

    report = load()
    ts = report.get("generated_at", "unknown")
    print(f"\nCoverage report  ·  generated {ts}")

    all_sections = not any([args.exercises, args.muscles, args.systems, args.todo])

    if all_sections or args.exercises:
        section_exercises(report)
    if all_sections or args.muscles:
        section_muscles(report)
    if all_sections or args.systems:
        section_systems(report)
    if all_sections or args.todo:
        section_todo(report)

    print()


if __name__ == "__main__":
    main()
