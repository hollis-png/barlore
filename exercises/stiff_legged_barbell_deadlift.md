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
