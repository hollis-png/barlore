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
