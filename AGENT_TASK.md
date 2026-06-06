# Agent Task: Refactor Encyclopedia Architecture — Programs as Top-Level, Remove Lens Layer

## Background

This is a fitness encyclopedia project structured as a Git repository of Markdown files
with YAML front matter. The current architecture has programs nested inside system folders
and a "lens" layer that attaches system-specific training perspectives to exercises.

A design decision has been made to:
1. Elevate `programs/` to a top-level folder (out of `systems/*/programs/`)
2. Remove the `systems/*/lenses/` layer entirely
3. Move all exercise-specific training knowledge (previously in lenses) INTO each
   program entry, under a structured `exercises[]` field
4. Slim down `systems/*/index.md` to philosophy/principles only — no exercise views

The rationale: programs are the actual unit users interact with. A user runs 5/3/1,
not "powerlifting as a system". Exercise-specific technique notes belong inside the
program that prescribes them, not in an abstract system-level lens.

---

## Current State (what exists now)

```
encyclopedia/
  core/
    muscles.yaml
    periodization.md
    progressive_overload.md
    sra_curve.md
  exercises/
    back_squat.md          ← complete, with EMG data (status: complete)
    bench_press.md         ← complete (status: complete)
    box_squat.md           ← complete (status: complete)
    conventional_deadlift.md  ← complete (status: complete)
    front_squat.md         ← complete (status: complete)
    goblet_squat.md        ← complete (status: complete)
    leg_press.md           ← complete (status: complete)
    overhead_press.md      ← complete (status: complete)
    [672 more stub entries imported from free-exercise-db]
  systems/
    powerlifting/
      index.md
      lenses/
        back_squat.md      ← TO BE DELETED (content migrated to program)
      programs/
        5_3_1.md           ← TO BE MOVED AND REWRITTEN
    bodybuilding/
      index.md
      lenses/
        back_squat.md      ← TO BE DELETED (content migrated to program)
      programs/
        [empty]
  crosscutting/
    nutrition/
      protein_requirements.md
    recovery/
      [empty]
  index/                   ← auto-generated, will be regenerated
  scripts/
    build_index.py
    coverage.py
    import_exercises.py
  SCHEMA.md
  glossary.md
  README.md
```

---

## Target State (what you must produce)

```
encyclopedia/
  core/                    ← unchanged
  exercises/               ← unchanged
  systems/
    powerlifting/
      index.md             ← REWRITE: slim to philosophy only
    bodybuilding/
      index.md             ← REWRITE: slim to philosophy only
    olympic/
      index.md             ← CREATE
    calisthenics/
      index.md             ← CREATE
    strongman/
      index.md             ← CREATE
    crossfit/
      index.md             ← CREATE
    [NO lenses/ subfolders anywhere]
  programs/                ← NEW TOP-LEVEL FOLDER
    powerlifting/
      5_3_1.md             ← REWRITE with full exercises[] structure
    bodybuilding/
      [empty for now]
    olympic/
    calisthenics/
    strongman/
    crossfit/
  crosscutting/            ← unchanged
  index/                   ← regenerate after changes
  scripts/
    build_index.py         ← UPDATE
    coverage.py            ← UPDATE
    import_exercises.py    ← unchanged
  SCHEMA.md                ← UPDATE
  glossary.md              ← unchanged
  README.md                ← UPDATE
```

---

## Detailed Instructions

### Step 1: Create new folder structure

```bash
mkdir -p programs/{powerlifting,bodybuilding,olympic,calisthenics,strongman,crossfit}
mkdir -p systems/{olympic,calisthenics,strongman,crossfit}
```

### Step 2: Rewrite `systems/*/index.md` files

Each system index.md must answer ONLY:
- What is this system's goal?
- What are its core training principles?
- What distinguishes it from other systems?
- Which programs belong to this system? (list of ids, no inline content)

Remove any reference to lenses, exercise-specific technique, or intensity tables.
The system file is a philosophy document, not a training manual.

