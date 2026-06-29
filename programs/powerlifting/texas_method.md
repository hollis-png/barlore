---

id: texas_method
name: Texas Method
aliases: [TM]
category: program
system: powerlifting
goal: Break through novice stalls via weekly volume-recovery-intensity cycling on the squat, press, and deadlift
goals: [strength]
level: intermediate
duration_weeks: 12
frequency_per_week: 3
periodization: linear
origin: classic
progression_model: >
  Weekly progression: Volume Day accumulates fatigue; Recovery Day dissipates it;
  Intensity Day tests a new 5-rep PR. Load increases each week on Intensity Day.
  Stall protocol: two consecutive failed Intensity Day PRs → adjust Volume Day load,
  add variation, or deload 10% and rebuild.

exercises:
  - ref: back_squat
    role: primary
    frequency_per_week: 3
    technical_notes: >
      Volume Day (Mon): 5×5 at ~90% of current 5RM — primary overload stimulus.
      Recovery Day (Wed): 2×5 at ~80% of 5RM — active recovery, not a training stimulus.
      Intensity Day (Fri): 1×5 PR attempt. Low-bar back squat recommended throughout.

  - ref: bench_press
    role: primary
    frequency_per_week: 2
    technical_notes: >
      Alternates weekly with overhead_press. Week A: bench on Volume + Intensity;
      Week B: OHP on Volume + Intensity. Recovery Day: the other lift, 3×5 light.

  - ref: overhead_press
    role: primary
    frequency_per_week: 2
    technical_notes: >
      Alternates with bench press. Strict standing press, no leg drive.
      Week A Recovery: OHP 3×5 light. Week B Volume + Intensity: OHP 5×5 and 1×5 PR.

  - ref: conventional_deadlift
    role: primary
    frequency_per_week: 1
    technical_notes: >
      Intensity Day (Fri) only: 1×5 PR. Lower volume than squat due to higher CNS cost.
      Some variants replace mid-week deadlift frequency with power cleans on Recovery Day.

sources:
  - title: "Practical Programming for Strength Training"
    author: "Rippetoe, M., Kilgore, L."
    year: 2006
    credibility: practitioner
---

# Texas Method

Designed by Mark Rippetoe as the intermediate step after novice linear progression. Three days per week with distinct physiological roles: Volume, Recovery, Intensity.

## Design Philosophy — Why Volume/Recovery/Intensity

The Texas Method exists to solve the specific problem that ends beginner programs: when you can no longer add weight every session, but you can still add weight every week.

**Monday (Volume)** accumulates training stress through 5×5 at a moderate percentage. This is the stimulus day — high total volume drives the adaptation signal. The 5×5 format was chosen because it produces sufficient mechanical tension and metabolic stress without requiring loads so heavy that technique breaks down.

**Wednesday (Recovery)** uses lighter loads (80% of Monday's weight) at lower volume (2×5). This session maintains movement pattern practice and promotes active recovery without adding meaningful fatigue. Removing Wednesday entirely was tested and found to slightly impair Friday performance — the light stimulus helps maintain neural readiness.

**Friday (Intensity)** tests the adaptation with a single heavy set of 5 at a new personal record. This is where progression is measured: if you hit 5 reps, add weight next week. The weekly PR attempt is the core mechanism — it converts Monday's volume stimulus into demonstrated strength.

**Why this works when daily progression doesn't:** A novice can recover from a heavy session in 48–72 hours and set a new PR. An intermediate's SRA curve (see `sra_curve`) is longer — they need an entire week of stimulus + recovery to produce the same adaptation. The Texas Method structures that weekly cycle explicitly: stress → recover → express.

## Weekly Structure

| Day | Role | Squat | Press | Pull |
|-----|------|-------|-------|------|
| Monday | Volume | 5×5 @ ~90% 5RM | 5×5 bench or OHP | — |
| Wednesday | Recovery | 2×5 @ ~80% 5RM | 3×5 (opposite lift, light) | — |
| Friday | Intensity | 1×5 PR | 1×5 PR (same as Mon) | 1×5 deadlift PR |

## Press Alternation (A/B Weeks)

| Week | Volume + Intensity | Recovery |
|------|--------------------|----------|
| A | Bench Press | OHP 3×5 |
| B | Overhead Press | Bench Press 3×5 |

## Common Assistance

- Pull-ups / chin-ups: 3 sets on Volume Day after pressing
- Back extensions or good mornings: 3×10 on Intensity Day after deadlift
- Dips: Recovery Day triceps volume

## Progression Rules

1. Add 2.5 kg to upper lifts, 5 kg to squat/deadlift on Intensity Day each week
2. Two consecutive failed PRs = stall → adjust Volume Day or deload 10%
3. Volume Day should feel challenging but submaximal; if 5×5 is impossible, reduce load 5%

> Natural progression from `starting_strength`. When TM stalls, transition to `5_3_1` or block periodization.
