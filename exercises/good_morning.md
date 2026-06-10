---
id: good_morning
name: Good Morning
status: complete
category: exercise
pattern: [hinge]
equipment: [barbell]

difficulty:
  technical_complexity: 3
  strength_prerequisite: 2
  mobility_prerequisite: 3

muscles:
  - id: erector_spinae
    role: primary
  - id: semitendinosus
    role: primary
  - id: biceps_femoris
    role: secondary
  - id: gluteus_maximus
    role: secondary
  - id: multifidus
    role: secondary
  - id: rectus_abdominis
    role: secondary

# Vigotsky 2015 (doi: 10.7717/peerj.708): n=15, trained males.
# Five load conditions 50–90% 1RM; concentric phase mean %MVIC.
# SD not published (95% CI provided in source). Do NOT average across loads.
muscle_activation_studies:
  - source_id: vigotsky_2015
    doi: "10.7717/peerj.708"
    n: 15
    population: "trained males"
    condition:
      load_pct_1rm: 50
      phase: concentric
      knee_flexion_deg: 17.1
    measurements:
      - {muscle: semitendinosus, mean_pct_mvc: 26.2, sd: null}
      - {muscle: biceps_femoris, mean_pct_mvc: 19.5, sd: null}
      - {muscle: erector_spinae, mean_pct_mvc: 50.8, sd: null}
  - source_id: vigotsky_2015
    doi: "10.7717/peerj.708"
    n: 15
    population: "trained males"
    condition:
      load_pct_1rm: 60
      phase: concentric
      knee_flexion_deg: 19.1
    measurements:
      - {muscle: semitendinosus, mean_pct_mvc: 28.4, sd: null}
      - {muscle: biceps_femoris, mean_pct_mvc: 19.3, sd: null}
      - {muscle: erector_spinae, mean_pct_mvc: 54.9, sd: null}
  - source_id: vigotsky_2015
    doi: "10.7717/peerj.708"
    n: 15
    population: "trained males"
    condition:
      load_pct_1rm: 70
      phase: concentric
      knee_flexion_deg: 20.1
    measurements:
      - {muscle: semitendinosus, mean_pct_mvc: 34.4, sd: null}
      - {muscle: biceps_femoris, mean_pct_mvc: 24.2, sd: null}
      - {muscle: erector_spinae, mean_pct_mvc: 61.5, sd: null}
  - source_id: vigotsky_2015
    doi: "10.7717/peerj.708"
    n: 15
    population: "trained males"
    condition:
      load_pct_1rm: 80
      phase: concentric
      knee_flexion_deg: 23.1
    measurements:
      - {muscle: semitendinosus, mean_pct_mvc: 37.3, sd: null}
      - {muscle: biceps_femoris, mean_pct_mvc: 26.4, sd: null}
      - {muscle: erector_spinae, mean_pct_mvc: 73.1, sd: null}
  - source_id: vigotsky_2015
    doi: "10.7717/peerj.708"
    n: 15
    population: "trained males"
    condition:
      load_pct_1rm: 90
      phase: concentric
      knee_flexion_deg: 24.8
    measurements:
      - {muscle: semitendinosus, mean_pct_mvc: 39.9, sd: null}
      - {muscle: biceps_femoris, mean_pct_mvc: 30.4, sd: null}
      - {muscle: erector_spinae, mean_pct_mvc: 70.9, sd: null}

joint_rom_required:
  hip_flexion_deg: 75.8
  knee_flexion_deg: 23.1
  ankle_dorsiflexion_deg: null
  notes: >
    ROM at 80% 1RM (peak mean condition). Knee flexion is not a fixed requirement —
    it increases self-regulatorily from 17.1° at 50% to 24.8° at 90% 1RM as a
    neural protective strategy to limit hamstring strain at terminal length.
  source: "vigotsky_2015"

