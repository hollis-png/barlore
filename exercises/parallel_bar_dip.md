---
id: parallel_bar_dip
name: Parallel Bar Dip
status: complete
category: exercise
pattern: [vertical_push]
equipment: [bodyweight]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 3
  mobility_prerequisite: 2

muscles:
  - id: triceps_brachii
    role: primary
  - id: pectoralis_major
    role: primary
  - id: deltoid_anterior
    role: secondary
  - id: serratus_anterior
    role: stabilizer

# ebd_2026 literature compilation.
# Condition 1: 75° elbow angle, concentric — triceps head-specific %MVIC.
# Condition 2: 95° elbow angle + 15° forward lean — pectoralis major %MVIC.
# Raw mV value (1.04 ± 0.27 mV) reported in source but NOT stored as mean_pct_mvc —
#   raw mV cannot be compared across subjects; excluded from structured data.
muscle_activation_studies:
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      elbow_angle_deg: 75
      phase: concentric
    measurements:
      - {muscle: triceps_long,    mean_pct_mvc: 55.70, sd: null}
      - {muscle: triceps_lateral, mean_pct_mvc: 41.76, sd: null}
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      elbow_angle_deg: 95
      torso_lean_deg: 15
      notes: "Forward lean increases pectoralis major recruitment"
    measurements:
      - {muscle: pectoralis_major, mean_pct_mvc: 95, sd: null}

joint_rom_required:
  shoulder_extension_deg: 78.20
  elbow_flexion_deg: 90
  notes: >
    Peak shoulder extension 78.20° ± 9.84° at the bottom of the dip. Elbows flex to
    at least 90° at the transition point. Scapulae should remain depressed and retracted
    throughout — avoid shrugging at the top.
  source: "ebd_2026"

strength_curve:
  type: descending
  sticking_point: lower_third
  peak_force_position: bottom
  notes: >
    Hardest at the bottom where the shoulder is in deep extension and the pec and
    triceps are in a maximally lengthened position. Mechanical leverage improves
    rapidly as the lifter presses out of the bottom, with the triceps dominating
    the final lockout.
  source: "ebd_2026"

injury_risk:
  joint_stress:
    shoulder: high
    elbow: low
    wrist: low
  common_injuries:
    - structure: anterior_shoulder_capsule
      mechanism: overstress_at_deep_shoulder_extension
      risk_factors: [excessive_depth_beyond_90_deg_elbow, anterior_shoulder_laxity, heavy_added_weight]
    - structure: pectoralis_major_tendon
      mechanism: eccentric_overload_at_maximum_stretch
      risk_factors: [excessive_depth, heavy_weight_belt, insufficient_warmup]
    - structure: acromioclavicular_joint
      mechanism: internal_rotation_under_load
      risk_factors: [wide_bar_spacing, elbows_flaring_outward]
  contraindications:
    - anterior_shoulder_instability
    - acute_pectoralis_major_tear
    - acromioclavicular_joint_pathology

variations: [ring_dips]
progressions: []
alternatives: []

sources:
  - source_id: ebd_2026
    title: "Exercise Biomechanics Data Extraction: Upper Push Accessories"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Parallel Bar Dip

The parallel bar dip is a closed-chain bodyweight pressing exercise on fixed parallel bars. The lifter supports their full body mass through the upper limbs, lowering by flexing the elbows and extending the shoulders before pressing back to the top. It is one of the most mechanically demanding upper-body pressing exercises per unit of body mass, generating high activation in both the triceps and pectoralis major simultaneously through a deep descending strength curve.

## Execution

1. Mount the bars with arms extended; keep scapulae depressed and retracted — not shrugged
2. Inhale, brace the core; lower by flexing the elbows and extending the shoulders simultaneously
3. Descend until the elbows reach 90° at minimum; lean the torso 15° forward to bias the pectorals
4. Reverse by driving through the palms; extend the elbows fully at the top
5. Control the descent to at least 2 seconds — the bottom position is the highest-risk point

## What the EMG Data Shows

The dip's primary advantage is the simultaneous high demand on both the triceps and pectoralis major:

**Triceps head activation at 75° elbow flexion (concentric)**: The long head leads at 55.70% MVIC, with the lateral head at 41.76% MVIC. The long head dominance occurs because at 90°+ shoulder extension, the long head's moment arm for elbow extension is optimal — it is a biarticular muscle crossing both the shoulder and elbow, contributing to both joint actions simultaneously.

**Pectoralis major at 95° elbow / 15° forward lean**: Activation reaches 95% MVIC. The forward lean is critical: upright torso shifts the load almost entirely to the triceps; a 15° forward lean brings the pec into primary engagement. Most trainees should lean slightly forward throughout the descent to share load between the triceps and pec.

The isometric phase (transitioning between eccentric and concentric) at a 75° elbow angle shows greater lateral head triceps activation than at 95°, indicating the lateral head preferentially activates at the more flexed (deeper) position — making the bottom of the dip the primary trigger for lateral head recruitment.

## Parallel Bar vs Ring Dip

The parallel bar dip allows a deeper shoulder extension (78.20°) than the ring dip (61.72°) — 27% greater extension due to the stable fixed bar. This produces a more demanding eccentric load at the bottom but also increases anterior shoulder risk. The ring dip imposes greater pectoralis major demand as an adductor throughout the movement; the bar dip produces a cleaner descending strength curve. See [ring_dips.md](ring_dips.md) for the comparative analysis.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Ring dips | Unstable; reduced shoulder extension; pec adduction demand | Advanced ring skill development; pec emphasis |
| Weighted dips | External load via belt or vest | Strength progression past bodyweight |
| Bench dips | Hands on bench behind; feet elevated | Lower strength requirement; triceps isolation |

> For system-specific training applications, see each system's lens entry.
