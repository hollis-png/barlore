# Plan Generator Prompt — Design Spec

**Date**: 2026-06-23
**Status**: Approved
**Deliverable**: `Barlore/prompts/plan_generator.md` — a single-file prompt template

---

## Overview

A structured prompt template that any LLM can use to generate a personalized training plan from the Barlore knowledge base. The user fills in their profile, pastes the entire file into an LLM, and receives a program recommendation with a weekly schedule.

### Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Delivery format | Single-file prompt template | Portable — works with any LLM, no tooling required |
| Data access | Hybrid (embedded matrix + file paths) | Key matching data inline; exercise details via file reads for LLMs that support it |
| Language | English | Consistent with Barlore KB |
| Level assessment | Self-assessment + data verification | Accurate cross-validation without being intimidating to beginners |
| Exercise substitution | Merged two-stage | When adjustments are needed, output one final schedule with a change log on top — avoids redundant full-schedule output that wastes tokens and triggers lazy LLM behavior |

---

## File Structure

The prompt is a single `.md` file with four sections:

```
Section A: System Prompt        — LLM role + behavioral rules (fixed)
Section B: User Profile         — Intake form (user fills in)
Section C: Decision Matrix      — Embedded matching data (fixed, from Barlore index)
Section D: Generation Rules     — Output flow instructions (fixed)
```

The user's only task is to fill Section B and submit the entire file to an LLM.

---

## Section A: System Prompt

Sets the LLM's role and constraints:

- Role: strength and conditioning coach with access to the Barlore knowledge base
- Must base all recommendations on Barlore entries — no inventing exercises or programs
- Must cite program IDs and exercise IDs from Barlore
- When the LLM has file-reading capability, it should read the referenced Barlore files for exercise details (execution cues, injury_risk, alternatives)
- When the LLM does NOT have file-reading capability: it must rely exclusively on the embedded Decision Matrix (Section C) and the program/system structure described in this prompt. It must NOT hallucinate Barlore-specific program structures from general training knowledge. Output must begin with: `[Preview: generated without reading Barlore source files — exercise details may differ from the canonical knowledge base]`
- All output in English; exercise names use Barlore canonical names

---

## Section B: User Profile

### Required Fields

| # | Field | Format | Purpose |
|---|-------|--------|---------|
| 1 | Primary Goal | Select one: `strength` / `hypertrophy` / `athletic_performance` / `calisthenics_skills` / `general_fitness` / `sport_specific` | System filtering |
| 2 | Self-Assessed Level | Select one: `beginner` / `intermediate` / `advanced` | Initial level match |
| 3 | Training History | Free text: years of training + key lift numbers or skills | Level cross-validation |
| 4 | Available Equipment | Multi-select: `full_gym` / `barbell_and_rack` / `dumbbells_only` / `bodyweight_only` / `has_strongman_implements` / `has_gymnastics_rings` | Exercise feasibility |
| 5 | Days Per Week | Number: 2-6 | Program frequency match |
| 6 | Session Duration | Select one: `30-45min` / `45-60min` / `60-90min` / `90min+` | Volume feasibility |

### Optional Fields

| # | Field | Format | Purpose |
|---|-------|--------|---------|
| 7 | Injuries / Limitations | Free text | Stage 2 exercise substitution |
| 8 | Age | Number | Triggers masters_athletes guidance (35+) |
| 9 | Sex | `male` / `female` | Triggers female_athletes guidance; adjusts level benchmarks |
| 10 | Body Weight (kg) | Number | Level verification (BW ratio) + nutrition guidance |
| 11 | Body Composition Goal | Select one: `gain_muscle` / `lose_fat` / `maintain` | Nutrition direction |

---

## Section C: Decision Matrix

Embedded data tables that the LLM uses for matching. These are generated from Barlore's `index/programs.json` and can be refreshed with a script.

### C.1 — Programs Table

All 41 programs with matching-relevant fields:

```
| system        | level        | program_id                        | name                              | periodization |
```

Full table to be generated from `index/programs.json` at implementation time.

### C.2 — Goal-to-System Mapping

```
strength              → powerlifting, strongman
hypertrophy           → bodybuilding
athletic_performance  → olympic, crossfit
calisthenics_skills   → calisthenics
general_fitness       → bodybuilding(beginner), crossfit
sport_specific        → LLM selects based on user's sport description:
                          power/contact sports → powerlifting or strongman
                          explosive/speed sports → olympic or crossfit
                          gymnastics/climbing → calisthenics
                          aesthetic sports → bodybuilding
                          endurance sports → crossfit (with cardio emphasis)
                          if unclear, ask the user to clarify
```

### C.3 — Equipment Feasibility

```
| equipment_tier        | feasible_systems                        | notes                           |
|-----------------------|-----------------------------------------|---------------------------------|
| full_gym              | all                                     |                                 |
| barbell_and_rack      | powerlifting, olympic, bodybuilding      | no cable/machine accessories    |
| dumbbells_only        | bodybuilding(beginner)                  | needs program modification      |
| bodyweight_only       | calisthenics                            | only feasible system            |
| has_strongman_implements | + strongman                          | adds strongman to base tier     |
| has_gymnastics_rings  | + calisthenics(intermediate, advanced)  | adds ring-based progressions    |
```

