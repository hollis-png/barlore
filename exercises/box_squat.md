---
id: box_squat
name: Box Squat
status: complete
category: exercise
pattern: [squat]
equipment: [barbell, squat rack, box]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 2

muscles:
  - id: rectus_femoris
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: vastus_medialis
    role: primary
  - id: vastus_intermedius
    role: primary
  - id: gluteus_maximus
    role: primary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: erector_spinae
    role: stabilizer

# No box-squat-specific EMG peer-reviewed study with %MVIC found.
# McBride_2010 and Swinton_2012 analyzed kinematics and kinetics but not surface EMG %MVIC.
# Expected muscle activation profile: similar to back squat but with greater posterior chain
# contribution due to wider stance and intentional sit-back cue (Westside protocol).
muscle_activation_studies: []

joint_rom_required:
  knee_flexion_deg: 95
  hip_flexion_deg: 115
  ankle_dorsiflexion_deg: 15
  source: "McBride et al. 2010; Swinton et al. 2012"

strength_curve:
  type: ascending
  sticking_point: dead_stop_bottom
  peak_force_position: lockout
  notes: "Dead stop from box eliminates stretch-shortening cycle; the initial concentric drive from a paused position is the primary sticking point; this dead-stop demand is the training rationale for Westside speed work"
  source: "Swinton et al. 2012"

injury_risk:
  joint_stress:
    knee: low
    hip: low
    lumbar: moderate
  common_injuries:
    - structure: lumbar_spine
      mechanism: compressive_load_during_pause
      risk_factors: [fully_relaxing_on_box, crashing_onto_box, heavy_load]
    - structure: hip_labrum
      mechanism: impingement_at_depth
      risk_factors: [box_too_low_for_hip_anatomy, excessive_forward_lean]
  contraindications:
    - acute_lumbar_disc_injury
    - acute_hip_labral_tear

variations: [back_squat]
progressions: []
alternatives: [goblet_squat, back_squat]

sources:
  - source_id: mcbride_2010
    title: "Comparison of kinetic variables and muscle activity during a squat vs. a box squat"
    author: "McBride, J. M. et al."
    year: 2010
    doi: "10.1519/JSC.0b013e3181c6a935"
    credibility: rct
  - source_id: swinton_2012
    title: "Kinematic and kinetic analysis of the barbell squat performed with box and safety squat bar"
    author: "Swinton, P. A. et al."
    year: 2012
    doi: "10.1519/JSC.0b013e318258e783"
    credibility: rct
  - source_id: simmons_westside
    title: "Westside Barbell Book of Methods"
    author: "Louie Simmons"
    year: null
    doi: null
    credibility: practitioner
---

# Box Squat

The box squat is a squat performed to a box set at a fixed height, with a brief controlled pause before the concentric drive. It serves two distinct purposes: a teaching tool for depth calibration, and a strength tool for eliminating the stretch-shortening cycle reflex and developing pure concentric power from the bottom position. It is a cornerstone exercise in the Westside Conjugate system for this reason.

## Execution

1. Set the box so the target depth is reached when sitting on it (typically parallel or slightly below)
2. Set up with the bar on the upper back as in a back squat
3. Sit back and down onto the box with the shins near-vertical; do not allow the knees to travel excessively forward
4. Pause briefly on the box without fully relaxing — maintain tension in the hips and lower back
5. Drive up explosively through the mid-foot

## Why the Dead Stop Matters

In a standard squat, the stretch-shortening cycle (SSC) stores elastic energy at the bottom and contributes to the upward drive. The box squat's pause interrupts the SSC, requiring the lifter to initiate the concentric phase from zero stored elastic energy. This is specifically why Westside uses box squats for dynamic effort work: the explosive drive from a dead stop trains rate of force development without the SSC crutch.

## Box Height Selection

| Box height | Depth achieved | Primary use |
|-----------|---------------|-------------|
| Above parallel | Partial squat | Early rehabilitation, heavy load exposure |
| Parallel | Hip crease at knee | Depth calibration and competition prep |
| Below parallel | Full squat | Advanced bottom-position strength |

## Critical Technique Points

- **Do not crash**: The descent must be controlled; crashing loads the lumbar spine dangerously
- **Do not fully relax**: Maintain hip tension; releasing completely compresses the spine and defeats the training purpose
- **Drive straight up**: Not forward — the bar path should be vertical from the box

> For system-specific training applications, see each system's lens entry.
