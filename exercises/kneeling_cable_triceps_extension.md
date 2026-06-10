---
id: kneeling_cable_triceps_extension
name: Kneeling Cable Triceps Extension
status: complete
category: exercise
pattern: [isolation]
equipment: [cable]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 1
  mobility_prerequisite: 2

muscles:
  - id: triceps_long
    role: primary
  - id: triceps_lateral
    role: primary
  - id: triceps_medial
    role: secondary

# No peer-reviewed EMG data found for this specific variation.
# Mechanically combines overhead shoulder position (~160-180°) with kneeling to eliminate hip drive.
# Expected activation similar to cable_rope_overhead_triceps_extension (boehler_2011: long 81%, lateral 72%).
muscle_activation_studies: []

joint_rom_required:
  elbow_flexion_deg: 130
  shoulder_flexion_deg: 160
  source: "biomechanical inference"

strength_curve:
  type: descending
  sticking_point: top_third
  peak_force_position: top
  notes: "Descending cable profile; hardest when elbows are most flexed behind the head; cable provides constant tension throughout"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    shoulder: moderate
  common_injuries:
    - structure: triceps_tendon_long_head
      mechanism: stretch_overload
      risk_factors: [forcing_excess_elbow_flexion, heavy_load, limited_shoulder_mobility]
    - structure: posterior_shoulder_capsule
      mechanism: passive_stretch
      risk_factors: [limited_shoulder_flexion, forcing_overhead_position]
  contraindications:
    - acute_triceps_long_head_tendinopathy
    - severe_shoulder_flexion_restriction

variations: []
progressions: []
alternatives: [cable_rope_overhead_triceps_extension, ez_bar_skullcrusher]

sources: []
---

# Kneeling Cable Triceps Extension

The kneeling cable triceps extension is an overhead cable extension performed from a kneeling position, facing away from the pulley. Kneeling removes lower-body contribution and the hip-drive compensation that standing overhead extensions can involve. The arms extend forward overhead from a starting position with the elbows bent behind the head, providing maximum long head stretch.

## Execution

1. Kneel in front of a high cable pulley, facing away; grasp a rope or bar with both hands
2. Position the hands behind the head with elbows bent — the starting position has the triceps at maximum stretch
3. Extend the elbows forward to push the rope or bar forward/overhead until the arms are straight
4. Return under control, allowing the elbows to flex behind the head
5. Keep the upper arms close to the sides of the head; avoid excessive elbow flare

## Alternate Form: Bench-Supported Kneeling

An alternate version uses a bench placed sideways in front of a high pulley, with the knees on the bench and the upper arms resting on the bench's pad:
1. Rest the upper arms on the bench behind you; face the stack
2. Hold the bar with elbows bent pointing toward the stack
3. Press the bar forward by extending the elbows in a semicircular motion

This bench-supported version further eliminates shoulder movement and provides purely elbow extension.

## Why Kneeling

The kneeling position:
- Eliminates leg drive that can allow torso momentum in standing overhead extensions
- Removes the ability to compensate by leaning forward at the hips
- Creates a more demanding core stability requirement
- Maintains the overhead shoulder position that maximizes long head stretch

Activation is expected to be similar to the standing cable overhead extension, with better form maintenance through fatigue.

> For system-specific training applications, see each system's lens entry.
