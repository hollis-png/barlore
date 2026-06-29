#!/usr/bin/env python3
"""
Build the index/ JSON files for the fitness encyclopedia.

Programs are top-level under programs/{system}/*.md. Each program entry
carries an exercises[] list; this script derives the reverse mapping
(exercise_id -> [program_ids]) automatically, so the two can never drift
out of sync.

Outputs:
  index/exercises.json              flat list of exercise base entries + metadata
  index/programs.json               flat list of program entries
  index/program_exercise_index.json exercise_id -> [program_ids] reverse map
  index/muscle_index.json           muscle_id -> [exercise_ids]
  index/coverage_report.json        three-dimensional coverage data

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
MUSCLES_FILE = ROOT / "core" / "muscles.yaml"
SYSTEM_GUIDES_DIR = ROOT / "system_guides"


# ── Muscle hierarchy ──────────────────────────────────────────────────────────

def load_muscle_hierarchy() -> dict:
    """Load core/muscles.yaml and return a flat map of every known muscle id
    to its parent group id (and grandparent if heads exist).

    Returns: {muscle_id: group_id, head_id: muscle_id, ...}
    Also returns the full tree for group->children lookups.
    """
    if not MUSCLES_FILE.exists():
        return {}, {}
    raw = yaml.safe_load(MUSCLES_FILE.read_text(encoding="utf-8")) or {}

    parent_of = {}   # child_id -> parent_id
    children_of = {} # group_id -> set of all descendant leaf ids

    for group_id, group in raw.items():
        children_of[group_id] = set()
        for muscle_id, muscle in (group.get("children") or {}).items():
            parent_of[muscle_id] = group_id
            children_of[group_id].add(muscle_id)
            for head_id in (muscle.get("heads") or {}).keys():
                parent_of[head_id] = muscle_id
                children_of[group_id].add(head_id)
                children_of.setdefault(muscle_id, set()).add(head_id)

    return parent_of, children_of


def expand_muscle_query(query_id: str, children_of: dict) -> set:
    """Return the set of leaf muscle ids that a query covers.
    - If query_id is a group (e.g. 'quadriceps'), return all its descendants.
    - If query_id is a leaf, return just {query_id}.
    """
    if query_id in children_of:
        return set(children_of[query_id])
    return {query_id}


def build_muscle_index(exercises: dict, children_of: dict) -> dict:
    """Return a map: muscle_id/group_id -> list of exercise ids that include it.
    Querying a group returns exercises that use ANY of its descendants.
    """
    # Build leaf -> exercises first
    leaf_to_exercises = {}
    for ex_id, ex in exercises.items():
        for m in ex.get("muscles", []):
            mid = m["id"]
            leaf_to_exercises.setdefault(mid, set()).add(ex_id)

    # Now expand: for every group, union its children's exercise sets
    muscle_index = {}
    all_ids = set(leaf_to_exercises) | set(children_of)
    for mid in all_ids:
        covered = expand_muscle_query(mid, children_of)
        ex_set = set()
        for leaf in covered:
            ex_set |= leaf_to_exercises.get(leaf, set())
        if ex_set:
            muscle_index[mid] = sorted(ex_set)

    return muscle_index


# ── Front matter parsing ──────────────────────────────────────────────────────

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
            "status": fm.get("status", "complete"),  # stub/partial/complete
            "source": fm.get("source"),
            "aliases": fm.get("aliases", []),
            "pattern": fm.get("pattern", []),
            "equipment": fm.get("equipment", []),
            "difficulty": fm.get("difficulty"),
            "muscles": fm.get("muscles", []),
            "muscle_activation_studies": fm.get("muscle_activation_studies", []),
            "joint_rom_required": fm.get("joint_rom_required"),
            "strength_curve": fm.get("strength_curve"),
            "injury_risk": fm.get("injury_risk"),
            "variations": fm.get("variations", []),
            "progressions": fm.get("progressions", []),
            "alternatives": fm.get("alternatives", []),
            "path": rel(md),
        }
    return out


def collect_principles() -> dict:
    """Principle + crosscutting entries, for resolving `related` references."""
    out = {}
    for sub in ("core", "crosscutting"):
        for md in sorted((ROOT / sub).rglob("*.md")):
            fm = parse_front_matter(md)
            ent_id = fm.get("id")
            if not ent_id:
                continue
            out[ent_id] = {
                "id": ent_id,
                "category": fm.get("category"),
                "related": fm.get("related", []),
                "path": rel(md),
            }
    return out


def collect_programs() -> dict:
    """Scan programs/ directory for concrete program entries."""
    out = {}
    programs_dir = ROOT / "programs"
    if not programs_dir.exists():
        return out
    for md in sorted(programs_dir.rglob("*.md")):
        fm = parse_front_matter(md)
        ent_id = fm.get("id")
        if not ent_id:
            continue
        exercise_refs = [
            e["ref"] for e in (fm.get("exercises") or [])
            if isinstance(e, dict) and e.get("ref")
        ]
        out[ent_id] = {
            "id": ent_id,
            "name": fm.get("name"),
            "type": fm.get("type", "program"),
            "system": fm.get("system"),
            "level": fm.get("level"),
            "goals": fm.get("goals", []),
            "periodization": fm.get("periodization"),
            "exercise_refs": exercise_refs,
            "path": rel(md),
        }
    return out


def collect_system_guides() -> dict:
    """Scan system_guides/ directory for system guide entries."""
    out = {}
    if not SYSTEM_GUIDES_DIR.exists():
        return out
    for md in sorted(SYSTEM_GUIDES_DIR.glob("*.md")):
        fm = parse_front_matter(md)
        ent_id = fm.get("id")
        if not ent_id:
            continue
        out[ent_id] = {
            "id": ent_id,
            "type": fm.get("type", "system_guide"),
            "system": fm.get("system"),
            "level": fm.get("level"),
            "frequency_per_week_range": fm.get("frequency_per_week_range"),
            "periodization_style": fm.get("periodization_style"),
            "path": rel(md),
        }
    return out


def build_program_exercise_index(programs: dict) -> dict:
    """Reverse map: exercise_id -> list of program_ids that use it."""
    index = {}
    for prog_id, prog in programs.items():
        for ex_ref in prog.get("exercise_refs", []):
            index.setdefault(ex_ref, []).append(prog_id)
    for ex_id in index:
        index[ex_id] = sorted(index[ex_id])
    return index


def check_integrity(exercises, principles, programs,
                    parent_of: dict, children_of: dict) -> list:
    """Verify every relation reference resolves. Returns list of error strings."""
    errors = []
    ex_ids = set(exercises)
    prog_ids = set(programs)
    principle_ids = set(principles)
    known_muscle_ids = (set(parent_of) | set(children_of)) if parent_of else None

    # Known system folder names
    systems_dir = ROOT / "systems"
    known_systems = {p.name for p in systems_dir.iterdir() if p.is_dir()} \
        if systems_dir.exists() else set()

    # Muscle id validation (only if muscles.yaml is loaded)
    if known_muscle_ids:
        for ex_id, ex in exercises.items():
            for m in ex.get("muscles", []):
                mid = m.get("id", "")
                # 'core' is a special group id — allow it
                if mid and mid not in known_muscle_ids:
                    errors.append(
                        f"{ex['path']}: muscles id '{mid}' not in core/muscles.yaml")
            for study in ex.get("muscle_activation_studies", []):
                for meas in study.get("measurements", []):
                    mid = meas.get("muscle", "")
                    if mid and mid not in known_muscle_ids:
                        errors.append(
                            f"{ex['path']}: EMG measurement muscle '{mid}' "
                            f"not in core/muscles.yaml")

    # Exercise relations must resolve to exercises
    for ex_id, ex in exercises.items():
        for field in ("variations", "progressions", "alternatives"):
            for ref in ex.get(field, []):
                if ref not in ex_ids:
                    errors.append(
                        f"{ex['path']}: {field} -> '{ref}' has no exercise entry")

    # Principle / crosscutting `related`
    for ent in principles.values():
        for ref in ent.get("related", []):
            if ref not in principle_ids:
                errors.append(
                    f"{ent['path']}: related -> '{ref}' has no core/crosscutting entry")

    # Program integrity
    for prog in programs.values():
        # system must match a known system folder
        sys_name = prog.get("system")
        if sys_name and known_systems and sys_name not in known_systems:
            errors.append(
                f"{prog['path']}: system -> '{sys_name}' has no matching "
                f"systems/{sys_name}/ folder")
        # exercises[].ref must resolve to real exercise ids
        # system_guide documents have no exercise_refs — skip this check
        if prog.get("type") == "system_guide":
            continue
        for ex_ref in prog.get("exercise_refs", []):
            if ex_ref not in ex_ids:
                errors.append(
                    f"{prog['path']}: exercises[].ref -> '{ex_ref}' "
                    f"has no exercise entry")

    return errors


def check_symmetry(exercises) -> list:
    """Warn (not error) when variations aren't declared on both sides."""
    warnings = []
    for ex_id, ex in exercises.items():
        for ref in ex.get("variations", []):
            other = exercises.get(ref)
            if other and ex_id not in other.get("variations", []):
                warnings.append(
                    f"asymmetric variation: {ex_id} lists {ref}, "
                    f"but {ref} doesn't list {ex_id}")
    return warnings


