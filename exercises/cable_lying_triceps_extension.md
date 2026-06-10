---
id: cable_lying_triceps_extension
name: Cable Lying Triceps Extension
status: complete
category: exercise
pattern: [isolation]
equipment: [cable, bench]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: triceps_long
    role: primary
  - id: triceps_lateral
    role: primary
  - id: triceps_medial
    role: secondary

# No peer-reviewed EMG data found for the cable lying variation.
# Mechanically similar to ez_bar_skullcrusher but cable provides constant tension at the stretched position.
muscle_activation_studies: []

joint_rom_required:
  elbow_flexion_deg: 130
  shoulder_flexion_deg: 90
  source: "biomechanical inference from ez_bar_skullcrusher"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Cable provides constant tension throughout including at the most stretched bottom position where the free-weight skullcrusher has near-zero load"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    shoulder: low
  common_injuries:
    - structure: distal_triceps_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, excessive_weight]
  contraindications:
    - acute_triceps_tendinopathy

variations: []
progressions: []
alternatives: [ez_bar_skullcrusher, lying_triceps_press]

sources: []
---

# Cable Lying Triceps Extension

The cable lying triceps extension replicates the skullcrusher pattern with a low-pulley cable instead of a free-weight bar. Lying on a bench with the head toward the low pulley, the cable runs over the head and the elbows flex and extend against the cable tension. Unlike the barbell skullcrusher — where the load approaches zero at the most extended arm position overhead — the cable provides constant tension throughout the entire range, including at the fully stretched bottom position.

## Execution

1. Place a flat bench directly in front of a low cable pulley; lie down with the head toward the stack
2. Grasp the straight bar attachment, arms extended overhead with elbows pointing at the ceiling
3. Lower by bending the elbows until the bar passes behind the head or reaches the forehead
4. Extend the elbows to return to the start; keep the upper arms stationary

## Cable vs Free-Weight Skullcrusher

At the starting position (arms extended), the barbell has maximum gravitational resistance. As the bar descends behind the head, the gravitational moment decreases significantly. Near full elbow flexion, the load approaches zero.

The cable reverses this: constant tension through the full range means the triceps is loaded when the elbows are fully flexed (maximum stretch) — a position that free-weight skullcrushers largely skip. This constant-tension characteristic is the mechanical argument for the cable version, analogous to why cable lateral raises are preferred over dumbbell raises for shoulder training.

> For system-specific training applications, see each system's lens entry.
