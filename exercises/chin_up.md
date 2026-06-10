---
id: chin_up
name: Chin-Up
status: complete
category: exercise
pattern: [vertical_pull]
equipment: [bodyweight]

difficulty:
  technical_complexity: 3
  strength_prerequisite: 3
  mobility_prerequisite: 1

muscles:
  - id: latissimus_dorsi
    role: primary
  - id: biceps_brachii
    role: primary
  - id: pectoralis_major
    role: secondary
  - id: trap_lower
    role: secondary
  - id: rhomboids
    role: secondary
  - id: infraspinatus
    role: stabilizer
  - id: erector_spinae
    role: stabilizer

# ssd_2026 literature compilation. All values %MVIC.
# Key finding: LD equivalent between chin-up and pull-up (117% both).
# BB significantly higher in chin-up (96 vs 78). PM higher (57 vs 44). trap_lower lower (45 vs 56).
muscle_activation_studies:
  - source_id: ssd_2026
    doi: null
    n: null
    population: "literature compilation"
    condition:
      grip: supinated
      width: shoulder-width
    measurements:
      - {muscle: latissimus_dorsi, mean_pct_mvc: 117, sd: 46}
      - {muscle: biceps_brachii,   mean_pct_mvc: 96,  sd: 34}
      - {muscle: pectoralis_major, mean_pct_mvc: 57,  sd: 36}
      - {muscle: trap_lower,        mean_pct_mvc: 45,  sd: 22}

joint_rom_required:
  shoulder_flexion_deg: 180
  elbow_flexion_deg: 100.6
  scapular_upward_rotation_deg: 60
  notes: >
    Chin-up requires greater elbow flexion ROM (100.6° ± 14.5°) than the pronated
    pull-up (93.4° ± 14.6°). The supinated grip positions the elbows anteriorly in
    the sagittal plane, enabling more terminal flexion at lockout. Scapular upward
    rotation of 60° is required throughout the ascending phase.
  source: "ssd_2026"

strength_curve:
  type: descending
  sticking_point: top_third
  peak_force_position: bottom_third
  notes: >
    Identical curve to the pronated pull-up: hardest at the top where the humerus
    is fully adducted and the primary extensors hit active insufficiency. Peak force
    in the bottom third where LD is at optimal length-tension. The supinated grip
    does not change the curve shape — it redistributes load between biceps and lower
    trapezius, not positional difficulty.
  source: "ssd_2026"

injury_risk:
  joint_stress:
    shoulder: moderate
    elbow: low
    wrist: low
  common_injuries:
    - structure: medial_elbow
      mechanism: valgus_stress_from_supinated_grip_under_load
      risk_factors: [heavy_weighted_chin_ups, medial_epicondylitis_history]
    - structure: shoulder_subacromial_space
      mechanism: impingement_at_top_of_movement
      risk_factors: [forced_scapular_retraction_at_full_overhead_flexion, inadequate_scapular_depression_cue]
  contraindications:
    - acute_medial_epicondylitis
    - distal_biceps_tendon_pathology
    - anterior_shoulder_instability

variations: []
progressions: []
alternatives: [pullups]

sources:
  - source_id: ssd_2026
    title: "Sports Science Data Extraction: Vertical Pulling and Horizontal Rowing"
    author: "Literature compilation"
    year: 2026
    doi: null
    credibility: literature_compilation
---

# Chin-Up

The chin-up is a closed-chain bodyweight vertical pulling exercise performed with a supinated (underhand) grip at approximately shoulder width. The supinated hand position places the elbows anteriorly in the sagittal plane throughout the movement, maximizing biceps brachii mechanical advantage and increasing pectoralis major involvement compared to the pronated pull-up. Latissimus dorsi activation is equivalent between grips — both reach 117% MVIC — refuting the common claim that chin-ups are inferior for lat development.

## Execution

1. Grip the bar with palms facing toward you, hands at shoulder width; hang at full arm extension
2. Depress the scapulae (pull shoulders down from ears) before initiating the pull
3. Drive the elbows down and back, pulling the chest toward the bar
4. Continue until the chin clears the bar; avoid craning the neck — the torso should rise, not the head
5. Lower under control to full arm extension; do not relax the shoulders at the bottom

## What the EMG Data Shows

**Chin-up vs pronated pull-up** (ssd_2026 direct comparison):

| Muscle | Chin-up | Pull-up | Difference |
|--------|---------|---------|------------|
| Latissimus dorsi | 117 ± 46% | 117–130% | Equivalent |
| Biceps brachii | 96 ± 34% | 78 ± 32% | +23% in chin-up |
| Pectoralis major | 57 ± 36% | 44 ± 27% | +30% in chin-up |
| Lower trapezius | 45 ± 22% | 56 ± 21% | −20% in chin-up |

The key finding: the LD is maximally recruited regardless of grip. The chin-up is not a "bicep exercise that also uses the back" — it is a full lat exercise with additional biceps loading.

**Why biceps are higher**: The supinated forearm puts the biceps brachii in optimal alignment for elbow flexion. In the pronated pull-up, the brachialis and brachioradialis compensate for the mechanically disadvantaged biceps.

**Why lower trapezius is lower**: The sagittal elbow path of the chin-up slightly reduces the horizontal scapular depression demand compared to the frontal-plane elbow path of the pull-up. Both exercises still require substantial lower trap activation for scapular stabilization throughout.

## ROM: Why Chin-Up Has Greater Elbow Flexion

The chin-up requires 100.6° ± 14.5° of elbow flexion vs 93.4° ± 14.6° for the pull-up. The supinated grip keeps the elbows close to the torso in the sagittal plane at lockout, allowing the forearm to travel further before being blocked by the shoulder. This 7° of additional elbow flexion contributes to the greater biceps peak contraction at lockout.

## Chin-Up vs Pull-Up: Selection Logic

- **Choose pull-up** when prioritizing lower trapezius development, scapular stability, or maximum lat activation at the highest absolute load
- **Choose chin-up** when prioritizing biceps brachii development, pectoralis major recruitment, or when easier mechanics allow more volume per session

Both are valid primary vertical pulling exercises. Programming both across a training block produces broader motor pattern coverage than specializing in one.

## Variations

| Variation | Key difference | Best for |
|-----------|----------------|----------|
| Pull-up (pronated) | Lower biceps; higher trap_lower | Scapular emphasis; wider grip pattern |
| Close-grip chin-up | Narrower than shoulder width | Maximum biceps elbow flexion ROM |
| Weighted chin-up | External load via belt | Strength progression past bodyweight |

> For system-specific training applications, see each system's lens entry.
