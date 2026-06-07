---
id: conventional_deadlift
name: Conventional Deadlift
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
