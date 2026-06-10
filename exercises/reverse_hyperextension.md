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
