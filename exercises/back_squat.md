---
id: back_squat
name: Back Squat
aliases: [High Bar Squat, Low Bar Squat]
category: exercise
pattern: [squat]
equipment: [barbell, squat rack]

difficulty:
  technical_complexity: 3
  strength_prerequisite: 3
  mobility_prerequisite: 3

muscles:
  - id: vastus_lateralis
    role: primary
  - id: vastus_medialis
    role: primary
  - id: rectus_femoris
    role: primary
  - id: gluteus_maximus
    role: primary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: erector_spinae
    role: stabilizer
  - id: core
    role: stabilizer

# EMG data from two independent studies under different load conditions.
# Values are % of maximum voluntary isometric contraction (MVC), concentric phase.
# Do NOT average across studies — conditions differ.
muscle_activation_studies:
  - source_id: yavuz_2015
    doi: "10.1080/02640414.2014.984240"
    n: 14
    population: "trained males"
    condition:
      load_pct_1rm: 80
      bar_position: high_bar
      depth: parallel
      phase: concentric
    measurements:
      - {muscle: vastus_lateralis,  mean_pct_mvc: 45.9, sd: 13.9}
      - {muscle: vastus_medialis,   mean_pct_mvc: 52.3, sd: 18.1}
      - {muscle: rectus_femoris,    mean_pct_mvc: 38.4, sd: 16.2}
      - {muscle: gluteus_maximus,   mean_pct_mvc: 28.8, sd: 18.9}
      - {muscle: biceps_femoris,    mean_pct_mvc: 18.7, sd: 14.9}
      - {muscle: semitendinosus,    mean_pct_mvc: 15.0, sd: 6.9}
      - {muscle: erector_spinae,    mean_pct_mvc: 41.1, sd: 14.0}
  - source_id: yavuz_2015
    doi: "10.1080/02640414.2014.984240"
    n: 14
    population: "trained males"
    condition:
      load_pct_1rm: 100
      bar_position: high_bar
      depth: parallel
      phase: concentric
    measurements:
      - {muscle: vastus_lateralis,  mean_pct_mvc: 48.5, sd: 17.2}
      - {muscle: vastus_medialis,   mean_pct_mvc: 61.8, sd: 19.3}
      - {muscle: rectus_femoris,    mean_pct_mvc: 42.1, sd: 17.8}
      - {muscle: gluteus_maximus,   mean_pct_mvc: 47.3, sd: 27.7}
      - {muscle: biceps_femoris,    mean_pct_mvc: 34.9, sd: 18.2}
      - {muscle: semitendinosus,    mean_pct_mvc: 29.0, sd: 16.2}
      - {muscle: erector_spinae,    mean_pct_mvc: 46.0, sd: 17.6}
  - source_id: kubo_2019
    doi: "10.1371/journal.pone.0217044"
    n: 13
    population: "resistance-trained males, 6±3 yrs experience"
    condition:
      load_pct_1rm: 70
      bar_position: high_bar
      depth: parallel
      phase: concentric
    measurements:
      - {muscle: vastus_lateralis,  mean_pct_mvc: 58, sd: null}
      - {muscle: vastus_medialis,   mean_pct_mvc: 55, sd: null}
      - {muscle: rectus_femoris,    mean_pct_mvc: 47, sd: null}
      - {muscle: gluteus_maximus,   mean_pct_mvc: 42, sd: null}
      - {muscle: biceps_femoris,    mean_pct_mvc: 28, sd: null}
      - {muscle: semitendinosus,    mean_pct_mvc: 24, sd: null}

joint_rom_required:
  ankle_dorsiflexion_deg: 20
  hip_flexion_deg: 120
  thoracic_extension_deg: 15
  source: "NASM; Greene 1994"

strength_curve:
  type: ascending
  sticking_point: bottom_third
  peak_force_position: lockout
  notes: >
    Hip moment arm peaks at the sticking point (~30–40% of ascent);
    hip extensor demand is highest there despite lower ground reaction force.
  source: "van den Tillaar & Andersen 2021, PMC8217455"

injury_risk:
  joint_stress:
    knee: moderate
    lower_back: moderate
    shoulder: low
  common_injuries:
    - structure: patellar_tendon
      mechanism: overuse
      risk_factors: [high_volume, rapid_load_increase]
    - structure: lumbar_disc
      mechanism: flexion_under_load
      risk_factors: [poor_bracing, excessive_forward_lean]
  contraindications:
    - acute_knee_injury
    - lumbar_herniation

variations: [front_squat]
progressions: [box_squat]
alternatives: [leg_press]

sources:
  - source_id: yavuz_2015
    title: "Kinematic and EMG Activities During Front and Back Squat Variations in Maximum Loads"
    author: "Yavuz HU et al."
    year: 2015
    doi: "10.1080/02640414.2014.984240"
    credibility: rct
  - source_id: kubo_2019
    title: "Comparison of muscle activation and kinematics during free-weight back squats with different loads"
    author: "Kubo K et al."
    year: 2019
    doi: "10.1371/journal.pone.0217044"
    credibility: rct
  - source_id: van_den_tillaar_2021
    title: "New Insights About the Sticking Region in Back Squats"
    author: "van den Tillaar R & Andersen V"
    year: 2021
    doi: "10.3389/fspor.2021.681581"
    credibility: rct
  - source_id: nasm_squat
    title: "The Muscles Used in Squats: Squat Biomechanics Explained"
    author: "NASM"
    credibility: expert_consensus
---

# Back Squat

The back squat is a squat pattern defined by the barbell resting across the upper back. It is one of the most widely used compound movements in strength training, and one of the three powerlifting competition lifts.

## Execution

1. Position the bar across the upper traps (high bar) or rear delts (low bar)
2. Stance slightly wider than shoulders, toes turned out 15–30 degrees
3. Inhale and brace with a Valsalva maneuver, tightening the core
4. Flex hips and knees together, tracking knees over the toes
5. Drive up out of the bottom by extending the hips

## Common Faults

- **Valgus collapse** — knees cave inward; typically from weak glute medius and abductors
- **Excessive forward lean** — usually limited ankle mobility or insufficient core bracing
- **Insufficient depth** — tight hip flexors or a miscalibrated sense of depth

## What the EMG Data Shows

Activation increases non-linearly with load. The quadriceps (vastus medialis, lateralis, rectus femoris) are consistently the dominant prime movers. Gluteus maximus activation increases markedly only at very high loads (90–100% 1RM), suggesting the glutes are more load-sensitive than depth-sensitive in the back squat. Erector spinae acts as a stabilizer throughout, with activation in the 40–46% MVC range at 80–100% 1RM.

The sticking point falls in the bottom third of the ascent, where the hip moment arm peaks despite a reduction in ground reaction force — this is primarily a hip extensor failure point, not a knee extensor failure point.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| High bar | More upright torso, quad-dominant | Bodybuilding, weightlifting accessory |
| Low bar | Greater lean, hips and legs share load | Powerlifting |
| Box squat | Fixed depth reference | Beginners, fear management |

> For system-specific training applications, see each system's lens entry.