**Template:**
```markdown
---
id: {system}_overview
name: {System Name}
category: system_overview
goal: One-line description
programs: [{program_id_1}, {program_id_2}]
---

# {System Name}

One paragraph on what this system is and who it's for.

## Defining Principles

- Principle 1
- Principle 2
- Principle 3

## Programs

See `programs/{system}/` for specific programs within this system.

## Related Core Principles

- `core/periodization.md`
- `core/progressive_overload.md`
- `core/sra_curve.md`
```

Create `index.md` for the four missing systems (olympic, calisthenics, strongman, crossfit)
using the same template. Write accurate content for each.

### Step 3: Create the new program entry format

Move `systems/powerlifting/programs/5_3_1.md` to `programs/powerlifting/5_3_1.md`
and REWRITE it completely with the following structure.

**Required front matter fields:**
```yaml
---
id: 5_3_1
name: 5/3/1
aliases: [Wendler 5/3/1]
category: program
system: powerlifting
goal: Slow, sustainable strength progress on the squat, bench, press, and deadlift
level: intermediate          # beginner | intermediate | advanced
duration_weeks: 4
frequency_per_week: 4
periodization: linear
progression_model: >
  After each 4-week cycle, add 2.5 kg to upper-body training maxes (bench, press)
  and 5 kg to lower-body training maxes (squat, deadlift). When AMRAP reps stall
  for two consecutive cycles on a lift, reset that lift's TM to 85–90% of current TM.

exercises:
  - ref: back_squat
    role: primary              # primary | supplemental | accessory
    frequency_per_week: 1
    technical_notes: >
      Low bar position preferred: shorter moment arm allows more forward lean,
      recruiting glutes and hamstrings alongside the quads. Stance wider than
      bodybuilding convention. Depth to just below parallel per IPF standards.
      Hip drive out of the hole is the cue — not "chest up".
    weeks:
      - week: 1
        sets: 3
        reps: [5, 5, "5+"]
        intensity:
          - {pct_tm: 65}
          - {pct_tm: 75}
          - {pct_tm: 85, amrap: true}
      - week: 2
        sets: 3
        reps: [3, 3, "3+"]
        intensity:
          - {pct_tm: 70}
          - {pct_tm: 80}
          - {pct_tm: 90, amrap: true}
      - week: 3
        sets: 3
        reps: [5, 3, "1+"]
        intensity:
          - {pct_tm: 75}
          - {pct_tm: 85}
          - {pct_tm: 95, amrap: true}
      - week: 4
        label: deload
        sets: 3
        reps: [5, 5, 5]
        intensity:
          - {pct_tm: 40}
          - {pct_tm: 50}
          - {pct_tm: 60}

  - ref: bench_press
    role: primary
    frequency_per_week: 1
    technical_notes: >
      Moderate grip width (index finger on the ring marks or slightly inside).
      Slight arch, scapulae retracted and depressed before unracking.
      Touch-and-go acceptable in training; pause preferred for competition prep.
      Bar path: slight diagonal from lower chest to over shoulders at lockout.
    weeks:
      [same 4-week wave structure as back_squat, pct_tm identical]

  - ref: overhead_press
    role: primary
    frequency_per_week: 1
    technical_notes: >
      Strict standing press — no leg drive. Grip just outside shoulders.
      Bar starts at clavicle level. Move the head back, not the bar forward.
      Lock out with bar over mid-foot. Core and glutes braced throughout.
    weeks:
      [same 4-week wave structure]

  - ref: conventional_deadlift
    role: primary
    frequency_per_week: 1
    technical_notes: >
      Hip-width stance, double overhand or mixed grip.
      Bar over mid-foot, shins touch bar at setup.
      Lat engagement ("protect your armpits") before breaking the floor.
      Reset between reps for competition specificity; touch-and-go acceptable
      for volume work.
    weeks:
      [same 4-week wave structure]

sources:
  - title: "5/3/1: The Simplest and Most Effective Training System"
    author: "Jim Wendler"
    credibility: practitioner
---
```

**Required prose sections in the body:**

