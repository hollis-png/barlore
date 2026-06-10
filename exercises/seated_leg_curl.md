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
