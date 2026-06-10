---
id: dumbbell_bicep_curl
name: Dumbbell Bicep Curl
status: complete
category: exercise
pattern: [isolation]
equipment: [dumbbell]

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

# parpa_2025 (n=11): 80% 1RM — biceps_brachii 111.46% ± 26.80% MVIC.
# oliveira_2009: biceps_brachii ~95% MVIC.
# High parpa_2025 value (>100%) reflects normalization artifact at 80% 1RM load;
# absolute values above 100% are methodologically valid (near-max MVIC is not the ceiling for loaded activation).
muscle_activation_studies:
  - source_id: parpa_2025
    doi: null
    n: 11
    population: "resistance-trained adults, 80% 1RM"
    condition:
      load_pct_1rm: 80
      implement: dumbbell
      phase: full_rep
    measurements:
      - {muscle: biceps_brachii, mean_pct_mvc: 111.46, sd: 26.80}
  - source_id: oliveira_2009
    doi: null
    n: null
    population: "general population"
    condition:
      implement: dumbbell
      phase: full_rep
    measurements:
      - {muscle: biceps_brachii, mean_pct_mvc: 95.0, sd: null}

joint_rom_required:
  elbow_flexion_deg: 132
  shoulder_flexion_deg: 0
  source: "Marcolin 2018 analogous data"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped; peak torque at ~90° elbow flexion; allows full forearm supination through the range unlike barbell"
  source: "biomechanical inference"

injury_risk:
  joint_stress:
    elbow: low
    wrist: low
  common_injuries:
    - structure: distal_biceps_tendon
      mechanism: eccentric_overload
      risk_factors: [rapid_eccentric, excessive_weight, pre_existing_tendinopathy]
  contraindications:
    - acute_distal_biceps_tendinopathy

variations: []
progressions: []
alternatives: [barbell_curl, ez_bar_curl]

sources:
  - source_id: parpa_2025
    title: "Electromyographic comparison of various curl exercises"
    author: "Parpa, Koulla et al."
    year: 2025
    doi: null
    credibility: rct
  - source_id: oliveira_2009
    title: "EMG analysis of biceps brachii in curl variations"
    author: "Oliveira, Leal et al."
    year: 2009
    doi: null
    credibility: rct
---

# Dumbbell Bicep Curl

The dumbbell bicep curl is the unilateral supinating version of the standard curl. Unlike the barbell which fixes wrist position, the dumbbell allows — and encourages — progressive forearm supination through the concentric phase, maximizing the biceps brachii's two mechanical actions simultaneously: elbow flexion and forearm supination. The unilateral format also allows left-right strength imbalances to be identified and addressed.

## Execution

1. Stand with dumbbells at the sides, neutral grip (thumbs forward)
2. As the curl begins, rotate the wrist into full supination (thumb pointing away) as the elbow flexes
3. Continue until the forearm is fully supinated and the dumbbell is at shoulder height
4. Lower under control while pronating back through the eccentric

## What the EMG Data Shows

Parpa 2025 (n=11, 80% 1RM): **111.46% ± 26.80% MVIC**. This value above 100% is methodologically expected at high loads — the MVIC reference is an isometric test that does not cap the maximum achievable EMG amplitude during dynamic loading. Oliveira 2009 reported ~95% MVIC with lighter loads. Both studies confirm very high biceps activation.

The supination component that dumbbells enable is mechanically significant: the biceps brachii has a substantial supination moment at the elbow, meaning that fully supinating through the curl produces greater biceps activation than a neutral or pronated grip.

## Alternating vs Simultaneous

Alternating curls allow each arm to briefly rest and may allow slightly greater peak force per rep. Simultaneous curls maintain bilateral attention and require less time. Both formats produce comparable hypertrophy outcomes; the choice is ergonomic.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Hammer curl | Neutral grip throughout; shifts to brachialis | Brachialis priority |
| Incline dumbbell curl | Shoulder behind body; greater biceps long head stretch | Lengthened-position loading |
| Concentration curl | Arm braced on leg; highest isolation | Peak contraction |

> For system-specific training applications, see each system's lens entry.
