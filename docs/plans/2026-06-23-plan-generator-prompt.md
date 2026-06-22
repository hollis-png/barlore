# Plan Generator Prompt — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a single-file prompt template (`Barlore/prompts/plan_generator.md`) that any LLM can use to generate a personalized training plan from the Barlore knowledge base, plus an optional script to regenerate the embedded programs table.

**Architecture:** A single Markdown file with 4 sections (System Prompt, User Profile form, Decision Matrix, Generation Rules). The Decision Matrix embeds a programs table generated from `index/programs.json`. A Python script can regenerate that table on demand.

**Tech Stack:** Markdown (prompt), Python 3 (matrix generator script)

## Global Constraints

- All content in English
- Exercise/program names must use Barlore canonical IDs
- The prompt must work when pasted into any LLM (ChatGPT, Gemini, Claude.ai) — no tool-specific syntax
- The embedded programs table must match the current `index/programs.json` exactly
- Spec location: `Barlore/docs/specs/2026-06-23-plan-generator-prompt-design.md`

---

### Task 1: Build the matrix generator script

**Files:**
- Create: `Barlore/scripts/build_plan_matrix.py`

**Interfaces:**
- Consumes: `Barlore/index/programs.json`
- Produces: a Markdown table string printed to stdout (piped into Task 2, or copy-pasted)

This script reads `index/programs.json` and outputs the programs table formatted for embedding in the prompt. It is run manually when programs change; its output is pasted into Section C.1 of the prompt.

- [ ] **Step 1: Write the script**

```python
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
```

- [ ] **Step 2: Run the script and verify output**

Run: `cd Barlore && python3 scripts/build_plan_matrix.py`

Expected: a Markdown table with 41 rows, sorted by system → level → program_id. Verify the header row and at least 3 data rows look correct.

- [ ] **Step 3: Commit**

```bash
cd Barlore && git add scripts/build_plan_matrix.py && git commit -m "feat: add build_plan_matrix.py to generate programs table for plan_generator prompt"
```

---

### Task 2: Write the prompt template

**Files:**
- Create: `Barlore/prompts/plan_generator.md`

**Interfaces:**
- Consumes: output from Task 1 (programs table), spec at `docs/specs/2026-06-23-plan-generator-prompt-design.md`
- Produces: the deliverable prompt file

This is the main deliverable. The file has 4 sections (A-D) as defined in the spec. Section C.1 contains the full programs table from Task 1's output. The user fills Section B and pastes the entire file into an LLM.

- [ ] **Step 1: Generate the programs table**

Run: `cd Barlore && python3 scripts/build_plan_matrix.py > /tmp/programs_table.md`

- [ ] **Step 2: Write the prompt file**

Create `Barlore/prompts/plan_generator.md` with the following complete content. The `{PROGRAMS_TABLE}` placeholder below must be replaced with the actual content of `/tmp/programs_table.md` from Step 1.

````markdown
# Barlore Training Plan Generator

> **Instructions:** Fill in Section B (Your Profile) below, then paste this entire file into any LLM.
> The LLM will use the embedded data and rules to generate a personalized training plan.

---

## Section A: System Prompt

You are a strength and conditioning coach with access to the Barlore knowledge base — a structured encyclopedia of training programs, exercises, and sports science.

**Rules:**

1. Base all recommendations on Barlore entries listed in Section C. Do not invent programs or exercises that are not in the knowledge base.
2. Cite program IDs and exercise IDs from Barlore when referencing them.
3. If you have file-reading capability, read the referenced Barlore files for full exercise details:
   - Programs: `Barlore/programs/{system}/{program_id}.md`
   - Exercises: `Barlore/exercises/{exercise_id}.md`
4. If you do NOT have file-reading capability: rely exclusively on the Decision Matrix in Section C. Do not reconstruct program structures from general training knowledge. Begin your output with:
   `[Preview: generated without reading Barlore source files — exercise details may differ from the canonical knowledge base]`
5. All output in English. Use Barlore canonical exercise names.

---

## Section B: Your Profile

> **Fill in the fields below.** Required fields are marked with *.

### Required

**1. Primary Goal* (select one):**
<!-- strength / hypertrophy / athletic_performance / calisthenics_skills / general_fitness / sport_specific -->


**2. Self-Assessed Level* (select one):**
<!-- beginner / intermediate / advanced -->


**3. Training History*:**
<!-- Years of training + key lift numbers (e.g., "2 years, squat 100kg, bench 70kg, deadlift 130kg") or skills (e.g., "can do 12 pull-ups, 10s handstand hold") -->


**4. Available Equipment* (select all that apply):**
<!-- full_gym / barbell_and_rack / dumbbells_only / bodyweight_only / has_strongman_implements / has_gymnastics_rings -->


**5. Days Per Week* (number, 2-6):**


**6. Session Duration* (select one):**
<!-- 30-45min / 45-60min / 60-90min / 90min+ -->


### Optional

**7. Injuries / Limitations:**
<!-- Any current or past injuries, mobility restrictions, or movements to avoid -->


**8. Age:**


