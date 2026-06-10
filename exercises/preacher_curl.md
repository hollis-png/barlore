---
id: preacher_curl
name: Preacher Curl
status: complete
category: exercise
pattern: [isolation]
equipment: [barbell, ez_bar]

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

# porcari_2014 (n=16): biceps_brachii 88.8% MVIC.
# oliveira_2009: biceps_brachii ~80% MVIC.
# ROM: 115.5° elbow flexion — reduced vs barbell curl (144.6°) due to pad limiting extension.
# Shoulder flexion ~50° — places the biceps long head at shorter length than neutral curls.
# Strength curve: ASCENDING — hardest at the bottom (extended position) where the biceps is longest.
muscle_activation_studies:
  - source_id: porcari_2014
    doi: null
    n: 16
    population: "healthy adults, standardized load"
    condition:
      implement: ez_bar
      phase: full_rep
      notes: "Upper arms resting on preacher pad; shoulder ~50° flexion"
    measurements:
      - {muscle: biceps_brachii, mean_pct_mvc: 88.8, sd: null}
  - source_id: oliveira_2009
    doi: null
    n: null
    population: "general population"
    condition:
      implement: barbell
      phase: full_rep
    measurements:
      - {muscle: biceps_brachii, mean_pct_mvc: 80.0, sd: null}

joint_rom_required:
  elbow_flexion_deg: 116
  shoulder_flexion_deg: 50
  source: "Marcolin 2018"

strength_curve:
  type: ascending
  sticking_point: bottom_third
  peak_force_position: bottom
  notes: "Hardest at the bottom of the range where the elbow is most extended and gravity moment arm is near maximum — opposite of the free-standing curl's bell curve"
  source: "Marcolin 2018"

injury_risk:
  joint_stress:
    elbow: moderate
    wrist: low
  common_injuries:
    - structure: distal_biceps_tendon
      mechanism: eccentric_overload_at_full_extension
      risk_factors: [dropping_weight_at_bottom, locking_out_fully, heavy_load, pre_existing_tendinopathy]
    - structure: biceps_tendon_long_head
      mechanism: stretch_overload
      risk_factors: [hyperextending_at_bottom, pre_existing_tendinopathy]
  contraindications:
    - acute_distal_biceps_tendinopathy
    - elbow_hyperextension_injury

variations: []
progressions: []
alternatives: [cable_preacher_curl, barbell_curl]

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

# Preacher Curl

The preacher curl places the upper arms against an angled pad with the shoulders flexed approximately 50°. This configuration reduces the available elbow flexion ROM to ~115° (vs 145° for standing curls) and shifts the resistance curve to ascending — the hardest point is at the bottom where the elbow is most extended. The preacher curl emphasizes the lengthened biceps position more than free-standing curls, making it a complementary stimulus rather than a substitute.

## Execution

1. Adjust the preacher bench so the top of the pad is at armpit height when seated
2. Rest the upper arms flat against the pad, shoulder slightly in front of the pad's top edge
3. Hold the EZ-bar or barbell at full arm extension (do not lock out completely)
4. Curl to the top — do not allow the upper arms to lift off the pad
5. Lower slowly and under control; do not bounce at the bottom — this is where distal biceps tendon injury risk is highest

## What the EMG Data Shows

| Study | Biceps Activation |
|-------|-------------------|
| Porcari 2014 | 88.8% MVIC |
| Oliveira 2009 | 80.0% MVIC |

The preacher curl activates less than concentration curls (97.9%) but more than the barbell curl (76.5%) — a counterintuitive result explained by the ascending strength curve: the harder bottom position demands more muscle force at maximum stretch.

## The Ascending Strength Curve

The preacher curl is one of few curl exercises where the ascending curve is pronounced. This is mechanically different from the bell-shaped barbell curl:

- **Barbell curl**: easiest at bottom and top; hardest at 90° elbow flexion
- **Preacher curl**: hardest at the bottom; progressively easier through the concentric

The practical implication: preacher curls are uniquely suited for training the biceps under load in the most stretched position, consistent with evidence that lengthened-position loading enhances hypertrophy stimulus.

## Injury Warning

The bottom position (full elbow extension against load) concentrates tensile stress on the distal biceps tendon. Do not allow the weight to drop through the eccentric or hyperextend the elbow. Trainees with pre-existing distal biceps tendinopathy should use cable preacher curls, which maintain constant tension without the hard stop at the bottom.

> For system-specific training applications, see each system's lens entry.
