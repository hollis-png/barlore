---
id: goblet_squat
name: Goblet Squat
status: complete
category: exercise
pattern: [squat]
equipment: [dumbbell, kettlebell]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
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
  - id: erector_spinae
    role: stabilizer

# No goblet-squat-specific peer-reviewed EMG study found.
# Collins_2021 studied kinematics but not EMG %MVIC.
# Gullett_2009 compared front vs back squat — goblet mechanics are analogous to front squat
# (anterior load, upright torso), so front squat EMG is the best available proxy.
# Expected: similar quad activation to front squat; lower absolute load limits total EMG output.
muscle_activation_studies: []

joint_rom_required:
  knee_flexion_deg: 120
  hip_flexion_deg: 115
  ankle_dorsiflexion_deg: 25
  source: "Collins et al. 2021; Gullett et al. 2009"

strength_curve:
  type: ascending
  sticking_point: bottom_third
  peak_force_position: lockout
  notes: "Ascending; anterior counterbalance shifts CoM forward, increasing knee flexion moment; sticking point at bottom similar to front squat; lower absolute loads than barbell squats"
  source: "Collins et al. 2021"

injury_risk:
  joint_stress:
    knee: low
    hip: low
    lumbar: low
  common_injuries:
    - structure: lumbar_spine
      mechanism: flexion_under_load
      risk_factors: [excessive_forward_lean, losing_neutral_spine_at_depth]
    - structure: knee
      mechanism: valgus_collapse
      risk_factors: [weak_hip_abductors, limited_ankle_dorsiflexion]
  contraindications:
    - acute_lumbar_disc_injury
    - acute_knee_injury

variations: []
progressions: [front_squat, back_squat]
alternatives: [front_squat, box_squat]

sources:
  - source_id: collins_2021
    title: "Effects of the goblet squat on muscle activity and kinematics"
    author: "Collins, K. S. et al."
    year: 2021
    doi: null
    credibility: rct
  - source_id: gullett_2009
    title: "A biomechanical comparison of back and front squats in healthy trained individuals"
    author: "Gullett, J. C. et al."
    year: 2009
    doi: "10.1519/JSC.0b013e31819c7928"
    credibility: rct
---

# Goblet Squat

The goblet squat is a squat performed holding a single dumbbell or kettlebell at chest height. The anterior load encourages an upright torso, makes depth more accessible, and is the most effective entry point for learning the squat pattern. Because the weight is held in front of the body, the counterbalance effect naturally corrects two of the most common beginner squat errors: forward lean and heel rise.

## Execution

1. Hold a dumbbell vertically or a kettlebell by the horns at chest height
2. Set stance about shoulder width, toes angled out 15–30°
3. Descend with an upright torso; let the elbows track inside the knees at the bottom
4. Sit into the deepest comfortable position without losing lumbar neutral
5. Drive up through the mid-foot to return to standing

## Why the Goblet Position Works

The weight held anteriorly shifts the center of mass forward, which:
- Counteracts the natural tendency to lean the torso forward
- Increases the demand on the knee extensors (similar to front squat mechanics)
- Reduces the hip moment arm vs the back squat
- Makes the required ankle dorsiflexion less daunting for beginners

These mechanical properties make the goblet squat ideal as a teaching tool and as a warm-up pattern before heavier loaded squats.

## Goblet vs Front Squat

The goblet squat and front squat share the same anterior-load principle. The key difference is load capacity: a kettlebell held at chest has a practical upper limit of ~60–80 kg, while a front-racked barbell can exceed bodyweight. Once technique is established in the goblet, the front squat or back squat provides the same pattern with greater overload potential.

## Common Faults

| Fault | Cause | Fix |
|-------|-------|-----|
| Heels rising | Limited ankle dorsiflexion | Elevate heels or improve ankle mobility |
| Weight drifting forward from chest | Fatigue or grip failure | Reduce load |
| Rounding at the bottom | Depth beyond current hip mobility | Reduce depth until mobility improves |

> For system-specific training applications, see each system's lens entry.
