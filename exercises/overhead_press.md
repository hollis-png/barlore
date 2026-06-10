---
id: overhead_press
name: Overhead Press
status: complete
aliases: [OHP, Strict Press, Military Press]
category: exercise
pattern: [vertical press]
muscles:
  - id: deltoid
    role: primary
  - id: triceps_brachii
    role: primary
  - id: pec_major_clavicular
    role: secondary
  - id: core
    role: secondary
equipment: [barbell, rack]
difficulty: intermediate
alternatives: []
muscle_activation_studies:
  - source_id: kettlebell_vs_db_2018
    doi: null
    n: 21
    population: "healthy adults"
    condition:
      implement: dumbbell
      tempo: "2s concentric / 2s eccentric"
      phase: full_rep
    measurements:
      - {muscle: deltoid_anterior, mean_pct_mvc: 63.30, sd: 13.30}
      - {muscle: pectoralis_major, mean_pct_mvc: 31.00, sd: 20.00}
  - source_id: kettlebell_vs_db_2018
    n: 21
    population: "healthy adults"
    condition:
      implement: kettlebell
      tempo: "2s concentric / 2s eccentric"
      phase: full_rep
    measurements:
      - {muscle: deltoid_anterior, mean_pct_mvc: 57.90, sd: 15.00}
  - source_id: marcos_pardo_2020
    doi: null
    n: 13
    population: "strength-trained men"
    condition:
      load_pct_1rm: 60
      reps: 12
      implement: barbell
      style: front_press
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 33.30, sd: null}
      - {muscle: deltoid_lateral,   mean_pct_mvc: 27.90, sd: null}
      - {muscle: deltoid_posterior, mean_pct_mvc: 11.40, sd: null}

joint_rom_required:
  shoulder_flexion_deg: 180
  notes: "Full lockout requires 180° shoulder flexion; scapular upward rotation, elevation, and posterior tilt required; elbows track scapular plane (~30° anterior to frontal plane); peak deltoid anterior moment arm at ~120° shoulder flexion"
  source: "Military Press Technique; Barbell Overhead Press ROM"

strength_curve:
  type: ascending
  sticking_point: mid_range
  peak_force_position: lockout
  notes: "Sticking point between chin and forehead (nose level); bar must arc around face, maximizing horizontal moment arm at glenohumeral joint; resolved when head moves through and bar stacks over shoulder joint"
  source: "Overhead Press Sticking Points review"

sources:
  - title: "Starting Strength"
    author: "Mark Rippetoe"
    credibility: practitioner
  - title: "Kettlebell vs. Dumbbell Overhead Press Study"
    year: 2018
    doi: null
    credibility: rct
  - title: "Electromyographic activity of shoulder muscles during different variations of the shoulder press exercise"
    author: "Marcos-Pardo, P. J., et al."
    year: 2020
    doi: null
    credibility: rct
---

# Overhead Press

The overhead press is a vertical pressing movement, driving a barbell from the front rack overhead to full lockout while standing. It builds shoulder and triceps strength and demands significant core stability.

## Execution

1. Take the bar at shoulder height in a front rack, hands just outside shoulders
2. Brace the core and squeeze the glutes to lock the torso
3. Press the bar straight up, moving the head back slightly to clear the chin
4. Lock out overhead with the bar over the mid-foot, then lower under control

## Common Faults

- **Excessive layback** — turns it into an incline press and stresses the lower back
- **Pressing around the face** — inefficient bar path
- **Soft core** — energy leaks through the trunk

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Push press | Leg drive assists | Overloading the top |
| Seated press | No leg drive | Stricter shoulder work |

> For system-specific training applications, see each system's lens entry.
