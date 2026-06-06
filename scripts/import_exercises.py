#!/usr/bin/env python3
"""
Import exercises from free-exercise-db into the encyclopedia as stub entries.

Source: https://github.com/yuhonas/free-exercise-db
License: Public Domain

Each imported exercise gets:
  - status: stub            (flags it as auto-imported, needs human review)
  - muscles[] derived from primaryMuscles / secondaryMuscles
  - difficulty from level field
  - pattern inferred from category + mechanic + force
  - A minimal prose body with the original instructions

Entries that already exist (matching id) are SKIPPED unless --overwrite is passed.

Usage:
  python3 scripts/import_exercises.py [--source PATH] [--dry-run] [--overwrite]
  python3 scripts/import_exercises.py --source /tmp/free_exercise_db.json

Dependencies: PyYAML, requests  (pip install pyyaml requests --break-system-packages)
"""
import sys
import json
import re
import pathlib
import argparse
import textwrap

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml --break-system-packages")

ROOT = pathlib.Path(__file__).resolve().parent.parent
EXERCISES_DIR = ROOT / "exercises"
SOURCE_URL = (
    "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/dist/exercises.json"
)

# ── Mapping tables ────────────────────────────────────────────────────────────

# free-exercise-db muscle name -> list of canonical ids from muscles.yaml
MUSCLE_MAP = {
    "abdominals":   ["rectus_abdominis"],
    "abductors":    ["gluteus_medius"],
    "adductors":    ["adductor_magnus", "adductor_longus"],
    "biceps":       ["biceps_brachii"],
    "calves":       ["gastrocnemius", "soleus"],
    "chest":        ["pectoralis_major"],
    "forearms":     ["forearm_flexors"],
    "glutes":       ["gluteus_maximus"],
    "hamstrings":   ["biceps_femoris", "semitendinosus"],
    "lats":         ["latissimus_dorsi"],
    "lower back":   ["erector_spinae", "multifidus"],
    "middle back":  ["rhomboids", "trapezius"],
    "neck":         ["trapezius"],          # closest available
    "quadriceps":   ["rectus_femoris", "vastus_lateralis", "vastus_medialis"],
    "shoulders":    ["deltoid"],
    "traps":        ["trapezius"],
    "triceps":      ["triceps_brachii"],
}

# free-exercise-db category -> pattern list
PATTERN_MAP = {
    "strength":             None,       # derive from force + mechanic below
    "powerlifting":         None,
    "olympic weightlifting": None,
    "plyometrics":          ["plyometric"],
    "stretching":           ["stretch"],
    "strongman":            ["carry"],
    "cardio":               ["cardio"],
}

# (force, mechanic) -> pattern
FORCE_MECHANIC_PATTERN = {
    ("push",   "compound"):   ["horizontal press"],   # rough defaults
    ("push",   "isolation"):  ["horizontal press"],
    ("pull",   "compound"):   ["hinge"],
    ("pull",   "isolation"):  ["vertical pull"],
    ("static", "compound"):   ["squat"],
    ("static", "isolation"):  ["squat"],
    (None,     "compound"):   ["squat"],
    (None,     "isolation"):  ["squat"],
    (None,     None):         ["squat"],
}

# difficulty passthrough
LEVEL_MAP = {
    "beginner":     "beginner",
    "intermediate": "intermediate",
    "expert":       "advanced",
}


def make_id(raw_id: str) -> str:
    """Convert free-exercise-db id (e.g. '3_4_Sit-Up') to snake_case."""
    s = raw_id.lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = s.strip("_")
    return s


def infer_pattern(entry: dict) -> list:
    cat   = entry.get("category", "")
    force = entry.get("force")
    mech  = entry.get("mechanic")
    name  = entry.get("name", "").lower()

    # Named pattern overrides
    if any(k in name for k in ["squat", "lunge", "leg press", "step up"]):
        return ["squat"]
    if any(k in name for k in ["deadlift", "rdl", "romanian", "good morning", "hinge"]):
        return ["hinge"]
    if any(k in name for k in ["bench press", "push up", "push-up", "chest press", "fly"]):
        return ["horizontal press"]
    if any(k in name for k in ["overhead press", "shoulder press", "lateral raise"]):
        return ["vertical press"]
    if any(k in name for k in ["row", "pull down", "pull-down", "pulldown"]):
        return ["horizontal pull"]
    if any(k in name for k in ["pull up", "pull-up", "chin up", "chin-up"]):
        return ["vertical pull"]
    if any(k in name for k in ["curl", "extension", "raise"]):
        return ["isolation"]

    # Category override
    if cat in PATTERN_MAP and PATTERN_MAP[cat] is not None:
        return PATTERN_MAP[cat]

    # Force + mechanic fallback
    return FORCE_MECHANIC_PATTERN.get((force, mech), ["squat"])