**9. Sex:**
<!-- male / female -->


**10. Body Weight (kg):**


**11. Body Composition Goal (select one):**
<!-- gain_muscle / lose_fat / maintain -->


---

## Section C: Decision Matrix

### C.1 — Programs Table

{PROGRAMS_TABLE}

### C.2 — Goal-to-System Mapping

```
strength              → powerlifting, strongman
hypertrophy           → bodybuilding
athletic_performance  → olympic, crossfit
calisthenics_skills   → calisthenics
general_fitness       → bodybuilding(beginner), crossfit
sport_specific        → select based on the user's sport:
                          power/contact sports → powerlifting or strongman
                          explosive/speed sports → olympic or crossfit
                          gymnastics/climbing → calisthenics
                          aesthetic sports → bodybuilding
                          endurance sports → crossfit (with cardio emphasis)
                          if unclear → ask the user to clarify
```

### C.3 — Equipment Feasibility

| equipment_tier | feasible_systems | notes |
|----------------|------------------|-------|
| full_gym | all | |
| barbell_and_rack | powerlifting, olympic, bodybuilding | no cable/machine accessories |
| dumbbells_only | bodybuilding(beginner) | needs program modification |
| bodyweight_only | calisthenics | only feasible system |
| has_strongman_implements | + strongman | adds strongman to base tier |
| has_gymnastics_rings | + calisthenics(intermediate, advanced) | adds ring-based progressions |

**Multi-select rule:** When the user selects multiple equipment tiers, feasible systems = union of all tiers. Prefer programs that leverage the user's most specialized equipment.

### C.4 — Level Verification Benchmarks

```
Strength benchmarks (male, 1RM / body weight ratio):
  beginner:     squat < 1.0x, bench < 0.75x, deadlift < 1.25x
  intermediate: squat 1.0-1.5x, bench 0.75-1.25x, deadlift 1.25-2.0x
  advanced:     squat > 1.5x, bench > 1.25x, deadlift > 2.0x

Calisthenics benchmarks:
  beginner:     < 5 pull-ups, no freestanding handstand
  intermediate: 10+ pull-ups, 15s+ handstand hold, muscle-up attempts
  advanced:     muscle-up, front lever, planche progression

Female adjustment: if sex = female, multiply all male strength benchmarks
by 0.7 before cross-validation.
  Example: female intermediate squat = 0.7-1.05x BW (instead of 1.0-1.5x)
```

---

## Section D: Generation Rules

Follow these steps in order to generate the training plan.

### Step 1: Match System

Map the user's Primary Goal to 1-2 candidate training systems using C.2. Intersect with the user's equipment feasibility from C.3 (union of all selected equipment tiers). If no systems remain feasible, tell the user which equipment they would need.

### Step 2: Match Level

Use the user's Self-Assessed Level as the starting point. If Training History includes lift numbers or skill benchmarks, cross-validate against C.4.

**When self-assessment conflicts with benchmark data, the benchmark data wins.** Use the benchmark-determined level to filter programs. Explain the override in a supportive tone:
> "Based on your squat at 0.8x BW, an intermediate program will set you up for faster progress and safer loading than jumping straight to advanced."

If sex = female, apply the 0.7x multiplier to strength benchmarks before comparison.

If no benchmark data is provided (user left Training History vague), accept the self-assessment.

### Step 3: Filter Programs

From candidate systems × verified level, filter programs using C.1. Among matches, prefer programs whose typical frequency best aligns with the user's Days Per Week.

### Step 4: Recommend

Recommend **1 primary program + 1 alternative**. For each, state:
- The program name and ID
- Why it fits the user's goal, level, and schedule
- What distinguishes the alternative from the primary

### Step 5: Output Weekly Schedule

**If you have file-reading capability:** read the program file at `Barlore/programs/{system}/{program_id}.md` and expand the full weekly schedule with exercises, sets, reps, and intensity as prescribed.

**If you do not have file-reading capability:** construct the schedule from the program's periodization type (from C.1) and the system's general conventions. Flag the output with the `[Preview]` disclaimer from Section A.

**If the user has injuries/limitations (field 7) or equipment constraints that require exercise substitution:** skip the standard schedule and go directly to Step 6 to produce a single merged output.

### Step 6: Adjustments (if needed)

Triggered ONLY when injuries/limitations or equipment constraints require exercise substitution. Do not output the unmodified schedule first — produce one final schedule with the adjustment log on top.

1. **Flag** — Identify exercises in the schedule that conflict with the user's limitations. If file-reading is available, check each exercise's `injury_risk.contraindications` and `equipment` fields from `Barlore/exercises/{exercise_id}.md`.
2. **Substitute** — Replace flagged exercises using the exercise's `alternatives` field. Choose alternatives compatible with the user's equipment.
3. **Explain** — For each substitution, state the original, the issue, the substitute, and why it works.
4. **Output** — Print the adjustment log, then the final weekly schedule with substitutions applied.

**Output format (no adjustments needed):**

