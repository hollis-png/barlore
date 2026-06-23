---
id: rp_hypertrophy
name: RP Hypertrophy Program
aliases: [Renaissance Periodization Hypertrophy, RP Hypertrophy 4-Day]
category: program
system: bodybuilding
goal: Maximize skeletal muscle hypertrophy via RIR-based autoregulated volume progression from MEV toward MRV across a 5-week mesocycle
level: intermediate
duration_weeks: 5
frequency_per_week: 4
periodization: block
origin: classic
progression_model: >
  Reps in Reserve (RIR) decreases one unit each week during the accumulation block:
  W1 3RIR → W2 2RIR → W3 1RIR → W4 0-1RIR → W5 deload 4-5RIR.
  Volume auto-regulates via a recovery scale assessed before each session:
  -2 = significant cut, -1 = minor cut, 0 = maintain, +1 = add 1 set, +2 = add 1-2 sets.
  Absolute load increases ~5-10 lb on compounds and ~2.5-5 lb on isolations each week.
  Deload: first 50% of sessions at 70% peak load, second 50% at 50% peak load; total volume = 50% of Week 1 baseline.
  Multi-mesocycle order: Basic Hypertrophy (10 wks) → Metabolite Focus (5 wks) → Resensitization (3 wks).

exercises:
  - ref: bench_press
    role: primary
    frequency_per_week: 2
    sets: 2
    reps: "8-12"
    technical_notes: >
      Day 1 (Upper A) and Day 3 (Upper B). Compound fractional counting: 1.0 set chest,
      0.5 anterior deltoid, 0.5 triceps. Per-session direct sets per muscle ≤ 10.

  - ref: seated_cable_rows
    role: primary
    frequency_per_week: 2
    sets: 2
    reps: "10-15"
    technical_notes: >
      Day 1 (Upper A). Counts 1.0 lat, 0.5 posterior deltoid, 0.5 biceps.

  - ref: pullups
    role: primary
    frequency_per_week: 2
    sets: 2
    reps: "6-10"
    technical_notes: >
      Day 3 (Upper B). Add load via belt when 3×10 bodyweight achieved.

  - ref: back_squat
    role: primary
    frequency_per_week: 2
    sets: 2
    reps: "6-10"
    technical_notes: >
      Day 2 (Lower A). Counts 1.0 quad, 0.5 glute. Accumulate from MEV (~8 sets/wk)
      toward MRV (~20 sets/wk) over the mesocycle via recovery-scale feedback.

  - ref: romanian_deadlift
    role: primary
    frequency_per_week: 2
    sets: 2
    reps: "8-12"
    technical_notes: >
      Day 4 (Lower B). Hamstring primary (1.0 set). Keep hips back, soft knee bend.

sources:
  - title: "Scientific Principles of Hypertrophy Training"
    author: "Israetel, M., Hoffman, J., Smith, C. W."
    year: 2021
    credibility: expert_consensus
  - title: "RP Training Volume Landmarks for Bodybuilding"
    author: "Israetel, M."
    publisher: "RP Strength"
    credibility: practitioner
---

# RP Hypertrophy Program

The Renaissance Periodization Hypertrophy Program (Israetel, Hoffman & Smith 2021) uses RIR-based autoregulation and MEV→MRV volume progression to systematically drive hypertrophy while managing accumulated fatigue within and across mesocycles.

## 4-Day Upper/Lower Split (Week 1 Baseline)

| Day | Focus | Key Exercises | Sets × Reps | RIR |
|-----|-------|---------------|-------------|-----|
| 1 — Upper A | Chest / Triceps / Back / Biceps | Incline DB Fly, Cable Triceps Ext, Seated Cable Row, Cable Biceps Curl | 2×10-15 each | 3 |
| 2 — Lower A | Quads / Hamstrings / Calves / Glutes / Delts | Back Squat, Lying Leg Curl, Calf Press, Hip Abductor, Cable Lateral Raise | 2×6-10 / 2×10-15 | 3 |
| 3 — Upper B | Back / Biceps / Chest | Pull-Up, EZ-Bar Preacher Curl, Incline Bench Press | 2×6-10 each | 3 |
| 4 — Lower B | Hamstrings / Glutes / Calves | Romanian Deadlift, Barbell Hip Thrust, Standing Calf Raise | 2×8-12 each | 3 |

## RIR Progression

| Week | Target RIR | Notes |
|------|-----------|-------|
| 1 | 3 | Establish baseline, validate weights |
| 2 | 2 | Moderate overload; add sets if recovery permits |
| 3 | 1 | Near-limit effort; assess joint and systemic fatigue |
| 4 | 0–1 | Peak overload; selected sets to concentric failure |
| 5 (Deload) | 4–5 | First half: 70% peak load; second half: 50% peak load; volume 50% of W1 |

## Volume Auto-Regulation Scale

| Rating | Recovery State | Action |
|--------|---------------|--------|
| +2 | No soreness, no pump | Add 1-2 sets next session |
| +1 | Recovered ahead of schedule | Add 1 set |
| 0 | Resolved just in time | Maintain current volume |
| -1 | Slightly sore or stalled | Minor volume reduction |
| -2 | Severely under-recovered | Significant volume cut |

## Fractional Set Counting (Compound Lifts)

| Exercise | Primary (1.0 set) | Secondary (0.5 set) | Tertiary (0.5 set) |
|----------|-------------------|---------------------|---------------------|
| Barbell Bench Press | Pectoralis Major | Anterior Deltoid | Triceps Brachii |
| Bent Over Barbell Row | Latissimus Dorsi | Posterior Deltoid | Biceps Brachii |
| Back Squat | Quadriceps | Gluteus Maximus | — |

## Multi-Mesocycle Block Structure

1. **Basic Hypertrophy** (2 × 5-week cycles = 10 weeks): 60–80% 1RM, 8–12 reps
2. **Metabolite Focus** (1 × 5-week cycle): 30–50% 1RM, 15–30 reps; myo-reps, drop sets, occlusion
3. **Resensitization** (3 weeks): MV only (~6 sets/week/muscle at 3 RIR); resets cellular sensitivity

> For muscle-group volume landmarks (MEV, MAV, MRV), see `core/volume_landmarks.md`.
