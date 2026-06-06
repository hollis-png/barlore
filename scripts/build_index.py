#!/usr/bin/env python3
"""
Build the index/ JSON files for the fitness encyclopedia.

Single source of truth: each lens entry declares `exercise_ref`. The exercise
base entries do NOT hand-write their lens list — this script generates the
reverse mapping by scanning all lenses, so the two can never drift out of sync.

Outputs:
  index/exercises.json       flat list of exercise base entries + their metadata
  index/lenses.json          flat list of lens entries
  index/cross_reference.json base -> {base path, lenses by system}

Usage: python3 scripts/build_index.py [--check]
  --check  exit non-zero if generated output differs from committed files
           (useful in CI / pre-commit)

Dependencies: PyYAML  (pip install pyyaml --break-system-packages)
"""
import sys
import json
import pathlib
import argparse

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml --break-system-packages")

ROOT = pathlib.Path(__file__).resolve().parent.parent
INDEX_DIR = ROOT / "index"


def parse_front_matter(path: pathlib.Path) -> dict:
    """Extract YAML front matter from a markdown file. Returns {} if none."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        data = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as e:
        print(f"  ! YAML error in {rel(path)}: {e}", file=sys.stderr)
        return {}
    return data


def rel(path: pathlib.Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def collect_exercises() -> dict:
    out = {}
    for md in sorted((ROOT / "exercises").glob("*.md")):
        fm = parse_front_matter(md)
        if fm.get("category") != "exercise":
            continue
        ex_id = fm.get("id")
        if not ex_id:
            print(f"  ! missing id in {rel(md)}", file=sys.stderr)
            continue
        out[ex_id] = {
            "id": ex_id,
            "name": fm.get("name"),
            "aliases": fm.get("aliases", []),
            "pattern": fm.get("pattern", []),
            "muscles_primary": fm.get("muscles_primary", []),
            "muscles_secondary": fm.get("muscles_secondary", []),
            "equipment": fm.get("equipment", []),
            "difficulty": fm.get("difficulty"),
            "path": rel(md),
        }
    return out


def collect_lenses() -> list:
    out = []
    for md in sorted((ROOT / "systems").rglob("lenses/*.md")):
        fm = parse_front_matter(md)
        if not fm.get("exercise_ref"):
            continue
        out.append({
            "id": fm.get("id"),
            "system": fm.get("system"),
            "exercise_ref": fm.get("exercise_ref"),
            "lens_type": fm.get("lens_type"),
            "competition_relevant": fm.get("competition_relevant", False),
            "related_programs": fm.get("related_programs", []),
            "path": rel(md),
        })
    return out


def build_cross_reference(exercises: dict, lenses: list) -> dict:
    xref = {}
    for ex_id, ex in exercises.items():
        xref[ex_id] = {"base": ex["path"], "lenses": {}}
    for lens in lenses:
        ref = lens["exercise_ref"]
        if ref not in xref:
            print(f"  ! lens {lens['path']} references unknown exercise "
                  f"'{ref}' (no base entry)", file=sys.stderr)
            xref[ref] = {"base": None, "lenses": {}}
        system = lens["system"]
        if system in xref[ref]["lenses"]:
            print(f"  ! duplicate lens for '{ref}' in system '{system}'",
                  file=sys.stderr)
        xref[ref]["lenses"][system] = lens["path"]
    return xref


def write_json(name: str, data, check: bool) -> bool:
    """Write or, in check mode, compare. Returns True if up to date."""
    path = INDEX_DIR / name
    new = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if check:
        old = path.read_text(encoding="utf-8") if path.exists() else ""
        if old != new:
            print(f"  ✗ {name} is OUT OF DATE", file=sys.stderr)
            return False
        print(f"  ✓ {name} up to date")
        return True
    INDEX_DIR.mkdir(exist_ok=True)
    path.write_text(new, encoding="utf-8")
    print(f"  → wrote {name}")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="verify index is current without writing")
    args = ap.parse_args()

    print("Scanning encyclopedia...")
    exercises = collect_exercises()
    lenses = collect_lenses()
    xref = build_cross_reference(exercises, lenses)
    print(f"  found {len(exercises)} exercises, {len(lenses)} lenses")

    ok = True
    ok &= write_json("exercises.json", exercises, args.check)
    ok &= write_json("lenses.json", lenses, args.check)
    ok &= write_json("cross_reference.json", xref, args.check)

    if args.check and not ok:
        sys.exit("Index out of date. Run: python3 scripts/build_index.py")
    print("Done.")


if __name__ == "__main__":
    main()