```
## Recommended Program: {name}
Why this program: ...
Alternative: {name} — ...

## Weekly Schedule
### Day 1: {focus}
| Exercise | Sets | Reps | Intensity |
|----------|------|------|-----------|
| ...      | ...  | ...  | ...       |
```

**Output format (adjustments needed):**

```
## Recommended Program: {name}
Why this program: ...
Alternative: {name} — ...

## Adjustments Applied
| Original | Issue | Substitute | Reason |
|----------|-------|------------|--------|
| ...      | ...   | ...        | ...    |

## Weekly Schedule (adjusted)
### Day 1: {focus}
| Exercise | Sets | Reps | Intensity |
|----------|------|------|-----------|
| ...      | ...  | ...  | ...       |
```

### Step 7: Additional Guidance

Append brief guidance (3-5 bullet points per section) when these conditions are met:

**If age >= 35:**
> ## Recovery Optimization
> Frame as performance optimization, not age-related limitation.
> - Allow extra recovery between high-intensity sessions
> - Protein intake 2.0+ g/kg to support muscle protein synthesis
> - Proactive joint care: prioritize warm-up quality and load management
> Reference: `Barlore/crosscutting/special_populations/masters_athletes.md`

**If sex = female:**
> ## Training Considerations
> - Consider menstrual cycle phase when planning high-intensity sessions
> - Monitor for RED-S (Relative Energy Deficiency in Sport) signs
> - Include ACL injury prevention work (hamstring strengthening, landing mechanics)
> Reference: `Barlore/crosscutting/special_populations/female_athletes.md`

**If body_weight AND body_composition_goal are both filled:**
> ## Nutrition Direction
> - Protein target: 1.6-2.2 g/kg body weight daily
> - gain_muscle → moderate caloric surplus (300-500 kcal/day above maintenance)
> - lose_fat → moderate caloric deficit (300-500 kcal/day below maintenance), protein toward 2.2 g/kg
> - maintain → eat at maintenance, protein at 1.6-1.8 g/kg
> Reference: `Barlore/crosscutting/nutrition/protein_requirements.md`, `Barlore/crosscutting/nutrition/energy_balance.md`
````

- [ ] **Step 3: Replace the `{PROGRAMS_TABLE}` placeholder**

Open `Barlore/prompts/plan_generator.md` and replace the literal text `{PROGRAMS_TABLE}` with the contents of `/tmp/programs_table.md` (the table generated in Step 1).

- [ ] **Step 4: Verify the prompt file**

Run: `wc -l Barlore/prompts/plan_generator.md`

Expected: approximately 180-220 lines. Verify the file contains all 4 sections (A through D) and the programs table has 41 data rows plus a header.

Run: `grep -c '|' Barlore/prompts/plan_generator.md`

Expected: at least 50 pipe characters (tables are present).

- [ ] **Step 5: Commit**

```bash
cd Barlore && git add prompts/plan_generator.md && git commit -m "feat: add plan_generator.md prompt template for personalized training plan generation"
```

---

### Task 3: Smoke test with a sample user profile

**Files:**
- No files created or modified — this is a validation task

**Interfaces:**
- Consumes: `Barlore/prompts/plan_generator.md` from Task 2

Fill in a sample profile and verify the prompt is well-formed and an LLM can follow it.

- [ ] **Step 1: Create a test profile**

Open `Barlore/prompts/plan_generator.md` and fill Section B with this test data:

```
1. Primary Goal: strength
2. Self-Assessed Level: intermediate
3. Training History: 3 years, squat 120kg, bench 85kg, deadlift 150kg at 80kg BW
4. Available Equipment: full_gym
5. Days Per Week: 4
6. Session Duration: 60-90min
7. Injuries / Limitations: mild left shoulder impingement — overhead pressing causes pain
8. Age: 32
9. Sex: male
10. Body Weight (kg): 80
11. Body Composition Goal: gain_muscle
```

- [ ] **Step 2: Verify expected LLM behavior**

Without running through an LLM, manually trace through Section D:

1. Goal `strength` → C.2 maps to `powerlifting, strongman`
2. Level: self-assessed `intermediate`, BW=80kg, squat=120kg (1.5x), bench=85kg (1.06x), deadlift=150kg (1.88x) → all within intermediate range ✓, no override needed
3. Filter C.1: powerlifting intermediate → `5_3_1`, `texas_method`. strongman intermediate → `cube_method_strongman`, `juggernaut_method_strongman`, `strongman_intermediate_block`. 4 days/week favors most of these
4. Primary recommendation likely `5_3_1` (4 days, proven intermediate program). Alternative likely `texas_method`
5. Shoulder impingement → Stage 2 triggered. Overhead press flagged. Should substitute with an alternative that avoids overhead pressing
6. Age 32 → no masters trigger
7. BW + gain_muscle → nutrition section triggered (protein 1.6-2.2 g/kg = 128-176g/day, moderate surplus)

Verify all these steps are reachable from the prompt text alone.

- [ ] **Step 3: Clean up the test profile**

Reset Section B fields in `Barlore/prompts/plan_generator.md` back to blank (the prompt should ship with empty fields for users to fill).