def build_coverage_report(exercises: dict, programs: dict,
                          children_of: dict) -> dict:
    """Build the three-dimensional coverage report."""
    import datetime

    # Which systems exist (from system index.md files)
    systems_defined = sorted(
        p.parent.name
        for p in (ROOT / "systems").glob("*/index.md")
    )

    # Program lookup: exercise_id -> [program_ids]
    prog_ex_index = build_program_exercise_index(programs)

    # ── Exercise dimension ──────────────────────────────────────────────────
    ex_coverage = {}
    for ex_id, ex in exercises.items():
        prog_refs = prog_ex_index.get(ex_id, [])
        ex_coverage[ex_id] = {
            "status":             ex.get("status", "complete"),
            "has_emg":            bool(ex.get("muscle_activation_studies")),
            "has_rom":            bool(ex.get("joint_rom_required")),
            "has_strength_curve": bool(ex.get("strength_curve")),
            "muscle_count":       len(ex.get("muscles", [])),
            "in_programs":        prog_refs,
            "program_count":      len(prog_refs),
        }

    # ── Muscle dimension ────────────────────────────────────────────────────
    muscle_coverage = {}
    all_queryable = set(children_of)
    for ex in exercises.values():
        for m in ex.get("muscles", []):
            all_queryable.add(m["id"])

    for mid in sorted(all_queryable):
        covered = expand_muscle_query(mid, children_of)
        ex_with = [
            ex_id for ex_id, ex in exercises.items()
            if any(m["id"] in covered for m in ex.get("muscles", []))
        ]
        ex_with_emg = [
            ex_id for ex_id in ex_with
            if exercises[ex_id].get("muscle_activation_studies")
        ]
        muscle_coverage[mid] = {
            "exercise_count": len(ex_with),
            "emg_count":      len(ex_with_emg),
            "exercises":      sorted(ex_with),
            "exercises_with_emg": sorted(ex_with_emg),
        }

    # ── System dimension ────────────────────────────────────────────────────
    system_coverage = {}
    for sys_id in systems_defined:
        sys_programs = [p for p in programs.values() if p.get("system") == sys_id]
        # Unique exercises covered across all programs in this system
        exercises_covered = set()
        for p in sys_programs:
            exercises_covered.update(p.get("exercise_refs", []))
        sys_index = ROOT / "systems" / sys_id / "index.md"
        core_refs = 0
        if sys_index.exists():
            text = sys_index.read_text()
            core_refs = text.count("core/")
        system_coverage[sys_id] = {
            "has_index":        sys_index.exists(),
            "program_count":    len(sys_programs),
            "exercises_covered": len(exercises_covered),
            "exercise_count":   len(exercises),   # denominator: all exercises
            "core_refs":        core_refs,
        }

    return {
        "generated_at":    datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        "systems_defined":  systems_defined,
        "exercise_count":   len(exercises),
        "program_count":    len(programs),
        "exercises":        ex_coverage,
        "muscle_coverage":  muscle_coverage,
        "system_coverage":  system_coverage,
    }


