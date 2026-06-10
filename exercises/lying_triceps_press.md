---
id: lying_triceps_press
name: Lying Triceps Press
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

# boehler_2011 (normalized to triangle push-up, NOT true %MVIC):
#   triceps_long 70%, triceps_lateral 55%.
# brettler_2023 (TRUE %MVIC at 65% 1RM): ~23.79% (identical protocol to skullcrusher).
# lying_triceps_press and ez_bar_skullcrusher are mechanically nearly identical.
# The distinction: skullcrusher lowers to forehead; lying press lowers behind head (slightly more shoulder flexion).
muscle_activation_studies:
  - source_id: boehler_2011
    doi: null
    n: null
    population: "healthy adults"
    condition:
      implement: ez_bar
      phase: full_rep
      notes: "Normalized to triangle push-up = 100%, NOT true %MVIC. Lying supine, arms overhead."
    measurements:
      - {muscle: triceps_long,    mean_pct_mvc: 70.0, sd: null}
      - {muscle: triceps_lateral, mean_pct_mvc: 55.0, sd: null}
  - source_id: brettler_2023
    doi: null
    n: 8
    population: "trained adults, 65% 1RM"
    condition:
      load_pct_1rm: 65
      implement: ez_bar
      phase: full_rep
      notes: "TRUE %MVIC — lying supine variation"
    measurements:
      - {muscle: triceps_long, mean_pct_mvc: 23.79, sd: 9.19}

joint_rom_required:
  elbow_flexion_deg: 130
  shoulder_flexion_deg: 90
  source: "boehler_2011"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped; essentially identical to skullcrusher in mechanics; lowering behind head adds slight extra long head stretch"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: moderate
    shoulder: low
  common_injuries:
    - structure: distal_triceps_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, dropping_bar, heavy_load, pre_existing_tendinopathy]
  contraindications:
    - acute_triceps_tendinopathy

variations: []
progressions: []
alternatives: [ez_bar_skullcrusher, cable_lying_triceps_extension]

sources:
  - source_id: boehler_2011
    title: "An electromyographic analysis of 3 muscles surrounding the elbow joint during a maximally forceful isometric contraction, concentric isotonic contraction, and 6 common exercises"
    author: "Boehler, Breanna et al."
    year: 2011
    doi: null
    credibility: rct
  - source_id: brettler_2023
    title: "Electromyographic analysis of triceps exercises at various intensities"
    author: "Brettler, S. et al."
    year: 2023
    doi: null
    credibility: rct
---

# Lying Triceps Press

The lying triceps press is performed supine on a flat bench, lowering a bar from fully extended arms overhead to behind the head by bending only the elbows. It is mechanically near-identical to the EZ-bar skullcrusher — the primary distinction is the finish position: the skullcrusher targets the bar to the forehead while the lying press lowers behind the head, slightly increasing shoulder flexion and elongating the triceps long head further at the bottom.

## Execution

1. Lie on a flat bench; hold an EZ-bar at full arm extension overhead, shoulder at ~90° flexion
2. Lower the bar by bending only the elbows, maintaining the upper arms' position
3. Lower to approximately behind the top of the head (not to the forehead)
4. The upper arms may drift slightly back toward the face during lowering; control this with the shoulders
5. Extend the elbows to return to the start

## Relationship to the Skullcrusher

| Feature | Skullcrusher | Lying Triceps Press |
|---------|-------------|---------------------|
| Bar lowered to | Forehead | Behind head |
| Shoulder flexion | ~90° | ~100°+ |
| Long head stretch | Mid-range | Slightly more |
| Elbow stress | Similar | Similar |

For most trainees the difference is minor; choose based on comfort and feel.

## EMG Data Context

The Boehler 2011 data (long 70%, lateral 55%, normalized) is virtually identical to the skullcrusher data from the same study — as expected given the near-identical mechanics. The Brettler 2023 true %MVIC value (23.79%) reflects 65% 1RM dynamic loading.

> For system-specific training applications, see each system's lens entry.
