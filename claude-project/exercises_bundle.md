# Barlore Exercise Reference (Full)

All complete exercises.

---

<!-- FILE: exercises/atlas_stones.md -->

---
id: atlas_stones
name: Atlas Stones
status: complete
category: exercise
pattern: [hinge, carry]
equipment: [atlas stone]

difficulty:
  technical_complexity: 5
  strength_prerequisite: 4
  mobility_prerequisite: 3

muscles:
  - id: erector_spinae
    role: primary
  - id: gluteus_maximus
    role: primary
  - id: rectus_femoris
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: vastus_medialis
    role: primary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: multifidus
    role: secondary
  - id: rectus_abdominis
    role: secondary
  - id: adductor_magnus
    role: secondary
  - id: adductor_longus
    role: secondary
  - id: biceps_brachii
    role: secondary
  - id: forearm_flexors
    role: secondary
  - id: rhomboids
    role: secondary
  - id: trap_upper
    role: secondary
  - id: trap_middle
    role: secondary
  - id: gastrocnemius_medial
    role: tertiary
  - id: gastrocnemius_lateral
    role: tertiary
  - id: soleus
    role: tertiary
  - id: deltoid_anterior
    role: tertiary

muscle_activation_studies: []

joint_rom_required:
  hip_flexion_deg: 120
  knee_flexion_deg: 110
  thoracic_flexion_deg: 40
  source: "biomechanical inference from lapping phase"

strength_curve:
  type: ascending
  sticking_point: initial_break_from_floor
  notes: "Heaviest demand at floor break; once lapped, hip extension is mechanically advantaged."

injury_risk:
  joint_stress:
    lumbar_spine: moderate
    biceps_tendon: moderate
    knee: low
  common_injuries:
    - structure: lumbar_disc
      mechanism: flexion_under_load_during_first_pull
      risk_factors: [inadequate hip_mobility, rounding_under_fatigue, excessive_load]
    - structure: biceps_tendon_long_head
      mechanism: sustained_isometric_flexion_grip_around_stone
      risk_factors: [heavy_stone, wet_or_uncoated_stone, fatigued_grip]
  contraindications:
    - acute_lumbar_disc_herniation
    - active_biceps_tendinopathy

variations: []
progressions: []
alternatives: [barbell_deadlift, sandbag_load]

sources: []
---

# Atlas Stones

A multi-phase strongman lift where a heavy spherical stone is pulled from the floor, lapped on the thighs, and loaded onto a platform or over a bar. The lift demands posterior chain strength, hip mobility, and a unique grip strategy using arm wrap and friction (often assisted by tacky/pine tar in competition). Among carry events, atlas stones produce relatively low lumbar spinal compression because the stone's center of mass stays close to the lower back throughout the lift.

## Execution

1. **Setup.** Stand with the atlas stone between your feet, toes slightly turned out. Hinge at the hips and squat down to wrap both arms around the stone, fingers reaching underneath. Many stones have a small flat spot on the bottom that aids initial grip.
2. **First Pull.** Drive through the posterior half of your feet, pulling the stone upward in a motion similar to a Romanian deadlift. Keep the stone as close to your body as possible.
3. **Lap.** As the stone passes the knees, sit back (similar to sitting onto a box) and roll the stone onto your thighs. Squeeze your thighs together to secure it. This is the transition point; adjust your arm position to reach over the top of the stone.
4. **Second Pull / Loading.** Explosively extend through the hips and knees, driving the stone up your torso. Lean back slightly to get the stone as high as possible, then close distance to the platform and extend the hips to place or push the stone onto the loading surface.
5. **Descent.** Control the stone's return to the floor. Do not drop from height if training alone.

## Programming Note

Atlas stones impose extreme full-body fatigue. Allow 7-10 days between heavy stone sessions. In competition prep, introduce tacky (pine tar adhesive) 6-8 weeks out so athletes adapt to the altered grip feel. For general strength development, sandbag loading is a safer progression that preserves the lapping motor pattern without the spinal loading peaks of a rigid sphere.


---

<!-- FILE: exercises/back_squat.md -->

---
id: back_squat
name: Back Squat
status: complete
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

variations: [front_squat, box_squat, overhead_squat]
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


---

<!-- FILE: exercises/barbell_curl.md -->

---
id: barbell_curl
name: Barbell Curl
status: complete
category: exercise
pattern: [isolation]
equipment: [barbell]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: biceps_brachii
    role: primary
  - id: brachialis
    role: secondary
  - id: brachioradialis
    role: secondary

# porcari_2014 (n=16): biceps_brachii 76.5% MVIC — highest among all curls tested except concentration.
# marcolin_2018 (n=12): qualitative only; no absolute %MVIC reported.
# ROM: 144.6° total elbow flexion. Shoulder position: neutral (0° flexion/extension).
muscle_activation_studies:
  - source_id: porcari_2014
    doi: null
    n: 16
    population: "healthy adults, standardized load"
    condition:
      implement: barbell
      phase: full_rep
    measurements:
      - {muscle: biceps_brachii, mean_pct_mvc: 76.5, sd: null}

joint_rom_required:
  elbow_flexion_deg: 145
  shoulder_flexion_deg: 0
  source: "Marcolin 2018"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Peak muscle force at ~90° elbow flexion where moment arm is maximal; bell-shaped across the full curl arc"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    wrist: low
  common_injuries:
    - structure: distal_biceps_tendon
      mechanism: eccentric_overload
      risk_factors: [excessive_weight, rapid_eccentric, pre_existing_tendinopathy]
    - structure: wrist_extensors
      mechanism: forced_pronation_at_top
      risk_factors: [wrist_flexion_at_top_of_curl, heavy_load]
  contraindications:
    - acute_distal_biceps_tendinopathy

variations: []
progressions: []
alternatives: [ez_bar_curl, dumbbell_bicep_curl]

sources:
  - source_id: porcari_2014
    title: "ACE-Sponsored Research: Best Biceps Exercises"
    author: "Porcari, John P. et al. (ACE)"
    year: 2014
    doi: null
    credibility: rct
  - source_id: marcolin_2018
    title: "Differences in electromyographic activity of biceps brachii and brachioradialis while performing three variants of curl"
    author: "Marcolin, Giuseppe et al."
    year: 2018
    doi: null
    credibility: rct
---

# Barbell Curl

The barbell curl is the foundational barbell elbow flexion exercise for biceps development. Both arms work in a fixed bilateral pattern that allows the greatest absolute load of any curl variation. The pronated-to-neutral wrist position and bilaterally locked grip limits supination but enables systematic progression through standardized load increments.

## Execution

1. Stand with a pronated-to-supinated grip at approximately shoulder width; elbows close to the torso
2. Keep the upper arms vertical and stationary throughout; do not allow the elbows to drift forward
3. Curl the bar in an arc from full extension to the shoulder, rotating the wrists to full supination at the top
4. Lower under control through the full eccentric without letting the bar drop

## What the EMG Data Shows

Porcari 2014 (ACE-commissioned, n=16):

| Exercise | Biceps Brachii |
|----------|----------------|
| Barbell curl | 76.5% MVIC |
| EZ-bar curl | 75.4% MVIC |
| Concentration curl | 97.9% MVIC |
| Incline dumbbell curl | 77.5% MVIC |

The barbell and EZ-bar produce nearly identical activation, differing by only 1.1%. The fixed supinated grip of the straight barbell maintains slightly higher activation than the EZ-bar's semi-pronated position.

## ROM and Shoulder Position

Marcolin 2018 measured 144.6° elbow flexion ROM for the barbell curl. The shoulder stays neutral (0° flexion). Because the shoulder is not flexed or extended, the biceps long head operates in a mid-range length position — mechanically favorable but not as long as the incline dumbbell curl's shoulder-extended position.

## Bilateral vs Unilateral

The bilateral barbell pattern allows higher absolute loads but prevents independent correction of left-right imbalances. Trainees with notable bilateral asymmetries should include unilateral dumbbell or cable curl variations in their programming.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| EZ-bar curl | Semi-pronated grip; reduces wrist stress | Wrist comfort |
| Dumbbell curl | Allows supination through ROM | Unilateral correction |
| Preacher curl | Supported upper arm; ascending strength curve | Lengthened-position emphasis |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/barbell_lunge.md -->

---
id: barbell_lunge
name: Barbell Lunge
status: complete
category: exercise
pattern: [squat]
equipment: [barbell, squat rack]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 3

muscles:
  - id: rectus_femoris
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: vastus_medialis
    role: primary
  - id: gluteus_maximus
    role: primary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: adductor_magnus
    role: secondary
  - id: soleus
    role: secondary
  - id: gastrocnemius_medial
    role: secondary
  - id: gastrocnemius_lateral
    role: secondary
  - id: erector_spinae
    role: stabilizer
  - id: gluteus_medius
    role: stabilizer
  - id: obliques
    role: stabilizer
  - id: rectus_abdominis
    role: stabilizer

muscle_activation_studies: []

joint_rom_required:
  hip_flexion_deg: 100
  knee_flexion_deg: 120
  hip_extension_deg: 20
  ankle_dorsiflexion_deg: 30
  source: "biomechanical inference"

strength_curve:
  type: ascending
  sticking_point: bottom
  peak_force_position: bottom
  notes: "Most difficult at the bottom of the lunge where the lead knee is deeply flexed and the hip is loaded. Mechanical advantage improves as the lifter pushes back up."
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    knee: moderate
    hip: low
    ankle: low
    lumbar_spine: low
  common_injuries:
    - structure: patellofemoral_joint
      mechanism: anterior_knee_stress_from_excessive_forward_lean_or_knee_drift
      risk_factors: [excessive_forward_knee_travel_under_load, weak_vastus_medialis, limited_ankle_dorsiflexion]
    - structure: hip_flexor
      mechanism: strain_on_trailing_leg_hip_flexor
      risk_factors: [tight_hip_flexors, excessive_stride_length, sudden_deceleration]
  contraindications:
    - acute_knee_injury
    - severe_balance_impairment
    - acute_hip_flexor_strain

variations: []
progressions: []
alternatives: []

sources: []
---

# Barbell Lunge

A unilateral squat variation performed with a barbell on the upper back. The lunge develops single-leg strength, hip stability, and addresses bilateral strength imbalances more effectively than bilateral squat variants.

## Execution

1. Set the barbell on a squat rack just below shoulder height. Step under the bar and position it across the upper traps (high bar) or rear delts (low bar). Grip the bar outside the shoulders and unrack by driving both legs up simultaneously.
2. Step back from the rack and set the feet at hip width. Brace the core.
3. Step forward with one leg, landing heel-first. Bend both knees to lower the torso straight down until the rear knee is just above the floor and the front thigh is approximately parallel to the ground. Keep the torso upright and the front shin as vertical as possible.
4. Drive through the front heel to push back to the starting position. Bring the front foot back in line with the rear foot.
5. Alternate legs each rep, or complete all reps on one side before switching.

## Programming Note

The barbell lunge is typically programmed for 3-4 sets of 8-12 reps per leg. It pairs well with bilateral squats in the same session as an accessory movement. Beginners should master bodyweight lunges and dumbbell lunges before loading a barbell. The walking lunge variant adds a dynamic balance challenge, while the reverse lunge reduces shear stress on the front knee and is preferable for trainees with knee sensitivity.


---

<!-- FILE: exercises/barbell_shrug.md -->

---
id: barbell_shrug
name: Barbell Shrug
status: complete
category: exercise
pattern: [isolation]
equipment: [barbell]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 2
  mobility_prerequisite: 1

muscles:
  - id: trap_upper
    role: primary
  - id: trap_middle
    role: secondary
  - id: rhomboids
    role: secondary
  - id: forearm_flexors
    role: stabilizer
  - id: erector_spinae
    role: stabilizer

muscle_activation_studies: []

joint_rom_required:
  scapular_elevation_deg: 20
  source: "biomechanical inference"

strength_curve:
  type: bell_shaped
  sticking_point: top
  peak_force_position: mid
  notes: "Tension is highest in the mid-range where scapular elevation velocity peaks. At the top of the shrug, the upper traps reach a shortened position and force output decreases slightly."
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    shoulder: low
    cervical_spine: low
  common_injuries:
    - structure: cervical_spine
      mechanism: strain_from_excessive_cervical_flexion_or_rotation_during_shrug
      risk_factors: [looking_down_during_reps, rolling_shoulders, excessive_load]
    - structure: biceps_tendon_long_head
      mechanism: traction_from_heavy_deadhang_grip
      risk_factors: [very_heavy_load, mixed_grip]
  contraindications:
    - acute_cervical_disc_herniation
    - acute_trap_strain

variations: []
progressions: []
alternatives: []

sources: []
---

# Barbell Shrug

An isolation exercise targeting the upper trapezius through scapular elevation. The barbell allows heavier loading than dumbbell variants, making it effective for building trap mass and grip strength simultaneously.

## Execution

1. Stand with feet shoulder-width apart. Hold a barbell at arms' length in front of the thighs using a pronated (overhand) grip slightly wider than shoulder width. Pull the shoulders back slightly and stand tall.
2. Without bending the elbows, elevate both shoulders straight up toward the ears as high as possible. Exhale at the top.
3. Hold the peak contraction for one second, squeezing the traps.
4. Lower the bar under control back to the starting position. Avoid bouncing or using momentum.
5. Keep the head neutral throughout — do not flex the neck forward or roll the shoulders.

## Programming Note

Barbell shrugs respond well to moderate-to-heavy loading for 3-4 sets of 10-15 reps. A controlled eccentric (2-3 seconds) enhances upper trap time under tension. Avoid rolling the shoulders in a circular motion, as this adds no extra trap activation and increases cervical spine stress. Straps are acceptable for grip-limited sets, but some trainees deliberately train shrugs without straps to develop grip endurance. Behind-the-back barbell shrugs shift emphasis slightly toward the middle traps and can be used as a variation.


---

<!-- FILE: exercises/bench_press.md -->

---
id: bench_press
name: Bench Press
status: complete
aliases: [Flat Barbell Bench Press]
category: exercise
pattern: [horizontal press]
muscles:
  - id: pectoralis_major
    role: primary
  - id: triceps_brachii
    role: primary
  - id: deltoid_anterior
    role: secondary
equipment: [barbell, bench, rack]
difficulty: intermediate
variations: []
alternatives: []
muscle_activation_studies:
  - source_id: saeterbakken_2017
    doi: null
    n: 21
    population: "healthy males"
    condition:
      reps: 6
      phase: concentric
      grip_width: narrow
    measurements:
      - {muscle: pectoralis_major, mean_pct_mvc: 39.24, sd: 19.53}
      - {muscle: triceps_brachii,  mean_pct_mvc: 36.56, sd: 11.92}
  - source_id: saeterbakken_2017
    n: 21
    population: "healthy males"
    condition:
      reps: 6
      phase: concentric
      grip_width: regular
    measurements:
      - {muscle: pectoralis_major, mean_pct_mvc: 43.14, sd: 19.53}
      - {muscle: triceps_brachii,  mean_pct_mvc: 33.22, sd: 14.20}
  - source_id: saeterbakken_2017
    n: 21
    population: "healthy males"
    condition:
      reps: 6
      phase: concentric
      grip_width: wide
    measurements:
      - {muscle: pectoralis_major, mean_pct_mvc: 46.48, sd: 15.81}
  - source_id: marcos_pardo_2020
    doi: null
    n: 13
    population: "strength-trained men"
    condition:
      load_pct_1rm: 60
      reps: 12
      grip_width: standard
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 21.40, sd: null}
      - {muscle: deltoid_lateral,   mean_pct_mvc: 5.00,  sd: null}
      - {muscle: deltoid_posterior, mean_pct_mvc: 3.50,  sd: null}

joint_rom_required:
  elbow_flexion_deg: 79.5
  wrist_flexion_extension_deg: 11.9
  notes: "ROM at 15% BW load (Muyor et al. 2022); shoulder-width grip requires ~20° greater shoulder flexion and ~25° greater elbow extension vs. wide grip"
  source: "Muyor et al. 2022; Duffey 2008"

strength_curve:
  type: ascending
  sticking_point: bottom_third
  peak_force_position: lockout
  notes: "Sticking point 2-3 inches off chest; pectoralis major at maximal stretch and worst leverage; J-curve bar path shifts load over shoulder joint earlier"
  source: "Saeterbakken et al. 2017; Westside Barbell analysis"

sources:
  - title: "Starting Strength"
    author: "Mark Rippetoe"
    credibility: practitioner
  - title: "Effects of grip width on muscle strength and activation in the bench press"
    author: "Saeterbakken, A. H., Andersen, V., Brudeseth, A., Lund, H., Fimland, M. S."
    year: 2017
    doi: null
    credibility: rct
  - title: "Electromyographic activity of shoulder muscles during different variations of the shoulder press exercise"
    author: "Marcos-Pardo, P. J., et al."
    year: 2020
    doi: null
    credibility: rct
  - title: "Kinematics of the barbell bench press"
    author: "Muyor, J. M., et al."
    year: 2022
    doi: null
    credibility: rct
---

# Bench Press

The bench press is a horizontal pressing movement performed lying on a bench, pressing a barbell from the chest to full arm extension. It is one of the three powerlifting competition lifts.

## Execution

1. Lie back with eyes under the bar, feet planted, slight arch in the upper back
2. Grip slightly wider than shoulders, retract and depress the shoulder blades
3. Unrack and lower the bar to the lower chest under control
4. Press up and slightly back toward the rack over the shoulders

## Common Faults

- **Flaring the elbows to 90 degrees** — shoulder strain; tuck to ~45–75 degrees
- **Bouncing off the chest** — loses tension and control
- **Hips rising off the bench** — invalid in competition and unsafe

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Close grip | Hands narrower, more triceps | Triceps and lockout |
| Paused | Pause on the chest | Powerlifting specificity |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/bench_press_with_bands.md -->

---
id: bench_press_with_bands
name: Bench Press with Bands
status: complete
category: exercise
pattern: [horizontal press]
equipment: [barbell, bench, rack, resistance_bands]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 1

muscles:
  - id: pectoralis_major
    role: primary
  - id: triceps_brachii
    role: primary
  - id: deltoid_anterior
    role: secondary
  - id: latissimus_dorsi
    role: stabilizer

# No peer-reviewed EMG %MVIC study specific to banded bench press found.
# Muscle activation distribution mirrors the standard bench press (saeterbakken_2017,
# marcos_pardo_2020). Bands shift load distribution without fundamentally changing
# which muscles are involved — they change the resistance profile, not the neural
# recruitment pattern. Triceps activation at lockout is amplified because band tension
# peaks where triceps contribute most to the ascending strength curve.
muscle_activation_studies: []

joint_rom_required:
  elbow_flexion_deg: 79.5
  notes: "Identical ROM to the standard bench press. Bands do not restrict ROM; they modify the load at each position within the same full range."
  source: "Muyor et al. 2022 (standard bench press ROM reference)"

strength_curve:
  type: ascending
  sticking_point: bottom_third
  peak_force_position: lockout
  notes: "The natural ascending bench press strength curve is preserved. Bands add a proportional resistance overlay: minimal tension at the chest, maximal tension at lockout. This creates a load-matched strength curve — the bar becomes progressively heavier precisely where the lifter is progressively stronger — forcing near-maximal effort throughout the full range rather than only at the sticking point. The result is that the lift becomes equally demanding at lockout as at the sticking point."
  source: "Anderson et al. 2008; Simmons (Westside) practitioner description"

injury_risk:
  joint_stress:
    shoulder: moderate
    elbow: low
    wrist: low
  common_injuries:
    - structure: glenohumeral_joint
      mechanism: anterior_impingement
      risk_factors: [band_tension_pulling_bar_toward_rack_on_descent, excessive_band_load_relative_to_bar_weight]
    - structure: pectoralis_major_tendon
      mechanism: eccentric_overload_at_stretch
      risk_factors: [band_tension_too_high_relative_to_bar_weight, elastic_rebound_at_bottom]
  notes: "Band tension at lockout should not exceed ~25–30% of the total load, or the band tension at the chest becomes so light that the effective load is almost purely barbell. The correct ratio ensures tension is meaningful throughout the range, not only at the top."
  contraindications:
    - acute_pectoralis_major_tear
    - acute_shoulder_impingement

variations: [bench_press, board_press]
progressions: []
alternatives: [bench_press, close_grip_barbell_bench_press]

sources:
  - source_id: simmons_westside
    title: "Westside Barbell Book of Methods"
    author: "Louie Simmons"
    year: null
    doi: null
    credibility: practitioner
  - source_id: anderson_2008
    title: "Effect of Load on Peak Power of the Bar, Body, and System During the Deadlift"
    author: "Anderson, C. E. et al."
    year: 2008
    doi: "10.1519/JSC.0b013e31816a6f7d"
    credibility: rct
  - source_id: saeterbakken_2017
    title: "Effects of grip width on muscle strength and activation in the bench press"
    author: "Saeterbakken, A. H. et al."
    year: 2017
    doi: null
    credibility: rct
---

# Bench Press with Bands

The bench press with bands is a bench press performed with resistance bands anchored to the base of the rack and looped over the bar ends, adding accommodating resistance — load that increases proportionally as the bar rises toward lockout. At the chest, band tension is minimal; at full lockout, band tension is at maximum. This modification matches the resistance curve more closely to the human strength curve, eliminating the "easy lockout" of standard free-weight pressing and demanding maximal effort throughout the full range of motion. It is the primary Dynamic Effort (DE) pressing exercise in the Westside Conjugate system.

## Setup

1. Loop each band securely around the base of the rack (or anchored to a loaded bar on the floor), one band per side
2. Stretch the bands over the bar ends and position them inside the collars; ensure bands are symmetric
3. Load the barbell to the target working weight — for Westside DE work, approximately 50–55% of 1RM barbell plus band tension
4. Verify that the bands do not contact the rack uprights during the press — they should hang free

**Band tension target**: Aim for bands that add approximately 20–25% of total load at lockout. At the chest, band tension should be minimal but the bands should remain taut (not slack).

## Execution

1. Set up with the standard bench press arch, scapular retraction, and foot drive
2. Unrack and lower the bar under control — the bands will reduce effective load during descent but do not use the bands as a "bounce assist" at the bottom
3. At the bottom, the bar feels lighter (minimal band tension); press immediately and accelerate the bar throughout the full range
4. As the bar rises, band tension increases — the load continues climbing toward lockout; drive through completion
5. Lock out against the full band tension; do not slow down approaching lockout

## The Accommodating Resistance Effect

Standard free weights are heaviest at the bottom (worst leverage, most stretched muscle) and effectively lighter at lockout (best leverage, strongest position). This creates a mismatch: the lifter has unused capacity at the top and is maximally challenged only at the sticking point.

Bands invert this asymmetry:

| Position | Bar load | Band tension | Total load |
|----------|----------|--------------|------------|
| Chest (bottom) | 100% | ~0% | ~100% |
| Midrange | 100% | ~12% | ~112% |
| Lockout | 100% | ~25% | ~125% |

The lifter's muscular capacity also increases from bottom to top (ascending strength curve). Bands apply more load precisely where the lifter is stronger — creating a closer match between load demand and force capacity at every joint angle.

## Westside DE Protocol

Dynamic Effort work uses submaximal loads with maximal intentional velocity. For the bench press with bands:

- **Load**: 50–55% 1RM barbell + bands (total ≈ 75–80% at lockout)
- **Sets/reps**: 8–9 sets of 3 reps
- **Rest**: 45–60 seconds between sets
- **Intent**: Every rep is pressed with absolute maximal acceleration; bar speed is the training variable, not the weight

The short rest and speed focus train rate of force development and bar acceleration — qualities that carry over to the maximal effort press by improving the initial drive off the chest, which determines whether the lifter clears the sticking point.

## Why Bands, Not Just Heavy Weights

Heavy free weights slow due to decelerative demand near lockout — the lifter must decelerate the bar before it flies out of the hands. With bands, the increasing resistance takes care of deceleration naturally, allowing the lifter to press with maximal speed through the complete range without a deliberate slowdown phase. This is critical for training bar acceleration as a motor skill.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/bent_over_barbell_row.md -->

---
id: bent_over_barbell_row
name: Bent Over Barbell Row
status: complete
category: exercise
pattern: [horizontal_pull]
equipment: [barbell]

difficulty:
  technical_complexity: 3
  strength_prerequisite: 2
  mobility_prerequisite: 3

muscles:
  - id: latissimus_dorsi
    role: primary
  - id: rhomboids
    role: primary
  - id: trap_middle
    role: primary
  - id: erector_spinae
    role: primary
  - id: biceps_brachii
    role: secondary
  - id: deltoid_posterior
    role: secondary
  - id: rectus_femoris
    role: stabilizer

# ssd_2026 is a literature compilation. The BOR study reports erector spinae subdivisions
# (LUES = left upper/thoracic ES; RLES/LLES = right/left lumbar ES) and rectus femoris
# with numeric values, but reports latissimus dorsi and biceps brachii as qualitative only
# ("high activation"). Do NOT fabricate %MVIC values for LD or biceps.
# Values are %MVC (not %MVIC — different normalization; directly comparable within study only).
muscle_activation_studies:
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation — multiple study populations"
    condition:
      grip: wide
      phase: concentric
      notes: "Bilateral bent-over barbell row"
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 72.8, sd: null, notes: "Left upper thoracic erector spinae (LUES); concentric phase"}
      - {muscle: latissimus_dorsi, mean_pct_mvc: null, sd: null, notes: "High activation — quantitative %MVIC not reported in source; increases significantly vs narrow grip (p<0.01)"}
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation — multiple study populations"
    condition:
      grip: wide
      phase: eccentric
      notes: "Bilateral bent-over barbell row"
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 54.1, sd: null, notes: "Left upper thoracic erector spinae (LUES); eccentric phase"}
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation — multiple study populations"
    condition:
      grip: wide
      phase: isometric
      notes: "Postural stabilization during bilateral BOR"
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 42.9, sd: null, notes: "Lumbar erector spinae; average of RLES 42.5% and LLES 43.3% MVC"}
      - {muscle: rectus_femoris, mean_pct_mvc: 8.2,  sd: null, notes: "Right rectus femoris isometric stabilization"}

joint_rom_required:
  hip_flexion_deg: 75
  elbow_flexion_deg: 110
  shoulder_extension_deg: 90
  notes: >
    Hip hinge to bring torso approximately parallel to the floor (requiring ~75° hip
    flexion and adequate hamstring flexibility). Elbow flexes through 90–110° during
    the concentric phase. Shoulder initiates at ~90° flexion and extends through
    neutral during the pull.
  source: "ssd_2026"

strength_curve:
  type: ascending_descending
  sticking_point: terminal_lockout
  peak_force_position: mid_range
  notes: >
    Peak mechanical force is generated at mid-range — elbow flexed ~90° and shoulder
    near neutral extension. The sticking point is at terminal concentric lockout where
    the bar contacts the torso, because the horizontal lever arm of the humerus
    relative to the shoulder requires maximum force to complete final scapular retraction.
  source: "ssd_2026"

injury_risk:
  joint_stress:
    lower_back: high
    shoulder: low
    elbow: low
  common_injuries:
    - structure: lumbar_disc
      mechanism: compressive_and_shear_forces_during_forward_flexion
      risk_factors: [heavy_loads, spinal_rounding, fatigue, rapid_load_increase]
    - structure: biceps_brachii_tendon
      mechanism: eccentric_overload
      risk_factors: [supinated_grip_at_heavy_loads, high_frequency, inadequate_recovery]
  contraindications:
    - acute_lumbar_disc_herniation
    - proximal_hamstring_tendinopathy

variations: []
progressions: []
alternatives: [inverted_row]

sources:
  - source_id: ssd_2026
    title: "Sports Science Data Extraction: Vertical Pulling and Horizontal Rowing"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Bent Over Barbell Row

The bent-over barbell row (BOR) is a compound barbell exercise performed with the torso near horizontal. It is the primary standing horizontal pulling movement in strength training and the most direct barbell developer of the upper and mid back musculature. Because no anterior support is provided, the lumbar spine and posterior chain must sustain the forward-flexed posture under heavy load throughout every repetition — making the BOR simultaneously one of the most effective back builders and one of the most spinal-loading exercises in training.

## Execution

1. Stand over a loaded barbell; set feet hip-width, hinge to grip the bar with a pronated double-overhand grip slightly wider than shoulder-width
2. Deadlift the bar to the standing position, then hinge forward until the torso is 10–30° above parallel to the floor; maintain a neutral lumbar spine with a hard brace
3. Begin each rep with the bar hanging at arm's length; pull the bar toward the lower sternum by driving the elbows upward and backward
4. Squeeze the scapulae together at the top; pause briefly with the bar contacting the torso
5. Lower under control through a full 2-second eccentric; do not let the bar drop

## What the EMG Data Shows

The quantitative EMG data from the ssd_2026 literature compilation documents the BOR's erector spinae and stabilizer demands directly, but reports the primary pulling muscles (latissimus dorsi, biceps brachii) in qualitative terms only — "high activation." This is a genuine limitation of the available data, not an omission from this entry.

**Erector spinae demand is substantial and phase-asymmetric**: The left upper thoracic erector spinae (LUES) — representative of the thoracic spinal extensors — activates at 72.8% MVC during the concentric pull and 54.1% MVC during the eccentric descent. The lumbar erector spinae (averaging 42.9% MVC) contracts isometrically throughout both phases to resist spinal flexion under the barbell's moment arm. These are not incidental activation values — they represent the primary mechanical cost of performing the BOR: the spine is loaded continuously and heavily throughout each set.

**Rectus femoris (8.2% MVC isometric)** contributes lower-body postural stability against backward toppling, confirming that the BOR is not an isolated upper-body exercise — the entire kinetic chain is engaged to maintain the forward-flexed posture.

## Technical Modifications and Their Effects

The BOR's neuromuscular stimulus is highly sensitive to grip width and hand orientation:

**Grip width**: Wide grip significantly increases latissimus dorsi sEMG amplitude vs narrow grip (p < 0.01), with wide-grip BOR showing superior RMS peaks even under accumulated fatigue. The abducted elbow path of a wide grip increases shoulder horizontal abduction, loading the mid and upper trapezius and posterior deltoid more than a narrow grip.

**Hand orientation (supinated grip)**: A supinated underhand grip increases biceps brachii and latissimus dorsi activation by improving the mechanical alignment of the humerus during sagittal shoulder extension. The supinated Yates row and supinated Pendlay row exploit this principle.

**Unilateral vs bilateral**: A direct comparison at 80% 1RM (n=30) found no statistically significant differences in latissimus dorsi, posterior deltoid, or biceps brachii activation between bilateral barbell rows and unilateral dumbbell rows. Neural drive to the primary back muscles is conserved across execution formats — unilateral execution adds lateral instability demand without compromising back muscle recruitment.

## Spinal Loading Tradeoff

The standing BOR places among the highest lumbar loads of any upper-body exercise. The inverted row produces equivalent latissimus dorsi (99.3% MVIC) and middle trapezius (98.6% MVIC) activation while reducing lumbar erector spinae demand to ~29% MVC (vs ~43% in the BOR) and rectus femoris to 2.7% MVC. For athletes with lower back pathology or fatigue accumulation from heavy deadlift training, the inverted row is the appropriate substitute.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Pendlay row | Bar returned to floor each rep; strict horizontal torso | Maximum force production per rep; minimizes momentum |
| Barbell Yates row | 70° torso angle; supinated grip | Mid-back emphasis; reduced lumbar load |
| Inverted row | Bodyweight; supine; no spinal compression | Low-back injury management; scapular retraction isolation |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/bent_over_dumbbell_rear_delt_raise_with_head_on_bench.md -->

---
id: bent_over_dumbbell_rear_delt_raise_with_head_on_bench
name: Bent-Over Dumbbell Rear Delt Raise With Head On Bench
status: complete
category: exercise
pattern: [isolation]
equipment: [dumbbell, bench]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: deltoid_posterior
    role: primary
  - id: deltoid_lateral
    role: primary
  - id: trap_middle
    role: secondary
  - id: rhomboids
    role: secondary
  - id: infraspinatus
    role: stabilizer

# No peer-reviewed quantitative EMG data found for this specific variation.
# Mechanically identical to seated_bent_over_rear_delt_raise but with lumbar fully supported.
# Posterior delt and lateral delt activation expected to match Sweeney 2014 (~73% and ~70% MVIC).
muscle_activation_studies: []

joint_rom_required:
  shoulder_abduction_deg: 90
  hip_flexion_deg: 90
  source: "biomechanical inference from seated_bent_over_rear_delt_raise"

strength_curve:
  type: ascending
  sticking_point: top_third
  peak_force_position: top
  notes: "Identical to seated bent-over rear delt raise — gravity profile unchanged; bench support only eliminates spinal loading"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    shoulder: low
    elbow: low
    lower_back: none
  common_injuries: []
  contraindications: []

variations: []
progressions: []
alternatives: [seated_bent_over_rear_delt_raise, face_pull]

sources: []
---

# Bent-Over Dumbbell Rear Delt Raise With Head On Bench

This variation of the rear delt raise places the forehead or chest against the end of an incline or flat bench while bending over, fully removing all lumbar erector spinae demand. The mechanics of the shoulder movement are identical to the seated bent-over raise — the torso is approximately parallel to the floor, arms raise laterally in horizontal abduction — but the spine is supported and the position is rigidly fixed throughout the set.

## Execution

1. Rest the forehead on the end of a flat bench or pad with the torso parallel to the floor; let the dumbbells hang straight down
2. Keep the arms nearly extended with a slight elbow bend
3. Raise the arms out to the sides until the elbows reach shoulder height, leading with the elbows
4. Avoid using upper trap shrugging to initiate; the movement should feel like pulling the shoulder blades apart
5. Lower under control

## Why the Head-Supported Variation

The seated bent-over raise requires sustained isometric erector spinae activity to hold the torso forward. During high-volume isolation work or at the end of a training session, the erectors often fatigue before the target posterior deltoid, forcing early set termination.

By resting the forehead on the bench:
- All lumbar and thoracic erector demand is eliminated
- The torso angle is passively maintained throughout the set
- All available neural drive goes to the posterior deltoid and upper back
- Athletes with lower back sensitivity can train this pattern without lumbar loading

The trade-off is that no hip hinge mobility or core stability is trained simultaneously. This is purely a posterior shoulder isolation exercise.

## Activation Expectations

Based on the mechanically equivalent seated bent-over raise (Sweeney 2014, n=16): posterior deltoid ~73% MVIC, lateral deltoid ~70% MVIC, anterior deltoid ~5% MVIC. The head/bench support does not change the shoulder mechanics.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/board_press.md -->

---
id: board_press
name: Board Press
status: complete
category: exercise
pattern: [horizontal press]
equipment: [barbell, bench, rack, boards]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 1

muscles:
  - id: pectoralis_major
    role: primary
  - id: triceps_brachii
    role: primary
  - id: deltoid_anterior
    role: secondary
  - id: latissimus_dorsi
    role: stabilizer

# No peer-reviewed EMG study with %MVIC found for the board press specifically.
# Muscle activation pattern is inferred from bench press EMG literature (saeterbakken_2017,
# marcos_pardo_2020) with the following modification: the bottom-range pectoralis stretch
# contribution (the dominant driver in the lowest third of the standard bench press) is
# absent. Board height shifts emphasis progressively toward triceps as ROM shortens.
muscle_activation_studies: []

joint_rom_required:
  elbow_flexion_deg: 30
  notes: "ROM depends on board height. 1 board (~50mm): removes only the deepest 10–15° of elbow flexion. 5 boards (~125mm): removes the bottom ~50–60° of elbow flexion. The exercise begins from lockout and ends at the board contact angle; no bottom-stretch position is reached."
  source: "Biomechanical inference from bench press ROM literature (Muyor et al. 2022)"

strength_curve:
  type: ascending
  sticking_point: board_contact_point
  peak_force_position: lockout
  notes: "The standard bench press sticking point (2–3 inches off the chest) is bypassed at 2+ boards — the exercise begins above it. At 3–5 boards, the lift starts in the strong mid-range and finishes at lockout, allowing supramaximal loads (>100% of standard bench 1RM) to be handled because pectoralis major active insufficiency at depth is eliminated. The effective sticking point becomes the board contact point itself."
  source: "Simmons (Westside) practitioner description; bench press sticking point literature"

injury_risk:
  joint_stress:
    shoulder: low
    elbow: moderate
    wrist: low
  common_injuries:
    - structure: triceps_brachii_tendon
      mechanism: overload_at_lockout
      risk_factors: [supramaximal_loading, rapid_load_increase, inadequate_warm_up]
    - structure: glenohumeral_joint
      mechanism: anterior_impingement
      risk_factors: [improper_bar_path_with_boards, elbow_flare_at_high_board_heights]
    - structure: wrist
      mechanism: compressive_and_shear_load
      risk_factors: [cocked_wrist_position, supramaximal_loading]
  notes: "Board stability is a setup safety concern — boards that shift during the lift create an unpredictable surface. Secure boards to the chest with a bungee cord, strapped vest, or dedicated training partner holding them in place."
  contraindications:
    - acute_triceps_tendon_rupture
    - acute_elbow_injury

variations: [bench_press, close_grip_barbell_bench_press]
progressions: []
alternatives: [bench_press, floor_press]

sources:
  - source_id: simmons_westside
    title: "Westside Barbell Book of Methods"
    author: "Louie Simmons"
    year: null
    doi: null
    credibility: practitioner
  - source_id: saeterbakken_2017
    title: "Effects of grip width on muscle strength and activation in the bench press"
    author: "Saeterbakken, A. H. et al."
    year: 2017
    doi: null
    credibility: rct
---

# Board Press

The board press is a range-of-motion restricted barbell bench press in which one to five wooden boards (2×6 lumber, stacked and secured) rest on the lifter's chest, stopping the bar's descent at a fixed height above the chest. The removed bottom ROM eliminates the pectoralis major's weakest position, allowing supramaximal loading and isolating the mid-range and lockout portions of the press. It is a foundational Maximum Effort (ME) exercise in the Westside Conjugate system.

## Execution

1. Set up identically to a standard bench press: arch, retract scapulae, feet planted, eyes under bar
2. Have a training partner place the boards on the chest (or secure them with a bungee cord through the shirt)
3. Unrack and lower the bar under control until it contacts the boards — do not crash into them
4. Pause briefly (or perform a touch-and-go depending on the programming intent), then press with maximal intent
5. Lock out completely before re-racking

## Board Height and Muscle Emphasis

Each board (nominally 38–50 mm thick) cuts approximately 10–15° of elbow flexion from the bottom of the lift. This shifts which muscles bear the primary load:

| Boards | Approximate ROM removed | Primary target |
|--------|------------------------|----------------|
| 1 board (~50 mm) | Deepest chest contact only | Balanced pec/triceps; pausing above chest |
| 2 boards (~100 mm) | First ~25° of elbow flexion | Mid-range; slightly more triceps emphasis |
| 3 boards (~150 mm) | First ~40° | Triceps dominant; above sticking point |
| 4–5 boards (~200–250 mm) | First ~55° | Near-lockout isolation; supramaximal loads |

## Why Boards Allow Supramaximal Loading

In the standard bench press, the sticking point 2–3 inches off the chest is where the pectoralis major operates at maximum stretch and minimum mechanical advantage — simultaneously its weakest and most loaded position. At 3+ boards, the lift begins above this sticking point entirely. The lifter's full lockout strength is now applied through a range where their musculature is mechanically stronger, allowing 10–30% more total load than their standard bench 1RM. This overload stimulus is the primary training rationale.

## Westside Application

The board press is a Max Effort exercise in the Conjugate system, not an accessory. It is rotated with other ME exercises (floor press, close-grip bench, slingshot bench) on a weekly or bi-weekly basis to prevent accommodation. Weekly max-effort rotation prevents the nervous system from adapting to any single movement pattern while continuously driving strength in the primary press ROM.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/bodyweight_squat.md -->

---
id: bodyweight_squat
name: Bodyweight Squat
status: complete
category: exercise
pattern: [squat]
equipment: [body only]

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
    role: secondary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: adductor_magnus
    role: secondary
  - id: erector_spinae
    role: stabilizer
  - id: rectus_abdominis
    role: stabilizer
  - id: gluteus_medius
    role: stabilizer

muscle_activation_studies: []

joint_rom_required:
  hip_flexion_deg: 110
  knee_flexion_deg: 120
  ankle_dorsiflexion_deg: 25
  source: "biomechanical inference"

strength_curve:
  type: ascending
  sticking_point: bottom
  peak_force_position: bottom
  notes: "Hardest at the bottom of the squat where hip and knee flexion are maximal. Mechanical advantage improves as the lifter ascends."
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    knee: low
    hip: low
    ankle: low
  common_injuries:
    - structure: patellofemoral_joint
      mechanism: anterior_knee_pain_from_poor_tracking
      risk_factors: [excessive_knee_valgus, limited_ankle_dorsiflexion]
  contraindications:
    - acute_knee_injury
    - acute_lumbar_disc_herniation

variations: []
progressions: []
alternatives: []

sources: []
---

# Bodyweight Squat

A foundational lower-body movement and the baseline progression for all loaded squat variations. It develops quadriceps, glute, and hip mobility simultaneously with minimal injury risk.

## Execution

1. Stand with feet shoulder-width apart, toes pointed slightly outward (15-30 degrees). Arms can be extended forward for counterbalance or held behind the head.
2. Brace the core and initiate the descent by simultaneously breaking at the hips and knees, sitting back as if into a chair.
3. Descend under control until the hip crease drops below the top of the knee (parallel or deeper if mobility allows). Keep the chest tall, the back neutral, and the knees tracking over the toes throughout.
4. Drive through the full foot to stand, extending the hips and knees together. Squeeze the glutes at the top to finish the rep.

## Programming Note

The bodyweight squat serves as a movement screen and warm-up drill for beginners and an active-recovery tool for intermediate trainees. High-rep sets (15-30) build muscular endurance and reinforce squat patterning. Progress to goblet squats or barbell back squats once 3 sets of 20 can be completed with full depth and good form.


---

<!-- FILE: exercises/box_squat.md -->

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


---

<!-- FILE: exercises/butterfly.md -->

---
id: butterfly
name: Butterfly
status: complete
source: free-exercise-db
category: exercise
pattern:
- isolation
equipment:
- machine
difficulty:
  technical_complexity: null
  strength_prerequisite: null
  mobility_prerequisite: null
muscles:
- id: pectoralis_major
  role: primary
- id: deltoid_anterior
  role: secondary
muscle_activation_studies:
  - source_id: schanke_2012
    doi: null
    n: 14
    population: "trained men"
    condition:
      load_pct_1rm: 80
      implement: machine
      elbow_angle_deg: null
      phase: full_rep
      notes: "Normalized to flat barbell bench press = 100%, NOT true %MVIC. Pec deck produced 98% of bench press activation — highest of all chest isolation exercises tested."
    measurements:
      - muscle: pectoralis_major
        mean_pct_mvc: null
        sd: null
  - source_id: botton_2013
    doi: null
    n: 8
    population: "trained males"
    condition:
      load_pct_1rm: null
      implement: machine
      elbow_angle_deg: null
      phase: full_rep
    measurements:
      - muscle: deltoid_anterior
        mean_pct_mvc: 50.0
        sd: null

joint_rom_required:
  shoulder_horizontal_adduction_deg: 90
  elbow_flexion_deg: null
  source: "ACE Fitness"

strength_curve:
  type: bell_shaped
  sticking_point: top_third
  peak_force_position: top
  notes: "Cam-driven resistance profile; primary sticking point at end-range (hands at midline); machine eliminates balance demands"

variations: []
progressions: []
alternatives: []
sources:
- title: "ACE-Sponsored Research: Top 3 Most Effective Chest Exercises"
  author: "Schanke et al."
  year: 2012
  doi: null
  source_id: schanke_2012
  credibility: rct
- title: "Electromyographical analysis of the deltoid muscle between different strength training exercises"
  author: "Botton et al."
  year: 2013
  doi: null
  source_id: botton_2013
  credibility: rct
- title: free-exercise-db
  author: yuhonas (Public Domain)
  credibility: anecdotal
---

# Butterfly

## Execution

1. Sit on the machine with your back flat on the pad.
2. Take hold of the handles. Tip: Your upper arms should be positioned parallel to the
   floor; adjust the machine accordingly. This will be your starting position.
3. Push the handles together slowly as you squeeze your chest in the middle. Breathe out
   during this part of the motion and hold the contraction for a second.
4. Return back to the starting position slowly as you inhale until your chest muscles are
   fully stretched.
5. Repeat for the recommended amount of repetitions.


---

<!-- FILE: exercises/cable_lying_triceps_extension.md -->

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


---

<!-- FILE: exercises/cable_one_arm_tricep_extension.md -->

---
id: cable_one_arm_tricep_extension
name: Cable One Arm Tricep Extension
status: complete
category: exercise
pattern: [isolation]
equipment: [cable]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: triceps_lateral
    role: primary
  - id: triceps_long
    role: primary
  - id: triceps_medial
    role: secondary

# No peer-reviewed EMG data found specifically for the single-arm cable pushdown variation.
# Mechanically similar to bilateral triceps_pushdown but unilateral.
muscle_activation_studies: []

joint_rom_required:
  elbow_flexion_deg: 90
  shoulder_flexion_deg: 0
  source: "biomechanical inference from triceps_pushdown"

strength_curve:
  type: descending
  sticking_point: top_third
  peak_force_position: top
  notes: "Same descending cable profile as bilateral pushdown — hardest at the start (elbows most flexed)"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    wrist: low
  common_injuries:
    - structure: lateral_epicondyle
      mechanism: repetitive_valgus_stress
      risk_factors: [grip_too_tight, heavy_load]
  contraindications:
    - acute_lateral_epicondylitis

variations: []
progressions: []
alternatives: [triceps_pushdown, cable_rope_overhead_triceps_extension]

sources: []
---

# Cable One Arm Tricep Extension

The cable one arm tricep extension is the unilateral version of the triceps pushdown, using a single-handle attachment on a high cable pulley. Performed one arm at a time, it allows the identical elbow extension pattern as the bilateral pushdown while enabling direct observation and correction of left-right strength differences. The unilateral format also increases the core stabilization demand to resist the asymmetric cable pull.

## Execution

1. Attach a single handle to a high cable pulley; grasp with one hand using an overhand or underhand grip
2. Stand directly in front of the stack with the upper arm close to the torso, elbow at approximately 90°
3. Push the handle downward by extending the elbow until the arm is fully extended
4. Hold the contracted position briefly, then return under control
5. Complete all reps for one arm before switching

## Grip Variations

| Grip | Effect |
|------|--------|
| Overhand (pronated) | Standard; slightly more lateral head emphasis |
| Underhand (supinated) | Shifts load toward medial head and long head |
| Neutral | Intermediate |

The underhand single-arm pushdown is sometimes preferred for trainees with elbow discomfort from the pronated position.

## When to Use

The single-arm cable extension is most useful as:
- **Asymmetry correction**: When left-right strength differences are identified in bilateral pushdowns
- **Volume accumulation**: Light unilateral work accumulates with minimal systemic fatigue at session end
- **Technical precision**: Single-arm allows better focus on elbow tracking and wrist position

For primary triceps development, the bilateral pushdown or overhead variation provides greater absolute load and is time-efficient.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/cable_preacher_curl.md -->

---
id: cable_preacher_curl
name: Cable Preacher Curl
status: complete
category: exercise
pattern: [isolation]
equipment: [cable, preacher_bench]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: biceps_brachii
    role: primary
  - id: brachialis
    role: secondary
  - id: brachioradialis
    role: secondary

# No peer-reviewed EMG data found specifically for the cable preacher curl.
# Mechanically similar to barbell preacher curl but with constant tension via cable at the bottom.
muscle_activation_studies: []

joint_rom_required:
  elbow_flexion_deg: 116
  shoulder_flexion_deg: 50
  source: "biomechanical inference from preacher_curl"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Cable provides constant tension at bottom of range where free-weight preacher has near-zero load — the ascending curve of the barbell preacher is converted to more bell-shaped by the cable"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    wrist: low
  common_injuries:
    - structure: distal_biceps_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, heavy_load]
  contraindications:
    - acute_distal_biceps_tendinopathy

variations: []
progressions: []
alternatives: [preacher_curl, barbell_curl]

sources: []
---

# Cable Preacher Curl

The cable preacher curl combines the arm-bracing isolation of the preacher bench with the constant-tension load profile of a cable. Unlike the barbell preacher curl — where the resistance is near zero at full elbow extension due to gravity alignment — the cable maintains tension throughout the entire range, including at the bottom where the biceps is at its longest and most injury-susceptible position.

## Execution

1. Place a preacher bench 2–3 feet in front of a low cable pulley; attach a straight bar or EZ-bar attachment
2. Sit at the bench with the upper arms resting flat against the pad; the cable should run directly up the pad's slope
3. Starting at full extension (cable taut), curl the bar to shoulder height
4. Lower under control; do not allow the weight stack to pull the elbow into hyperextension

## Cable vs Barbell Preacher: The Critical Difference

The barbell preacher curl has an **ascending strength curve** — resistance is greatest at the bottom where the elbow is extended. This means the sticking point is at the most stretched position, and momentum-driven cheating can allow the bar to drop freely to the bottom (where the distal biceps tendon is most at risk).

The cable preacher converts this to a more **bell-shaped curve** because the cable provides constant tension even at full elbow extension. Benefits:
1. The biceps is loaded under tension at the most vulnerable lengthened position rather than having zero load there
2. This controlled eccentric at full stretch reduces the "crashing" risk present with free-weight preacher curls
3. Continuous tension from the cable eliminates the "dead zone" at the bottom of the barbell version

## Best Use Case

The cable preacher curl is particularly appropriate for:
- Trainees with a history of distal biceps tendon issues who want to train the preacher pattern with controlled bottom-range loading
- High-volume biceps work where constant tension reduces joint stress accumulation
- As a companion to barbell preacher curls to provide a different resistance profile for the same joint angle

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/cable_rope_overhead_triceps_extension.md -->

---
id: cable_rope_overhead_triceps_extension
name: Cable Rope Overhead Triceps Extension
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

# boehler_2011 (normalized to triangle push-up, NOT true %MVIC):
#   triceps_long 81% ± 21.4%, triceps_lateral 72% ± 16.5%.
# Highest long head activation in boehler_2011 among all exercises tested (tied with rope pushdown).
# Shoulder at 180° (overhead) → triceps long head at maximum length.
muscle_activation_studies:
  - source_id: boehler_2011
    doi: null
    n: null
    population: "healthy adults, rope attachment overhead"
    condition:
      implement: cable_rope
      phase: full_rep
      notes: "Normalized to triangle push-up = 100%, NOT true %MVIC. Shoulder at ~180° flexion overhead."
    measurements:
      - {muscle: triceps_long,    mean_pct_mvc: 81.0, sd: 21.4}
      - {muscle: triceps_lateral, mean_pct_mvc: 72.0, sd: 16.5}

joint_rom_required:
  elbow_flexion_deg: 130
  shoulder_flexion_deg: 180
  source: "boehler_2011"

strength_curve:
  type: descending
  sticking_point: top_third
  peak_force_position: top
  notes: "Descending; hardest when elbows are most flexed behind the head (maximum triceps stretch); cable provides constant tension throughout"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    shoulder: moderate
  common_injuries:
    - structure: triceps_tendon_long_head
      mechanism: stretch_overload
      risk_factors: [forcing_too_much_elbow_flexion_behind_head, heavy_load, pre_existing_triceps_tendinopathy]
    - structure: posterior_shoulder_capsule
      mechanism: passive_stretch
      risk_factors: [limited_shoulder_flexion_mobility, forced_overhead_position]
  contraindications:
    - acute_triceps_long_head_tendinopathy
    - severe_shoulder_flexion_restriction

variations: []
progressions: []
alternatives: [ez_bar_skullcrusher, lying_triceps_press]

sources:
  - source_id: boehler_2011
    title: "An electromyographic analysis of 3 muscles surrounding the elbow joint during a maximally forceful isometric contraction, concentric isotonic contraction, and 6 common exercises"
    author: "Boehler, Breanna et al."
    year: 2011
    doi: null
    credibility: rct
---

# Cable Rope Overhead Triceps Extension

The cable rope overhead triceps extension places the shoulder at approximately 180° flexion (fully overhead) and extends the elbow against the cable resistance. This overhead shoulder position takes the triceps long head — which crosses the shoulder joint — to its maximum mechanical length, producing the highest long head activation stimulus among triceps isolation exercises. The cable provides constant tension, including at the bottom of the range where the triceps is most stretched.

## Execution

1. Attach a rope to a low cable pulley; face away from the stack
2. Grasp the rope with both hands behind the head, shoulder fully overhead, elbows bent and pointing forward
3. Extend the elbows to push the rope upward until the arms are straight overhead
4. Lower under control until the forearms are fully behind the head at maximum stretch
5. Keep the upper arms close to the sides of the head throughout — do not let the elbows flare

## What the EMG Data Shows

Boehler 2011 (normalized to triangle push-up, not %MVIC):

| Exercise | Triceps Long | Triceps Lateral |
|----------|-------------|-----------------|
| Overhead cable extension | 81 ± 21.4 | 72 ± 16.5 |
| Rope pushdown | 81 ± 32.3 | 67 ± 15.7 |
| Skullcrusher | 70 ± 20.9 | 55 ± 14.1 |
| Kickback | 88 ± 33.0 | 87 ± 23.7 |

The overhead position ties the pushdown for long head activation in normalized terms, with notably less variance (SD 21.4 vs 32.3). The key advantage over the pushdown is the overhead position places the long head at its maximum length.

## Why the Overhead Position Matters

The triceps long head originates at the infraglenoid tubercle of the scapula (shoulder). When the arm is raised overhead (shoulder at 180°), the long head is stretched at the proximal end simultaneously with elbow flexion stretching it at the distal end. This dual-stretch produces the maximum elongation available for the long head — which constitutes approximately 60% of triceps volume.

Programs that rely entirely on pushdowns and skullcrushers underload the long head's lengthened range. The overhead extension addresses this gap.

## Cable vs Dumbbell Overhead Extension

The cable provides constant tension at the most stretched position (elbows maximally bent behind the head), where a dumbbell would have near-zero effective resistance at that angle. For maximizing the lengthened-range stimulus, the cable overhead extension is mechanically superior to the dumbbell version.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/cable_seated_lateral_raise.md -->

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


---

<!-- FILE: exercises/chin_up.md -->

---
id: chin_up
name: Chin-Up
status: complete
category: exercise
pattern: [vertical_pull]
equipment: [bodyweight]

difficulty:
  technical_complexity: 3
  strength_prerequisite: 3
  mobility_prerequisite: 1

muscles:
  - id: latissimus_dorsi
    role: primary
  - id: biceps_brachii
    role: primary
  - id: pectoralis_major
    role: secondary
  - id: trap_lower
    role: secondary
  - id: rhomboids
    role: secondary
  - id: infraspinatus
    role: stabilizer
  - id: erector_spinae
    role: stabilizer

# ssd_2026 literature compilation. All values %MVIC.
# Key finding: LD equivalent between chin-up and pull-up (117% both).
# BB significantly higher in chin-up (96 vs 78). PM higher (57 vs 44). trap_lower lower (45 vs 56).
muscle_activation_studies:
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      grip: supinated
      width: shoulder-width
    measurements:
      - {muscle: latissimus_dorsi, mean_pct_mvc: 117, sd: 46}
      - {muscle: biceps_brachii,   mean_pct_mvc: 96,  sd: 34}
      - {muscle: pectoralis_major, mean_pct_mvc: 57,  sd: 36}
      - {muscle: trap_lower,        mean_pct_mvc: 45,  sd: 22}

joint_rom_required:
  shoulder_flexion_deg: 180
  elbow_flexion_deg: 100.6
  scapular_upward_rotation_deg: 60
  notes: >
    Chin-up requires greater elbow flexion ROM (100.6° ± 14.5°) than the pronated
    pull-up (93.4° ± 14.6°). The supinated grip positions the elbows anteriorly in
    the sagittal plane, enabling more terminal flexion at lockout. Scapular upward
    rotation of 60° is required throughout the ascending phase.
  source: "ssd_2026"

strength_curve:
  type: descending
  sticking_point: top_third
  peak_force_position: bottom_third
  notes: >
    Identical curve to the pronated pull-up: hardest at the top where the humerus
    is fully adducted and the primary extensors hit active insufficiency. Peak force
    in the bottom third where LD is at optimal length-tension. The supinated grip
    does not change the curve shape — it redistributes load between biceps and lower
    trapezius, not positional difficulty.
  source: "ssd_2026"

injury_risk:
  joint_stress:
    shoulder: moderate
    elbow: low
    wrist: low
  common_injuries:
    - structure: medial_elbow
      mechanism: valgus_stress_from_supinated_grip_under_load
      risk_factors: [heavy_weighted_chin_ups, medial_epicondylitis_history]
    - structure: shoulder_subacromial_space
      mechanism: impingement_at_top_of_movement
      risk_factors: [forced_scapular_retraction_at_full_overhead_flexion, inadequate_scapular_depression_cue]
  contraindications:
    - acute_medial_epicondylitis
    - distal_biceps_tendon_pathology
    - anterior_shoulder_instability

variations: []
progressions: []
alternatives: [pullups]

sources:
  - source_id: ssd_2026
    title: "Sports Science Data Extraction: Vertical Pulling and Horizontal Rowing"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Chin-Up

The chin-up is a closed-chain bodyweight vertical pulling exercise performed with a supinated (underhand) grip at approximately shoulder width. The supinated hand position places the elbows anteriorly in the sagittal plane throughout the movement, maximizing biceps brachii mechanical advantage and increasing pectoralis major involvement compared to the pronated pull-up. Latissimus dorsi activation is equivalent between grips — both reach 117% MVIC — refuting the common claim that chin-ups are inferior for lat development.

## Execution

1. Grip the bar with palms facing toward you, hands at shoulder width; hang at full arm extension
2. Depress the scapulae (pull shoulders down from ears) before initiating the pull
3. Drive the elbows down and back, pulling the chest toward the bar
4. Continue until the chin clears the bar; avoid craning the neck — the torso should rise, not the head
5. Lower under control to full arm extension; do not relax the shoulders at the bottom

## What the EMG Data Shows

**Chin-up vs pronated pull-up** (ssd_2026 direct comparison):

| Muscle | Chin-up | Pull-up | Difference |
|--------|---------|---------|------------|
| Latissimus dorsi | 117 ± 46% | 117–130% | Equivalent |
| Biceps brachii | 96 ± 34% | 78 ± 32% | +23% in chin-up |
| Pectoralis major | 57 ± 36% | 44 ± 27% | +30% in chin-up |
| Lower trapezius | 45 ± 22% | 56 ± 21% | −20% in chin-up |

The key finding: the LD is maximally recruited regardless of grip. The chin-up is not a "bicep exercise that also uses the back" — it is a full lat exercise with additional biceps loading.

**Why biceps are higher**: The supinated forearm puts the biceps brachii in optimal alignment for elbow flexion. In the pronated pull-up, the brachialis and brachioradialis compensate for the mechanically disadvantaged biceps.

**Why lower trapezius is lower**: The sagittal elbow path of the chin-up slightly reduces the horizontal scapular depression demand compared to the frontal-plane elbow path of the pull-up. Both exercises still require substantial lower trap activation for scapular stabilization throughout.

## ROM: Why Chin-Up Has Greater Elbow Flexion

The chin-up requires 100.6° ± 14.5° of elbow flexion vs 93.4° ± 14.6° for the pull-up. The supinated grip keeps the elbows close to the torso in the sagittal plane at lockout, allowing the forearm to travel further before being blocked by the shoulder. This 7° of additional elbow flexion contributes to the greater biceps peak contraction at lockout.

## Chin-Up vs Pull-Up: Selection Logic

- **Choose pull-up** when prioritizing lower trapezius development, scapular stability, or maximum lat activation at the highest absolute load
- **Choose chin-up** when prioritizing biceps brachii development, pectoralis major recruitment, or when easier mechanics allow more volume per session

Both are valid primary vertical pulling exercises. Programming both across a training block produces broader motor pattern coverage than specializing in one.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Pull-up (pronated) | Lower biceps; higher trap_lower | Scapular emphasis; wider grip pattern |
| Close-grip chin-up | Narrower than shoulder width | Maximum biceps elbow flexion ROM |
| Weighted chin-up | External load via belt | Strength progression past bodyweight |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/clean_and_jerk.md -->

---
id: clean_and_jerk
name: Clean and Jerk
status: complete
category: exercise
pattern: [hinge]
equipment: [barbell]

difficulty:
  technical_complexity: 5
  strength_prerequisite: 4
  mobility_prerequisite: 5

muscles:
  - id: gluteus_maximus
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: erector_spinae
    role: primary
  - id: multifidus
    role: primary
  - id: trap_upper
    role: primary
  - id: triceps_brachii
    role: primary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: rectus_femoris
    role: secondary
  - id: vastus_medialis
    role: secondary
  - id: deltoid_anterior
    role: secondary
  - id: gastrocnemius
    role: secondary
  - id: soleus
    role: secondary
  - id: forearm_flexors
    role: stabilizer

# Geisler 2023 measured Hang Power Clean (HPC) for the clean phase — used as proxy.
# The full clean starts from the floor (first pull demand) and catches in a full front
# squat (adds quad recovery demand). Pull-phase VL and GM data from HPC apply.
# No peer-reviewed %MVIC study found for the jerk phase specifically.
muscle_activation_studies:
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 50
      phase: pull
      notes: "Hang Power Clean proxy for clean pull phase"
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 163.82, sd: 64.41}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 124.91, sd: 76.67}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 50
      phase: pull
      notes: "Hang Power Clean proxy for clean pull phase"
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 324.41, sd: 305.15}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 298.74, sd: 195.54}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 90
      phase: pull
      notes: "Hang Power Clean proxy; no jerk-phase EMG available"
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 249.30, sd: 213.53}

joint_rom_required:
  hip_flexion_clean_deg: 120
  knee_flexion_front_squat_catch_deg: 130
  ankle_dorsiflexion_deg: 25
  shoulder_flexion_front_rack_deg: 173
  shoulder_external_rotation_front_rack_deg: 107
  shoulder_flexion_overhead_deg: 180
  shoulder_external_rotation_overhead_deg: 90
  notes: >
    The clean and jerk requires both front-rack and overhead mobility — more total
    demands than either the clean or the jerk individually.
    Clean front-rack: 173° shoulder flexion, 107° ER (same as power_clean).
    Jerk overhead: 180° shoulder flexion, 90° ER.
    The front squat catch adds ~130° knee flexion and ~25° ankle dorsiflexion.
    Athletes with adequate front-rack mobility but insufficient overhead mobility
    cannot complete the jerk without compensatory forward bar displacement.
  source: "nasm_2020 / crossfit_2022; everett_weightlifting"

strength_curve:
  type: bell_shaped
  sticking_point: first_pull_to_transition
  peak_force_position: second_pull
  notes: >
    Clean phase: bell-shaped GRF profile. First pull ~1.5×BW; second pull peak
    2.0–2.5×BW; unweighting at double-knee bend ~1.0×BW.
    VL and GM activation at elite level reach 324% and 299% MVIC respectively at 50% 1RM.
    Front squat recovery: ascending curve from the deep front squat position.
    Jerk phase: distinct impulse profile — dip (brief eccentric, 10–15° knee flexion),
    drive (explosive triple extension peak GRF ~2.5–3.0×BW), catch (overhead eccentric
    stabilisation, GRF ~1.5×BW as split stance absorbs landing).
    Total system: the clean and jerk is not the sum of its parts — the transition from
    clean rack to jerk dip requires resetting bracing and position under fatigue.
  source: "geisler_2023 / garhammer_1993 / kawamori_2005"

injury_risk:
  joint_stress:
    wrist: high
    shoulder: high
    lower_back: moderate
    knee: moderate
  common_injuries:
    - structure: wrist_extensors
      mechanism: forced_extension_on_clean_catch
      risk_factors: [insufficient_shoulder_er, poor_front_rack_mobility, heavy_load]
    - structure: rotator_cuff
      mechanism: eccentric_overload_at_jerk_catch
      risk_factors: [insufficient_overhead_shoulder_flexion, fatigue_from_preceding_clean]
    - structure: lumbar_disc
      mechanism: shear_under_load
      risk_factors: [bar_drifting_away_from_body_during_pull, poor_bracing]
    - structure: knee
      mechanism: valgus_in_front_squat_recovery
      risk_factors: [fatigue, restricted_ankle_dorsiflexion, weak_hip_abductors]
  notes: "The transition from clean to jerk is a distinct injury window: the lifter must re-brace and stabilise the front rack under fatigue before initiating the jerk dip. Rushing this transition with unstable position is a common cause of failed attempts and shoulder injuries."
  contraindications:
    - acute_wrist_injury
    - acute_shoulder_injury
    - lumbar_herniation

variations: [power_clean]
progressions: [power_clean, front_squat]
alternatives: [power_clean]

sources:
  - source_id: geisler_2023
    title: "Effects of Expertise on Muscle Activity during the Hang Power Clean and Hang Power Snatch Compared to Snatch and Clean Pulls"
    author: "Geisler S et al."
    year: 2023
    doi: "10.52082/jssm.2023.778"
    credibility: rct
  - source_id: kawamori_2005
    title: "Comparisons of Peak Ground Reaction Force and Rate of Force Development During Variations of the Power Clean"
    author: "Kawamori N et al."
    year: 2005
    doi: "10.1519/00124278-200508000-00011"
    credibility: rct
  - source_id: garhammer_1993
    title: "A Review of Power Output Studies of Olympic and Powerlifting: Methodology, Performance Prediction, and Evaluation Tests"
    author: "Garhammer, J."
    year: 1993
    doi: "10.1519/1533-4287(1993)007<0076:AROPOS>2.3.CO;2"
    credibility: literature_review
  - source_id: nasm_2020
    title: "NASM Optimum Performance Training"
    author: "National Academy of Sports Medicine"
    year: 2020
    credibility: expert_consensus
  - source_id: everett_weightlifting
    title: "Olympic Weightlifting: A Complete Guide for Athletes & Coaches"
    author: "Greg Everett"
    year: 2016
    doi: null
    credibility: practitioner
---

# Clean and Jerk

The clean and jerk is the second of the two Olympic competition lifts and produces the highest absolute loads of any barbell movement in competitive sport. It consists of two distinct sub-movements: the clean (pulling the barbell from the floor to the front-rack position on the shoulders, received in a full front squat) and the jerk (driving the bar from the front rack to full overhead lockout). World records exceed 265 kg. Because the jerk uses leg drive to initiate the overhead press, the clean-and-jerk can be loaded substantially heavier than a strict overhead press — typically 40–50% more.

## Execution

### Phase 1: The Clean

1. **Setup:** Feet hip-width, bar over mid-foot. Narrow clean grip just outside the hips. Hips below shoulders, shoulders over bar. Neutral spine, 120° hip flexion.
2. **First pull (floor to knee):** Extend hips and knees simultaneously while maintaining back angle. Bar tracks against the shins.
3. **Transition:** As bar passes the knees, knees re-bend and hips push forward; torso rises.
4. **Second pull (triple extension):** Explosive hip, knee, and ankle extension; shrug at peak. Full extension, slightly posterior lean.
5. **Third pull / elbow turnover:** Pull elbows under the bar rapidly; receive in front-rack — elbows high and parallel, bar on anterior deltoids. Descend into a full front squat.
6. **Front squat recovery:** Drive through the floor to standing while maintaining upright torso and elbows up.

### Phase 2: The Jerk

7. **Dip:** With the bar in the front rack and core braced, flex knees ~10–15° in a controlled descent; hips stay directly under the bar (do not push backward).
8. **Drive:** Reverse direction explosively — maximal triple extension. The bar leaves the shoulders driven by leg power.
9. **Split receive:** As the bar rises, split the feet (one forward, one back) and lock the arms overhead simultaneously. Bar must be over midfoot with elbows fully extended before the feet land.
10. **Recovery:** Bring the front foot back, then the rear foot forward until feet are level; the bar stays locked overhead.
11. Lower the bar under control.

## Clean Phase EMG

The clean pull phase is dominated by vastus lateralis and gluteus maximus. Elite athletes at 50% 1RM show VL 324% MVIC and GM 299% MVIC (Geisler 2023, Hang Power Clean proxy). These supramaximal values reflect the explosive motor unit synchronisation of experienced weightlifters — not greater absolute force but faster recruitment.

VL and GM activation at elite level plateaus from 70–90% 1RM (249–307% VL range), consistent with power_clean data: the pull mechanism reaches near-ceiling activation at moderate relative loads, and heavier absolute loads require more time-under-tension rather than greater peak activation.

The full clean front squat recovery adds quadriceps and gluteus maximus demand for the ascending portion from a ~130° knee flexion position — this is not captured in the pull-phase EMG values.

## Jerk Phase: Power Output

The jerk produces the highest instantaneous power output in the clean-and-jerk sequence. Garhammer (1993) estimated system peak power during the jerk at 35–50 W/kg bodyweight in elite lifters, driven by the brief but maximal leg drive. The jerk's GRF profile shows a sharp impulse peak (2.5–3.0×BW) during the drive, substantially above the clean's second pull peak, because the knee range is shorter and the bar is already at shoulder height (zero pull height required).

## The Clean-to-Jerk Transition

The transition is a frequently under-trained phase. After a maximal clean, the lifter must:
1. Stand with the bar in front rack under fatigue
2. Re-establish foot position and brace
3. Execute a precisely timed dip-drive

Rushing this sequence while the core is compromised by the preceding clean is a primary cause of failed jerks and shoulder injuries. Advanced programming dedicates specific work to this transition (e.g., pause clean and jerks, clean + 3-second pause + jerk).

## Load Relationship: Why C&J > Snatch

Across elite athletes, clean-and-jerk 1RM is consistently ~135–158% of snatch 1RM. The snatch requires bar velocity sufficient to reach full overhead height from the floor in one motion; the clean only needs the bar to reach shoulder height, and the jerk's leg drive provides the remaining overhead energy. This mechanical advantage — splitting the lift into two sub-movements — allows substantially higher total loads.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/clean_pull.md -->

---
id: clean_pull
name: Clean Pull
status: complete
category: exercise
pattern: [hinge]
equipment: [barbell]

difficulty:
  technical_complexity: 4
  strength_prerequisite: 3
  mobility_prerequisite: 3

muscles:
  - id: vastus_lateralis
    role: primary
  - id: gluteus_maximus
    role: primary
  - id: erector_spinae
    role: primary
  - id: multifidus
    role: primary
  - id: trap_upper
    role: primary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: rectus_femoris
    role: secondary
  - id: vastus_medialis
    role: secondary
  - id: gastrocnemius
    role: secondary
  - id: soleus
    role: secondary
  - id: forearm_flexors
    role: stabilizer

# Geisler 2023: Hang Clean Pull (HCP) across three expertise levels and three loads.
# %MVIC values, pull phase. No catch phase — all motor drive directed into shrug terminal.
# Elite TZ activation significantly greater in clean pull than power clean at 50–70% 1RM
# (p < 0.05, Hedges' g = 0.61–1.08); specific %MVIC values not tabulated in Geisler 2023.
muscle_activation_studies:
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 50
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 152.72, sd: 70.36}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 81.67,  sd: 27.32}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 70
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 213.18, sd: 111.04}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 118.62, sd: null}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 90
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 225.98, sd: 201.09}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 10
    population: "advanced"
    condition:
      load_pct_1rm: 50
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 195.47, sd: 165.81}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 90.53,  sd: 52.44}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 10
    population: "advanced"
    condition:
      load_pct_1rm: 70
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 215.58, sd: 189.90}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 109.90, sd: null}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 10
    population: "advanced"
    condition:
      load_pct_1rm: 90
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 273.86, sd: 271.11}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 50
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 239.40, sd: 86.53}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 258.65, sd: 258.35}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 70
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 279.38, sd: 138.83}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 228.31, sd: null}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 90
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 311.81, sd: 271.74}

joint_rom_required:
  hip_flexion_deg: 120
  notes: "Setup: 120° hip flexion. No catch — terminates at full triple extension with shrug."
  source: "nasm_2020 / geisler_2023"

strength_curve:
  type: bell_shaped
  sticking_point: first_pull_to_transition
  peak_force_position: second_pull
  notes: >
    Midthigh (hang) start: peak GRF 2880±482 N, instantaneous RFD 15321±3533 N/s —
    significantly greater than floor-start power clean (2306±388 N; 8840±2940 N/s).
    Removing the catch phase directs terminal motor drive entirely into shoulder elevation,
    producing superior upper trapezius stimulus vs the power clean at submaximal loads
    (elite, p < 0.05, Hedges' g = 0.61–1.08).
    Can be loaded at 100–110%+ of power clean 1RM as an overload tool.
  source: "kawamori_2005 / geisler_2023"

injury_risk:
  joint_stress:
    lower_back: moderate
    knee: low
  common_injuries:
    - structure: lumbar_disc
      mechanism: shear_under_load
      risk_factors: [bar_drifting_away_from_body, poor_bracing]
  contraindications:
    - acute_lumbar_injury

variations: [power_clean]
progressions: []
alternatives: [snatch_pull]

sources:
  - source_id: geisler_2023
    title: "Effects of Expertise on Muscle Activity during the Hang Power Clean and Hang Power Snatch Compared to Snatch and Clean Pulls"
    author: "Geisler S et al."
    year: 2023
    doi: "10.52082/jssm.2023.778"
    credibility: rct
  - source_id: kawamori_2005
    title: "Comparisons of Peak Ground Reaction Force and Rate of Force Development During Variations of the Power Clean"
    author: "Kawamori N et al."
    year: 2005
    doi: "10.1519/00124278-200508000-00011"
    credibility: rct
  - source_id: nasm_2020
    title: "NASM Optimum Performance Training"
    author: "National Academy of Sports Medicine"
    year: 2020
    credibility: expert_consensus
---

# Clean Pull

The clean pull is an Olympic weightlifting derivative in which the barbell is pulled from the floor through a full triple extension (hip, knee, ankle) with a terminal shrug, but without the catch phase of the power clean or clean. It trains the pulling mechanics of the clean with reduced technical demand and the ability to exceed the athlete's catching 1RM.

## Execution

1. **Setup:** Identical to the clean — feet hip-width, bar over mid-foot, 120° hip flexion, neutral spine, elbows fully extended, hook grip just outside knees.
2. **First pull (floor to knee):** Drive hips and knees simultaneously; maintain constant back angle. Bar stays close to the shins.
3. **Transition:** As bar passes the knees, knees re-bend and hips push forward.
4. **Second pull (triple extension):** Explosive simultaneous hip, knee, and ankle extension drives the bar vertically. Shrug the shoulders at full extension without flexing the elbows.
5. **Termination:** Movement ends at peak shrug height — no arm pull, no catch. Lower the bar to the floor under control.

## What the EMG Data Shows

Vastus lateralis (VL) and gluteus maximus (GM) are the primary pull-phase movers, with activation profiles nearly identical to the power clean at equivalent relative loads. At elite level and 70% 1RM: VL 279% MVIC, GM 228% MVIC.

The key differentiation from the power clean is the upper trapezius. Removing the catch phase allows the athlete to direct peak motor drive entirely into the terminal shrug: at submaximal loads (50–70% 1RM), elite weightlifters show significantly greater upper trapezius activity during the clean pull versus the power clean (p < 0.05, Hedges' g = 0.61–1.08, Geisler 2023).

The midthigh hang variation produces substantially higher peak GRF (2880 vs 2306 N) and RFD (15321 vs 8840 N/s) than the floor-start power clean, confirming its utility as a pure power development overload tool.

## Programming Notes

The clean pull can be loaded at 100–110% of the power clean 1RM. This makes it the primary overload tool in the Olympic lifting system for athletes who cannot increase their catch capacity but need to continue developing triple-extension power. For athletes with restricted front-rack mobility, the clean pull delivers an equivalent lower-body stimulus without the wrist, elbow, and shoulder demands of the catch.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Hang clean pull | Starts from mid-thigh | Higher peak RFD; simplified first pull |
| Power clean | Adds front-rack catch | Complete lift; catch-position conditioning |
| Snatch pull | Wide snatch grip | Snatch-specific pulling pattern |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/close_grip_barbell_bench_press.md -->

---
id: close_grip_barbell_bench_press
name: Close-Grip Barbell Bench Press
status: complete
category: exercise
pattern: [horizontal_push]
equipment: [barbell]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 1

muscles:
  - id: triceps_brachii
    role: primary
  - id: pec_major_clavicular
    role: secondary
  - id: pec_major_sternal
    role: secondary
  - id: deltoid_anterior
    role: secondary

# ebd_2026 literature compilation.
# Condition 1: triceps at 50% BAD grip — submaximal load comparison (narrow vs wide grip).
#   Absolute value (16%) reflects specific load condition, not maximal effort test.
# Condition 2: triceps lateral head at 95% 1RM — peak activation during high-intensity lockout.
# Sternal pectoralis: qualitative only (decreased vs wide grip).
muscle_activation_studies:
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      grip_width: "50% biacromial distance (BAD)"
      notes: "Relative comparison — specific load not reported; submaximal condition"
    measurements:
      - {muscle: triceps_brachii,   mean_pct_mvc: 16,   sd: null, notes: "vs 12% MVIC at 150% BAD standard grip — 33% greater at narrow grip"}
      - {muscle: pec_major_sternal, mean_pct_mvc: null, sd: null, notes: "Decreased vs wider grip variations"}
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      grip_width: "standard close grip (~95% BAD)"
      load_pct_1rm: 95
    measurements:
      - {muscle: triceps_lateral, mean_pct_mvc: 120, sd: null, notes: "Peak activation during high-intensity lockout; lateral head dominates at terminal elbow extension"}

joint_rom_required:
  elbow_flexion_deg: 90
  shoulder_extension_deg: null
  notes: >
    Elbows tucked close to the sides (~30° angle relative to torso) throughout.
    Bar contacts near the base of the sternum (lower than standard bench press).
    Grip width ~95% of biacromial distance — approximately 10–16 inches for most lifters.
  source: "ebd_2026"

strength_curve:
  type: ascending
  sticking_point: mid_range
  peak_force_position: lockout
  notes: >
    Sticking point occurs mid-range at the shoulder-to-triceps transition phase.
    The greater ROM vs wide-grip bench press extends time under tension. The mechanical
    advantage shifts heavily to the triceps in the final third — making this the premier
    barbell exercise for overcoming terminal lockout weakness.
  source: "ebd_2026"

injury_risk:
  joint_stress:
    wrist: moderate
    elbow: moderate
    shoulder: low
  common_injuries:
    - structure: wrist_extensor_tendons
      mechanism: ulnar_deviation_stress_from_narrow_grip
      risk_factors: [excessively_narrow_grip_under_shoulder_width, heavy_loads, elbow_flare]
    - structure: medial_elbow_common_flexor_tendon
      mechanism: valgus_stress_from_narrow_grip
      risk_factors: [heavy_loads, high_frequency, insufficient_recovery]
  contraindications:
    - acute_wrist_tendinopathy
    - medial_epicondylitis_acute
    - distal_biceps_tendon_pathology

variations: []
progressions: []
alternatives: []

sources:
  - source_id: ebd_2026
    title: "Exercise Biomechanics Data Extraction: Upper Push Accessories"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Close-Grip Barbell Bench Press

The close-grip barbell bench press is a flat pressing variation with a narrow hand placement — typically 95% of biacromial distance (BAD), or roughly 10–16 inches of separation for most lifters. Narrowing the grip reduces the moment arm at the sternum while increasing the sagittal-plane moment arm at the elbow, redistributing load away from the sternal pec head and onto the triceps brachii, anterior deltoid, and clavicular pec head.

## Execution

1. Lie on a flat bench; grip the bar at approximately 95% of shoulder width, wrists neutral
2. Unrack the bar at full arm extension; position it over the mid-chest
3. Lower the bar under control, keeping the elbows tucked tight to the sides (~30° from torso)
4. Touch the lower sternum lightly; drive the bar upward through full elbow extension
5. Do not narrow the grip further than shoulder width — this increases wrist stress without further triceps benefit

## What the EMG Data Shows

The close-grip bench press data from ebd_2026 documents a relative comparison rather than absolute peak values at a standardized load.

**Grip width effect on triceps**: A 50% BAD grip (very narrow, approximately 5–8 inches) produces 16% MVIC in the triceps brachii vs 12% MVIC at a 150% BAD standard grip — a 33% relative increase. These values reflect a submaximal load condition; the study documents the directional difference, not maximal effort activation.

**High-intensity lockout**: At 95% of 1RM with a standard close grip, the lateral head of the triceps reaches 120% MVIC at terminal elbow extension. This confirms the close-grip press as a highly effective triceps overload tool at near-maximal loads — particularly for the lateral head which dominates lockout mechanics.

**Sternal pectoralis**: Activation decreases vs wider grip variations. This is expected biomechanically — the narrow grip reduces the horizontal adduction component of the movement, diminishing sternal head demand.

## Why Close-Grip for Triceps

The close-grip press succeeds at triceps isolation for a structural reason: the narrow grip forces the elbows into a more sagittal plane, extending the range of elbow motion and lengthening the time the triceps is under concentric load. Combined with the higher load capacity of the barbell format, this produces a mechanical overload the triceps cannot achieve in isolation exercises at equivalent absolute loads.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Standard bench press | Wide grip; greater pec demand | Overall pressing strength |
| Triceps pushdown | Isolation; constant cable tension | Pump work; high-rep triceps volume |
| Floor press (close grip) | Limited ROM; no shoulder extension | Lockout-specific triceps overload |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/concentration_curls.md -->

---
id: concentration_curls
name: Concentration Curls
status: complete
category: exercise
pattern: [isolation]
equipment: [dumbbell]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: biceps_brachii
    role: primary
  - id: brachialis
    role: secondary

# porcari_2014 (n=16): biceps_brachii 97.9% MVIC — highest of all curl variations tested.
# The braced elbow position eliminates momentum and anterior deltoid contribution.
muscle_activation_studies:
  - source_id: porcari_2014
    doi: null
    n: 16
    population: "healthy adults, standardized load"
    condition:
      implement: dumbbell
      phase: full_rep
      notes: "Elbow braced against inner thigh"
    measurements:
      - {muscle: biceps_brachii, mean_pct_mvc: 97.9, sd: null}

joint_rom_required:
  elbow_flexion_deg: 145
  shoulder_flexion_deg: 30
  source: "Porcari 2014 protocol"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped; bracing the elbow against the thigh eliminates momentum but does not fundamentally alter the moment arm profile"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    wrist: low
  common_injuries:
    - structure: distal_biceps_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, grip_too_heavy]
  contraindications:
    - acute_distal_biceps_tendinopathy

variations: []
progressions: []
alternatives: [dumbbell_bicep_curl, preacher_curl]

sources:
  - source_id: porcari_2014
    title: "ACE-Sponsored Research: Best Biceps Exercises"
    author: "Porcari, John P. et al. (ACE)"
    year: 2014
    doi: null
    credibility: rct
---

# Concentration Curls

The concentration curl produces the highest biceps brachii activation of all curl variations in the ACE-commissioned Porcari 2014 study (97.9% MVIC), outperforming the barbell curl (76.5%), EZ-bar curl (75.4%), and incline dumbbell curl (77.5%). The seated position with the elbow braced against the inner thigh forces the biceps to produce the entire curl force without contributions from the anterior deltoid, upper body swing, or gravity-assisted momentum.

## Execution

1. Sit at the end of a bench with the legs spread; hold a dumbbell in one hand
2. Lean forward and brace the back of the working upper arm against the inner thigh, near the knee
3. Curl the dumbbell upward while supinating the wrist; the elbow stays fixed against the thigh
4. At the top, fully supinate and contract; lower under control through the full eccentric
5. Complete all reps for one arm, then switch

## Why Concentration Curls Produce Highest Activation

The braced elbow eliminates three compensation patterns that reduce effective biceps work in free-standing curls:
1. **Anterior deltoid swing** — the shoulder cannot flex to assist the curl when the upper arm is pinned
2. **Momentum** — no swing available; all force must come from elbow flexion
3. **Bilateral assistance** — the unilateral load prevents the stronger arm from compensating

The combination produces a purer biceps stimulus. The trade-off is that load is limited by the single-arm position and the inability to use controlled momentum at the sticking point.

## ROM Note

ROM approximates the barbell curl (144.6°) because elbow flexion range is not constrained by the thigh position. The shoulder is flexed approximately 30° by the lean-forward posture, which places the biceps long head in a slightly shorter length than an incline curl but longer than a preacher curl.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/conventional_deadlift.md -->

---
id: conventional_deadlift
name: Conventional Deadlift
status: complete
aliases: [Deadlift]
category: exercise
pattern: [hinge]
muscles:
  - id: gluteus_maximus
    role: primary
  - id: biceps_femoris
    role: primary
  - id: semitendinosus
    role: primary
  - id: erector_spinae
    role: primary
  - id: latissimus_dorsi
    role: secondary
  - id: trapezius
    role: secondary
  - id: forearm_flexors
    role: secondary
  - id: rectus_femoris
    role: secondary
  - id: vastus_lateralis
    role: secondary
  - id: vastus_medialis
    role: secondary
equipment: [barbell]
difficulty: intermediate
variations: []
alternatives: []
muscle_activation_studies:
  - source_id: diamant_2021
    doi: null
    n: 15
    population: "trained males"
    condition:
      phase: concentric
      style: bilateral_barbell
    measurements:
      - {muscle: gluteus_maximus,  mean_pct_mvc: 85.70, sd: 29.20}
      - {muscle: biceps_femoris,   mean_pct_mvc: 74.20, sd: 28.80}
      - {muscle: erector_spinae,   mean_pct_mvc: 79.10, sd: 22.10}
  - source_id: diamant_2021
    n: 15
    population: "trained males"
    condition:
      phase: eccentric
      style: bilateral_barbell
    measurements:
      - {muscle: gluteus_maximus, mean_pct_mvc: 28.70, sd: 9.80}
      - {muscle: biceps_femoris,  mean_pct_mvc: 37.30, sd: 18.10}
      - {muscle: erector_spinae,  mean_pct_mvc: 64.00, sd: 16.80}
  - source_id: escamilla_2002
    doi: null
    n: null
    population: "trained lifters"
    condition:
      load_pct_1rm: 100
      phase: full_rep
    measurements:
      - {muscle: gluteus_maximus, mean_pct_mvc: 35.00, sd: 27.00}
      - {muscle: biceps_femoris,  mean_pct_mvc: 28.00, sd: 19.00}
      - {muscle: semitendinosus,  mean_pct_mvc: 27.00, sd: 23.00}

joint_rom_required:
  hip_flexion_setup_deg: 112
  knee_flexion_setup_deg: 135
  ankle_dorsiflexion_phase1_deg: 12.8
  notes: "Hip 100-125° and knee 120-150° at setup; both reach 180° at lockout; conventional requires greater ankle dorsiflexion in phase 1 (floor to knee) than sumo"
  source: "Conventional vs. Sumo Deadlift Kinematics"

strength_curve:
  type: ascending
  sticking_point: two_points
  peak_force_position: lockout
  notes: "Sticking point 1: off the floor (insufficient quad drive or lats/core tension, hips rise early); sticking point 2: at or just below knee (glute and erector weakness, lost momentum)"
  source: "Deadlift Movement Analysis; Westside Barbell Sticking Points"

sources:
  - title: "Starting Strength"
    author: "Mark Rippetoe"
    credibility: practitioner
  - title: "Bilateral vs. unilateral deadlift: EMG analysis"
    author: "Diamant, W., et al."
    year: 2021
    doi: null
    credibility: rct
  - title: "Biomechanics of the conventional and sumo deadlift"
    author: "Escamilla, R. F., et al."
    year: 2002
    doi: null
    credibility: rct
---

# Conventional Deadlift

The conventional deadlift is a hip-hinge movement lifting a barbell from the floor to a standing lockout with a hip-width stance and hands outside the knees. It is one of the three powerlifting competition lifts.

## Execution

1. Stand with mid-foot under the bar, hip-width stance
2. Hinge to grip the bar just outside the knees, shins to the bar
3. Set a flat back, brace, and take the slack out of the bar
4. Drive the floor away, keeping the bar against the legs
5. Lock out by extending the hips, then lower under control

## Common Faults

- **Rounding the lower back** — high injury risk; set and keep a neutral spine
- **Bar drifting forward** — increases the moment arm and stresses the back
- **Hips shooting up early** — turns the pull into a stiff-legged lift

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Sumo | Wide stance, hands inside knees | Shorter range, upright torso |
| Deficit | Standing on a platform | Off-the-floor strength |
| Romanian | Top-down, minimal knee bend | Hamstring hypertrophy |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/decline_dumbbell_flyes.md -->

---
id: decline_dumbbell_flyes
name: Decline Dumbbell Flyes
status: complete
source: free-exercise-db
category: exercise
pattern:
- isolation
equipment:
- dumbbell
difficulty:
  technical_complexity: null
  strength_prerequisite: null
  mobility_prerequisite: null
muscles:
- id: pectoralis_major
  role: primary

muscle_activation_studies: []

joint_rom_required:
  shoulder_horizontal_adduction_deg: 90
  elbow_flexion_deg: 15
  source: "Squatwolf"

strength_curve:
  type: descending
  sticking_point: bottom_third
  peak_force_position: bottom
  notes: "Horizontal moment arm decreases as arms adduct toward midline; tension drops to near zero at vertical lockout"

variations: []
progressions: []
alternatives: []
sources:
- title: free-exercise-db
  author: yuhonas (Public Domain)
  credibility: anecdotal
---

# Decline Dumbbell Flyes

## Execution

1. Secure your legs at the end of the decline bench and lie down with a dumbbell on each
   hand on top of your thighs. The palms of your hand will be facing each other.
2. Once you are laying down, move the dumbbells in front of you at shoulder width. The
   palms of the hands should be facing each other and the arms should be perpendicular
   to the floor and fully extended. This will be your starting position.
3. With a slight bend on your elbows in order to prevent stress at the biceps tendon, lower
   your arms out at both sides in a wide arc until you feel a stretch on your chest.
   Breathe in as you perform this portion of the movement. Tip: Keep in mind that
   throughout the movement, the arms should remain stationary; the movement should only
   occur at the shoulder joint.
4. Return your arms back to the starting position as you squeeze your chest muscles and
   breathe out. Tip: Make sure to use the same arc of motion used to lower the weights.
5. Hold for a second at the contracted position and repeat the movement for the prescribed
   amount of repetitions.


---

<!-- FILE: exercises/decline_ez_bar_triceps_extension.md -->

---
id: decline_ez_bar_triceps_extension
name: Decline EZ-Bar Triceps Extension
status: complete
category: exercise
pattern: [isolation]
equipment: [ez_bar, bench]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 1

muscles:
  - id: triceps_long
    role: primary
  - id: triceps_lateral
    role: primary
  - id: triceps_medial
    role: secondary

muscle_activation_studies:
  - source_id: boehler_2011
    doi: null
    n: 15
    population: "healthy female volunteers, 20-24 yr"
    condition:
      load_pct_1rm: null
      implement: "barbell"
      phase: dynamic
      notes: "Tested as flat 'lying barbell extensions' (skull crusher); decline variant not specifically measured. Values are relative to triangle push-up = 100%, NOT true %MVIC. Long head 70% (SD 20.9), lateral head 55% (SD 14.1) of reference."
    measurements:
      - muscle: triceps_long
        mean_pct_mvc: null
        sd: null
      - muscle: triceps_lateral
        mean_pct_mvc: null
        sd: null
      - muscle: triceps_medial
        mean_pct_mvc: null
        sd: null

joint_rom_required:
  elbow_flexion_deg: 130
  shoulder_extension_deg: 10
  source: "biomechanical inference"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped similar to flat skullcrusher; decline angle shifts gravity moment arm distribution slightly"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: moderate
    shoulder: low
  common_injuries:
    - structure: distal_triceps_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, heavy_load, bouncing_at_bottom]
  contraindications:
    - acute_triceps_tendinopathy
    - blood_pressure_contraindicated_for_inverted_positions

variations: []
progressions: []
alternatives: [ez_bar_skullcrusher, lying_triceps_press]

sources:
  - title: "ACE-sponsored research: Best triceps exercises"
    author: "Boehler, B. et al."
    year: 2011
    doi: null
    source_id: boehler_2011
    credibility: practitioner
---

# Decline EZ-Bar Triceps Extension

The decline EZ-bar triceps extension is performed on a decline bench with the feet secured, performing elbow extension against the EZ-bar's load. The decline angle (typically 15–30°) creates a shoulder position in slight extension, which places the triceps long head in a slightly more elongated position than the flat skullcrusher while still performing the same elbow extension movement pattern.

## Execution

1. Secure the feet at the high end of a decline bench; lie back with the head at the lower end
2. Hold the EZ-bar with close grip, arms extended perpendicular to the torso
3. Lower the bar by bending only the elbows, allowing the bar to approach the forehead
4. Extend the elbows to return; keep the upper arms stationary throughout

## Mechanical Difference from Flat Skullcrusher

On a flat bench, the shoulder is at approximately 90° flexion when the arms are extended overhead. On a decline bench:
- The legs are elevated, tilting the body so the head is lower than the hips
- In the arms-extended starting position, the shoulders are in slight extension relative to the torso axis
- This extends the long head's proximal length slightly beyond the flat variation

The practical effect is a modest increase in long head tension through the range. The decline extension is primarily useful for lifters who find the decline position more comfortable for their elbows or who want a slight variation in stimulus.

## Safety Note

The inverted position of a decline bench slightly increases intracranial pressure. Trainees with blood pressure conditions should consult a physician before using decline variations. Use a spotter for the bar due to the awkward loading position.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/donkey_calf_raises.md -->

---
id: donkey_calf_raises
name: Donkey Calf Raises
status: complete
category: exercise
pattern: [isolation]
equipment: [machine]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 2

muscles:
  - id: gastrocnemius_medial
    role: primary
  - id: gastrocnemius_lateral
    role: primary
  - id: soleus
    role: secondary

# No peer-reviewed EMG data found for the donkey calf raise.
# Mechanically: hip ~90° flexion + knee extended → gastrocnemius stretched at BOTH ends.
# Proximal stretch (hip flexion elongates gastrocnemius from above the knee)
# + distal stretch (ankle dorsiflexion) = maximum gastrocnemius length of any calf exercise.
muscle_activation_studies: []

joint_rom_required:
  ankle_plantarflexion_deg: 40
  ankle_dorsiflexion_deg: 20
  hip_flexion_deg: 90
  source: "biomechanical inference"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped similar to standing raise; gastrocnemius starts from a greater elongated length due to hip flexion, providing greater stretch-mediated stimulus than standing raises"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    ankle: low
    knee: low
  common_injuries:
    - structure: achilles_tendon
      mechanism: eccentric_overload
      risk_factors: [excessive_dorsiflexion, rapid_eccentric, pre_existing_achilles_tendinopathy]
    - structure: gastrocnemius_muscle
      mechanism: stretch_overload_at_maximum_length
      risk_factors: [heavy_load_at_maximum_hip_and_ankle_flexion, pre_existing_gastrocnemius_strain]
  contraindications:
    - acute_achilles_tendinopathy
    - gastrocnemius_strain

variations: []
progressions: []
alternatives: [standing_calf_raises, seated_calf_raise]

sources: []
---

# Donkey Calf Raises

The donkey calf raise is performed with the torso bent forward at 90°, placing the hip in approximately 90° flexion while the knees remain extended. This position elongates the gastrocnemius from both ends simultaneously: hip flexion stretches it proximally (above the knee) and ankle dorsiflexion stretches it distally. No other calf exercise achieves this dual-end gastrocnemius stretch, making it the most mechanically favorable exercise for loading the gastrocnemius at its greatest possible length.

## Execution

1. Use a donkey calf raise machine — position the lower back/tailbone under the padded lever; or bend forward 90° at the hips with hands on a fixed support
2. Place the balls of the feet on the platform edge with heels off; keep the knees straight
3. Lower the heels below the platform to the maximum comfortable dorsiflexion
4. Raise the heels to full plantarflexion; hold briefly
5. Lower under full control

## The Dual-Stretch Advantage

The gastrocnemius crosses two joints: the knee and the ankle. In a standard standing raise, only the ankle is loaded in dorsiflexion. In the donkey position:

| Stretch point | Standing raise | Donkey raise |
|--------------|---------------|-------------|
| Proximal (via hip) | None | Hip flexion pulls origin further from calcaneus |
| Distal (via ankle) | Full dorsiflexion | Full dorsiflexion |
| Overall gastrocnemius length | Moderate | Maximum |

Loading muscles at longer lengths provides a greater stimulus for hypertrophy — the theoretical basis for why the donkey raise has historically been preferred by bodybuilders for gastrocnemius development.

## No EMG Data

No quantitative EMG data exists for the donkey calf raise. Expected activation: similar to or greater than standing calf raises for the gastrocnemius medial and lateral heads. The soleus remains secondary due to the extended knee.

## Practical Access

Traditional donkey calf raises require a dedicated machine or a training partner to load the hips. When unavailable, the standing calf raise is the primary gastrocnemius alternative.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/drag_curl.md -->

---
id: drag_curl
name: Drag Curl
status: complete
category: exercise
pattern: [isolation]
equipment: [barbell]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: biceps_brachii
    role: primary
  - id: brachialis
    role: secondary

# No peer-reviewed EMG data found for the drag curl.
# The shoulder extension component and unique bar path are mechanically distinct from standard curls.
muscle_activation_studies: []

joint_rom_required:
  elbow_flexion_deg: 120
  shoulder_extension_deg: 20
  source: "biomechanical inference"

strength_curve:
  type: descending
  sticking_point: bottom_third
  peak_force_position: bottom
  notes: "Easiest at the top due to simultaneous shoulder extension reducing biceps effective length; resistance felt most at the start where shoulder is neutral and elbow begins extending"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    shoulder: low
  common_injuries:
    - structure: biceps_tendon_long_head
      mechanism: repetitive_shoulder_extension
      risk_factors: [excessive_shoulder_extension_range, heavy_load, pre_existing_biceps_tendinopathy]
  contraindications:
    - acute_posterior_shoulder_impingement

variations: []
progressions: []
alternatives: [barbell_curl, dumbbell_bicep_curl]

sources: []
---

# Drag Curl

The drag curl is a barbell curl variation where the bar is kept in contact with the torso throughout the movement. Unlike a standard curl where the bar arcs forward away from the body, the drag curl pulls the bar directly upward while simultaneously pulling the elbows backward. This shoulder extension component fundamentally alters the movement pattern: as the elbows come back, the shoulder extends, which shortens the biceps from the proximal (shoulder) end while the elbow flexion shortens it from the distal end.

## Execution

1. Hold a barbell at the hips with a supinated grip
2. Keep the bar in contact with the torso throughout — do not allow it to swing forward
3. Initiate by pulling the elbows backward while curling the bar upward; the bar should drag up the torso
4. At the top, the elbows will be behind the torso and the bar near the upper abdomen/chest
5. Lower by reversing the path — elbows move forward while extending, bar returns to hips

## The Mechanical Rationale

In a standard curl, the shoulder stays fixed at 0° flexion while the elbow flexes. The biceps shortens only from the distal (elbow) end. In the drag curl:
- The elbows move backward (shoulder extends) while the elbow flexes
- The shoulder extension reduces the effective biceps moment arm at the proximal end
- This allows the elbow to flex to a higher degree without the "finishing" difficulty of a standard curl

The result is a strength curve that shifts load toward the shortened biceps position at the top — the opposite of the lengthened-position emphasis of preacher and incline curls.

## Data Note

No quantitative EMG data exists for the drag curl. The muscle priority assignments and strength curve characterization are based on mechanical analysis of the shoulder extension + elbow flexion coupling. The drag curl is most useful as a variation that provides peak-contraction emphasis for lifters who respond well to that stimulus type, rather than as a primary mass builder.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/dumbbell_bicep_curl.md -->

---
id: dumbbell_bicep_curl
name: Dumbbell Bicep Curl
status: complete
category: exercise
pattern: [isolation]
equipment: [dumbbell]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: biceps_brachii
    role: primary
  - id: brachialis
    role: secondary
  - id: brachioradialis
    role: secondary

# parpa_2025 (n=11): 80% 1RM — biceps_brachii 111.46% ± 26.80% MVIC.
# oliveira_2009: biceps_brachii ~95% MVIC.
# High parpa_2025 value (>100%) reflects normalization artifact at 80% 1RM load;
# absolute values above 100% are methodologically valid (near-max MVIC is not the ceiling for loaded activation).
muscle_activation_studies:
  - source_id: parpa_2025
    doi: null
    n: 11
    population: "resistance-trained adults, 80% 1RM"
    condition:
      load_pct_1rm: 80
      implement: dumbbell
      phase: full_rep
    measurements:
      - {muscle: biceps_brachii, mean_pct_mvc: 111.46, sd: 26.80}
  - source_id: oliveira_2009
    doi: null
    n: null
    population: "general population"
    condition:
      implement: dumbbell
      phase: full_rep
    measurements:
      - {muscle: biceps_brachii, mean_pct_mvc: 95.0, sd: null}

joint_rom_required:
  elbow_flexion_deg: 132
  shoulder_flexion_deg: 0
  source: "Marcolin 2018 analogous data"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped; peak torque at ~90° elbow flexion; allows full forearm supination through the range unlike barbell"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    wrist: low
  common_injuries:
    - structure: distal_biceps_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, excessive_weight, pre_existing_tendinopathy]
  contraindications:
    - acute_distal_biceps_tendinopathy

variations: []
progressions: []
alternatives: [barbell_curl, ez_bar_curl]

sources:
  - source_id: parpa_2025
    title: "Electromyographic comparison of various curl exercises"
    author: "Parpa, Koulla et al."
    year: 2025
    doi: null
    credibility: rct
  - source_id: oliveira_2009
    title: "EMG analysis of biceps brachii in curl variations"
    author: "Oliveira, Leal et al."
    year: 2009
    doi: null
    credibility: rct
---

# Dumbbell Bicep Curl

The dumbbell bicep curl is the unilateral supinating version of the standard curl. Unlike the barbell which fixes wrist position, the dumbbell allows — and encourages — progressive forearm supination through the concentric phase, maximizing the biceps brachii's two mechanical actions simultaneously: elbow flexion and forearm supination. The unilateral format also allows left-right strength imbalances to be identified and addressed.

## Execution

1. Stand with dumbbells at the sides, neutral grip (thumbs forward)
2. As the curl begins, rotate the wrist into full supination (thumb pointing away) as the elbow flexes
3. Continue until the forearm is fully supinated and the dumbbell is at shoulder height
4. Lower under control while pronating back through the eccentric

## What the EMG Data Shows

Parpa 2025 (n=11, 80% 1RM): **111.46% ± 26.80% MVIC**. This value above 100% is methodologically expected at high loads — the MVIC reference is an isometric test that does not cap the maximum achievable EMG amplitude during dynamic loading. Oliveira 2009 reported ~95% MVIC with lighter loads. Both studies confirm very high biceps activation.

The supination component that dumbbells enable is mechanically significant: the biceps brachii has a substantial supination moment at the elbow, meaning that fully supinating through the curl produces greater biceps activation than a neutral or pronated grip.

## Alternating vs Simultaneous

Alternating curls allow each arm to briefly rest and may allow slightly greater peak force per rep. Simultaneous curls maintain bilateral attention and require less time. Both formats produce comparable hypertrophy outcomes; the choice is ergonomic.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Hammer curl | Neutral grip throughout; shifts to brachialis | Brachialis priority |
| Incline dumbbell curl | Shoulder behind body; greater biceps long head stretch | Lengthened-position loading |
| Concentration curl | Arm braced on leg; highest isolation | Peak contraction |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/dumbbell_flyes.md -->

---
id: dumbbell_flyes
name: Dumbbell Flyes
status: complete
source: free-exercise-db
category: exercise
pattern:
- isolation
equipment:
- dumbbell
difficulty:
  technical_complexity: null
  strength_prerequisite: null
  mobility_prerequisite: null
muscles:
- id: pectoralis_major
  role: primary
- id: deltoid_anterior
  role: secondary
muscle_activation_studies:
  - source_id: solstad_2020
    doi: null
    n: 17
    population: "trained males"
    condition:
      load_pct_1rm: null
      implement: dumbbell
      elbow_angle_deg: 15
      phase: concentric
      notes: "Relative comparison only; flat dumbbell fly produced 16% lower pectoralis_major and 25% lower deltoid_anterior vs. barbell bench press (p<0.05). No absolute %MVIC reported."
    measurements:
      - muscle: pectoralis_major
        mean_pct_mvc: null
        sd: null
      - muscle: deltoid_anterior
        mean_pct_mvc: null
        sd: null
      - muscle: biceps_brachii
        mean_pct_mvc: null
        sd: null
  - source_id: botton_2020
    doi: null
    n: 13
    population: "strength-trained men"
    condition:
      load_pct_1rm: 60
      implement: dumbbell
      elbow_angle_deg: 15
      phase: full_rep
    measurements:
      - muscle: deltoid_anterior
        mean_pct_mvc: 18.8
        sd: null
      - muscle: deltoid_lateral
        mean_pct_mvc: 3.4
        sd: null
      - muscle: deltoid_posterior
        mean_pct_mvc: 2.5
        sd: null
  - source_id: tavares_2017
    doi: null
    n: 17
    population: "trained males"
    condition:
      load_pct_1rm: null
      implement: dumbbell
      elbow_angle_deg: 15
      phase: full_rep
      notes: "Relative comparison only; flat fly generated significantly higher pec_major_sternal activation than incline (d=1.07). No absolute %MVIC reported."
    measurements:
      - muscle: pec_major_sternal
        mean_pct_mvc: null
        sd: null

joint_rom_required:
  shoulder_horizontal_adduction_deg: 90
  elbow_flexion_deg: 15
  source: "Reiser 2017"

strength_curve:
  type: descending
  sticking_point: bottom_third
  peak_force_position: bottom
  notes: "Peak force at bottom where moment arm is maximized; tension drops to near zero at vertical lockout"

variations: []
progressions: []
alternatives: []
sources:
- title: "A Comparison of Muscle Activation between Barbell Bench Press and Dumbbell Flyes in Resistance-Trained Males"
  author: "Solstad et al."
  year: 2020
  doi: null
  source_id: solstad_2020
  credibility: rct
- title: "Different Shoulder Exercises Affect the Activation of Deltoid Portions in Resistance-Trained Individuals"
  author: "Botton et al."
  year: 2020
  doi: null
  source_id: botton_2020
  credibility: rct
- title: "Journal of Exercise Physiologyonline — Electromyography of Dumbbell Fly Exercise Using Different Planes and Labile Surfaces"
  author: "Tavares et al."
  year: 2017
  doi: null
  source_id: tavares_2017
  credibility: rct
- title: free-exercise-db
  author: yuhonas (Public Domain)
  credibility: anecdotal
---

# Dumbbell Flyes

## Execution

1. Lie down on a flat bench with a dumbbell on each hand resting on top of your thighs. The
   palms of your hand will be facing each other.
2. Then using your thighs to help raise the dumbbells, lift the dumbbells one at a time so
   you can hold them in front of you at shoulder width with the palms of your hands
   facing each other. Raise the dumbbells up like you're pressing them, but stop and
   hold just before you lock out. This will be your starting position.
3. With a slight bend on your elbows in order to prevent stress at the biceps tendon, lower
   your arms out at both sides in a wide arc until you feel a stretch on your chest.
   Breathe in as you perform this portion of the movement. Tip: Keep in mind that
   throughout the movement, the arms should remain stationary; the movement should only
   occur at the shoulder joint.
4. Return your arms back to the starting position as you squeeze your chest muscles and
   breathe out. Tip: Make sure to use the same arc of motion used to lower the weights.
5. Hold for a second at the contracted position and repeat the movement for the prescribed
   amount of repetitions.


---

<!-- FILE: exercises/ez_bar_curl.md -->

---
id: ez_bar_curl
name: EZ-Bar Curl
status: complete
category: exercise
pattern: [isolation]
equipment: [ez_bar]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: biceps_brachii
    role: primary
  - id: brachialis
    role: secondary
  - id: brachioradialis
    role: secondary

# porcari_2014 (n=16): biceps_brachii 75.4% MVIC.
# ROM: 144.6° elbow flexion — identical to barbell curl.
# EZ-bar places the wrist in ~45° semi-pronation, reducing wrist/forearm stress vs straight bar.
# Activation difference vs barbell curl: only 1.1 percentage points (76.5% vs 75.4%).
muscle_activation_studies:
  - source_id: porcari_2014
    doi: null
    n: 16
    population: "healthy adults, standardized load"
    condition:
      implement: ez_bar
      phase: full_rep
    measurements:
      - {muscle: biceps_brachii, mean_pct_mvc: 75.4, sd: null}

joint_rom_required:
  elbow_flexion_deg: 145
  shoulder_flexion_deg: 0
  source: "Marcolin 2018"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped; identical to barbell curl; semi-pronated grip reduces wrist moment but does not significantly alter elbow flexion moment profile"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    wrist: low
  common_injuries:
    - structure: distal_biceps_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, excessive_weight]
  contraindications:
    - acute_wrist_tendinopathy

variations: []
progressions: []
alternatives: [barbell_curl, dumbbell_bicep_curl]

sources:
  - source_id: porcari_2014
    title: "ACE-Sponsored Research: Best Biceps Exercises"
    author: "Porcari, John P. et al. (ACE)"
    year: 2014
    doi: null
    credibility: rct
---

# EZ-Bar Curl

The EZ-bar curl is the most wrist-friendly barbell curl variation. The curved bar places the hands in a semi-pronated position (~45°), reducing the stress on the wrist and forearm that many lifters experience with a fully supinated straight bar grip. EMG data shows virtually identical biceps brachii activation to the straight barbell curl (75.4% vs 76.5% MVIC), making the EZ-bar a practical substitute for lifters with wrist discomfort during standard barbell curls.

## Execution

1. Grip the inner (closer to center) curves of the EZ-bar; this produces the semi-pronated position that reduces wrist torque
2. Stand with the upper arms close to the torso
3. Curl the bar upward, keeping the upper arms stationary
4. Lower under control; full extension at the bottom is acceptable if the load is appropriate

## The 1.1% Difference

Porcari 2014 found only a 1.1 percentage point difference between the barbell curl (76.5%) and EZ-bar curl (75.4%). This difference is practically meaningless. Lifters who experience discomfort with the straight bar can switch to the EZ-bar without measurable loss of biceps stimulus.

The semi-pronated position does reduce the supination component of the lift, which slightly shifts load from the biceps brachii supination function toward brachialis and brachioradialis. The net effect on hypertrophy is negligible for most practical purposes.

## Inner vs Outer Grip

EZ-bars have two sets of angled grips:
- **Inner (closer to center)**: Semi-pronated, reduced wrist torque — recommended
- **Outer (wider)**: More pronated, increases brachioradialis contribution, harder on the wrists

The inner grip most closely approximates the barbell curl's mechanical effect.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Barbell curl | Full supination; highest biceps activation | Max biceps stimulus |
| Dumbbell curl | Independent supination per arm | Unilateral control |
| EZ-bar preacher curl | Semi-pronated + supported upper arm | Wrist comfort + lengthened load |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/ez_bar_skullcrusher.md -->

---
id: ez_bar_skullcrusher
name: EZ-Bar Skullcrusher
status: complete
category: exercise
pattern: [isolation]
equipment: [ez_bar, bench]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 1

muscles:
  - id: triceps_long
    role: primary
  - id: triceps_lateral
    role: primary
  - id: triceps_medial
    role: secondary

# brettler_2023 (n=8): TRUE %MVIC — triceps (combined) 23.79% ± 9.19% at 65% 1RM.
# boehler_2011 (normalized to triangle push-up, NOT true %MVIC):
#   triceps_long 70% ± 20.9%, triceps_lateral 55% ± 14.1%.
# The boehler_2011 values are comparative within that study only.
muscle_activation_studies:
  - source_id: brettler_2023
    doi: null
    n: 8
    population: "trained adults, 65% 1RM"
    condition:
      load_pct_1rm: 65
      implement: ez_bar
      phase: full_rep
      notes: "TRUE %MVIC — NOT normalized to another exercise"
    measurements:
      - {muscle: triceps_long, mean_pct_mvc: 23.79, sd: 9.19}
  - source_id: boehler_2011
    doi: null
    n: null
    population: "healthy adults"
    condition:
      implement: ez_bar
      phase: full_rep
      notes: "Normalized to triangle push-up = 100%, NOT true %MVIC. Values are relative comparisons only."
    measurements:
      - {muscle: triceps_long,    mean_pct_mvc: 70.0, sd: 20.9}
      - {muscle: triceps_lateral, mean_pct_mvc: 55.0, sd: 14.1}

joint_rom_required:
  elbow_flexion_deg: 130
  shoulder_flexion_deg: 90
  source: "boehler_2011"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped; hardest at ~90° elbow flexion where moment arm is maximal"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: moderate
    shoulder: low
  common_injuries:
    - structure: distal_triceps_tendon
      mechanism: eccentric_overload_at_full_flexion
      risk_factors: [rapid_eccentric, dropping_bar, heavy_load, pre_existing_tendinopathy]
    - structure: lateral_epicondyle
      mechanism: valgus_stress
      risk_factors: [wide_grip, elbow_flaring]
  contraindications:
    - acute_triceps_tendinopathy
    - elbow_medial_collateral_ligament_injury

variations: []
progressions: []
alternatives: [lying_triceps_press, cable_lying_triceps_extension]

sources:
  - source_id: brettler_2023
    title: "Electromyographic analysis of triceps exercises at various intensities"
    author: "Brettler, S. et al."
    year: 2023
    doi: null
    credibility: rct
  - source_id: boehler_2011
    title: "An electromyographic analysis of 3 muscles surrounding the elbow joint during a maximally forceful isometric contraction, concentric isotonic contraction, and 6 common exercises"
    author: "Boehler, Breanna et al."
    year: 2011
    doi: null
    credibility: rct
---

# EZ-Bar Skullcrusher

The EZ-bar skullcrusher is performed supine on a bench with the EZ-bar lowered from arms-extended overhead toward the forehead. The fixed shoulder position at ~90° flexion places all three triceps heads in a moderately lengthened position while elbow extension provides the isolated triceps stimulus. The EZ-bar's semi-pronated grip reduces wrist stress compared to a straight bar.

## Execution

1. Lie on a flat bench; hold an EZ-bar with a close grip (inner knurling), arms extended perpendicular to the floor
2. Keep the upper arms vertical and stationary; lower the bar by bending the elbows only
3. Lower until the bar is just above the forehead — the "skull" reference point
4. Extend the elbows to return to the start; keep the upper arms stationary throughout
5. Do not lock out forcefully at the top; maintain muscular tension

## What the EMG Data Shows

Two studies with different normalization methods:

| Study | Measurement | Triceps Long | Triceps Lateral |
|-------|-------------|-------------|-----------------|
| Brettler 2023 | **True %MVIC**, 65% 1RM | 23.79% ± 9.19% | — |
| Boehler 2011 | Normalized (not %MVIC) | 70% ± 20.9% | 55% ± 14.1% |

The Brettler 2023 value (23.79% MVIC) appears low because: (1) the load was 65% 1RM, not maximal; (2) the MVIC reference is an isometric maximal contraction, which produces different neural drive than dynamic lifting. The Boehler 2011 values are relative to the triangle push-up baseline within that study.

## Shoulder Position Comparison

| Exercise | Shoulder | Long Head Length |
|----------|----------|-----------------|
| Skullcrusher | 90° flexion | Mid-range |
| Overhead extension | 180° flexion | Maximum |
| Pushdown | 0° (neutral) | Minimum |

The skullcrusher trains the long head in a mid-length position — more stimulus than a pushdown, less than an overhead extension. For comprehensive triceps development, pair with an overhead variation.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/face_pull.md -->

---
id: face_pull
name: Face Pull
status: complete
category: exercise
pattern: [isolation]
equipment: [cable]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: deltoid_posterior
    role: primary
  - id: infraspinatus
    role: primary
  - id: teres_minor
    role: primary
  - id: trap_middle
    role: secondary
  - id: trap_lower
    role: secondary
  - id: rhomboids
    role: secondary
  - id: supraspinatus
    role: stabilizer

# No peer-reviewed quantitative EMG data found for the face pull.
# Widely used in shoulder health protocols based on posterior cuff anatomy.
# Combination of horizontal abduction + external rotation makes it unique vs other rear delt exercises.
muscle_activation_studies: []

joint_rom_required:
  shoulder_horizontal_abduction_deg: 90
  shoulder_external_rotation_deg: 90
  source: "biomechanical inference"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Cable provides constant tension throughout; peak load at mid-range where both horizontal abduction and external rotation moment arms are maximal"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    shoulder: low
    elbow: low
  common_injuries: []
  contraindications:
    - acute_posterior_shoulder_impingement

variations: []
progressions: []
alternatives: [seated_bent_over_rear_delt_raise, bent_over_dumbbell_rear_delt_raise_with_head_on_bench]

sources: []
---

# Face Pull

The face pull is a cable-based isolation exercise combining shoulder horizontal abduction with external rotation. It is unique among rear deltoid exercises in that it simultaneously loads the infraspinatus, teres minor, and posterior deltoid — the complete posterior rotator cuff and deltoid complex. This combination makes it a cornerstone of shoulder health programming, not merely an aesthetic exercise.

## Execution

1. Set a cable machine pulley to approximately head height; attach a rope
2. Grip the rope with both hands, thumbs facing you, and step back until there is tension on the cable
3. Pull the rope toward the face, splitting the hands apart so each hand moves to the side of the head
4. At the end position, the upper arms should be roughly parallel to the floor, elbows at 90°, with the forearms angled upward — this is the external rotation component
5. Return under control; do not let the cable snap the shoulders forward

## The Dual Movement Pattern

Most posterior shoulder exercises train only horizontal abduction. The face pull adds **external rotation** by ending with the forearms pointing upward. This dual pattern:

1. Loads the infraspinatus and teres minor through their concentric range (external rotation)
2. Loads the posterior deltoid through horizontal abduction
3. Reinforces the upper/lower trap balance needed for scapular upward rotation

This makes the face pull functionally different from the bent-over rear delt raise — the rear delt raise primarily trains horizontal abduction in a fixed sagittal plane, while the face pull adds the external rotation that the rotator cuff needs for shoulder longevity.

## Role in Programming

The face pull is most valuable as a:
- **Shoulder health exercise**: Direct posterior cuff loading that counters the internal rotation bias of pressing movements
- **Scapular stabilizer**: Upper-back retraction and depression training via mid and lower trapezius
- **Volume accumulation**: High rep tolerability (15–30 reps) makes it suitable at the end of upper-body sessions

In programs heavily loaded with pressing volume, the face pull is one of the few exercises addressing the weakness patterns associated with shoulder impingement.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Seated bent-over rear delt raise | Dumbbell; horizontal abduction only | Pure rear delt isolation |
| Band pull-apart | No cable needed; high reps | Shoulder warm-up; travel |
| Cuban rotation | External rotation from 90° abduction | Rotator cuff strengthening |
| Kneeling face pull | Eliminates hip drive | Strict form |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/farmers_walk.md -->

---
id: farmers_walk
name: Farmer's Walk
status: complete
category: exercise
pattern: [carry]
equipment: [farmer handles]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 3
  mobility_prerequisite: 1

muscles:
  - id: forearm_flexors
    role: primary
  - id: trap_upper
    role: primary
  - id: erector_spinae
    role: primary
  - id: rectus_abdominis
    role: secondary
  - id: obliques
    role: secondary
  - id: gluteus_maximus
    role: secondary
  - id: gluteus_medius
    role: secondary
  - id: rectus_femoris
    role: secondary
  - id: vastus_lateralis
    role: secondary
  - id: vastus_medialis
    role: secondary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: multifidus
    role: secondary
  - id: trap_middle
    role: secondary
  - id: gastrocnemius_medial
    role: tertiary
  - id: gastrocnemius_lateral
    role: tertiary
  - id: soleus
    role: tertiary

muscle_activation_studies: []

joint_rom_required:
  hip_flexion_deg: 30
  knee_flexion_deg: 30
  source: "biomechanical inference — minimal ROM; primarily upright gait"

strength_curve:
  type: isometric_hold
  sticking_point: grip_failure
  notes: "Grip is the limiting factor. Trunk and legs work isometrically to maintain posture during locomotion."

injury_risk:
  joint_stress:
    lumbar_spine: low
    grip: moderate
    shoulder: low
  common_injuries:
    - structure: finger_flexor_tendons
      mechanism: grip_overload_during_prolonged_carry
      risk_factors: [excessive_distance, wet_handles, insufficient_grip_training]
    - structure: lumbar_paraspinals
      mechanism: lateral_trunk_sway_under_asymmetric_loading
      risk_factors: [uneven_implements, excessive_load, fatigue]
  contraindications:
    - acute_finger_flexor_tendinopathy
    - acute_lumbar_strain

variations: []
progressions: []
alternatives: [yoke_walk]

sources: []
---

# Farmer's Walk

A loaded carry where the athlete picks up heavy implements (one in each hand) and walks as fast as possible over a set distance. The farmer's walk develops grip strength, trunk stability, and total-body work capacity. Research shows it generates greater vertical ground reaction force than a conventional deadlift (2893 +/- 442 N vs 2679 +/- 471 N) and 13x greater anterior force than a back squat, while actually reducing lumbar shear stress compared to deadlifting due to the more upright torso and shorter moment arm.

## Execution

1. **Setup.** Stand between the implements (farmer handles, heavy dumbbells, or trap bar). Feet hip-width apart, hips hinged, back flat, head neutral.
2. **Pick.** Grip the handles firmly, drive through the heels, and stand tall in one smooth motion. Lock out the hips and set the shoulders — slight scapular depression, chest up.
3. **Walk.** Take short, quick steps. Stride length should be approximately 1.35-1.67 m at competition pace. Keep the torso rigid and avoid lateral sway. Breathe in a braced pattern — short, pressurized breaths.
4. **Turn (if applicable).** Decelerate with shortened steps, pivot with small foot adjustments, and re-accelerate. Turns are where most drops occur.
5. **Set down.** At the finish, hinge the hips and lower the implements under control. Do not release from standing height.

## Programming Note

The farmer's walk is one of the most accessible strongman movements and transfers well to general strength goals (grip, posture, trunk stability). Typical competition distances are 15-25 m (50-75 ft) with near-maximal loads. For conditioning, use moderate loads over longer distances (40-60 m). Grip is almost always the limiting factor; chalk and mixed grip are not used — double overhand is standard on farmer handles. Recovery is moderate (3-5 days) compared to other strongman events.


---

<!-- FILE: exercises/flat_bench_cable_flyes.md -->

---
id: flat_bench_cable_flyes
name: Flat Bench Cable Flyes
status: complete
source: free-exercise-db
category: exercise
pattern:
- isolation
equipment:
- cable
difficulty:
  technical_complexity: null
  strength_prerequisite: null
  mobility_prerequisite: null
muscles:
- id: pectoralis_major
  role: primary

muscle_activation_studies: []

joint_rom_required:
  shoulder_horizontal_adduction_deg: 90
  elbow_flexion_deg: 15
  source: "Legion Athletics"

strength_curve:
  type: flat
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Lateral cable tension provides constant resistance throughout ROM; no drop-off at midline unlike dumbbell variants"

variations: []
progressions: []
alternatives: []
sources:
- title: free-exercise-db
  author: yuhonas (Public Domain)
  credibility: anecdotal
---

# Flat Bench Cable Flyes

## Execution

1. Position a flat bench between two low pulleys so that when you are laying on it, your
   chest will be lined up with the cable pulleys.
2. Lay flat on the bench and keep your feet on the ground.
3. Have someone hand you the handles on each hand. You will grab each single handle
   attachment with a palms up grip.
4. Extend your arms by your side with a slight bend on your elbows. Tip: You will keep this
   bend constant through the whole movement. Your arms should be parallel to the floor.
   This is your starting position.
5. Now start lifting the arms in a semi-circle motion directly in front of you by pulling
   the cables together until both hands meet at the top of the movement. Squeeze your
   chest as you perform this motion and breathe out during this movement. Also, hold the
   contraction for a second at the top. Tip: When performed correctly, at the top
   position of this movement, your arms should be perpendicular to your torso and the
   floor touching above your chest.
6. Slowly come back to the starting position.
7. Repeat for the recommended amount of repetitions.


---

<!-- FILE: exercises/floor_press.md -->

---
id: floor_press
name: Floor Press
status: complete
category: exercise
pattern: [horizontal_push]
equipment: [barbell]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 1

muscles:
  - id: triceps_brachii
    role: primary
  - id: pectoralis_major
    role: secondary
  - id: deltoid_anterior
    role: secondary

# ebd_2026 literature compilation. All activation data is qualitative — no specific
# %MVIC values reported. Relative descriptions preserved as notes.
muscle_activation_studies:
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      surface: floor
      phase: full_rep
    measurements:
      - {muscle: triceps_brachii,  mean_pct_mvc: null, notes: "Dominant throughout; especially high during concentric drive from dead stop with no stretch reflex"}
      - {muscle: pectoralis_major, mean_pct_mvc: null, notes: "Reduced vs full bench press — floor eliminates bottom stretch and stretch-shortening contribution"}
      - {muscle: deltoid_anterior,  mean_pct_mvc: null, notes: "Highly active during initial concentric ascent phase"}

joint_rom_required:
  shoulder_extension_deg: 0
  elbow_flexion_deg: 90
  notes: >
    Shoulder extension strictly limited to 0° — the floor blocks posterior humerus
    travel. Elbow flexion limited to ~90° when upper arms contact the floor. The
    combination eliminates the bottom third of the standard bench press ROM.
  source: "ebd_2026"

strength_curve:
  type: ascending
  sticking_point: bottom
  peak_force_position: lockout
  notes: >
    Sticking point is immediately off the floor — no stretch reflex available.
    All force production is purely concentric. Operates exclusively in the mechanically
    stronger mid-range and lockout portion of the pressing curve. Pause before pressing
    is recommended to fully dissipate stored elastic energy.
  source: "ebd_2026"

injury_risk:
  joint_stress:
    shoulder: low
    elbow: low
    wrist: low
  common_injuries:
    - structure: elbow_soft_tissue
      mechanism: impact
      risk_factors: [slamming_elbows_into_floor, uncontrolled_descent]
    - structure: wrist
      mechanism: hyperextension
      risk_factors: [uncontrolled_bar_drop, excessively_heavy_load]
  contraindications: []

variations: []
progressions: []
alternatives: []

sources:
  - source_id: ebd_2026
    title: "Exercise Biomechanics Data Extraction: Upper Push Accessories"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Floor Press

The floor press is a horizontal pressing variation performed lying supine on the floor rather than on an elevated bench. The floor acts as a hard stop, limiting shoulder extension to 0° (arms parallel to the floor) and restricting elbow flexion to approximately 90° when the upper arms contact the ground. This eliminates the bottom third of the standard bench press range of motion.

## Execution

1. Set J-hooks low in a power rack; lie underneath with the bar above the mid-chest
2. Grip at standard bench press width; keep shoulder blades retracted and depressed against the floor
3. Unrack and begin the descent; lower the bar until the triceps touch the floor — do not bounce
4. Pause for 1 second with full weight suspended; this dissipates elastic energy and converts the lift to pure concentric
5. Drive the bar upward by extending the elbows; keep the bar directly over the mid-chest

## What the Data Shows

The floor press data from ebd_2026 is qualitative — no specific %MVIC values are reported. The key findings are comparative:

**Triceps dominance**: The triceps brachii is the dominant muscle throughout the lift, especially during the concentric drive from the dead-stop position. Because the stretch-shortening cycle is unavailable at the bottom, the triceps cannot rely on elastic energy transfer — all force must come from active contractile effort.

**Reduced pectoralis major**: The floor press structurally prevents the pectoralis major from reaching its fully stretched state at the bottom. This reduces the elastic contribution of the pec and lowers overall pec activation compared to a full-ROM bench press. The floor press is therefore not primarily a chest exercise.

**Anterior deltoid**: Highly active during the initial concentric ascent phase, functioning as a key prime mover alongside the triceps.

## The Design Purpose

The floor press was originally used by powerlifters to address mid-range and lockout weaknesses. By eliminating leg drive and the stretch reflex, it isolates the concentric pressing capacity without the mechanical boost that full bench press technique provides. Bodybuilders use it for elbow-tendon management — the restricted ROM reduces tendon stress at the shoulder while allowing heavy triceps loading.

The floor press is also one of the safest pressing exercises for athletes with shoulder pathology: by restricting extension to 0°, it eliminates the anterior shoulder impingement risk associated with deep shoulder extension in the full bench press.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Dumbbell floor press | Independent arm path; greater ROM flexibility | Unilateral assessment; shoulder management |
| Close-grip floor press | Narrow grip + floor ROM restriction | Maximum triceps overload with minimal shoulder risk |
| Full bench press | Full ROM; stretch reflex available | Primary horizontal pressing development |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/front_cable_raise.md -->

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


---

<!-- FILE: exercises/front_dumbbell_raise.md -->

---
id: front_dumbbell_raise
name: Front Dumbbell Raise
status: complete
category: exercise
pattern: [isolation]
equipment: [dumbbell]

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

# Sweeney 2014 (n=16): 70% 1RM, pronated grip — deltoid_anterior 57% ± 11.9%.
# Demirtas 2023 (n=14): 80% 1RM across three grip conditions.
# Pronated grip: anterior 51.57% concentric. Hammer grip: anterior 43.36%.
# Grip orientation shifts anterior vs posterior delt emphasis significantly.
muscle_activation_studies:
  - source_id: sweeney_2014
    doi: null
    n: 16
    population: "healthy males, 70% 1RM, pronated grip"
    condition:
      load_pct_1rm: 70
      implement: dumbbell
      phase: full_rep
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 57.0, sd: 11.9}
      - {muscle: deltoid_lateral,   mean_pct_mvc: 36.0, sd: 15.5}
      - {muscle: deltoid_posterior, mean_pct_mvc: 9.0,  sd: 5.8}
  - source_id: demirtas_2023
    doi: null
    n: 14
    population: "resistance-trained males, 80% 1RM, pronated grip, concentric"
    condition:
      load_pct_1rm: 80
      implement: dumbbell
      phase: concentric
      notes: "Pronated (overhand) grip — highest anterior delt in concentric phase"
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 51.57, sd: null}
      - {muscle: deltoid_posterior, mean_pct_mvc: 29.43, sd: null}
  - source_id: demirtas_2023
    doi: null
    n: 14
    population: "resistance-trained males, 80% 1RM, hammer grip, concentric"
    condition:
      load_pct_1rm: 80
      implement: dumbbell
      phase: concentric
      notes: "Neutral (hammer) grip — lower anterior delt"
    measurements:
      - {muscle: deltoid_anterior, mean_pct_mvc: 43.36, sd: null}
  - source_id: demirtas_2023
    doi: null
    n: 14
    population: "resistance-trained males, 80% 1RM, supinated grip, concentric"
    condition:
      load_pct_1rm: 80
      implement: dumbbell
      phase: concentric
      notes: "Supinated (underhand) grip"
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 47.00, sd: null}
      - {muscle: deltoid_posterior, mean_pct_mvc: 22.59, sd: null}

joint_rom_required:
  shoulder_flexion_deg: 90
  source: "Sweeney 2014"

strength_curve:
  type: ascending
  sticking_point: top_third
  peak_force_position: top
  notes: "Resistance moment arm is longest and perpendicular to gravity at 90° shoulder flexion — peak load at top of movement"
  source: "Sweeney 2014"

injury_risk:
  joint_stress:
    shoulder: low
    elbow: low
  common_injuries:
    - structure: biceps_tendon_long_head
      mechanism: anterior_shoulder_impingement
      risk_factors: [load_above_90_deg, rapid_eccentric, pre_existing_biceps_tendinopathy]
  contraindications:
    - acute_anterior_shoulder_impingement

variations: []
progressions: []
alternatives: [front_cable_raise]

sources:
  - source_id: sweeney_2014
    title: "Dynamite Delts: ACE Research Identifies Top Shoulder Exercises"
    author: "Sweeney, Samantha; Porcari, John P. et al."
    year: 2014
    doi: null
    credibility: rct
  - source_id: demirtas_2023
    title: "The effects of handgrip and range of motion variations on muscle activity in different deltoid exercises"
    author: "Demirtaş, Barbaros et al."
    year: 2023
    doi: null
    credibility: rct
---

# Front Dumbbell Raise

The front dumbbell raise is a shoulder flexion isolation exercise that targets the anterior deltoid. Unlike the lateral raise, which trains shoulder abduction, the front raise moves the humerus forward in the sagittal plane — the exact mechanical action of the anterior deltoid. Both grip orientation and range of motion significantly affect activation distribution, with the pronated grip producing the highest anterior deltoid values.

## Execution

1. Stand with dumbbells in front of the thighs, pronated grip (thumbs toward each other)
2. Raise one or both arms directly forward to shoulder height (90°) with a slight elbow bend
3. Do not swing or use leg drive — keep the core braced and torso stationary
4. Lower under control without letting the weights drop through the eccentric

## What the EMG Data Shows

**Grip comparison** (Demirtas 2023, n=14, 80% 1RM, concentric phase):

| Grip | Anterior Delt | Notes |
|------|--------------|-------|
| Pronated (overhand) | 51.57% | Highest anterior delt in concentric |
| Supinated (underhand) | 47.00% | Moderate |
| Neutral/Hammer | 43.36% | Lowest anterior |

**Full-rep comparison** (Sweeney 2014, n=16, 70% 1RM, pronated):

| Muscle | Activation |
|--------|-----------|
| Anterior deltoid | 57.0 ± 11.9% |
| Lateral deltoid | 36.0 ± 15.5% |
| Posterior deltoid | 9.0 ± 5.8% |

## Programming Note

The anterior deltoid receives substantial stimulus from all pressing movements (overhead press, incline bench, bench press). In most programs, the front raise adds redundant volume. Include front raises only when anterior delt is deliberately undertrained relative to lateral and posterior heads.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Front cable raise | Constant tension at bottom of range | Lengthened anterior delt load |
| Plate front raise | Fixed pronated grip; heavier load | Load progression |
| Alternating front raise | Unilateral; core anti-rotation demand | Core integration |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/front_squat.md -->

---
id: front_squat
name: Front Squat
status: complete
aliases: [Clean Grip Front Squat]
category: exercise
pattern: [squat]
muscles:
  - id: rectus_femoris
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: vastus_medialis
    role: primary
  - id: gluteus_maximus
    role: primary
  - id: core
    role: secondary
  - id: trapezius
    role: secondary
  - id: rhomboids
    role: secondary
equipment: [barbell, squat rack]
difficulty: intermediate
variations: [back_squat, overhead_squat]
progressions: [goblet_squat]
alternatives: [leg_press]
muscle_activation_studies:
  - source_id: erdag_yavuz_2019
    doi: null
    n: null
    population: "resistance-trained males"
    condition:
      load_pct_1rm: 60
      phase: full_rep
    measurements:
      - {muscle: vastus_medialis,  mean_pct_mvc: 61.6, sd: 18.9}
      - {muscle: vastus_lateralis, mean_pct_mvc: 58.4, sd: 14.1}
      - {muscle: rectus_femoris,   mean_pct_mvc: 36.1, sd: 17.7}
      - {muscle: erector_spinae,   mean_pct_mvc: 36.8, sd: 17.1}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 18.3, sd: 6.7}
      - {muscle: semitendinosus,   mean_pct_mvc: 8.2,  sd: 3.1}
      - {muscle: biceps_femoris,   mean_pct_mvc: 6.8,  sd: 6.7}

joint_rom_required:
  knee_flexion_deg: 130
  hip_flexion_deg: 115
  ankle_dorsiflexion_deg: 18
  source: "Greene 1994; Gullett et al. 2009"

strength_curve:
  type: ascending
  sticking_point: bottom_third
  peak_force_position: lockout
  notes: "Anterior load increases knee flexion moment; sticking point worsens if trapezius/rhomboids fatigue and torso tips forward"
  source: "van den Tillaar & Andersen 2021"

sources:
  - title: "Olympic Weightlifting: A Complete Guide for Athletes & Coaches"
    author: "Greg Everett"
    credibility: practitioner
  - title: "Evaluation of muscle activities during different squat variations using electromyography signals"
    author: "Erdag, D., Yavuz, H. U."
    year: 2019
    doi: null
    credibility: rct
  - title: "A biomechanical comparison of back and front squats in healthy trained individuals"
    author: "Gullett, J. C., Tillman, M. D., Gutierrez, G. M., Chow, J. W."
    year: 2009
    doi: "10.1519/JSC.0b013e3181b83d36"
    credibility: rct
  - title: "Joint range of motion guidelines"
    author: "Greene, W. A."
    year: 1994
    publisher: "American Academy of Orthopaedic Surgeons"
    credibility: expert_consensus
---

# Front Squat

The front squat is a squat pattern with the barbell racked across the front of the shoulders. The front-loaded position forces a more upright torso and shifts emphasis toward the quadriceps and upper-back stability.

## Execution

1. Rack the bar across the front delts, elbows high (clean grip or cross-arm grip)
2. Stance about shoulder width, toes turned out slightly
3. Brace the core and keep the elbows up throughout
4. Descend with an upright torso, knees tracking over the toes
5. Drive up while maintaining the rack position

## Common Faults

- **Dropping the elbows** — collapses the rack and pulls the torso forward
- **Limited wrist or thoracic mobility** — prevents a secure clean grip
- **Heels rising** — usually limited ankle mobility

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Clean grip | Bar held on fingertips, elbows high | Weightlifters |
| Cross-arm grip | Arms crossed over the bar | Limited wrist mobility |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/glute_ham_raise.md -->

---
id: glute_ham_raise
name: Glute Ham Raise
status: complete
category: exercise
pattern: [isolation]
equipment: [machine]

difficulty:
  technical_complexity: 3
  strength_prerequisite: 3
  mobility_prerequisite: 2

muscles:
  - id: biceps_femoris
    role: primary
  - id: semitendinosus
    role: primary
  - id: semimembranosus
    role: primary
  - id: gluteus_maximus
    role: secondary
  - id: gastrocnemius_medial
    role: secondary
  - id: gastrocnemius_lateral
    role: secondary

# ebben_2009: Overall hamstrings 98% MVIC — highest activation of any leg curl variation tested.
# The GHR uniquely loads the hamstrings through BOTH knee flexion AND hip extension simultaneously,
# producing very high force demands on both proximal and distal hamstring attachment points.
muscle_activation_studies:
  - source_id: ebben_2009
    doi: null
    n: null
    population: "healthy adults, glute-ham raise machine"
    condition:
      implement: machine
      phase: full_rep
      notes: "Simultaneous knee flexion and hip extension; highest hamstring demand of any curl variation in this study"
    measurements:
      - {muscle: biceps_femoris, mean_pct_mvc: 98.0, sd: null}

joint_rom_required:
  knee_flexion_deg: 130
  hip_extension_deg: 30
  source: "ebben_2009"

strength_curve:
  type: descending
  sticking_point: bottom_third
  peak_force_position: bottom
  notes: "Descending; hardest at the bottom of the rep (body horizontal, hamstrings maximally loaded through both joints); difficulty is front-loaded"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    knee: moderate
    hip: low
  common_injuries:
    - structure: proximal_hamstring_tendon
      mechanism: eccentric_overload
      risk_factors: [attempting_without_adequate_strength, bodyweight_too_high_for_current_strength]
    - structure: distal_hamstring_tendon
      mechanism: eccentric_overload_at_knee
      risk_factors: [rapid_eccentric, insufficient_warm_up]
  contraindications:
    - acute_proximal_hamstring_tendinopathy
    - acute_posterior_knee_injury
    - insufficient_hamstring_strength_for_bodyweight

variations: []
progressions: []
alternatives: [lying_leg_curls, seated_leg_curl]

sources:
  - source_id: ebben_2009
    title: "Hamstring muscle EMG activity during various weight-bearing exercises"
    author: "Ebben, William P. et al."
    year: 2009
    doi: null
    credibility: rct
---

# Glute Ham Raise

The glute ham raise (GHR) produces the highest hamstring activation of any leg curl variation, approximately 98% MVIC in Ebben 2009. Unlike machine leg curls that load the hamstrings through knee flexion only, the GHR simultaneously demands both knee flexion and hip extension — forcing the hamstrings to contract forcefully across both of their attachment points at once. This dual-joint loading is why the GHR is exceptionally demanding and requires significant base hamstring strength.

## Execution

1. Adjust the GHR machine so the knees sit just behind the round pad, with feet secured against the footplate
2. Begin in the horizontal position (body parallel to the floor) — this is the starting position with hamstrings maximally loaded
3. Flex the knees to pull the body upward toward vertical while maintaining a neutral spine and driving the toes into the footplate
4. At the top, the body is approximately vertical with full knee flexion
5. Lower under complete control — the eccentric is the highest-risk portion

## What the EMG Data Shows

Ebben 2009:

| Exercise | Hamstring activation |
|----------|---------------------|
| GHR | 98% MVIC |
| Seated leg curl | 80.8% MVIC |
| Prone leg curl | 80% MVIC |

The near-maximal activation reflects the simultaneous demand on both the proximal (hip extension) and distal (knee flexion) functions of the hamstrings. No other isolation exercise matches this.

## Why the GHR Is Different from Leg Curls

| Feature | Machine Leg Curl | Glute Ham Raise |
|---------|-----------------|-----------------|
| Hip position | Fixed | Extends during rep |
| Knee flexion | Yes | Yes |
| Hamstring joints loaded | 1 (knee) | 2 (knee + hip) |
| Strength prerequisite | Low | High |

The GHR is appropriate for intermediate-to-advanced trainees with well-developed hamstring strength. Beginners should establish a base with machine leg curls first.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/goblet_squat.md -->

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


---

<!-- FILE: exercises/good_morning.md -->

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


---

<!-- FILE: exercises/hammer_curls.md -->

---
id: hammer_curls
name: Hammer Curls
status: complete
category: exercise
pattern: [isolation]
equipment: [dumbbell]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: brachialis
    role: primary
  - id: brachioradialis
    role: primary
  - id: biceps_brachii
    role: secondary

# jahizi_2023 (n=30): neutral grip — no absolute %MVIC values reported; qualitative analysis only.
# Neutral grip eliminates the supination function of biceps brachii → shifts load to brachialis and brachioradialis.
# ROM: 140° elbow flexion.
muscle_activation_studies:
  - source_id: jahizi_2023
    doi: null
    n: 30
    population: "resistance-trained adults, neutral grip"
    condition:
      implement: dumbbell
      phase: full_rep
      notes: "Neutral (hammer) grip maintained throughout; no forearm supination. No absolute %MVIC values were reported."
    measurements: []

joint_rom_required:
  elbow_flexion_deg: 140
  shoulder_flexion_deg: 0
  source: "jahizi_2023"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped gravity curve similar to supinated curl, but neutral grip distributes load differently across the three elbow flexors"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    wrist: low
  common_injuries:
    - structure: distal_biceps_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, excessive_weight]
  contraindications: []

variations: []
progressions: []
alternatives: [dumbbell_bicep_curl, barbell_curl]

sources:
  - source_id: jahizi_2023
    title: "Electromyographic comparison of biceps curl grip orientations"
    author: "Jahizi, Peyman et al."
    year: 2023
    doi: null
    credibility: rct
---

# Hammer Curls

The hammer curl uses a neutral grip (thumbs up) throughout the entire range of motion, mechanically eliminating the supination function of the biceps brachii. This grip redistributes elbow flexor demand: the brachialis and brachioradialis become primary movers, while biceps brachii contributes as a secondary flexor without its most efficient mechanical advantage. Hammer curls are the primary training stimulus for the brachialis — a muscle that sits under the biceps and contributes to upper arm size regardless of supination capability.

## Execution

1. Stand with dumbbells at the sides in a neutral grip (palms facing each other)
2. Keep the neutral grip throughout the entire movement — do not rotate into supination
3. Curl both dumbbells simultaneously or alternating to shoulder height
4. Lower under control; maintain the neutral wrist position through the eccentric

## The Neutral Grip Mechanics

The biceps brachii is a powerful forearm supinator. In a supinated grip (palms up), the biceps can exert both flexion and supination torque simultaneously, producing high activation. In a neutral grip:

- Supination is eliminated as a mechanical input
- Biceps brachii activation decreases significantly
- Brachialis activation increases (it has no supination function and flexes the elbow regardless of grip)
- Brachioradialis — which prefers a neutral grip — becomes more active

The practical result: hammer curls are a brachialis-first exercise, not a biceps-first exercise.

## Why Train the Brachialis

The brachialis sits deep to the biceps brachii and does not contribute to the "peak" shape of the biceps. However, a well-developed brachialis pushes the biceps upward, increasing overall upper arm circumference and visual height from the side. Including hammer curls ensures the brachialis — which is undertrained by all supinated curl variations — receives direct work.

## Data Note

Jahizi 2023 (n=30) confirmed the grip-specific activation shift but did not report absolute %MVIC values. The muscle priority assignments (brachialis/brachioradialis primary) are based on mechanical analysis of the neutral grip position supported by the study's qualitative findings.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/handstand_push_ups.md -->

---
id: handstand_push_ups
name: Handstand Push-Ups
status: complete
category: exercise
pattern: [vertical press]
equipment: [body only]

difficulty:
  technical_complexity: 4
  strength_prerequisite: 4
  mobility_prerequisite: 3

muscles:
  - id: deltoid_anterior
    role: primary
  - id: deltoid_lateral
    role: primary
  - id: triceps_long
    role: primary
  - id: triceps_lateral
    role: primary
  - id: triceps_medial
    role: primary
  - id: trap_upper
    role: secondary
  - id: pec_major_clavicular
    role: secondary
  - id: serratus_anterior
    role: secondary
  - id: erector_spinae
    role: stabilizer
  - id: rectus_abdominis
    role: stabilizer
  - id: obliques
    role: stabilizer
  - id: forearm_flexors
    role: stabilizer

muscle_activation_studies: []

joint_rom_required:
  shoulder_flexion_deg: 180
  elbow_extension_deg: 0
  wrist_extension_deg: 80
  source: "biomechanical inference"

strength_curve:
  type: ascending
  sticking_point: bottom
  peak_force_position: bottom
  notes: "Hardest at the bottom when the head is near the floor and the shoulders are in maximal flexion under full bodyweight. Mechanical advantage improves as the arms extend."
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    shoulder: high
    wrist: high
    elbow: moderate
    cervical_spine: moderate
  common_injuries:
    - structure: rotator_cuff
      mechanism: impingement_under_full_bodyweight_overhead
      risk_factors: [insufficient_shoulder_mobility, previous_shoulder_injury, excessive_volume]
    - structure: wrist_joint
      mechanism: hyperextension_under_compression
      risk_factors: [limited_wrist_extension, high_bodyweight]
    - structure: cervical_spine
      mechanism: axial_compression_from_head_contact
      risk_factors: [uncontrolled_descent, lack_of_padding]
  contraindications:
    - acute_shoulder_impingement
    - rotator_cuff_tear
    - wrist_injury
    - cervical_disc_herniation
    - uncontrolled_hypertension

variations: []
progressions: []
alternatives: []

sources: []
---

# Handstand Push-Ups

An advanced bodyweight vertical press performed in an inverted position. The movement loads the shoulders and triceps with near-full bodyweight, making it one of the most demanding calisthenics pressing exercises.

## Execution

1. Face a wall and place both hands on the floor at shoulder width, roughly 15-20 cm from the wall.
2. Kick up into a handstand against the wall with arms fully extended. Keep the body in a straight line from wrists to ankles — engage the core and glutes to prevent excessive lumbar arch.
3. Lower yourself slowly by bending the elbows, allowing them to flare outward at roughly 45 degrees. Descend until the top of the head lightly touches the floor (or a pad placed on the floor).
4. Press back up by driving through the palms, extending the elbows fully at the top. Exhale on the way up.
5. Maintain a controlled tempo throughout — never drop onto the head.

## Programming Note

Wall-supported handstand push-ups are the standard variant for building overhead pressing strength without equipment. Progress toward this movement using pike push-ups, elevated pike push-ups, and box handstand push-ups. A solid 30-second freestanding wall handstand hold is a prerequisite before attempting the pressing component. Typical working sets are 3-5 reps due to the high strength demand. Freestanding handstand push-ups (no wall) represent the ultimate progression and require significant balance skill beyond raw pressing strength.


---

<!-- FILE: exercises/hang_snatch.md -->

---
id: hang_snatch
name: Hang Snatch
status: complete
category: exercise
pattern: [hinge, vertical pull]
equipment: [barbell]

difficulty:
  technical_complexity: 5
  strength_prerequisite: 3
  mobility_prerequisite: 4

muscles:
  - id: gluteus_maximus
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: vastus_medialis
    role: primary
  - id: rectus_femoris
    role: primary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: erector_spinae
    role: secondary
  - id: trap_upper
    role: secondary
  - id: deltoid_lateral
    role: secondary
  - id: deltoid_posterior
    role: secondary
  - id: soleus
    role: secondary
  - id: gastrocnemius_medial
    role: secondary
  - id: gastrocnemius_lateral
    role: secondary
  - id: rectus_abdominis
    role: stabilizer
  - id: multifidus
    role: stabilizer
  - id: forearm_flexors
    role: stabilizer

muscle_activation_studies: []

joint_rom_required:
  ankle_dorsiflexion_deg: 25
  hip_flexion_deg: 130
  shoulder_flexion_deg: 180
  thoracic_extension_deg: 20
  source: "biomechanical inference"

strength_curve:
  type: ascending
  sticking_point: bottom_of_catch
  peak_force_position: top_of_pull
  notes: "Hardest at the bottom of the catch position where the lifter must decelerate the bar and stabilize overhead in a deep squat. The initial pull benefits from the stretch-shortening cycle at the hang position."
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    wrist: high
    shoulder: high
    lumbar_spine: moderate
    knee: moderate
  common_injuries:
    - structure: wrist_ligaments
      mechanism: hyperextension_during_catch
      risk_factors: [poor_wrist_mobility, excessive_load, improper_turnover_timing]
    - structure: rotator_cuff
      mechanism: overhead_impingement
      risk_factors: [limited_shoulder_flexion, inadequate_thoracic_extension, fatigue]
    - structure: lumbar_spine
      mechanism: flexion_under_load
      risk_factors: [poor_hip_hinge_mechanics, excessive_load, insufficient_core_bracing]
  contraindications:
    - wrist_injury
    - shoulder_impingement
    - lumbar_herniation
    - limited_overhead_mobility

variations: [hang_snatch_below_knees, muscle_snatch]
progressions: [snatch_deadlift, snatch_pull]
alternatives: [power_snatch, one_arm_kettlebell_snatch]

sources: []
---

# Hang Snatch

A full snatch initiated from the hang position (bar at the hips, above the knee), finishing in a deep overhead squat. The shortened pulling distance compared to a floor snatch makes it an effective teaching progression and positional strength builder. One of the most technically demanding barbell movements, requiring explosive triple extension, fast turnover, and full overhead squat mobility.

## Execution

1. Set up with a wide snatch grip using a hook grip. Stand with feet hip-width apart, toes slightly turned out. Hinge at the hips to lower the bar to just above the knees, keeping the spine neutral and chest tall.
2. From the hang position, drive explosively through the floor by extending the hips, knees, and ankles simultaneously. Keep the bar close to the body.
3. At full extension, shrug the shoulders and pull the elbows high and wide. The bar should travel vertically, staying as close to the torso as possible.
4. As the bar reaches its peak height, aggressively pull yourself under the bar by dropping into a deep overhead squat. Punch the arms straight overhead and lock out the elbows as you receive the bar.
5. Stabilize in the bottom of the overhead squat with the bar directly over the midfoot, shoulders active, and core braced.
6. Stand up to full extension with the bar overhead. Lower the bar under control to the hang position for the next rep, or return it to the floor.

## Programming Note

The hang snatch is primarily used in Olympic weightlifting programs for technique refinement, positional strength at the hip, and rate-of-force development. It is also valuable for field sport athletes seeking explosive hip extension power. Due to its extreme technical complexity, prioritize movement quality over load. Program at 60-80% of full snatch 1RM for sets of 1-3 reps, with full recovery between sets. Ensure adequate shoulder and thoracic mobility before loading.


---

<!-- FILE: exercises/hanging_leg_raise.md -->

---
id: hanging_leg_raise
name: Hanging Leg Raise
status: complete
category: exercise
pattern: [isolation]
equipment: [pull_up_bar]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 2

muscles:
  - id: rectus_abdominis
    role: primary
  - id: iliopsoas
    role: primary
  - id: external_oblique
    role: secondary
  - id: rectus_femoris
    role: secondary

muscle_activation_studies:
  - source_id: mcgill_2015
    doi: "10.1080/02640414.2014.946437"
    n: null
    population: "healthy young adult males"
    condition:
      load_pct_1rm: null
      implement: "pull-up bar"
      phase: dynamic
      notes: "Hanging straight leg raise to 90°. Generates ~3000 N spinal compression — highest anterior chain compressive load in the study. MVC normalization."
    measurements:
      - muscle: rectus_abdominis
        mean_pct_mvc: 130.0
        sd: null
      - muscle: external_oblique
        mean_pct_mvc: 88.0
        sd: null

joint_rom_required:
  hip_flexion_deg: 90
  shoulder_flexion_deg: 180
  source: "McGill et al. 2015"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Hip flexor moment arm is maximal at 90° (legs horizontal); force demand increases from 0° to 90°, then decreases as legs travel past horizontal toward the bar. Sticking point at the horizontal leg position."
  source: "biomechanical inference; McGill et al. 2015"

injury_risk:
  joint_stress:
    lumbar: moderate
    shoulder: low
  common_injuries:
    - structure: lumbar_spine
      mechanism: compressive_load
      risk_factors: [straight_leg_raise_at_high_repetitions, pre_existing_disc_pathology, lumbar_stenosis]
    - structure: shoulder_joint
      mechanism: distraction_force
      risk_factors: [extended_hang_duration, rotator_cuff_weakness]
  contraindications:
    - acute_lumbar_disc_herniation
    - acute_shoulder_instability

variations: []
progressions: []
alternatives: []

sources:
  - title: "Muscle activity and spine load during anterior chain whole body linkage exercises: the body saw, hanging leg raise and walkout from a push-up"
    author: "McGill, S. M., Andersen, J., & Cannon, J."
    year: 2015
    doi: "10.1080/02640414.2014.946437"
    source_id: mcgill_2015
    credibility: rct
---

# Hanging Leg Raise

The hanging leg raise is performed by hanging from a pull-up bar and raising the legs to horizontal using the hip flexors and abdominal muscles. McGill et al. (2015) identified it as one of the highest anterior chain challenges available, generating rectus abdominis activation of 130% MVC — exceeding the normalization reference value. This high activation comes with a significant trade-off: approximately 3000 N of spinal compressive force, the highest of any common core exercise studied.

## Execution

1. Hang from a pull-up bar with arms fully extended, grip slightly wider than shoulder width
2. Depress the scapulae and brace the core before initiating the movement
3. Raise the legs by flexing at the hip — keep the knees extended for maximum difficulty
4. Raise until the legs are parallel to the floor (90° hip flexion); pause briefly
5. Lower under control, resisting the eccentric with the hip flexors and abdominals

## Why Activation Exceeds 100% MVC

Values above 100% MVC indicate that the dynamic demand of the exercise exceeds the force produced during the isolated isometric normalization test. This occurs when the stretch-shortening cycle, momentum, or eccentric demands exceed a simple isometric maximum. It reflects high dynamic challenge, not measurement error.

## Spinal Compression Trade-Off

| Exercise | Spinal Compression | Rectus Abdominis |
|---|---|---|
| Hanging straight leg raise | ~3000 N | 130% MVC |
| Suspension body saw | <2500 N | ~58% MVC |
| Front plank | Low | ~48% MVC |

For athletes with lumbar disc pathology or stenosis, lower-compression alternatives (ab wheel rollout, body saw, plank progressions) should be prioritised. For healthy athletes, the hanging leg raise is a high-yield core exercise.

## Regression / Progression

| Level | Exercise |
|-------|----------|
| Beginner | Hanging knee raise (shorter lever arm, lower compression) |
| Intermediate | Hanging leg raise to 90° |
| Advanced | Toes-to-bar (full hip flexion range) |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/incline_cable_flye.md -->

---
id: incline_cable_flye
name: Incline Cable Flye
status: complete
source: free-exercise-db
category: exercise
pattern:
- isolation
equipment:
- cable
difficulty:
  technical_complexity: null
  strength_prerequisite: null
  mobility_prerequisite: null
muscles:
- id: pectoralis_major
  role: primary
- id: deltoid_anterior
  role: secondary

muscle_activation_studies: []

joint_rom_required:
  shoulder_horizontal_adduction_deg: 90
  elbow_flexion_deg: 15
  source: "Gold's Gym"

strength_curve:
  type: ascending
  sticking_point: top_third
  peak_force_position: top
  notes: "Low-to-high cable arc aligns with clavicular fiber direction; peak force at end-range (fully shortened) position"

variations: []
progressions: []
alternatives: []
sources:
- title: free-exercise-db
  author: yuhonas (Public Domain)
  credibility: anecdotal
---

# Incline Cable Flye

## Execution

1. To get yourself into the starting position, set the pulleys at the floor level (lowest
   level possible on the machine that is below your torso).
2. Place an incline bench (set at 45 degrees) in between the pulleys, select a weight on
   each one and grab a pulley on each hand.
3. With a handle on each hand, lie on the incline bench and bring your hands together at
   arms length in front of your face. This will be your starting position.
4. With a slight bend of your elbows (in order to prevent stress at the biceps tendon),
   lower your arms out at both sides in a wide arc until you feel a stretch on your
   chest. Breathe in as you perform this portion of the movement. Tip: Keep in mind that
   throughout the movement, the arms should remain stationary. The movement should only
   occur at the shoulder joint.
5. Return your arms back to the starting position as you squeeze your chest muscles and
   exhale. Hold the contracted position for a second. Tip: Make sure to use the same arc
   of motion used to lower the weights.
6. Repeat the movement for the prescribed amount of repetitions.


---

<!-- FILE: exercises/incline_dumbbell_curl.md -->

---
id: incline_dumbbell_curl
name: Incline Dumbbell Curl
status: complete
category: exercise
pattern: [isolation]
equipment: [dumbbell]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 2

muscles:
  - id: biceps_brachii
    role: primary
  - id: brachialis
    role: secondary
  - id: brachioradialis
    role: secondary

# porcari_2014 (n=16): biceps_brachii 77.5% MVIC — virtually identical to barbell curl (76.5%).
# oliveira_2009: biceps_brachii ~95% MVIC.
# ROM: 134.3° elbow flexion — shorter than barbell curl due to supine position limiting extension.
# Shoulder: -50° (hyperextension) — biceps long head is at its longest mechanical length.
muscle_activation_studies:
  - source_id: porcari_2014
    doi: null
    n: 16
    population: "healthy adults, standardized load"
    condition:
      implement: dumbbell
      phase: full_rep
      notes: "Seated on incline bench ~60°; shoulder in hyperextension"
    measurements:
      - {muscle: biceps_brachii, mean_pct_mvc: 77.5, sd: null}
  - source_id: oliveira_2009
    doi: null
    n: null
    population: "general population"
    condition:
      implement: dumbbell
      phase: full_rep
    measurements:
      - {muscle: biceps_brachii, mean_pct_mvc: 95.0, sd: null}

joint_rom_required:
  elbow_flexion_deg: 134
  shoulder_extension_deg: 50
  source: "Marcolin 2018"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped overall, but the bottom of the range is uniquely loaded due to shoulder hyperextension stretching the biceps long head at its maximum length — greater lengthened-position stimulus than upright curls"
  source: "Marcolin 2018"

injury_risk:
  joint_stress:
    elbow: low
    shoulder: low
  common_injuries:
    - structure: biceps_tendon_long_head
      mechanism: stretch_overload_at_shoulder
      risk_factors: [allowing_full_extension_at_max_stretch, heavy_load, pre_existing_biceps_tendinopathy]
    - structure: anterior_shoulder_capsule
      mechanism: passive_stretch
      risk_factors: [bench_angle_too_low, pre_existing_shoulder_instability]
  contraindications:
    - acute_biceps_long_head_tendinopathy
    - anterior_shoulder_instability

variations: []
progressions: []
alternatives: [dumbbell_bicep_curl, barbell_curl]

sources:
  - source_id: porcari_2014
    title: "ACE-Sponsored Research: Best Biceps Exercises"
    author: "Porcari, John P. et al. (ACE)"
    year: 2014
    doi: null
    credibility: rct
  - source_id: oliveira_2009
    title: "EMG analysis of biceps brachii in curl variations"
    author: "Oliveira, Leal et al."
    year: 2009
    doi: null
    credibility: rct
  - source_id: marcolin_2018
    title: "Differences in electromyographic activity of biceps brachii and brachioradialis while performing three variants of curl"
    author: "Marcolin, Giuseppe et al."
    year: 2018
    doi: null
    credibility: rct
---

# Incline Dumbbell Curl

The incline dumbbell curl places the lifter on a bench angled at approximately 45–60° with the arms hanging behind the body. This positions the shoulder in hyperextension (approximately -50°), placing the biceps long head — which crosses the shoulder joint — at its maximum mechanical length. No other common curl variation achieves this degree of long head stretch, making the incline curl uniquely valuable for loading the biceps in its most lengthened position.

## Execution

1. Set an incline bench to approximately 45–60°; steeper angles reduce the shoulder hyperextension benefit
2. Sit back against the bench with the arms hanging freely at the sides; dumbbells should be behind the body's plane, not at the hips
3. Starting from the fully hanging position (maximum stretch), curl upward with simultaneous supination
4. Do not allow the shoulders to roll forward or the upper arms to drift forward from the bench
5. Lower under full control — the eccentric through the stretched position is the most mechanically unique aspect of this exercise

## What the EMG Data Shows

| Study | Biceps Activation | Notes |
|-------|-------------------|-------|
| Porcari 2014 | 77.5% MVIC | Near-identical to barbell curl (76.5%) |
| Oliveira 2009 | 95.0% MVIC | Higher load condition |

The Porcari values suggest that incline curls produce similar peak EMG to standing curls. The mechanistic advantage of the incline curl is not peak activation but the unique loading of the biceps at its maximum elongated length — a stimulus type that growing evidence links to superior long-head hypertrophy.

## Why the Stretch Position Matters

The biceps long head originates at the supraglenoid tubercle of the scapula (above the shoulder). When the shoulder is extended (arm behind the body), the long head is stretched beyond the position it occupies in upright curls. This combination of active muscle contraction at long length is associated with elevated hypertrophic signaling in the long head specifically. The incline curl is therefore most valuable as a complement to exercises that load the mid- and shortened positions (concentration curl, preacher curl).

## Setup Cautions

- Bench angle: 45–60° is optimal. Angles below 45° over-stretch the anterior shoulder capsule. Angles above 60° reduce the hyperextension benefit.
- Load: Use lighter loads than standing curls. The stretched starting position limits available force and injury risk is elevated with excessive weight.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/incline_dumbbell_flyes.md -->

---
id: incline_dumbbell_flyes
name: Incline Dumbbell Flyes
status: complete
source: free-exercise-db
category: exercise
pattern:
- isolation
equipment:
- dumbbell
difficulty:
  technical_complexity: null
  strength_prerequisite: null
  mobility_prerequisite: null
muscles:
- id: pectoralis_major
  role: primary
- id: deltoid_anterior
  role: secondary
muscle_activation_studies:
  - source_id: schanke_2012
    doi: null
    n: 14
    population: "trained men"
    condition:
      load_pct_1rm: 80
      implement: dumbbell
      elbow_angle_deg: 15
      phase: full_rep
      notes: "Normalized to flat barbell bench press = 100%, NOT true %MVIC. Incline dumbbell fly produced 69% of bench press activation."
    measurements:
      - muscle: pectoralis_major
        mean_pct_mvc: null
        sd: null
  - source_id: tavares_2017
    doi: null
    n: 17
    population: "trained males"
    condition:
      load_pct_1rm: null
      implement: dumbbell
      elbow_angle_deg: 15
      phase: full_rep
      notes: "Relative comparison only; incline produced significantly higher deltoid_anterior (d=1.15) and lower pec_major_sternal (d=1.07) vs. flat. No absolute %MVIC reported."
    measurements:
      - muscle: deltoid_anterior
        mean_pct_mvc: null
        sd: null
      - muscle: pec_major_sternal
        mean_pct_mvc: null
        sd: null

joint_rom_required:
  shoulder_horizontal_adduction_deg: 90
  elbow_flexion_deg: 15
  source: "Reiser 2017"

strength_curve:
  type: descending
  sticking_point: bottom_third
  peak_force_position: bottom
  notes: "Sticking point and peak force occur at the bottom, lengthened position; bench angle 15–30° optimizes clavicular head recruitment"

variations: []
progressions: []
alternatives: []
sources:
- title: "ACE-Sponsored Research: Top 3 Most Effective Chest Exercises"
  author: "Schanke et al."
  year: 2012
  doi: null
  source_id: schanke_2012
  credibility: rct
- title: "Journal of Exercise Physiologyonline — Electromyography of Dumbbell Fly Exercise Using Different Planes and Labile Surfaces"
  author: "Tavares et al."
  year: 2017
  doi: null
  source_id: tavares_2017
  credibility: rct
- title: free-exercise-db
  author: yuhonas (Public Domain)
  credibility: anecdotal
---

# Incline Dumbbell Flyes

## Execution

1. Hold a dumbbell on each hand and lie on an incline bench that is set to an incline angle
   of no more than 30 degrees.
2. Extend your arms above you with a slight bend at the elbows.
3. Now rotate the wrists so that the palms of your hands are facing you. Tip: The pinky
   fingers should be next to each other. This will be your starting position.
4. As you breathe in, start to slowly lower the arms to the side while keeping the arms
   extended and while rotating the wrists until the palms of the hand are facing each
   other. Tip: At the end of the movement the arms will be by your side with the palms
   facing the ceiling.
5. As you exhale start to bring the dumbbells back up to the starting position by reversing
   the motion and rotating the hands so that the pinky fingers are next to each other
   again. Tip: Keep in mind that the movement will only happen at the shoulder joint and
   at the wrist. There is no motion that happens at the elbow joint.
6. Repeat for the recommended amount of repetitions.


---

<!-- FILE: exercises/incline_dumbbell_press.md -->

---
id: incline_dumbbell_press
name: Incline Dumbbell Press
status: complete
category: exercise
pattern: [horizontal_push]
equipment: [dumbbell]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 1

muscles:
  - id: pec_major_clavicular
    role: primary
  - id: pec_major_sternal
    role: secondary
  - id: deltoid_anterior
    role: secondary
  - id: triceps_brachii
    role: secondary
  - id: serratus_anterior
    role: stabilizer

# ebd_2026 is a literature compilation. All activation data for incline dumbbell press
# is qualitative — no specific %MVIC values are reported. Relative comparisons are
# preserved as notes. Do NOT fabricate numeric %MVIC values.
muscle_activation_studies:
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      bench_angle_deg: "30-45"
      notes: "Optimal bench angle range for clavicular head targeting"
    measurements:
      - {muscle: pec_major_clavicular, mean_pct_mvc: null, notes: "Peak at 30–45°; +34% vs 0° flat press"}
      - {muscle: pec_major_sternal,    mean_pct_mvc: null, notes: "Higher at 30° than 44–45°; sternal contribution decreases at steeper angles"}
      - {muscle: deltoid_anterior,     mean_pct_mvc: null, notes: "Increases linearly with bench angle >45°; becomes dominant above 45°"}

joint_rom_required:
  elbow_flexion_deg: 90
  shoulder_horizontal_adduction_deg: null
  notes: >
    Elbows tucked 30–60° from torso (not fully flared). Dumbbells lower to chest level
    or slightly below with handles level with the upper chest. Concentric ends with
    arms nearly straight — avoid hard lockout to maintain pec tension.
  source: "ebd_2026"

strength_curve:
  type: ascending
  sticking_point: bottom_third
  peak_force_position: bottom
  notes: >
    Hardest at the bottom where the clavicular fibers are maximally stretched and the
    shoulder moment arm is greatest. Mechanical advantage increases as the elbows extend.
    Independent dumbbell path prevents the dominant limb from compensating at the sticking
    point, forcing bilateral symmetry through the hardest range.
  source: "ebd_2026"

injury_risk:
  joint_stress:
    shoulder: moderate
    elbow: low
  common_injuries:
    - structure: rotator_cuff
      mechanism: subacromial_impingement
      risk_factors: [elbows_flared_beyond_60_deg, excessive_depth_below_chest, shoulder_internal_rotation]
    - structure: pec_major_clavicular_insertion
      mechanism: eccentric_overload_at_maximum_stretch
      risk_factors: [excessive_depth, rapid_load_increase, cold_muscles]
  contraindications:
    - acute_shoulder_impingement
    - acute_pectoralis_major_tear
    - acromioclavicular_joint_pathology

variations: []
progressions: []
alternatives: []

sources:
  - source_id: ebd_2026
    title: "Exercise Biomechanics Data Extraction: Upper Push Accessories"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Incline Dumbbell Press

The incline dumbbell press is a multi-joint upper-body pressing exercise performed on a bench set to 30–45° of inclination. The elevated angle shifts the force vector relative to the torso, redirecting the primary plane of motion from pure horizontal adduction toward shoulder flexion and targeting the clavicular head of the pectoralis major. Independent dumbbell paths allow natural wrist rotation and greater horizontal adduction at the top of the concentric phase compared to the barbell incline press.

## Execution

1. Set the bench to 30–45°; sit back with dumbbells held at shoulder height, palms facing forward
2. Brace the core; drive the dumbbells upward, keeping the elbows 30–60° from the torso (avoid full flare)
3. Lower under control until the dumbbells are level with the upper chest; allow the elbows to drift no further than 60° from the torso
4. Press back up in the same arc, stopping just before elbow lockout to maintain continuous pec tension
5. Control the descent to at least 2 seconds per rep

## What the Data Shows

The available data on the incline dumbbell press is comparative rather than absolute — the ebd_2026 literature compilation reports relative activation changes rather than specific %MVIC values.

Key findings:
- A 30–45° bench angle produces peak clavicular pec activation; a 30° angle yields +34% greater upper pec EMG compared to flat pressing
- Bench angles exceeding 45° shift the load progressively toward the anterior deltoid, converting the movement into a shoulder press pattern above ~60°
- The sternal head shows higher relative activation at 30° than at 44–45°, suggesting that even the lower fibers respond better to moderate inclination than steep inclination
- An elbow path of 30–60° relative to the torso produces higher EMG in both pec heads than a fully flared elbow position

## Angle Selection

The 30° vs 45° decision has a meaningful effect on target-muscle distribution. At 30°, the sternal fibers contribute more, producing a fuller chest stimulus. At 45°, the clavicular head takes a greater proportion of the load, producing better upper-chest isolation. For general hypertrophy, 30–35° is the most commonly supported angle. For specifically targeting the upper chest in athletes with strong lower pec development, 40–45° is appropriate — beyond 45°, anterior deltoid dominates.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Incline barbell press | Fixed bar path; less ROM | Heavier loading; better bilateral strength testing |
| Flat dumbbell press | 0° angle; sternal pec emphasis | Primary horizontal pressing hypertrophy |
| Cable incline fly | Constant tension through full ROM | Pec stretch-shortening without triceps assistance |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/inverted_row.md -->

---
id: inverted_row
name: Inverted Row
status: complete
category: exercise
pattern: [horizontal_pull]
equipment: [barbell]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: latissimus_dorsi
    role: primary
  - id: trap_middle
    role: primary
  - id: deltoid_posterior
    role: primary
  - id: biceps_brachii
    role: secondary
  - id: rhomboids
    role: secondary
  - id: erector_spinae
    role: stabilizer
  - id: rectus_femoris
    role: stabilizer

# ssd_2026 literature compilation. All values %MVIC.
# Stable bar and suspension (TRX) conditions both reported.
# Erector spinae values are isometric (holding plank position), not dynamic.
# Rectus femoris 2.7% confirms minimal hip flexor demand.
muscle_activation_studies:
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      variation: stable_bar
      grip: overhand
    measurements:
      - {muscle: latissimus_dorsi,  mean_pct_mvc: 99.3,  sd: 53.3}
      - {muscle: trap_middle,        mean_pct_mvc: 98.6,  sd: 35.6}
      - {muscle: deltoid_posterior,  mean_pct_mvc: 103.4, sd: 35.7}
      - {muscle: biceps_brachii,    mean_pct_mvc: 67.9,  sd: 20.1}
      - {muscle: erector_spinae,    mean_pct_mvc: 29.3,  sd: null, notes: "LUES isometric 29.9%, RLES isometric 28.7%; stabilizer demand only"}
      - {muscle: rectus_femoris,    mean_pct_mvc: 2.7,   sd: null, notes: "Minimal hip flexor demand confirms spinal unloading vs standing rows"}
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      variation: suspension_trx
    measurements:
      - {muscle: latissimus_dorsi,  mean_pct_mvc: 101.6, sd: 46.5}
      - {muscle: trap_middle,        mean_pct_mvc: 98.4,  sd: 54.2}
      - {muscle: deltoid_posterior,  mean_pct_mvc: 103.4, sd: 35.7}
      - {muscle: biceps_brachii,    mean_pct_mvc: 67.9,  sd: 20.1}

joint_rom_required:
  shoulder_flexion_start_deg: 90
  elbow_flexion_deg: 110
  notes: >
    Body remains in a rigid supine plank with knees bent ~90°. Movement begins with
    shoulder at 90° flexion (arms straight overhead). Concentric phase drives shoulder
    through horizontal extension to ~0° as elbows flex 90–110°. Scapulae retract
    dynamically throughout the pull.
  source: "ssd_2026"

strength_curve:
  type: descending
  sticking_point: top_quarter
  peak_force_position: first_quarter
  notes: >
    Gravity acts perpendicular to the supine torso at the start, maximizing resistance
    in the first quarter. The sticking point is the terminal lockout (top quarter) —
    here elbow flexor leverage is reduced and the remaining movement requires maximal
    scapular retraction against a shortened lever arm. This contrasts with standing
    rows, which display an ascending-descending (bell-shaped) curve with peak force
    at mid-range.
  source: "ssd_2026"

injury_risk:
  joint_stress:
    shoulder: low
    elbow: low
    lower_back: low
  common_injuries:
    - structure: wrist
      mechanism: hyperextension_under_load
      risk_factors: [bar_too_high, insufficient_grip_strength, fatigue]
  contraindications: []

variations: []
progressions: []
alternatives: [bent_over_barbell_row]

sources:
  - source_id: ssd_2026
    title: "Sports Science Data Extraction: Vertical Pulling and Horizontal Rowing"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Inverted Row

The inverted row is a closed-chain, bodyweight horizontal pulling exercise performed beneath a fixed bar set to roughly waist height. The lifter hangs supine with arms extended, body rigid in a plank, and pulls their chest to the bar by flexing the elbows and retracting the scapulae. It elicits near-identical back and shoulder activation to standing rows while almost completely eliminating lumbar erector spinae demand — making it the primary horizontal rowing substitute for athletes with lower back pathology or for general training contexts where spinal loading must be managed.

## Execution

1. Set a bar in a rack to approximately waist height; lie beneath it with arms fully extended and hands just outside shoulder width, overhand grip
2. Extend the body into a rigid plank — hips up, heels on the floor, knees bent ~90°; do not let the hips sag
3. Pull the chest toward the bar by flexing the elbows and driving the shoulder blades together and down
4. Pause briefly when the chest touches the bar; lower under control to full arm extension
5. Difficulty is adjusted by bar height — lower bar = greater bodyweight fraction = harder

## What the EMG Data Shows

**Primary movers** (stable bar, overhand):

- Latissimus dorsi: 99.3 ± 53.3% MVIC
- Middle trapezius: 98.6 ± 35.6% MVIC
- Posterior deltoid: 103.4 ± 35.7% MVIC
- Biceps brachii: 67.9 ± 20.1% MVIC

These values are equivalent to the standing bent-over barbell row for LD and trap_middle — the inverted row is not a reduced-stimulus exercise.

**Spinal load contrast**: Erector spinae activation is 28.7–29.9% MVIC (isometric stabilizer only) and rectus femoris is 2.7% MVIC. In the standing bent-over row, the ES must eccentrically control a loaded hip hinge under high shear — here it only maintains a horizontal plank. This is the key clinical trade-off: equal back development stimulus, dramatically lower spinal cost.

**Suspension (TRX) variation**: LD increases marginally to 101.6 ± 46.5% MVIC; the primary difference is instability demand rather than a meaningful change in primary mover activation.

## The Spinal Unloading Mechanism

The inverted row achieves spinal unloading through body position, not exercise modification. In a standing bent-over row at ~75° of hip flexion, the erector spinae must counteract both the gravitational moment of the torso and the additional moment created by the loaded bar — generating compressive and shear forces at the lumbar discs that increase linearly with load. In the inverted row, the body is horizontal and the spine is not resisting a gravitational flexion moment. The ES fires isometrically only to prevent sagging. Load capacity is limited to bodyweight fraction rather than absolute load, but the neuromuscular stimulus to the target muscles (LD, middle trap, posterior delt) is preserved.

## Strength Curve

The inverted row has a steep descending curve — hardest at the bottom where gravity acts directly perpendicular to the body. This is opposite to standing rows, which build to peak resistance at mid-range. Trainees who struggle with lockout at the top can place the bar slightly higher; trainees who find the bottom too easy should lower the bar or elevate their feet.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Feet elevated inverted row | Greater bodyweight fraction; closer to BW pull-up difficulty | Progressive overload without external load |
| Suspension (TRX) inverted row | Unstable; handles rotate; increased stabilizer demand | Shoulder stabilizer training; travel/no-rack contexts |
| Wide-grip inverted row | Greater posterior delt and trap demand | Upper back width emphasis |
| Weighted vest inverted row | External load while maintaining closed-chain mechanics | Load progression beyond bodyweight |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/kneeling_cable_triceps_extension.md -->

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


---

<!-- FILE: exercises/leg_extensions.md -->

---
id: leg_extensions
name: Leg Extensions
status: complete
category: exercise
pattern: [isolation]
equipment: [machine]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: rectus_femoris
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: vastus_medialis
    role: primary
  - id: vastus_intermedius
    role: primary

# perry_2009: Isometric contractions at various joint angles.
# rectus_femoris 27.8%, vastus_lateralis 25.9%, vastus_medialis 22.9% MVIC.
# Note: these are ISOMETRIC values — not dynamic %MVIC during the full leg extension ROM.
muscle_activation_studies:
  - source_id: perry_2009
    doi: null
    n: null
    population: "healthy adults, isometric contractions at various knee angles"
    condition:
      implement: machine
      phase: isometric
      notes: "Isometric contractions only — not dynamic full-ROM values"
    measurements:
      - {muscle: rectus_femoris,   mean_pct_mvc: 27.8, sd: null}
      - {muscle: vastus_lateralis, mean_pct_mvc: 25.9, sd: null}
      - {muscle: vastus_medialis,  mean_pct_mvc: 22.9, sd: null}

joint_rom_required:
  knee_flexion_deg: 90
  knee_extension_deg: 0
  source: "perry_2009"

strength_curve:
  type: ascending
  sticking_point: top_third
  peak_force_position: top
  notes: "Ascending; hardest at full extension where the moment arm is maximal; the rectus femoris is also shortened at the hip (seated position), reducing available force — making the top the sticking point"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    knee: moderate
    patellofemoral: moderate
  common_injuries:
    - structure: patellofemoral_joint
      mechanism: shear_stress_at_full_extension
      risk_factors: [pre_existing_patellofemoral_pain, locking_out_forcefully, heavy_load]
    - structure: patellar_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, heavy_load, pre_existing_patellar_tendinopathy]
  contraindications:
    - acute_patellofemoral_pain_syndrome
    - acute_patellar_tendinopathy
    - post_ACL_reconstruction_early_phase

variations: []
progressions: []
alternatives: [single_leg_leg_extension]

sources:
  - source_id: perry_2009
    title: "Electromyographic analysis of the knee extension exercise"
    author: "Perry, Frank T. et al."
    year: 2009
    doi: null
    credibility: rct
---

# Leg Extensions

The leg extension is the primary open-chain quadriceps isolation exercise. Seated on a leg extension machine with the ankle pad just above the foot, the exercise produces pure knee extension against resistance, isolating all four quadriceps heads (rectus femoris, vastus lateralis, vastus medialis, vastus intermedius) from any hip involvement. It provides the only direct rectus femoris stimulus in a shortened-hip-flexion configuration that squats and lunges cannot replicate.

## Execution

1. Sit on the machine with the back of the knees at the seat edge; adjust the ankle pad to sit just above the ankle
2. The starting angle should be approximately 90° knee flexion (or the machine's maximum range)
3. Extend the knees to full extension under controlled speed; hold briefly at the top
4. Lower under control; do not let the weight drop through the eccentric

## What the EMG Data Shows

Perry 2009 (isometric contractions):

| Muscle | Activation |
|--------|-----------|
| Rectus femoris | 27.8% MVIC |
| Vastus lateralis | 25.9% MVIC |
| Vastus medialis | 22.9% MVIC |

These are **isometric values**, not dynamic full-ROM values. They indicate relatively balanced quad head activation during the leg extension pattern.

## The Rectus Femoris Uniqueness

The rectus femoris is the only quadriceps head that also flexes the hip. In the seated position, the hip is flexed at ~90°, which places the rectus femoris in a shortened proximal configuration. This creates a stimulus that squats and lunges do not replicate: the rectus femoris must contract against a mechanically disadvantaged position at the hip.

## Patellofemoral Considerations

Open-chain terminal knee extension (the last 30°) produces patellofemoral compressive forces. Trainees with active patellofemoral pain syndrome should limit range to 60–90° and avoid the last 30° until symptoms resolve. This restriction is not categorically necessary for healthy trainees.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/leg_press.md -->

---
id: leg_press
name: Leg Press
aliases: [45-degree leg press, machine leg press, seated leg press]
status: complete
category: exercise
pattern: [squat]
muscles:
  - id: rectus_femoris
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: vastus_medialis
    role: primary
  - id: gluteus_maximus
    role: primary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
equipment: [leg press machine]
difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 2
alternatives: [back_squat]
joint_rom_required:
  knee_flexion_deg: 110
  hip_flexion_deg: 85
  ankle_dorsiflexion: minimal
  notes: "Knee 100-120°; hip 80-90° (fixed by seat geometry); ankle relatively unconstrained; foot placement shifts emphasis: high foot = more glute/hamstring, low foot = more quad"
  source: "da Silva 2008; Martin-Fuentes 2020"

strength_curve:
  type: ascending
  sticking_point: mid_range
  peak_force_position: near_extension
  notes: "Sticking point at 90-100° knee flexion where moment arm is greatest; machine guides path eliminating balance demand; eccentric often underutilized in standard practice"
  source: "Walker 2025; Martin-Fuentes 2022"

sources:
  - title: "NSCA's Essentials of Strength Training and Conditioning"
    author: "NSCA"
    credibility: expert_consensus
  - title: "Muscle activity in the leg press exercise with different foot positions"
    author: "da Silva, E. M., et al."
    year: 2008
    doi: null
    credibility: rct
  - title: "Electromyographic analysis of the leg press exercise and its variants"
    author: "Martin-Fuentes, I., et al."
    year: 2020
    doi: null
    credibility: rct
---

# Leg Press

The leg press is a machine-based squat-pattern movement where the lifter pushes a weighted platform away with the legs from a seated or reclined position. The fixed path removes most balance and bracing demands, isolating the legs.

## Execution

1. Sit with the back flat against the pad, feet shoulder width on the platform
2. Release the safeties and lower the platform under control
3. Descend until the knees reach roughly 90 degrees without the lower back rounding
4. Press the platform up without locking the knees aggressively

## Common Faults

- **Lower back rounding** — descending too deep lifts the hips off the pad
- **Locking knees hard** — joint stress at the top
- **Feet too low** — shifts excessive load to the knees

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| High foot placement | More glute and hamstring | Posterior emphasis |
| Low foot placement | More quad | Quad emphasis |
| Single leg | One side at a time | Imbalance correction |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/log_lift.md -->

---
id: log_lift
name: Log Lift
status: complete
category: exercise
pattern: [vertical press]
equipment: [log]

difficulty:
  technical_complexity: 4
  strength_prerequisite: 4
  mobility_prerequisite: 3

muscles:
  - id: deltoid_anterior
    role: primary
  - id: deltoid_lateral
    role: secondary
  - id: triceps_long
    role: primary
  - id: triceps_lateral
    role: primary
  - id: triceps_medial
    role: secondary
  - id: pectoralis_major
    role: secondary
  - id: trap_upper
    role: secondary
  - id: trap_middle
    role: secondary
  - id: erector_spinae
    role: secondary
  - id: multifidus
    role: secondary
  - id: rectus_abdominis
    role: secondary
  - id: obliques
    role: secondary
  - id: gluteus_maximus
    role: secondary
  - id: rectus_femoris
    role: secondary
  - id: vastus_lateralis
    role: secondary
  - id: vastus_medialis
    role: secondary
  - id: biceps_femoris
    role: tertiary
  - id: semitendinosus
    role: tertiary
  - id: rhomboids
    role: tertiary

muscle_activation_studies: []

joint_rom_required:
  trunk_rom_deg: 83
  hip_rom_deg: 126
  shoulder_flexion_deg: 170
  source: "biomechanical comparison with Olympic clean & jerk — log lift requires 24% greater trunk ROM (82.7 +/- 8.4 deg vs 66.8 +/- 12.0 deg) and 8% greater hip ROM (125.5 +/- 8.9 deg vs 115.7 +/- 10.4 deg)"

strength_curve:
  type: ascending
  sticking_point: transition_from_rack_to_press
  notes: "The log's diameter forces the elbows wide at the rack position, creating a mechanically disadvantaged start for the press. The neutral grip reduces shoulder external rotation demand compared to a barbell."

injury_risk:
  joint_stress:
    shoulder: moderate
    lumbar_spine: moderate
    wrist: low
  common_injuries:
    - structure: lumbar_disc
      mechanism: hyperextension_during_layback_press
      risk_factors: [excessive_layback, weak_anterior_core, fatigue]
    - structure: shoulder_labrum
      mechanism: overhead_pressing_with_wide_implement
      risk_factors: [poor_thoracic_mobility, pre_existing_impingement, excessive_load]
  contraindications:
    - acute_shoulder_impingement
    - acute_lumbar_disc_herniation
    - limited_overhead_mobility

variations: []
progressions: [push_press]
alternatives: [overhead_press, push_press]

sources: []
---

# Log Lift

A strongman overhead press performed with a cylindrical log implement featuring neutral-grip handles inside. The movement consists of two phases: a clean from the floor to the rack position on the chest, followed by a push press (or strict press) overhead. The log's large diameter demands significantly greater trunk and hip range of motion than an Olympic clean and jerk — approximately 24% more trunk ROM and 8% more hip ROM. The neutral grip reduces shoulder external rotation demand, making it more accessible for athletes with limited shoulder mobility in external rotation.

## Execution

1. **Setup.** Stand over the log with feet hip-width apart. Reach through the log openings and grip the neutral handles firmly.
2. **Clean — First Pull.** Extend through the hips and knees to pull the log from the floor. Keep the log tight against the body.
3. **Clean — Lap and Roll.** As the log reaches thigh height, sit back slightly and roll the log up the torso. Transition to a front rack position by driving the elbows up and pushing the head back to create a shelf on the upper chest.
4. **Dip and Drive.** Flex the knees 4-6 inches, then explosively extend to generate vertical momentum on the log.
5. **Press and Lockout.** Continue pressing through the elbows. As the log clears the head, push the head forward through the "window" between the arms. Lock out with the log directly over the base of support.
6. **Descent.** Lower the log back to the rack position under control, then to the floor (or perform another rep from the rack).

## Programming Note

The log lift is technically demanding due to the implement's diameter and the transition from clean to press. Athletes should be proficient with barbell push press mechanics before introducing the log. In competition, the log is typically contested as a max single or timed max reps. Allow the same recovery as heavy overhead pressing (48-72 hours). Wrist wraps are commonly used to support the extended wrist position in the rack.


---

<!-- FILE: exercises/lying_leg_curls.md -->

---
id: lying_leg_curls
name: Lying Leg Curls
status: complete
category: exercise
pattern: [isolation]
equipment: [machine]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: biceps_femoris
    role: primary
  - id: semitendinosus
    role: primary
  - id: semimembranosus
    role: primary
  - id: gastrocnemius_medial
    role: secondary
  - id: gastrocnemius_lateral
    role: secondary

# schoenfeld_2014 (n=13): prone position.
# biceps_femoris 80% MVIC, semitendinosus 65% MVIC.
# Hip neutral (0° flexion) → hamstring heads in mid-range length.
# Bell-shaped strength curve: hardest at ~90° knee flexion.
muscle_activation_studies:
  - source_id: schoenfeld_2014
    doi: null
    n: 13
    population: "healthy males, prone leg curl machine"
    condition:
      implement: machine
      phase: full_rep
      notes: "Prone (lying face-down) position; hip at 0°"
    measurements:
      - {muscle: biceps_femoris, mean_pct_mvc: 80.0, sd: null}
      - {muscle: semitendinosus, mean_pct_mvc: 65.0, sd: null}

joint_rom_required:
  knee_flexion_deg: 130
  hip_flexion_deg: 0
  source: "schoenfeld_2014"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped; peak hamstring force at ~90° knee flexion; prone hip position places hamstrings in mid-length"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    knee: low
    hip: low
  common_injuries:
    - structure: proximal_hamstring_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, heavy_load, pre_existing_proximal_tendinopathy]
  contraindications:
    - acute_proximal_hamstring_tendinopathy
    - acute_posterior_knee_injury

variations: []
progressions: []
alternatives: [seated_leg_curl, glute_ham_raise]

sources:
  - source_id: schoenfeld_2014
    title: "Effects of Different Volume-Equated Resistance Training Loading Strategies on Muscular Adaptations in Well-Trained Men"
    author: "Schoenfeld, Brad J. et al."
    year: 2014
    doi: null
    credibility: rct
---

# Lying Leg Curls

The lying leg curl is the standard prone isolation exercise for the hamstrings. Performed face-down on a leg curl machine, the knee flexion movement loads the biceps femoris, semitendinosus, and semimembranosus against pad resistance. The prone (hip neutral) position places all three hamstring heads in their natural mid-range length, producing a bell-shaped resistance curve with peak load at approximately 90° knee flexion.

## Execution

1. Adjust the leg curl machine pad so it sits just above the ankle and lie face-down
2. Keep the hips flat on the pad throughout — do not allow the hips to lift as the legs curl up
3. Curl the legs toward the glutes as far as the machine allows; hold briefly at the contracted position
4. Lower under control through the full eccentric — do not let the weight drop

## What the EMG Data Shows

Schoenfeld 2014 (n=13, prone):

| Muscle | Activation |
|--------|-----------|
| Biceps femoris | 80% MVIC |
| Semitendinosus | 65% MVIC |

The biceps femoris generates significantly higher activation than the semitendinosus in the prone position. This biceps femoris dominance is a consistent finding in prone leg curl research.

## Prone vs Seated: Hip Position Matters

The key mechanical difference between lying and seated leg curls is hip angle:
- **Prone (lying)**: Hip at 0° — hamstrings in mid-range length
- **Seated**: Hip at ~90° flexion — hamstrings pre-stretched at proximal end

The seated position places the hamstrings in a more lengthened overall configuration. Both machines train knee flexion, but through different muscle length conditions — making them complementary rather than interchangeable.

## Foot Positioning

Toe rotation affects medial vs lateral hamstring emphasis:
- **Toes forward**: Balanced biceps femoris and semitendinosus
- **Toes in (internal rotation)**: Slightly greater biceps femoris emphasis
- **Toes out (external rotation)**: Slightly greater semitendinosus/semimembranosus emphasis

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/lying_triceps_press.md -->

---
id: lying_triceps_press
name: Lying Triceps Press
status: complete
category: exercise
pattern: [isolation]
equipment: [ez_bar, bench]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 1

muscles:
  - id: triceps_long
    role: primary
  - id: triceps_lateral
    role: primary
  - id: triceps_medial
    role: secondary

# boehler_2011 (normalized to triangle push-up, NOT true %MVIC):
#   triceps_long 70%, triceps_lateral 55%.
# brettler_2023 (TRUE %MVIC at 65% 1RM): ~23.79% (identical protocol to skullcrusher).
# lying_triceps_press and ez_bar_skullcrusher are mechanically nearly identical.
# The distinction: skullcrusher lowers to forehead; lying press lowers behind head (slightly more shoulder flexion).
muscle_activation_studies:
  - source_id: boehler_2011
    doi: null
    n: null
    population: "healthy adults"
    condition:
      implement: ez_bar
      phase: full_rep
      notes: "Normalized to triangle push-up = 100%, NOT true %MVIC. Lying supine, arms overhead."
    measurements:
      - {muscle: triceps_long,    mean_pct_mvc: 70.0, sd: null}
      - {muscle: triceps_lateral, mean_pct_mvc: 55.0, sd: null}
  - source_id: brettler_2023
    doi: null
    n: 8
    population: "trained adults, 65% 1RM"
    condition:
      load_pct_1rm: 65
      implement: ez_bar
      phase: full_rep
      notes: "TRUE %MVIC — lying supine variation"
    measurements:
      - {muscle: triceps_long, mean_pct_mvc: 23.79, sd: 9.19}

joint_rom_required:
  elbow_flexion_deg: 130
  shoulder_flexion_deg: 90
  source: "boehler_2011"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped; essentially identical to skullcrusher in mechanics; lowering behind head adds slight extra long head stretch"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: moderate
    shoulder: low
  common_injuries:
    - structure: distal_triceps_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, dropping_bar, heavy_load, pre_existing_tendinopathy]
  contraindications:
    - acute_triceps_tendinopathy

variations: []
progressions: []
alternatives: [ez_bar_skullcrusher, cable_lying_triceps_extension]

sources:
  - source_id: boehler_2011
    title: "An electromyographic analysis of 3 muscles surrounding the elbow joint during a maximally forceful isometric contraction, concentric isotonic contraction, and 6 common exercises"
    author: "Boehler, Breanna et al."
    year: 2011
    doi: null
    credibility: rct
  - source_id: brettler_2023
    title: "Electromyographic analysis of triceps exercises at various intensities"
    author: "Brettler, S. et al."
    year: 2023
    doi: null
    credibility: rct
---

# Lying Triceps Press

The lying triceps press is performed supine on a flat bench, lowering a bar from fully extended arms overhead to behind the head by bending only the elbows. It is mechanically near-identical to the EZ-bar skullcrusher — the primary distinction is the finish position: the skullcrusher targets the bar to the forehead while the lying press lowers behind the head, slightly increasing shoulder flexion and elongating the triceps long head further at the bottom.

## Execution

1. Lie on a flat bench; hold an EZ-bar at full arm extension overhead, shoulder at ~90° flexion
2. Lower the bar by bending only the elbows, maintaining the upper arms' position
3. Lower to approximately behind the top of the head (not to the forehead)
4. The upper arms may drift slightly back toward the face during lowering; control this with the shoulders
5. Extend the elbows to return to the start

## Relationship to the Skullcrusher

| Feature | Skullcrusher | Lying Triceps Press |
|---------|-------------|---------------------|
| Bar lowered to | Forehead | Behind head |
| Shoulder flexion | ~90° | ~100°+ |
| Long head stretch | Mid-range | Slightly more |
| Elbow stress | Similar | Similar |

For most trainees the difference is minor; choose based on comfort and feel.

## EMG Data Context

The Boehler 2011 data (long 70%, lateral 55%, normalized) is virtually identical to the skullcrusher data from the same study — as expected given the near-identical mechanics. The Brettler 2023 true %MVIC value (23.79%) reflects 65% 1RM dynamic loading.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/one_arm_flat_bench_dumbbell_flye.md -->

---
id: one_arm_flat_bench_dumbbell_flye
name: One-Arm Flat Bench Dumbbell Flye
status: complete
source: free-exercise-db
category: exercise
pattern:
- isolation
equipment:
- dumbbell
difficulty:
  technical_complexity: null
  strength_prerequisite: null
  mobility_prerequisite: null
muscles:
- id: pectoralis_major
  role: primary

muscle_activation_studies: []

joint_rom_required:
  shoulder_horizontal_adduction_deg: 90
  elbow_flexion_deg: 15
  source: "REP Fitness"

strength_curve:
  type: descending
  sticking_point: bottom_third
  peak_force_position: bottom
  notes: "Sticking point and peak force at bottom stretched position; core stabilization demand peaks at bottom where lateral lever arm is longest"

variations: []
progressions: []
alternatives: []
sources:
- title: free-exercise-db
  author: yuhonas (Public Domain)
  credibility: anecdotal
---

# One-Arm Flat Bench Dumbbell Flye

## Execution

1. Lie down on a flat bench with a dumbbell in one hand resting on top of your thigh. The
   palm of your hand with the dumbbell in it should be at a neutral grip.
2. By using your thighs to help you get the dumbbell up, clean the dumbbell so that you can
   hold it in front of you with your lifting arm being fully extended. Remember to
   maintain a neutral grip with this exercise. Your non lifting hand should be to the
   side holding the flat bench for better support. This will be your starting position.
3. Your arm with the weight should have a slight bend on your elbow in order to prevent
   stress at the biceps tendon. Begin by lowering your arm with the weight in it out in
   a wide arc until you feel a stretch on your chest. Breathe in as you perform this
   portion of the movement. Tip: Keep in mind that throughout the movement, your lifting
   arm should remain stationary; the movement should only occur at the shoulder joint.
4. Return your lifting arm back to the starting position as you squeeze your chest muscles
   and breathe out. Tip: Make sure to use the same arc of motion used to lower the
   weights.
5. Hold for a second at the contracted position and repeat the movement for the prescribed
   amount of repetitions.
6. Switch arms and repeat the exercise.


---

<!-- FILE: exercises/overhead_press.md -->

---
id: overhead_press
name: Overhead Press
status: complete
aliases: [OHP, Strict Press, Military Press]
category: exercise
pattern: [vertical press]
muscles:
  - id: deltoid
    role: primary
  - id: triceps_brachii
    role: primary
  - id: pec_major_clavicular
    role: secondary
  - id: core
    role: secondary
equipment: [barbell, rack]
difficulty: intermediate
alternatives: []
muscle_activation_studies:
  - source_id: kettlebell_vs_db_2018
    doi: null
    n: 21
    population: "healthy adults"
    condition:
      implement: dumbbell
      tempo: "2s concentric / 2s eccentric"
      phase: full_rep
    measurements:
      - {muscle: deltoid_anterior, mean_pct_mvc: 63.30, sd: 13.30}
      - {muscle: pectoralis_major, mean_pct_mvc: 31.00, sd: 20.00}
  - source_id: kettlebell_vs_db_2018
    n: 21
    population: "healthy adults"
    condition:
      implement: kettlebell
      tempo: "2s concentric / 2s eccentric"
      phase: full_rep
    measurements:
      - {muscle: deltoid_anterior, mean_pct_mvc: 57.90, sd: 15.00}
  - source_id: marcos_pardo_2020
    doi: null
    n: 13
    population: "strength-trained men"
    condition:
      load_pct_1rm: 60
      reps: 12
      implement: barbell
      style: front_press
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 33.30, sd: null}
      - {muscle: deltoid_lateral,   mean_pct_mvc: 27.90, sd: null}
      - {muscle: deltoid_posterior, mean_pct_mvc: 11.40, sd: null}

joint_rom_required:
  shoulder_flexion_deg: 180
  notes: "Full lockout requires 180° shoulder flexion; scapular upward rotation, elevation, and posterior tilt required; elbows track scapular plane (~30° anterior to frontal plane); peak deltoid anterior moment arm at ~120° shoulder flexion"
  source: "Military Press Technique; Barbell Overhead Press ROM"

strength_curve:
  type: ascending
  sticking_point: mid_range
  peak_force_position: lockout
  notes: "Sticking point between chin and forehead (nose level); bar must arc around face, maximizing horizontal moment arm at glenohumeral joint; resolved when head moves through and bar stacks over shoulder joint"
  source: "Overhead Press Sticking Points review"

sources:
  - title: "Starting Strength"
    author: "Mark Rippetoe"
    credibility: practitioner
  - title: "Kettlebell vs. Dumbbell Overhead Press Study"
    year: 2018
    doi: null
    credibility: rct
  - title: "Electromyographic activity of shoulder muscles during different variations of the shoulder press exercise"
    author: "Marcos-Pardo, P. J., et al."
    year: 2020
    doi: null
    credibility: rct
---

# Overhead Press

The overhead press is a vertical pressing movement, driving a barbell from the front rack overhead to full lockout while standing. It builds shoulder and triceps strength and demands significant core stability.

## Execution

1. Take the bar at shoulder height in a front rack, hands just outside shoulders
2. Brace the core and squeeze the glutes to lock the torso
3. Press the bar straight up, moving the head back slightly to clear the chin
4. Lock out overhead with the bar over the mid-foot, then lower under control

## Common Faults

- **Excessive layback** — turns it into an incline press and stresses the lower back
- **Pressing around the face** — inefficient bar path
- **Soft core** — energy leaks through the trunk

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Push press | Leg drive assists | Overloading the top |
| Seated press | No leg drive | Stricter shoulder work |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/overhead_squat.md -->

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


---

<!-- FILE: exercises/pallof_press.md -->

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


---

<!-- FILE: exercises/parallel_bar_dip.md -->

---
id: parallel_bar_dip
name: Parallel Bar Dip
status: complete
category: exercise
pattern: [vertical_push]
equipment: [bodyweight]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 3
  mobility_prerequisite: 2

muscles:
  - id: triceps_brachii
    role: primary
  - id: pectoralis_major
    role: primary
  - id: deltoid_anterior
    role: secondary
  - id: serratus_anterior
    role: stabilizer

# ebd_2026 literature compilation.
# Condition 1: 75° elbow angle, concentric — triceps head-specific %MVIC.
# Condition 2: 95° elbow angle + 15° forward lean — pectoralis major %MVIC.
# Raw mV value (1.04 ± 0.27 mV) reported in source but NOT stored as mean_pct_mvc —
#   raw mV cannot be compared across subjects; excluded from structured data.
muscle_activation_studies:
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      elbow_angle_deg: 75
      phase: concentric
    measurements:
      - {muscle: triceps_long,    mean_pct_mvc: 55.70, sd: null}
      - {muscle: triceps_lateral, mean_pct_mvc: 41.76, sd: null}
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      elbow_angle_deg: 95
      torso_lean_deg: 15
      notes: "Forward lean increases pectoralis major recruitment"
    measurements:
      - {muscle: pectoralis_major, mean_pct_mvc: 95, sd: null}

joint_rom_required:
  shoulder_extension_deg: 78.20
  elbow_flexion_deg: 90
  notes: >
    Peak shoulder extension 78.20° ± 9.84° at the bottom of the dip. Elbows flex to
    at least 90° at the transition point. Scapulae should remain depressed and retracted
    throughout — avoid shrugging at the top.
  source: "ebd_2026"

strength_curve:
  type: descending
  sticking_point: lower_third
  peak_force_position: bottom
  notes: >
    Hardest at the bottom where the shoulder is in deep extension and the pec and
    triceps are in a maximally lengthened position. Mechanical leverage improves
    rapidly as the lifter presses out of the bottom, with the triceps dominating
    the final lockout.
  source: "ebd_2026"

injury_risk:
  joint_stress:
    shoulder: high
    elbow: low
    wrist: low
  common_injuries:
    - structure: anterior_shoulder_capsule
      mechanism: overstress_at_deep_shoulder_extension
      risk_factors: [excessive_depth_beyond_90_deg_elbow, anterior_shoulder_laxity, heavy_added_weight]
    - structure: pectoralis_major_tendon
      mechanism: eccentric_overload_at_maximum_stretch
      risk_factors: [excessive_depth, heavy_weight_belt, insufficient_warmup]
    - structure: acromioclavicular_joint
      mechanism: internal_rotation_under_load
      risk_factors: [wide_bar_spacing, elbows_flaring_outward]
  contraindications:
    - anterior_shoulder_instability
    - acute_pectoralis_major_tear
    - acromioclavicular_joint_pathology

variations: [ring_dips]
progressions: []
alternatives: []

sources:
  - source_id: ebd_2026
    title: "Exercise Biomechanics Data Extraction: Upper Push Accessories"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Parallel Bar Dip

The parallel bar dip is a closed-chain bodyweight pressing exercise on fixed parallel bars. The lifter supports their full body mass through the upper limbs, lowering by flexing the elbows and extending the shoulders before pressing back to the top. It is one of the most mechanically demanding upper-body pressing exercises per unit of body mass, generating high activation in both the triceps and pectoralis major simultaneously through a deep descending strength curve.

## Execution

1. Mount the bars with arms extended; keep scapulae depressed and retracted — not shrugged
2. Inhale, brace the core; lower by flexing the elbows and extending the shoulders simultaneously
3. Descend until the elbows reach 90° at minimum; lean the torso 15° forward to bias the pectorals
4. Reverse by driving through the palms; extend the elbows fully at the top
5. Control the descent to at least 2 seconds — the bottom position is the highest-risk point

## What the EMG Data Shows

The dip's primary advantage is the simultaneous high demand on both the triceps and pectoralis major:

**Triceps head activation at 75° elbow flexion (concentric)**: The long head leads at 55.70% MVIC, with the lateral head at 41.76% MVIC. The long head dominance occurs because at 90°+ shoulder extension, the long head's moment arm for elbow extension is optimal — it is a biarticular muscle crossing both the shoulder and elbow, contributing to both joint actions simultaneously.

**Pectoralis major at 95° elbow / 15° forward lean**: Activation reaches 95% MVIC. The forward lean is critical: upright torso shifts the load almost entirely to the triceps; a 15° forward lean brings the pec into primary engagement. Most trainees should lean slightly forward throughout the descent to share load between the triceps and pec.

The isometric phase (transitioning between eccentric and concentric) at a 75° elbow angle shows greater lateral head triceps activation than at 95°, indicating the lateral head preferentially activates at the more flexed (deeper) position — making the bottom of the dip the primary trigger for lateral head recruitment.

## Parallel Bar vs Ring Dip

The parallel bar dip allows a deeper shoulder extension (78.20°) than the ring dip (61.72°) — 27% greater extension due to the stable fixed bar. This produces a more demanding eccentric load at the bottom but also increases anterior shoulder risk. The ring dip imposes greater pectoralis major demand as an adductor throughout the movement; the bar dip produces a cleaner descending strength curve. See [ring_dips.md](ring_dips.md) for the comparative analysis.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Ring dips | Unstable; reduced shoulder extension; pec adduction demand | Advanced ring skill development; pec emphasis |
| Weighted dips | External load via belt or vest | Strength progression past bodyweight |
| Bench dips | Hands on bench behind; feet elevated | Lower strength requirement; triceps isolation |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/plank.md -->

---
id: plank
name: Plank
status: complete
category: exercise
pattern: [isolation]
equipment: [bodyweight]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: rectus_abdominis
    role: primary
  - id: external_oblique
    role: primary
  - id: internal_oblique
    role: secondary
  - id: transverse_abdominis
    role: secondary
  - id: erector_spinae
    role: stabilizer
  - id: multifidus
    role: stabilizer

# McGill 2010 literature review values; forearm plank sustained hold.
# Values reported as %MVC (maximum voluntary contraction) — treat as equivalent
# to %MVIC for indexing. No single DOI for forearm plank; these represent
# averages across McGill's laboratory studies compiled in the 2010 review.
muscle_activation_studies:
  - source_id: mcgill_2010
    doi: "10.1519/SSC.0b013e3181df4521"
    n: null
    population: "mixed cohorts, laboratory compilation"
    condition:
      position: forearm_plank
      phase: sustained_isometric
    measurements:
      - {muscle: rectus_abdominis, mean_pct_mvc: 50.0, sd: null}
      - {muscle: external_oblique, mean_pct_mvc: 49.0, sd: null}
      - {muscle: erector_spinae,   mean_pct_mvc: 35.0, sd: null}

joint_rom_required:
  notes: "Static isometric hold; no dynamic ROM threshold. Requires the ability to maintain lumbar neutral in a prone-supported position. Ankle plantarflexion needed for toes-only contact point."
  source: "McGill 2010"

strength_curve:
  type: isometric
  sticking_point: null
  peak_force_position: null
  notes: "No dynamic force curve — the plank is a timed static hold. Difficulty scales with lever arm length (elevating feet, raising one limb) or duration, not with load."
  source: "McGill 2010"

injury_risk:
  joint_stress:
    lumbar: low
    shoulder: low
  common_injuries:
    - structure: lumbar_spine
      mechanism: extension_under_compressive_load
      risk_factors: [sagging_hips, breath_holding_increasing_intra_abdominal_pressure, exceeding_duration_before_technique_breaks]
    - structure: glenohumeral_joint
      mechanism: impingement
      risk_factors: [internal_rotation_of_shoulder_during_elbow_plank, excessive_duration_with_protracted_scapulae]
  contraindications:
    - acute_lumbar_disc_herniation

variations: []
progressions: []
alternatives: [dead_bug]

sources:
  - source_id: mcgill_2010
    title: "Core Training: Evidence Translating to Better Performance and Injury Prevention"
    author: "McGill, S. M."
    year: 2010
    doi: "10.1519/SSC.0b013e3181df4521"
    credibility: literature_review
---

# Plank

The plank is an isometric anti-extension core exercise performed in a prone-supported position on the forearms and toes. The goal is to resist lumbar extension and maintain a rigid, straight line from heels to crown. It is the foundational movement for anti-extension core training and a prerequisite for more demanding progressions.

## Execution

1. Place the forearms flat on the floor, elbows directly below the shoulders, forearms parallel or hands clasped
2. Extend the legs back, supporting only on the toes; feet hip-width apart
3. Brace the entire midsection — contract the glutes, squeeze the quads, and create tension through the torso
4. Align the body from heels to ears in a single plane; do not let the hips sag or pike up
5. Breathe steadily; do not hold the breath, which dramatically increases spinal compressive load
6. Hold the position; terminate the set when lumbar neutral cannot be maintained

## What the EMG Data Shows

McGill's laboratory work shows the forearm plank produces moderate bilateral activation across the core musculature: rectus abdominis (~50% MVC), external oblique (~49% MVC), and lumbar erector spinae (~35% MVC). These values are lower than many dynamic exercises but are produced simultaneously and held continuously — the cumulative spinal stability demand is the training stimulus, not peak activation.

The transverse abdominis and multifidus contribute to segmental stiffness but are not captured by surface EMG in these studies; their contribution is inferred from spinal stability models.

## Common Faults and Corrections

| Fault | Effect | Fix |
|-------|--------|-----|
| Hips sagging | Lumbar hyperextension; compressive stress | Drive hips up until the body is flat; squeeze glutes harder |
| Hips piked up | Reduces core demand; becomes a shoulder exercise | Lower hips until heels, hips, and shoulders are level |
| Breath holding | Spikes intra-abdominal pressure; increases lumbar compression | Breathe slowly throughout the hold |
| Protracted scapulae | Shoulder impingement risk | Depress and slightly retract the shoulder blades; "pull shoulders away from ears" |

## Progressions

The plank is not made harder by simply holding longer — once 60 seconds can be maintained with perfect form, progression should increase the mechanical demand:

1. **Feet-elevated plank** — elevating the feet increases the lever arm and shifts more load anteriorly
2. **Single-arm or single-leg plank** — reduces the base of support, creating rotational demand
3. **RKC (Hardstyle) Plank** — maximal full-body co-contraction superimposed on the hold; dramatically increases core activation at shorter durations
4. **Ab Wheel Rollout** — transforms the anti-extension demand from static to dynamic

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/power_clean.md -->

---
id: power_clean
name: Power Clean
status: complete
category: exercise
pattern: [hinge]
equipment: [barbell]

difficulty:
  technical_complexity: 5
  strength_prerequisite: 3
  mobility_prerequisite: 4

muscles:
  - id: vastus_lateralis
    role: primary
  - id: gluteus_maximus
    role: primary
  - id: erector_spinae
    role: primary
  - id: multifidus
    role: primary
  - id: trap_upper
    role: primary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: rectus_femoris
    role: secondary
  - id: vastus_medialis
    role: secondary
  - id: deltoid_anterior
    role: secondary
  - id: gastrocnemius
    role: secondary
  - id: soleus
    role: secondary
  - id: forearm_flexors
    role: stabilizer
  - id: rhomboids
    role: stabilizer

# Geisler 2023: Hang Power Clean (HPC) across three expertise levels and three loads.
# %MVIC values are for the pull phase only; catch phase adds eccentric stabilisation demand.
# Do NOT average across expertise levels — motor unit synchronisation differs substantially.
muscle_activation_studies:
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 50
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 163.82, sd: 64.41}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 124.91, sd: 76.67}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 70
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 208.20, sd: 113.02}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 99.50,  sd: 56.46}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 90
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 203.96, sd: 119.85}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 10
    population: "advanced"
    condition:
      load_pct_1rm: 50
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 247.70, sd: 259.48}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 97.20,  sd: 37.72}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 10
    population: "advanced"
    condition:
      load_pct_1rm: 70
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 321.09, sd: 367.87}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 107.70, sd: null}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 10
    population: "advanced"
    condition:
      load_pct_1rm: 90
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 307.97, sd: 288.30}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 50
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 324.41, sd: 305.15}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 298.74, sd: 195.54}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 70
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 248.37, sd: 221.22}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 186.84, sd: null}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 90
      phase: pull
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 249.30, sd: 213.53}

joint_rom_required:
  hip_flexion_deg: 120
  knee_flexion_deg: 90
  ankle_dorsiflexion_deg: 20
  shoulder_flexion_deg: 173
  shoulder_external_rotation_deg: 107
  shoulder_internal_rotation_deg: 89
  notes: "Setup: 120° hip flexion. Front-rack catch: 90° knee flexion, 173° shoulder flexion, 107°/89° ER/IR"
  source: "nasm_2020 / crossfit_2022"

strength_curve:
  type: bell_shaped
  sticking_point: first_pull_to_transition
  peak_force_position: second_pull
  notes: >
    GRF profile: first pull ~1.5×BW, unweighting (double-knee bend) ~1.0×BW,
    second pull peak 2.0–2.5×BW. Floor-start: peak GRF 2306±388 N,
    instantaneous RFD 8840±2940 N/s (Kawamori 2005).
    VL and GM activation is statistically equivalent between power clean and clean pull
    at loads ≥70% 1RM — the catch adds eccentric demand, not additional concentric power.
  source: "kawamori_2005 / geisler_2023"

injury_risk:
  joint_stress:
    wrist: high
    elbow: moderate
    lower_back: moderate
  common_injuries:
    - structure: wrist_extensors
      mechanism: forced_extension_on_catch
      risk_factors: [insufficient_shoulder_er, poor_front_rack_mobility]
    - structure: lumbar_disc
      mechanism: shear_under_load
      risk_factors: [bar_drifting_away_from_body, poor_bracing]
  contraindications:
    - acute_wrist_injury
    - acute_shoulder_impingement

variations: [clean_and_jerk, clean_pull]
progressions: [clean_pull]
alternatives: []

sources:
  - source_id: geisler_2023
    title: "Effects of Expertise on Muscle Activity during the Hang Power Clean and Hang Power Snatch Compared to Snatch and Clean Pulls"
    author: "Geisler S et al."
    year: 2023
    doi: "10.52082/jssm.2023.778"
    credibility: rct
  - source_id: kawamori_2005
    title: "Comparisons of Peak Ground Reaction Force and Rate of Force Development During Variations of the Power Clean"
    author: "Kawamori N et al."
    year: 2005
    doi: "10.1519/00124278-200508000-00011"
    credibility: rct
  - source_id: nasm_2020
    title: "NASM Optimum Performance Training"
    author: "National Academy of Sports Medicine"
    year: 2020
    credibility: expert_consensus
---

# Power Clean

The power clean is an Olympic weightlifting derivative in which the barbell is pulled from the floor and caught on the anterior shoulders in a partial squat (≥90° knee flexion). It is the most widely programmed catching derivative in athletic conditioning, training explosive triple extension — simultaneous hip, knee, and ankle extension at peak velocity.

## Execution

1. **Setup:** Feet hip-width, bar over mid-foot. Hips below shoulders, shoulders over or slightly in front of bar. Neutral spine, 120° hip flexion, elbows fully extended, pronated hook grip just outside the knees.
2. **First pull (floor to knee):** Drive hips and knees simultaneously; maintain constant back angle. Bar stays against the shins.
3. **Transition (double-knee bend):** As bar passes the knees, knees re-bend and hips push forward; torso angle becomes more upright.
4. **Second pull (triple extension):** Forceful simultaneous extension of hips, knees, and ankles; shrug at full extension.
5. **Catch:** Elbows rotate rapidly under the bar; receive in front-rack position — elbows high and parallel to floor, bar resting on anterior deltoids, ≥90° knee flexion.
6. **Recovery:** Extend hips and knees to standing; lower bar under control.

## What the EMG Data Shows

The pull phase is dominated by vastus lateralis (VL) and gluteus maximus (GM). Beginners at 50% 1RM: VL 164% MVIC, GM 125% MVIC. Elite athletes at the same relative load: VL 324% MVIC, GM 299% MVIC — reflecting superior motor unit synchronisation rather than greater absolute force.

Critically, VL and GM activation is statistically equivalent between the power clean and the clean pull at loads ≥70% 1RM (Geisler 2023). The pulling phase produces an identical concentric extension stimulus whether or not a catch follows. The catch adds eccentric stabilisation demand on the wrist, elbow, and shoulder girdle — not additional triple-extension power.

VL activation at elite level does not increase monotonically from 70% to 90% 1RM (248 → 249% MVIC), suggesting motor efficiency plateaus at high expertise and that load increases beyond ~70% produce diminishing neuromuscular returns for the pull.

## Front-Rack Mobility Requirements

The catch position requires specific mobility cut-points that are frequently under-screened. Deficits force the bar onto the anterior deltoid or clavicle, creating wrist and elbow torque and causing the fingers to release:

- Shoulder flexion: ≥173°
- Shoulder external rotation: ≥107°; internal rotation: ≥89°
- Elbow flexion: ≥135°; pronation: ≥90°
- Wrist extension: ≥90°

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Hang power clean | Starts from mid-thigh or knee | Learning the second pull; reduced first-pull complexity |
| Clean (full) | Catch in full squat | Maximising load; competitive weightlifting |
| Clean pull | No catch phase | Overload training; athletes with restricted front-rack mobility |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/power_jerk.md -->

---
id: power_jerk
name: Power Jerk
status: complete
category: exercise
pattern: [vertical press]
equipment: [barbell]

difficulty:
  technical_complexity: 4
  strength_prerequisite: 3
  mobility_prerequisite: 4

muscles:
  - id: gluteus_maximus
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: rectus_femoris
    role: primary
  - id: vastus_medialis
    role: primary
  - id: triceps_brachii
    role: primary
  - id: deltoid_anterior
    role: secondary
  - id: trap_upper
    role: secondary
  - id: gastrocnemius
    role: secondary
  - id: soleus
    role: secondary
  - id: erector_spinae
    role: stabilizer
  - id: gluteus_medius
    role: stabilizer

# No peer-reviewed EMG %MVIC study found for the power jerk.
# Muscle activation pattern is inferred from structural similarity to push_press
# (dip-drive-overhead sequence) with the difference that the power jerk includes
# a receiving catch in a partial squat, adding eccentric quadriceps demand.
muscle_activation_studies: []

joint_rom_required:
  knee_flexion_dip_deg: 15
  knee_flexion_catch_deg: 90
  hip_flexion_catch_deg: 45
  ankle_dorsiflexion_deg: 20
  shoulder_flexion_deg: 180
  shoulder_external_rotation_deg: 90
  notes: >
    Dip: only 10–15° knee flexion; hips remain directly under bar.
    Catch (power receive): ~90° knee flexion, ~45° hip flexion in a shallow squat.
    Overhead lockout: 180° shoulder flexion required; elbow full extension.
    Overhead mobility is the limiting factor — insufficient shoulder flexion forces
    the bar to land behind the midfoot, creating an unstable receive position.
  source: "everett_weightlifting / crossfit_2022"

strength_curve:
  type: bell_shaped
  sticking_point: dip_reversal
  peak_force_position: drive_phase_peak
  notes: >
    The jerk GRF profile is a sharp impulse: brief eccentric dip (~10–15° knee flexion),
    maximal concentric drive (peak GRF 2.5–3.0×BW), then an eccentric landing phase
    as the feet shift and the arms receive the bar.
    The sticking point is the dip-to-drive reversal — any forward hip displacement
    during the dip shifts the bar forward off the shoulders, making the drive
    mechanically inefficient. The drive must be perfectly vertical.
    Unlike the push press (which continues pressing through the top), the power jerk
    drive terminates at full extension and the lifter drops under the bar, requiring
    precise timing of the re-squat.
  source: "garhammer_1993 / everett_weightlifting"

injury_risk:
  joint_stress:
    shoulder: high
    knee: moderate
    lower_back: low
  common_injuries:
    - structure: rotator_cuff
      mechanism: eccentric_overload_at_overhead_catch
      risk_factors: [insufficient_shoulder_flexion, fatigue, bar_forward_of_midfoot_at_receive]
    - structure: glenohumeral_joint
      mechanism: anterior_impingement
      risk_factors: [internal_rotation_at_lockout, insufficient_thoracic_extension]
    - structure: knee
      mechanism: valgus_in_squat_catch
      risk_factors: [fatigue, heavy_load_with_weak_hip_abductors, restricted_ankle_dorsiflexion]
  notes: "The power jerk is safer than the split jerk for athletes with limited hip mobility; the symmetric squat receive is easier to stabilise than the split. However, the partial squat catch places substantial quadriceps eccentric demand at ~90° knee flexion — a high-torque position."
  contraindications:
    - acute_shoulder_injury
    - acute_knee_injury

variations: [push_press]
progressions: []
alternatives: [push_press, overhead_press]

sources:
  - source_id: garhammer_1993
    title: "A Review of Power Output Studies of Olympic and Powerlifting: Methodology, Performance Prediction, and Evaluation Tests"
    author: "Garhammer, J."
    year: 1993
    doi: "10.1519/1533-4287(1993)007<0076:AROPOS>2.3.CO;2"
    credibility: literature_review
  - source_id: everett_weightlifting
    title: "Olympic Weightlifting: A Complete Guide for Athletes & Coaches"
    author: "Greg Everett"
    year: 2016
    doi: null
    credibility: practitioner
  - source_id: crossfit_2022
    title: "Olympic Weightlifting Movement Standards"
    author: "CrossFit Training"
    year: 2022
    doi: null
    credibility: practitioner
---

# Power Jerk

The power jerk is a jerk variation in which the bar is driven from the front rack to overhead using an explosive leg drive (dip-drive), and received with both feet moving to a slightly wider stance in a partial squat (≥90° knee angle at receive). It differs from the split jerk — the standard competition style — in that the receive position is symmetric rather than split. It is primarily used as a teaching progression to establish overhead barbell stability and dip-drive mechanics before introducing the asymmetric split position.

## Execution

1. **Front rack:** Barbell rests on the anterior deltoids with elbows high and parallel to the floor; same position as the front squat rack. Feet hip-width, core braced.
2. **Dip:** Flex the knees approximately 10–15° with a controlled, vertical descent. The hips stay directly under the bar — do not allow the torso to incline forward or the hips to push backward. This is the most commonly broken technical point.
3. **Drive:** Immediately reverse the dip with maximum force. Extend hips, knees, and ankles explosively. The bar leaves the shoulders driven entirely by the legs and momentum — do not initiate a press from the shoulders.
4. **Drop:** As the bar reaches peak height, push the body downward by pressing the arms into full lockout overhead. Move the feet slightly wider (approximately hip-width) as the body drops into the partial squat catch.
5. **Receive:** Lock the elbows completely before the feet re-contact the floor. Bar must be over the midfoot with the torso upright; hips and knees in the partial squat (~90° knee flexion).
6. **Recover:** Stand by extending hips and knees while keeping the bar locked overhead; return feet to hip-width.

## Power Jerk vs Push Press vs Split Jerk

| Feature | Push Press | Power Jerk | Split Jerk |
|---------|-----------|------------|------------|
| Leg drive | Yes (drives bar) | Yes (drives bar) | Yes (drives bar) |
| Receive position | Standing (no drop) | Symmetric partial squat | Split stance |
| Overhead stability | Stationary catch | Symmetric squat | Asymmetric split |
| Maximum load | Moderate | High | Highest |
| Technical demand | Lower | Moderate | High |

The push press does not involve dropping under the bar — the lifter stands and presses through. The power jerk drops under the bar into a receive position, allowing heavier loads because the bar needs to travel a shorter vertical distance before being caught. The split jerk allows the heaviest loads of the three by providing the deepest possible drop under the bar.

## The Dip: The Critical Phase

The dip is the most commonly faulted phase. Two errors eliminate the effectiveness of the jerk drive:

1. **Forward torso inclination during the dip** — shifts the bar forward off the anterior deltoids onto the wrists, making the drive non-vertical. The bar follows the torso angle; a forward-inclined dip produces a forward bar trajectory that cannot be received over the midfoot.

2. **Hip travel backward during the dip** — same effect: the hips moving back shift the center of mass and produce a non-vertical bar path. The cue "dip straight down, not back" corrects this.

A correctly executed dip is indistinguishable from a vertical piston movement: the bar and the hips travel down the same vertical line and reverse direction together.

## The Drive-to-Drop Transition

The window between the end of the leg drive and the overhead catch is where timing determines success. At full extension:
- The bar has peak upward velocity
- The legs are no longer in contact with the floor (brief weightless phase in maximal efforts)
- The feet must relocate to the slightly wider receive stance before the bar reaches peak height

Practicing the footwork pattern without load — "dip, drive, stomp" — builds the motor pattern before load is introduced.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/power_snatch.md -->

---
id: power_snatch
name: Power Snatch
status: complete
category: exercise
pattern: [hinge]
equipment: [barbell]

difficulty:
  technical_complexity: 5
  strength_prerequisite: 3
  mobility_prerequisite: 5

muscles:
  - id: erector_spinae
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: gluteus_maximus
    role: primary
  - id: multifidus
    role: primary
  - id: trap_upper
    role: primary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: rectus_femoris
    role: secondary
  - id: vastus_medialis
    role: secondary
  - id: deltoid_anterior
    role: secondary
  - id: triceps_brachii
    role: secondary
  - id: gastrocnemius
    role: secondary
  - id: soleus
    role: secondary
  - id: forearm_flexors
    role: stabilizer

# Geisler 2023: Hang Power Snatch (HPS) across three expertise levels and two loads.
# Phase: pull_and_catch — ES values include both pull and overhead catch demands.
# The catch is responsible for the majority of the ES elevation vs the snatch pull.
# At elite level, catch-phase ES significantly exceeds snatch pull (p < 0.05).
muscle_activation_studies:
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 50
      phase: pull_and_catch
    measurements:
      - {muscle: trap_upper,     mean_pct_mvc: 71.69, sd: 23.21}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 10
    population: "advanced"
    condition:
      load_pct_1rm: 50
      phase: pull_and_catch
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 175.69, sd: 134.95}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 50
      phase: pull_and_catch
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 294.28, sd: 152.77}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 90
      phase: pull_and_catch
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 215.68, sd: 321.69}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 90
      phase: pull_and_catch
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 371.62, sd: 271.60}

joint_rom_required:
  hip_flexion_deg: 120
  knee_flexion_deg: 90
  ankle_dorsiflexion_deg: 20
  shoulder_flexion_deg: 180
  shoulder_external_rotation_deg: 90
  shoulder_internal_rotation_deg: 70
  notes: "Setup: 120° hip flexion. Overhead catch: 180° shoulder flexion, 90°/70° ER/IR required for stable lockout"
  source: "nasm_2020 / setpt_2020"

strength_curve:
  type: bell_shaped
  sticking_point: first_pull_to_transition
  peak_force_position: second_pull
  notes: >
    Wider snatch grip shortens effective pull height vs clean grip, requiring greater
    barbell velocity to achieve a successful catch. Peak power at 45–65% 1RM.
    Under repeated fatiguing reps, athletes increase spinal stiffness (L5-S1 extension
    decreases significantly, p=0.03) to protect passive lumbar tissues — a healthy
    protective neural strategy.
    Catch-phase ES at elite level (372% MVIC at 90% 1RM) is ~76% greater than the
    snatch pull (212% MVIC) — the overhead eccentric stabilisation is the defining demand.
  source: "geisler_2023 / jsc_2013"

injury_risk:
  joint_stress:
    shoulder: high
    wrist: high
    lower_back: high
  common_injuries:
    - structure: rotator_cuff
      mechanism: eccentric_overload_at_catch
      risk_factors: [insufficient_shoulder_flexion, restricted_thoracic_extension]
    - structure: lumbar_disc
      mechanism: hyperextension_during_catch
      risk_factors: [excessive_lordosis, poor_bracing]
  contraindications:
    - acute_shoulder_injury
    - lumbar_herniation

variations: [snatch_pull]
progressions: [overhead_squat]
alternatives: []

sources:
  - source_id: geisler_2023
    title: "Effects of Expertise on Muscle Activity during the Hang Power Clean and Hang Power Snatch Compared to Snatch and Clean Pulls"
    author: "Geisler S et al."
    year: 2023
    doi: "10.52082/jssm.2023.778"
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
---

# Power Snatch

The power snatch is the snatch family's catching derivative. The barbell is pulled from the floor with a wide (snatch) grip and received overhead in a partial squat (≥90° knee flexion). It is the highest-mobility-demand movement in standard strength training, requiring 180° of shoulder flexion and stable overhead control throughout the catch.

## Execution

1. **Setup:** Feet hip-width, bar over mid-foot, wide snatch grip (roughly 1.5× shoulder width). 120° hip flexion, neutral spine. Shins and torso roughly parallel to each other.
2. **First pull (floor to knee):** Drive hips and knees; maintain back angle. Bar stays against the shins.
3. **Transition (double-knee bend):** As bar passes the knees, knees re-bend and hips push forward.
4. **Second pull (triple extension):** Explosive hip, knee, and ankle extension; shrug at peak. Wider grip requires higher peak barbell velocity than the clean grip to achieve the catch position.
5. **Catch:** Arms press out and up, receiving the bar locked overhead with elbows fully extended. Hips and knees flex to ≥90°. Requires 180° shoulder flexion to keep the bar over the midfoot.
6. **Recovery:** Stand by extending hips and knees while maintaining the overhead bar position.

## What the EMG Data Shows

The defining feature of the power snatch versus the snatch pull is the massive erector spinae demand at the catch. Elite athletes at 90% 1RM show ES activation of 372% MVIC during the power snatch versus 212% MVIC during the snatch pull (p < 0.05, Geisler 2023). This ~76% difference represents the eccentric stabilisation cost of arresting a high-velocity barbell overhead — the spinal erectors must decelerate trunk extension through the catch.

Under repeated fatiguing repetitions, athletes adopt a protective neural strategy: L5-S1 intervertebral extension decreases significantly (p = 0.03) as fatigue accumulates, reflecting increased spinal stiffness to protect passive lumbar tissue. Technical failure in this protective mechanism is the injury pathway.

Upper trapezius (beginners, 50% 1RM: 72% MVIC) elevates the shoulder girdle during the shrug and assists in pulling the body under the bar.

## Overhead Catch Mobility Requirements

These are the strictest mobility demands in strength training. Restrictions force a forward bar displacement that cannot be recovered mid-lift:

- Shoulder flexion: ≥180°
- Shoulder external rotation: ≥90°; internal rotation: ≥70°
- Thoracic extension to maintain bar over the midfoot

Shoulder flexibility correlates significantly with trunk angle at the bottom position (r = −0.67, p = 0.003): restricted shoulders force a compensatory forward trunk lean that shifts the bar forward and destabilises the catch.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Snatch pull | No catch phase | Overload training (100–140% snatch 1RM); reduced shoulder demand |
| Snatch (full) | Catch in full squat | Maximising load; competitive weightlifting |
| Overhead squat | No pull; static overhead | Mobility screening; catch-position conditioning |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/preacher_curl.md -->

---
id: preacher_curl
name: Preacher Curl
status: complete
category: exercise
pattern: [isolation]
equipment: [barbell, ez_bar]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: biceps_brachii
    role: primary
  - id: brachialis
    role: secondary
  - id: brachioradialis
    role: secondary

# porcari_2014 (n=16): biceps_brachii 88.8% MVIC.
# oliveira_2009: biceps_brachii ~80% MVIC.
# ROM: 115.5° elbow flexion — reduced vs barbell curl (144.6°) due to pad limiting extension.
# Shoulder flexion ~50° — places the biceps long head at shorter length than neutral curls.
# Strength curve: ASCENDING — hardest at the bottom (extended position) where the biceps is longest.
muscle_activation_studies:
  - source_id: porcari_2014
    doi: null
    n: 16
    population: "healthy adults, standardized load"
    condition:
      implement: ez_bar
      phase: full_rep
      notes: "Upper arms resting on preacher pad; shoulder ~50° flexion"
    measurements:
      - {muscle: biceps_brachii, mean_pct_mvc: 88.8, sd: null}
  - source_id: oliveira_2009
    doi: null
    n: null
    population: "general population"
    condition:
      implement: barbell
      phase: full_rep
    measurements:
      - {muscle: biceps_brachii, mean_pct_mvc: 80.0, sd: null}

joint_rom_required:
  elbow_flexion_deg: 116
  shoulder_flexion_deg: 50
  source: "Marcolin 2018"

strength_curve:
  type: ascending
  sticking_point: bottom_third
  peak_force_position: bottom
  notes: "Hardest at the bottom of the range where the elbow is most extended and gravity moment arm is near maximum — opposite of the free-standing curl's bell curve"
  source: "Marcolin 2018"

injury_risk:
  joint_stress:
    elbow: moderate
    wrist: low
  common_injuries:
    - structure: distal_biceps_tendon
      mechanism: eccentric_overload_at_full_extension
      risk_factors: [dropping_weight_at_bottom, locking_out_fully, heavy_load, pre_existing_tendinopathy]
    - structure: biceps_tendon_long_head
      mechanism: stretch_overload
      risk_factors: [hyperextending_at_bottom, pre_existing_tendinopathy]
  contraindications:
    - acute_distal_biceps_tendinopathy
    - elbow_hyperextension_injury

variations: []
progressions: []
alternatives: [cable_preacher_curl, barbell_curl]

sources:
  - source_id: porcari_2014
    title: "ACE-Sponsored Research: Best Biceps Exercises"
    author: "Porcari, John P. et al. (ACE)"
    year: 2014
    doi: null
    credibility: rct
  - source_id: oliveira_2009
    title: "EMG analysis of biceps brachii in curl variations"
    author: "Oliveira, Leal et al."
    year: 2009
    doi: null
    credibility: rct
  - source_id: marcolin_2018
    title: "Differences in electromyographic activity of biceps brachii and brachioradialis while performing three variants of curl"
    author: "Marcolin, Giuseppe et al."
    year: 2018
    doi: null
    credibility: rct
---

# Preacher Curl

The preacher curl places the upper arms against an angled pad with the shoulders flexed approximately 50°. This configuration reduces the available elbow flexion ROM to ~115° (vs 145° for standing curls) and shifts the resistance curve to ascending — the hardest point is at the bottom where the elbow is most extended. The preacher curl emphasizes the lengthened biceps position more than free-standing curls, making it a complementary stimulus rather than a substitute.

## Execution

1. Adjust the preacher bench so the top of the pad is at armpit height when seated
2. Rest the upper arms flat against the pad, shoulder slightly in front of the pad's top edge
3. Hold the EZ-bar or barbell at full arm extension (do not lock out completely)
4. Curl to the top — do not allow the upper arms to lift off the pad
5. Lower slowly and under control; do not bounce at the bottom — this is where distal biceps tendon injury risk is highest

## What the EMG Data Shows

| Study | Biceps Activation |
|-------|-------------------|
| Porcari 2014 | 88.8% MVIC |
| Oliveira 2009 | 80.0% MVIC |

The preacher curl activates less than concentration curls (97.9%) but more than the barbell curl (76.5%) — a counterintuitive result explained by the ascending strength curve: the harder bottom position demands more muscle force at maximum stretch.

## The Ascending Strength Curve

The preacher curl is one of few curl exercises where the ascending curve is pronounced. This is mechanically different from the bell-shaped barbell curl:

- **Barbell curl**: easiest at bottom and top; hardest at 90° elbow flexion
- **Preacher curl**: hardest at the bottom; progressively easier through the concentric

The practical implication: preacher curls are uniquely suited for training the biceps under load in the most stretched position, consistent with evidence that lengthened-position loading enhances hypertrophy stimulus.

## Injury Warning

The bottom position (full elbow extension against load) concentrates tensile stress on the distal biceps tendon. Do not allow the weight to drop through the eccentric or hyperextend the elbow. Trainees with pre-existing distal biceps tendinopathy should use cable preacher curls, which maintain constant tension without the hard stop at the bottom.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/pullups.md -->

---
id: pullups
name: Pull-Up
status: complete
category: exercise
pattern: [vertical_pull]
equipment: [bodyweight]

difficulty:
  technical_complexity: 3
  strength_prerequisite: 3
  mobility_prerequisite: 1

muscles:
  - id: latissimus_dorsi
    role: primary
  - id: infraspinatus
    role: primary
  - id: teres_major
    role: secondary
  - id: biceps_brachii
    role: secondary
  - id: trap_lower
    role: secondary
  - id: pectoralis_major
    role: secondary
  - id: deltoid_posterior
    role: secondary
  - id: rhomboids
    role: secondary
  - id: erector_spinae
    role: stabilizer
  - id: external_oblique
    role: stabilizer

# ssd_2026 is a literature compilation (no single DOI) aggregating multiple EMG studies.
# Values for pronated pull-up: LD range 117–130% MVIC; midpoint 123.5 stored as mean.
# Chin-up data included as a separate condition for comparison, not as a separate exercise.
# No SD reported for erector_spinae and external_oblique (range only).
muscle_activation_studies:
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation — multiple study populations"
    condition:
      grip: pronated
      width: shoulder-width
      notes: "Conventional pull-up"
    measurements:
      - {muscle: latissimus_dorsi, mean_pct_mvc: 123.5, sd: null, notes: "Range 117–130% MVIC across studies"}
      - {muscle: biceps_brachii,   mean_pct_mvc: 78.0,  sd: 32.0}
      - {muscle: infraspinatus,    mean_pct_mvc: 79.0,  sd: 56.0}
      - {muscle: trap_lower,       mean_pct_mvc: 56.0,  sd: 21.0}
      - {muscle: pectoralis_major, mean_pct_mvc: 44.0,  sd: 27.0}
      - {muscle: erector_spinae,   mean_pct_mvc: 40.0,  sd: null, notes: "Isometric stabilization; range 39–41% MVIC"}
      - {muscle: external_oblique, mean_pct_mvc: 33.0,  sd: null, notes: "Isometric stabilization; range 31–35% MVIC"}
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation — multiple study populations"
    condition:
      grip: supinated
      width: shoulder-width
      notes: "Chin-up"
    measurements:
      - {muscle: latissimus_dorsi, mean_pct_mvc: 117.0, sd: 46.0}
      - {muscle: biceps_brachii,   mean_pct_mvc: 96.0,  sd: 34.0}
      - {muscle: trap_lower,       mean_pct_mvc: 45.0,  sd: 22.0}
      - {muscle: pectoralis_major, mean_pct_mvc: 57.0,  sd: 36.0}

joint_rom_required:
  shoulder_flexion_deg: 180
  elbow_flexion_deg: 93.4
  elbow_flexion_chinup_deg: 100.6
  scapular_upward_rotation_deg: 60
  glenohumeral_contribution_deg: 120
  notes: >
    Full overhead shoulder flexion (180°) required to achieve dead-hang start.
    Chin-up requires greater terminal elbow flexion (100.6° vs 93.4°) because the
    supinated grip keeps the elbows in the sagittal plane, maximizing terminal ROM.
    Scapulothoracic joint contributes 60° of upward rotation; glenohumeral joint 120°.
  source: "ssd_2026"

strength_curve:
  type: descending
  sticking_point: top_third
  peak_force_position: bottom_third
  notes: >
    Peak force generation occurs in the bottom third of the movement where the
    latissimus dorsi operates at its optimal length-tension relationship with its
    greatest moment arm. The primary sticking point is the top third, when the
    humerus is fully extended and adducted — the primary shoulder extensors suffer
    active insufficiency and secondary muscles must compensate to pull the chest to the bar.
  source: "ssd_2026"

injury_risk:
  joint_stress:
    shoulder: moderate
    elbow: low
  common_injuries:
    - structure: biceps_brachii_tendon
      mechanism: eccentric_overload_at_full_extension
      risk_factors: [excessive_eccentric_velocity, high_volume_fatigue, cold_muscles]
    - structure: glenohumeral_joint
      mechanism: impingement
      risk_factors: [inadequate_scapular_depression_at_top, kipping_technique, forward_head_posture]
    - structure: medial_elbow_common_flexor_tendon
      mechanism: repetitive_valgus_stress
      risk_factors: [wide_grip, high_frequency, insufficient_recovery]
  contraindications:
    - acute_biceps_tendon_rupture
    - shoulder_labral_tear_acute
    - medial_epicondylitis_acute

variations: []
progressions: [weighted_pull_ups]
alternatives: [chin_up]

sources:
  - source_id: ssd_2026
    title: "Sports Science Data Extraction: Vertical Pulling and Horizontal Rowing"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Pull-Up

The pull-up is a closed-chain vertical pulling exercise in which the body hangs from a fixed overhead bar with a pronated (overhand) grip and is pulled upward until the chin clears the bar or the chest contacts it. As one of the few upper-body exercises that requires moving the entire bodyweight through a full range of motion against gravity, it serves as both a strength benchmark and a primary latissimus dorsi developer.

## Execution

1. Hang from the bar with a pronated (palms-away) double-overhand grip, hands approximately shoulder-width apart
2. Before initiating the pull, depress and retract the scapulae slightly — avoid passive hanging with the shoulders near the ears
3. Initiate the pull by driving the elbows down and back, thinking "elbows to hips" rather than "chin over bar"
4. Continue pulling until the chin clears the bar or the upper chest contacts it; maintain a slight backward lean throughout
5. Lower under control with a 2–3 second eccentric; do not drop from the top position

## What the EMG Data Shows

The pull-up produces among the highest latissimus dorsi activation of any exercise: 117–130% MVIC across studies compiled in the ssd_2026 literature review. Peak values at 130% MVIC are recorded on rotating-handle pull-up devices, where natural hand supination during the pull likely improves LD moment arm.

The infraspinatus (79% MVIC) is notably active as a dynamic glenohumeral stabilizer — not a prime mover, but essential for preventing superior humeral head migration under load. Lower trapezius (56% MVIC) acts as the primary scapular stabilizer throughout the movement.

The core contracts isometrically throughout: erector spinae 39–41% MVIC and external oblique 31–35% MVIC to suppress lower-body swinging and maintain pelvic alignment. This isometric trunk demand increases proportionally with bodyweight and with added external load.

## Pull-Up vs Chin-Up: What the Data Shows

Changing grip from pronated to supinated produces a distinct neuromuscular shift:

| Muscle | Pull-Up (pronated) | Chin-Up (supinated) |
|--------|-------------------|---------------------|
| Latissimus dorsi | 123.5% (117–130 range) | 117.0% ± 46.0 |
| Biceps brachii | 78.0% ± 32.0 | 96.0% ± 34.0 |
| Lower trapezius | 56.0% ± 21.0 | 45.0% ± 22.0 |
| Pectoralis major | 44.0% ± 27.0 | 57.0% ± 36.0 |

The chin-up is not a "biceps exercise disguised as a back exercise" — its latissimus dorsi activation (117% MVIC) is statistically equivalent to the pronated pull-up. The practical difference is that the chin-up provides a larger biceps brachii stimulus (+18% MVIC) while the pronated pull-up provides a larger lower trapezius stimulus (+11% MVIC). Neither variation is superior for lat development; selection should be based on which secondary muscles need more work.

## Strength Curve Implications

The descending strength curve — hardest at the top, easiest at the bottom — has direct programming implications. Strategies that address the sticking point in the top third:

- **Dead stop reps**: Pause 1 second at full extension before each rep; this starts every rep in the hardest position of the subsequent rep, forcing adaptation at the sticking point
- **Eccentric-focused reps**: Jump to the top and lower for 5–8 seconds; maximally loads the top-to-mid range under eccentric tension
- **Weighted pull-ups**: External load increases total force demand throughout, shifting the full range above the capability threshold and forcing strength adaptation at the sticking point

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Chin-up | Supinated grip; greater biceps demand | Biceps development; beginners (easier due to elbow mechanics) |
| Weighted pull-up | External load via belt or vest | Strength progression once bodyweight reps exceed 8–10 |
| Band-assisted pull-up | Band reduces effective bodyweight | Learning the movement pattern; increasing volume |
| Scapular pull-up | Arms straight throughout; scapula only | Isolating lower/mid trapezius and serratus; injury rehabilitation |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/push_press.md -->

---
id: push_press
name: Push Press
status: complete
category: exercise
pattern: [vertical_push]
equipment: [barbell]

difficulty:
  technical_complexity: 4
  strength_prerequisite: 3
  mobility_prerequisite: 2

muscles:
  - id: deltoid_anterior
    role: primary
  - id: deltoid_lateral
    role: primary
  - id: triceps_brachii
    role: primary
  - id: rectus_femoris
    role: secondary
  - id: vastus_lateralis
    role: secondary
  - id: vastus_medialis
    role: secondary
  - id: erector_spinae
    role: secondary
  - id: external_oblique
    role: secondary
  - id: gluteus_maximus
    role: secondary

# ebd_2026 literature compilation. All activation data qualitative or comparative only.
# Power output data (75% and 65% 1RM) is quantitative but represents mechanical output,
# not %MVIC. Preserved as condition notes.
muscle_activation_studies:
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      phase: full_rep
      comparison: "push press vs strict overhead press"
    measurements:
      - {muscle: erector_spinae,    mean_pct_mvc: null, notes: "Significantly greater than strict overhead press (p<0.05); driven by dynamic deceleration-acceleration load transfer"}
      - {muscle: external_oblique,  mean_pct_mvc: null, notes: "Elevated to stabilize spine against dynamic loading; significantly greater than strict press (p<0.05)"}
      - {muscle: rectus_femoris,    mean_pct_mvc: null, notes: "Heavily active during eccentric dip and concentric drive phases"}
      - {muscle: vastus_lateralis,   mean_pct_mvc: null, notes: "Heavily active during eccentric dip and concentric drive phases"}
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      notes: "Power output optimization conditions"
    measurements:
      - {muscle: deltoid_anterior, mean_pct_mvc: null, notes: "Peak upper body power at 75% 1RM; mean upper body power at 65% 1RM"}

joint_rom_required:
  knee_flexion_deg: null
  shoulder_flexion_deg: 180
  notes: >
    Knee flexion restricted to a shallow quarter-squat (~10–15% of lifter height).
    Torso must remain vertical during the dip to prevent forward bar drift.
    Terminal overhead position requires full shoulder flexion (180°) with locked elbows.
  source: "ebd_2026"

strength_curve:
  type: accommodated
  sticking_point: terminal_lockout
  peak_force_position: dip_to_drive_transition
  notes: >
    Lower body kinetic energy transfer bypasses the strict overhead press sticking point
    at chin-to-eye level. Peak mechanical demand occurs at the transition from eccentric
    dip to concentric drive. The sticking point shifts to terminal lockout where the
    triceps must lock out the loaded bar at high velocity.
  source: "ebd_2026"

injury_risk:
  joint_stress:
    shoulder: moderate
    lower_back: moderate
    knee: low
  common_injuries:
    - structure: shoulder_subacromial_space
      mechanism: impingement_at_overhead_lockout
      risk_factors: [forward_head_posture, inadequate_thoracic_extension, bar_drifting_forward]
    - structure: lumbar_disc
      mechanism: dynamic_compression_from_dip_and_drive
      risk_factors: [forward_torso_lean_during_dip, inadequate_core_bracing, heavy_loads]
  contraindications:
    - acute_shoulder_impingement
    - acute_lumbar_disc_herniation
    - shoulder_labral_pathology

variations: []
progressions: []
alternatives: []

sources:
  - source_id: ebd_2026
    title: "Exercise Biomechanics Data Extraction: Upper Push Accessories"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Push Press

The push press is a barbell overhead pressing exercise that incorporates a lower-body "dip and drive" to transfer power through the kinetic chain and assist the arms in pressing heavy loads overhead. Unlike the strict overhead press, the push press is a full-body movement. The brief lower-body dip generates kinetic energy that carries the bar past the strict press sticking point at chin-to-eye level, allowing loads 15–25% heavier than the strict press max to be taken overhead.

## Execution

1. Begin in the front rack position: bar across the anterior deltoids and clavicle, elbows at 45°, grip just outside shoulder width
2. Inhale and brace hard; perform a rapid, shallow dip — bend the knees to approximately a quarter squat while keeping the torso vertical
3. At the bottom of the dip, immediately reverse direction in an explosive triple extension of the hips, knees, and ankles
4. The lower body drive accelerates the bar; once momentum carries it to forehead level, press through to full lockout with elbows straight, bar over the crown of the head
5. Lower the bar back to the front rack under control; do not drop it

## What the Data Shows

The available data from ebd_2026 is comparative, not absolute, but establishes the push press's unique muscular profile relative to the strict overhead press.

**Erector spinae and external oblique**: Both are significantly more active in the push press than the strict overhead press (p < 0.05). The explosive dip-and-drive creates a rapid acceleration/deceleration cycle that demands far greater spinal stabilization than the slow grind of a strict press. This is why the push press is used to develop core stiffness in strength and power athletes — not just shoulder strength.

**Lower body**: The rectus femoris, vastus lateralis, and biceps femoris are heavily recruited during both the eccentric dip (controlling the descent) and the concentric drive. The push press is a compound exercise with meaningful lower-body demand — it is not simply a shoulder press with a leg assist.

**Power output**: Peak upper body mechanical power is maximized at 75% of 1RM; mean power is maximized at 65% 1RM. These intensities are the practical optimal zone for push press training when power development (rather than maximal strength) is the goal.

## The Bypassed Sticking Point

The strict overhead press has a severe sticking point at chin-to-eye level where the anterior deltoids reach their weakest mechanical position. The push press bypasses this zone entirely via kinetic energy transfer — the bar arrives at the trouble zone already traveling upward at high velocity, eliminating the need to generate force in the weakest portion. The sticking point shifts to terminal lockout, where the triceps must stabilize and lock the bar at the end of an accelerated movement.

This is why the push press can produce 15–25% greater load than the strict press: it doesn't eliminate the shoulder demand, it reroutes force production through a mechanically superior range.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Strict overhead press | No lower body; full shoulder demand | Maximum shoulder strength development |
| Push jerk | Re-bend after drive; lower bar catch | Greater load capacity; Olympic lifting derivative |
| Dumbbell push press | Independent arms | Bilateral asymmetry assessment; shoulder rehabilitation |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/push_press_behind_the_neck.md -->

---
id: push_press_behind_the_neck
name: Push Press - Behind the Neck
status: complete
category: exercise
pattern: [vertical press]
equipment: [barbell, squat rack]

difficulty:
  technical_complexity: 3
  strength_prerequisite: 3
  mobility_prerequisite: 4

muscles:
  - id: deltoid_anterior
    role: primary
  - id: deltoid_lateral
    role: primary
  - id: deltoid_posterior
    role: primary
  - id: triceps_long
    role: secondary
  - id: triceps_lateral
    role: secondary
  - id: triceps_medial
    role: secondary
  - id: trap_upper
    role: secondary
  - id: serratus_anterior
    role: secondary
  - id: erector_spinae
    role: stabilizer
  - id: rectus_abdominis
    role: stabilizer
  - id: rectus_femoris
    role: stabilizer
  - id: vastus_lateralis
    role: stabilizer
  - id: vastus_medialis
    role: stabilizer

muscle_activation_studies: []

joint_rom_required:
  shoulder_external_rotation_deg: 90
  shoulder_flexion_deg: 180
  thoracic_extension_deg: 25
  source: "biomechanical inference"

strength_curve:
  type: ascending
  sticking_point: just_above_head
  peak_force_position: lockout
  notes: "The dip-drive transfers momentum through the sticking point just above head height. The ascending curve means the lift gets mechanically easier as the arms extend toward lockout."
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    shoulder: high
    wrist: moderate
    lumbar_spine: low
  common_injuries:
    - structure: rotator_cuff
      mechanism: anterior_impingement_in_behind_neck_position
      risk_factors: [limited_shoulder_external_rotation, insufficient_thoracic_extension, excessive_load]
    - structure: labrum
      mechanism: shear_force_from_behind_neck_pressing
      risk_factors: [shoulder_instability, poor_bar_path, excessive_load]
  contraindications:
    - shoulder_impingement
    - labral_tear
    - limited_shoulder_mobility
    - rotator_cuff_injury

variations: []
progressions: [push_press]
alternatives: [push_press, barbell_shoulder_press]

sources: []
---

# Push Press - Behind the Neck

An overhead pressing movement with leg drive, performed with the barbell resting on the rear deltoids behind the neck. The behind-neck bar position distributes load more evenly across all three deltoid heads compared to a front rack push press, with greater emphasis on the lateral and posterior deltoid. Popularized as an Olympic weightlifting accessory by coaches like Dmitry Klokov, it builds overhead strength in the position used to receive snatches and jerks.

## Execution

1. Set up in a squat rack with the bar at upper back height. Unrack the bar onto the rear deltoids with a grip slightly wider than shoulder width. Step back and set your feet directly under your hips.
2. Initiate the dip by flexing the knees slightly while keeping the torso vertical. The dip should be short and controlled — only 2-3 inches of knee bend.
3. Reverse direction explosively, driving through the heels to generate upward momentum on the bar. Keep the torso upright throughout the drive phase.
4. Use the leg-drive momentum to press the bar overhead, extending through the elbows to full lockout directly over the midfoot.
5. Lower the bar under control back to the rear deltoids, using a slight knee bend to absorb the load.

## Programming Note

This exercise demands excellent shoulder external rotation and thoracic extension mobility. If you cannot comfortably hold the bar on the rear deltoids with an upright torso, do not load this movement — use a front rack push press instead. The behind-neck position places the glenohumeral joint in a more vulnerable position under load, making the risk-reward tradeoff unfavorable for lifters with any shoulder history. Program at moderate loads for sets of 3-6 reps as an accessory to Olympic lifting, not as a primary strength builder.


---

<!-- FILE: exercises/pushups.md -->

---
id: pushups
name: Pushups
status: complete
category: exercise
pattern: [horizontal_push]
equipment: [bodyweight]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: pectoralis_major
    role: primary
  - id: triceps_brachii
    role: primary
  - id: deltoid_anterior
    role: secondary
  - id: serratus_anterior
    role: stabilizer
  - id: rectus_abdominis
    role: stabilizer
  - id: external_oblique
    role: stabilizer

# ebd_2026 literature compilation.
# Standard pushup values are ranges (95–105% PM; 73–109% TB; 67–87% SA).
# Midpoints stored as mean_pct_mvc; actual ranges preserved as notes.
# Bodyweight load (~68% on hands) is a kinematic load value, not %MVIC.
muscle_activation_studies:
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      variation: standard
      hand_width: shoulder-width
    measurements:
      - {muscle: pectoralis_major,  mean_pct_mvc: 100, sd: null, notes: "Range 95–105% MVIC; higher in diamond and TRX variations"}
      - {muscle: triceps_brachii,   mean_pct_mvc: 91,  sd: null, notes: "Range 73–109% MVIC; higher in diamond variations"}
      - {muscle: serratus_anterior, mean_pct_mvc: 77,  sd: null, notes: "Range 67–87% MVIC; primary scapular protractor"}
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      variation: diamond
      hand_width: close
    measurements:
      - {muscle: pectoralis_major, mean_pct_mvc: null, notes: "Highest relative EMG across standard/diamond/wide hand positions"}
      - {muscle: triceps_brachii,  mean_pct_mvc: null, notes: "Highest relative EMG across standard/diamond/wide hand positions"}

joint_rom_required:
  elbow_flexion_deg: null
  shoulder_abduction_deg: null
  notes: >
    Elbows tucked 45–70° relative to torso for shoulder safety (not fully flared).
    Chest lowers until close to the floor. Standard pushup supports ~68% of total
    bodyweight on the hands throughout the movement.
  source: "ebd_2026"

strength_curve:
  type: ascending
  sticking_point: bottom_third
  peak_force_position: bottom
  notes: >
    Hardest at the bottom where the pec is maximally stretched and chest is near the floor.
    Mechanical demand decreases as the elbows extend. The concentric phase produces higher
    raw RMS EMG than the eccentric phase, confirming the primary training stimulus
    is in the pressing phase.
  source: "ebd_2026"

injury_risk:
  joint_stress:
    shoulder: low
    wrist: moderate
    elbow: low
  common_injuries:
    - structure: wrist_extensor_tendons
      mechanism: repetitive_dorsiflexion_under_load
      risk_factors: [high_volume, inadequate_wrist_preparation, hard_floor]
    - structure: shoulder_subacromial_space
      mechanism: impingement
      risk_factors: [fully_flared_elbows_beyond_70_deg, excessively_wide_hand_placement]
  contraindications:
    - acute_wrist_tendinopathy
    - distal_radius_fracture_acute

variations: []
progressions: []
alternatives: []

sources:
  - source_id: ebd_2026
    title: "Exercise Biomechanics Data Extraction: Upper Push Accessories"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Pushups

The pushup is a closed-chain bodyweight pressing exercise performed in a prone plank position. It is the most accessible upper-body pressing movement, requiring no equipment and supporting approximately 68% of total bodyweight through the hands. EMG analysis confirms the pushup elicits pectoralis major activation (95–105% MVIC) comparable to a bench press loaded at approximately 60% of 1RM — making it a meaningful training stimulus across a wide range of populations.

## Execution

1. Place hands slightly wider than shoulder-width; fingers pointing forward or 15° outward
2. Set a rigid plank from head to heel — no hip sag or pike; brace the core throughout
3. Lower the chest toward the floor with elbows at 45–70° from the torso (not fully flared)
4. Touch or approach the floor; pause briefly
5. Press through both hands simultaneously until the elbows are straight; actively protract (push) the scapulae at the top

## What the EMG Data Shows

**Pectoralis major (95–105% MVIC)**: Standard pushups produce near-maximal pec activation despite supporting only 68% of bodyweight. This is equivalent to a bench press loaded at ~60% 1RM — the pec is under significant loading without requiring external load.

**Triceps brachii (73–109% MVIC)**: The wide range reflects variation in hand width and execution. Diamond pushups (hands close under chest) push triceps activation toward the upper end; standard pushups cluster in the mid-range.

**Serratus anterior (67–87% MVIC)**: This is the pushup's differentiating feature from the bench press. The bench press pins the scapulae to the pad, suppressing serratus anterior activity. The pushup requires active scapular protraction throughout, generating substantial serratus activation — a major contributor to serratus health and long thoracic nerve function. The pushup is the primary exercise prescribed for serratus anterior strengthening in rehabilitation.

**Diamond pushup superiority**: The diamond (triangle) hand position produces the highest relative EMG for both the pectoralis major and triceps brachii across all hand widths, making it the most demanding standard-surface pushup variation.

## The Scapular Advantage

The pushup's key mechanical distinction from all forms of bench pressing is scapular freedom. Because the chest is not anchored to a pad, the scapulothoracic joint can move through full protraction and retraction throughout each rep. This creates:

1. Active serratus anterior strengthening (67–87% MVIC) — unavailable in the bench press
2. Natural scapulohumeral rhythm — the glenohumeral joint is not exposed to impingement positions created by forcible scapular pinning
3. Core demand — the entire chain from feet to hands must remain rigid, unlike the supine bench position

For populations prioritizing shoulder health over maximum load, the pushup is often superior to the bench press despite lower absolute loading.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Diamond pushup | Narrow hands; highest triceps and pec EMG | Triceps emphasis; maximum bodyweight pressing demand |
| Wide pushup | >shoulder width hands; greater pec horizontal adduction | Pec major width emphasis |
| Pushup on rings/TRX | Unstable; significantly increases pec and core activation | Pec emphasis; serratus and shoulder stabilizer demand |
| Archer pushup | Asymmetric; loads one arm progressively | Progression toward one-arm pushup |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/reverse_hyperextension.md -->

---
id: reverse_hyperextension
name: Reverse Hyperextension
status: complete
category: exercise
pattern: [isolation]
equipment: [machine]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: erector_spinae
    role: primary
  - id: multifidus
    role: primary
  - id: gluteus_maximus
    role: primary
  - id: biceps_femoris
    role: primary
  - id: semitendinosus
    role: secondary
  - id: gastrocnemius
    role: secondary
  - id: soleus
    role: secondary

# Three independent studies with different execution tempos — values differ substantially.
# Dicus 2023 (doi: 10.70252/ZAOJ6139): 50% load, strict; used RDL as comparator.
# Cuthbert 2021 (doi: 10.1519/JSC.0000000000004049): n=10, strict 1-second tempo with pause.
# Lawrence 2019 (doi: 10.1519/JSC.0000000000003146): n=20, free swinging tempo.
# Execution tempo is the primary driver of activation differences. Do NOT average across studies.
muscle_activation_studies:
  - source_id: dicus_2023
    doi: "10.70252/ZAOJ6139"
    n: null
    population: "apparently healthy young males"
    condition:
      load_pct_1rm: 50
      phase: concentric
    measurements:
      - {muscle: erector_spinae,   mean_pct_mvc: 81.6, sd: 5.9}
      - {muscle: multifidus,       mean_pct_mvc: 89.8, sd: 7.2}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 64.3, sd: 9.5}
      - {muscle: biceps_femoris,   mean_pct_mvc: 70.8, sd: 7.0}
      - {muscle: semitendinosus,   mean_pct_mvc: 57.1, sd: 8.9}
  - source_id: dicus_2023
    doi: "10.70252/ZAOJ6139"
    n: null
    population: "apparently healthy young males"
    condition:
      load_pct_1rm: 50
      phase: eccentric
    measurements:
      - {muscle: erector_spinae,   mean_pct_mvc: 54.6, sd: 6.0}
      - {muscle: multifidus,       mean_pct_mvc: 59.0, sd: 5.1}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 36.3, sd: 4.1}
      - {muscle: biceps_femoris,   mean_pct_mvc: 55.6, sd: 8.1}
      - {muscle: semitendinosus,   mean_pct_mvc: 43.8, sd: 9.5}
  - source_id: dicus_2023
    doi: "10.70252/ZAOJ6139"
    n: null
    population: "apparently healthy young males"
    condition:
      load_pct_1rm: 50
      phase: full_rep
    measurements:
      - {muscle: erector_spinae,   mean_pct_mvc: 66.6, sd: 4.4}
      - {muscle: multifidus,       mean_pct_mvc: 72.8, sd: 4.6}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 49.1, sd: 5.8}
      - {muscle: biceps_femoris,   mean_pct_mvc: 62.4, sd: 6.5}
      - {muscle: semitendinosus,   mean_pct_mvc: 49.4, sd: 7.8}
  - source_id: cuthbert_2021
    doi: "10.1519/JSC.0000000000004049"
    n: 10
    population: "recreationally resistance-trained adults"
    condition:
      load_pct_1rm: null
      phase: concentric
      tempo: "1-second strict with pause at top and bottom"
    measurements:
      - {muscle: erector_spinae,  mean_pct_mvc: 71.0, sd: 20.5}
      - {muscle: gluteus_maximus, mean_pct_mvc: 23.4, sd: 15.8}
      - {muscle: biceps_femoris,  mean_pct_mvc: 39.7, sd: 13.4}
  - source_id: cuthbert_2021
    doi: "10.1519/JSC.0000000000004049"
    n: 10
    population: "recreationally resistance-trained adults"
    condition:
      load_pct_1rm: null
      phase: eccentric
      tempo: "1-second strict with pause at top and bottom"
    measurements:
      - {muscle: erector_spinae,  mean_pct_mvc: 51.8, sd: 16.1}
      - {muscle: gluteus_maximus, mean_pct_mvc: 18.6, sd: 9.2}
      - {muscle: biceps_femoris,  mean_pct_mvc: 28.3, sd: 2.3}
  - source_id: lawrence_2019
    doi: "10.1519/JSC.0000000000003146"
    n: 20
    population: "recreationally active individuals"
    condition:
      load_pct_1rm: null
      phase: full_rep
      tempo: "free swinging"
    measurements:
      - {muscle: erector_spinae,  mean_pct_mvc: 36.9, sd: 25.4}
      - {muscle: gluteus_maximus, mean_pct_mvc: 50.1, sd: 23.7}
      - {muscle: biceps_femoris,  mean_pct_mvc: 44.7, sd: 31.3}

joint_rom_required:
  hip_flexion_deg: 76.6
  knee_flexion_deg: null
  ankle_dorsiflexion_deg: null
  notes: "Thigh-to-trunk ROM during the RHE (Lawrence 2019). Machine constrains the movement pattern; mobility constraints are minimal."
  source: "lawrence_2019"

strength_curve:
  type: ascending
  sticking_point: null
  peak_force_position: lockout
  notes: >
    The pendulum design shifts peak mechanical torque to terminal hip extension.
    This is the opposite of the descending curves of the RDL, SLDL, and good morning.
    The ascending curve makes the RHE a mechanical complement to closed-chain hip
    hinges — it trains the range where they are weakest.
  source: "lawrence_2019"

injury_risk:
  joint_stress:
    lower_back: low
    hip: low
  common_injuries:
    - structure: lumbar_disc
      mechanism: hyperextension_at_top
      risk_factors: [excessive_range_of_motion, momentum_driven_technique]
  contraindications:
    - acute_lumbar_disc_herniation_with_anterior_symptoms

variations: []
progressions: []
alternatives: [romanian_deadlift, good_morning]

sources:
  - source_id: dicus_2023
    title: "A Comparison of Muscle Recruitment Across Three Straight-Legged, Hinge-Pattern Resistance Training Exercises"
    author: "Dicus JR, Ellestad SH, Sheaffer JE, Weber CA, Novak NC, Holmstrup ME"
    year: 2023
    doi: "10.70252/ZAOJ6139"
    credibility: rct
  - source_id: cuthbert_2021
    title: "Electromyographical Differences Between the Hyperextension and Reverse-Hyperextension"
    author: "Cuthbert M, Ripley NJ, Suchomel TJ, Alejo R, McMahon JJ, Comfort P"
    year: 2021
    doi: "10.1519/JSC.0000000000004049"
    credibility: rct
  - source_id: lawrence_2019
    title: "Biomechanical Comparison of the Reverse Hyperextension Machine and the Hyperextension Exercise"
    author: "Lawrence MA, Chin A, Swanson BT"
    year: 2019
    doi: "10.1519/JSC.0000000000003146"
    credibility: rct
---

# Reverse Hyperextension

The reverse hyperextension (RHE) is an open-chain hip extension exercise performed on a dedicated machine. The upper body is fixed prone on a pad while the pelvis and lower limbs swing freely on a pendulum. This structure uncouples hip extension from axial spinal loading — an arrangement that distinguishes the RHE from every other posterior-chain exercise.

## Execution

1. Lie prone on the pad; position the hips at the rear edge; grip the handles firmly
2. Begin with legs hanging below horizontal (the stretched starting position)
3. Swing the legs upward by extending the hips; aim to bring the legs to horizontal or slightly above
4. Control the descent; do not use momentum to cycle through repetitions
5. Pause briefly at the top and bottom to maximize muscular tension if possible

## What the EMG Data Shows

Three independent studies show a wide range of EMG values driven primarily by execution tempo:

**Dicus 2023 (50% load, strict)**: Multifidus 89.8%, erector spinae 81.6%, biceps femoris 70.8%, gluteus maximus 64.3% MVIC (concentric). These values are substantially higher than the RDL measured in the same study — the RHE removed the trunk-stabilization constraint, freeing the hip extensors to fire closer to their maximal potential.

**Cuthbert 2021 (strict 1-second tempo with pause)**: Erector spinae 71.0%, biceps femoris 39.7%, gluteus maximus 23.4% MVIC (concentric). The RHE produced 28–65% greater mean EMG than the standard hyperextension exercise across all muscles, confirming it as the superior open-chain posterior-chain option.

**Lawrence 2019 (free swinging)**: Erector spinae 36.9%, gluteus maximus 50.1%, biceps femoris 44.7% MVIC (full rep). Substantially lower than both other studies — swinging motion generates momentum that bypasses mid-range muscular activation.

## The Open-Chain Advantage

In closed-chain hinges (RDL, SLDL, good morning), the limiting factor for hip extensor recruitment is the trunk's ability to stabilize the spine against vertical gravitational load. The RHE bypasses this constraint by fixing the chest to the machine. The limiting factor becomes hip extensor output capacity — not spinal tolerance. This is why RHE values in Dicus 2023 exceed RDL values at the same relative load despite being a machine accessory exercise.

The pendulum creates an ascending strength curve, peaking at terminal hip extension — the mechanical opposite of the descending curves of the RDL, SLDL, and good morning. This means the RHE targets the contractile range where closed-chain exercises are mechanically weakest.

## Spinal Decompression

During the descent of the RHE, the pendulum generates traction on the lumbar spine, helping to decompress the intervertebral discs. This is why the RHE is used after heavy deadlift sessions by programs like Westside Conjugate — not only as a posterior chain accessory, but as an active recovery and decompression modality. The reverse hyperextension is one of the few resistance exercises that may provide a therapeutic benefit to the lumbar spine during execution.

## Tempo Matters

Heavier pendulum loads increase biceps femoris activation linearly, but erector spinae and gluteus maximus do not scale proportionally with load — momentum increases disproportionately at heavier loads, reducing muscular demand per unit of apparent effort. A strict tempo (1-second concentric, pause at top, 1-second eccentric) reliably outperforms free-swinging by up to 65% in mean EMG across all muscles.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/ring_dips.md -->

---
id: ring_dips
name: Ring Dips
status: complete
category: exercise
pattern: [vertical_push]
equipment: [gymnastic_rings]

difficulty:
  technical_complexity: 4
  strength_prerequisite: 4
  mobility_prerequisite: 2

muscles:
  - id: triceps_brachii
    role: primary
  - id: pectoralis_major
    role: primary
  - id: deltoid_anterior
    role: secondary
  - id: serratus_anterior
    role: stabilizer
  - id: latissimus_dorsi
    role: stabilizer
  - id: trap_lower
    role: stabilizer

# ebd_2026 literature compilation.
# Triceps peak: 1.05 ± 0.27 mV (raw millivolts) — NOT stored as mean_pct_mvc because
#   raw mV values are not normalized and cannot be compared across subjects or exercises.
#   This value is reported in the prose for comparison with bar dip (1.04 ± 0.27 mV).
# Pectoralis major: qualitative only ("extremely high").
# Stabilizers: qualitative increase with fatigue.
# Shoulder extension ROM is the primary quantitative kinematic measure.
muscle_activation_studies:
  - source_id: ebd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      apparatus: gymnastic_rings
      phase: full_rep
    measurements:
      - {muscle: triceps_brachii,   mean_pct_mvc: null, notes: "Peak 1.05 ± 0.27 mV (raw mV, not %MVIC; equivalent to bar dip 1.04 ± 0.27 mV)"}
      - {muscle: pectoralis_major,  mean_pct_mvc: null, notes: "Extremely high — functions as primary adductor to prevent rings from flaring outward"}
      - {muscle: serratus_anterior, mean_pct_mvc: null, notes: "Increases significantly with fatigue to maintain ring stability"}
      - {muscle: trap_lower,         mean_pct_mvc: null, notes: "Increases significantly with fatigue as primary compensatory stabilizer"}
      - {muscle: latissimus_dorsi,   mean_pct_mvc: null, notes: "Increases significantly with fatigue; secondary adduction stabilizer"}

joint_rom_required:
  shoulder_extension_deg: 61.72
  elbow_flexion_deg: 90
  notes: >
    Peak shoulder extension 61.72° ± 13.51° — significantly less than parallel bar dip
    (78.20° ± 9.84°) due to ring instability limiting depth. Elbows maintained at ~90°
    at the bottom. Forearms must remain vertical to prevent ring drift and shoulder strain.
  source: "ebd_2026"

strength_curve:
  type: descending_to_flat
  sticking_point: bottom_and_lockout
  peak_force_position: eccentric_concentric_transition
  notes: >
    Bottom position remains highly demanding (descending curve portion). At lockout,
    a secondary sticking point appears: the lifter must generate substantial adduction
    force to prevent rings from drifting laterally, reducing the mechanical advantage
    normally present at full elbow extension in a stable bar dip.
  source: "ebd_2026"

injury_risk:
  joint_stress:
    shoulder: moderate
    elbow: moderate
    wrist: moderate
  common_injuries:
    - structure: glenohumeral_joint
      mechanism: uncontrolled_shoulder_loads_from_ring_instability
      risk_factors: [inadequate_ring_control_skill, fatigue, wide_ring_spacing]
    - structure: elbow_ligaments
      mechanism: valgus_or_varus_stress_from_ring_drift
      risk_factors: [inadequate_ring_control_skill, fatigue, excessive_elbow_flare]
    - structure: wrist_extensors
      mechanism: forced_dorsiflexion_under_load
      risk_factors: [inadequate_wrist_preparation, excessive_ring_distance_from_body]
  contraindications:
    - anterior_shoulder_instability
    - acute_elbow_ligament_injury

variations: [parallel_bar_dip]
progressions: []
alternatives: []

sources:
  - source_id: ebd_2026
    title: "Exercise Biomechanics Data Extraction: Upper Push Accessories"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Ring Dips

The ring dip is an advanced bodyweight pressing exercise performed on gymnastic rings suspended from an overhead anchor. Unlike the stable parallel bar dip, the rings can move freely in three dimensions. This structural instability forces the pectoralis major to function as a primary adductor throughout the movement — preventing the rings from drifting laterally — while the rotator cuff, serratus anterior, lower trapezius, and latissimus dorsi must co-contract continuously to maintain ring position.

## Execution

1. Mount the rings; lock the elbows and externally rotate the wrists so palms face inward-forward; rings should be tight to the body
2. Brace the core; keep feet together or crossed behind
3. Lower by flexing the elbows; keep the rings close and forearms vertical to prevent ring drift
4. Descend until the elbows reach 90°; do not chase depth — ring instability limits safe extension to ~62° of shoulder extension vs 78° for bar dips
5. Drive through the rings to lockout; at the top, actively close the rings slightly toward each other to prevent flaring

## What the Data Shows

**Triceps activation is equivalent to the parallel bar dip**: Ring dip triceps peak activation is 1.05 ± 0.27 mV vs 1.04 ± 0.27 mV for the bar dip — statistically identical. Despite their dramatically different difficulty profiles, the ring dip does not produce greater triceps activation than the bar dip.

**Pectoralis major is the differentiating factor**: The pec is described as "extremely high" in the ring dip — but not for the same reason as in the bar dip. In the bar dip, the pec works as a shoulder extensor and flexor during the pressing movement. In the ring dip, the pec must also contract continuously as an adductor to prevent the rings from drifting, adding an independent component of pec demand that doesn't exist in bar dip.

**Stabilizers escalate under fatigue**: As ring dip sets progress, the serratus anterior, lower trapezius, and latissimus dorsi show significantly increased EMG amplitude. This is the nervous system recruiting additional stabilizers to compensate for degrading ring control — a phenomenon that does not occur in stable bar dips. This fatigue response is both the mechanism of ring dip's additional demand and the primary injury risk factor.

## Ring Dip vs Parallel Bar Dip

| Feature | Parallel Bar Dip | Ring Dip |
|---------|-----------------|----------|
| Shoulder extension ROM | 78.20° ± 9.84° | 61.72° ± 13.51° |
| Triceps peak activation | 1.04 ± 0.27 mV | 1.05 ± 0.27 mV |
| Pectoralis major demand | High (extensors + flexors) | Extremely high (+adduction) |
| Stabilizer demand at lockout | Low | High (prevents ring drift) |
| Strength curve | Descending, clear lockout | Descending-to-flat |

The ring dip is not simply a "harder dip." It is a qualitatively different movement that trains ring stabilization as a primary skill. Its reduced shoulder extension ROM (62° vs 78°) actually makes the bottom position safer for the anterior shoulder, but the unpredictable ring drift creates higher peak joint loads during loss of control. The prerequisite is competence at 3× 10 bodyweight bar dips before attempting ring dips.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Parallel bar dip | Stable; greater shoulder extension ROM | Primary pressing strength |
| Ring support hold | No dipping; isometric ring stabilization | Building ring control prerequisite |
| Weighted ring dip | External load; extremely high difficulty | Gymnastic strength beyond bodyweight |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/romanian_deadlift.md -->

---
id: romanian_deadlift
name: Romanian Deadlift
status: complete
category: exercise
pattern: [hinge]
equipment: [barbell]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 3

muscles:
  - id: erector_spinae
    role: primary
  - id: multifidus
    role: primary
  - id: biceps_femoris
    role: primary
  - id: semitendinosus
    role: primary
  - id: gluteus_maximus
    role: secondary
  - id: rectus_femoris
    role: secondary
  - id: gastrocnemius
    role: secondary
  - id: soleus
    role: secondary
  - id: forearm_flexors
    role: stabilizer

# Dicus 2023 (doi: 10.70252/ZAOJ6139): measured longissimus dorsi (erector spinae component)
# and multifidus separately. Values mapped to 'erector_spinae' and 'multifidus' canonical IDs.
# Lee 2018 (doi: 10.1016/j.jesf.2018.08.001): n=21, experienced males, 70% RDL 1RM.
# Do NOT average across studies — load conditions and populations differ.
muscle_activation_studies:
  - source_id: dicus_2023
    doi: "10.70252/ZAOJ6139"
    n: null
    population: "apparently healthy young males"
    condition:
      load_pct_1rm: 50
      phase: concentric
      knee_flexion_deg: 15
    measurements:
      - {muscle: erector_spinae,  mean_pct_mvc: 69.2, sd: 5.9}
      - {muscle: multifidus,      mean_pct_mvc: 75.5, sd: 6.0}
      - {muscle: gluteus_maximus, mean_pct_mvc: 44.3, sd: 7.6}
      - {muscle: biceps_femoris,  mean_pct_mvc: 52.6, sd: 5.4}
      - {muscle: semitendinosus,  mean_pct_mvc: 45.6, sd: 6.7}
  - source_id: dicus_2023
    doi: "10.70252/ZAOJ6139"
    n: null
    population: "apparently healthy young males"
    condition:
      load_pct_1rm: 50
      phase: eccentric
      knee_flexion_deg: 15
    measurements:
      - {muscle: erector_spinae,  mean_pct_mvc: 49.2, sd: 3.8}
      - {muscle: multifidus,      mean_pct_mvc: 52.2, sd: 3.2}
      - {muscle: gluteus_maximus, mean_pct_mvc: 20.6, sd: 3.4}
      - {muscle: biceps_femoris,  mean_pct_mvc: 23.5, sd: 3.5}
      - {muscle: semitendinosus,  mean_pct_mvc: 21.8, sd: 2.7}
  - source_id: dicus_2023
    doi: "10.70252/ZAOJ6139"
    n: null
    population: "apparently healthy young males"
    condition:
      load_pct_1rm: 50
      phase: full_rep
      knee_flexion_deg: 15
    measurements:
      - {muscle: erector_spinae,  mean_pct_mvc: 56.7, sd: 3.8}
      - {muscle: multifidus,      mean_pct_mvc: 61.2, sd: 3.5}
      - {muscle: gluteus_maximus, mean_pct_mvc: 29.6, sd: 5.0}
      - {muscle: biceps_femoris,  mean_pct_mvc: 34.5, sd: 4.2}
      - {muscle: semitendinosus,  mean_pct_mvc: 31.2, sd: 4.2}
  - source_id: lee_2018
    doi: "10.1016/j.jesf.2018.08.001"
    n: 21
    population: "experienced males"
    condition:
      load_pct_1rm: 70
      phase: full_rep
      knee_flexion_deg: 33.86
    measurements:
      - {muscle: rectus_femoris,  mean_pct_mvc: 25.26, sd: 14.21}
      - {muscle: biceps_femoris,  mean_pct_mvc: 56.66, sd: 18.56}
      - {muscle: gluteus_maximus, mean_pct_mvc: 46.88, sd: 7.39}

joint_rom_required:
  hip_flexion_deg: 79.97
  knee_flexion_deg: 33.86
  ankle_dorsiflexion_deg: null
  notes: "ROM at maximum depth (Lee 2018). Ankle dorsiflexion is not a limiting factor due to minimal knee flexion."
  source: "lee_2018"

strength_curve:
  type: descending
  sticking_point: null
  peak_force_position: bottom
  notes: >
    Hip extensor torque peaks at maximum hip flexion. Hamstring tension falls as hips
    extend toward lockout. Concentric erector spinae activation (69.2% MVIC) exceeds
    eccentric (49.2% MVIC), indicating active spinal stabilization during the ascent.
  source: "dicus_2023 / lee_2018"

injury_risk:
  joint_stress:
    lower_back: moderate
    knee: low
    shoulder: low
  common_injuries:
    - structure: lumbar_disc
      mechanism: flexion_under_load
      risk_factors: [lumbar_rounding, excessive_hip_drop, rapid_load_increase]
    - structure: proximal_hamstring
      mechanism: eccentric_overload_at_long_length
      risk_factors: [inadequate_warmup, excessive_range_of_motion, high_frequency]
  contraindications:
    - acute_lumbar_herniation
    - proximal_hamstring_tendinopathy

variations: [stiff_legged_barbell_deadlift]
progressions: []
alternatives: [reverse_hyperextension, good_morning]

sources:
  - source_id: dicus_2023
    title: "A Comparison of Muscle Recruitment Across Three Straight-Legged, Hinge-Pattern Resistance Training Exercises"
    author: "Dicus JR, Ellestad SH, Sheaffer JE, Weber CA, Novak NC, Holmstrup ME"
    year: 2023
    doi: "10.70252/ZAOJ6139"
    credibility: rct
  - source_id: lee_2018
    title: "An electromyographic and kinetic comparison of conventional and Romanian deadlifts"
    author: "Lee S, Schultz J, Liu Y"
    year: 2018
    doi: "10.1016/j.jesf.2018.08.001"
    credibility: rct
---

# Romanian Deadlift

The Romanian deadlift (RDL) is a barbell hinge-pattern exercise performed from the standing position. It trains the posterior chain — primarily the hamstrings, erector spinae, and multifidus — through a controlled eccentric descent with a slight, constant knee flexion of 15–20°. Unlike the conventional deadlift, the RDL begins at the top and the bar never touches the floor.

## Execution

1. Stand holding a barbell at hip height with a double-overhand or mixed grip, feet hip-width
2. Inhale and brace with a Valsalva maneuver; maintain a neutral lumbar spine
3. Push the hips backward while hinging at the waist; keep the bar dragging against the legs
4. Lower until a strong hamstring stretch is felt (typically bar at mid-shin level); stop before lumbar rounding
5. Drive the hips forward to return to standing; exhale at lockout

## What the EMG Data Shows

At 50% 1RM (Dicus 2023), the multifidus (75.5% MVIC) and erector spinae/longissimus (69.2% MVIC) are the most active muscles during the concentric phase — not the hamstrings. The biceps femoris (52.6%) and semitendinosus (45.6%) are the primary hip extensors. Gluteus maximus contributes 44.3% MVIC concentric.

The concentric/eccentric ratio is asymmetric and instructive: erector spinae drops from 69.2% (concentric) to 49.2% MVIC (eccentric). The spinal extensors work harder during the return than the descent — confirming active lumbar stabilization drives the ascent.

At 70% 1RM (Lee 2018), biceps femoris reaches 56.7% MVIC and gluteus maximus 46.9% MVIC, consistent with load-dependent recruitment of the hip extensors. The conventional deadlift at the same relative load produces significantly greater gluteus maximus and rectus femoris activation; biceps femoris activation is comparable between the two styles.

## Comparison with Related Hip Hinge Variations

The open-chain reverse hyperextension produces 19.5% greater total gluteus maximus activation and 27.9% greater biceps femoris activation than the RDL at equal relative load (Dicus 2023). The RHE achieves this by bypassing the trunk-stabilization constraint — with the chest fixed on a bench, the hip extensors can fire closer to their maximal potential. The cable pull-through, conversely, produces 11–14% less posterior chain activation than the RDL across all measured muscles.

The stiff-legged deadlift (SLDL) targets the gluteus maximus more strongly than the standard RDL (Effect Size 0.99, Coratella 2022), because the fully extended knee removes the hamstring's active contribution to knee stabilization. However, the RDL produces greater semitendinosus activation than the SLDL (ES 1.38), because the slight knee flexion allows the medial hamstrings to function more effectively as hip extensors.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Stiff-legged deadlift | Knees fully extended; bar drifts slightly forward | Maximum passive hamstring stretch; higher GM demand |
| Step-RDL | Standing on a raised platform for greater depth | Maximal posterior chain excitation (ES 3.28 greater than standard RDL) |
| Single-leg RDL | Unilateral; challenges hip abductor stability | Hip stability; addressing bilateral asymmetries |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/scapular_pull_up.md -->

---
id: scapular_pull_up
name: Scapular Pull-Up
status: complete
category: exercise
pattern: [isolation]
equipment: [bodyweight]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: trap_lower
    role: primary
  - id: serratus_anterior
    role: secondary
  - id: latissimus_dorsi
    role: secondary
  - id: rhomboids
    role: secondary

# No peer-reviewed EMG study with %MVIC exists specifically for the scapular pull-up.
# youdas_2010 measured trap_lower during a full pull-up (concentric phase) — proxy for the
# initial scapular depression phase that the scapular pull-up isolates.
# ekstrom_2003 measured closed-chain press-up and prone retraction — scapular depression
# exercises that share the same trap_lower activation mechanism.
muscle_activation_studies:
  - source_id: youdas_2010
    doi: "10.1519/JSC.0b013e3181df44d5"
    n: 25
    population: "recreationally active adults, 21M/4F, age 24.9 ± 2.4 yr"
    condition:
      load_pct_1rm: null
      implement: "pull-up bar"
      phase: concentric
      notes: "Full pronated-grip pull-up, not scapular pull-up isolation. Proxy: the lower trapezius initiates the pull-up via scapular depression before elbow flexion engages. Values reflect full pull-up activation, not isolated scapular depression."
    measurements:
      - muscle: trap_lower
        mean_pct_mvc: 56.0
        sd: 12.0
      - muscle: latissimus_dorsi
        mean_pct_mvc: 130.0
        sd: 24.0
      - muscle: biceps_brachii
        mean_pct_mvc: 78.0
        sd: 15.0
  - source_id: ekstrom_2003
    doi: "10.2519/jospt.2003.33.5.247"
    n: 19
    population: "healthy adults, 9M/10F, age 24.6 ± 3.1 yr"
    condition:
      load_pct_1rm: null
      implement: "table surface"
      phase: isometric
      notes: "Closed-chain press-up: seated on table, hands flat, arms extended to depress scapulae and lift torso. Shares the scapular depression mechanism with the scapular pull-up. NOT a hanging exercise."
    measurements:
      - muscle: trap_lower
        mean_pct_mvc: 56.0
        sd: 23.0
      - muscle: trap_upper
        mean_pct_mvc: 27.0
        sd: 32.0

joint_rom_required:
  shoulder_flexion_deg: 180
  scapular_depression_deg: 15
  notes: "Arms must be fully extended overhead (180° shoulder flexion) to achieve the dead-hang starting position. The exercise ROM is small — approximately 5–15° of scapular depression — but requires full overhead mobility to set up correctly."
  source: "Anatomical inference; pullup literature"

strength_curve:
  type: ascending
  sticking_point: initiation
  peak_force_position: full_depression
  notes: "The initial motor pattern (learning to depress the scapula without flexing the elbow) is the primary technical challenge. Once the pattern is established, the ascending curve reflects greater lower trapezius moment arm advantage at moderate depression."
  source: "Biomechanical inference"

injury_risk:
  joint_stress:
    shoulder: low
    acromioclavicular: low
  common_injuries:
    - structure: acromioclavicular_joint
      mechanism: repetitive_compression
      risk_factors: [excessive_volume, performing_with_elevation_instead_of_depression]
    - structure: glenohumeral_joint
      mechanism: impingement
      risk_factors: [protraction_instead_of_depression, forward_head_posture]
  contraindications:
    - acute_acromioclavicular_joint_injury
    - acute_rotator_cuff_tear

variations: []
progressions: [pullups]
alternatives: [face_pull]

sources:
  - source_id: bwf_skill_standards
    title: "Recommended Routine and Skill Standards"
    author: "Bodyweight Fitness community"
    year: null
    doi: null
    credibility: practitioner
  - source_id: kibler_2003
    title: "The role of the scapula in athletic shoulder function"
    author: "Kibler, W. B."
    year: 2003
    doi: "10.1177/036354659802600117"
    credibility: literature_review
  - source_id: youdas_2010
    title: "Surface electromyographic muscle activity of several scapular stabilizers during isometric exercises performed on and off a Swiss ball"
    author: "Youdas, J. W. et al."
    year: 2010
    doi: "10.1519/JSC.0b013e3181df44d5"
    credibility: rct
  - source_id: ekstrom_2003
    title: "Surface electromyographic analysis of exercises for the trapezius and serratus anterior muscles"
    author: "Ekstrom, R. A., Donatelli, R. A., & Soderberg, G. L."
    year: 2003
    doi: "10.2519/jospt.2003.33.5.247"
    credibility: rct
---

# Scapular Pull-Up

The scapular pull-up is a bodyweight isolation drill for the lower trapezius and scapular depressors. The arms remain straight throughout — there is no elbow flexion and no attempt to pull the chin to the bar. The only movement is the depression of the shoulder girdle, lifting the body a few centimeters by pulling the shoulder blades downward. It is used as a prerequisite drill in bodyweight strength programs to establish the scapular control required for full pull-up competence.

## Execution

1. Hang from a pull-up bar with a pronated (overhand) grip at approximately shoulder width; arms fully extended, body relaxed in a passive dead hang
2. Without bending the elbows, depress the shoulder girdle — imagine pulling the shoulder blades down and slightly back, away from the ears
3. The body will rise a few centimeters; this is the full ROM of the movement
4. Pause briefly at the top with the scapulae fully depressed
5. Lower under control, allowing the shoulders to return toward the ears (passive hang)
6. Repeat for the prescribed reps

## Why This Drill Exists

In a full pull-up, initiating the movement from a depressed scapular position is mechanically efficient and distributes load across a larger muscular system. Lifters who lack lower trapezius activation tend to begin the pull with the arms (biceps-dominant) rather than with the back, which limits performance and increases impingement risk.

The scapular pull-up trains the depression pattern in isolation, before any arm involvement is introduced. Once the pattern is established here, it transfers directly to the dead-hang starting position of the full pull-up.

## The Common Error: Shrugging vs. Depressing

The most frequent error is initiating the movement by shrugging (elevating the scapulae) rather than depressing them. Shrugging creates elevation, not depression, and activates the upper trapezius instead of the lower trapezius. The correct motor pattern feels like "squeezing the armpits downward" or "pulling the shoulder blades into the back pockets."

| Cue | Wrong movement | Correct movement |
|-----|---------------|-----------------|
| "Lift yourself up" | Often produces shoulder shrug | Use this cue only once the pattern is established |
| "Shoulder blades to back pockets" | N/A | Correct — drives depression and retraction |
| "Armpits toward the floor" | N/A | Correct — emphasizes depression |

## Progressions

The scapular pull-up is a prerequisite to the full pull-up, not a permanent component of programming. Once consistent scapular depression at the initiation of a pull can be felt, the scapular pull-up has served its purpose. At that point, progress to full pull-ups, incorporating the depression initiation into every rep.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/seated_bent_over_rear_delt_raise.md -->

---
id: seated_bent_over_rear_delt_raise
name: Seated Bent-Over Rear Delt Raise
status: complete
category: exercise
pattern: [isolation]
equipment: [dumbbell]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: deltoid_posterior
    role: primary
  - id: deltoid_lateral
    role: primary
  - id: trap_middle
    role: secondary
  - id: rhomboids
    role: secondary
  - id: infraspinatus
    role: stabilizer

# Sweeney 2014 (n=16): 70% 1RM, torso bent forward parallel to ground.
# Posterior delt 73% ± 9.9% MVIC; lateral delt 70% ± 14.6%.
# Anterior delt near-zero (5% ± 4.1%) confirms effective posterior isolation.
# Bending torso 90° forward aligns the transverse plane of horizontal abduction with gravity.
muscle_activation_studies:
  - source_id: sweeney_2014
    doi: null
    n: 16
    population: "healthy males, 70% 1RM, torso parallel to floor"
    condition:
      load_pct_1rm: 70
      implement: dumbbell
      phase: full_rep
      notes: "Seated, torso bent forward until parallel to ground"
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 5.0,  sd: 4.1}
      - {muscle: deltoid_lateral,   mean_pct_mvc: 70.0, sd: 14.6}
      - {muscle: deltoid_posterior, mean_pct_mvc: 73.0, sd: 9.9}

joint_rom_required:
  shoulder_abduction_deg: 90
  hip_flexion_deg: 90
  source: "Sweeney 2014"

strength_curve:
  type: ascending
  sticking_point: top_third
  peak_force_position: top
  notes: "Maximum gravity-dependent resistance torque at 90° horizontal abduction when humerus is parallel to the ground"
  source: "Sweeney 2014"

injury_risk:
  joint_stress:
    shoulder: low
    elbow: low
    lower_back: low
  common_injuries:
    - structure: lumbar_disc
      mechanism: prolonged_hip_flexion_under_load
      risk_factors: [heavy_loads, sustained_bent_over_position, pre_existing_lumbar_pathology]
  contraindications:
    - acute_lumbar_disc_herniation

variations: []
progressions: []
alternatives: [face_pull, bent_over_dumbbell_rear_delt_raise_with_head_on_bench]

sources:
  - source_id: sweeney_2014
    title: "Dynamite Delts: ACE Research Identifies Top Shoulder Exercises"
    author: "Sweeney, Samantha; Porcari, John P. et al."
    year: 2014
    doi: null
    credibility: rct
---

# Seated Bent-Over Rear Delt Raise

The seated bent-over rear delt raise is the most evidence-supported open-chain isolation exercise for the posterior deltoid. Performed seated with the torso hinged forward until parallel to the floor, the movement targets the posterior deltoid and lateral deltoid simultaneously through horizontal abduction against gravity. The near-zero anterior deltoid activation (5% MVIC) confirms that the bent-forward torso position effectively eliminates anterior deltoid contribution present in upright movements.

## Execution

1. Sit at the end of a bench with dumbbells hanging between the legs
2. Hinge the torso forward until nearly parallel to the floor; keep the spine neutral (do not round)
3. With elbows slightly bent and fixed, raise the dumbbells laterally in an arc until arms are parallel to the floor
4. Focus on "opening" the shoulder blades apart rather than shrugging
5. Lower under control; do not let the dumbbells pull the shoulders forward at the bottom

## What the EMG Data Shows

Sweeney 2014 (n=16, 70% 1RM):

| Muscle | Activation |
|--------|-----------|
| Posterior deltoid | 73.0 ± 9.9% MVIC |
| Lateral deltoid | 70.0 ± 14.6% MVIC |
| Anterior deltoid | 5.0 ± 4.1% MVIC |

The posterior and lateral deltoid values are nearly identical, confirming that bending the torso 90° forward aligns both heads with the gravity vector. Compared to the standard lateral raise (posterior delt only 33% MVIC in Sweeney 2014), the torso-forward position more than doubles posterior delt activation without changing the load.

## Torso Angle Is the Key Variable

By bending 90° forward, the horizontal plane of shoulder abduction becomes the line of action against gravity. The posterior deltoid, which performs horizontal abduction, now drives directly against gravitational resistance rather than acting as a stabilizer. Sitting removes lower-body compensation and prevents upper-body momentum.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Face pull | Cable; adds external rotation | Shoulder health; rotator cuff involvement |
| Chest-supported rear delt raise | Forehead on bench; eliminates spinal erector demand | Lumbar sensitivity |
| Cable rear delt fly | Constant tension | Lengthened-position load |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/seated_cable_rows.md -->

---
id: seated_cable_rows
name: Seated Cable Rows
status: complete
category: exercise
pattern: [horizontal_pull]
equipment: [cable]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: latissimus_dorsi
    role: primary
  - id: trap_middle
    role: primary
  - id: trap_lower
    role: primary
  - id: deltoid_posterior
    role: secondary
  - id: biceps_brachii
    role: secondary
  - id: rhomboids
    role: secondary
  - id: erector_spinae
    role: stabilizer

# ssd_2026 literature compilation. No absolute %MVIC values reported.
# Data is comparative (narrow vs wide grip, fixed vs free scapular) with effect sizes.
# Do NOT fabricate numeric %MVIC values. Effect sizes stored as notes.
muscle_activation_studies:
  - source_id: ssd_2026
    doi: null
    n: 14
    population: "resistance-trained men, 8-RM load, HD-sEMG"
    condition:
      variation: narrow_grip
      shoulder_abduction_deg: 0
    measurements:
      - {muscle: latissimus_dorsi, mean_pct_mvc: null, notes: "Significantly greater than wide grip, concentric and eccentric (ES = 1.08)"}
      - {muscle: biceps_brachii,   mean_pct_mvc: null, notes: "Maximized at 0° abduction (supinated, neutral, or pronated narrow grip)"}
  - source_id: ssd_2026
    doi: null
    n: 14
    population: "resistance-trained men, 8-RM load, HD-sEMG"
    condition:
      variation: wide_grip
      shoulder_abduction_deg: 90
    measurements:
      - {muscle: trap_middle,       mean_pct_mvc: null, notes: "Significantly greater than narrow grip, concentric ES = 1.35, eccentric ES = 2.79"}
      - {muscle: trap_lower,         mean_pct_mvc: null, notes: "Significantly greater than narrow grip; same ES pattern as trap_middle"}
      - {muscle: deltoid_posterior,  mean_pct_mvc: null, notes: "Significantly greater than narrow grip; lateral deltoid ES = 1.35"}
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      variation: fixed_scapular_row
      notes: "Scapular movement restricted throughout the set"
    measurements:
      - {muscle: deltoid_posterior, mean_pct_mvc: null, notes: "Significantly increased during concentric phase vs free scapular row (ES = 0.66)"}
      - {muscle: trap_middle,        mean_pct_mvc: null, notes: "Significantly increased during eccentric phase vs free scapular row (ES = 0.67)"}
      - {muscle: latissimus_dorsi,  mean_pct_mvc: null, notes: "Significantly increased during eccentric phase vs free scapular row (ES = 0.85)"}

joint_rom_required:
  shoulder_flexion_start_deg: 90
  elbow_flexion_deg: 110
  notes: >
    Movement begins with shoulders at ~90° flexion (arms extended forward). Concentric
    phase drives the shoulder from flexion through horizontal extension to neutral (0°
    for narrow grip; up to 90° abduction for wide grip). Elbows flex 90–110° at the
    terminal contraction. Torso remains upright with a neutral lumbar spine throughout.
  source: "ssd_2026"

strength_curve:
  type: ascending_descending
  sticking_point: terminal_lockout
  peak_force_position: mid_range
  notes: >
    Bell-shaped (ascending-descending) curve. Peak resistance at mid-range when the
    elbow is flexed ~90° and the shoulder is in neutral extension — optimal moment arm
    for both LD and trapezius. Sticking point is terminal lockout where the handle
    meets the torso: the horizontal lever arm shortens and scapular retraction must be
    completed against a compressed range. Cable maintains near-constant tension at
    full arm extension, unlike free-weight rows which lose tension at that position.
  source: "ssd_2026"

injury_risk:
  joint_stress:
    shoulder: low
    elbow: low
    lower_back: low
  common_injuries:
    - structure: lumbar_disc
      mechanism: excessive_forward_torso_lean_at_start
      risk_factors: [torso_lean_beyond_30_deg, heavy_loads, fatigue]
    - structure: shoulder_rotator_cuff
      mechanism: impingement_at_terminal_retraction
      risk_factors: [excessively_wide_grip, forced_scapular_retraction_at_end_range]
  contraindications: []

variations: []
progressions: []
alternatives: [bent_over_barbell_row, inverted_row]

sources:
  - source_id: ssd_2026
    title: "Sports Science Data Extraction: Vertical Pulling and Horizontal Rowing"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Seated Cable Rows

The seated cable row is an open-chain horizontal pulling exercise performed on a low-pulley cable machine. The seated position eliminates hip hinge mechanics and spinal erector loading, directing the stimulus entirely to the upper back, mid-trapezius, and posterior shoulder. Constant cable tension provides resistance throughout the full ROM — unlike free weights, which lose tension as the lever arm shortens at lockout. Grip width and shoulder abduction angle are the primary variables that shift load between the latissimus dorsi (narrow) and trapezius/posterior deltoid (wide).

## Execution

1. Sit at the machine with feet flat on the platform, knees slightly bent; grip the attachment at shoulder width or narrower
2. Begin with the torso upright and arms fully extended, cable taut — do not lean back beyond ~10° to initiate the pull
3. Pull the handle toward the lower sternum, driving the elbows behind the torso and retracting the scapulae
4. Pause briefly at full retraction; return the handle under control to full arm extension
5. Allow the scapulae to protract at the end of the eccentric — do not hold them pinned throughout the set

## What the Data Shows

The seated cable row data from ssd_2026 is comparative — no absolute %MVIC values are reported. The findings are effect sizes from a 14-person HD-sEMG study at 8-RM.

**Narrow grip (0° shoulder abduction)** produces significantly greater latissimus dorsi activation across both concentric and eccentric phases (ES = 1.08 vs wide grip). Biceps brachii is also maximized at narrow grip angles. The narrow-grip cable row is the preferred variant for LD development.

**Wide grip (90° shoulder abduction)** produces significantly greater activation of the middle and lower trapezius (concentric ES = 1.35, eccentric ES = 2.79) and posterior/lateral deltoid (ES = 1.35). The wide-grip cable row is primarily a rear-delt and trap exercise.

**Fixed vs free scapular movement** changes target muscle emphasis across phases. Restricting scapular movement increases posterior deltoid in the concentric phase (ES = 0.66) and traps + LD in the eccentric phase (ES = 0.85–0.67). Free scapular movement distributes load evenly and reinforces normal scapulohumeral coordination — preferred for long-term shoulder health. Fixed scapular technique can be used selectively for eccentric trap or LD isolation emphasis.

## Grip Width Selection

| Goal | Grip | Shoulder abduction |
|------|------|--------------------|
| LD hypertrophy | Narrow (V-bar, supinated) | 0° |
| Upper/mid trap | Wide (straight bar, pronated) | 60–90° |
| Rear delt | Wide + fixed scapula | 90° |
| General back | Neutral narrow | 0° |

## Constant Tension Advantage

Free-weight rows (barbell, dumbbell) lose resistance at full arm extension because the moment arm collapses when the weight stack reaches its lowest point relative to the shoulder. The cable maintains near-constant tension throughout, including at the fully stretched position. This makes the seated cable row superior for training the stretched lengthened position of the LD and trapezius — where mechanosensitive hypertrophy signaling is highest per recent stretch-mediated hypertrophy research.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Bent-over barbell row | Free weight; erector loading; heavier loads | Athletic strength; spinal erector training |
| Inverted row | Bodyweight; closed-chain; spinal unloading | Rehabilitation; bodyweight training |
| Single-arm cable row | Unilateral; greater ROM; anti-rotation core | Asymmetry correction; core integration |
| Face pull | High cable position; external rotation emphasis | Posterior cuff and rear delt isolation |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/seated_calf_raise.md -->

---
id: seated_calf_raise
name: Seated Calf Raise
status: complete
category: exercise
pattern: [isolation]
equipment: [machine]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: soleus
    role: primary
  - id: gastrocnemius_medial
    role: secondary
  - id: gastrocnemius_lateral
    role: secondary

# maeo_2023: Hypertrophy study comparing seated vs standing calf raise over a training period.
# Not an EMG %MVIC study — confirmed soleus selective hypertrophy vs standing raises.
# Seated position (knee ~90°) slackens gastrocnemius at proximal attachment,
# forcing soleus to carry nearly all plantarflexion load.
muscle_activation_studies: []

joint_rom_required:
  ankle_plantarflexion_deg: 40
  ankle_dorsiflexion_deg: 20
  knee_flexion_deg: 90
  source: "maeo_2023"

strength_curve:
  type: descending
  sticking_point: top_third
  peak_force_position: bottom
  notes: "Descending; torque production is maximized in deep dorsiflexion and declines linearly through the range; sticking point at full plantarflexion where soleus must bear load in a shortened state; bent knee eliminates gastrocnemius contribution throughout"
  source: "biomechanical inference; Maeo 2023"

injury_risk:
  joint_stress:
    ankle: low
    knee: low
  common_injuries:
    - structure: achilles_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, excessive_drop_below_platform, pre_existing_achilles_tendinopathy]
  contraindications:
    - acute_achilles_tendinopathy

variations: []
progressions: []
alternatives: [standing_calf_raises, donkey_calf_raises]

sources:
  - source_id: maeo_2023
    title: "Seated calf training selectively develops soleus hypertrophy vs standing calf training"
    author: "Maeo, Sumiaki et al."
    year: 2023
    doi: null
    credibility: rct
---

# Seated Calf Raise

The seated calf raise isolates the soleus by performing ankle plantarflexion with the knee bent at approximately 90°. The bent knee slackens the gastrocnemius at its proximal attachment (femoral condyles), removing it from meaningful load-bearing. The soleus — which only crosses the ankle, not the knee — maintains its full mechanical advantage and carries nearly all the plantarflexion load. Maeo 2023 confirmed that the seated raise selectively develops soleus hypertrophy compared to the standing raise.

## Execution

1. Sit on the machine with the lower thigh pad adjusted to rest just above the knees
2. Place the balls of the feet on the edge of the platform, heels off
3. Lift the thigh pad by pushing up on the heels to release the safety catch
4. Lower the heels below the platform for a full soleus stretch
5. Raise to full plantarflexion; hold briefly at the top, then lower under control

## Why the Soleus Matters

The soleus constitutes approximately 60% of calf muscle volume — larger than the gastrocnemius heads combined. It is primarily slow-twitch (Type I), making it resistant to fatigue but requiring high-volume, controlled loading for growth. Many programs under-develop the soleus by focusing exclusively on standing calf raises.

The seated raise is the only major exercise that fully isolates the soleus from gastrocnemius contribution.

## Maeo 2023 Key Finding

Direct comparison of seated vs standing calf raises over a training period:
- Standing calf raises → primarily gastrocnemius hypertrophy
- Seated calf raises → primarily **soleus** hypertrophy
- Neither variation produced significant hypertrophy in the other's primary target

The two variations are not interchangeable — they develop different muscles. A complete calf program requires both.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/seated_leg_curl.md -->

---
id: seated_leg_curl
name: Seated Leg Curl
status: complete
category: exercise
pattern: [isolation]
equipment: [machine]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: biceps_femoris
    role: primary
  - id: semitendinosus
    role: primary
  - id: semimembranosus
    role: primary
  - id: gastrocnemius_medial
    role: secondary
  - id: gastrocnemius_lateral
    role: secondary

# ebben_2009 (n=not reported): seated leg curl at hip 90° flexion.
# Overall hamstrings (combined): 80.8% ± 28% MVIC.
# Hip at 90° flexion pre-stretches the hamstrings at their proximal attachment (ischium).
muscle_activation_studies:
  - source_id: ebben_2009
    doi: null
    n: null
    population: "healthy adults, seated leg curl machine"
    condition:
      implement: machine
      phase: full_rep
      notes: "Seated position; hip at ~90° flexion — proximal hamstring pre-stretched"
    measurements:
      - {muscle: biceps_femoris, mean_pct_mvc: 80.8, sd: 28.0}

joint_rom_required:
  knee_flexion_deg: 130
  hip_flexion_deg: 90
  source: "ebben_2009"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped; hip at 90° places hamstrings at greater overall length than prone — the lengthened starting position provides a more favorable stretch-shortening stimulus"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    knee: low
    hip: low
  common_injuries:
    - structure: proximal_hamstring_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, heavy_load, pre_existing_proximal_tendinopathy]
  contraindications:
    - acute_proximal_hamstring_tendinopathy
    - acute_posterior_knee_injury

variations: []
progressions: []
alternatives: [lying_leg_curls, glute_ham_raise]

sources:
  - source_id: ebben_2009
    title: "Hamstring muscle EMG activity during various weight-bearing exercises"
    author: "Ebben, William P. et al."
    year: 2009
    doi: null
    credibility: rct
---

# Seated Leg Curl

The seated leg curl performs the same knee flexion pattern as the lying leg curl but from a seated position with the hip at approximately 90° flexion. This hip angle pre-stretches the hamstrings at their proximal (ischial) attachment before the knee flexion movement begins, placing all three heads in a more lengthened position throughout the range. The seated variation is preferred for hypertrophy applications based on the evidence for lengthened-position training advantages.

## Execution

1. Sit in the machine with the back pad adjusted so the knees align with the machine's pivot point
2. Place the ankle pad just above the heels; secure the thigh pad firmly to prevent hip lifting
3. Curl the legs downward and back toward the seat as far as the machine allows
4. Hold briefly at the contracted position, then return under control

## What the EMG Data Shows

Ebben 2009 (seated, hip 90°): **80.8% ± 28% MVIC** for the hamstrings overall. The large SD (28%) reflects individual differences in machine fit and hip angle maintenance.

## Why the Seated Version Is Mechanically Preferable

The hip angle at 90° creates two advantages:

1. **Proximal pre-stretch**: The hamstrings originate at the ischial tuberosity. When the hip is flexed 90°, this origin point moves further from the distal attachment (tibia), elongating the muscle before any active contraction.

2. **Lengthened-position hypertrophy**: Research consistently shows greater muscle growth when exercises load the target muscle at longer lengths.

## Seated vs Lying

| Feature | Lying | Seated |
|---------|-------|--------|
| Hip angle | 0° | 90° |
| Hamstring length | Mid-range | Lengthened |
| Preferred for | Bilateral symmetry check | Hypertrophy |

If only one curl variation is included in a program, the seated version is the first choice based on current evidence.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/seated_side_lateral_raise.md -->

---
id: seated_side_lateral_raise
name: Seated Side Lateral Raise
status: complete
category: exercise
pattern: [isolation]
equipment: [dumbbell]

difficulty:
  technical_complexity: 1
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

muscle_activation_studies:
  - source_id: campos_2020
    doi: "10.2478/hukin-2020-0033"
    n: 13
    population: "strength-trained men, 3.58 ± 2.90 yr training experience"
    condition:
      load_pct_1rm: 60
      implement: dumbbell
      phase: dynamic
      notes: "1 set of 12 repetitions; seated variation"
    measurements:
      - muscle: deltoid_lateral
        mean_pct_mvc: 30.3
        sd: null
      - muscle: deltoid_anterior
        mean_pct_mvc: 21.2
        sd: null
      - muscle: deltoid_posterior
        mean_pct_mvc: 24.0
        sd: null

joint_rom_required:
  shoulder_abduction_deg: 90
  source: "biomechanical inference from side_lateral_raise"

strength_curve:
  type: ascending
  sticking_point: top_third
  peak_force_position: top
  notes: "Identical ascending gravity profile to standing variation; momentum eliminated by seated position"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    shoulder: low
    elbow: low
  common_injuries:
    - structure: supraspinatus_tendon
      mechanism: subacromial_impingement
      risk_factors: [internal_rotation_above_90_deg, load_too_heavy, pre_existing_impingement]
  contraindications:
    - acute_shoulder_impingement

variations: []
progressions: []
alternatives: [side_lateral_raise, cable_seated_lateral_raise]

sources:
  - title: "Different Shoulder Exercises Affect the Activation of Deltoid Portions in Resistance-Trained Individuals"
    author: "Campos, Y. A. C. et al."
    year: 2020
    doi: "10.2478/hukin-2020-0033"
    source_id: campos_2020
    credibility: rct
---

# Seated Side Lateral Raise

The seated side lateral raise is the strict-form variant of the standard lateral raise. By sitting, the lower body is removed from the kinetic chain, eliminating the leg drive and hip extension that frequently turns standing lateral raises into a momentum-assisted exercise. The activation profile of the seated variation is mechanically identical to the standing form — lateral deltoid remains the primary mover — but the seated position enforces pure deltoid-driven abduction.

## Execution

1. Sit upright at the end of a bench with dumbbells at the sides
2. Depress the scapulae; do not allow the upper traps to initiate the movement with a shrug
3. Raise the arms laterally in an arc to approximately shoulder height (90° abduction)
4. Lead with the elbows rather than the hands; keep a slight elbow bend throughout
5. Lower under control, maintaining tension through the eccentric

## Why Seated vs Standing

Standing lateral raises allow three compensatory patterns:
1. **Leg drive** — a slight knee bend and hip push uses momentum to clear the initial dead zone
2. **Torso lean** — leaning away from the working side extends the effective moment arm
3. **Trap shrug** — upper trapezius takes over when the load exceeds the lateral delt's capacity

The seated position blocks all three. The practical effect is that the effective load at the deltoid is higher per pound lifted, which is why lifters typically use noticeably less weight seated than standing.

## EMG Data

Campos et al. (2020) measured deltoid activation during the seated dumbbell lateral raise at 60% 1RM in 13 strength-trained men:

| Muscle | Mean % MVIC |
|--------|-------------|
| Deltoid lateral | 30.3% |
| Deltoid posterior | 24.0% |
| Deltoid anterior | 21.2% |

The notably similar anterior and posterior deltoid values reflect the inherent multi-head co-activation of shoulder abduction in the frontal plane. The lateral head dominates but neither the anterior nor posterior head is truly silent during the movement.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/side_lateral_raise.md -->

---
id: side_lateral_raise
name: Side Lateral Raise
status: complete
category: exercise
pattern: [isolation]
equipment: [dumbbell]

difficulty:
  technical_complexity: 1
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

# Multiple studies across different humeral rotation conditions.
# Sweeney 2014 used bent-arm (elbow ~90°) variation at 70% 1RM → deltoid_lateral 77% ± 16.1%.
# Coratella 2020 shows humeral rotation dramatically shifts anterior vs posterior delt dominance:
#   External rotation → anterior delt 80%; Internal rotation → posterior delt 85%.
# Standard neutral position: lateral delt is primary (30–77% MVIC across studies).
muscle_activation_studies:
  - source_id: campos_2020
    doi: "10.1515/hukin-2020-0023"
    n: 13
    population: "resistance-trained males, 60% 1RM, standard neutral"
    condition:
      load_pct_1rm: 60
      implement: dumbbell
      phase: full_rep
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 21.2, sd: null}
      - {muscle: deltoid_lateral,   mean_pct_mvc: 30.3, sd: null}
      - {muscle: deltoid_posterior, mean_pct_mvc: 24.0, sd: null}
  - source_id: coratella_2020
    doi: "10.3390/ijerph17176015"
    n: 10
    population: "competitive bodybuilders, neutral humeral rotation"
    condition:
      load_pct_1rm: null
      implement: dumbbell
      phase: concentric
      notes: "Standard neutral grip"
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 36.0, sd: null}
      - {muscle: deltoid_lateral,   mean_pct_mvc: 55.0, sd: null}
      - {muscle: deltoid_posterior, mean_pct_mvc: 52.0, sd: null}
  - source_id: coratella_2020
    doi: "10.3390/ijerph17176015"
    n: 10
    population: "competitive bodybuilders, external humeral rotation"
    condition:
      load_pct_1rm: null
      implement: dumbbell
      phase: concentric
      notes: "Humerus externally rotated — shifts emphasis to anterior deltoid"
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 80.0, sd: null}
      - {muscle: deltoid_lateral,   mean_pct_mvc: 48.0, sd: null}
      - {muscle: deltoid_posterior, mean_pct_mvc: 36.0, sd: null}
  - source_id: coratella_2020
    doi: "10.3390/ijerph17176015"
    n: 10
    population: "competitive bodybuilders, internal humeral rotation"
    condition:
      load_pct_1rm: null
      implement: dumbbell
      phase: concentric
      notes: "Humerus internally rotated — shifts emphasis to posterior deltoid"
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 34.0, sd: null}
      - {muscle: deltoid_lateral,   mean_pct_mvc: 52.0, sd: null}
      - {muscle: deltoid_posterior, mean_pct_mvc: 85.0, sd: null}
  - source_id: sweeney_2014
    doi: null
    n: 16
    population: "healthy males, 70% 1RM, bent-arm variation"
    condition:
      load_pct_1rm: 70
      implement: dumbbell
      phase: full_rep
      notes: "Bent-arm (elbow ~90°) reduces moment arm and allows heavier load"
    measurements:
      - {muscle: deltoid_anterior,  mean_pct_mvc: 32.0, sd: 18.5}
      - {muscle: deltoid_lateral,   mean_pct_mvc: 77.0, sd: 16.1}
      - {muscle: deltoid_posterior, mean_pct_mvc: 33.0, sd: 14.4}

joint_rom_required:
  shoulder_abduction_deg: 90
  source: "Sweeney 2014"

strength_curve:
  type: ascending
  sticking_point: top_third
  peak_force_position: top
  notes: "Gravity moment arm increases from 0 at side to maximum at 90° abduction — resistance is lowest at the start and peaks at full parallel position"
  source: "Kassiano 2023"

injury_risk:
  joint_stress:
    shoulder: low
    elbow: low
  common_injuries:
    - structure: supraspinatus_tendon
      mechanism: subacromial_impingement
      risk_factors: [internal_rotation_past_90_deg, pronated_grip_at_top, pre_existing_impingement]
    - structure: upper_trapezius
      mechanism: compensatory_shrug_under_load
      risk_factors: [load_too_heavy, fatigue, poor_scapular_depression_cue]
  contraindications:
    - acute_shoulder_impingement
    - supraspinatus_tear

variations: []
progressions: []
alternatives: [cable_seated_lateral_raise]

sources:
  - source_id: campos_2020
    title: "Different Shoulder Exercises Affect the Activation of Deltoid Portions in Resistance-Trained Individuals"
    author: "Campos, Yuri de Almeida Costa et al."
    year: 2020
    doi: "10.1515/hukin-2020-0023"
    credibility: rct
  - source_id: coratella_2020
    title: "An Electromyographic Analysis of Lateral Raise Variations and Frontal Raise in Competitive Bodybuilders"
    author: "Coratella, Giuseppe et al."
    year: 2020
    doi: "10.3390/ijerph17176015"
    credibility: rct
  - source_id: sweeney_2014
    title: "Dynamite Delts: ACE Research Identifies Top Shoulder Exercises"
    author: "Sweeney, Samantha; Porcari, John P. et al."
    year: 2014
    doi: null
    credibility: rct
---

# Side Lateral Raise

The side lateral raise is the primary open-chain isolation exercise for the lateral deltoid. Performed by abducting the arms from the sides to shoulder height against a dumbbell or cable load, it produces the characteristic shoulder width associated with bodybuilding aesthetics. Despite its apparent simplicity, the lateral raise is highly sensitive to humeral rotation — a single technical variable that shifts the primary load among all three deltoid heads.

## Execution

1. Stand with dumbbells at the sides, arms nearly straight (slight elbow bend to reduce joint stress)
2. Depress the scapulae before initiating — do not allow the traps to shrug as the primary movement
3. Raise the arms to approximately shoulder height (90° abduction), leading with the elbows rather than the hands
4. Keep the thumbs slightly lower than the pinkies throughout (slight internal rotation) to avoid subacromial impingement
5. Lower under control; avoid letting the weight crash back to the starting position

## What the EMG Data Shows

Three independent studies establish the lateral deltoid as the primary mover in the standard neutral raise:

| Study | Condition | Deltoid Lateral | Deltoid Anterior | Deltoid Posterior |
|-------|-----------|-----------------|------------------|-------------------|
| Campos 2020 | 60% 1RM, neutral | 30.3% | 21.2% | 24.0% |
| Coratella 2020 | Neutral, bodybuilders | 55.0% | 36.0% | 52.0% |
| Sweeney 2014 | 70% 1RM, bent-arm | 77.0% ± 16.1% | 32.0% ± 18.5% | 33.0% ± 14.4% |

The wide range in lateral deltoid values (30–77%) reflects both load and technique differences. Sweeney 2014 used a bent-arm (elbow 90°) variation at 70% 1RM — shorter moment arm, heavier absolute load, highest values. The Campos 2020 values at 60% 1RM with full extension represent the stricter, lighter version.

## The Humeral Rotation Effect

Coratella 2020 is the critical study for programming decisions. The three rotation conditions produced dramatically different activation profiles:

| Rotation | Lateral Delt | Anterior Delt | Posterior Delt |
|----------|--------------|---------------|----------------|
| Neutral | 55% | 36% | 52% |
| External | 48% | **80%** | 36% |
| Internal | 52% | 34% | **85%** |

External rotation primarily recruits the anterior deltoid — a muscle already well-stimulated by pressing. Internal rotation at end-range (above 90°) increases subacromial impingement risk. Keep the thumb-down position only through the middle range; do not force full internal rotation at peak.

## Cable vs Dumbbell

Free-weight dumbbells have zero resistance when the arms hang at the sides and peak resistance at 90° abduction. This mismatches the deltoid's strength curve and creates a dead zone at the start. Cable variations from a low pulley provide resistance at longer deltoid lengths. See `cable_seated_lateral_raise` for cable-specific guidance.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Seated lateral raise | Eliminates leg drive and momentum | Strict isolation |
| Cable lateral raise | Constant tension at bottom of range | Lengthened-position loading |
| Bent-arm lateral raise | Shorter moment arm; heavier load | Load progression |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/single_leg_leg_extension.md -->

---
id: single_leg_leg_extension
name: Single-Leg Leg Extension
status: complete
category: exercise
pattern: [isolation]
equipment: [machine]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: rectus_femoris
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: vastus_medialis
    role: primary
  - id: vastus_intermedius
    role: primary

# saeterbakken_2021: Compared bilateral vs unilateral leg extension.
# Reported effect sizes only — no absolute %MVIC values.
# Key finding: unilateral produces greater peak force and activation per leg vs bilateral (bilateral deficit).
muscle_activation_studies:
  - source_id: saeterbakken_2021
    doi: null
    n: null
    population: "healthy adults, bilateral vs unilateral leg extension comparison"
    condition:
      implement: machine
      phase: full_rep
      notes: "Effect sizes only reported — no absolute %MVIC. Unilateral showed greater per-leg activation than bilateral due to bilateral deficit."
    measurements: []

joint_rom_required:
  knee_flexion_deg: 90
  knee_extension_deg: 0
  source: "saeterbakken_2021"

strength_curve:
  type: ascending
  sticking_point: top_third
  peak_force_position: top
  notes: "Same ascending profile as bilateral leg extension — peak load at full extension"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    knee: moderate
    patellofemoral: moderate
  common_injuries:
    - structure: patellofemoral_joint
      mechanism: shear_stress_at_full_extension
      risk_factors: [pre_existing_patellofemoral_pain, heavy_load]
    - structure: patellar_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, heavy_load, pre_existing_patellar_tendinopathy]
  contraindications:
    - acute_patellofemoral_pain_syndrome
    - acute_patellar_tendinopathy

variations: []
progressions: []
alternatives: [leg_extensions]

sources:
  - source_id: saeterbakken_2021
    title: "The effects of bilateral and unilateral lower limb exercises on muscle strength and hypertrophy"
    author: "Saeterbakken, Atle H. et al."
    year: 2021
    doi: null
    credibility: rct
---

# Single-Leg Leg Extension

The single-leg leg extension is the unilateral version of the standard leg extension, performed one leg at a time on the same machine. Saeterbakken 2021 found that unilateral leg extension produces greater peak force and activation per leg compared to the bilateral version — a manifestation of the bilateral deficit. This makes the single-leg extension useful for identifying and correcting left-right quadriceps strength asymmetries.

## Execution

1. Set up the machine identically to the bilateral version; sit with the non-working leg hanging free or resting to the side
2. Extend the working leg to full extension under controlled speed
3. Hold briefly at the top contraction, then lower under control
4. Complete all reps for one leg before switching

## The Bilateral Deficit

When both legs extend simultaneously, each leg produces less force than it would working alone. For the leg extension specifically, Saeterbakken 2021 confirmed that switching to unilateral work increases per-leg neural demand — making single-leg variations appropriate for trainees who have plateaued on bilateral leg extensions or need to address asymmetries.

## When to Use

- **Asymmetry correction**: When left-right strength differences are identified in bilateral testing
- **Rehabilitation**: Post-injury limb retraining
- **Volume accumulation**: Unilateral volume with less systemic fatigue than bilateral

For primary quadriceps development, the bilateral leg extension is more time-efficient. Include single-leg work when asymmetry is a concern.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/snatch.md -->

---
id: snatch
name: Snatch
status: complete
category: exercise
pattern: [hinge]
equipment: [barbell]

difficulty:
  technical_complexity: 5
  strength_prerequisite: 3
  mobility_prerequisite: 5

muscles:
  - id: erector_spinae
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: gluteus_maximus
    role: primary
  - id: multifidus
    role: primary
  - id: trap_upper
    role: primary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: rectus_femoris
    role: secondary
  - id: vastus_medialis
    role: secondary
  - id: deltoid_anterior
    role: secondary
  - id: triceps_brachii
    role: secondary
  - id: gastrocnemius
    role: secondary
  - id: soleus
    role: secondary
  - id: forearm_flexors
    role: stabilizer

# Geisler 2023 measured Hang Power Snatch (HPS) — a proxy for the full snatch's
# pull phase. The full snatch starts from the floor (adds first-pull demands) and
# catches in a full overhead squat (adds quad/hip squat recovery demands not
# captured here). Pull-phase activation is comparable; catch-phase ES values
# reflect the overhead eccentric load, which applies to the full snatch catch equally.
muscle_activation_studies:
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 10
    population: "advanced"
    condition:
      load_pct_1rm: 50
      phase: pull_and_catch
      notes: "Hang Power Snatch proxy; full snatch adds overhead squat recovery demand"
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 175.69, sd: 134.95}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 50
      phase: pull_and_catch
      notes: "Hang Power Snatch proxy"
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 294.28, sd: 152.77}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 90
      phase: pull_and_catch
      notes: "Hang Power Snatch proxy; peak ES values"
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 371.62, sd: 271.60}

joint_rom_required:
  hip_flexion_deg: 130
  knee_flexion_deg: 135
  ankle_dorsiflexion_deg: 38
  shoulder_flexion_deg: 180
  shoulder_external_rotation_deg: 90
  shoulder_internal_rotation_deg: 70
  notes: >
    Setup: 120° hip flexion (same as power snatch). Full squat catch is more demanding
    than the power snatch: requires 130–135° knee flexion, 38° ankle dorsiflexion at
    full depth. Overhead lockout: 180° shoulder flexion required throughout squat recovery.
    Thoracic extension mobility is a secondary limiting factor — restricted thoracic extension
    forces forward trunk lean, shifting the bar forward out of the midfoot line.
  source: "nasm_2020 / setpt_2020; squat depth from Schoenfeld 2010"

strength_curve:
  type: bell_shaped
  sticking_point: first_pull_to_transition
  peak_force_position: second_pull
  notes: >
    Pull phase: bell-shaped GRF curve identical to power snatch — first pull ~1.5×BW,
    unweighting at double-knee bend ~1.0×BW, second pull peak 2.0–2.5×BW.
    The wider snatch grip (vs clean grip) shortens the effective pull height, requiring
    greater barbell velocity to achieve the catch. This is why snatch 1RM is consistently
    ~63–65% of clean-and-jerk 1RM across elite weightlifters.
    Catch/squat-recovery phase: ascending (same as front squat from deep position).
    ES at catch: elite, 90% 1RM: 372% MVIC — overhead eccentric stabilisation during
    the squat descent is the defining physiological demand of the full snatch vs the power snatch.
  source: "geisler_2023 / garhammer_1993"

injury_risk:
  joint_stress:
    shoulder: high
    wrist: high
    lower_back: high
    knee: moderate
  common_injuries:
    - structure: rotator_cuff
      mechanism: eccentric_overload_at_catch_and_squat_recovery
      risk_factors: [insufficient_shoulder_flexion, restricted_thoracic_extension, fatigue]
    - structure: lumbar_disc
      mechanism: hyperextension_during_catch
      risk_factors: [excessive_lordosis, poor_bracing, bar_drifting_forward]
    - structure: knee
      mechanism: valgus_collapse_in_deep_squat_catch
      risk_factors: [insufficient_hip_external_rotation, weak_gluteus_medius, restricted_ankle_dorsiflexion]
  contraindications:
    - acute_shoulder_injury
    - lumbar_herniation
    - acute_knee_injury

variations: [power_snatch]
progressions: [snatch_pull, overhead_squat]
alternatives: [power_snatch]

sources:
  - source_id: geisler_2023
    title: "Effects of Expertise on Muscle Activity during the Hang Power Clean and Hang Power Snatch Compared to Snatch and Clean Pulls"
    author: "Geisler S et al."
    year: 2023
    doi: "10.52082/jssm.2023.778"
    credibility: rct
  - source_id: garhammer_1993
    title: "A Review of Power Output Studies of Olympic and Powerlifting: Methodology, Performance Prediction, and Evaluation Tests"
    author: "Garhammer, J."
    year: 1993
    doi: "10.1519/1533-4287(1993)007<0076:AROPOS>2.3.CO;2"
    credibility: literature_review
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
  - source_id: everett_weightlifting
    title: "Olympic Weightlifting: A Complete Guide for Athletes & Coaches"
    author: "Greg Everett"
    year: 2016
    doi: null
    credibility: practitioner
---

# Snatch

The snatch is one of the two Olympic competition lifts. The barbell is pulled from the floor with a wide grip and received overhead in a full squat — simultaneously the most technically demanding and mobility-intensive movement in competitive strength sports. The bar travels from the floor to arm's length overhead in a single uninterrupted motion; the lifter descends into a full overhead squat to receive it, then stands to complete the lift. World-class performances require coordinating more than 30 joints and over 200 muscles within approximately 1 second.

## Execution

1. **Setup:** Wide snatch grip (roughly 1.5× shoulder width, measured by a forearm-length from the hip). Feet hip-width, bar over mid-foot. Hips below shoulders, shoulders over or in front of the bar. 120° hip flexion, neutral spine throughout.
2. **First pull (floor to knee):** Push the floor away; maintain constant back angle. Bar stays against the shins and thighs.
3. **Transition (double-knee bend):** As bar passes the knees, knees re-bend and hips drive forward — the torso angle rises and the bar accelerates toward the hips.
4. **Second pull (triple extension):** Explosive simultaneous hip, knee, and ankle extension. Shrug at peak. At full extension the body is vertical and slightly posterior; arms still long.
5. **Third pull (pull-under):** Simultaneously pull the body under the bar by pulling the elbows high and wide; the bar continues upward while the body drops into the overhead squat position. The bar must be locked overhead with elbows fully extended before the catch is complete.
6. **Overhead squat catch:** Receive the bar in a full squat — hips below parallel, bar directly over the midfoot, arms locked, torso upright. Stabilise the position before standing.
7. **Recovery:** Drive through the floor to stand while maintaining the overhead position; lower the bar to the thighs and then the floor.

## The Pull Phase: EMG Data

The pull-phase erector spinae demand scales dramatically with expertise. At 50% 1RM: advanced athletes 176% MVIC, elite athletes 294% MVIC. This does not reflect greater brute force but rather superior motor unit synchronisation — elite lifters recruit more muscle simultaneously rather than sequentially, producing more force in less time.

At 90% 1RM, elite erector spinae activation reaches 372% MVIC. This value reflects the full pull-and-catch cycle; the overhead squat catch portion contributes the eccentric deceleration component that elevates ES above the equivalent snatch pull (≈212% MVIC at similar loads).

## The Full Snatch vs the Power Snatch

The critical difference is the catch depth:

| Parameter | Power Snatch | Full Snatch |
|-----------|-------------|------------|
| Catch depth | ≥90° knee flexion (partial squat) | Below parallel (full squat) |
| Maximum load | ~85–90% of snatch 1RM | 100% |
| Mobility demand | Shoulder dominant | Shoulder + full squat + ankle |
| ES at catch | High | Higher — longer eccentric overhead stabilisation during squat descent |

The full snatch can handle more total load because the lifter does not need to generate enough bar height for a power (partial) catch — the bar only needs to rise high enough for the lifter to drop under it into a deep position.

## The 63% Rule

Across elite weightlifters, snatch 1RM is consistently ~63–65% of clean-and-jerk 1RM. This ratio reflects the fundamental constraint of the snatch: the wide grip shortens the effective pull height, requiring greater barbell velocity to achieve a stable overhead catch. The clean grip's narrower width allows a higher bar trajectory at equivalent force input, enabling heavier absolute loads in the clean.

## Mobility Priorities

The snatch is the most mobility-dependent barbell exercise. Deficits in any of these create compensatory faults that cannot be trained around:

1. **Shoulder flexion** (≥180°): Bar must sit directly over midfoot in the overhead squat; any restriction pushes the bar forward
2. **Thoracic extension**: Supports upright torso in the catch; restriction causes forward lean
3. **Ankle dorsiflexion** (≥38° at full depth): Restricts squat depth; forces heel rise and forward bar displacement
4. **Hip external rotation**: Determines squat stance width; restriction causes valgus collapse at depth

Shoulder flexibility correlates significantly with trunk angle at depth (r = −0.67, p = 0.003): restricted lifters lean forward, which moves the bar off the midfoot line and destabilises the catch.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/snatch_pull.md -->

---
id: snatch_pull
name: Snatch Pull
status: complete
category: exercise
pattern: [hinge]
equipment: [barbell]

difficulty:
  technical_complexity: 4
  strength_prerequisite: 3
  mobility_prerequisite: 3

muscles:
  - id: erector_spinae
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: gluteus_maximus
    role: primary
  - id: multifidus
    role: primary
  - id: trap_upper
    role: primary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: rectus_femoris
    role: secondary
  - id: vastus_medialis
    role: secondary
  - id: gastrocnemius
    role: secondary
  - id: soleus
    role: secondary
  - id: forearm_flexors
    role: stabilizer

# Geisler 2023: Hang Snatch Pull (HSP) across three expertise levels and two loads.
# %MVIC values, pull phase only (no catch). ES values substantially lower than power snatch
# because catch-phase eccentric stabilisation demand is absent.
muscle_activation_studies:
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 50
      phase: pull
    measurements:
      - {muscle: trap_upper,     mean_pct_mvc: 78.58, sd: 27.10}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 10
    population: "advanced"
    condition:
      load_pct_1rm: 50
      phase: pull
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 101.97, sd: 99.91}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 50
      phase: pull
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 147.35, sd: 147.64}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 11
    population: "beginners"
    condition:
      load_pct_1rm: 90
      phase: pull
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 144.53, sd: 185.68}
  - source_id: geisler_2023
    doi: "10.52082/jssm.2023.778"
    n: 6
    population: "elite"
    condition:
      load_pct_1rm: 90
      phase: pull
    measurements:
      - {muscle: erector_spinae, mean_pct_mvc: 211.80, sd: 190.72}

joint_rom_required:
  hip_flexion_deg: 120
  notes: "Setup: 120° hip flexion with snatch-width grip. No catch — terminates at full triple extension with shrug."
  source: "nasm_2020 / geisler_2023"

strength_curve:
  type: bell_shaped
  sticking_point: first_pull_to_transition
  peak_force_position: second_pull
  notes: >
    Wide snatch grip shortens effective pull height, placing greater velocity demand
    on the second pull compared to the clean pull.
    No catch allows loading at 100–140% of snatch 1RM — the primary overload mechanism
    for athletes who cannot increase overhead catch capacity.
    ES pull-phase activation (elite 148–212% MVIC) is ~43–56% lower than the power snatch
    (elite 294–372% MVIC) because catch eccentric demand is absent.
    Lifting straps increase latissimus dorsi and VL activation by removing grip as a limiter.
  source: "geisler_2023 / nsca_2016"

injury_risk:
  joint_stress:
    lower_back: moderate
    knee: low
  common_injuries:
    - structure: lumbar_disc
      mechanism: shear_under_load
      risk_factors: [bar_drifting_forward, poor_bracing]
  contraindications:
    - acute_lumbar_injury

variations: [power_snatch]
progressions: []
alternatives: [clean_pull]

sources:
  - source_id: geisler_2023
    title: "Effects of Expertise on Muscle Activity during the Hang Power Clean and Hang Power Snatch Compared to Snatch and Clean Pulls"
    author: "Geisler S et al."
    year: 2023
    doi: "10.52082/jssm.2023.778"
    credibility: rct
  - source_id: nsca_2016
    title: "NSCA Position Statement on Weightlifting for Sports Performance"
    author: "National Strength and Conditioning Association"
    year: 2016
    credibility: expert_consensus
  - source_id: nasm_2020
    title: "NASM Optimum Performance Training"
    author: "National Academy of Sports Medicine"
    year: 2020
    credibility: expert_consensus
---

# Snatch Pull

The snatch pull is the snatch family's pulling derivative. The barbell is pulled from the floor with a wide (snatch) grip through a full triple extension and terminal shrug, but without the overhead catch of the power snatch or snatch. It is the primary overload tool in Olympic weightlifting, allowing loads of 100–140% of snatch 1RM to develop pulling strength without the overhead mobility or technical demands of the catch.

## Execution

1. **Setup:** Feet hip-width, bar over mid-foot, wide snatch grip (roughly 1.5× shoulder width). 120° hip flexion, neutral spine, elbows fully extended.
2. **First pull (floor to knee):** Drive hips and knees simultaneously; maintain back angle. Bar stays close to the shins.
3. **Transition:** As bar passes the knees, knees re-bend and hips push forward.
4. **Second pull (triple extension):** Explosive simultaneous hip, knee, and ankle extension; shrug at full extension without flexing the elbows. Bar is driven vertically — no pull-under follows.
5. **Termination:** Movement ends at peak shrug height. Lower the bar under control.

## What the EMG Data Shows

The snatch pull's most important finding is the contrast with the power snatch. At elite level and 90% 1RM, erector spinae activation is 212% MVIC versus 372% MVIC in the power snatch — a ~43% reduction. This difference is entirely attributable to the overhead catch: the eccentric deceleration of a high-velocity bar at arm's length demands extreme spinal stabilisation that the snatch pull never generates.

This makes the snatch pull a lower-lumbar-risk option when the training goal is developing pulling power rather than catch-position stability. Athletes with lumbar concerns can train triple-extension mechanics without the spinal overload of the overhead catch.

Lifting straps increase latissimus dorsi and vastus lateralis activation by removing grip fatigue as a limiting factor, allowing leg drive and back pull to operate at full capacity.

Upper trapezius (beginners, 50% 1RM: 79% MVIC) reflects the terminal shrug demand.

## Programming Notes

The snatch pull is uniquely positioned as an overload tool: 100–140% of snatch 1RM is a standard programming range because the pull can tolerate substantially more load than the catch phase can receive. It is the standard prescription for athletes who have reached their overhead catch limit but need to continue developing first- and second-pull strength.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Power snatch | Adds overhead catch | Complete snatch training; catch stability |
| Clean pull | Narrow clean grip | Clean-specific pulling pattern |
| Hang snatch pull | Starts mid-thigh | Higher peak RFD; simplified first pull |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/standing_calf_raises.md -->

---
id: standing_calf_raises
name: Standing Calf Raises
status: complete
category: exercise
pattern: [isolation]
equipment: [machine]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: gastrocnemius_medial
    role: primary
  - id: gastrocnemius_lateral
    role: primary
  - id: soleus
    role: secondary

# riemann_2011: gastrocnemius_medial 46%, gastrocnemius_lateral 35%, soleus 35% MVIC.
# Standing (knee extended) → gastrocnemius at optimal length (crosses knee joint).
# Soleus activates at lower relative level vs gastrocnemius because knee extension
# puts gastrocnemius at a favorable length while soleus (knee-independent) contributes proportionally less.
muscle_activation_studies:
  - source_id: riemann_2011
    doi: null
    n: null
    population: "healthy adults, standing calf raise machine"
    condition:
      implement: machine
      phase: full_rep
      notes: "Standing with knee extended; gastrocnemius at optimal length"
    measurements:
      - {muscle: gastrocnemius_medial,  mean_pct_mvc: 46.0, sd: null}
      - {muscle: gastrocnemius_lateral, mean_pct_mvc: 35.0, sd: null}
      - {muscle: soleus,               mean_pct_mvc: 35.0, sd: null}

joint_rom_required:
  ankle_plantarflexion_deg: 40
  ankle_dorsiflexion_deg: 20
  source: "riemann_2011"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped; peak plantarflexion force at mid-range (heel level with platform); decreasing at extreme dorsiflexion and extreme plantarflexion"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    ankle: low
    knee: low
  common_injuries:
    - structure: achilles_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, excessive_drop_below_platform, pre_existing_achilles_tendinopathy]
    - structure: plantar_fascia
      mechanism: stretch_overload_at_bottom
      risk_factors: [excessive_dorsiflexion_range, pre_existing_plantar_fasciitis]
  contraindications:
    - acute_achilles_tendinopathy
    - acute_plantar_fasciitis

variations: []
progressions: []
alternatives: [seated_calf_raise, donkey_calf_raises]

sources:
  - source_id: riemann_2011
    title: "Electromyographic analysis of the calf complex during various heel-raise conditions"
    author: "Riemann, Bryan L. et al."
    year: 2011
    doi: null
    credibility: rct
---

# Standing Calf Raises

The standing calf raise is the primary gastrocnemius-biased calf exercise. Performed with the knee extended, the gastrocnemius — which crosses both the knee and ankle joints — is at its optimal mechanical length for force production. Riemann 2011 confirms gastrocnemius medial dominance (46% MVIC) with the soleus as secondary contributor at the same level as the lateral head (35% each).

## Execution

1. Position the shoulders under the machine pads; stand with the balls of the feet on the edge of the platform, heels hanging off
2. Keep the knees straight but not hyperextended throughout
3. Lower the heels below platform level to achieve full ankle dorsiflexion (calf stretch)
4. Raise the heels as high as possible into full plantarflexion; hold at the top for a count
5. Lower under full control — do not let the heels bounce at the bottom

## What the EMG Data Shows

Riemann 2011 (standing, knee extended):

| Muscle | Activation |
|--------|-----------|
| Gastrocnemius medial | 46% MVIC |
| Gastrocnemius lateral | 35% MVIC |
| Soleus | 35% MVIC |

The medial gastrocnemius dominates, consistent with its larger cross-sectional area.

## Why the Knee Must Be Extended

The gastrocnemius originates above the knee (femoral condyles). When the knee is bent, the gastrocnemius is slackened at its proximal end, reducing its mechanical advantage. Standing calf raises with the knee straight maximize gastrocnemius length and contribution. The seated calf raise (knee ~90°) dramatically reduces gastrocnemius contribution and isolates the soleus instead.

## Foot Position

| Foot position | Effect |
|--------------|--------|
| Toes forward | Balanced medial/lateral |
| Toes out (external rotation) | Slightly greater medial head emphasis |
| Toes in (internal rotation) | Slightly greater lateral head emphasis |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/standing_leg_curl.md -->

---
id: standing_leg_curl
name: Standing Leg Curl
status: complete
category: exercise
pattern: [isolation]
equipment: [machine]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: biceps_femoris
    role: primary
  - id: semitendinosus
    role: primary
  - id: semimembranosus
    role: primary
  - id: gastrocnemius_medial
    role: secondary
  - id: gastrocnemius_lateral
    role: secondary

# No peer-reviewed EMG data found for the standing leg curl.
# Hip at ~0° (similar to prone variation). Unilateral format is the key differentiator.
muscle_activation_studies: []

joint_rom_required:
  knee_flexion_deg: 130
  hip_flexion_deg: 0
  source: "biomechanical inference"

strength_curve:
  type: descending
  sticking_point: bottom_third
  peak_force_position: bottom
  notes: "Descending; hardest at the start (knee extended, greatest gravity moment arm for the pad); gets easier as the knee flexes and the moment arm shortens"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    knee: low
    hip: low
  common_injuries:
    - structure: proximal_hamstring_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, excessive_weight, unilateral_compensation]
  contraindications:
    - acute_proximal_hamstring_tendinopathy

variations: []
progressions: []
alternatives: [lying_leg_curls, seated_leg_curl]

sources: []
---

# Standing Leg Curl

The standing leg curl is a unilateral hamstring isolation exercise performed one leg at a time on a dedicated standing leg curl machine. The torso leans forward approximately 30–45° against a support pad, and the free leg curls the resistance pad toward the glutes. The unilateral format makes bilateral compensation impossible and allows direct left-right strength comparison.

## Execution

1. Adjust the machine so the pad rests just above the ankle of the working leg; the front of the knee is supported by the machine's upper pad
2. Lean forward into the support pad; hold the handles
3. Curl the working leg toward the glutes as high as possible
4. Hold briefly at peak contraction, then lower under control
5. Complete all reps for one leg before switching

## Mechanical Characteristics

The standing position places the hip at approximately 0° flexion (neutral), similar to the prone leg curl. The key difference from the lying version is the unilateral loading:
- Prevents the stronger leg from compensating
- Allows left/right activation comparison
- Adds minor postural demand from standing on one leg

No EMG data is available for this variation. Based on mechanical equivalence to the prone leg curl (schoenfeld_2014: biceps femoris 80% MVIC), similar activation is expected.

## When to Use

Most useful as a unilateral accessory or when bilateral leg curl machines are unavailable. For maximum hamstring hypertrophy stimulus, the seated leg curl (hip 90°) remains the first-choice variation.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/stiff_legged_barbell_deadlift.md -->

---
id: stiff_legged_barbell_deadlift
name: Stiff-Legged Barbell Deadlift
status: complete
category: exercise
pattern: [hinge]
equipment: [barbell]

difficulty:
  technical_complexity: 2
  strength_prerequisite: 2
  mobility_prerequisite: 3

muscles:
  - id: biceps_femoris
    role: primary
  - id: multifidus
    role: primary
  - id: gastrocnemius
    role: primary
  - id: gluteus_maximus
    role: primary
  - id: vastus_lateralis
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: erector_spinae
    role: secondary

# Miranda 2013: n=14, recreationally trained males, 70% 1RM.
# Values reported as % of mean EMG peak (not %MVIC normalized to isolated MVC).
# Values >100% are valid — they exceed the average dynamic EMG peak across the set.
muscle_activation_studies:
  - source_id: miranda_2013
    doi: null
    n: 14
    population: "recreationally trained males"
    condition:
      load_pct_1rm: 70
      phase: full_rep
      knee_flexion_deg: 0
    measurements:
      - {muscle: biceps_femoris,   mean_pct_mvc: 98.6,  sd: 28.5}
      - {muscle: vastus_lateralis, mean_pct_mvc: 101.1, sd: 14.6}
      - {muscle: multifidus,       mean_pct_mvc: 106.0, sd: 20.5}
      - {muscle: gastrocnemius,    mean_pct_mvc: 108.3, sd: 16.3}

joint_rom_required:
  hip_flexion_deg: null
  knee_flexion_deg: 0
  ankle_dorsiflexion_deg: null
  notes: >
    Knees remain locked in full extension throughout. The bar drifts slightly forward
    as depth increases, lengthening the moment arm to the lumbar spine. Greater hamstring
    flexibility is required than the RDL to reach the same bar height.
  source: "miranda_2013"

strength_curve:
  type: descending
  sticking_point: null
  peak_force_position: bottom
  notes: >
    Hamstring tension and lumbar extensor torque peak at maximum hip flexion.
    With knees locked, VL activation (101.1%) reflects isometric stabilization against
    knee hyperextension rather than active extension. Dynamic quadriceps recruitment is
    significantly lower than in the conventional deadlift (101.1% vs 128.3% VL, Miranda 2013).
  source: "miranda_2013"

injury_risk:
  joint_stress:
    lower_back: high
    knee: low
    hamstring: high
  common_injuries:
    - structure: lumbar_disc
      mechanism: flexion_under_load
      risk_factors: [locked_knees_increasing_moment_arm, excessive_depth, rapid_load_increase]
    - structure: proximal_hamstring
      mechanism: eccentric_overload_at_maximum_length
      risk_factors: [full_knee_extension_maximising_passive_tension, high_frequency]
  contraindications:
    - acute_lumbar_herniation
    - proximal_hamstring_tendinopathy
    - hamstring_strain

variations: [romanian_deadlift]
progressions: []
alternatives: []

sources:
  - source_id: miranda_2013
    title: "Electromyographic Activity of Lower Body Muscles during the Deadlift and Stiff-Legged Deadlift"
    author: "Bezerra ES, Simão R, Fleck SJ, Paz G, Maia M, Costa PB, Amadio AC, Miranda H, Serrão JC"
    year: 2013
    doi: null
    credibility: rct
  - source_id: coratella_2022
    title: "An Electromyographic Analysis of Romanian, Step-Romanian, and Stiff-Leg Deadlift"
    author: "Coratella G et al."
    year: 2022
    doi: "10.1519/JSC.0000000000004215"
    credibility: rct
---

# Stiff-Legged Barbell Deadlift

The stiff-legged barbell deadlift (SLDL) is a barbell hinge-pattern exercise performed with the knees locked in full extension throughout the movement. This fully-extended knee position places the hamstrings under maximum passive tension during the eccentric descent and increases the horizontal moment arm of the bar relative to the lumbar spine compared to the Romanian deadlift.

## Execution

1. Stand holding a barbell at hip height with a double-overhand grip, feet hip-width
2. Lock the knees in full extension and maintain this position throughout
3. Hinge at the hips with a neutral spine; allow the bar to drift slightly away from the legs as you descend
4. Lower until a maximum hamstring stretch is felt or the spine begins to flex
5. Drive the hips forward and extend to return to standing

## What the EMG Data Shows

At 70% 1RM (Miranda 2013), the SLDL produces high activation across the posterior chain: gastrocnemius 108.3%, multifidus 106.0%, vastus lateralis 101.1%, and biceps femoris 98.6% (% of mean EMG peak). Values exceeding 100% indicate the muscle contracted harder at some point in the lift than its average dynamic peak — not a methodological error.

The high VL activation (101.1%) in an exercise with locked knees is notable: the quadriceps are not driving knee extension but instead contracting isometrically to prevent knee hyperextension against the forward pull of the hamstrings. This value is nonetheless significantly lower than the conventional deadlift VL (128.3%) in the same study, confirming reduced quadriceps drive in straight-legged variations.

## Comparison with the Romanian Deadlift

The SLDL and RDL differ in two key ways: knee angle (0° vs 15–20°) and bar trajectory (drifts forward vs stays against the legs). These differences produce distinct neuromuscular profiles:

- **Gluteus maximus**: SLDL produces greater GM activation than the standard RDL (Effect Size 0.99, Coratella 2022). The fully-extended knee prevents the hamstrings from contributing to knee stabilization, shifting the hip extensor demand toward the gluteals.
- **Semitendinosus**: The RDL produces greater semitendinosus activation than the SLDL (ES 1.38). The slight knee flexion of the RDL keeps the medial hamstrings in a mechanically advantageous position for hip extension.
- **Spinal load**: Forward bar drift in the SLDL increases the horizontal moment arm to the lumbar spine, requiring greater static erector spinae force to maintain spine neutrality.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Romanian deadlift | 15–20° knee flexion; bar stays against legs | Hamstring-dominant development; lower spinal load |
| Step-SLDL | Standing on a raised platform | Maximum range of motion for advanced trainees |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/sumo_deadlift.md -->

---
id: sumo_deadlift
name: Sumo Deadlift
status: complete
category: exercise
pattern: [hinge]
equipment: [barbell]

difficulty:
  technical_complexity: 3
  strength_prerequisite: 3
  mobility_prerequisite: 3

muscles:
  - id: erector_spinae
    role: primary
  - id: biceps_femoris
    role: primary
  - id: gluteus_maximus
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: vastus_medialis
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: adductor_magnus
    role: secondary
  - id: adductor_longus
    role: secondary
  - id: multifidus
    role: secondary
  - id: gastrocnemius
    role: secondary
  - id: rhomboids
    role: stabilizer
  - id: trap_upper
    role: stabilizer
  - id: forearm_flexors
    role: stabilizer

# Hanen 2025 (doi: 10.3389/fbioe.2025.1597209): n=30, experienced male lifters, 85% 1RM.
# Values are median %MVC (IQR); stored as mean_pct_mvc with sd: null.
# Phase 1 = lift-off to mid-pull (knee level); Phase 2 = mid-pull to lockout.
# Escamilla 2002 (doi: 10.1097/00005768-200204000-00019): n=13, collegiate football players,
# 12-RM intensity. Values are mean %MVIC.
# Do NOT average across studies — intensity and populations differ.
muscle_activation_studies:
  - source_id: hanen_2025
    doi: "10.3389/fbioe.2025.1597209"
    n: 30
    population: "experienced male lifters"
    condition:
      load_pct_1rm: 85
      phase: concentric
      stance: sumo
      notes: "Phase 1: lift-off to knee level"
    measurements:
      - {muscle: biceps_femoris,   mean_pct_mvc: 71.3, sd: null}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 71.2, sd: null}
      - {muscle: vastus_lateralis, mean_pct_mvc: 63.3, sd: null}
      - {muscle: erector_spinae,   mean_pct_mvc: 74.7, sd: null}
  - source_id: hanen_2025
    doi: "10.3389/fbioe.2025.1597209"
    n: 30
    population: "experienced male lifters"
    condition:
      load_pct_1rm: 85
      phase: concentric
      stance: sumo
      notes: "Phase 2: knee level to lockout"
    measurements:
      - {muscle: biceps_femoris,   mean_pct_mvc: 69.9, sd: null}
      - {muscle: gluteus_maximus,  mean_pct_mvc: 74.2, sd: null}
      - {muscle: vastus_lateralis, mean_pct_mvc: 40.0, sd: null}
      - {muscle: erector_spinae,   mean_pct_mvc: 67.0, sd: null}
  - source_id: escamilla_2002
    doi: "10.1097/00005768-200204000-00019"
    n: 13
    population: "collegiate football players"
    condition:
      load: "12-RM"
      phase: concentric
      stance: sumo
    measurements:
      - {muscle: vastus_lateralis, mean_pct_mvc: 48.0, sd: null}
      - {muscle: vastus_medialis,  mean_pct_mvc: 44.0, sd: null}

joint_rom_required:
  hip_flexion_deg: 39.9
  knee_flexion_deg: 38.1
  ankle_dorsiflexion_deg: 15.0
  hip_abduction_deg: 7.9
  hip_external_rotation_deg: 15.4
  notes: >
    ROM values represent movement occurring during Phase 1 (Hanen 2025).
    The wide stance requires substantial hip abduction and external rotation mobility —
    a common limiting factor for athletes with restricted hip mobility.
  source: "hanen_2025"

strength_curve:
  type: descending
  sticking_point: null
  peak_force_position: bottom
  notes: >
    Torque demands peak at lift-off. Vastus lateralis demand drops significantly
    from Phase 1 (63.3% MVC) to Phase 2 (40.0% MVC), confirming quadriceps dominance
    during the initial drive with hip extensors taking over through lockout.
  source: "hanen_2025"

injury_risk:
  joint_stress:
    lower_back: moderate
    knee: moderate
    hip: moderate
  common_injuries:
    - structure: hip_adductors
      mechanism: groin_strain
      risk_factors: [extreme_foot_flare, inadequate_hip_mobility, rapid_load_increase]
    - structure: lumbar_disc
      mechanism: flexion_under_load
      risk_factors: [poor_bracing, trunk_forward_collapse]
    - structure: medial_knee
      mechanism: valgus_stress
      risk_factors: [knees_caving_inward, weak_hip_abductors]
  contraindications:
    - acute_hip_labral_tear
    - acute_groin_strain
    - acute_lumbar_herniation

variations: []
progressions: []
alternatives: []

sources:
  - source_id: hanen_2025
    title: "Biomechanical analysis of conventional and sumo deadlift"
    author: "Hanen NC, Ben Mansour K, Ertel GN, Duchene Y, Gauchard GC"
    year: 2025
    doi: "10.3389/fbioe.2025.1597209"
    credibility: rct
  - source_id: escamilla_2002
    title: "An electromyographic analysis of sumo and conventional style deadlifts"
    author: "Escamilla RF, Francisco AC, Kayes AV, Speer KP, Moorman CT"
    year: 2002
    doi: "10.1097/00005768-200204000-00019"
    credibility: rct
---

# Sumo Deadlift

The sumo deadlift is a barbell hinge-pattern exercise performed with a wide foot stance — typically two to three times hip-width — and feet rotated outward approximately 40–45°. This stance positions the hips closer to the bar, producing a more upright trunk angle and a shorter moment arm from the bar to the lumbar spine compared to the conventional deadlift.

## Execution

1. Set feet very wide, near the collars of the barbell, toes flared 40–45°
2. Bend at the hips and grip the bar inside the legs with a pronated, mixed, or hook grip; arms vertical
3. Inhale and brace hard; drive the knees outward over the toes before initiating the pull
4. Drive through the floor by spreading the feet apart; keep the chest up and the bar close
5. Extend hips and knees simultaneously; lock out by driving hips into the bar at the top

## What the EMG Data Shows

At 85% 1RM in experienced male lifters (Hanen 2025), the sumo deadlift shows distinct phase-specific activation:

**Phase 1 (floor to knee):** Erector spinae leads at 74.7% MVC, followed closely by biceps femoris (71.3%), gluteus maximus (71.2%), and vastus lateralis (63.3%). All major posterior chain muscles are near-maximally recruited during this demanding initial drive.

**Phase 2 (knee to lockout):** Gluteus maximus increases slightly to 74.2% MVC while vastus lateralis drops sharply to 40.0% MVC. The sumo deadlift transitions to a glute-dominant lockout with quadriceps contribution diminishing rapidly after bar clearance of the knees.

At 12-RM intensity (Escamilla 2002), sumo VL (48% MVIC) and VM (44% MVIC) exceeds conventional (VL 40%, VM 36%), confirming greater quadriceps demand during the drive phase. Medial gastrocnemius is lower in sumo (19%) than conventional (26%) — the wider stance reduces sagittal-plane calf stabilization demand.

## Biomechanical Distinctions from Conventional Deadlift

The wide stance creates two mechanical advantages:

1. **Reduced spinal moment arm**: Positioning the hips closer to the bar shortens the horizontal distance from the load to the lumbar spine, reducing shear forces on the vertebrae by roughly 8–10% compared to conventional.

2. **Multi-planar loading**: The sumo generates significantly greater frontal-plane hip abduction moments (7.9° vs 3.0° in conventional, Hanen 2025) and transverse-plane hip external rotation (15.4° vs 8.9°), recruiting hip adductors and external rotators in addition to standard sagittal-plane hip extensors.

Biceps femoris and gluteus maximus peak values are comparable between sumo and conventional styles, invalidating the myth that one is categorically superior for posterior chain development. The key difference is distribution: sumo is quadriceps-dominant early in the pull; conventional maintains higher hamstring and erector demand throughout.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Conventional deadlift | Narrower stance; greater trunk lean | Maximum hip extensor and erector demand |
| Semi-sumo | Intermediate stance; moderate foot flare | Athletes with moderate hip mobility |

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/tire_flip.md -->

---
id: tire_flip
name: Tire Flip
status: complete
category: exercise
pattern: [hinge]
equipment: [tire]

difficulty:
  technical_complexity: 3
  strength_prerequisite: 4
  mobility_prerequisite: 2

muscles:
  - id: gluteus_maximus
    role: primary
  - id: erector_spinae
    role: primary
  - id: rectus_femoris
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: vastus_medialis
    role: primary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: multifidus
    role: secondary
  - id: rectus_abdominis
    role: secondary
  - id: deltoid_anterior
    role: secondary
  - id: pectoralis_major
    role: secondary
  - id: triceps_long
    role: secondary
  - id: triceps_lateral
    role: secondary
  - id: triceps_medial
    role: tertiary
  - id: forearm_flexors
    role: secondary
  - id: trap_upper
    role: secondary
  - id: trap_middle
    role: tertiary
  - id: gastrocnemius_medial
    role: tertiary
  - id: gastrocnemius_lateral
    role: tertiary
  - id: soleus
    role: tertiary

muscle_activation_studies: []

joint_rom_required:
  hip_flexion_deg: 100
  knee_flexion_deg: 90
  shoulder_flexion_deg: 60
  source: "biomechanical inference from deadlift-like initial pull and push-over phase"

strength_curve:
  type: ascending
  sticking_point: initial_break_from_ground
  notes: "Hardest at the floor where the moment arm on the hips is longest. Once past 45 degrees, the push-over phase is mechanically easier."

injury_risk:
  joint_stress:
    lumbar_spine: high
    biceps_tendon: high
    shoulder: moderate
  common_injuries:
    - structure: biceps_tendon_distal
      mechanism: supinated_grip_under_heavy_load_during_initial_lift
      risk_factors: [underhand_curl_grip, excessive_tire_weight, fatigue]
    - structure: lumbar_disc
      mechanism: flexion_under_load_with_rounded_spine
      risk_factors: [excessive_tire_weight, poor_hip_hinge, fatigue]
    - structure: pectoralis_major
      mechanism: explosive_push_phase_with_arms_extended
      risk_factors: [cold_muscles, excessive_speed, pre_existing_strain]
  contraindications:
    - active_biceps_tendinopathy
    - acute_lumbar_disc_herniation
    - pectoralis_major_strain

variations: []
progressions: []
alternatives: [barbell_deadlift, power_clean]

sources: []
---

# Tire Flip

A full-body strongman movement where the athlete lifts and overturns a large tractor tire. The initial phase resembles a deadlift with a more forward lean (pulling from the ground with hip and knee extension), transitioning into an explosive push-over once the tire passes roughly 45 degrees. The tire flip is unique in that it combines hip-dominant pulling with a chest/shoulder push in a single repetition.

## Execution

1. **Setup.** Face the tire, feet shoulder-width apart, toes close to the base of the tire. Drop the hips and grip the bottom of the tire on the tread with fingers underneath. Chest drives into the tire surface. Use a pronated (palms-down) grip — never supinate (curl grip), as this dramatically increases biceps tendon rupture risk.
2. **Initial Drive.** Extend through the hips, knees, and ankles simultaneously, driving your chest into the tire. Think "leg press the ground away" rather than pulling with the arms. The arms hold position; the legs and hips generate force.
3. **Transition.** As the tire reaches approximately 45 degrees, step forward aggressively. Drive a knee into the tire for support. Quickly switch hand position from an underside grip to the upper face of the tire.
4. **Push-Over.** With hands on the upper face, extend through the arms and drive the tire forward and over. Use a split stance for balance.
5. **Reset.** Let the tire settle flat before approaching for the next rep.

## Programming Note

The tire flip carries higher injury risk than most strongman events, particularly to the distal biceps tendon. The single most important coaching cue is to avoid a supinated (underhand curl) grip during the initial lift — always grip with palms facing down. Tire flips are typically programmed for low reps (3-6 per set) with full recovery between sets. They are not well-suited to high-rep conditioning circuits due to the technical breakdown that occurs under fatigue. Choose a tire weight where technique remains clean for every rep.


---

<!-- FILE: exercises/tricep_dumbbell_kickback.md -->

---
id: tricep_dumbbell_kickback
name: Tricep Dumbbell Kickback
status: complete
category: exercise
pattern: [isolation]
equipment: [dumbbell]

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

# boehler_2011 (normalized to triangle push-up, NOT true %MVIC):
#   triceps_long 88% ± 33.0%, triceps_lateral 87% ± 23.7%.
# HIGHEST relative values in boehler_2011, BUT with the largest SD (33%).
# Ascending strength curve: near-zero resistance at start (elbow 90°, forearm vertical),
# maximum only at full extension (arm horizontal). Effective load at peak contraction is low.
muscle_activation_studies:
  - source_id: boehler_2011
    doi: null
    n: null
    population: "healthy adults, bent-over kickback"
    condition:
      implement: dumbbell
      phase: full_rep
      notes: "Normalized to triangle push-up = 100%, NOT true %MVIC. Ascending curve: near-zero effective load at start."
    measurements:
      - {muscle: triceps_long,    mean_pct_mvc: 88.0, sd: 33.0}
      - {muscle: triceps_lateral, mean_pct_mvc: 87.0, sd: 23.7}

joint_rom_required:
  elbow_flexion_deg: 90
  shoulder_extension_deg: 20
  hip_flexion_deg: 90
  source: "boehler_2011"

strength_curve:
  type: ascending
  sticking_point: top_third
  peak_force_position: top
  notes: "SEVERE gravity mismatch — maximum resistance only when arm is extended and horizontal; near-zero resistance at the start (elbow 90°, forearm vertical)"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    shoulder: low
    lower_back: low
  common_injuries:
    - structure: lumbar_disc
      mechanism: prolonged_hip_flexion_with_load
      risk_factors: [heavy_dumbbells, sustained_bent_over_position, pre_existing_lumbar_pathology]
  contraindications:
    - acute_lumbar_disc_herniation

variations: []
progressions: []
alternatives: [triceps_pushdown, cable_rope_overhead_triceps_extension]

sources:
  - source_id: boehler_2011
    title: "An electromyographic analysis of 3 muscles surrounding the elbow joint during a maximally forceful isometric contraction, concentric isotonic contraction, and 6 common exercises"
    author: "Boehler, Breanna et al."
    year: 2011
    doi: null
    credibility: rct
---

# Tricep Dumbbell Kickback

The dumbbell kickback is performed bent over with the upper arm held parallel to the floor, extending the forearm backward (toward the ceiling) against gravity. Boehler 2011 reports the highest normalized values among all triceps exercises tested — but this is largely an artifact of the ascending strength curve: the triceps is most activated at full extension, which is also the position of highest gravitational resistance. However, the effective load through most of the range is extremely low because gravity provides near-zero resistance when the forearm is vertical.

## Execution

1. Hold a dumbbell in one hand; place the opposite hand and knee on a bench for support
2. Raise the upper arm until it is parallel to the floor and close to the torso
3. Start with the forearm pointing down (elbow at ~90°)
4. Extend the elbow until the arm is fully extended and horizontal
5. Lower under control; do not allow the elbow to swing

## What the EMG Data Shows

Boehler 2011 normalized values:

| Exercise | Triceps Long | Triceps Lateral |
|----------|-------------|-----------------|
| Kickback | **88 ± 33.0** | **87 ± 23.7** |
| Overhead cable ext. | 81 ± 21.4 | 72 ± 16.5 |
| Rope pushdown | 81 ± 32.3 | 67 ± 15.7 |
| Skullcrusher | 70 ± 20.9 | 55 ± 14.1 |

These are the highest normalized values but the SD of 33% for the long head is the largest of any exercise. This reflects the severe load variability across subjects and the ascending curve's inconsistency.

## The Fundamental Limitation: Gravity Mismatch

The kickback's ascending strength curve creates a mechanical paradox:
- At the starting position (elbow 90°, forearm vertical): gravity applies near-zero torque — the triceps does almost no work
- Only at full extension (arm horizontal) does maximum gravitational resistance apply
- Only the last few degrees of extension are meaningfully loaded

The result: most of the rep is performed against negligible resistance. A cable pushdown or overhead extension loads the triceps throughout the entire range.

## When Kickbacks Are Useful

- **End-of-session finisher**: Very high rep sets (20–30) with light load accumulate metabolic stress at peak contraction
- **Proprioception and isolation practice**: The joint-fixed position trains clean elbow extension technique
- **Situations without cable access**: When only dumbbells are available

For primary triceps development, pushdowns and overhead extensions provide superior load application.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/triceps_pushdown.md -->

---
id: triceps_pushdown
name: Triceps Pushdown
status: complete
category: exercise
pattern: [isolation]
equipment: [cable]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: triceps_lateral
    role: primary
  - id: triceps_long
    role: primary
  - id: triceps_medial
    role: secondary

# boehler_2011: Values are normalized to triangle push-up = 100%, NOT true %MVIC.
# Rope attachment: triceps_long 81% ± 32.3%, triceps_lateral 67% ± 15.7%.
# Straight-bar: triceps_long 75% ± 29.3%, triceps_lateral 59% ± 14.3%.
# Rope produces higher activation for both heads vs straight-bar.
muscle_activation_studies:
  - source_id: boehler_2011
    doi: null
    n: null
    population: "healthy adults, rope attachment"
    condition:
      implement: cable_rope
      phase: full_rep
      notes: "Normalized to triangle push-up = 100%, NOT true %MVIC. Values are relative comparisons only."
    measurements:
      - {muscle: triceps_long,    mean_pct_mvc: 81.0, sd: 32.3}
      - {muscle: triceps_lateral, mean_pct_mvc: 67.0, sd: 15.7}
  - source_id: boehler_2011
    doi: null
    n: null
    population: "healthy adults, straight-bar attachment"
    condition:
      implement: cable_bar
      phase: full_rep
      notes: "Normalized to triangle push-up = 100%, NOT true %MVIC. Values are relative comparisons only."
    measurements:
      - {muscle: triceps_long,    mean_pct_mvc: 75.0, sd: 29.3}
      - {muscle: triceps_lateral, mean_pct_mvc: 59.0, sd: 14.3}

joint_rom_required:
  elbow_flexion_deg: 90
  shoulder_flexion_deg: 0
  source: "boehler_2011"

strength_curve:
  type: descending
  sticking_point: top_third
  peak_force_position: top
  notes: "Hardest at the start (elbows most flexed); decreases as elbows extend — shortened-position biased relative to overhead extensions"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    wrist: low
  common_injuries:
    - structure: lateral_epicondyle
      mechanism: repetitive_valgus_stress
      risk_factors: [grip_too_wide, wrist_deviation_at_bottom, heavy_load]
    - structure: triceps_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, excessive_weight]
  contraindications:
    - acute_lateral_epicondylitis

variations: []
progressions: []
alternatives: [cable_one_arm_tricep_extension, ez_bar_skullcrusher]

sources:
  - source_id: boehler_2011
    title: "An electromyographic analysis of 3 muscles surrounding the elbow joint during a maximally forceful isometric contraction, concentric isotonic contraction, and 6 common exercises"
    author: "Boehler, Breanna et al."
    year: 2011
    doi: null
    credibility: rct
---

# Triceps Pushdown

The triceps pushdown is the most accessible cable isolation exercise for all three triceps heads. With the upper arm held stationary at the side and the forearm pushing downward against the cable, the exercise provides a controlled elbow extension stimulus without the shoulder mobility or stability demands of overhead variations. The rope attachment produces higher activation than the straight-bar for both the long and lateral heads.

## Execution

1. Attach a rope (or straight bar) to a high cable pulley; grip with elbows close to the sides
2. Keep the upper arms stationary throughout — do not allow them to drive forward or backward
3. Push the attachment downward by extending the elbows until the arms are fully extended
4. At the bottom of the rope version, spread the hands slightly to maximize triceps contraction
5. Return under control, allowing the forearms to rise to approximately 90° at the start

## What the EMG Data Shows

Boehler 2011 data is normalized to triangle push-up (not true %MVIC). The values are relative comparisons within that study:

| Attachment | Triceps Long | Triceps Lateral |
|------------|-------------|-----------------|
| Rope | 81 ± 32.3 | 67 ± 15.7 |
| Straight bar | 75 ± 29.3 | 59 ± 14.3 |

The rope consistently produces ~6–8 points higher activation for both heads. The spreading action at the bottom of the rope rep adds a final contraction impulse not available with the fixed bar grip.

## Rope vs Bar: Why the Difference

The rope allows the wrists and forearms to rotate slightly during the push, which aligns with the triceps' optimal pull direction. The bar locks the wrists into a fixed position that may not suit all anatomical configurations. For most trainees, the rope is the recommended default.

## Shoulder Position and Long Head

The shoulder is neutral (0° flexion/extension) during pushdowns. This puts the triceps long head in a mid-range position — shortened relative to overhead extensions. Trainees seeking maximum long head stimulus should pair pushdowns with an overhead extension variation.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/weighted_pull_ups.md -->

---
id: weighted_pull_ups
name: Weighted Pull-Up
status: complete
category: exercise
pattern: [vertical_pull]
equipment: [bodyweight, dip_belt]

difficulty:
  technical_complexity: 3
  strength_prerequisite: 3
  mobility_prerequisite: 1

muscles:
  - id: latissimus_dorsi
    role: primary
  - id: infraspinatus
    role: primary
  - id: teres_major
    role: secondary
  - id: biceps_brachii
    role: secondary
  - id: trap_lower
    role: secondary
  - id: pectoralis_major
    role: secondary
  - id: deltoid_posterior
    role: secondary
  - id: rhomboids
    role: secondary
  - id: erector_spinae
    role: stabilizer
  - id: external_oblique
    role: stabilizer

# EMG data from ssd_2026 (unweighted pronated pull-up). No weighted pull-up
# specific EMG %MVIC study found. Adding external load increases absolute force
# demand proportionally while preserving the relative muscle activation distribution —
# %MVIC values would remain similar or increase across all muscles.
muscle_activation_studies:
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation — multiple study populations"
    condition:
      grip: pronated
      width: shoulder-width
      load: bodyweight_unweighted
      notes: "Unweighted baseline; weighted execution preserves this distribution at higher absolute force output"
    measurements:
      - {muscle: latissimus_dorsi, mean_pct_mvc: 123.5, sd: null, notes: "Range 117–130% MVIC across studies"}
      - {muscle: biceps_brachii,   mean_pct_mvc: 78.0,  sd: 32.0}
      - {muscle: infraspinatus,    mean_pct_mvc: 79.0,  sd: 56.0}
      - {muscle: trap_lower,       mean_pct_mvc: 56.0,  sd: 21.0}
      - {muscle: pectoralis_major, mean_pct_mvc: 44.0,  sd: 27.0}
      - {muscle: erector_spinae,   mean_pct_mvc: 40.0,  sd: null, notes: "Isometric stabilization; increases with added load"}
      - {muscle: external_oblique, mean_pct_mvc: 33.0,  sd: null, notes: "Isometric stabilization; increases with added load"}

joint_rom_required:
  shoulder_flexion_deg: 180
  elbow_flexion_deg: 93.4
  scapular_upward_rotation_deg: 60
  glenohumeral_contribution_deg: 120
  notes: >
    Identical ROM requirements to the unweighted pull-up. Added load does not
    change the joint angles required; it only increases the force needed to move
    through them. Full overhead shoulder flexion (180°) required for the dead-hang start.
  source: "ssd_2026"

strength_curve:
  type: descending
  sticking_point: top_third
  peak_force_position: bottom_third
  notes: >
    Same descending strength curve as the unweighted pull-up — peak force production
    in the bottom third where the latissimus dorsi has its greatest length-tension
    advantage, with a sticking point in the top third where active insufficiency
    of the primary shoulder extensors requires secondary muscle compensation.
    Added load shifts the entire force requirement upward, making the top third
    sticking point the limiting factor for load progression.
  source: "ssd_2026"

injury_risk:
  joint_stress:
    shoulder: high
    elbow: moderate
    lumbar: low
  common_injuries:
    - structure: biceps_brachii_tendon
      mechanism: eccentric_overload_at_full_extension
      risk_factors: [excessive_load_jump, fast_eccentric_descent, inadequate_warm_up]
    - structure: glenohumeral_joint
      mechanism: impingement
      risk_factors: [added_load_with_inadequate_scapular_control, kipping_with_weight, forward_head_posture]
    - structure: medial_elbow_common_flexor_tendon
      mechanism: repetitive_valgus_stress_amplified_by_load
      risk_factors: [wide_grip_with_heavy_weight, high_frequency, insufficient_recovery]
    - structure: lumbar_spine
      mechanism: compressive_load_from_dip_belt
      risk_factors: [heavy_loads_at_belt_attachment_point, pre_existing_disc_pathology]
  contraindications:
    - acute_biceps_tendon_rupture
    - shoulder_labral_tear_acute
    - medial_epicondylitis_acute

variations: [pullups, chin_up]
progressions: []
alternatives: [wide_grip_lat_pulldown, band_assisted_pull_up]

sources:
  - source_id: ssd_2026
    title: "Sports Science Data Extraction: Vertical Pulling and Horizontal Rowing"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Weighted Pull-Up

The weighted pull-up is the primary strength progression from the bodyweight pull-up. External load is added via a dip belt (hanging plates or kettlebells), a weight vest, or a dumbbell held between the feet or ankles. The movement mechanics are identical to the unweighted pull-up; the added resistance increases the total force demand beyond what bodyweight alone can provide, driving continued strength adaptation once bodyweight reps plateau.

## Prerequisites

The weighted pull-up should not be attempted until the lifter can perform 8–10 consecutive clean bodyweight pull-ups — full dead hang at the bottom, chin over bar at the top, controlled eccentric. Attempting to add load before this threshold is established shifts the limiting factor from strength to technique and increases injury risk at the shoulder and elbow.

## Execution

1. Attach plates or a kettlebell to a dip belt; secure the belt around the hips with the weight hanging freely below
2. Hang from the bar with a pronated grip at approximately shoulder width; arms fully extended
3. Depress and slightly retract the scapulae before initiating the pull — do not begin from a passive shrug
4. Initiate by driving the elbows down and back ("elbows to hips"), not by curling the wrists toward the bar
5. Pull until the chin clears the bar or the upper chest contacts it
6. Lower under control for 2–3 seconds; do not drop from the top

## Load Selection and Progression

| Rep target at bodyweight | Starting added load | Notes |
|-------------------------|--------------------|----|
| 8–10 | 5–10 kg | Confirm technique is preserved before adding load |
| 10–12 | 10–15 kg | Speed of load increase should slow as absolute load rises |
| 15+ | 20+ kg | At this threshold, treat weighted pull-ups as a primary strength lift |

Small load increments (2.5–5 kg) are preferred over large jumps. The sticking point in the top third is exaggerated by added load — if technique breaks at the top before bodyweight pull-ups do, the load is too heavy.

## Dip Belt vs Weight Vest

| Method | Advantage | Disadvantage |
|--------|-----------|-------------|
| Dip belt with plates | Precise load adjustment; no body heat | Belt can shift; requires setup time |
| Weight vest | Evenly distributed; no setup | Load increments fixed by vest design; expensive |
| Dumbbell between feet/ankles | No equipment required | Limits range of motion; unstable |

The dip belt is the standard method for dedicated strength work and allows the most precise load progression.

## Relationship to Bodyweight Pull-Up

The weighted pull-up does not change the exercise — it changes the load. The ssd_2026 EMG data from unweighted pronated pull-ups represents the relative muscle activation distribution, which is preserved under load. What changes is absolute force output: at bodyweight + 20 kg, the latissimus dorsi is producing proportionally more absolute force than at bodyweight, even though the %MVIC distribution remains similar.

This is why weighted pull-ups are the logical final progression for vertical pulling — they overload the same movement pattern at higher absolute intensities without introducing technique variables.

> For system-specific training applications, see each system's lens entry.


---

<!-- FILE: exercises/yoke_walk.md -->

---
id: yoke_walk
name: Yoke Walk
status: complete
category: exercise
pattern: [carry]
equipment: [yoke]

difficulty:
  technical_complexity: 3
  strength_prerequisite: 5
  mobility_prerequisite: 1

muscles:
  - id: erector_spinae
    role: primary
  - id: rectus_femoris
    role: primary
  - id: vastus_lateralis
    role: primary
  - id: vastus_medialis
    role: primary
  - id: gluteus_maximus
    role: primary
  - id: trap_upper
    role: primary
  - id: rectus_abdominis
    role: secondary
  - id: obliques
    role: secondary
  - id: multifidus
    role: secondary
  - id: gluteus_medius
    role: secondary
  - id: adductor_magnus
    role: secondary
  - id: adductor_longus
    role: secondary
  - id: biceps_femoris
    role: secondary
  - id: semitendinosus
    role: secondary
  - id: gastrocnemius_medial
    role: secondary
  - id: gastrocnemius_lateral
    role: secondary
  - id: soleus
    role: secondary

muscle_activation_studies: []

joint_rom_required:
  hip_flexion_deg: 24
  knee_flexion_deg: 20
  source: "biomechanical data — hip 23.8 +/- 7.1 deg flexion at heel strike; knees highly extended throughout stance"

strength_curve:
  type: isometric_hold
  sticking_point: pick_and_first_step
  notes: "The pick (unracking) demands peak force production. During the walk, legs and trunk work near-isometrically under extreme compressive load."

injury_risk:
  joint_stress:
    lumbar_spine: high
    thoracic_spine: high
    knee: moderate
  common_injuries:
    - structure: lumbar_disc
      mechanism: axial_compression_under_supramaximal_load
      risk_factors: [excessive_load, lateral_sway, uneven_surface]
    - structure: knee_meniscus
      mechanism: compressive_load_during_short_stride_gait
      risk_factors: [excessive_load, pre_existing_knee_pathology, uneven_terrain]
  contraindications:
    - acute_lumbar_disc_herniation
    - spinal_compression_fracture_history
    - active_knee_meniscus_tear

variations: []
progressions: []
alternatives: [farmers_walk]

sources: []
---

# Yoke Walk

A maximal-load carry event where the athlete walks with a yoke apparatus racked across the upper back and shoulders. The yoke walk presents one of the most extreme axial compressive challenges in strength sport, with competition loads often reaching 300-400+ kg. Biomechanically, it produces a distinctive gait pattern: compressed stride length (approximately 1.14 m vs 1.54 m in the farmer's walk), elevated stride rate (1.62 Hz), and increased stance duration (0.42 s). The knees remain highly extended throughout the stance phase to prevent center-of-mass drop under the extreme load.

## Execution

1. **Setup.** Position yourself under the yoke crossbar so it sits across the upper trapezius and rear deltoids — the same shelf as a high-bar back squat. Grip the uprights lightly to stabilize the frame. Set feet shoulder-width apart directly under the bar.
2. **Pick.** Brace hard — full trunk pressurization. Drive through the heels to stand the yoke up. Pause briefly to let the yoke settle and stop swinging before moving.
3. **Walk.** Take short, quick steps. Do not overstride — compressed steps keep the center of mass stable. Look forward, not down. Hold the uprights to dampen lateral oscillation.
4. **Turn (if applicable).** Decelerate with even shorter steps, pivot using small foot adjustments, and re-accelerate. Lateral stability is critical — the yoke's momentum wants to continue forward.
5. **Set down.** At the finish line, control the descent by squatting the yoke down rather than dumping it. Re-racking on the pins protects the equipment and the floor.

## Programming Note

The yoke walk is one of the most systemically taxing strongman events. Allow 7-10 days between heavy yoke sessions, especially at competition loads. For general training, 3-5 sets of 15-25 m at moderate load (60-75% of max) develop the motor pattern without excessive recovery cost. The limiting factor is usually trunk rigidity and the ability to resist lateral sway, not leg strength per se. Athletes should be comfortable with heavy back squats (at minimum 1.5x bodyweight) before training the yoke walk.


---

