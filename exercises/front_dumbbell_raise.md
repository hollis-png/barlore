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
