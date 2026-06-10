---
id: overhead_squat
name: Overhead Squat
status: complete
category: exercise
pattern: [squat]
equipment: [barbell]

difficulty:
  technical_complexity: 4
  strength_prerequisite: 2
  mobility_prerequisite: 5

muscles:
  - id: vastus_lateralis
    role: primary
  - id: rectus_femoris
    role: primary
  - id: vastus_medialis
    role: primary
  - id: gluteus_maximus
    role: primary
  - id: trap_middle
    role: primary
  - id: deltoid_anterior
    role: primary
  - id: serratus_anterior
    role: primary
  - id: erector_spinae
    role: secondary
  - id: multifidus
    role: secondary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: external_oblique
    role: secondary
  - id: rectus_abdominis
    role: secondary
  - id: triceps_brachii
    role: stabilizer
  - id: gastrocnemius
    role: stabilizer
  - id: soleus
    role: stabilizer

# Bautista 2020 (doi: 10.70252/BTUH3630): n=7, recreationally trained.
# Measurements at 95% of 3RM, concentric phase. Values are %MVIC.
# Same study also recorded raw µV for trap_middle (1399±736 µV at 95% 3RM),
# deltoid_anterior (1941±1897 µV), and serratus_anterior (1235±873 µV) —
# these cannot be directly compared to %MVIC values; documented in prose below.
#
# Aspe 2014 (doi: 10.1519/JSC.0000000000000462): n=14, rugby union athletes.
# Values are %MVIC, full repetition.
muscle_activation_studies:
  - source_id: bautista_2020
    doi: "10.70252/BTUH3630"
    n: 7
    population: "recreationally_trained"
    condition:
      load_pct_1rm: 95
      phase: concentric
      notes: "95% of 3RM"
    measurements:
      - {muscle: erector_spinae,   mean_pct_mvc: 63.40, sd: 23.30}
      - {muscle: rectus_abdominis, mean_pct_mvc: 14.40, sd: 6.40}
      - {muscle: external_oblique, mean_pct_mvc: 16.90, sd: 3.10}
  - source_id: aspe_2014
    doi: "10.1519/JSC.0000000000000462"
    n: 14
    population: "rugby_union_athletes"
    condition:
      load_pct_1rm: 90
      phase: full_rep
      notes: "90% of 3RM"
    measurements:
      - {muscle: gluteus_maximus,  mean_pct_mvc: 60.90, sd: null}
      - {muscle: biceps_femoris,   mean_pct_mvc: 54.00, sd: null}

joint_rom_required:
  hip_flexion_deg: 120
  ankle_dorsiflexion_deg: 20
  shoulder_flexion_deg: 180
  shoulder_external_rotation_deg: 90
  shoulder_internal_rotation_deg: 70
  notes: >
    Shoulder flexibility correlates with trunk angle at the bottom (r = −0.67, p = 0.003):
    restricted shoulders force a compensatory forward trunk lean that shifts the bar forward.
    All ROM requirements apply throughout the entire descent and ascent.
  source: "nasm_2020 / bautista_2020 / setpt_2020"

strength_curve:
  type: ascending
  sticking_point: just_above_parallel
  peak_force_position: lockout
  notes: >
    Ascending curve: hardest at the bottom, progressively easier toward lockout.
    Sticking point at ~90° knee flexion where passive-elastic contributions drop
    before active-concentric force compensates.
    Unique kinetic feature: increasing load from 0 to 40% BW significantly increases hip
    extensor torque but does not change knee extensor torque — progressive loading targets
    hip extensors and pelvic stabilisers, not the quadriceps.
    ES and core at 95% 3RM (63% and 14–17% MVIC) is equal to or less than the front squat
    at equivalent relative load — the OHS is not a superior core-building exercise.
  source: "bautista_2020 / johk_2025"

injury_risk:
  joint_stress:
    shoulder: high
    lower_back: moderate
    knee: low
  common_injuries:
    - structure: rotator_cuff
      mechanism: overhead_compression_with_restricted_mobility
      risk_factors: [insufficient_shoulder_flexion, restricted_thoracic_extension]
    - structure: wrist
      mechanism: forced_extension_under_load
      risk_factors: [poor_overhead_position, wrist_deviation]
  contraindications:
    - acute_shoulder_injury
    - lumbar_herniation

variations: [front_squat, back_squat]
progressions: []
alternatives: []

