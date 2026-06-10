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
