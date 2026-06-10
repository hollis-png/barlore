---
id: barbell_curl
name: Barbell Curl
status: complete
category: exercise
pattern: [isolation]
equipment: [barbell]

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

# porcari_2014 (n=16): biceps_brachii 76.5% MVIC — highest among all curls tested except concentration.
# marcolin_2018 (n=12): qualitative only; no absolute %MVIC reported.
# ROM: 144.6° total elbow flexion. Shoulder position: neutral (0° flexion/extension).
muscle_activation_studies:
  - source_id: porcari_2014
    doi: null
    n: 16
    population: "healthy adults, standardized load"
    condition:
      implement: barbell
      phase: full_rep
    measurements:
      - {muscle: biceps_brachii, mean_pct_mvc: 76.5, sd: null}

joint_rom_required:
  elbow_flexion_deg: 145
  shoulder_flexion_deg: 0
  source: "Marcolin 2018"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Peak muscle force at ~90° elbow flexion where moment arm is maximal; bell-shaped across the full curl arc"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    wrist: low
  common_injuries:
    - structure: distal_biceps_tendon
      mechanism: eccentric_overload
      risk_factors: [excessive_weight, rapid_eccentric, pre_existing_tendinopathy]
    - structure: wrist_extensors
      mechanism: forced_pronation_at_top
      risk_factors: [wrist_flexion_at_top_of_curl, heavy_load]
  contraindications:
    - acute_distal_biceps_tendinopathy

variations: []
progressions: []
alternatives: [ez_bar_curl, dumbbell_bicep_curl]

sources:
  - source_id: porcari_2014
    title: "ACE-Sponsored Research: Best Biceps Exercises"
    author: "Porcari, John P. et al. (ACE)"
    year: 2014
    doi: null
    credibility: rct
  - source_id: marcolin_2018
    title: "Differences in electromyographic activity of biceps brachii and brachioradialis while performing three variants of curl"
    author: "Marcolin, Giuseppe et al."
    year: 2018
    doi: null
    credibility: rct
---

# Barbell Curl

The barbell curl is the foundational barbell elbow flexion exercise for biceps development. Both arms work in a fixed bilateral pattern that allows the greatest absolute load of any curl variation. The pronated-to-neutral wrist position and bilaterally locked grip limits supination but enables systematic progression through standardized load increments.

## Execution

1. Stand with a pronated-to-supinated grip at approximately shoulder width; elbows close to the torso
2. Keep the upper arms vertical and stationary throughout; do not allow the elbows to drift forward
3. Curl the bar in an arc from full extension to the shoulder, rotating the wrists to full supination at the top
4. Lower under control through the full eccentric without letting the bar drop

## What the EMG Data Shows

Porcari 2014 (ACE-commissioned, n=16):

| Exercise | Biceps Brachii |
|----------|----------------|
| Barbell curl | 76.5% MVIC |
| EZ-bar curl | 75.4% MVIC |
| Concentration curl | 97.9% MVIC |
| Incline dumbbell curl | 77.5% MVIC |

The barbell and EZ-bar produce nearly identical activation, differing by only 1.1%. The fixed supinated grip of the straight barbell maintains slightly higher activation than the EZ-bar's semi-pronated position.

## ROM and Shoulder Position

Marcolin 2018 measured 144.6° elbow flexion ROM for the barbell curl. The shoulder stays neutral (0° flexion). Because the shoulder is not flexed or extended, the biceps long head operates in a mid-range length position — mechanically favorable but not as long as the incline dumbbell curl's shoulder-extended position.

## Bilateral vs Unilateral

The bilateral barbell pattern allows higher absolute loads but prevents independent correction of left-right imbalances. Trainees with notable bilateral asymmetries should include unilateral dumbbell or cable curl variations in their programming.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| EZ-bar curl | Semi-pronated grip; reduces wrist stress | Wrist comfort |
| Dumbbell curl | Allows supination through ROM | Unilateral correction |
| Preacher curl | Supported upper arm; ascending strength curve | Lengthened-position emphasis |

> For system-specific training applications, see each system's lens entry.
