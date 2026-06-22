#!/usr/bin/env python3
"""
Audit stub exercises against program references.

Usage:
  python3 scripts/stub_audit.py                # stubs referenced by programs
  python3 scripts/stub_audit.py --all          # all stubs grouped by pattern
  python3 scripts/stub_audit.py --pattern hip_hinge  # stubs of a specific pattern
  python3 scripts/stub_audit.py --unreferenced # stubs NOT used by any program

Run build_index.py first to regenerate index files.
"""
import json
import pathlib
import argparse
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
COVERAGE_FILE = ROOT / "index" / "coverage_report.json"
PROGRAM_EX_FILE = ROOT / "index" / "program_exercise_index.json"
EXERCISES_FILE = ROOT / "index" / "exercises.json"


def load_json(path: pathlib.Path) -> dict:
    if not path.exists():
        sys.exit(f"{path.name} not found. Run: python3 scripts/build_index.py")
    return json.load(path.open())


def get_stubs(coverage: dict) -> dict[str, dict]:
    return {
        ex_id: info
        for ex_id, info in coverage.get("exercises", {}).items()
        if info.get("status") == "stub"
    }


def stubs_in_programs(stubs: dict, program_index: dict) -> list[tuple[str, list[str]]]:
    results = []
    for ex_id in sorted(stubs):
        if ex_id in program_index:
            results.append((ex_id, program_index[ex_id]))
    return results


def stubs_by_pattern(stubs: dict, exercises: dict) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = {}
    for ex_id in sorted(stubs):
        ex = exercises.get(ex_id, {})
        patterns = ex.get("pattern", ["unknown"])
        for p in patterns:
            grouped.setdefault(p, []).append(ex_id)
    return grouped


def print_program_stubs(results: list[tuple[str, list[str]]]) -> None:
    print(f"\n{'='*60}")
    print(f" Stub exercises referenced by programs: {len(results)}")
    print(f"{'='*60}\n")
    if not results:
        print("  None — all program-referenced exercises are complete.\n")
        return
    for ex_id, programs in results:
        print(f"  {ex_id}")
        for p in programs:
            print(f"    <- {p}")
        print()


def print_all_stubs(stubs: dict, exercises: dict) -> None:
    grouped = stubs_by_pattern(stubs, exercises)
    print(f"\n{'='*60}")
    print(f" All stubs by pattern (total: {len(stubs)})")
    print(f"{'='*60}\n")
    for pattern in sorted(grouped):
        ids = grouped[pattern]
        print(f"  [{pattern}] ({len(ids)})")
        for ex_id in ids:
            print(f"    {ex_id}")
        print()


def print_pattern_stubs(stubs: dict, exercises: dict, pattern: str) -> None:
    grouped = stubs_by_pattern(stubs, exercises)
    ids = grouped.get(pattern, [])
    print(f"\n  [{pattern}] stubs: {len(ids)}\n")
    for ex_id in ids:
        print(f"    {ex_id}")
    if not ids:
        print(f"    No stubs with pattern '{pattern}'.")
    print()


def print_unreferenced(stubs: dict, program_index: dict) -> None:
    unreferenced = sorted(ex_id for ex_id in stubs if ex_id not in program_index)
    print(f"\n{'='*60}")
    print(f" Unreferenced stubs (not in any program): {len(unreferenced)}")
    print(f"{'='*60}\n")
    for ex_id in unreferenced:
        print(f"  {ex_id}")
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit stub exercises")
    parser.add_argument("--all", action="store_true", help="Show all stubs grouped by pattern")
    parser.add_argument("--pattern", type=str, help="Filter stubs by movement pattern")
    parser.add_argument("--unreferenced", action="store_true", help="Show stubs not used by any program")
    args = parser.parse_args()

    coverage = load_json(COVERAGE_FILE)
    program_index = load_json(PROGRAM_EX_FILE)
    exercises = load_json(EXERCISES_FILE)

    stubs = get_stubs(coverage)

    if args.all:
        print_all_stubs(stubs, exercises)
    elif args.pattern:
        print_pattern_stubs(stubs, exercises, args.pattern)
    elif args.unreferenced:
        print_unreferenced(stubs, program_index)
    else:
        results = stubs_in_programs(stubs, program_index)
        print_program_stubs(results)


if __name__ == "__main__":
    main()
