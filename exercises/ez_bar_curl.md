---
id: ez_bar_curl
name: EZ-Bar Curl
status: complete
category: exercise
pattern: [isolation]
equipment: [ez_bar]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 1

muscles:
  - id: biceps_brachii
    role: primary
  - id: brachialis
    role: secondary
  - id: brachioradialis
    role: secondary

# porcari_2014 (n=16): biceps_brachii 75.4% MVIC.
# ROM: 144.6° elbow flexion — identical to barbell curl.
# EZ-bar places the wrist in ~45° semi-pronation, reducing wrist/forearm stress vs straight bar.
# Activation difference vs barbell curl: only 1.1 percentage points (76.5% vs 75.4%).
muscle_activation_studies:
  - source_id: porcari_2014
    doi: null
    n: 16
    population: "healthy adults, standardized load"
    condition:
      implement: ez_bar
      phase: full_rep
    measurements:
      - {muscle: biceps_brachii, mean_pct_mvc: 75.4, sd: null}

joint_rom_required:
  elbow_flexion_deg: 145
  shoulder_flexion_deg: 0
  source: "Marcolin 2018"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped; identical to barbell curl; semi-pronated grip reduces wrist moment but does not significantly alter elbow flexion moment profile"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    wrist: low
  common_injuries:
    - structure: distal_biceps_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, excessive_weight]
  contraindications:
    - acute_wrist_tendinopathy

variations: []
progressions: []
alternatives: [barbell_curl, dumbbell_bicep_curl]

sources:
  - source_id: porcari_2014
    title: "ACE-Sponsored Research: Best Biceps Exercises"
    author: "Porcari, John P. et al. (ACE)"
    year: 2014
    doi: null
    credibility: rct
---

# EZ-Bar Curl

The EZ-bar curl is the most wrist-friendly barbell curl variation. The curved bar places the hands in a semi-pronated position (~45°), reducing the stress on the wrist and forearm that many lifters experience with a fully supinated straight bar grip. EMG data shows virtually identical biceps brachii activation to the straight barbell curl (75.4% vs 76.5% MVIC), making the EZ-bar a practical substitute for lifters with wrist discomfort during standard barbell curls.

## Execution

1. Grip the inner (closer to center) curves of the EZ-bar; this produces the semi-pronated position that reduces wrist torque
2. Stand with the upper arms close to the torso
3. Curl the bar upward, keeping the upper arms stationary
4. Lower under control; full extension at the bottom is acceptable if the load is appropriate

## The 1.1% Difference

Porcari 2014 found only a 1.1 percentage point difference between the barbell curl (76.5%) and EZ-bar curl (75.4%). This difference is practically meaningless. Lifters who experience discomfort with the straight bar can switch to the EZ-bar without measurable loss of biceps stimulus.

The semi-pronated position does reduce the supination component of the lift, which slightly shifts load from the biceps brachii supination function toward brachialis and brachioradialis. The net effect on hypertrophy is negligible for most practical purposes.

## Inner vs Outer Grip

EZ-bars have two sets of angled grips:
- **Inner (closer to center)**: Semi-pronated, reduced wrist torque — recommended
- **Outer (wider)**: More pronated, increases brachioradialis contribution, harder on the wrists

The inner grip most closely approximates the barbell curl's mechanical effect.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Barbell curl | Full supination; highest biceps activation | Max biceps stimulus |
| Dumbbell curl | Independent supination per arm | Unilateral control |
| EZ-bar preacher curl | Semi-pronated + supported upper arm | Wrist comfort + lengthened load |

> For system-specific training applications, see each system's lens entry.
