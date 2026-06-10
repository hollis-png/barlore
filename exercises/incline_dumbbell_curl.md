---
id: incline_dumbbell_curl
name: Incline Dumbbell Curl
status: complete
category: exercise
pattern: [isolation]
equipment: [dumbbell]

difficulty:
  technical_complexity: 1
  strength_prerequisite: 1
  mobility_prerequisite: 2

muscles:
  - id: biceps_brachii
    role: primary
  - id: brachialis
    role: secondary
  - id: brachioradialis
    role: secondary

# porcari_2014 (n=16): biceps_brachii 77.5% MVIC — virtually identical to barbell curl (76.5%).
# oliveira_2009: biceps_brachii ~95% MVIC.
# ROM: 134.3° elbow flexion — shorter than barbell curl due to supine position limiting extension.
# Shoulder: -50° (hyperextension) — biceps long head is at its longest mechanical length.
muscle_activation_studies:
  - source_id: porcari_2014
    doi: null
    n: 16
    population: "healthy adults, standardized load"
    condition:
      implement: dumbbell
      phase: full_rep
      notes: "Seated on incline bench ~60°; shoulder in hyperextension"
    measurements:
      - {muscle: biceps_brachii, mean_pct_mvc: 77.5, sd: null}
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
  elbow_flexion_deg: 134
  shoulder_extension_deg: 50
  source: "Marcolin 2018"

strength_curve:
  type: bell_shaped
  sticking_point: mid_range
  peak_force_position: mid
  notes: "Bell-shaped overall, but the bottom of the range is uniquely loaded due to shoulder hyperextension stretching the biceps long head at its maximum length — greater lengthened-position stimulus than upright curls"
  source: "Marcolin 2018"

injury_risk:
  joint_stress:
    elbow: low
    shoulder: low
  common_injuries:
    - structure: biceps_tendon_long_head
      mechanism: stretch_overload_at_shoulder
      risk_factors: [allowing_full_extension_at_max_stretch, heavy_load, pre_existing_biceps_tendinopathy]
    - structure: anterior_shoulder_capsule
      mechanism: passive_stretch
      risk_factors: [bench_angle_too_low, pre_existing_shoulder_instability]
  contraindications:
    - acute_biceps_long_head_tendinopathy
    - anterior_shoulder_instability

variations: []
progressions: []
alternatives: [dumbbell_bicep_curl, barbell_curl]

sources:
  - source_id: porcari_2014
    title: "ACE-Sponsored Research: Best Biceps Exercises"
    author: "Porcari, John P. et al. (ACE)"
    year: 2014
    doi: null
    credibility: rct
  - source_id: oliveira_2009
    title: "EMG analysis of biceps brachii in curl variations"
    author: "Oliveira, Leal et al."
    year: 2009
    doi: null
    credibility: rct
  - source_id: marcolin_2018
    title: "Differences in electromyographic activity of biceps brachii and brachioradialis while performing three variants of curl"
    author: "Marcolin, Giuseppe et al."
    year: 2018
    doi: null
    credibility: rct
---

# Incline Dumbbell Curl

The incline dumbbell curl places the lifter on a bench angled at approximately 45–60° with the arms hanging behind the body. This positions the shoulder in hyperextension (approximately -50°), placing the biceps long head — which crosses the shoulder joint — at its maximum mechanical length. No other common curl variation achieves this degree of long head stretch, making the incline curl uniquely valuable for loading the biceps in its most lengthened position.

## Execution

1. Set an incline bench to approximately 45–60°; steeper angles reduce the shoulder hyperextension benefit
2. Sit back against the bench with the arms hanging freely at the sides; dumbbells should be behind the body's plane, not at the hips
3. Starting from the fully hanging position (maximum stretch), curl upward with simultaneous supination
4. Do not allow the shoulders to roll forward or the upper arms to drift forward from the bench
5. Lower under full control — the eccentric through the stretched position is the most mechanically unique aspect of this exercise

## What the EMG Data Shows

| Study | Biceps Activation | Notes |
|-------|-------------------|-------|
| Porcari 2014 | 77.5% MVIC | Near-identical to barbell curl (76.5%) |
| Oliveira 2009 | 95.0% MVIC | Higher load condition |

The Porcari values suggest that incline curls produce similar peak EMG to standing curls. The mechanistic advantage of the incline curl is not peak activation but the unique loading of the biceps at its maximum elongated length — a stimulus type that growing evidence links to superior long-head hypertrophy.

## Why the Stretch Position Matters

The biceps long head originates at the supraglenoid tubercle of the scapula (above the shoulder). When the shoulder is extended (arm behind the body), the long head is stretched beyond the position it occupies in upright curls. This combination of active muscle contraction at long length is associated with elevated hypertrophic signaling in the long head specifically. The incline curl is therefore most valuable as a complement to exercises that load the mid- and shortened positions (concentration curl, preacher curl).

## Setup Cautions

- Bench angle: 45–60° is optimal. Angles below 45° over-stretch the anterior shoulder capsule. Angles above 60° reduce the hyperextension benefit.
- Load: Use lighter loads than standing curls. The stretched starting position limits available force and injury risk is elevated with excessive weight.

> For system-specific training applications, see each system's lens entry.
