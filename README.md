# Strength & Physique Encyclopedia

A structured, offline-friendly knowledge base covering strength and physique training systems — powerlifting, bodybuilding, weightlifting, calisthenics, strongman, and CrossFit — plus shared nutrition and recovery knowledge.

## Design Principle

The core idea is **separating the movement itself from how each system trains it.**

- `exercises/` holds neutral, objective **base entries** — what a movement *is*, with no system bias.
- `systems/*/lenses/` holds **lens entries** — how a given system reinterprets that movement, written like a coach in that discipline talking.

This avoids writing the back squat five times (once per system) with inconsistent, duplicated content. Each movement has one base entry and many lenses pointing at it.

## Structure

```
core/                 Definitional layer — short, precise principle entries
exercises/            Movement base entries (flat; classified by `pattern` field)
systems/
  powerlifting/
    index.md          Human-facing system overview / map
    lenses/           Per-movement lens entries (declare `exercise_ref`)
    programs/         Named programs (5/3/1, conjugate, ...)
  bodybuilding/
    ...
crosscutting/
  nutrition/          Shared across all systems
  recovery/
index/                AUTO-GENERATED — do not hand-edit
scripts/
  build_index.py      Scans entries, regenerates index/
glossary.md           Canonical term table — single source of naming truth
```

## Conventions

- **Single source of truth for cross-references.** Lens entries declare `exercise_ref`. Exercise base entries do *not* hand-write their lens list — `build_index.py` generates the reverse mapping. The two cannot drift.
- **Flat exercises, pattern as a field.** `exercises/` has no subfolders. Movement pattern lives in the `pattern` YAML field (a list, so a movement can belong to several patterns). This avoids ambiguous folder placement.
- **Canonical naming.** Every concept uses its canonical name from `glossary.md`; all other forms go in `aliases`.
- **Evidence tiers.** `sources[].credibility` uses graded tiers: `meta_analysis` > `rct` > `expert_consensus` > `practitioner` > `anecdotal`.

## Building the Index

```bash
pip install pyyaml --break-system-packages
python3 scripts/build_index.py          # regenerate index/
python3 scripts/build_index.py --check  # verify index is current (CI)
```

The generated `index/cross_reference.json` lets a downstream search or RAG layer locate the right file in one step instead of scanning the whole corpus.

## Status

Skeleton with worked examples. Next: expand exercises, add the remaining systems, fill nutrition and recovery, then run a retrieval sanity check before bulk authoring.
