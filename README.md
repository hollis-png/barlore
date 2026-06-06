# Strength & Physique Encyclopedia

A structured, offline-friendly knowledge base covering strength and physique training systems — powerlifting, bodybuilding, weightlifting, calisthenics, strongman, and CrossFit — plus shared nutrition and recovery knowledge.

## Design Principle

The core idea is **three independent, flat layers connected by references, not by folder hierarchy.**

- `exercises/` holds neutral, objective **base entries** — what a movement *is*, with no system bias.
- `systems/` holds **philosophy documents** — what each training system values, how it thinks, what distinguishes it. No exercise views, no intensity tables.
- `programs/` holds **prescription entries** — how a specific named program uses each movement, including technique cues, weekly structure, and intensity prescriptions.

A movement is never "owned" by a system. The back squat belongs to no folder other than `exercises/`. A program references it via `exercises[].ref`; the system philosophy mentions the program by id. The three layers are independent and connected only by explicit references.

### Why This Matters

- **One movement, many programs**: The back squat can be prescribed by 5/3/1, Sheiko, a PPL bodybuilding template, and a CrossFit strength cycle — all pointing to the same base entry, with each program providing its own `technical_notes`.
- **Programs are the user's unit**: A lifter runs 5/3/1, not "powerlifting as a system". Starting from `programs/` and looking up the base entry in `exercises/` is the natural query path.
- **Systems stay clean**: System index files answer philosophical questions only — goal, principles, what distinguishes this system. No duplication of exercise content.

## Structure

```
core/                 Definitional layer — short, precise principle entries
exercises/            Movement base entries (flat; classified by `pattern` field)
systems/
  powerlifting/
    index.md          System philosophy, goal, program list (no exercise views)
  bodybuilding/
    index.md
  olympic/
  calisthenics/
  strongman/
  crossfit/
programs/             Named training programs (top-level; grouped by system subfolder)
  powerlifting/
    5_3_1.md          Full prescription: exercises[], technical_notes, weekly structure
  bodybuilding/
  olympic/
  calisthenics/
  strongman/
  crossfit/
crosscutting/
  nutrition/          Shared across all systems
  recovery/
index/                AUTO-GENERATED — do not hand-edit
scripts/
  build_index.py      Scans entries, regenerates index/
  coverage.py         Human-readable coverage report
  import_exercises.py Bulk import from free-exercise-db
glossary.md           Canonical term table — single source of naming truth
SCHEMA.md             Formal field specification for every entry category
```

## Conventions

- **Single source of truth for cross-references.** Program entries declare `exercises[].ref`. Exercise base entries do *not* hand-write their program list — `build_index.py` generates the reverse mapping (`index/program_exercise_index.json`). The two cannot drift.
- **Flat exercises, pattern as a field.** `exercises/` has no subfolders. Movement pattern lives in the `pattern` YAML field (a list, so a movement can belong to several patterns). This avoids ambiguous folder placement.
- **Structured movement relations.** Exercises declare `variations`, `progressions`, and `alternatives` as lists of entry ids — machine-readable, not just prose tables.
- **Canonical naming.** Every concept uses its canonical name from `glossary.md`; all other forms go in `aliases`.
- **Evidence tiers.** `sources[].credibility` uses graded tiers: `meta_analysis` > `rct` > `expert_consensus` > `practitioner` > `anecdotal`.
- **Field spec is formal.** Every category's fields are defined in `SCHEMA.md`. Update it whenever a field changes.

## Program Entry Format

Each program entry in `programs/{system}/` carries an `exercises[]` list that describes how the program uses each movement:

```yaml
exercises:
  - ref: back_squat           # resolves to exercises/back_squat.md
    role: primary             # primary | supplemental | accessory
    frequency_per_week: 1
    technical_notes: >
      Low bar position. Stance wider than shoulder-width. Drive hips out
      of the hole. Depth to just below parallel per IPF standards.
    weeks:
      - week: 1
        sets: 3
        reps: [5, 5, "5+"]
        intensity:
          - {pct_tm: 65}
          - {pct_tm: 75}
          - {pct_tm: 85, amrap: true}
```

This is where system-specific technique lives. There are no separate "lens" files.

## Building the Index

```bash
pip install pyyaml --break-system-packages
python3 scripts/build_index.py          # regenerate index/
python3 scripts/build_index.py --check  # verify index is current (CI)
```

The build does three things: regenerates the `index/` JSON, runs a **referential
integrity check** (every `exercises[].ref` in a program must resolve to a real
exercise entry, or the build fails), and emits **symmetry warnings** for one-sided
variation links. The generated `index/program_exercise_index.json` maps each
exercise id to the programs that prescribe it, enabling a downstream search or
RAG layer to locate the right file in one step.

## Viewing Coverage

```bash
python3 scripts/coverage.py               # full report
python3 scripts/coverage.py --systems     # which systems have programs
python3 scripts/coverage.py --exercises   # which exercises are in programs
python3 scripts/coverage.py --todo        # highest-impact gaps
```

## Status

Skeleton with worked examples. Current state:
- 680 exercise base entries (8 human-reviewed, 672 stubs from free-exercise-db)
- 1 complete program (5/3/1 powerlifting, 4 exercises with full weekly prescription)
- 6 system philosophy files (powerlifting, bodybuilding, olympic, calisthenics, strongman, crossfit)

Next: expand programs for remaining systems, promote stub exercises to partial/complete, fill nutrition and recovery, then run a retrieval sanity check before bulk authoring.