strength_curve:
  type: descending
  sticking_point: null
  peak_force_position: bottom
  notes: >
    Extremely long moment arm (bar on upper traps) generates peak lumbar and hip extensor
    torque at maximum trunk lean. Erector spinae peak activation reaches 158% MVIC at
    90% 1RM — among the highest lumbar demands of any barbell exercise.
    Medial hamstrings (semitendinosus) consistently exceed lateral hamstrings (biceps
    femoris) at all loads, consistent with hip-extension-dominant exercise recruitment.
  source: "vigotsky_2015"

injury_risk:
  joint_stress:
    lower_back: high
    knee: low
    hamstring: moderate
  common_injuries:
    - structure: lumbar_disc
      mechanism: flexion_under_load
      risk_factors: [heavy_loads, lumbar_rounding, fatigue]
    - structure: proximal_hamstring
      mechanism: eccentric_overload
      risk_factors: [insufficient_hamstring_flexibility, excessive_depth]
  contraindications:
    - acute_lumbar_herniation
    - proximal_hamstring_tendinopathy
    - lumbar_instability

variations: []
progressions: []
alternatives: [romanian_deadlift]

sources:
  - source_id: vigotsky_2015
    title: "Effects of load on good morning kinematics and EMG activity"
    author: "Vigotsky AD, Harper EN, Ryan DR, Contreras B"
    year: 2015
    doi: "10.7717/peerj.708"
    credibility: rct
---

# Good Morning

The good morning is a barbell hinge-pattern exercise in which the bar rests on the upper traps or rear delts — the same position as a low-bar back squat. As the trunk hinges forward, this placement creates an exceptionally long external moment arm relative to the hip joint, imposing massive static demand on the lumbar erector spinae and deep spinal extensors.

## Execution

1. Rack the bar across the rear delts at low-bar squat height
2. Step back; set feet shoulder-width with a slight knee bend
3. Inhale and brace hard; hinge forward at the hips until the trunk approaches parallel to the floor
4. Maintain a neutral lumbar spine; allow the knees to bend naturally as load increases
5. Drive the hips forward, extending the spine to return to upright; exhale at lockout

## What the EMG Data Shows

The good morning is primarily a lumbar spine exercise — not a hamstring exercise. At every load from 50% to 90% 1RM (Vigotsky 2015), the erector spinae consistently dominates:

| Load | Erector Spinae (%MVIC) | Semitendinosus | Biceps Femoris |
|------|------------------------|----------------|----------------|
| 50%  | 50.8 | 26.2 | 19.5 |
| 60%  | 54.9 | 28.4 | 19.3 |
| 70%  | 61.5 | 34.4 | 24.2 |
| 80%  | 73.1 | 37.3 | 26.4 |
| 90%  | 70.9 | 39.9 | 30.4 |

Peak erector spinae activation reaches **158% MVIC** at 90% 1RM — among the highest lumbar demands of any barbell exercise. The hamstrings increase with load but remain roughly half the erector activity.

Medial hamstrings (semitendinosus) are consistently more active than lateral hamstrings (biceps femoris) at all loads — a recruitment pattern seen in other hip-extension-dominant exercises and attributed to the semitendinosus's superior mechanical alignment for sagittal hip extension.

## The Protective Knee-Bend Strategy

As load increases from 50% to 90% 1RM, knee flexion increases systematically — from 17.1° to 24.8° — while hip flexion remains stable (~75°). This is not a technical error. The nervous system automatically allows the knees to bend under heavier loads to prevent passive hamstring strain at terminal length. The added knee flexion reduces tension in the biarticular hamstrings, allowing heavier loading without risking proximal hamstring tear. Coaches should cue only hip angle and neutral spine — the knees regulate themselves.

## Programming Context

The good morning is used as a spinal strength and posterior chain stiffness exercise, not as a primary hamstring developer. Programs that include it (Catalyst Athletics 12-Week, Westside Conjugate) use it to address lumbar fatigue resistance and hip-hinge mechanical efficiency under load. The risk-to-reward ratio worsens significantly above 80% 1RM given the extremely high lumbar peak forces.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Romanian deadlift | Bar at hips; shorter moment arm | Higher hamstring stimulus; lower spinal risk |
| Seated good morning | Seated; eliminates lower-body compensation | Isolated hip extensor development |

> For system-specific training applications, see each system's lens entry.
