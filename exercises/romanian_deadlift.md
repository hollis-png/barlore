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
