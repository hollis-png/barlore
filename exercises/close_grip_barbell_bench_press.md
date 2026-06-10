---
id: close_grip_barbell_bench_press
name: Close-Grip Barbell Bench Press
status: complete
category: exercise
pattern: [horizontal_push]
equipment: [barbell]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 1

muscles:
  - id: triceps_brachii
    role: primary
  - id: pec_major_clavicular
    role: secondary
  - id: pec_major_sternal
    role: secondary
  - id: deltoid_anterior
    role: secondary

# ebd_2026 literature compilation.
# Condition 1: triceps at 50% BAD grip — submaximal load comparison (narrow vs wide grip).
#   Absolute value (16%) reflects specific load condition, not maximal effort test.
# Condition 2: triceps lateral head at 95% 1RM — peak activation during high-intensity lockout.
# Sternal pectoralis: qualitative only (decreased vs wide grip).
muscle_activation_studies:
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      grip_width: "50% biacromial distance (BAD)"
      notes: "Relative comparison — specific load not reported; submaximal condition"
    measurements:
      - {muscle: triceps_brachii,   mean_pct_mvc: 16,   sd: null, notes: "vs 12% MVIC at 150% BAD standard grip — 33% greater at narrow grip"}
      - {muscle: pec_major_sternal, mean_pct_mvc: null, sd: null, notes: "Decreased vs wider grip variations"}
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      grip_width: "standard close grip (~95% BAD)"
      load_pct_1rm: 95
    measurements:
      - {muscle: triceps_lateral, mean_pct_mvc: 120, sd: null, notes: "Peak activation during high-intensity lockout; lateral head dominates at terminal elbow extension"}

joint_rom_required:
  elbow_flexion_deg: 90
  shoulder_extension_deg: null
  notes: >
    Elbows tucked close to the sides (~30° angle relative to torso) throughout.
    Bar contacts near the base of the sternum (lower than standard bench press).
    Grip width ~95% of biacromial distance — approximately 10–16 inches for most lifters.
  source: "ebd_2026"

strength_curve:
  type: ascending
  sticking_point: mid_range
  peak_force_position: lockout
  notes: >
    Sticking point occurs mid-range at the shoulder-to-triceps transition phase.
    The greater ROM vs wide-grip bench press extends time under tension. The mechanical
    advantage shifts heavily to the triceps in the final third — making this the premier
    barbell exercise for overcoming terminal lockout weakness.
  source: "ebd_2026"

injury_risk:
  joint_stress:
    wrist: moderate
    elbow: moderate
    shoulder: low
  common_injuries:
    - structure: wrist_extensor_tendons
      mechanism: ulnar_deviation_stress_from_narrow_grip
      risk_factors: [excessively_narrow_grip_under_shoulder_width, heavy_loads, elbow_flare]
    - structure: medial_elbow_common_flexor_tendon
      mechanism: valgus_stress_from_narrow_grip
      risk_factors: [heavy_loads, high_frequency, insufficient_recovery]
  contraindications:
    - acute_wrist_tendinopathy
    - medial_epicondylitis_acute
    - distal_biceps_tendon_pathology

variations: []
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

# Close-Grip Barbell Bench Press

The close-grip barbell bench press is a flat pressing variation with a narrow hand placement — typically 95% of biacromial distance (BAD), or roughly 10–16 inches of separation for most lifters. Narrowing the grip reduces the moment arm at the sternum while increasing the sagittal-plane moment arm at the elbow, redistributing load away from the sternal pec head and onto the triceps brachii, anterior deltoid, and clavicular pec head.

## Execution

1. Lie on a flat bench; grip the bar at approximately 95% of shoulder width, wrists neutral
2. Unrack the bar at full arm extension; position it over the mid-chest
3. Lower the bar under control, keeping the elbows tucked tight to the sides (~30° from torso)
4. Touch the lower sternum lightly; drive the bar upward through full elbow extension
5. Do not narrow the grip further than shoulder width — this increases wrist stress without further triceps benefit

## What the EMG Data Shows

The close-grip bench press data from ebd_2026 documents a relative comparison rather than absolute peak values at a standardized load.

**Grip width effect on triceps**: A 50% BAD grip (very narrow, approximately 5–8 inches) produces 16% MVIC in the triceps brachii vs 12% MVIC at a 150% BAD standard grip — a 33% relative increase. These values reflect a submaximal load condition; the study documents the directional difference, not maximal effort activation.

**High-intensity lockout**: At 95% of 1RM with a standard close grip, the lateral head of the triceps reaches 120% MVIC at terminal elbow extension. This confirms the close-grip press as a highly effective triceps overload tool at near-maximal loads — particularly for the lateral head which dominates lockout mechanics.

**Sternal pectoralis**: Activation decreases vs wider grip variations. This is expected biomechanically — the narrow grip reduces the horizontal adduction component of the movement, diminishing sternal head demand.

## Why Close-Grip for Triceps

The close-grip press succeeds at triceps isolation for a structural reason: the narrow grip forces the elbows into a more sagittal plane, extending the range of elbow motion and lengthening the time the triceps is under concentric load. Combined with the higher load capacity of the barbell format, this produces a mechanical overload the triceps cannot achieve in isolation exercises at equivalent absolute loads.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Standard bench press | Wide grip; greater pec demand | Overall pressing strength |
| Triceps pushdown | Isolation; constant cable tension | Pump work; high-rep triceps volume |
| Floor press (close grip) | Limited ROM; no shoulder extension | Lockout-specific triceps overload |

> For system-specific training applications, see each system's lens entry.
