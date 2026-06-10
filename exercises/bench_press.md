---
id: bench_press
name: Bench Press
status: complete
aliases: [Flat Barbell Bench Press]
category: exercise
pattern: [horizontal press]
muscles:
  - id: pectoralis_major
    role: primary
  - id: triceps_brachii
    role: primary
  - id: deltoid_anterior
    role: secondary
equipment: [barbell, bench, rack]
difficulty: intermediate
variations: []
alternatives: []
muscle_activation_studies:
  - source_id: saeterbakken_2017
    doi: null
    n: 21
    population: "healthy males"
    condition:
      reps: 6
      phase: concentric
      grip_width: narrow
    measurements:
      - {muscle: pectoralis_major, mean_pct_mvc: 39.24, sd: 19.53}
      - {muscle: triceps_brachii,  mean_pct_mvc: 36.56, sd: 11.92}
  - source_id: saeterbakken_2017
    n: 21
    population: "healthy males"
    condition:
      reps: 6
      phase: concentric
      grip_width: regular
    measurements:
      - {muscle: pectoralis_major, mean_pct_mvc: 43.14, sd: 19.53}
      - {muscle: triceps_brachii,  mean_pct_mvc: 33.22, sd: 14.20}
  - source_id: saeterbakken_2017
    n: 21
    population: "healthy males"
    condition:
      reps: 6
      phase: concentric
      grip_width: wide
    measurements:
      - {muscle: pectoralis_major, mean_pct_mvc: 46.48, sd: 15.81}
  - source_id: marcos_pardo_2020
    doi: null
    n: 13
    population: "strength-trained men"
    condition:
      load_pct_1rm: 60
      reps: 12
      grip_width: standard
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 21.40, sd: null}
      - {muscle: deltoid_lateral,   mean_pct_mvc: 5.00,  sd: null}
      - {muscle: deltoid_posterior, mean_pct_mvc: 3.50,  sd: null}

joint_rom_required:
  elbow_flexion_deg: 79.5
  wrist_flexion_extension_deg: 11.9
  notes: "ROM at 15% BW load (Muyor et al. 2022); shoulder-width grip requires ~20° greater shoulder flexion and ~25° greater elbow extension vs. wide grip"
  source: "Muyor et al. 2022; Duffey 2008"

strength_curve:
  type: ascending
  sticking_point: bottom_third
  peak_force_position: lockout
  notes: "Sticking point 2-3 inches off chest; pectoralis major at maximal stretch and worst leverage; J-curve bar path shifts load over shoulder joint earlier"
  source: "Saeterbakken et al. 2017; Westside Barbell analysis"

sources:
  - title: "Starting Strength"
    author: "Mark Rippetoe"
    credibility: practitioner
  - title: "Effects of grip width on muscle strength and activation in the bench press"
    author: "Saeterbakken, A. H., Andersen, V., Brudeseth, A., Lund, H., Fimland, M. S."
    year: 2017
    doi: null
    credibility: rct
  - title: "Electromyographic activity of shoulder muscles during different variations of the shoulder press exercise"
    author: "Marcos-Pardo, P. J., et al."
    year: 2020
    doi: null
    credibility: rct
  - title: "Kinematics of the barbell bench press"
    author: "Muyor, J. M., et al."
    year: 2022
    doi: null
    credibility: rct
---

# Bench Press

The bench press is a horizontal pressing movement performed lying on a bench, pressing a barbell from the chest to full arm extension. It is one of the three powerlifting competition lifts.

## Execution

1. Lie back with eyes under the bar, feet planted, slight arch in the upper back
2. Grip slightly wider than shoulders, retract and depress the shoulder blades
3. Unrack and lower the bar to the lower chest under control
4. Press up and slightly back toward the rack over the shoulders

## Common Faults

- **Flaring the elbows to 90 degrees** — shoulder strain; tuck to ~45–75 degrees
- **Bouncing off the chest** — loses tension and control
- **Hips rising off the bench** — invalid in competition and unsafe

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Close grip | Hands narrower, more triceps | Triceps and lockout |
| Paused | Pause on the chest | Powerlifting specificity |

> For system-specific training applications, see each system's lens entry.
