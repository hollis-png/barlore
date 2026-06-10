---
id: pallof_press
name: Pallof Press
status: complete
category: exercise
pattern: [isolation]
equipment: [cable]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: external_oblique
    role: primary
  - id: internal_oblique
    role: primary
  - id: transverse_abdominis
    role: primary
  - id: rectus_abdominis
    role: secondary
  - id: erector_spinae
    role: stabilizer

# No peer-reviewed EMG study with %MVIC exists for the Pallof press.
# The exercise is classified as anti-rotation by bilateral EMG characteristics
# in clinical practice, but published %MVIC quantification is absent.
muscle_activation_studies: []

joint_rom_required:
  shoulder_flexion_deg: 90
  elbow_extension_deg: 0
  notes: "Cable is pressed to full elbow extension at shoulder height. No extreme ROM required; limiting factor is rotational stiffness, not range of motion."
  source: "Pallof clinical description"

strength_curve:
  type: isometric
  sticking_point: full_arm_extension
  peak_force_position: full_arm_extension
  notes: "Peak rotational torque demand occurs at full arm extension, when the cable's moment arm about the lumbar spine is greatest. Returning the handle to the chest reduces the moment arm and unloads the core. The hardest point of each rep is the held extension."
  source: "Biomechanical inference from moment arm principles"

injury_risk:
  joint_stress:
    lumbar: low
    shoulder: low
  common_injuries:
    - structure: lumbar_spine
      mechanism: rotational_overload
      risk_factors: [excessive_load_causing_trunk_rotation, fast_uncontrolled_extension]
    - structure: glenohumeral_joint
      mechanism: impingement
      risk_factors: [shoulder_above_90_degrees_flexion, internal_rotation_during_press]
  contraindications:
    - acute_lumbar_disc_herniation
    - acute_rotator_cuff_tear

variations: []
progressions: []
alternatives: [plank, dead_bug]

sources:
  - source_id: pallof_nsca_2014
    title: "Anti-Rotation Exercises: A Guide to the Pallof Press"
    author: "Gentilcore, T."
    year: 2008
    doi: null
    credibility: practitioner
---

# Pallof Press

The Pallof press is an anti-rotation core exercise performed standing (or kneeling) perpendicular to a cable pulley. The cable creates a rotational moment that the core must resist throughout the movement. Unlike most core exercises, which train flexion or extension, the Pallof press specifically trains rotational stiffness — the ability to resist twisting forces through the lumbar spine.

## Execution

1. Set the cable to shoulder height; attach a single D-handle
2. Stand perpendicular to the cable, feet hip-width apart, soft knee bend; the cable should be at the side of the body
3. Grip the handle with both hands and step away from the stack so the cable is taut; hold the handle at chest level — this is the starting position
4. Brace the entire core as if bracing for a punch; breathe in
5. Press the handle directly forward until the elbows are fully extended, holding the press for 1–3 seconds; resist any rotation of the torso toward the cable
6. Return the handle to the chest under control
7. Complete all reps, then face the opposite direction and repeat

## The Anti-Rotation Mechanism

The cable pulls the hands toward the pulley, creating a moment that attempts to rotate the spine. The obliques (primary rotators and anti-rotators of the trunk) and transverse abdominis (the deep stabilizing cylinder) must co-contract to prevent that rotation. The moment arm — and therefore the core demand — increases as the arms extend further from the midline. This is why the fully extended position is the sticking point.

This is fundamentally different from a crunch or plank: there is no sagittal-plane movement, no flexion/extension demand. The Pallof press trains the rotational plane in isolation.

## Load and Position Selection

| Variable | Easier | Harder |
|----------|--------|--------|
| Stance | Wide stance | Narrow stance; single-leg |
| Position | Standing | Half-kneeling; tall kneeling |
| Arm extension | Partial press | Full arm extension with hold |
| Load | Light cable | Heavy cable |

The standing version with a wide base is the starting point. Progressing to half-kneeling removes the lower-body base of support and increases the rotational challenge substantially.

## Programming Notes

The Pallof press is best used as accessory core work after primary strength lifts or as a warm-up pattern to activate the anti-rotation system before compound movements. Sets of 8–12 reps with a 2-second hold at extension per rep, each side, provide sufficient stimulus without generating fatigue that interferes with primary work.

> For system-specific training applications, see each system's lens entry.
