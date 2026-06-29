---

id: gzclp
name: GZCLP
aliases: [GZCL Linear Progression, Cody GZCLP]
category: program
system: powerlifting
goal: Build strength on competition lifts through a tiered set structure that tolerates more volume than simple 5x5 while retaining novice-friendly linear progression
goals: [strength, hypertrophy]
level: beginner
duration_weeks: 16
frequency_per_week: 4
periodization: linear
origin: classic
progression_model: >
  Three tiers with independent progression.
  T1 (competition lifts): 5×3+ (AMRAP last set). Add 5 kg lower / 2.5 kg upper each session.
  Fail T1: next session 6×2 → then 10×1 → third fail: reset weight 15%, restart 5×3+.
  T2 (supplemental): 4×10. Add weight when all 40 reps completed.
  Fail T2: drop to 3×10; second fail: reset 10%.
  T3 (accessories): 3×15+ AMRAP. Add weight when ≥ 25 cumulative reps across 3 sets.

exercises:
  - ref: back_squat
    role: primary
    frequency_per_week: 4
    technical_notes: >
      T1 Day 1 and Day 3 (5×3+); T2 Day 2 and Day 4 (4×10 at ~50-60% of T1 load).
      Squats appear in every session as either T1 or T2.

  - ref: bench_press
    role: primary
    frequency_per_week: 2
    technical_notes: >
      T1 Day 1 (5×3+). T2 Day 3 (4×10). Alternates top-tier role with overhead_press.

  - ref: overhead_press
    role: primary
    frequency_per_week: 2
    technical_notes: >
      T1 Day 3 (5×3+). T2 Day 1 (4×10). Alternates with bench press.

  - ref: conventional_deadlift
    role: primary
    frequency_per_week: 2
    technical_notes: >
      T1 Day 2 (5×3+). T2 Day 4 (4×10; Romanian deadlift is a common T2 substitute).

  - ref: pullups
    role: secondary
    frequency_per_week: 4
    technical_notes: >
      T3 on all four days (3×15+ AMRAP). Add load or difficulty when ≥ 25 reps across 3 sets.
      Band-assisted acceptable for beginners; ring rows as regression.

sources:
  - title: "GZCL Method — The Tier System"
    author: "LeClair, C. (u/Cody_LeClair)"
    publisher: "swoleateveryheight.com; r/gzcl"
    year: 2014
    credibility: practitioner
---

# GZCLP

Created by powerlifter Cody LeClair. A four-day linear progression program using three tiers of diminishing specificity and increasing volume. Tolerates more training stimulus than Starting Strength while remaining appropriate for beginners and early-intermediate lifters.

## Design Philosophy — Why Three Tiers

GZCLP is built around Cody LeClair's observation that simple 5×5 programs (Starting Strength, StrongLifts) produce diminishing returns after 2–3 months because they only train one quality: heavy low-rep strength. The tier system solves this by training three qualities simultaneously, each with its own progression:

**Tier 1 (heavy, low-rep)** trains maximal strength through the competition lifts at 5×3. This is the same stimulus as Starting Strength, but at slightly lower reps per set — which means heavier loads for the same number of total reps. The AMRAP last set provides autoregulation: if you crush the set, your training max is probably conservative; if you barely get 3, it's well-calibrated.

**Tier 2 (moderate, moderate-rep)** trains the same movement pattern at 3×10 with lighter weight. This accumulates hypertrophy volume that a pure strength program lacks. More muscle cross-sectional area means a higher strength ceiling later. T2 progresses independently of T1, so you can keep building muscle even when your heavy strength stalls.

**Tier 3 (light, high-rep)** is isolation work for weak points and joint health. It produces the least fatigue per set and addresses imbalances that compound lifts miss.

**Why the failure cascade matters:** When T1 stalls at 5×3, you don't deload — you change the rep scheme to 6×2, then 10×1. This extends the linear progression by reducing reps per set while increasing total sets, so you can continue adding weight by reducing per-set difficulty. Only after exhausting all three rep schemes do you reset. This gives beginners 3–4 months of additional progression compared to programs that deload at the first stall.

## Four-Day Schedule

| Day | T1 — 5×3+ | T2 — 4×10 | T3 — 3×15+ |
|-----|-----------|-----------|------------|
| 1 | Back Squat | Bench Press | Pull-ups |
| 2 | OHP | Deadlift | Pull-ups |
| 3 | Deadlift | Back Squat | Pull-ups |
| 4 | Bench Press | OHP | Pull-ups |

## Tier Definitions

| Tier | Sets × Reps | Purpose | Progression trigger |
|------|-------------|---------|---------------------|
| T1 | 5×3 + AMRAP | Specificity — competition lift strength | Every session: +5 kg lower / +2.5 kg upper |
| T2 | 4×10 | Supplemental volume at sub-maximal load | All 40 reps completed cleanly |
| T3 | 3×15+ AMRAP | Accessories / GPP | ≥ 25 total reps across 3 sets |

## T1 Failure Cascade

| Failure | Response |
|---------|----------|
| 1st fail | Switch to 6×2 at same weight next session |
| 2nd fail | Switch to 10×1 at same weight |
| 3rd fail | Reset load −15%, restart at 5×3+ |

## Common T3 Accessories

| Session slot | Examples |
|--------------|---------|
| Upper T3 | Pull-ups, dips, face pulls, triceps pushdown |
| Lower T3 | Leg press, lying leg curl, calf raise, ab wheel |

> Beginner alternative to `starting_strength` with higher volume tolerance. Transition to `texas_method` or full GZCL block when linear gains end.
