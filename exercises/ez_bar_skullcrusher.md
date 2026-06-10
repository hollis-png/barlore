---
id: ez_bar_skullcrusher
name: EZ-Bar Skullcrusher
status: complete
category: exercise
pattern: [isolation]
equipment: [ez_bar, bench]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 1

muscles:
  - id: triceps_long
    role: primary
  - id: triceps_lateral
    role: primary
  - id: triceps_medial
    role: secondary

# brettler_2023 (n=8): TRUE %MVIC — triceps (combined) 23.79% ± 9.19% at 65% 1RM.
# boehler_2011 (normalized to triangle push-up, NOT true %MVIC):
#   triceps_long 70% ± 20.9%, triceps_lateral 55% ± 14.1%.
# The boehler_2011 values are comparative within that study only.
muscle_activation_studies:
  - source_id: brettler_2023
    doi: null
    n: 8
    population: "trained adults, 65% 1RM"
    condition:
      load_pct_1rm: 65
      implement: ez_bar
      phase: full_rep
      notes: "TRUE %MVIC — NOT normalized to another exercise"
    measurements:
      - {muscle: triceps_long, mean_pct_mvc: 23.79, sd: 9.19}
  - source_id: boehler_2011
    doi: null
    n: null
    population: "healthy adults"
    condition:
      implement: ez_bar
      phase: full_rep
      notes: "Normalized to triangle push-up = 100%, NOT true %MVIC. Values are relative comparisons only."
    measurements:
      - {muscle: triceps_long,    mean_pct_mvc: 70.0, sd: 20.9}
      - {muscle: triceps_lateral, mean_pct_mvc: 55.0, sd: 14.1}

joint_rom_required:
  elbow_flexion_deg: 130
  shoulder_flexion_deg: 90
  source: "boehler_2011"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped; hardest at ~90° elbow flexion where moment arm is maximal"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: moderate
    shoulder: low
  common_injuries:
    - structure: distal_triceps_tendon
      mechanism: eccentric_overload_at_full_flexion
      risk_factors: [rapid_eccentric, dropping_bar, heavy_load, pre_existing_tendinopathy]
    - structure: lateral_epicondyle
      mechanism: valgus_stress
      risk_factors: [wide_grip, elbow_flaring]
  contraindications:
    - acute_triceps_tendinopathy
    - elbow_medial_collateral_ligament_injury

variations: []
progressions: []
alternatives: [lying_triceps_press, cable_lying_triceps_extension]

sources:
  - source_id: brettler_2023
    title: "Electromyographic analysis of triceps exercises at various intensities"
    author: "Brettler, S. et al."
    year: 2023
    doi: null
    credibility: rct
  - source_id: boehler_2011
    title: "An electromyographic analysis of 3 muscles surrounding the elbow joint during a maximally forceful isometric contraction, concentric isotonic contraction, and 6 common exercises"
    author: "Boehler, Breanna et al."
    year: 2011
    doi: null
    credibility: rct
---

# EZ-Bar Skullcrusher

The EZ-bar skullcrusher is performed supine on a bench with the EZ-bar lowered from arms-extended overhead toward the forehead. The fixed shoulder position at ~90° flexion places all three triceps heads in a moderately lengthened position while elbow extension provides the isolated triceps stimulus. The EZ-bar's semi-pronated grip reduces wrist stress compared to a straight bar.

## Execution

1. Lie on a flat bench; hold an EZ-bar with a close grip (inner knurling), arms extended perpendicular to the floor
2. Keep the upper arms vertical and stationary; lower the bar by bending the elbows only
3. Lower until the bar is just above the forehead — the "skull" reference point
4. Extend the elbows to return to the start; keep the upper arms stationary throughout
5. Do not lock out forcefully at the top; maintain muscular tension

## What the EMG Data Shows

Two studies with different normalization methods:

| Study | Measurement | Triceps Long | Triceps Lateral |
|-------|-------------|-------------|-----------------|
| Brettler 2023 | **True %MVIC**, 65% 1RM | 23.79% ± 9.19% | — |
| Boehler 2011 | Normalized (not %MVIC) | 70% ± 20.9% | 55% ± 14.1% |

The Brettler 2023 value (23.79% MVIC) appears low because: (1) the load was 65% 1RM, not maximal; (2) the MVIC reference is an isometric maximal contraction, which produces different neural drive than dynamic lifting. The Boehler 2011 values are relative to the triangle push-up baseline within that study.

## Shoulder Position Comparison

| Exercise | Shoulder | Long Head Length |
|----------|----------|-----------------|
| Skullcrusher | 90° flexion | Mid-range |
| Overhead extension | 180° flexion | Maximum |
| Pushdown | 0° (neutral) | Minimum |

The skullcrusher trains the long head in a mid-length position — more stimulus than a pushdown, less than an overhead extension. For comprehensive triceps development, pair with an overhead variation.

> For system-specific training applications, see each system's lens entry.