def build_muscles(primaries: list, secondaries: list) -> list:
    out = []
    seen = set()
    for name in primaries:
        for mid in MUSCLE_MAP.get(name, [name.replace(" ", "_")]):
            if mid not in seen:
                out.append({"id": mid, "role": "primary"})
                seen.add(mid)
    for name in secondaries:
        for mid in MUSCLE_MAP.get(name, [name.replace(" ", "_")]):
            if mid not in seen:
                out.append({"id": mid, "role": "secondary"})
                seen.add(mid)
    return out


def entry_to_markdown(entry: dict) -> str:
    ex_id      = make_id(entry["id"])
    name       = entry["name"]
    muscles    = build_muscles(
        entry.get("primaryMuscles", []),
        entry.get("secondaryMuscles", []),
    )
    pattern    = infer_pattern(entry)
    difficulty = LEVEL_MAP.get(entry.get("level", "intermediate"), "intermediate")
    equipment  = [entry["equipment"]] if entry.get("equipment") else []
    equipment  = [e for e in equipment if e and e.lower() not in ("none", "other")]
    instructions = entry.get("instructions", [])

    # ── front matter ──
    fm = {
        "id":       ex_id,
        "name":     name,
        "status":   "stub",
        "source":   "free-exercise-db",
        "category": "exercise",
        "pattern":  pattern,
        "equipment": equipment,
        "difficulty": {
            "technical_complexity": None,
            "strength_prerequisite": None,
            "mobility_prerequisite": None,
        },
        "muscles":  muscles,
        "variations":   [],
        "progressions": [],
        "alternatives": [],
        "sources": [
            {
                "title":       "free-exercise-db",
                "author":      "yuhonas (Public Domain)",
                "credibility": "anecdotal",
            }
        ],
    }

    fm_str = yaml.dump(
        fm,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    ).rstrip()

    # ── body ──
    body_lines = [f"# {name}", ""]

    if instructions:
        body_lines += ["## Execution", ""]
        for i, step in enumerate(instructions, 1):
            wrapped = textwrap.fill(step.strip(), width=88,
                                    subsequent_indent="   ")
            body_lines.append(f"{i}. {wrapped}")
        body_lines.append("")

    body_lines += [
        "## Notes",
        "",
        "> ⚠️ This is a stub entry imported from free-exercise-db.",
        "> Fields marked `null` need human review.",
        "> Add EMG data, ROM requirements, relations, and lens entries before",
        "> changing `status` to `partial` or `complete`.",
        "",
    ]

    return f"---\n{fm_str}\n---\n\n" + "\n".join(body_lines)


def load_source(path: str | None) -> list:
    if path:
        return json.load(open(path, encoding="utf-8"))
    try:
        import requests
        r = requests.get(SOURCE_URL, timeout=20)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        sys.exit(f"Cannot fetch source: {e}\nPass --source PATH to use a local file.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", help="Path to exercises.json (default: fetch from GitHub)")
    ap.add_argument("--dry-run", action="store_true", help="Print stats without writing")
    ap.add_argument("--overwrite", action="store_true",
                    help="Overwrite existing stub entries (skips complete/partial)")
    ap.add_argument("--category", help="Only import entries of this category")
    args = ap.parse_args()

    data = load_source(args.source)
    print(f"Loaded {len(data)} entries from source")

    if args.category:
        data = [e for e in data if e.get("category") == args.category]
        print(f"Filtered to {len(data)} entries in category '{args.category}'")

    skipped = created = overwritten = 0

    for entry in data:
        ex_id = make_id(entry["id"])
        out_path = EXERCISES_DIR / f"{ex_id}.md"

        if out_path.exists() and not args.overwrite:
            skipped += 1
            continue

        if out_path.exists() and args.overwrite:
            # Don't overwrite human-reviewed entries
            text = out_path.read_text()
            if "status: complete" in text or "status: partial" in text:
                skipped += 1
                continue
            overwritten += 1
        else:
            created += 1

        md = entry_to_markdown(entry)

        if args.dry_run:
            print(f"  [dry-run] would write {out_path.name}")
        else:
            out_path.write_text(md, encoding="utf-8")

    action = "would create" if args.dry_run else "created"
    print(f"\nDone: {action} {created}, overwritten {overwritten}, skipped {skipped}")


if __name__ == "__main__":
    main()
