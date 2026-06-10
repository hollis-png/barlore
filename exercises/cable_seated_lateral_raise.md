---
id: cable_seated_lateral_raise
name: Cable Seated Lateral Raise
status: complete
category: exercise
pattern: [isolation]
equipment: [cable]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: deltoid_lateral
    role: primary
  - id: deltoid_anterior
    role: secondary
  - id: deltoid_posterior
    role: secondary
  - id: supraspinatus
    role: secondary
  - id: trap_upper
    role: stabilizer

# No peer-reviewed quantitative EMG data found for this specific variation.
# Cable mechanics provide resistance at bottom of range (lengthened deltoid) unlike dumbbell.
# Kassiano 2024 demonstrated greater lateral deltoid hypertrophy vs dumbbell over 12 weeks.
muscle_activation_studies: []

joint_rom_required:
  shoulder_abduction_deg: 90
  source: "biomechanical inference from side_lateral_raise"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Low cable provides maximal tension at bottom (arm at side) where dumbbell has near-zero load — combined effect is a more bell-shaped resistance profile"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    shoulder: low
    elbow: low
  common_injuries:
    - structure: supraspinatus_tendon
      mechanism: subacromial_impingement
      risk_factors: [internal_rotation_above_90_deg, load_too_heavy]
  contraindications:
    - acute_shoulder_impingement

variations: []
progressions: []
alternatives: [side_lateral_raise, seated_side_lateral_raise]

sources: []
---

# Cable Seated Lateral Raise

The cable seated lateral raise loads the lateral deltoid in a fundamentally different resistance profile from the dumbbell lateral raise. By routing the cable from below hip height, resistance is highest when the arm is at the side (where dumbbells have zero tension) and maintained throughout the arc. Sitting eliminates leg momentum. The combination produces a more consistent deltoid stimulus across the full range of abduction — particularly at the lengthened position where evidence suggests mechanical hypertrophy signaling is elevated.

## Execution

1. Sit sideways to a low cable pulley, holding the rope or single-grip handle in the far hand (the hand farthest from the pulley)
2. Keep the elbow slightly bent and raise the arm laterally in an arc to shoulder height, the cable crossing in front of or behind the body depending on handle setup
3. The working shoulder should move directly away from the pulley attachment point
4. Lower under control, allowing the deltoid to stretch under tension at the bottom

## Cable vs Dumbbell: The Resistance Profile Difference

Free-weight dumbbells produce a gravity-dependent resistance curve that is zero at the sides and maximum at 90° abduction. The cable, attached below hip height, generates tension that peaks at the start of the movement (arm at side) and decreases slightly as the arm rises.

This makes the cable raise particularly valuable for loading the lateral deltoid at its **longest muscle length**. A 2024 study (Kassiano et al.) confirmed greater lateral deltoid hypertrophy with cable lateral raises compared to dumbbell raises over a 12-week training block, consistent with the stretch-mediated hypertrophy hypothesis.

## Setup Note

The cable position determines the resistance profile. A low pulley (below hip level) with the hand crossing in front of the torso creates the most favorable load at the bottom. A side-mounted pulley at the same height reduces the lengthened-position advantage.

> For system-specific training applications, see each system's lens entry.
