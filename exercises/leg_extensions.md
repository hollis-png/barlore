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