sources:
  - source_id: bautista_2020
    title: "A Comparison of Muscle Activation Among the Front Squat, Overhead Squat, Back Extension and Plank"
    author: "Bautista IJ et al."
    year: 2020
    doi: "10.70252/BTUH3630"
    credibility: rct
  - source_id: aspe_2014
    title: "Electromyographic and Kinetic Comparison of the Back Squat and Overhead Squat"
    author: "Aspe RR, Swinton PA"
    year: 2014
    doi: "10.1519/JSC.0000000000000462"
    credibility: rct
  - source_id: nasm_2020
    title: "NASM Optimum Performance Training"
    author: "National Academy of Sports Medicine"
    year: 2020
    credibility: expert_consensus
  - source_id: setpt_2020
    title: "Weightlifting Series Part I: Improving Overhead Mobility"
    author: "Set Physical Therapy"
    year: 2020
    credibility: practitioner
  - source_id: johk_2025
    title: "Impact of Load Variation on Lower Limb Joint Torque during Overhead Squats"
    author: "PMC12612806"
    year: 2025
    doi: "10.3390/jfmk10020116"
    credibility: rct
---

# Overhead Squat

The overhead squat (OHS) is a squat-pattern movement in which the barbell is held locked out overhead throughout the full range of motion. It is the catch position of the snatch and the most mobility-demanding movement in strength training, requiring simultaneous 180° shoulder flexion, full thoracic extension, and deep hip and ankle mobility.

## Execution

1. **Setup:** Take a wide snatch-width grip. Press or snatch the bar overhead, elbows fully locked. Feet slightly wider than shoulder-width, toes turned out. Retract and depress the scapulae; actively press the bar into the ceiling throughout.
2. **Descent:** Flex hips and knees simultaneously; track knees over toes. Maintain the bar over the midfoot by actively pressing up through the arms. Hip crease below the knee at the bottom.
3. **Bottom position:** 120° hip flexion, ≥90° knee flexion, 20° ankle dorsiflexion. Bar directly over the midfoot.
4. **Ascent:** Drive hips and knees together; maintain overhead bar position. Stand to full extension.

## What the EMG Data Shows

The OHS challenges a common assumption: the overhead bar position does NOT produce superior trunk or core activation compared to the front squat at equivalent relative load. Bautista 2020 found no significant difference in ES activation between OHS and front squat (63.4% vs 61.7% MVIC at 95% 3RM). Rectus abdominis (14.4% MVIC) and external oblique (16.9% MVIC) activations are moderate.

The primary neuromuscular demand is concentrated on the scapular stabilisers and shoulder girdle. Middle trapezius recorded 1399±736 µV raw EMG at 95% 3RM — significantly greater than during the front squat, confirming the OHS as the primary scapulothoracic stabilisation exercise in Olympic lifting. Serratus anterior (1235±873 µV) and anterior deltoid (1941±1897 µV) also show high raw activation, reflecting the demands of maintaining a stable overhead position against gravity and bar oscillation.

Lower-body prime movers (GM ≈61% MVIC, BF ≈54% MVIC) show activation comparable to other squat variations at equated relative loads, but because the absolute load is constrained by shoulder mobility, the total lower-body stimulus is less than a front or back squat.

## Unique Kinetic Feature: Hip-Dominant Load Response

Adding load to the OHS (from 0 to 40% BW) significantly increases hip extensor torque but does not change knee extensor torque. The OHS becomes progressively hip-dominant as load increases — unusual for a movement that looks quad-dominated. The practical implication: the OHS is not an efficient quadriceps builder; it is a hip stability and overhead coordination exercise.

## Classification: Mobility Tool, Not Core Builder

The OHS should be classified primarily as:
- A **dynamic mobility assessment and training tool** for overhead position quality
- A **scapulothoracic stabilisation exercise** (trap_middle, serratus_anterior, deltoid_anterior)
- A **snatch catch position conditioner**

It is not a primary tool for quadriceps hypertrophy, trunk strength, or general strength development — the absolute loads required to achieve a meaningful muscle-building stimulus cannot be reached when shoulder mobility is the limiting factor.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Front squat | Front-rack position; no overhead demand | Higher absolute load; similar lower body stimulus |
| Snatch balance | Dynamic drive under the bar | Snatch catch-position speed and confidence |

> For system-specific training applications, see each system's lens entry.