**Multi-select combination rule:** When the user selects multiple equipment tiers, the feasible systems are the **union** of all selected tiers. The LLM should prefer programs that leverage the user's most specialized equipment. Example: `barbell_and_rack` + `has_gymnastics_rings` → powerlifting, olympic, bodybuilding, calisthenics(intermediate, advanced). Prefer calisthenics programs that integrate ring work alongside barbell lifts if the user's goal aligns.

### C.4 — Level Verification Benchmarks

```
Strength benchmarks (male, 1RM / BW ratio):
  beginner:     squat < 1.0x, bench < 0.75x, deadlift < 1.25x
  intermediate: squat 1.0-1.5x, bench 0.75-1.25x, deadlift 1.25-2.0x
  advanced:     squat > 1.5x, bench > 1.25x, deadlift > 2.0x

Calisthenics benchmarks:
  beginner:     < 5 pull-ups, no freestanding handstand
  intermediate: 10+ pull-ups, 15s+ handstand hold, muscle-up attempts
  advanced:     muscle-up, front lever, planche progression

Female adjustment: if sex = female, multiply all male strength benchmarks by 0.7 before cross-validation.
  Example: female intermediate squat = 0.7-1.05x BW (instead of 1.0-1.5x)
```

---

## Section D: Generation Rules

### Stage 1: Standard Plan

The LLM executes these steps in order:

1. **Match system** — Map the user's goal to 1-2 candidate systems using C.2
2. **Match level** — Use self-assessed level; if training history data is provided, cross-validate against C.4 benchmarks. **When self-assessment conflicts with benchmark data, the benchmark data wins.** Use the benchmark-determined level to filter programs. Explain the override to the user in a supportive tone (e.g., "Based on your squat at 0.8x BW, an intermediate program will set you up for faster progress and safer loading than jumping to advanced")
3. **Filter programs** — From candidate systems × level, filter programs using C.1. Prefer programs whose frequency aligns with the user's days/week
4. **Recommend 1 primary + 1 alternative** — Explain why the primary is the best fit and why the alternative is also viable
5. **Output weekly schedule** — Read the recommended program file at `Barlore/programs/{system}/{program_id}.md` (if file reading is available) and expand the full weekly schedule with exercises, sets, reps, and intensity. If file reading is unavailable, construct the schedule from the embedded Decision Matrix data (periodization type, system conventions) and flag the output with the `[Preview]` disclaimer from Section A. If Stage 2 adjustments are needed (injuries or equipment constraints detected), skip the standard schedule output and go directly to Stage 2 to produce a single merged output

### Stage 1 Output Format

```markdown
## Recommended Program: {name}
**Why this program:** ...
**Alternative:** {name} — ...

## Weekly Schedule
### Day 1: {focus}
| Exercise | Sets | Reps | Intensity |
|----------|------|------|-----------|
| ...      | ...  | ...  | ...       |

### Day 2: {focus}
...
```

### Stage 2: Adjustments (merged output)

Triggered ONLY when the user has filled injuries/limitations (field 7) or has equipment constraints that require exercise substitution. When Stage 2 is triggered, **do not output the unmodified Stage 1 schedule first** — produce a single final schedule with the adjustment log on top.

1. **Flag** — Identify exercises that conflict with the user's limitations. When file reading is available, check each exercise's `injury_risk.contraindications` and `equipment` fields from `Barlore/exercises/{id}.md`
2. **Substitute** — Replace flagged exercises using the exercise's `alternatives` field. Choose alternatives that match the user's available equipment
3. **Explain** — For each substitution, state the original exercise, the issue, the substitute, and why it works
4. **Output** — Print the adjustment log, then the final weekly schedule with substitutions already applied. Only one schedule is output.

### Stage 2 Output Format

```markdown
## Adjustments Applied

| Original | Issue | Substitute | Reason |
|----------|-------|------------|--------|
| ...      | ...   | ...        | ...    |

## Weekly Schedule (adjusted)
### Day 1: {focus}
| Exercise | Sets | Reps | Intensity |
|----------|------|------|-----------|
| ...      | ...  | ...  | ...       |
...
```

### Additional Guidance Triggers

Appended after the schedule when conditions are met:

| Condition | Action |
|-----------|--------|
| age >= 35 | Append key points from `crosscutting/special_populations/masters_athletes.md`. Frame advice as optimization, not limitation — e.g., "recovery optimization becomes more important" rather than "you need more rest because of your age." Focus on: allow extra recovery between high-intensity sessions, protein 2.0+ g/kg, proactive joint care (warm-up quality, load management) |
| sex = female | Append key points from `crosscutting/special_populations/female_athletes.md`: menstrual cycle phase adjustments, RED-S awareness, ACL injury prevention |
| body_weight + body_composition_goal both filled | Append protein target (1.6-2.2 g/kg per `crosscutting/nutrition/protein_requirements.md`) and caloric direction (surplus/deficit/maintenance per goal) |

Guidance is kept to 3-5 bullet points per trigger — brief pointers, not full articles.

---

## File Paths

| File | Purpose |
|------|---------|
| `Barlore/prompts/plan_generator.md` | The prompt template (deliverable) |
| `Barlore/scripts/build_plan_matrix.py` | Optional: regenerates the Section C tables from `index/programs.json` |

---

## Out of Scope

- Detailed nutrition plans (only brief directional guidance)
- Detailed recovery protocols (only brief pointers)
- Periodization across multiple mesocycles (the plan covers one cycle of the recommended program)
- Progress tracking or plan updates over time
- Web UI or interactive CLI
