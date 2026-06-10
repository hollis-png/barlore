---
id: front_cable_raise
name: Front Cable Raise
status: complete
category: exercise
pattern: [isolation]
equipment: [cable]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: deltoid_anterior
    role: primary
  - id: deltoid_lateral
    role: secondary
  - id: pec_major_clavicular
    role: secondary
  - id: trap_upper
    role: stabilizer

# No peer-reviewed quantitative EMG data found for the cable variation.
# Mechanically similar to front_dumbbell_raise but with altered resistance profile.
# Cable from low pulley provides tension at arm-at-side starting position where dumbbell has near-zero load.
muscle_activation_studies: []

joint_rom_required:
  shoulder_flexion_deg: 90
  source: "biomechanical inference from front_dumbbell_raise"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Low cable provides constant tension at bottom of range where free weight has near-zero load; combined effect is more bell-shaped than dumbbell variant"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    shoulder: low
    elbow: low
  common_injuries:
    - structure: biceps_tendon_long_head
      mechanism: anterior_shoulder_impingement
      risk_factors: [forcing_above_90_deg, anterior_shoulder_instability]
  contraindications:
    - acute_anterior_shoulder_impingement

variations: []
progressions: []
alternatives: [front_dumbbell_raise]

sources: []
---

# Front Cable Raise

The front cable raise is the cable variation of the front dumbbell raise, directing an anterior deltoid isolation stimulus with constant cable tension throughout the range of motion. The cable from a low pulley provides meaningful resistance at the starting position (arm at the hip) where a dumbbell has near-zero load, loading the anterior deltoid through its full elongated range.

## Execution

1. Attach a single grip handle to a low cable pulley; grasp with one hand
2. Stand facing away from the pulley, arm hanging at the side behind the hip
3. Raise the arm forward in the sagittal plane to shoulder height (90° flexion)
4. Keep a slight elbow bend throughout; avoid swinging the torso
5. Lower under control, allowing the cable to pull the arm back past neutral slightly for a full eccentric stretch

## Cable vs Dumbbell

A free-weight front raise starts with essentially zero resistance when the arm is at the side and peaks at 90° flexion. The cable maintains tension from the very beginning, loading the anterior deltoid in its lengthened position at the hip.

## Programming Note

The anterior deltoid receives high activation from pressing movements (bench press, overhead press, incline press). Most trainees do not need dedicated front raise volume. When included, limit to 1–2 sets as complementary volume rather than a primary movement. The cable version's advantage is the loaded eccentric stretch at the starting position, consistent with the stretch-mediated hypertrophy hypothesis.

> For system-specific training applications, see each system's lens entry.
