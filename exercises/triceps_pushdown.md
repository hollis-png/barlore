---
id: triceps_pushdown
name: Triceps Pushdown
status: complete
category: exercise
pattern: [isolation]
equipment: [cable]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: triceps_lateral
    role: primary
  - id: triceps_long
    role: primary
  - id: triceps_medial
    role: secondary

# boehler_2011: Values are normalized to triangle push-up = 100%, NOT true %MVIC.
# Rope attachment: triceps_long 81% ± 32.3%, triceps_lateral 67% ± 15.7%.
# Straight-bar: triceps_long 75% ± 29.3%, triceps_lateral 59% ± 14.3%.
# Rope produces higher activation for both heads vs straight-bar.
muscle_activation_studies:
  - source_id: boehler_2011
    doi: null
    n: null
    population: "healthy adults, rope attachment"
    condition:
      implement: cable_rope
      phase: full_rep
      notes: "Normalized to triangle push-up = 100%, NOT true %MVIC. Values are relative comparisons only."
    measurements:
      - {muscle: triceps_long,    mean_pct_mvc: 81.0, sd: 32.3}
      - {muscle: triceps_lateral, mean_pct_mvc: 67.0, sd: 15.7}
  - source_id: boehler_2011
    doi: null
    n: null
    population: "healthy adults, straight-bar attachment"
    condition:
      implement: cable_bar
      phase: full_rep
      notes: "Normalized to triangle push-up = 100%, NOT true %MVIC. Values are relative comparisons only."
    measurements:
      - {muscle: triceps_long,    mean_pct_mvc: 75.0, sd: 29.3}
      - {muscle: triceps_lateral, mean_pct_mvc: 59.0, sd: 14.3}

joint_rom_required:
  elbow_flexion_deg: 90
  shoulder_flexion_deg: 0
  source: "boehler_2011"

strength_curve:
  type: descending
  sticking_point: top_third
  peak_force_position: top
  notes: "Hardest at the start (elbows most flexed); decreases as elbows extend — shortened-position biased relative to overhead extensions"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    wrist: low
  common_injuries:
    - structure: lateral_epicondyle
      mechanism: repetitive_valgus_stress
      risk_factors: [grip_too_wide, wrist_deviation_at_bottom, heavy_load]
    - structure: triceps_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, excessive_weight]
  contraindications:
    - acute_lateral_epicondylitis

variations: []
progressions: []
alternatives: [cable_one_arm_tricep_extension, ez_bar_skullcrusher]

sources:
  - source_id: boehler_2011
    title: "An electromyographic analysis of 3 muscles surrounding the elbow joint during a maximally forceful isometric contraction, concentric isotonic contraction, and 6 common exercises"
    author: "Boehler, Breanna et al."
    year: 2011
    doi: null
    credibility: rct
---

# Triceps Pushdown

The triceps pushdown is the most accessible cable isolation exercise for all three triceps heads. With the upper arm held stationary at the side and the forearm pushing downward against the cable, the exercise provides a controlled elbow extension stimulus without the shoulder mobility or stability demands of overhead variations. The rope attachment produces higher activation than the straight-bar for both the long and lateral heads.

## Execution

1. Attach a rope (or straight bar) to a high cable pulley; grip with elbows close to the sides
2. Keep the upper arms stationary throughout — do not allow them to drive forward or backward
3. Push the attachment downward by extending the elbows until the arms are fully extended
4. At the bottom of the rope version, spread the hands slightly to maximize triceps contraction
5. Return under control, allowing the forearms to rise to approximately 90° at the start

## What the EMG Data Shows

Boehler 2011 data is normalized to triangle push-up (not true %MVIC). The values are relative comparisons within that study:

| Attachment | Triceps Long | Triceps Lateral |
|------------|-------------|-----------------|
| Rope | 81 ± 32.3 | 67 ± 15.7 |
| Straight bar | 75 ± 29.3 | 59 ± 14.3 |

The rope consistently produces ~6–8 points higher activation for both heads. The spreading action at the bottom of the rope rep adds a final contraction impulse not available with the fixed bar grip.

## Rope vs Bar: Why the Difference

The rope allows the wrists and forearms to rotate slightly during the push, which aligns with the triceps' optimal pull direction. The bar locks the wrists into a fixed position that may not suit all anatomical configurations. For most trainees, the rope is the recommended default.

## Shoulder Position and Long Head

The shoulder is neutral (0° flexion/extension) during pushdowns. This puts the triceps long head in a mid-range position — shortened relative to overhead extensions. Trainees seeking maximum long head stimulus should pair pushdowns with an overhead extension variation.

> For system-specific training applications, see each system's lens entry.