```markdown
# 5/3/1

[One paragraph: what this program is and the core philosophy]

## How the Training Max Works

[Explain TM = ~90% of true 1RM, why this matters, how to calculate it]

## The Four-Week Wave

[Table showing week-by-week percentages and rep targets]

## AMRAP Sets

[Explain the purpose of the + sets — progress signal, auto-regulation]

## Progression

[Explain the monthly TM increases and reset protocol]

## Assistance Work

[Describe the "Boring But Big" and other common assistance templates —
these are separate from the main lift prescription above]

## Why It Works

[Explain the submaximal approach and long-term sustainability]
```

### Step 4: Update SCHEMA.md

Replace the current `## category: program` section with the following:

```markdown
## category: program  (`programs/{system}/`)

| Field | Req | Type | Notes |
|-------|-----|------|-------|
| `id` | req | str | snake_case, unique |
| `name` | req | str | |
| `aliases` | opt | list[str] | |
| `category` | req | const | Always `program` |
| `system` | req | str | Must match a system folder name |
| `goal` | req | str | One line |
| `level` | req | enum | `beginner` \| `intermediate` \| `advanced` |
| `duration_weeks` | opt | int | |
| `frequency_per_week` | opt | int | |
| `periodization` | opt | enum | `linear` \| `undulating` \| `block` \| `conjugate` |
| `progression_model` | req | str | How load/volume advances |
| `exercises` | req | list[program_exercise] | See Program Exercise object |
| `sources` | opt | list[source] | |

### Program Exercise object

Each entry in `exercises[]` describes how the program uses one specific movement:

| Field | Req | Type | Notes |
|-------|-----|------|-------|
| `ref` | req | id | Must resolve to an exercise in `exercises/` |
| `role` | req | enum | `primary` \| `supplemental` \| `accessory` |
| `frequency_per_week` | opt | int | |
| `technical_notes` | req | str | This program's technique prescription for this movement. Write in second person, as a coach giving instructions. Be specific: bar position, stance, depth cues, grip, breathing. |
| `weeks` | opt | list[week] | Per-week prescriptions |

### Week object

| Field | Req | Type | Notes |
|-------|-----|------|-------|
| `week` | req | int | Week number |
| `label` | opt | str | e.g. `deload` |
| `sets` | req | int | |
| `reps` | req | list | Can be int or string (e.g. `"5+"` for AMRAP) |
| `intensity` | req | list[intensity_unit] | |

### Intensity unit object

```yaml
intensity:
  - {pct_tm: 65}                    # percentage of training max
  - {pct_1rm: 80}                   # percentage of true 1RM
  - {rpe: 8}                        # RPE target
  - {pct_tm: 85, amrap: true}       # AMRAP set
