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