def build_goal_index(programs: dict) -> dict:
    """Build goal -> [{id, level, system, name}] index for goal-based queries."""
    index = {}
    for prog in programs.values():
        for goal in prog.get("goals", []):
            if goal not in index:
                index[goal] = []
            index[goal].append({
                "id": prog["id"],
                "name": prog.get("name"),
                "level": prog.get("level"),
                "system": prog.get("system"),
            })
    for goal in index:
        index[goal].sort(key=lambda p: (
            {"beginner": 0, "intermediate": 1, "advanced": 2}.get(p.get("level", ""), 9),
            p.get("system", ""),
        ))
    return index


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
    parent_of, children_of = load_muscle_hierarchy()
    if parent_of:
        print(f"  loaded muscles.yaml: {len(parent_of)} muscle ids, "
              f"{len(children_of)} groups/muscles with children")
    else:
        print("  ! core/muscles.yaml not found — muscle validation skipped")

    exercises      = collect_exercises()
    principles     = collect_principles()
    programs       = collect_programs()
    system_guides  = collect_system_guides()
    print(f"  found {len(exercises)} exercises, "
          f"{len(programs)} programs, {len(system_guides)} system guides, "
          f"{len(principles)} principle/crosscutting")

    errors   = check_integrity(exercises, principles, programs, parent_of, children_of)
    warnings = check_symmetry(exercises)
    for w in warnings:
        print(f"  ⚠ {w}", file=sys.stderr)
    if errors:
        for e in errors:
            print(f"  ✗ {e}", file=sys.stderr)
        sys.exit(f"\nIntegrity check failed: {len(errors)} broken reference(s).")
    print(f"  integrity OK ({len(warnings)} symmetry warning(s))")

    muscle_index         = build_muscle_index(exercises, children_of)
    prog_exercise_index  = build_program_exercise_index(programs)
    goal_index           = build_goal_index(programs)
    coverage             = build_coverage_report(exercises, programs, children_of)
    print(f"  muscle index: {len(muscle_index)} queryable ids")
    print(f"  program-exercise index: {len(prog_exercise_index)} exercises referenced")
    print(f"  goal index: {len(goal_index)} goals")

    ok = True
    ok &= write_json("exercises.json",             exercises,           args.check)
    ok &= write_json("programs.json",              programs,    args.check)
    ok &= write_json("program_exercise_index.json", prog_exercise_index, args.check)
    ok &= write_json("muscle_index.json",          muscle_index,        args.check)
    ok &= write_json("goal_index.json",             goal_index,          args.check)
    ok &= write_json("coverage_report.json",       coverage,            args.check)
    ok &= write_json("system_guides.json",         system_guides,       args.check)

    if args.check and not ok:
        sys.exit("Index out of date. Run: python3 scripts/build_index.py")
    print("Done.")


if __name__ == "__main__":
    main()