```

Remove the `## category: lens` section entirely — lenses no longer exist.
```

### Step 5: Update `scripts/build_index.py`

Make the following changes:

**a) Update `collect_programs()`**

Change the scan path from `systems/*/programs/` to the new top-level `programs/`:

```python
def collect_programs() -> dict:
    out = {}
    for md in sorted((ROOT / "programs").rglob("*.md")):
        fm = parse_front_matter(md)
        ent_id = fm.get("id")
        if not ent_id:
            continue
        out[ent_id] = {
            "id": ent_id,
            "name": fm.get("name"),
            "system": fm.get("system"),
            "level": fm.get("level"),
            "periodization": fm.get("periodization"),
            "exercise_refs": [
                e["ref"] for e in (fm.get("exercises") or [])
                if isinstance(e, dict) and e.get("ref")
            ],
            "path": rel(md),
        }
    return out
```

**b) Remove all lens-related functions and logic**

Delete or comment out:
- `collect_lenses()`
- `build_cross_reference()` (which used lenses)
- All references to `lenses` in `check_integrity()`
- The `lenses.json` and `cross_reference.json` write calls in `main()`

**c) Add `build_program_exercise_index()`**

```python
def build_program_exercise_index(programs: dict) -> dict:
    """Reverse map: exercise_id -> list of program_ids that use it."""
    index = {}
    for prog_id, prog in programs.items():
        for ex_ref in prog.get("exercise_refs", []):
            index.setdefault(ex_ref, []).append(prog_id)
    for ex_id in index:
        index[ex_id] = sorted(index[ex_id])
    return index
```

Call it in `main()` and write to `index/program_exercise_index.json`.

**d) Update `check_integrity()`**

Remove lens validation. Add:
- Validate that each `program.exercise_refs` resolves to a real exercise id
- Validate that each `program.system` matches an existing system folder name

**e) Update `build_coverage_report()`**

Remove the `lens_count` field from system coverage.
Add `program_count` and `exercises_covered` (how many unique exercise refs
appear across all programs in a system).

### Step 6: Update `scripts/coverage.py`

In `section_systems()`, remove the lenses column.
Add a `programs` column showing count, and an `ex. coverage` column
showing how many exercises have at least one program prescribing them.

In `section_exercises()`, replace the per-system lens columns with a single
`in programs` column showing how many programs reference that exercise.

In `section_todo()`, update priority messages:
- Remove "Add lenses" item
- Add: "Exercises with no program reference" (high priority)
- Add: "Programs missing technical_notes for some exercises"

### Step 7: Clean up

Delete these paths:
```
systems/powerlifting/lenses/
systems/bodybuilding/lenses/
systems/powerlifting/programs/
systems/bodybuilding/programs/
```

Verify nothing else references these paths before deleting.

### Step 8: Regenerate the index

```bash
cd encyclopedia
python3 scripts/build_index.py
```

Fix any integrity errors before committing.

### Step 9: Update README.md

Update the Structure section to reflect the new layout.
Remove all references to "lens entries".
Add a description of the `programs/` folder and the `exercises[]` field.

### Step 10: Git commit

```bash
git add -A
git commit -m "Refactor: programs top-level, remove lens layer

- programs/ moved to top-level, out of systems/*/programs/
- systems/*/lenses/ removed entirely
- Program entries now carry exercises[] with technical_notes per movement
- 5/3/1 rewritten with full per-exercise prescription
- 4 new system index.md files (olympic, calisthenics, strongman, crossfit)
- build_index.py: collect_programs scans programs/, adds program_exercise_index
- coverage.py: updated for new structure
- SCHEMA.md: program category rewritten, lens category removed
- README.md: updated structure section"
```

---

## Integrity Rules to Enforce

After all changes, `python3 scripts/build_index.py` must:

1. Exit with code 0 (no integrity errors)
2. Produce `index/program_exercise_index.json`
3. NOT produce `index/lenses.json` or `index/cross_reference.json`
4. Report correct exercise and program counts

Any `exercise_ref` in a program's `exercises[]` that does not resolve to a
real exercise entry must be flagged as an integrity error (not a warning).

---

## What NOT to change

- `exercises/*.md` — do not touch any exercise base entries
- `core/*.md` — do not touch principle entries
- `crosscutting/**` — do not touch
- `core/muscles.yaml` — do not touch
- `scripts/import_exercises.py` — do not touch
- `glossary.md` — do not touch
- Exercise front matter fields (id, name, muscles, EMG data, etc.)

---

## Verification Checklist

Before finishing, verify:

- [ ] `programs/powerlifting/5_3_1.md` exists with valid YAML front matter
- [ ] `5_3_1.md` has `exercises[]` with 4 entries (back_squat, bench_press, overhead_press, conventional_deadlift)
- [ ] Each exercise entry has `technical_notes` (non-empty string)
- [ ] Each exercise entry has `weeks[]` with 4 week objects
- [ ] `systems/powerlifting/lenses/` does NOT exist
- [ ] `systems/bodybuilding/lenses/` does NOT exist
- [ ] `systems/{olympic,calisthenics,strongman,crossfit}/index.md` exist
- [ ] `python3 scripts/build_index.py` exits 0
- [ ] `index/program_exercise_index.json` exists and maps exercise ids to program ids
- [ ] `python3 scripts/coverage.py --systems` runs without error
- [ ] `python3 scripts/coverage.py --todo` runs without error
- [ ] `git log --oneline` shows a new commit on top
