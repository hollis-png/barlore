# Barlore Learning Guide

> **Instructions:** Fill in Section A (Your Current State) below, then paste this entire file into any LLM.
> The LLM will tell you what to read next, what to skip, and why — based on where you are right now.

---

## Section A: Your Current State

> Fill in what you know. Write `not_sure` for anything you're uncertain about.

**1. Training experience:**
<!--
  Examples:
  • "Never trained before"
  • "3 months, following Starting Strength"
  • "1 year, mostly machines, switching to barbell"
  • "2 years, running PPL, hit a plateau"
-->


**2. Current program (if any):**
<!-- Program name, or "none" / "random gym sessions" -->


**3. What's bothering you right now? (select all that apply)**
<!--
  • I don't know where to start
  • I don't understand my program's notation (sets, reps, RPE)
  • I don't know how to do the exercises correctly
  • I'm not sure I'm eating enough / eating right
  • I'm sore all the time and don't know if that's normal
  • Progress has stalled — same weight for 2+ weeks
  • Something hurts (joint pain, not muscle soreness)
  • I've finished my program cycle and don't know what's next
  • I want to understand WHY my program works, not just follow it
  • I want to switch goals (e.g., from strength to muscle building)
  • Nothing specific — I just want to learn more about training
-->


**4. Equipment available:**
<!-- full_gym / barbell_and_rack / dumbbells_only / bodyweight_only -->


**5. Days per week you can train:**


---

## Section B: Knowledge Base Reference

The Barlore knowledge base is organized in three learning layers. Each layer answers one question:

### Layer 1 — "What should I do?" (Action)

| Step | Content | URL |
|------|---------|-----|
| Check conditions | Equipment, schedule, frequency | (use Section A answers) |
| Pick a goal | Goal → program mapping | `Barlore/index/goal_index.json` |
| Pick a program | Filtered recommendations | `Barlore/index/programs.json` |
| Read the program | Understand sets, reps, intensity | `Barlore/glossary.md` |
| Learn movements | Exercise execution cues | `Barlore/exercises/{id}.md` |
| Start tracking | Workout log template | `Barlore/prompts/workout_log.md` |

### Layer 2 — "Why does this work?" (Understanding)

| Topic | Content | URL |
|-------|---------|-----|
| Progressive overload | Why adding weight/reps matters | `Barlore/core/progressive_overload.md` |
| Protein & calories | How much to eat, with examples | `Barlore/crosscutting/nutrition/protein_requirements.md`, `Barlore/crosscutting/nutrition/energy_balance.md` |
| Body recomposition | Gaining muscle while losing fat | `Barlore/crosscutting/nutrition/body_recomposition.md` |
| Hypertrophy mechanisms | What makes muscles grow | `Barlore/core/hypertrophy_mechanisms.md` |
| Volume landmarks | How many sets is enough | `Barlore/core/volume_landmarks.md` |
| Recovery timing | SRA curve and rest days | `Barlore/core/sra_curve.md` |
| Deload | Planned recovery weeks | `Barlore/core/deload.md` |
| Sleep | Why 7-9 hours matters | `Barlore/crosscutting/recovery/sleep.md` |

### Layer 3 — "What's next?" (Progression)

| Topic | Content | URL |
|-------|---------|-----|
| Testing strength | 1RM testing and training max | `Barlore/core/testing_protocols.md` |
| Training to failure | When to push, when to hold back | `Barlore/core/training_to_failure.md` |
| Injury management | Load adjustment and tissue health | `Barlore/crosscutting/injury_prevention/load_management.md`, `Barlore/crosscutting/injury_prevention/connective_tissue.md` |
| Periodization | Beyond linear progression | `Barlore/core/periodization.md` |
| System guides | Intermediate programming logic | `Barlore/system_guides/{system}_{level}_guide.md` |
| Body recomposition | When to switch to bulk/cut | `Barlore/crosscutting/nutrition/body_recomposition.md` |

---

## Section C: Generation Rules

Follow these steps to generate a personalized learning recommendation.

### Step 1: Determine the user's layer

Based on their training experience and current concerns:

- **No program / < 1 month / "don't know where to start"** → Layer 1
- **Following a program / 1–3 months / questions about why** → Layer 2
- **3+ months / stalled / hurt / program ended** → Layer 3
- **Mixed concerns** → Identify the highest-priority concern and start there

### Step 2: Map concerns to specific content

Use the "What's bothering you" responses to select the exact entries:

| Concern | Read this | Layer |
|---------|-----------|-------|
| Don't know where to start | goal_index → programs → beginner_lifters | 1 |
| Don't understand notation | glossary.md (Reading a Program Table) | 1 |
| Don't know how to do exercises | exercises/{id}.md for their program's exercises | 1 |
| Not sure about nutrition | protein_requirements + energy_balance (worked examples) | 2 |
| Sore all the time | sra_curve + deload + sleep | 2 |
| Want to understand why | progressive_overload + hypertrophy_mechanisms | 2 |
| Progress stalled | testing_protocols + periodization | 3 |
| Something hurts | load_management + connective_tissue | 3 |
| Program finished | system_guides + programs by goal | 3 |
| Want to switch goals | goal_index → new goal programs | 1 (restart) |

### Step 3: Generate the reading list

Output format:

```
## Your Current Layer: [1/2/3]

Based on [brief reason], here's what to read next:

### Read Now (addresses your current concern)
1. [Title](URL) — one-sentence reason why this is relevant to you
2. [Title](URL) — one-sentence reason

### Read Later (when you're ready for the next layer)
- [Title](URL) — what it covers and when it becomes relevant

### Skip For Now
- [Topic] — why it's not relevant yet (e.g., "Training to failure is for intermediate+ trainees; focus on building consistent form first")
```

### Step 4: If the user has a program, check their exercises

If the user named a specific program and their concern involves exercise execution:
1. Look up the program in `programs.json` to get its `exercise_refs`
2. List the 3–5 most important exercises (primary role) with links to their exercise pages
3. For each, give the single most important execution cue from the exercise's technical_notes

### Step 5: Actionable next step

End with one concrete action the user can take today:
- "Open workout_log.md, fill in today's date, and do Session A of [program]"
- "Read protein_requirements.md and calculate your daily target using the worked example"
- "Test your squat 5RM next session using the protocol in testing_protocols.md"
